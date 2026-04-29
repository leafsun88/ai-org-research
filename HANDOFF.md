# Agent Handoff

## 一句话定位

AI Org Research 是一个研究 AI 公司组织形态的本地工作台：它把公开/半公开资料采集、转录、证据笔记和最终组织分析报告串成可复查链路。

## 新 agent 先读什么

先读根目录四个核心文件，顺序不要变：

1. `Agent.md`：协作协议、planning 规则、执行标准。
2. `progress.md`：当前任务面板、已完成事项、风险和下一步。
3. `core-principles-and-lessons.md`：跨任务复用的方法论和踩坑教训。
4. `project-structure.md`：目录结构、脚本职责、输出路径。

如果四者冲突，优先级是 `Agent.md` > `progress.md` > `core-principles-and-lessons.md` > `project-structure.md`。

## 项目核心目的

项目研究 AI 公司如何形成组织优势，默认问题是：

- Founder 有什么独到认知？
- 这些认知落成了哪些组织动作、招聘机制、协作方式和 AI workflow？
- 这些组织动作怎样影响产品速度、成本结构、商业化、社区、治理和投资判断？

默认研究链条：

```text
Founder 认知 -> 组织机制 -> 执行动作 -> 业务结果 -> 投资意义
```

## 目录怎么理解

- `config/company_targets.json`：公司配置总表。新增公司先改这里，不要在脚本里硬编码。
- `scripts/discovery/`：通用采集脚本区。
- `companies/{slug}/_staging/`：运行区，保存脚本中间产物、status、failure、临时缓存。
- `companies/{slug}/vault/`：正式证据库。
- `companies/{slug}/analysis/`：最终报告、fact pack、一页分析、HTML 阅读版等交付物。
- `学习/skills/`：项目内 active skills，主链路是 `collect`、`essence`、`analysis`、`analysis2`、`analysis-add`、`financial-modeling`、`public-company-collect`。
- `一页分析/`：面向展示或推荐的一页 PDF。
- `experiments/`：实验性脚本或模型输出，不是主入口。

## Public Collect：公开信息能抓什么

默认 `--channels all` 只抓四块：

- `podcasts`：播客搜索、metadata、音频转录、Founder/高管/行业访谈。
- `financials`：上市公司财报、SEC/EDGAR、XBRL、年报季报、市场数据、财务模型基础输入。
- `substack`：Substack 和长文 URL discovery、公开正文抓取、Jina Reader fallback、付费墙状态记录。
- `youtube`：YouTube 搜索、metadata relevance gate、字幕/transcript、多 provider fallback。

默认命令：

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --dry-run
python3 scripts/discovery/collect_target.py TARGET_KEY --channels all
```

## Private / Semi-Public Collect：私有公司或半公开信息能抓什么

这里的私有信息不是绕过权限，而是指非上市公司没有标准财报披露，需要从公开可访问但分散的资料里拼组织证据。可抓或可整理：

- Founder、CEO、C-level、产品/增长/设计负责人公开访谈。
- 官网、blog、docs、jobs/careers、values、security、governance 页面。
- funding、投资人文章、合作伙伴、客户案例、公开社区信号。
- Reddit、X、LinkedIn、broad web 等 optional source。
- 用户手动提供、已授权或本地已有材料。

要最大化抓取时，用：

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --channels all_sources
```

付费墙、登录墙、不可公开访问内容只记录 metadata / status / failure reason，不编造正文。

## Source 分层

每家公司每个 source 基本有三层：

- `metadata/`：query map、candidate list、status、failure、URL index、sidecar JSON。
- `transcripts/`：播客、YouTube、Substack、长文或财报正文。
- `essence/`：逐源厚笔记，也叫 source note / evidence note。

Financials 特殊一点：

- `financials/metadata/`
- `financials/reports/`
- `financials/essence/`

后续分析优先读 `vault/*/essence/`，不要直接把大量 raw transcripts 塞进上下文。raw transcript 用来追溯核验。

## 关键脚本地图

- `target_config.py`：解析 `company_targets.json` 和标准路径。
- `collect_target.py`：统一编排、同步 vault、生成 source inventory / evidence map。
- `fetch_podcasts.py`：播客 metadata 和 query map。
- `fetch_podcast_transcript.py`：播客 ASR，多 provider fallback。
- `fetch_web_sources.py`：Substack / web source 采集。
- `manual_substack_search.py`：Substack 手动 URL 或搜索 fallback。
- `fetch_youtube.py`：YouTube search + transcript。
- `fetch_financials.py` / `fetch_sec_edgar.py` / `fetch_xbrl.py`：上市公司财务采集。
- `build_source_dedupe_index.py`：跨 source 去重索引。
- `build_transcript_essence_queue.py`：从 transcript 生成 essence backlog。
- `public_company/*`：上市公司采集、质量循环、市场数据、财务模型等模块化实现。

## API / 环境变量

可能用到：

- `RAPIDAPI_KEY`：YouTube search/transcript provider。
- `PERPLEXITY_API_KEY` 或 `PPLX_API_KEY`：web/Substack discovery helper。
- Groq / DashScope / OSS 相关密钥：播客 ASR fallback。

密钥不要提交到 git。根目录 `.gitignore` 已排除 `.env` 和 `.env.*`。

## 重要规则

- 新公司必须先写 `config/company_targets.json`。
- Podcast 搜索前要有关键词地图 `_podcast_query_map.md`，后续 YouTube/Substack 继承它。
- Podcast 默认跳过已知小于 10 分钟的 episode；未知时长不要直接丢。
- YouTube 下载 transcript 前必须先做 metadata relevance gate，避免浪费 API。
- 采集失败必须写 status / failure 文件，不能静默失败。
- Essence 是逐源厚笔记，不是短摘要；一篇 source 对应一份 source note。
- 分析报告必须区分事实、推断和待核验数字。
- `_staging` 是运行区，`vault` 是正式证据库，`analysis` 是交付区。

## GitHub 版本说明

仓库应包含脚本、配置、文档、文本证据、分析报告和 PDF。原始音频、标准化音频、转码缓存、本地 `.env`、`.vercel` 和 `.DS_Store` 不提交。

音频类缓存已经从 `.gitignore` 排除，因为正式证据以 transcript、metadata、source note 和 analysis 的形式保留。
