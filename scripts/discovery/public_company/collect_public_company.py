"""CLI orchestrator for public-company collection and modeling."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from target_config import load_target

from .books import collect_books
from .capital_signals import collect_capital_signals
from .cninfo_a import collect_cninfo_a
from .common import PublicCompanyTarget, ensure_public_company_dirs, update_collection_status, write_json
from .earnings_calls import fetch_earnings_calls
from .financial_model import write_financial_model
from .hkex import collect_hkex
from .market_data import fetch_market_data
from .quality_loop import run_quality_loop
from .sec_us import extract_mda_from_filings, fetch_sec_filings, parse_companyfacts_to_statements
from .semi_public_collect import scaffold_semi_public
from .audit import audit_public_company
from .source_strategy import discover_source_strategy


def _cached_sec_available(target: PublicCompanyTarget) -> bool:
    root = target.public_company_root / "metadata"
    return all((root / name).exists() for name in ["sec_submissions.json", "sec_companyfacts.json", "raw_manifest.json"])


def run_collection(target: PublicCompanyTarget, max_filings: int = 3, skip_network: bool = False, skip_model: bool = False) -> dict[str, Any]:
    ensure_public_company_dirs(target)
    status: dict[str, Any] = {
        "company": target.company_name,
        "ticker": target.ticker,
        "market": target.market,
        "started_at": datetime.now().isoformat(timespec="seconds"),
        "steps": {},
        "gaps": [],
    }
    update_collection_status(target, {**status, "status": "running"})

    try:
        status["steps"]["source_strategy"] = discover_source_strategy(target)
    except Exception as exc:  # noqa: BLE001
        status["steps"]["source_strategy"] = {"status": "failed", "error": str(exc)}
        status["gaps"].append({"step": "source_strategy", "reason": str(exc)})

    if skip_network:
        status["steps"]["network"] = {"status": "skipped"}
    else:
        if target.market == "US":
            try:
                status["steps"]["sec_filings"] = fetch_sec_filings(target, max_filings_per_type=max_filings)
            except Exception as exc:  # noqa: BLE001
                if _cached_sec_available(target):
                    status["steps"]["sec_filings"] = {
                        "status": "cached_after_fetch_error",
                        "error": str(exc),
                        "cache_files": [
                            "metadata/sec_submissions.json",
                            "metadata/sec_companyfacts.json",
                            "metadata/raw_manifest.json",
                        ],
                    }
                else:
                    status["steps"]["sec_filings"] = {"status": "failed", "error": str(exc)}
                    status["gaps"].append({"step": "sec_filings", "reason": str(exc)})
            try:
                status["steps"]["statements"] = parse_companyfacts_to_statements(target)
            except Exception as exc:  # noqa: BLE001
                status["steps"]["statements"] = {"status": "failed", "error": str(exc)}
                status["gaps"].append({"step": "statements", "reason": str(exc)})
            try:
                status["steps"]["mda"] = extract_mda_from_filings(target)
            except Exception as exc:  # noqa: BLE001
                status["steps"]["mda"] = {"status": "failed", "error": str(exc)}
                status["gaps"].append({"step": "mda", "reason": str(exc)})
        elif target.market == "HK":
            status["steps"]["hkex"] = collect_hkex(target)
        elif target.market in {"CN", "A"}:
            status["steps"]["cninfo_a"] = collect_cninfo_a(target)
        else:
            status["gaps"].append({"step": "market_adapter", "reason": f"unsupported_market: {target.market}"})

        for step_name, fn in [
            ("earnings_calls", fetch_earnings_calls),
            ("market_data", fetch_market_data),
            ("capital_signals", collect_capital_signals),
            ("books", collect_books),
        ]:
            try:
                status["steps"][step_name] = fn(target)
            except Exception as exc:  # noqa: BLE001
                status["steps"][step_name] = {"status": "failed", "error": str(exc)}
                status["gaps"].append({"step": step_name, "reason": str(exc)})

    try:
        status["steps"]["semi_public"] = scaffold_semi_public(target)
    except Exception as exc:  # noqa: BLE001
        status["steps"]["semi_public"] = {"status": "failed", "error": str(exc)}
        status["gaps"].append({"step": "semi_public", "reason": str(exc)})

    if not skip_model:
        try:
            status["steps"]["financial_model"] = write_financial_model(target)
            validation_path = status["steps"]["financial_model"].get("validation_path")
            if validation_path and Path(validation_path).exists():
                validation = json.loads(Path(validation_path).read_text(encoding="utf-8"))
                status["steps"]["financial_model"]["validation_status"] = validation.get("status")
                status["steps"]["financial_model"]["model_usability"] = validation.get("model_usability")
                if validation.get("gaps"):
                    status["gaps"].append({"step": "financial_model", "reason": "model_validation_gaps", "gaps": validation.get("gaps", [])})
        except Exception as exc:  # noqa: BLE001
            status["steps"]["financial_model"] = {"status": "failed", "error": str(exc)}
            status["gaps"].append({"step": "financial_model", "reason": str(exc)})

    try:
        status["steps"]["data_quality_audit"] = audit_public_company(target)
        if status["steps"]["data_quality_audit"].get("gaps"):
            status["gaps"].append(
                {
                    "step": "data_quality_audit",
                    "reason": "data_quality_gaps",
                    "gaps": status["steps"]["data_quality_audit"].get("gaps", []),
                }
            )
    except Exception as exc:  # noqa: BLE001
        status["steps"]["data_quality_audit"] = {"status": "failed", "error": str(exc)}
        status["gaps"].append({"step": "data_quality_audit", "reason": str(exc)})

    status["finished_at"] = datetime.now().isoformat(timespec="seconds")
    step_statuses = [str(step.get("status", "ok")) if isinstance(step, dict) else "ok" for step in status["steps"].values()]
    status["status"] = "ok" if status["steps"] and not status["gaps"] and not any(item == "failed" for item in step_statuses) else "needs_review"
    write_json(target.public_company_root / "metadata" / "api_probe_status.json", {"steps": status["steps"], "updated_at": status["finished_at"]})
    update_collection_status(target, status)
    return status


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Configured research key, ticker, or slug")
    parser.add_argument("--max-filings", type=int, default=3)
    parser.add_argument("--skip-network", action="store_true")
    parser.add_argument("--skip-model", action="store_true")
    parser.add_argument("--quality-loop", action="store_true", help="Run audit/repair/model loop until pass or bounded blocker.")
    parser.add_argument("--max-quality-iterations", type=int, default=3)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    config = load_target(args.target)
    target = PublicCompanyTarget.from_config(config)
    status = run_collection(target, max_filings=args.max_filings, skip_network=args.skip_network, skip_model=args.skip_model)
    if args.quality_loop:
        pre_loop_gaps = list(status.get("gaps", []))
        loop_status = run_quality_loop(target, max_iterations=args.max_quality_iterations)
        status["steps"]["quality_loop"] = loop_status
        status["quality_loop_status"] = loop_status.get("status")
        status["pre_quality_loop_gaps"] = pre_loop_gaps
        if loop_status.get("status") == "pass":
            status["status"] = "ok"
            status["gaps"] = []
        else:
            status["status"] = "needs_review"
            status["gaps"] = [
                {
                    "step": "quality_loop",
                    "reason": "quality_loop_blocked",
                    "gaps": loop_status.get("remaining_gaps", []),
                    "blocker_notes": loop_status.get("blocker_notes", {}),
                }
            ]
        status["finished_at"] = datetime.now().isoformat(timespec="seconds")
        write_json(target.public_company_root / "metadata" / "api_probe_status.json", {"steps": status["steps"], "updated_at": status["finished_at"]})
        update_collection_status(target, status)
    if args.json:
        print(json.dumps(status, ensure_ascii=False, indent=2, default=str))
    else:
        print(f"{target.company_name} public-company collection: {status['status']}")
        print(target.public_company_root)
    return 0 if status["status"] in {"ok", "needs_review", "partial"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
