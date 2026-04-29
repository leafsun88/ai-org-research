"""
Daily Signals — 批量价格信号采集
================================
用yfinance一次下载所有ticker的价格数据，计算技术指标，
输出 {TICKER}/signals/{date}_price.md 供后续Agent搜索补充。

用法:
  python3 daily_signals.py APP NVDA POP CURSOR DUOL
  python3 daily_signals.py --all   # 读取companies.py中所有非private公司
"""

import sys
import math
import pandas as pd
import yfinance as yf
from pathlib import Path
from datetime import datetime, timedelta

DB_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(DB_DIR))
from companies import COMPANIES, get_yf_ticker, is_private, is_hk_stock


def is_nan(v):
    if v is None:
        return True
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


def compute_signals(ticker: str, hist: pd.DataFrame, date: str) -> dict:
    """从历史价格DataFrame计算当日信号指标。"""
    if hist.empty or len(hist) < 2:
        return None

    # 最新一天
    latest = hist.iloc[-1]
    prev = hist.iloc[-2]

    close = float(latest['Close'])
    prev_close = float(prev['Close'])
    change_pct = (close - prev_close) / prev_close * 100

    volume = float(latest['Volume']) if not is_nan(latest.get('Volume')) else 0

    # 均量 (20日)
    vol_20 = hist['Volume'].tail(20).mean() if len(hist) >= 20 else hist['Volume'].mean()
    vol_ratio = volume / vol_20 if vol_20 > 0 else 0

    # 50MA / 200MA
    ma50 = hist['Close'].tail(50).mean() if len(hist) >= 50 else None
    ma200 = hist['Close'].tail(200).mean() if len(hist) >= 200 else None

    vs_ma50 = ((close - ma50) / ma50 * 100) if ma50 else None
    vs_ma200 = ((close - ma200) / ma200 * 100) if ma200 else None

    # 52周高低
    hist_52w = hist.tail(252)
    high_52w = float(hist_52w['High'].max())
    low_52w = float(hist_52w['Low'].min())
    pos_52w = ((close - low_52w) / (high_52w - low_52w) * 100) if high_52w != low_52w else 50

    # 5日涨跌
    if len(hist) >= 6:
        close_5d_ago = float(hist.iloc[-6]['Close'])
        change_5d = (close - close_5d_ago) / close_5d_ago * 100
    else:
        change_5d = None

    return {
        'close': close,
        'prev_close': prev_close,
        'change_pct': change_pct,
        'volume': volume,
        'vol_ratio': vol_ratio,
        'ma50': ma50,
        'ma200': ma200,
        'vs_ma50': vs_ma50,
        'vs_ma200': vs_ma200,
        'high_52w': high_52w,
        'low_52w': low_52w,
        'pos_52w': pos_52w,
        'change_5d': change_5d,
    }


def write_price_signal(ticker: str, signals: dict, date: str, currency: str = "USD"):
    """写入 {TICKER}/signals/{date}_price.md"""
    out_dir = DB_DIR / ticker / 'signals'
    out_dir.mkdir(parents=True, exist_ok=True)

    prefix = "HK$" if currency == "HKD" else "$"

    s = signals
    vs50 = f"{s['vs_ma50']:+.1f}%" if s['vs_ma50'] is not None else "N/A"
    vs200 = f"{s['vs_ma200']:+.1f}%" if s['vs_ma200'] is not None else "N/A"
    chg5d = f"{s['change_5d']:+.1f}%" if s['change_5d'] is not None else "N/A"

    # 异常标记
    flags = []
    if abs(s['change_pct']) >= 5:
        flags.append(f"{'大涨' if s['change_pct'] > 0 else '大跌'} {s['change_pct']:+.1f}%")
    if s['vol_ratio'] >= 2.0:
        flags.append(f"放量 {s['vol_ratio']:.1f}x")
    if s['pos_52w'] >= 95:
        flags.append("接近52周新高")
    if s['pos_52w'] <= 5:
        flags.append("接近52周新低")

    flag_line = f"**异常信号**: {', '.join(flags)}" if flags else ""

    md = f"""---
ticker: {ticker}
date: {date}
type: daily_price_signal
credibility: S5
evidence: E4
currency: {currency}
---

## Price Action [S5·E4]

| Metric | Value |
|--------|-------|
| Close | {prefix}{s['close']:.2f} |
| Change | {s['change_pct']:+.2f}% |
| 5d Change | {chg5d} |
| Volume | {fmt(s['volume'], '')} ({s['vol_ratio']:.2f}x avg) |
| vs 50MA | {vs50} |
| vs 200MA | {vs200} |
| 52w High | {prefix}{s['high_52w']:.2f} |
| 52w Low | {prefix}{s['low_52w']:.2f} |
| 52w Position | {s['pos_52w']:.0f}% |

{flag_line}
"""
    filepath = out_dir / f"{date}_price.md"
    filepath.write_text(md.strip() + '\n', encoding='utf-8')
    return filepath


def main(tickers: list[str]):
    date = datetime.now().strftime('%Y-%m-%d')
    print(f"\n{'='*60}")
    print(f"  Daily Signals — Price Batch Download")
    print(f"  Date: {date}")
    print(f"  Tickers: {len(tickers)}")
    print(f"{'='*60}\n")

    # 分离: 可下载 vs 跳过
    downloadable = []
    skipped = []
    yf_map = {}  # yf_ticker -> our_ticker

    for t in tickers:
        if is_private(t):
            skipped.append((t, 'private'))
            continue
        yf_t = get_yf_ticker(t)
        yf_map[yf_t] = t
        downloadable.append(yf_t)

    if not downloadable:
        print("  No downloadable tickers.")
        return

    # 批量下载 (1年数据，一次请求)
    print(f"  Downloading {len(downloadable)} tickers...")
    try:
        data = yf.download(downloadable, period='1y', progress=False, threads=True)
    except Exception as e:
        print(f"  ERROR: yf.download failed: {e}")
        return

    success = []
    no_data = []

    for yf_t, our_t in yf_map.items():
        try:
            if len(downloadable) == 1:
                hist = data
            else:
                # 多ticker时，data是MultiIndex columns
                hist = data.xs(yf_t, level='Ticker', axis=1) if 'Ticker' in data.columns.names else data
        except (KeyError, Exception):
            no_data.append(our_t)
            continue

        if hist.empty or hist['Close'].dropna().empty:
            no_data.append(our_t)
            continue

        hist = hist.dropna(subset=['Close'])
        signals = compute_signals(our_t, hist, date)
        if signals is None:
            no_data.append(our_t)
            continue

        company = COMPANIES.get(our_t, {})
        currency = company.get('currency', 'USD')
        filepath = write_price_signal(our_t, signals, date, currency)

        flag = " ⚠" if abs(signals['change_pct']) >= 5 or signals['vol_ratio'] >= 2.0 else ""
        print(f"  ✅ {our_t}: {signals['change_pct']:+.2f}%{flag} → {filepath.name}")
        success.append(our_t)

    # Summary
    print(f"\n{'='*60}")
    print(f"  Done: {len(success)} success, {len(no_data)} no data, {len(skipped)} skipped")
    if no_data:
        print(f"  No data: {', '.join(no_data)}")
    if skipped:
        print(f"  Skipped: {', '.join(f'{t}({r})' for t,r in skipped)}")
    print(f"{'='*60}\n")

    # 输出成功列表供后续Agent使用
    print(f"SUCCESS_TICKERS={','.join(success)}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 daily_signals.py TICKER1 TICKER2 ...")
        print("       python3 daily_signals.py --all")
        sys.exit(1)

    if sys.argv[1] == '--all':
        tickers = [t for t in COMPANIES if not is_private(t)]
    else:
        tickers = sys.argv[1:]

    main(tickers)
