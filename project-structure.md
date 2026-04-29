# Project Structure

> 每次 serious plan 前先看这份路径地图。当前原则：脚本归脚本，公司归公司，source 分三层。

## 根目录

- `Agent.md`：项目级协作协议。
- `progress.md`：当前活跃任务面板，只保留当前状态和短历史。
- `core-principles-and-lessons.md`：可复用准则与教训。
- `project-structure.md`：当前路径和脚本说明。
- `config/company_targets.json`：公司配置总表。公司名、slug、ticker、aliases、founders、channels、输出路径都放这里，不写死进 Python。
- `scripts/discovery/`：唯一通用脚本区。
- `companies/`：公司研究主目录。
- `学习/skills/`：active skills，当前主路径为 `collect`、`essence`、`analysis`、`analysis2`、`analysis-add`。
- `学习/_legacy/skills/`：旧 skill 归档。
- `companies/_legacy/`：旧脚本、历史 sample、外部旧 repo 归档。

## 标准公司结构

```text
companies/{slug}/
├── _staging/                 # 脚本运行中间产物、status、failure、临时缓存
├── vault/                    # 正式证据库
│   ├── podcasts/
│   │   ├── metadata/
│   │   ├── transcripts/
│   │   └── essence/
│   ├── youtube/
│   │   ├── metadata/
│   │   ├── transcripts/
│   │   └── essence/
│   ├── substack/
│   │   ├── metadata/
│   │   ├── transcripts/
│   │   └── essence/
│   ├── financials/
│   │   ├── metadata/
│   │   ├── reports/
│   │   └── essence/
│   └── _optional/            # official / jobs / social / funding / broad web 等非默认 source
└── analysis/                 # fact pack、复杂报告、一页分析、500字版本
```

`_staging/` 是运行区，不是正式证据库；`vault/` 才是研究输入；`analysis/` 才是交付输出。

## Source 分层含义

- `metadata/`：query map、candidate list、status、failure、URL index、sidecar JSON、episode metadata。
- `transcripts/`：播客全文、YouTube transcript、Substack/长文全文或可访问正文。
- `essence/`：逐条 source 的精华提炼。后续分析优先读 essence，raw transcript 只用于核验。
- `financials/reports/`：profile、financials、XBRL、SEC/年报/季报正文或报告。
- `financials/metadata/`：财务 raw JSON、索引、状态文件。

## 通用脚本

所有当前可用脚本都在 `scripts/discovery/`：

- `target_config.py`：读取 `config/company_targets.json`，解析 `companies/{slug}/_staging`、`vault`、`analysis`。
- `collect_target.py`：统一编排。`--channels all` 只跑四块：podcasts / financials / substack / youtube；`--channels all_sources` 才跑 optional source。
- `fetch_podcasts.py`：抓 podcast metadata，输出到 `_staging/sources/podcasts/metadata/`。
- `fetch_podcast_transcript.py`：播客 ASR，输出到 `_staging/sources/podcasts/transcripts/`。
- `fetch_web_sources.py`：当前核心用途是 Substack，输出到 `_staging/sources/substack/{metadata,transcripts}/`。
- `fetch_perplexity.py`：Perplexity API URL discovery helper，被 `fetch_web_sources.py` 调用；需要 `PERPLEXITY_API_KEY` / `PPLX_API_KEY`。
- `fetch_youtube.py`：YouTube search + transcript，输出到 `_staging/sources/youtube/{metadata,transcripts}/`。
- `fetch_financials.py`、`fetch_sec_edgar.py`、`fetch_xbrl.py`：上市公司财务，输出到 `_staging/sources/financials/`。
- `build_transcript_essence_queue.py`：为已有 transcript 建 essence backlog，目标路径是 `vault/{source}/essence/`。
- `migrate_project_structure.py`：一次性结构迁移脚本，默认 dry-run。

旧 root 脚本已归档到 `companies/_legacy/root_scripts_legacy/`；旧 discovery 全量/小宇宙/日频信号脚本已归档到 `companies/_legacy/discovery_legacy/`。这些都不要作为新任务入口。

## 推荐流程

### 1. 确认 target

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --dry-run
```

如果 target 不存在，先改 `config/company_targets.json`。

### 2. 采集

默认四块：

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --channels all
```

单独跑：

```bash
python3 scripts/discovery/fetch_podcasts.py --target TARGET_KEY --min-duration-min 10
python3 scripts/discovery/fetch_podcast_transcript.py TARGET_KEY 0 auto companies/{slug}/_staging/sources/podcasts/metadata/_podcast_episodes_org_curated.json
python3 scripts/discovery/fetch_web_sources.py --target TARGET_KEY --channels substack
python3 scripts/discovery/fetch_youtube.py --target TARGET_KEY
python3 scripts/discovery/collect_target.py TARGET_KEY --channels financials --skip-transcript
```

### 3. 同步

`collect_target.py` 会把 `_staging/sources/{source}` 同步到 `vault/{source}/{metadata,transcripts,reports}`。手工跑单个 fetch 后，如果需要同步，跑：

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --channels podcasts --skip-transcript
```

### 4. Essence

使用 `学习/skills/essence/SKILL.md`。每条高相关 source 成功后立刻写 essence：

```text
companies/{slug}/vault/podcasts/essence/
companies/{slug}/vault/youtube/essence/
companies/{slug}/vault/substack/essence/
companies/{slug}/vault/financials/essence/
```

### 5. Analysis

使用 `学习/skills/analysis/SKILL.md`。自动脚本只稳定生成：

- `source_inventory`
- `evidence_map`

fact pack、复杂报告、一页分析、500 字提交版由 agent 读 essence 后写入 `companies/{slug}/analysis/`。

## 当前公司

- `companies/anthropic/`
- `companies/block/`
- `companies/cursor/`
- `companies/lovable/`
- `companies/midjourney/`
- `companies/perplexity/`
- `companies/qunhe/`

历史 public-company samples 在 `companies/_legacy/public_company_samples/`，不是当前研究对象。
