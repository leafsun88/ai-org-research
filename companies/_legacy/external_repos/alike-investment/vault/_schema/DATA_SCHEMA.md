# Discovery Database — 数据结构与接口文档

> 本文档供下游AI系统（Deep Thinking Engine、Winner Pattern Expert）读取和解析Discovery Database的数据。
> 所有数据为Markdown格式，每个文件以YAML frontmatter开头，包含机器可读的元数据字段。

---

## 1. 目录结构

每家公司一个目录，以股票代码命名。目录结构固定如下：

```
discovery_database/
├── {TICKER}/                          # 每家公司一个目录（如 APP/, NVDA/, POP/）
│   │
│   ├── profile.md                     # 公司基本面：行业、市值、员工数、CEO、总部
│   ├── financials.md                  # 财务数据：损益表、资产负债表、现金流、估值、分析师预期
│   ├── financials_detailed.md         # XBRL精选指标（季度+年度，SEC EDGAR来源）
│   ├── data_full_xbrl.md             # XBRL全量371个标准化指标
│   ├── data_full_statements.md       # yfinance全部财务报表行（完整dump）
│   ├── data_price_history.md         # 完整历史股价（日线/周线/月线，IPO至今）
│   ├── data_holders.md               # 机构持股+insider持股+分析师覆盖
│   │
│   ├── organization/                  # 组织穿透
│   │   ├── _org_scan_report.md       # 汇总报告：组织关系结构+关键发现
│   │   ├── overview/
│   │   │   └── org_structure.md      # 高管名单（C-Suite + VP + 董事会）
│   │   ├── c_suite/
│   │   │   ├── {ceo_name}.md         # 每位C-level高管的完整穿透
│   │   │   └── ...
│   │   ├── board/
│   │   │   ├── {director_name}.md    # 每位董事的完整穿透
│   │   │   └── ...
│   │   ├── vp_level/
│   │   │   └── ...                   # VP级别高管穿透（如有）
│   │   └── departed/
│   │       └── {name}.md             # 已离职关键高管
│   │
│   ├── sources/                       # 原始信息源
│   │   ├── earnings/                 # SEC 10-K/10-Q全文（每份filing一个文件）
│   │   │   ├── 2026-02-19_10-K.md
│   │   │   ├── 2025-11-05_10-Q.md
│   │   │   └── ...
│   │   ├── youtube/                  # YouTube视频transcript
│   │   │   ├── 2026-03-31_AppLovin-Q4-Earnings-Call.md
│   │   │   └── ...
│   │   ├── podcasts/                 # 播客元数据（标题、日期、音频URL、描述）
│   │   │   ├── 2026-02-22_AppLovin-Q4-Earnings-Analysis.md
│   │   │   └── ...
│   │   ├── podcasts_transcripts/     # 播客转录全文（百炼Paraformer-v2引擎）
│   │   │   ├── 2026-02-22_AppLovin-Q4-Earnings-Analysis.md
│   │   │   └── ...
│   │   ├── social/                   # 社交媒体汇总
│   │   │   ├── twitter_x.md         # Twitter推文汇总
│   │   │   ├── reddit_discussions.md # Reddit帖子汇总
│   │   │   ├── linkedin.md          # LinkedIn管理层动态
│   │   │   ├── substack_*.md        # Substack文章全文（每篇独立文件）
│   │   │   ├── key_events_timeline.md # 关键事件时间线
│   │   │   └── sentiment_summary.md  # 情绪分析汇总
│   │   ├── substack_analysis/        # Substack独立分析文章（Perplexity发现+WebFetch全文）
│   │   │   └── {author}_{slug}.md
│   │   ├── news_investigations/      # 新闻深度报道
│   │   │   └── ...
│   │   └── perplexity/              # Perplexity AI研究结果（二手信源，需交叉验证）
│   │       ├── 2026-04-01_twitter_discussions.md
│   │       ├── 2026-04-01_reddit_discussions.md
│   │       ├── 2026-04-01_product_technology.md
│   │       └── ...
│   │
│   ├── signals/                      # 每日信号（按日期滚动，每天一个文件）
│   │   └── YYYY-MM-DD.md
│   │
│   └── _podcast_episodes.json        # 播客元数据索引（JSON，供转录脚本使用）
│
├── scripts/                           # 采集脚本（不含数据）
├── companies.py                       # 公司注册表
└── DATA_SCHEMA.md                     # 本文档
```

---

## 2. YAML Frontmatter规范

每个.md文件以YAML frontmatter开头（`---`包围），包含机器可读的元数据。

### 2.1 必选字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `ticker` | string | 股票代码，如 "APP", "NVDA" |
| `type` | string | 文件类型，见§2.3类型枚举 |

### 2.2 常见字段

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `date` | string | 数据日期或发布日期 | "2026-02-19" |
| `last_updated` | string | 最后更新时间 | "2026-03-31" |
| `credibility` | string | 信源置信度标签 | "S5", "S3", "S1-S3" |
| `evidence` | string | 材料置信度标签 | "E4", "E2", "E1-E2" |
| `data_source` | string | 数据来源 | "Yahoo Finance", "SEC EDGAR" |
| `url` | string | 原始来源URL | "https://..." |
| `chars` | integer | 正文字符数 | 65389 |
| `title` | string | 标题 | "AppLovin Q4 2025..." |
| `author` | string | 作者 | "Komodo Capital" |

### 2.3 type字段枚举

| type值 | 对应目录 | 说明 | 默认S·E标签 |
|--------|----------|------|-------------|
| `company_profile` | `profile.md` | 公司基本面 | S5·E3 |
| `financials` | `financials.md` | 财务报表+估值 | S5·E3 |
| `financials_xbrl` | `financials_detailed.md` | XBRL精选指标 | S5·E4 |
| `sec_filing` | `sources/earnings/` | SEC 10-K/10-Q全文 | S5·E4 |
| `youtube` | `sources/youtube/` | YouTube视频transcript | S1-S3·E1-E2 |
| `podcast_metadata` | `sources/podcasts/` | 播客元数据（无全文） | S2·E1 |
| `podcast_transcript` | `sources/podcasts_transcripts/` | 播客转录全文 | S2-S3·E2 |
| `substack` | `sources/substack_analysis/` | Substack分析文章全文 | S2·E2 |
| `twitter` | `sources/social/twitter_x.md` | Twitter推文汇总 | S1-S3·E1-E2 |
| `reddit` | `sources/social/reddit_*.md` | Reddit讨论 | S1·E1 |
| `news` | `sources/news_investigations/` | 新闻/深度报道 | S2·E2-E3 |
| `perplexity_research` | `sources/perplexity/` | AI研究结果（需交叉验证） | S1-S2·E1-E2 |
| `person_profile` | `organization/*/` | 高管个人穿透 | mixed S1-S5 |
| `org_overview` | `organization/overview/` | 组织架构 | S5·E4 |
| `org_scan_report` | `organization/` | 组织穿透汇总 | mixed |
| `signal` | `signals/` | 每日信号 | mixed |

---

## 3. 信源置信度标签系统

所有数据均标注信源置信度。下游系统应根据标签调整权重。

### 3.1 信源置信度（Source Credibility）

| 标签 | 定义 | 权重建议 |
|------|------|----------|
| **S5** | 客观事实·直接导出（SEC filing、交易所数据） | 100% |
| **S4** | 客观事实·间接推导（LinkedIn员工数→推导组织变化） | 90% |
| **S3** | 主观一手信源（CEO发言、管理层访谈） | 80% |
| **S2** | 主观二手信源（分析师观点、媒体深度报道、Substack） | 60% |
| **S1** | 主观三手信源（Reddit讨论、自媒体、市场传闻） | 30% |

### 3.2 材料置信度（Evidence Dimensionality）

| 标签 | 定义 | 权重建议 |
|------|------|----------|
| **E4** | 多维度×多信源交叉验证 | 100% |
| **E3** | 多维度×单信源 或 单维度×多信源 | 75% |
| **E2** | 单维度×单信源（有具体证据） | 50% |
| **E1** | 单维度×单信源（仅观点无证据） | 25% |

### 3.3 置信度计算公式

```
Confidence% = S_weight × E_weight × 100
```

示例：
- SEC 10-K filing (S5·E4) → 100% × 100% = **100%**
- CEO播客发言 (S3·E3) → 80% × 75% = **60%**
- Substack分析 (S2·E2) → 60% × 50% = **30%**
- Reddit匿名观点 (S1·E1) → 30% × 25% = **7.5%**

### 3.4 数据源→默认标签映射表

| 数据源 | S标签 | E标签 | 说明 |
|--------|-------|-------|------|
| SEC EDGAR (10-K/10-Q/DEF 14A) | S5 | E4 | 法定披露 |
| SEC EDGAR XBRL | S5 | E4 | 结构化财务指标 |
| SEC Form 4 (insider trading) | S5 | E4 | insider交易记录 |
| yfinance | S5 | E3 | 交易所数据，偶有延迟 |
| Earnings Call Transcript | S3 | E3 | 管理层一手发言 |
| CEO推文 | S3 | E2 | 一手但可能有PR包装 |
| CEO播客/采访 | S3 | E3 | 一手深度发言 |
| 公司IR页面 | S4 | E3 | 选择性披露 |
| Substack | S2 | E2 | 独立分析师 |
| 新闻 (CNBC/Reuters) | S2 | E3 | 有事实核查 |
| Reddit DD帖子 | S1 | E1-E2 | 匿名 |
| Twitter一般讨论 | S1 | E1 | 噪音极高 |
| LinkedIn profile | S4 | E2 | 本人维护 |
| Perplexity研究 | S1-S2 | E1-E2 | AI生成，需交叉验证 |
| 播客转录 (Paraformer-v2) | 继承原播客 | 继承原播客 | 转录引擎不影响S/E |

---

## 4. 核心文件Schema

### 4.1 profile.md

公司基本面。字段通过Markdown表格呈现。

```yaml
---
ticker: APP
last_updated: 2026-03-31
data_source: Yahoo Finance
credibility: S5
evidence: E3
---
```

**主要数据节点**：
- 基本信息：行业、市值、员工数、CEO、总部、上市交易所、IPO日期
- 公司简介：业务描述（truncated to ~500字）

### 4.2 financials.md

财务报表+估值指标。数据以Markdown表格呈现。

```yaml
---
ticker: APP
last_updated: 2026-03-31
data_source: Yahoo Finance + FMP
credibility: S5
evidence: E3
---
```

**主要数据节点**（均为Markdown表格）：
- 估值快照：市值、P/E、P/S、P/B、EV/EBITDA、PEG、52周范围、Beta
- 年度损益表：营收、毛利率、研发费用、营业利润率、净利润率、EPS（近5年）
- 季度损益表：同上（近8个季度）
- 年度资产负债表：现金、债务、股东权益（近5年）
- 季度资产负债表：同上（近6季度）
- 年度现金流量表：经营性现金流、FCF、SBC、回购（近5年）
- 季度现金流量表：同上
- TTM关键指标：Rule of 40、ROE、ROA、人均营收等
- Earnings Beat/Miss历史：实际EPS vs 预期EPS
- 分析师预期：目标价、营收预期、EPS预期、评级分布、近期评级变动

### 4.3 sources/earnings/{date}_{form}.md

SEC filing全文。单文件可达150KB。

```yaml
---
ticker: APP
type: sec_filing
form: 10-K         # 10-K=年报, 10-Q=季报
date: 2026-02-19   # filing日期
accession: 0001751008-26-000010
url: https://www.sec.gov/Archives/edgar/data/...
text_length: 150048
credibility: S5
evidence: E4
---
```

**内容**：SEC filing的纯文本提取，包含完整的财务报表、管理层讨论（MD&A）、风险因素等。HTML标签已剥离。

### 4.4 sources/youtube/{date}_{title}.md

YouTube视频transcript。

```yaml
---
ticker: APP
type: youtube
title: "视频标题"
channel: "频道名"
date: 2026-03-31
url: https://www.youtube.com/watch?v=VIDEO_ID
transcript_method: yt-dlp_subtitle  # yt-dlp自动字幕 或 manual_subtitle（人工字幕）
language: en
chars: 65389
credibility: S1-S3    # 取决于视频作者
evidence: E1-E2
---
```

**内容**：视频的完整转录文本。自动生成字幕可能有拼写错误，但内容完整。

### 4.5 sources/podcasts_transcripts/{date}_{title}.md

播客转录全文。

```yaml
---
ticker: APP
type: podcast_transcript
title: "播客标题"
podcast: "节目名"
date: 2026-02-22
audio_url: https://...mp3
language: en
chars: 8180
credibility: S2-S3
evidence: E2
transcription_engine: dashscope_paraformer_v2
---
```

**内容**：播客音频的完整转录文本。由阿里云百炼Paraformer-v2引擎生成。可能包含贴片广告内容。英文/中文均支持。

### 4.6 sources/substack_analysis/{author}_{slug}.md

Substack独立分析文章全文。

```yaml
---
ticker: APP
type: substack
title: "文章标题"
author: "作者名"
date: 2024-06-27
url: https://xxx.substack.com/p/article-slug
credibility: S2
evidence: E2
chars: 7842
---
```

**内容**：文章原文全文。部分文章可能因paywall截断，frontmatter中会标注`note: paywalled`。

### 4.7 organization/*/{name}.md

高管个人穿透。

```yaml
---
ticker: APP
type: person_profile
name: "Adam Foroughi"
title: "CEO, Co-Founder"
credibility: "mixed S1-S5"
evidence: "mixed E1-E4"
last_updated: 2026-04-01
---
```

**内容结构**（固定章节）：
1. **基本身份** [S4·E2] — 全名、年龄、教育、LinkedIn
2. **完整职业轨迹** [S4·E2-E3] — 每段经历含公司、职位、时间、成就
3. **在当前公司的角色** [S3-S5·E2-E4] — 负责什么、推动了什么
4. **人脉网络** [S4·E2] — 与谁有共事关系、顾问/董事席位
5. **争议/负面信息** [S2-S5·E2-E4] — 诉讼、SEC记录、负面报道
6. **关键发现与信号** — 正面/负面/值得追踪

每节标注了各自的S·E标签。搜索结果以引用块（`>`）保留原文。

### 4.8 organization/_org_scan_report.md

组织穿透汇总报告。

**内容结构**：
1. **组织关系结构** — 用文字描述权力结构、汇报关系、核心团队
2. **人才来源分析** — 高管来自哪些公司、招聘模式
3. **关键发现** — 正面信号（团队稳定性、人才质量）和负面信号（insider卖出、法律风险）
4. **组织变动时间线** — 按时间排列的人事变动
5. **最值得关注的人物** — 推荐深入研究的高管

---

## 5. 数据质量说明

### 5.1 已知完整性

| 数据类型 | 完整性 | 说明 |
|----------|--------|------|
| 财务报表 (yfinance) | 近4-5年 | yfinance限制，IPO前无数据 |
| XBRL指标 | 371个概念 | SEC EDGAR全量 |
| SEC Filing | IPO至今全部10-K/10-Q | 每份~150KB |
| 价格历史 | IPO至今日线 | 含周线/月线 |
| YouTube transcript | 14-20个视频 | 取决于搜索结果，自动字幕 |
| 播客元数据 | 40-60个episode | iTunes API搜索，可能遗漏 |
| 播客转录 | 部分（进行中） | 依赖音频URL可达性 |
| 组织穿透 | C-Suite + Board + 已离职 | VP级别待补充 |

### 5.2 已知局限

1. **港股/非美股公司**：无SEC filing、无XBRL数据、无insider交易记录。仅有yfinance财务+媒体搜索
2. **Substack**：部分文章paywall，只能获取免费内容
3. **Twitter/X**：WebSearch对Twitter索引有限，Chrome MCP可补充但需登录
4. **播客转录**：Paraformer-v2偶尔拼写错误（如"Foroughi"→"ferroi"），音频redirect可能失败
5. **Perplexity研究结果**：AI生成内容，可能包含幻觉，必须交叉验证后使用
6. **时效性**：财务数据季度更新，社交媒体数据为采集时刻的快照

---

## 6. 读取指南（给下游AI系统）

### 6.1 推荐读取顺序

对一家公司进行分析时，建议按以下顺序读取：

1. **profile.md** → 了解公司是什么
2. **financials.md** → 了解公司的财务状况和估值
3. **organization/_org_scan_report.md** → 了解管理团队
4. **sources/earnings/ 最新的10-K** → 了解业务细节和风险
5. **sources/youtube/ 和 sources/podcasts_transcripts/** → 管理层的声音
6. **sources/social/** → 市场情绪和外部观点
7. **data_full_xbrl.md** → 需要精确财务数据时查阅

### 6.2 按分析目的的读取路径

| 分析目的 | 读取文件 | 优先S标签 |
|----------|----------|-----------|
| 基本面判断 | financials.md → data_full_xbrl.md → 最新10-K | S5 |
| 管理层质量评估 | _org_scan_report.md → c_suite/*.md → earnings transcript | S3-S5 |
| 市场情绪判断 | twitter_x.md → reddit_discussions.md → substack_*.md | S1-S2 |
| 风险识别 | perplexity/controversies_short_reports.md → 10-K风险因素 → social/ | S1-S5 |
| 竞争分析 | perplexity/competitive_landscape.md → 行业播客/YouTube | S2-S3 |
| 估值判断 | financials.md (分析师预期) → substack_*.md → data_price_history.md | S2-S5 |

### 6.3 解析YAML frontmatter

```python
import yaml

def parse_frontmatter(md_text: str) -> tuple[dict, str]:
    """解析Markdown文件，返回(frontmatter_dict, body_text)"""
    if md_text.startswith('---'):
        parts = md_text.split('---', 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return meta, body
    return {}, md_text
```

### 6.4 过滤低置信度数据

```python
S_WEIGHT = {'S5': 1.0, 'S4': 0.9, 'S3': 0.8, 'S2': 0.6, 'S1': 0.3}
E_WEIGHT = {'E4': 1.0, 'E3': 0.75, 'E2': 0.5, 'E1': 0.25}

def confidence(s_tag: str, e_tag: str) -> float:
    """计算置信度百分比"""
    # 处理范围标签如 "S1-S3"
    if '-' in s_tag:
        s_tag = s_tag.split('-')[0]  # 取最低值（保守）
    if '-' in e_tag:
        e_tag = e_tag.split('-')[0]
    return S_WEIGHT.get(s_tag, 0.5) * E_WEIGHT.get(e_tag, 0.5) * 100
```

---

## 7. 采集技能（Skills）

以下Claude Code Skills可触发数据采集。它们是skill文件（`.claude/commands/*.md`），通过slash command调用。

| Skill | 命令 | 功能 | 输出 |
|-------|------|------|------|
| `/collect` | `/collect APP AppLovin` | 一键全量采集 | 全部目录 |
| `/social-search` | `/social-search APP "AppLovin" "Adam Foroughi"` | Perplexity URL发现+WebFetch全文 | sources/social/, substack_analysis/ |
| `/org-scan` | `/org-scan APP "AppLovin"` | 多Agent组织穿透 | organization/ |
| `/deep-search` | `/deep-search APP AppLovin` | 8维度深度搜索 | sources/deep_search_{date}.md |
| `/guru` | `/guru APP AppLovin` | 投资大师持仓搜索 | sources/ |
| `/founder` | `/founder APP "Adam Foroughi"` | CEO公开言论搜索 | sources/ |
| `/signals` | `/signals APP` | 每日信号扫描 | signals/{date}.md |

### 采集Pipeline

```
/collect TICKER CompanyName
    │
    ├── [Python] collect.py → 并行执行7个采集模块
    │   ├── financials (yfinance)
    │   ├── xbrl (SEC EDGAR)
    │   ├── full_dump (全量数据)
    │   ├── sec_filings (10-K/10-Q全文)
    │   ├── youtube (搜索+字幕)
    │   ├── podcasts (iTunes API搜索)
    │   └── xiaoyuzhou (小宇宙搜索)
    │
    ├── [Python] fetch_perplexity.py → 5个维度URL发现+全文提取
    │   ├── twitter → sources/twitter/
    │   ├── reddit → sources/reddit/ (目录可能不存在，回退到social/)
    │   ├── substack → sources/substack_analysis/
    │   ├── podcasts_transcripts → sources/podcasts_transcripts/
    │   └── news → sources/news_investigations/
    │
    ├── [Skill] /social-search → 并行Agent补充搜索
    │
    ├── [Python] fetch_podcast_transcript.py → 百炼ASR转录
    │
    └── [Skill] /org-scan → 多Agent组织穿透
```

---

## 8. 已采集公司

| Ticker | 公司 | 数据量 | SEC | 组织穿透 | 播客转录 |
|--------|------|--------|-----|----------|----------|
| APP | AppLovin | 5.5MB / 138文件 | 全量（20份10-K/10-Q） | 10人穿透 | 进行中 |
| POP | 泡泡玛特 (9992.HK) | 768KB / 83文件 | N/A（港股） | 待做 | 待做 |
| DUOL | Duolingo | ~1.6MB / ~90文件 | 部分 | 待做 | 待做 |

---

*文档生成时间：2026-04-02*
*Discovery Database v2*
