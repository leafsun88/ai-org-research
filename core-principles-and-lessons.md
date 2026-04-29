# Core Principles And Lessons

> 这里只保留跨任务复用的短规则。旧长版已归档到 `companies/_meta/archive/core-principles-and-lessons_archive_2026-04-21_before_cleanup.md`。

## 核心准则

1. 复杂任务先读四个核心文件：`Agent.md`、`progress.md`、`core-principles-and-lessons.md`、`project-structure.md`。
2. 先搭系统，再堆内容；路径、脚本、状态文件不清楚时，先修流程。
3. 原始证据优先：Founder 原声、播客转录、财报、官方文档高于二手总结。
4. 投资研究默认链条：`Founder认知 -> 组织机制 -> 执行动作 -> 业务结果 -> 投资意义`。
5. AI org 默认三问：Founder 有什么独到见解、落地了哪些动作、对业务有什么影响。
6. 事实与推断分开写；没有来源的数字只能标 `待核验`。
7. 复用现有脚本，能配置就不硬编码，能 patch 就不重写。
8. 长音频 ASR / 批量转录是慢任务，用户允许时应交给 sub agent，主线程继续做不阻塞的工作。
9. 结果要可追踪：结论回到 source，失败回到 status/failure 文件。
10. `companies/{slug}/_staging/` 是脚本运行区，`companies/{slug}/vault/` 是正式证据库，`companies/{slug}/analysis/` 是分析主目录。
11. 写作少用 AI 腔模板，尤其避免“不是 X，而是 Y”作为默认句式。
12. 私有公司和非标准 ticker 必须先写入 `config/company_targets.json`。

## 当前默认采集边界

`collect` 默认只抓四块，按优先级排序：

1. podcast
2. financials
3. Substack
4. YouTube

其他 source 默认不抓：official、jobs、social、Reddit、X、funding、partnership、broad web。需要时显式使用 `--channels all_sources` 或指定 channel。

## Podcast 规则

- 搜索前先生成 `_podcast_query_map.md`，覆盖公司名、别名、Founder/C-level、产品、行业、客户/伙伴/竞品、组织与 AI 转型关键词。
- 已知短于 10 分钟的 episode 默认跳过；未知时长不直接丢弃。
- metadata 不是完成，必须继续转录或说明不可转录原因。
- 转录状态必须落 `_podcast_transcription_status.json` 和 `_podcast_transcription_failures.json`。
- `skipped_short` 与 `deferred_max_limit` 是可解释跳过，不算真实失败。

ASR provider 顺序：

```text
Groq Whisper URL
-> DashScope/百炼 URL
-> 本地下载 + DashScope OSS
-> 标准音频 + DashScope REST
```

标准音频 fallback：

- 本地下载成功但 DashScope 报 `FILE_DOWNLOAD_FAILED` 时，转成标准 `mp3` 或 `wav`。
- 推荐 `16kHz / mono / 16-bit PCM WAV`。
- 需要 `oss://` 或 `X-DashScope-OssResourceResolve` 时走 REST API，不走 Python SDK。
- `_audio_cache/` 和 `_standard_audio/` 不同步进 company vault。

## YouTube / Substack 规则

- YouTube / Substack 必须继承 `_podcast_query_map.md`，不重新临场只搜公司名。
- 每个平台必须有自己的 query coverage。
- YouTube 默认 provider：

```text
Search: rapidapi_metadata_search -> yt_dlp_search
Transcript: rapidapi_transcript3 -> youtube_transcript_api -> yt_dlp_subtitle
```

- YouTube 下载 transcript 前必须做 metadata relevance gate。
- 宽 alias 只做 query expansion，不单独构成下载资格。
- `match_count=0` 且没有有效 metadata/snippet 命中的候选要写入 `_youtube_rejected_candidates.json`。
- `_youtube_search_status.json` / `_youtube_collection_status.json` 必须记录 API 消耗量。
- Substack 通过 `scripts/discovery/fetch_web_sources.py --target TARGET --channels substack` 执行；付费墙只存 URL/index，不伪造全文。

## Essence 规则

- 具体执行见 `学习/skills/essence/SKILL.md`；`collect` 只负责准备 transcript、report 和 backlog。
- Essence 是采集流程的一部分，不是最终分析阶段才补；当前 essence 层应理解为 `source_note` / `evidence_note` / 逐源厚笔记，不是短摘要。
- 保留 essence 层，不直接把所有 transcript 塞进报告上下文。正确路径是：一篇 source 一份厚 source note；多篇 source note 再汇总成公司级 research notebook；最后从 notebook 做 theme map 和正式报告。
- 每条高相关 source 成功后立即生成 essence，不等全量抓完。
- 分析优先读 `vault/{source}/essence/`，raw transcript 只用于核验。
- 一份 source 对应一份 source note；一份 source note 内部可以有多条 insight blocks。高相关长访谈出现 15-30 个 blocks 是正常的，宁可厚，不要聪明但空。
- 必须 sequential pass：从头往后逐段判断是否有新机制、动作、数字、组织信号、产品策略、用户反馈、商业模式或竞争信息。
- 批量写 essence 时，一个 batch 读一次 `essence` skill 和 style reference；不要每条 transcript 重学，也不要一次把十几条 transcript 都塞进上下文。新会话、subagent 或 context 被压缩后必须重新读。
- Insight block 下直接写判断自然段，再贴 quote pack；不要加 `关键引用`、`近原文证据`、`原文定位`、`可用于哪些分析角度` 这类工具标签。
- Quote pack 不能只放一句很短的证据标签，也不能写成第三人称 analyst recap。公开英文播客/视频默认使用一条较长、连续、有上下文的中文译引；不要拆成三四条短句。可以轻微修正 ASR 错字和断句；内部/已授权 transcript 才保留更长连续原文。
- Long Quote Gate：如果 quote 短到像 slogan、关键词锚点或一句证据标签，默认返工。新版 source note 的每个 high-relevance block 应有一条连续、有上下文的中文译引，通常至少两个连续句子，能独立说明说话人、机制和上下文。
- Podcast、YouTube、Substack 之间必须做 cross-source dedupe。同一访谈在 podcast 和 YouTube 同步出现时，优先保留 transcript 质量更高的一份进入 essence，其余只标 `duplicate_of`，不要重复抓取或重复分析。
- Relevance 分两级：转录前只能根据 metadata 粗筛，无法确定就先转录；转录后再做 transcript-level relevance gate。低相关 source 标 `no_essence_low_relevance`，不生成完整 essence。
- Founder / CEO / 负责人原声优先，但不是 essence 的硬门槛。第三方科技媒体、投资人、律师、客户、行业专家、竞品 founder 的深度分析，只要高度相关且有机制、数据、竞争、风险或商业判断，也应进入 essence。播客/视频 quote pack 用 speaker 原话；第三方文章/报告 quote pack 可以用作者原文判断，不必强行寻找 founder 原声。
- ASR、YouTube metadata search、Substack discovery、transcript relevance review、essence batch 都可以并行；脚本、skill、全局 queue/status 的修改必须由主线程合并，避免多个 worker 同时改同一文件。source-note subagent 只能写自己被分配的互不重叠输出文件，并在最终回报 block 数、quote 数、跳过/重复项和验证结果；主线程再统一更新 status/progress 并做跨文件验收。
- 风格基准：`学习/style_references/anthropic_org_investment_style_notes_2026-04-21.md`。

## Analysis 规则

- `scripts/discovery/collect_target.py` 只稳定自动生成两类 analysis：`source_inventory` 和 `evidence_map`。
- fact pack、复杂报告、一页分析、500 字提交版属于研究写作流程，不是脚本自动产物。
- 分析前读 `学习/skills/analysis/SKILL.md`。
- 默认输入优先级：`vault/*/essence/` > `vault/financials/reports/` > raw transcripts / raw source。
- 数字必须带来源；私有公司收入、ARR、估值要标 reported / estimated / third-party estimate。

## Skill 精简原则

Active skill 只保留主路径：

- `collect`
- `essence`
- `analysis`

Optional skill 只在用户明确要求时启用：

- `alike` / `alike-memo` / `winner-pattern-org`：旧 D1-D7 评分。
- `founder` / `org-scan` / `private-search` / `social-search` / `deepsearch` / `guru` / `signals-scan`：旧分散抓取入口或专题入口。
- `transcript-critic`：已有音视频单文件处理。
- `vault-*`：旧 vault 支撑工具，当前公司级 `companies/{slug}` 结构优先。

旧 skill 已归档到 `学习/_legacy/skills/`；默认不调用，只在用户明确要求旧框架时回看。

## 高价值组织证据

- Founder 如何解释组织设计、招聘标准、绩效机制、AI 协作和内部工具。
- headcount 政策、AI-before-hiring、组织重组、关键岗位任命、信息流变化。
- 私有 AI 应用公司重点看 careers / JD / values / governance / security 页面。
- 业务影响看产品速度、客户结果、毛利/成本、收入质量、新业务线和扩招节奏之间的关系。
- 像 Midjourney 这类 creator / community 型 AI 公司，组织证据要分层：`strict org` 只算 founder governance、团队规模、社区结构、算力经营、平台迁移、moderation/API/IP governance；客户工作流和创作者采用只能算 `extended org impact`，不能直接当作公司内部组织架构证据。
- 当旧 `_essence.md` 与新 `_source_note.md` 并存时，必须把旧短 essence 移入 `_legacy/`，否则后续分析容易误读短 quote 版本。正式分析目录里应只保留 source notes 和状态文件。
