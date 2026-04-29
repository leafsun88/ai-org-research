# 项目结构重构执行计划

## Summary

这次重构的核心目标是把三类东西彻底分开：

- `scripts/discovery/` 只放通用脚本本体，不再混放某家公司跑出来的材料。
- `companies/{slug}/_staging/` 放脚本跑某家公司时产生的中间结果、状态文件、失败清单。
- `companies/{slug}/vault/` 放研究证据库，每个 source 都统一拆成 `metadata / transcripts / essence`。

重构后的标准公司结构：

```text
companies/{slug}/
├── _staging/                # 脚本运行产物、状态、失败清单、缓存，不作为正式证据
├── vault/                   # 正式证据库
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
│   └── financials/
│       ├── metadata/
│       ├── reports/
│       └── essence/
└── analysis/                # 最终报告、fact pack、evidence map、一页分析、500字版本
```

## Key Changes

- YouTube：`vault/youtube/*.md` 迁到 `transcripts/`；`*.segments.json`、`*.providers.json`、`_youtube_*.json/md` 迁到 `metadata/`；`youtube-essence/` 迁到 `essence/`；`_stale_rejected/` 迁到 `metadata/rejected_archive/`。
- Substack：`vault/substack/*.md` 迁到 `transcripts/`；`_substack_query_map.md`、`_url_index.json`、`_search_status.json`、`_collection_status.json`、`_collection_failures.json` 迁到 `metadata/`；`source-essence/` 迁到 `essence/`。
- Podcast：保留 `metadata/` 和 `transcripts/`；`podcast-essence/` 改为 `essence/`；`_podcast_query_map.md`、`_podcast_episodes*.json` 放入 `metadata/`。
- 脚本与运行产物拆开：保留 `scripts/discovery/*.py`；把 `scripts/LOVABLE`、`scripts/MIDJOURNEY`、`scripts/ANTHROPIC` 等运行产物迁到对应 `companies/{slug}/_staging/`。
- Legacy：`Alike-Investment/` 迁入 `companies/_legacy/external_repos/alike-investment/`；旧 root 版重复脚本迁入 `companies/_legacy/root_scripts_legacy/`；非 active skills 迁入 `学习/_legacy/skills/`。
- Active skills：`学习/skills/` 只保留 `collect` 和 `analysis`；其他 skill 归档但不删除。

## Implementation Changes

- 新增一次性迁移脚本 `scripts/discovery/migrate_project_structure.py`，默认 `--dry-run`，`--apply` 才执行移动；所有 move 都写入 `companies/_meta/migrations/project_structure_migration_2026-04-21.json`。
- 修改 `scripts/discovery/target_config.py`、`collect_target.py`、`fetch_podcasts.py`、`fetch_podcast_transcript.py`、`fetch_youtube.py`、`fetch_web_sources.py`、`fetch_financials.py`，让公司运行产物进入 `_staging`。
- 修改 `build_transcript_essence_queue.py`，把 essence 目标路径统一为 `vault/{source}/essence/`。
- 更新 `Agent.md`、`project-structure.md`、`companies/README.md`、`progress.md`、`core-principles-and-lessons.md`、`学习/_skill-guide.md`、`学习/skills/collect/SKILL.md`、`学习/skills/analysis/SKILL.md`。
- 重写 `companies/lovable/analysis/Lovable_project_structure_2026-04-21.md`，作为标准公司结构示例。

## Test Plan

- `python3 scripts/discovery/migrate_project_structure.py --dry-run`
- `python3 scripts/discovery/migrate_project_structure.py --apply`
- `python3 -m json.tool config/company_targets.json >/dev/null`
- `python3 -m py_compile scripts/discovery/target_config.py scripts/discovery/collect_target.py scripts/discovery/fetch_youtube.py scripts/discovery/fetch_web_sources.py scripts/discovery/build_transcript_essence_queue.py`
- `python3 scripts/discovery/collect_target.py LOVABLE --dry-run`
- `python3 scripts/discovery/fetch_youtube.py --target LOVABLE --dry-run --max-queries 1`
- `find companies/*/vault/youtube -maxdepth 1 -type f`
- `find companies/*/vault/substack -maxdepth 1 -type f`
- `rg -n "youtube/youtube-essence|podcast-essence|source-essence|scripts/LOVABLE|scripts/MIDJOURNEY|scripts/ANTHROPIC|scripts/QUNHE|scripts/CURSOR" Agent.md project-structure.md companies/README.md progress.md core-principles-and-lessons.md 学习/skills 学习/_skill-guide.md config scripts/discovery`

## Assumptions

- 通用脚本只保留在 `scripts/discovery/`。
- `companies/{slug}/_staging/` 是脚本运行区，不是最终证据库；正式分析只读 `vault/` 和 `analysis/`。
- 这次做全量迁移：Anthropic、Block、Cursor、Lovable、Midjourney、Perplexity、Qunhe，以及已有历史 script outputs。
- Legacy 只归档不删除。
- 重构过程中不重新抓取外部数据，只做路径、同步逻辑、文档和 skill 的结构性整理。
