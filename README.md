# AI Org Research

这是一个面向 AI 公司组织研究和投资研究的工作台。项目把公开与半公开资料采集、转录、逐源证据笔记、组织分析报告放在同一个可追踪目录里，让后续 agent 能从原始材料一路回溯到最终判断。

进入复杂任务前先读四个核心文件：

1. `Agent.md`
2. `progress.md`
3. `core-principles-and-lessons.md`
4. `project-structure.md`

## 项目在做什么

核心问题是研究 AI 公司如何把 founder 认知、组织机制、AI 工具、招聘方式和业务结果连接起来。默认分析链条是：

```text
Founder 认知 -> 组织机制 -> 执行动作 -> 业务结果 -> 投资意义
```

项目当前覆盖私有 AI 公司和上市公司样本，例如 Anthropic、Anysphere/Cursor、Midjourney、Lovable、Perplexity、Block、Qunhe、Sandisk 等。公司配置统一放在 `config/company_targets.json`。

## 两类采集

### 公开信息采集

默认四类 source：

- `podcasts`：播客 metadata、音频转录、Founder/高管/行业深访。
- `youtube`：YouTube metadata、字幕/transcript、访谈与产品演示。
- `substack`：Substack/长文 discovery、公开正文抓取、付费墙状态记录。
- `financials`：上市公司财报、SEC/XBRL、市场数据和财务模型输入。

这些由 `scripts/discovery/collect_target.py` 编排，单项脚本在 `scripts/discovery/` 下。

### 私有/半公开信息采集

这里的“私有”主要指非上市公司和不在标准财报系统里的资料，不代表绕过权限或抓取不可访问内容。项目会抓取或整理：

- Founder、CEO、C-level 的公开访谈和播客。
- 公司官网、jobs/careers、values、security、governance、funding 等 optional source。
- 社区、产品文档、公开帖子、第三方深度文章、投资人或行业专家评论。
- 用户手动提供或已授权的材料。

付费墙、登录墙、不可访问页面只记录 URL、标题、状态和失败原因，不伪造正文。

## 数据流

```text
config/company_targets.json
  -> scripts/discovery/*
  -> companies/{slug}/_staging/
  -> companies/{slug}/vault/{source}/metadata|transcripts|essence
  -> companies/{slug}/analysis/
```

`_staging/` 是运行区，`vault/` 是正式证据库，`analysis/` 是报告输出区。分析时优先读 `vault/*/essence/`，raw transcript 只用于核验。

## 常用命令

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --dry-run
python3 scripts/discovery/collect_target.py TARGET_KEY --channels all
python3 scripts/discovery/collect_target.py TARGET_KEY --channels all_sources
python3 scripts/discovery/fetch_podcasts.py --target TARGET_KEY --min-duration-min 10
python3 scripts/discovery/fetch_podcast_transcript.py TARGET_KEY 0 auto companies/{slug}/_staging/sources/podcasts/metadata/_podcast_episodes_org_curated.json
python3 scripts/discovery/fetch_web_sources.py --target TARGET_KEY --channels substack
python3 scripts/discovery/fetch_youtube.py --target TARGET_KEY
python3 scripts/discovery/build_transcript_essence_queue.py TARGET_KEY
```

## 交接

完整交接文档见 `HANDOFF.md`。后续 agent 如果只读一份新文档，先读它；如果要执行任务，再回到四个核心文件。
