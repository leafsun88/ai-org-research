"""Launcher for the public-company collector package."""

from __future__ import annotations

import sys
from pathlib import Path


MODULE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(MODULE_DIR))

from public_company.collect_public_company import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())

