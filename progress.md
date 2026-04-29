# Progress

> 当前活跃任务面板。每次 serious plan 前先读这里；旧长记录已归档，不再堆在主文件里。

## 当前任务

- 名称：项目 GitHub 交接与独立仓库初始化
- 日期：2026-04-29
- 状态：进行中。已按 `Agent.md` 规则重读四个核心文件，并新增 `README.md` 与 `HANDOFF.md`，说明项目定位、公开信息采集、私有/半公开信息采集、source 分层、关键脚本、环境变量和 GitHub 提交边界。
- 决策：仓库应提交脚本、配置、项目文档、文本证据、analysis 报告和 PDF；不提交 `.env`、`.vercel`、`.DS_Store`、原始音频、标准化音频和 ASR 转码缓存。原因是项目已有 transcript / metadata / source note / analysis 作为可复查文本证据，音频缓存体积约 19G，不适合作为 GitHub 仓库内容。
- 已知风险：本机 `gh` 未登录，无法直接通过 GitHub API 创建新 repo；SSH 到 GitHub 账号 `leafsun88` 已验证可用。若不能自动创建远端仓库，需要用户先创建一个空 GitHub repo 或完成 `gh auth login`。
- 下一步：初始化本地 git 仓库，提交当前项目快照；随后尝试创建/连接远端并 push。

- 名称：Midjourney V8 HTML / 报告清理与社群增强版
- 日期：2026-04-24
- 状态：已完成。已从当前 Midjourney v8 母版生成两个保留版本：v9 结构清理版与 v10 社群增强版。v9 删除 Founder 洞见标题括号中文、替换公开资料公司架构为 8 卡功能图、核心人物表改成公开职业介绍；v10 在 v9 基础上融合 `/Users/leafsun/Downloads/ai-community-building-report.md` 第一部分，补充 Midjourney 创立历史、Discord 社群建立机制、新手区、公开生成、Office Hours、Daily Theme、零营销出圈和 Web 迁移。2026-04-24 追加按用户指定重排社群章：删除三个独立补充块标题，把 Discord 选择、dog/space dog 原型故事、三次出圈增长飞轮分别合并进对应 block，并把默认公开、命令/新手区、Daily Theme/Office Hours 三块移动到“为什么用 Discord？”之后。
- 输出文件：`companies/midjourney/analysis/Midjourney_组织哲学报告_v9_structure_clean_2026-04-24.{md,html}`；`companies/midjourney/analysis/Midjourney_组织哲学报告_v10_community_enriched_2026-04-24.{md,html}`。当前 v8 HTML 也已小修用户指出的裸 `####对新用户友好` 渲染问题。
- 验证：v10 浏览器桌面 1440x1000 与移动 390x844 均通过；9 个 report section、42 个 evidence article、39 条 blockquote、4 张 table、8 个 org cards；无 console error、无横向溢出、无裸 `####`、无旧 code tree、无 `组织含义`、两个目标 h4 小标题均为绿色。
- 已知风险：核心人物履历来自 LinkedIn / Crunchbase / TheOfficialBoard / 会议 bio / 公开组织目录等公开资料，少数岗位以第三方目录或搜索摘要为依据，仍应视作公开资料层而非内部 org chart。
- 下一步：若用户认可 v10，可继续对社群章节做更强叙事顺稿或部署成可分享链接。
- 当前继续：用户要求把 v10 全文 wording 顺一遍，重心转向“社区构建”，小标题更明晰；本轮新建 v11，不覆盖 v10。原则：先不删 block，候选删减项在最终汇总中说明，等用户许可后再删；完成后生成 HTML 并部署到 Vercel，部署名需包含 `midjourney`。
- v11 已完成并部署：`companies/midjourney/analysis/Midjourney_社区构建与组织哲学报告_v11_community_centered_2026-04-24.{md,html}`；静态部署目录 `companies/midjourney/analysis/vercel-midjourney-community-report-v11/`；生产 alias `https://vercel-midjourney-community-report.vercel.app`。验证：本地与远程桌面/移动均为 9 个 h2、39 个 article、39 条 blockquote、4 张 table、8 个 org cards、section 5 为 10 个社群 block；无横向溢出、无裸 `####`、无旧独立补充块标题。
- 用户要求删除“迁移：从 Discord 社群到 Creative Workspace”整章并重新上传；已新建 v12 保留旧版：`companies/midjourney/analysis/Midjourney_社区构建与组织哲学报告_v12_no_migration_2026-04-24.{md,html}`，并重新部署到同一 Vercel alias。验证：远程桌面/移动均为 8 个 h2、36 个 article、36 条 blockquote、4 张 table、8 个 org cards、8 个 nav links；线上无迁移章节残留、无裸 `####`、无横向溢出。

- 名称：Perplexity 全源 collect
- 日期：2026-04-23
- 状态：进行中。已按 collect 规范重读四个核心文件，确认 Perplexity target 存在且为私有公司，默认跳过 financials；本轮用户要求“所有信息”，优先尝试 `all_sources` 口径，并按脚本能力回退到 podcasts / Substack / YouTube / optional web 等可执行渠道。
- 已知风险：`progress.md` 记录本机当前未配置 `PERPLEXITY_API_KEY` / `PPLX_API_KEY`，Perplexity API discovery 可能需要走无 API fallback；YouTube / podcast transcript 受外部 API、ASR provider 和配额影响，失败必须写入 status/failure。
- 下一步：检查 target query map 和脚本参数，dry-run 后执行 Perplexity collect，并同步 `_staging` 产物到 `companies/perplexity/vault/`。

## 当前执行

- 名称：Midjourney podcast / YouTube source note 全量返工
- 日期：2026-04-22
- 状态：已完成。用户指出 Midjourney 已写 YouTube note 的 quote 过短，要求先返工并把问题修进 `essence` skill，再把 Midjourney 全部 podcast / YouTube notes 写完，可使用 subagent。已完成 skill 修订、三篇旧短 quote note 返工、podcast / YouTube source-note 批量写作、status 更新和主线程总验收。
- Skill 修订：`学习/skills/essence/SKILL.md` 已新增 `Long Quote Gate`，要求 high-relevance block 的译引保留连续上下文，短到像 slogan / 关键词证据的 quote 默认不合格；同一文件已新增 `Subagent batch mode`，明确主线程负责 skill/status/progress，subagent 只写互不重叠的 source note 输出。
- Midjourney podcast：新增新版 `_source_note.md` 16 份，其中 15 份 full source note、1 份 rejected low-relevance record；另有 1 条 S07E05 podcast 转录去重到 YouTube note、1 条 2026-03-19 泛新闻跳过。状态文件：`companies/midjourney/vault/podcasts/essence/_midjourney_podcast_source_note_status_2026-04-22.md`。
- Midjourney YouTube：38 份 transcript 已全量归类，新增 / 返工正式 `_source_note.md` 31 份；5 条 low relevance 不写 full note，2 条短重复源去重到更好 source note。状态文件：`companies/midjourney/vault/youtube/essence/_midjourney_youtube_essence_status_2026-04-22.md`。
- 验证：主线程全量检查 `source_note_files=47`，其中 `podcast_source_notes=16`、`youtube_source_notes=31`；block / quote 数全部对齐，禁用工具字段检查为空，短 quote 检查为空，frontmatter 必填字段检查为空。
- 注意：旧 `_essence.md` 文件未删除，保留作审计；后续正式 Midjourney 分析默认读新版 `_source_note.md`。

## 当前排查

- 名称：Lovable 报告质量 root-cause audit
- 日期：2026-04-22
- 状态：已完成第一轮定位。产出 `companies/lovable/analysis/Lovable_essence_coverage_root_cause_audit_2026-04-22.md`。结论：Lenny / Anton 2025-03-09 访谈属于 transcript 已入库但正式 essence 抽漏；careers/jobs 岗位变化属于 source 未入库、无 essence。报告质量问题主要来自 essence 层不完整，而不是“只读 essence”规则本身错误。

## 当前实验

- 名称：Lovable source note 样板
- 日期：2026-04-22
- 状态：样板 v3 已固化为 reference：`学习/style_references/essence_source_note_example_lovable_lenny_2026-04-22.md`。`学习/skills/essence/SKILL.md` 已重写为新版“source_note / evidence_note / 逐源厚笔记”规范：保留 essence 层但不再做短摘要；一次只读一篇 source；每个 block 用标题、中文判断段、一条较长连续中文译引；source notes 后续再汇总为公司级 research notebook / theme map；不加入 `Evidence anchors`、`Tags`、`Report use`、`Fact Bank` 等工具性字段。

## 当前写作

- 名称：Lovable 第二篇新版 source note
- 日期：2026-04-22
- 状态：已完成并验证。文件：`companies/lovable/vault/podcasts/essence/2025-08-18_20VC-Lovable-CEO-Anton-Osika-on-120M-in-ARR-in-7-Months--The_source_note.md`。本次选择 20VC / Anton 2025-08-18 CEO 原声，按新版 essence skill 写成 23 个 insight blocks，每个 block 使用标题、中文判断段、一条较长连续中文译引；验证为 157 行、23 个 `##` blocks、23 条中文译引，旧工具字段检查为空。

## 当前批量重写

- 名称：Lovable 旧 essence 批量升级为新版 source note
- 日期：2026-04-22
- 状态：Lovable high-relevance podcast source note 全量收尾批次已完成并验证。当前已完成 podcast `_source_note.md` 共 23 份，另有 YouTube 2025-03-09 canonical `_source_note.md` 1 份；本轮新增 13 份：Podcast 2025-09-11 Anton/Wharton、2025-09-19、2025-10-15、2025-11-03、2025-11-24、2025-11-26、2025-12-11、2025-12-18、2025-12-28、2026-01-25、2026-02-18、2026-03-10、2026-03-14。状态清单：`companies/lovable/vault/podcasts/essence/_source_note_rewrite_status_2026-04-22.md`。验证：23 份 podcast source note 全部 `##` block 数等于中文译引数，禁用工具字段检查为空，frontmatter 基本字段齐全。
- 归档：旧短 `_essence.md` 已从 Lovable 正式 vault 移出，归档到 `companies/lovable/_legacy/short_essence_2026-04-22/`，共 87 份。后续正式分析默认只读新版 `_source_note.md`；legacy 仅用于审计或必要回溯。

## 当前分析草稿

- 名称：Lovable theme map / thesis spine
- 日期：2026-04-22
- 状态：已基于 24 份正式 `_source_note.md` 生成 analysis 草稿：`companies/lovable/analysis/Lovable_theme_map_2026-04-22.md` 和 `companies/lovable/analysis/Lovable_thesis_spine_2026-04-22.md`。这两份只作为主线导航和论证压力测试，最终报告仍需直接读取 source note。

## 当前 skill 调整

- 名称：analysis2 简化分析 skill
- 日期：2026-04-22
- 状态：已更新 `学习/skills/analysis2/SKILL.md`，定位为 `analysis` 的简化版和“逐源笔记证据块拼装”写法。最新原则是“材料是根本，主线只是摆放材料的方法”：先通读正式逐源笔记，临时建立积木清单，标记每个高价值证据块是直接纳入、合并纳入、顺带点到，还是有理由放弃；报告初稿后必须做反向查漏，尤其检查 Linear、FigJam、work simulation、weekly planning、demo、office、lunch、岗位变化、security、churn、gross margin 等容易被抽象吞掉的细节。skill 已加入三条强写作规则：一是正文判断段直接讲公司怎么做，不用“某某说/某某认为”推进；二是正式报告不能出现“上一版/本轮/这篇报告/材料丢失”等写作过程痕迹；三是中文优先但不硬翻专有名词，ARR、PMF、GTM、workflow、roadmap、demo、ship、AI-native、founder-mode、Minimum Lovable Product 等保留英文更自然。全局入口 `~/.codex/skills/ai-org-analysis2/SKILL.md` 已同步指向项目内正式 skill。`学习/skills/essence/SKILL.md` 也已补规则：中文译引必须像真正引用，保留第一人称和现场语气，不能把 quote 写成第三人称访谈旁白，quote 也不能只重复上一段判断。

## 当前 analysis2 报告

- 名称：Lovable analysis2 直写最终报告
- 日期：2026-04-22
- 状态：已按最新版 `analysis2` 重新写报告，目标从“抽取主题”改成“把逐源笔记里的高价值材料放回正确位置”。文件：`companies/lovable/analysis/Lovable_AI组织最终报告_analysis2_2026-04-22.md`。新版已恢复早期组织细节：work simulation、一周工作试用、硬核招聘描述、FigJam weekly planning、weekly demo、三个月 roadmap、Linear 跟踪人才申请、office 和 lunch 的高带宽协作。结构为核心判断、入口变化、产品边界后移、早期组织操作系统、组织扩张、企业化和安全、growth、反方与待核验；已去掉“AI 组织三问”固定小节，每节开头都有总起。当前报告已开始清掉“某某说/上一版/本轮”这类过程和访谈转述腔，并对 Linear quote 回源修正为一手译引；后续若继续打磨，需要按新规则检查所有 quote 是否真是一手原话、正文和 quote 是否互相重复、专有名词英文/中文是否平衡。

## 当前增补准备

- 名称：Lovable YouTube source notes 与 analysis-add skill
- 日期：2026-04-23
- 状态：已按新版 `essence` skill 对 Lovable YouTube transcript 做完 source-note 层处理，并已用 `analysis-add` 把 YouTube 新证据增补进 Lovable analysis2 报告。当前 YouTube transcript 共 65 份，正式 `_source_note.md` 共 36 份，low relevance / duplicate / pure tutorial 跳过 29 份；状态文件：`companies/lovable/vault/youtube/essence/_youtube_source_note_status_2026-04-23.md`。主线程验证：36 份 source note 合计 267 个 `##` blocks、267 条中文 quote，全部 block/quote 对齐，旧工具字段扫描为空。2025-03-09 Lenny / Anton 旧 tool-field canonical note 已替换为当前 source-note 格式，旧样板归档到 `companies/lovable/_legacy/youtube_source_note_samples_2026-04-23/`。
- 新 skill：已新增 `学习/skills/analysis-add/SKILL.md`，并同步全局入口 `/Users/leafsun/.codex/skills/ai-org-analysis-add/SKILL.md`。这个 skill 专门用于在保留既有报告框架的前提下，把新增 source notes 放进原报告对应位置；原则是先固定现有报告骨架，再逐块判断新 evidence block 是直接插入、合并加厚、替换证据、边界/待核验还是不纳入。本次 Lovable YouTube 增补已按该 skill 执行。
- 报告增补：`companies/lovable/analysis/Lovable_AI组织最终报告_analysis2_2026-04-22.md` 已从 24 份 source note 扩展为 59 份 source note 证据口径，仍保留原七节结构；新增内容集中在 Studio 71 报价 demo、教育平台后台、Daymaker HR workflow、Lovable agency、Nad 设计/招聘、办公室扩张、growth engineer / GTM engineer、Avery 生产化、安全 100+ daily changes、AI agent 权限、creator economy、Google AI Studio / Figma / v0 / Claude Code 竞争边界等。原文件备份在 `companies/lovable/analysis/Lovable_AI组织最终报告_analysis2_2026-04-22_pre_youtube_add_backup.md`。完成检查：过程痕迹关键词为空，旧工具字段为空，正式 source note 总数复核为 59，其中 YouTube 36。

## Goal

让后续 agent 进入项目后能快速回答三件事：

- `scripts/discovery/` 只放通用脚本本体。
- `companies/{slug}/_staging/` 放运行产物、status、failure、缓存。
- `companies/{slug}/vault/{source}/{metadata,transcripts,essence}` 放正式证据。
- `学习/skills/` 只保留 active skills：collect / essence / analysis。

## Active Plan

- [x] 建立 podcast source dedupe index：`companies/{slug}/vault/podcasts/metadata/_source_dedupe_index.{json,md}`
- [x] 保存 Lovable essence quote-pack 样例：`学习/style_references/essence_quote_pack_example_lovable_2026-04-21.md`
- [x] 更新 `collect` / `essence` / `analysis` skill：去重只读轻量 index；分析默认只读 essence；第三方深度材料可进入 essence。
- [x] 生成 relevance plan：`companies/_meta/transcripts/lovable_midjourney_podcast_essence_plan_2026-04-21.{json,md}`
- [x] 将 Lovable 2025-08-18 20VC 测试 essence 转成正式 essence。
- [x] 将 Midjourney David Holz 旧格式 essence 重写成当前格式。
- [x] Lovable 高相关 podcast essence 批量生成。
- [ ] Midjourney 高相关 podcast essence 批量生成。
- [ ] 根据 essence-only 输入分别写 Lovable / Midjourney 复杂长文分析。
- [x] Lovable essence-only 复杂长文分析已完成：`companies/lovable/analysis/Lovable_essence_only_investment_org_report_2026-04-21.md`。
- [x] Lovable block-style 组织报告已完成：`companies/lovable/analysis/Lovable_org_block_report_2026-04-21.md`。新稿按 style reference 的 block + quote 写法，组织篇幅约 75%。
- [x] `analysis` / `essence` skill 已补充“读者无背景、说人话、看不懂就回原始 source_path 核验”的规则；block 编号改为按章节 A/B/C 重置。Lovable block 报告已同步改成 A01-F04。
- [x] Lovable block-style 组织报告已重写成人话版：删掉旧稿里的过度压缩表达，中文判断段改成逐步解释机制与业务传导；自检已清除“不是/而是”等模板句和 AI 黑话。
- [x] Lovable 报告洞见不足诊断已完成：`companies/lovable/analysis/Lovable_report_diagnostic_2026-04-21.md`。结论是材料并不贫瘠，主要问题是 report 按职能分类整理，漏掉了 waitlist / prompt box / Lovable Launch / token cascade / load-bearing infrastructure / benchmark risk 等更有因果力的主题；下一版应先做 insight audit，再按 A 类核心机制重搭骨架。
- [x] `analysis` skill 已吸收 Lovable 诊断教训：新增 insight audit / omission audit / thesis spine / A 类核心机制规则，要求先自下而上保留 sharp points，再上升到组织投资框架，避免报告变成职能目录。
- [x] 已按 Lovable diagnostic 的更高层元思考更新 `analysis` skill，并重写 `Lovable_org_block_report_2026-04-21.md`：新稿从 sharp points 上升到软件生产权外溢 / builder density loop / 组织镜像产品 / 可控地快四个机制。
- [x] 二次返工：用户反馈上一版仍未按 `analysis` skill 的正式文章形态写作。已把 `Lovable_org_block_report_2026-04-21.md` 从 workflow/证据清单式文本重写为 style reference 要求的 `storyline + blocks + speaker quote pack`；正文不再塞文件清单，source gate / insight audit 留在 `Lovable_analysis_workflow_2026-04-22.md`。验证：22 个判断 block、66 条 quote、87 份 essence 证据池，未检出 `Evidence Pack` / `_essence.md` 文件清单残留。
- [x] 三次返工：用户反馈“没有读完所有 essence、没有对照 Anthropic 案例、引用太短、文章没血”。已重新读 87 份 essence，新增 `companies/lovable/analysis/Lovable_full_essence_audit_2026-04-22.md`，把 Podcast/YouTube 证据分层、sharp-point audit 和 thesis upgrade 落盘；`Lovable_org_block_report_2026-04-21.md` 已按“软件生产权外溢以后，平台把供给/分发/运营/安全/治理重新收口”重写，并加厚 speaker quote pack。
- [x] `analysis` skill 已补入新教训：复杂报告前必须通读该公司全部 essence，先做 source weighting 和 sharp-point audit；正式报告正文不得展示研究过程、不得用第一人称写研究动作；若存在 recovered 文风样例，写作前必须学习并做 tone pass。Lovable 当前报告已同步清理过程性段落和 `我这次重新过...` 这类工作日志口吻。
- [x] `analysis` skill 已补入英文和术语规则：报告正文不要滥用英文，只在必要专有名词、产品名、岗位名、指标名上保留；专有名词首次出现必须解释；组织报告必须把 AI 组织三问放在最前面，组织内容占比至少 70%。Lovable 当前报告已把三问移到最前，并重写为少英文、术语先解释的版本。
- [x] Lovable 报告已按用户要求扩写：放弃旧的 A-E 机制并列结构，改成三问主结构；判断 block 从 21 个扩到 36 个，长度约增加一倍，新增 GPT Engineer、工程师角色边界、North Star、资深/年轻人才配比、Stockholm、创始人组合、销售负责人文化复制、社区、每日发布、业务基础设施、安全、评估体系等 block。
- [x] Lovable 报告已按用户最新要求完全重写：不沿用上一版正文，以 AI 组织三问作为整篇主结构，重新组织为“创始人认知 / 组织落地动作 / 业务影响”三大部分；保持 block + quote pack 写法，组织内容为主体。
- [x] Midjourney 补搜 podcast / YouTube / Substack：YouTube 高相关候选已去重无新增；Substack query 已写入 manifest；新增 David Holz 原声 podcast 已转录。
- [x] Midjourney podcast / YouTube source notes 已按 repaired essence 口径完成：47 份 `_source_note.md`（podcast 16、YouTube 31）通过 block/quote/frontmatter 校验；旧短 `_essence.md` 不再作为正式输入。
- [x] Midjourney 研究 notebook / theme map / 组织最终报告已完成：`companies/midjourney/analysis/Midjourney_research_notebook_2026-04-22.md`、`companies/midjourney/analysis/Midjourney_theme_map_2026-04-22.md`、`companies/midjourney/analysis/Midjourney_AI组织最终报告_analysis_2026-04-22.md`。报告按 `analysis` skill，以组织为重心，核心机制为 founder taste、community as operating system、compute-first cash discipline、product-control migration、governance as platform layer。
- [x] Midjourney 已按用户要求另写 `analysis2` 版最终报告：`companies/midjourney/analysis/Midjourney_AI组织最终报告_analysis2_2026-04-22.md`。新版采用 evidence-block 拼装写法，保留逐源笔记里的具体判断和较长中文译引；不再默认放“AI 组织三问”固定章节，组织重心放在 David interface worldview、小团队/算力优先、Discord 操作系统、creative workspace 迁移、专业采用和治理平台化。
- [x] Midjourney 旧短 essence 已归档：13 份 podcast、26 份 YouTube 移至 `companies/midjourney/_legacy/short_essence_2026-04-22/`；正式 `vault/*/essence/` 目录保留 47 份 `_source_note.md` 和状态文件。

## Current Facts

- active skill 当前应为 `学习/skills/collect/SKILL.md`、`学习/skills/essence/SKILL.md`、`学习/skills/analysis/SKILL.md`。
- inactive skills 已归档到 `学习/_legacy/skills/`。
- 旧 root 脚本已归档到 `companies/_legacy/root_scripts_legacy/`。
- `Alike-Investment/` 已归档到 `companies/_legacy/external_repos/alike-investment/`。
- `scripts/discovery/collect_target.py --channels all` 只跑四大核心块：podcasts / financials / substack / youtube。
- `_staging/` 是运行区；正式分析只读 `vault/` 和 `analysis/`。
- HTML 流程图：`companies/_meta/workflows/collect_analysis_flow_2026-04-21.html`。
- Lovable 结构说明：`companies/lovable/analysis/Lovable_project_structure_2026-04-21.md`。
- Perplexity API helper 已保留，但本机当前未配置 `PERPLEXITY_API_KEY` / `PPLX_API_KEY`。
- 当前 Lovable / Midjourney podcast plan：Lovable 高相关 23 条（已完成 1），Midjourney 高相关 17 条（已完成 1）。低相关、重复、optional reference 均已记录在 `companies/_meta/transcripts/lovable_midjourney_podcast_essence_plan_2026-04-21.md`。
- Lovable 当前可用于分析的 podcast essence 已有 24 个文件，其中包含 founder 原声、growth/operator、竞品/行业视角和一份旧测试稿；新 Lovable 报告已按 essence-only 口径完成。
- Midjourney 当前正式 podcast / YouTube 分析输入：47 份 `_source_note.md`（podcast 16、YouTube 31）。旧短 `_essence.md` 已移入 `_legacy/short_essence_2026-04-22/`，不要再作为正式分析输入。Substack 已接入 manual fallback，metadata/status 可追踪，transcript 4 md、essence 0。

## Latest External Update

Lovable podcast 重抓已由 sub agent 收口：

- metadata：50 个 episode entry，52 个 metadata markdown 文件。
- transcript：49 成功，1 真实失败。
- skipped_short / deferred：0。
- 失败原因：`limitededitionjonathan.com` 原始 host 无法解析，Groq / DashScope URL / 标准音频 REST 都失败。
- 输出已同步到 `companies/lovable/vault/podcasts/`。

Midjourney collect 补搜更新：

- YouTube：RapidAPI/yt-dlp 查询 6 组关键词，每组最多 8 个候选；通过 relevance 的 6 个均为 existing transcript，新增 transcript 0，RapidAPI transcript 调用 0。
- Podcast：增补 `How Computers Dream`、`What Future`、`Stratechery`、`bootstrapped/no VC`、`Discord community`、`aesthetic technology` 等 query 后，Apple Podcasts metadata 从 76 条扩到 104 条 curated。
- Founder voice：新增并转录 `How Computers Dream with David Holz`，58 分钟，80,111 chars，已同步到 `companies/midjourney/vault/podcasts/transcripts/2022-11-10_How-Computers-Dream-with-David-Holz.md`。
- Substack：新增手动/公开搜索 fallback 脚本 `scripts/discovery/manual_substack_search.py`。当前环境缺 `PERPLEXITY_API_KEY` / `PPLX_API_KEY`，DuckDuckGo/Bing 搜索质量不稳定；手动 URL list 路径 `companies/midjourney/vault/substack/metadata/manual_urls_2026-04-21.txt` 已跑通，5 个候选中 4 篇通过 Jina Reader fallback 抓到正文并同步到 `companies/midjourney/vault/substack/transcripts/`，1 篇标记为 subscriber/paywall。

## Lovable Report Framework Update — 2026-04-23

- 用户提供的 Lovable 组织哲学报告已去链接后存入 `学习/style_references/lovable_org_philosophy_framework_reference_2026-04-23.md`，作为 analysis2 以后做组织哲学 / 组织结构 / 框架重组时必须读取的结构参考。
- `学习/skills/analysis2/SKILL.md` 已加入该 reference 的读取规则和 dossier 式报告框架：摘要、目录、组织哲学概览、使命/愿景、价值观、领导层、组织结构图、招聘、办公政策、AI 内部运营、关键引述、演进、治理和未知项。
- 已新建 Lovable 重组报告 `companies/lovable/analysis/Lovable_组织哲学报告_analysis2_reorg_2026-04-23.md`，没有覆盖旧报告；旧报告和新报告均保持 63 个 `###` block。新报告已清理 citation links 和写作过程痕迹。
- 进一步新建 Lovable 融合版报告 `companies/lovable/analysis/Lovable_组织哲学报告_analysis2_fused_2026-04-23.md`，把用户提供的组织哲学参考报告内容作为组织档案事实层嵌回正文：使命/信条、正式价值观、高管表、工程骨干、员工规模、IPS、办公室、AI 运营、时间线、融资/投资人、已知/未披露和来源索引。旧报告和重组版未覆盖；融合版仍保持 63 个 `###` block，且无 URL / markdown citation link。
- 版本线已整理为 `Lovable_组织哲学报告_V1_long_2026-04-22.md`、`Lovable_组织哲学报告_V2_reorg_2026-04-23.md`、`Lovable_组织哲学报告_V3_fused_2026-04-23.md`、`Lovable_组织哲学报告_V4_curated_2026-04-23.md`。V4 是有取舍版：删除偏客户案例和市场评论的“其他”章节、移除中段 quote 索引，保留组织结构、招聘、办公、AI 运营、治理、安全、留存、PMF、毛利和平台分发威胁。V4 当前 50 个 `###` block，无 URL / markdown citation link，无写作过程词。
- 已按 `frontend-skill` 生成并迭代 V4 静态 HTML 阅读版：`companies/lovable/analysis/Lovable_组织哲学报告_V4_curated_2026-04-23.html`。保持 V4 原文顺序和结构，不做信息重组；左侧目录已去掉重复编号，首屏改成无连线的组织机制堆栈，组织结构图已从代码树改成中文为主的功能架构图，并修正移动端首屏标题和说明文字换行。基础检查：14 个 report section、50 个 article、9 张 table、50 条 blockquote，目录锚点无缺失，无 URL / markdown citation link。
- 发现 `companies/lovable/analysis/Lovable_组织哲学报告_V4_curated_2026-04-23.md` 在本地变成 0 字节；为避免覆盖可能仍在编辑器里的版本，已先从 HTML 反向恢复出 `companies/lovable/analysis/Lovable_组织哲学报告_V4_curated_2026-04-23_recovered_from_html.md`，当前 590 行、14 个 `##`、50 个 `###`。
- 用户在 recovered 版本上重新改稿后，已将其提升回正式 V4：`companies/lovable/analysis/Lovable_组织哲学报告_V4_curated_2026-04-23.md`。提升前已备份 recovered 和旧 HTML；V4 主章节编号已整理为 1-8，并按新章节重写目录。HTML 已按原视觉框架重新生成，只替换文字内容和目录锚点；当前检查：10 个 report section、33 个 article、9 张 table、43 条 blockquote，目录锚点无缺失，组织结构图仍为可视化卡片，无 URL / markdown citation link。
- Lovable V4 报告已部署到 Vercel。为避免把整个研究目录暴露出去，已创建最小部署目录 `companies/lovable/analysis/vercel-v4-report/`，只包含 `index.html`。首次部署发现本地 `V4_curated_2026-04-23.html` 被 Cocoa 导出壳覆盖，导致线上样式异常；随后已用 `V4_curated_2026-04-23_html_backup_20260423_160532.html` 作为正确模板重新生成 HTML，并完成二次生产部署。当前生产地址：`https://vercel-v4-report.vercel.app`；远端桌面 / 移动端截图已验证样式正常。
- 用户于 2026-04-24 再次修改 `V4_curated_2026-04-23.md` 后，已按同一 HTML 壳重新生成本地阅读页，并同步覆盖 `vercel-v4-report/index.html` 后重新部署到同一 Vercel 项目。线上源码已确认包含本轮新增标题文字（如“增长团队直接做 Shopify 集成和语音模式，说明职能边界彻底模糊”“新职业：全职 vibe builder。把创意build为产品。”），生产 alias 仍为 `https://vercel-v4-report.vercel.app`。

## Midjourney Report Framework Update — 2026-04-23

- 用户要求 `reference/` 不保留新重组稿，只保留原始 `Midjourney_组织研究报告.md`。已删除 `companies/midjourney/reference/Midjourney_组织哲学报告_analysis2_reorg_2026-04-23.md`，并把 `/Users/leafsun/Downloads/Midjourney_组织研究报告.md` 原样复制到 `companies/midjourney/reference/Midjourney_组织研究报告.md`。
- `analysis/` 保留旧重组稿 `Midjourney_组织哲学报告_analysis2_reorg_2026-04-23.md`，并新增版本线：`Midjourney_组织哲学报告_v1_reference_2026-04-23.md`、`Midjourney_组织哲学报告_v2_reorg_2026-04-23.md`、`Midjourney_组织哲学报告_v3_fused_2026-04-23.md`。
- V3 融合版以用户提供的组织研究报告框架为外层，保留其使命、组织结构图、核心人物、招聘、远程政策、AI 运营、金句、时间线与来源索引；同时把 Midjourney source-note 长报告的 50 个 evidence block 嵌入相应章节。V3 当前保持 50 个 `###` block、50 条中文译引，无 URL / markdown citation link。
- 用户反馈 V3 对组织研究报告保留仍不够完整；已新增 `Midjourney_组织哲学报告_v4_full_fused_2026-04-23.md`。V4 改为以 V1 去链接组织研究报告全文为底稿，保留原报告正文所有非空行和一到十章结构，再把 50 个 evidence block 插入相应章节作为“补充组织证据”。V4 当前 50 个 `###` block、50 条中文译引，无 URL / markdown citation link。
- 用户进一步要求把 `/Users/leafsun/Downloads/Midjourney_组织研究报告 (1).md` 的所有内容原样融进报告，不准丢东西；已新增 `Midjourney_组织哲学报告_v5_userdoc_full_fused_2026-04-23.md`。V5 以用户新文档原文为底稿，保留其中所有非空行、链接、表格、引文和参考来源；50 个 source-note evidence block 作为四级标题插入对应章节，避免打乱原文 `###` 编号层级。
- 用户要求回到 V4 精简重组：新增材料要服从原组织长文档的信息形式，Founder 引用单独成章，薪酬和模糊弱信息去掉，跑题 block 可删。已新增 `Midjourney_组织哲学报告_v6_curated_from_v4_2026-04-23.md`，从 V4 出发重写为 12 章：执行摘要、组织哲学、Founder 的洞见、组织结构、招聘与工作方式、Community-as-Organization、算力与 AI 运营、Creative Workspace 迁移、治理风险、时间线、待核验、参考来源；不再保留 50-block 全量结构，改为精选证据融入正文。
- 用户进一步澄清仍要保留 block 形式，并要求参考 `Lovable_组织哲学报告_V4_curated_2026-04-23.md`。已新增 `Midjourney_组织哲学报告_v7_curated_blocks_from_v4_2026-04-23.md`：从 V4 重新精选 41 个组织相关 block，去掉 A01/F01 编号但保留 `### 判断标题 + 判断段 + quote` 形式；删除薪酬、弱估算、外部客户案例和偏竞争 workflow 的 block，章节改为摘要、目录、组织哲学、Founder 的洞见、组织结构、招聘实践、Community、算力运营、Creative Workspace、治理风险、时间线和待核验。
- 用户要求再次按 Lovable V4 方式重做，保留 block 形式但让信息形态更贴近组织档案。已新增 `Midjourney_组织哲学报告_v8_curated_blocks_2026-04-23.md`：从 V4 重新组织为 12 节，前置 Founder 洞见索引，正文精选 40 个 `### 判断标题 + 判断段 + quote` block；删除薪酬、外部客户案例、竞争工具流水账和证据弱的二手运营信号，保留 Meta licensing 作为审美层平台化边界；当前校验为 543 行、40 个 `###` block、40 条 quote。
- 已按用户选择的方案 A 生成 Midjourney V8 HTML 阅读版：`companies/midjourney/analysis/Midjourney_组织哲学报告_v8_curated_blocks_2026-04-23.html`。页面 1:1 复用 Lovable V4 的深色 hero、sticky 目录、纸张底色、组织图、table、blockquote 和滚动进度框架；内容从当前 `Midjourney_组织哲学报告_v8_curated_blocks_2026-04-23.md` 生成。浏览器校验：9 个 report section、33 个 evidence article、30 条 blockquote、2 张 table，桌面与移动端无横向溢出，控制台错误为空。
- Midjourney 社群构建线已推进到 V14：V12 `companies/midjourney/analysis/Midjourney_社区构建与组织哲学报告_v12_no_migration_2026-04-24.md` / `.html` 保留为“删除独立迁移章节”的上一版；V13 `Midjourney_社区构建与组织哲学报告_v13_community_loop_2026-04-24.md` / `.html` 保留为“社群机制五步循环”版；V14 新增 `companies/midjourney/analysis/Midjourney_社区构建与组织哲学报告_v14_toc_map_2026-04-24.md` / `.html`，正文内容延续 V12/V13，首屏右侧改为参考正文目录的 `Report Map`，六项对应正文主章：组织哲学、创立历史、Founder 洞见、小团队、社群操作系统、社群治理。Vercel 生产 alias 已同步更新为 `https://vercel-midjourney-community-report.vercel.app`，线上验证 HTTP 200、8 个 h2、36 个 evidence article、36 条 blockquote、4 张 table、桌面与移动端无 hero 溢出。
- Midjourney V15 已保存并部署：`companies/midjourney/analysis/Midjourney_社区构建与组织哲学报告_v15_imagine_together_2026-04-24.md` / `.html`。V15 在 V14 基础上把首屏“共同想象”改为 `imagine together`；删除报告里“默认值 / Default Values / 默认设置 / founder-led defaults”相关表达，改写为“产品选择 / 审美选择 / 社群规则 / 展示规则”；并把“10 人团队同时背模型、社群和治理”改成“10 人团队同时承担模型、社群和治理”。线上 alias 仍为 `https://vercel-midjourney-community-report.vercel.app`，验证 HTTP 200、无默认值残留、无“同时背模型”、目录锚点无缺失、桌面首屏无溢出。
- Midjourney V16 已保存并部署：`companies/midjourney/analysis/Midjourney_社区构建与组织哲学报告_v16_wording_polish_2026-04-24.md` / `.html`。V16 删除摘要里“五个支柱”句；把“Midjourney 的公开语言很稳定”改成“Midjourney 对自己的定位一直很清楚”；把“Discord 的价值是让学习发生在同一个房间”改成“Discord：让 A 用户的 Prompt 变成 B 用户的教材”；把“默认公开把每次生成变成公共教材”改成“用户产出都是默认公开的”。线上 alias 仍为 `https://vercel-midjourney-community-report.vercel.app`，验证 HTTP 200、无旧句残留、新标题存在、目录锚点无缺失、桌面首屏无溢出。
- Lovable HTML 报告已更新首屏右侧摘要条目：改为 `产品哲学 / 公司信条 / 组织结构 / 招聘机制 / 协作方式 / 内部工作流`，替换掉用户不喜欢的 `办公室 / AI 运营`。本地文件：`companies/lovable/analysis/Lovable_组织哲学报告_V4_curated_2026-04-23.html`。
- Vercel 部署已分成两条线：旧项目 `leafsuns-projects/vercel-v4-report` 继续保留，生产地址 `https://vercel-v4-report.vercel.app` 已同步最新版内容；由于项目存在 `ssoProtection.deploymentType = all_except_custom_domains`，手动追加的 `.vercel.app` alias 会落到 Vercel Authentication。为获得公开且带 `lovable` 的地址，已新建独立项目 `leafsuns-projects/lovable-org-philosophy`，并成功部署到 `https://lovable-org-philosophy.vercel.app`。

## Open Items

- Lovable 49 条 transcript 还需要 relevance review 和 `podcasts/essence/`。
- Midjourney podcast / YouTube source-note 层已完成；Midjourney Substack essence 仍可作为 optional 补充继续做，不影响当前组织报告。
- Perplexity API 当前本机未配置 `PERPLEXITY_API_KEY` / `PPLX_API_KEY`，只能作为可选增强；不影响默认四源 collect。

## Archive

- 旧完整 progress：`companies/_meta/archive/progress_archive_2026-04-21_before_cleanup.md`
- 旧完整 lessons：`companies/_meta/archive/core-principles-and-lessons_archive_2026-04-21_before_cleanup.md`
- 当前流程图：`companies/_meta/workflows/collect_analysis_flow_2026-04-21.html`
