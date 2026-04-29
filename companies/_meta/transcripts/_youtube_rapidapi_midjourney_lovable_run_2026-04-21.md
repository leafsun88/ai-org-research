---
type: youtube_rapidapi_run_summary
date: 2026-04-21
status: current
---

# YouTube RapidAPI Run Summary: Midjourney / Lovable

## Scope

- Companies: `MIDJOURNEY`, `LOVABLE`
- Search provider: `rapidapi_metadata_search -> yt_dlp_search`
- Transcript provider: `rapidapi_transcript3 -> youtube_transcript_api -> yt_dlp_subtitle`
- Relevance gate: enabled before transcript download
- Key safety rule: broad aliases do not automatically qualify a video for transcript download

## Results

| Company | Search API calls | Passed candidates | Rejected before transcript | Transcript successes | Transcript failures | Vault transcript files | Characters |
|---|---:|---:|---:|---:|---:|---:|---:|
| Midjourney | 23 | 26 | 129 | 25 | 1 | 25 | 1,019,445 |
| Lovable | 27 | 63 | 64 | 63 | 0 | 63 | 2,297,555 |

## API Consumption Notes

- Clean run estimate from scratch:
  - Midjourney: 23 metadata search calls + 26 transcript calls
  - Lovable: 27 metadata search calls + 63 transcript calls
- Actual transcript calls recorded in final status files are lower when existing transcripts were reused:
  - Midjourney final status records 5 transcript provider calls because 22 files already existed from the first pass and were skipped on the clean rerun.
  - Lovable final status records 54 transcript provider calls because 9 files already existed and were skipped.
- Actual one-off development consumption was higher than a clean run because Midjourney was intentionally rerun after tightening the relevance gate.

## Output Paths

- Midjourney vault: `companies/midjourney/vault/youtube/`
- Lovable vault: `companies/lovable/vault/youtube/`
- Rejected candidates:
  - `companies/midjourney/vault/youtube/_youtube_rejected_candidates.json`
  - `companies/lovable/vault/youtube/_youtube_rejected_candidates.json`
- Stale / rejected previous files:
  - `companies/midjourney/vault/youtube/_stale_rejected/2026-04-21/`
  - `companies/lovable/vault/youtube/_stale_rejected/2026-04-21/`

## Follow-up Workers

- `Socrates`: Lovable podcast metadata/transcript rerun
- `Sagan`: Midjourney YouTube essence
- `Noether`: Lovable YouTube essence
