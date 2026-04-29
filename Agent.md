# Agent 协作操作系统

> 这是本项目的最高优先级工作规范。只要任务进入“认真 plan / 多步骤执行 / 研究产出”阶段，必须先参考本文件与另外三个核心文件。

## 0. 四个核心文件

每次进入认真 planning 前，必须先快速重读这四个文件：

1. `Agent.md`
   作用：定义协作协议、任务节奏、执行标准、文档维护规则。
2. `progress.md`
   作用：记录当前任务状态、已完成、进行中、风险、下一步。
3. `core-principles-and-lessons.md`
   作用：沉淀稳定准则、方法论、踩坑教训、可复用判断框架。
4. `project-structure.md`
   作用：说明目录结构、脚本职责、输出路径、命名与落盘约定。

**硬规则**：
- 不允许在没看这四个文件的情况下直接展开复杂 plan。
- 如果这四个文件之间出现冲突，优先顺序为：
  `Agent.md` > `progress.md` > `core-principles-and-lessons.md` > `project-structure.md`
- 每次复杂任务结束后，至少检查是否需要更新 `progress.md` 和 `core-principles-and-lessons.md`。

---

## 1. 什么叫“认真 plan”

以下任一情况都算进入“认真 plan”阶段：
- 任务涉及多步骤执行
- 任务涉及多文件或多模块
- 任务需要抓数、转录、清洗、分析、写结论的链路
- 任务需要做投资判断，而不只是搬运信息
- 任务要产出可复用文档、模板或项目规范
- 任务存在明显的依赖、风险、决策分叉或验证要求
- 任务里有长音频转录、批量抓取、失败重试等慢速可并行环节

一旦进入这个阶段，必须先做第 2 节的 Pre-Plan Protocol。

---

## 2. Pre-Plan Protocol

正式 plan 前固定执行以下步骤：

### Step 1. 刷新四个核心文件
- 重读 `Agent.md`
- 检查 `progress.md` 当前状态是否过期
- 检查 `core-principles-and-lessons.md` 是否有适用于本任务的准则/教训
- 检查 `project-structure.md` 是否有脚本、路径、输出约定需要遵守

### Step 2. 明确任务四件套
必须写清楚或在脑中明确：
- `Goal`：最终交付物是什么
- `Context`：现有材料、脚本、目录、信源、已有研究有哪些
- `Constraints`：边界、不可做、风格、时效、来源、格式要求
- `Done when`：做到什么程度才算完成

### Step 3. 更新 `progress.md`
至少刷新这些内容：
- 当前目标
- 当前状态
- 当前 plan
- 已知风险/缺口
- 下一步动作

### Step 4. 再输出正式 plan
plan 必须：
- 步骤少而清晰
- 每一步都有可观察产出
- 尽量能并行
- 有验证点
- 有失败后的回退方式
- 明确哪些慢任务应该交给 sub agent，主线程继续推进非阻塞工作

---

## 3. 默认工作流

### A. Intake
- 先理解用户真实目标，不急着动手
- 能从本地环境确认的，不把问题抛回给用户
- 只有在缺少关键参数且无法安全假设时才提问

### B. Context Build
- 优先读代码、脚本、已有数据、项目文档
- 优先看原始材料，而不是二手摘要
- 先建立路径感和数据流，再开始执行

### C. Plan
- 给出可执行 plan
- 计划必须与现有项目结构和脚本能力对齐
- 如果脚本已有 80% 能力，优先复用，不重复造轮子

### D. Execute
- 边做边更新用户进展
- 执行链路中出现新事实后，要及时修正 plan
- 不因早期假设错误而硬做到底
- 长音频 ASR、批量网页抓取等慢任务应交给 sub agent 持续执行，不阻塞主线程

### E. Verify
- 验证脚本是否真的跑通
- 验证输出是否落到正确路径
- 验证结果是否满足任务要求，而不是只看“命令成功”

### F. Synthesize
- 先区分“已确认”和“推断”
- 先组织证据，再写结论
- 结论必须能回到原始材料与行动证据

### G. Retrospect
- 把通用规则写回 `core-principles-and-lessons.md`
- 把当前状态写回 `progress.md`
- 必要时更新 `project-structure.md` 和 `Agent.md`

---

## 4. 文档维护分工

### `Agent.md`
记录：
- 工作协议
- planning 规则
- 执行规则
- 协作习惯
- 文档维护规则

何时更新：
- 用户对工作方式提出新要求
- 现有协议不够规范
- 出现反复犯错、反复提醒的问题

### `progress.md`
记录：
- 当前活跃任务
- 已完成
- 进行中
- 风险/阻塞
- 决策
- 下一步

何时更新：
- 开始认真 plan 前
- 完成关键阶段后
- 发现新阻塞或新决策后
- 每次大块执行结束后

### `core-principles-and-lessons.md`
记录：
- 稳定方法论
- 研究和投资判断准则
- 抓数与转录的经验规则
- 失败案例与修正教训

何时更新：
- 出现可复用方法
- 某次踩坑值得沉淀
- 某类判断标准被验证有效

### `project-structure.md`
记录：
- 目录说明
- 关键脚本与职责
- 输出路径
- 命名规则
- 数据流与依赖关系

何时更新：
- 新增目录/脚本
- 输出路径变化
- 执行约定变化

---

## 5. 研究与抓数执行准则

### 5.1 原始材料优先
- 优先 Founder 原声、播客、访谈、财报、产品原文、组织原始证据
- 不以 AI 摘要代替原文
- 如果只能拿到摘要，要明确标注其性质和限制

### 5.1.0 播客搜索前的元思考
- 搜 podcast 前必须先做关键词地图，不允许只搜公司名。
- 关键词地图至少包含：
  - 公司名、简称、旧名、产品名、核心协议/技术名
  - Founder、CEO、C-level、关键产品/研究/商业负责人
  - 公司对应行业关键词和行业访谈关键词
  - 重要客户、伙伴、竞争对手
  - 组织与 AI 转型相关词，如 hiring、org、culture、AI transformation、agent、workflow、developer productivity
- 关键词地图必须落盘为 `_podcast_query_map.md` 或同等文件，后续 source inventory 要能解释“为什么搜这些词”。
- YouTube、Substack、web longform、X、Reddit、LinkedIn 搜索必须继承 podcast 阶段形成的关键词地图，不能每个平台重新临时想关键词。
- 每个 source 都要逐个关键词搜索，并在自己的 `_query_map.md` / `_search_status.json` 里记录 `query -> returned urls/posts -> selected -> rejected/reason`。
- 如果某个关键词在 YouTube / Substack / X 上太宽，先追加 source-specific 限定词、人物名、产品名、时间范围或站点限定收窄；不能直接跳过。
- YouTube 默认 provider 顺序是：Search `rapidapi_metadata_search` -> `yt_dlp_search`；Transcript `rapidapi_transcript3` -> `youtube_transcript_api` -> `yt_dlp_subtitle`。RapidAPI key 只读 `RAPIDAPI_KEY` 环境变量；缺 key、401/403、429、空 transcript 都要写入 status，再切 fallback，不能静默跳过。
- YouTube 必须在下载 transcript 前做 metadata relevance gate：先用 company / Founder / 明确产品组合 / exclude terms 判断候选是否值得烧 transcript API；`match_count=0` 或只命中泛词的候选要过滤并记录。像 `Niji`、`Moodboards`、`Rooms`、`vibe coding` 这类宽词不能单独构成下载资格，必须和公司或明确负责人/产品语境共同出现。
- YouTube 抓取必须输出 `_youtube_query_map.md`、`_youtube_search_status.json`、`_youtube_candidates.json`、`_youtube_rejected_candidates.json`、`_youtube_collection_status.json`、`_youtube_collection_failures.json`；status 必须写 `api_request_counts`，方便估算 free plan 消耗；RapidAPI transcript 成功时还要保留 `.segments.json` sidecar。
- 已知时长小于 10 分钟的 podcast episode 默认不抓、不转录；未知时长不直接丢弃，后续 relevance review 再判断。
- `skipped_short` 与 `deferred_max_limit` 是可解释跳过，不应混入真实失败清单；真实失败只保留需要重试、修脚本或标准音频兜底的条目。

### 5.1.1 播客 ASR provider 顺序与标准音频兜底
- 播客转录失败不能停在单一 provider 报错。默认 ASR 顺序是：`Groq Whisper URL` -> `DashScope/百炼 URL` -> `本地下载 + DashScope OSS` -> `标准音频 + DashScope REST`。
- Groq 作为第一 provider：
  1. 先使用 RSS enclosure / metadata 里的原始 `audio_url` 作为公网 URL 直接提交 Groq Whisper；这一步最快，也不需要 OSS。
  2. Groq 请求必须使用 `multipart/form-data`；即使传的是 `url` 字段，也不能用普通 form-urlencoded。
  3. 如果 Groq 返回额度不足、rate limit、远程 URL 拉取失败、文件过大、转录空结果或其他错误，记录 provider attempt，然后切到 DashScope/百炼，不要卡住。
- DashScope/百炼作为第二 provider：
  1. Groq 失败后，再把同一批候选 `audio_url` 提交给 DashScope/百炼 Paraformer。
  2. 如果 RSS 原始音频 URL 失败、过期、403、云端读取失败或转录空结果，才下载音频到 `_audio_cache/` 或同级临时目录。
  3. 本地下载成功后，优先上传到百炼 OSS，再用 OSS 地址转录。
  4. 如果本地下载和 OSS 上传都成功，但 DashScope 仍报 `FILE_DOWNLOAD_FAILED`，进入标准音频兜底：优先 `mp3`；如果本机没有 `ffmpeg` 或 MP3 编码不可用，使用百炼同样支持且更稳的 `wav`，推荐 `16kHz / mono / 16-bit PCM`。
  5. 标准化音频放到 `_standard_audio/`，不要和原始缓存混在一起。
  6. 上传标准化音频到 OSS 后，用 RESTful API 提交转录；需要 `oss://` 临时 URL 或 `X-DashScope-OssResourceResolve` header 时，不要走 Python SDK，因为 SDK 不支持这些 header / `oss://` 场景。
  7. 写出 transcript 后，必须检查 markdown 非空、包含 `## Transcript`、状态 JSON 中对应条目为 success，再删除原始下载音频。
  8. `_audio_cache/` 和 `_standard_audio/` 不同步到 company vault，vault 只保留 transcript、status、failures。
- 每份 transcript frontmatter 应记录 `transcription_provider` 和 `transcription_engine`，状态 JSON 应记录 provider attempts，方便追踪 Groq / DashScope / OSS 哪一层成功或失败。
- 参考官方文档：
  - Groq Speech to Text: https://console.groq.com/docs/speech-to-text
  - Paraformer RESTful API: https://help.aliyun.com/zh/model-studio/paraformer-recorded-speech-recognition-restful-api
  - Paraformer Python SDK: https://help.aliyun.com/zh/model-studio/paraformer-recorded-speech-recognition-python-sdk

### 5.1.2 Transcript 后处理与 Essence 层
- 具体执行使用 `学习/skills/essence/SKILL.md`；`collect` 只负责抓取和同步，`analysis` 默认从 essence 开始读。
- 每次抓完 podcast / YouTube / Substack / web transcript 后，不能直接进入最终分析。
- 固定后处理顺序：
  1. 先做 relevance review。和公司、行业、管理层、产品、组织或投资主题相关性太低的材料，标为淘汰，不进入 essence。
  2. 对高相关材料逐条提炼 essence。每条 transcript / article 必须一一对应一份 essence 文档。
  3. Essence 提炼必须采用 sequential pass：从 source 开头往后顺序读，一段一段判断是否值得保留。用户确认的角度只作为优先级提示，不能先预设一个高层角度再俯瞰式摘材料。
  4. 每份 essence 必须包含多条 insight blocks，不能做成“一篇一条总结”：每读到一个重要段落、机制、业务数据、管理层判断、组织动作、产品战略、用户反馈或可投资化证据，就新增一条 block。
  5. 每条 insight block 的基本格式是：短标题 + 一段可直接进入报告的详实判断自然段 + 紧贴判断自然段的 quote pack。标题下面直接进入判断自然段，不加 `**判断段**` 这类标签；不要使用“关键引用 / 近原文证据”标题，不要用“近原文”冒充引用，也不要加 `可用于哪些分析角度`、`原文定位` 这类工具性尾巴。quote pack 不是象征性的一句证据，默认保留 3-8 条高信息密度原文，允许完整长句，给后续手动改写留出剪裁空间。判断自然段要像研究 memo 的自然段，不要写成机械摘要。
  6. Essence 语言要像人写的研究笔记：有判断、有细节、有语气，少黑话。避免二元对照模板句；核心概念可以保留英文，如 `workflow`、`feedback loop`、`cadence`、`owner`、`context`，但英文词必须服务判断。当前风格基准是 `学习/style_references/anthropic_org_investment_style_notes_2026-04-21.md`。
  7. 长访谈和长文出现十几条到几十条 insight blocks 是正常结果；不要为了简洁把不同主题强行合并。
  8. 进入正式分析前，优先读 essence；raw transcript 只用于追溯核验，不作为主要阅读入口。
- Essence 写作前必须先向用户确认本次提炼角度。默认候选角度包括：
  - 组织结构相关核心信息
  - 管理层的思考
  - 组织形态与业务的关系
  - 招聘技巧、人才标准、人才密度
  - 内部如何进行 AI 转型
  - AI 相关管理工具、agent、workflow
  - 过去使用哪些管理工具，现在发生了什么工具变化
  - AI 如何和人协作
  - 每家公司的管理产品是什么
  - 工具体系如何构成
  - 管理产品背后的世界观是什么
  - 商业模式、行业结构、业务数据、CEO 对行业的哲学判断
- 默认输出目录：
  - podcast essence: `companies/{slug}/vault/podcasts/essence/`
  - YouTube essence: `companies/{slug}/vault/youtube/essence/`
  - Substack essence: `companies/{slug}/vault/substack/essence/`

### 5.2 证据分层
- 一手高价值：Founder/高管原话、财报电话会、官方文档、原始转录
- 二手支持：媒体采访、行业分析、研究文章
- 低置信补充：社媒讨论、论坛情绪、非结构化点评

### 5.3 组织研究默认三问
对每家公司默认回答：
1. Founder 对 AI 组织的独到见解是什么？
2. Founder 在组织落地上做了哪些具体动作？
3. 这些动作对业务产生了什么影响？

### 5.4 组织到业务的传导链
默认判断顺序：
`Founder认知 -> 组织动作 -> 机制变化 -> 执行结果 -> 业务影响 -> 市场/投资意义`

### 5.5 明确区分
- 已验证事实
- 强推断
- 弱推断
- 待验证问题

---

## 6. 输出标准

### 对外输出
- 先说结论，再给依据
- 不堆砌资料
- 让每一段都服务于任务目标

### 对内文档
- 优先可维护、可复用、可追踪
- 模板不要空泛，要能直接拿来用
- 任务进行中允许不完美，但必须真实反映状态

---

## 7. 失败与修正规则

如果执行过程中出现以下情况，必须修正而不是硬推进：
- 目标公司不明确
- 输出路径不对
- 脚本能跑但结果不对
- 抓到了元数据但没抓到可用原文/转录
- 结论建立在低质量证据之上
- 当前规范不足以支撑任务

修正动作优先顺序：
1. 先更新 `progress.md`
2. 再修正 plan
3. 必要时补充到 `core-principles-and-lessons.md`
4. 如果属于流程层面问题，回写 `Agent.md`

---

## 8. 当前阶段特别规则

本项目当前处于“研究工作流搭建 + 播客原始材料沉淀”阶段，因此：
- 优先完善流程，不急着写最终结论
- 优先沉淀可反复使用的规范和结构
- 优先抓 Founder/管理层的原始播客与转录
- 每次 serious plan 前先看四个核心 md，这一条必须执行

---

## 9. 执行口令

每次准备认真开工时，默认按以下顺序走：

1. 看四个核心文件
2. 更新 `progress.md`
3. 输出计划
4. 执行
5. 验证
6. 回填文档

如果没走完这六步，不算完整执行。
