---
company: Midjourney
research_key: MIDJOURNEY
type: youtube_essence
source_transcript: /Users/leafsun/Desktop/AI Org研究/companies/midjourney/vault/youtube/transcripts/2026-04-20_Discord-Open-Office-Hours-with-MidJourney-Founder.md
source_type: youtube
source_title: "Discord Open Office Hours with MidJourney Founder David Holz 9/7/22"
source_url: https://www.youtube.com/watch?v=k_gKFwF_q4o
source_date: 2026-04-20
original_event_date: 2022-09-07
relevance: high
status: v2_sample
generated_at: 2026-04-21
style_reference: 学习/style_references/anthropic_org_investment_style_notes_2026-04-21.md
---

# Discord Open Office Hours with MidJourney Founder David Holz 9/7/22

这条材料最值得保留的地方，是它把 Midjourney 早期的 operating system 露出来了：Founder 每周直接站在 Discord 社区里讲模型路线、时间表、内容治理、web 体验和用户学习问题。它不是一场普通 AMA，更像一个公开产品会。David Holz 在这里扮演的不是 CEO 公关角色，而是 roadmap owner、community moderator、model taste judge 和客服升级队列的最终节点。

## Office hours 是 Midjourney 的产品管理界面

Midjourney 早期没有把产品管理藏在内部会议里，而是把相当一部分 product review 放进 Discord office hours：David 先讲团队在想什么、在做什么、哪些东西可能会来，然后用几个小时接用户问题。这种 cadence 很粗糙，但对一个 image model 公司很有效，因为用户的痛点通常不是抽象需求，而是非常具体的 prompt、风格、审核、速度、学习成本和失败案例。Founder 每周直接听这些问题，等于把 roadmap、support、community sentiment 和模型缺陷放在同一个现场处理。

“we do this every week” —— David Holz, Discord Office Hours, 2022-09-07

## 10 人团队的真正压力，不是便宜做人，而是同时押太多正确方向

David 当时讲得很诚实：团队一边想修现有 test models，一边想推下一代系统，一边还有 web flow、organization flow、specialized model 和社区稳定性。小团队带来的好处是 context loss 很低，坏处是所有方向都看起来重要，最后时间表会天然变得不稳定。Midjourney 的组织不是传统产品公司那种季度 roadmap 机器，更像一个 frontier lab 加社区产品混合体：方向判断在 Founder 脑子里高速排队，团队用很少的人去追多个技术窗口。

“we’re only around 10 people” —— David Holz, Discord Office Hours, 2022-09-07

“12 things at the same time” —— David Holz, Discord Office Hours, 2022-09-07

## Midjourney 的模型判断一直围绕 taste，而不是只追 realism

这段里 David 对 V3 和 test algorithms 的比较很关键。V3 被他说成 artistic、vibey、understands your words；test algorithms 更 realistic、更有 knowledge，但读 prompt 的能力更差，容易只盯一个词、忽略后面的词，而且 less vibey。这个 trade-off 解释了 Midjourney 为什么长期给人一种“审美默认值更强”的感觉：它不是单纯把图做得像照片，而是在模型能力、prompt understanding、艺术感和可控性之间找默认平衡。对 Midjourney 来说，default aesthetic 本身就是产品能力。

## 算力不是后台资源，已经进入产品节奏和组织焦虑

David 提到下一代模型要在 big AI mainframes 上训练，但这些机器本身是 experimental scarce resource，会下线、换 driver、让代码突然不能跑。这里能看到一个很早期的 AI 公司现实：产品发布节奏不完全由 PM 或工程排期决定，而是由算力、底层 driver、训练稳定性和模型路线共同决定。Midjourney 的小团队可以很快做判断，但它依赖的基础设施仍然会把确定性打碎。

## Discord 从分发渠道变成社区实验场

Midjourney 当时已经是 Discord 上最大的社区之一，David 明确说随着服务器继续变大，团队进入了 Discord 自己也没怎么见过的 territory。这个点很重要：Discord 对 Midjourney 不是一个尴尬的临时入口，而是增长、用户教育、反馈、moderation 和社群文化的共同容器。越多人在同一个空间里生成、展示、模仿和争论，模型产品越容易形成 shared taste；同时，治理难度也会同步放大。

“biggest discord server” —— David Holz, Discord Office Hours, 2022-09-07

## 用户教育是产品本体，gallery 和 prompt copy 都是学习系统

后半段有个用户提到：他在 gallery 里复制别人 prompt，却因为 flags 没复制完整，得不到同样结果。David 的反应不是把它当边缘 bug，而是承认学习体验本身很重要。Midjourney 的核心使用门槛不是按钮复杂，而是用户要理解词、参数、风格和模型随机性如何共同影响结果。gallery、library、prompt copy、社区问答都在承担同一个任务：让用户更便宜、更顺滑、更有乐趣地学习如何和模型协作。

“experience is just learning” —— David Holz, Discord Office Hours, 2022-09-07

## 个性化不能把 imagination 训练窄

一个用户用 Pandora 和 YouTube 举例，说可训练算法很容易把自己越训越窄，最后只剩一小片内容。David 认可这个风险，并说团队已经见过类似情况。这个回答很能说明 Midjourney 的 personalization 难题：模型要学会少做 bad things，但不能只做 one good thing；它要记住用户偏好，也要不断把 crazy and new things 推回系统。对一个创意工具来说，推荐系统如果只优化满意度，很快会杀掉探索性。Midjourney 要做的个性化，其实是“带人离开审美舒适区”的个性化。

## 这条材料后面应该这样用

写 Midjourney 组织分析时，这条 source 应该优先服务三个判断：第一，David 的 founder mode 不是强管控，而是把社区反馈、模型路线和产品节奏收在自己身边；第二，小团队是 Midjourney 的速度来源，也是 roadmap 不稳定的来源；第三，Midjourney 的核心产品不是 image generation API，而是一套围绕 taste、learning、community 和 exploration 的创作系统。旧 essence 把这条材料压得太像摘要，真正值得保留的是这些机制。
