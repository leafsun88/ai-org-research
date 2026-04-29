---
company: Lovable
type: project_structure
date: 2026-04-21
status: current_after_structure_refactor
---

# Lovable 项目结构说明

这份文档只解释 `companies/lovable/` 现在怎么读。核心原则很简单：`_staging/` 是脚本运行区，`vault/` 是正式证据库，`analysis/` 是最终研究稿。后续不要再去 `scripts/LOVABLE/` 找材料；这类公司级运行产物已经迁到 `_staging/`。

## 一眼看懂

```text
companies/lovable/
├── _staging/                 # 脚本运行产物、status、failure、临时缓存
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
│   └── _optional/            # official / jobs / social / web 等非默认 source
└── analysis/                 # 最终报告、source inventory、evidence map、500 字版本
```

## 当前材料快照

| 目录 | 文件数 | 含义 |
|---|---:|---|
| `vault/podcasts/metadata/` | 54 | podcast query map、episode index、episode metadata、转录状态 |
| `vault/podcasts/transcripts/` | 49 | 播客转录原文，用来核原话 |
| `vault/podcasts/essence/` | 0 | 还未补齐；下一步分析前应优先生成 |
| `vault/youtube/metadata/` | 121 | YouTube query map、candidate、status、segments、provider 轨迹 |
| `vault/youtube/transcripts/` | 63 | YouTube transcript 原文 |
| `vault/youtube/essence/` | 63 | 当前 Lovable 最完整的二次提炼层 |
| `vault/substack/metadata/` | 0 | 暂无可用 Substack metadata |
| `vault/substack/transcripts/` | 0 | 暂无可用 Substack 正文 |
| `vault/substack/essence/` | 0 | 暂无可用 Substack essence |
| `vault/financials/` | 0 | Lovable 是私有公司，默认不抓 SEC / yfinance |
| `analysis/` | 3 | 已有组织分析、复杂报告、本文档 |

## `_staging/`

`_staging/` 是脚本运行时的工作台。这里可以有 status、failure、cache、分片、未同步的临时文件；正式写报告时不要从这里开始读。

```text
companies/lovable/_staging/sources/
├── podcasts/
│   ├── metadata/
│   └── transcripts/
├── youtube/
│   ├── metadata/
│   └── transcripts/
├── substack/
│   ├── metadata/
│   └── transcripts/
├── financials/
│   ├── metadata/
│   └── reports/
└── web_longform/             # 旧 longform staging，保留作归档线索
```

如果重新跑 collect，通用脚本会先写这里，然后再同步到 `vault/`。这样设计的好处是：失败清单和缓存不会污染正式证据库。

## `vault/podcasts/`

`podcasts/metadata/` 放播客候选池和转录状态。重要文件通常包括：

- `_podcast_query_map.md`：搜索前的关键词宇宙。YouTube / Substack 后续搜索必须复用它，不能每个 source 临时乱想关键词。
- `_podcast_episodes.json`：播客候选池，记录 title、podcast、date、duration、audio_url 等 metadata。
- `_podcast_episodes_org_curated.json`：按 founder / org / product / GTM 相关性排序后的候选清单。
- `_podcast_transcription_status.json`：转录总状态。
- `_podcast_transcription_failures.json`：真实失败清单。

`podcasts/transcripts/` 放长音频转录原文。这里用于核查引用，不建议直接从这里开始写分析，因为 raw transcript 的信息密度太低。

`podcasts/essence/` 是下一步应该补齐的目录。格式应是“读到一个重要点，就写一段判断 + 一段或多段长引用”，而不是一篇播客只写一句总评。

## `vault/youtube/`

`youtube/metadata/` 放 YouTube 的结构化信息：

- `_youtube_query_map.md`：继承 podcast 关键词宇宙后生成的 YouTube query map。
- `_youtube_candidates.json`：候选视频池，记录 videoId、title、channel、source_query、relevance 等。
- `_youtube_collection_status.json`：整轮抓取状态。
- `_youtube_collection_failures.json`：真实失败清单。
- `*.segments.json`：结构化字幕段落，保留 offset、duration、text。
- `*.providers.json`：provider 轨迹，用于排查 RapidAPI / youtube-transcript-api / yt-dlp fallback。
- `rejected_archive/`：低相关或旧版本误抓候选的归档。

`youtube/transcripts/` 放 YouTube transcript 原文。

`youtube/essence/` 是当前 Lovable 最值得先读的材料层。这里已经有 63 个文件，后续写复杂报告或 500 字版本时，默认先读这里，再回原文核引用。

## `vault/substack/`

Substack 也使用同一套结构：

```text
vault/substack/
├── metadata/
├── transcripts/
└── essence/
```

当前 Lovable 没有可用 Substack 正文或 essence。后续补抓时，URL index、search status、query map 放 `metadata/`；正文 markdown 放 `transcripts/`；逐段提炼放 `essence/`。

## `vault/financials/`

Lovable 是私有公司，默认不跑 SEC / yfinance。若后续补 ARR、估值、融资、收入结构，应放在：

- `financials/metadata/`：source index、状态、口径说明。
- `financials/reports/`：融资新闻、公司公告、可信媒体原文。
- `financials/essence/`：数字口径和可用判断。

私有公司数字必须写清 `official / reported / estimated / third-party estimate`，不要把传闻当事实。

## `vault/_optional/`

```text
vault/_optional/
├── funding/
├── jobs/
├── official/
├── partnerships/
├── social/
└── web/
```

这些目录来自早期“全网最大化”schema。当前主流程已经收窄为 podcast、financials、Substack、YouTube 四块，所以 `_optional/` 不默认填充。只有用户明确要求 all sources 或某个 source 时再启用。

## `analysis/`

当前有三个文件：

- `Lovable_AI组织分析.md`：较早的组织分析稿，回答 Founder 组织观、落地动作、业务影响。
- `Lovable_AI组织复杂报告_2026-04-16.md`：更完整的复杂报告，适合先读。
- `Lovable_project_structure_2026-04-21.md`：本文档。

以后新的报告也都放这里，例如：

- `Lovable_source_inventory_YYYY-MM-DD.md`
- `Lovable_evidence_map_YYYY-MM-DD.md`
- `Lovable_complex_report_YYYY-MM-DD.md`
- `Lovable_500字版本_YYYY-MM-DD.md`

## 推荐阅读顺序

1. 先读 `analysis/Lovable_AI组织复杂报告_2026-04-16.md`，建立主判断。
2. 再读 `vault/youtube/essence/`，这是当前质量最高、覆盖最完整的 essence 层。
3. 如果要核 Anton Osika 或团队成员原话，回到 `vault/youtube/transcripts/` 或 `vault/podcasts/transcripts/`。
4. 如果要继续写新报告，先补 `vault/podcasts/essence/`，再进入 `学习/skills/analysis/SKILL.md` 的 fact pack、evidence map、alike lens、complex report 流程。
