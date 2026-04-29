---
company: lovable
source_type: podcasts
type: source_note
status: done
source_path: companies/lovable/vault/podcasts/transcripts/2025-09-19_Metas-creepy-new-Ray-Bans-Beehiiv-teams-with-Discord-AND-a-v.md
source_title: "Meta’s “creepy” new Ray Bans, Beehiiv teams with Discord, AND a visit from Lovable CEO Anton Osika! | E2181"
source_date: 2025-09-19
created_at: 2026-04-22
speaker: "Anton Osika / Jason Calacanis / Alex Wilhelm"
source_weight: A
relevance: high
quote_language: zh_translation_from_en_transcript
---

# Meta’s “creepy” new Ray Bans, Beehiiv teams with Discord, AND a visit from Lovable CEO Anton Osika! | E2181

> 这期是多主题新闻播客；本 note 只保留 Anton 访谈、主持人围绕 Lovable 的使用案例和竞争/社区讨论，忽略 Meta glasses、Beehiiv、IPO 等非 Lovable 新闻段落。

## 20,000 付费客户到接近 20 倍，说明 Lovable 的 adoption 已经越过 AI 尝鲜层

Anton 在 TWIST 里给出比 ARR headline 更细的增长线索：2 月刚到约 20,000 paying customers，9 月已经接近 20 倍。这个数字说明 Lovable 的扩散不是少数大客户或投机 demo 拉起来的表面繁荣，而是付费人群规模快速扩大。Anton 把增长同时连接到 99% non-coders、founders、enterprise PM/designer/marketer，说明 Lovable 的需求两端都在长：个人/小团队做产品，大企业做 prototype 和工作流提速。

“上次我们二月聊的时候，我记得我们刚刚达到大概 20,000 个付费客户；现在这个数字几乎是那时的 20 倍。产品其实还处在非常早期。我们要做的是让那 99% 不会写代码的人，能够立刻把自己的想法变成软件；这会释放创业，也会让非常大的企业提速，因为产品经理、设计师、营销人员都能在不被工程师卡住的情况下推进。随着产品能力变得更强，我们也自然能够捕获软件世界里被释放出来的更多价值。” —— Anton Osika, This Week in Startups, 2025-09-19

## Security 被 Anton 定义为 Lovable 的许可门槛，而不是附加功能

Jason 从 vibe-coded tea 等安全事故切入问 production readiness，Anton 的回答很硬：如果你构建的东西不安全，就不该构建。这个 framing 很重要，因为 Lovable 的主用户很多不是开发者，平台不能把安全责任甩给用户；它必须把 secure code、扫描和 guardrails 做进默认系统。Anton 用登月火箭类比，表达的是复杂任务里 AI system 会比人类手工更可靠，但他也保留了敏感场景仍需专家的边界。

“我们把 security 当成最高优先级，因为如果你在构建一个不安全的东西，那你一开始就不应该构建它。你看 60 年代把人送上月球，当然可以让一个人坐在 cockpit 里操控火箭，但那时人们已经意识到，你需要一台计算机来运行火箭发射任务，因为在某个明确范围里它可靠得多。人类总会犯错，计算机安全也会发生同样的事情：你不会只是信任一个人类写出安全代码，你需要一个 AI system 来写安全代码。过去几个月我们发布了几个 security features，会扫描 AI 为你写下的所有 client 和代码；我今天不能说它比安全专家更安全，所以对生死攸关的应用或非常敏感的数据，我百分之百建议把安全专家拉进来。” —— Anton Osika, This Week in Startups, 2025-09-19

## Lovable 押注 18 个月内在标准应用安全上超过人类专家

Anton 对 security crossover 的判断很激进：完全在 Lovable 内构建的应用，平均安全性会在未来 18 个月超过专家手写。这不是泛泛“AI 会变强”，而是 Lovable 对自己 platform scope 的判断：只要架构足够 opinionated，AI 决策空间足够受控，系统就能在大量标准软件上跑出比普通人类开发更一致的安全结果。这个判断需要后续用漏洞事件、enterprise security review 和 compliance 能力验证。

“如果你问的是在 Lovable 里完全构建的应用，和从零开始的主要替代方案相比，我认为平均来看会更安全；未来 18 个月内，它会在平均意义上更安全。不是任意项目都这样，也不是那些 AI 从没见过的非常特殊项目；在那些 frontier novelty 上，人类仍然是在前沿探索、弄清问题的人。但对几乎所有标准软件，甚至像银行软件这类标准化软件，我们会看到领先平台越来越安全。” —— Anton Osika, This Week in Startups, 2025-09-19

## Opinionated stack 是 Lovable 可靠性的核心，不是产品能力变窄

面对听众质疑“opinionated stack 会不会限制 Lovable 能力”，Anton 的回答把平台战略讲清楚：Lovable 要覆盖 95% SaaS 所需 primitives，真正 opinionated 的是这些 primitives 如何组合成架构。对 non-technical 用户来说，任意性不是优势，可靠性才是；Lovable 把数据库、用户、支付、托管、集成等决策收进平台，让 AI 更容易作出正确决定。这和 Cursor/Claude Code 的 professional coding tool 路线明显不同。

“Lovable 需要在软件架构层面拥有所有 primitives，才能创建 95% SaaS 公司需要的一切。Facebook 规模的产品也许很难在 Lovable 上 vibe code，但这些不同 primitives 如何组合成技术架构，才是我们 opinionated 的地方。只要你拥有所有 primitives，就不应该显著缩窄你能生产什么。我们正在构建完整平台，让 AI 在我们的特定应用架构里尽可能容易地作决策；把它适配给 AI、把周边体验打磨好、给 AI 加上 guardrails，同时大模型实验室每三个月发布能力更强的新模型，这几件事有很强协同。我们做得 opinionated，不像 Claude Code 和 Cursor，正是为什么它会快速变得对非技术人也更可靠。” —— Anton Osika, This Week in Startups, 2025-09-19

## Lovable 的 long product scope 是把前置和后置条件都塞进平台

Anton 不把 Lovable 限定在“生成代码”，而是明确讲到一键支付、未来公司注册、银行账户、AI inside apps。这个路线图把 Lovable 从 app builder 推向 business builder：用户不想理解 Stripe、Atlas、hosting、AI compute、domain 和运营拼装细节，而是希望从想法直接走到可运营业务。上限由此变大，但平台要承担的成本、合规和客户支持复杂度也同步升高。

“你说得对，我们在思考 vibe coding 周围所有前置条件和后置条件。Hosting 今天完全免费，你在平台里买 custom domain 才付费；构建本身会消耗很多 AI compute，所以我们现在主要为这个收费。未来你一旦做出了某个东西，它上线后就应该能够向客户收费，Stripe 就是这样赚钱的；现在多数公司和软件都有 AI 内置，而你不应该还要去想这到底如何工作，它应该就是能用。比如未来也许一键支付就设置好了，再往后也许你的整家公司、银行账户都在一个平台里设置好。” —— Anton Osika, This Week in Startups, 2025-09-19

## Paying users 已经毛利为正，Lovable 的增长不是完全靠 token 补贴

Jason 追问 AI 工具是否 per-user 亏损，Anton 给出关键 unit economics 线索：free users 和 paying users 拆开看，付费用户已 gross margin profitable。这不能说明整体公司已经成熟盈利，因为免费层、增长投入、模型成本波动仍然重要；但它足以反驳“AI app 的收入都是烧 token 买来的假收入”的最粗糙怀疑。Lovable 至少可以在不改变业务模式的情况下走向盈利。

“我们希望构建和创造东西变得越来越便宜，因为使命的一部分就是让人类创造力成为驱动力，而不是让我们只消费无脑内容。今天我们处在一个很好的位置：不需要对业务运作方式做很大改变，就可以很容易变得盈利。如果把用户拆成免费用户和付费用户来看，付费用户这一侧已经有 gross margin profitability。这意味着我们可以非常快速地获得和增长用户，而不用因为银行账户而恐慌。” —— Anton Osika, This Week in Startups, 2025-09-19

## Anton 不愿把战略压成价格战，因为当前窗口仍是产品代际机会

当主持人问 pricing war，Anton 说自己多数周几乎不想 pricing，而是想怎样做出 customers love 的 generational product。这不是说定价不重要，而是 Lovable 仍在 category formation 期：如果过早用价格竞争定义赛道，会错过产品能力和用户心智的窗口。Anton 反复把目标放到 billion builders、foundation for building anything，也是在用更大市场叙事抵抗短期价格战。

“我不太想 pricing；你们这次对话里想 pricing 的时间，比我多数周想得还多。我们真正想的是构建一个客户热爱的产品，并在它之上做出一个 generational product 和 generational company。我们希望 Lovable 被十亿个开发者，或者不需要写软件代码的 builders 使用。今天大概有五千万开发者，但它应该成为人们构建任何东西的 foundation。对我们来说，可能做到的不只是把 trillion-dollar outcome 当成目标，而是把它变成一个 proving ground，让欧洲公司更多的雄心、人才和强文化被激励去拥有全球级目标。” —— Anton Osika, This Week in Startups, 2025-09-19

## “为什么没看到更多 AI app”这个质疑错在观察位置

Anton 对“AI coding claims don't add up”的回应很有用：很多 Lovable 产物不会出现在 GitHub 或 App Store，而是存在于 web apps、内部工具、部门流程、founder-led 小业务、企业验证阶段。Q Group founder 三周做产品并借既有分发两天 $3M，是一个极端但说明问题的案例。Lovable 的真实 adoption 可能大量发生在传统开发者统计看不到的边缘。

“批评者看错了地方。今天我们使用的软件产品太多，所以成功案例不一定进入主流媒体。比如在巴西有一家叫 Q Group 的公司，创始人自己坐下来，三周内为他们做出一个新产品并发布，借助一些既有分发渠道，发布后前两天就做了 300 万美元收入。这只是成千上万正在被构建的业务之一，而这些业务很多时候来自过去没有基础资本、也没有专门技能去构建业务的人。非常大的公司也在用这项技术，把它用于产品生命周期的一部分，也就是最耗时的那 60%：弄清这件事到底是否值得投资、是否值得一路推到客户面前。” —— Anton Osika, This Week in Startups, 2025-09-19

## Lovable 给 PM、designer、marketer 的价值是把 specification 变成可试产品

Anton 对企业 workflow 的描述很直接：PM、designer、marketer 不再只“讲一个想法”，而是在几个小时里 build 出来，给经理或客户试，再决定是否 launch。工程师拿到的也不是抽象 PRD，而是“perfect specification”。这个机制解释 Lovable 为什么能在大公司里扩散：它不一定先替代工程，而是减少需求转译、方向验证和内部说服的浪费。

“产品经理、设计师和营销人员现在能快很多，Lovable 是他们证明‘这是我的好想法’的最佳工具。他们不只是谈论一个想法，而是在几个小时内把它构建出来，拿给经理看，或者和客户一起试，然后说我们发布它吧。这样你就节省了 60% 的时间，工程师也拿到了一个完美 specification，去系统里真正实现它。” —— Anton Osika, This Week in Startups, 2025-09-19

## AI-native 年轻人的组织价值，是主动把重复工作产品化

Jason 把 Lovable 连接到年轻人就业和 spec work 3.0，Anton 顺势讲了公司内部 20 岁 automation 人才。这个片段说明 AI-native 的竞争优势不只是会 prompt，而是能发现重复、无聊、昂贵的流程，把它变成自动化或小产品。Lovable 这类工具会让 entry-level worker 用更高阶的 artifact 证明自己，也会改变组织内部谁能推动改变。

“我觉得你说的这种情况一定会发生：年轻人学习更快，也更有主动性，他们会进入公司说，我能做你们现有员工目前不能做的这些新东西，因为我是在 AI-native 环境里长大的。我公司里就有一个 20 岁的人在帮我们做 automations；我不能把最 senior 的工程师放到 automations 上，但我给他的使命是：你要 automate Lovable，这就是你的目标，把 Lovable 的一切都自动化。” —— Anton Osika, This Week in Startups, 2025-09-19

## 学生不是当前最大收入来源，但 Lovable 在押注下一代 founder cohort

Anton 说 Lovable 在学生里很受欢迎，但学生资本不足，还不是主要收入来源；真正的收入大头是 founders、entrepreneurs、小公司和 developer agencies。这里的投资含义是，学生 adoption 是未来 founder pipeline，而不是当前 monetization。Lovable 如果能成为大学生和年轻 builder 的默认软件创建工具，未来可能像 GitHub、Figma、Notion 一样从教育/side project 进入工作和创业。

“Lovable 在学生中非常受欢迎，因为很多学生有点幻灭，觉得自己在大学里做的只是问 ChatGPT，然后把答案交到作业里，他们在想下一步是什么。我听说瑞典最有名的技术大学里，毕业后会考虑创业或成为 founding team 一员的学生，过去十年从 8% 到了 80%，这是巨大的变化。你在活动现场真的能感受到，很多年轻人想做成功的 startup，也经常来找我说，我太感谢你了，你救了我的公司，或者你让我能基于在 Lovable 里做出来的东西融到一大轮。学生资本不够，所以还不是我们收入最大部分；我们押注的是，当他们成为 founder 时，这会变成收入来源，而 founders、entrepreneurs、小公司、developer agencies 这些被找不到好工程师或付不起好工程师卡住的人，今天就是我们最大的收入来源。” —— Anton Osika, This Week in Startups, 2025-09-19

## 10 万人 Discord 和 300 场草根活动，是 Lovable 的教育和分发资产

Lovable 的 community 不只是支持论坛，而是用户互相学习如何“和 AI 串联工作”的教育系统。Jason 读出 Discord 有 106,258 members、8,744 online，Anton 又提到年底 300 场 grassroots events；这说明 Lovable 已经有自发社区能承接产品复杂度。Anton 也承认团队在 community 上人手不足，说明这里既是 moat 也是组织短板：如果做成 ambassador platform，教育成本和分发成本都会下降。

“社区和用户想互相教会彼此怎样释放这个工具的全部潜力，因为它看起来很简单，只是一个 chat box，但要真正掌握它、能和 AI tandem 工作，其实有很多东西要学，教育部分非常大。所有 hackathons 和活动也一样，我们今年年底大概会有 300 场围绕 Lovable 的 grassroots events。现在我们还没有像本可以那样主动投入，主要一个人在做这些事，团队完全人手不足；但你要思考的是，人们进入社区后的 journey 是什么，如果有人是好的 ambassador、能教育别人，就给他们一个平台，一个他们可以在社区里利用的个人平台。” —— Anton Osika, This Week in Startups, 2025-09-19

## Anton 对 AI regulation 的立场，是避免欧洲式过早重监管，但承认 frontier risk

虽然这段不是 Lovable 产品本身，但反映 founder 世界观：Anton 讨厌 overregulation，尤其把欧洲当反例；同时他承认引入可能超过人类的新智能确实有不可预测性，应该有某些提前监管。关键是避免 regulatory capture，把 burden 放在足够大的 frontier players 上，而不是压死小玩家。这个立场会影响 Lovable 对 AI policy、Europe building 和大模型供应商关系的判断。

“我讨厌过度监管。我觉得欧洲就是一个例子，我们也许太容易在看到问题之前就扣动过度监管的扳机。当然，引入一个新的智能物种有点吓人；人类是这个星球上的主导物种，是因为我们有智能，如果你引入一种新智能，也许几年后在很多方面比我们更聪明，那就更不可预测。可能我们确实应该提前思考监管其中一些东西。但我认为可以用一种不造成 regulatory capture 的方式来做，领导者应该从 first principles 出发问：如果我们应该监管，能不能以不造成 regulatory capture 的方式监管？我认为答案是可以，让比 Anthropic 小的玩家不用承担那么多监管负担，而只有大玩家需要承担这些负担。” —— Anton Osika, This Week in Startups, 2025-09-19

## Stockholm 的 AI 优势来自认真做产品的工程文化和长期主义

Anton 对 Stockholm 的解释不是“水好”这种玩笑，而是当地有一批好奇、 grounded、认真做产品的工程师，不频繁 cloud hopping，愿意长期投入。他还追溯到 2015-2016 年左右 Stockholm AI 社区，大家读论文、实现模型、把 AI 做成产品。这个背景让 Lovable 的欧洲叙事更可信：它不是突然冒出的 AI app，而是从本地 AI community、unicorn alumni 和产品工程文化里长出来。

“Stockholm 有一个很深的工程师池子，他们非常好奇、脚踏实地，也很认真地构建好产品。这里的人不是每年在 startup 之间跳来跳去追逐 cloud，他们真的在乎自己在做什么；这种长期思考的文化很重要。十年前我在 AI 这边的时候，deep learning 正在起飞，我们这里有些人建立了早期 AI 社区，里面出来了很多很强的 alumni；那不是 hype，只是一小群人在读最新研究论文、实现它们、真的关心怎么把它一路做到产品。我觉得那种在 AI 之上做产品的精神留下来了。现在 Stockholm 是人才磁铁，我的大部分 leadership team 都是从 SF 搬到 Stockholm 来的。” —— Anton Osika, This Week in Startups, 2025-09-19

## Lovable mafia 是长期生态想象，二级出售被用来降低风险厌恶而不是提前兑现

Anton 把上一家公司 Depict 里走出的多家 YC 公司作为 Lovable mafia 的先例，说明他把员工未来创业当成生态结果；但对 secondary，他强调只允许有限 chips off the table，目的是减少员工个人风险厌恶，而不是让人过早失去动力。对高速估值上升公司，这是现实组织机制：既要让早期员工相信 equity 有价值，又要防止流动性破坏长期冲刺。

“我以前在上一家公司 Depict 时也会这样说，从那里我们已经看到四家 YC 公司出来，其中多家估值到了数亿美元。对 Lovable 来说，这更多是未来的事情。我们想帮助员工；拿一点 chips off the table 应该是为了让你少一点风险厌恶。做 secondary sales 时，我们会限制总量。你真正应该在这里结束后感到骄傲的，是我们构建了怎样的 generational product、generational company 和 team；如果拿一些筹码下来，也应该只是为了让你更少从 risk-averse 的角度思考。” —— Anton Osika, This Week in Startups, 2025-09-19
