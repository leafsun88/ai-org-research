---
name: signals-scan
description: 每日信号快速扫描 — 新闻、分析师、insider交易、社交媒体、竞争动态
argument-hint: TICKER
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

# /signals-scan — 每日信号扫描

对已研究公司执行快速信号扫描，5分钟内完成。

## 参数
$ARGUMENTS: TICKER

## 信源置信度标签

| 信号类型 | 典型来源 | S标签 | E标签 |
|----------|----------|-------|-------|
| SEC 8-K filing | SEC EDGAR | S5 | E4 |
| Insider交易 | SEC Form 4 | S5 | E4 |
| 分析师评级变动 | 券商报告 | S1 | E2 |
| 新闻报道 | CNBC/Reuters | S2 | E2-E3 |
| 社交媒体讨论 | Reddit/Twitter | S1 | E1 |
| 竞争对手动态 | 新闻 | S2 | E2 |

**输出文件YAML frontmatter必须包含 `credibility` 和 `evidence` 字段。**

## 执行步骤

并行搜索以下6个维度:

### 1. 最新新闻 [S2·E2-E3]
- `"{CompanyName}" news today`
- `"{TICKER}" stock news`
- `"{CompanyName}" SEC filing 8-K`

### 2. 分析师动态 [S1·E2]
- `"{TICKER}" analyst upgrade downgrade`
- `"{TICKER}" price target change`

### 3. Insider交易 [S5·E4]
- `"{TICKER}" insider buying selling SEC Form 4`

### 4. 社交媒体热度 [S1·E1]
- `"{TICKER}" reddit wallstreetbets OR investing`
- `"{CompanyName}" twitter trending`

### 5. 竞争对手动态 [S2·E2]
- `"{CompanyName}" competitor OR rival news`

### 6. 行业动态 [S2·E2]
- 根据公司所在行业搜索行业级新闻

## 保存

保存到 `vault/companies/{slug}/discovery/signals/{YYYY-MM-DD}.md`

每条信号标注重要程度（RED/YELLOW/GREEN）和置信度标签。
