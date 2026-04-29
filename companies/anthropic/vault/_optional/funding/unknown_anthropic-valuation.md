---
company: "Anthropic"
research_key: ANTHROPIC
type: funding_compute
source: "www.longtermwiki.com"
title: "anthropic-valuation"
url: https://www.longtermwiki.com/knowledge-base/organizations/anthropic-valuation/
date: unknown
fetched_at: 2026-04-17T13:45:38
credibility: S2-S4
evidence: E2-E3
chars: 50149
---

# anthropic-valuation

**Source**: https://www.longtermwiki.com/knowledge-base/organizations/anthropic-valuation/
**Channel**: funding_compute

---

Skip to content

Toggle Sidebar

Organizations

Overview

Biosecurity Orgs

Community Building

Epistemic Orgs

Finance

AI Revenue Sources
Anthropic IPO
Anthropic Valuation Analysis
Situational Awareness LP
Value Aligned Research Advisors

Funders

Governance

Government

Industry

Labs

Safety Orgs

Venture Capital

Other

Navigation

Organizations

Overview

Biosecurity Orgs

Community Building

Epistemic Orgs

Finance

AI Revenue Sources
Anthropic IPO
Anthropic Valuation Analysis
Situational Awareness LP
Value Aligned Research Advisors

Funders

Governance

Government

Industry

Labs

Safety Orgs

Venture Capital

Other

Updated 2026-03-22HistoryData
Feedback

Citations verified6 accurate5 flagged8 unchecked

Page StatusContent

Edited 4 weeks ago2.3k words12 backlinksUpdated every 3 weeksOverdue by 5 days

72QualityGood •Quality: 72/100LLM-assigned rating of overall page quality, considering depth, accuracy, and completeness.Structure suggests 10034ImportanceReferenceImportance: 34/100How central this topic is to AI safety. Higher scores mean greater relevance to understanding or mitigating AI risk.58.5ResearchModerateResearch Value: 58.5/100How much value deeper investigation of this topic could yield. Higher scores indicate under-explored topics with high insight potential.

Content10/13

SummarySummaryBasic text summary used in search results, entity link tooltips, info boxes, and related page cards.ScheduleScheduleHow often the page should be refreshed. Drives the overdue tracking system.EntityEntityYAML entity definition with type, description, and related entries.Edit history3Edit historyTracked changes from improve pipeline runs and manual edits.OverviewOverviewA ## Overview heading section that orients readers. Helps with search and AI summaries.

Tables19/ ~9TablesData tables for structured comparisons and reference material.Diagrams1/ ~1DiagramsVisual content — Mermaid diagrams, charts, or Squiggle estimate models.Int. links19/ ~19Int. linksLinks to other wiki pages. More internal links = better graph connectivity.–Ext. links11/ ~12Ext. linksLinks to external websites, papers, and resources outside the wiki.Add links to external sourcesFootnotes19/ ~7FootnotesFootnote citations [^N] with source references at the bottom of the page.References18/ ~7ReferencesCurated external resources linked via <R> components or cited_by in YAML.–Quotes11/19QuotesSupporting quotes extracted from cited sources to back up page claims.crux citations extract-quotes <id>–Accuracy11/19AccuracyCitations verified against their sources for factual accuracy.crux citations verify <id>RatingsN:6 R:7 A:6 C:7RatingsSub-quality ratings: Novelty, Rigor, Actionability, Completeness (0-10 scale).Backlinks12BacklinksNumber of other wiki pages that link to this page. Higher backlink count means better integration into the knowledge graph.

Change History3

fix(calc-derive): robust JSON parsing, auto-fallback validation, prompt improvements#3288 weeks ago

Resumed issue #316 (thorough testing of crux facts calc pipeline across more pages).
Fixed three issues found through live testing: (1) switched from bare parseJsonResponse
to parseJsonFromLlm for resilient JSON parsing — eliminates silent parse failures;
(2) added auto-fallback in validateProposal to recover proposals blocked by table pipes
or excess-width originalText by retrying with just the match string; (3) tightened
system prompt with "ABSOLUTELY FORBIDDEN" language for | characters. Applied 3 ≈25x
→ <Calc> replacements in anthropic-valuation.mdx. Added 9 new validateOriginalText
tests (37 total in calc-derive.test.ts). Batch scan of 20 pages confirmed calc pipeline
correctly finds no derivable patterns in capabilities/cruxes pages — capability
multiples (compute cost reductions, inference speed) are not in the facts system.
All 7 gate checks pass, 609 tests pass.

sonnet-4-6 · ~25min · ~$1.50

Calc pipeline iteration: fix range facts, index mismatch, prompt quality8 weeks ago

Ran `crux facts calc` on anthropic-valuation and anthropic pages post-implementation, discovered and fixed three bugs: (1) range-valued facts ({min: N}) invisible to LLM and evaluator, (2) proposal-to-pattern index mismatch causing wrong validation expected values, (3) over-wide originalText proposals including JSX tags or prose. Applied validated Calc replacements to two pages (openai.39d6868e/$500B valuation now computes correctly).

sonnet-4 · ~40min

Migrate fact IDs from human-readable to hash-based8 weeks ago

Migrated all canonical fact IDs from human-readable slugs (e.g., `revenue-arr-2025`) to 8-char random hex hashes (e.g., `55d88868`), matching the pattern used by resources. Updated all YAML files, MDX references, build scripts, tests, LLM prompts, and documentation.

opus-4-6 · ~45min

Issues2

QualityRated 72 but structure suggests 100 (underrated by 28 points)

Links6 links could use <R> components

TODOs3

Track Q1 2026 revenue updates from both companies

Update customer concentration data as diversification progresses

Monitor OpenAI's $100B funding round closing and final valuation

Anthropic Valuation Analysis

Analysis
Anthropic Valuation Analysis

Valuation analysis updated March 2026. Series G closed at $380B (Feb 2026) with $14B run-rate; by March 2026, secondary/derivatives markets price Anthropic at ~$595B implied (Ventuals), a 57% premium over the primary round. Revenue grew to $19B run-rate, maintaining ≈31x multiple at secondary pricing — the 'Moderate Bull' scenario ($500-700B) is already materializing in derivatives markets. Bull case: 88% enterprise retention, coding benchmark leadership, dual AWS/Google Cloud partnerships. Bear case: 25%+ customer concentration (Cursor + GitHub Copilot), margin compression (50%→40%), AI bubble warnings.

Related

Organizations

AnthropicOrganizationAnthropicComprehensive reference page on Anthropic covering financials ($380B valuation, $14B ARR at Series G growing to $19B by March 2026), safety research (Constitutional AI, mechanistic interpretability...Quality: 74/100OpenAIOrganizationOpenAIComprehensive organizational profile of OpenAI documenting evolution from 2015 non-profit to Public Benefit Corporation, with detailed analysis of governance crisis, 2024-2025 ownership restructuri...Quality: 62/100

Analyses

Anthropic IPOAnalysisAnthropic IPOAnthropic is actively preparing for a potential 2026 IPO with concrete steps like hiring Wilson Sonsini and conducting bank discussions, though timeline uncertainty remains with prediction markets ...Quality: 65/100Anthropic (Funder)AnalysisAnthropic (Funder)Comprehensive model of EA-aligned philanthropic capital at Anthropic. At $380B valuation (Series G, Feb 2026, $30B raised): $27-76B risk-adjusted EA capital expected. Total funding raised exceeds $...Quality: 65/100

2.3k words · 12 backlinks

Contents

Page Scope

This page covers Anthropic valuation analysis. For company overview, see AnthropicOrganizationAnthropicComprehensive reference page on Anthropic covering financials ($380B valuation, $14B ARR at Series G growing to $19B by March 2026), safety research (Constitutional AI, mechanistic interpretability...Quality: 74/100. For IPO timeline, see Anthropic IPOAnalysisAnthropic IPOAnthropic is actively preparing for a potential 2026 IPO with concrete steps like hiring Wilson Sonsini and conducting bank discussions, though timeline uncertainty remains with prediction markets ...Quality: 65/100. For EA capital analysis, see Anthropic (Funder)AnalysisAnthropic (Funder)Comprehensive model of EA-aligned philanthropic capital at Anthropic. At $380B valuation (Series G, Feb 2026, $30B raised): $27-76B risk-adjusted EA capital expected. Total funding raised exceeds $...Quality: 65/100.

Data as of: March 2026. Key figures: Anthropic $380BValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation → valuation (Series G, Feb 2026), ≈$595B implied on secondary/derivatives markets (Ventuals, Mar 2026), $19BRevenue$19 billionAs of: Mar 2026Nearing $20B ARR; company guidance $20-26B for 2026Source: bloomberg.comsid_mK9pX3rQ7n.revenue → run-rate revenue; OpenAI $500BValuation$500 billionAs of: Oct 2025PBC restructuring valuation, October 2025Source: cnbc.comsid_1LcLlMGLbw.valuation → valuation, $20BRevenue$25 billionAs of: Feb 2026Annualized revenue run rate as of February 2026 per Sacra; up from $20B at end of 2025Source: sacra.comsid_1LcLlMGLbw.revenue → ARR.

Quick Assessment

MetricAnthropicOpenAIAssessment

Valuation$380BValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation → (Series G, Feb 2026)$500BValuation$500 billionAs of: Oct 2025PBC restructuring valuation, October 2025Source: cnbc.comsid_1LcLlMGLbw.valuation → (targeting $750-830B)OpenAI 1.3-2.2x larger

Revenue (Run Rate)$14BRevenue$14 billionAs of: Feb 2026Run-rate revenue at Series G announcement; 500+ customers spending $1M+ annuallySource: reuters.comsid_mK9pX3rQ7n.revenue → (Feb 2026)$20BRevenue$25 billionAs of: Feb 2026Annualized revenue run rate as of February 2026 per Sacra; up from $20B at end of 2025Source: sacra.comsid_1LcLlMGLbw.revenue → (Jan 2026)OpenAI 1.4x higher

Revenue Multiple≈27x≈20x≈20xCalculated$500.0 billion / $25.0 billionsid_1LcLlMGLbw.valuation=$500.0 billion(2025-10)sid_1LcLlMGLbw.revenue=$25.0 billion(2026-02), ≈41x (at $830B)Near parity

Gross Margin40%Gross Margin40%As of: Dec 2025Actual 2025 gross margin; 10 percentage points below previous estimate; inference costs surged 23% more than expectedSource: theinformation.comsid_mK9pX3rQ7n.gross-margin → (revised down)40-50% (70% compute margin)Similar, both under pressure

Enterprise Retention88%UnknownAnthropic above industry (76% avg)

Path to Breakeven2028UnknownAnthropic more transparent

Overview

AnthropicOrganizationAnthropicComprehensive reference page on Anthropic covering financials ($380B valuation, $14B ARR at Series G growing to $19B by March 2026), safety research (Constitutional AI, mechanistic interpretability...Quality: 74/100's $380 billionValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation → valuation (February 2026 Series G) reflects rapid revenue growth from $9BRevenue$9.0 billionAs of: Dec 2025Run-rate exceeding $9B at end of 2025Source: finance.yahoo.comsid_mK9pX3rQ7n.revenue → at end of 2025 to $14BRevenue$14 billionAs of: Feb 2026Run-rate revenue at Series G announcement; 500+ customers spending $1M+ annuallySource: reuters.comsid_mK9pX3rQ7n.revenue → run-rate by the time of the funding round. At ≈27x current revenue, Anthropic now trades at a multiple closer to OpenAIOrganizationOpenAIComprehensive organizational profile of OpenAI documenting evolution from 2015 non-profit to Public Benefit Corporation, with detailed analysis of governance crisis, 2024-2025 ownership restructuri...Quality: 62/100's ≈20x≈20xCalculated$500.0 billion / $25.0 billionsid_1LcLlMGLbw.valuation=$500.0 billion(2025-10)sid_1LcLlMGLbw.revenue=$25.0 billion(2026-02) (at $500BValuation$500 billionAs of: Oct 2025PBC restructuring valuation, October 2025Source: cnbc.comsid_1LcLlMGLbw.valuation → with $20BRevenue$25 billionAs of: Feb 2026Annualized revenue run rate as of February 2026 per Sacra; up from $20B at end of 2025Source: sacra.comsid_1LcLlMGLbw.revenue → ARR)—a convergence from the ≈39x multiple at the previous $350B valuation with $9BRevenue$9.0 billionAs of: Dec 2025Run-rate exceeding $9B at end of 2025Source: finance.yahoo.comsid_mK9pX3rQ7n.revenue → revenue.

This page provides an investment-grade analysis of scenarios across different outcomes, incorporating data on customer concentration, margin pressure, and competitive dynamics.1

Updated thesis: The revenue multiple gap between Anthropic and OpenAI has narrowed substantially (≈27x vs 25x). The remaining difference may reflect enterprise performance metrics (88% retention, 80% enterprise revenue, 500+ million-dollar customers) and coding benchmark positioning—or may indicate persistent valuation risk given customer concentration and margin compression.

Current Valuation Context

Revenue Multiple Comparison

CompanyValuationRevenue (Run Rate)MultipleData Source

Anthropic$380BValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation → (Series G, Feb 2026)$14BRevenue$14 billionAs of: Feb 2026Run-rate revenue at Series G announcement; 500+ customers spending $1M+ annuallySource: reuters.comsid_mK9pX3rQ7n.revenue → (Feb 2026)≈27xAnthropic

Anthropic (prev.)$350B (Nov 2025)$9BRevenue$9.0 billionAs of: Dec 2025Run-rate exceeding $9B at end of 2025Source: finance.yahoo.comsid_mK9pX3rQ7n.revenue → (end 2025)≈39xBloomberg

OpenAI$500BValuation$500 billionAs of: Oct 2025PBC restructuring valuation, October 2025Source: cnbc.comsid_1LcLlMGLbw.valuation →$20BRevenue$25 billionAs of: Feb 2026Annualized revenue run rate as of February 2026 per Sacra; up from $20B at end of 2025Source: sacra.comsid_1LcLlMGLbw.revenue → (Jan 2026)≈20x≈20xCalculated$500.0 billion / $25.0 billionsid_1LcLlMGLbw.valuation=$500.0 billion(2025-10)sid_1LcLlMGLbw.revenue=$25.0 billion(2026-02)i10x

OpenAI (proposed)$750-830B$20BRevenue$25 billionAs of: Feb 2026Annualized revenue run rate as of February 2026 per Sacra; up from $20B at end of 2025Source: sacra.comsid_1LcLlMGLbw.revenue →37-41xTechCrunch

Key insight: Anthropic's revenue growth from $9BRevenue$9.0 billionAs of: Dec 2025Run-rate exceeding $9B at end of 2025Source: finance.yahoo.comsid_mK9pX3rQ7n.revenue → to $14BRevenue$14 billionAs of: Feb 2026Run-rate revenue at Series G announcement; 500+ customers spending $1M+ annuallySource: reuters.comsid_mK9pX3rQ7n.revenue → compressed its revenue multiple from ≈39x to ≈27x, bringing it closer to ≈20x≈20xCalculated$500.0 billion / $25.0 billionsid_1LcLlMGLbw.valuation=$500.0 billion(2025-10)sid_1LcLlMGLbw.revenue=$25.0 billion(2026-02). The valuation itself only increased 8.6% ($350B → $380BValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation →) while revenue grew 56%. If OpenAI closes its $100B round at $830B, OpenAI would trade at ≈41x—above Anthropic's current multiple.2

Revenue Growth Trajectories

Company20242025Current Run Rate2026 (Guidance)2027 (Projected)

Anthropic$1B$9BRevenue$9.0 billionAs of: Dec 2025Run-rate exceeding $9B at end of 2025Source: finance.yahoo.comsid_mK9pX3rQ7n.revenue →$14BRevenue$14 billionAs of: Feb 2026Run-rate revenue at Series G announcement; 500+ customers spending $1M+ annuallySource: reuters.comsid_mK9pX3rQ7n.revenue → (Feb 2026)$20-26B$34.5B

OpenAI$6B$20BRevenue$25 billionAs of: Feb 2026Annualized revenue run rate as of February 2026 per Sacra; up from $20B at end of 2025Source: sacra.comsid_1LcLlMGLbw.revenue →$20BRevenue$25 billionAs of: Feb 2026Annualized revenue run rate as of February 2026 per Sacra; up from $20B at end of 2025Source: sacra.comsid_1LcLlMGLbw.revenue → (Jan 2026)$46B (2.3x)$92B (2x)

Both companies are growing rapidly. OpenAI projects reaching $100B revenue by 2028.3

Valuation Progression

DateRoundValuationRevenue (ARR)Multiple

May 2021Series A$550M≈$0—

April 2022Series B$4B≈$10M400x

March 2025Series E$61.5B≈$1B62x

Sept 2025Series F$183B≈$4B46x

Nov 2025Microsoft/Nvidia$350B≈$9BRevenue$9.0 billionAs of: Dec 2025Run-rate exceeding $9B at end of 2025Source: finance.yahoo.comsid_mK9pX3rQ7n.revenue →≈39x

Feb 2026Series G$380BValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation →≈$14BRevenue$14 billionAs of: Feb 2026Run-rate revenue at Series G announcement; 500+ customers spending $1M+ annuallySource: reuters.comsid_mK9pX3rQ7n.revenue →≈27x

Multiple compression from 400x to ≈27x reflects a business with rapidly growing revenue scaling toward profitability.

Secondary Market Pricing (March 2026)

By mid-March 2026, secondary/derivatives markets showed a dramatic divergence from the Series G price:

PlatformShare PriceImplied Valuationvs. Series GType

Employee tender offerat $350B pre-money$350B-8%Company-run; Bloomberg

Premier Alternatives$186≈$273B-28%OTC; Premier

Notice$252≈$370B-3%OTC; Notice

Forge Global$259≈$380B0%OTC; Forge

UpMarket≈$370≈$542B+43%OTC; UpMarket

Hiive$474≈$695B+83%Indicative (0 orders); Hiive

Ventuals mark≈$596≈$595B+57%Derivatives; Ventuals

Secondary market pricing shows extreme dispersion in March 2026 — from a 28% discount (Premier Alternatives) to an 83% premium (Hiive indicative). Traditional OTC platforms cluster around $250-380/share (near or below Series G), while forward-looking platforms (UpMarket, Ventuals, Hiive) price at significant premiums. The employee tender offer at $350B pre-money sets a company-endorsed floor below the Series G post-money price.

At the higher end ($542-695B implied), the revenue multiple with $19B run-rate would be ≈29-37x — still within the range of recent AI company multiples. A Polymarket contract on "Anthropic $500B+ valuation in 2026" is actively trading, suggesting meaningful market-implied probability that the next primary round exceeds $500B.

Important caveats: Hiive's $474 price has zero live orders and may be algorithmic. Ventuals is a derivatives/prediction market, not a traditional OTC market. The wide price range underscores deep uncertainty about fair value for a company growing this rapidly.

Bull Case: Data Supporting Higher Valuation

1. Enterprise Performance Metrics

Anthropic's enterprise metrics exceed industry benchmarks:

MetricAnthropicIndustry AverageDifference

Enterprise retention88%76%+12 percentage points

Revenue from enterprise80%VariesHigh-quality revenue

Multi-year commitmentsGrowingUncommonImproved forecasting

Large accounts (>$100K)7x YoY growth—Expansion pattern

The 88% retention rate indicates product-market fit and switching costs. Enterprise contracts include SLA guarantees, compliance certifications (HIPAA, SOC 2 Type II, ISO 27001), and custom data retention policies that create lock-in.45

2. Coding Benchmark Performance

Claude leads commercially important software development benchmarks:

BenchmarkClaude Opus 4.5GPT-5.2Gemini 3 ProLeader

SWE-bench Verified80.9%74.9%76.8%Claude

Terminal-bench 2.059.3%——Claude

Prompt injection resistance4.7% success21.9%12.5%Claude

AIME 2025 (math)—100%—GPT-5.2

GPQA Diamond (science)——91.9%Gemini

Claude leads in SWE-bench (software engineering tasks) and security (lowest prompt injection rate). No single model dominates all categories—GPT-5.2 leads reasoning, Gemini leads multimodal.67

3. Dual Cloud Infrastructure Partnerships

Anthropic has secured infrastructure commitments from both major cloud providers:

Amazon Web Services:

$10.75B total investment from Amazon

1 million+ Trainium2 chips committed

$11B dedicated data center in Indiana

Projected $1.28B → $3B → $5.6B AWS revenue (2025 → 2026 → 2027)

Google Cloud:

"Tens of billions" TPU deal announced October 2025

Expands beyond AWS dependency

Access to both Trainium and TPU architectures89

This dual-cloud strategy reduces infrastructure risk and provides leverage in chip negotiations.

4. Technical Leadership Team

Anthropic's founding team includes researchers from OpenAIOrganizationOpenAIComprehensive organizational profile of OpenAI documenting evolution from 2015 non-profit to Public Benefit Corporation, with detailed analysis of governance crisis, 2024-2025 ownership restructuri...Quality: 62/100:

Founding Team (7 ex-OpenAI researchers):

Dario AmodeiPersonDario AmodeiComprehensive biographical profile of Anthropic CEO Dario Amodei documenting his competitive safety development philosophy, 10-25% catastrophic risk estimate, 2026-2030 AGI timeline, and Constituti...Quality: 41/100 (CEO) - Former VP Research at OpenAI

Daniela AmodeiPersonDaniela AmodeiBiographical profile of Anthropic's President covering her education, early career, roles at Stripe and OpenAI, and her operational and commercial leadership at Anthropic. Includes fundraising hist...Quality: 21/100 (President) - Former VP Operations at OpenAI

Chris OlahPersonChris OlahComprehensive biographical profile of Chris Olah covering his unconventional career path, foundational contributions to mechanistic interpretability (feature visualization, circuit analysis, sparse...Quality: 27/100 - InterpretabilityResearch AreaInterpretabilityMechanistic interpretability has extracted 34M+ interpretable features from Claude 3 Sonnet with 90% automated labeling accuracy and demonstrated 75-85% success in causal validation, though less th...Quality: 66/100 researcher

Tom BrownPersonTom BrownA biographical wiki page on Tom B. Brown covering his foundational contributions to GPT-3, RLHF, and AI alignment; reasonably thorough but hampered by opaque sourcing (no URLs, just 'research data'... - Lead author of GPT-3

Jared KaplanPersonJared KaplanComprehensive biographical profile of Jared Kaplan covering his scaling laws research, Anthropic co-founder role, and Responsible Scaling Officer appointment, with notable coverage of RSP enforceme... - Scaling laws researcher

Key Acquisitions:

Jan LeikePersonJan LeikeBiography of Jan Leike covering his career from Australian National University through DeepMind, OpenAI's Superalignment team, to his current role as VP of Alignment Science at Anthropic. Documents...Quality: 27/100 (2024) - Former OpenAI Superalignment co-lead

John SchulmanPersonJohn SchulmanCo-founder of OpenAI. Researcher known for foundational work on reinforcement learning, including Proximal Policy Optimization (PPO) and TRPO. Joined Anthropic in 2024. (2024) - OpenAI co-founder, invented PPO algorithm

Holden KarnofskyPersonHolden KarnofskyHolden Karnofsky directed $300M+ in AI safety funding through Coefficient Giving (formerly Open Philanthropy), growing the field from ~20 to 400+ FTE researchers and developing influential framewor...Quality: 40/100 (2025) - Coefficient GivingOrganizationCoefficient GivingCoefficient Giving (formerly Open Philanthropy) has directed $4B+ in grants since 2014, including $336M to AI safety (~60% of external funding). The organization spent ~$50M on AI safety in 2024, w...Quality: 55/100 co-founder

Team Scale:

Interpretability team: 40-60Interpretability Team Size50As of: Dec 2025Estimate; no published source. Estimated 40-60 researchers; among the largest concentrations globallysid_mK9pX3rQ7n.interpretability-team-size → researchers (largest globally)

Safety researchers: 200-330Safety Researchers265As of: Dec 2025Estimate; no published source. Estimated 200-330 across interpretability, alignment science, policy, trust & safety; ~20-30% of technical staffsid_mK9pX3rQ7n.safety-researcher-count → (20-30% of technical staff)

5. Open Source Competition Dynamics

Open-source models' enterprise market share has declined:

Metric20242025Trend

Open source enterprise share19%11%Declining

Llama enterprise productionHigher9%Declining

Anthropic/OpenAI/Google share—88%Consolidating

Llama 4's launch underperformed in real-world settings according to enterprise surveys. The performance gap between open and proprietary models widened throughout 2024-2025.10

Bear Case: Data Indicating Valuation Risk

1. Customer Concentration Risk

Anthropic's revenue shows concentration in two customers:

CustomerEstimated RevenueShare of Total

Cursor≈$600M≈13%

GitHub Copilot≈$600M≈13%

Combined≈$1.2B≈25%+

Approximately 25% of Anthropic's revenue comes from two coding tool customers. If either relationship ends or shifts to a competitor, revenue would decline. This concentration in AI-assisted coding also means Anthropic is vulnerable to disruption in that specific market.11

2. Gross Margin Revision

Anthropic revised its gross margin forecast:

MetricOriginal ForecastRevised ForecastChange

2025 Gross Margin50%40%Gross Margin40%As of: Dec 2025Actual 2025 gross margin; 10 percentage points below previous estimate; inference costs surged 23% more than expectedSource: theinformation.comsid_mK9pX3rQ7n.gross-margin →-10 percentage points

Cause—Rising inference costsStructural

AI inference costs scale with usage. Unlike traditional software with near-zero marginal costs, every AI query consumes compute. As revenue grows, costs grow—potentially faster than efficiency gains can offset.1213

For comparison, OpenAI reports 70% "compute margin" but overall gross margins are 40-50% after partner revenue shares and free-tier subsidies.14

3. AI Valuation Environment Assessments

Multiple sources have characterized current AI valuations as elevated:

SourceStatementDate

Sam AltmanPersonSam AltmanComprehensive biographical profile of Sam Altman documenting his role as OpenAI CEO, timeline predictions (AGI within presidential term, superintelligence in "few thousand days"), and controversies...Quality: 40/100 (OpenAI CEO)"AI bubble is ongoing"2025

Jamie Dimon (JPMorgan)"Higher chance of meaningful drop" than markets reflect2025

DeepSeek launch impactNvidiaOrganizationNVIDIANVIDIA holds 90-95% of the AI accelerator market, with its H100, H200, and B200 GPUs powering virtually all frontier AI training. Revenue reached $130.5B in FY2025 (114% YoY growth), driven almost ... dropped 17% in one dayJan 2025

Market concentration30% of S&P 500 in 5 companies—highest concentration in half a centuryLate 2025

When the CEO of OpenAI characterizes the market as experiencing bubble conditions, valuations across the sector face uncertainty.1516

4. Benchmark Distribution Across Categories

While Claude leads coding, it does not lead all categories:

CategoryLeaderClaude's Position

CodingClaude#1

Mathematical reasoningGPT-5.2Behind

Scientific knowledgeGemini 3 ProBehind

Multimodal/contextGemini (1M tokens)Smaller context

The market appears to be evolving toward model routing—using different models for different tasks—rather than winner-take-all. This limits any single company's ability to capture the entire market.17

5. OpenAI's Scale Position

OpenAI has scale advantages in certain metrics:

MetricOpenAIAnthropicGap

Weekly active users800MUnknownLarge differential

Revenue$20BRevenue$25 billionAs of: Feb 2026Annualized revenue run rate as of February 2026 per Sacra; up from $20B at end of 2025Source: sacra.comsid_1LcLlMGLbw.revenue →$14BRevenue$14 billionAs of: Feb 2026Run-rate revenue at Series G announcement; 500+ customers spending $1M+ annuallySource: reuters.comsid_mK9pX3rQ7n.revenue →1.4x

Total raised—$67B+Total Funding Raised$67 billionAs of: Feb 2026Total funding raised as of Series G (Feb 2026), per Reuters. Includes Series A-G equity rounds plus Amazon's $10.75B and Google's $3.3B strategic investments. Excludes Microsoft/Nvidia 'up to $15B' commitment (not fully deployed). The FTX ~$500M investment (2022) was sold to creditors after FTX's collapse and is not counted in the live total.Source: reuters.comsid_mK9pX3rQ7n.total-funding →—

Valuation (proposed)$750-830B$380BValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation →2.0-2.2x

If OpenAI raises $100B at $830B, it will have capital to invest in compute, talent, and product development.18

Revised Valuation Scenarios

Given updated data, probability-weighted scenarios:

ScenarioValuationMultiple vs CurrentProbabilityKey Drivers

Bear$175-250B0.5-0.7x15-20%Market correction, customer churn

Base$380BValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation →1x40-50%Status quo, margin pressure offsets growth

Moderate Bull$500-700B1.3-1.8x20-30%Diversified customers, sustained growth

Strong Bull$1-1.75T2.6-4.6x5-10%Market leadership, AGI progress

Diagram (loading…)flowchart LR
 BEAR[Bear: $175-250B] --> BASE[Base: $380B]
 BASE --> MODERATE[Moderate Bull: $500-700B]
 MODERATE --> STRONG[Strong Bull: $1T+]

 style BEAR fill:#ffcccc
 style BASE fill:#ffffcc
 style MODERATE fill:#ccffcc
 style STRONG fill:#ccccff

Key changes since previous analysis: (1) The Series G at $380BValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation → and $14BRevenue$14 billionAs of: Feb 2026Run-rate revenue at Series G announcement; 500+ customers spending $1M+ annuallySource: reuters.comsid_mK9pX3rQ7n.revenue → revenue (≈27x multiple) compressed the revenue multiple toward OpenAI's level. (2) As of March 2026, secondary/derivatives markets are pricing Anthropic at ≈$595B — already in the "Moderate Bull" range. Revenue has also grown to $19BRevenue$19 billionAs of: Mar 2026Nearing $20B ARR; company guidance $20-26B for 2026Source: bloomberg.comsid_mK9pX3rQ7n.revenue → run-rate, maintaining a ≈31x multiple at secondary pricing. The question is whether the next primary round will validate or trail secondary market levels.

Unit Economics Analysis

Gross Margin Comparison

CompanyCompute MarginOverall Gross MarginTrend

AnthropicUnknown40%Gross Margin40%As of: Dec 2025Actual 2025 gross margin; 10 percentage points below previous estimate; inference costs surged 23% more than expectedSource: theinformation.comsid_mK9pX3rQ7n.gross-margin → (revised)Declining

OpenAI70%40-50%Improving

Mature SaaSN/A70-80%Stable

AI companies operate with structurally lower margins than traditional SaaS due to inference costs. This may improve with efficiency gains, but the timeline is uncertain.

Path to Profitability

MilestoneAnthropicOpenAI

Stop burning cash2027Unknown

Breakeven2028"Years away"

Positive FCF2027 (projected $17B by 2028)Unknown

Anthropic projects reaching breakeven in 2028, which provides visibility into profitability timeline.19

Implications for Stakeholders

For Investors

ScenarioReturnRisk Assessment

Bear (-50%)-50%Customer concentration, market correction

Base (0%)0%Current pricing reflects fair value at $380BValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation →

Moderate Bull (+30-85%)+30-85%Growth execution, multiple expansion

Strong Bull (+160%+)+160%+Market dominance, requires sustained execution

The risk/reward profile has shifted since Anthropic's revenue multiple compressed from ≈39x to ≈27x. The downside risk from multiple compression is reduced, though sector-wide corrections remain a risk.

For EA-Aligned Capital

See Anthropic (Funder)AnalysisAnthropic (Funder)Comprehensive model of EA-aligned philanthropic capital at Anthropic. At $380B valuation (Series G, Feb 2026, $30B raised): $27-76B risk-adjusted EA capital expected. Total funding raised exceeds $...Quality: 65/100 for detailed philanthropic capital analysis:

ValuationRisk-Adjusted EA Capital

$175B (bear)$12-35B

$380BValuation$380 billionAs of: Feb 2026Series G post-money valuation; second-largest venture deal ever behind OpenAI's $40BSource: reuters.comsid_mK9pX3rQ7n.valuation → (current)$27-76B

$700B (moderate bull)$50-140B

$1T+ (strong bull)$70-200B+

For the AI Safety Field

Anthropic's trajectory affects the field regardless of exact valuation:

Talent attraction: Valuations at current levels attract safety researchers

Model legitimacy: Demonstrates "safety lab" can compete commercially

Research funding: Higher valuations fund more safety research

Industry influence: Commercial success encourages competitors to adopt safety practices

Key Uncertainties

UncertaintyIf Resolves PositiveIf Resolves Negative

Customer concentrationDiversifies, reduces riskMajor customer churns

Margin trajectoryEfficiency gains, 50%+ marginsContinues declining

Benchmark performanceMaintains/extends coding leadLoses to GPT/Gemini

Market dynamicsSoft landingSharp correction

OpenAI executionOpenAI stumblesOpenAI pulls ahead

Methodology Notes

This analysis uses:

February 2026 revenue data where available (Anthropic Series G announcement)

Multiple independent sources for each claim

Explicit acknowledgment of prior errors

Risk-weighted scenario probabilities

Limitations:

Private company financials are estimates

Customer concentration data is from single source

Margin data may be self-reported

Competitive benchmark data varies by source

Footnotes

Citation rc-e56b ↩

Citation rc-e9a4 ↩

Citation rc-9e97 ↩

Citation rc-4dc1 ↩

Citation rc-98de ↩

Citation rc-aaa9 ↩

Citation rc-88bb ↩

Citation rc-1849 ↩

Citation rc-a277 ↩

Citation rc-ad66 ↩

Citation rc-4b92 ↩

Citation rc-3497 ↩

Citation rc-fc26 ↩

Citation rc-3a5f ↩

Citation rc-8735 ↩

Citation rc-635e ↩

Citation rc-5ccc ↩

Citation rc-49a6 ↩

Citation rc-a5a0 ↩

References

1Deep Research Global - Anthropic Company Analysisdeepresearchglobal.com▸

A business and strategic analysis of Anthropic, covering the company's mission, competitive positioning, funding landscape, and outlook as a leading AI safety-focused organization. The report examines Anthropic's approach to balancing commercial viability with its safety-first research mandate.

deepresearchglobal.com

Claims (1)

Anthropic projects reaching <F e="anthropic" f="023e1116">breakeven in 2028</F>, which provides visibility into profitability timeline.

Minor issues90%Feb 22, 2026

“Unlike OpenAI, Anthropic projects positive free cash flow by 2027 with potential $17 billion in cash flow by 2028, demonstrating superior unit economics.”
The claim states that Anthropic projects reaching breakeven in 2028, but the source states that Anthropic projects positive free cash flow by 2027 with potential $17 billion in cash flow by 2028.

2Epoch AI - OpenAI Revenue ProjectionsSubstack·Blog post▸

Epoch AI analyzes OpenAI's ambitious revenue projections, examining the scale and pace of expected growth in the AI industry. The analysis contextualizes these projections within broader trends in AI commercialization and compute investment, offering perspective on what such growth would mean for the trajectory of AI development.

★★☆☆☆

epochai.substack.com

Claims (1)

OpenAI projects reaching \$100B revenue by 2028.

Accurate100%Feb 22, 2026

“According to The Information , in Q3 2025 OpenAI projected its 2028 revenue to be $100 billion .”

3Getlatka - Anthropic Customer Datagetlatka.com▸

A third-party SaaS database profile of Anthropic providing business metrics including reported 2025 revenue of $5B, 2400% year-over-year growth, 300K customers, and $22.6B in total funding. The page aggregates financial and operational data about Anthropic sourced from founder interviews and public records. It serves primarily as a business intelligence reference rather than an AI safety resource.

getlatka.com

Claims (1)

Enterprise contracts include SLA guarantees, compliance certifications (HIPAA, SOC 2 Type II, ISO 27001), and custom data retention policies that create lock-in.

4WebProNews - Anthropic Cost Surgewebpronews.com▸

Anthropic revised its 2025 gross margin forecast down to 40% from 50% due to rising AI inference costs, even as revenue surged from $1 billion in 2024 to approximately $10 billion in 2025. The article highlights the tension between explosive AI revenue growth and the high computational costs of running increasingly complex models. Projections suggest revenue could reach $26 billion by 2026, with a potential IPO on the horizon.

webpronews.com

Claims (1)

As revenue grows, costs grow—potentially faster than efficiency gains can offset.

Accurate100%Feb 22, 2026

“This juxtaposition highlights a broader tension in the AI industry: explosive growth potential clashing with the high costs of innovation.”

5Menlo Ventures - 2025 Mid-Year LLM Market Updatemenlovc.com▸

Menlo Ventures' mid-2025 report analyzes the enterprise LLM market, finding that Anthropic has surpassed OpenAI in enterprise usage, model API spending has more than doubled to $8.4B, and AI spend is shifting from training to inference. Key findings include that enterprises switch models for performance rather than price, and open-source adoption has plateaued.

menlovc.com

Claims (1)

The performance gap between open and proprietary models widened throughout 2024-2025.

Accurate100%Feb 22, 2026

“But despite these benefits and recent improvements, open-source has continued to trail frontier, closed-source models in performance by nine to 12 months.”

6Vellum - Flagship Model Reportvellum.ai▸

Vellum's flagship model report analyzes the latest frontier AI releases (GPT-5.1, Gemini 3 Pro, Claude Opus 4.5) against the backdrop of scaling limits and a shift toward agentic AI systems. It identifies three major trends: the rise of long-context agents, infrastructure as a competitive differentiator, and growing enterprise adoption challenges. The report situates these developments within broader national AI initiatives like the US Genesis Mission.

vellum.ai

Claims (1)

No single model dominates all categories—GPT-5.2 leads reasoning, Gemini leads multimodal.

Accurate100%Feb 22, 2026

“Frontier models now compete on one question: which one is best for this agent and this job? No single model wins in every single category.”

7Wikipedia, "AI bubble" (https://en.wikipedia.org/wiki/AI_bubble)Wikipedia·Reference▸

Wikipedia's overview of the theorized AI stock market bubble, examining concerns about circular investment flows artificially inflating AI company valuations, comparisons to the dot-com bubble, and evidence including Nvidia's dramatic valuation growth and reports that 95% of organizations see zero return on GenAI investment.

★★★☆☆

en.wikipedia.org

Claims (1)

When the CEO of OpenAI characterizes the market as experiencing bubble conditions, valuations across the sector face uncertainty.

8TechCrunch - OpenAI \$100B Raise at \$830B ValuationTechCrunch▸

TechCrunch reports that OpenAI is attempting to raise $100 billion in new funding at an $830 billion valuation, targeting completion by end of Q1 2026. The company is reportedly courting sovereign wealth funds as potential investors in this round, reflecting the massive capital demands of frontier AI development.

★★★☆☆

techcrunch.com

Claims (1)

If OpenAI raises \$100B at \$830B, it will have capital to invest in compute, talent, and product development.

Unsupported0%Feb 22, 2026

“The funding would come as OpenAI commits to spend trillions of dollars and strikes deals around the world as the company tries to stay ahead in the race to develop AI technology.”
The source does not mention that OpenAI will have capital to invest in compute, talent, and product development if it raises $100B at $830B.

9SaaStr - OpenAI Compute Margin Analysissaastr.com▸

Analyzes OpenAI's reported compute margin improvement from 35% to 70% between early 2024 and October 2025, arguing that while foundation model economics are improving, B2B AI startups face a 'treadmill problem' where cost savings on older models are offset by rising costs of frontier models and agentic workflows consuming 10x-100x more tokens.

saastr.com

Claims (1)

For comparison, OpenAI reports 70% "compute margin" but overall gross margins are 40-50% after partner revenue shares and free-tier subsidies.

Unsupported0%Feb 22, 2026

“OpenAI’s compute margin on paid products is now about 70% as of October which is roughly double early 2024 levels.”
The source does not mention OpenAI's overall gross margins after partner revenue shares and free-tier subsidies.

10AI Certs - Anthropic Enterprise Metricsaicerts.ai▸

This article from AICerts covers Anthropic's improving financial trajectory driven by surging enterprise adoption of its Claude AI models. It highlights key business metrics indicating the company is moving toward profitability as large organizations increasingly deploy its AI products. The piece contextualizes Anthropic's commercial growth within the broader competitive landscape of AI companies.

aicerts.ai

Claims (1)

Enterprise contracts include SLA guarantees, compliance certifications (HIPAA, SOC 2 Type II, ISO 27001), and custom data retention policies that create lock-in.

Unsupported30%Feb 22, 2026

“Enterprise traction boosts Anthropic profitability by bundling support, security, and compliance into predictable invoices.”
The source mentions enterprise contracts but does not specify that they include SLA guarantees, compliance certifications (HIPAA, SOC 2 Type II, ISO 27001), or custom data retention policies.

11Oliver Wyman - Impact of AI Bubble Burst on Global Financial Marketsoliverwyman.com▸

This Oliver Wyman analysis examines the potential systemic financial risks if current AI investment enthusiasm constitutes a bubble and it subsequently bursts. It explores how overvaluation in AI-related assets could trigger broader market contagion, credit tightening, and macroeconomic instability similar to past tech bubbles.

oliverwyman.com

Claims (1)

When the CEO of OpenAI characterizes the market as experiencing bubble conditions, valuations across the sector face uncertainty.

12Fello AI - Best AI of December 2025felloai.com▸

A curated roundup of the most notable AI tools, models, and releases from December 2025, compiled by Fello AI. The resource serves as a reference snapshot of the AI landscape at a specific point in time, highlighting standout capabilities and products.

felloai.com

Claims (1)

This limits any single company's ability to capture the entire market.

Unsupported0%Feb 22, 2026

“Even if Gemini, Claude, and OpenAI dominate the top spots, a few other frontier models matter depending on your constraints (cost, privacy, self-hosting, or speed).”

13VentureBeat - Anthropic Customer ConcentrationVentureBeat▸

A VentureBeat article reporting on Anthropic's financial vulnerability due to heavy customer concentration, with revenue dependent on just two major customers, while intensifying price competition among AI providers threatens profit margins across the industry.

★★★☆☆

venturebeat.com

Claims (1)

This concentration in AI-assisted coding also means Anthropic is vulnerable to disruption in that specific market.

14Anthropic: Raises \$30 Billion Series G Funding at \$380 Billion Post-Money ValuationAnthropic▸

Anthropic announced a major Series G funding round, reflecting significant investor confidence in safety-focused AI development. The round highlights the growing capital flowing into frontier AI labs and the commercial viability of safety-oriented AI research organizations.

★★★★☆

anthropic.com

Claims (1)

This page provides an investment-grade analysis of scenarios across different outcomes, incorporating data on customer concentration, margin pressure, and competitive dynamics.

15Anthropic's Revenue Run Rate Tops $9 Billion as VCs Pile InBloomberg▸

Bloomberg reports that Anthropic's annualized revenue run rate has surpassed $9 billion, reflecting rapid commercial growth driven by enterprise adoption of Claude and continued heavy investment from venture capital. This milestone signals Anthropic's emergence as a major commercial AI lab alongside OpenAI, with significant implications for the competitive AI landscape and its ability to fund safety research.

★★★★☆

bloomberg.com

Claims (1)

If OpenAI closes its \$100B round at \$830B, OpenAI would trade at ≈41x—above Anthropic's current multiple.

16Bloomberg▸

★★★★☆

bloomberg.com

17Anthropic Secondary Market Price Tracker - Premier Alternativespremieralts.com▸

A financial data page tracking the secondary market valuation and share price of Anthropic, the AI safety company. This resource provides investors and analysts with real-time or regularly updated pricing information for Anthropic's privately-held equity on secondary markets.

premieralts.com

18Ventuals - Buy Anthropic (Investment Platform)app.ventuals.com▸

This page appears to be a financial trading or investment platform allowing users to purchase shares or tokens related to Anthropic, the AI safety company. The content is extremely sparse and provides no substantive information about AI safety, Anthropic's research, or related topics.

app.ventuals.com

Citation source check: 5 verified, 8 unchecked of 19 total

Related Wiki Pages

Top Related Pages

Analysis

Anthropic IPO

Tracking Anthropic's preparation for a potential 2026 initial public offering, including timeline estimates, valuation trajectory, competitive dyna...

Analysis

Anthropic (Funder)

Analysis of EA-aligned philanthropic capital at Anthropic, including founder pledges, investor stakes, and employee matching programs. $27-76B risk...

Organization

Anthropic

An AI safety company founded by former OpenAI researchers that develops frontier AI models while pursuing safety research, including the Claude mod...

Table

Anthropic Stakeholders

Who owns Anthropic and how much: founders (2-3% each, $7.6-11.4B), strategic investors (Google 14%, Amazon significant minority), EA-aligned invest...

Organization

OpenAI

Leading AI lab that developed GPT models and ChatGPT, analyzing organizational evolution from non-profit research to commercial AGI development ami...

Approaches

Constitutional AIApproachConstitutional AIConstitutional AI is Anthropic's methodology using explicit principles and AI-generated feedback (RLAIF) to train safer models, achieving 3-10x improvements in harmlessness while maintaining helpfu...Quality: 70/100

Analysis

Anthropic Impact Assessment ModelAnalysisAnthropic Impact Assessment ModelModels Anthropic's net impact on AI safety by weighing positive contributions (safety research $100-200M/year, Constitutional AI as industry standard, largest interpretability team globally, RSP fr...Quality: 55/100Frontier Lab Cost StructureAnalysisFrontier Lab Cost StructureAnalysis of capital allocation at frontier AI labs. OpenAI operates on approximately $20B ARR with $14B+ annual costs; Anthropic on approximately $9B ARR with $7-10B costs; Google DeepMind within A...Quality: 53/100Pre-TAI Capital Deployment: $100B-$300B+ Spending AnalysisAnalysisPre-TAI Capital Deployment: $100B-$300B+ Spending AnalysisAnalysis of how frontier AI labs (Anthropic, OpenAI, Google DeepMind) could deploy $100-300B+ before TAI. Compute infrastructure absorbs 50-65% of spending ($200-400B+ across the industry), with St...Quality: 55/100

Safety Research

Anthropic Core ViewsSafety AgendaAnthropic Core ViewsAnthropic allocates 15-25% of R&D (~$100-200M annually) to safety research including the world's largest interpretability team (40-60 researchers), while maintaining $5B+ revenue by 2025. Their RSP...Quality: 62/100

Historical

Anthropic-Pentagon Standoff (2026)EventAnthropic-Pentagon Standoff (2026)Comprehensive analysis of the February 2026 confrontation between Anthropic and the US government. Triggered when Claude AI was used in the January 2026 Venezuela raid via Palantir, Anthropic refus...Quality: 70/100Mainstream EraHistoricalMainstream EraComprehensive timeline of AI safety's transition from niche to mainstream (2020-present), documenting ChatGPT's unprecedented growth (100M users in 2 months), the OpenAI governance crisis, and firs...Quality: 42/100

Organizations

AI Revenue SourcesOrganizationAI Revenue SourcesAnalysis of the AI revenue gap. Hyperscalers are spending ~$700B on AI infrastructure in 2026 while direct AI service revenue is ~$25-50B—a 6-14x mismatch. Sequoia's framework identifies a $500B+ h...Quality: 55/100Coefficient GivingOrganizationCoefficient GivingCoefficient Giving (formerly Open Philanthropy) has directed $4B+ in grants since 2014, including $336M to AI safety (~60% of external funding). The organization spent ~$50M on AI safety in 2024, w...Quality: 55/100

Other

InterpretabilityResearch AreaInterpretabilityMechanistic interpretability has extracted 34M+ interpretable features from Claude 3 Sonnet with 90% automated labeling accuracy and demonstrated 75-85% success in causal validation, though less th...Quality: 66/100Dario AmodeiPersonDario AmodeiComprehensive biographical profile of Anthropic CEO Dario Amodei documenting his competitive safety development philosophy, 10-25% catastrophic risk estimate, 2026-2030 AGI timeline, and Constituti...Quality: 41/100Holden KarnofskyPersonHolden KarnofskyHolden Karnofsky directed $300M+ in AI safety funding through Coefficient Giving (formerly Open Philanthropy), growing the field from ~20 to 400+ FTE researchers and developing influential framewor...Quality: 40/100Sam AltmanPersonSam AltmanComprehensive biographical profile of Sam Altman documenting his role as OpenAI CEO, timeline predictions (AGI within presidential term, superintelligence in "few thousand days"), and controversies...Quality: 40/100Jan LeikePersonJan LeikeBiography of Jan Leike covering his career from Australian National University through DeepMind, OpenAI's Superalignment team, to his current role as VP of Alignment Science at Anthropic. Documents...Quality: 27/100Chris OlahPersonChris OlahComprehensive biographical profile of Chris Olah covering his unconventional career path, foundational contributions to mechanistic interpretability (feature visualization, circuit analysis, sparse...Quality: 27/100

Concepts

Frontier Ai ComparisonFrontier Ai ComparisonHead-to-head comparison of frontier AI companies on talent, safety culture, agentic AI capability, and 3-10 year financial projections. Key findings: Anthropic leads talent (8x more likely to hire ...Quality: 52/100Longtermwiki Value PropositionLongtermwiki Value PropositionInternal strategy document exploring ambitious value pathways for LongtermWiki, including improving longtermist prioritization (Coefficient integration, cross-funder coordination), attracting new c...Quality: 4/100
