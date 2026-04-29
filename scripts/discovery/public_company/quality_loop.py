"""Bounded audit/repair loop for public-company collection quality."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Callable

from .audit import audit_public_company
from .books import collect_books
from .capital_signals import collect_capital_signals
from .common import PublicCompanyTarget, write_json, write_markdown
from .earnings_calls import fetch_earnings_calls
from .financial_model import write_financial_model
from .market_data import fetch_market_data
from .sec_us import extract_mda_from_filings, fetch_sec_filings, parse_companyfacts_to_statements
from .source_strategy import discover_source_strategy


HARD_BLOCKER_NOTES = {
    "semi_public_fetched_sources": "Semi-public folders are scaffolded, but source fetching requires collect/webfetch credentials or manual approval.",
}


def _repair_source_strategy(target: PublicCompanyTarget) -> dict[str, Any]:
    return {"action": "discover_source_strategy", "result": discover_source_strategy(target)}


def _repair_statements(target: PublicCompanyTarget) -> dict[str, Any]:
    return {"action": "parse_companyfacts_to_statements", "result": parse_companyfacts_to_statements(target)}


def _repair_filings(target: PublicCompanyTarget) -> dict[str, Any]:
    return {"action": "fetch_sec_filings", "result": fetch_sec_filings(target)}


def _repair_mda(target: PublicCompanyTarget) -> dict[str, Any]:
    return {"action": "extract_mda_from_filings", "result": extract_mda_from_filings(target)}


def _repair_market_data(target: PublicCompanyTarget) -> dict[str, Any]:
    return {"action": "fetch_market_data", "result": fetch_market_data(target)}


def _repair_books(target: PublicCompanyTarget) -> dict[str, Any]:
    return {"action": "collect_books", "result": collect_books(target)}


def _repair_earnings_calls(target: PublicCompanyTarget) -> dict[str, Any]:
    return {"action": "fetch_earnings_calls", "result": fetch_earnings_calls(target)}


def _repair_capital_signals(target: PublicCompanyTarget) -> dict[str, Any]:
    return {"action": "collect_capital_signals", "result": collect_capital_signals(target)}


REPAIR_ACTIONS: dict[str, list[Callable[[PublicCompanyTarget], dict[str, Any]]]] = {
    "source_strategy": [_repair_source_strategy],
    "raw_annual_reports": [_repair_filings],
    "annual_report_pdf": [_repair_filings],
    "annual_report_pdf_content_identity": [_repair_filings],
    "raw_quarterly_reports": [_repair_filings],
    "raw_prospectus": [_repair_filings],
    "annual_statement_completeness": [_repair_statements],
    "annual_metric_completeness": [_repair_statements],
    "annual_history_coverage": [_repair_statements],
    "annual_statement_schema": [_repair_statements],
    "annual_statement_density": [_repair_statements],
    "quarterly_income_statement": [_repair_statements],
    "quarterly_statement_schema": [_repair_statements],
    "quarterly_statement_density": [_repair_statements],
    "mda_extract": [_repair_mda],
    "mda_content_identity": [_repair_mda],
    "earnings_presentations": [_repair_earnings_calls],
    "earnings_presentation_content_identity": [_repair_earnings_calls],
    "earnings_transcripts": [_repair_earnings_calls],
    "earnings_transcript_content_identity": [_repair_earnings_calls],
    "market_data_price_history": [_repair_market_data],
    "market_cap_confidence": [_repair_market_data],
    "valuation_snapshot_density": [_repair_market_data],
    "peer_multiples": [_repair_market_data],
    "comps_multiples": [_repair_market_data],
    "institutional_holders": [_repair_capital_signals],
    "institutional_holder_density": [_repair_capital_signals],
    "investor_views_sources": [_repair_capital_signals],
    "books": [_repair_books],
    "model_validation": [],
}


def _unique_actions(gaps: list[str]) -> list[Callable[[PublicCompanyTarget], dict[str, Any]]]:
    actions: list[Callable[[PublicCompanyTarget], dict[str, Any]]] = [_repair_source_strategy]
    for gap in gaps:
        actions.extend(REPAIR_ACTIONS.get(gap, []))
    unique: list[Callable[[PublicCompanyTarget], dict[str, Any]]] = []
    seen: set[str] = set()
    for action in actions:
        if action.__name__ in seen:
            continue
        seen.add(action.__name__)
        unique.append(action)
    return unique


def run_quality_loop(target: PublicCompanyTarget, max_iterations: int = 3, as_of_date: str | None = None) -> dict[str, Any]:
    history: list[dict[str, Any]] = []
    status = "needs_review"
    last_gaps: list[str] = []
    blocker_notes: dict[str, str] = {}
    max_iterations = max(1, max_iterations)

    for iteration in range(1, max_iterations + 1):
        model = write_financial_model(target, as_of_date=as_of_date)
        audit = audit_public_company(target)
        gaps = list(dict.fromkeys([*audit.get("gaps", []), *model.get("gaps", [])]))
        last_gaps = gaps
        entry: dict[str, Any] = {
            "iteration": iteration,
            "audit_status": audit.get("status"),
            "gaps_before_repair": gaps,
            "model": model,
            "repair_actions": [],
        }
        if audit.get("status") == "pass":
            status = "pass"
            history.append(entry)
            break

        actions = _unique_actions(gaps)
        if not actions:
            status = "blocked"
            history.append(entry)
            break

        for action in actions:
            try:
                entry["repair_actions"].append(action(target))
            except Exception as exc:  # noqa: BLE001
                entry["repair_actions"].append({"action": action.__name__, "status": "failed", "error": str(exc)})
        history.append(entry)

        repaired_model = write_financial_model(target, as_of_date=as_of_date)
        repaired_audit = audit_public_company(target)
        repaired_gaps = list(repaired_audit.get("gaps", []))
        if repaired_audit.get("status") == "pass":
            status = "pass"
            last_gaps = []
            history.append(
                {
                    "iteration": iteration,
                    "audit_status": "pass_after_repair",
                    "gaps_before_repair": gaps,
                    "gaps_after_repair": [],
                    "model": repaired_model,
                    "repair_actions": [],
                }
            )
            break
        if sorted(repaired_gaps) == sorted(gaps):
            status = "blocked"
            last_gaps = repaired_gaps
            break
        last_gaps = repaired_gaps

    if status != "pass":
        for gap in last_gaps:
            if gap in HARD_BLOCKER_NOTES:
                blocker_notes[gap] = HARD_BLOCKER_NOTES[gap]
        if not blocker_notes:
            blocker_notes = {gap: "Quality gap remained after automated repair loop." for gap in last_gaps}
        status = "blocked"

    payload = {
        "company": target.company_name,
        "ticker": target.ticker,
        "status": status,
        "max_iterations": max_iterations,
        "iterations_run": len(history),
        "remaining_gaps": last_gaps,
        "blocker_notes": blocker_notes,
        "history": history,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    root = target.public_company_root / "metadata"
    write_json(root / "quality_loop_status.json", payload)
    gap_lines = [f"- {gap}: {blocker_notes.get(gap, '')}".rstrip() for gap in last_gaps] or ["- none"]
    write_markdown(
        root / "quality_loop_status.md",
        [
            f"# {target.company_name} Quality Loop",
            "",
            f"- Status: {status}",
            f"- Iterations run: {len(history)}",
            "",
            "## Remaining Gaps",
            *gap_lines,
        ],
    )
    return payload
