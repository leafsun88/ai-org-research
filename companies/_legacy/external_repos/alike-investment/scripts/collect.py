#!/usr/bin/env python3
"""
Discovery Database — 统一数据采集引擎 v3
=========================================
一键启动，并行执行所有数据源采集。

Usage:
    python collect.py APP AppLovin --cn 应用乐欣
    python collect.py NVDA NVIDIA
    python collect.py APP AppLovin --only financials,youtube
    python collect.py APP AppLovin --skip podcasts

输出结构:
    {TICKER}/
    ├── profile.md                  公司概况（静态层）
    ├── financials.md               财务摘要+估值（慢速层）
    ├── financials_detailed.md      XBRL精选指标
    ├── data_full_xbrl.md           XBRL全量371指标
    ├── data_full_statements.md     yfinance全量报表
    ├── data_price_history.md       完整历史股价
    ├── data_holders.md             持股+insider+分析师
    ├── financials_fmp.md           FMP财务报表（季度+年度）
    ├── metrics_fmp.md              FMP关键指标+比率
    ├── analysts_fmp.md             FMP分析师+评级+持仓
    ├── earnings_transcripts_fmp.md FMP Earnings Call Transcripts
    ├── sources/
    │   ├── earnings/               SEC 10-K/10-Q全文
    │   ├── youtube/                YouTube transcript
    │   └── podcasts/               播客元数据
    └── _collection_report.md       采集报告
"""

import sys
import json
import time
import argparse
import traceback
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add scripts dir to path
sys.path.insert(0, str(Path(__file__).parent))

DB_DIR = Path(__file__).parent.parent

# ── Company Registry ──
COMPANY_ALIASES = {
    "APP": ("AppLovin", "应用乐欣"),
    "NVDA": ("NVIDIA", "英伟达"),
    "AAPL": ("Apple", "苹果"),
    "MSFT": ("Microsoft", "微软"),
    "GOOG": ("Alphabet", "谷歌"),
    "AMZN": ("Amazon", "亚马逊"),
    "META": ("Meta", "Meta"),
    "ORCL": ("Oracle", "甲骨文"),
    "CRM": ("Salesforce", "赛富时"),
    "ADBE": ("Adobe", "奥多比"),
    "NFLX": ("Netflix", "奈飞"),
    "SNOW": ("Snowflake", "雪花"),
    "PLTR": ("Palantir", "Palantir"),
    "CRWD": ("CrowdStrike", "CrowdStrike"),
    "TTD": ("TradeDesk", "萃弈"),
    "BABA": ("Alibaba", "阿里巴巴"),
    "PDD": ("PDD Holdings", "拼多多"),
    "BIDU": ("Baidu", "百度"),
    "NTES": ("NetEase", "网易"),
    "BILI": ("Bilibili", "哔哩哔哩"),
}

ALL_MODULES = [
    "financials",       # yfinance + FMP profile → profile.md, financials.md
    "xbrl",             # SEC EDGAR XBRL → financials_detailed.md
    "full_dump",        # XBRL全量 + yfinance全量 + 价格 + 持股
    "fmp_enhanced",     # FMP全量数据（财务报表+指标+分析师+transcript）
    "sec_filings",      # 10-K/10-Q全文
    "youtube",          # YouTube搜索+字幕提取
    "podcasts",         # Apple Podcasts搜索
    "xiaoyuzhou",       # 小宇宙搜索
]

# Modules that can run in parallel (no dependencies between them)
PARALLEL_GROUP_1 = ["financials", "xbrl", "fmp_enhanced"]  # API-based, fast
PARALLEL_GROUP_2 = ["full_dump", "sec_filings"]             # Heavier API calls
PARALLEL_GROUP_3 = ["youtube", "podcasts", "xiaoyuzhou"]    # Search-based, slow


def setup_dirs(ticker):
    """Create company directory structure."""
    base = DB_DIR / ticker
    for subdir in ["sources/earnings", "sources/youtube", "sources/podcasts", "signals"]:
        (base / subdir).mkdir(parents=True, exist_ok=True)
    return base


def run_module(module_name, ticker, company_name, company_name_cn):
    """Run a single collection module. Returns (module_name, success, details)."""
    start = time.time()
    try:
        if module_name == "financials":
            from fetch_financials import fetch_financials
            fetch_financials(ticker)
            return (module_name, True, {"files": ["profile.md", "financials.md"]})

        elif module_name == "xbrl":
            from fetch_xbrl import fetch_company_facts, build_detailed_financials
            facts = fetch_company_facts(ticker)
            if facts:
                build_detailed_financials(ticker, facts)
                return (module_name, True, {"files": ["financials_detailed.md"]})
            return (module_name, False, {"error": "No XBRL data found"})

        elif module_name == "full_dump":
            from fetch_everything import dump_xbrl_full, dump_yfinance_statements, dump_price_history, dump_holders_analysts
            dump_xbrl_full(ticker)
            dump_yfinance_statements(ticker)
            dump_price_history(ticker)
            dump_holders_analysts(ticker)
            return (module_name, True, {"files": [
                "data_full_xbrl.md", "data_full_statements.md",
                "data_price_history.md", "data_holders.md"
            ]})

        elif module_name == "fmp_enhanced":
            from fetch_fmp_enhanced import main as fmp_main
            fmp_main(ticker)
            return (module_name, True, {"files": [
                "financials_fmp.md", "metrics_fmp.md", "analysts_fmp.md",
                "earnings_transcripts_fmp.md", "price_history_fmp.md", "segments_fmp.md"
            ]})

        elif module_name == "sec_filings":
            from fetch_sec_edgar import fetch_sec_filings
            result = fetch_sec_filings(ticker, filing_types=['10-K', '10-Q'], max_per_type=4)
            count = sum(len(v) for v in result.get("filings", {}).values())
            return (module_name, True, {"filing_count": count})

        elif module_name == "youtube":
            from fetch_youtube import fetch_youtube_for_company
            videos = fetch_youtube_for_company(ticker, company_name, max_videos=20)
            success_count = sum(1 for v in videos if v.get("chars"))
            return (module_name, True, {
                "total": len(videos),
                "with_transcript": success_count,
                "total_chars": sum(v.get("chars", 0) for v in videos)
            })

        elif module_name == "podcasts":
            from fetch_podcasts import fetch_podcasts_for_company
            episodes = fetch_podcasts_for_company(ticker, company_name, company_name_cn)
            return (module_name, True, {"episode_count": len(episodes)})

        elif module_name == "xiaoyuzhou":
            from fetch_xiaoyuzhou import fetch_xiaoyuzhou_for_company
            episodes = fetch_xiaoyuzhou_for_company(ticker, company_name, company_name_cn)
            return (module_name, True, {"episode_count": len(episodes)})

        else:
            return (module_name, False, {"error": f"Unknown module: {module_name}"})

    except Exception as e:
        tb = traceback.format_exc()
        return (module_name, False, {"error": str(e), "traceback": tb})
    finally:
        elapsed = time.time() - start
        print(f"  {'✓' if True else '✗'} {module_name}: {elapsed:.1f}s")


def run_parallel_group(group, ticker, company_name, company_name_cn, modules_to_run):
    """Run a group of modules in parallel."""
    active = [m for m in group if m in modules_to_run]
    if not active:
        return {}

    results = {}
    with ThreadPoolExecutor(max_workers=len(active)) as executor:
        futures = {
            executor.submit(run_module, m, ticker, company_name, company_name_cn): m
            for m in active
        }
        for future in as_completed(futures):
            mod = futures[future]
            try:
                name, success, details = future.result()
                results[name] = {"success": success, **details}
            except Exception as e:
                results[mod] = {"success": False, "error": str(e)}

    return results


def generate_report(ticker, company_name, all_results, elapsed):
    """Generate comprehensive collection report."""
    lines = [
        f"# {ticker} ({company_name}) — 数据采集报告",
        f"**采集时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**总耗时**: {elapsed:.1f}秒",
        "",
    ]

    # Module results
    for module in ALL_MODULES:
        r = all_results.get(module, {})
        if not r:
            lines.append(f"### {module}: ⏭ 跳过")
        elif r.get("success"):
            lines.append(f"### {module}: ✅ 成功")
            for k, v in r.items():
                if k not in ("success", "traceback"):
                    lines.append(f"  - {k}: {v}")
        else:
            lines.append(f"### {module}: ❌ 失败")
            lines.append(f"  - error: {r.get('error', 'unknown')}")
        lines.append("")

    # File inventory
    lines.append("## 文件清单")
    company_dir = DB_DIR / ticker
    if company_dir.exists():
        total_size = 0
        for f in sorted(company_dir.rglob("*.md")):
            if f.name.startswith("_"):
                continue
            rel = f.relative_to(company_dir)
            size = f.stat().st_size
            total_size += size
            lines.append(f"  - {rel} ({size // 1024}KB)")
        lines.append(f"\n**总计**: {total_size // 1024}KB")

    report = "\n".join(lines)
    report_path = company_dir / "_collection_report.md"
    report_path.write_text(report, encoding="utf-8")
    return report


def collect(ticker, company_name=None, company_name_cn=None,
            only=None, skip=None):
    """
    Main entry point — collect all data for one company.

    Args:
        ticker: Stock ticker (e.g. 'APP')
        company_name: English name (auto-lookup if omitted)
        company_name_cn: Chinese name (auto-lookup if omitted)
        only: List of modules to run (exclusive)
        skip: List of modules to skip
    """
    # Auto-resolve names
    if not company_name:
        alias = COMPANY_ALIASES.get(ticker, (ticker, ""))
        company_name = alias[0]
    if not company_name_cn:
        alias = COMPANY_ALIASES.get(ticker, ("", ""))
        company_name_cn = alias[1] if len(alias) > 1 else ""

    # Determine which modules to run
    if only:
        modules_to_run = set(only)
    else:
        modules_to_run = set(ALL_MODULES)
    if skip:
        modules_to_run -= set(skip)

    print(f"\n{'='*60}")
    print(f"  📊 Discovery Database — 数据采集")
    print(f"  公司: {ticker} ({company_name})")
    print(f"  模块: {', '.join(sorted(modules_to_run))}")
    print(f"{'='*60}\n")

    setup_dirs(ticker)
    start_time = time.time()
    all_results = {}

    # Group 1: Fast API calls (parallel)
    print("── 阶段 1/3: 财务数据 ──")
    r = run_parallel_group(PARALLEL_GROUP_1, ticker, company_name, company_name_cn, modules_to_run)
    all_results.update(r)

    # Group 2: Heavy API calls (parallel)
    print("\n── 阶段 2/3: 全量数据 + SEC文档 ──")
    r = run_parallel_group(PARALLEL_GROUP_2, ticker, company_name, company_name_cn, modules_to_run)
    all_results.update(r)

    # Group 3: Search-based (parallel)
    print("\n── 阶段 3/3: 媒体搜索 ──")
    r = run_parallel_group(PARALLEL_GROUP_3, ticker, company_name, company_name_cn, modules_to_run)
    all_results.update(r)

    elapsed = time.time() - start_time

    # Generate report
    report = generate_report(ticker, company_name, all_results, elapsed)
    print(f"\n{'='*60}")
    print(report)
    print(f"{'='*60}")

    return all_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Discovery Database 统一数据采集")
    parser.add_argument("ticker", help="股票代码 (e.g. APP)")
    parser.add_argument("company_name", nargs="?", help="公司英文名 (e.g. AppLovin)")
    parser.add_argument("--cn", help="公司中文名")
    parser.add_argument("--only", help=f"仅运行指定模块 (逗号分隔): {','.join(ALL_MODULES)}")
    parser.add_argument("--skip", help="跳过指定模块 (逗号分隔)")

    args = parser.parse_args()

    only = args.only.split(",") if args.only else None
    skip = args.skip.split(",") if args.skip else None

    collect(
        ticker=args.ticker,
        company_name=args.company_name,
        company_name_cn=args.cn,
        only=only,
        skip=skip,
    )
