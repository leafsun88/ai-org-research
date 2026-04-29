---
name: social-search
description: 全平台社交媒体与深度分析搜索 — Perplexity URL发现 + WebFetch全文提取
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

# /social-search — 全平台信息搜索（Perplexity + WebFetch两阶段）

两阶段架构：Phase 1用Perplexity发现URL → Phase 2用WebFetch提取全文。杜绝AI幻觉，只保存真实原文。

## 参数
$ARGUMENTS: `TICKER "CompanyName" ["CEO Name"]`

## 信源置信度标签

| 平台 | S标签 | E标签 |
|------|-------|-------|
| CEO推文 | S3 | E2 |
| Twitter分析师 | S2 | E2 |
| Twitter一般讨论 | S1 | E1 |
| Substack深度分析 | S2 | E2 |
| Reddit DD帖子 | S1 | E1-E2 |
| LinkedIn profile | S4 | E2 |
| 新闻 (CNBC/Reuters) | S2 | E3 |

**所有输出YAML frontmatter必须包含 `credibility` 和 `evidence` 字段。**

## 执行流程

### Phase 0: 准备
1. 解析TICKER, CompanyName, CEO Name
2. 如果未提供CEO，从profile.md读取
3. 创建目录: `vault/companies/{slug}/discovery/sources/` 下各子目录

### Phase 1: Perplexity URL发现（脚本自动执行）

运行:
```bash
cd /Users/wangguanjie/Desktop/Claude\ Data/共创产品 && python3 scripts/discovery/fetch_perplexity.py {TICKER} "{CompanyName}" "{CEO Name}"
```

脚本会向Perplexity发送5个搜索prompt（twitter/reddit/substack_analysis/podcasts_transcripts/news_investigations），每个只要求返回URL列表JSON。然后自动用requests抓取每个URL的全文。

结果保存到 `vault/companies/{slug}/discovery/sources/{topic}/` 各子目录。

### Phase 2: WebSearch + WebFetch补充搜索

Perplexity覆盖不全的用WebSearch补充。**并行启动多个Agent**:

#### Agent 1: Twitter/X补充
WebSearch按年份切片:
```
"{CompanyName}" OR "${TICKER}" site:x.com {year}
"{CEO Name}" site:x.com {year}
```
对高价值结果用WebFetch提取全文。
输出: `vault/companies/{slug}/discovery/sources/social/twitter_x.md`

#### Agent 2: Substack全文补充
对Perplexity发现的URL中未成功提取全文的，用WebFetch重试:
```
WebFetch(url, "Extract the COMPLETE article text...")
```
每篇独立文件: `vault/companies/{slug}/discovery/sources/substack_analysis/{author}_{slug_title}.md`

#### Agent 3: Reddit搜索
用Reddit MCP搜索:
- `get_subreddit_hot_posts("AppLovin")`
- `get_subreddit_top_posts("stocks")` → 筛选含ticker的帖子
- `get_post_content(post_id)` → 获取全文+评论

补充WebSearch:
```
"{CompanyName}" DD OR "due diligence" site:reddit.com
"${TICKER}" bull case bear case site:reddit.com
```
输出: `vault/companies/{slug}/discovery/sources/social/reddit_discussions.md`

#### Agent 4: 新闻/深度报道补充
WebSearch搜索行业媒体:
```
"{CompanyName}" site:adexchanger.com OR site:digiday.com OR site:techcrunch.com
"{CompanyName}" analysis OR investigation -paywall
```
对找到的URL用WebFetch提取全文。
输出: `vault/companies/{slug}/discovery/sources/news_investigations/`

### Phase 3: 整合
生成汇总: `vault/companies/{slug}/discovery/sources/social/key_events_timeline.md` + `vault/companies/{slug}/discovery/sources/social/sentiment_summary.md`

## 注意事项
- Perplexity只用来发现URL，不信任其生成的内容
- 全文由WebFetch或requests直接从原始网站获取
- 付费墙内容跳过（Bloomberg/WSJ/Stratechery/TheInformation）
- 每个文件YAML frontmatter必须含credibility和evidence标签

## 关键规则：禁止写摘要文件

**严格禁止以下行为**：
1. **不允许写"仅URL+摘要"的文件**。如果WebFetch或requests无法获取全文（paywall、SSL错误、403等），**不要创建文件**，只在_url_index.json中记录URL和失败原因
2. **不允许用AI总结替代原文**。文件内容必须是从网站直接提取的原始文本，不是你的改写或摘要
3. **不允许标注`fetch_status: url_only`**。这个标签的存在本身就意味着违规——应该根本不创建这个文件
4. **文件最小长度要求**：Substack文章至少1000字符，新闻文章至少500字符。低于此阈值不保存

正确做法：
- 能拿到全文 → 保存完整文件
- 拿不到全文 → 不创建文件，在_url_index.json中标注`"status": "fetch_failed", "reason": "..."`
- 部分内容（paywall截断） → 保存已获取部分，在frontmatter中标注`note: "partial content, paywalled after paragraph X"`
