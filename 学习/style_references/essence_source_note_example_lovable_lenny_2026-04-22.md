---
type: essence_source_note_style_reference
company: lovable
source_type: youtube
status: active_reference
source_path: companies/lovable/vault/youtube/transcripts/2025-03-09_Building-Lovable-10M-ARR-in-60-days-with-15-people.md
source_title: "Building Lovable: $10M ARR in 60 days with 15 people | Anton Osika (co-founder and CEO)"
source_date: 2025-03-09
created_at: 2026-04-22
speaker: "Anton Osika"
source_weight: A
relevance: high
note_version: 1.0
quote_language: zh_translation_from_en_transcript
quote_style: single_long_translated_excerpt_per_block
---

# Lovable / Lenny 2025-03-09 — Source Note Reference

> 以下每个 insight block 后面只放一条较长的中文译引，不拆成碎句。译引来自英文 transcript，保留说话人的原意和口吻；如需逐字核验，回到 `source_path`。

## Lovable 的核心不是帮工程师快一点，而是让不会写代码的人也能把想法变成产品

Anton 对 Lovable 的定义很干净：用户说出一个想法，Lovable 给出一个可运行产品。这里真正变化的不是“写代码更快”，而是谁有资格创建软件。过去朋友、家人、设计师、产品经理、创业者都可能卡在“我怎么找到一个靠谱工程师”这一步；Lovable 想把这道门槛改成表达意图、检查结果、继续迭代。这个 founder insight 很重要，因为它解释了 Lovable 为什么不是 Cursor 的同类：Cursor 默认服务工程师，Lovable 默认服务那些以前进不了软件生产流程的人。

“Lovable 就像你的个人 AI 软件工程师：你描述一个想法，然后得到一个完整可运行的产品。它意味着创业者今天可以把想法变成真实业务，很多设计师和产品经理可以先做出产品想法的第一版给团队看，其中一些人甚至会因为这种能力变成 founder；当然开发者也会更快地写代码和创建产品。但我们做 Lovable 的原因很简单：我妈妈不会写代码，我几乎所有朋友都问过我，Anton，我想做点东西，怎么才能找到一个好的软件工程师？所以我们是在为 99% 不写代码的人做这个东西；长期看，构建软件自然会变成和 AI 对话。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## 15 人做到 $10M ARR，靠的是把模型能力包装成普通人能用的产品界面

这条访谈里的增长数字很猛：发布不到三个月、30 万月活、3 万付费、前两个月 $10M ARR、团队只有 15 人。但 Anton 没有把它讲成纯模型红利，而是讲成一套 product packaging：基础模型是新石油，Lovable 做的是把这股能力包装成用户能理解、能试错、能上线的界面。视觉编辑、Supabase 后端、Cloudflare 部署、GitHub sync、Cursor handoff 这些细节，都是把“AI 会生成代码”翻译成“普通人能真的完成一个产品”的关键。

“我们发布 Lovable 还不到三个月，现在有 30 万月活，其中 3 万人已经在付费，而且增长几乎完全来自 organic word of mouth。说到为什么 15 个人能做到这么快，我当然愿意把功劳都揽到自己身上，说我们端到端做了所有产品工作，但真实情况是，我们站在 foundation models 这层新发现的石油之上；我们真正做的是痴迷地思考，怎样把这股能力呈现给用户，什么界面能让人从里面拿到最多价值，怎样把认证、后端、部署这些东西包装到一起，让它作为一个整体无缝工作。人们喜欢这个产品，这才是增长的驱动力。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## GPT Engineer 到 Lovable 的转向，是从工程师效率工具转向全民软件创建入口

Lovable 的源头不是传统 no-code，而是 Anton 为了证明 LLM 能写软件做出的 GPT Engineer。这个开源工具能把一句“做一个贪吃蛇游戏”变成一堆代码文件并跑起来，后来积累大量 GitHub stars。真正的转向发生在 Anton 发现：让工程师更高效当然有价值，但更大的杠杆，是让不会写代码的人也能把想法变成真实软件。所以 Lovable 不是 GPT Engineer 的付费版，而是把“LLM 能造应用”的 demo，重做成非工程人能使用的 creation surface。

“ChatGPT 出来以后，模型已经很擅长把人的指令变成代码，但我当时在一个 YC startup 做 CTO，团队里的人还觉得我在夸大，说这几年不会改变什么。所以我想证明这一点，做了一个开源工具 GPT Engineer：你写一句‘做一个贪吃蛇游戏’，它就生成很多不同文件的代码，然后把游戏打开。我发了一段视频，后来 GPT Engineer 成了展示大语言模型创建应用能力的最流行开源工具之一。但我继续想，我们正在看到人类历史上最大的变化，以前机器接管的是体力劳动，现在机器开始把认知劳动做得比人更好；这时候最有正向影响的事，不是让工程师更高效，而是让那些一直卡在找不到好软件工程师的人，也能把自己的想法和梦想变成现实。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Lovable 的可靠性来自一张“AI 卡点地图”，不是等模型自己变强

Anton 提到一个很容易被粗摘要漏掉的机制：AI 生成应用时常常一开始很惊艳，后面会在 bug、登录、数据持久化、支付这些真实产品环节卡住。Lovable 的工作不是只等下一代模型，而是痛苦地识别这些卡点，量化它们，再快速调系统。这个动作解释了 Lovable 为什么需要小而强的工程团队：他们在产品内部做的是 failure mode reduction，把普通用户最不可能自己解决的技术断点提前消掉。

“做 AI 系统会有很多 scaling law，其中一个是：你往系统里投入更多工作，产品就能可靠地越来越好。一般你会看到，AI 构建东西的时候开头非常好，然后会在某些地方卡住；我们做的是很痛苦地识别它到底卡在哪里，再用不同方式处理这些卡点，量化地调整整个系统，并用非常快的 feedback loop 去改进那些最重要、最常卡住的区域。它现在有时仍然会卡住，但这就是那条 scaling law，而且我们还处在这条 scaling law 的很早期。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Lovable 降低了写代码门槛，但没有取消产品判断门槛

Lenny 在 demo 中反复强调一个很朴素的产品管理问题：你没说清楚，AI 就会做错。Anton 后面也说，用户要有耐心和好奇心，要用 chat mode 追问系统为什么这样工作。Lovable 不要求用户写代码，但要求用户会描述预期、判断结果、指出哪些部分工作、哪些部分没工作。这个点很适合放进组织分析：AI 把生产权外溢给更多人，但真正变稀缺的是 problem framing、taste 和验收能力。

“要掌握 Lovable 这样的工具，需要很多好奇心和耐心。我们有一个 chat mode，你可以直接问它：这到底是怎么工作的？我为什么没有得到想要的结果？我是不是漏掉了什么？我应该怎么做？这既是提高生产力的最好方式之一，也是学习软件工程如何工作的最好方式之一。你不再需要自己写代码，但理解软件或产品是怎么构建的仍然很有用。第二点是，如果我坐在你旁边，我大概会说：你这里说得不够清楚；不要只说‘它不工作’，而是要准确说明你期待什么、哪些部分已经工作、哪些部分没有工作，这件事很多人天然不会做。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Lovable 招的人不是单点 craft 强，而是 care 很重、能快速跨界的人

Anton 讲招聘时反复回到 care 和 generalist。Lovable 早期不是在拼传统职能表，而是在找那些真的在乎产品、用户和团队的人；他们要能快速学习很多技能，同时在某一维有绝对强项。这个标准和 Lovable 产品是一体两面：产品把软件创建交给更多非工程人，公司内部也需要员工跨过职能边界，把 AI、工程、设计、用户和业务一起想。AI 放大执行以后，窄 craft 反而不够，能把问题整体想通的人变得更贵。

“我会问候选人过去做过什么，这类人通常都做过一些自己非常在乎的东西，所以我会深入追问他们当时做过的技术细节。我们也会做正常的事，给一个很难、最好有点不常规、他们以前没见过的问题，看他们怎么思考、怎么推理。我觉得更不常见的是，我们几乎总会让人参加 work simulation，至少一天，很多时候是一整周；我们真正想看的是，他们是不是深度在乎自己做过的东西，能不能在细节上讲清楚，也能不能和团队一起把真实工作推进下去。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Work simulation 和硬核 JD 是 Lovable 的自筛选器

Lovable 的招聘不是普通面试流程。Anton 说他们几乎总会让候选人参加 work simulation，至少一天，经常一整周；Lenny 还读出早期 JD 里的句子：长时间、高速度、高紧迫感，不适合追求舒适工作的人。这套设计很硬，但也很诚实。它先把节奏、强度和不确定性摆出来，让不适合的人自己退出；留下来的人，才更可能适应一个 15 人团队每周推进 $1M ARR、不断改产品卡点的环境。

“Lenny 在访谈里读出那份岗位描述：长时间、高速度，候选人必须能在 AGI timeline 逼近的高紧迫感下工作；前方是困难使命，成功时会有荣誉和认可，追求舒适工作的人不要申请，另外还有和其他 exceptional minds 协作、比普通工程岗位更大的使命、以及对公司成功的慷慨分享。Anton 回应说，那份 JD 的格式确实有一些帮助，但不同句子的精确措辞主要是他自己写的；Lenny 接着说，这对一些人会是‘我绝对不报名’，但对你想要的人会是‘对，这正是我想做的事’，所以这本质上是在招聘里先把强度说清楚，让想要这种强度的人被吸引过来。” —— Lenny Rachitsky / Anton Osika, Lenny's Podcast, 2025-03-09

## Lovable 用很轻的 cadence 保住速度，三个月 roadmap 只做方向锚

Anton 对产品节奏的描述非常像早期 AI 应用公司的 operating system：先找最大的产品瓶颈，解决它，再找下一个。团队用 FigJam 把主要问题放在一起排序；用 weekly planning 决定本周聚焦什么；用 demo 让大家看到本周 ship 了什么；roadmap 能看到三个月，但一个月后变样也正常。这里的重点不是流程漂亮，而是流程足够轻，能承认 AI 应用公司的变量变化太快。它既避免完全混乱，也避免用重 roadmap 制造假确定性。

“如果回看三个月前，我们主要就是做 weekly planning：有一个 FigJam board，上面放着所有主要问题，然后我们把它们排一下，决定接下来或这一周聚焦哪一个；接着我们会做 demo，说这些就是这周 ship 出来的东西，让所有人都在同一页上。现在我们确实多了一点 roadmap，会说接下来要支持 custom domains，再之后加 collaboration；当前最大的 initiative 是让系统更 agentic，这个会有更长一点的 roadmap。但我们仍然保持 weekly planning 的 cadence，明确这周聚焦什么；比如这周一的计划基本就是 polish、fix bugs、polish，所以这周就是 polish week。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Linear 被拿来跟踪人才申请，说明早期 Lovable 还没有把工具按职能切死

Anton 顺口说公司很多事都在 Linear 里做，甚至 talent application tracking 也在 Linear 里。这个小细节比看起来重要：早期 Lovable 没有先搭一整套 HR、产品、工程、项目管理系统，再把职能边界一层层切开；它更像把一切能压进轻工具里的东西都先压进去，用少数工具降低 context loss。这个状态很适合早期高密度团队，但也暗示未来扩张会遇到边界：当 enterprise、GRC、security、sales 和 hiring 全部变复杂，轻工具可能需要被更专业的 owner 和系统替代。

“当 Lenny 问他们用什么工具、除了 FigJam 还有什么最新 stack 时，Anton 说：我们公司里很多事都用 Linear，因为它真的是一个很棒的产品；我们甚至用 Linear 做 talent application tracking。Lenny 听到以后很惊讶，Anton 补了一句，说他们看过很多为招聘专门定制的工具之后，最后还是用了 Linear 和 FigJam，很简单。” —— Anton Osika / Lenny Rachitsky, Lenny's Podcast, 2025-03-09

## Office 和 lunch 是 Lovable 的高带宽协调机制，不是生活方式细节

当 Lenny 问还有什么让小团队跑这么快，Anton 没有先讲 AI workflow，而是讲 office 和 lunch。大家多数时间在办公室，可以直接说“我们是不是想错了”；一起吃午饭是 cross-pollination 的高产时间；office 同时提供专注和非结构化高带宽沟通。这是 Lovable 很值得写进报告的反直觉点：AI-native 不等于纯远程、纯异步、全靠工具。AI 放大执行速度之后，错误方向也会更快被执行，线下高带宽校准反而更重要。

“我们大多数时间都在办公室工作，我觉得这很好，因为你可以直接说：嘿，我觉得我们在这件事上想错了，或者我们是不是其实应该做另一件事。尤其是午饭，一起吃午饭其实是很高产的一个小时，大家会互相 cross-pollinate；人们也会在潜意识里一直想着怎么解决不同问题，以及哪些问题才是最重要的。所以在办公室里，大部分时间你应该是专注的，但同时也会有这种高带宽的、稍微非结构化的沟通。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## 工程瓶颈下降后，产品团队更需要 taste、用户直觉和跨职能能力

Lenny 把未来产品团队的变化讲得很直：当构建本身越来越自动化，最值钱的是知道该做什么，以及判断做出来的东西是否正确。Anton 基本同意，并说如果今天组产品团队，他会强烈希望每个人都有尽可能多的技能：懂系统架构、懂设计、有产品 taste、会和用户沟通。这个判断和 Lovable 的招聘是一体的：AI 让执行变便宜之后，组织更需要能跨职能判断问题的人，而不是只完成一个窄任务的人。

“如果今天重新组一个产品团队，我会希望每个人都对使用 AI 很兴奋，这是很重要的一点；同时团队要能很好地一起工作，就像午饭时大家坐下来一起解问题一样。对大多数产品来说，未来瓶颈不会再那么集中在 engineering 上，而会更多落在好的 taste、对用户的好直觉上；工程师以及团队里的每个人，最好至少愿意经历那套动作，去听用户说话，真正理解他们在乎什么。我们招到的人最强相关的特征是原始认知能力，但也有很强的 startup mindset：更想快速移动、快速迭代，而不是要很多结构和流程；更愿意思考整个业务，而不是只守着自己的职业或 craft。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Lovable 的下一步，是从生成 demo 走向发布、协作、增长和运营

Anton 讲路线图时没有把 Lovable 停在“生成应用”。他提到 agentic behavior、custom domain、团队协作，也提到帮助 founder 在第一版产品之后获得用户、拿反馈、传播出去。更远一点，他还想让 AI 读取用户行为、提出产品优化、自动跑 A/B test。这个方向说明 Lovable 的野心不是 app builder，而是把早期公司从 idea 到 product，再到 growth 和运营的整条链路吃进去。真正的上限也在这里：demo 很容易被复制，持续业务闭环才更难。

“接下来我提到过 agentic behavior；我说 agentic，意思是你给系统更多自由，让它决定下一步发生什么，比如它可能想写测试、跑测试，看到测试失败以后再修，这会是让用户走得更远、更快的一个大 unlock。然后还有一些更明显的事：怎样一路走到真正用 Lovable 赚钱，比如怎么把它托管到自己的域名上，怎么和团队无缝协作。我们也在想，怎么帮助 founder 在做出第一版之后成功：他们怎么拿到更多用户，怎么获得反馈，如果他们做出了有用的东西，怎么让别人知道。” —— Anton Osika, Lenny's Podcast, 2025-03-09

## Anton 的失败案例说明，AI 产品不能只是把新技术硬塞进旧流程

Anton 讲 Sana Labs 旧经历时给了一个很有用的产品教训：他们曾经想把个性化学习 API 接到已有教育软件里，但让别人“换引擎”很难。这不是技术不够好，而是产品没有从端到端体验重新设计。这个教训解释了 Lovable 为什么要做完整产品，而不是只给开发者一个 API：用户不是想买一块 AI 能力，而是想从想法直接走到可用产品。反过来，这也是 Lovable 未来进入企业既有系统时会遇到的风险：一旦变成 retrofit，难度会重新上升。

“我职业里有一个产品教训：我曾经是斯德哥尔摩一家 AI startup Sana Labs 的第一个员工，当时的前提是人用不同方式学习，如果能个性化，学习效率会高两个标准差，所以我们做了一个个性化学习 API。AI 本身还不错，但最后我们做的事情其实是：这里已经有一个教育软件，比如某种学英语的产品，拥有这个产品的人必须接入我们的 advanced AI API，把它变成个性化。这是非常难的 retrofit，相当于让别人把原来的引擎换掉再塞进 AI。最大的学习是，你必须从端到端看这个产品到底怎样工作，再决定 AI 应该加在哪里；你要看到用户体验的大图，然后用 AI 去解决具体问题。” —— Anton Osika, Lenny's Podcast, 2025-03-09
