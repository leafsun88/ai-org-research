---
name: collect
description: Use when starting or repairing a company research collection pipeline for AI org / investment work, especially when the task needs podcasts, financials, Substack, YouTube, transcripts, or vault sync.
argument-hint: TARGET_KEY
---

# Collect Skill

`collect` 负责把高价值材料抓干净，并把 transcript / report 同步进 company vault。essence 的写作交给 `学习/skills/essence/SKILL.md`。默认 source 只保留四块，按重要性排序：

1. podcast
2. financials
3. Substack
4. YouTube

`official / jobs / social / Reddit / X / funding / partnership / broad web` 默认不跑。用户明确要求“全网最大化”时才用 `--channels all_sources`。

## 0. 必读

serious collection 前先读：

- `Agent.md`
- `progress.md`
- `core-principles-and-lessons.md`
- `project-structure.md`

## 1. Canonical Paths

```text
config/company_targets.json
scripts/discovery/
companies/{slug}/_staging/
companies/{slug}/vault/
companies/{slug}/analysis/
```

`scripts/discovery/` 是通用脚本本体；`_staging/` 是某家公司本轮运行产物；`vault/` 是正式证据库。

每个 source 固定三层：

```text
metadata/
transcripts/
essence/
```

financials 特殊一点：

```text
financials/metadata/
financials/reports/
financials/essence/
```

## 2. Script Map

| 块 | 脚本 | 输出 |
|---|---|---|
| target 解析 | `scripts/discovery/target_config.py` | `companies/{slug}/_staging`、`vault`、`analysis` |
| 默认编排 | `scripts/discovery/collect_target.py` | `source_inventory`、`evidence_map`、vault sync |
| podcast metadata | `scripts/discovery/fetch_podcasts.py` | `_staging/sources/podcasts/metadata/` |
| podcast ASR | `scripts/discovery/fetch_podcast_transcript.py` | `_staging/sources/podcasts/transcripts/` |
| financials | `fetch_financials.py` / `fetch_sec_edgar.py` / `fetch_xbrl.py` | `_staging/sources/financials/` |
| Substack API path | `scripts/discovery/fetch_web_sources.py --channels substack` | `_staging/sources/substack/{metadata,transcripts}/` |
| Substack manual fallback | `scripts/discovery/manual_substack_search.py --target TARGET_KEY` | `_staging/sources/substack/{metadata,transcripts}/` |
| YouTube | `scripts/discovery/fetch_youtube.py` | `_staging/sources/youtube/{metadata,transcripts}/` |
| cross-source 去重索引 | `scripts/discovery/build_source_dedupe_index.py` | `vault/{source}/metadata/_source_dedupe_index.json/md` |
| essence queue | `scripts/discovery/build_transcript_essence_queue.py` | 待写 essence backlog；具体写作用 `学习/skills/essence/SKILL.md` |

## 3. Target Manifest First

如果 target 不存在，先改 `config/company_targets.json`，不要在 Python 里硬编码公司名。

至少填：

- `ticker` / `research_key`
- `slug`
- `company_name`
- `is_public`
- `aliases`
- `founders`
- `executives`
- `exclude_terms`
- `output_paths.script_root = companies/{slug}/_staging`
- `channels.podcasts.queries`
- `channels.podcasts.relevance_terms`
- `channels.youtube.queries`
- `channels.youtube.relevance_terms`
- `channels.substack.queries`

私有公司 `is_public: false` 默认跳过 financials。

## 4. Query Universe

Podcast 阶段的 `_podcast_query_map.md` 是所有 source 的关键词底座。

位置：

```text
companies/{slug}/_staging/sources/podcasts/metadata/_podcast_query_map.md
companies/{slug}/vault/podcasts/metadata/_podcast_query_map.md
```

关键词必须覆盖：

- 公司名、简称、旧名、产品名、核心协议/技术名
- Founder、CEO、C-level、关键产品/研究/商业负责人
- 行业关键词和行业访谈关键词
- 重要客户、伙伴、竞争对手
- 组织与 AI 转型词：`hiring`、`org`、`culture`、`AI transformation`、`agent`、`workflow`、`developer productivity`

Substack / YouTube 必须复用这份 query map。没有 query map 时，先补 podcast metadata 或手写 query map，不要临场只搜公司名。

## 5. Default Flow

### Step 1. Dry Run

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --dry-run
```

检查 `is_public`、aliases、founders、queries、`_staging` 和 `vault` 路径。

### Step 2. Podcast Metadata

```bash
python3 scripts/discovery/fetch_podcasts.py --target TARGET_KEY --min-duration-min 10
```

必须检查：

```text
companies/{slug}/_staging/sources/podcasts/metadata/_podcast_query_map.md
companies/{slug}/_staging/sources/podcasts/metadata/_podcast_episodes.json
companies/{slug}/_staging/sources/podcasts/metadata/_podcast_episodes_org_curated.json
```

已知短于 10 分钟的 episode 默认跳过；未知时长保留。

### Step 3. Podcast Transcript

```bash
python3 scripts/discovery/fetch_podcast_transcript.py TARGET_KEY 0 auto companies/{slug}/_staging/sources/podcasts/metadata/_podcast_episodes_org_curated.json
```

ASR provider 顺序：

```text
Groq Whisper URL
-> DashScope/百炼 URL
-> 本地下载 + DashScope OSS
-> 标准音频 + DashScope REST
```

状态文件在：

```text
companies/{slug}/_staging/sources/podcasts/transcripts/_podcast_transcription_status.json
companies/{slug}/_staging/sources/podcasts/transcripts/_podcast_transcription_failures.json
```

成功判定：

- transcript markdown 非空
- 有 transcript 正文
- frontmatter 写了 provider / engine
- status 中该 episode 是 success

转录并行规则：

- Podcast ASR 是天然可并行任务。metadata 和 curated list 出来后，把 episode 按 5-10 条一批切开，可用 subagent / worker 并行跑转录。
- 每个 worker 只负责自己的 batch，不要改同一份全局脚本；输出必须写入同一公司的 `_staging/sources/podcasts/transcripts/`，并写 batch status。
- 主线程不要等待音频转录空转。subagent 跑 ASR 时，主线程继续做 financials、Substack、YouTube metadata、cross-source dedupe 和 source inventory。
- 如果 provider 失败，按既定顺序重试：Groq -> DashScope URL -> 本地下载 + OSS -> 标准音频 + DashScope REST。真实失败必须写 failure reason。

Relevance 在 podcast 阶段分两级：

- 转录前只能做 metadata 粗筛：短于 10 分钟、标题明显无关、纯新闻串烧、广告/教程类可以跳过。只靠标题无法判断的内容不要提前淘汰。
- 转录后再做 transcript-level relevance gate。低相关 transcript 不进入 essence；在 `_transcript_essence_queue*.json/md` 或 collection status 里标 `no_essence_low_relevance`，写明原因即可，不需要生成完整 essence。
- Founder / CEO / 负责人原声优先，但不是 relevance 的唯一标准。第三方深度科技媒体、投资人、律师、客户、行业专家、竞品 founder 的材料，如果高度相关并提供机制、数据、竞争、风险或商业判断，也要进入 essence 队列。第三方文章/报告进入 essence 时，quote pack 可以引用作者原文判断；不要因为它不是 founder 原声而降级。

### Step 4. Financials

仅 `is_public: true` 执行：

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --channels financials --skip-transcript
```

输出：

```text
companies/{slug}/_staging/sources/financials/
companies/{slug}/vault/financials/{metadata,reports,essence}/
```

### Step 5. Substack

```bash
python3 scripts/discovery/fetch_web_sources.py --target TARGET_KEY --channels substack
python3 scripts/discovery/collect_target.py TARGET_KEY --channels substack --skip-transcript
```

如果本机没有 `PERPLEXITY_API_KEY / PPLX_API_KEY`，或 API path 搜不到足够 URL，立刻切手动 fallback：

```bash
python3 scripts/discovery/manual_substack_search.py --target TARGET_KEY --max-queries 12 --results-per-query 8 --sync-vault
```

如果公开搜索页被拦，先人工把 URL 放到一个文本文件，每行一个 URL，再交给脚本统一去重、打分、抓取和同步：

```bash
python3 scripts/discovery/manual_substack_search.py --target TARGET_KEY --url-file companies/{slug}/vault/substack/metadata/manual_urls.txt --sync-vault
```

`manual_substack_search.py` 会先尝试直接抓取公开页面；直接抓不到正文时，默认用 Jina Reader fallback 抓取公开 markdown。付费墙 / subscriber-only 文章只保留 URL、title、status 和失败原因，不伪造全文。

输出：

```text
companies/{slug}/_staging/sources/substack/metadata/
companies/{slug}/_staging/sources/substack/transcripts/
companies/{slug}/vault/substack/metadata/
companies/{slug}/vault/substack/transcripts/
```

付费墙只存 URL/index，不伪造全文。

### Step 6. YouTube

```bash
python3 scripts/discovery/fetch_youtube.py --target TARGET_KEY
python3 scripts/discovery/collect_target.py TARGET_KEY --channels youtube --skip-transcript
```

默认 provider：

```text
Search: rapidapi_metadata_search -> yt_dlp_search
Transcript: rapidapi_transcript3 -> youtube_transcript_api -> yt_dlp_subtitle
```

下载 transcript 前必须做 metadata relevance gate。低相关候选写入 `_youtube_rejected_candidates.json`，不要烧 transcript API。

YouTube 必须先做 cross-source dedupe，再决定是否下载 transcript。不要每次临时读取一堆 podcast transcript / essence；先生成轻量 index：

```bash
python3 scripts/discovery/build_source_dedupe_index.py TARGET_KEY --source podcasts
```

YouTube 抓取前只读这两个文件：

```text
companies/{slug}/vault/podcasts/metadata/_source_dedupe_index.json
companies/{slug}/vault/podcasts/metadata/_source_dedupe_index.md
```

`_source_dedupe_index` 只包含 title、date、show、speaker、duration、URL、transcript path、essence path 和 essence headings，不包含长 transcript / essence 正文。

对 YouTube candidate 做 normalized key：

```text
normalized_title
speaker / guest / founder name
publisher / channel / podcast name
publish_date 或 episode_date
duration bucket
canonical_url / video_id / enclosure_url
```

3. 判重分三档：

- `exact_duplicate`：同一访谈在 podcast 和 YouTube 同步发布，标题/嘉宾/日期/时长高度一致；如果 podcast transcript 已成功，不再下载 YouTube transcript，也不生成 YouTube essence。
- `likely_duplicate`：标题或日期略有差异，但嘉宾、主题、时长高度重合；先保留 YouTube metadata，除非 podcast transcript 失败或 YouTube 明显更完整，否则不抓 transcript。
- `complementary`：同一嘉宾但内容不同，比如不同节目、不同日期、不同主题；正常抓 transcript。

4. 结果写入：

```text
companies/{slug}/_staging/sources/youtube/metadata/_youtube_cross_source_dedupe.json
companies/{slug}/vault/youtube/metadata/_youtube_cross_source_dedupe.json
```

已抓到的重复 YouTube transcript 不进入 essence 队列。若需要审计，只在 queue/status 标 `duplicate_of: podcasts/{file}`，不要再写一份重复 essence。

### Step 7. Sync

单独跑 fetch 后，用对应 channel 同步：

```bash
python3 scripts/discovery/collect_target.py TARGET_KEY --channels podcasts --skip-transcript
```

`collect_target.py` 会把 `_staging/sources/{source}` 同步到 `vault/{source}/{metadata,transcripts,reports}`。

### Step 8. Essence Handoff

每条高相关 source 成功后，进入 `学习/skills/essence/SKILL.md`。不要把“所有 transcript 都必须写 essence”当作默认规则；低相关、重复、缺少有效内容的 source 只保留 metadata/status，不进入 essence。

```text
companies/{slug}/vault/podcasts/essence/
companies/{slug}/vault/youtube/essence/
companies/{slug}/vault/substack/essence/
companies/{slug}/vault/financials/essence/
```

先生成或更新 backlog：

```bash
python3 scripts/discovery/build_transcript_essence_queue.py \
  --output-json companies/_meta/transcripts/_transcript_essence_queue_TARGET_KEY_YYYY-MM-DD.json \
  --output-md companies/_meta/transcripts/_transcript_essence_queue_TARGET_KEY_YYYY-MM-DD.md
```

然后用 `/essence` 逐条做 relevance review、sequential pass 和 source-level essence。`collect` 不直接写最终判断段，避免抓取脚本和研究写作混在一起。

批量场景下不要每条 transcript 都重新读完整 essence 规范。正确方式是：`collect` 生成 backlog；`essence` 按 5-10 条 source 为一个 batch 处理，batch 开始读一次 `学习/skills/essence/SKILL.md` 和 style reference，之后逐条 source 落盘。新会话、subagent 或 context 被压缩后，再重新读 essence skill。

Essence queue 必须先做三类过滤：

- `duplicate`: 与 podcast / YouTube / Substack 已有 source 高度重复，选最高质量版本进入 essence，其余标 `duplicate_of`。
- `low_relevance`: transcript 已读后判断和公司、管理层、组织、产品、客户、财务、行业判断无关，标 `no_essence_low_relevance`。
- `high_relevance`: 进入 `essence` 批处理。

优先级：podcast founder/CEO 长访谈 > 第三方深度分析 / 行业专家 / 法律与竞争深度材料 > Substack 深度文章 > YouTube founder/CEO 长访谈 > 财务报告 > 其他材料。同一内容多 source 重复时，优先选择 transcript 质量最高、上下文最长、判断最有增量的一份版本。

## 5.1 Parallel Work Rules

适合并行的任务：

- podcast ASR batch 转录
- YouTube metadata search across query groups
- Substack URL discovery across query groups
- transcript-level relevance review across independent sources
- 已确认高相关 source 的 essence 批处理

不适合并行的任务：

- 修改 `config/company_targets.json`
- 修改 `scripts/discovery/*.py`
- 修改 skill / core docs
- 同一份 transcript 的 essence 写作
- 同一份 status / queue 文件的手工重写

并行原则：

- 每个 subagent / worker 必须有独立 batch 和明确输入输出路径。
- worker 不要重复抓同一 URL / episode / video；主线程先生成 batch manifest。
- worker 完成后只汇报 changed files、success/failure、low relevance、duplicates。
- 主线程负责合并 status、dedupe、queue，不让多个 worker 同时编辑同一个全局文件。

## 6. Failure Rules

- metadata 不等于完成；podcast 必须尽力转 transcript。
- `skipped_short` 与 `deferred_max_limit` 是可解释跳过，不算真实失败。
- 失败必须进入 status/failure 文件。
- 若失败来自脚本能力不足，先修脚本再重试。
- `_audio_cache/` 和 `_standard_audio/` 不同步进 vault。

## 7. Output Rule

分析阶段只读：

```text
companies/{slug}/vault/
companies/{slug}/analysis/
```

不要把 `_staging/` 当最终材料库。`_staging/` 只用于查运行状态和失败原因。
