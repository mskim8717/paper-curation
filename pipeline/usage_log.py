"""Best-effort pipeline token-usage reporter.

Posts per-call token counts (from google-genai ``usage_metadata``) to the local
OpenTelemetry usage receiver's ``/pc/usage`` endpoint, which bins them into
5-minute buckets for the API-usage (종량제) dashboard graph.

Fire-and-forget on a daemon thread with a short timeout; every failure is
swallowed so instrumentation can never affect the pipeline run.
"""
from __future__ import annotations

import json
import os
import threading
import urllib.request

ENDPOINT = os.environ.get("PC_USAGE_ENDPOINT", "http://localhost:4318/pc/usage")


def _post(payload: dict) -> None:
    def run():
        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                ENDPOINT, data=data, headers={"Content-Type": "application/json"}, method="POST"
            )
            urllib.request.urlopen(req, timeout=3).read()
        except Exception:
            pass

    try:
        threading.Thread(target=run, daemon=True).start()
    except Exception:
        pass


def record_gemini(resp, model: str | None = None) -> None:
    """Extract token counts from a google-genai response and report them."""
    try:
        um = getattr(resp, "usage_metadata", None)
        if um is None:
            return

        def g(*names):
            for n in names:
                v = getattr(um, n, None)
                if isinstance(v, (int, float)) and v:
                    return int(v)
            return 0

        by_type = {
            "input": g("prompt_token_count"),
            "output": g("candidates_token_count"),
            "cached": g("cached_content_token_count"),
            "reasoning": g("thoughts_token_count"),
        }
        by_type = {k: v for k, v in by_type.items() if v}
        if not by_type:
            return
        _post({"provider": "gemini", "by_type": by_type, "model": model})
    except Exception:
        pass
