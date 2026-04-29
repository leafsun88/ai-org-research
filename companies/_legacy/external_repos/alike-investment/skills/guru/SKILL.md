---
name: guru
description: 投资大师持仓与观点搜索 — 13F持仓、做空报告、分析师观点
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

# /guru — 投资大师观点搜索

搜索知名投资人、对冲基金经理、分析师对特定公司的观点和持仓变化。

## 参数
$ARGUMENTS: "TICKER CompanyName"

## 信源置信度标签

| 来源 | S标签 | E标签 |
|------|-------|-------|
| 13F filing (SEC) | S5 | E4 |
| 做空机构公开报告 | S2 | E2-E3 |
| 卖方分析师报告 | S1 | E2 |
| 投资人公开发言 | S2-S3 | E2 |
| 播客/视频讨论 | S2 | E2 |
| 中文投资社区 | S1 | E1 |

**输出文件YAML frontmatter必须包含 `credibility` 和 `evidence` 字段。**

## 执行步骤

### 1. 搜索大师持仓 (13F) [S5·E4]
- `"{CompanyName}" 13F hedge fund holdings`
- `"{TICKER}" institutional investor position`
- `"{TICKER}" whale investor bought sold`

### 2. 搜索知名投资人观点 [S2-S3·E2]
逐一搜索:
- Buffett/Berkshire, ARK/Cathie Wood, Michael Burry
- Bill Ackman, Druckenmiller, Tiger Global, Coatue
- D1 Capital, Altimeter, Appaloosa/Tepper

### 3. 做空机构报告 [S2·E2-E3]
- `"{CompanyName}" short seller report`
- `"{TICKER}" short interest Muddy Waters Hindenburg Citron`
- `"{CompanyName}" bear case analysis`

### 4. 卖方分析师 [S1·E2]
- `"{TICKER}" Morgan Stanley Goldman Sachs equity research`
- `"{CompanyName}" analyst upgrade downgrade`

### 5. 播客/视频讨论 [S2·E2]
- `"{CompanyName}" "All-In Podcast"`
- `"{CompanyName}" "Aswath Damodaran"`

### 6. 中文投资社区 [S1·E1]
- `"{CompanyName}" 投资分析 雪球`

## 保存

保存到 `vault/companies/{slug}/discovery/sources/guru_opinions.md`

每条标注置信度标签和来源URL。
