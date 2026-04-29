---
company: midjourney
source_type: youtube
type: source_note
status: done
source_path: companies/midjourney/vault/youtube/transcripts/2026-04-21_The-Truth-about-Midjourneys-Discord-Server-I-was-VERY-w.md
source_title: "The Truth about Midjourney's Discord Server! (I was VERY wrong)"
source_date: 2026-04-21
created_at: 2026-04-22
speaker: "No Text To Speech / Midjourney volunteer moderator"
source_weight: B
relevance: high
quote_language: zh_translation_from_en_transcript
---

# Midjourney / Discord Server Correction — Source Note

## 这条材料的价值不在澄清八卦，而在暴露超大 Discord 的 onboarding 结构

视频作者一开始承认自己前一条阴谋论视频误导，把本条内容改成对 volunteer moderator 信息的更正；真正有价值的是，他解释了 Midjourney server 如何把新人分到不同 group，只让他们看到有限 newcomer rooms。对 Midjourney 的 community operating model，这说明服务器规模不是简单“一个大群”，而是用 group role 和房间可见性把 200 个 newcomer rooms 切成更可承受的入口，降低新用户被复杂社区吓退的概率。

“Midjourney server 非常独特，因为你加入服务器时会被分到不同 group；比如我看这个用户，他在 group four，这意味着他只能看到非常有限的一部分 newcomer rooms。我认为服务器里大概有 200 个 newcomer rooms，但因为这个产品被很多媒体宣传过，从 Daily Dose of Internet 到 John Oliver，很多不熟 Discord 的人都会进来，所以这个 Discord server 必须对新用户相对友好，这也是为什么他们让用户可见的频道更少。” —— No Text To Speech, YouTube, 2026-04-21

## David 不想处理投资人，成员数的价值更多是增长飞轮而不是融资展示

这条材料从 volunteer moderator 侧面确认了一个重要 operating signal：Midjourney CEO David 不想 deal with investors。作者自己的判断是，成员数确实有商业价值，因为“最大 Discord server”会带来认知、试用、25 个免费 credits 和订阅转化，但它不是为了欺骗投资人。这个区分很关键：Midjourney 的社区规模是 distribution asset 和 social proof，不是融资 KPI；这也和 bootstrapped、compute-first 的公司叙事一致。

“我被告知，Midjourney CEO David 不想处理投资人，因此那位 trial moderator 也试图告诉我，Midjourney 人为增加成员数其实没有什么好处。我的看法是，Midjourney 确实会从很多成员里获益，因为更多人会知道它：大家会说，哇，这是最大的 Discord server；随后更多人使用 Midjourney，先用 25 个免费 credits，最后可能购买订阅。所以我认为拥有大量 Discord 成员有内在好处，但不是为了愚弄投资人那一套。” —— No Text To Speech, YouTube, 2026-04-21

## 反 bot 策略的核心 tradeoff，是把加入摩擦降到奶奶也能出图，同时用内部系统控滥用成本

视频问到为什么没有传统 captcha / verification。Moderator 不能披露检测方法，但明确说不希望设置会让人难加入的门槛；同时 Midjourney 有自己的 bot 和 abuse detection，因为免费滥用会直接消耗服务器资源。这个细节把 Midjourney 的增长逻辑和成本逻辑放在同一张表里：低摩擦进入是消费级增长的前提，但每一次 abuse 都是 compute cost，所以系统必须在不破坏 onboarding 的情况下做风控。

“Volunteer moderator 说，他们不能谈具体检测方法，这也合理，因为你不会告诉别人你怎么判断 bot；但他们确实没有 Discord 上常见的那种传统 verification，而且他们真的不想要任何会让人更难加入的东西。原因也讲得通：如果你想让一个 Discord server 对所有人开放，就要尽可能简单，让奶奶也能上 Midjourney 生成漂亮的艺术图；同时 Midjourney 有自己的系统检测 bot 和 abuse，因为滥用 Midjourney 最终会让 Midjourney 花钱，别人是在免费使用并消耗服务器。” —— No Text To Speech, YouTube, 2026-04-21

## Midjourney 对 false positive 极度敏感，宁愿少自动封也要保护真实用户留存

关于 anti-raid bot，作者还原了服务器曾经启用、后来关闭 ban 功能的背景。Moderator 的解释是，服务器和普通 Discord 不同，false positive 是大担忧，团队希望真实普通人尽量少被移除和封禁。这不是普通 moderation 小事，而是 Midjourney 的 acquisition funnel：AI art 热潮带来很多非传统 Discord 用户，如果自动化防御误伤，会直接损害试用和转化；所以安全策略不能只追求“干净”，还要维护开放性。

“从聊天记录看，这确实是 Midjourney team 的一个 concern：他们不想要 false positives，bot developer 也说确实有风险，而 Midjourney 的整个 motive 是尽量让它对所有人开放，所以他们关闭了 ban 功能。Volunteer moderator 认为这个 bot 现在更多用于检查 suspicious users，也说早期确实用过；但他们这边没有 ban system，因为这个 server 和其他 server 很不一样，false positives 是很大的担忧，他们希望真实普通人被移除和封禁得越少越好。” —— No Text To Speech, YouTube, 2026-04-21

## David 选择 Discord 的哲学理由，是群体会让想象力从 dog 进化到 Aztec space dog

视频引用 The Verge 对 David 的采访来解释为什么不用独立网站。David 的核心判断是，大多数人单独面对“你可以想象任何东西”时不知道自己要什么；但在群体里，一个人的 dog 会被另一个人加成 space dog，再被加成 Aztec space dog。这里是 Midjourney 最强的 community insight：产品不是只帮用户表达已有意图，而是在公共空间里生成意图本身。Discord 因此不是 UI 过渡方案，而是创意学习和需求发现机制。

“David 在 The Verge 采访里的说法是：我们去年 9 月开始测试 raw technology，很快发现大多数人并不知道自己想要什么。你说，这里有一台机器，你可以用它想象任何东西，你想要什么？他们说 dog；你说真的吗？他们说 pink dog。于是你给他们一张狗的图片，他们说 okay，然后就去做别的事了。但如果你把他们放进一个 group，比如 Discord server，他们会说 dog，别人会说 space dog，再有人会说 Aztec space dog；在 community setting 里，人们会在彼此的想法上继续搭建。” —— No Text To Speech / David Holz via The Verge, YouTube, 2026-04-21

## Server group role 同时解决性能、可见性和新人体验，比简单清理 inactive accounts 更重要

作者追问为什么不定期 prune inactive accounts，moderator 的回答是：以前因 100 万 cap 需要清理，现在 Discord 提供后台基础设施，group role 系统也降低了性能和可见性压力。这个点让 Midjourney 的社区规模更可解释：服务器人数不是单纯实时活跃数，而是“尝试过这个 bot 的人”的累计入口；只要技术和 Discord 合作能承载，保留 inactive accounts 本身也有 social proof 和 reactivation 价值。

“我问 Midjourney 是否计划处理 inactive accounts，比如做 7 day prune；moderator 回答说，他们其实不知道现在是否还 purge inactive accounts，以前有 100 万成员上限时确实不得不清理大量账号。现在他们不担心基于 user count 的 server performance，因为 Discord 帮 Midjourney 做了后台基础设施工作，还有我前面讲的 group role system，让用户不会看到所有房间。” —— No Text To Speech, YouTube, 2026-04-21

## 560,000 个外部服务器说明 Midjourney bot 的分发不只在官方 server 内部

视频提供了一个很容易被忽略的 adoption signal：Midjourney bot 被加入到 56 万个 servers。官方 Discord 成员数可能混有 inactive、重复或免费 credit 规避，但 bot 被外部服务器加入，说明 Midjourney 的使用场景已经外溢到其他社区。对社区和增长分析，这意味着官方 server 是最大 onboarding 和展示场，但 Midjourney 的实际 distribution 还通过 Discord 的 bot architecture 扩散到大量小型群体。

“为了让你更满足一点，判断 Midjourney 是否人为 inflated，这里有一张 bot 所在服务器数量的图：它在 560,000 个 servers 里，这是非常多的服务器，而且这还是在 Midjourney 有很多限制的情况下，比如你的 server 超过 30,000 人好像就不能添加这个 bot。这样多的服务器也解释了为什么 Midjourney server 会有这么多成员；同时也要考虑，有些人可能自动生成 Discord accounts 来绕过 25 credit limit，但我看到他们似乎正在收紧这个问题。” —— No Text To Speech, YouTube, 2026-04-21

## Midjourney 是 Discord 的极限测试样本，平台伙伴关系本身也是增长基础设施

视频最后把 Midjourney 和 Discord 的关系讲成一种互相依赖：Midjourney 带来全网曝光，Discord 不希望新用户因为服务器容量上限被拒；同时 moderator 认为 Discord 可能把 Midjourney 当作超大服务器基础设施的 guinea pig。这个视角补足了 Midjourney 的 operating model：它不是单独承载 1800 万用户，而是借助 Discord 平台工程、容量特批和 bug 修复来扩张。平台依赖是优势，也是一种风险。

“有人会把 Discord 对 Midjourney 的特殊处理看成不公平，但如果从商业角度想，Midjourney 在全网获得大量宣传，而且它基于 Discord，Discord 公司最不想发生的事就是新用户因为看了 late night TV 或 YouTube 之后想加入，却被服务器容量挡在门外。所以 Discord 允许 Midjourney 拥有大量成员。我也和 moderator 聊过这个，他们说 Discord 很可能把 Midjourney 当成一点 guinea pig、一个小测试对象；服务器这么大确实有很多 bug，但希望 Discord 解决之后，其他大型 server 也能容纳更多人。” —— No Text To Speech, YouTube, 2026-04-21

## 这条更正视频反而证明，Midjourney 的规模已经大到会破坏普通 Discord 经验法则

作者承认自己最初用普通 server 的反 bot / 成员增长经验套 Midjourney，结果误判。Midjourney 的规模、AI art 的外部热度、Discord 的主流化、媒体曝光和 bot 可复制性叠在一起，形成了普通社区判断工具失效的场景。对后续研究，这条材料提醒：Midjourney 的社区指标不能按传统 SaaS 活跃社群看，也不能按普通 Discord 服务器判定真假；它更像一个消费级 AI 产品、社交学习环境和平台 stress test 的混合体。

“很多人觉得这个增长非常 suspicious；坦白说，我们过去判断一个 server 是否买了成员、是否 bot 化的那些 preconceived notions，在 Midjourney 这个规模下几乎不可能用了。它太大、太不规则，会打破我们平常的原则。要理解这件事，需要一点 food for thought：AI art 到处都很流行，Discord 也很流行，Midjourney 的增长注定会发生；这几乎是 perfect storm，而且 Midjourney 出图质量在我的体验里可能是最好的，人们喜欢大量细节。” —— No Text To Speech, YouTube, 2026-04-21
