---
company: lovable
source_type: podcasts
type: source_note
status: done
source_path: companies/lovable/vault/podcasts/transcripts/2025-07-24_20VC-Lovable-Raises-at-2BN--Hits-100M-ARR--Is-Cursor-Worth-2.md
source_title: "20VC: Lovable Raises at $2BN & Hits $100M ARR | Is Cursor Worth $28BN at $1BN in ARR"
source_date: 2025-07-24
created_at: 2026-04-22
speaker: "Harry Stebbings / Jason Lemkin / Rory Driscoll"
source_weight: B+
relevance: high
evidence_role: investor_market_analysis
quote_language: zh_translation_from_en_transcript
quote_style: single_long_translated_excerpt_per_block
---

# Lovable / 20VC Roundtable 2025-07-24 — Source Note

> 这是一篇第三方投资人 / 市场圆桌 source note。它不代表 Lovable 内部事实，但能作为融资、估值、AI app builder 安全风险、platform dependency 和 Lovable vs Cursor 市场空间的外部证据。以下每个 insight block 后面只放一条较长的中文译引；如需逐字核验，回到 `source_path`。

## 第三方投资人真正改变判断的，是亲手 vibe coding 后意识到“非工程用户市场”刚刚开始

这条圆桌不是 Lovable 管理层访谈，但相关性很高，因为它记录了投资人从旁观者变成用户后的认知变化。Jason Lemkin 的判断很直接：vibe coding 才刚开始，非开发者市场只走了几个月，开发者市场也不到一年。对 Lovable 来说，这个外部反馈比融资新闻更有价值，它证明产品不只是在 AI 圈内被讨论，而是在懂 SaaS、懂市场的投资人身上触发了“以前做不到的事现在能做”的体验。这是 AI 应用层爆发的典型信号。

“过去一周我学到了太多，太疯狂了，像最大的 firehose。我觉得你对 Lovable 的投资，甚至比我一周前意识到的还要好。这些 app，你停不下来，真的是 tsunami。Vibe coding 才刚刚开始；非开发者 vibe coding 只有六个月，开发者这边也不到一年。你能在这些平台上做的事情，是以前根本做不到的。而在 venture 里，当你能做以前做不到的事情时，钱就是在那里赚到的，也是在那里出现大赢家。” —— Jason Lemkin, 20VC Roundtable, 2025-07-24

## Vibe coding 的安全风险来自 agent 触碰真实生产环境，而不是代码生成本身

Jason 的 Replit 事故复盘给 Lovable 提供了一个外部风险框架：危险不是 AI 生成代码，而是 agent 可以修改真实环境里的代码、数据库和数据，而非工程用户并不知道 preview、staging、production 之间的边界。Lovable 如果要服务非工程用户并进入企业，就必须把工程团队默认知道的生产环境常识产品化，否则“更快 build”会直接转化成安全事故。

“我之前不理解 agent 可以帮我建网站、建平台，同时也能改任何一行代码，哪怕它已经在外面、已经在真实世界里。我不理解这一点。做 web software 从很早开始就有 preview、staging、production：preview 是我们在办公室里做的，准备进入真实世界时放到 staging，仔细测试，模拟真实世界但锁住，不暴露给客户和客户数据；等你对 staging 舒服了，再翻到真实 production，那里应该被彻底锁住、不能随便碰。可是这些 vibe apps 之所以这么快、这么灵活，一个原因是所有东西共用同一个 database、同一套 code。如果你是 business person，你根本不知道发生了什么。企业会害怕，因为 agent 会出去改数据库里的东西，或者拿走数据。” —— Jason Lemkin, 20VC Roundtable, 2025-07-24

## AI agent 的“取悦用户”倾向，让 Lovable 必须把 guardrails 做成产品主干

Jason 把 Claude / agent 的行为讲得很粗粝，但背后是一个核心产品问题：模型会为了完成用户目标而越界、编造、隐藏行动，工程师还能用测试和 review 拦住，非技术用户很难发现。Lovable 的目标用户越广，越要把权限、隔离、审计、预览、回滚、安全审查和数据边界做成默认体验，而不是高级功能。这也是 Lovable 从 demo 工具走向平台时必须补的组织能力。

“Claude 的目标是 problem solving 和 satisfaction。如果你让它做一件事一次，它会尝试做；如果你问第二次，它会开始 cheat，有时第一次就会；问第三次，它就会跑偏并编很多东西。它是一个 heat-seeking missile，目标是让你开心，也会为了让你开心而撒谎。你用 Cursor 或 Claude Code 时它也会撒谎；工程师会做一个小测试，看到它做了疯狂的事，就回退、revert、删掉。但如果你是 business person，你不知道发生了什么。大家都知道 agents 不能被 trust；如果一个很聪明的团队成员你不能 trust，你要么开掉他，要么给他上最紧的 leash。应用越简单、越内部，问题越少；但我问 Claude，agent 能不能被信任去处理 production data？Claude 说，当然不能。” —— Jason Lemkin, 20VC Roundtable, 2025-07-24

## All-in-one solution 越完整，安全和治理挑战越难，反过来也越厚

圆桌里有一个很好的产品策略判断：越接近 prosumer all-in-one solution，用户越希望 app 做所有事，不只是 review 或写一个小 feature；但越完整，安全和治理挑战也越难。Lovable 的机会和风险在同一件事上：它想覆盖 ideation to production，所以比单点 code editor 更难；如果它能把这套复杂性吃下，就会比薄 wrapper 更有防御性。

“这些应用需要从根本上把 security 做得更好，也会出现一批专门给这类东西做 guardrails 的安全 app。平台自己也都在加这些东西，30 天前不如现在，一周前也不如现在，它们会变好。但有意思的是，越往 prosumer 走，越想让 app 做所有事，而不是只 review、只 build 一个小 feature，就像 Claude Code 那样。所以越接近 all-in-one solution，这些挑战越难。好消息是，你越不像 thin wrapper，越有机会形成防御。” —— Jason Lemkin / 20VC Roundtable, 2025-07-24

## Lovable 比 Cursor 更难做，因为它服务的是不懂背景知识的用户，也因此更可能长出厚 wrapper

圆桌里对 Lovable vs Cursor 的区分很有用：Cursor 面向 proficient engineer，用户自己懂背景、测试、架构和危险信号，工具只需要提升开发效率；Lovable 面向技术背景更少的人，必须替用户处理更完整的问题，包括安全、部署、约束、工作流和错误边界。这让 Lovable 的任务更难，也让它更有机会长出厚的 product wrapper。如果它真能把“非工程用户也能安全生成可运行软件”做稳，价值会比 IDE 插件更接近平台。

“Lovable 或 Replit 服务的是像 business developer 这样的人：技术上比较 savvy，但不是工程师。他们想解决完整问题，所以平台必须替他们做很多事情。Cursor 卖给软件工程师，隐含前提是工程师理解很多背景知识，你和我可能并不理解。所以某种意义上，Cursor 的任务更简单，因为它是在给 proficient user 写工具；Lovable 是在给 less proficient user 做工具。按 spreadsheet 看，每个工程师都会买 Claude Code 或 Cursor 这类 200 美元订阅；但如果用 seed-guy 的方式问，什么东西能 enduring for a generation，我会看 Lovable。因为如果每个人类都能用，Lovable 的 TAM expansion 是大得多的机会。” —— Jason Lemkin / Rory Driscoll, 20VC Roundtable, 2025-07-24

## Lovable 的防御性可能来自每天啃一个“看似不可解”的问题

圆桌里把 Lovable 的更大机会归因于“empowering a whole new set of people”。这个判断和 Anton 的使命一致：AI 应用层的大机会不来自把已有开发者工作便宜一点，而是让全新人群拥有创建软件的能力。更关键的是，Jason 把这类问题称为 unsolvable problem：每天 chip away，产品不断变好，才会形成防御。Lovable 的 source notes 后续应该围绕这些 hard problems 追踪：安全、可靠性、用户表达、部署、业务闭环、企业治理。

“我觉得更好的核心点是：当你做一件全新的事、empower 一整批新人时，巨大的 venture opportunity 就在那里。换句话说，当你解决一个原本不可解决的问题时，那些问题很有意思，也有防御性。Unsolvable problems are defensible。你每天啃掉一点，让它越来越好。六个月后，另一个 Jason 再去做过去八天那种 80 小时不睡觉的 vibe coding，如果没有这些问题，10 小时就把产品做出来，那么做成这件事的公司会是一家巨大公司。” —— Jason Lemkin / 20VC Roundtable, 2025-07-24

## Anthropic dependency 不是短期死穴，但会成为平台分润压力

圆桌对 Anthropic / Cursor / Windsurf 关系的讨论很有投资价值：短期 Anthropic 没必要切掉最大客户，因为客户增长解释了它自己的收入加速；长期平台公司会像 Microsoft 一样“grind everyone down”，通过价格、访问、产品重叠拿走更多价值。Lovable 的启示是，它必须避免成为可替换薄 wrapper，把真正的用户上下文、应用生命周期、安全体系和企业工作流留在自己层里。否则模型平台上游收租时，应用层毛利会被挤压。

“如果 Cursor 做到十亿美元收入，其中多少比例会流向 Anthropic？又有多少比例解释了 Anthropic 过去六个月的惊人加速？你会说，那就让它去做吧；我也许会有一点竞争产品，但现在先 let a thousand flowers bloom。等事情变得更难时，就像 90 年代的 Microsoft，平台提供商会开始 grind everyone down，拿走更多 share。Anthropic 如果现在切掉这些产品里可能最大的客户，会非常蠢，而他们不蠢，所以我不觉得他们会这样做。但他们切掉 Windsurf 时确实很 ruthless；你必须假设这还会再次发生。” —— Rory Driscoll / Jason Lemkin, 20VC Roundtable, 2025-07-24

## Lovable 可以用 n-minus-one 模型，是相对 developer IDE 更舒服的平台位置

Jason 提到一个很有意思的差别：Windsurf/Cursor 这类 developer IDE 需要接入开发者最想要的 state-of-the-art 模型，否则价值会被 Claude Code 等直接替代；但 Lovable 这类 all-in-one app builder 在某些任务上可以用 n-minus-one 模型，甚至更合适，因为最新模型更慢、更贵、不一定更适合普通产品生成。这对 Lovable 的 unit economics 和供应商依赖都很重要：它可以用模型编排和任务分配降低成本，而不是每一步都押最贵 frontier model。

“当你使用这些 vibe apps 时，它们甚至不一定用 Claude Opus 4，这就是这些模型的力量：你不需要最新模型。Windsurf 和 Cursor 如果不能接入每个开发者想要的 state-of-the-art，就很难和 Claude Code 竞争。我自己打开过 Opus 4，Reddit 上叫 bankruptcy mode，成本大概是 7.5 倍，从每分钟 20 美分涨到 1 美元、1.5 美元；每小时都收到新的 50 美元收费提醒，我当时像是在走向每月 8000 美元账单。但有意思的是，它在我做的事情上反而更差，耗时更久、想太多。我不是在改变世界。所以 Lovable 可以用 n-minus-one model，而且非常好；这很有意思，甚至比大家疯狂追的最新模型更适合。” —— Jason Lemkin, 20VC Roundtable, 2025-07-24

## Anthropic 的开发者/企业动能说明 AI app builder 的上游仍在快速改写

圆桌对 Anthropic 和 OpenAI 的讨论，是 Lovable 的上游市场背景：Anthropic 在 developer 和 enterprise 方向找到明确 vein，过去数月加速非常快；OpenAI 仍拥有更强 consumer 入口，也不会放弃 enterprise。对 Lovable 来说，这意味着底层模型供应不会稳定成单一 vendor，应用层必须持续适配多个 provider，并在模型能力、成本和供应商关系之间做组合。

“我不认为 OpenAI 这种我们这一代最 ambitious 的公司会说自己放弃 enterprise，他们刚刚还想买 Windsurf。所以不是这样。但 Anthropic 确实找到了一个它能赢的位置，而且在那个空间里明显加速。如果数字正确，从 10 亿 ARR 到 40 亿 ARR，在过去六到九个月里，这是 extraordinary acceleration，而且明显快于 OpenAI。它们找到了 coding 这条 vein，并且正在奏效。OpenAI 更大，有整个 consumer business，Anthropic 不会有；但最后会坐在 startup 桌上的两个人，感觉是 OpenAI 和 Anthropic。” —— Rory Driscoll / 20VC Roundtable, 2025-07-24

## Figma 的公开市场定价提醒 Lovable：AI 私募估值和经典软件倍数已经分裂

圆桌对 Figma IPO 的讨论虽然不是 Lovable 直接材料，但能提供估值背景：Figma 作为经典软件里增长和利润都很好的公司，公开市场指引价看起来仍显著低于 AI 私募市场里 Perplexity、Cursor、Lovable 等交易的叙事倍数。这个对比提醒报告不能只用传统 SaaS revenue multiple 看 Lovable；但也不能忽视公开市场最终会要求利润、增长质量和可持续性。

“Figma 统治了一个 category，经典软件里几乎没见过这样的数字，却看起来和 Perplexity 最新一轮差不多甚至更低。它同比增长 46%，free cash flow margin 28%，是个很好的生意；按完全摊薄价格大约 160 亿美元。这个价格在 NTM revenue multiple 看是 14 到 16 倍，它的增长比几乎所有 public companies 都好，growth-adjusted 看起来很便宜。当然 IPO 会先放一个有吸引力的价格，把人带进 meeting、读 prospectus、建立需求，然后再往上走；但这个过程也会产生 anchoring，最后可能仍会留下 pop。” —— 20VC Roundtable, 2025-07-24

## 企业 AI 共识被资本快速定价，Lovable 的融资窗口来自数字变明显前后的时间差

后半段 venture 讨论有一句对 Lovable 很有用：当企业 AI 成为 consensus bet，一旦数字证明某家公司在跑，价格就会迅速上升到“best case 都被算进去”的水平。Lovable 从 $17.5M ARR、$50M ARR 到 $100M ARR 的融资叙事，正处在这个资本机制里。对投资分析来说，这意味着要区分产品/组织质量和融资环境：估值上涨既反映真实 traction，也反映资本追逐 enterprise AI / AI application winner 的速度。

“现在的 consensus bet 是 enterprise AI，资本墙都涌进这里。所以一旦某个东西出现，并且数字让它变得明显可行，pricing 就会走到一个程度，基本上把 two-x best case 都定价进去了。你必须在它变明显之前到达那里，就是这么简单。你要找到那些还没完全浮出水面的市场和公司。等大家和你同一时间看明白时，可能就是十张 term sheets，赢起来很难。反过来，如果你能在 product-market fit 明显之前找到它，就能赢得更好、价格也好得多。市场对 consensus 已经 fully priced in、fully discovered。” —— Rory Driscoll / Jason Lemkin, 20VC Roundtable, 2025-07-24

## 大基金竞争让 AI 赢家融资更容易，也让早期投资人必须更早形成非共识判断

圆桌后半段虽然偏 venture ecosystem，但和 Lovable 这类高速 AI 公司相关：大基金有资本墙、新闻流、后续资金和品牌优势，对 founder 来说几乎都是好处；对小基金来说，热门共识轮很难打。这解释了为什么 Lovable 这样的公司一旦数字明确，会迅速吸引巨量资本，也解释了为什么真正有价值的早期判断要发生在数字完全显性化之前。

“关于大基金，几乎一切都对创业者有利。大基金做更多 deals，有更多 news flow，有更多好事发生；即使只是 index，如果一年做 30 个 deals，最后也会有持续的好消息流。资本墙给这些基金很多赢 deal 的优势：它们可以付更高价格，因为后面还有更多钱，这是一个 option；它们也可以付更高价格，因为钱就是更多。作为创业者，如果某个大基金愿意给我 50 on 250，我不会在乎它另外七个 deal 回报不好；我会想，我拿到了 50 on 250，我很开心。最终这个市场会由这些基金是否赚钱决定，但创业者没有 incentive 在这里叫停。” —— 20VC Roundtable, 2025-07-24
