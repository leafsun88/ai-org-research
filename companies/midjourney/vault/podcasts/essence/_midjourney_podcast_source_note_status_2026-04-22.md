# Midjourney Podcast Source Note Status

- Date: 2026-04-22
- Scope: high / medium-high Midjourney podcast transcript candidates in `companies/midjourney/vault/podcasts/transcripts/`
- Output dir: `companies/midjourney/vault/podcasts/essence/`
- Style:新版 `source_note`，每个 insight block 使用判断自然段 + 一条长连续中文译引。

## Summary

- Assigned podcast candidates: 18
- Full source notes written: 15
- Rejected low-relevance records written: 1
- Duplicate / skipped without note: 1
- Low-value news skipped without note: 1
- Old `_essence.md` files: left untouched for audit; formal new input should use `_source_note.md`.

## Completed Full Source Notes

- `2022-11-10_How-Computers-Dream-with-David-Holz_source_note.md` — 18 blocks / 18 quotes
- `2023-06-20_David-Holz-Midjourney_source_note.md` — 15 / 15
- `2023-05-08_Stable-Diffusion-都快倒闭了Midjourney-凭什么是绘画的未来_source_note.md` — 13 / 13
- `2023-07-06_Vol09-大模型之下Midjourney等内容工具和平台的新机会在哪里_source_note.md` — 14 / 14
- `2023-11-06_Nick-from-Midjourney-for-Creatives-Unlocking-the-full-power_source_note.md` — 8 / 8
- `2025-04-13_Midjourney-V7-Showed-Up-in-Crocs-and-COOKED_source_note.md` — 9 / 9
- `2025-04-22_Midjourneys-Secret-Playground-Chaos-Weird-and-New-Editor_source_note.md` — 10 / 10
- `2025-06-17_EP-548-Disney-vs-Midjourney---Will-Hollywood-kill-AI_source_note.md` — 9 / 9
- `2025-06-17_Midjourney-Made-300M-Disneys-Fuming-and-AI-Pets-Are-TV-Stars_source_note.md` — 5 / 5
- `2025-07-09_MLA-025-AI-Image-Generation-Midjourney-vs-Stable-Diffusion-G_source_note.md` — 12 / 12
- `2025-08-26_Metas-Midjourney-Deal-Oz-Remixed-Premiere-AI--Runway-Gaming_source_note.md` — 3 / 3
- `2025-09-09_Why-Disney-vs-MidJourney-Could-Rewrite-Hollywoods-IP-Playboo_source_note.md` — 15 / 15
- `2025-10-05_446-David-Holz-Maker-Mantra-Embrace-Technology-Ignite-Your-I_source_note.md` — 1 / 1
- `2025-12-21_Midjourney-v8-Countdown-Are-AI-Artists-A-Thing--Nano-Banana_source_note.md` — 10 / 10
- `2026-02-17_EP-25-AI-in-Visual-Art---Midjourney-DALL-E-and-the-Copyright_source_note.md` — 9 / 9

## Rejected / Skipped

- `2025-09-12_Preview-New-iPhones-and-an-Absence-of-Awe-How-Oracle-Wins-in_source_note.md`
  - status: `rejected_low_relevance`
  - reason: available transcript is a short Sharp Tech preview and contains no substantive Midjourney discussion beyond title/frontmatter.
- `2025-07-02_S07E05---Character-Copyright-and-the-Disney--Universal-Lawsu.md`
  - status: `duplicate_of`
  - duplicate_of: `companies/midjourney/vault/youtube/essence/2026-04-22_S07E05-Character-Copyright-and-The-Disney-Universal-Law_source_note.md`
  - reason: same legal source/content covered by cleaner YouTube transcript note.
- `2026-03-19_March-19-2026---Midjourney-V8-Gemini-Privacy--Mamba-3Midjour.md`
  - status: `no_essence_low_relevance`
  - reason: generic AI news roundup; Midjourney appears only in a short secondhand V8 pricing/speed segment.

## Verification

Latest main-thread validation:

```text
source_note_files=47
podcast_source_notes=16
youtube_source_notes=31
mismatched_block_quote_counts
forbidden_fields
short_quote_lines
frontmatter_missing
```

No output appeared under mismatched counts, forbidden fields, short quote lines, or missing frontmatter keys.

