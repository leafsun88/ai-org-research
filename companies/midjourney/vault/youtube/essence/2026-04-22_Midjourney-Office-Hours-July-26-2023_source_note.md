---
company: midjourney
source_type: youtube
type: source_note
status: done
source_path: companies/midjourney/vault/youtube/transcripts/2026-04-22_Midjourney-Office-Hours-July-26-2023.md
source_title: "Midjourney Office Hours | July 26, 2023"
source_date: 2023-07-26
created_at: 2026-04-22
speaker: "David Holz"
source_weight: A
relevance: high
quote_language: zh_translation_from_en_transcript
---

# Midjourney Office Hours | July 26, 2023

## Midjourney 把年度订阅现金流转成算力库存，这是一种很早期的基础设施优先经营法

David 开场先讲的不是某个模型功能，而是把年度订阅带来的现金提前锁定为未来一年的 GPU 供给。他把这件事说成公司当前的第一优先级：独立 web、独立 mobile、可靠 compute、成本优化、未来视频和 3D 都要建立在同一套长期平台上。这个细节对 Midjourney 很关键，因为它解释了为什么一家 bootstrapped 公司能在没有外部融资的情况下扛住生成式 AI 最贵的变量：它不是把收入立刻花在销售组织上，而是先买下供给侧确定性，让用户体验和模型路线不被 GPU 短缺牵着走。

“我们现在的主要优先级还是建设自己的平台：独立的 Midjourney web、独立的 mobile，并且投资更多服务器。我们觉得接下来一年会有很多 GPU 短缺，所以基本上是在拿年度订阅的钱问：用这笔已经确定的钱，能不能为下一年买下足够好的供给，让我们有快速而充足的 compute。长期看，我们想有自己的界面、可靠的算力，并且把基础设施优化到以后做 video 和 3D 时不用靠涨价来支撑。” —— David Holz, Midjourney Office Hours, 2023-07-26

## 从 Discord 走向自有 web / mobile，不是渠道迁移，而是产品控制权回收

这场 office hours 反复出现一个张力：Midjourney 仍然依赖 Discord 的交互和社区，但新功能发布已经会被 Discord UI 和移动端支持卡住。David 提到 inpainting 已经准备好，却因为 Discord 需要上线新的 UI 元件而拖慢；同时他又说团队正在投资 standalone web 和 mobile，让用户更容易进入 flow。这里的组织含义很直接：Discord 是早期分发和学习网络，但当产品进入更复杂的编辑、档案、搜索、支持和治理阶段，Midjourney 必须把核心界面收回到自己手里。

“inpainting 和更好的 styles 已经差不多准备好了，可能会作为 5.3 发出来；但这次又被 Discord 卡住了。我们在 Discord 里做 inpainting 的方式需要一些新的 UI，它们还没有发布，Discord 也在考虑是不是要先让 mobile app 支持，或者我们干脆关掉 mobile 版本、先做 desktop-only。我完全可以接受先发 desktop，如果这样能更快上线；只是这个 release 同时牵涉 Midjourney 和 Discord，所以拖得比我们这边需要的时间久很多。” —— David Holz, Midjourney Office Hours, 2023-07-26

## V6 延迟说明 David 的发布标准不是“比上一代好”，而是是否值得承受一次大迁移

David 说当时团队已经有比 V5 更好的版本，理论上随时能发，但他不想为了一个更像 V5.5 的进步承担 V6 这种大版本发布的复杂度。这个判断体现的是 Midjourney 的研发节奏：模型 release 不是简单的 benchmark 冲刺，而是产品、社区预期、迁移成本和长期质量曲线的组合决策。对于组织研究，这说明 David 会让团队在短期发布压力和长期模型质量之间反复校准，而不是用固定 roadmap 压研发。

“V6 还在继续推进，我们已经有比 V5 更好的版本了，所以如果想发，其实任何时候都可以发一点东西。但现在它感觉还不像真正的 V6，更像 V5.5；如果提升没有达到我们想要的幅度，我不知道是否值得经历一次大 release 的麻烦。我们还在做更多实验，既看低垂果实，也看更难的方向；这会花更久，但我们百分之百相信还可以好很多。” —— David Holz, Midjourney Office Hours, 2023-07-26

## Ranking 系统是 Midjourney 把社区行为转成模型改进的中间层

David 提到团队正在改 rank images，希望从用户排序里拿到更多数据，让算法和 ranking 本身变好。这不是一个边缘功能，而是 Midjourney 的核心组织机制：用户在 Discord 和网站上大量生成、比较、排序、反馈，团队再把这些行为变成模型迭代输入。Midjourney 的社区价值不只是增长，它还是研发数据系统的一部分；这也是为什么前端、社区、算法、moderation 不能被切成孤立部门。

“我们试着改了一些 ranked images 的工作方式，因为有机会从里面拿到更多数据；现在还不知道能不能成功，所以如果大家看到 rank image 有什么问题，请告诉我们。这个 ranking system 很实验性，但如果它跑得好，可能会同时改善算法表现，也让 ranking 本身变得更好。” —— David Holz, Midjourney Office Hours, 2023-07-26

## Front page 规则微调暴露了 Midjourney 对社区注意力的治理方式

David 说他们调整了 front page 规则，让同一个人的图片不能连续占据太多位置，原因是之前首页会被少数用户接管。这个细节很小，但它解释了 Midjourney 的治理哲学：生成社区的分发规则会反过来塑造用户创作、审美趋同和模型反馈。如果首页只奖励少数重度用户，社区会变窄；如果分发更多样，用户看到的可能性、prompt 学习路径和模型反馈都会变宽。Midjourney 的产品管理很大一部分是在调这种社区-审美-数据的闭环。

“我们稍微收紧了 front page 的规则，让你不会在首页看到同一个人的两张以上图片。之前首页有时会被少数人接管，现在结构上已经不可能了，我觉得这让 front page 更丰富。我们还在为未来版本做更复杂的首页算法，希望它能好很多；我们正在投入很多精力思考，怎样让人更容易探索其他人在 Midjourney 上做出的图片。” —— David Holz, Midjourney Office Hours, 2023-07-26

## Turbo mode 的讨论说明 Midjourney 在按“迭代速度”重构价格和算力体验

David 讲 turbo mode 时没有只说更快，而是在想不同用户愿不愿意用更少图片换更快反馈，尤其是锁定 seed 后快速试错。这是一个很 Midjourney 的产品问题：用户真正购买的不是单张图，而是 creative iteration 的速度、批量和成本结构。未来如果视频、3D、实时交互进入产品，Midjourney 的商业模式也会继续围绕算力单位和创作 flow 做更细的分层。

“我们在重新评估 turbo mode：是把速度做得更快但价格不变，还是给大家更多选择，比如同样价格下只出两张图而不是四张图，但速度更快。确实有一类用户不需要那么多图片，只想特别快地迭代，尤其是锁住 seed 以后，他们会希望用更少的图片换更快反馈。所以我们可能会推出更快的 turbo，也可能做一个和普通 job 价格类似、但图更少更快的 turbo 版本。” —— David Holz, Midjourney Office Hours, 2023-07-26

## David 对视频的判断很克制：先找到有限但好用的 moving image，而不是承诺完整电影

当用户问视频时，David 没有把愿景讲成“输入一句话得到一部猫电影”。他说视频很难，可能会有明显限制，但一个有边界的 moving image 仍然比没有好；Midjourney 会谨慎，因为团队标准很高，也担心做出一个少数人真正使用的功能。这个判断解释了 Midjourney 与很多追热点模型公司的差异：它不会只为了证明 capability 就发布，而是要找到与用户创作流程相容的交互形态。

“我们对 video 总体是谨慎的，因为要把它做好很难，但我觉得可以稍微作弊一下，找到某种好的 moving image。它可能不是你想要的一切，也很可能有明显限制；但一个有限制的视频，仍然比什么都没有好。大家不要期待输入一句‘我想要一部猫电影’它就直接给你，这不会发生；我们会很小心，因为我们标准很高，也不想做出一个其实没多少人真正使用的东西。” —— David Holz, Midjourney Office Hours, 2023-07-26

## Support 和 moderation 被 David 说成可积累系统，而不是人肉客服池

David 提到新的 help website、可搜索文档、非实时客服，以及每次回答新问题后把答案补进 FAQ。这条信息很适合放进组织分析：Midjourney 早期依赖 Discord 社区和人工 moderation，但规模扩大后，支持和治理必须从“回答当下问题”变成“每次回答都让系统更好”。他明确说当时 support 和 moderation 还不能随时间变好，所以系统化是优先级。

“我们也在做新的 help 网站，可能会是 midjourney.com/help 之类的东西，里面会有很多文档、好用的搜索；如果找不到答案，也可以联系 Midjourney 的客服拿到回复。它不会是实时的，我不觉得以我们现在的规模还能给几百万用户做实时支持；但我们会有团队回答问题，并且每当他们回答了 FAQ 里没有的问题，就把它加进去。我们想把 moderation 和答疑系统化，让它们随着时间变好，而不是像现在这样只是一直在那里、不会积累。” —— David Holz, Midjourney Office Hours, 2023-07-26

## API 被延后不是因为需求不够，而是因为 moderation 组织容量不够

David 说 Midjourney 暂时不做 API，核心原因是要先解决 moderation；一旦开放 API，公司就不只要管理自己的平台用户，还要管理 API 服务上发生的使用。这个回答把 Midjourney 的商业上限和组织瓶颈连在了一起：API 可能带来更大分发和收入，但如果治理系统没有规模化，它会把外部风险带进公司。Midjourney 的保守不是没有企业野心，而是知道治理能力追不上分发时，增长会变成负债。

“我们现在没有计划做 API。我觉得我们得先解决 moderation，因为一旦有 API，我们就不只是管 Midjourney 自己平台上的用户，还要去管 API service 里的使用；我们现在没有时间同时 moderation 这两边。如果以后有 API，我们也许会赞助 hackathon，但现在大概会先按住。” —— David Holz, Midjourney Office Hours, 2023-07-26

## David 仍然亲自做 office hours，因为社区连接本身是 Midjourney 的操作系统

这场 office hours 本来很短，David 身体不舒服，但他还是上线给更新、答问题、解释延期、收 bug 和想法。这个行为本身就是 Midjourney 的组织证据：创始人没有把社区沟通外包给 PR，而是把 product roadmap、模型限制、内容治理、计费、支持、审美方向都放进一个公开反馈场。Midjourney 的社区不是营销资产，而是创始人、用户和产品系统共享上下文的地方。

“今天我身体不太舒服，所以 office hours 会短一点；通常我会回答几个小时的问题，但这次可能更像 lightning round，大家在 chat 里丢问题，我就像 Twitch streamer 一样快速过一遍。虽然我想保存一点精力、喝点水，但还是想给大家更新我们在想什么、正在做什么，也回答一些问题。即使今天声音低一点，我还是来做 office hours，因为我希望它有帮助，让大家开心，也让大家觉得彼此连接着。” —— David Holz, Midjourney Office Hours, 2023-07-26
