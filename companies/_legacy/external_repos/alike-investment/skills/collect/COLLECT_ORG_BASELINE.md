# Collect Org Baseline

## Current Automation Scope

`/collect` currently auto-runs these organization-related modules:

- `org_basic`
  - Generates `discovery/organization/overview/org_structure.md`
  - Generates basic management profiles under `organization/c_suite/` and `organization/vp_level/`
- `founder`
  - Generates `discovery/sources/founder_voice.md`
  - Summarizes CEO/founder voice from local transcripts, web sources, and insider activity
- `org_scan`
  - Generates first-pass person profiles with source inventory
  - Creates `organization/_org_scan_report.md`
- `proxy_governance`
  - Pulls latest `DEF 14A`
  - Generates `organization/governance_summary.md`
  - Generates `organization/board/*.md` from proxy nominee parsing
- `validation`
  - Generates `discovery/_validation.json`
  - Generates `discovery/_validation.md`

## What This Means

The current `/collect` is no longer a pure raw-data fetcher. It is now an org-oriented intake pipeline that can produce:

- Basic org static map
- Founder / CEO voice starter pack
- First-pass executive profiles
- First-pass proxy / governance / board layer
- Explicit readiness validation for downstream org scoring

## What Is Good Enough To Auto-Trust

- Presence / absence of key artifacts
- SEC / earnings / YouTube / podcasts coverage
- Founder voice starter coverage
- Initial org map coverage
- Board nominee list and governance risk snapshot

## What Still Needs Human Review

- Board member deep biographies
- Departed executive tracking
- Committee / proxy / compensation detailed interpretation
- Executive network mapping
- Employee sentiment / former employee signals
- Cross-checking whether org evidence is strong enough for D1-D7

## Readiness Levels

- `minimum org dataset`
  - Founder voice exists
  - Org structure exists
  - Org scan report exists
- `high-quality org dataset`
  - Requires more than auto-generated starter docs
  - Still expects human or semi-manual deepening

## Operating Rule

If `_validation.json` says `high_quality_org_ready = false`, the company should not be treated as fully ready for high-confidence D1-D7 scoring.
