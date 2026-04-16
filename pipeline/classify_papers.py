"""
Paper classification via node-based distance in the SPECTER2 embedding space.

Phase 3 re-implementation. Replaces the legacy Haiku-prompt approach with a
density-faithful (HDBSCAN-style) assignment:

  * Primary category = nearest neighbor's sub-cluster's parent category
    (single-linkage 1-NN).
  * all_categories  = top-3 sub-clusters that win the K-nearest-neighbor vote
    (default K=10, MIN_VOTES=3) sorted by mean distance ascending.
    The primary category is always included (even if it didn't reach the
    vote threshold) and pinned to position 0.

Why node-based: HDBSCAN is density-based and has no centroid concept; using
centroid cosine biases assignments toward isotropic blobs. Node-pair distances
respect cluster shape and density.

Pipeline contract:
  * Reads `{topic}/_embeddings_cache.json` (slug → 768D SPECTER2 vector).
  * Reads `{topic}/_new_classification.json` (slug → sub_category mapping for
    existing papers; provides the "anchor set" for kNN search).
  * For papers without a cached embedding, computes one on the fly via
    `topic_modeling.compute_embeddings` (incremental cache update).
  * Updates `docs/papers/_papers_index.json` and rewrites
    `{topic}/_new_classification.json`.

Usage:
  PYTHONUTF8=1 python pipeline/classify_papers.py --topic ai4s
  PYTHONUTF8=1 python pipeline/classify_papers.py --topic ai4s --slugs 088,1093
  PYTHONUTF8=1 python pipeline/classify_papers.py --topic ai4s --dry-run
  PYTHONUTF8=1 python pipeline/classify_papers.py --topic ai4s --k 15 --min-votes 4
"""

import argparse
import json
import os
import sys
from collections import Counter
from pathlib import Path

import numpy as np

from config_loader import PAPERS_DIR as _PAPERS_DIR, get_topic_dir
PAPERS_DIR = str(_PAPERS_DIR)

DEFAULT_K = 20
DEFAULT_MIN_VOTES = 2
TOP_N_CATEGORIES = 3


def log(msg):
    print(msg, flush=True)


def load_index():
    p = Path(PAPERS_DIR) / "_papers_index.json"
    return json.loads(p.read_text(encoding="utf-8")), p


def load_anchor_set(topic_dir):
    """Read existing classification → slug→sub map, sub→category map.

    The "anchor set" is the set of slugs whose cluster membership is fixed and
    used to vote on new papers. We exclude assignments whose sub_category is
    empty (failed previous runs).
    """
    cls_path = Path(topic_dir) / "_new_classification.json"
    if not cls_path.exists():
        log(f"ERROR: {cls_path} missing — run topic_modeling.py first to seed clusters.")
        sys.exit(2)
    cls = json.loads(cls_path.read_text(encoding="utf-8"))

    slug_to_sub = {}
    sub_to_cat = {}
    for a in cls.get("assignments", []):
        sub = a.get("sub_category")
        cat = a.get("primary_category")
        slug = a.get("slug")
        if not sub or not cat or not slug:
            continue
        slug_to_sub[slug] = sub
        sub_to_cat[sub] = cat
    return slug_to_sub, sub_to_cat


def cosine_distances_to_all(query_vec, anchor_mat):
    """Return cosine distance vector (n,) of query against each anchor row."""
    q = query_vec / (np.linalg.norm(query_vec) + 1e-12)
    A = anchor_mat / (np.linalg.norm(anchor_mat, axis=1, keepdims=True) + 1e-12)
    sims = A @ q
    return 1.0 - sims  # cosine distance


def hybrid_classify(query_vec, query_slug, anchor_slugs, anchor_mat,
                    slug_to_sub, sub_to_cat, k=DEFAULT_K, min_votes=DEFAULT_MIN_VOTES):
    """Hybrid node-based assignment.

    Returns (primary_category, all_categories, primary_sub, sub_per_cat_map).
    """
    # Distances to every anchor (exclude self if present)
    dists = cosine_distances_to_all(query_vec, anchor_mat)
    if query_slug in anchor_slugs:
        self_idx = anchor_slugs.index(query_slug)
        dists[self_idx] = np.inf  # exclude

    # Sort all anchors ascending by distance
    order = np.argsort(dists)

    # K-NN vote among nearest k anchors
    knn_idxs = order[:k]
    sub_votes = Counter()
    sub_dists = {}
    for i in knn_idxs:
        s = slug_to_sub[anchor_slugs[int(i)]]
        sub_votes[s] += 1
        sub_dists.setdefault(s, []).append(float(dists[int(i)]))

    # Primary: highest vote count, tie-break by smallest mean distance
    # (replaces 1-NN to reduce single-neighbor noise; per user directive 2026-04-16)
    def primary_key(item):
        s, votes = item
        return (-votes, float(np.mean(sub_dists[s])))
    primary_sub = sorted(sub_votes.items(), key=primary_key)[0][0]
    primary_cat = sub_to_cat[primary_sub]

    # Qualifying subs for all_categories: vote >= min_votes
    qualifying_subs = [s for s, n in sub_votes.items() if n >= min_votes]
    # Sort qualifying by mean distance ascending (tighter cluster first)
    qualifying_subs.sort(key=lambda s: float(np.mean(sub_dists[s])))

    # Build all_categories: primary always pinned at index 0, then top qualifying subs' parents
    sub_per_cat = {primary_cat: primary_sub}
    all_cats = [primary_cat]
    for s in qualifying_subs:
        cat = sub_to_cat[s]
        if cat not in all_cats:
            all_cats.append(cat)
            sub_per_cat[cat] = s
        if len(all_cats) >= TOP_N_CATEGORIES:
            break

    return primary_cat, all_cats, primary_sub, sub_per_cat


def main():
    ap = argparse.ArgumentParser(description="Node-based hybrid classifier (Phase 3)")
    ap.add_argument("--topic", required=True)
    ap.add_argument("--slugs", default="",
                    help="Comma-separated slug prefixes. If set, only these "
                         "papers are (re)classified; others keep existing entries.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print assignment summary without writing JSONs.")
    ap.add_argument("--k", type=int, default=DEFAULT_K,
                    help="K for kNN vote on all_categories (default 10).")
    ap.add_argument("--min-votes", type=int, default=DEFAULT_MIN_VOTES,
                    help="Minimum kNN votes for a sub to qualify for "
                         "all_categories (default 3).")
    args = ap.parse_args()

    topic = args.topic
    topic_dir = str(get_topic_dir(topic))

    # 1. Anchor set: existing slug→sub & sub→cat
    slug_to_sub, sub_to_cat = load_anchor_set(topic_dir)
    log(f"[anchor] {len(slug_to_sub)} anchored slugs, "
        f"{len(set(sub_to_cat.values()))} parent categories, "
        f"{len(sub_to_cat)} sub-clusters")

    # 2. Index → topic_papers
    all_papers, index_path = load_index()
    topic_papers = [p for p in all_papers if topic in p.get("topics", [])]
    log(f"[index] {len(topic_papers)} {topic} papers")

    # 3. Embeddings (incremental cache; computes new ones via SPECTER2 if needed)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from topic_modeling import extract_originalities, compute_embeddings
    originalities = extract_originalities(topic_papers)
    cache_path = os.path.join(topic_dir, "_embeddings_cache.json")
    embeddings, slugs = compute_embeddings(originalities, cache_path)
    slug_to_vec = dict(zip(slugs, embeddings))

    # 4. Build anchor matrix from anchored slugs that ALSO have embeddings
    anchor_slugs = [s for s in slug_to_sub if s in slug_to_vec]
    if not anchor_slugs:
        log("ERROR: no anchored slug has an embedding — cannot classify.")
        sys.exit(3)
    anchor_mat = np.array([slug_to_vec[s] for s in anchor_slugs])
    log(f"[anchor matrix] shape={anchor_mat.shape}")

    # 5. Slug filter (--slugs)
    slug_filter = None
    if args.slugs:
        prefixes = [s.strip() for s in args.slugs.split(",") if s.strip()]
        slug_filter = {p["slug"] for p in topic_papers
                       if any(p["slug"].startswith(pref) or p["slug"] == pref
                              for pref in prefixes)}
        log(f"[slug filter] restricting to {len(slug_filter)} papers")

    # 6. Classify
    reassigned = 0
    unchanged = 0
    skipped = 0
    assignments = []
    for p in topic_papers:
        slug = p["slug"]
        if slug_filter is not None and slug not in slug_filter:
            cls = p.get("classifications", {}).get(topic)
            if cls:
                assignments.append({
                    "slug": slug,
                    "primary_category": cls.get("primary_category", ""),
                    "all_categories": cls.get("all_categories", []),
                    "sub_category": cls.get("sub_category", ""),
                })
            continue
        vec = slug_to_vec.get(slug)
        if vec is None:
            log(f"  WARN: {slug} missing embedding — skipped")
            skipped += 1
            continue
        primary, all_cats, sub, sub_map = hybrid_classify(
            vec, slug, anchor_slugs, anchor_mat,
            slug_to_sub, sub_to_cat, k=args.k, min_votes=args.min_votes)

        prev = p.get("classifications", {}).get(topic, {})
        if prev.get("primary_category") == primary and prev.get("sub_category") == sub:
            unchanged += 1
        else:
            reassigned += 1

        if not args.dry_run:
            if "classifications" not in p:
                p["classifications"] = {}
            p["classifications"][topic] = {
                "primary_category": primary,
                "all_categories": all_cats,
                "sub_category": sub,
                "sub_categories": sub_map,
            }

        assignments.append({
            "slug": slug,
            "primary_category": primary,
            "all_categories": all_cats,
            "sub_category": sub,
        })

    log(f"[classify] reassigned={reassigned}, unchanged={unchanged}, skipped={skipped}")

    if args.dry_run:
        cats = Counter(a["primary_category"] for a in assignments)
        log("[dry-run] per-category counts:")
        for c, n in cats.most_common():
            log(f"  {c}: {n}")
        return

    # Write back
    from lib.atomic_io import atomic_write_json
    atomic_write_json(index_path, all_papers)
    log(f"[write] {index_path}")

    cats_list = sorted({a["primary_category"] for a in assignments})
    cls_data = {
        "categories": [{"name": c} for c in cats_list],
        "assignments": assignments,
    }
    cls_path = Path(topic_dir) / "_new_classification.json"
    atomic_write_json(cls_path, cls_data)
    log(f"[write] {cls_path}  ({len(cats_list)} categories)")


if __name__ == "__main__":
    main()
