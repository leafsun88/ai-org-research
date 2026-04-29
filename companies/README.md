# Companies 研究目录

`companies/` 是当前项目的研究主目录。每家公司都用同一套结构：`_staging` 跑脚本，`vault` 存证据，`analysis` 写结论。

## 标准结构

```text
companies/{slug}/
├── _staging/
├── vault/
│   ├── podcasts/{metadata,transcripts,essence}/
│   ├── youtube/{metadata,transcripts,essence}/
│   ├── substack/{metadata,transcripts,essence}/
│   ├── financials/{metadata,reports,essence}/
│   └── _optional/
└── analysis/
```

## 目录含义

- `_staging/`：脚本运行中间产物、status、failure、临时缓存。这里不是正式证据库。
- `vault/`：正式证据库。分析前优先看这里。
- `vault/*/metadata/`：query map、candidate、status、failure、sidecar JSON。
- `vault/*/transcripts/`：播客、YouTube、Substack 等正文或转录。
- `vault/*/essence/`：逐条材料压缩后的 insight blocks。正式分析优先读这里。
- `vault/financials/reports/`：财务报告、profile、SEC/XBRL、年报季报正文。
- `vault/_optional/`：official、jobs、social、funding、partnership、broad web 等非默认 source。
- `analysis/`：fact pack、复杂报告、一页分析、500 字提交版等最终或阶段性研究文档。

## 当前公司

- `anthropic/`
- `block/`
- `cursor/`
- `lovable/`
- `midjourney/`
- `perplexity/`
- `qunhe/`

## 项目级目录

- `_meta/`：流程图、全局 transcript inventory、跨公司比较、migration report。
- `_legacy/`：旧脚本、旧 repo、历史 sample company、无法马上删除但不再默认使用的材料。

## 使用规则

- 新抓取通过 `scripts/discovery/` 的通用脚本进入 `companies/{slug}/_staging/`。
- 同步后的正式材料进入 `companies/{slug}/vault/`。
- Essence 写作用 `学习/skills/essence/SKILL.md`，一份 source 对应一份 `vault/{source}/essence/` 文件。
- 最终交付稿只写入 `companies/{slug}/analysis/`。
- 旧路径或 legacy 文件只作追溯，不作为新任务入口。
- YouTube / Substack 必须继承 podcast 阶段的 query universe；每个 source 都要保留自己的 query map 和 status。
- 抓完 transcript 后先做 relevance review 和 essence；后续分析优先读 essence，raw transcript 只用于核验。
