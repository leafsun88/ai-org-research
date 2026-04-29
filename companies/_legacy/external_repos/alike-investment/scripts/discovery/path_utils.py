import json
import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
VAULT_DIR = PROJECT_ROOT / "vault" / "companies"
INDEX_PATH = PROJECT_ROOT / "vault" / "_index.json"


def _ticker_to_slug(ticker: str) -> str:
    try:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        return data.get("ticker_map", {}).get(ticker, ticker.lower())
    except Exception:
        return ticker.lower()


def resolve_discovery_dir(ticker: str) -> Path:
    alike_db_dir = os.environ.get("ALIKE_DB_DIR")
    if alike_db_dir:
        candidate = Path(alike_db_dir) / ticker
        if candidate.exists():
            return candidate
    slug = _ticker_to_slug(ticker)
    return VAULT_DIR / slug / "discovery"
