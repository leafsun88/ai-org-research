---
company: lovable
source_type: youtube
type: source_note_status
status: done
created_at: 2026-04-23
---

# Lovable YouTube Source Note Status — 2026-04-23

## Summary

- YouTube transcripts reviewed: 65
- Formal `_source_note.md` files in `companies/lovable/vault/youtube/essence/`: 36
- Skipped / duplicate / low relevance transcripts: 29
- Total insight blocks across formal YouTube source notes: 267
- Total quote blocks across formal YouTube source notes: 267
- Validation: `blocks == quotes` for all 36 source notes
- Old tool fields check: no `Evidence anchors`, `Tags`, `Report use`, `Fact Bank`, `关键引用`, `近原文证据`, `原文定位`, `可用于哪些分析角度`

## Notes Created Or Kept As Formal Source Notes

The formal set covers:

- 2025-03-09 Lenny / Anton canonical source note, repaired from the old tool-field format into the current source-note format.
- CEO / founder / company strategy interviews and panels.
- Growth / Elena Verna materials with incremental growth, brand, launch, and distribution evidence.
- Design, hiring, cofounder, office, and behind-the-scenes materials.
- Security / production / competitive boundary materials.
- Customer and operator stories with business-result, workflow, agency, education, SMB, and revenue evidence.

Formal notes are the files matching:

```text
companies/lovable/vault/youtube/essence/*_source_note.md
```

Old 2025-03-09 sample variants were moved to:

```text
companies/lovable/_legacy/youtube_source_note_samples_2026-04-23/
```

## Skipped Or Deduped Transcripts

These transcripts were reviewed but did not become full source notes:

- `2026-04-16_Everything-I-wish-I-knew-before-using-Lovable-tips.md` — low relevance tutorial / usage tips.
- `2026-04-16_Lovable-AI-is-INSANE--Build-Apps-Without-Coding-Fu.md` — low relevance tutorial / demo.
- `2026-04-16_Master-Lovable-AI-in-20-Minutes-NEW-20-UPDATE.md` — low relevance tutorial.
- `2026-04-16_STOP-Paying-25-a-Month-for-Lovable-Use-THIS-Instea.md` — low relevance tool-substitution tutorial.
- `2026-04-16_STOP-Wasting-Money-On-AI-Coding-Tools-Like-Lovable.md` — low relevance tool-substitution tutorial.
- `2026-04-21_5-Quick-Lovable-Tips-to-Build-Production-Ready-Applicat.md` — low relevance tips/tutorial.
- `2026-04-21_Build-a-SaaS-App-in-18-Mins-with-Lovable-Vibe-Coding-Tu.md` — low relevance tutorial.
- `2026-04-21_Build-an-AI-Agent-in-Lovable-that-Scrapes-ANYTHING-3-Pr.md` — low relevance tutorial.
- `2026-04-21_Building-5-AI-Apps-In-30-Minutes-ChatGPT-Lovable-Tutori.md` — low relevance tutorial compilation.
- `2026-04-21_Every-Level-of-Lovable-Explained-in-40-Minutes.md` — low relevance usage walkthrough.
- `2026-04-21_From-Idea-to-App-in-Hours-Vibe-Coding-Masterclass-with.md` — low relevance masterclass/tutorial.
- `2026-04-21_How-Anton-Osika-created-Worlds-Fastest-Growing-Company.md` — duplicate / low incremental signal, mostly founder-story recap.
- `2026-04-21_How-To-Vibe-Code-for-BeginnersLovable-Tutorial.md` — low relevance beginner tutorial.
- `2026-04-21_How-to-Build-an-App-From-SCRATCH-with-Lovable-Supabase.md` — low relevance Lovable + Supabase tutorial.
- `2026-04-21_How-to-Win-the-Lovable-Vibe-Coding-Hackathon.md` — low relevance hackathon tutorial / tips.
- `2026-04-21_I-Built-a-Voice-AI-Agent-to-Crush-My-PM-Interview-Vapi.md` — off-topic tutorial / PM interview app.
- `2026-04-21_Lovable-AI-How-to-Build-an-App-Upload-to-App-Store-Tuto.md` — low relevance app-store tutorial.
- `2026-04-21_Lovable-Head-of-Growth-on-The-New-AI-Native-Growth-Play.md` — duplicate of podcast source note `2025-11-26_Lovable-Head-of-Growth-on-The-New-AI-Native-Growth-Playbook_source_note.md`.
- `2026-04-21_Lovable-Tutorial-Build-Your-Business-App-Idea-in-Minute.md` — low relevance tutorial.
- `2026-04-21_Lovable-Tutorial-for-Beginners-Best-AI-App-Builder.md` — low relevance beginner tutorial.
- `2026-04-21_Lovable-in-15-Minutes-Build-an-App-Pitch-Deck-AND-Marke.md` — low relevance tutorial.
- `2026-04-21_Master-Lovable-In-24-Minutes.md` — low relevance tutorial.
- `2026-04-21_Master-Lovable-in-17-minutes-Starter-Tutorial.md` — low relevance starter tutorial.
- `2026-04-21_Product-Manager-Interview-Mock-Interview-Partner-w-Clau.md` — off-topic / not Lovable evidence.
- `2026-04-21_STOP-Wasting-Credits-Master-Lovable-AI-Vibe-Coding-Tuto.md` — low relevance credit-optimization tutorial.
- `2026-04-21_The-new-AI-growth-playbook-for-2026-How-Lovable-hit-200.md` — duplicate of podcast source note `2025-12-18_The-new-AI-growth-playbook-for-2026-How-Lovable-hit-200M-ARR_source_note.md`.
- `2026-04-21_Turn-Your-Idea-Into-a-Working-App-With-One-Prompt-Live.md` — low relevance live tutorial.
- `2026-04-21_Самый-быстрый-ИИ-стартап-в-истории-Lovable---сайт-в-1-к.md` — Russian secondhand translation / recap, duplicated by stronger Anton source notes.
- `2026-04-22_Base44-vs-Lovable-which-AI-app-builder-comes-out-on-top.md` — pure product trial / competitor comparison, no incremental Lovable organization or strategy evidence.

## Final Validation

Commands run from project root:

```bash
for f in companies/lovable/vault/youtube/essence/*_source_note.md; do
  b=$(rg -c '^## ' "$f" || true)
  q=$(rg -c '^[> ]*“' "$f" || true)
  test "$b" = "$q" || printf 'MISMATCH\t%s\tblocks=%s\tquotes=%s\n' "$f" "$b" "$q"
done
```

Result:

```text
notes=36
blocks=267
quotes=267
mismatches=0
```
