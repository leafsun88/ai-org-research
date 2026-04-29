---
company: midjourney
source_type: youtube
type: source_note
status: done
source_path: companies/midjourney/vault/youtube/transcripts/2026-04-21_Midjourney-V8-Did-They-Cook-or-Are-They-Cooked.md
source_title: "Midjourney V8: Did They Cook, or Are They Cooked?"
source_date: 2026-04-21
created_at: 2026-04-22
speaker: "Tim / Theoretically Media"
source_weight: B
relevance: high
quote_language: zh_translation_from_en_transcript
---

# Midjourney V8: Did They Cook, or Are They Cooked?

## V8 不是稳定大版本，而是把用户带进一条新的风格探索路线

Tim 对 V8 的判断比简单好坏更有研究价值：这是 alpha，粗糙、janky、需要调校，但它也把 Midjourney 的方向从“一个 prompt 得到一张完成图”推向 personalization、mood board、style creator 和视觉化选择。这个 source 对后续分析的意义在于，Midjourney 正在把产品重心压到 taste discovery 和 style system，而不是和 Google、OpenAI 直接比全能图像编辑。

“版本 8 是 alpha，这说实话让它边缘更粗糙；从版本号更新的 bingo card 来看，它基本都是典型项目：更快、更好审美、更好 prompt understanding，甚至 Midjourney 自己也写了文字能力会更好。基线 V8 的确还有很多要调，很多人也注意到了，但你现在还是能从里面得到一些不错的东西，而它们似乎在把工作流推向另一个方向。” —— Tim / Theoretically Media, 2026-04-21

## 默认审美还没调好，用户必须主动把 stylize、profile 和 mood board 纳入流程

V8 的默认输出被 Tim 描述成“vanilla V7”，低 stylize 下皮肤和服装都偏平，开到 1000 才接近经典 Midjourney。这个细节说明 V8 的新能力不是自动显现，而是要求用户更懂参数和个人化系统。对 Midjourney 这样的创作者工具来说，这会提高高级用户上限，但也会增加普通用户迁移成本：新模型不是直接更好，而是需要重学旋钮。

“Midjourney 已经表示他们还在调 V8 的默认审美，并鼓励我们使用 personalization，甚至把 style 拉到 1000；在 stylize 100 的时候，你会看到皮肤纹理有很多 smoothing，衬衫也很普通，拉到 500 会改善一些，而拉到 1000 基本就到了经典 Midjourney 领域，那个帅哥盯着太阳，西装很有型，整体就是我熟悉的标准 Midjourney 图像。” —— Tim / Theoretically Media, 2026-04-21

## HD、Q4 和 fast hours 把 V8 的成本问题暴露出来

Tim 对成本的描述很具体：alpha 没有 relax mode，只跑 fast mode；HD、Q4、style reference、mood board 都会显著烧 credit，HD 加 Q4 可能等于 16 倍普通生成。这会影响专业创作者的试错方式，因为 Midjourney 的价值恰恰来自大量探索和挑选。如果探索本身变贵，用户会减少迭代，或者把高成本阶段留给更可控的模型。

“关于 alpha 还有几件事要说，第一是它挺贵的，没有 relax mode，只能跑 fast mode，而且非常烧 credit；前面说过，HD mode、quality 4，再加上 style references 和 mood boards，目前都可能慢四倍、也贵四倍，如果你在 HD 里加 Q4，基本上会花掉普通生成 16 倍的量，所以我现在并不太推荐这样做。” —— Tim / Theoretically Media, 2026-04-21

## 多重 style reference 会把 V8 搞坏，说明新系统仍缺稳定组合能力

V8 被 Midjourney 推向 style reference 和 personalization，但 Tim 的测试显示两个 style reference 同时用会明显“break”输出，脸部乱码、纹理异常。这个缺陷很重要，因为真正专业的视觉开发往往依赖多参考源：角色、色彩、镜头、材质、时代感会来自不同参考。如果 V8 不能稳定组合多重视觉条件，它就很难从单张灵感图工具升级为 production design 系统。

“当你同时跑两个 image reference style 的时候，它真的会把 V8 搞坏；后面那个人的脸是乱码的，整个画面上还有奇怪的颗粒质感，所以我强烈建议不要这样做。我继续尝试不同的 stylization code、上下调 stylization、换不同参考图，里面有些东西我喜欢，但没有一个真正抓住我想要的感觉。” —— Tim / Theoretically Media, 2026-04-21

## Style Creator 让 Midjourney 更像视觉搜索和 lookbook，而不是最终编辑器

Tim 最有价值的观察是 Style Creator：用户不只是写 prompt，而是在一串视觉选项里点击、筛选、让系统往某个审美空间走。这是 David Holz 所说 post-prompting 世界的产品化雏形。Midjourney 的护城河如果存在，可能不在“文字到图像”本身，而在把用户 taste、社区风格、历史偏好和视觉探索界面合成一个审美操作系统。

“当我开始玩 style creator 的时候，事情变得很怪也很有意思；你点这个按钮进入 style creator 模块，prompt 已经加载进去，你基本上是在找一些想玩的审美图像，过了一定阈值以后它会自己开始生成。结果马上就很有趣，有那种 80 年代末漫画混欧洲漫画的感觉，也有现代漫画、编辑时装、科技街头服和向量化效果，有些完全不是我会主动提示的方向。” —— Tim / Theoretically Media, 2026-04-21

## Midjourney 的工作流位置被重新定义为“style definer”

Tim 明确提出一个新 framing：Midjourney 不必成为所有生成、编辑、修复的一站式平台，而可以成为项目的 style definer 或 lookbook。这个判断和 Curious Refuge 的结论互相印证，说明创作者社区已经自然形成了一种多模型工作流：Midjourney 定义 look and feel，Nano Banana 等模型负责替换角色、编辑细节、扩展场景。Midjourney 的战略问题是，它能否把这个“前端审美层”做得足够不可替代。

“CEO David Holz 讲过一种 post-prompting world 的感觉，我不是直接引用，但你能从 personalization codes、mood boards，尤其是 stylization 里看到这种思路。Midjourney 更好的 framing 也许不是一站式平台，不是所有图像都在这里生成和处理，而是用来发现你想探索的 look、style、tone 和 character，基本上变成项目里的 style definer 或 lookbook。” —— Tim / Theoretically Media, 2026-04-21

## V8 的基础重写是长期利好，但短期会让输出像“重新起步”

视频提到 V8 完全重写、从 Google TPU 切到 GPU 和新代码库，这解释了为什么 V8 输出不像巨大飞跃：它不只是模型权重更新，而是底层运行系统切换。对公司研究来说，这条信息意味着 Midjourney 在做长期 inference 成本、工程迭代速度和硬件适配的重构；但用户短期看到的是“V7 到 V8 差异很小甚至退步”。这类重构的风险是技术债被还掉之前，产品口碑会被竞品抢走。

“V8 实际上是完全重写过的，他们从 Google 的 TPU，也就是 tensor processing units，切到了 GPU，并换成新的代码库，这会优化很多东西，让工作更容易，甚至和我们上个视频聊到的 Nvidia 有关系，以后他们可以在 Vera Rubin 上跑 Midjourney；所以 V8 不只是一个新模型，而是一整个新代码库，某种意义上是在重新开始，虽然不是从零开始。” —— Tim / Theoretically Media, 2026-04-21

## 用户规模和无外部融资给 Midjourney 留出试错时间

Tim 最后给出一个反市场情绪的信号：尽管有人觉得 Midjourney 像 ghost town，但它上一年仍有 2100 万用户，而且公司没有外部融资压力。这两点解释了为什么 Midjourney 可以慢慢迭代 V8 alpha，而不是被迫用一个完美版本立即回应市场。对投资分析来说，这既是韧性也是风险：用户基础和资本结构给它时间，但如果产品方向长期只剩风格探索，商业上限会被下游执行工具限制。

“至于 Midjourney 是不是 cooked，我诚实说不是，他们不会消失；有些人总觉得 Midjourney 是 ghost town，没人用了，但截至去年他们仍然有 2100 万用户，对一家不欠任何外部融资人的公司来说，这是很多用户。所以他们会继续往前做，而我也会继续给新版本做这些傻乎乎的缩略图，至少会做到版本 10。” —— Tim / Theoretically Media, 2026-04-21
