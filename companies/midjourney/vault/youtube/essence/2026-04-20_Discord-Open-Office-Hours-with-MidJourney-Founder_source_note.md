---
company: midjourney
source_type: youtube
type: source_note
status: done
source_path: companies/midjourney/vault/youtube/transcripts/2026-04-20_Discord-Open-Office-Hours-with-MidJourney-Founder.md
source_title: "Discord Open Office Hours with MidJourney Founder David Holz 9/7/22"
source_date: 2026-04-20
created_at: 2026-04-22
speaker: "David Holz"
source_weight: A
relevance: high
quote_language: zh_translation_from_en_transcript
---

# Discord Open Office Hours with MidJourney Founder David Holz 9/7/22

## Midjourney 早期最真实的组织状态，是 10 人团队同时背着模型、社区、网页和 moderation 的多线程压力

这场 office hours 最有价值的不是某个单点功能，而是 David Holz 对团队负载的裸露描述：公司只有约 10 人，却同时要修当前 test 模型、推进从头训练的下一代模型、做 web flow、组织流、网页创作体验、Discord 社区稳定性和内容安全。Midjourney 的早期组织不是清晰职能分工后的产品机器，而是 founder 直接把技术路线、用户反馈、社区治理和商业约束揉在一起做取舍；这解释了它为什么能快，也解释了时间表为什么经常不确定。

“我们现在大概只有 10 个人，所以有时候真的很挣扎；一边要把当前系统调好，一边要准备下一代系统，还要分心做网页功能、组织流程、网页创作流程和一些还不能讲的新功能。问题不是我们不知道方向，而是内部同时有很多东西都看起来又热、又好、又重要，我们很难把自己砍到更少的事项上。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## V3 的 vibey 和 test 模型的 realism 被 Holz 当成两套未合并的产品能力

Holz 对模型状态的解释很具体：V3 更艺术、更 vibey、更懂词；test 系列更真实、知识更多，但读词顺序和权重不稳定，容易重开头轻结尾，且速度、batch size、aspect ratio 都有约束。这个判断说明 Midjourney 并不是简单追求 photorealism，而是在同时优化语言理解、审美、速度和可控性。它的产品难点是把不同模型的优点合成一个默认体验，而不是给高级用户堆一排参数。

“现在我们处在一个很有意思的中间地带：V3 很艺术、很有 vibe，也很理解你的词；这些 test 算法更真实、知识更多，但它们不一定会好好读词，可能只抓一个词，或者更关注开头的词而忽略后面的词。它们也更慢，不太能做大 batch 或大宽高比，所以我们对这个状态并不满意。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## 下一代模型被稀缺 AI mainframe 卡住，Midjourney 的路线图天然带硬件供应风险

这条材料把 2022 年 Midjourney 的算力约束讲得很直：他们在实验性的大型 AI mainframe 上训练下一代系统，机器会下线、驱动会更新、代码会突然失效。这里的投资含义是，Midjourney 的质量跃迁和发布时间不只由团队执行力决定，也由外部稀缺算力栈的稳定性决定。早期 AI 应用公司的 roadmap，其实很大一部分暴露在底层硬件和训练平台的不确定性里。

“我们很多下一代版本会好很多，但它们是在这些巨大的 AI mainframe 上训练的，而这些机器现在很实验，可能会被拿下线。我本来希望几周前就拿到结果，但 mainframe 下线了，后来他们更新了驱动，我们的代码又不能跑了；在这种从来没人真正用过的大机器上训练，我们会受制于稀缺资源的上下线。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## Holz 把当前 Discord 体验称作教程，真正的产品边界会从 text-to-image 扩到更高级创作工具

Midjourney 当时的默认入口还在 Discord 里，但 Holz 已经把它看成未来一两年更大体验的 tutorial。他提到 specialized model、web creation flow、organization flow、打破传统 text-to-image 的新功能，以及独立 web experience。这个信号说明 Midjourney 的产品野心不是停在 prompt bot，而是把“生成图片”推进到更完整的创作工作台，Discord 先承担用户增长、社区学习和实时反馈，web 则承接更个人化、更结构化的生产流程。

“我觉得现在的 Midjourney 体验在很多方面只是接下来一两年真正会发生的事情的教程，像一个很 intense、很 amazing 的视频游戏的入门体验。我们想做更多高级工具，想展示 specialized model、网页创作流程、组织流程，以及一些跳出传统 text-to-image 的东西，让大家开始感觉到这个东西到底会往哪里去。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## 150 万 Discord 社区不是增长指标而已，它直接变成产品和治理实验场

Holz 说 Discord server 已经到 150 万，并且成为全世界最大的 Discord server，未来可能一个月内再放大五倍。这个数字在组织分析里不只是用户量，而是一个前所未有的实时创作社区：它提供 prompt、rating、审美反馈、bug 暴露、moderation 压力和产品想法。Midjourney 的特殊性在于，模型不是在安静的 SaaS dashboard 中使用，而是在一个超大公共空间里被学习、模仿、扩散和调校。

“Discord server 已经到 150 万了，我们现在是世界上最大的 Discord server，而且很快可能比后面几个最大的加起来还大。随着服务器变大，事情会变得有点奇怪，因为 Discord 也没有见过这么大的社区；如果有人知道怎样让一个巨大 server 变得更好，请把想法丢到 feedback channel，我们真的会读。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## 内容治理被 Holz 讲成 feedback loop 管理，而不是道德口号

Midjourney 对 porn、gore、front page 的治理逻辑很清楚：平台允许什么，什么就会形成反馈回路，进而驱逐另一批用户。Holz 不把 moderation 讲成抽象价值观，而是讲成 social system design：如果色情、血腥或 shock image 变成最强反馈回路，社区会被它们主导。Midjourney 的定位因此更像“安全的通用艺术探索空间”，把成人内容或极端冲击内容留给别人做。

“我们必须非常小心 feedback loop，因为如果有人做很血腥的内容，所有喜欢血腥的人都会来，然后大家都在做 gore；色情也是一样。很多社交网络会被它们允许的反馈回路主导，我们不想让这个系统被最糟的反馈回路主导。总有人会做 AI porn 服务，但我们更想做一个安全空间，聚焦一般性的艺术探索。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## Midjourney 的 moderation 路线不是更多禁词，而是让模型学会边界

Holz 明确说理想状态是几乎没有 word filter，除了 slur 这类词之外，用户语言更自由，但图像输出本身不越界。这把 moderation 从规则表推向模型行为：系统要理解 nudity vs pornography、blood vs gore、art vs shock image 的细粒度差别。对 AI 组织来说，这意味着 trust & safety 不是外部审查层，而会进入模型训练、审美调优和数据标注本身。

“目标应该是几乎没有词过滤，除了 slur 之类的词以外，你可以有语言自由，但图像仍然不会变成冒犯性的东西。比如你要求 nude person，它可能会做裸露感，但用树枝或物体挡住关键部位；它可以有 blood，但不做 gore。我们需要让系统学会这些细微差别，随着它学得更好，过滤就能慢慢放松。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## 付费模型会向两端分叉：让付不起的人进来，也让大预算项目花得出去

Holz 对 pricing 的解释透露出 Midjourney 的商业模型雏形：中间价格段不是重点，重点是两端，一端是让真正付不起的人通过 gift、free hours、rating 或数据贡献进入平台，另一端是让有大项目和大预算的人更顺畅地消费。这个思路把社区增长、数据标注和商业化绑在一起；免费或低价用户不是纯补贴对象，而可能通过 rating 和 feedback 改善模型。

“我看定价大概有两个极端方向：一边是怎样让真的付不起钱、甚至没有信用卡的人也能进平台；另一边是怎样让那些有无限预算的人更容易、更高效地花钱。中间那种帮某个人省四美元的事相对没那么重要。等我们有更好的数据管线，也许会让一批用户免费使用，交换条件是持续帮我们做有用的数据和 rating。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## 计算成本下降会带来便宜版和昂贵版，但 Holz 仍把 $30 flagship 定位成质量优先的主产品

这场问答里，Holz 已经预期未来会出现 20 美元限制版、60 美元甚至更高价位的 plan：便宜版限制算法，贵版接入更昂贵的新能力。但他反复强调用户调查显示大家更想要“同价更好”，不是“更便宜但更弱”。Midjourney 的商业判断很明确：它不想做低价 commodity image generator，也不想只服务顶级预算，而是做普通人能负担的高质量 flagship。

“某个时候定价会分叉：可能有 20 美元计划，只能用某些更便宜的功能；30 美元计划继续加入越来越昂贵的东西；以后也可能有 60 美元或更高的计划。我们会尽量在现有价格点给大家越来越好的东西，同时增加更贵和更便宜的计划。每次我们问用户是想更便宜还是同价更好，大家总是说想在同样价格下变得更好，所以质量仍然是第一优先级。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## Midjourney 当时已经在用租赁 GPU 扛起 1 亿美元级算力，云端体验压倒本地化诉求

Holz 说 Midjourney 可能运行在 1 亿美元甚至更多的 GPU 上，且当前 upscaler 需要 37GB VRAM，消费级显卡无法运行。这个信息把 Midjourney 和开源本地模型的路线差别讲透：它不是要优化给 3000 美元显卡的发烧友，而是把最强模型、batch 并发、队列和存储做成普通电脑也能用的云服务。云端集中算力不仅是商业模式，也是用户体验本身。

“我们现在用的 GPU 太多了，Midjourney 可能跑在 1 亿美元的 GPU 上，可能还更多；好处是我们买不起 1 亿美元的 GPU，但租得起。比如我们的 upscaler 需要 37GB VRAM，消费者显卡根本跑不了；就算低分辨率能本地跑，也会慢，只能一张一张做。我们更想为普通电脑的人优化，让他们用很便宜的方式得到最好的体验。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## Holz 把模型质量定义成 craftsmanship：两三个词也要漂亮，背后是大量人工看图和调参

Midjourney 的审美优势不是 Holz 口中的“模型自然会好看”，而是团队把 craftsmanship 放进核心 engine：发布前看上万张图、跨上千 prompt 比较细节，让用户只输入两三个词也能得到漂亮结果。这里的组织信号很重要：Midjourney 的 moat 不只是训练数据或算力，而是 founder-led 的审美调参能力，团队在模型后面做的是把普通扩散模型从 generic Google image 推向 beautiful / transcendental。

“我们真的很关注质量和细节。很多人低估了这一点，但 craftsmanship 的意思就是细节重要；你们在 craft 图像，我们这边日夜把 craftsmanship 放进核心 engine。任何东西发出来前，我们会在每个模型上看大概一万张图，跨上千个 prompt 去看；对我们来说，两三个词放进去就看起来漂亮，这件事非常重要。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## Quantitative aesthetics 是 Midjourney 的内部科学：美、创造力、清晰度和一致性都被当成可调变量

Holz 花了很长时间解释“美”并不完全主观：花朵对昆虫和人都美，说明自然中存在 shared aesthetics；同时个人审美、创造力和一致性之间又有 trade-off。这个视角解释了 Midjourney 为什么会比单纯复现照片的系统更重视调性。它的核心研究不是“dog 像不像 dog”，而是怎样让模型理解什么更美、什么更有创造力、什么更 coherent，并在这些目标之间做取舍。

“我们真的在尝试理解美学和创造力的更深层性质：什么让东西美，什么让东西有创造力，什么让东西 coherent 和 clear，这些东西之间有没有 trade-off。很多人觉得美完全相对，但我不认为完全如此；花为什么对蜜蜂美，也对我们美？自然里似乎有一种 shared aesthetics，同时又有个人审美，这些都需要被理解。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## Community tuning 让用户不只是消费者，而是审美模型的训练者

Holz 提到他们越来越难只靠内部判断哪个版本更漂亮，因为很多图都已经很好；下一步可能让社区直接 rating 不同系统版本，甚至逐渐把 tuning 交给社区自动完成。这是 Midjourney 最核心的组织-产品耦合：社区不是营销渠道，而是审美数据层。用户通过生成、点赞、模仿、rating，把 collective taste 写回模型，形成一个高速共演化系统。

“我们现在已经到一个阶段，很多图都太漂亮了，连我们自己都有点难判断系统应该往哪边调。所以可能会把一部分交给社区，让大家 rating 不同版本生成的图片，帮助 steer 系统 tuning；现在我们也用社区数据，但通常还是我们先看、再调 knob、再 push。未来有一条路是它几乎完全自动，社区自己持续调系统，我们把手从方向盘上拿开。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## Holz 不把 AI 当艺术家，而把它当成会塑形的自然流体，故事和情绪仍来自人

在“AI 是否有创造力”的长回答里，Holz 的哲学很稳定：AI 可以把 cyberpunk 和 onion 混合，这是组合式创造；但它没有故事、情绪、意图或内在想法。这个判断把 Midjourney 的产品定位锁定为 extension of mind，而不是替代艺术家。它解释了为什么公司会回避“AI artist”叙事，也解释了为什么它重视 user expression、故事和审美边界，而不只追求自动生成。

“一个艺术家不是图片来源而已，艺术常常关于故事和情绪，而这个系统内部没有故事和情绪；那些来自你。我更愿意把它看成一种会做出美的画笔，或者像水流一样，你把石头丢进河里，河会塑形，石头也许很美，但水没有意图、信念、想法或意志。它能混合概念，能塑形，能产生美，但它不是一个有故事要讲的东西。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## Midjourney 的数据分工很清楚：互联网教概念，用户教什么值得看

当用户问是否会用生成图片训练新模型时，Holz 说生成图不会用来教模型“猫是什么”，因为概念来自互联网；用户数据主要教模型 beauty、creativity、expression 和 people actually want。这个分工很关键：Midjourney 的闭环不是让模型吞自己的输出，而是用用户行为学习偏好、审美和成功样式。这也解释了为什么 community rating、style exploration 和 feed 结构会直接影响模型质量。

“图片本身来自互联网；用户生成的图主要不是用来教它猫是什么。如果系统已经能画猫，它不需要再看自己生成的猫来学习猫；但如果有某张猫的图片大家都特别喜欢，那就教会它一些东西。所以互联网教它概念，用户更多是在教它 beauty、expression，以及人们真正想要什么。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## API 和 Photoshop plugin 会等到 Midjourney 有足够强的工作流能力，而不是为了生态叙事先开放

关于 Photoshop plugin 和 integration，Holz 的回答说明 Midjourney 对 API 很谨慎：他们知道未来要让别人做 integrations，但不会简单丢一个 API 让生态自行粗糙生长。只有当新功能在专业 workflow 里足够有价值，第三方才能做出“世界上最好的 Photoshop plugin”。这是一种 product-first 的平台化路径，先把核心能力做到足够强，再开放集成。

“某个时候我们会提供一种方式，让别人可以做 Photoshop plugin 这类 integration，而不一定要我们自己做；也可以是 After Effects 或非 Adobe 的东西。但如果我们现在只是做一个 API，我不确定大家会立刻做出最好的东西。我们正在做很多对专业 workflow 越来越有意思的新功能，然后再想象不同 integration 由谁来做、怎样让别人做。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## 可控性不能以变丑为代价，Holz 更想做 composition / color / character anchors

用户提到 sketch-to-image 和 image-to-image 时，Holz 的核心原则是：控制力要让结果更好，而不是让人更容易生成变差的图。他偏好的方向是 anchors：用一张图锚定构图、另一张图锚定颜色、另一张图锚定角色，再用文本指定场景。这比简单把鼠标画的草图塞给模型更接近 Midjourney 的产品哲学：保留用户意图和物理感，同时不牺牲美学质量。

“我们确实想做对会画画的人、对艺术家更好的工具，但现在很多 image-to-image 的结果总体会变差；如果一个人多花一点时间用词来做，可能反而更漂亮。我的问题是，怎样增加 controllability 但让图更好，而不是更差。我更喜欢 anchors 的方向：这张图锚定构图，那张图锚定颜色，这张图锚定角色，然后你说我要把它放在沙漠里。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## Holz 的最终界面想象不是 prompt box，而是重新变得 physical 的创作工作室

Midjourney 早期体验很“脑内”和“非物理”：用户在 Discord 输入文字。Holz 对未来的想象却很 physical：像做饭、像在工坊、像在艺术家 studio，甚至不排斥硬件、AR/VR、投影和新设备。这个信号对组织研究很重要：Founder 并不满足于网页工具或 bot，而是在思考 AI 创作怎样重新获得人类身体感。Midjourney 的长期路线可能会从软件工具走向创作环境。

“我强烈想走向第二种未来：艺术家的 studio 不应该只是键盘和显示器，而应该仍然像一个物理空间，人们在里面做美的东西。我不确定是 AR 眼镜、投影、新物件还是硬件；我以前做过硬件，所以如果 Midjourney 持续增长，我完全愿意做 Midjourney hardware，把艺术工作室变成很多对象、物理东西和新设备组成的空间。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07

## Onboarding 的真正瓶颈是学习语言和反馈循环，不只是多写文档

一个新用户从卡车驾驶室里讲自己的学习过程：免费额度很快烧完，复制优秀 prompt 也复现不了，因为参数没复制，手握剑这种失败不知道是 prompt 问题还是模型限制。Holz 的回应把 onboarding 重点放到 prompt craft、可搜索图库、预渲染词库、学习风格词和社区互助。Midjourney 的教育产品其实是创作基础设施的一部分；当用户越多，帮助他们学习词、风格和模型边界会变成留存与付费的核心。

“我们确实要想办法让人更容易学习。现在最好的建议是去 prompt craft 这些频道，问大家这个东西怎么做，常常会有人刚好很会做 sword 之类的题目。我们也想提前渲染很多图片，做成一个免费看的 library，让你不用自己生成就能看不同词会怎样影响结果；用户 gallery 也能帮忙，但现在还有点慢。提醒得很好，学习本身就是体验里很大的一部分。” —— David Holz, Midjourney Discord Open Office Hours, 2022-09-07
