"""
全量数据导出器 — "Bloomberg级"数据dump
========================================
把SEC EDGAR XBRL的全部371个财务指标 + yfinance全部数据
一次性导出为结构化Markdown。

输出文件:
  {TICKER}/data_full_xbrl.md       — SEC XBRL 全部371个指标，按类别组织
  {TICKER}/data_full_statements.md — yfinance完整财务报表（每一行都导出）
  {TICKER}/data_price_history.md   — 完整历史股价
  {TICKER}/data_holders.md         — 机构持股 + insider + 分析师全量
"""

import os
import sys
import json
import math
import requests
import yfinance as yf
import pandas as pd
from pathlib import Path
from datetime import datetime
from collections import defaultdict

DB_DIR = Path(os.environ.get('ALIKE_DB_DIR', str(Path(__file__).parent.parent)))
HEADERS = {'User-Agent': 'InvestmentResearch research@example.com'}
FMP_KEY = "d6TWVuHkxLqJqXN3M8VfgPiyfDzVfSOv"

# ── Ticker映射 ──
def _get_yf_ticker(ticker: str) -> str:
    """港股等特殊ticker映射"""
    try:
        sys.path.insert(0, str(DB_DIR))
        from companies import get_yf_ticker
        return get_yf_ticker(ticker)
    except ImportError:
        return ticker

# ── Utils ──

def fmt_num(v):
    """Format a number for display."""
    if v is None:
        return "N/A"
    try:
        v = float(v)
    except (TypeError, ValueError):
        return str(v)
    if math.isnan(v) or math.isinf(v):
        return "N/A"
    av = abs(v)
    sign = "-" if v < 0 else ""
    if av >= 1e12: return f"{sign}${av/1e12:.2f}T"
    if av >= 1e9: return f"{sign}${av/1e9:.3f}B"
    if av >= 1e6: return f"{sign}${av/1e6:.2f}M"
    if av >= 1e3: return f"{sign}${av/1e3:.1f}K"
    if av == int(av): return f"{sign}{int(av)}"
    return f"{sign}{v:.4f}"

def safe_str(v):
    if v is None: return "N/A"
    if isinstance(v, float) and (math.isnan(v) or math.isinf(v)): return "N/A"
    return str(v)

# ── CIK Lookup ──

_CIK_CACHE = {}
def get_cik(ticker):
    global _CIK_CACHE
    if not _CIK_CACHE:
        try:
            r = requests.get('https://www.sec.gov/files/company_tickers.json', headers=HEADERS, timeout=30)
            for item in r.json().values():
                _CIK_CACHE[item['ticker'].upper()] = str(item['cik_str']).zfill(10)
        except: pass
    return _CIK_CACHE.get(ticker.upper())


# ═══════════════════════════════════════════
# Part 1: XBRL Full Dump (371 concepts)
# ═══════════════════════════════════════════

def categorize_concept(name):
    """Categorize an XBRL concept into a section."""
    name_lower = name.lower()
    if any(k in name_lower for k in ['revenue', 'sales']): return '收入'
    if any(k in name_lower for k in ['costof', 'cogs']): return '成本'
    if any(k in name_lower for k in ['grossprofit']): return '毛利'
    if any(k in name_lower for k in ['research', 'development']): return '研发'
    if any(k in name_lower for k in ['selling', 'marketing', 'general', 'admin']): return '销售管理'
    if any(k in name_lower for k in ['operatingincome', 'operatingloss']): return '营业利润'
    if any(k in name_lower for k in ['interest']): return '利息'
    if any(k in name_lower for k in ['tax', 'deferred']): return '税务'
    if any(k in name_lower for k in ['netincome', 'earnings', 'eps', 'diluted', 'basic']): return '盈利/EPS'
    if any(k in name_lower for k in ['depreciation', 'amortization', 'impairment']): return '折旧摊销'
    if any(k in name_lower for k in ['stockbased', 'sharebase', 'compensation']): return '股权激励'
    if any(k in name_lower for k in ['cash', 'restricted']): return '现金'
    if any(k in name_lower for k in ['receivable']): return '应收'
    if any(k in name_lower for k in ['payable', 'accrued']): return '应付'
    if any(k in name_lower for k in ['goodwill', 'intangible']): return '商誉/无形资产'
    if any(k in name_lower for k in ['asset']): return '资产'
    if any(k in name_lower for k in ['debt', 'borrow', 'loan', 'note']): return '债务'
    if any(k in name_lower for k in ['liabilit']): return '负债'
    if any(k in name_lower for k in ['equity', 'stock', 'share', 'capital', 'retained', 'treasury']): return '权益/股本'
    if any(k in name_lower for k in ['dividend']): return '股息'
    if any(k in name_lower for k in ['repurchase', 'buyback']): return '回购'
    if any(k in name_lower for k in ['acquisition', 'business combination', 'merger']): return '并购'
    if any(k in name_lower for k in ['lease', 'rent']): return '租赁'
    if any(k in name_lower for k in ['property', 'equipment', 'ppe']): return 'PP&E'
    if any(k in name_lower for k in ['contract', 'deferred revenue']): return '合同/递延'
    if any(k in name_lower for k in ['segment']): return '分部信息'
    if any(k in name_lower for k in ['comprehensive']): return '综合收益'
    if any(k in name_lower for k in ['foreign', 'exchange']): return '外汇'
    return '其他'


def dump_xbrl_full(ticker: str) -> str:
    """Dump ALL XBRL concepts as markdown."""
    cik = get_cik(ticker)
    if not cik:
        return f"# {ticker} — XBRL数据不可用 (CIK not found)"

    r = requests.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json', headers=HEADERS, timeout=30)
    if r.status_code != 200:
        return f"# {ticker} — XBRL数据不可用 (HTTP {r.status_code})"

    data = r.json()
    gaap = data.get('facts', {}).get('us-gaap', {})
    dei = data.get('facts', {}).get('dei', {})
    entity = data.get('entityName', ticker)

    lines = []
    lines.append("---")
    lines.append(f"ticker: {ticker}")
    lines.append(f"company: {entity}")
    lines.append(f"last_updated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append(f"data_source: SEC EDGAR XBRL (全量dump)")
    lines.append(f"total_concepts: {len(gaap)}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {entity} ({ticker}) — XBRL全量财务数据 ({len(gaap)}个指标)")
    lines.append("")

    # Organize by category
    categorized = defaultdict(list)
    for concept_name in sorted(gaap.keys()):
        cat = categorize_concept(concept_name)
        categorized[cat].append(concept_name)

    # Preferred category order
    cat_order = ['收入', '成本', '毛利', '研发', '销售管理', '营业利润', '利息',
                 '盈利/EPS', '折旧摊销', '股权激励', '税务', '综合收益',
                 '现金', '应收', '应付', '商誉/无形资产', 'PP&E', '资产',
                 '债务', '负债', '合同/递延', '权益/股本', '回购', '股息',
                 '并购', '租赁', '外汇', '分部信息', '其他']

    for cat in cat_order:
        concepts = categorized.get(cat, [])
        if not concepts:
            continue

        lines.append(f"## {cat} ({len(concepts)}个指标)")
        lines.append("")

        for concept_name in concepts:
            concept = gaap[concept_name]
            desc = concept.get('description', '')
            units = concept.get('units', {})

            for unit_type, datapoints in units.items():
                if not datapoints:
                    continue

                # Separate annual (10-K) and quarterly (10-Q)
                annual = {}
                quarterly = {}

                for dp in datapoints:
                    form = dp.get('form', '')
                    frame = dp.get('frame', '')
                    fp = dp.get('fp', '')
                    val = dp.get('val')
                    end = dp.get('end', '')
                    start = dp.get('start', '')

                    if val is None:
                        continue

                    # Use CY frame for clean period labels
                    if frame and frame.startswith('CY'):
                        label = frame[2:]  # e.g., CY2025Q3 -> 2025Q3, CY2025 -> 2025
                        if 'Q' in label:
                            quarterly[label] = val
                        else:
                            annual[label] = val
                    elif form == '10-K' and fp == 'FY':
                        # Annual from 10-K without CY frame
                        try:
                            year = end[:4]
                            if year not in annual:
                                annual[year] = val
                        except:
                            pass
                    elif form == '10-Q':
                        # Quarterly without CY frame - use end date
                        try:
                            dt = datetime.strptime(end, '%Y-%m-%d')
                            q = (dt.month - 1) // 3 + 1
                            qlabel = f"{dt.year}Q{q}"
                            if qlabel not in quarterly:
                                quarterly[qlabel] = val
                        except:
                            pass

                if not annual and not quarterly:
                    continue

                lines.append(f"### {concept_name}")
                if desc:
                    lines.append(f"*{desc[:200]}*")
                lines.append(f"单位: {unit_type}")
                lines.append("")

                # Annual table
                if annual:
                    a_keys = sorted(annual.keys(), reverse=True)
                    lines.append(f"**年度** ({len(a_keys)}年)")
                    lines.append("| " + " | ".join(a_keys) + " |")
                    lines.append("| " + " | ".join(["---"] * len(a_keys)) + " |")
                    lines.append("| " + " | ".join(fmt_num(annual[k]) for k in a_keys) + " |")
                    lines.append("")

                # Quarterly table
                if quarterly:
                    q_keys = sorted(quarterly.keys(), reverse=True)
                    # Split into rows of 8 for readability
                    for chunk_start in range(0, len(q_keys), 10):
                        chunk = q_keys[chunk_start:chunk_start + 10]
                        label = f"**季度** ({len(q_keys)}Q)" if chunk_start == 0 else ""
                        if label:
                            lines.append(label)
                        lines.append("| " + " | ".join(chunk) + " |")
                        lines.append("| " + " | ".join(["---"] * len(chunk)) + " |")
                        lines.append("| " + " | ".join(fmt_num(quarterly[k]) for k in chunk) + " |")
                    lines.append("")

                lines.append("")

    return "\n".join(lines)


# ═══════════════════════════════════════════
# Part 2: yfinance Full Statement Dump
# ═══════════════════════════════════════════

def dump_df(df, title, mode='year'):
    """Convert a pandas DataFrame to markdown table with ALL rows."""
    if df is None or df.empty:
        return f"### {title}\n*数据不可用*\n"

    lines = []
    lines.append(f"### {title}")

    # Column headers
    if mode == 'year':
        col_labels = [c.strftime('%Y') if hasattr(c, 'strftime') else str(c)[:4] for c in df.columns]
    else:
        col_labels = []
        for c in df.columns:
            if hasattr(c, 'month'):
                q = (c.month - 1) // 3 + 1
                col_labels.append(f"{c.year}Q{q}")
            else:
                col_labels.append(str(c)[:10])

    headers = ["指标"] + col_labels
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for row_name in df.index:
        row = [f"**{row_name}**"]
        for c in df.columns:
            try:
                v = df.loc[row_name, c]
                row.append(fmt_num(v))
            except:
                row.append("N/A")
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")
    return "\n".join(lines)


def dump_yfinance_statements(ticker: str) -> str:
    """Dump ALL yfinance financial statements with every row."""
    stock = yf.Ticker(_get_yf_ticker(ticker))
    info = stock.info or {}

    lines = []
    lines.append("---")
    lines.append(f"ticker: {ticker}")
    lines.append(f"last_updated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("data_source: Yahoo Finance (全量dump)")
    lines.append("---")
    lines.append("")
    lines.append(f"# {ticker} — 完整财务报表 (yfinance)")
    lines.append("")

    # All info fields
    lines.append("## 公司信息 (全部字段)")
    lines.append("| Key | Value |")
    lines.append("|-----|-------|")
    for k in sorted(info.keys()):
        v = info[k]
        if v is not None and k != 'companyOfficers':
            vstr = str(v)
            if len(vstr) > 200:
                vstr = vstr[:200] + "..."
            # Escape pipe characters in markdown
            vstr = vstr.replace('|', '\\|')
            lines.append(f"| {k} | {vstr} |")
    lines.append("")

    # Company Officers detail
    officers = info.get('companyOfficers', [])
    if officers:
        lines.append("## 管理层完整信息")
        lines.append("| Name | Title | Age | Fiscal Year | Total Pay | Exercised Value | Unexercised Value |")
        lines.append("|------|-------|-----|-------------|-----------|-----------------|-------------------|")
        for o in officers:
            lines.append(f"| {o.get('name','N/A')} | {o.get('title','N/A')} | {o.get('age','N/A')} | {o.get('fiscalYear','N/A')} | {fmt_num(o.get('totalPay'))} | {fmt_num(o.get('exercisedValue'))} | {fmt_num(o.get('unexercisedValue'))} |")
        lines.append("")

    # Financial statements - ALL rows
    statements = [
        ('年度损益表', 'income_stmt', 'year'),
        ('季度损益表', 'quarterly_income_stmt', 'quarter'),
        ('年度资产负债表', 'balance_sheet', 'year'),
        ('季度资产负债表', 'quarterly_balance_sheet', 'quarter'),
        ('年度现金流量表', 'cashflow', 'year'),
        ('季度现金流量表', 'quarterly_cashflow', 'quarter'),
    ]

    for title, attr, mode in statements:
        try:
            df = getattr(stock, attr)
            lines.append(dump_df(df, title, mode))
        except Exception as e:
            lines.append(f"### {title}\n*Error: {e}*\n")

    return "\n".join(lines)


# ═══════════════════════════════════════════
# Part 3: Price History
# ═══════════════════════════════════════════

def dump_price_history(ticker: str) -> str:
    """Dump complete daily price history."""
    stock = yf.Ticker(_get_yf_ticker(ticker))
    hist = stock.history(period='max')

    lines = []
    lines.append("---")
    lines.append(f"ticker: {ticker}")
    lines.append(f"last_updated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append(f"data_source: Yahoo Finance (历史价格)")
    lines.append(f"trading_days: {len(hist)}")
    lines.append(f"date_range: {hist.index[0].strftime('%Y-%m-%d')} to {hist.index[-1].strftime('%Y-%m-%d')}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {ticker} — 完整历史股价 ({len(hist)}个交易日)")
    lines.append("")

    # Monthly summary first
    lines.append("## 月度汇总")
    monthly = hist.resample('ME').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
    monthly = monthly.dropna()
    lines.append("| 月份 | 开盘 | 最高 | 最低 | 收盘 | 月涨跌% | 成交量 |")
    lines.append("|------|------|------|------|------|---------|--------|")
    prev_close = None
    for idx, row in monthly.iterrows():
        month = idx.strftime('%Y-%m')
        change = ""
        if prev_close and prev_close > 0:
            pct = (row['Close'] - prev_close) / prev_close * 100
            change = f"{pct:+.1f}%"
        prev_close = row['Close']
        lines.append(f"| {month} | ${row['Open']:.2f} | ${row['High']:.2f} | ${row['Low']:.2f} | ${row['Close']:.2f} | {change} | {fmt_num(row['Volume'])} |")
    lines.append("")

    # Weekly summary — 全量（所有历史周数据）
    lines.append(f"## 周度汇总 (全量)")
    weekly = hist.resample('W-FRI').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last', 'Volume': 'sum'})
    weekly = weekly.dropna()
    lines.append(f"*共{len(weekly)}周数据*")
    lines.append("")
    lines.append("| 周 | 开盘 | 最高 | 最低 | 收盘 | 周涨跌% | 成交量 |")
    lines.append("|------|------|------|------|------|---------|--------|")
    prev_close = None
    for idx, row in weekly.iterrows():
        week = idx.strftime('%Y-%m-%d')
        change = ""
        if prev_close and prev_close > 0:
            pct = (row['Close'] - prev_close) / prev_close * 100
            change = f"{pct:+.1f}%"
        prev_close = row['Close']
        lines.append(f"| {week} | ${row['Open']:.2f} | ${row['High']:.2f} | ${row['Low']:.2f} | ${row['Close']:.2f} | {change} | {fmt_num(row['Volume'])} |")
    lines.append("")

    # Daily data — 全量（所有历史日线数据）
    lines.append(f"## 每日数据 (全量, {len(hist)}个交易日)")
    lines.append("")
    lines.append("| 日期 | 开盘 | 最高 | 最低 | 收盘 | 涨跌% | 成交量 |")
    lines.append("|------|------|------|------|------|-------|--------|")
    prev_close = None
    for idx, row in hist.iterrows():
        date = idx.strftime('%Y-%m-%d')
        change = ""
        if prev_close and prev_close > 0:
            pct = (row['Close'] - prev_close) / prev_close * 100
            change = f"{pct:+.1f}%"
        prev_close = row['Close']
        lines.append(f"| {date} | ${row['Open']:.2f} | ${row['High']:.2f} | ${row['Low']:.2f} | ${row['Close']:.2f} | {change} | {fmt_num(row['Volume'])} |")
    lines.append("")

    # Key statistics
    lines.append("## 价格统计")
    lines.append("| 指标 | 数值 |")
    lines.append("|------|------|")
    lines.append(f"| IPO以来最高 | ${hist['High'].max():.2f} |")
    lines.append(f"| IPO以来最低 | ${hist['Low'].min():.2f} |")
    lines.append(f"| IPO开盘价 | ${hist['Open'].iloc[0]:.2f} |")
    lines.append(f"| 当前价格 | ${hist['Close'].iloc[-1]:.2f} |")
    ipo_return = (hist['Close'].iloc[-1] / hist['Open'].iloc[0] - 1) * 100
    lines.append(f"| IPO以来回报 | {ipo_return:+.1f}% |")
    lines.append(f"| 日均成交量(全历史) | {fmt_num(hist['Volume'].mean())} |")
    lines.append(f"| 日均成交量(近30天) | {fmt_num(hist['Volume'].tail(30).mean())} |")
    lines.append("")

    return "\n".join(lines)


# ═══════════════════════════════════════════
# Part 4: Holders & Analysts Full Dump
# ═══════════════════════════════════════════

def dump_holders_analysts(ticker: str) -> str:
    """Dump all holder and analyst data."""
    stock = yf.Ticker(_get_yf_ticker(ticker))

    lines = []
    lines.append("---")
    lines.append(f"ticker: {ticker}")
    lines.append(f"last_updated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {ticker} — 持股与分析师全量数据")
    lines.append("")

    # Institutional holders
    try:
        ih = stock.institutional_holders
        if ih is not None and not ih.empty:
            lines.append(f"## 机构持股 ({len(ih)}家机构)")
            lines.append("| 报告日 | 机构 | 持股比例 | 股数 | 市值 | 变动% |")
            lines.append("|--------|------|----------|------|------|-------|")
            for _, row in ih.iterrows():
                date = row.get('Date Reported', '')
                if hasattr(date, 'strftime'): date = date.strftime('%Y-%m-%d')
                holder = str(row.get('Holder', 'N/A')).replace('|', '/')
                pct = row.get('pctHeld', 0)
                shares = row.get('Shares', 0)
                value = row.get('Value', 0)
                change = row.get('pctChange', 0)
                pct_s = f"{pct*100:.2f}%" if not (isinstance(pct, float) and math.isnan(pct)) else "N/A"
                change_s = f"{change*100:+.1f}%" if not (isinstance(change, float) and math.isnan(change)) else "N/A"
                lines.append(f"| {date} | {holder} | {pct_s} | {fmt_num(shares)} | {fmt_num(value)} | {change_s} |")
            lines.append("")
    except Exception as e:
        lines.append(f"## 机构持股\n*Error: {e}*\n")

    # Mutual fund holders
    try:
        mf = stock.mutualfund_holders
        if mf is not None and not mf.empty:
            lines.append(f"## 共同基金持股 ({len(mf)}只基金)")
            lines.append("| 报告日 | 基金 | 持股比例 | 股数 | 市值 | 变动% |")
            lines.append("|--------|------|----------|------|------|-------|")
            for _, row in mf.iterrows():
                date = row.get('Date Reported', '')
                if hasattr(date, 'strftime'): date = date.strftime('%Y-%m-%d')
                holder = str(row.get('Holder', 'N/A')).replace('|', '/')
                pct = row.get('pctHeld', 0)
                shares = row.get('Shares', 0)
                value = row.get('Value', 0)
                change = row.get('pctChange', 0)
                pct_s = f"{pct*100:.2f}%" if not (isinstance(pct, float) and math.isnan(pct)) else "N/A"
                change_s = f"{change*100:+.1f}%" if not (isinstance(change, float) and math.isnan(change)) else "N/A"
                lines.append(f"| {date} | {holder} | {pct_s} | {fmt_num(shares)} | {fmt_num(value)} | {change_s} |")
            lines.append("")
    except Exception as e:
        lines.append(f"## 共同基金持股\n*Error: {e}*\n")

    # Insider transactions - ALL
    try:
        it = stock.insider_transactions
        if it is not None and not it.empty:
            lines.append(f"## Insider交易记录 ({len(it)}笔)")
            lines.append("| 日期 | Insider | 职位 | 股数 | 金额 | 说明 | 所有权 |")
            lines.append("|------|---------|------|------|------|------|--------|")
            for _, row in it.iterrows():
                date = row.get('Start Date', '')
                if hasattr(date, 'strftime'): date = date.strftime('%Y-%m-%d')
                insider = str(row.get('Insider', 'N/A')).replace('|', '/')
                position = str(row.get('Position', 'N/A')).replace('|', '/')
                shares = row.get('Shares', 0)
                value = row.get('Value', 0)
                text = str(row.get('Text', '')).replace('|', '/').replace('\n', ' ')[:80]
                ownership = row.get('Ownership', 'N/A')
                lines.append(f"| {date} | {insider} | {position} | {fmt_num(shares)} | {fmt_num(value)} | {text} | {ownership} |")
            lines.append("")
    except Exception as e:
        lines.append(f"## Insider交易记录\n*Error: {e}*\n")

    # ALL analyst upgrades/downgrades
    try:
        ud = stock.upgrades_downgrades
        if ud is not None and not ud.empty:
            lines.append(f"## 分析师评级变动 ({len(ud)}条记录)")
            lines.append("| 日期 | 机构 | 新评级 | 旧评级 | 动作 | 目标价 | 前目标价 |")
            lines.append("|------|------|--------|--------|------|--------|----------|")
            for idx, row in ud.iterrows():
                date = idx.strftime('%Y-%m-%d') if hasattr(idx, 'strftime') else str(idx)[:10]
                firm = str(row.get('Firm', 'N/A')).replace('|', '/')
                to_g = row.get('ToGrade', 'N/A')
                from_g = row.get('FromGrade', 'N/A')
                action = row.get('Action', 'N/A')
                target = row.get('currentPriceTarget')
                prior = row.get('priorPriceTarget')
                target_s = f"${target:.0f}" if target and not (isinstance(target, float) and math.isnan(target)) else "N/A"
                prior_s = f"${prior:.0f}" if prior and not (isinstance(prior, float) and math.isnan(prior)) else "N/A"
                lines.append(f"| {date} | {firm} | {to_g} | {from_g} | {action} | {target_s} | {prior_s} |")
            lines.append("")
    except Exception as e:
        lines.append(f"## 分析师评级变动\n*Error: {e}*\n")

    # Earnings history
    try:
        eh = stock.earnings_history
        if eh is not None and not eh.empty:
            lines.append(f"## Earnings历史 ({len(eh)}个季度)")
            lines.append("| 季度 | 实际EPS | 预期EPS | 差值 | 超预期% |")
            lines.append("|------|--------|--------|------|---------|")
            for idx, row in eh.iterrows():
                q = str(idx)[:10]
                actual = row.get('epsActual')
                est = row.get('epsEstimate')
                diff = row.get('epsDifference')
                surprise = row.get('surprisePercent')
                lines.append(f"| {q} | {fmt_num(actual)} | {fmt_num(est)} | {fmt_num(diff)} | {fmt_num(surprise)} |")
            lines.append("")
    except Exception as e:
        pass

    return "\n".join(lines)


# ═══════════════════════════════════════════
# Main
# ═══════════════════════════════════════════

def fetch_everything(ticker: str):
    """Dump absolutely everything available for a company."""
    print(f"\n{'='*70}")
    print(f"  FULL DATA DUMP: {ticker}")
    print(f"{'='*70}")

    company_dir = DB_DIR / ticker
    company_dir.mkdir(parents=True, exist_ok=True)

    # Part 1: XBRL
    print("\n[1/4] SEC EDGAR XBRL (全部指标)...")
    xbrl_md = dump_xbrl_full(ticker)
    (company_dir / "data_full_xbrl.md").write_text(xbrl_md, encoding='utf-8')
    print(f"  ✓ data_full_xbrl.md ({len(xbrl_md):,} chars, {xbrl_md.count(chr(10))} lines)")

    # Part 2: yfinance statements
    print("\n[2/4] yfinance完整报表...")
    yf_md = dump_yfinance_statements(ticker)
    (company_dir / "data_full_statements.md").write_text(yf_md, encoding='utf-8')
    print(f"  ✓ data_full_statements.md ({len(yf_md):,} chars, {yf_md.count(chr(10))} lines)")

    # Part 3: Price history
    print("\n[3/4] 完整历史股价...")
    price_md = dump_price_history(ticker)
    (company_dir / "data_price_history.md").write_text(price_md, encoding='utf-8')
    print(f"  ✓ data_price_history.md ({len(price_md):,} chars, {price_md.count(chr(10))} lines)")

    # Part 4: Holders & Analysts
    print("\n[4/4] 持股与分析师全量...")
    holders_md = dump_holders_analysts(ticker)
    (company_dir / "data_holders.md").write_text(holders_md, encoding='utf-8')
    print(f"  ✓ data_holders.md ({len(holders_md):,} chars, {holders_md.count(chr(10))} lines)")

    # Summary
    total = len(xbrl_md) + len(yf_md) + len(price_md) + len(holders_md)
    print(f"\n{'='*70}")
    print(f"  总数据量: {total:,} chars ({total//1024}KB)")
    print(f"{'='*70}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_everything.py TICKER")
        sys.exit(1)
    fetch_everything(sys.argv[1])
