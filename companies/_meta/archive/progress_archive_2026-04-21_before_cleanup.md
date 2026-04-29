# Progress

> 这是当前活跃任务的唯一进度面板。每次认真 plan 前、每个关键阶段完成后，都要先更新这里。

## 文档使用规则

- serious planning 前先读本文件
- 当前任务变化后立即刷新，不允许长期过期
- 这里写“真实状态”，不写理想状态
- 如果 plan、风险、下一步变了，优先更新这里

---

## 当前任务

- 名称：Lovable podcast metadata / transcript 重抓
- 日期：2026-04-21
- 状态：已完成 Lovable podcast metadata 与 transcript 重抓；补齐 `_podcast_query_map.md`，重新生成 50 条 metadata，转录 49 条成功、1 条真实失败，并已同步到 `companies/lovable/vault/podcasts/`。转录链路按 Groq Whisper URL -> DashScope/百炼 URL -> 本地下载+OSS -> 标准音频 REST fallback 执行。

## Goal

把 Lovable 的 podcast 采集闭环补齐：先生成/刷新关键词 query map，再重新抓 metadata，然后按 provider 顺序完成 transcript，最后把 metadata、transcripts、status、failures 同步进 company vault。

## Active Plan

- [x] 确认 Lovable target 已在 `config/company_targets.json`
- [x] 检查现有 Lovable podcast 目录、metadata 数量、transcript 数量与缺失状态文件
- [x] 重新抓 Lovable podcast metadata，生成/刷新 `_podcast_query_map.md`
- [x] 运行 Lovable transcript 重抓，并落 `_podcast_transcription_status.json` / `_podcast_transcription_failures.json`
- [x] 同步 metadata / transcripts 到 `companies/lovable/vault/podcasts/`
- [x] 汇总成功数、失败数、跳过数与主要失败原因

## Progress Log

### 已完成

- Collect / Analysis skill 二次重构：
  - 已重写 `学习/skills/collect/SKILL.md`：默认只保留 podcast / financials / Substack / YouTube 四块；optional high-entropy source 只能显式开启
  - 已新增 `学习/skills/analysis/SKILL.md`：确认当前只有 `collect_target.py` 自动生成 source inventory / evidence map；fact pack、复杂报告、一页分析、500 字提交版属于基于 essence 的研究写作流程
  - 已把用户最早的 analysis 生成过程写入 analysis skill：先学习 `Agent.md` 和 `学习/`，再 plan，再围绕 Founder 认知、组织动作、业务影响三问展开
  - 已修改 `scripts/discovery/collect_target.py`：`--channels all` 只跑核心四块；`--channels all_sources` 才跑 optional source；新增 financials channel 同步逻辑
  - 已修改 `scripts/discovery/fetch_web_sources.py`：`--channels all` 只等价于 Substack；`--channels all_sources` 才恢复 broad web / official / jobs / social / funding
  - 已修改 `scripts/discovery/target_config.py`：新 target 默认只创建核心 vault 目录，减少空的 social / jobs / funding 目录噪音
  - 已更新 `project-structure.md`、`core-principles-and-lessons.md`、`学习/_skill-guide.md`，把脚本路径、状态文件、输出目录和默认/可选边界写清楚
  - 验证已完成：`config/company_targets.json` 可解析；`collect_target.py` / `fetch_web_sources.py` / `target_config.py` 等核心脚本 `py_compile` 通过；`collect_target.py LOVABLE --dry-run` 显示 `all` 只计划 podcast / financials / substack / youtube，且私有公司 financials 为 disabled
  - 已检查 `scripts/discovery/fetch_perplexity.py --smoke-test`：当前本机未设置 `PERPLEXITY_API_KEY` / `PPLX_API_KEY`，所以 Perplexity URL discovery 不能作为默认可用链路，只能作为后续配置 key 后的可选增强

- Transcript inventory / essence 准备：
  - 已将 essence 模板改成“逐段 insight block + 判断段 + 引用紧贴”的格式，并把用户给定的 Claude Cowork 示例写入 `学习/skills/collect/SKILL.md`
  - 已按用户最新要求进一步去掉 `**判断段**` 标签：每条 insight block 现在是短标题后直接写详实判断自然段，然后紧跟完整原文短句引用
  - 已按用户反馈把引用从“最小证据”改为 quote pack：一个 insight 后保留多条更有上下文的原文摘录，避免后续写作时没有可剪裁素材
  - 已按用户截图反馈删除 sample 与模板里的 `可用于哪些分析角度` / `原文定位` 尾部字段
  - 已保存用户提供的风格文章：`学习/style_references/anthropic_org_investment_style_reference_2026-04-21.md`
  - 已生成风格拆解笔记：`学习/style_references/anthropic_org_investment_style_notes_2026-04-21.md`
  - 已把 Anthropic 风格基准和两段硬编码样例写入 `学习/skills/collect/SKILL.md`
  - 已生成新格式测试文件：`学习/style_references/essence_format_tests_2026-04-21.md`，当前包含 4 条样例：Lovable planning、Midjourney 多线探索、Lovable hiring filter、Midjourney community onboarding
  - 已生成当前 transcript inventory：raw transcript markdown 398 个；按 canonical company/source/date/title 去重后约 240 条；其中 podcast 197 条、YouTube 42 条、web 1 条
  - inventory 文件位于 `companies/_meta/transcripts/_transcript_inventory_2026-04-21.md`
  - 已生成 essence queue：240 条 unique transcript；其中 Lovable 16 条、Midjourney 78 条
  - essence queue 位于 `companies/_meta/transcripts/_transcript_essence_queue_2026-04-21.json` 与 `companies/_meta/transcripts/_transcript_essence_queue_2026-04-21.md`
  - 已按用户反馈清理 `companies/` 根目录：历史 public-company sample 进入 `companies/_legacy/public_company_samples/`；跨公司稿进入 `companies/_meta/cross_company/`；全局 transcript 辅助文件进入 `companies/_meta/transcripts/`
  - 已把 sequential pass 写入 `Agent.md`、`core-principles-and-lessons.md`、`project-structure.md`、`companies/README.md` 与 `学习/skills/collect/SKILL.md`
  - 已完成 sample essence：
    - `companies/lovable/vault/youtube/youtube-essence/2025-03-09_Building-Lovable-10M-ARR-in-60-days-with-15-people_essence.md`
    - `companies/lovable/vault/youtube/youtube-essence/2026-04-16_A-conversation-with-Lovable-CEO-Anton-Osika_essence.md`
    - `companies/midjourney/vault/podcasts/podcast-essence/2023-06-20_David-Holz-Midjourney_essence.md`
    - `companies/midjourney/vault/youtube/youtube-essence/2026-04-20_Discord-Open-Office-Hours-with-MidJourney-Founder_essence.md`
  - 当前 queue 状态：Lovable 2/16 done；Midjourney 2/78 done

- Podcast ASR provider 链路：
  - 已确认 Groq key 可用，`whisper-large-v3-turbo` 小样本 URL 与本地文件上传均转录成功
  - 已发现并记录 Groq `url` 请求必须使用 `multipart/form-data`
  - 已新增本项目 `.env`，并用 `.gitignore` 保护
  - 已修改 `scripts/discovery/fetch_podcast_transcript.py`：默认先 Groq URL，再 DashScope URL，再本地下载 + DashScope OSS；transcript frontmatter 写入 `transcription_provider` / `transcription_engine`，status JSON 记录 provider attempts
  - 已修复转录脚本在 Python 3.9 下导入时报错的 `Path | None` 类型注解问题
  - 已用 JFK 11 秒公开音频跑通 smoke test：provider=`groq`，engine=`groq_whisper-large-v3-turbo`

- Midjourney：
  - 已暂停 Cursor 主动采集；Cursor 播客转录 worker 已关闭，避免继续占用资源
  - 已完成四个核心文件前置复核：`Agent.md`、`progress.md`、`core-principles-and-lessons.md`、`project-structure.md`
  - 已确认首轮采集边界：私有公司，不跑 SEC / yfinance；重点抓 official / docs / founder voice / team / jobs / product releases / community / web longform / podcast / YouTube / funding revenue estimates
  - 已建立 `MIDJOURNEY` target，配置位于 `config/company_targets.json` 的 `targets.MIDJOURNEY`
  - 已建立 `companies/midjourney/vault/` 与 `companies/midjourney/analysis/`
  - 已跑 `collect_target.py MIDJOURNEY --dry-run`，manifest 输出路径验证正常
  - 首轮 web source fetch 已完成：founder_voice 2/4 成功、web_longform 2/8 成功、enterprise_partnerships 1/3 成功；official / products / jobs / social / funding 多数因页面渲染、反爬或 Perplexity 401 仅保留 URL index
  - Podcast metadata 已完成：76 条 episode
  - Podcast ASR 经验已更新：前 30 条里 `FILE_DOWNLOAD_FAILED` 不是本机下载失败，而是 DashScope 云端读取失败；通过本地标准化音频（`_standard_audio/`，16kHz / mono / 16-bit PCM WAV）+ OSS + RESTful API + `X-DashScope-OssResourceResolve` 兜底，第一批失败项已批量救回
  - 已按用户补充修正流程顺序：RSS enclosure / 原始 `audio_url` 是第一选择；下载、转码、OSS 重传是失败后的 fallback，不作为默认起手式
  - 已按用户新增要求修正播客规则：
    - 已知短于 10 分钟的 episode 默认不抓 / 不转录
    - podcast 搜索前必须先做关键词元思考并落 `_podcast_query_map.md`
    - transcript 抓完后必须做 relevance review，低相关淘汰，高相关逐条生成 essence
    - 后续分析优先基于 `podcast-essence` / `youtube-essence` / `source-essence`，raw transcript 只做追溯核验
  - 已按用户更正修正 essence 粒度：一个 source 对应一份 essence 文档，但文档内部必须拆成多条 insight blocks；每读到重要段落、机制、业务数据、管理层判断、组织动作、产品战略、用户反馈或可投资化证据，就新增一条 block，长材料可以有十几条到几十条
  - 当前脚本目录与 vault 已同步 33 条 transcript；vault 中没有 `_audio_cache/` 或 `_standard_audio/` 音频目录
  - 当前仍有一个 `fetch_podcast_transcript.py MIDJOURNEY 0 auto ...` 后台进程在继续跑全量 curated；最新状态文件显示 33 条成功、1 条失败、1 条 running，状态仍可能继续变化
  - YouTube transcript 已完成 3 条，约 259k 字符；其中包括 David Holz office hours / Midjourney 使用相关长转录
  - 已同步一条高价值 podcast transcript：`David Holz (Midjourney)` / Power Law with John Coogan
  - 已补写 source notes：
    - `companies/midjourney/vault/official/official_source_note_2026-04-20.md`
    - `companies/midjourney/vault/products/product_updates_source_note_2026-04-20.md`
    - `companies/midjourney/vault/jobs/careers_source_note_2026-04-20.md`
    - `companies/midjourney/vault/funding/funding_revenue_source_note_2026-04-20.md`
    - `companies/midjourney/vault/web/legal_source_note_2026-04-20.md`
    - `companies/midjourney/vault/social/social_community_source_note_2026-04-20.md`
  - 已重写 source inventory / evidence map：
    - `companies/midjourney/analysis/Midjourney_source_inventory_2026-04-20.md`
    - `companies/midjourney/analysis/Midjourney_evidence_map_2026-04-20.md`
  - 已新增首版 fact pack：
    - `companies/midjourney/analysis/Midjourney_fact_pack_2026-04-20.md`
  - 验证通过：`config/company_targets.json` 可解析；Midjourney analysis 三份 md 均非空；vault 当前约 119 个文件

### 当前缺口

- Podcast ASR 尚未完全闭环：标准音频 REST fallback 已验证有效，当前脚本目录与 vault 已有 33 条 transcript；全量 curated 后台进程仍在运行，后续需要等进程结束后再检查 final status / failures
- Official / products / jobs 多数由浏览器核验后补 source notes，脚本仍未能直接全文抓取这些 JS/反爬页面
- 收入、估值、员工数均无公司披露，只能引用 Sacra / Contrary / ProductGrowth / Andrew 等第三方估算，并清楚标注置信度
- 社区材料目前只到 Reddit / Discord URL index 和搜索片段，未做登录/深抓

---

## 暂停任务：Cursor / Anysphere 公开信息采集

- 日期：2026-04-20
- 状态：按用户指示暂停；首轮采集已有 `CURSOR` target、`companies/cursor/` 目录、145 个 vault 文件、68 条 podcast metadata、7 条 YouTube transcript；source inventory / fact pack 尚未收口

### 已完成

- Cursor / Anysphere：
  - 已完成四个核心文件前置复核：`Agent.md`、`progress.md`、`core-principles-and-lessons.md`、`project-structure.md`
  - 已确认首轮采集边界：私有公司，不跑 SEC / yfinance；重点抓 official / products / founder voice / jobs org / funding / media / community / podcast / YouTube
  - 已通过公开网页初步定位官方 Series A/B/C/D、pricing、enterprise、security、careers、founder interview、team blog、changelog 等核心源
  - 已停止 Cursor 播客 ASR worker；当前 ASR 状态为 0 成功、2 失败、1 running 被关闭、38 条因 max episode limit 延后

---

## 上一阶段任务：群核科技公开信息与年报/招股书采集

- 日期：2026-04-18
- 状态：首轮公开信息采集完成；已建立 `companies/qunhe/` 与 `QUNHE` target，已收集招股书、配发结果、会计师报告、经审计合并财务报表、备考财务资料、行业报告、官网与媒体 HTML；已确认 2025 年度不会另行发布完整年报，年度财务资料先以招股书及展示文件为主

### 已完成

- 群核科技：
  - 新增 `QUNHE` target，ticker 标记为 `00068.HK`
  - 建立 `companies/qunhe/vault/` 与 `companies/qunhe/analysis/`
  - 下载港交所官方英文/中文招股书、配发结果、展示文件页面
  - 下载展示文件中的会计师报告、经审计合并财务报表、未经审计备考财务资料、弗若斯特沙利文行业报告
  - 将核心 PDF 转为 txt 便于后续检索
  - 保存 Manycore / Kujiale / Coohom / Coohom Blog / PRNewswire 官方 HTML
  - 保存新浪、经济观察网、杭州网、每经网等媒体 HTML
  - 通用 web fetcher 已跑，Perplexity query 因 quota 401 受限；seed URL 与失败状态已落盘
  - 生成 `companies/qunhe/analysis/Qunhe_source_inventory_2026-04-18.md`
  - 生成 `companies/qunhe/analysis/Qunhe_fact_pack_2026-04-18.md`

---

## 上一阶段任务

- 名称：Anthropic 全网采集与通用化抓取代码
- 日期：2026-04-17
- 状态：正在把抓取系统改为 target manifest 驱动，并用 `ANTHROPIC` 做首个私有 AI Lab 全网最大化采集

## Goal

把现有抓取系统升级为 `config/company_targets.json` 驱动，避免把公司名写死在脚本里；随后用同一套链路为 Anthropic 收集 official / founder voice / podcast / YouTube / web longform / enterprise partnership / jobs org / social community / funding compute 材料。

## Context

- 四个核心 md 已建立，本轮进入项目结构重整与 Perplexity / Block 重新研究
- 仓库内已有播客、YouTube、补充搜索脚本：
  - `scripts/discovery/fetch_podcasts.py`
  - `scripts/discovery/fetch_podcast_transcript.py`
  - `scripts/discovery/fetch_youtube.py`
  - `scripts/discovery/fetch_perplexity.py`
- 用户反馈：Lovable 的组织分析明显更深，Perplexity / Block 需要按类似深度重新拆开分析
- 重新分析前先完成项目结构重整：
  - `codeX.md` 改名为 `Agent.md`
  - 每家公司建立 `companies/{company}/vault/`
  - 每家公司建立 `companies/{company}/analysis/`
- 已有 Perplexity / Block / Lovable 脚本输出需要同步到新 company vault
- 新目标：Anthropic，按私有 AI Lab 处理，研究 key 为 `ANTHROPIC`，目标目录为 `companies/anthropic/`
- 用户已确认：
  - 采集范围：全网最大化
  - 配置形态：JSON manifest

## Constraints

- 先参考四个核心 md，再进入正式研究
- 优先复用现有 scripts，不重复造轮子
- 抓取应优先落原始材料与转录，不用 AI 摘要替代原文
- 播客转录必须闭环：跑完后检查状态和失败清单；失败要重试；脚本有问题先修脚本再重试；不能把部分成功说成完成
- 音频 URL 预检失败或百炼远程拉取失败时，不能直接放弃；先下载到本地 `_audio_cache/`，再上传百炼 OSS 后重试转录
- 长音频 ASR 属于慢速可并行任务；本轮起拆给 sub agent，主线程继续做 Substack/长文和分析框架
- 本阶段优先级：
  1. 先完成项目结构
  2. 再重新抓 Perplexity / Block podcast
  3. 再补 Substack / 长文
  4. 最后分别重写两家公司组织分析
- 写作风格继续贴近 old friends：记者笔法、判断明确、少解释腔
- 成稿避免“不是 X，而是 Y”模板句，改用正向判断和证据压缩
- Anthropic 不跑 SEC / yfinance；重点抓 careers、founder voice、product docs、policy/safety、funding/compute、enterprise partnerships、developer/community adoption
- 新增抓取代码必须通用化，公司名、aliases、founder、channels 从 JSON manifest 读取

## Done when

- [x] 完成四个核心 md 前置检查
- [x] `codeX.md` 改名为 `Agent.md`
- [x] 建立 `companies/perplexity/`
- [x] 建立 `companies/block/`
- [x] 建立 `companies/lovable/`
- [x] 每家公司建立 `vault/` 与 `analysis/`
- [x] 已有原始数据同步进 company vault
- [x] Perplexity / Block 初版分析拆成独立 analysis 文件
- [ ] 重新完成 Perplexity / Block podcast 抓取与转录
- [ ] 播客失败项完成重试、脚本修复和最终状态记录
- [x] 已将 Perplexity / Block 播客转录拆给 sub agent 并行处理
- [x] 已修正转录脚本：URL 预检失败也进入本地下载 / 百炼 OSS fallback，而非直接失败
- [ ] 补抓 Perplexity / Block Substack / 长文
- [ ] 分别重写 Perplexity / Block 深度组织分析
- [x] 基于当前材料完成 Perplexity / Block / Lovable 三家公司长版复杂报告
- [x] 完成三家公司 Open Evidence 扩展提交版，按三问 bullet point 组织
- [x] Lovable 提交版按用户新重心重写：招聘筛选器、轻 cadence、office/lunch 信息密度、founder mode protective layer、enterprise muscle、controllable speed
- [x] Block 提交版二次压缩：删除泛泛 AI 流程/uncertainty，保留 company self-query、money signal、IC/DRI/player-coach、capability-gap roadmap、P&L 硬验证
- [x] 新增 `config/company_targets.json`，首个 target 为 `ANTHROPIC`
- [x] 新增 `scripts/discovery/target_config.py`
- [x] 新增 `scripts/discovery/fetch_web_sources.py`
- [x] 新增 `scripts/discovery/collect_target.py`
- [x] 改造 `fetch_youtube.py` 支持 `--target`
- [x] 改造 `fetch_podcasts.py` 支持 `--target` 并生成 curated episode list
- [x] 完成 Anthropic dry-run 验证
- [x] 完成 Anthropic 首轮 official / web / jobs / partnerships / funding 抓取
- [x] 完成 Anthropic YouTube 抓取：20 条候选中 12 条 transcript 成功，8 条无字幕失败可追踪
- [x] 完成 Anthropic podcast metadata 抓取：179 条独立相关 episode，已生成 curated list
- [ ] Anthropic podcast ASR 转录闭环进行中：已拆给 sub agent 跑前 80 条 curated episode
- [x] 生成 Anthropic source inventory 和 evidence map
- [x] 基于当前 Anthropic 全量材料与已同步播客转录，完成长版 AI 组织复杂报告
- [x] 新增 Anthropic live fact check，固定 2026-04-17 核验过的融资、run-rate、compute、enterprise partnership 动态事实
- [x] 按 `一页分析` PDF 风格完成 Anthropic 项目推荐版，压成公司简介 / 事 / 人 / 好公司 / 业务影响 / 好价格 / 竞争 / 风险指标结构

## Active Plan

- [x] 将 Anthropic 采集系统改为 `config/company_targets.json` 驱动
- [x] 完成通用 loader / web fetcher / orchestrator
- [x] 完成 Anthropic dry-run 与首轮抓取
- [x] 同步首轮产物到 `companies/anthropic/vault/`
- [x] 生成 Anthropic source inventory 与 evidence map
- [x] 补强 podcast metadata 文件名防碰撞
- [x] 补强 podcast ASR 状态文件：后续每个 episode 开始时先写 `running` heartbeat
- [ ] 等待 Anthropic podcast ASR sub agent 收口，检查 status/failures 后同步 transcript vault
- [ ] 对 ASR 失败项重试；如果失败来自脚本问题，先修脚本再重跑
- [x] 同步当前 Anthropic podcast ASR 成功产物：18 条 transcript 已进入 `companies/anthropic/vault/podcasts/transcripts/`
- [x] 撰写 `companies/anthropic/analysis/Anthropic_AI组织复杂报告_2026-04-17.md`
- [x] 撰写 `companies/anthropic/analysis/Anthropic_一页分析_2026-04-17.md`

## Progress Log

### 已完成

- Lovable 新任务：
  - podcast metadata 抓取完成，9 条落在 `scripts/LOVABLE/sources/podcasts/`
  - YouTube 抓取完成，15 条视频中 14 条成功落字幕，约 528k 字符
  - 定点补抓 Lenny 访谈原始 YouTube transcript：`Building Lovable: $10M ARR in 60 days with 15 people`
  - 复用并迁移此前已转录的 20VC Lovable podcast transcript 到 `scripts/LOVABLE/sources/podcasts_transcripts/`
  - 完成 Lovable AI 组织分析文稿：`Lovable_AI组织分析.md`
- 项目结构重整：
  - `codeX.md` 已改名为 `Agent.md`
  - 新增 `companies/perplexity/`
  - 新增 `companies/block/`
  - 新增 `companies/lovable/`
  - 三家公司均已建立 `vault/` 与 `analysis/`
  - 已把现有 podcast / transcript / YouTube / financials 同步进对应 company vault
  - 已将 `Perplexity_Block_AI组织分析.md` 拆成公司级分析稿
  - 已将旧根目录分析稿归档到 `companies/_legacy/`
  - 已新增 `companies/README.md` 作为公司目录使用说明
- 本轮 Perplexity / Block 重抓：
  - 已增强 podcast metadata 脚本，支持公司别名和短 ticker 精确匹配
  - 已增强 podcast transcript 脚本，支持 curated episode JSON、状态文件、失败文件、多轮重试和行缓冲 checkpoint
  - 已继续增强 podcast transcript 脚本：远程 URL 被百炼拒拉时，自动下载到 `_audio_cache/` 并上传到百炼 OSS 后重试转录
  - 已再次增强 podcast transcript 脚本：URL 预检失败不再直接放弃，而是继续进入本地下载 / 百炼 OSS 兜底；长音频百炼轮询时间改为 `PODCAST_MAX_POLL_SECONDS` 可配置
  - 已重新抓取 Perplexity podcast metadata：72 条
  - 已重新抓取 Block podcast metadata：17 条
  - 已生成组织分析用 curated podcast 清单：Perplexity 8 条，Block 12 条
  - 已将 Perplexity / Block 音频转录分别拆给 sub agent 并行处理
  - 已新增 Perplexity / Block web source notes，记录 Substack/长文/官方材料抓取结果
  - 已新增 Perplexity / Block evidence map，先拆组织证据和待验证缺口
  - 已新增 Perplexity / Block v2 working draft，明确标注等待剩余 podcast transcript
  - 已按用户给的字节样文结构，完成 Perplexity / Block / Lovable 三家公司复杂报告
  - 已新增三家公司 Open Evidence 扩展提交版，每家公司分别回答 founder 洞见、组织动作、业务影响三问
  - 已根据用户新反馈回翻 Lovable 组织分析、Lenny 访谈、20VC、Stripe 对话，将 Lovable 提交版改成更强调招聘模式、轻 cadence、线下信息密度、protective layer 和企业化组织补课
  - Block 播客转录子 agent 回报：12 条 curated 中 8 条成功、4 条失败；失败原因集中为 `FILE_DOWNLOAD_FAILED`，已同步状态与失败清单到 `companies/block/vault/podcasts/transcripts/`
  - 已根据用户反馈二次压缩 Block 提交版：去掉“AI 进入核心流程”和泛泛 uncertainty，改为围绕 company intelligence、money signal、role redesign、capability-driven roadmap 和 P&L 验证写
  - Anthropic 通用抓取代码已实现：
    - 新增 `config/company_targets.json`
    - 新增 `scripts/discovery/target_config.py`
    - 新增 `scripts/discovery/fetch_web_sources.py`
    - 新增 `scripts/discovery/collect_target.py`
    - `fetch_youtube.py` / `fetch_podcasts.py` 支持 `--target`
  - Anthropic 首轮采集已跑：
    - official：9/10 成功
    - founder_voice：8/50 成功，失败多为页面太短/不可抓全文，但 URL 已保留
    - enterprise_partnerships：2/5 成功
    - jobs_org：1/1 成功
    - web_longform：3/10 成功
    - funding_compute：1/6 成功
    - social_community：0/9 全部 indexed/fetch failed，仍保留 URL index
    - youtube：12/20 transcript 成功，约 1.52M 字符
    - podcasts：179 条 metadata，curated list 已生成
  - Perplexity API 已出现 quota 401，后续 web discovery 需优先靠 seed URLs / 官方源 / web search 工具补足
  - Anthropic podcast ASR 已交给 sub agent 跑前 80 条 curated episode；当前不能算 transcript 闭环完成
  - Anthropic podcast ASR 当前已有 2 条成功 transcript（Jared Kaplan / Life with Machines 等）并已同步到 `companies/anthropic/vault/podcasts/transcripts/`
  - Anthropic podcast ASR 当前 3 条失败，失败原因均为远程拉取与 OSS 兜底后仍 `FILE_DOWNLOAD_FAILED`；脚本仍在继续处理后续 episode
  - 已补强 podcast metadata 文件名防碰撞，避免同名 episode 覆盖导致 JSON 数量与落盘 markdown 数量不一致
  - 已补强 podcast transcript 状态文件：后续每个 episode 开始前先写 `running` heartbeat，避免长音频轮询时外部无法判断是否卡住
  - 已补强 YouTube / podcast / transcript frontmatter 转义，避免标题自带引号时生成不可解析 YAML
  - 已修正 transcript existing 检查：从标题前缀模糊匹配改为 frontmatter `title + date` 精确匹配，避免相近标题被误判为已完成
  - 已修正 `collect_target.py`：如果当天 evidence map 已经存在，后续重跑不再用占位模板覆盖人工整理过的证据地图
  - Anthropic podcast ASR 已由新 sub agent 接管继续跑，当前进程 PID 28680，状态文件能看到 `running` heartbeat
  - 已同步 Anthropic 当前 ASR 成功产物到 company vault：18 条 podcast transcript 可用于写作；后台 ASR 进程仍在继续，尚未闭环
  - 已新增 `companies/anthropic/analysis/Anthropic_live_fact_check_2026-04-17.md`，记录 Series G、run-rate revenue、Google/Broadcom compute、Salesforce/Cognizant/IBM partnership 等动态事实来源
  - 已新增 `companies/anthropic/analysis/Anthropic_AI组织复杂报告_2026-04-17.md`，按 Founder 认知、组织动作、业务影响、对比视角和关键不确定性写成长版报告
  - 已新增 `companies/anthropic/analysis/Anthropic_一页分析_2026-04-17.md`，参照 `一页分析` PDF 写成项目推荐页风格，保留估值、收入、组织动作、业务影响、竞争和风险跟踪指标
- 读完 `Agent.md`、学习目录、抓数 skill、投资框架
- 定位到播客抓取与转录脚本
- 验证本地环境可 import `dashscope`
- 确认转录脚本中已有 DashScope / 百炼配置
- 确认当前历史输出主要落在 `scripts/{TICKER}/sources/podcasts_transcripts/`
- 完成四个核心 md 的初版搭建
- 明确本轮目标公司为 `Perplexity` 与 `Block`
- 完成两家公司播客 metadata 抓取：
  - `Block`: 17 条
  - `Perplexity`: 15 条
- 完成第一轮播客转录：
  - `Block`: 4/5 条长音频成功
  - `Perplexity`: 3/9 条长音频成功
- 已补强 `scripts/discovery/fetch_podcast_transcript.py`：
  - DashScope 瞬时网络错误自动重试
  - 同一条播客按多个 URL 形态重试
- 已补强 `scripts/discovery/fetch_youtube.py`，但用户已明确当前先收口 podcast 线
- 补充收获：定向 YouTube 抓取已落部分高价值视频，但当前仍以 podcast 为主线
- 已完成一版 `Perplexity / Block` 的可提交 md 文稿，并补入更多 podcast / founder 原话
- 已将 `Perplexity` 的重心从“产品定义”改回“组织变革”：
  - 当前最关键的判断是：Perplexity 已明显改变工作节奏、激励方向与反馈链条
  - 但这套 AI 组织仍更像 founder mode，而非已经制度化完成

### 进行中

- 准备按新结构重做 Perplexity / Block 的播客抓取、拆解和 Substack 补充

### 待处理

- 重新跑 Perplexity / Block podcast metadata 与 transcript
- 将新抓取结果同步到 `companies/perplexity/vault/` 和 `companies/block/vault/`
- 补抓 Perplexity / Block 的 Substack / 独立长文 / 高质量报道
- 分别重写 `companies/perplexity/analysis/Perplexity_AI组织分析.md`
- 分别重写 `companies/block/analysis/Block_AI组织分析.md`

## Decisions

- serious planning 前必须先读四个核心 md，其中最高优先级文件为 `Agent.md`
- 当前优先使用 `scripts/discovery/` 版本脚本，与历史输出路径保持一致
- 抓播客时先抓 metadata，再跑 transcript
- 用户当前要求：先完成 podcast + 阿里云 transcript，再继续
- `Perplexity` 按非上市公司处理，优先原始内容；`Block` 后续再扩财务与其他源
- 当前交付文稿优先写得像“记者/old friends”，而不是解释型摘要
- 写 `Perplexity` 时，优先写“工作单元 / 激励 / 信息流 / founder 依赖”，避免滑向产品定义
- 写 `Lovable` 时，核心不是“AI app builder 产品定义”，而是“产品团队的组织重构”：工程瓶颈下降后，taste、用户理解、端到端判断和 governance 成为新组织重心
- `scripts/` 只作为采集 staging；长期研究材料以 `companies/{company}/vault/` 为准
- 最终分析以 `companies/{company}/analysis/` 为准

## Risks / Open Questions

- Apple Podcasts 搜索存在噪音，后续仍需人工筛 relevance
- 一部分播客音频 URL 会出现 DashScope `FILE_DOWNLOAD_FAILED`
- 一部分任务在 DashScope 轮询阶段会出现 SSL / RemoteDisconnected 类瞬时错误
- 当前判断：
  - `Block` 剩余 1 条大概率属于可重试网络类问题
  - `Perplexity` 剩余条目里，部分是可重试网络问题，部分是 DashScope 对某些音频源拉取失败
- 当前写作风险：
  - 组织洞见容易滑向空泛管理话术
  - 原话引用过多会牺牲成稿密度
- Lovable 本轮限制：
  - podcast 整批 DashScope 转录曾启动，但长时间无中间落盘，已中断改为高相关优先
  - YouTube 泛搜索抓到部分教程噪音，分析只采用 Founder / 投资人 / 官方材料
  - 官网资料对业务影响更强，对内部组织细节仍需 Founder 访谈交叉验证

## Validation

- [x] 核心脚本存在
- [x] 关键依赖存在
- [x] 核心文档体系完成
- [x] 抓取路径与命名符合项目约定
- [x] 实际生成播客元数据
- [x] 实际生成播客转录（部分成功）
- [ ] 失败条目完成最大化补救
- [x] Lovable 分析文稿完成

## Next Action

按新结构重新抓取与拆解 Perplexity / Block podcast，并补充 Substack / 长文材料。
