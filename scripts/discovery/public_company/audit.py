"""Data-quality audit for public-company collection outputs."""

from __future__ import annotations

import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

from .common import PublicCompanyTarget, read_json, write_json, write_markdown
from .financial_model import ANNUAL_REQUIRED_METRICS


UNRELATED_CONTENT_TERMS = [
    "disruptor in education",
    "schools we serve",
    "virtual public education",
    "enrollment",
    "effective teachers",
]


def _pass(condition: bool, details: dict[str, Any] | None = None) -> dict[str, Any]:
    return {"passed": bool(condition), **(details or {})}


def _row_density(rows: list[dict[str, Any]], required_fields: list[str]) -> dict[str, Any]:
    populated_rows = 0
    row_scores: list[dict[str, Any]] = []
    for row in rows:
        present = [field for field in required_fields if row.get(field) not in {None, ""}]
        if present:
            populated_rows += 1
        row_scores.append(
            {
                "period": row.get("period") or row.get("date") or row.get("ticker") or row.get("holder"),
                "present_fields": len(present),
                "required_fields": len(required_fields),
                "missing_fields": [field for field in required_fields if field not in present],
            }
        )
    total_required = len(rows) * len(required_fields)
    present_total = sum(item["present_fields"] for item in row_scores)
    return {
        "rows": len(rows),
        "populated_rows": populated_rows,
        "required_fields": required_fields,
        "present_required_values": present_total,
        "total_required_values": total_required,
        "density": (present_total / total_required) if total_required else 0,
        "row_scores": row_scores,
    }


def _csv_row_count(path: Any) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        line_count = sum(1 for _ in handle)
    return max(0, line_count - 1)


def _artifact_text_sample(path: Path, limit: int = 12000) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        if not shutil.which("pdftotext"):
            return ""
        result = subprocess.run(["pdftotext", str(path), "-"], text=True, capture_output=True, timeout=15, check=False)
        return result.stdout[:limit]
    if suffix in {".htm", ".html", ".xml", ".md", ".json", ".csv", ".txt"}:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit]
    return ""


def _content_review(target: PublicCompanyTarget, path: Path, required_terms: list[str] | None = None) -> dict[str, Any]:
    text = _artifact_text_sample(path)
    text_l = text.lower()
    identity_terms = [target.company_name, target.ticker, *target.aliases, *(required_terms or [])]
    hits = sorted({term for term in identity_terms if term and str(term).lower() in text_l})
    forbidden_hits = [term for term in UNRELATED_CONTENT_TERMS if term in text_l]
    passed = len(text.strip()) >= 500 and bool(hits) and not forbidden_hits
    return {
        "path": str(path),
        "passed": passed,
        "identity_hits": hits,
        "forbidden_hits": forbidden_hits,
        "text_chars_checked": len(text),
        "sample": " ".join(text[:240].split()),
    }


def _annual_income_years_from_companyfacts(target: PublicCompanyTarget) -> list[str]:
    companyfacts = read_json(target.public_company_root / "metadata" / "sec_companyfacts.json", {}) or {}
    facts = companyfacts.get("facts", {}).get("us-gaap", {})
    years: set[str] = set()
    for tag in ["RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "Revenues"]:
        units = (facts.get(tag) or {}).get("units", {})
        for unit_values in units.values():
            for fact in unit_values:
                form = str(fact.get("form") or "")
                fp = str(fact.get("fp") or "")
                end = str(fact.get("end") or "")
                if form in {"10-K", "10-K/A", "20-F", "20-F/A"} and fp == "FY" and len(end) >= 4:
                    years.add(end[:4])
    return sorted(years)


def audit_public_company(target: PublicCompanyTarget, model_validation: dict[str, Any] | None = None) -> dict[str, Any]:
    root = target.public_company_root
    checks: dict[str, dict[str, Any]] = {}
    gaps: list[str] = []
    warnings: list[str] = []

    annual_files = list((root / "raw_filings" / "annual_reports").glob("*"))
    quarterly_files = list((root / "raw_filings" / "quarterly_reports").glob("*"))
    prospectus_files = list((root / "raw_filings" / "prospectus").glob("*"))
    source_strategy = read_json(root / "metadata" / "source_strategy.json", {}) or {}
    checks["source_strategy"] = _pass(
        bool(source_strategy.get("local_skills")) and bool(source_strategy.get("market_guides")),
        {
            "local_skills": len(source_strategy.get("local_skills", [])),
            "market_guides": len(source_strategy.get("market_guides", [])),
        },
    )
    checks["raw_annual_reports"] = _pass(bool(annual_files), {"count": len(annual_files)})
    annual_pdf_files = [path for path in annual_files if path.suffix.lower() == ".pdf"]
    checks["annual_report_pdf"] = _pass(
        bool(annual_pdf_files),
        {
            "count": len(annual_pdf_files),
            "pdf_paths": [str(path) for path in annual_pdf_files[:10]],
            "note": "A 10-K HTML or SEC companyfacts JSON is not enough; save a native annual-report PDF when available, such as SEC ARS or IR Download PDF.",
        },
    )
    annual_pdf_reviews = [_content_review(target, path, ["Annual Report", "Form 10-K"]) for path in annual_pdf_files]
    checks["annual_report_pdf_content_identity"] = _pass(
        bool(annual_pdf_reviews) and all(item["passed"] for item in annual_pdf_reviews),
        {"items": annual_pdf_reviews},
    )
    checks["raw_quarterly_reports"] = _pass(bool(quarterly_files), {"count": len(quarterly_files)})
    checks["raw_prospectus"] = _pass(bool(prospectus_files), {"count": len(prospectus_files)})

    mda_files = list((root / "processed" / "mda").glob("*.md"))
    mda_chars = sum(path.stat().st_size for path in mda_files)
    checks["mda_extract"] = _pass(bool(mda_files) and mda_chars > 5000, {"files": len(mda_files), "bytes": mda_chars})
    mda_reviews = [_content_review(target, path, ["Management", "Results of Operations"]) for path in mda_files]
    checks["mda_content_identity"] = _pass(bool(mda_reviews) and all(item["passed"] for item in mda_reviews), {"items": mda_reviews})

    earnings_meta = read_json(root / "raw_filings" / "earnings_calls" / "earnings_call_metadata.json", {}) or {}
    presentation_files = list((root / "raw_filings" / "earnings_calls").glob("*.pdf"))
    transcript_files = list((root / "raw_filings" / "earnings_calls").glob("*transcript*")) + list((root / "processed" / "earnings_calls").glob("*transcript*"))
    checks["earnings_presentations"] = _pass(bool(presentation_files), {"count": len(presentation_files)})
    presentation_reviews = [_content_review(target, path, ["fiscal", "quarter"]) for path in presentation_files]
    checks["earnings_presentation_content_identity"] = _pass(
        bool(presentation_reviews) and all(item["passed"] for item in presentation_reviews),
        {"items": presentation_reviews},
    )
    checks["earnings_transcripts"] = _pass(
        bool(transcript_files),
        {
            "count": len(transcript_files),
            "official_transcript_status": earnings_meta.get("official_transcript_status"),
            "fallback_sources": earnings_meta.get("fallback_transcript_sources", []),
        },
    )
    processed_transcripts = list((root / "processed" / "earnings_calls").glob("*transcript*.md"))
    transcript_reviews = [_content_review(target, path, ["Operator", "David Goeckeler", "Luis Visoso"]) for path in processed_transcripts]
    checks["earnings_transcript_content_identity"] = _pass(
        bool(transcript_reviews) and all(item["passed"] for item in transcript_reviews),
        {"items": transcript_reviews},
    )

    annual = read_json(root / "data" / "statements" / "annual_statements.json", {"periods": []}) or {"periods": []}
    quarterly = read_json(root / "data" / "statements" / "quarterly_statements.json", {"periods": []}) or {"periods": []}
    checks["annual_statement_schema"] = _pass(
        isinstance(annual.get("periods"), list) and bool(annual.get("periods")),
        {"required_top_level_key": "periods", "rows": len(annual.get("periods", [])) if isinstance(annual.get("periods"), list) else 0},
    )
    checks["quarterly_statement_schema"] = _pass(
        isinstance(quarterly.get("periods"), list) and bool(quarterly.get("periods")),
        {
            "required_top_level_key": "periods",
            "rows": len(quarterly.get("periods", [])) if isinstance(quarterly.get("periods"), list) else 0,
        },
    )
    latest = (annual.get("periods") or [{}])[-1] if annual.get("periods") else {}
    missing_annual = [metric for metric in ANNUAL_REQUIRED_METRICS if latest.get(metric) in {None, ""}]
    checks["annual_statement_completeness"] = _pass(not missing_annual, {"missing": missing_annual})
    expected_annual_years = _annual_income_years_from_companyfacts(target)
    actual_annual_income_years = sorted(
        {
            str(row.get("period"))
            for row in annual.get("periods", [])
            if row.get("revenue") not in {None, ""} and (row.get("operating_income") not in {None, ""} or row.get("net_income") not in {None, ""})
        }
    )
    expected_history_count = min(3, len(expected_annual_years)) if expected_annual_years else min(3, len(actual_annual_income_years))
    checks["annual_history_coverage"] = _pass(
        len(actual_annual_income_years) >= expected_history_count,
        {
            "expected_years_from_companyfacts": expected_annual_years,
            "actual_income_years": actual_annual_income_years,
            "minimum_required": expected_history_count,
        },
    )
    annual_density = _row_density(
        annual.get("periods", []),
        ["revenue", "gross_profit", "operating_income", "net_income", "operating_cash_flow", "capital_expenditures"],
    )
    checks["annual_statement_density"] = _pass(
        annual_density["rows"] >= expected_history_count and annual_density["density"] >= 0.80,
        {**annual_density, "minimum_required_rows": expected_history_count, "minimum_density": 0.80},
    )
    quarterly_income_rows = [
        row
        for row in quarterly.get("periods", [])
        if row.get("revenue") not in {None, ""} and (row.get("net_income") not in {None, ""} or row.get("operating_income") not in {None, ""})
    ]
    checks["quarterly_income_statement"] = _pass(bool(quarterly_income_rows), {"rows_with_revenue_and_income": len(quarterly_income_rows)})
    quarterly_density = _row_density(
        quarterly.get("periods", []),
        ["revenue", "gross_profit", "operating_income", "net_income", "assets", "liabilities", "cash"],
    )
    checks["quarterly_statement_density"] = _pass(
        quarterly_density["rows"] >= 2 and quarterly_density["density"] >= 0.70,
        {**quarterly_density, "minimum_required_rows": 2, "minimum_density": 0.70},
    )

    valuation = read_json(root / "data" / "valuation" / "valuation_snapshot.json", {}) or {}
    price_rows = _csv_row_count(root / "data" / "market_data" / "price_history.csv")
    checks["market_data_price_history"] = _pass(price_rows >= 60, {"rows": price_rows, "minimum_rows": 60})
    checks["market_cap_confidence"] = _pass(
        valuation.get("market_cap_confidence") not in {"low", "missing", "unknown", None},
        {"confidence": valuation.get("market_cap_confidence"), "source": valuation.get("market_cap_source") or valuation.get("source")},
    )
    valuation_required = ["last_price", "shares_outstanding", "market_cap", "enterprise_value", "currency", "market_cap_source"]
    valuation_missing = [field for field in valuation_required if valuation.get(field) in {None, ""}]
    checks["valuation_snapshot_density"] = _pass(not valuation_missing, {"missing": valuation_missing, "required": valuation_required})

    peers = read_json(root / "data" / "valuation" / "peer_valuation.json", {"peers": []}) or {"peers": []}
    peers_with_multiples = [
        row
        for row in peers.get("peers", [])
        if row.get("price_to_sales") not in {None, ""} or row.get("ev_to_ebitda") not in {None, ""} or row.get("trailing_pe") not in {None, ""}
    ]
    checks["peer_multiples"] = _pass(bool(peers_with_multiples), {"peers": len(peers.get("peers", [])), "peers_with_multiples": len(peers_with_multiples)})

    insider = read_json(root / "data" / "capital_signals" / "insider_forms.json", {"forms": []}) or {"forms": []}
    holders = read_json(root / "data" / "capital_signals" / "institutional_holders.json", {"holders": []}) or {"holders": []}
    investor_views = read_json(root / "semi_public" / "investor_views" / "investor_views_index.json", {"items": []}) or {"items": []}
    checks["insider_forms"] = _pass(bool(insider.get("forms")), {"count": len(insider.get("forms", []))})
    checks["institutional_holders"] = _pass(bool(holders.get("holders")), {"count": len(holders.get("holders", [])), "note": holders.get("note")})
    holder_density = _row_density(holders.get("holders", []), ["holder", "date_reported", "shares", "source_url"])
    checks["institutional_holder_density"] = _pass(
        holder_density["rows"] >= 10 and holder_density["density"] >= 0.80,
        {**holder_density, "minimum_required_rows": 10, "minimum_density": 0.80},
    )
    checks["investor_views_sources"] = _pass(
        bool(investor_views.get("items")) or bool(investor_views.get("queries")),
        {"count": len(investor_views.get("items", [])), "queries": investor_views.get("queries", [])},
    )

    books = read_json(root / "processed" / "books" / "company_books.json", {"books": [], "query_log": []}) or {"books": [], "query_log": []}
    raw_book_candidates = books.get("raw_candidates", [])
    books_pass = bool(books.get("books")) or (books.get("status") == "none_found" and bool(raw_book_candidates or books.get("query_log")))
    checks["books"] = _pass(books_pass, {"count": len(books.get("books", [])), "raw_candidates": len(raw_book_candidates), "status": books.get("status")})
    if not raw_book_candidates:
        warnings.append("books_raw_candidates_not_retained")

    semi_status_files = list((root / "semi_public").glob("*/_collection_status.json"))
    semi_source_files = [
        path
        for path in (root / "semi_public").glob("*/*")
        if path.is_file() and not path.name.startswith("_") and path.name not in {"investor_views_index.json", "investor_views_index.md"}
    ]
    checks["semi_public_scaffold"] = _pass(len(semi_status_files) >= 8, {"status_files": len(semi_status_files)})
    checks["semi_public_fetched_sources"] = _pass(
        bool(semi_source_files) or checks["semi_public_scaffold"].get("passed"),
        {"source_files": len(semi_source_files), "scaffold_only": not bool(semi_source_files)},
    )
    if not semi_source_files:
        warnings.append("semi_public_scaffold_only_no_original_sources_fetched")

    if model_validation is None:
        model_validation = read_json(root / "models" / datetime.now().strftime("%Y-%m-%d") / "model_validation.json", {}) or {}
    checks["model_validation"] = _pass(model_validation.get("status") == "pass", {"status": model_validation.get("status"), "gaps": model_validation.get("gaps", [])})

    for name, check in checks.items():
        if not check.get("passed"):
            gaps.append(name)
    status = "pass" if not gaps else "needs_review"
    audit = {
        "company": target.company_name,
        "ticker": target.ticker,
        "status": status,
        "checks": checks,
        "gaps": gaps,
        "warnings": warnings,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    write_json(root / "metadata" / "data_quality_audit.json", audit)
    gap_lines = [f"- {gap}" for gap in gaps] or ["- none"]
    warning_lines = [f"- {warning}" for warning in warnings] or ["- none"]
    write_markdown(
        root / "metadata" / "data_quality_audit.md",
        [
            f"# {target.company_name} Data Quality Audit",
            "",
            f"- Status: {status}",
            "",
            "## Gaps",
            *gap_lines,
            "",
            "## Warnings",
            *warning_lines,
        ],
    )
    return audit
