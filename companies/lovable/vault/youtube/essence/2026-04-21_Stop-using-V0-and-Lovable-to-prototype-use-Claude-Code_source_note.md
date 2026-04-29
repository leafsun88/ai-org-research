---
type: source_note
company: lovable
source_type: youtube
status: done
source_path: companies/lovable/vault/youtube/transcripts/2026-04-21_Stop-using-V0-and-Lovable-to-prototype-use-Claude-Code.md
source_title: "Stop using V0 and Lovable to prototype, use Claude Code instead"
source_date: 2026-04-21
created_at: 2026-04-23
speaker: "Diane"
source_weight: A
relevance: high
note_version: 1.0
quote_language: zh_translation_from_en_transcript
quote_style: single_long_translated_excerpt_per_block
---

# Stop using V0 and Lovable to prototype, use Claude Code instead

> 这篇 source note 只保留“什么时候该从 Lovable 的沙盒切回代码库”的边界判断。

## Lovable 适合沙盒原型，但不适合停在沙盒里
这篇视频的核心不是“Lovable 好不好”，而是“Lovable 该在什么阶段用”。Diane 的结论很明确：如果你还在验证想法、做一次性原型，Lovable 很合适；但如果你已经反复在同一个 bug 上打转，或者需要和现有代码库对齐，就应该退回代码级工作流。这个判断对 Lovable 的定位很有帮助，因为它把产品价值限定在正确的阶段。

“如果你现在用 V0 或 Lovable 做原型，而且它正在起作用，那就继续用。但如果你已经在 AI 之间来回折腾了 45 分钟，修了一个东西又把另一个东西弄坏了，你其实已经碰到墙了。今天我想讲的是：什么时候该停止在沙盒里原型化，V0、Lovable、Base44 这些都是沙盒工具，它们是站在真实代码之上的；而什么时候应该开始直接在代码库里原型化。” —— Diane, Stop using V0 and Lovable to prototype, use Claude Code instead, 2026-04-21

## 产品团队最常见的浪费，是先做一个漂亮 prototype，再让工程团队重建一遍
这段视频最有说服力的地方，在于它把产品团队最常见的浪费说穿了：prototype 看起来很美，但交到工程团队手里却没法直接用，最后只能重建。对 Lovable 来说，这不是产品失败，而是边界判断的问题。只要团队还在做 throwaway prototype，Lovable 就很值；一旦要进入真实代码系统，工作方式就得换。

“更大的问题是，产品团队往往先在 V0 里做出一个很漂亮的 prototype，拿去给利益相关方看，大家都很兴奋，结果交给开发团队之后，他们会说：‘这东西我们没法直接用，它不符合我们的代码库、设计系统或者架构。’于是最后他们还是得从头重做一遍。你其实只是给开发流程又加了一轮，而不是少了一轮。问题不在于工具不好，而在于你把原型建在了孤立的沙盒里。” —— Diane, Stop using V0 and Lovable to prototype, use Claude Code instead, 2026-04-21

## 当你开始需要和现有代码对齐时，Claude Code 这类工具更像下一站
Diane 之所以建议从 Lovable 转到 Claude Code，不是因为 Lovable 不行，而是因为后者让你直接在真实 codebase 里继续工作。这个切换的本质，是从“描述想法”变成“在已有系统里实施想法”。对 Lovable 来说，这反而能帮我们更清楚地理解它的适用边界：它最强的地方是起步，而不是整个生命周期。

“如果你想像团队一样在真实代码库里原型化，那就进入 Claude Code 这样的工作流。终端其实就是一个聊天窗口，只是没有那些漂亮 UI。你仍然可以用自然语言说你要什么，但现在它是基于你们公司已经有的代码基础来工作的，而不是建在一个独立的 sandbox 上。这种方式更适合你已经要把 prototype 变成真产品的时候。” —— Diane, Stop using V0 and Lovable to prototype, use Claude Code instead, 2026-04-21

## Plan mode 的价值，是让非技术人也能在代码层面更快理解系统
这支视频其实也在讲一个很现实的事实：即便进入代码库，非技术人也不一定要退场。通过 plan mode、清晰的提问和逐步澄清，产品人依旧可以参与实施，只是协作的位置从原型工具转到了代码工作流。这个视角很适合放进 Lovable 的反方材料里，因为它解释了为什么有些团队会在 prototype 之后自然转向代码级工具。

“我现在会先让 Claude Code 在 plan mode 里给我一个清晰的实现思路，然后它会列出要改哪些文件、要遵循哪些现有模式、要测试什么。这个过程让我第一次真正看懂了它在做什么，而不是只看着它在沙盒里猜你想要什么。对我来说，最有价值的不是它替我写代码，而是它让我在代码库里也能继续用对话的方式思考。” —— Diane, Stop using V0 and Lovable to prototype, use Claude Code instead, 2026-04-21
