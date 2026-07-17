"""
config.json 로더 + Zotero User ID / Collection Key 자동 조회.

모든 스크립트가 이 모듈을 통해 설정을 읽는다.
config.json이 없으면 환경변수 폴백.

Collection은 이름(예: "AI assisted Research")으로 지정하면
Zotero API로 collection key를 자동 조회한다.
"""

import json
import os
import ssl
import urllib.request
from pathlib import Path

# Corporate proxy intercepts HTTPS with self-signed cert; skip verification
_ssl_ctx = ssl.create_default_context()
_ssl_ctx.check_hostname = False
_ssl_ctx.verify_mode = ssl.CERT_NONE

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PIPELINE_DIR.parent
CONFIG_PATH = PROJECT_ROOT / "config.json"


def _load_dotenv():
    """PROJECT_ROOT/.env 를 읽어 환경변수로 주입. 셸에서 이미 설정된 값이 우선.

    외부 의존성 없는 단순 파서: KEY=VALUE 줄만 처리하고 빈 줄·'#' 주석은
    무시한다. 'export ' 접두사와 값 양끝 따옴표는 벗겨낸다.
    (.env 는 whitelist .gitignore 에 의해 자동으로 커밋 제외됨)
    """
    env_path = PROJECT_ROOT / ".env"
    if not env_path.exists():
        return
    try:
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            if line.startswith("export "):
                line = line[len("export "):]
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip("'\"")
            if key:
                os.environ.setdefault(key, value)
    except Exception as e:
        print(f"WARNING: .env 로드 실패: {e}")


_load_dotenv()

# 배포 파일 경로 (GitHub Pages 서빙 루트)
DOCS_DIR = PROJECT_ROOT / "docs"
PAPERS_DIR = DOCS_DIR / "papers"

# 타임라인/워크플로우 이미지 출력
IMG_TIMELINES_DIR = PIPELINE_DIR / "_img_timelines"
IMG_WORKFLOWS_DIR = PIPELINE_DIR / "_img_workflows"

REPO = PROJECT_ROOT  # backward compat alias

_config_cache = None
_user_id_cache = None
_collection_key_cache = None


def load_config():
    """config.json 로드. 없으면 환경변수 폴백."""
    global _config_cache
    if _config_cache is not None:
        return _config_cache

    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            _config_cache = json.load(f)
    else:
        _config_cache = {
            "zotero": {
                "api_key": os.environ.get("ZOTERO_API_KEY", ""),
                "email": os.environ.get("UNPAYWALL_EMAIL", ""),
                "collections": {},
            },
            "unpaywall_email": os.environ.get("UNPAYWALL_EMAIL", ""),
        }

    return _config_cache


def get_zotero_api_key():
    cfg = load_config()
    return cfg.get("zotero", {}).get("api_key", "") or os.environ.get("ZOTERO_API_KEY", "")


def get_zotero_user_id():
    """Zotero API Key로 User ID를 자동 조회. 캐싱."""
    global _user_id_cache
    if _user_id_cache is not None:
        return _user_id_cache

    env_id = os.environ.get("ZOTERO_USER_ID", "")
    if env_id:
        _user_id_cache = env_id
        return env_id

    api_key = get_zotero_api_key()
    if not api_key:
        raise ValueError("Zotero API key not found. Set config.json or ZOTERO_API_KEY env var.")

    try:
        url = "https://api.zotero.org/keys/current"
        req = urllib.request.Request(url, headers={
            "Zotero-API-Key": api_key, "User-Agent": "Mozilla/5.0",
        })
        with urllib.request.urlopen(req, timeout=15, context=_ssl_ctx) as resp:
            data = json.load(resp)
        _user_id_cache = str(data.get("userID", ""))
        return _user_id_cache
    except Exception as e:
        raise ValueError(f"Failed to fetch Zotero User ID: {e}")


def get_zotero_library_base():
    """Zotero API 라이브러리 베이스 경로 반환.

    config.json의 zotero.library가 "group:<groupID>"면 'groups/<groupID>',
    그 외("user" 또는 미설정)는 'users/<userID>'.
    환경변수 ZOTERO_LIBRARY 폴백 지원.
    """
    cfg = load_config()
    lib = str(cfg.get("zotero", {}).get("library", "")
              or os.environ.get("ZOTERO_LIBRARY", "")).strip()
    if lib.startswith("group:"):
        group_id = lib.split(":", 1)[1].strip()
        if not group_id.isdigit():
            raise ValueError(f"Invalid zotero.library group ID: '{lib}' (expected 'group:<numeric ID>')")
        return f"groups/{group_id}"
    return f"users/{get_zotero_user_id()}"


def _fetch_collection_keys():
    """Zotero에서 collection name → key 매핑을 조회. 캐싱."""
    global _collection_key_cache
    if _collection_key_cache is not None:
        return _collection_key_cache

    api_key = get_zotero_api_key()
    lib_base = get_zotero_library_base()

    try:
        url = f"https://api.zotero.org/{lib_base}/collections?format=json&limit=100"
        req = urllib.request.Request(url, headers={
            "Zotero-API-Key": api_key, "User-Agent": "Mozilla/5.0",
        })
        with urllib.request.urlopen(req, timeout=15, context=_ssl_ctx) as resp:
            cols = json.load(resp)
        _collection_key_cache = {c["data"]["name"]: c["data"]["key"] for c in cols}
        return _collection_key_cache
    except Exception as e:
        print(f"WARNING: Failed to fetch Zotero collections: {e}")
        _collection_key_cache = {}
        return _collection_key_cache


def _resolve_collection_value(value):
    """Collection value가 이름이면 key로 변환, 이미 key면 그대로.

    Zotero collection key는 8자 대문자 영숫자 (예: WKEZLEE8).
    "Humanoid"처럼 8자이면서 알파벳이 섞인 이름과 구분하기 위해
    먼저 이름으로 조회한다.
    """
    if not value:
        return ""
    # 이름으로 먼저 조회 (API 캐시)
    name_to_key = _fetch_collection_keys()
    if value in name_to_key:
        return name_to_key[value]
    # Zotero key 패턴: 8자 + 대문자/숫자만 (소문자 불가)
    if len(value) == 8 and value.isalnum() and not any(c.islower() for c in value):
        return value
    print(f"WARNING: Collection '{value}' not found in Zotero.")
    return value


def get_collections():
    """topic → collection key dict 반환. 이름은 자동으로 key로 변환."""
    cfg = load_config()
    raw = cfg.get("zotero", {}).get("collections", {})
    return {topic: _resolve_collection_value(val) for topic, val in raw.items()}


def get_collection_key(topic):
    return get_collections().get(topic, "")


def get_unpaywall_email():
    cfg = load_config()
    return cfg.get("unpaywall_email", "") or cfg.get("zotero", {}).get("email", "")


def get_paperbanana_dir():
    cfg = load_config()
    return cfg.get("paperbanana_dir", "")


def get_zotero_dir():
    """Zotero PDF 저장 디렉토리."""
    cfg = load_config()
    return (cfg.get("zotero", {}).get("pdf_dir", "")
            or os.environ.get("ZOTERO_DIR", ""))


def get_github_repo():
    """GitHub repo (owner/repo 형식)."""
    cfg = load_config()
    return (cfg.get("github", {}).get("repo", "")
            or os.environ.get("GITHUB_REPO", ""))


def get_github_branch():
    """GitHub branch (기본 master)."""
    cfg = load_config()
    return (cfg.get("github", {}).get("branch", "")
            or os.environ.get("GITHUB_BRANCH", "master"))


def get_pages_base_url():
    """GitHub Pages base URL."""
    cfg = load_config()
    return (cfg.get("github", {}).get("pages_base_url", "")
            or os.environ.get("PAGES_BASE_URL", ""))


def get_topic_dir(topic: str) -> Path:
    """docs/{topic} 경로 반환."""
    return DOCS_DIR / topic


def get_papers_index_path() -> Path:
    """papers/_papers_index.json 경로 반환."""
    return PAPERS_DIR / "_papers_index.json"
