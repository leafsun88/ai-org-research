---
company: midjourney
source_type: youtube
type: source_note
status: done
source_path: companies/midjourney/vault/youtube/transcripts/2026-04-21_Midjourney-Get-started-with-MidJourney-and-Discord---In.md
source_title: "Midjourney! Get started with MidJourney and Discord -  Interviewing Gailya"
source_date: 2026-04-21
created_at: 2026-04-22
speaker: "Scott Detweiler / Gailya"
source_weight: B
relevance: medium
quote_language: zh_translation_from_en_transcript
---

# Midjourney / Scott Detweiler 2026-04-21 — Source Note

## Discord 是 Midjourney 早期增长入口，也是真实新手的第一道产品摩擦

这条访谈的价值在于 Gailya 不是 AI power user，而是专业摄影师和 Discord 新手。她的困惑很具体：官网看起来像独立网站，却要求 Discord 登录；她以为自己在订阅一个聊天软件；fast / relaxed mode 和图片额度让第一次付费认知变得混乱。Midjourney 早期把 Discord 当作 front end，降低了自己搭完整社交产品的成本，也借用了现成社区分发，但代价是把“学习 Discord”变成“学习 Midjourney”的前置条件。

“我以前的在线聊天经历大概是 AIM、MySpace、Facebook，也玩过一些游戏，但 Discord 出现的时候我已经是成年人、有工作了，所以中间有一个 gap。到最近为止，我以为它只是一个有不同频道的聊天平台；我去找 Midjourney 时，官网看起来像它自己的网页，我没看出这必然是 Discord，然后它要我用 Discord 登录，这让我很困惑。接着它又像是订阅，我就在想，我是在订阅一个聊天吗？为什么又只能用这么多图片，还有 fast 和 relaxed mode？我只是想看一些很酷的图片。” —— Gailya, YouTube, 2026-04-21

## 公开 prompt 流既是学习机制，也是创作者隐私和原创感的冲突来源

Scott 解释 Midjourney 公共频道时，核心不是单纯展示社区热闹，而是展示一个独特的 adoption loop：用户能看别人作品、看别人 prompt、借用 prompt 学习模型语言。这个机制对新手很有用，却天然触发创作者的不适，因为 prompt 被视为“prompt wizardry”和个人诀窍。Midjourney 因此形成了一个付费 privacy upsell：默认公共学习，想隐藏作品和 prompt 要进入更高 tier 或 private mode。

“如果你在 Midjourney 的 general areas 里，你可以看到别人的作品和别人的 prompts；Midjourney 会让 prompts 公开，所以你可以去借别人的作品，如果你想的话。这很有意思，但也会让很多人生气，因为那其实还不完全是他们的作品，更像是他们的 prompt wizardry，是他们学会按自己方式写 prompt 的能力。我的第一反应也会是，我不想所有人做出和我一模一样的图，所以我理解这种感觉；因此也有 private mode。” —— Scott Detweiler, YouTube, 2026-04-21

## Seed 和 job ownership 暴露了 Discord-native 交互的复杂性，复现能力被藏在 emoji 工作流里

访谈里关于 seed 的解释很能说明早期 Midjourney 的产品形态：想复现别人的结果，不能只是复制 prompt，还要拿到 seed；想拿 seed，要给 Discord 消息加 envelope emoji。这个能力很强，但交互非常“Discord 原生”，对普通创作者并不直观。更重要的是，Scott 提到 job ownership 不能共享，说明协作和可复现 workflow 仍然受限；Midjourney 当时更像个人实验台，而不是团队协作工具。

“如果你喜欢这张图，想继续拿它工作，现在不能真正共享 job ownership，但我们可以接近它；这也是 Midjourney 不太清楚的一点，因为它基于 Discord，也基于 emojis。你到 emoji 这里给这条结果发一个 envelope，它会回我这张图用的 seed；然后我就可以写 standing in a field of flowers，再加上 seed 和那个数字，系统就会用同一个 random seed 去生成。复制同一句 prompt 不会自动得到同一张图，因为 reroll 会用不同的 noise generator。” —— Scott Detweiler, YouTube, 2026-04-21

## 高阶用户会把个人偏好固化成默认参数，Midjourney 的使用会从“学命令”走向“搭个人创作环境”

Scott 用 `prefer suffix` 固定 2:3 aspect ratio，是一个很小但很有用的 adoption detail。它说明 Midjourney 的 power user 会逐渐把重复参数沉淀成默认环境，而不是每次手写命令。对摄影师来说，2:3 对应 Sony A7R4 的画幅，比默认方图更自然；这种个人化设置让 Midjourney 更接近专业工作台。产品含义是：prompt tool 一旦进入专业 workflow，默认参数、可保存偏好和项目级设置会变得和模型质量一样重要。

“我觉得 Midjourney 默认的 square aspect ratio 很难用，我不是很喜欢；我用 portrait 或 2x3 aspect ratio，和我的 Sony A7R4 一样，因为这对我更自然，也更符合我要走的方向。你会注意到我没有在每一个 prompt 后面都输入它，因为可以用 prefer suffix，然后给它 options，比如 ar 2:3；如果你更偏 landscape，也可以用 3:2。这样它会自动加到每个 prompt 末尾，你不用每次都担心。” —— Scott Detweiler, YouTube, 2026-04-21

## Fast / Relaxed mode 是 Midjourney 的核心经济界面，但新手会被套餐边界和手动切换绊住

Gailya 问一组四宫格算一张还是四张，Scott 又解释 `info`、fast hours、relaxed mode、max upscale 必须切回 fast。这些细节说明 Midjourney 的成本模型直接进入用户界面：用户不是只在付费页理解套餐，而是在每次生成、排队、升级分辨率时被提醒 compute 是有限资源。这里的摩擦也很明确：如果某个操作必须 fast，产品却不自动切换，用户需要学会 slash command 级别的状态管理。

“如果你想知道自己用了多少，随时可以输入 info，它会告诉你；比如我还有 917 images 或 15.5 CPU hours，但我大多数时候在 relax 里工作，所以 relaxed mode 不会消耗 fast hours。Gailya 也提到，只有更高 membership 才能用 relax，10 美元 basic plan 基本只能用 fast。还有一个痛点是，如果你要把图 upsize 到 maximum resolution，就必须在 fast 里，但它不会自动帮你切换，所以你得输入 slash fast 再继续；我批评过这一点，如果某件事要求 fast，就请自动帮我切到 fast，然后再切回 relax。” —— Scott Detweiler / Gailya, YouTube, 2026-04-21

## Relaxed mode 把生成从即时反馈变成排队式创作，适合专业用户“挂任务再回来挑”

Scott 对 relaxed mode 的使用方式很像专业创作者的 batch workflow：排三四个任务，离开，过十分钟或午休后回来挑选。这个细节对理解 Midjourney 商业化很重要。无限 relaxed mode 的价值不在“快”，而在让用户摆脱每张图都计费的心理负担，进入长期探索状态；当用户把工作变成 queue management，Midjourney 甚至可以用更深队列继续收费。

“我通常会 queue 几个任务，好像能排三四个，或者三层深，然后我就走开，之后再回来看看。一天里有些时候它可能要等十分钟，但我不太在意。有人说他们也许会用更多钱提供更深的 queue，因为很多人喜欢把工作排进去、走开，几个小时后回来；如果你有正常工作，可以下个 break 或午饭时回来看看发生了什么，给它更多指令，然后一天结束再回来。” —— Scott Detweiler, YouTube, 2026-04-21

## 专业摄影师把 Midjourney 当作 ideation 和 photo-bashing 起点，而不是直接替代交付品

访谈里最有用的职业 adoption signal 是：Scott 和 Gailya 都没有把 Midjourney 当成“替代摄影”的简单结论，而是把它放进构图草稿、创意阻塞、Photoshop / Corel Painter / 3D background / photo-bashing 的链路里。AI 生成不是终点，而是补足摄影素材库里“缺一个世界、缺一个背景、缺一个方向”的部分。这个 workflow 说明 Midjourney 对专业创作者的真实价值可能是扩大前期探索和后期合成空间，而不是立即吃掉拍摄收入。

“我把它当成很棒的 brainstorming tool。以前如果有 idea block，要在纸上画 thumbnail、找构图、找粗略想法；现在如果我没灵感，就进 Midjourney 随便输入一些东西。Gailya 也说，她会提前 sketch 一个创意拍摄，现在可以把那些想法放进去，得到一个很好的视觉参考，看看光应该从哪里来、它可能是什么样子。对我来说，这不是替代最终作品，而是从这些图开始，再把我的摄影加进去做 photo bashing，Photoshop skills 反而变得非常重要。” —— Scott Detweiler / Gailya, YouTube, 2026-04-21

## 所有权和商业条款是 adoption 的隐性门槛，创作者需要知道“你拥有图像”并不等于平台完全放弃权利

Scott 对 ownership 的解释显示，Midjourney 用户很快会进入版权、商业授权、企业条款的灰区。平台把规则调整成用户拥有生成图像，但 Midjourney 保留使用、修改、分发等权利；达到较大收入规模的公司还需要 corporate agreement。这不是法律细节，而是 adoption friction：摄影师、设计师、品牌和 NFT 卖家在真正商业使用前都需要把权利边界弄清楚。

“Midjourney 很聪明地改变了 ownership 的方式：现在你拥有自己创建的图像，不过 Midjourney 仍然保留对这些图像进行使用、修改和处理的权利，而且是持续的。现在更像 stock photography 的情况，你拥有自己上传的 stock photo，但平台也可能把它用于营销等目的。这里包含商业 release，但如果你是更大的公司，年收入达到某个规模，就必须和他们签 corporate level agreement，所以这里确实有 caveats。” —— Scott Detweiler, YouTube, 2026-04-21

## Midjourney 的网页 app、community feed、dictionary 和 ranking 把社区学习、发现和模型训练连在一起

Scott 后半段展示 `midjourney.com/app`、community feed、map、dictionary、styles、ranking，这些不是简单功能清单。它们把用户作品管理、prompt 学习、相似创作者发现、审美投票和额外时长奖励放到一个循环里。用户通过 rating 获得更多时间，平台通过 rating 学习什么是好脸、好手、好 prompt 对应；这是一种把社区劳动产品化的机制，也解释了 Midjourney 为什么早期高度依赖公开社区而不是封闭单机工具。

“每个人都有自己的 Midjourney app page，登录 Discord 后可以看到自己的页面，用来找图、看 prompt、复制 prompt 或 job id。更有意思的是 community feed，你可以看到社区里正在做什么，也可以直接复制 prompt；Midjourney 也在说，去复制、偷、借别人的 prompt，学习引擎怎么工作。还有 ranking，你每天可以给图打分，是 trash、meh、good 还是 love it；你这样训练 bot 的时候，还会解锁额外时间或图片，因为你花时间训练它，平台也给你额外 benefit。” —— Scott Detweiler, YouTube, 2026-04-21

## Midjourney 对 reference image 的处理更偏风格迁移而非内容复刻，这既是安全边界也是产品定位

当观众问 reference images 看 style 还是 content，Scott 的理解是 Midjourney 更看 style，不追求把输入图直接改成另一个内容版本，并且团队不想做 deep fake engine。这个点对 Midjourney 的产品边界有用：它把自己定位成创作解释器和风格扩展工具，而不是人脸复制或内容编辑工具。这样的安全取向可能牺牲一部分“精确改图”需求，却有助于保持艺术创作和平台治理的边界。

“有人问，如果给它一张或一组 reference images，它看的是图片的 style 还是 content？按我的理解，它看的是 style，content 还不是它真正要走的方向；DALL-E 2 是相反的，更倾向于拿图去修改和推进。Midjourney 更像是对你的图做艺术解释，给你一个 rough idea，而不是复制那张图本身。还要记住，这个团队的想法不是做 deep fake engine；他们做的所有东西都基于用户想创造 art，而不是复制已经存在的东西。” —— Scott Detweiler, YouTube, 2026-04-21
