---
name: private-search
description: 非上市公司深度信息搜索 — 以人为核心，先找组织核心人物，再按人展开社交媒体搜索
argument-hint: TICKER "CompanyName" ["CEO Name"]
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

# /private-search — 非上市公司深度信息搜索

非上市公司没有SEC filing和公开财务数据。核心策略：**以人为核心展开搜索**。
先找到公司的关键人物，再按人分别穿透社交媒体和公开发言，最后补充公司层面信息。

## 参数
$ARGUMENTS: `TICKER "CompanyName" ["CEO Name"]`

## 信源置信度
| 来源 | S标签 | E标签 |
|------|-------|-------|
| Crunchbase/PitchBook融资数据 | S4 | E3 |
| 创始人公开采访/播客 | S3 | E3 |
| 创始人Twitter/X | S3 | E2 |
| TechCrunch/The Verge等科技媒体 | S2 | E3 |
| Substack/博客分析 | S2 | E2 |
| Reddit/HackerNews讨论 | S1 | E1-E2 |
| GitHub/ProductHunt | S4 | E2 |
| LinkedIn profile | S4 | E2 |

## 执行流程

### Phase 1: 发现核心人物（Orchestrator）

先搜索确定公司的关键人物名单：

**目标：找到至少10人。** 不仅是创始人和C-level，还要找VP、核心工程师、早期员工、已离职关键人物。

搜索（每个都要搜）：
- `"{CompanyName}" founders co-founders team leadership`
- `"{CompanyName}" site:crunchbase.com/organization`
- `"{CompanyName}" CTO CPO COO VP engineering`
- `"{CompanyName}" key people executives`
- `"{CompanyName}" site:linkedin.com/in employees`
- `"{CompanyName}" "head of" OR "director of" OR "VP of"`
- `"{CompanyName}" engineer OR researcher site:linkedin.com`
- `"{CompanyName}" departed left former CTO OR "co-founder" OR resigned` (关注离职高管)
- `"{CompanyName}" hired OR joined OR appointed 2024 2025 2026` (新加入的关键人物)
- `"{CompanyName}" board advisor investor` (董事/顾问)

输出一份**至少10人**的名单，包括：
- 姓名、职位、是否在职
- 已知的Twitter handle或LinkedIn URL
- 为什么此人重要（创始人/核心技术/关键业务/离职信号等）

如果公开信息不足10人，扩大搜索范围：
- 搜索此公司在GitHub的贡献者
- 搜索此公司在ProductHunt的提交者
- 搜索此公司融资新闻中提到的人名
- 搜索此公司播客/采访中出现的嘉宾

创建目录: `vault/companies/{slug}/discovery/organization/`

保存名单到: `vault/companies/{slug}/discovery/organization/_people_list.md`

### Phase 2: 按人并行穿透（每人一个Agent）

对Phase 1发现的每位核心人物，**并行启动一个Agent**。每批最多4-5个。

#### 每个Person Agent的任务：

```
穿透 {name} ({title}) at {company}

搜索以下内容，对每个结果用WebFetch提取全文：

### 1. 社交媒体原文 [S3·E2]
- WebSearch: "{name}" site:x.com OR site:twitter.com
- WebSearch: "{name}" site:linkedin.com
- 提取: Twitter handle、近期推文原文、LinkedIn简介

### 2. 公开采访/播客/演讲 [S3·E3]
- WebSearch: "{name}" interview 2024 2025 2026
- WebSearch: "{name}" podcast 2024 2025 2026
- WebSearch: "{name}" site:youtube.com
- WebSearch: "{name}" keynote OR conference OR talk
- 对找到的URL用WebFetch提取全文/transcript

### 3. 背景和职业轨迹 [S4·E2]
- WebSearch: "{name}" biography career background education
- WebSearch: "{name}" MIT OR Stanford OR {school}
- WebSearch: "{name}" before "{company}" OR previous company
- 提取: 教育、前公司、创业历史

### 4. 关于公司的观点 [S3·E3]
- WebSearch: "{name}" "{company}" vision OR future OR strategy
- WebSearch: "{name}" "{company}" product OR technology OR AI
- 提取: 此人对公司方向的公开表态

### 5. 松散信息 [S1-S2·E1-E2]
- WebSearch: "{name}" net worth OR billionaire
- WebSearch: "{name}" controversy OR criticism
- WebSearch: "{name}" angel investor OR advisor OR board
- WebSearch: "{name}" "{company}" culture OR hiring OR team
```

保存到: `vault/companies/{slug}/discovery/organization/{safe_name}.md`
如果是已离职人员: `vault/companies/{slug}/discovery/organization/{safe_name}_departed.md`

YAML frontmatter:
```yaml
---
ticker: {TICKER}
type: person_profile
name: "{name}"
title: "{title}"
status: active | departed
credibility: "mixed S1-S5"
evidence: "mixed E1-E4"
---
```

每段搜索结果用 > 引用块保留原文。

### Phase 3: 公司层面信息补充（2个并行Agent）

#### Agent A: 融资+产品+竞争
搜索:
- `"{CompanyName}" funding round valuation 2024 2025 2026`
- `"{CompanyName}" revenue ARR growth`
- `"{CompanyName}" site:crunchbase.com`
- `"{CompanyName}" site:techcrunch.com`
- `"{CompanyName}" vs {competitors} comparison`
- `"{CompanyName}" pricing enterprise`
- `"{CompanyName}" site:producthunt.com`
- `"{CompanyName}" site:github.com`

输出: `vault/companies/{slug}/discovery/sources/social/funding_product.md`

#### Agent B: 社区+媒体+中文
搜索:
- `"{CompanyName}" site:news.ycombinator.com`
- `"{CompanyName}" site:reddit.com`
- `"{CompanyName}" site:substack.com`
- `"{CompanyName}" site:medium.com`
- `"{CompanyName}" site:forbes.com OR site:fortune.com`
- `"{CompanyName}" site:cnbc.com`
- `"{CompanyName}" controversy OR criticism OR problem`
- `"{CompanyName}" 分析 评测 site:36kr.com OR site:sspai.com`

输出: `vault/companies/{slug}/discovery/sources/social/community_media.md` + `vault/companies/{slug}/discovery/sources/social/cn_sources.md`

### Phase 4: 汇总

生成: `vault/companies/{slug}/discovery/organization/_org_scan_report.md`

包含:
- 组织关系结构讲述（谁是谁，什么角色，什么关系）
- 人物来源分析（这群人怎么凑到一起的）
- 离职/变动信号（谁走了，为什么）
- 关键发现（每人1-2条最重要的信号）
- 信息缺口（哪些人信息不足，需要进一步挖掘）

## 目录结构

```
vault/companies/{slug}/discovery/
├── organization/
│   ├── _people_list.md           # 人物名单
│   ├── _org_scan_report.md       # 汇总报告
│   ├── {ceo_name}.md             # CEO穿透
│   ├── {cpo_name}.md             # CPO穿透
│   ├── {coo_name}.md             # COO穿透
│   └── {cto_name}_departed.md    # 离职CTO穿透
├── sources/
│   ├── social/
│   │   ├── funding_product.md
│   │   ├── community_media.md
│   │   └── cn_sources.md
│   ├── youtube/                  # (由collect填充)
│   ├── podcasts/                 # (由collect填充)
│   └── podcasts_transcripts/     # (由百炼转录填充)
└── profile.md
```

## 注意事项
- **以人为核心**：非上市公司的关键信息往往藏在创始人的公开发言里
- **离职高管特别关注**：联创离职是重大信号，必须深挖原因
- HackerNews对爬虫友好，优先用WebFetch
- Reddit和SeekingAlpha会block，只保留搜索摘要
- 付费墙内容跳过
- 每个文件YAML frontmatter必须含credibility和evidence标签

## 关键规则：禁止写摘要文件

**严禁创建"仅URL+摘要"的文件。** 如果无法获取全文，不要创建文件，只在_url_index.json中记录。
文件最小长度：Substack 1000字符，新闻 500字符。低于此阈值不保存。
不允许用AI总结替代原文。文件内容必须是网站直接提取的原始文本。
