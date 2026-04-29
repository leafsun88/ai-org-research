#!/usr/bin/env python3
"""
Discovery Database — 统一数据采集引擎 v3 (Alike Investment集成版)
================================================================
一键启动，并行执行所有数据源采集。
输出到 vault/companies/{slug}/discovery/

Usage:
    python collect.py VEEV "Veeva Systems"
    python collect.py TTD TradeDesk --cn 萃弈
    python collect.py PLTR --only financials,xbrl
    python collect.py FTNT --skip youtube,podcasts
"""

import os
import sys
import json
import time
import argparse
import traceback
import subprocess
import unicodedata
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add scripts dir to path
sys.path.insert(0, str(Path(__file__).parent))

# ── Alike Investment vault路径 ──
PROJECT_ROOT = Path(__file__).parent.parent.parent
VAULT_DIR = PROJECT_ROOT / "vault" / "companies"
INDEX_FILE = PROJECT_ROOT / "vault" / "_index.json"


def _ticker_to_slug(ticker):
    """从 _index.json 的 ticker_map 查找 slug"""
    if INDEX_FILE.exists():
        idx = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
        tm = idx.get("ticker_map", {})
        if ticker in tm:
            return tm[ticker]
    return ticker.lower()


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
    "FTNT": ("Fortinet", "飞塔"),
    "VEEV": ("Veeva Systems", "维瓦"),
    "CVNA": ("Carvana", "卡瓦纳"),
    "TDG": ("TransDigm", "TransDigm"),
    "LMND": ("Lemonade", "Lemonade"),
    "BABA": ("Alibaba", "阿里巴巴"),
    "PDD": ("PDD Holdings", "拼多多"),
    "BIDU": ("Baidu", "百度"),
    "NTES": ("NetEase", "网易"),
    "BILI": ("Bilibili", "哔哩哔哩"),
    "DUOL": ("Duolingo", "多邻国"),
}

ALL_MODULES = [
    "financials",       # yfinance → profile.md, financials.md
    "xbrl",             # SEC EDGAR XBRL → financials_detailed.md
    "full_dump",        # XBRL全量 + yfinance全量 + 价格 + 持股
    "sec_filings",      # 10-K/10-Q全文
    "youtube",          # YouTube搜索+字幕提取
    "podcasts",         # Apple Podcasts搜索
    "xiaoyuzhou",       # 小宇宙搜索
    "org_basic",        # 基础组织结构自动生成
    "founder",          # Founder / CEO voice 自动生成
    "org_scan",         # 组织穿透脚本版
    "proxy_governance", # Proxy / governance 自动采集
]
# 注意：fmp_enhanced 因 fetch_fmp_enhanced.py 缺失，暂不纳入

PARALLEL_GROUP_1 = ["financials", "xbrl"]           # API-based, fast
PARALLEL_GROUP_2 = ["full_dump", "sec_filings"]      # Heavier API calls
PARALLEL_GROUP_3 = ["youtube", "podcasts", "xiaoyuzhou"]  # Search-based
POST_MODULES = ["org_basic", "founder", "org_scan", "proxy_governance"]


def setup_output_dir(ticker):
    """创建vault输出目录，设置 ALIKE_DB_DIR 环境变量。

    子脚本用 DB_DIR / ticker 写文件。
    设 ALIKE_DB_DIR 使得 DB_DIR/ticker = vault/companies/{slug}/discovery/
    即 ALIKE_DB_DIR = vault/companies/{slug}/discovery 的父目录（但ticker作为子目录名）

    解决 ticker != slug 的问题：创建临时 symlink
    """
    slug = _ticker_to_slug(ticker)
    discovery_dir = VAULT_DIR / slug / "discovery"

    # 创建目录结构
    for subdir in ["sources/earnings", "sources/youtube", "sources/podcasts",
                    "sources/perplexity", "signals"]:
        (discovery_dir / subdir).mkdir(parents=True, exist_ok=True)

    # 方案：设置 ALIKE_DB_DIR 为一个临时目录，在其中创建 ticker -> discovery_dir 的 symlink
    import tempfile
    tmpdir = Path(tempfile.mkdtemp(prefix="alike_"))
    symlink = tmpdir / ticker
    symlink.symlink_to(discovery_dir)
    os.environ["ALIKE_DB_DIR"] = str(tmpdir)
    print(f"  📁 Output: vault/companies/{slug}/discovery/")

    return discovery_dir, tmpdir


def cleanup_tmpdir(tmpdir):
    """清理临时目录"""
    import shutil
    if tmpdir.exists():
        shutil.rmtree(tmpdir)
        print(f"  🧹 Cleaned up temp dir")


def run_module(module_name, ticker, company_name, company_name_cn):
    """Run a single collection module."""
    start = time.time()
    ok = False
    try:
        if module_name == "financials":
            from fetch_financials import fetch_financials
            fetch_financials(ticker)
            ok = True
            return (module_name, True, {"files": ["profile.md", "financials.md"]})

        elif module_name == "xbrl":
            from fetch_xbrl import fetch_company_facts, build_detailed_financials
            facts = fetch_company_facts(ticker)
            if facts:
                build_detailed_financials(ticker, facts)
                ok = True
                return (module_name, True, {"files": ["financials_detailed.md"]})
            return (module_name, False, {"error": "No XBRL data found (non-US stock?)"})

        elif module_name == "full_dump":
            from fetch_everything import dump_xbrl_full, dump_yfinance_statements, dump_price_history, dump_holders_analysts
            dump_xbrl_full(ticker)
            dump_yfinance_statements(ticker)
            dump_price_history(ticker)
            dump_holders_analysts(ticker)
            ok = True
            return (module_name, True, {"files": [
                "data_full_xbrl.md", "data_full_statements.md",
                "data_price_history.md", "data_holders.md"
            ]})

        elif module_name == "sec_filings":
            from fetch_sec_edgar import fetch_sec_filings
            result = fetch_sec_filings(ticker, filing_types=['10-K', '10-Q'], max_per_type=4)
            count = sum(len(v) for v in result.get("filings", {}).values())
            ok = result.get("success", True)
            return (module_name, True, {"filing_count": count})

        elif module_name == "youtube":
            from fetch_youtube import fetch_youtube_for_company
            videos = fetch_youtube_for_company(ticker, company_name, max_videos=20)
            success_count = sum(1 for v in videos if v.get("chars"))
            ok = True
            return (module_name, True, {
                "total": len(videos),
                "with_transcript": success_count,
                "total_chars": sum(v.get("chars", 0) for v in videos)
            })

        elif module_name == "podcasts":
            from fetch_podcasts import fetch_podcasts_for_company
            episodes = fetch_podcasts_for_company(ticker, company_name, company_name_cn)
            ok = True
            return (module_name, True, {"episode_count": len(episodes)})

        elif module_name == "xiaoyuzhou":
            from fetch_xiaoyuzhou import fetch_xiaoyuzhou_for_company
            episodes = fetch_xiaoyuzhou_for_company(ticker, company_name, company_name_cn)
            ok = True
            return (module_name, True, {"episode_count": len(episodes)})

        elif module_name == "org_basic":
            from fetch_org_basic import fetch_org_basic
            result = fetch_org_basic(ticker, company_name)
            ok = True
            return (module_name, True, result)

        elif module_name == "founder":
            from fetch_founder import fetch_founder_voice
            result = fetch_founder_voice(ticker, company_name)
            ok = True
            return (module_name, True, result)

        elif module_name == "org_scan":
            from fetch_org_scan import fetch_org_scan
            result = fetch_org_scan(ticker, company_name)
            ok = True
            return (module_name, True, result)

        elif module_name == "proxy_governance":
            from fetch_proxy_governance import fetch_proxy_governance
            result = fetch_proxy_governance(ticker, company_name)
            ok = True
            return (module_name, True, result)

        else:
            return (module_name, False, {"error": f"Unknown module: {module_name}"})

    except Exception as e:
        tb = traceback.format_exc()
        return (module_name, False, {"error": str(e), "traceback": tb})
    finally:
        elapsed = time.time() - start
        print(f"  {'✓' if ok else '✗'} {module_name}: {elapsed:.1f}s")


def _contains_cjk(text):
    if not text:
        return False
    return any("CJK" in unicodedata.name(ch, "") for ch in text if ch.strip())


def _is_china_relevant_company(ticker, company_name_cn):
    ticker_upper = ticker.upper()
    china_suffixes = (".HK", ".SS", ".SZ", ".BJ", ".TW")
    known_china_tickers = {"BABA", "BIDU", "PDD", "NTES", "BILI", "JD", "TCOM", "TME"}
    return (
        ticker_upper.endswith(china_suffixes)
        or ticker_upper in known_china_tickers
        or (ticker_upper.isalpha() and len(ticker_upper) > 5 and company_name_cn and _contains_cjk(company_name_cn))
    )


def _is_us_sec_expected(ticker, output_dir=None):
    ticker_upper = ticker.upper()
    non_us_suffixes = (".HK", ".SS", ".SZ", ".BJ", ".TW", ".NS", ".KS", ".L", ".TO", ".PA")
    if ticker_upper.endswith(non_us_suffixes):
        return False

    if output_dir:
        profile_path = output_dir / "profile.md"
        if profile_path.exists():
            profile_text = profile_path.read_text(encoding="utf-8", errors="ignore")
            private_signals = [
                "- **交易所**: N/A",
                "- **IPO日期**: N/A",
                "company: HARVEY",
            ]
            if any(signal in profile_text for signal in private_signals):
                return False
            foreign_signals = [
                "Netherlands",
                "Taiwan",
                "China",
                "Singapore",
                "Israel",
                "Ireland",
                "United Kingdom",
                "Germany",
                "France",
                "Japan",
                "Korea",
                "headquartered in veldhoven",
                "headquartered in hsinchu",
            ]
            lower_text = profile_text.lower()
            if any(signal.lower() in lower_text for signal in foreign_signals):
                return False

    return True


def _list_files(output_dir):
    return [f for f in output_dir.rglob("*") if f.is_file() and f.name != ".DS_Store"]


def _files_touched_since(output_dir, started_at):
    return [f for f in _list_files(output_dir) if f.stat().st_mtime >= started_at]


def _check(name, level, passed, detail, remediation=None):
    return {
        "name": name,
        "level": level,
        "passed": passed,
        "detail": detail,
        "remediation": remediation,
    }


def generate_summary(output_dir):
    """Generate discovery summary via the existing helper script."""
    script = PROJECT_ROOT / "skills" / "collect" / "generate-summary.sh"
    company_dir = output_dir.parent
    if not script.exists():
        return {"success": False, "error": f"Missing summary script: {script}"}

    try:
        result = subprocess.run(
            ["bash", str(script), str(company_dir)],
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
        return {
            "success": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


def scaffold_org_workspace(ticker, company_name, company_name_cn, output_dir):
    """Create org-oriented placeholders so /collect naturally flows into org work."""
    organization_dir = output_dir / "organization"
    overview_dir = organization_dir / "overview"
    c_suite_dir = organization_dir / "c_suite"
    vp_dir = organization_dir / "vp_level"
    board_dir = organization_dir / "board"
    departed_dir = organization_dir / "departed"
    founder_voice_path = output_dir / "sources" / "founder_voice.md"
    org_brief_path = organization_dir / "_org_brief.md"
    org_request_path = organization_dir / "_org_scan_request.md"
    org_report_path = organization_dir / "_org_scan_report.md"
    org_structure_path = overview_dir / "org_structure.md"

    for path in [overview_dir, c_suite_dir, vp_dir, board_dir, departed_dir]:
        path.mkdir(parents=True, exist_ok=True)

    if not founder_voice_path.exists():
        founder_voice_path.write_text(
            f"""---
ticker: {ticker}
type: founder_voice
status: pending
credibility: S3
evidence: E2
generated: {datetime.now().strftime('%Y-%m-%d')}
---

# {company_name} ({ticker}) — Founder / CEO Voice

## Purpose
该文件由 `/collect` 自动创建，作为 `/founder` 的承接入口。

## Next Actions
- 确认 CEO / founder 身份与当前角色
- 收集近 12-18 个月公开采访、播客、演讲、推文
- 补充 insider trading / public response / strategy shift 信号

## Key Questions
- CEO 最近最常谈的战略主题是什么？
- 是否出现组织设计、考核机制、AI/产品方向的变化？
- 言行是否一致？
""",
            encoding="utf-8",
        )

    if not org_brief_path.exists():
        org_brief_path.write_text(
            f"""---
ticker: {ticker}
type: org_brief
status: pending
generated: {datetime.now().strftime('%Y-%m-%d')}
---

# {company_name} ({ticker}) — 组织穿透简报

## Why This Exists
Alike Investment 的核心判断依赖组织穿透。`/collect` 已完成基础数据采集，但组织静态/动态信息仍需专门补齐。

## Minimum Org Dataset
- CEO / founder profile
- C-Suite 名单与职责
- Board 结构
- 近 2 年关键高管变动
- CEO / CFO / CTO 近期公开发言
- 组织变化与关键战略信号

## Suggested Skills
- `/org-scan {ticker} "{company_name}"`
- `/founder {ticker} "CEO Name"`
""",
            encoding="utf-8",
        )

    if not org_request_path.exists():
        org_request_path.write_text(
            f"""---
ticker: {ticker}
type: org_scan_request
status: pending
generated: {datetime.now().strftime('%Y-%m-%d')}
---

# {company_name} ({ticker}) — Org Scan Request

## Required Outputs
- `organization/overview/org_structure.md`
- `organization/_org_scan_report.md`
- `organization/c_suite/*.md`
- `organization/board/*.md`
- `organization/vp_level/*.md`
- `organization/departed/*.md`

## Validation Focus
- 是否能描述汇报关系与关键职能 owner
- 是否识别到近 2 年管理层变动
- 是否有跨公司共事网络/人才来源线索
- 是否识别到争议、离职、治理异常
""",
            encoding="utf-8",
        )

    if not org_report_path.exists():
        org_report_path.write_text(
            f"""---
ticker: {ticker}
type: org_scan_report
status: pending
generated: {datetime.now().strftime('%Y-%m-%d')}
credibility: S4
evidence: E2
---

# {company_name} ({ticker}) — 组织架构穿透报告

该文件由 `/collect` 自动创建为占位文件，表示组织穿透尚未完成。

## Status
- pending: 需要运行 `/org-scan`
- pending: 需要补充 `founder_voice.md`

## Missing Sections
- 组织概览
- C-Suite 核心团队
- VP 级关键人物
- 已离职关键人物
- 关键发现与投资信号
""",
            encoding="utf-8",
        )

    if not org_structure_path.exists():
        org_structure_path.write_text(
            f"""---
ticker: {ticker}
type: org_structure
status: pending
generated: {datetime.now().strftime('%Y-%m-%d')}
credibility: S4
evidence: E2
---

# {company_name} ({ticker}) — Org Structure

待 `/org-scan` 补充：
- CEO / founder
- C-Suite 汇报关系
- 关键 VP owner
- board / committee
- 近两年 departed leaders
""",
            encoding="utf-8",
        )

    return {
        "founder_voice": founder_voice_path,
        "org_brief": org_brief_path,
        "org_request": org_request_path,
        "org_report": org_report_path,
        "org_structure": org_structure_path,
    }


def validate_collection(ticker, company_name, company_name_cn, output_dir,
                        modules_to_run, run_started_at, elapsed):
    """Post-collection validation with explicit PASS/WARN/FAIL semantics."""
    sec_expected = _is_us_sec_expected(ticker, output_dir=output_dir)
    china_relevant = _is_china_relevant_company(ticker, company_name_cn)

    profile_path = output_dir / "profile.md"
    financials_path = output_dir / "financials.md"
    detailed_financials_path = output_dir / "financials_detailed.md"
    report_path = output_dir / "_collection_report.md"
    summary_path = output_dir / "_summary.json"
    validation_json_path = output_dir / "_validation.json"
    validation_md_path = output_dir / "_validation.md"
    founder_voice_path = output_dir / "sources" / "founder_voice.md"
    org_report_path = output_dir / "organization" / "_org_scan_report.md"
    org_structure_path = output_dir / "organization" / "overview" / "org_structure.md"
    governance_summary_path = output_dir / "organization" / "governance_summary.md"
    proxy_dir = output_dir / "organization" / "proxy"

    earnings_files = sorted((output_dir / "sources" / "earnings").glob("*.md"))
    youtube_files = sorted((output_dir / "sources" / "youtube").glob("*.md"))
    podcast_files = sorted((output_dir / "sources" / "podcasts").glob("*.md"))
    xiaoyuzhou_files = [f for f in podcast_files if "_xy_" in f.name]
    new_files = _files_touched_since(output_dir, run_started_at)

    checks = []
    if "financials" in modules_to_run:
        checks.append(_check(
            "profile_exists",
            "fail",
            profile_path.exists() and profile_path.stat().st_size > 0,
            f"profile.md {'exists' if profile_path.exists() else 'missing'}",
            "检查 financials 模块是否成功写入 profile.md。",
        ))
        checks.append(_check(
            "financials_exists",
            "fail",
            financials_path.exists() and financials_path.stat().st_size > 0,
            f"financials.md {'exists' if financials_path.exists() else 'missing'}",
            "检查 financials 模块是否成功写入 financials.md。",
        ))

    if "xbrl" in modules_to_run:
        checks.append(_check(
            "xbrl_output",
            "fail" if sec_expected else "warn",
            detailed_financials_path.exists() and detailed_financials_path.stat().st_size > 0,
            f"financials_detailed.md {'exists' if detailed_financials_path.exists() else 'missing'}",
            "若为美股，检查 SEC CIK 映射与 XBRL 拉取。",
        ))

    if "sec_filings" in modules_to_run:
        checks.append(_check(
            "sec_filings_count",
            "fail" if sec_expected else "warn",
            len(earnings_files) > 0,
            f"earnings filings: {len(earnings_files)}",
            "若为美股，检查 SEC filings 是否成功下载。",
        ))

    if "youtube" in modules_to_run:
        checks.append(_check(
            "youtube_count",
            "warn",
            len(youtube_files) > 0,
            f"youtube transcripts: {len(youtube_files)}",
            "检查 yt-dlp、YouTube 搜索词和字幕可用性。",
        ))

    if "podcasts" in modules_to_run:
        checks.append(_check(
            "podcast_count",
            "warn",
            len(podcast_files) > 0,
            f"podcast files: {len(podcast_files)}",
            "检查 Apple Podcasts 搜索是否返回结果。",
        ))

    if "xiaoyuzhou" in modules_to_run:
        if china_relevant:
            checks.append(_check(
                "xiaoyuzhou_count",
                "warn",
                len(xiaoyuzhou_files) > 0,
                f"xiaoyuzhou files: {len(xiaoyuzhou_files)}",
                "中国相关公司可补查小宇宙；若持续为 0，再走 WebSearch 补搜。",
            ))
        else:
            checks.append(_check(
                "xiaoyuzhou_applicability",
                "info",
                True,
                "非中国相关公司，小宇宙为 0 不视为问题。",
            ))

    checks.append(_check(
        "report_freshness",
        "warn",
        report_path.exists() and report_path.stat().st_mtime >= run_started_at,
        f"_collection_report.md {'fresh' if report_path.exists() and report_path.stat().st_mtime >= run_started_at else ('stale' if report_path.exists() else 'missing')}",
        "若报告未更新，优先查看 _validation.json / _summary.json 和实际产物。",
    ))
    checks.append(_check(
        "new_files_this_run",
        "warn",
        len(new_files) > 0,
        f"files touched this run: {len(new_files)}",
        "如果本轮没有新增文件，检查是否只是复用了旧缓存或外部请求失败。",
    ))

    summary_result = generate_summary(output_dir)
    checks.append(_check(
        "summary_generated",
        "warn",
        summary_result.get("success", False) and summary_path.exists(),
        f"_summary.json {'generated' if summary_path.exists() else 'missing'}",
        "检查 generate-summary.sh 是否可执行。",
    ))

    founder_voice_text = founder_voice_path.read_text(encoding="utf-8", errors="ignore") if founder_voice_path.exists() else ""
    org_report_text = org_report_path.read_text(encoding="utf-8", errors="ignore") if org_report_path.exists() else ""
    org_structure_text = org_structure_path.read_text(encoding="utf-8", errors="ignore") if org_structure_path.exists() else ""

    founder_voice_ready = founder_voice_path.exists() and founder_voice_path.stat().st_size > 0 and "status: pending" not in founder_voice_text
    org_report_ready = org_report_path.exists() and org_report_path.stat().st_size > 0 and "status: pending" not in org_report_text
    org_structure_ready = org_structure_path.exists() and org_structure_path.stat().st_size > 0 and "status: pending" not in org_structure_text
    high_quality_org_ready = (
        founder_voice_ready and org_report_ready and org_structure_ready
        and "status: auto_basic" not in founder_voice_text
        and "status: auto_basic" not in org_report_text
        and "status: auto_basic" not in org_structure_text
    )

    checks.append(_check(
        "org_foundation_present",
        "warn",
        founder_voice_path.exists() and org_report_path.exists() and org_structure_path.exists(),
        "org workspace scaffolded",
        "若缺失，重新运行 /collect 或手动创建 organization/founder 入口文件。",
    ))
    checks.append(_check(
        "founder_voice_ready",
        "warn",
        founder_voice_ready,
        f"founder_voice {'ready' if founder_voice_ready else 'pending'}",
        "运行 /founder 并补齐 CEO / founder 公开发言与 insider signal。",
    ))
    checks.append(_check(
        "org_scan_ready",
        "warn",
        org_report_ready and org_structure_ready,
        f"org_scan_report={'ready' if org_report_ready else 'pending'}, org_structure={'ready' if org_structure_ready else 'pending'}",
        "运行 /org-scan 补齐组织静态与关键高管变动。",
    ))
    checks.append(_check(
        "org_dataset_minimum",
        "warn",
        founder_voice_ready and org_report_ready and org_structure_ready,
        "minimum org dataset for D1-D7",
        "在 founder/org-scan 完成前，不建议进入高质量 D1-D7 评分。",
    ))
    checks.append(_check(
        "org_dataset_high_quality",
        "warn",
        high_quality_org_ready,
        "high-quality org dataset",
        "当前若仍是 auto_basic 版本，建议继续运行 `/founder` 和 `/org-scan` 做深挖。",
    ))
    if "proxy_governance" in modules_to_run:
        checks.append(_check(
            "governance_summary_ready",
            "warn",
            governance_summary_path.exists() and governance_summary_path.stat().st_size > 0,
            f"governance_summary {'ready' if governance_summary_path.exists() else 'missing'}",
            "检查 proxy / governance 模块是否成功写入治理摘要。",
        ))
        checks.append(_check(
            "proxy_filing_present",
            "warn",
            len(list(proxy_dir.glob("*.md"))) > 0,
            f"proxy filings: {len(list(proxy_dir.glob('*.md')))}",
            "若美股 proxy 仍为空，检查 DEF 14A 抓取是否成功。",
        ))

    fail_count = sum(1 for c in checks if c["level"] == "fail" and not c["passed"])
    warn_count = sum(1 for c in checks if c["level"] == "warn" and not c["passed"])
    status = "FAIL" if fail_count else ("WARN" if warn_count else "PASS")

    validation = {
        "ticker": ticker,
        "company_name": company_name,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": status,
        "elapsed_seconds": round(elapsed, 1),
        "run_started_at": datetime.fromtimestamp(run_started_at).strftime("%Y-%m-%d %H:%M:%S"),
        "market_expectations": {
            "sec_expected": sec_expected,
            "china_relevant": china_relevant,
        },
        "counts": {
            "total_files": len(_list_files(output_dir)),
            "new_files_this_run": len(new_files),
            "earnings_files": len(earnings_files),
            "youtube_files": len(youtube_files),
            "podcast_files": len(podcast_files),
            "xiaoyuzhou_files": len(xiaoyuzhou_files),
        },
        "org_readiness": {
            "founder_voice_ready": founder_voice_ready,
            "org_report_ready": org_report_ready,
            "org_structure_ready": org_structure_ready,
            "high_quality_org_ready": high_quality_org_ready,
        },
        "checks": checks,
        "summary_generation": summary_result,
        "new_files_preview": [str(f.relative_to(output_dir)) for f in sorted(new_files)[:20]],
    }

    validation_json_path.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        "---",
        "type: collect_validation",
        f"ticker: {ticker}",
        f"status: {status}",
        f"generated: {datetime.now().strftime('%Y-%m-%d')}",
        "---",
        "",
        f"# {ticker} ({company_name}) — 采集校验",
        f"- 状态: **{status}**",
        f"- 总耗时: {elapsed:.1f}秒",
        f"- 本轮新增文件: {len(new_files)}",
        f"- SEC应有预期: {'yes' if sec_expected else 'no'}",
        f"- 中国公司相关: {'yes' if china_relevant else 'no'}",
        "",
        "## 检查结果",
    ]
    for check in checks:
        icon = "PASS" if check["passed"] else check["level"].upper()
        lines.append(f"- [{icon}] `{check['name']}`: {check['detail']}")
        if not check["passed"] and check.get("remediation"):
            lines.append(f"- 建议: {check['remediation']}")
    lines.append("")
    lines.append("## 本轮新增文件（前20）")
    if validation["new_files_preview"]:
        for item in validation["new_files_preview"]:
            lines.append(f"- {item}")
    else:
        lines.append("- 无")

    validation_md_path.write_text("\n".join(lines), encoding="utf-8")
    return validation


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


def generate_report(ticker, company_name, all_results, elapsed, output_dir):
    """Generate comprehensive collection report."""
    lines = [
        f"---",
        f"credibility: S5",
        f"evidence: E3",
        f"source: collect-script",
        f"date: {datetime.now().strftime('%Y-%m-%d')}",
        f"---",
        f"",
        f"# {ticker} ({company_name}) — 数据采集报告",
        f"**采集时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**总耗时**: {elapsed:.1f}秒",
        f"**输出目录**: {output_dir}",
        "",
    ]

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
    if output_dir.exists():
        total_size = 0
        for f in sorted(output_dir.rglob("*.md")):
            if f.name.startswith("_"):
                continue
            rel = f.relative_to(output_dir)
            size = f.stat().st_size
            total_size += size
            lines.append(f"  - {rel} ({size // 1024}KB)")
        lines.append(f"\n**总计**: {total_size // 1024}KB")

    report = "\n".join(lines)
    report_path = output_dir / "_collection_report.md"
    report_path.write_text(report, encoding="utf-8")
    return report


def collect(ticker, company_name=None, company_name_cn=None,
            only=None, skip=None):
    """Main entry point — collect all data for one company."""
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
    print(f"  📊 Alike Investment — 数据采集")
    print(f"  公司: {ticker} ({company_name})")
    print(f"  Slug: {_ticker_to_slug(ticker)}")
    print(f"  模块: {', '.join(sorted(modules_to_run))}")
    print(f"{'='*60}\n")

    output_dir, tmpdir = setup_output_dir(ticker)

    try:
        start_time = time.time()
        all_results = {}

        scaffold = scaffold_org_workspace(
            ticker=ticker,
            company_name=company_name,
            company_name_cn=company_name_cn,
            output_dir=output_dir,
        )

        # Group 1: Fast API calls
        print("── 阶段 1/3: 财务数据 ──")
        r = run_parallel_group(PARALLEL_GROUP_1, ticker, company_name, company_name_cn, modules_to_run)
        all_results.update(r)

        # Group 2: Heavy API calls
        print("\n── 阶段 2/3: 全量数据 + SEC文档 ──")
        r = run_parallel_group(PARALLEL_GROUP_2, ticker, company_name, company_name_cn, modules_to_run)
        all_results.update(r)

        # Group 3: Search-based
        print("\n── 阶段 3/3: 媒体搜索 ──")
        r = run_parallel_group(PARALLEL_GROUP_3, ticker, company_name, company_name_cn, modules_to_run)
        all_results.update(r)

        active_post = [m for m in POST_MODULES if m in modules_to_run]
        if active_post:
            print("\n── 阶段 4/4: 组织入口增强 ──")
            for module_name in active_post:
                name, success, details = run_module(module_name, ticker, company_name, company_name_cn)
                all_results[name] = {"success": success, **details}

        elapsed = time.time() - start_time

        # Generate report + validation
        report = generate_report(ticker, company_name, all_results, elapsed, output_dir)
        validation = validate_collection(
            ticker=ticker,
            company_name=company_name,
            company_name_cn=company_name_cn,
            output_dir=output_dir,
            modules_to_run=modules_to_run,
            run_started_at=start_time,
            elapsed=elapsed,
        )
        print(f"\n{'='*60}")
        print(report)
        print(f"校验状态: {validation['status']}")
        print(f"新增文件: {validation['counts']['new_files_this_run']}")
        print(f"组织入口: {scaffold['org_report']}")
        print(f"Founder入口: {scaffold['founder_voice']}")
        print(f"校验文件: {output_dir / '_validation.json'}")
        print(f"{'='*60}")

        return {
            "results": all_results,
            "validation": validation,
        }
    finally:
        cleanup_tmpdir(tmpdir)
        os.environ.pop("ALIKE_DB_DIR", None)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Alike Investment — 数据采集")
    parser.add_argument("ticker", help="股票代码 (e.g. VEEV)")
    parser.add_argument("company_name", nargs="?", help="公司英文名")
    parser.add_argument("--cn", help="公司中文名")
    parser.add_argument("--only", help=f"仅运行指定模块: {','.join(ALL_MODULES)}")
    parser.add_argument("--skip", help="跳过指定模块")

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
