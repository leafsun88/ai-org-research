---
credibility: S2
evidence: E2
source: substack
url: https://karozieminski.substack.com/p/claude-cowork-anthropic-product-deep-dive
author: Karo (Product with Attitude)
date: 2026-01-13
---

# Anthropic Shipped Cowork in 10 Days Using Its Own AI

## User Behavior That Started Everything

Anthropic observed users deploying Claude Code for non-coding tasks: vacation research, creating presentations, organizing emails. Rather than restricting usage, Anthropic recognized users understood the product's true value — agency and automation — better than internal teams.

The company responded by removing friction: simplifying the sandbox interface, eliminating terminal requirements, and renaming it to something less developer-centric. Ten days later, Cowork launched.

## The Mechanics

Cowork grants Claude access to a designated computer folder. Users describe tasks in plain language; Claude reads, edits, and creates files autonomously. Unlike chat interfaces offering suggestions, Cowork executes directly. Users queue tasks; Claude processes them in parallel.

## AI Building AI

Anthropic engineered Cowork in approximately ten days using Claude Code itself. Key internal metrics:
- Engineers utilize Claude in 60% of their work (up from 28% annually)
- 50% productivity gains reported
- 60-100 internal releases shipped daily
- Roughly 90% of Claude Code's codebase was written by Claude Code

## Strategic Positioning

Claude Code's primary limitation was positioning. The name signaled "developers only" to non-technical users. Cowork removes this barrier.

The underlying Agent SDK remained largely unchanged — the transformation was primarily accessibility-focused.

## Security Architecture

Uses Apple's VZVirtualMachine framework with containerized Linux environments for sandboxing. Granted folder access mounts into isolated containers; Cowork cannot access anything outside explicitly shared directories.

## Competitive Implications

Cowork positions Anthropic to own the "autonomous execution on your computer" category. ChatGPT and Gemini lack equivalent functionality. Claude Code reportedly generates over $500 million in annualized revenue. By removing technical barriers, Cowork targets knowledge workers — a vastly larger market segment.
