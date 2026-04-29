---
ticker: AXON
type: controversy
title: "Axon's Draft One Is Designed to Defy Transparency (EFF Investigation)"
url: https://www.eff.org/deeplinks/2025/07/axons-draft-one-designed-defy-transparency
date: 2025-07-10
credibility: S2
evidence: E2
fetched: 2026-04-07
---

# Axon's Draft One Is Designed to Defy Transparency

*Source: Electronic Frontier Foundation (Matthew Guariglia, Dave Maass)*

Axon Enterprise's Draft One — a generative AI product that writes police reports based on audio from officers' body-worn cameras — **seems deliberately designed to avoid audits that could provide any accountability to the public**, an EFF investigation has found.

## Core Finding: No Audit Trail By Design

Draft One does not save the first draft it generates. Nor does the system store any subsequent versions. Instead, the officer copies and pastes the text into the police report, and the previous draft disappears as soon as the window closes.

**Axon's own senior principal product manager for generative AI stated explicitly:**

> "So we don't store the original draft and that's by design and that's really because **the last thing we want to do is create more disclosure headaches for our customers and our attorney's offices** — so basically the officer generates that draft, they make their edits, if they submit it into our Axon records system then that's the only place we store it, if they copy and paste it into their third-party RMS system as soon as they're done with that and close their browser tab, it's gone. It's actually never stored in the cloud at all so you don't have to worry about extra copies floating around."

## How Draft One Works

Draft One uses a ChatGPT variant to process body-worn camera **audio** of public encounters and create police reports based only on the captured verbal dialogue; it does not process the video. The Draft One-generated text is sprinkled with bracketed placeholders that officers are encouraged to add observations to — or can quickly delete.

When finished, the officer copies and pastes text into the police report. The previous draft disappears when the window closes. No log, no record of what AI wrote vs. what the officer wrote.

## What the "Audit Trail" Actually Looks Like

Two types of basic logs exist:
1. **A log of basic actions on a particular report** (whether officer ran a Draft One request or signed liability disclosure — nothing more)
2. **A log of an individual officer's basic activity** (when they logged in, uploaded videos, accessed evidence — not the content of AI-generated text)

To do a comprehensive review, an evaluator may need to go through each officer individually — potentially combing through hundreds or thousands of individual user logs.

**Key inconsistency:** Axon tracks police use of the technology at a level not available to the police department itself. When Frederick Police Department couldn't export Draft One reports, Axon representative said: "We track which reports use Draft One internally so I exported the data" — then provided custom JSON code.

## Frederick PD Email: "We love having new toys until the public gets wind of them"

An administrator in the Frederick Police Department (one of Axon's first Draft One customers) sent to an Axon representative after receiving a public records request:

> "We love having new toys until the public gets wind of them."

## Regulatory Response

**California SB 524:** Would require disclosure whenever police use AI to write reports and require the first draft to be retained as long as the final report. **Because Draft One is designed not to retain first drafts, it cannot comply with this bill, and any law enforcement usage would be unlawful.**

**King County (Seattle) DA's office instructions:**
> "We do not fear advances in technology – but we do have legitimate concerns about some of the products on the market now... For now, our office has made the decision not to accept any police narratives that were produced with the assistance of AI."

## EFF's Conclusion

Police should not be using AI to write police reports. There are too many unanswered questions. There is no way for the public to reliably discern what was written by a person and what was written by a computer. This compounds existing problems in an already unfair and untransparent criminal justice system.
