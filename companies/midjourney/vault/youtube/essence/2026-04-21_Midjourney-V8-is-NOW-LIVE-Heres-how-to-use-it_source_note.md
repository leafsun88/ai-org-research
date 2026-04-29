---
company: midjourney
source_type: youtube
type: source_note
status: done
source_path: companies/midjourney/vault/youtube/transcripts/2026-04-21_Midjourney-V8-is-NOW-LIVE-Heres-how-to-use-it.md
source_title: "Midjourney V8 is NOW LIVE!! Here's how to use it."
source_date: 2026-04-21
created_at: 2026-04-22
speaker: "Wade McMaster / Creator Impact"
source_weight: B
relevance: high
quote_language: zh_translation_from_en_transcript
---

# Midjourney V8 is NOW LIVE!! Here's how to use it.

## V8 先在 alpha 站点上线，说明 Midjourney 仍采用分层发布来保护主站体验

Wade 的教程一开始强调 V8 不在主 Midjourney 网站，而是在 alpha.midjourney.com 试用，生成图也不会出现在 midjourney.com。这是一个产品发布信号：Midjourney 没有把新模型直接推给全量用户，而是把 alpha 与主站分开，既让重度用户先试，也避免新模型不稳时污染主体验。对公司研究来说，这体现了 Midjourney release discipline：社区可以抢先体验，但核心产品仍保留稳定层。

“Midjourney version 8 现在已经 live，但不是在主 Midjourney 网站上；如果你想使用这个模型，本质上要去 alpha.midjourney.com，那里会出现一个页面，列出很多改进。你如果去 midjourney.com，是看不到你生成的 V8 images 的，但在 alpha 这里会注意到一些界面差异，比如设置现在有 sidebar，模型仍然可以在 model section 里切换，也有新的 HD mode。” —— Wade McMaster / Creator Impact, 2026-04-21

## Conversational mode 明显提高复杂指令理解，是 V8 最像“智能升级”的部分

Wade 的测试很有价值，因为他用“快乐家庭加宠物但不要狗”这种否定约束验证 prompt understanding。普通 V8 和 raw mode 都失败，conversational mode 成功去掉狗。这说明 V8 的智能提升不一定都在基础模型输出里，而可能来自 prompt rewriting / conversational layer。Midjourney 的产品能力正在从纯生成模型扩展到输入解释层，未来可控性可能更多依赖这个中间层。

“我用同一个 prompt 让它生成一个快乐家庭，周围有宠物，但不要包含任何狗；在版本 8 的每张 grid 图里都有狗，raw mode 也没有真的改善这个指令。然后我切到 conversational mode，再放入同样的 prompt，这些图是 conversational mode 做的，没有狗。所以如果我们想要更高层级的智能指令解释，可能最好使用 conversational mode。” —— Wade McMaster / Creator Impact, 2026-04-21

## V8 在隐含概念和多细节约束上比 V7 进步，补上了被 Nano Banana 拉开的智能差距

Wade 用 Statue of Liberty 和一张复杂人脸 prompt 测试 V8：不直接说自由女神，而说美国最著名雕像；要求左右眼颜色、红痣、发际线、细胡子、背景七个人。V8 比 V7 更能理解隐含对象和细节约束。这个信号对 Midjourney 很重要，因为此前 Google/Nano Banana 的优势正是“理解你到底想要什么”，V8 如果补上这一层，Midjourney 才能把审美优势转回主流程。

“我换了一个更详细的 prompt，要求一张焦虑男人脸的专业照片，左眼红色，右眼蓝色，发际线后退，肤色较白，鼻子左边有一个小红痣，很细的胡子，背景里应该有一片海滩和七个人；版本 7 基本没有理解任务，只得到一点红眼和蓝眼，也没真正做到我想要的东西，但版本 8 出现红眼和蓝眼，也有公平肤色，很多图鼻子旁边有红痣，所以它的智能确实提升了。” —— Wade McMaster / Creator Impact, 2026-04-21

## 文字渲染是 V8 的真实增量，但长段落仍不是完美可靠

Wade 的文字测试从额头上的单词到手写长段落，显示 V8 相比 V7 有明显提升：V7 对长段落基本是乱码，V8 能放入大部分信息但不完美。这个能力对广告、海报、UI mockup 和品牌创意很关键，因为文字长期是 Midjourney 的短板。V8 的意义不是一下子成为排版工具，而是让 Midjourney 从“只能出氛围图”扩展到“部分可用于含文字视觉概念”。

“我让它生成一张手写便条的专业照片，里面写一整段我从 Midjourney 更新帖里拿来的文字，给它很多 text 来处理，因为我知道 Nano Banana 2 过去在这方面做得不错；版本 7 只是尝试塞一点 V8，基本都是没有意义的乱码和手写，版本 8 做得好多了，我不会说完美，但大部分信息似乎都在那里，文字生成能力真的进了一大步。” —— Wade McMaster / Creator Impact, 2026-04-21

## 五倍速度是实测可见的，但 HD、Q4、seed 不稳定让高分辨率流程不够顺

Wade 用 V7/V8 permutation 实时对比，V8 明显更快；HD 输出 2048x2048，也保留不错细节。但他同时发现 V8 没有 upscale option，想要 2K 必须一开始就开 HD；同一 seed 切 HD 会生成不同图，Q4 也会明显改图。这对专业流程是个痛点：创作者常常先低成本挑构图，再 upscale 选中图；V8 的当前路径要求在早期就押注 HD，增加试错成本。

“我下载刚才这张普通版本 8 图，它是 1024x1024，基本是标准 Midjourney 尺寸；同样 prompt 开 HD mode 后再下载，是 2048x2048，质量保持得很好。但还有一个问题，版本 8 图没有 upscale option，如果你想要 2048x2048，就必须一开始用 HD mode；更烦的是，即使用同一个 seed 重新生成 HD，它也会产生完全不同的一组图，所以如果你想要高分辨率，必须从 HD 开始。” —— Wade McMaster / Creator Impact, 2026-04-21

## Q4 更像“再发展一次图像”，不是简单无损增强

Quality 4 在 Wade 的测试中并非纯粹提高细节，而会改变文本、草地、纹理和画面结构。这一点对专业用户很重要：如果 Q4 会重塑图像，就不能把它当成最终无损 upscale，只能当成另一次高成本重生成。Midjourney 在 V8 里需要解决的不是有没有高质量按钮，而是如何让质量提升与用户已经选中的构图、角色和文字保持一致。

“我把同一张图放进 Photoshop 对比，quality one 会看到一些头发细节和照片感，quality four 会进一步发展画面，文字变厚，细节有些差不多；在文字图例里，quality four 实际改变了图像，虽然我不太喜欢它的文字，但草地细节和 grungy overlay 变多了。所以它值得实验，但会大幅 transform the image，你不会用 quality mode 得到完全相同的图。” —— Wade McMaster / Creator Impact, 2026-04-21

## Personalization 和 mood board 仍可用，但 HD 不兼容削弱了统一工作流

Wade 测试 global profile、mood boards、liked style codes，说明 V7 的个性化资产可以带到 V8，且 mood board 可以有效影响风格。但他也遇到 mood boards 不能和 HD mode 同用的问题。这个限制和其他评测互相印证：Midjourney 把风格系统当作核心，但当前 alpha 的高分辨率、高质量、风格参考之间还没有打通。专业创作者最需要的是这些能力叠加，而不是互斥。

“你的 personalization codes 也能工作，而且是 backwards compatible，你在版本 7 做的东西现在可以在版本 8 使用；我打开 global profile，再加 mood board，提示词下方能看到正在使用哪些 profiles 和 mood boards。不过我遇到一个小障碍，mood boards 不能在 HD mode 打开时使用，这一点值得注意，我之前没有意识到，现在我们知道了。” —— Wade McMaster / Creator Impact, 2026-04-21

## V8 技术升级明显，但审美风格可能从 Midjourney 标志性优势里退了一步

Wade 最终的反方判断很有分量：V8 在智能、文字、速度上是技术进步，但在某些 stylized 用例里不如 V7，尤其是 vector、dot matrix、Malovich 风格等更艺术化的场景。Midjourney 的品牌资产恰恰是 aesthetics，如果技术升级让输出更 photorealistic、更 generic，就会和 Google/Nano Banana 的竞争区重叠，反而削弱差异化。最可能的用户行为是按任务回退 V7 或更旧版本。

“这个更新到这里就有点转折了，因为技术进步真的很扎实，百分之百很棒，但 Midjourney 以审美出名，而那个 aesthetic style 的流失，每次模型改进似乎都会慢慢发生。所以版本 8 对某些事情会很好，但版本 7 可能更适合 stylizing，甚至可以再回到更早版本；它不是全面更优的模型，技术上是一步向前，审美上有点向后。” —— Wade McMaster / Creator Impact, 2026-04-21

## V8 的推荐用例是 realism、text 和 style reference，不是所有创意任务

Wade 的结论给了一个清晰的产品定位：V8 适合 photorealism、文字、需要 style reference 控制的任务；V7 仍适合强风格化。这个任务分工会直接影响 Midjourney 的产品复杂度：平台不再是“永远用最新版”，而是多模型共存、按创作目标选择版本。对用户是灵活性，对公司是教育成本，因为产品必须让创作者理解每个版本的最佳场景。

“Version 8 很适合 photorealism，也适合它能适配的那些 style；当你做文字，或者想用 style references 获得更多控制时，它会更好。但它不一定是整体 step up，技术上是 step up，审美上是 step back。Midjourney 以 aesthetics 闻名，所以我不太确定该怎么说；我建议大家自己去玩，按你真正会使用它的方式测试 version 8，看看会得到什么结果。” —— Wade McMaster / Creator Impact, 2026-04-21
