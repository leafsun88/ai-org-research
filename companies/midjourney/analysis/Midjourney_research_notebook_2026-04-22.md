---
company: Midjourney
type: research_notebook
date: 2026-04-22
status: current
evidence_base: 47 source_note files from podcasts and YouTube
analysis_mode: source_note_first
---

# Midjourney Research Notebook

## 0. 证据口径

本 notebook 只把 `companies/midjourney/vault/podcasts/essence/` 和 `companies/midjourney/vault/youtube/essence/` 下的 47 份 `_source_note.md` 当作正式输入；旧 `_essence.md` 仅保留作历史审计，不进入报告主线。

来源权重分布：

| source_weight | 数量 | 主要用途 |
| --- | ---: | --- |
| A | 10 | Founder 原声、office hours、官方社区教育、专业工作流、法律深访 |
| B | 26 | 重度用户观察、产品 cadence、社区/法律/商业讨论 |
| B- | 4 | 补充产品比较和中等相关材料 |
| C / C+ | 6 | 新闻语境、边缘采用、二级线索 |
| D | 1 | 低相关，仅作背景 |

按“组织架构/组织机制”筛选：

| 层级 | 数量 | 口径 |
| --- | ---: | --- |
| Strict org | 15 | 直接涉及 Midjourney 内部团队大小、创始人治理、Discord 社区结构、算力经营、平台迁移、moderation/support、API/enterprise 边界、Meta licensing、IP governance |
| Extended org impact | 9 | 不直接讲 Midjourney 内部组织，但能证明它如何改变客户/创作者/小工作室的组织方式和工作流 |
| Product/market support | 23 | 产品教程、竞品比较、法律新闻、一般采用；只作为反证或业务影响补充 |

Strict org 15 份包括：David Holz 2022 访谈、2022 Discord office hours、2023 Midjourney office hours、Power Law 2023、2015 SVVR David Holz、Discord server correction、AI Podcast $500M、Meta deal、Disney/IP legal 深访、S07E05 legal、V7 Fast Hours、Secret Playground、V8 Quick Start、Ep.62、Ep.64。

## 1. 业务本质画像

Midjourney 不是单纯的 image generator，而是在卖“creative iteration capacity”：用户把模糊意图、参考图、风格词、个人审美和社区学习放进系统，系统用算力和模型把它们变成可比较、可选择、可继续编辑的视觉候选。

理想组织形态因此不是传统 SaaS 销售组织，也不是纯 research lab。它更像一个由五个部件组成的创意操作系统：

1. Founder taste / interface philosophy：创始人必须长期定义“什么样的图、交互、社区和边界是对的”。
2. Community as OS：社区同时承担教育、审美反馈、prompt 扩散、bug 暴露、moderation 压力和产品传播。
3. Compute-first cash discipline：收入先换成 GPU/server/inference 调度确定性，而不是先换销售队伍。
4. Product-control migration：Discord 先承接学习和分发，复杂编辑、档案、搜索、支持、移动端和治理最终要回到自有 web/mobile。
5. Governance as platform layer：版权、角色、色情/暴力、API 使用、企业客户和品牌安全必须从人工社区治理升级成产品化规则。

## 2. Founder 认知

### Midjourney 的公司起点是“未来十年的工作家园”，不是融资叙事

David Holz 在 2022 年把 Midjourney 定义为未来十年和一群人做 reflection、imagination、coordination 的地方。这解释了几个反常识动作：不融资、不急着 enterprise、不先做 API、不把产品降格成 Photoshop 插件。

关键证据：

- `How Computers Dream with David Holz`：David 说 Midjourney 对他更像“未来十年可以待着的地方”，主题是反思、想象、协调。
- `Power Law 2023`：John Coogan 把它解释为 post-boom 公司样本：小团队、低 overhead、现金流极强。
- `AI Podcast 2026`：第三方把其概括为“控制权优先”的 AI 公司，而不是单纯模型公司。

投资含义：Midjourney 的控制权偏好不是“缺融资能力”，而是 founder 在 Leap Motion 之后对资本、平台化和组织膨胀的再选择。

### David 的核心产品隐喻是 imagination vehicle

David 有意回避“AI art”或“AI artist”，而把产品叫作 machine-augmented imagination vehicle。这个隐喻直接影响组织选择：公司要优化的不是“替人画完”，而是人和模型之间的 taste-driven back-and-forth。

关键证据：

- `How Computers Dream`：David 把 Midjourney 比作想象力的船、车和飞机，帮助人探索审美可能性。
- `Discord Open Office Hours 2022`：Holz 说 AI 没有故事和情绪，故事来自用户；AI 更像画笔或自然流体。
- `2015 SVVR`：Leap Motion 时期 David 已经在解决人和技术之间的 interface bottleneck，关注“技术消失到用户自然感知里”。

组织含义：这家公司需要 founder-led 的审美和界面判断，而不是完全指标化的 PM 组织。因为默认值、过滤规则、参数设计、社区展示和发布节奏都会携带价值观。

### David 早期就有“技术变成非技术”的世界观

2015 年 SVVR 演讲显示，David 不是突然在 2022 年因为 diffusion model 才有创意工具想象。他长期相信抽象技术会变成日常材料，更多有身体直觉、情绪、社交和审美能力的人会参与抽象劳动。

关键证据：

- `2015 SVVR`：David 说 digital medium 会像塑料、木头、金属一样成为 physical material。
- 同场演讲中，他说 technical 会变成 non-technical，抽象问题会被 physical、intuitive、social、emotional intelligence 解决。
- 这和 Midjourney 让非专业用户、独立设计师、小工作室进入视觉生产是一条连续线。

## 3. 组织机制 A：小团队和控制权纪律

### Midjourney 的小团队不是美德叙事，而是知识劳动效率观

2022 年 office hours 里，Midjourney 约 10 人同时承担模型、web、community、organization flow、moderation 和未来功能。2023 年 Power Law 进一步引用 David 的“小组织理论”：知识劳动有效性大致随人数对数增长。

关键证据：

- `Discord Open Office Hours 2022`：团队约 10 人，同时做当前系统、下一代系统、网页功能、组织流程、网页创作流程和新功能。
- `Power Law 2023`：David 的观点是 1000 人可能只比 100 人有效两倍，10000 人公司可能比 100 个 100 人公司低效 25 倍。
- `AI Podcast 2026`：第三方估计 Midjourney 年收入约 $500M，强调 bootstrapped 和高收入/人效，但数字需标注为外部估计。

机制判断：Midjourney 的规模不是靠人扩张，而是靠 GPU、订阅现金流、Discord/社区和自有平台界面扩张。人效来自组织边界选择，不只是模型利润率。

### Leap Motion 是反面教材

Power Law 对 Leap Motion 的复盘说明，David 经历过硬科技公司拿融资、做平台、扩到约 100 人、开发者生态太早、最终未能进入大众日常的路径。Midjourney 几乎系统性反转了这条路：先不造硬件，不先做平台，不先开 API，借 Discord 找用户学习曲线。

关键证据：

- `Power Law 2023`：Leap Motion 到约 100 人仍找不到进入数百万用户日常的路径。
- 同源提到传统 VC 对 Leap Motion 的 monetization 问题错位，解释 David 后来不急着拿钱。
- `Discord Open Office Hours 2022`：David 仍想做更高级创作工具和未来可能的 hardware，但先让当前产品和社区跑起来。

机制判断：这不是“创始人讨厌融资”，而是曾经为过早平台化和组织膨胀交过学费。

## 4. 组织机制 B：Discord / community 是操作系统

### Discord 的价值是生成意图，不只是分发

Midjourney 把 Discord 当作早期入口，不是因为懒得做前端，而是因为用户一个人面对“你可以想象任何东西”时常常只会说 dog；在群体里，dog 会变成 space dog、Aztec space dog。社区让用户学习别人怎样 prompt，也让模型和团队看到真实需求。

关键证据：

- `Discord Server Correction` 引用 David 的 The Verge 说法：group setting 会让想象力在彼此想法上继续搭建。
- `Power Law 2023`：Discord 提供 mobile、desktop、图片展示、按钮、slash command、bot 和协作环境，用户能复制 prompt 并学习。
- `AI Podcast 2026`：Discord 早期价值是 beta testing、prompt education 和用户共学。

组织含义：Midjourney 的社区不是 marketing channel，而是产品学习层、教育层和审美数据层。

### 社区行为被写回模型和产品

Midjourney 不是只收集 prompt/image pair。David 多次把用户选择、rating、rank image 和 community tuning 讲成模型改进输入。用户教模型的不是“猫是什么”，而是哪些猫值得看，哪些审美/表达更符合人类偏好。

关键证据：

- `Discord Open Office Hours 2022`：Holz 说互联网教概念，用户数据更多教 beauty、expression 和 people actually want。
- 同源提到 community tuning：社区 rating 不同版本，可能逐渐 steer system tuning。
- `Midjourney Office Hours 2023`：ranking system 是拿更多数据改善算法和 ranking 的实验。
- `V7 Fast Hours`：personalization 通过用户 ranking 改善手、appendage、颜色和 composition，形成用户 taste lock-in。

机制判断：Midjourney 的数据闭环更像“审美反馈闭环”，而不是广告平台的转化闭环。它的稀缺资产是 collective taste signal。

### 社区治理直接塑造产品价值

David 早期把 porn、gore、front page、词表和女性小组反馈都当作产品机制，而不是 PR 风险。允许什么，什么就会形成 feedback loop；不治理，社区会被最强刺激反馈占据。

关键证据：

- `How Computers Dream`：David 每周四小时 office hours，拉 12 位女性讨论 bikini 图片，约 40 个 moderators 可用 slash ban。
- `Discord Open Office Hours 2022`：Holz 说色情、血腥内容会形成反馈回路，吸引对应人群并改变社区。
- `Midjourney Office Hours 2023`：front page 不让同一人的图片连续占据太多位置，避免少数人接管注意力。
- `Discord Server Correction`：服务器通过 group role / newcomer rooms 降低新人复杂度，同时对 false positive 极敏感。

组织含义：Midjourney 的 trust & safety 和 community design 不是边缘职能，而是产品护城河的一部分。

## 5. 组织机制 C：compute-first 现金流经营

Midjourney 的 bootstrapped subscription 让商业闭环很直接：用户喜欢就付钱，公司拿 margin 支付 inference 和研发。更关键的是，David 把年度订阅现金流提前换成未来一年的 GPU/server 供给，避免生成式 AI 应用最稀缺的资源被市场短缺牵制。

关键证据：

- `How Computers Dream`：David 说这是诚实生意，云端算力要花钱，用户付 subscription，公司拿一点 margin。
- `Discord Open Office Hours 2022`：Midjourney 可能运行在 1 亿美元级 GPU 上，团队买不起但租得起；upscaler 需要 37GB VRAM。
- `Power Law 2023`：稀缺资源不是钱，而是 GPU allocation 和全球 inference 调度。
- `Midjourney Office Hours 2023`：David 把年度订阅现金用于买下未来一年供给，优先投资服务器、web/mobile、compute 优化，未来视频和 3D 建在其上。

机制判断：Midjourney 的组织优先级是先保“生成体验的确定性”，再谈销售/生态扩张。和多数 AI 应用“融资换 GPU”不同，它更像“订阅现金流换 GPU”。

## 6. 组织机制 D：先借平台，再回收产品控制权

Discord 是早期最正确的入口，但复杂编辑、搜索、档案、支付、移动端、support、moderation、API/企业治理都需要更强 owned surface。Midjourney 迁向 web/mobile 不是否定 Discord，而是当产品复杂度上升后回收控制权。

关键证据：

- `Discord Open Office Hours 2022`：David 已把当时 Discord 体验视为未来一两年更大创作体验的 tutorial。
- `Midjourney Office Hours 2023`：inpainting 被 Discord 新 UI 和 mobile 支持拖慢；团队投资 standalone web/mobile。
- `AI Podcast 2026`：先借平台再建平台，触发点是品牌行为成熟和 economics / 产品限制开始不对。
- `Discord Server Correction`：Midjourney 与 Discord 互相依赖，Discord 也把它当作超大 server 基础设施测试样本。

机制判断：Midjourney 的长期组织不可能一直是“Discord bot company”。它必须拥有创作工作台、用户资产、支持系统和治理规则，否则会被平台限制住产品复杂度。

## 7. 产品组织：release cadence 是社区机制

Midjourney 的模型发布不是一次性 benchmark 事件，而是社区学习、prompt 知识重建和产品预期管理。V7/V8 的材料共同说明：用户愿意学习新模型，但当替代工具增多，等待和 alpha 发布的代价变高。

关键证据：

- `V7 Fast Hours`：每次大模型更新会重置一整套社区知识，用户回到 drawing board 重新测试参数。
- `Secret Playground`：drip release 让社区重新点燃，发布节奏本身变成产品机制。
- `Ep.62`：V8 延迟让用户开始关心公司能不能按节奏 ship。
- `Ep.64`：V8 Alpha 最大负面信号是老用户没有像过去那样第一时间冲进去。
- `Quick Start V8`：官方社区教育承认 Alpha chaotic，课程把重点放在重新获得画布控制权。

机制判断：Midjourney 过去可以靠“神秘大版本”拉动社区兴奋；进入成熟期后，需要更稳定的小步发布、清晰迁移路径和更强官方教育。

## 8. 产品差异化：aesthetic engine + 控制层

Midjourney 的核心差异仍然是 creativity/coherence 平衡，而不只是听话。V7/V8 讨论显示，它强在风格、构图、微观 surprise、文字触发审美联想；短板在产品化控制、编辑稳定性、reference 迁移、商业可交付和 LLM-native workflow。

关键证据：

- `V7 Fast Hours`：Midjourney 的核心差异是 creativity/coherence 平衡，不是单纯更听话。
- `Ep.62`：Midjourney 仍最适合“文字触发审美联想”；但 V8 需缩小“可玩图”和“业务可交付图”的质量差距。
- `Ep.64`：V8 底层仍有强审美能力，问题是稳定性和可控性没跟上。
- `Secret Playground`：SREF 仍是相对其他图像工具最强的差异化层；weird/chaos 是探索 latent space 的旋钮。
- `Quick Start V8`：V8 Alpha 不一定知道更多，但在已有知识上更有效率、更 adherence、更 coherent。

组织含义：Midjourney 要保持的不是“最好图片模型”单点，而是从 aesthetic engine 发展为可交付 creative workspace。

## 9. 外部组织影响：小团队和创作者的经济性被重写

Midjourney 对客户/创作者组织的影响很明显：高 taste 的独立创意人、小工作室、startup brand team 可以用它承担过去需要摄影、agency、大预算或多职能团队完成的视觉探索。

关键证据：

- `Midjourney AI Masterclass`：真实设计工作室用 Midjourney 给客户做 branding、advertising、event booth、product 概念内容。
- 同源把流程压成 create、refine、finish、repeat、animate、evolve，repeat 是商业价值关键。
- `5 steps to generate consistent brand images`：交付物从照片本身转成客户可复用的品牌生成包。
- `Jamey Gannon`：AI 让独立设计师或极小团队能接更高价值项目，不必扩成人海 agency。
- `Phi Hoang`：Perplexity 品牌团队用 Midjourney 跟上每周产品发布节奏，Twitter 成为视觉实验场。

业务含义：Midjourney 的付费价值不在第一张漂亮图，而在 repeatability、reference system、prompt sheet、style code、personalization 和 finishing stack。

## 10. 商业路径：订阅、平台授权、专业工作流

现有来源指向三条商业路径：

1. Consumer / prosumer subscription：10/30/60 美元等订阅层级，用户为 inference 和创意迭代付费。
2. Platform licensing：Meta deal 证明 Midjourney look / aesthetic tech 可以被大平台采购。
3. Professional creative workflow：品牌、agency、小工作室、设计师把 Midjourney 放入 Figma、Photoshop、Magnific、Runway、Luma、Nano Banana、Flora、Weavy 等多模型流水线。

关键证据：

- `Power Law 2023`：三档订阅价、Discord 1800 万用户、收入传闻从 5000 万到 3 亿美元不等。
- `AI Podcast 2026`：年收入约 $500M 为第三方估计，需谨慎使用。
- `Meta deal`：Meta 想把 Midjourney 的 aesthetic tech 放入 Instagram、Facebook、WhatsApp 和广告/创意效果体系。
- `Masterclass / Jamey / Phi`：专业用户不是只买图片，而是买速度、可重复性和创意总监杠杆。

## 11. 风险和反证

### V8 / release cadence 风险

老用户仍爱 Midjourney，但 V8 Alpha 反应显示，市场替代路径已经变多。过去用户愿意花几周学会新模型，现在 LLM+image、agentic edit、node workspace 工具正在抢走学习时间。

证据：`Ep.64`、`Ep.62`、`Quick Start V8`。

### Workflow 被外部工具包住

Midjourney 可能成为高质量生成核心，但用户正在用 Claude/Codex、Cosmos、Pinterest、Weavy、Flora、Google Drive、prompt database、system prompt 自建工作流。若 Midjourney 不拥有 workspace，它可能被嵌入别人的 workflow。

证据：`Ep.64` 后半段 Claude Code、`Ep.62` skill gap、`Secret Playground` Flora/Weavy/Patchwork。

### IP / licensing risk

Disney / Universal 案把风险从训练数据推到角色输出。Midjourney 的价值和风险重合：用户愿意为可识别风格、角色、IP 和文化符号付费，但这些输出也最容易被权利方攻击。

证据：`Why Disney vs. MidJourney Could Rewrite Hollywood's IP Playbook`、`S07E05`、`AI Podcast 2026`。

### Enterprise / API 被治理能力卡住

David 2023 年明确说 API 被延后不是需求不足，而是 moderation 组织容量不足。平台化、企业化、IP licensing 都要求更强 policy、审计、过滤、申诉、rights management 和客户合规。

证据：`Midjourney Office Hours 2023`、`Technically Creative legal`。

### 平台依赖和分发关系

Discord 带来早期学习和增长，但也会卡 UI、mobile 和 release；Meta licensing 带来分发和背书，也可能削弱终端创作者关系。Midjourney 必须平衡平台杠杆与自有界面。

证据：`Midjourney Office Hours 2023`、`Discord Server Correction`、`Meta deal`。

## 12. 信息缺口

1. 内部团队结构：除了“约 10 人/小团队/百人级估计”外，缺少正式 org chart、key leader、工程/社区/moderation/support 的分工。
2. 招聘与人才密度：缺少岗位、面试、绩效、薪酬、离职和关键人才背景的系统材料。
3. 财务：收入 $300M/$500M 均为第三方估计，缺少审计口径、毛利、GPU 成本、现金流和 headcount。
4. 企业与授权：Meta deal 细节、IP licensing 谈判、rights management 产品化程度仍不清楚。
5. 自有 web/mobile 迁移数据：Discord 与 web 用户留存、生成量、付费转化、社区行为如何迁移缺少量化证据。

## 13. 报告主线候选

最强主线：

Midjourney 是一家把“社区审美反馈 + founder taste + 订阅现金流换算力 + 小团队控制权”组合成 creative iteration engine 的 AI 公司。它的组织优势不是传统意义的职能架构，而是把用户社区直接接到模型、产品和治理里；它的下一阶段问题，是能否把这套社区型操作系统升级为可治理、可授权、可生产的创意平台。

报告里应该压低“图片模型谁更强”的比重，重点写：

1. David 的界面/想象力世界观如何决定公司边界。
2. Discord 社区如何从渠道变成操作系统。
3. Bootstrapped + compute-first 如何形成控制权和基础设施纪律。
4. Release cadence / community education 如何成为组织能力，也如何在 V8 后变成风险。
5. IP governance / professional workflow 如何决定它能否从创作者工具升级为平台。
