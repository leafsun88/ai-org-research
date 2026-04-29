---
name: deepsearch
description: 8维度深度信息搜索 — 大师持仓、做空、创始人、产品、市场、人才、行业、中文源
argument-hint: TICKER CompanyName
---

## 路径约定（Alike Investment集成）

本skill的输出路径已适配Alike Investment的vault结构：
- 输出根目录：`vault/companies/{slug}/discovery/`（不再是 `discovery_database/{TICKER}/`）
- slug = kebab-case公司名（如 applovin, duolingo, pop-mart）
- TICKER→slug映射：查询 `vault/_index.json` 的 `tickerMap` 字段
- 如果_index.json中没有该TICKER，创建新目录并更新_index.json

所有输出路径中的 `discovery_database/{TICKER}/` 或 `{TICKER}/` 替换为 `vault/companies/{slug}/discovery/`。
例如：`APP/sources/youtube/` → `vault/companies/applovin/discovery/sources/youtube/`

所有采集数据的YAML frontmatter必须包含 `credibility: S?` 和 `evidence: E?` 字段。

# /deep-search — 深度信息搜索

对一家公司执行全网深度信息搜索，覆盖所有非财务数据源。并行跑完8个维度。

## 参数
$ARGUMENTS: "TICKER CompanyName"

## 信源置信度标签

| 维度 | 典型来源 | S标签 | E标签 |
|------|----------|-------|-------|
| 大师持仓 (13F) | SEC filing | S5 | E4 |
| 做空报告 | 做空机构发布 | S2 | E2-E3 |
| CEO声音 | 播客/采访 | S3 | E2-E3 |
| 产品技术 | 官方博客/专利 | S4-S5 | E2-E3 |
| 客户市场 | 新闻/行业报告 | S2-S4 | E2-E3 |
| 员工文化 | Glassdoor/Blind | S1 | E1 |
| 行业趋势 | 行业报告/媒体 | S2 | E2 |
| 中文源 | 雪球/36kr | S1-S2 | E1-E2 |

**输出文件YAML frontmatter必须包含 `credibility` 和 `evidence` 字段。**

## 执行步骤

请**并行**发起以下所有搜索，然后汇总结果。

### 维度1: 投资大师持仓 [S5·E4]
- `"{CompanyName}" 13F hedge fund holdings 2025 2026`
- `"ARK Invest" OR "Cathie Wood" "{TICKER}"`
- `"Tiger Global" OR "Coatue" OR "D1 Capital" "{TICKER}"`
- `"{TICKER}" institutional investor bought sold`

### 维度2: 做空与争议 [S2·E2-E3]
- `"{CompanyName}" short seller report Hindenburg Muddy Waters Citron`
- `"{CompanyName}" SEC investigation OR probe OR lawsuit`
- `"{CompanyName}" fraud OR scandal OR controversy`

### 维度3: 创始人/CEO声音 [S3·E2-E3]
从profile.md获取CEO名字:
- `"{CEO Name}" interview 2025 OR 2026`
- `"{CEO Name}" podcast OR keynote OR conference`
- `"{CEO Name}" site:x.com`

### 维度4: 产品与技术 [S4·E2-E3]
- `"{CompanyName}" product launch OR new feature 2025 2026`
- `"{CompanyName}" technology OR AI OR machine learning`
- `"{CompanyName}" patent OR innovation`

### 维度5: 客户与市场 [S2-S4·E2-E3]
- `"{CompanyName}" customer win OR partnership OR deal`
- `"{CompanyName}" market share OR TAM`
- `"{CompanyName}" vs competitor comparison`

### 维度6: 员工与文化 [S1·E1]
- `"{CompanyName}" glassdoor review OR rating`
- `"{CompanyName}" layoff OR hiring OR headcount`

### 维度7: 行业趋势 [S2·E2]
- `{industry} market outlook 2026`
- `{industry} growth trends AI`

### 维度8: 中文信息源 [S1-S2·E1-E2]
- `"{CompanyName}" site:xueqiu.com`
- `"{CompanyName}" 深度分析 OR 投资逻辑`
- `"{CompanyName}" site:36kr.com`

## 保存

保存到 `vault/companies/{slug}/discovery/sources/deep_search_{date}.md`

每条信息标注来源URL和置信度标签。最后写"关键发现总结"——按投资决策价值排序的3-5个发现。
