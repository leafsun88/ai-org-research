"""SEC EDGAR collection for US-listed companies."""

from __future__ import annotations

import html
import os
import re
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests

from .common import (
    PROJECT_ROOT,
    PublicCompanyTarget,
    record_extraction_gap,
    relative_to_project,
    safe_filename,
    write_csv,
    write_json,
    write_markdown,
    write_probe_report,
)


SEC_DATA = "https://data.sec.gov"
SEC_ARCHIVES = "https://www.sec.gov/Archives/edgar/data"
SEC_USER_AGENT = os.environ.get("SEC_USER_AGENT", "AIOrgResearchBot leafsun@example.com")
SEC_HEADERS = {"User-Agent": SEC_USER_AGENT, "Accept-Encoding": "gzip, deflate"}

ANNUAL_FORMS = {"10-K", "10-K/A", "20-F", "20-F/A", "40-F", "40-F/A", "ARS", "AR"}
QUARTERLY_FORMS = {"10-Q", "10-Q/A", "6-K", "6-K/A"}
PROSPECTUS_FORMS = {"S-1", "S-1/A", "F-1", "F-1/A", "424B", "424B1", "424B2", "424B3", "424B4", "424B5", "424B7"}
GOVERNANCE_FORMS = {"DEF 14A", "DEFA14A", "PRE 14A", "8-A12B", "3", "4", "5", "SC 13D", "SC 13G"}

METRIC_TAGS = {
    "revenue": ["RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "Revenues"],
    "gross_profit": ["GrossProfit"],
    "operating_income": ["OperatingIncomeLoss", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"],
    "net_income": ["NetIncomeLoss", "ProfitLoss"],
    "operating_cash_flow": ["NetCashProvidedByUsedInOperatingActivities"],
    "capital_expenditures": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
    "cash": ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"],
    "assets": ["Assets"],
    "liabilities": ["Liabilities"],
    "stockholders_equity": ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
    "debt_current": ["ShortTermBorrowings", "LongTermDebtCurrent", "FinanceLeaseLiabilityCurrent"],
    "debt_noncurrent": ["LongTermDebtNoncurrent", "LongTermDebtAndFinanceLeaseObligationsNoncurrent"],
    "shares_outstanding": ["WeightedAverageNumberOfDilutedSharesOutstanding", "CommonStocksIncludingAdditionalPaidInCapitalMember"],
}


def sec_get_json(url: str) -> dict[str, Any]:
    response = requests.get(url, headers=SEC_HEADERS, timeout=30)
    response.raise_for_status()
    time.sleep(0.12)
    return response.json()


def sec_get_bytes(url: str) -> bytes:
    response = requests.get(url, headers={**SEC_HEADERS, "Accept": "*/*"}, timeout=45)
    response.raise_for_status()
    time.sleep(0.12)
    return response.content


def resolve_cik(ticker: str) -> str:
    tickers = sec_get_json("https://www.sec.gov/files/company_tickers.json")
    upper = ticker.upper()
    for item in tickers.values():
        if str(item.get("ticker", "")).upper() == upper:
            return str(item["cik_str"]).zfill(10)
    raise KeyError(f"Ticker not found in SEC company_tickers.json: {ticker}")


def classify_filing(form: str, description: str = "") -> str:
    form = str(form or "").upper().strip()
    description_l = str(description or "").lower()
    if form in ANNUAL_FORMS:
        return "annual_reports"
    if form in {"10-Q", "10-Q/A"}:
        return "quarterly_reports"
    if form in PROSPECTUS_FORMS or form.startswith("424B"):
        return "prospectus"
    if form in GOVERNANCE_FORMS or form.startswith("SC 13"):
        return "governance"
    if form in {"8-K", "8-K/A"}:
        if any(term in description_l for term in ["results", "operations", "earnings", "financial statements", "item 2.02"]):
            return "earnings_calls"
        return "material_events"
    if form in {"6-K", "6-K/A"} and any(term in description_l for term in ["interim", "quarter", "results", "earnings"]):
        return "quarterly_reports"
    return "material_events"


def filing_url(cik: str, accession: str, primary_doc: str) -> str:
    cik_int = str(int(cik))
    accession_clean = accession.replace("-", "")
    return f"{SEC_ARCHIVES}/{cik_int}/{accession_clean}/{primary_doc}"


def fetch_sec_filings(target: PublicCompanyTarget, max_filings_per_type: int = 3) -> dict[str, Any]:
    root = target.public_company_root
    cik = target.cik or resolve_cik(target.ticker)
    target.cik = cik
    submissions = sec_get_json(f"{SEC_DATA}/submissions/CIK{cik}.json")
    companyfacts = sec_get_json(f"{SEC_DATA}/api/xbrl/companyfacts/CIK{cik}.json")
    metadata_root = root / "metadata"
    write_json(metadata_root / "sec_submissions.json", submissions)
    write_json(metadata_root / "sec_companyfacts.json", companyfacts)

    recent = submissions.get("filings", {}).get("recent", {})
    rows = []
    forms = recent.get("form", [])
    counters: dict[str, int] = defaultdict(int)
    allowed_categories = {"annual_reports", "quarterly_reports", "prospectus", "governance", "earnings_calls", "material_events"}
    downloaded: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []

    for idx, form in enumerate(forms):
        accession = recent.get("accessionNumber", [""])[idx]
        primary_doc = recent.get("primaryDocument", [""])[idx]
        description = recent.get("primaryDocDescription", [""])[idx] or recent.get("items", [""])[idx]
        category = classify_filing(form, description)
        if category not in allowed_categories:
            continue
        if counters[category] >= max_filings_per_type:
            continue
        if not accession or not primary_doc:
            continue
        counters[category] += 1
        url = filing_url(cik, accession, primary_doc)
        filing_date = recent.get("filingDate", [""])[idx]
        report_date = recent.get("reportDate", [""])[idx]
        suffix = Path(primary_doc).suffix or ".html"
        filename = safe_filename(f"{filing_date}_{form}_{accession}_{Path(primary_doc).stem}") + suffix
        local_path = root / "raw_filings" / category / filename
        row = {
            "form": form,
            "category": category,
            "filing_date": filing_date,
            "report_date": report_date,
            "accession": accession,
            "primary_document": primary_doc,
            "description": description,
            "source_url": url,
            "local_path": relative_to_project(local_path),
        }
        try:
            content = sec_get_bytes(url)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_bytes(content)
            row["bytes"] = len(content)
            downloaded.append(row)
        except Exception as exc:  # noqa: BLE001 - network status belongs in manifest
            row["error"] = str(exc)
            failures.append(row)
        rows.append(row)

    manifest = {
        "company": target.company_name,
        "ticker": target.ticker,
        "cik": cik,
        "status": "ok" if downloaded else "partial",
        "downloaded": downloaded,
        "failures": failures,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    write_json(metadata_root / "raw_manifest.json", manifest)
    write_probe_report(
        target,
        "sec_us",
        {"status": manifest["status"], "items": downloaded, "gaps": failures, "cik": cik},
        [
            f"# {target.company_name} SEC Probe",
            "",
            f"- CIK: `{cik}`",
            f"- Downloaded filings: {len(downloaded)}",
            f"- Failures: {len(failures)}",
            "",
            "## Downloaded",
            *[f"- {item['form']} {item.get('filing_date', '')}: `{item['local_path']}`" for item in downloaded[:20]],
        ],
    )
    return manifest


def html_to_text(raw: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", raw)
    text = re.sub(r"(?is)<br\s*/?>", "\n", text)
    text = re.sub(r"(?is)</p\s*>", "\n", text)
    text = re.sub(r"(?is)<.*?>", " ", text)
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s+", "\n", text)
    return text


def extract_mda_section(text: str) -> str:
    normalized = html_to_text(text)
    heading_pattern = re.compile(
        r"(?is)\bitem\s+7\.?\s+management['’]?\s*s?\s+discussion\s+and\s+analysis"
        r"\s+of\s+financial\s+condition\s+and\s+results\s+of\s+operations\b"
    )
    true_heading_candidates: list[str] = []
    for heading in heading_pattern.finditer(normalized):
        start = heading.start()
        intro_window = normalized[start : start + 2000].lower()
        following_pos = intro_window.find("following discussion and analysis")
        overview_pos = intro_window.find("results of operations overview")
        item7a_pos = intro_window.find("item 7a")
        marker_pos = following_pos if following_pos >= 0 else overview_pos
        if marker_pos < 0:
            continue
        if item7a_pos >= 0 and item7a_pos < marker_pos:
            continue
        end_search_start = start + marker_pos
        end_match = re.search(
            r"(?is)(?:\d+\s+)?table\s+of\s+contents\s+item\s+7a\.?\s+quantitative",
            normalized[end_search_start:],
        )
        if end_match:
            end = end_search_start + end_match.start()
        else:
            fallback = re.search(r"(?is)\bitem\s+7a\.?\s+quantitative", normalized[start + 1000 :])
            end = start + 1000 + fallback.start() if fallback else len(normalized)
        section = re.sub(r"\n{3,}", "\n\n", normalized[start:end]).strip()
        if section:
            true_heading_candidates.append(section)
    if true_heading_candidates:
        return max(true_heading_candidates, key=len)

    patterns = [
        re.compile(
            r"(?is)\bitem\s+7\.?\s+management['’]?\s*s?\s+discussion\s+and\s+analysis"
            r"(?P<body>.*?)"
            r"(?=\bitem\s+7a\.?|\bitem\s+8\.?)"
        ),
        re.compile(r"(?is)\bitem\s+7\.?\s*(?P<body>.*?)(?=\bitem\s+7a\.?|\bitem\s+8\.?)"),
    ]
    candidates: list[str] = []
    for pattern in patterns:
        for match in pattern.finditer(normalized):
            section = re.sub(r"\n{3,}", "\n\n", match.group(0)).strip()
            if section:
                candidates.append(section)
    if not candidates:
        return ""
    return max(candidates, key=len)


def extract_mda_from_filings(target: PublicCompanyTarget) -> dict[str, Any]:
    root = target.public_company_root
    manifest = {}
    manifest_path = root / "metadata" / "raw_manifest.json"
    if manifest_path.exists():
        manifest = manifest_path.read_text(encoding="utf-8")
        try:
            import json

            manifest = json.loads(manifest)
        except Exception:
            manifest = {}
    annuals = [item for item in (manifest.get("downloaded", []) if isinstance(manifest, dict) else []) if item.get("category") == "annual_reports"]
    items: list[dict[str, Any]] = []
    gaps: list[dict[str, Any]] = []
    if not annuals:
        annuals = [
            {"local_path": relative_to_project(path), "filing_date": path.name[:10], "form": "10-K"}
            for path in sorted((root / "raw_filings" / "annual_reports").glob("*"))
        ]
    for item in annuals:
        local = Path(item["local_path"])
        path = local if local.is_absolute() else PROJECT_ROOT / local
        if not path.exists():
            path = root / "raw_filings" / "annual_reports" / Path(item["local_path"]).name
        try:
            raw = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:  # noqa: BLE001
            gaps.append({"file": str(path), "reason": f"read_failed: {exc}"})
            continue
        section = extract_mda_section(raw)
        if not section:
            gap = {"file": relative_to_project(path), "reason": "mda_section_not_found"}
            gaps.append(gap)
            record_extraction_gap(target, gap)
            continue
        year = (item.get("report_date") or item.get("filing_date") or path.name[:10] or "unknown")[:4]
        out = root / "processed" / "mda" / f"{year}_{safe_filename(item.get('form', '10-K'))}_mda.md"
        lines = [
            "---",
            f"company: {target.company_name}",
            f"ticker: {target.ticker}",
            f"source_file: {relative_to_project(path)}",
            f"source_url: {item.get('source_url', '')}",
            f"filing_date: {item.get('filing_date', '')}",
            f"report_date: {item.get('report_date', '')}",
            "type: mda_extract",
            "---",
            "",
            f"# {target.company_name} MD&A Extract ({year})",
            "",
            section,
        ]
        write_markdown(out, lines)
        items.append({"year": year, "source": relative_to_project(path), "output": relative_to_project(out), "characters": len(section)})
    status = {"status": "ok" if items else "gap", "items": items, "gaps": gaps}
    write_probe_report(target, "mda_extraction", status)
    return status


def _facts_for_tag(companyfacts: dict[str, Any], tag: str) -> list[dict[str, Any]]:
    fact = companyfacts.get("facts", {}).get("us-gaap", {}).get(tag)
    if not fact:
        return []
    units = fact.get("units", {})
    values: list[dict[str, Any]] = []
    for unit_key in ["USD", "shares", "USD/shares", "pure"]:
        values.extend(units.get(unit_key, []))
    if not values:
        for unit_values in units.values():
            values.extend(unit_values)
    return values


def _date_value(value: Any) -> int:
    text = str(value or "")
    digits = re.sub(r"\D", "", text)
    return int(digits[:8]) if len(digits) >= 8 else 0


def _duration_days(fact: dict[str, Any]) -> int | None:
    start = str(fact.get("start") or "")
    end = str(fact.get("end") or "")
    if not start or not end:
        return None
    try:
        return (datetime.fromisoformat(end) - datetime.fromisoformat(start)).days
    except ValueError:
        return None


def _is_duration_metric(metric: str) -> bool:
    return metric in {
        "revenue",
        "gross_profit",
        "operating_income",
        "net_income",
        "operating_cash_flow",
        "capital_expenditures",
        "shares_outstanding",
    }


def _fact_score(metric: str, period_type: str, fact: dict[str, Any], tag_index: int) -> tuple[Any, ...]:
    end_value = _date_value(fact.get("end"))
    filed_value = _date_value(fact.get("filed"))
    frame = str(fact.get("frame") or "")
    duration = _duration_days(fact)
    tag_preference = -tag_index
    if period_type == "quarterly" and _is_duration_metric(metric):
        is_calendar_quarter = bool(re.search(r"CY\d{4}Q[1-4]$", frame))
        is_short_duration = duration is not None and duration <= 125
        duration_closeness = -(abs(duration - 91) if duration is not None else 9999)
        return (is_calendar_quarter, is_short_duration, end_value, filed_value, duration_closeness, tag_preference)
    return (end_value, filed_value, tag_preference)


def _prepare_fact_value(metric: str, value: Any) -> Any:
    if metric == "capital_expenditures" and isinstance(value, (int, float)) and value > 0:
        return -value
    return value


def _period_identity(period_type: str, fy: str, fp: str, fact: dict[str, Any]) -> tuple[str, str, str]:
    if period_type == "annual":
        end = str(fact.get("end") or "")
        period_year = end[:4] if re.match(r"^\d{4}-\d{2}-\d{2}$", end) else fy
        return period_year, "FY", period_year
    return fy, fp, f"{fy}-{fp}"


def parse_companyfacts_to_statements(target: PublicCompanyTarget) -> dict[str, Any]:
    root = target.public_company_root
    companyfacts_path = root / "metadata" / "sec_companyfacts.json"
    if not companyfacts_path.exists():
        gap = {"reason": "sec_companyfacts_missing"}
        record_extraction_gap(target, gap)
        return {"status": "gap", "gaps": [gap]}
    import json

    companyfacts = json.loads(companyfacts_path.read_text(encoding="utf-8"))
    records: dict[tuple[str, str, str], dict[str, Any]] = {}
    source_map: dict[str, Any] = {}
    candidates: dict[tuple[str, str, str, str], list[dict[str, Any]]] = defaultdict(list)
    expected_annual_income_years: set[str] = set()

    for metric, tags in METRIC_TAGS.items():
        for tag_index, tag in enumerate(tags):
            for fact in _facts_for_tag(companyfacts, tag):
                form = str(fact.get("form") or "")
                fp = str(fact.get("fp") or "")
                fy = str(fact.get("fy") or "")
                if form not in {"10-K", "10-K/A", "10-Q", "10-Q/A", "20-F", "20-F/A"}:
                    continue
                if not fy or not fp:
                    continue
                period_type = "annual" if fp == "FY" or form in {"10-K", "10-K/A", "20-F", "20-F/A"} else "quarterly"
                period_year, period_fp, period = _period_identity(period_type, fy, fp, fact)
                if period_type == "annual" and metric in {"revenue", "operating_income", "net_income"} and period_year:
                    expected_annual_income_years.add(period_year)
                key = (period_type, period_year, period_fp, metric)
                candidates[key].append({"tag": tag, "tag_index": tag_index, "fact": fact, "source_fy": fy, "source_fp": fp, "period": period})

    for (period_type, period_year, period_fp, metric), metric_candidates in candidates.items():
        selected = max(metric_candidates, key=lambda item: _fact_score(metric, period_type, item["fact"], item["tag_index"]))
        fact = selected["fact"]
        tag = selected["tag"]
        source_fy = selected["source_fy"]
        source_fp = selected["source_fp"]
        key = (period_type, period_year, period_fp)
        row = records.setdefault(
            key,
            {
                "period_type": period_type,
                "period": selected["period"],
                "fiscal_year": int(period_year) if str(period_year).isdigit() else period_year,
                "fiscal_period": period_fp,
                "form": fact.get("form"),
                "filed": fact.get("filed"),
                "end": fact.get("end"),
            },
        )
        row.setdefault("source_fiscal_years", [])
        row.setdefault("source_fiscal_periods", [])
        if source_fy not in row["source_fiscal_years"]:
            row["source_fiscal_years"].append(source_fy)
        if source_fp not in row["source_fiscal_periods"]:
            row["source_fiscal_periods"].append(source_fp)
        row["filed"] = max(str(row.get("filed") or ""), str(fact.get("filed") or ""))
        if _date_value(fact.get("end")) >= _date_value(row.get("end")):
            row["end"] = fact.get("end")
        row[metric] = _prepare_fact_value(metric, fact.get("val"))
        row[f"{metric}_tag"] = tag
        row[f"{metric}_filed"] = fact.get("filed")
        source_map.setdefault(metric, []).append(
            {
                "tag": tag,
                "form": fact.get("form"),
                "fy": source_fy,
                "fp": source_fp,
                "period": selected["period"],
                "filed": fact.get("filed"),
                "end": fact.get("end"),
                "frame": fact.get("frame"),
                "source": "sec_companyfacts.json",
                "selection_rule": "annual_by_actual_end_year_or_quarter_duration_preference",
            }
        )

    annual_all = sorted([row for row in records.values() if row["period_type"] == "annual"], key=lambda row: (str(row.get("end", "")), str(row.get("fiscal_year", ""))))
    annual_sparse_periods = [
        row
        for row in annual_all
        if row.get("revenue") in {None, ""} and not (row.get("assets") not in {None, ""} and row.get("liabilities") not in {None, ""})
    ]
    annual = [row for row in annual_all if row not in annual_sparse_periods]
    quarterly = sorted([row for row in records.values() if row["period_type"] == "quarterly"], key=lambda row: (str(row.get("fiscal_year", "")), str(row.get("fiscal_period", ""))))
    for row in annual + quarterly:
        debt = sum(float(row.get(key) or 0) for key in ["debt_current", "debt_noncurrent"])
        if debt:
            row["debt"] = debt

    statement_dir = root / "data" / "statements"
    coverage = {
        "expected_annual_income_years_from_companyfacts": sorted(expected_annual_income_years),
        "actual_annual_periods": [str(row.get("period")) for row in annual],
        "actual_quarterly_periods": [str(row.get("period")) for row in quarterly],
        "sparse_annual_periods_excluded_from_main_table": [
            {
                "period": row.get("period"),
                "end": row.get("end"),
                "present_metrics": [metric for metric in METRIC_TAGS if row.get(metric) not in {None, ""}],
            }
            for row in annual_sparse_periods
        ],
    }
    payload_annual = {"status": "ok" if annual else "gap", "periods": annual, "source_map": source_map, "coverage": coverage}
    payload_quarterly = {"status": "ok" if quarterly else "gap", "periods": quarterly, "source_map": source_map, "coverage": coverage}
    write_json(statement_dir / "annual_statements.json", payload_annual)
    write_json(statement_dir / "quarterly_statements.json", payload_quarterly)
    fieldnames = [
        "period_type",
        "period",
        "fiscal_year",
        "fiscal_period",
        "form",
        "filed",
        "end",
        "revenue",
        "gross_profit",
        "operating_income",
        "net_income",
        "operating_cash_flow",
        "capital_expenditures",
        "cash",
        "debt",
        "assets",
        "liabilities",
        "stockholders_equity",
        "shares_outstanding",
    ]
    write_csv(statement_dir / "annual_statements.csv", annual, fieldnames)
    write_csv(statement_dir / "quarterly_statements.csv", quarterly, fieldnames)
    status = {
        "status": "ok" if annual or quarterly else "gap",
        "annual_periods": len(annual),
        "quarterly_periods": len(quarterly),
        "coverage": coverage,
        "gaps": [] if annual else [{"reason": "no_annual_periods_from_companyfacts"}],
    }
    write_probe_report(target, "sec_companyfacts_statements", status)
    return status
