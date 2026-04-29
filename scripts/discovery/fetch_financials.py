"""
Phase 1: 财务数据采集 v2
- yfinance: 财务报表、估值、分析师预期、机构持股、insider交易、评级
- FMP API: 公司profile补充 (CEO, 描述等)
输出:
  {TICKER}/profile.md     公司概况 + 管理层 + 股东结构
  {TICKER}/financials.md  完整财务数据 + 估值 + 分析师
"""

import yfinance as yf
import requests
import math
import os
import sys
import time
import pandas as pd
from pathlib import Path
from datetime import datetime

FMP_KEY = "d6TWVuHkxLqJqXN3M8VfgPiyfDzVfSOv"
FMP_BASE = "https://financialmodelingprep.com/stable"
DB_DIR = Path(os.environ.get('ALIKE_DB_DIR', str(Path(__file__).parent.parent)))


def financial_output_dir(ticker: str) -> Path:
    configured = os.environ.get("ALIKE_OUTPUT_DIR", "").strip()
    if configured:
        return Path(configured)
    return DB_DIR / ticker


def fmp_profile(symbol):
    """Fetch company profile from FMP API."""
    try:
        r = requests.get(f"{FMP_BASE}/profile", params={"symbol": symbol, "apikey": FMP_KEY}, timeout=15)
        if r.status_code == 200:
            data = r.json()
            if isinstance(data, list) and data:
                return data[0]
    except Exception:
        pass
    return {}


# ── Formatting helpers ──

def is_nan(v):
    if v is None:
        return True
    if isinstance(v, str):
        return v.strip() in ('', 'N/A', 'nan', 'None')
    try:
        return math.isnan(float(v)) or math.isinf(float(v))
    except (TypeError, ValueError):
        return True


def fmt(value, prefix="$"):
    if is_nan(value):
        return "N/A"
    value = float(value)
    abs_val = abs(value)
    sign = "-" if value < 0 else ""
    if abs_val >= 1e12:
        return f"{sign}{prefix}{abs_val/1e12:.2f}T"
    if abs_val >= 1e9:
        return f"{sign}{prefix}{abs_val/1e9:.2f}B"
    if abs_val >= 1e6:
        return f"{sign}{prefix}{abs_val/1e6:.0f}M"
    if abs_val >= 1e3:
        return f"{sign}{prefix}{abs_val/1e3:.0f}K"
    return f"{sign}{prefix}{value:.2f}"


def pct(num, denom):
    if is_nan(num) or is_nan(denom) or float(denom) == 0:
        return "N/A"
    return f"{float(num)/float(denom)*100:.1f}%"


def pct_val(v):
    if is_nan(v):
        return "N/A"
    v = float(v)
    if abs(v) < 5:
        return f"{v*100:.1f}%"
    return f"{v:.1f}%"


def ratio_fmt(v, decimals=1):
    if is_nan(v):
        return "N/A"
    return f"{float(v):.{decimals}f}"


def yoy_calc(current, previous):
    if is_nan(current) or is_nan(previous) or float(previous) == 0:
        return "N/A"
    return f"{(float(current)-float(previous))/abs(float(previous))*100:+.1f}%"


def safe_val(df, row_names, col):
    if df is None or df.empty:
        return None
    for name in row_names:
        if name in df.index:
            try:
                v = df.loc[name, col]
                if not is_nan(v):
                    return float(v)
            except Exception:
                pass
    return None


def col_label(c, mode="year"):
    if mode == "year":
        return c.strftime("%Y") if hasattr(c, 'strftime') else str(c)[:4]
    else:
        if hasattr(c, 'month'):
            q = (c.month - 1) // 3 + 1
            return f"{c.year}Q{q}"
        return str(c)[:10]


# ── Row name aliases ──

REV = ['Total Revenue', 'TotalRevenue', 'Revenue', 'Operating Revenue']
GP = ['Gross Profit', 'GrossProfit']
OI = ['Operating Income', 'OperatingIncome', 'EBIT']
NI = ['Net Income', 'NetIncome', 'Net Income Common Stockholders']
EBITDA = ['EBITDA', 'Ebitda', 'Normalized EBITDA']
RD = ['Research And Development', 'ResearchAndDevelopment']
SGA = ['Selling General And Administration', 'SellingGeneralAndAdministration']
EPS = ['Diluted EPS', 'DilutedEPS', 'Basic EPS']
SHARES = ['Diluted Average Shares', 'DilutedAverageShares', 'Ordinary Shares Number']

CASH = ['Cash And Cash Equivalents', 'CashAndCashEquivalents', 'Cash']
ST_INV = ['Other Short Term Investments', 'OtherShortTermInvestments']
RECV = ['Net Receivables', 'Receivables', 'Accounts Receivable']
ASSETS = ['Total Assets', 'TotalAssets']
LIAB = ['Total Liabilities Net Minority Interest', 'TotalLiabilitiesNetMinorityInterest']
EQUITY = ['Stockholders Equity', 'StockholdersEquity', 'Total Equity Gross Minority Interest']
LT_DEBT = ['Long Term Debt', 'LongTermDebt', 'Long Term Debt And Capital Lease Obligation']
ST_DEBT = ['Current Debt', 'CurrentDebt', 'Current Debt And Capital Lease Obligation']
GOODWILL = ['Goodwill', 'GoodwillAndOtherIntangibleAssets']
INTANGIBLES = ['Other Intangible Assets', 'OtherIntangibleAssets', 'Net Intangible Assets']
DEFERRED_REV = ['Deferred Revenue', 'Current Deferred Revenue']

OCF = ['Operating Cash Flow', 'OperatingCashFlow', 'Cash Flow From Continuing Operating Activities']
CAPEX = ['Capital Expenditure', 'CapitalExpenditure']
FCF = ['Free Cash Flow', 'FreeCashFlow']
SBC = ['Stock Based Compensation', 'StockBasedCompensation']
BUYBACK = ['Repurchase Of Capital Stock', 'RepurchaseOfCapitalStock']
DIV_PAID = ['Cash Dividends Paid', 'CommonStockDividendPaid']
ACQ = ['Net Business Purchase And Sale', 'Purchase Of Business']
DEBT_REPAY = ['Repayment Of Debt', 'Long Term Debt Payments']
DEBT_ISSUE = ['Long Term Debt Issuance', 'Issuance Of Debt']


# ── profile.md (ENHANCED) ──

def build_profile(ticker, stock, fp):
    info = stock.info or {}
    lines = []
    lines.append("---")
    lines.append(f"ticker: {ticker}")
    lines.append(f"company: {fp.get('companyName', info.get('shortName', ticker))}")
    lines.append(f"last_updated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {fp.get('companyName', info.get('shortName', ticker))} ({ticker})")
    lines.append("")

    # ── 公司概况 ──
    lines.append("## 公司概况")
    lines.append(f"- **行业**: {info.get('industryDisp', fp.get('industry', 'N/A'))}")
    lines.append(f"- **细分行业**: {info.get('sectorDisp', fp.get('sector', 'N/A'))}")
    lines.append(f"- **IPO日期**: {fp.get('ipoDate', 'N/A')}")
    lines.append(f"- **总部**: {info.get('city', fp.get('city', 'N/A'))}, {info.get('state', fp.get('state', 'N/A'))}")
    lines.append(f"- **CEO**: {fp.get('ceo', 'N/A')}")
    emp = info.get('fullTimeEmployees') or fp.get('fullTimeEmployees')
    lines.append(f"- **员工数**: {int(emp):,}" if emp else "- **员工数**: N/A")
    lines.append(f"- **交易所**: {info.get('fullExchangeName', fp.get('exchangeFullName', 'N/A'))}")
    lines.append(f"- **官网**: {fp.get('website', info.get('website', 'N/A'))}")
    lines.append(f"- **地址**: {info.get('address1', 'N/A')}, {info.get('city', '')}, {info.get('state', '')} {info.get('zip', '')}")
    lines.append("")

    # ── 业务描述 ──
    desc = info.get('longBusinessSummary', fp.get('description', ''))
    if desc:
        lines.append("## 业务描述")
        lines.append(desc)
        lines.append("")

    # ── 管理层 ──
    officers = info.get('companyOfficers', [])
    if officers:
        lines.append("## 管理层")
        lines.append("| 姓名 | 职位 | 年龄 | 薪酬 |")
        lines.append("|------|------|------|------|")
        for officer in officers[:15]:
            name = officer.get('name', 'N/A')
            title = officer.get('title', 'N/A')
            age = officer.get('age', 'N/A')
            pay = officer.get('totalPay')
            pay_str = fmt(pay) if pay else 'N/A'
            lines.append(f"| {name} | {title} | {age} | {pay_str} |")
        lines.append("")

    # ── 股东结构 ──
    lines.append("## 股东结构")

    # Major holders summary
    insider_pct = info.get('heldPercentInsiders')
    inst_pct = info.get('heldPercentInstitutions')
    inst_count = info.get('institutionsCount') if 'institutionsCount' in info else None
    float_shares = info.get('floatShares')

    lines.append("### 持股概览")
    lines.append("| 类别 | 比例 |")
    lines.append("|------|------|")
    if insider_pct is not None:
        lines.append(f"| 内部人持股 | {insider_pct*100:.1f}% |")
    if inst_pct is not None:
        lines.append(f"| 机构持股 | {inst_pct*100:.1f}% |")
    if float_shares:
        lines.append(f"| 流通股 | {fmt(float_shares, '')} |")
    shares_out = info.get('sharesOutstanding')
    if shares_out:
        lines.append(f"| 总股本 | {fmt(shares_out, '')} |")
    lines.append("")

    # Institutional holders
    try:
        inst_holders = stock.institutional_holders
        if inst_holders is not None and not inst_holders.empty:
            lines.append("### 前十大机构股东")
            lines.append("| 机构 | 持股比例 | 股数 | 市值 | 变动 |")
            lines.append("|------|----------|------|------|------|")
            for _, row in inst_holders.head(10).iterrows():
                holder = row.get('Holder', 'N/A')
                pct_held = row.get('pctHeld', 0)
                shares = row.get('Shares', 0)
                value = row.get('Value', 0)
                change = row.get('pctChange', 0)
                change_str = f"{change*100:+.1f}%" if not is_nan(change) else "N/A"
                lines.append(f"| {holder} | {pct_held*100:.1f}% | {fmt(shares, '')} | {fmt(value)} | {change_str} |")
            lines.append("")
    except Exception:
        pass

    # ── Insider交易 ──
    try:
        insider_txns = stock.insider_transactions
        if insider_txns is not None and not insider_txns.empty:
            lines.append("### 近期Insider交易")
            lines.append("| 日期 | 内部人 | 职位 | 类型 | 股数 | 金额 |")
            lines.append("|------|--------|------|------|------|------|")
            for _, row in insider_txns.head(15).iterrows():
                date = row.get('Start Date', 'N/A')
                if hasattr(date, 'strftime'):
                    date = date.strftime('%Y-%m-%d')
                insider = row.get('Insider', 'N/A')
                position = row.get('Position', 'N/A')
                text = str(row.get('Text', ''))
                txn_type = "卖出" if "Sale" in text else "买入" if "Purchase" in text else "赠予" if "Gift" in text else text[:15]
                shares = row.get('Shares', 0)
                value = row.get('Value', 0)
                lines.append(f"| {date} | {insider} | {position} | {txn_type} | {fmt(shares, '')} | {fmt(value)} |")
            lines.append("")

            # Insider summary
            try:
                ip = stock.insider_purchases
                if ip is not None and not ip.empty:
                    lines.append("### Insider交易汇总 (近6个月)")
                    lines.append("| 类别 | 股数 | 笔数 |")
                    lines.append("|------|------|------|")
                    for _, row in ip.iterrows():
                        cat = row.iloc[0] if len(row) > 0 else 'N/A'
                        shares = row.get('Shares', 'N/A')
                        trans = row.get('Trans', 'N/A')
                        shares_str = fmt(shares, '') if not is_nan(shares) else str(shares)
                        lines.append(f"| {cat} | {shares_str} | {trans} |")
                    lines.append("")
            except Exception:
                pass
    except Exception:
        pass

    # ── 做空数据 ──
    short_ratio = info.get('shortRatio')
    short_pct = info.get('shortPercentOfFloat')
    short_shares = info.get('sharesShort')
    short_prev = info.get('sharesShortPriorMonth')

    if short_ratio or short_pct:
        lines.append("## 做空数据")
        lines.append("| 指标 | 数值 |")
        lines.append("|------|------|")
        if short_shares:
            lines.append(f"| 做空股数 | {fmt(short_shares, '')} |")
        if short_prev:
            lines.append(f"| 上月做空股数 | {fmt(short_prev, '')} |")
            if short_shares and short_prev:
                chg = (short_shares - short_prev) / short_prev * 100
                lines.append(f"| 做空变化 | {chg:+.1f}% |")
        if short_pct:
            lines.append(f"| 做空占流通股比 | {short_pct*100:.1f}% |")
        if short_ratio:
            lines.append(f"| 做空比率(天) | {short_ratio:.1f} |")
        lines.append("")

    # ── 治理风险 ──
    audit_risk = info.get('auditRisk')
    board_risk = info.get('boardRisk')
    comp_risk = info.get('compensationRisk')
    overall_risk = info.get('overallRisk')
    if any(x is not None for x in [audit_risk, board_risk, comp_risk, overall_risk]):
        lines.append("## 治理风险评分 (1=最低风险, 10=最高风险)")
        lines.append("| 类别 | 评分 |")
        lines.append("|------|------|")
        if overall_risk: lines.append(f"| 综合风险 | {overall_risk}/10 |")
        if audit_risk: lines.append(f"| 审计风险 | {audit_risk}/10 |")
        if board_risk: lines.append(f"| 董事会风险 | {board_risk}/10 |")
        if comp_risk: lines.append(f"| 薪酬风险 | {comp_risk}/10 |")
        shr_risk = info.get('shareHolderRightsRisk')
        if shr_risk: lines.append(f"| 股东权利风险 | {shr_risk}/10 |")
        lines.append("")

    return "\n".join(lines)


# ── financials.md (ENHANCED) ──

def build_financials(ticker, stock, fp):
    info = stock.info or {}
    lines = []
    lines.append("---")
    lines.append(f"ticker: {ticker}")
    lines.append(f"last_updated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append("data_source: Yahoo Finance + FMP")
    lines.append("---")
    lines.append("")
    lines.append(f"# {ticker} 财务数据")
    lines.append("")

    # ── 估值快照 ──
    lines.append("## 估值快照")
    lines.append("| 指标 | 数值 |")
    lines.append("|------|------|")
    price = info.get('currentPrice') or info.get('regularMarketPrice')
    for label, key, f in [
        ("当前股价", "currentPrice", lambda v: f"${v:.2f}"),
        ("市值", "marketCap", lambda v: fmt(v)),
        ("企业价值", "enterpriseValue", lambda v: fmt(v)),
        ("P/E (TTM)", "trailingPE", lambda v: ratio_fmt(v)),
        ("P/E (Forward)", "forwardPE", lambda v: ratio_fmt(v)),
        ("P/S (TTM)", "priceToSalesTrailing12Months", lambda v: ratio_fmt(v)),
        ("P/B", "priceToBook", lambda v: ratio_fmt(v)),
        ("EV/EBITDA", "enterpriseToEbitda", lambda v: ratio_fmt(v)),
        ("EV/Revenue", "enterpriseToRevenue", lambda v: ratio_fmt(v)),
        ("PEG", "pegRatio", lambda v: ratio_fmt(v, 2)),
        ("Trailing PEG", "trailingPegRatio", lambda v: ratio_fmt(v, 2)),
    ]:
        v = info.get(key)
        lines.append(f"| {label} | {f(v) if v is not None else 'N/A'} |")

    # 52 week and moving averages
    lo = info.get('fiftyTwoWeekLow', 'N/A')
    hi = info.get('fiftyTwoWeekHigh', 'N/A')
    lines.append(f"| 52周范围 | {lo} - {hi} |")
    lines.append(f"| 52周变化 | {pct_val(info.get('52WeekChange'))} |")
    lines.append(f"| 50日均线 | ${info.get('fiftyDayAverage', 'N/A'):.2f} |" if info.get('fiftyDayAverage') else "| 50日均线 | N/A |")
    lines.append(f"| 200日均线 | ${info.get('twoHundredDayAverage', 'N/A'):.2f} |" if info.get('twoHundredDayAverage') else "| 200日均线 | N/A |")
    lines.append(f"| Beta | {ratio_fmt(info.get('beta'), 2)} |")
    lines.append(f"| 日均成交量 | {fmt(info.get('averageVolume'), '')} |")
    lines.append("")

    # ── 年度损益表 ──
    inc_a = None
    try:
        inc_a = stock.income_stmt
    except:
        pass

    if inc_a is not None and not inc_a.empty:
        lines.append("## 年度损益表")
        cols = list(inc_a.columns)
        headers = ["指标"] + [col_label(c) for c in cols]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        rev_vals = [safe_val(inc_a, REV, c) for c in cols]
        gp_vals = [safe_val(inc_a, GP, c) for c in cols]
        oi_vals = [safe_val(inc_a, OI, c) for c in cols]
        ni_vals = [safe_val(inc_a, NI, c) for c in cols]

        rows = [
            ("营收", REV, "money"),
            ("营收增速YoY", None, "rev_yoy"),
            ("毛利润", GP, "money"),
            ("毛利率", None, "gm"),
            ("研发费用", RD, "money"),
            ("研发占营收%", None, "rd_pct"),
            ("销售管理费", SGA, "money"),
            ("营业利润", OI, "money"),
            ("营业利润率", None, "om"),
            ("净利润", NI, "money"),
            ("净利润率", None, "nm"),
            ("EBITDA", EBITDA, "money"),
            ("稀释EPS", EPS, "eps"),
            ("稀释股数", SHARES, "shares"),
        ]

        for name, aliases, fmt_type in rows:
            row = [f"**{name}**"]
            for i, c in enumerate(cols):
                if fmt_type == "rev_yoy":
                    if i + 1 < len(cols) and rev_vals[i] and rev_vals[i+1]:
                        row.append(yoy_calc(rev_vals[i], rev_vals[i+1]))
                    else:
                        row.append("N/A")
                elif fmt_type == "gm":
                    row.append(pct(gp_vals[i], rev_vals[i]))
                elif fmt_type == "om":
                    row.append(pct(oi_vals[i], rev_vals[i]))
                elif fmt_type == "nm":
                    row.append(pct(ni_vals[i], rev_vals[i]))
                elif fmt_type == "rd_pct":
                    rd_v = safe_val(inc_a, RD, c)
                    row.append(pct(rd_v, rev_vals[i]))
                elif fmt_type == "eps":
                    v = safe_val(inc_a, aliases, c)
                    row.append(f"${v:.2f}" if v is not None else "N/A")
                elif fmt_type == "shares":
                    v = safe_val(inc_a, aliases, c)
                    row.append(fmt(v, ""))
                else:
                    v = safe_val(inc_a, aliases, c)
                    row.append(fmt(v))
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    # ── 季度损益表 ──
    inc_q = None
    try:
        inc_q = stock.quarterly_income_stmt
    except:
        pass

    if inc_q is not None and not inc_q.empty:
        lines.append("## 季度损益表 (近8个季度)")
        cols = list(inc_q.columns)[:8]
        headers = ["指标"] + [col_label(c, "quarter") for c in cols]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        rev_q = [safe_val(inc_q, REV, c) for c in cols]
        gp_q = [safe_val(inc_q, GP, c) for c in cols]
        oi_q = [safe_val(inc_q, OI, c) for c in cols]
        ni_q = [safe_val(inc_q, NI, c) for c in cols]

        for name, aliases, fmt_type in [
            ("营收", REV, "money"),
            ("营收YoY", None, "yoy"),
            ("营收QoQ", None, "qoq"),
            ("毛利率", None, "gm"),
            ("营业利润", OI, "money"),
            ("营业利润率", None, "om"),
            ("净利润", NI, "money"),
            ("净利润率", None, "nm"),
            ("稀释EPS", EPS, "eps"),
        ]:
            row = [f"**{name}**"]
            for i, c in enumerate(cols):
                if fmt_type == "yoy":
                    all_cols = list(inc_q.columns)
                    if i + 4 < len(all_cols):
                        prev = safe_val(inc_q, REV, all_cols[i+4])
                        row.append(yoy_calc(rev_q[i], prev))
                    else:
                        row.append("N/A")
                elif fmt_type == "qoq":
                    if i + 1 < len(cols) and rev_q[i] and rev_q[i+1]:
                        row.append(yoy_calc(rev_q[i], rev_q[i+1]))
                    else:
                        row.append("N/A")
                elif fmt_type == "gm":
                    row.append(pct(gp_q[i], rev_q[i]))
                elif fmt_type == "om":
                    row.append(pct(oi_q[i], rev_q[i]))
                elif fmt_type == "nm":
                    row.append(pct(ni_q[i], rev_q[i]))
                elif fmt_type == "eps":
                    v = safe_val(inc_q, aliases, c)
                    row.append(f"${v:.2f}" if v is not None else "N/A")
                else:
                    v = safe_val(inc_q, aliases, c)
                    row.append(fmt(v))
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    # ── 资产负债表 (年度) ──
    bs = None
    try:
        bs = stock.balance_sheet
    except:
        pass

    if bs is not None and not bs.empty:
        lines.append("## 资产负债表 (年度)")
        cols = list(bs.columns)
        headers = ["指标"] + [col_label(c) for c in cols]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        for name, aliases in [
            ("现金及等价物", CASH),
            ("短期投资", ST_INV),
            ("应收账款", RECV),
            ("商誉", GOODWILL),
            ("无形资产", INTANGIBLES),
            ("总资产", ASSETS),
            ("递延收入", DEFERRED_REV),
            ("短期债务", ST_DEBT),
            ("长期债务", LT_DEBT),
            ("总负债", LIAB),
            ("股东权益", EQUITY),
        ]:
            row = [f"**{name}**"]
            for c in cols:
                row.append(fmt(safe_val(bs, aliases, c)))
            lines.append("| " + " | ".join(row) + " |")

        # Net cash
        row = ["**净现金/净负债**"]
        for c in cols:
            cash_v = (safe_val(bs, CASH, c) or 0) + (safe_val(bs, ST_INV, c) or 0)
            debt_v = (safe_val(bs, LT_DEBT, c) or 0) + (safe_val(bs, ST_DEBT, c) or 0)
            row.append(fmt(cash_v - debt_v))
        lines.append("| " + " | ".join(row) + " |")

        # Tangible book value
        row = ["**有形账面价值**"]
        for c in cols:
            equity_v = safe_val(bs, EQUITY, c) or 0
            gw_v = safe_val(bs, GOODWILL, c) or 0
            intg_v = safe_val(bs, INTANGIBLES, c) or 0
            row.append(fmt(equity_v - gw_v - intg_v))
        lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    # ── 季度资产负债表 ──
    bs_q = None
    try:
        bs_q = stock.quarterly_balance_sheet
    except:
        pass

    if bs_q is not None and not bs_q.empty:
        lines.append("## 资产负债表 (季度)")
        cols = list(bs_q.columns)[:6]
        headers = ["指标"] + [col_label(c, "quarter") for c in cols]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        for name, aliases in [
            ("现金及等价物", CASH),
            ("应收账款", RECV),
            ("总资产", ASSETS),
            ("长期债务", LT_DEBT),
            ("总负债", LIAB),
            ("股东权益", EQUITY),
        ]:
            row = [f"**{name}**"]
            for c in cols:
                row.append(fmt(safe_val(bs_q, aliases, c)))
            lines.append("| " + " | ".join(row) + " |")

        row = ["**净现金/净负债**"]
        for c in cols:
            cash_v = (safe_val(bs_q, CASH, c) or 0) + (safe_val(bs_q, ST_INV, c) or 0)
            debt_v = (safe_val(bs_q, LT_DEBT, c) or 0) + (safe_val(bs_q, ST_DEBT, c) or 0)
            row.append(fmt(cash_v - debt_v))
        lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    # ── 现金流量表 (年度) ──
    cf = None
    try:
        cf = stock.cashflow
    except:
        pass

    if cf is not None and not cf.empty:
        lines.append("## 现金流量表 (年度)")
        cols = list(cf.columns)
        headers = ["指标"] + [col_label(c) for c in cols]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        for name, aliases in [
            ("经营性现金流", OCF),
            ("资本开支", CAPEX),
            ("自由现金流", FCF),
            ("股权激励(SBC)", SBC),
            ("股票回购", BUYBACK),
            ("分红支出", DIV_PAID),
            ("收购支出", ACQ),
            ("偿还债务", DEBT_REPAY),
            ("发行债务", DEBT_ISSUE),
        ]:
            row = [f"**{name}**"]
            for c in cols:
                v = safe_val(cf, aliases, c)
                if v is None and name == "自由现金流":
                    o = safe_val(cf, OCF, c)
                    cx = safe_val(cf, CAPEX, c)
                    if o is not None and cx is not None:
                        v = o + cx
                row.append(fmt(v))
            lines.append("| " + " | ".join(row) + " |")

        # FCF margin
        if inc_a is not None:
            row = ["**FCF利润率**"]
            for c in cols:
                fcf_v = safe_val(cf, FCF, c)
                if fcf_v is None:
                    o = safe_val(cf, OCF, c)
                    cx = safe_val(cf, CAPEX, c)
                    if o is not None and cx is not None:
                        fcf_v = o + cx
                rev_v = None
                for ic in inc_a.columns:
                    if hasattr(c, 'year') and hasattr(ic, 'year') and c.year == ic.year:
                        rev_v = safe_val(inc_a, REV, ic)
                        break
                row.append(pct(fcf_v, rev_v))
            lines.append("| " + " | ".join(row) + " |")

        # SBC as % of revenue
        if inc_a is not None:
            row = ["**SBC占营收%**"]
            for c in cols:
                sbc_v = safe_val(cf, SBC, c)
                rev_v = None
                for ic in inc_a.columns:
                    if hasattr(c, 'year') and hasattr(ic, 'year') and c.year == ic.year:
                        rev_v = safe_val(inc_a, REV, ic)
                        break
                row.append(pct(sbc_v, rev_v))
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    # ── 季度现金流 ──
    cf_q = None
    try:
        cf_q = stock.quarterly_cashflow
    except:
        pass

    if cf_q is not None and not cf_q.empty:
        lines.append("## 现金流量表 (季度)")
        cols = list(cf_q.columns)[:6]
        headers = ["指标"] + [col_label(c, "quarter") for c in cols]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        for name, aliases in [
            ("经营性现金流", OCF),
            ("资本开支", CAPEX),
            ("自由现金流", FCF),
            ("股权激励(SBC)", SBC),
            ("股票回购", BUYBACK),
        ]:
            row = [f"**{name}**"]
            for c in cols:
                v = safe_val(cf_q, aliases, c)
                if v is None and name == "自由现金流":
                    o = safe_val(cf_q, OCF, c)
                    cx = safe_val(cf_q, CAPEX, c)
                    if o is not None and cx is not None:
                        v = o + cx
                row.append(fmt(v))
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    # ── TTM关键指标 ──
    lines.append("## TTM关键指标")
    lines.append("| 指标 | 数值 |")
    lines.append("|------|------|")
    ttm_items = [
        ("营收", "totalRevenue", fmt),
        ("毛利率", "grossMargins", pct_val),
        ("营业利润率", "operatingMargins", pct_val),
        ("EBITDA利润率", "ebitdaMargins", pct_val),
        ("净利润率", "profitMargins", pct_val),
        ("EBITDA", "ebitda", fmt),
        ("自由现金流", "freeCashflow", fmt),
        ("经营性现金流", "operatingCashflow", fmt),
        ("营收增速", "revenueGrowth", pct_val),
        ("盈利增速", "earningsGrowth", pct_val),
        ("每股营收", "revenuePerShare", lambda v: f"${v:.2f}" if not is_nan(v) else "N/A"),
        ("ROE", "returnOnEquity", pct_val),
        ("ROA", "returnOnAssets", pct_val),
        ("流动比率", "currentRatio", lambda v: ratio_fmt(v, 2)),
        ("速动比率", "quickRatio", lambda v: ratio_fmt(v, 2)),
        ("负债权益比", "debtToEquity", lambda v: ratio_fmt(v, 1)),
        ("总现金", "totalCash", fmt),
        ("每股现金", "totalCashPerShare", lambda v: f"${v:.2f}" if not is_nan(v) else "N/A"),
        ("总债务", "totalDebt", fmt),
    ]
    for label, key, f in ttm_items:
        v = info.get(key)
        lines.append(f"| {label} | {f(v) if v is not None else 'N/A'} |")

    # Rule of 40
    rg = info.get('revenueGrowth')
    om = info.get('operatingMargins')
    if rg is not None and om is not None:
        r40 = (rg + om) * 100
        lines.append(f"| **Rule of 40** | **{r40:.1f}** (增长{rg*100:.1f}% + 利润率{om*100:.1f}%) |")

    rev_ttm = info.get('totalRevenue')
    emp = info.get('fullTimeEmployees')
    if rev_ttm and emp:
        try:
            lines.append(f"| 人均营收 | {fmt(rev_ttm / int(emp))} |")
        except:
            pass
    lines.append("")

    # ── Earnings Beat/Miss历史 ──
    try:
        eh = stock.earnings_history
        if eh is not None and not eh.empty:
            lines.append("## Earnings Beat/Miss 历史")
            lines.append("| 季度 | 实际EPS | 预期EPS | 差值 | 超预期% |")
            lines.append("|------|--------|--------|------|---------|")
            for idx, row in eh.iterrows():
                q_label = idx.strftime('%Y-Q%q') if hasattr(idx, 'strftime') else str(idx)[:10]
                actual = row.get('epsActual', 'N/A')
                est = row.get('epsEstimate', 'N/A')
                diff = row.get('epsDifference', 'N/A')
                surprise = row.get('surprisePercent', 'N/A')
                actual_s = f"${actual:.2f}" if not is_nan(actual) else "N/A"
                est_s = f"${est:.2f}" if not is_nan(est) else "N/A"
                diff_s = f"${diff:+.2f}" if not is_nan(diff) else "N/A"
                surp_s = f"{surprise*100:+.1f}%" if not is_nan(surprise) else "N/A"
                lines.append(f"| {q_label} | {actual_s} | {est_s} | {diff_s} | {surp_s} |")
            lines.append("")
    except Exception:
        pass

    # ── 分析师预期 (Forward) ──
    lines.append("## 分析师预期")
    lines.append("### 目标价")
    lines.append("| 指标 | 数值 |")
    lines.append("|------|------|")
    for label, key in [
        ("目标价(均值)", "targetMeanPrice"),
        ("目标价(中位数)", "targetMedianPrice"),
        ("目标价(高)", "targetHighPrice"),
        ("目标价(低)", "targetLowPrice"),
        ("推荐评级", "recommendationKey"),
        ("评级均值(1=强买,5=强卖)", "recommendationMean"),
        ("分析师数量", "numberOfAnalystOpinions"),
    ]:
        v = info.get(key)
        if v is not None:
            if isinstance(v, float) and key.endswith('Price'):
                lines.append(f"| {label} | ${v:.2f} |")
            elif isinstance(v, float):
                lines.append(f"| {label} | {v:.2f} |")
            else:
                lines.append(f"| {label} | {v} |")
        else:
            lines.append(f"| {label} | N/A |")

    # Upside/downside
    mean_target = info.get('targetMeanPrice')
    if mean_target and price:
        upside = (mean_target - price) / price * 100
        lines.append(f"| **隐含涨幅** | **{upside:+.1f}%** |")
    lines.append("")

    # Revenue/earnings estimates
    try:
        rev_est = stock.revenue_estimate
        if rev_est is not None and not rev_est.empty:
            lines.append("### 营收预期")
            lines.append("| 期间 | 均值 | 低值 | 高值 | 分析师数 | 去年同期 | 增速 |")
            lines.append("|------|------|------|------|----------|----------|------|")
            for idx, row in rev_est.iterrows():
                avg = fmt(row.get('avg'))
                low = fmt(row.get('low'))
                high = fmt(row.get('high'))
                n = row.get('numberOfAnalysts', 'N/A')
                yago = fmt(row.get('yearAgoRevenue'))
                growth = pct_val(row.get('growth'))
                lines.append(f"| {idx} | {avg} | {low} | {high} | {n} | {yago} | {growth} |")
            lines.append("")
    except Exception:
        pass

    try:
        eps_est = stock.earnings_estimate
        if eps_est is not None and not eps_est.empty:
            lines.append("### EPS预期")
            lines.append("| 期间 | 均值 | 低值 | 高值 | 去年EPS | 分析师数 | 增速 |")
            lines.append("|------|------|------|------|---------|----------|------|")
            for idx, row in eps_est.iterrows():
                avg = f"${row['avg']:.2f}" if not is_nan(row.get('avg')) else "N/A"
                low = f"${row['low']:.2f}" if not is_nan(row.get('low')) else "N/A"
                high = f"${row['high']:.2f}" if not is_nan(row.get('high')) else "N/A"
                yago = f"${row['yearAgoEps']:.2f}" if not is_nan(row.get('yearAgoEps')) else "N/A"
                n = row.get('numberOfAnalysts', 'N/A')
                growth = pct_val(row.get('growth'))
                lines.append(f"| {idx} | {avg} | {low} | {high} | {yago} | {n} | {growth} |")
            lines.append("")
    except Exception:
        pass

    # ── 分析师评级变动 ──
    try:
        upgrades = stock.upgrades_downgrades
        if upgrades is not None and not upgrades.empty:
            lines.append("### 近期分析师评级变动")
            lines.append("| 日期 | 机构 | 评级 | 前评级 | 动作 | 目标价 |")
            lines.append("|------|------|------|--------|------|--------|")
            recent = upgrades.head(20)
            for idx, row in recent.iterrows():
                date = idx.strftime('%Y-%m-%d') if hasattr(idx, 'strftime') else str(idx)[:10]
                firm = row.get('Firm', 'N/A')
                to_grade = row.get('ToGrade', 'N/A')
                from_grade = row.get('FromGrade', 'N/A')
                action = row.get('Action', 'N/A')
                action_cn = {"up": "上调", "down": "下调", "main": "维持", "reit": "重申", "init": "首次覆盖"}.get(action, action)
                target = row.get('currentPriceTarget')
                target_s = f"${target:.0f}" if not is_nan(target) else "N/A"
                lines.append(f"| {date} | {firm} | {to_grade} | {from_grade} | {action_cn} | {target_s} |")
            lines.append("")
    except Exception:
        pass

    # ── 推荐分布 ──
    try:
        rec = stock.recommendations
        if rec is not None and not rec.empty:
            lines.append("### 推荐评级分布")
            lines.append("| 期间 | 强烈买入 | 买入 | 持有 | 卖出 | 强烈卖出 |")
            lines.append("|------|----------|------|------|------|----------|")
            for idx, row in rec.iterrows():
                period = row.get('period', f'Row {idx}')
                sb = int(row.get('strongBuy', 0))
                b = int(row.get('buy', 0))
                h = int(row.get('hold', 0))
                s = int(row.get('sell', 0))
                ss = int(row.get('strongSell', 0))
                lines.append(f"| {period} | {sb} | {b} | {h} | {s} | {ss} |")
            lines.append("")
    except Exception:
        pass

    lines.append("---")
    lines.append(f"*数据更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}*")

    return "\n".join(lines)


def fetch_financials(ticker):
    """Fetch and save financial data for a single company."""
    print(f"[财务] Fetching {ticker}...")

    # 港股/特殊ticker映射
    try:
        import sys as _sys
        _sys.path.insert(0, str(DB_DIR))
        from companies import get_yf_ticker, is_private
        yf_ticker = get_yf_ticker(ticker)
        if is_private(ticker):
            print(f"  ⏭ {ticker} is private company, skipping financials")
            return False
    except ImportError:
        yf_ticker = ticker

    if yf_ticker != ticker:
        print(f"  Using yfinance ticker: {yf_ticker} (mapped from {ticker})")

    company_dir = financial_output_dir(ticker)
    company_dir.mkdir(parents=True, exist_ok=True)

    stock = yf.Ticker(yf_ticker)
    fp = fmp_profile(ticker)

    # Write profile.md
    profile_md = build_profile(ticker, stock, fp)
    (company_dir / "profile.md").write_text(profile_md, encoding="utf-8")
    print(f"  ✓ profile.md")

    # Write financials.md
    financials_md = build_financials(ticker, stock, fp)
    (company_dir / "financials.md").write_text(financials_md, encoding="utf-8")
    print(f"  ✓ financials.md")

    return True


if __name__ == "__main__":
    tickers = sys.argv[1:] if len(sys.argv) > 1 else ["APP"]
    for t in tickers:
        try:
            fetch_financials(t)
        except Exception as e:
            print(f"  ✗ {t}: {e}")
            import traceback
            traceback.print_exc()
