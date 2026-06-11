"""
paper-curation 설치 스크립트.

한 번 실행으로 전체 설치를 완료한다:
  1. config.json 생성 (인터랙티브)
  2. 환경변수 확인 (ANTHROPIC_API_KEY, GOOGLE_API_KEY)
  3. Zotero 연결 테스트 (User ID 조회 + 컬렉션 검증)
  4. PaperBanana 확인 (없으면 자동 클론)
  5. SKILL.md 생성 (템플릿 플레이스홀더 치환)
  6. SKILL.md를 ~/.claude/skills/paper-curation/에 설치

Usage:
  python pipeline/setup.py              # 전체 설치
  python pipeline/setup.py --no-install # SKILL.md 스킬 설치 건너뛰기
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO / "config.json"
EXAMPLE_PATH = REPO / "config.example.json"
TEMPLATE_PATH = REPO / "SKILL.md.template"
SKILL_OUTPUT = REPO / "SKILL.md"
GITIGNORE_PATH = REPO / ".gitignore"
SKILL_INSTALL_DIR = Path.home() / ".claude" / "skills" / "paper-curation"


def step_config():
    """Step 1: config.json 생성 또는 로드."""
    if CONFIG_PATH.exists():
        print(f"[1/6] config.json 발견: {CONFIG_PATH}")
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    if not EXAMPLE_PATH.exists():
        print("ERROR: config.example.json이 없습니다.")
        sys.exit(1)

    print("=== Paper Curation 초기 설정 ===\n")
    print("[1/6] config.json 생성\n")

    # Zotero 설정
    api_key = input("  Zotero API Key (https://www.zotero.org/settings/keys): ").strip()
    email = input("  이메일 (Zotero/Unpaywall용): ").strip()

    # 컬렉션 alias 설정
    print("\n  앞으로 이 Collection의 Paper Curation을 운영하려면 부르기 편한 이름을 하나 정하는 게 좋습니다.")
    print("  짧은 영문 이름을 하나 지어주세요 (예: ai4s, bioml, climate).")
    alias = input("  Topic alias: ").strip()
    collection_name = input(f"  Zotero 컬렉션 이름 ('{alias}'에 매핑할 컬렉션): ").strip()

    pdf_dir = input("\n  Zotero PDF 저장 경로: ").strip()
    paperbanana_dir = input("  PaperBanana 경로 (없으면 Enter): ").strip()

    # GitHub 설정 (선택)
    print("\n  GitHub Pages 배포 설정 (선택, Enter로 건너뛰기):")
    github_repo = input("  GitHub repo (예: username/paper-curation): ").strip()

    cfg = {
        "zotero": {
            "api_key": api_key or "YOUR_ZOTERO_API_KEY_HERE",
            "email": email or "your.email@example.com",
            "collections": {
                alias or "my_topic": collection_name or "Your Zotero Collection Name"
            },
            "pdf_dir": pdf_dir or "/path/to/your/zotero/pdfs"
        },
        "unpaywall_email": email or "your.email@example.com",
    }
    if github_repo:
        cfg["github"] = {
            "repo": github_repo,
            "branch": "master",
            "pages_base_url": f"https://{github_repo.split('/')[0]}.github.io/{github_repo.split('/')[-1]}" if '/' in github_repo else ""
        }
    if paperbanana_dir:
        cfg["paperbanana_dir"] = paperbanana_dir

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
    print(f"\n  → config.json 생성 완료")

    return cfg


def step_env_check(cfg):
    """Step 2: LLM API 키 환경변수 확인.

    ANTHROPIC / GOOGLE 키는 경고만 출력하고 넘어간다.
    OPENAI_API_KEY는 Deep Research 검색 인덱스 빌드에 필수라 없으면
    직접 입력받아 config.json에 저장하고, 입력을 건너뛰면 설치를 중단한다.
    (config.json은 .gitignore 로 보호됨)"""
    print("\n[2/6] 환경변수 확인")

    for key in ["ANTHROPIC_API_KEY", "GOOGLE_API_KEY"]:
        val = os.environ.get(key, "")
        if val:
            print(f"  ✓ {key} 설정됨")
        else:
            print(f"  ✗ {key} 미설정 — 파이프라인 실행 시 필요합니다")

    # OPENAI_API_KEY: required for Deep Research search index
    env_key = os.environ.get("OPENAI_API_KEY", "")
    cfg_key = cfg.get("openai_api_key", "")
    openai_key = env_key or cfg_key
    if openai_key:
        source = "env" if env_key else "config.json"
        print(f"  ✓ OPENAI_API_KEY 설정됨 ({source})")
        os.environ["OPENAI_API_KEY"] = openai_key
        return

    print()
    print("  ✗ OPENAI_API_KEY 미설정")
    print("    Deep Research 검색 인덱스 빌드에 필수입니다.")
    print("    발급: https://platform.openai.com/api-keys")
    print("    지금 입력하시면 config.json에 저장되어 다음 실행에서도 자동 사용됩니다.")
    print("    입력을 건너뛰시면 설치가 여기서 중단됩니다. 발급 후 다시 setup.py를 실행하세요.")
    print()
    user_input = input("    OpenAI API Key (sk-..., Enter로 중단): ").strip()
    if not user_input:
        print("\n  OPENAI_API_KEY가 필요합니다. 설치를 중단합니다.")
        print("  키를 발급한 뒤 다시 `python pipeline/setup.py` 를 실행해주세요.")
        sys.exit(1)

    cfg["openai_api_key"] = user_input
    _save_config(cfg)
    os.environ["OPENAI_API_KEY"] = user_input
    print("  ✓ OPENAI_API_KEY → config.json 에 저장")


def step_zotero_test(cfg):
    """Step 3: Zotero API 연결 테스트."""
    import urllib.request

    print("\n[3/6] Zotero 연결 테스트")

    api_key = cfg.get("zotero", {}).get("api_key", "")
    if not api_key or api_key == "YOUR_ZOTERO_API_KEY_HERE":
        print("  ✗ Zotero API key가 설정되지 않았습니다")
        return False

    # User ID 조회
    try:
        url = "https://api.zotero.org/keys/current"
        req = urllib.request.Request(url, headers={
            "Zotero-API-Key": api_key, "User-Agent": "Mozilla/5.0",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.load(resp)
        user_id = str(data.get("userID", ""))
        print(f"  ✓ User ID: {user_id}")
    except Exception as e:
        print(f"  ✗ User ID 조회 실패: {e}")
        return False

    # 컬렉션 검증
    collections = cfg.get("zotero", {}).get("collections", {})
    if not collections:
        print("  ✗ 컬렉션이 설정되지 않았습니다")
        return False

    try:
        url = f"https://api.zotero.org/users/{user_id}/collections?format=json&limit=100"
        req = urllib.request.Request(url, headers={
            "Zotero-API-Key": api_key, "User-Agent": "Mozilla/5.0",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            cols = json.load(resp)
        name_to_key = {c["data"]["name"]: c["data"]["key"] for c in cols}
    except Exception as e:
        print(f"  ✗ 컬렉션 목록 조회 실패: {e}")
        return False

    all_ok = True
    failed = {}
    available = sorted(name_to_key.keys())
    for alias, name in collections.items():
        if name in name_to_key:
            print(f"  ✓ '{alias}' → '{name}' (key: {name_to_key[name]})")
        else:
            print(f"  ✗ '{alias}' → '{name}' — Zotero에서 찾을 수 없습니다")
            print(f"    사용 가능한 컬렉션: {', '.join(available)}")
            failed[alias] = name
            all_ok = False

    if failed:
        # Claude Code가 파싱할 수 있도록 JSON으로도 출력
        print(f"  [COLLECTION_ERROR] {json.dumps({'failed': failed, 'available': available}, ensure_ascii=False)}")

    return all_ok


PAPERBANANA_REPO = "https://github.com/dwzhu-pku/PaperBanana.git"
PAPERBANANA_DEFAULT_DIR = REPO / "paperbanana"


def step_paperbanana(cfg):
    """Step 4: PaperBanana 확인 및 자동 클론."""
    print("\n[4/6] PaperBanana 확인")

    pb_dir = cfg.get("paperbanana_dir", "")

    # 경로가 설정되어 있고 실제 존재하면 OK
    if pb_dir and Path(pb_dir).exists():
        print(f"  ✓ PaperBanana: {pb_dir}")
        return cfg

    # 경로가 설정되어 있지만 존재하지 않는 경우
    if pb_dir and not Path(pb_dir).exists():
        print(f"  ✗ PaperBanana 경로가 존재하지 않습니다: {pb_dir}")
        print(f"  → 기본 위치에 자동 클론합니다")

    # 기본 위치에 이미 클론되어 있는지 확인
    if PAPERBANANA_DEFAULT_DIR.exists() and (PAPERBANANA_DEFAULT_DIR / "README.md").exists():
        print(f"  ✓ PaperBanana 발견 (기존 클론): {PAPERBANANA_DEFAULT_DIR}")
        cfg["paperbanana_dir"] = str(PAPERBANANA_DEFAULT_DIR)
        _save_config(cfg)
        return cfg

    # 자동 클론
    print(f"  → PaperBanana를 클론합니다: {PAPERBANANA_REPO}")
    print(f"     위치: {PAPERBANANA_DEFAULT_DIR}")
    try:
        result = subprocess.run(
            ["git", "clone", PAPERBANANA_REPO, str(PAPERBANANA_DEFAULT_DIR)],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode == 0:
            print(f"  ✓ PaperBanana 클론 완료")
            cfg["paperbanana_dir"] = str(PAPERBANANA_DEFAULT_DIR)
            _save_config(cfg)
        else:
            print(f"  ✗ 클론 실패: {result.stderr.strip()}")
            print(f"  → 타임라인 생성 없이 파이프라인을 사용할 수 있습니다")
    except Exception as e:
        print(f"  ✗ 클론 실패: {e}")
        print(f"  → 타임라인 생성 없이 파이프라인을 사용할 수 있습니다")

    return cfg


def _save_config(cfg):
    """config.json 업데이트."""
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)


def step_skill_md(cfg):
    """Step 5: SKILL.md 생성."""
    print("\n[5/6] SKILL.md 생성")

    zotero = cfg.get("zotero", {})
    github = cfg.get("github", {})

    replacements = {
        "{github_repo}": github.get("repo", ""),
        "{pages_base_url}": github.get("pages_base_url", ""),
        "{zotero_dir}": zotero.get("pdf_dir", ""),
        "{project_dir}": str(REPO),
        "{email}": zotero.get("email", "") or cfg.get("unpaywall_email", ""),
    }

    if not TEMPLATE_PATH.exists():
        print("  ✗ SKILL.md.template이 없습니다")
        return False

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)

    with open(SKILL_OUTPUT, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {SKILL_OUTPUT}")

    # .gitignore에 config.json 확인
    if GITIGNORE_PATH.exists():
        gi = GITIGNORE_PATH.read_text(encoding="utf-8")
        if "config.json" not in gi:
            with open(GITIGNORE_PATH, "a", encoding="utf-8") as f:
                f.write("\nconfig.json\n")
            print("  ✓ .gitignore에 config.json 추가")

    return True


def step_install():
    """Step 5: SKILL.md를 Claude Code skills에 설치."""
    print("\n[6/6] SKILL.md 설치")

    if not SKILL_OUTPUT.exists():
        print("  ✗ SKILL.md가 없습니다")
        return False

    SKILL_INSTALL_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SKILL_OUTPUT, SKILL_INSTALL_DIR / "SKILL.md")
    print(f"  ✓ {SKILL_INSTALL_DIR / 'SKILL.md'}")
    return True


# classify_papers / topic_modeling 이 의존하는 클러스터링 스택 — 이 import 들이
# 실제로 돌 인터프리터(py312) 에서 모두 통과해야 auto-run 이 중간에 안 죽는다.
_CLUSTERING_IMPORTS = "import umap, hdbscan, sentence_transformers, sklearn, numpy, joblib"


def _resolve_py312():
    """topic_modeling/classify 가 실제로 쓸 인터프리터를 run_update_force 와 동일 규칙으로 해석.

    run_update_force._resolve_topic_modeling_python() 를 그대로 재사용해 우선순위
    (PAPER_CURATION_PY312 → 형제 py312 env → which python3.12 → sys.executable)가
    런타임과 어긋나지 않게 한다. import 실패 시 보수적으로 sys.executable 로 fallback.
    """
    try:
        sys.path.insert(0, str(REPO / "pipeline"))
        from run_update_force import _resolve_topic_modeling_python  # type: ignore
        return _resolve_topic_modeling_python()
    except Exception:
        return sys.executable


def _preflight_clustering_env():
    """auto-run 전에 클러스터링 의존성이 py312 인터프리터에서 import 가능한지 확인.

    두 가지 실패 모드를 모두 잡는다:
      (a) py314 단일 env → numba CALL_KW 크래시 (UMAP/HDBSCAN 미라우팅)
      (b) 의존성 미설치 → ModuleNotFoundError
    실패하면 정확한 conda 명령을 안내하고 False 를 반환해 auto-run 을 건너뛴다.
    setup.py 자기 프로세스가 아니라 *실제로 돌 인터프리터* 로 probe 해야 의미가 있다.
    """
    py = _resolve_py312()
    try:
        probe = subprocess.run(
            [py, "-c", _CLUSTERING_IMPORTS],
            capture_output=True, text=True, timeout=120,
        )
    except Exception as e:
        print(f"  ✗ 클러스터링 인터프리터 점검 실패: {e}")
        probe = None

    if probe is not None and probe.returncode == 0:
        if py != sys.executable:
            print(f"  ✓ 클러스터링 인터프리터 확인: {py}")
        return True

    # 실패 — 정확한 복구 명령 안내
    print("  ✗ UMAP/HDBSCAN 클러스터링 환경이 준비되지 않았습니다.")
    print(f"    점검 인터프리터: {py}")
    if probe is not None and probe.stderr.strip():
        # 마지막 줄(주로 ModuleNotFoundError / numba CALL_KW)만 간결히 표시
        last = probe.stderr.strip().splitlines()[-1]
        print(f"    원인: {last}")
    print()
    print("    classify_papers/topic_modeling 은 numba+Python 3.14 충돌을 피하려고")
    print("    별도 py312 conda env 에서 돌아야 합니다. 아래를 실행해 환경을 만드세요:")
    print()
    print("      conda create -n py312 -c conda-forge python=3.12 pip -y")
    print("      conda run -n py312 pip install umap-learn hdbscan sentence-transformers \\")
    print("          joblib numpy scikit-learn anthropic openai")
    print()
    print("    (형제 env 가 아닌 경로면 PAPER_CURATION_PY312 환경변수로 절대 경로 지정)")
    return False


def main():
    parser = argparse.ArgumentParser(description="paper-curation setup")
    parser.add_argument("--no-install", action="store_true",
                        help="SKILL.md 스킬 설치를 건너뜁니다")
    parser.add_argument("--no-run", action="store_true",
                        help="설치만 하고 첫 파이프라인 실행은 건너뜁니다")
    args = parser.parse_args()

    print("=" * 50)
    print("  Paper Curation — Setup")
    print("=" * 50)

    # Step 1: config.json
    cfg = step_config()

    # Step 2: 환경변수 (OPENAI_API_KEY 는 필수 — 없으면 여기서 중단)
    step_env_check(cfg)

    # Step 3: Zotero 연결
    step_zotero_test(cfg)

    # Step 4: PaperBanana
    cfg = step_paperbanana(cfg)

    # Step 5: SKILL.md
    step_skill_md(cfg)

    # Step 5: 스킬 설치
    if not args.no_install:
        step_install()
    else:
        print(f"\n[6/6] 스킬 설치 건너뜀 (--no-install)")
        print(f"  수동 설치: cp {SKILL_OUTPUT} ~/.claude/skills/paper-curation/SKILL.md")

    # 요약
    collections = cfg.get("zotero", {}).get("collections", {})
    topics = list(collections.keys())

    print("\n" + "=" * 50)
    print("  설치 완료!")
    print("=" * 50)
    print(f"  Config:  {CONFIG_PATH}")
    if SKILL_OUTPUT.exists():
        print(f"  SKILL:   {SKILL_OUTPUT}")

    # 다음 단계 안내
    print("\n" + "-" * 50)
    print("  다음 단계: 파이프라인 실행")
    print("-" * 50)
    print()
    print("  설치가 완료되었습니다. 이제 파이프라인을 실행하여")
    print("  Zotero 컬렉션의 논문을 리뷰하고 웹 페이지로 배포할 수 있습니다.")
    print()
    print("  ⚠ 주의: Zotero 컬렉션의 논문 편수에 따라 시간이 크게 달라집니다 (Anthropic Tier·concurrency 의존).")
    print("    - 10편 이하: 수 분")
    print("    - 50편: ~15분 (Tier 4 default --concurrency 16) ~ 1~2시간 (Tier 1 --concurrency 4)")
    print("    - 500편 이상: 비례 증가. Tier별 권장값은 README 'Concurrency 가이드' 참고.")
    print()
    if topics:
        topic = topics[0]
        print(f"  실행 명령어 (이후에 수동으로 돌릴 때 — 단일 진입점은 run_full.py):")
        print(f"    # 전체 파이프라인 (Zotero에서 가져와서 리뷰 + Deep Research 인덱스 + 배포)")
        print(f"    PYTHONUTF8=1 python pipeline/run_full.py --topic {topic} --mode curate --source zotero")
        print()
        print(f"    # 주간 운영 (웹 검색으로 신규 논문 추가, 기존 유지)")
        print(f"    PYTHONUTF8=1 python pipeline/run_full.py --topic {topic} --mode curate --source web --days 7")
        print()
        print(f"    # 전체 재빌드 (categorization/insights/timelines 까지 재생성 — 시간·비용 ↑)")
        print(f"    PYTHONUTF8=1 python pipeline/run_full.py --topic {topic} --mode rebuild --yes")
    print()

    # Step 7: 첫 파이프라인 자동 실행 (--no-run 으로 건너뛸 수 있음)
    if topics and not args.no_run:
        topic = topics[0]
        print("-" * 50)
        print(f"  첫 파이프라인을 자동 실행합니다 (topic: {topic})")
        print("-" * 50)

        # Preflight: classify/topic_modeling 은 UMAP/HDBSCAN 의존 — 별도 py312 env
        # 에서 돌아야 한다 (numba 가 Python 3.14 의 CALL_KW opcode 를 못 다룸).
        # 의존성이 없거나 인터프리터가 py314 단일 env 면 build_papers_index →
        # topic_modeling 에서 CRITICAL_STEP 이 hard-fail 하므로, 깊숙이 들어가
        # 죽기 전에 여기서 미리 막고 정확한 conda 명령을 안내한 뒤 auto-run 을 건너뛴다.
        if not _preflight_clustering_env():
            print()
            print("  (위 환경을 준비한 뒤 'python pipeline/setup.py' 를 다시 실행하세요.)")
        else:
            print("  Zotero에서 논문을 가져와 리뷰 → 분류 → 인덱스 →")
            print("  Deep Research 검색 인덱스 → (GitHub 설정 시) 배포까지 진행합니다.")
            print("  Ctrl+C 로 중단할 수 있고, 중단 후에는 --resume 모드로 이어서 진행할 수 있습니다.")
            print()
            try:
                # 문서화된 단일 진입점 run_full.py 사용 — curate/zotero 가 비파괴
                # 기본 경로이며, topic_modeling/classify 의 py312 라우팅은 내부에서 처리.
                subprocess.run(
                    [sys.executable, str(REPO / "pipeline" / "run_full.py"),
                     "--topic", topic, "--mode", "curate", "--source", "zotero",
                     "--concurrency", "4"],
                    env={**os.environ, "PYTHONUTF8": "1"},
                    cwd=str(REPO),
                )
            except KeyboardInterrupt:
                print("\n  (파이프라인 실행이 중단되었습니다. 나중에 --resume 으로 재개 가능)")
    elif topics and args.no_run:
        print("  (--no-run 지정: 첫 파이프라인 실행은 건너뜁니다)")
    print()


if __name__ == "__main__":
    main()
