"""Market data and valuation collection using lightweight Yahoo chart JSON."""

from __future__ import annotations

import re
from datetime import datetime
from html import unescape
from typing import Any

import requests

from .common import PublicCompanyTarget, read_json, write_csv, write_json, write_probe_report


HEADERS = {"User-Agent": "Mozilla/5.0 AIOrgResearchBot/1.0"}


def normalize_yahoo_ticker(target: PublicCompanyTarget) -> str:
    ticker = target.ticker
    if target.market == "HK" and not ticker.endswith(".HK"):
        return f"{ticker.zfill(4)}.HK" if ticker.isdigit() else f"{ticker}.HK"
    if target.market == "CN" and ticker.isdigit():
        return f"{ticker}.SS" if ticker.startswith("6") else f"{ticker}.SZ"
    return ticker


def _chart(ticker: str, range_value: str = "max") -> dict[str, Any]:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    response = requests.get(
        url,
        params={"range": range_value, "interval": "1d", "events": "div,splits"},
        headers=HEADERS,
        timeout=15,
    )
    response.raise_for_status()
    payload = response.json()
    error = payload.get("chart", {}).get("error")
    if error:
        raise RuntimeError(error)
    result = (payload.get("chart", {}).get("result") or [None])[0]
    if not result:
        raise RuntimeError("empty chart result")
    return result


def _history_rows(chart: dict[str, Any]) -> list[dict[str, Any]]:
    timestamps = chart.get("timestamp") or []
    quote = (chart.get("indicators", {}).get("quote") or [{}])[0]
    adjclose = ((chart.get("indicators", {}).get("adjclose") or [{}])[0]).get("adjclose", [])
    rows: list[dict[str, Any]] = []
    for idx, timestamp in enumerate(timestamps):
        rows.append(
            {
                "date": datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d"),
                "open": _list_get(quote.get("open"), idx),
                "high": _list_get(quote.get("high"), idx),
                "low": _list_get(quote.get("low"), idx),
                "close": _list_get(quote.get("close"), idx),
                "adj_close": _list_get(adjclose, idx),
                "volume": _list_get(quote.get("volume"), idx),
            }
        )
    return rows


def _list_get(values: Any, idx: int) -> Any:
    if not isinstance(values, list) or idx >= len(values):
        return None
    return values[idx]


def _latest_annual(target: PublicCompanyTarget) -> dict[str, Any]:
    annual = read_json(target.public_company_root / "data" / "statements" / "annual_statements.json", {"periods": []}) or {"periods": []}
    periods = annual.get("periods") or []
    return periods[-1] if periods else {}


def _stockanalysis_url(ticker: str) -> str:
    return f"https://stockanalysis.com/stocks/{ticker.lower()}/statistics/"


def _scaled_number(text: str) -> float | None:
    clean = text.strip().replace(",", "").replace("$", "")
    match = re.match(r"(?i)^(-?\d+(?:\.\d+)?)\s*([KMBT])?$", clean)
    if not match:
        return None
    value = float(match.group(1))
    multiplier = {"K": 1_000, "M": 1_000_000, "B": 1_000_000_000, "T": 1_000_000_000_000}.get((match.group(2) or "").upper(), 1)
    return value * multiplier


def _label_number(text: str, label: str) -> float | None:
    pattern = re.compile(rf"{re.escape(label)}\s+(n/a|-?\$?\d+(?:\.\d+)?\s*[KMBT]?)", re.IGNORECASE)
    match = pattern.search(text)
    if not match or match.group(1).lower() == "n/a":
        return None
    return _scaled_number(match.group(1))


def _stockanalysis_statistics(ticker: str) -> dict[str, Any]:
    url = _stockanalysis_url(ticker)
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    stripped = unescape(re.sub(r"<[^>]+>", " ", response.text))
    text = re.sub(r"\s+", " ", stripped)
    market_cap = None
    enterprise_value = None
    market_cap_match = re.search(r"market cap or net worth of \$([\d.]+)\s+(million|billion|trillion)", text, re.IGNORECASE)
    if market_cap_match:
        market_cap = _scaled_number(f"{market_cap_match.group(1)}{market_cap_match.group(2)[0].upper()}")
    ev_match = re.search(r"enterprise value is \$([\d.]+)\s+(million|billion|trillion)", text, re.IGNORECASE)
    if ev_match:
        enterprise_value = _scaled_number(f"{ev_match.group(1)}{ev_match.group(2)[0].upper()}")
    return {
        "ticker": ticker.upper(),
        "source": "stockanalysis_statistics_page",
        "source_url": url,
        "market_cap": market_cap,
        "enterprise_value": enterprise_value,
        "shares_outstanding": _label_number(text, "Shares Outstanding"),
        "trailing_pe": _label_number(text, "PE Ratio"),
        "forward_pe": _label_number(text, "Forward PE"),
        "price_to_sales": _label_number(text, "PS Ratio"),
        "forward_price_to_sales": _label_number(text, "Forward PS"),
        "ev_to_ebitda": _label_number(text, "EV / EBITDA"),
        "total_debt": _label_number(text, "Total Debt"),
    }


def fetch_market_data(target: PublicCompanyTarget, period: str = "max") -> dict[str, Any]:
    root = target.public_company_root
    data_dir = root / "data" / "market_data"
    valuation_dir = root / "data" / "valuation"
    status: dict[str, Any] = {"status": "partial", "items": [], "gaps": []}
    yahoo_ticker = normalize_yahoo_ticker(target)

    chart = None
    try:
        chart = _chart(yahoo_ticker, period)
        rows = _history_rows(chart)
        if rows:
            write_csv(data_dir / "price_history.csv", rows, ["date", "open", "high", "low", "close", "adj_close", "volume"])
            status["items"].append({"type": "price_history", "rows": len(rows), "path": str(data_dir / "price_history.csv")})
        else:
            status["gaps"].append({"reason": "empty_price_history", "ticker": yahoo_ticker})
    except Exception as exc:  # noqa: BLE001
        status["gaps"].append({"reason": "price_history_failed", "ticker": yahoo_ticker, "error": str(exc)})

    latest = _latest_annual(target)
    meta = (chart or {}).get("meta", {})
    last_price = meta.get("regularMarketPrice") or meta.get("chartPreviousClose")
    shares = latest.get("shares_outstanding")
    market_cap = None
    if isinstance(last_price, (int, float)) and isinstance(shares, (int, float)):
        market_cap = float(last_price) * float(shares)
    debt = latest.get("debt") or 0
    cash = latest.get("cash") or 0
    enterprise_value = market_cap + float(debt or 0) - float(cash or 0) if market_cap is not None else None
    statistics = None
    if target.market == "US":
        try:
            statistics = _stockanalysis_statistics(target.ticker)
            market_cap = statistics.get("market_cap") or market_cap
            enterprise_value = statistics.get("enterprise_value") or enterprise_value
            shares = statistics.get("shares_outstanding") or shares
            status["items"].append({"type": "valuation_statistics", "source": statistics.get("source_url")})
        except Exception as exc:  # noqa: BLE001
            status["gaps"].append({"reason": "stockanalysis_statistics_failed", "ticker": target.ticker, "error": str(exc)})
    market_cap_source = "stockanalysis_statistics_page" if statistics and statistics.get("market_cap") else "computed_from_weighted_average_diluted_shares"
    shares_source = "stockanalysis_statistics_page" if statistics and statistics.get("shares_outstanding") else "data/statements/annual_statements.json"
    snapshot = {
        "ticker": yahoo_ticker,
        "source": "yahoo_chart_json + stockanalysis_statistics_page + sec_companyfacts",
        "market_cap_source": market_cap_source,
        "market_cap_confidence": "medium" if market_cap_source == "stockanalysis_statistics_page" else "low" if market_cap is not None else "missing",
        "currency": meta.get("currency"),
        "exchange": meta.get("fullExchangeName") or meta.get("exchangeName"),
        "last_price": last_price,
        "regular_market_time": meta.get("regularMarketTime"),
        "year_high": meta.get("fiftyTwoWeekHigh"),
        "year_low": meta.get("fiftyTwoWeekLow"),
        "shares_outstanding_source": shares_source,
        "shares_outstanding": shares,
        "market_cap": market_cap,
        "enterprise_value": enterprise_value,
        "price_to_sales": statistics.get("price_to_sales") if statistics else None,
        "ev_to_ebitda": statistics.get("ev_to_ebitda") if statistics else None,
        "trailing_pe": statistics.get("trailing_pe") if statistics else None,
        "source_urls": [statistics["source_url"]] if statistics and statistics.get("source_url") else [],
        "cash": cash,
        "debt": debt,
        "valuation_note": "StockAnalysis statistics are used as a medium-confidence public fallback when unauthenticated Yahoo quote fields are unavailable; SEC statement fields remain canonical for financial statements.",
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    write_json(valuation_dir / "valuation_snapshot.json", snapshot)
    status["items"].append({"type": "valuation_snapshot", "path": str(valuation_dir / "valuation_snapshot.json")})
    if market_cap is None:
        status["gaps"].append({"reason": "market_cap_not_computed", "details": "missing last price or SEC shares_outstanding"})

    peers = []
    for peer in target.peer_tickers:
        try:
            peer_chart = _chart(peer, "1mo")
            peer_meta = peer_chart.get("meta", {})
            peer_stats = None
            if re.match(r"^[A-Z.]+$", peer):
                try:
                    peer_stats = _stockanalysis_statistics(peer)
                except Exception as exc:  # noqa: BLE001
                    peer_stats = {"error": str(exc)}
            peers.append(
                {
                    "ticker": peer,
                    "currency": peer_meta.get("currency"),
                    "exchange": peer_meta.get("fullExchangeName") or peer_meta.get("exchangeName"),
                    "last_price": peer_meta.get("regularMarketPrice") or peer_meta.get("chartPreviousClose"),
                    "year_high": peer_meta.get("fiftyTwoWeekHigh"),
                    "year_low": peer_meta.get("fiftyTwoWeekLow"),
                    "market_cap": peer_stats.get("market_cap") if peer_stats else None,
                    "enterprise_value": peer_stats.get("enterprise_value") if peer_stats else None,
                    "trailing_pe": peer_stats.get("trailing_pe") if peer_stats else None,
                    "price_to_sales": peer_stats.get("price_to_sales") if peer_stats else None,
                    "ev_to_ebitda": peer_stats.get("ev_to_ebitda") if peer_stats else None,
                    "source": "yahoo_chart_json + stockanalysis_statistics_page" if peer_stats and not peer_stats.get("error") else "yahoo_chart_json",
                    "source_url": peer_stats.get("source_url") if peer_stats else None,
                    "gap": peer_stats.get("error") if peer_stats and peer_stats.get("error") else None,
                }
            )
        except Exception as exc:  # noqa: BLE001
            peers.append({"ticker": peer, "error": str(exc), "source": "yahoo_chart_json"})
    if peers:
        write_json(valuation_dir / "peer_valuation.json", {"peers": peers, "updated_at": datetime.now().isoformat(timespec="seconds")})
        status["items"].append({"type": "peer_valuation", "count": len(peers), "path": str(valuation_dir / "peer_valuation.json")})

    status["status"] = "ok" if status["items"] else "gap"
    write_probe_report(target, "market_data", status)
    return status
