---
company: lovable
source_type: youtube
type: source_note
status: draft_sample
source_path: companies/lovable/vault/youtube/transcripts/2025-03-09_Building-Lovable-10M-ARR-in-60-days-with-15-people.md
source_title: "Building Lovable: $10M ARR in 60 days with 15 people | Anton Osika (co-founder and CEO)"
source_date: 2025-03-09
created_at: 2026-04-22
speaker: "Anton Osika"
source_weight: A
relevance: high
note_version: 0.1
---

# Building Lovable: $10M ARR in 60 days with 15 people — Source Note

## Why This Source Matters

这篇是 Lovable 早期组织研究里必须承重的 A 类材料。它不是单纯的产品介绍，而是 Anton 在公司只有十几个人、ARR 已经冲得很快的时候，连续解释了 Lovable 的产品定义、增长来源、招聘方式、内部节奏、工具使用和线下协作密度。它最有价值的地方，是能把“15 人做到 $10M ARR”这个表面数字拆成更细的组织机制：团队为什么可以少人高速，哪些流程被保留，哪些流程被压掉，AI 杠杆和人的判断分别放在哪里。

这份 note 是新版 source note 样板：它不追求短摘要，而是尽量把后续报告可能用到的证据先完整搬出来。英文只保留短锚点；每条都附中文译意，后续写作主要用中文判断和译意，不依赖长英文引文。

## Source Weighting

- `A1 founder/operator source`：Anton 本人解释产品、组织和招聘。
- `A1 timing`：访谈发生在 Lovable 极早期爆发阶段，能看到组织机制还没被大公司流程稀释前的形态。
- `A2 limitation`：材料主要来自 founder 自述，缺少员工、客户、竞品和离职人员交叉验证。强判断需要和 careers/jobs、后续 Elena Verna、客户案例、竞品 founder 材料互相校准。

## High-Value Evidence Blocks

### 01 — Lovable 的产品定义不是“帮工程师写代码”，而是把软件创建权交给非工程人

Anton 对 Lovable 的定义非常直接：用户用自然语言描述想法，系统给出可运行产品。这个定义的组织含义很大，因为它把软件生产的瓶颈从“找工程师写代码”移动到“用户能不能把意图表达清楚，并判断结果是否可用”。他反复讲到妈妈、朋友、设计师、产品经理和创业者，这些人过去都被卡在“找不到好工程师”这个环节。Lovable 的起点不是服务已有工程团队，而是服务那 99% 不会写代码但有想法的人。这会改变 Lovable 自己需要建设的能力：它要同时懂软件工程、产品体验、教育、用户表达和上线后的业务闭环。

Evidence anchors:

- `"personal AI software engineer"` — 中文译意：Lovable 是“你的个人 AI 软件工程师”。
- 中文译意：用户描述一个想法，然后拿到一个可以工作的产品。
- 中文译意：Lovable 想服务的是不会写代码的绝大多数人，而不是只给工程师再加一层效率工具。

Tags: `product_definition`, `non_coder_market`, `software_creation_access`

Report use:

- 可用于解释 Lovable 为什么不是 Cursor 的直接同类。Cursor 的默认用户是工程师，Lovable 的默认用户是不会写代码但要把事情做出来的人。
- 可用于解释为什么 Lovable 的组织里必须有强产品直觉和用户教育能力，而不是只堆模型工程。

### 02 — 15 人做到 $10M ARR 的关键，不只是模型红利，还有“产品包装”把模型能力变成普通人可用的界面

访谈里 Lenny 反复强调 Lovable 的数字：前 4 周 $4M ARR、前 2 个月 $10M ARR、15 人团队、欧洲最快增长创业公司。Anton 没有把增长完全归功于自己，而是说他们站在 foundation models 这层“新石油”上。但他真正强调 Lovable 做对的，是把模型能力包装成用户能直接使用的产品界面：AI 生成 UI，用户可以直接视觉编辑；可以接 Supabase 后端、Cloudflare 部署；可以继续加登录、listing management 之类真实功能。这里的核心机制是：基础模型提供能力，但 Lovable 把能力压成普通用户能理解、能迭代、能上线的操作面。

Evidence anchors:

- 中文译意：Lovable 发布不到三个月，已有 300,000 月活用户，其中约 30,000 付费。
- 中文译意：前四周达到约 $4M ARR，两个月达到约 $10M ARR，团队只有 15 人。
- 中文译意：Anton 说他们主要做的是找到“人怎样最大化利用模型能力”的界面。

Tags: `growth`, `product_packaging`, `model_leverage`, `interface`

Report use:

- 可用于把 ARR 增长和组织机制连接起来：少人高增长不是“人少神奇”，而是产品界面把模型能力规模化了。
- 也能支撑反方：如果底层模型能力 commoditize，Lovable 的护城河要落在包装、可靠性、工作流和品牌上。

### 03 — GPT Engineer 到 Lovable 的迁移，说明 Anton 的起点是“证明 LLM 能造软件”，但商业化方向是“让不会写代码的人造软件”

Anton 在访谈里讲 GPT Engineer 的起源：他曾在 YC startup 做 CTO，不满意大家对 LLM 写代码能力的低估，于是做了一个开源工具，输入一个简单目标，生成多文件代码并运行出来。这个项目后来有大量 GitHub stars，也暴露出使用量压力。关键转折不是“开源工具火了”，而是他意识到，让工程师更高效不是最大杠杆，真正的大机会是让不写代码的人也能把想法变成产品。所以 Lovable 不是 GPT Engineer 的商业壳，而是把 open-source coding demo 转成面向非工程人的产品系统。

Evidence anchors:

- `"GPT engineer"` — 中文译意：Anton 先做的是 GPT Engineer 这个开源工具。
- 中文译意：工具展示了大语言模型可以把人类指令转成可运行应用。
- 中文译意：Anton 后来把方向改成“给不会写代码的人使用”的产品。

Tags: `origin_story`, `open_source_to_product`, `non_engineer_workflow`

Report use:

- 可用于解释 Lovable 的 founder insight：不是所有 cognitive labor 自动化都有同等价值，最大增量来自扩大谁能创建软件。
- 可用于和 Replit、Cursor 区分：Lovable 的根不是 IDE，而是“software creation interface”。

### 04 — 产品可靠性来自不断找“AI 卡住”的地方，而不是只等待模型自然变强

Anton 讲了一个很重要的技术/组织机制：AI 构建应用时常常一开始很好，后面卡在 bug、登录、数据持久化、支付这类环节。Lovable 做的事情，是系统性找出 AI 最常卡住的区域，然后用量化反馈和快速迭代去调整个系统。这个机制不是纯技术细节，它解释了 Lovable 为什么需要一支小而强的工程团队：他们不是简单调用模型 API，而是在做“失败模式地图”。每解决一类卡点，非工程用户就更接近真的把产品上线。

Evidence anchors:

- 中文译意：AI 一开始生成效果很好，但会在某些地方卡住。
- 中文译意：Lovable 会识别最重要的卡点，并针对这些区域快速改进系统。
- 中文译意：登录、数据持久化、Stripe 支付，是他们明确提到要避免卡住的例子。

Tags: `reliability`, `agent_failure_modes`, `feedback_loop`, `platform_engineering`

Report use:

- 可用于解释 Lovable 的技术护城河不只是“prompt 更好”，而是把常见失败模式产品化地消除。
- 可用于写风险：如果用户进入更复杂企业场景，失败模式会从技术 bug 扩展到权限、数据、合规和业务流程。

### 05 — Lovable 的用户技能要求，开始像产品经理训练：表达清楚预期、指出哪里工作、哪里不工作

Lenny 在 demo 里指出，一个不清楚的需求会让 AI 误解；Anton 后面也说，用户需要耐心、好奇心，最好用 chat mode 去理解软件如何工作。这个点很关键：Lovable 降低了写代码门槛，但没有取消“定义问题”的门槛。用户不需要解释为什么重要，却必须清楚表达要什么、现在哪里对、哪里不对。这意味着未来非工程用户如果要变强，学的不是传统 coding，而是产品经理式表达、验收和迭代能力。

Evidence anchors:

- 中文译意：Anton 建议用户保持好奇和耐心，用 chat mode 追问系统怎么工作。
- 中文译意：不要只说“不工作”，而要解释自己期待什么、哪些部分已经工作、哪些部分没有。
- 中文译意：和 AI 协作时，清楚表达预期比过去更重要。

Tags: `user_skill`, `product_management`, `prompting`, `human_ai_collaboration`

Report use:

- 可用于写“AI 没有消灭产品判断，反而把产品判断前置给更多人”。
- 也可作为留存/教育风险：普通用户能否跨过“描述和验收”这道门槛，会影响 Lovable 的长期使用深度。

### 06 — Lovable 早期招聘不是找单一 craft 强的人，而是找 care、generalist brain 和 AI 系统调参能力

Anton 对招聘标准讲得非常具体。他说最重要的是 care：候选人不是把这当工作，而是真的在乎产品、用户和团队如何一起工作。然后是 generalist brain：能快速学习很多技能，同时在某个维度有绝对超能力。在 Lovable 早期，这个“超能力”主要体现为把大语言模型能力榨干，理解有哪些参数、系统部件和产品包装会影响最终表现。这个标准非常贴合 Lovable 的业务：如果产品本身就是把模型能力包装成可用软件，团队成员就不能只懂一个职能，他们要同时懂 AI、产品、工程、用户和速度。

Evidence anchors:

- 中文译意：Anton 说最重要的是候选人真的在乎产品、用户和团队。
- 中文译意：他偏好能快速学习多种技能的 generalist，同时在一个维度极强。
- 中文译意：早期团队最核心的能力之一，是理解怎么把 LLM 的表现调到更好。

Tags: `hiring`, `talent_density`, `generalist`, `ai_native_team`

Report use:

- 可用于写 Lovable 的人才模型：不是传统“工程、产品、设计”职能拼图，而是每个人都要跨边界。
- 也能解释为什么后续规模化会困难：这种人才模型稀缺，很难线性扩张。

### 07 — Work simulation 是 Lovable 招聘里的强筛选器，它比面试更接近真实组织压力

Anton 说他们几乎总会让候选人进入 work simulation，至少一天，经常是一整周。这个机制比普通面试更能暴露候选人在 Lovable 环境里的真实表现：是否能和团队高密度协作，是否能在不确定问题里快速推理，是否真的 care，是否能承受高速度。后面 Lenny 读了一段早期岗位描述，里面强调长时间、高速度、高紧迫感，以及不适合追求舒适工作的人。它很像一个“自我筛选器”：对一部分人会劝退，但会吸引想加入高强度使命的人。

Evidence anchors:

- `"work simulation"` — 中文译意：候选人会进入真实工作模拟。
- `"full week"` — 中文译意：有时会持续一整周。
- `"comfortable work"` — 中文译意：这类岗位不适合追求舒适工作的人。

Tags: `hiring_filter`, `work_trial`, `intensity`, `culture`

Report use:

- 可用于解释 Lovable 早期速度背后的代价：高 agency、高强度、高筛选，不是轻松文化。
- 可用于和 careers 页面交叉验证：后续如果出现更多专业岗位，说明这种 founder-mode 强筛选开始被组织流程补充。

### 08 — Product cadence 很轻：先找最大瓶颈，再用 weekly planning、FigJam、demo 和短 roadmap 保持方向

Anton 对产品优先级的算法非常朴素：找最大的产品问题，快速解决，然后再找下一个。难点不在算法，而在判断“最大问题”本身，所以团队会和用户交流、读用户反馈、看 feature request board。具体节奏上，早期他们用 weekly planning，把主要问题放到 FigJam 上，按本周应该聚焦什么排序；每周 demo 已经 ship 的东西，让大家保持同一页面；roadmap 现在能看到未来几个月，但一个月后可能就变样。这个节奏很适合 AI 应用公司：模型和用户需求变化快，太重的 roadmap 会制造假确定性；没有 cadence 又会失控。

Evidence anchors:

- `"fig Jam board"` — 中文译意：他们用 FigJam 白板承载和排序主要问题。
- 中文译意：每周 demo 本周 ship 的内容，让团队保持同步。
- 中文译意：roadmap 大概看三个月，但一个月后可能已经变化。

Tags: `product_process`, `weekly_planning`, `cadence`, `roadmap`, `figjam`

Report use:

- 这是最该补进最终组织报告的材料之一。它说明 Lovable 的速度不是无流程，而是“少量固定节奏 + 大量弹性判断”。
- 可作为和后续 Product Manager (Agents)、GRC、FDE 等岗位变化的对照：早期轻 cadence 如何演变成专业组织线。

### 09 — Linear 被拿来做 talent application tracking，说明 Lovable 早期没有把工具按职能切死

Anton 说 Lovable 在 Linear 里做很多事，甚至用 Linear 做 talent application tracking。这个细节很小，但组织含义很大。它说明早期 Lovable 不是先采购一堆职能系统，再把工作塞进 HR / product / engineering 的边界里；相反，它用一个足够轻、足够顺手的工具承载多种 workflow。这种做法降低切换成本和协调成本，也暴露出公司还处在强 founder-mode / maker-mode：工具服务于速度，而不是服务于职能完整性。

Evidence anchors:

- `"Talent application tracking in linear"` — 中文译意：他们甚至用 Linear 跟踪人才申请。
- 中文译意：Anton 认为 Linear 是非常好的产品，所以公司很多事情都在里面做。

Tags: `tools`, `linear`, `workflow_compression`, `early_org`

Report use:

- 可用于写 Lovable 的组织状态：不是没有流程，而是用少数工具压缩流程。
- 也可作为后续扩张风险：当 hiring、GTM、enterprise 和 compliance 复杂起来，Linear 式轻工具可能不够，需要专门系统和专门 owner。

### 10 — Office 和 lunch 是 Lovable 的高带宽协调机制，不是生活方式细节

Anton 被问到还有什么让小团队跑得快时，没有先讲某个 AI workflow，而是讲 office 和 lunch。他说大家多数时间在办公室，可以直接指出“我们是不是想错了”，午饭是 cross-pollination 的高产时间。这个点很有价值，因为它修正了一个常见误解：AI-native 公司不一定是纯远程、纯异步、全靠工具协调。Lovable 的模型更像“AI 放大执行，人用高带宽线下沟通快速校准方向”。当每个人都能更快 build，错误方向也会更快被 build；所以面对面校准反而更重要。

Evidence anchors:

- `"lunch together"` — 中文译意：一起吃午饭是高产的协作时间。
- 中文译意：office 让团队可以随时指出方向可能错了。
- 中文译意：线下环境同时提供专注和非结构化高带宽沟通。

Tags: `office`, `lunch`, `high_bandwidth`, `coordination`, `human_ai_work`

Report use:

- 可用于写 Lovable 组织的反直觉点：AI 杠杆越强，人类同步和方向校准越重要。
- 可用于和 Anthropic / Cursor / Midjourney 比较不同 AI 公司对 office、节奏和协作的选择。

### 11 — Anton 对未来产品团队的判断：工程瓶颈下降后，taste、用户直觉和 generalist 能力更值钱

Lenny 提出一个判断：当构建越来越自动化，最值钱的能力变成知道该做什么、判断做出来的东西是否正确。Anton 基本同意，并进一步说，如果今天组建产品团队，会非常看重每个人尽可能多的技能：懂系统架构、懂设计、有产品 taste、会和用户沟通。这个观点和 Lovable 的招聘标准是一体的：AI 把执行层杠杆放大后，职能边界变松，产品团队需要更多“能判断全局的人”，而不是只会完成一个窄任务的人。

Evidence anchors:

- 中文译意：工程瓶颈会下降，好的 taste、用户直觉和理解用户会更重要。
- 中文译意：Anton 会希望产品团队成员尽可能多地掌握架构、设计、产品和用户沟通能力。
- 中文译意：工程师也需要上升几个抽象层次，理解技术约束如何转成产品解决方案。

Tags: `future_of_product_team`, `taste`, `generalist`, `engineer_role`

Report use:

- 可用于解释 Lovable 自身组织和产品的镜像关系：产品让用户变成 builder，公司也要求员工变成跨职能 builder。
- 可用于写 AI org 三问中的 founder insight：AI 不是让人只做原职能更快，而是让高质量判断变成稀缺环节。

### 12 — Lovable 下一阶段不只让人 build，还要帮人上线、协作、增长和继续经营

Anton 讲下一步时提到 agentic behavior、custom domains、team collaboration，以及帮助 founder 在做出第一版后获得用户、反馈和传播。他并没有把 Lovable 的边界停在“生成代码”或“生成 demo”。更长期看，他甚至想让 AI 帮用户理解产品数据、提出改进、跑 A/B test。这说明 Lovable 的战略野心是从 creation surface 往 operation surface 扩展：先把 idea 变成 product，再帮助 product 进入真实业务循环。

Evidence anchors:

- 中文译意：更 agentic 的系统可以自己写测试、运行测试、修复失败。
- 中文译意：他们要补 custom domain、collaboration 等从 demo 到上线的能力。
- 中文译意：Lovable 正在思考如何帮助 founder 获取用户、收集反馈和传播产品。

Tags: `roadmap`, `agentic_behavior`, `collaboration`, `growth_tools`, `operation_surface`

Report use:

- 可用于写 Lovable 的上限：如果只做 demo，价值有限；如果能承接发布、协作、增长和运营，才会进入更大的工作流。
- 也可用于写竞争：这条路会和 website builder、product analytics、growth tooling、internal tools、enterprise workflow 重叠。

### 13 — Anton 的失败案例说明：AI 不能作为外接引擎硬塞进旧产品，必须从端到端用户体验重想

Anton 讲到自己以前在 Sana Labs 的经历：他们曾想把个性化学习 API 接到已有教育产品里，但这个 retrofit 很难。教训是，不能先有一块酷技术，再期待别人把旧产品换引擎；要从端到端用户体验出发，判断 AI 应该放在哪里、解决什么具体问题。这个教训直接解释 Lovable 为什么要做完整产品，而不是只做 API 或 developer tool：用户要的是从想法到产品的完整路径，不是一个孤立模型能力。

Evidence anchors:

- 中文译意：把 AI API 接进别人已有产品，是很难的 retrofit。
- 中文译意：更好的路径是先看完整用户体验，再判断 AI 应该加在哪里。
- 中文译意：技术新奇不能替代真实问题。

Tags: `failure_case`, `ai_product_design`, `end_to_end_experience`

Report use:

- 可用于解释 Lovable 的产品哲学：不是“AI inside”，而是“AI 重写端到端软件创建流程”。
- 也能做反方：Lovable 进入企业既有系统时，也会重新遇到 retrofit 难题。

### 14 — “一周用 AI 做出真实东西”是 Anton 对个人 AI fluency 的最低训练法

访谈最后 Anton 讲到如何成为 AI 工具高手：找一个真实问题，花一整周用 AI 从 idea 做到别人真的能用的东西；遇到不懂就问 AI。这个建议看起来像用户教育，但对 Lovable 的增长也有含义。它给用户设定了一条从玩具到生产力的路径：不是每天试 100 个 prompt，而是完整解决一个问题。Lovable 如果能把这种训练路径产品化，就能把用户从好奇试用带到持续 build。

Evidence anchors:

- 中文译意：找一个真实问题，用 AI 端到端解决，做到有人真的使用。
- 中文译意：花一整周做这件事，就已经超过全球大多数人。
- 中文译意：不懂时直接向 AI 提问，理解工具和领域。

Tags: `ai_fluency`, `user_education`, `activation`, `retention`

Report use:

- 可用于写 activation：Lovable 的长期价值取决于用户是否完成一个真实 outcome，而不是只生成一次 demo。
- 可用于写社区和教育产品机会。

## Concrete Fact Bank

- Lovable 在访谈时发布不到三个月。
- Lenny 口径：前 4 周约 $4M ARR，前 2 个月约 $10M ARR，团队约 15 人。
- Anton 口径：当时约 300,000 monthly active users，其中约 30,000 paying users。
- 早期团队约 18 人，其中至少 12 人会部分时间写代码。
- Lovable 前身包括 GPT Engineer / GPT Engineer app；正式 Lovable 产品在 11 月 21 日左右发布。
- Anton 提到发布后达到每周约 $1M ARR，且仍以类似或更快速度增长。
- 产品栈/体验里提到 Supabase、Cloudflare、GitHub sync、Cursor、visual edit、chat mode。
- 内部工具/节奏里提到 FigJam、Linear、weekly planning、weekly demo、feature request board。
- 未来路线里提到 agentic behavior、custom domains、collaboration、帮助 founder 获得用户和反馈。

## Open Questions / Need Cross-Check

- Founder 自述中的 ARR、MAU、paid users 需要和后续 Sifted / 20VC / financial reporting 口径交叉验证，尤其 ARR 是否只是 MRR x 12。
- Work simulation 和高强度文化需要 careers 页面、候选人/员工材料、后续招聘规模交叉验证，不能只靠 founder 访谈。
- Weekly planning / FigJam / Linear 是早期 15-18 人阶段的机制；公司进入 70+ open roles 后是否仍有效，需要后续 source。
- Office/lunch 高带宽协作是否是 Stockholm 早期组织优势，还是可跨 Boston/London/SF 复制，需要 jobs/careers 和 later-stage interviews 验证。
- Lovable 从 creation surface 到 operation surface 的扩张，需要和 product roadmap、pricing、enterprise roles、security/GRC roles 互证。

## Candidate Mainlines For Later Report

1. **软件创建权外溢**：Lovable 的 founder insight 是把软件工程从工程师手里抽出一部分，交给不会写代码但有需求的人。
2. **执行自动化后，判断更稀缺**：AI 让 build 变快，但 problem selection、taste、用户理解和验收能力更值钱。
3. **小队速度来自轻 cadence + 高带宽线下沟通**：weekly planning、FigJam、demo、Linear 和 office/lunch 共同构成早期 operating system。
4. **招聘是产品镜像**：Lovable 产品要求用户从意图到结果全链路负责；Lovable 组织也要求员工跨职能、强 ownership、高强度、能在 AI 系统里找到杠杆。
5. **下一阶段是从 demo 到业务闭环**：custom domains、collaboration、growth playbooks、analytics/A-B test 这些能力决定 Lovable 是否能从 AI website/app demo 工具变成真正的软件运营平台。

## Coverage Notes

- 本 note 已覆盖原正式 essence 漏掉的核心组织材料：weekly planning、FigJam、demo cadence、Linear、work simulation、hard job description、office/lunch、高带宽协作。
- 本 note 仍未覆盖 careers/jobs 角色变化；那批材料应单独建 jobs/careers source note，不应强行塞进这篇访谈。
- 如果后续把 `essence` skill 改成 `source_note` skill，这篇可以作为 Lovable A 类 founder interview 的格式样板。
