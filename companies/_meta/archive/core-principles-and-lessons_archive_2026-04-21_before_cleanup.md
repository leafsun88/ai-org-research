# Core Principles And Lessons

> 这里沉淀的是能跨任务复用的稳定准则，不是一次性进度。每次 serious plan 前先扫一遍。

## 一、核心准则

### 1. 先搭系统，再堆内容
- 如果流程还不稳定，先修流程
- 如果目录、输出、命名不清楚，先修结构
- 如果规范不够支撑任务，先写规范再执行

### 2. 复杂任务先看四个核心文件
- `Agent.md`
- `progress.md`
- `core-principles-and-lessons.md`
- `project-structure.md`

没有完成这一步，不进入 serious planning。

### 3. 原始证据优先于摘要
- Founder 原声 > 二手媒体总结
- 播客/访谈转录 > 节目简介
- 官方文档/财报 > 三方复述
- AI 生成总结不能替代原文

### 4. 投资研究先看组织，再看业务映射
默认分析链条：

`Founder认知 -> 组织机制 -> 执行动作 -> 业务结果 -> 投资意义`

### 5. 组织研究默认回答三问
1. Founder 对 AI 组织有什么独到见解？
2. Founder 在 AI 组织落地上做了哪些具体动作？
3. AI 组织变革对业务有什么影响？

### 6. 事实与推断必须分开
- 能被原始材料直接支持的是事实
- 跨证据拼出来的是推断
- 没有足够支撑的只能列为待验证问题

### 7. 复用已有脚本，少造新轮子
- 先看仓库里有没有现成链路
- 能 patch 就不重写
- 能配置就不重构

### 8. 慢速抓取任务要并行代理化
- 播客转录、长音频 ASR、批量网页抓取这类慢任务，不应该阻塞主线程
- 一旦用户允许使用 sub agent，慢任务应拆给子 agent 持续跑
- 主线程继续做不依赖该结果的工作，比如 Substack/长文补抓、证据框架搭建、目录同步
- 子 agent 必须交付状态文件、失败清单、重试记录，而不是只说“跑了”

### 9. 输出必须可追踪
- 结果要能回到路径
- 结论要能回到材料
- 失败要能回到原因

### 10. `companies/` 是研究主目录
- `scripts/` 负责采集和历史输出，不再承担最终研究归档职责
- 每家公司用 `companies/{company}/vault/` 存原始证据
- 每家公司用 `companies/{company}/analysis/` 存最终分析
- 重抓数据后必须同步到对应 company vault，避免材料散在 `scripts/` 里
- `companies/` 根目录只放当前公司目录、`_meta/`、`_legacy/` 和说明文件；不要把临时 inventory、queue、format test 或历史 sample company 直接铺在根目录

### 11. 成稿避免模板化转折
- 投资 memo 和提交版里避免二元对照类 AI 腔模板
- 优先写正向判断：`X > Y`、`核心变量是 X`、`动作指向 X`
- 需要对比时压成短标题或并列判断，不靠转折句撑结构

### 12. 私有 AI Lab 走 target manifest
- Anthropic / Lovable / Perplexity 这类私有或非标准 ticker 标的，不应靠脚本内置 ticker 字典或命令行临时参数维持
- 公司名、别名、founder、executive、渠道、seed URL、输出路径统一写进 `config/company_targets.json`
- 脚本只读 manifest，不把公司名硬编码进 Python
- 私有 AI Lab 默认跳过 SEC / yfinance，重点抓 careers、founder voice、product docs、policy/safety、funding/compute、enterprise partnerships、developer/community adoption

---

## 二、当前项目适用的方法论

### A. 抓播客的默认顺序
1. 先做 podcast 搜索元思考，列出公司名、别名、Founder/C-level、产品、行业、客户/伙伴/竞品、组织/AI 转型关键词
2. 保存 `_podcast_query_map.md`，让搜索完整性可追溯
3. 再抓 podcast metadata
4. 默认跳过已知短于 10 分钟的 episode；未知时长不直接丢弃
5. 再筛可转录长音频
6. 再跑 transcript
7. 检查转录状态文件和失败清单
8. 对失败条目重试；如果仍失败，检查并修正脚本后再重试
9. `skipped_short` 与 `deferred_max_limit` 是可解释跳过，不算真实失败；真实 failure list 只放需要重试或修脚本的条目
10. 再人工筛 relevance
11. 高相关材料逐条提炼为 essence，后续分析优先基于 essence，而不是直接啃 raw transcript

播客任务只有在“全部成功”或“剩余失败均有明确原因、URL、已尝试修复动作”后才算收口。

YouTube / Substack 搜索必须继承 podcast 阶段的 `_podcast_query_map.md`。Podcast query map 是整家公司公开材料搜索的关键词底座，不是播客专用文件。每个 source 都要逐个关键词搜索，再按平台加限定词；如果关键词太宽，先收窄，不直接跳过。每个平台必须留下 query coverage，记录每个关键词是否搜索、返回了什么、选了什么、为什么拒绝其他结果。X / Reddit / LinkedIn / broad web longform 只作为 explicit opt-in，不进入默认采集。

YouTube 默认把 RapidAPI 作为反爬增强路径，不替代可追溯的状态记录。Search 顺序是 `rapidapi_metadata_search` -> `yt_dlp_search`；Transcript 顺序是 `rapidapi_transcript3` -> `youtube_transcript_api` -> `yt_dlp_subtitle`。`RAPIDAPI_KEY` 只放环境变量，脚本和 markdown 不保存真实 key。401/403 要停止 RapidAPI provider 并切 fallback；429/quota 要把剩余候选标记为 deferred；无结果、空 transcript、无字幕都必须进入 `_youtube_search_status.json` 或 `_youtube_collection_failures.json`。状态文件必须记录 API 消耗量，至少包括 `rapidapi_metadata_search_calls` 和 `rapidapi_transcript3_calls`。

YouTube transcript 下载前必须先做 metadata relevance gate。RapidAPI fuzzy search 的召回很强，但会把普通词、产品泛词、同名词带进来；候选必须命中 company / Founder / 明确公司产品组合，且不能命中 exclude terms，才进入 transcript provider。宽词不能单独放行：`Niji` 可能是偶像名，`Moodboards` 可能是普通创意访谈，`vibe coding` 可能是泛行业视频；这些词只能辅助排序，不能作为下载资格。被挡掉的候选必须写进 `_youtube_rejected_candidates.json`，让后续知道是“搜到了但主动拒绝”，不是漏抓。

Podcast / YouTube / Substack / web transcript 抓完后，必须先做 relevance review。相关性太低的材料要标记淘汰；相关性高的材料必须一一对应生成 essence 文档，但 essence 不能压成“一篇一条总结”。每个高相关 source 内部应拆成多条 insight blocks：每读到一个重要段落、机制、业务数据、管理层判断、组织动作、产品战略、用户反馈或可投资化证据，就新增一条 block。标题下面直接进入详实判断自然段，不加 `**判断段**` 这类标签；判断自然段后面直接贴 quote pack，不再使用“关键引用 / 近原文证据”标题。quote pack 默认保留 3-8 条高信息密度原文摘录，允许完整长句，给后续手动改写留出剪裁空间。insight block 不再加 `可用于哪些分析角度`、`原文定位` 这类工具性尾巴。正式分析优先读 essence，raw transcript 只做追溯核验。

Essence 提炼必须采用 sequential pass：从 source 开头往后顺序读，一段一段判断是否值得保留。用户确认的角度只作为优先级提示，不能先预设一个高层角度再俯瞰式摘材料。每一段都问一次：这里有没有新的机制、动作、数字、管理层判断、组织信号、产品策略、用户反馈、商业模式、竞争信息或可投资化证据？有，就新增 insight block 或并入正在形成的同一机制 block；没有，才跳过。这样做是为了防止高层框架先行导致细节漏掉。

Essence 语言风格要像人写的研究笔记，有判断、有细节、有语气，避免二元对照模板句，少用黑话。核心概念可以保留英文，如 `workflow`、`feedback loop`、`cadence`、`owner`、`context`，但英文词必须服务判断，不要当装饰。当前风格基准是 `学习/style_references/anthropic_org_investment_style_notes_2026-04-21.md`。

做 essence 前要先问用户确认本轮提炼角度。默认角度库：组织结构、管理层思考、组织形态与业务关系、招聘技巧、AI 转型、AI 管理工具、旧管理工具如何变化、AI 与人协作、管理产品、工具体系、管理产品世界观、商业模式、行业结构、业务数据、CEO 行业哲学。

默认先走轻路径，但 provider 顺序已调整为 Groq 优先：优先使用 RSS enclosure / episode metadata 里的原始 `audio_url` 作为公网 URL 直接提交 Groq Whisper。Groq 失败、额度不足、rate limit、远程 URL 拉取失败、文件过大或转录空结果时，再把同一批候选 URL 交给 DashScope/百炼。只有 Groq 与 DashScope URL 路径都失败，才进入本地下载、OSS 上传或标准音频兜底。不要一上来就下载和转码所有音频。

Groq 的一个实现细节必须记住：即使传的是 `url` 字段，也要用 `multipart/form-data` 请求；普通 form-urlencoded 会返回 `request Content-Type isn't multipart/form-data`。Groq URL 拉取遇到 307 redirect 时可能失败，这种情况直接进入 DashScope URL 或本地下载兜底。

如果远程音频 URL 对浏览器/curl 可访问，但百炼 ASR 报 `FILE_403_FORBIDDEN`、`FILE_DOWNLOAD_FAILED` 或长时间超时，要升级为本地音频 fallback：先下载到 `_audio_cache/`，再上传到百炼 OSS，最后用 OSS 地址转录。

如果脚本的 URL 预检失败，也不能马上把 episode 判死刑。预检只是节省 API 调用的保护层，不是最终裁判；只要链接仍像音频源，就继续走本地下载和 OSS 上传兜底。

如果本机下载成功、OSS 上传也没有直接失败，但 DashScope 子任务仍报 `FILE_DOWNLOAD_FAILED`，要继续升级为“标准音频 + REST API”兜底：
- 先把本地音频转成标准格式。优先 `mp3`；如果本机没有 `ffmpeg` 或 MP3 编码不可用，用百炼同样支持且更稳的 `wav`，建议 `16kHz / mono / 16-bit PCM`。
- 标准音频统一放入 `_standard_audio/`，不要和 `_audio_cache/` 混放。
- 上传标准音频到 OSS 后，使用 Paraformer RESTful API 提交；需要 `oss://` 临时 URL或 `X-DashScope-OssResourceResolve: enable` 时不要用 Python SDK，因为官方文档说明 SDK 不支持 `oss://` 临时 URL，也不支持配置该 header。
- 转录成功后先校验 markdown transcript 非空、包含正文、状态 JSON 成功，再删除原始 `_audio_cache` 文件；标准化音频可短期保留复查，但不得同步进 company vault。
- 官方依据：
  - RESTful API 支持 HTTP/HTTPS URL，REST 场景支持 `oss://` 临时 URL，并可在 header 中启用 `X-DashScope-OssResourceResolve`。
  - Python SDK 不支持 `oss://` 临时 URL，也不支持配置该 header。
  - 官方支持 `mp3`、`m4a`、`wav` 等格式，但也明确说格式变种无法穷尽测试，不能保证所有变种都能正确识别。

每条 transcript 的 frontmatter 要写 `transcription_provider` 和 `transcription_engine`；状态 JSON 要保留 provider attempts，方便之后判断是 Groq、DashScope URL、DashScope OSS 还是标准音频兜底起效。

### B. Founder 研究的高价值内容类型
- 解释组织设计的段落
- 解释招聘标准的段落
- 解释绩效/考核/激励的段落
- 解释 AI 如何改变组织边界的段落
- 解释 headcount、人才密度、速度、流程、产品开发的段落
- 解释管理产品、内部工具体系、AI agent 如何参与管理和协作的段落
- 解释业务模式、行业结构、CEO 对行业哲学判断、关键业务数据的段落

### C. 组织动作的高价值证据
- headcount 政策
- AI-before-hiring 之类的硬要求
- 组织重组
- 考核机制改动
- 关键岗位任命与授权
- 决策流程和信息流变化
- 私有 AI 应用公司尤其要看 careers / job description：
  - open roles 暴露公司正在补的能力
  - 岗位要求暴露真实工作方式与人才标准
  - values 页面如果写到绩效、kickoff、feedback、award，通常比媒体报道更接近组织事实

### D. 业务影响的识别方式
- 管理层是否把组织变化和产品速度/客户结果直接挂钩
- 是否出现更快发布、更低成本、更高毛利、更强产品迭代
- 是否出现新业务线但没有等比例扩招
- 是否出现经营指标改善与组织动作的时间先后关系

---

## 三、当前已确认的经验

### 经验 1
只保留一个 `Agent.md` 不够，项目需要至少四个核心文件共同运转。

### 经验 2
播客链路不能只抓 episode 列表，真正有价值的是能落成全文 transcript 的那部分。

### 经验 3
目录结构不写清楚，后面会在 root 脚本和 `scripts/discovery/` 版本之间反复混淆。

### 经验 4
在目标公司未明确时，不应盲目抓取；先完成规范和链路确认，再补一个最小必要问题。

### 经验 5
对 Lovable 这类非上市、快速变化的 AI 应用公司，组织判断不能只看融资新闻和 ARR。Founder 长访谈、careers 页面、关键岗位 JD、官方 governance/security 文章，往往比二手报道更能说明组织正在如何从 founder mode 走向可规模化组织。

### 经验 6
当同一项目进入多公司研究阶段，必须尽早拆成公司级目录。`scripts/{TICKER}` 适合作为采集缓存，但不适合作为长期研究主目录；长期研究应进入 `companies/{company}/vault` 和 `companies/{company}/analysis`。

### 经验 7
长音频 ASR 是典型慢任务，不能绑死主线程。只要用户允许 sub agent，应把每家公司或每组音频拆给子 agent 并行跑；主线程继续推进网页、Substack、证据拆解和写作框架。

### 经验 8
长音频转录脚本不能只在 episode 完成后写状态。每个 episode 开始前也要写 `running` heartbeat，并在状态里保留 attempt round、stage、audio URL；否则百炼轮询 10-20 分钟时，主线程无法区分“正常等待”和“脚本卡死”。

### 经验 9
metadata 落盘不能只靠标题生成文件名。同一家公司、同一天、相似标题会发生碰撞；保存 markdown 时必须追加 `_2` / `_3` 这类后缀，保证 JSON 记录数和 vault 文件数可对齐。

### 经验 10
写 markdown frontmatter 时，标题、节目名、URL 这类外部字符串必须用 `json.dumps` 或等价方式转义。播客标题里经常自带引号；直接写 `title: "{title}"` 会生成不可解析的 YAML。

### 经验 11
判断 transcript 是否已存在，不能靠标题前缀模糊匹配。Founder 访谈标题高度相似，必须读取现有 transcript frontmatter，用 `title + date` 精确匹配；否则会把多条相近 episode 误判成同一条完成记录。

### 经验 12
DashScope / 百炼播客失败经常不是“本机拿不到音频”，而是云端读取远程文件或 OSS 临时文件失败。Midjourney 案例里，失败项本地全部可下载，OSS 上传也没有明显失败，但 SDK 路径仍大量 `FILE_DOWNLOAD_FAILED`；将音频标准化为 `16kHz / mono / 16-bit PCM WAV` 后，改用 REST API + OSS 资源解析，失败项可以被批量救回。以后不要把 `FILE_DOWNLOAD_FAILED` 当终局错误，它通常意味着需要切换传输路径和音频封装。

### 经验 13
Transcript 不是分析入口，essence 才是。原始 transcript 太长、噪音太多，直接基于 transcript 写分析会被材料拖散。正确流程是：先做 relevance review，淘汰低相关材料；再把每条高相关 transcript / article 提炼成一份 essence；essence 内部按重要片段拆成多条 insight blocks，长材料可以有十几条到几十条 block；最终分析优先读 essence，只有需要核验原文时才回到 transcript。

### 经验 14
播客搜索的召回率取决于搜索前的元思考。只搜公司名会漏掉大量 Founder/C-level 访谈、行业主题访谈、产品名访谈和客户/竞品语境。每次搜索前必须先写 query map，把公司、人物、产品、行业、组织、AI 转型关键词摊开，再执行搜索。

### 经验 15
`companies/` 根目录一旦混入临时文件和历史 sample company，很快会误导后续研究。全局 inventory / queue 放 `companies/_meta/`，旧分析稿和历史 public-company sample 放 `companies/_legacy/`，当前研究公司才留在根目录第一层。看起来是洁癖，实际是在保护检索和判断。

### 经验 16
YouTube、Substack、X 这类 source 的召回率不能靠临场关键词。正确做法是先把 podcast 阶段的关键词宇宙当作全局 query map，再派生平台限定词。这样能避免“播客搜得很完整，长文/视频/社媒又退回只搜公司名”的断层。

### 经验 17
YouTube 反爬变强后，不要把 `yt-dlp` 当唯一入口。更稳的结构是双 provider：用 RapidAPI metadata search 先找到 transcript/caption 命中的候选，再用 RapidAPI transcript 拉全文；失败再切 `youtube_transcript_api` 和 `yt-dlp` 字幕。RapidAPI search snippets 只能当候选证据，不能假装是完整 transcript；完整 transcript 成功后要写 `.segments.json`，方便后续 essence 按时间片追溯。

### 经验 18
RapidAPI metadata search 的 fuzzy 模式有召回优势，也会返回 `match_count=0` 的低置信候选。不能把 API 返回结果直接喂给 transcript provider，否则会把 free plan / 付费额度烧在无关视频上。默认规则：`match_count=0` 且 title/channel/summary/timestamp 中没有公司、Founder、产品或有效 query term 的候选，先过滤并记录 `filtered_low_confidence_rapidapi`；如果 RapidAPI 只返回低置信结果，立刻切 `yt_dlp_search`。

### 经验 19
下载前相关性不能把所有 alias 都当硬条件。Midjourney 这次抓取里，`Niji`、`Moodboards`、`Rooms` 这类词如果直接进入 required terms，会把日文 idol、泛创意访谈等视频放进 transcript 下载阶段。修正规则：manifest 里的 `channels.youtube.relevance_terms` 应作为严格下载资格；一旦配置了该字段，就只用公司名、Founder/executive 和这些严格 terms，不自动把全部 aliases 放进 required gate。aliases 仍可用于 query expansion，但不等于下载资格。

### 经验 20
Skill 不能只写原则，必须写清楚具体脚本、具体路径和状态文件。类似 `_podcast_query_map.md` 这种“后续所有 source 的关键词底座”，必须在 skill 里明确生成脚本、script staging 路径、vault 同步路径和下游读取顺序；否则后续 agent 会知道原则，却不知道文件到底在哪里。

### 经验 21
Perplexity 只能作为可选增强，不应写成默认稳定链路。当前 Perplexity API 需要先跑 `scripts/discovery/fetch_perplexity.py --smoke-test` 检查 key/quota；如果 smoke test 失败，`fetch_web_sources.py` 只能稳定处理 manifest seed URLs，不能把 query discovery 结果写成“已完成全网搜索”。Perplexity 脚本也必须只读环境变量，不在代码里硬编码 key。

### 经验 22
采集默认源要低熵。过去“全网最大化”容易把 official/jobs/social/funding/broad web 全部拉进来，材料量很大但分析信噪比下降。当前默认只保留四块：podcast、financials、Substack、YouTube；其他 source 作为 explicit opt-in。`collect_target.py --channels all` 表示四大核心块，`--channels all_sources` 才表示最大化抓取。

### 经验 23
Essence 应尽量在每个 source 抓完后立即生成，而不是等全量采集结束再集中处理。原因很简单：刚读完 raw transcript / article 时，上下文最完整，马上压成 insight blocks 可以节省后续 context window，也能避免长材料在最终分析阶段反复塞入上下文。全局 essence queue 只用于历史 backlog，不应成为新采集的默认等待室。

### 经验 24
Analysis 不是 alike 的同义词。本项目当前 `companies/{slug}/analysis/` 里的 source inventory / evidence map 可由 `collect_target.py` 生成，但 fact pack、复杂报告、一页分析、500 字提交版仍是研究写作流程。写作前必须先读 `学习/skills/analysis/SKILL.md`：先学项目规范和“学习”文件夹，再和用户 plan，再围绕 Founder 认知、组织动作、业务影响三问展开。

---

## 四、教训区

### 教训 1：规范写得太像“说明”，不够像“执行协议”
修正：
- 增加硬规则
- 增加前置检查
- 增加何时更新哪份文档

### 教训 2：只写模板，不写当前状态，团队会失去节奏
修正：
- `progress.md` 必须预填当前任务
- 不是只给空模板

### 教训 3：脚本存在不等于链路清晰
修正：
- 要把脚本职责、输出路径、推荐使用版本写进 `project-structure.md`

---

## 五、后续更新规则

出现以下情况时，必须回写本文件：
- 同类任务做了两次以上，有稳定套路
- 某次错误值得防止再次发生
- 某类证据特别有效或特别误导
- 某条方法论被实际执行验证
