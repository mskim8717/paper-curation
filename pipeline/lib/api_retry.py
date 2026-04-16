"""
Tenacity-style retry wrappers for Anthropic / OpenAI / Gemini API calls.

Use as decorator or context. Aborts on permanent errors (auth, billing,
malformed request) and retries on transient (5xx, network, rate-limit) up
to 3 attempts with exponential backoff (2s, 4s, 8s).
"""

import functools
import time

# Permanent (do not retry). Detected by HTTP status or exception class.
_PERMANENT_HTTP = {400, 401, 403, 404, 422}

# Retryable
_RETRYABLE_HTTP = {408, 429, 500, 502, 503, 504, 529}


def _classify(exc):
    """Return 'permanent' | 'retryable' | 'unknown'."""
    code = getattr(exc, "status_code", None)
    # Anthropic / OpenAI exceptions expose .status_code
    if code in _PERMANENT_HTTP:
        return "permanent"
    if code in _RETRYABLE_HTTP:
        return "retryable"
    # Network errors: retry
    cls_name = type(exc).__name__
    if any(k in cls_name for k in ("Timeout", "Connection", "APIConnection",
                                    "RateLimit")):
        return "retryable"
    # Billing / quota errors: permanent (no point retrying)
    text = str(exc).lower()
    if any(k in text for k in ("billing", "spending cap", "quota exceeded",
                                 "exceeded its monthly", "insufficient_quota")):
        return "permanent"
    return "unknown"


def with_retry(max_attempts=3, base_delay=2.0):
    """Decorator: retry on transient failures with exponential backoff.

    `base_delay * 2**(attempt-1)` seconds. Permanent errors raise immediately.
    """
    def deco(fn):
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception as exc:
                    kind = _classify(exc)
                    if kind == "permanent" or attempt >= max_attempts:
                        raise
                    delay = base_delay * (2 ** (attempt - 1))
                    print(f"[api_retry] attempt {attempt}/{max_attempts} "
                          f"failed ({kind}: {type(exc).__name__}: "
                          f"{str(exc)[:120]}); sleeping {delay}s",
                          flush=True)
                    time.sleep(delay)
        return wrapped
    return deco
