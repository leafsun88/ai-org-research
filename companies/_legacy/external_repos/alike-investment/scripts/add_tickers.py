#!/usr/bin/env python3
"""给 portfolio.json 中的88家公司添加 ticker 字段"""

import json
import sys
from collections import OrderedDict

PORTFOLIO_PATH = "presentation/data/portfolio.json"

# slug -> ticker 映射（手动校对）
TICKER_MAP = {
    "transdigm": "TDG",
    "veeva": "VEEV",
    "duolingo": "DUOL",
    "cursor": "PRIVATE",
    "stripe": "PRIVATE",
    "amd": "AMD",
    "datadog": "DDOG",
    "broadcom": "AVGO",
    "axon": "AXON",
    "palantir": "PLTR",
    "bytedance": "PRIVATE",
    "crowdstrike": "CRWD",
    "rippling": "PRIVATE",
    "sea-limited": "SE",
    "kanzhun": "BZ",
    "vercel": "PRIVATE",
    "adobe": "ADBE",
    "trade-desk": "TTD",
    "meituan": "3690.HK",
    "airbnb": "ABNB",
    "snowflake": "SNOW",
    "reddit": "RDDT",
    "nubank": "NU",
    "netease": "NTES",
    "roku": "ROKU",
    "affirm": "AFRM",
    "trip-com": "TCOM",
    "spotify": "SPOT",
    "doordash": "DASH",
    "salesforce": "CRM",
    "mercadolibre": "MELI",
    "cohere": "PRIVATE",
    "amazon": "AMZN",
    "booking": "BKNG",
    "servicenow": "NOW",
    "atlassian": "TEAM",
    "canva": "PRIVATE",
    "pinterest": "PINS",
    "instacart": "CART",
    "fortinet": "FTNT",
    "lemonade": "LMND",
    "take-two": "TTWO",
    "bilibili": "BILI",
    "coinbase": "COIN",
    "figma": "PRIVATE",
    "zscaler": "ZS",
    "cloudflare": "NET",
    "hubspot": "HUBS",
    "kuaishou": "1024.HK",
    "tencent-music": "TME",
    "wix": "WIX",
    "pop-mart": "9992.HK",
    "klaviyo": "KVYO",
    "okta": "OKTA",
    "servicetitan": "TTAN",
    "sentinelone": "S",
    "block-square": "XYZ",
    "elastic": "ESTC",
    "confluent": "CFLT",
    "dynatrace": "DT",
    "robinhood": "HOOD",
    "etsy": "ETSY",
    "arm": "ARM",
    "carvana": "CVNA",
    "mongodb": "MDB",
    "toast": "TOST",
    "gitlab": "GTLB",
    "snap": "SNAP",
    "asana": "ASAN",
    "hims": "HIMS",
    "plaid": "PRIVATE",
    "roper": "ROP",
    "tesla": "TSLA",
    "unity": "U",
    "mobvista": "1860.HK",
    "roblox": "RBLX",
    "paypal": "PYPL",
    "twilio": "TWLO",
    "taboola": "TBLA",
    "grab": "GRAB",
    "appfolio": "APPF",
    "digitalocean": "DOCN",
    "workday": "WDAY",
    "magnite": "MGNI",
    "match-group": "MTCH",
    "pubmatic": "PUBM",
    "criteo": "CRTO",
    "sprinklr": "CXM",
}

def main():
    with open(PORTFOLIO_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    companies = data["companies"]

    print(f"共 {len(companies)} 家公司\n")
    print(f"{'#':>3s}  {'slug':40s}  {'name':35s}  {'ticker':10s}")
    print("-" * 95)

    missing = []
    for i, company in enumerate(companies):
        slug = company["slug"]
        ticker = TICKER_MAP.get(slug)
        if ticker is None:
            missing.append(slug)
            ticker = "???"
        print(f"{i+1:3d}  {slug:40s}  {company['name']:35s}  {ticker}")

    if missing:
        print(f"\n⚠️  缺少 {len(missing)} 家公司的ticker映射: {missing}")
        sys.exit(1)

    print(f"\n✅ 全部 {len(companies)} 家公司已匹配ticker")

    # 确认后写入
    if "--write" not in sys.argv:
        print("\n加 --write 参数执行写入")
        return

    # 添加ticker字段（放在slug后面）
    for company in companies:
        slug = company["slug"]
        ticker = TICKER_MAP[slug]

        # 重建OrderedDict，把ticker放在slug后面
        new_company = OrderedDict()
        for key, value in company.items():
            new_company[key] = value
            if key == "slug":
                new_company["ticker"] = ticker
        company.clear()
        company.update(new_company)

    with open(PORTFOLIO_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\n✅ 已写入 {PORTFOLIO_PATH}")

if __name__ == "__main__":
    main()
