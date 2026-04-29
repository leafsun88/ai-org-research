---
company: lovable
source_type: youtube
type: source_note
status: draft_sample_v2
source_path: companies/lovable/vault/youtube/transcripts/2025-03-09_Building-Lovable-10M-ARR-in-60-days-with-15-people.md
source_title: "Building Lovable: $10M ARR in 60 days with 15 people | Anton Osika (co-founder and CEO)"
source_date: 2025-03-09
created_at: 2026-04-22
speaker: "Anton Osika"
source_weight: A
relevance: high
note_version: 0.2
quote_language: zh_translation_from_en_transcript
---

# Building Lovable: $10M ARR in 60 days with 15 people — Source Note V2

> 以下 quote pack 均为英文 transcript 的中文翻译，保留原话含义和说话口吻，方便后续中文报告直接使用；如需精确核验，回到 `source_path`。

## Lovable 的核心不是帮工程师快一点，而是让不会写代码的人也能把想法变成产品

Anton 对 Lovable 的定义很干净：用户说出一个想法，Lovable 给出一个可运行产品。这里真正变化的不是“写代码更快”，而是谁有资格创建软件。过去朋友、家人、设计师、产品经理、创业者都可能卡在“我怎么找到一个靠谱工程师”这一步；Lovable 想把这道门槛改成表达意图、检查结果、继续迭代。这个 founder insight 很重要，因为它解释了 Lovable 为什么不是 Cursor 的同类：Cursor 默认服务工程师，Lovable 默认服务那些以前进不了软件生产流程的人。

“Lovable 就像你的个人 AI 软件工程师。你描述一个想法，然后得到一个完整可运行的产品。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我几乎所有朋友都找我帮过忙：Anton，我想做点东西，我该怎么找到一个好的软件工程师？” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我们是在为那 99% 不会写代码的人做这个东西。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“从长远看，构建软件自然会变成和 AI 对话。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## 15 人做到 $10M ARR，靠的是把模型能力包装成普通人能用的产品界面

这条访谈里的增长数字很猛：发布不到三个月、30 万月活、3 万付费、前两个月 $10M ARR、团队只有 15 人。但 Anton 没有把它讲成纯模型红利，而是讲成一套 product packaging：基础模型是新石油，Lovable 做的是把这股能力包装成用户能理解、能试错、能上线的界面。视觉编辑、Supabase 后端、Cloudflare 部署、GitHub sync、Cursor handoff 这些细节，都是把“AI 会生成代码”翻译成“普通人能真的完成一个产品”的关键。

“我们发布 Lovable 还不到三个月，现在有 30 万月活，其中 3 万人已经付费。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“他们前四周做到 400 万 ARR，前两个月过了 1000 万 ARR，而且只有 15 个人。” —— Lenny Rachitsky, Lenny's Podcast, 2025-03-09

“我们当然站在 foundation models 这层新石油上。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我们真正做的是想清楚：怎样把这些能力呈现给人，让用户从里面拿到尽可能多的价值。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## GPT Engineer 到 Lovable 的转向，是从工程师效率工具转向全民软件创建入口

Lovable 的源头不是传统 no-code，而是 Anton 为了证明 LLM 能写软件做出的 GPT Engineer。这个开源工具能把一句“做一个贪吃蛇游戏”变成一堆代码文件并跑起来，后来积累大量 GitHub stars。真正的转向发生在 Anton 发现：让工程师更高效当然有价值，但更大的杠杆，是让不会写代码的人也能把想法变成真实软件。所以 Lovable 不是 GPT Engineer 的付费版，而是把“LLM 能造应用”的 demo，重做成非工程人能使用的 creation surface。

“ChatGPT 出来以后，模型已经很擅长把人的指令变成代码，但我身边的人还觉得我夸大了。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“所以我做了一个开源工具 GPT Engineer：你写一句‘做一个贪吃蛇游戏’，它就吐出很多代码文件，然后把游戏打开。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“GPT Engineer 后来成了最流行的开源项目之一，用来展示大语言模型创建应用的能力。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我们应该做一个类似 GPT Engineer 的东西，但它必须服务那些不会写代码的人。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Lovable 的可靠性来自一张“AI 卡点地图”，不是等模型自己变强

Anton 提到一个很容易被粗摘要漏掉的机制：AI 生成应用时常常一开始很惊艳，后面会在 bug、登录、数据持久化、支付这些真实产品环节卡住。Lovable 的工作不是只等下一代模型，而是痛苦地识别这些卡点，量化它们，再快速调系统。这个动作解释了 Lovable 为什么需要小而强的工程团队：他们在产品内部做的是 failure mode reduction，把普通用户最不可能自己解决的技术断点提前消掉。

“AI 做东西时，开头通常很好，然后会在某些地方卡住。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我们做的是很痛苦地找出它卡在哪里，再用不同方法处理这些卡点。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我们会量化调整整个系统，并用很快的 feedback loop 去改进最重要的卡点。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“比如登录、数据持久化、Stripe 支付，这些是我们明确确保它不要卡住的地方。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Lovable 降低了写代码门槛，但没有取消产品判断门槛

Lenny 在 demo 中反复强调一个很朴素的产品管理问题：你没说清楚，AI 就会做错。Anton 后面也说，用户要有耐心和好奇心，要用 chat mode 追问系统为什么这样工作。Lovable 不要求用户写代码，但要求用户会描述预期、判断结果、指出哪些部分工作、哪些部分没工作。这个点很适合放进组织分析：AI 把生产权外溢给更多人，但真正变稀缺的是 problem framing、taste 和验收能力。

“不要只说‘它不工作’，你要解释你期待什么，哪些地方已经工作，哪些地方没有。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“掌握 Lovable 这样的工具，需要好奇心和耐心。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“chat mode 可以让你直接问：这怎么工作？我是不是漏掉了什么？我应该怎么做？” —— Anton Osika, Lenny's Podcast, 2025-03-09

“你不再需要写代码，但理解软件和产品是怎么工作的，仍然很有用。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Lovable 招的人不是单点 craft 强，而是 care 很重、能快速跨界的人

Anton 讲招聘时反复回到 care 和 generalist。Lovable 早期不是在拼传统职能表，而是在找那些真的在乎产品、用户和团队的人；他们要能快速学习很多技能，同时在某一维有绝对强项。这个标准和 Lovable 产品是一体两面：产品把软件创建交给更多非工程人，公司内部也需要员工跨过职能边界，把 AI、工程、设计、用户和业务一起想。AI 放大执行以后，窄 craft 反而不够，能把问题整体想通的人变得更贵。

“最重要的是，人要真的 care，而不是像乘客一样只是来上班。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“每个人都应该非常在乎产品、用户，也非常在乎团队如何一起工作。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我们想要那种 generalist brain，能很快学会各种技能，但在某一个维度又有绝对超能力。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“对我们来说，这个强项往往是尽可能榨出大语言模型的能力，理解哪些参数会让产品表现更好。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Work simulation 和硬核 JD 是 Lovable 的自筛选器

Lovable 的招聘不是普通面试流程。Anton 说他们几乎总会让候选人参加 work simulation，至少一天，经常一整周；Lenny 还读出早期 JD 里的句子：长时间、高速度、高紧迫感，不适合追求舒适工作的人。这套设计很硬，但也很诚实。它先把节奏、强度和不确定性摆出来，让不适合的人自己退出；留下来的人，才更可能适应一个 15 人团队每周推进 $1M ARR、不断改产品卡点的环境。

“我们几乎总会让人加入 work simulation，至少一天，通常是一整周。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“工作试炼很好，本质上就是让他们和团队一起工作一天，有时是一周。” —— Lenny Rachitsky, Lenny's Podcast, 2025-03-09

“岗位描述里写着：长时间、高速度，候选人必须能在 AGI 时间线逼近的高紧迫感下工作。” —— Lenny Rachitsky, Lenny's Podcast, 2025-03-09

“追求舒适工作的人，不适合申请。” —— Lenny Rachitsky, Lenny's Podcast, 2025-03-09

## Lovable 用很轻的 cadence 保住速度，三个月 roadmap 只做方向锚

Anton 对产品节奏的描述非常像早期 AI 应用公司的 operating system：先找最大的产品瓶颈，解决它，再找下一个。团队用 FigJam 把主要问题放在一起排序；用 weekly planning 决定本周聚焦什么；用 demo 让大家看到本周 ship 了什么；roadmap 能看到三个月，但一个月后变样也正常。这里的重点不是流程漂亮，而是流程足够轻，能承认 AI 应用公司的变量变化太快。它既避免完全混乱，也避免用重 roadmap 制造假确定性。

“我们主要会做 weekly planning，有一个 FigJam board，上面放着所有主要问题，然后给它们排序，看这周先聚焦哪一个。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我们会做 demo，说这些就是这周 ship 出来的东西，让所有人在同一页上。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“现在确实有更多 roadmap，比如接下来支持自定义域名、再之后加协作。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“roadmap 大概能看清接下来一个月，也会延伸到三个月，但一个月后它可能就会变得不一样。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Linear 被拿来跟踪人才申请，说明早期 Lovable 还没有把工具按职能切死

Anton 顺口说公司很多事都在 Linear 里做，甚至 talent application tracking 也在 Linear 里。这个小细节比看起来重要：早期 Lovable 没有先搭一整套 HR、产品、工程、项目管理系统，再把职能边界一层层切开；它更像把一切能压进轻工具里的东西都先压进去，用少数工具降低 context loss。这个状态很适合早期高密度团队，但也暗示未来扩张会遇到边界：当 enterprise、GRC、security、sales 和 hiring 全部变复杂，轻工具可能需要被更专业的 owner 和系统替代。

“我们在公司里很多事情都用 Linear 做，因为它真的是一个很棒的产品。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我们甚至用 Linear 做人才申请跟踪。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我们看过不少为招聘定制的工具之后，还是用了 Linear 和 FigJam，很简单。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Office 和 lunch 是 Lovable 的高带宽协调机制，不是生活方式细节

当 Lenny 问还有什么让小团队跑这么快，Anton 没有先讲 AI workflow，而是讲 office 和 lunch。大家多数时间在办公室，可以直接说“我们是不是想错了”；一起吃午饭是 cross-pollination 的高产时间；office 同时提供专注和非结构化高带宽沟通。这是 Lovable 很值得写进报告的反直觉点：AI-native 不等于纯远程、纯异步、全靠工具。AI 放大执行速度之后，错误方向也会更快被执行，线下高带宽校准反而更重要。

“我们大多数时间都在办公室工作，这很好，因为你可以直接说：我觉得我们在这件事上想错了。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“午饭一起吃其实是很高产的一个小时，大家会互相 cross-pollinate。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“人会在潜意识里一直想着怎么解决不同问题，以及哪些问题最重要。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“办公室既有专注，也有高带宽的非结构化沟通。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## 工程瓶颈下降后，产品团队更需要 taste、用户直觉和跨职能能力

Lenny 把未来产品团队的变化讲得很直：当构建本身越来越自动化，最值钱的是知道该做什么，以及判断做出来的东西是否正确。Anton 基本同意，并说如果今天组产品团队，他会强烈希望每个人都有尽可能多的技能：懂系统架构、懂设计、有产品 taste、会和用户沟通。这个判断和 Lovable 的招聘是一体的：AI 让执行变便宜之后，组织更需要能跨职能判断问题的人，而不是只完成一个窄任务的人。

“我同意，找到真正的 pain point，并判断怎样把现有解决方案做得十倍好，非常重要。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“如果是已有产品，taste 会变得更重要：什么是好的，什么是真的解决问题。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“如果我今天组一个产品团队，我会非常执着于让每个人尽可能多地拥有不同技能。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“他们最好懂系统架构、懂设计、有产品 taste，也知道怎么和用户交流。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Lovable 的下一步，是从生成 demo 走向发布、协作、增长和运营

Anton 讲路线图时没有把 Lovable 停在“生成应用”。他提到 agentic behavior、custom domain、团队协作，也提到帮助 founder 在第一版产品之后获得用户、拿反馈、传播出去。更远一点，他还想让 AI 读取用户行为、提出产品优化、自动跑 A/B test。这个方向说明 Lovable 的野心不是 app builder，而是把早期公司从 idea 到 product，再到 growth 和运营的整条链路吃进去。真正的上限也在这里：demo 很容易被复制，持续业务闭环才更难。

“更 agentic 的意思是，你给系统更多自由，让它决定下一步，比如它可能会写测试、跑测试，看到失败后再修。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“还有一些很明显的东西：怎么挂到自己的域名，怎么和团队无缝协作。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“我们也在思考，怎么帮助 founder 在做出第一版之后成功：怎么拿到更多用户，怎么获得反馈，怎么让别人知道它。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“AI 可以大规模理解用户行为，然后向人提出产品改动，也可以自动跑 A/B test。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Anton 的失败案例说明，AI 产品不能只是把新技术硬塞进旧流程

Anton 讲 Sana Labs 旧经历时给了一个很有用的产品教训：他们曾经想把个性化学习 API 接到已有教育软件里，但让别人“换引擎”很难。这不是技术不够好，而是产品没有从端到端体验重新设计。这个教训解释了 Lovable 为什么要做完整产品，而不是只给开发者一个 API：用户不是想买一块 AI 能力，而是想从想法直接走到可用产品。反过来，这也是 Lovable 未来进入企业既有系统时会遇到的风险：一旦变成 retrofit，难度会重新上升。

“我们当时做的是一个个性化学习 API，让已有教育产品把自己的引擎换成我们的 AI。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“这是很难的 retrofit，很难让别人把原来的产品引擎换掉。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“最大的教训是，你必须从端到端看这个产品怎么工作，再决定 AI 应该加在哪里。” —— Anton Osika, Lenny's Podcast, 2025-03-09

“你真的要理解用户体验的大图，然后用 AI 去解决具体问题。” —— Anton Osika, Lenny's Podcast, 2025-03-09
