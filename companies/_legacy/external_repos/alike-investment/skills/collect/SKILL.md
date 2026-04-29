---
name: collect
description: 一键启动全量数据采集 — 输入公司代码即可自动采集所有财务、SEC年报、YouTube、播客、社交媒体数据
argument-hint: TICKER [CompanyName] [--cn 中文名]
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

# Discovery Database — 全量数据采集

你是数据采集调度中心。用户输入一个公司代码，你需要执行完整的数据采集流程。

## 输入解析

用户输入: `$ARGUMENTS`

解析规则:
- 第一个参数是 TICKER（如 APP, NVDA, GOOG）
- 第二个参数（可选）是英文公司名
- `--cn` 后面是中文公司名
- 如果只给了TICKER，从内置字典自动查找公司名

## 信源置信度标签（本skill涉及的来源）

所有采集的数据在YAML frontmatter中必须包含 `credibility` 和 `evidence` 字段。
参见 CLAUDE.md 中的"信源置信度标签系统"完整定义。

| 模块 | 默认S标签 | 默认E标签 |
|------|-----------|-----------|
| financials (yfinance) | S5 | E3 |
| xbrl (SEC EDGAR) | S5 | E4 |
| full_dump | S5 | E3-E4 |
| sec_filings (10-K/10-Q) | S5 | E4 |
| youtube | S1-S3 | E1-E2 |
| podcasts | S2-S3 | E2 |
| xiaoyuzhou | S2-S3 | E2 |
| social-search (Twitter) | S1-S3 | E1-E2 |
| social-search (Substack) | S2 | E2 |
| social-search (Reddit) | S1 | E1 |
| perplexity research | S1-S2 | E1-E2 |
| org-scan (SEC DEF 14A) | S5 | E4 |
| org-scan (LinkedIn) | S4 | E2 |

## 执行流程

### Step 1: 运行统一采集脚本

```bash
cd /Users/wangguanjie/Desktop/Claude\ Data/共创产品 && python3 scripts/discovery/collect.py $ARGUMENTS
```

这个脚本会并行执行以下模块:
1. **financials** — yfinance基础财务 → profile.md, financials.md
2. **xbrl** — SEC EDGAR XBRL详细指标 → financials_detailed.md
3. **full_dump** — 全量数据dump（XBRL全371指标+yfinance全报表+完整价格+持股）
4. **sec_filings** — SEC年报/季报全文下载（10-K, 10-Q）
5. **youtube** — YouTube搜索+字幕提取（20个视频）
6. **podcasts** — Apple Podcasts搜索（中英文）
7. **xiaoyuzhou** — 小宇宙播客搜索

如果需要一次采集多家公司，可使用批量入口：

```bash
cd /Users/wangguanjie/Desktop/Claude\ Data/共创产品 && python3 scripts/discovery/collect_batch.py APP NVDA
```

也支持更完整的格式：

```bash
python3 scripts/discovery/collect_batch.py "RDDT=Reddit" "NVDA|NVIDIA|英伟达"
python3 scripts/discovery/collect_batch.py --file companies.txt --continue-on-error
```

`companies.txt` 每行一家公司，支持：
- `APP`
- `RDDT=Reddit`
- `NVDA|NVIDIA|英伟达`

### Step 1.5: Perplexity深度研究

```bash
cd /Users/wangguanjie/Desktop/Claude\ Data/共创产品 && python3 scripts/discovery/fetch_perplexity.py {TICKER} "{CompanyName}" "{CEO Name}"
```

这个脚本会用Perplexity sonar-pro模型进行7个维度的深度研究:
1. **twitter_discussions** — Twitter/X上的全面讨论汇总
2. **reddit_discussions** — Reddit DD帖子和讨论全文
3. **independent_analysis** — Substack/独立分析师的深度文章
4. **management_interviews** — CEO/管理层所有公开访谈和播客出场
5. **product_technology** — 产品和技术深度分析
6. **controversies_short_reports** — 做空报告、SEC调查、争议事件
7. **competitive_landscape** — 竞争格局和行业分析
8. **financial_deep_dive** — 五年财务深度分析

输出到 `vault/companies/{slug}/discovery/sources/perplexity/` 目录。

### Step 2: 全平台社交媒体搜索

脚本执行完后，调用 `/social-search {TICKER} "{CompanyName}" "{CEO Name}"` skill，覆盖:
- Twitter/X — CEO动态、市场讨论（优先Chrome MCP，备选WebSearch）
- Substack — 深度分析文章（WebFetch全文提取）
- Reddit — 散户情绪和DD帖子（WebFetch全文提取）
- LinkedIn — 管理层职业动态

### Step 2.5: 创始人/CEO专项搜索

调用 `/founder {TICKER} "{CEO Name}"` skill，覆盖:
- CEO推文和公开言论
- 公开采访和演讲
- 播客出场记录
- 内部人交易信号

### Step 3: 补充搜索（WebSearch增强）

使用 WebSearch 工具补充搜索:

1. **最新新闻** — 搜索 "{CompanyName} latest news 2026"
2. **分析师观点** — 搜索 "{CompanyName} analyst upgrade downgrade 2026"
3. **竞争动态** — 搜索 "{CompanyName} vs competitors market share"
4. **做空/争议** — 搜索 "{CompanyName} short seller OR fraud OR SEC 2025 2026"
5. **产品战略** — 搜索 "{CompanyName} new product OR expansion 2025 2026"

将搜索结果追加到 `vault/companies/{slug}/discovery/sources/deep_search_{DATE}.md`

### Step 4: YouTube Transcript增强

对于脚本中没有获取到字幕的视频，尝试用 youtube-transcript MCP 工具重新获取:

```
mcp__youtube-transcript__get-transcript(url="https://youtube.com/watch?v=VIDEO_ID")
```

### Step 5: 生成采集总结

向用户报告:
- 成功采集了哪些数据
- 哪些模块失败了，原因是什么
- 总文件数和数据量
- 建议下一步

## 组织导向约定（Alike特化）

`/collect` 不再只负责“把数据抓下来”，还必须为组织穿透准备入口与验收：

- 自动创建 `discovery/organization/` 基础结构
- 自动创建 `discovery/sources/founder_voice.md` 占位文件，承接 `/founder`
- 自动创建 `discovery/organization/_org_scan_report.md` 和 `overview/org_structure.md` 占位文件，承接 `/org-scan`
- 自动生成 `discovery/_validation.json` 与 `discovery/_validation.md`

校验分两层：
- **采集完整性**：profile / financials / SEC / YouTube / podcasts 等是否达到最低要求
- **组织充分性**：founder voice、org scan、org structure 是否已经准备好进入 D1-D7 组织评分

特别约定：
- 非中国相关公司，`xiaoyuzhou = 0` 不视为问题
- 在 `founder/org-scan` 仍为 pending 时，不应把该公司视为“已具备高质量组织打分条件”

## 常用公司字典

| TICKER | English | 中文 |
|--------|---------|------|
| APP | AppLovin | 应用乐欣 |
| NVDA | NVIDIA | 英伟达 |
| AAPL | Apple | 苹果 |
| MSFT | Microsoft | 微软 |
| GOOG | Alphabet | 谷歌 |
| META | Meta | Meta |
| CRM | Salesforce | 赛富时 |
| SNOW | Snowflake | 雪花 |
| PLTR | Palantir | Palantir |
| CRWD | CrowdStrike | CrowdStrike |
| TTD | TradeDesk | 萃弈 |
| BABA | Alibaba | 阿里巴巴 |
| BIDU | Baidu | 百度 |

## 数据来源说明

| 来源 | 用途 | 成本 |
|------|------|------|
| yfinance | 财务报表、估值、价格 | 免费 |
| SEC EDGAR XBRL | 371个标准化财务指标 | 免费 |
| SEC EDGAR Filings | 10-K/10-Q全文 | 免费 |
| YouTube (yt-dlp) | 视频搜索+字幕提取 | 免费 |
| Apple Podcasts (iTunes API) | 播客搜索+元数据 | 免费 |
| 小宇宙 | 中文播客搜索 | 免费 |
| WebSearch | 新闻、社交媒体、分析 | 内置 |
| Chrome MCP | Twitter/X深度抓取 | 需要登录 |

## 收尾步骤（采集完成后必须执行）

采集完成后，自动生成 discovery/_summary.json：
```bash
bash skills/collect/generate-summary.sh vault/companies/{slug}
```
这个summary文件是其他skill的路由缓存——让下游skill无需扫描150+文件就知道有什么数据可用。

## 注意事项

- SEC EDGAR限速10 req/sec，脚本已内置延迟
- YouTube字幕提取依赖yt-dlp，部分视频无字幕
- 播客目前只保存元数据，转录功能待ASR接入
- Twitter/X搜索需要Chrome登录状态
- 整个流程约5-10分钟/公司
