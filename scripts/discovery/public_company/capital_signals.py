"""Capital-market signals: insider forms, holder data, investor-view scaffolds."""

from __future__ import annotations

import time
from datetime import datetime
import json
import re
import subprocess
from html import unescape
from typing import Any

import requests

from .common import PublicCompanyTarget, read_json, write_csv, write_json, write_markdown, write_probe_report


NASDAQ_HEADERS = {
    "User-Agent": "Mozilla/5.0 AIOrgResearchBot/1.0",
    "Accept": "application/json",
    "Origin": "https://www.nasdaq.com",
    "Referer": "https://www.nasdaq.com/",
}


def _fetch_nasdaq_institutional_holders(ticker: str, limit: int = 25) -> dict[str, Any]:
    url = f"https://api.nasdaq.com/api/company/{ticker.upper()}/institutional-holdings"
    last_error: Exception | None = None
    for attempt in range(2):
        try:
            response = requests.get(url, params={"limit": limit, "offset": 0, "type": "TOTAL"}, headers=NASDAQ_HEADERS, timeout=8)
            response.raise_for_status()
            break
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(1 + attempt)
    else:
        raise RuntimeError(str(last_error))
    payload = response.json()
    data = payload.get("data") or {}
    table = ((data.get("holdingsTransactions") or {}).get("table") or {})
    rows = []
    for row in table.get("rows", []) or []:
        rows.append(
            {
                "holder": row.get("ownerName"),
                "date_reported": row.get("date"),
                "shares": row.get("sharesHeld"),
                "shares_change": row.get("sharesChange"),
                "shares_change_percent": row.get("sharesChangePCT"),
                "market_value_000s": row.get("marketValue"),
                "source_url": "https://www.nasdaq.com/market-activity/stocks/{ticker}/institutional-holdings".format(ticker=ticker.lower()),
                "source": "nasdaq_institutional_holdings_api",
            }
        )
    return {
        "source": "nasdaq_institutional_holdings_api",
        "source_url": "https://www.nasdaq.com/market-activity/stocks/{ticker}/institutional-holdings".format(ticker=ticker.lower()),
        "summary": data.get("ownershipSummary") or {},
        "active_positions": data.get("activePositions") or {},
        "new_sold_out_positions": data.get("newSoldOutPositions") or {},
        "holders": rows,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }


def _fetch_nasdaq_with_curl(ticker: str, limit: int = 25) -> dict[str, Any]:
    url = f"https://api.nasdaq.com/api/company/{ticker.upper()}/institutional-holdings?limit={limit}&offset=0&type=TOTAL"
    command = [
        "curl",
        "--http1.1",
        "--retry",
        "3",
        "--retry-delay",
        "1",
        "--max-time",
        "15",
        "-sS",
        "-H",
        "User-Agent: Mozilla/5.0",
        "-H",
        "Accept: application/json",
        "-H",
        "Origin: https://www.nasdaq.com",
        "-H",
        "Referer: https://www.nasdaq.com/",
        url,
    ]
    output = subprocess.check_output(command, text=True, timeout=20)
    payload = json.loads(output)
    data = payload.get("data") or {}
    table = ((data.get("holdingsTransactions") or {}).get("table") or {})
    rows = []
    for row in table.get("rows", []) or []:
        rows.append(
            {
                "holder": row.get("ownerName"),
                "date_reported": row.get("date"),
                "shares": row.get("sharesHeld"),
                "shares_change": row.get("sharesChange"),
                "shares_change_percent": row.get("sharesChangePCT"),
                "market_value_000s": row.get("marketValue"),
                "source_url": "https://www.nasdaq.com/market-activity/stocks/{ticker}/institutional-holdings".format(ticker=ticker.lower()),
                "source": "nasdaq_institutional_holdings_api_curl",
            }
        )
    return {
        "source": "nasdaq_institutional_holdings_api_curl",
        "source_url": "https://www.nasdaq.com/market-activity/stocks/{ticker}/institutional-holdings".format(ticker=ticker.lower()),
        "summary": data.get("ownershipSummary") or {},
        "active_positions": data.get("activePositions") or {},
        "new_sold_out_positions": data.get("newSoldOutPositions") or {},
        "holders": rows,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }


def _clean_html_cell(value: str) -> str:
    text = re.sub(r"(?is)<.*?>", " ", value)
    return re.sub(r"\s+", " ", unescape(text)).replace("\xa0", " ").strip()


def _fetch_holdingschannel_holders(ticker: str, limit: int = 25) -> dict[str, Any]:
    url = f"https://www.holdingschannel.com/bystock/?symbol={ticker.upper()}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 AIOrgResearchBot/1.0"}, timeout=20)
    response.raise_for_status()
    table_match = re.search(r'(?is)<table[^>]+id=["\']hldtable["\'][^>]*>(.*?)</table>', response.text)
    if not table_match:
        raise RuntimeError("holdingschannel_hldtable_not_found")
    rows: list[dict[str, Any]] = []
    for row_html in re.findall(r'(?is)<tr[^>]+class=["\']mainrow["\'][^>]*>(.*?)</tr>', table_match.group(1)):
        cells = re.findall(r"(?is)<td[^>]*>(.*?)</td>", row_html)
        if len(cells) < 4:
            continue
        holder = _clean_html_cell(cells[0])
        holder = re.sub(r"(?i)^expandrow\([^)]*\);\s*", "", holder).strip()
        rows.append(
            {
                "holder": holder,
                "date_reported": _clean_html_cell(cells[3]),
                "shares": _clean_html_cell(cells[1]),
                "shares_change": None,
                "shares_change_percent": None,
                "market_value_000s": _clean_html_cell(cells[2]),
                "source_url": url,
                "source": "holdingschannel_13f_aggregate_page",
            }
        )
        if len(rows) >= limit:
            break
    if not rows:
        raise RuntimeError("holdingschannel_no_holder_rows")
    return {
        "source": "holdingschannel_13f_aggregate_page",
        "source_url": url,
        "summary": {},
        "holders": rows,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }


def _fetch_institutional_holders_with_fallbacks(ticker: str) -> dict[str, Any]:
    errors: list[dict[str, str]] = []
    for source_name, fetcher in [
        ("nasdaq_requests", _fetch_nasdaq_institutional_holders),
        ("nasdaq_curl_http1", _fetch_nasdaq_with_curl),
        ("holdingschannel", _fetch_holdingschannel_holders),
    ]:
        try:
            payload = fetcher(ticker)
            payload["fallback_chain"] = {"selected": source_name, "errors": errors}
            if payload.get("holders"):
                return payload
            errors.append({"source": source_name, "error": "empty_holders"})
        except Exception as exc:  # noqa: BLE001
            errors.append({"source": source_name, "error": str(exc)})
    raise RuntimeError(json.dumps(errors, ensure_ascii=False))


def collect_capital_signals(target: PublicCompanyTarget) -> dict[str, Any]:
    root = target.public_company_root
    data_dir = root / "data" / "capital_signals"
    views_dir = root / "semi_public" / "investor_views"
    status: dict[str, Any] = {"status": "partial", "items": [], "gaps": []}

    submissions_path = root / "metadata" / "sec_submissions.json"
    insider_rows: list[dict[str, Any]] = []
    if submissions_path.exists():
        import json

        submissions = json.loads(submissions_path.read_text(encoding="utf-8"))
        recent = submissions.get("filings", {}).get("recent", {})
        for idx, form in enumerate(recent.get("form", [])):
            if str(form).upper() not in {"3", "4", "5"}:
                continue
            insider_rows.append(
                {
                    "form": form,
                    "filing_date": recent.get("filingDate", [""])[idx],
                    "accession": recent.get("accessionNumber", [""])[idx],
                    "description": recent.get("primaryDocDescription", [""])[idx],
                    "primary_document": recent.get("primaryDocument", [""])[idx],
                    "source": "sec_submissions",
                }
            )
    write_json(data_dir / "insider_forms.json", {"forms": insider_rows, "updated_at": datetime.now().isoformat(timespec="seconds")})
    write_csv(data_dir / "insider_forms.csv", insider_rows, ["form", "filing_date", "accession", "description", "primary_document", "source"])
    status["items"].append({"type": "insider_forms", "count": len(insider_rows)})
    if not insider_rows:
        status["gaps"].append({"reason": "no_recent_form_3_4_5_in_sec_recent_filings"})

    holder_payload: dict[str, Any]
    try:
        holder_payload = _fetch_institutional_holders_with_fallbacks(target.ticker)
        status["items"].append({"type": "institutional_holders", "count": len(holder_payload.get("holders", [])), "source": holder_payload.get("source_url")})
    except Exception as exc:  # noqa: BLE001
        cached = read_json(data_dir / "institutional_holders.json", {}) or {}
        if cached.get("holders"):
            holder_payload = {
                **cached,
                "source": f"{cached.get('source', 'unknown')}_cached",
                "cache_reused_at": datetime.now().isoformat(timespec="seconds"),
                "cache_reuse_reason": str(exc),
            }
            status["items"].append({"type": "institutional_holders_cached", "count": len(holder_payload.get("holders", [])), "source": holder_payload.get("source_url")})
        else:
            holder_payload = {
                "source": "deferred",
                "updated_at": datetime.now().isoformat(timespec="seconds"),
                "holders": [],
                "note": "Institutional-holder fetch failed after free fallbacks; ask for a paid holder-data API if this gap remains important.",
                "error": str(exc),
            }
            status["gaps"].append({"reason": "institutional_holders_fetch_failed", "error": str(exc), "paid_api_next": True})
    write_json(data_dir / "institutional_holders.json", holder_payload)
    write_csv(
        data_dir / "institutional_holders.csv",
        holder_payload.get("holders", []),
        ["holder", "date_reported", "shares", "shares_change", "shares_change_percent", "market_value_000s", "source_url", "source"],
    )

    investor_queries = [
        f'{target.ticker} 13F holders',
        f'{target.company_name} institutional ownership',
        f'{target.company_name} investor letter',
        f'{target.ticker} hedge fund position',
        f'{target.company_name} short seller report',
    ]
    views = {
        "company": target.company_name,
        "ticker": target.ticker,
        "source_types": [
            "sec_form_13f",
            "institutional_ownership_page",
            "public_fund_letter",
            "public_interview",
            "substack_or_investor_blog",
            "short_seller_report",
        ],
        "queries": investor_queries,
        "items": [
            {
                "type": "institutional_ownership_page",
                "source": holder_payload.get("source"),
                "source_url": holder_payload.get("source_url"),
                "holders": len(holder_payload.get("holders", [])),
            }
        ]
        if holder_payload.get("holders")
        else [],
        "status": "query_index_created",
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    write_json(views_dir / "investor_views_index.json", views)
    write_markdown(
        views_dir / "investor_views_index.md",
        [
            f"# {target.company_name} Investor Views",
            "",
            "Best effort index. Treat these as leads until original filings, fund letters, or interviews are fetched.",
            "",
            "## Queries",
            *[f"- {query}" for query in investor_queries],
            "",
            "## Current Data",
            f"- SEC insider forms: {len(insider_rows)}",
            f"- Nasdaq institutional holder rows: {len(holder_payload.get('holders', []))}",
        ],
    )
    status["items"].append({"type": "investor_views_index", "count": len(investor_queries)})
    status["status"] = "ok" if status["items"] else "gap"
    write_probe_report(target, "capital_signals", status)
    return status
