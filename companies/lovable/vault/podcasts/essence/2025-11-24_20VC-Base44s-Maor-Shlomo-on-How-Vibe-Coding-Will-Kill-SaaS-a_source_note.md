---
company: lovable
source_type: podcasts
type: source_note
status: done
source_path: companies/lovable/vault/podcasts/transcripts/2025-11-24_20VC-Base44s-Maor-Shlomo-on-How-Vibe-Coding-Will-Kill-SaaS-a.md
source_title: "20VC: Base44's Maor Shlomo on How Vibe Coding Will Kill SaaS and Salesforce | Why it is BS that Vibe Coding Platforms Do Not Have Defensibility and Bad Margins | Why He Worries About Google, Not Replit and Lovable | Why Long Anthropic, Not OpenAI?"
source_date: 2025-11-24
created_at: 2026-04-22
speaker: "Maor Shlomo / Harry Stebbings"
source_weight: B
relevance: high
quote_language: zh_translation_from_en_transcript
---

# 20VC: Base44's Maor Shlomo on How Vibe Coding Will Kill SaaS and Salesforce

> 这是 Lovable 竞品 Base44 founder 的第三方行业访谈；本 note 只保留能校准 Lovable 市场结构、竞争风险、毛利、模型依赖和产品边界的证据。

## Base44 founder 把 vibe coding 看成会吞并多类 SaaS 的最大软件品类

Maor 对品类上限的判断很激进：CRM、support、task management、project management 等既有软件类别会折进 vibe coding。这个观点对 Lovable 是外部校准：如果成立，Lovable 的可服务市场不是 app-builder 小工具，而是“软件如何被创建、定制、运营”的新入口；如果不成立，Lovable 的天花板会被限制在 prototype/MVP 和内部小工具。Maor 的论证核心是 software 变得更 liquid，用户可以从模板或开源起点出发，按自身流程持续改。

“在我看来，这会成为软件行业最大的 category，因为很多我们熟悉的既有 category，比如 CRM、support systems、task management、project management 等等，都会折进 vibe coding category。会有一个时间点，也许几个月、也许几年以后，自己构建一个 Salesforce 类型 CRM，会比买一个现成 license 更容易。软件会变得更 liquid：也许你有一个起点，有 templates，或者有 open-source projects，然后你 vibe code 自己的 features，比如我想要阿拉伯语从右到左版本，或者每个 lead 都能加我自己的图片。它会被转化成更符合你需求的东西。现在 one-size-fits-all 的模式对很多买家并不合理。” —— Maor Shlomo, 20VC, 2025-11-24

## SMB 的替代逻辑不是“拥有代码”，而是更 lean、更贴合自己的流程

Harry 质疑小企业是否真的在乎拥有 code/data，Maor 的回答更现实：小企业不一定关心代码所有权，但非常关心软件是否简单、是否为自己的流程定制、是否能理解和调整。这个洞察同样适用于 Lovable：非技术用户购买的不是“我拥有代码”的意识形态，而是“我能把复杂通用软件替换成刚好适合我的工具”的体验。Lovable 的价值要从具体小流程里证明，而不是抽象地喊 no-code。

“不一定是代码和数据本身，但他们确实需要更简单、更贴合自己需求的东西。我当初开始做 Base44，就是因为我当时的女朋友、现在的妻子有一个小生意，她需要一个 CLM 和一些系统；她是纹身艺术家，也教艺术。我们试过用传统的 drag-and-drop、可自定义表格或 CRM 工具来做，过程太糟了。我是软件人，按理说应该知道怎么做，但光是配置它，让它支持她处理 leads 和 customers 的方式，就已经很痛苦。LLM 完全可以写出一个更 lean、更好、更精确满足她需要的东西，没有一整套她不需要的 enterprise features、team management 和 settings。” —— Maor Shlomo, 20VC, 2025-11-24

## Vibe coding 的 moat 不在“能生成页面”，而在复杂应用所需的 mini-cloud

Maor 直接回应“这个品类没有 moat”：做一个能生成网站或前端的 vibe coding tool 很容易，但让真实用户构建复杂、可用、日常使用的软件很难，需要数据库、用户管理、权限、集成、scheduled tasks、cloud services 等一整套平台。这个判断能解释 Lovable 为什么不断扩 primitives，也说明竞争会从 demo 质量转向 depth of platform。真正的 moat 是把 AI 可控地接入真实软件基础设施。

“我认为创建一个 vibe coding tool 相对容易，但创建一个能帮助人们构建真正会使用、功能完整、复杂到足以覆盖现实 use cases 的产品的平台，是非常非常非常难的。为此你需要很多层 integrations，需要调校 agent 去处理非常复杂的项目；Base44 里有些 application 是数百万行代码。你几乎是在构建一个 small cloud，因为你想让 LLM 能访问 databases、有 user management、有内置 integrations、能跑 scheduled tasks，这才是真实软件会做的事。你还想让 LLM 能访问很多 cloud services 和 integrations，所以你是在这个平台里构建整个 ecosystem。” —— Maor Shlomo, 20VC, 2025-11-24

## 网站和 landing page 会 commoditize，利润更好的用例是日常复杂应用

Maor 把早期 vibe coding 中大量前端、landing page、电商网站 use case 视为会 commodity 化的部分，因为做完就不再持续 prompt，host 成本也低。相反，复杂 functional apps、organizational apps、personal apps、fully fledged SaaS platforms 会带来更高价值和更持续使用。Lovable 的收入质量也要按这个标准看：如果大部分使用停留在一次性生成网站，ARPA 和 retention 会受限；如果进入日常 workflow，平台价值会高很多。

“早期 vibe coding category 很大程度聚焦在 frontend、landing pages，很多 use case 是网站或电商网站之类。我认为这部分会被 commodity 化。比如你给自己的 business 做一个漂亮网站，做到某个时点它看起来很好，那就结束了，你不会再继续 prompt；而这个品类很多商业模式是围绕 prompting credits。所以你最后说，好了，我有这个东西了，host 成本也不高。我认为更 profitable、margin 更高、价值更大的，是构建复杂应用，也就是你每天使用的那些东西。” —— Maor Shlomo, 20VC, 2025-11-24

## Incumbent SaaS 也会把 vibe coding 嵌进去，Lovable 面临的是多入口竞争

Maor 认为 Salesforce、Monday、Microsoft 等既有软件会在自身系统上加入 built-in vibe coding，让用户自定义界面和工作流。这对 Lovable 是重要竞争风险：不仅有 Base44/Replit/Bolt，还有 incumbents 把 AI customization 嵌入现有 system of record。如果用户只是想改变 Salesforce UI 或 Monday workflow，现有平台可能更自然；Lovable 需要赢在跨系统创建、新应用启动和更强默认体验。

“我会把你说的 incumbents 叫作不同既有软件类别。比如 Salesforce 或 Monday.com，很多这类工具都会在平台内部构建 built-in vibe coding tools。你已经能看到 Monday Vibe，它建在 Monday 的 infrastructure 之上，背后有 database、user management、roles、permissions 等等。这就是我说 software 会变得更 liquid。也许未来你能为 Salesforce 创建自己的 UI，而 Salesforce 变成 system of record，你可以按自己想要的方式看 lead、contact 或 account。Microsoft 也会在 Office 等工作流上做 vibe coding 工具，所以我能看到未来很多既有 SaaS 产品都会内置‘把软件按你的需求自定义’的能力。” —— Maor Shlomo, 20VC, 2025-11-24

## Base44/Lovable 的方向是“不要看代码”，Cursor/Cognition 的方向是服务开发者

Maor 对市场分层说得很清楚：Base44、Bolt、Lovable 这类 visual/AI app builders 面向不想看代码的人；Cursor、Windsurf、Cognition 这类 professional tools 面向开发者和复杂工程项目。两边会互相上下探，但用户定义决定产品体验。对 Lovable 来说，进入更多复杂软件类型不等于把用户推到代码里，而是不断把更多 capability 封装成可 prompt 的平台能力。

“Base44 从第一天起的目标，就是你不需要看到一行代码。对很多用户来说，看到代码即便不是恐惧，也不是他们想做的事。比如你是律师，想给自己的律所做一个系统，你没有必要看代码；你应该能够只通过 prompting 自定义和做任何你想做的事。Cursor、Windsurf、Cognition 这些工具在服务现有 developer community 和他们的目标用户上做得很好；而 Base44、Bolt、Lovable 这类工具还需要很长时间，才能达到能构建今天还不能构建的那一部分软件。” —— Maor Shlomo, 20VC, 2025-11-24

## Lovable 不被 Maor 视为最大威胁，真正风险是模型供应商赢下全栈

Harry 让 Maor 在 Lovable、Replit、Bolt 等玩家里选最担心的对手，Maor 说“不担心这三个”，更关心模型供应商的市场动态。这个观点对 Lovable 很关键：应用层之间会互相竞争，但更结构性的威胁是某个 foundation model provider 长期大幅领先，然后顺手进入 vibe coding。Lovable 的上限依赖模型层保持竞争，让应用层可以多模型路由、吃成本下降和能力提升红利。

“我不担心那三个。我更想的是市场动态，以及事情会如何被模型供应商改变。我的理论是，能和多个模型供应商一起玩的公司总会有巨大优势。但如果某个模型供应商在某个时点以很大差距赢下市场，下一步合乎逻辑的事，就是去征服 vibe coding 市场，因为在我并不客观的眼里，这会是最大的软件 category。只要还有竞争、还有 race，我们就有位置去控制市场很大一部分，并给市场带来更好的解决方案。” —— Maor Shlomo, 20VC, 2025-11-24

## Google 是最大潜在威胁，因为它有 Gemini、Cloud、data、Workspace 和 integrations

Maor 在模型供应商里最担心 Google，这对 Lovable enterprise strategy 是强提醒。Google 如果在模型 race 里赢，拥有 cloud、数据、Workspace、integrations 和企业分发，可以把生成软件能力直接塞进用户已有工作流。Lovable 的 defensibility 不能只靠模型调用和生成体验，而要靠品牌、社区、应用平台、用户成功、跨栈 execution 和 faster product taste。

“如果问谁更可能做到，我会说 Google，远远是 Google。他们有 compute，动作非常快。如果 Gemini 在某个时点赢下 race，真的赢下 race，那他们就有整个 stack：Google Cloud、数据、各种 integrations、Google Suite，以及构建一个 incredible empire 所需的一切。我希望这场 race 会很激烈，而现在看起来确实是这样。” —— Maor Shlomo, 20VC, 2025-11-24

## 模型供应商切换只是一行配置，应用层要把模型竞争变成自己的红利

Maor 说 Base44 可以通过改一行代码，把数十万甚至数百万 spend 从一个模型供应商迁到另一个供应商。这说明 LLM API 的 switching cost 远低于 cloud，模型层很难成为 Lovable 的防御；Lovable 的价值必须建在 workflow、用户数据、product surface、社区和业务结果上。反过来，激烈模型竞争会让应用层根据设计、bug 修复、成本和吞吐做路由，持续改善体验和 margin。

“这个市场动态太疯狂了。我们当然在 AI 上花很多钱，而一瞬间你改代码里一个字符串，就能把数百万 spend 移到另一个 provider，它会根据谁有最好的模型、成本和 throughput 来回跳。比如 coding 空间里，Claude 出了 Sonnet 4，我们说很好，用它；之前我们可能在 Sonnet 和 Gemini 之间分配。然后 OpenAI 出了 GPT-5，你会发现不同模型在不同地方更强：Sonnet 可能是最好的 designer，擅长从零组织项目；但 GPT-5，尤其 thinking 和 pull 版本，很擅长解决 hard bugs。于是你会把很多复杂应用和大 context API calls 的 workload 移到 OpenAI。” —— Maor Shlomo, 20VC, 2025-11-24

## 毛利不是 Maor 最担心的问题，因为模型价格会下行且可智能路由

Maor 对“vibe coding 毛利差”的反驳有两层：模型价格会趋近零；应用层可以把简单请求路由给更小、更便宜、更快的模型，把复杂请求交给 frontier models。这个观点支持 Lovable 继续用体验换增长，但也要求产品架构能做 intelligent routing、成本观测和服务质量控制。毛利不会自动变好，变好来自模型竞争 + 平台工程 + 使用场景分层。

“我们在做战略选择时，会把模型价格会往零走这件事纳入考虑，至少对 Base44 这样的平台是这样。你当然可以今天投入很多人去优化成本，我们也会做，但也要考虑模型价格一直在往下。所有 coding agents 最终都会发生的一件事，是更便宜的 open source models 会变得更好；你仍然想用最强模型，但我们内部也在看一个 switch 或 proxy：当用户给一个 prompt，也许这个 prompt 很简单，像把按钮颜色从蓝改成红，那我不需要用 heavy Sonnet maximum thinking 去付很多钱，我可以把这个请求交给更小、更便宜的模型，体验还会更好，因为它更快。随着更小或开源模型能承担更大比例的 requests 和 prompts，margins 显然会大幅改善。” —— Maor Shlomo, 20VC, 2025-11-24

## 快速复制迫使平台做更深的结构性赌注

Maor 说每个新 feature 几周或几个月就会被复制，甚至 app suggestions 这种小功能几天就被同行抄走。这个竞争环境对 Lovable 同样成立：界面小亮点不能形成长期 moat，真正值得押的是用户重度需要且很难复制的结构性能力，比如自建 backend、应用基础设施、权限、analytics、agent environment、社区和企业流程。AI 应用公司的 product velocity 要同时服务 delight 和 defensibility。

“我们发布的每个 feature，都知道竞争对手几周或几个月内就会复制，我们也经常看到这种情况。两周前我们做了一个叫 app suggestions 的很小 feature，prompt 之后它会给你下一步建议，比如现在要不要加 dashboard，这是个很小但不错的功能；竞争对手几天就抄了。游戏就是这样。你要在对用户很重要、同时很难复制的东西上下注。Base44 存在的核心理由就是 built-in backend：每个 application 已经有内置 database、user management、authentication、integrations、analytics 等等；我们没有像行业其他人那样用 Superbase 之类第三方，而是内建了它，这一步很勇敢，也会让别人很难复制、很难把数百万用户从第三方迁到自研方案。” —— Maor Shlomo, 20VC, 2025-11-24

## 用户成功指标正在从“有没有 bug”转向“agent 是否准确执行意图”

Maor 描述 Base44 的内部指标时说，早期主要看 bug 和 breakage；现在基础设施和模型更稳定，问题转向 agent 是否真的做了用户要的事、有没有误改其他功能。他们甚至按分钟测 chat sentiment。这对 Lovable 很有参考价值：AI app builder 的 quality metric 不能只看 deploy 成功或页面可打开，而要看用户意图满足、变更精准度、负面情绪、真实日常使用。谁能更快把这些反馈转成系统改进，谁的可靠性提升更快。

“我们会测几件事。首先，我们测用户在 chat 里发的消息的 sentiment，这对我也很奇妙，但事实是很多人像跟人说话一样跟 chat 说话。他们会直接说，太棒了，这正是我想要的；或者说，这不是我想要的，你删了这个按钮，我想要的是那个。所以我们真的按分钟测，有多少 prompts 是负面的。业务里的 metric 也变化很大：刚开始主要围绕 bugs，模型多少次搞坏东西、应用不能工作；现在在你的 app 里制造 bug 已经不容易了，基础设施也经过 battle test，所以更多问题变成 agent 是否真的做了用户要求的事，是否做了正确改动，又没有额外乱改其他功能。” —— Maor Shlomo, 20VC, 2025-11-24

## Maor 的投资筛子提示，AI app revenue 需要和 vertical integration 一起看

Maor 说早期投资 AI 应用不能只看收入 hockey stick，还要看是否会被模型供应商吃掉、是否有 vertical integration。这个框架也适用于 Lovable：高 ARR 重要，但更重要的是收入背后是否有平台基础设施、用户 workflow、community、distribution 和多模型策略，而不是只是一层 prompt UX。Lovable 的投资判断应避免被增长曲线单独说服。

“作为投资人，我也在问自己这个问题。今天的指标确实不同，以前做到 200 万 ARR 可能要一年半，大家就会欢呼；现在如果你展示从 0 到 1000 万或 2000 万美元的 hockey stick，所有事情都会改变。我最看重的除了快速收入增长，还有两件事：第一，这个业务有多健康，有多可能被其他玩家或模型供应商吃掉；第二，也是很相关的，是它是不是 vertically integrated business。比如如果一家公司只是怎么 prompt 一个 LLM，或者更好地把它调到法律或金融需求上，而下面的基础设施并不复杂，那就很难有 moat。” —— Maor Shlomo, 20VC, 2025-11-24

## 非技术用户的正确起步方式，是从自己的问题出发并愿意扔掉第一版

Maor 给非技术用户的建议和 Lovable 用户教育高度相关：从自己的问题出发，不要一开始写完整 PRD，而是先做一个注定会扔掉的版本，用它找 product truth。AI app builder 让代码成本下降，真正稀缺的是用户问题理解、快速试错和产品判断。Lovable 的 onboarding 如果能教用户接受 revert、restart、throwaway prototypes，会显著提高成功率。

“step zero 是最大的 hack：构建你自己的问题。这样最容易做出之后你真的会用、甚至可能成功的软件。刚开始用 Base44 这类工具时，需要一种 mindset：Base44 不是一个人类开发者，工作一周后回来给你看成果。你要进入一种很容易 revert 或从头开始的心态。不要先写一个 PRD 再塞进去，而是先做一个你知道会扔掉的第一版；对一些人来说，扔掉几万行代码在情感上很难接受，但没关系，你真正需要弄清楚的是产品。一旦产品想清楚了，几个 prompts 就能到达你之前几百上千个 prompts 才到的位置。” —— Maor Shlomo, 20VC, 2025-11-24
