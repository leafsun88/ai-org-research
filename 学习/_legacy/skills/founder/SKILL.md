---
name: founder
description: 创始人/CEO社交媒体与公开言论搜索 — 推文、采访、演讲、内部人交易
argument-hint: TICKER "CEO Name"
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

# /founder - 创始人/CEO社交媒体与公开言论搜索

搜索公司创始人/CEO在Twitter(X)、LinkedIn、公开演讲、采访中的观点和动态。

## 信源置信度标签

| 来源 | S标签 | E标签 |
|------|-------|-------|
| CEO推文（本人发） | S3 | E2 |
| CEO播客/采访发言 | S3 | E3 |
| CEO公开演讲 | S3 | E3 |
| 公司官方博客/PR | S4 | E3 |
| 媒体采访报道 | S2 | E2 |
| LinkedIn帖子 | S3-S4 | E2 |
| Insider交易 | S5 | E4 |

**所有输出文件YAML frontmatter必须包含 `credibility` 和 `evidence` 字段。**

## 使用方式
```
/founder APP "Adam Foroughi"
/founder NVDA "Jensen Huang"
```

## 参数
- $ARGUMENTS: 格式为 "TICKER \"CEO Name\""

## 执行步骤

### 1. 确认CEO身份
从 `vault/companies/{slug}/discovery/profile.md` 读取CEO信息。如果没有profile，先搜索确认。

### 2. 搜索CEO的Twitter/X账号
- WebSearch: `"{CEO Name}" twitter site:x.com OR site:twitter.com`
- WebSearch: `"{CEO Name}" @{猜测的handle} {CompanyName}`
- 找到账号后，搜索其近期推文和互动

### 3. 搜索CEO近期推文/观点
- `"{CEO Name}" site:x.com {CompanyName} 2026`
- `"{CEO Name}" site:x.com AI OR growth OR product`
- `from:{twitter_handle}` (如果找到了handle)

### 4. 搜索CEO公开采访
- `"{CEO Name}" interview 2025 OR 2026`
- `"{CEO Name}" CNBC OR Bloomberg OR podcast`
- `"{CEO Name}" keynote OR conference OR presentation`
- `"{CEO Name}" earnings call comments`

### 5. 搜索CEO在LinkedIn的动态
- `"{CEO Name}" site:linkedin.com {CompanyName}`

### 6. 搜索其他高管的公开言论
- `"{CompanyName}" CTO OR CFO interview 2025 OR 2026`
- `"{CompanyName}" management conference presentation`

### 7. 搜索公司官方博客/PR
- `site:{company_website}/blog`
- `"{CompanyName}" press release 2026`
- `"{CompanyName}" product announcement`

### 8. 整理并保存
保存到 `vault/companies/{slug}/discovery/sources/founder_voice.md`

格式：
```markdown
# {TICKER} 创始人/管理层声音

## CEO社交媒体
- **Twitter**: @{handle} (followers: XX)
- **LinkedIn**: [link]
- **最近活跃度**: 每天/每周/不活跃

## 近期推文要点
### [日期] [推文摘要]
- 关键信号: ...
- 链接: ...

## 公开采访与演讲
### [日期] [采访标题] - [媒体]
- 关键观点: ...
- 来源: [URL]

## 其他高管动态
...

## 公司官方动态
...
```

## 高频信号关注点
- CEO是否在卖股票的同时公开唱多？（言行不一致信号）
- CEO社交媒体活跃度是否突然变化？
- 是否有战略方向变化的暗示？
- 是否在回应做空/质疑？
- 是否透露了财报中没有的信息？
