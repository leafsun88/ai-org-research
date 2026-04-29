#!/usr/bin/env python3
"""
collect_lite.py — 精简版数据采集
=================================
只跑4个核心模块（financials, xbrl, youtube, podcasts）+ CSV导出。
零token消耗（纯Python），每家公司约2-3分钟。

Usage:
    python3 scripts/collect_lite.py PLTR "Palantir Technologies"
    python3 scripts/collect_lite.py RBLX Roblox
    python3 scripts/collect_lite.py SPOT Spotify --podcast-limit 2
    python3 scripts/collect_lite.py AFRM Affirm --skip youtube
"""

import sys
import json
import time
import argparse
import traceback
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = Path(__file__).parent
VAULT_DIR = PROJECT_ROOT / "vault"
INDEX_PATH = VAULT_DIR / "_index.json"

sys.path.insert(0, str(SCRIPTS_DIR))


def load_slug(ticker: str) -> str:
    """Look up slug from _index.json ticker_map."""
    with open(INDEX_PATH) as f:
        index = json.load(f)
    slug = index.get("ticker_map", {}).get(ticker)
    if not slug:
        raise ValueError(f"Ticker {ticker} not found in _index.json. Run init_100_companies.py first.")
    return slug


def setup_dirs(discovery_dir: Path):
    """Create directory structure under discovery/."""
    for subdir in ["sources/youtube", "sources/podcasts", "sources/earnings", "signals"]:
        (discovery_dir / subdir).mkdir(parents=True, exist_ok=True)


def run_financials(ticker: str, discovery_dir: Path):
    """Run fetch_financials with output redirected to discovery_dir."""
    import fetch_financials as fm
    # Monkeypatch DB_DIR so fm writes to discovery_dir's parent
    # fm uses: DB_DIR / ticker → we want discovery_dir
    # So set DB_DIR = discovery_dir, and call with ticker=""... no, that's hacky.
    # Better: just call the low-level functions directly.

    import yfinance as yf
    import requests

    print(f"  📊 Fetching financials for {ticker}...")
    stock = yf.Ticker(ticker)
    info = stock.info or {}

    # Get FMP profile for CEO etc
    fmp_data = fm.fmp_profile(ticker)

    # Write profile.md
    profile_path = discovery_dir / "profile.md"
    with open(profile_path, "w") as f:
        f.write("---\n")
        f.write(f"ticker: {ticker}\n")
        f.write("credibility: S5\n")
        f.write("evidence: E3\n")
        f.write(f"updated: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("---\n\n")
        f.write(f"# {info.get('longName', ticker)} ({ticker})\n\n")

        f.write("## Company Overview\n\n")
        f.write(f"- **Sector**: {info.get('sector', 'N/A')}\n")
        f.write(f"- **Industry**: {info.get('industry', 'N/A')}\n")
        f.write(f"- **Country**: {info.get('country', 'N/A')}\n")
        f.write(f"- **Website**: {info.get('website', 'N/A')}\n")
        f.write(f"- **Employees**: {info.get('fullTimeEmployees', 'N/A'):,}\n" if isinstance(info.get('fullTimeEmployees'), int) else "")
        f.write(f"- **Market Cap**: ${info.get('marketCap', 0)/1e9:.1f}B\n" if info.get('marketCap') else "")
        f.write(f"- **Exchange**: {info.get('exchange', 'N/A')}\n\n")

        if fmp_data:
            f.write(f"- **CEO**: {fmp_data.get('ceo', 'N/A')}\n")
            f.write(f"- **HQ**: {fmp_data.get('city', '')}, {fmp_data.get('state', '')}, {fmp_data.get('country', '')}\n")
            f.write(f"- **IPO Date**: {fmp_data.get('ipoDate', 'N/A')}\n\n")

        desc = info.get("longBusinessSummary", "")
        if desc:
            f.write(f"## Business Description\n\n{desc}\n\n")

    # Write financials.md
    fin_path = discovery_dir / "financials.md"
    with open(fin_path, "w") as f:
        f.write("---\n")
        f.write(f"ticker: {ticker}\n")
        f.write("credibility: S5\n")
        f.write("evidence: E3\n")
        f.write(f"updated: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("---\n\n")
        f.write(f"# {ticker} — Financial Summary\n\n")

        # Key metrics
        f.write("## Key Metrics\n\n")
        metrics = [
            ("Market Cap", info.get("marketCap"), lambda v: f"${v/1e9:.1f}B"),
            ("Enterprise Value", info.get("enterpriseValue"), lambda v: f"${v/1e9:.1f}B"),
            ("Revenue (TTM)", info.get("totalRevenue"), lambda v: f"${v/1e9:.2f}B"),
            ("Net Income (TTM)", info.get("netIncomeToCommon"), lambda v: f"${v/1e9:.2f}B"),
            ("Gross Margin", info.get("grossMargins"), lambda v: f"{v*100:.1f}%"),
            ("Operating Margin", info.get("operatingMargins"), lambda v: f"{v*100:.1f}%"),
            ("Profit Margin", info.get("profitMargins"), lambda v: f"{v*100:.1f}%"),
            ("P/E (Trailing)", info.get("trailingPE"), lambda v: f"{v:.1f}"),
            ("P/E (Forward)", info.get("forwardPE"), lambda v: f"{v:.1f}"),
            ("EV/EBITDA", info.get("enterpriseToEbitda"), lambda v: f"{v:.1f}"),
            ("Revenue Growth", info.get("revenueGrowth"), lambda v: f"{v*100:.1f}%"),
            ("Earnings Growth", info.get("earningsGrowth"), lambda v: f"{v*100:.1f}%"),
            ("52W High", info.get("fiftyTwoWeekHigh"), lambda v: f"${v:.2f}"),
            ("52W Low", info.get("fiftyTwoWeekLow"), lambda v: f"${v:.2f}"),
            ("Current Price", info.get("currentPrice"), lambda v: f"${v:.2f}"),
        ]
        f.write("| Metric | Value |\n|--------|-------|\n")
        for label, val, fmt in metrics:
            if val is not None:
                try:
                    f.write(f"| {label} | {fmt(val)} |\n")
                except (TypeError, ValueError):
                    pass
        f.write("\n")

        # Analyst targets
        f.write("## Analyst Targets\n\n")
        for key, label in [("targetHighPrice", "High"), ("targetMeanPrice", "Mean"),
                           ("targetLowPrice", "Low"), ("numberOfAnalystOpinions", "# Analysts")]:
            val = info.get(key)
            if val:
                prefix = "$" if "Price" in key else ""
                f.write(f"- **{label}**: {prefix}{val}\n")
        f.write("\n")

    return ["profile.md", "financials.md"]


def run_xbrl(ticker: str, discovery_dir: Path):
    """Run XBRL data fetch."""
    print(f"  📈 Fetching XBRL data for {ticker}...")
    import fetch_xbrl as xm

    # Monkeypatch DB_DIR
    original_db = xm.DB_DIR
    xm.DB_DIR = discovery_dir.parent  # so DB_DIR / ticker-like → discovery_dir
    # Actually xbrl uses DB_DIR / ticker, we need DB_DIR such that DB_DIR / ticker = discovery_dir
    # But ticker != slug. Instead, we'll just call the functions and handle output manually.
    xm.DB_DIR = original_db  # restore

    facts = xm.fetch_company_facts(ticker)
    if not facts:
        print(f"  ⚠️  No XBRL data for {ticker}")
        return []

    # build_detailed_financials writes to DB_DIR / ticker
    # We need to redirect. Simplest: temporarily create a symlink or just monkeypatch
    old_db = xm.DB_DIR
    # Create a fake parent so that DB_DIR / ticker == discovery_dir
    fake_parent = discovery_dir.parent
    fake_ticker_dir = fake_parent / ticker
    needs_cleanup = False
    if not fake_ticker_dir.exists() and str(fake_ticker_dir) != str(discovery_dir):
        fake_ticker_dir.symlink_to(discovery_dir)
        needs_cleanup = True

    xm.DB_DIR = fake_parent
    try:
        xm.build_detailed_financials(ticker, facts)
    finally:
        xm.DB_DIR = old_db
        if needs_cleanup and fake_ticker_dir.is_symlink():
            fake_ticker_dir.unlink()

    return ["financials_detailed.md"]


def run_youtube(ticker: str, company_name: str, discovery_dir: Path, max_videos: int = 20):
    """Run YouTube transcript fetch."""
    print(f"  🎬 Fetching YouTube transcripts for {ticker} (max {max_videos})...")
    import fetch_youtube as ym

    # Monkeypatch DB_DIR
    old_db = ym.DB_DIR
    fake_parent = discovery_dir.parent
    fake_ticker_dir = fake_parent / ticker
    needs_cleanup = False
    if not fake_ticker_dir.exists() and str(fake_ticker_dir) != str(discovery_dir):
        fake_ticker_dir.symlink_to(discovery_dir)
        needs_cleanup = True

    ym.DB_DIR = fake_parent
    try:
        videos = ym.fetch_youtube_for_company(ticker, company_name, max_videos=max_videos)
    finally:
        ym.DB_DIR = old_db
        if needs_cleanup and fake_ticker_dir.is_symlink():
            fake_ticker_dir.unlink()

    success = sum(1 for v in videos if v.get("chars"))
    print(f"  🎬 YouTube: {success}/{len(videos)} transcripts saved")
    return [f"sources/youtube/{v.get('file', '')}" for v in videos if v.get("chars")]


def run_podcasts(ticker: str, company_name: str, discovery_dir: Path, limit: int = 2):
    """Run podcast metadata fetch (limited episodes)."""
    print(f"  🎙️  Fetching podcasts for {ticker} (limit {limit})...")
    import fetch_podcasts as pm

    old_db = pm.DB_DIR
    fake_parent = discovery_dir.parent
    fake_ticker_dir = fake_parent / ticker
    needs_cleanup = False
    if not fake_ticker_dir.exists() and str(fake_ticker_dir) != str(discovery_dir):
        fake_ticker_dir.symlink_to(discovery_dir)
        needs_cleanup = True

    pm.DB_DIR = fake_parent
    try:
        episodes = pm.fetch_podcasts_for_company(ticker, company_name, company_name_cn=None)
        # Trim to limit
        if len(episodes) > limit:
            episodes = episodes[:limit]
    finally:
        pm.DB_DIR = old_db
        if needs_cleanup and fake_ticker_dir.is_symlink():
            fake_ticker_dir.unlink()

    print(f"  🎙️  Podcasts: {len(episodes)} episodes saved")
    return [f"podcast_{i}" for i in range(len(episodes))]


def export_csv(ticker: str, discovery_dir: Path):
    """Export yfinance financial data as CSV files."""
    print(f"  📁 Exporting CSV data for {ticker}...")
    import yfinance as yf
    import pandas as pd

    stock = yf.Ticker(ticker)
    csv_dir = discovery_dir / "csv"
    csv_dir.mkdir(exist_ok=True)

    files = []
    for name, getter in [
        ("income_statement", lambda: stock.income_stmt),
        ("balance_sheet", lambda: stock.balance_sheet),
        ("cashflow", lambda: stock.cashflow),
        ("quarterly_income", lambda: stock.quarterly_income_stmt),
        ("quarterly_balance", lambda: stock.quarterly_balance_sheet),
        ("quarterly_cashflow", lambda: stock.quarterly_cashflow),
    ]:
        try:
            df = getter()
            if df is not None and not df.empty:
                path = csv_dir / f"{name}.csv"
                df.to_csv(path)
                files.append(f"csv/{name}.csv")
        except Exception as e:
            print(f"    ⚠️  CSV {name}: {e}")

    # Price history (2 years)
    try:
        hist = stock.history(period="2y")
        if not hist.empty:
            path = csv_dir / "price_history_2y.csv"
            hist.to_csv(path)
            files.append("csv/price_history_2y.csv")
    except Exception as e:
        print(f"    ⚠️  CSV price_history: {e}")

    print(f"  📁 CSV: {len(files)} files exported")
    return files


def generate_report(ticker: str, company_name: str, discovery_dir: Path, results: dict, duration: float):
    """Generate _collection_report.md."""
    report_path = discovery_dir / "_collection_report.md"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(report_path, "w") as f:
        f.write(f"# Collection Report: {ticker} ({company_name})\n\n")
        f.write(f"- **Date**: {now}\n")
        f.write(f"- **Duration**: {duration:.1f}s\n")
        f.write(f"- **Mode**: collect_lite (精简版)\n\n")
        f.write("## Module Results\n\n")

        for module, (success, files, error) in results.items():
            status = "✅" if success else "❌"
            f.write(f"### {status} {module}\n")
            if success:
                f.write(f"- Files: {len(files)}\n")
                for fn in files[:10]:
                    f.write(f"  - {fn}\n")
                if len(files) > 10:
                    f.write(f"  - ... and {len(files)-10} more\n")
            else:
                f.write(f"- Error: {error}\n")
            f.write("\n")

        # File inventory
        f.write("## File Inventory\n\n")
        total_size = 0
        file_count = 0
        for p in discovery_dir.rglob("*"):
            if p.is_file():
                size = p.stat().st_size
                total_size += size
                file_count += 1
        f.write(f"- Total files: {file_count}\n")
        f.write(f"- Total size: {total_size/1024:.0f} KB\n")


def main():
    parser = argparse.ArgumentParser(description="Lite data collection for a company")
    parser.add_argument("ticker", help="Stock ticker (e.g., PLTR)")
    parser.add_argument("company_name", help="Company name (e.g., 'Palantir Technologies')")
    parser.add_argument("--podcast-limit", type=int, default=2, help="Max podcasts to fetch (default: 2)")
    parser.add_argument("--youtube-limit", type=int, default=20, help="Max YouTube videos (default: 20)")
    parser.add_argument("--skip", help="Comma-separated modules to skip (e.g., youtube,podcasts)")
    args = parser.parse_args()

    ticker = args.ticker
    company_name = args.company_name
    skip = set(args.skip.split(",")) if args.skip else set()

    # Resolve slug and paths
    slug = load_slug(ticker)
    discovery_dir = VAULT_DIR / "companies" / slug / "discovery"
    setup_dirs(discovery_dir)

    print(f"{'='*60}")
    print(f"🚀 collect_lite: {ticker} ({company_name})")
    print(f"📂 Output: vault/companies/{slug}/discovery/")
    print(f"{'='*60}")

    start = time.time()
    results = {}

    # Phase 1: financials + xbrl (parallel)
    phase1_modules = {}
    if "financials" not in skip:
        phase1_modules["financials"] = lambda: run_financials(ticker, discovery_dir)
    if "xbrl" not in skip:
        phase1_modules["xbrl"] = lambda: run_xbrl(ticker, discovery_dir)

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {}
        for name, func in phase1_modules.items():
            futures[executor.submit(func)] = name

        for future in as_completed(futures):
            name = futures[future]
            try:
                files = future.result()
                results[name] = (True, files, None)
            except Exception as e:
                print(f"  ❌ {name}: {e}")
                traceback.print_exc()
                results[name] = (False, [], str(e))

    # Phase 2: youtube + podcasts (parallel)
    phase2_modules = {}
    if "youtube" not in skip:
        phase2_modules["youtube"] = lambda: run_youtube(ticker, company_name, discovery_dir, args.youtube_limit)
    if "podcasts" not in skip:
        phase2_modules["podcasts"] = lambda: run_podcasts(ticker, company_name, discovery_dir, args.podcast_limit)

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {}
        for name, func in phase2_modules.items():
            futures[executor.submit(func)] = name

        for future in as_completed(futures):
            name = futures[future]
            try:
                files = future.result()
                results[name] = (True, files, None)
            except Exception as e:
                print(f"  ❌ {name}: {e}")
                traceback.print_exc()
                results[name] = (False, [], str(e))

    # Phase 3: CSV export
    if "csv" not in skip:
        try:
            files = export_csv(ticker, discovery_dir)
            results["csv_export"] = (True, files, None)
        except Exception as e:
            print(f"  ❌ csv_export: {e}")
            results["csv_export"] = (False, [], str(e))

    duration = time.time() - start
    generate_report(ticker, company_name, discovery_dir, results, duration)

    # Summary
    print(f"\n{'='*60}")
    print(f"✅ Done in {duration:.1f}s")
    for name, (success, files, error) in results.items():
        status = "✅" if success else "❌"
        print(f"  {status} {name}: {len(files)} files" if success else f"  {status} {name}: {error}")
    print(f"📂 vault/companies/{slug}/discovery/")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
