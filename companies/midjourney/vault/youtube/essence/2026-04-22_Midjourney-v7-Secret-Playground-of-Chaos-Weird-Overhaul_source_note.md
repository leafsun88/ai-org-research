---
company: midjourney
source_type: youtube
type: source_note
status: done
source_path: companies/midjourney/vault/youtube/transcripts/2026-04-22_Midjourney-v7-Secret-Playground-of-Chaos-Weird-Overhaul.md
source_title: "Midjourney v7: Secret Playground of Chaos & Weird + Overhauled Editor"
source_date: 2026-04-22
created_at: 2026-04-22
speaker: "Rory Flynn / Drew Brucker"
source_weight: B
relevance: high
quote_language: zh_translation_from_en_transcript
---

# Midjourney V7 Weird / Editor Overhaul — Source Note

## 小步快发重新点燃了社区注意力，比单次大版本更适合现在的 AI 工具市场

这期的开场是对 Midjourney release cadence 的直接反馈：主持人更喜欢持续 drip 新功能，而不是长时间等 V7/V8 一次性大爆发。原因很现实：Twitter/X 上 Midjourney 讨论曾经变少，功能重新滚动发布后，用户又开始测试、分享和讨论。Midjourney 的社区增长不只是模型质量，也依赖不断制造“今天能试什么”的节奏。

“这些更新一滴一滴出来，我觉得比还在等 V7 要好太多；我说过很多次，他们以前有点过度思考，应该直接发布、让我们玩，然后进入下一件事。五六周前我在 Twitter 上几乎没看到那么多 Midjourney 内容，现在又回来了，因为不断有新东西，大家都在测试、都在玩，而不是一次巨大发布把所有东西都淹掉。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-22

## Weird 参数回归的价值，是让用户挖掘 Midjourney 不能被普通语言 prompt 出来的审美空间

Weird 的讨论不是参数教程，而是关于 Midjourney 的创意差异化。主持人把 weird 当成“Midjourney playground”和 SREF/mood board 挖矿工具：它不追求控制，而是把模型带到用户不会主动描述的地方。对 Midjourney 来说，这类参数保留了“模型有自己的想象力”的体验，这是 LLM-style 精准执行工具难替代的部分。

“Weird 对我来说就是 Midjourney playground；如果你想要独特的东西，单靠 stylize 和 base model 不一定够，你需要 personalization、blend，或者像 weird 和 chaos 这种参数。高 weird 加高 chaos 会产出 Midjourney 最独特的东西，很多不是人会正常 prompt 出来的，所以我常把它当成 explore page，用来找新的 style reference。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-22

## Personalization 会压住 Weird 的发散，说明 Midjourney 的参数不是独立旋钮，而是互相耦合

他们在测试中发现，开着 profile 时 weird 仍会被个人化风格拉回，关掉 personalization 后结果发散更大。这是一个重要产品机制：Midjourney 的参数不是机械相加，而是 profile、style raw、weird、chaos、aspect ratio、SREF 之间共同决定探索空间。对 power users 这是创造力；对普通用户则是复杂度，解释了为什么 UI/教育成为 Midjourney 的重要瓶颈。

“当 weird 和你的 profile 一起用时，它还是会相当忠于 profile；如果把 personalization 关掉，你会得到更大范围的结果。我基本上会关掉 personalization 来用 weird，把它当作挖 SREF 的方式，因为我是在找那些我不知道怎么 prompt 的东西，测试 Midjourney 的创意能力。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-22

## Weird + Describe 形成了反向工程模型审美的工作流

节目里很有价值的一段是用 weird 生成古代战士，再用 describe 看 Midjourney 如何理解图像：close-up portrait、Canon EOS、Helmut Newton、Richard Avedon 等词会浮现出来。这个工作流把 Midjourney 变成审美发现和语言化工具：用户先让模型发散，再让模型解释自己，再把解释拿回 prompt 或 SREF 系统。这里有一条产品路线：Midjourney 可以把探索、describe、style library、prompt reuse 做成闭环。

“有趣的是你可以把那些特别 out there 的图再跑 describe，看看 Midjourney 到底怎么理解它；我们只写了 award-winning photo of an ancient warrior，然后加一点 chaos 和 weird，它开始把结果描述成 close-up portrait、Canon EOS R5、Helmut Newton、Richard Avedon 这类东西。这样你就能反向工程它在想什么，再拿去当新的 style 或 prompt 入口。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-22

## Editor 合并和 smart select 让 Midjourney 更接近资产编辑器，但图层操作仍显得粗糙

这期深入测试了新版 editor：smart select、erase background、erase selection、layer stacking、retexture、style weight 等都能在一个界面里完成。正面是对象提取、替换和风格化比旧版顺；负面是图层无法旋转、透明度/选中逻辑混乱、edit/retexture tab 容易切错、提示不够清晰。Midjourney 已经在往 Photoshop/Figma 的轻编辑方向走，但还没把图层交互做成专业工作流。

“Smart select 现在很方便，你点一下对象，再选 erase background 就能把它孤立出来；反过来选 erase selection 就能把它拿掉，然后你可以堆图层、retexture，让风格混在一起。但这里也很 clunky，比如你不能旋转图层，不能简单调 opacity，有时候你以为在编辑输入图，实际选到了某个 variation；如果没人讲，你根本不知道这里所有变量怎么用。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-22

## Retexture 在产品图/素材图上已经有实用价值，但 V6.1 和 V7 的编辑一致性差异明显

主持人用鞋子做对象替换测试，把产品鞋从原图里抠出来放到人物/街景中，再让 Midjourney 生成不同背景和风格。最有价值的观察是：V6.1 在 editor 里比 V7 更 coherent，说明某些编辑功能可能仍更适配旧引擎；但即便如此，Midjourney 能自动匹配鞋子色彩、材质、阴影、环境氛围，这对产品资产生成是很强的实用场景。问题不是能不能做，而是是否稳定、是否值得在这里做。

“我把一双鞋从图片里拿出来，放进另一个场景里，它会把鞋子的颜色和风格带到整张图上，还会处理脚下阴影、人物身上的光、背景质感；这在 Photoshop 里单独做会非常夸张。但同一个任务里 V6.1 明显比 V7 更 coherent，V7 的质量有时更像 V7，可结构和腿会碎，所以现在编辑这块感觉还是 6.1 更稳。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-22

## SREF 仍是 Midjourney 相对其他图像工具最强的差异化层

主持人明确说 SREF 是 Midjourney 最好的东西之一，可能是和其他工具差距最大的功能。它的价值在于不只是 image reference，而是 style plus control，可以 blend、apply、random unlock，再和 weird/chaos/mood boards 叠加。未来如果 Midjourney 做 super SREF、SREF library、SREF explore page，就能把用户的审美探索变成可管理资产，而不是散落在 prompt 历史和第三方网站里。

“SREF 对我来说可能是 Midjourney 最好的东西，真的是和其他工具差距最大的地方；很多工具现在才开始做 style blending，而 Midjourney 很早就能把两个 style reference mash 在一起，不只是 image prompt，而是 style 加 control 再应用。要是能有一个 SREF library 或 SREF explore page，用户就能按风格找代码、保存常用代码，而不是到处翻历史。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-22

## Q4、Omni reference、creative mode 和 video roadmap 暗示 Midjourney 在补齐“控制层”

节目后半段读 office hours notes，提到 Q4、character/omni reference、super SREF、prompt accuracy、anatomy/artifact reduction、creative mode、ultra-fast draft、video model training 等。这里能看出 Midjourney 的产品路线不是单点模型，而是在速度、质量、引用、编辑、视频和审美模式之间找组合。风险也明显：每条都重要，但全部叠加会让产品复杂度继续上升。

“Q4 正在实验，意思是更慢但更高质量；还有 character reference、omni reference、super SREF、更好的 prompt accuracy、anatomy 和 artifact reduction，甚至一个新的 creative mode，可能是在不加太多 slider 的情况下给更多用户控制。视频模型训练据说月底完成，调试和发布如果没有 hiccups 可能还要一两个月。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-22

## ChatGPT image 的日常入口优势提醒 Midjourney：用户最后会收敛到少数几个工具

主持人把 Midjourney、ChatGPT image、Reve、Photoshop、Runway、Sora 等放在“20 个工具收敛到 3 个工具”的框架里看。Midjourney 的优势是审美、SREF、用户肌肉记忆和潜在视频整合；ChatGPT 的优势是日常入口和巨大用户量。真正的竞争不是某张图谁好，而是谁能成为用户每天打开的少数工作台之一，尤其当图像、视频、编辑和 LLM 编排逐渐合并。

“我们都在找的不是 20 个工具，而是 3 个工具；能把更多东西带进一个地方的工具，加上已有 adoption，会赢。ChatGPT 已经是很多人每天打开的地方，给它一个还不错的 image generation 就是巨大 lift；Reve 可能很强，但它还只是另一个要打开的工具。Midjourney 如果有好的视频模型，而且就在我已经使用的工具里，我大概率不会去用别的视频模型。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-22

## Patchwork / node-based workspace 是 Midjourney 扩展到生产流程的可能路径

节目最后讨论 Flora、Weavy、Patchwork、image-to-video、multi-image reference、storyboard 和 node-based workspace。这里对 Midjourney 很关键：用户不只是要一张图，而是要把 stills、character reference、video、resize、outpaint、model choice、LLM prompt concentrator 放在一个项目空间里。Midjourney 已有 Patchwork 概念，但执行需要更清晰；如果能把 create、video、reference、project organization 放在一个 canvas，它就能从生成工具变成创意操作系统。

“我喜欢这种 node-based workspace，因为你能把图放在一起、重新生成、做 video、resize、换模型，而不是在不同 tab 里来回找图。Midjourney 也许可以把 Patchwork 的某个版本带进这里，让人把 stills 到 animation 的流程放在一个地方，不用切 tab；有所有工具和可视化目标在同一个空间里，是一个很大的 unlock。” —— Rory Flynn / Drew Brucker, Midjourney Fast Hours, 2026-04-22

