"""Launcher for public-company data-quality audits."""

from __future__ import annotations

import json
import sys
from pathlib import Path


MODULE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(MODULE_DIR))

from public_company.audit import audit_public_company  # noqa: E402
from public_company.common import PublicCompanyTarget  # noqa: E402
from target_config import load_target  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    target = PublicCompanyTarget.from_config(load_target(args.target))
    audit = audit_public_company(target)
    if args.json:
        print(json.dumps(audit, ensure_ascii=False, indent=2))
    else:
        print(target.public_company_root / "metadata" / "data_quality_audit.json")
    return 0 if audit["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

