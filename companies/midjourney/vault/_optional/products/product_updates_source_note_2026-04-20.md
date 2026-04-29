---
company: Midjourney
research_key: MIDJOURNEY
type: product_updates_source_note
date: 2026-04-20
fetched_at: 2026-04-20
credibility: S1
evidence: E1-E2
status: browser_verified_after_script_index_only
---

# Midjourney 产品与路线图补充笔记

## 核心来源

- Version docs: https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version
- V7 default announcement: https://updates.midjourney.com/v7-is-now-the-default-model/
- V1 Video announcement: https://updates.midjourney.com/introducing-our-v1-video-model/
- V8 Alpha announcement: https://updates.midjourney.com/v8-alpha/
- V8.1 Alpha announcement: https://updates.midjourney.com/v8-1-alpha/

## 已核验事实

- V7 于 2025-04-03 发布，2025-06-17 成为默认模型。官方称 V7 在 image quality、prompt understanding、image coherence 上提升，并引入 Draft Mode 与 Omni Reference。
- 官方 V7 默认公告披露：Draft Mode 速度为普通图像生成的 10x；new sref 与 moodboard 算法提升 mood/style precision；personalization profiles 改进后被 85% 用户偏好。
- V1 Video 于 2025-06-18 面向整个社区发布。官方把 video 视为通往 real-time open-world simulations 的 building block。
- V1 Video 初期是 image-to-video：用户先生成或上传图片，再用 Animate 生成视频；支持 automatic / manual motion prompt、高/低 motion、约 4 秒一段的 extend。
- V1 Video 首发 web-only；官方披露 video job 约为 image job 8x 成本，每个 job 生成四个 5 秒视频，并计划观察成本和服务器压力后调整价格。
- V8 Alpha 于 2026-03-17 发布到 alpha.midjourney.com 社区测试。官方称 V8 更擅长 detailed directions、personalization、srefs、moodboards，image generation 约 5x faster。
- V8 Alpha 支持多 aspect ratios、`--chaos`、`--weird`、`--exp`、`--raw`，并新增 `--hd` 2K 与 `--q 4` 模式；官方明确要求社区在 lightbox 里评价图像，帮助改进 V8。
- V8.1 Alpha 于 2026-04-14 发布。官方披露 V8.1 的 HD mode 变成 3x faster / 3x cheaper，并成为 V8.1 default；standard resolution 50% faster / 25% cheaper。
- V8.1 Alpha 恢复 image prompts / image weights，加入 Prompt Shortener 和更详细的 Describe；V8 系列仍在 alpha.midjourney.com 测试。

## 研究含义

- Midjourney 的产品路线不是单纯 image generator 增强，而是 image -> video -> 3D -> real-time simulation 的连续路线。
- 它的迭代方式非常社区化：rating parties、lightbox ratings、Discord feedback、alpha website 测试共同构成模型改进 loop。
- 价格与成本被直接写进产品公告，说明 Midjourney 在 GPU 约束下做的是“可持续探索速度”，不是无限免费增长。

## 限制

- 官方没有披露模型参数、训练数据规模、GPU/云供应商、具体付费用户数量。
- V8/V8.1 仍为 alpha，不能按稳定默认模型评价商业化贡献。
