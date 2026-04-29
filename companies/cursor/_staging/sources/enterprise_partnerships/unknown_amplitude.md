---
company: "Anysphere"
research_key: CURSOR
type: enterprise_partnerships
source: "cursor.com"
title: "amplitude"
url: https://cursor.com/blog/amplitude
date: unknown
fetched_at: 2026-04-20T17:56:07
credibility: S2-S4
evidence: E2-E3
chars: 19388
---

# amplitude

**Source**: https://cursor.com/blog/amplitude
**Channel**: enterprise_partnerships

---

Blog / customers

Contact sales

Amplitude is a Software company in North America.

60-70%

of low-risk PRs merged directly to production

1,000+

Automated agent runs every week without manual prompting

3x

Increase in weekly production commits since adopting cloud agents

Top 3

Cursor is now a top contributor by commit volume at Amplitude

Amplitude is a Software company in North America.

60-70%

of low-risk PRs merged directly to production

1,000+

Automated agent runs every week without manual prompting

3x

Increase in weekly production commits since adopting cloud agents

Top 3

Cursor is now a top contributor by commit volume at Amplitude

Amplitude's engineering team wanted to build a fully autonomous development pipeline that could take software from idea to production with minimal developer intervention. With Cursor, Amplitude has now set up systems that take in context from across the software lifecycle—from customer feedback to observability tools to code reviews—and hand it off to agents for execution.

Now, when customers report bugs or feature requests in Slack, cloud agents automatically kick off to investigate, open a ticket, and write a fix. Cursor Automations run continuously in the background, migrating legacy code and classifying risk levels for every new or updated PR. Bugbot serves as the first line of review, merging low-risk changes automatically while routing high-risk PRs to the right reviewers.

Most AI coding tools give you more code. Cursor gives you more useful production software. The ability to run agents that can effectively parallelize work, test their own changes, and take a feature from idea to production is the difference.

Curtis Liu

CTO, Amplitude

#Local-only agents constrain parallelization and autonomy

Early on in its adoption of coding agents, Amplitude ran into what Adam Lohner, a staff software engineer, described as a false plateau in engineering productivity.

Real accelerants to development velocity come when agents produce genuinely useful production software, not just lots of code. We needed much better agent parallelism and autonomy for the former, which agents confined to local developer workstations don't offer.

Adam Lohner

Staff Software Engineer, Amplitude

Local agents compete for the same set of limited resources and quickly run into conflicts. Even running two or three agents at once can lead to performance degradation. Amplitude's codebase is large enough that local developer machines were hitting memory limits, even on high-end hardware with large amounts of RAM.

Local agents also do not have access to a full development environment the way an engineer would. Without it, agents cannot test or verify their own work. Developers still have to configure environments, run end-to-end tests, and manually verify changes before anything can ship.

#Cloud breaks agents out of the local ceiling

For better parallelism and autonomy, Amplitude turned to Cursor's cloud agents. A few capabilities stood out:

Parallel execution at scale: Cloud agents run in isolated, scalable VMs, removing the resource constraints that cap local parallelism.

Full dev environment: Cloud agents can test, verify, and iterate on their work just like an engineer would, with access to a complete development environment.

Long-running execution: Amplitude is delegating deeper, more ambitious tasks for cloud agents to tackle end-to-end instead of short, synchronous ones.

Always-on agents: Cursor Automations let Amplitude set up cloud agents that run in response to triggers or recurring schedules instead of manual prompting.

We're running many cloud agents at once in Cursor, each with full access to our tool stack. The ability to spin up agents that don't run into local resource constraints or require constant micromanagement has been a step-function change.

Adam Lohner

Staff Software Engineer, Amplitude

Engineers at Amplitude now move between cloud and local agents depending on the type of work. New ideas often start in the cloud, where Cursor's harness allows agents to work independently for long stretches of time. Many engineers kick off Cursor directly from Slack threads where feature ideas are being discussed.

Developers pull agents locally when they are ready to focus on more controlled iteration or get closer to the details. Cursor serves as the unified workspace across both cloud and local.

Cursor offers the best interface to orchestrate all your different parallel agents. You can stay high-level or dig into details like diffs and files when you need it.

Spencer Pauly

Head of Engineering, AI Feedback, Amplitude

Since adopting cloud agents, Amplitude has seen a 3x increase in weekly production commits. Cursor has become a top 3 contributor to Amplitude's codebase by commit volume, with over 1,000 agent runs kicked off every week without any prompting or developer intervention.

Cloud is where software is built, local is where we test and iterate. Cursor's support for seamless handoffs between the two has been the key unlock for Amplitude's product velocity.

Spencer Pauly

Head of Engineering, AI Feedback, Amplitude

#From Slack to ticket to PR

Amplitude has dedicated Slack channels where field teams relay customer bug reports and feature requests. Before Cursor, they had a dedicated team member monitor these channels, triage issues, chase down tickets, and assign work from the backlog.

Then, Pauly built a Cursor Automation to hand this entire workstream off to agents. When a new message lands in Slack, a cloud agent checks Linear to see if a ticket already exists for the issue. If one does, the agent adds the new customer context. If not, the agent explores the codebase, opens a new ticket, and opens a PR with its solution implemented.

Cursor Automations are helping us eliminate the gap between the customer and our engineers. We're addressing customer needs faster and with better solutions.

Spencer Pauly

Head of Engineering, AI Feedback, Amplitude

You can start building an automation to turn Slack reports into PRs with this template.

#Automated legacy refactoring

Amplitude's frontend codebase had accumulated years of competing patterns encompassing legacy CSS components, stale React layouts, and inconsistent styling conventions.

We have so many competing legacy patterns that agents struggle to interpret the right way forward. It's a garbage in, garbage out problem.

Adam Lohner

Staff Software Engineer, Amplitude

To fix this, Lohner built a set of cron-based Cursor Automations that run hourly to chip away at legacy migrations. One automation scans CSS files for styles directly replaceable with Tailwind classes, makes the substitutions, deletes the old files, opens a PR, and posts a Slack notification. Another works through Amplitude's 20,000-plus instances of legacy React layout components, swapping them out for native Tailwind equivalents.

Running these migrations in the cloud as automations means they happen continuously in the background without displacing other work or consuming developers' time.

Adam Lohner

Staff Software Engineer, Amplitude

#Agent-led code review

The other bottleneck slowing Amplitude's engineering velocity was manual code review. Amplitude wanted an agent-first review process that improved product reliability and resulted in fewer interruptions for developers.

Amplitude implemented Bugbot as its dedicated agentic review layer. Adoption grew organically as developers saw Bugbot catch issues that human reviewers were missing given the size and complexity of Amplitude's codebase.

Bugbot regularly catches really hard bugs and proposes solid fixes to the issues.

Spencer Pauly

Head of Engineering, AI Feedback, Amplitude

Lohner also built a Cursor Automation that judges the risk impact level of every PR. Low-risk changes can move to merge, with Bugbot reviewing and autofixing issues without developer intervention. High-risk PRs with more complex logic changes are routed to the right engineers automatically. Roughly 60-70% of low-risk PRs are merged without any additional developer work. You can start building an automation to turn Slack reports into PRs with this template.

Bugbot's track record of frequently catching real, production-threatening bugs has made it a key part of our code review process.

Adam Lohner

Staff Software Engineer, Amplitude

Next, Amplitude is focused on pushing automations into the back half of the development lifecycle: CI/CD pipelines, build validation, and deployment. The goal is to have agents take software from reviewed PR to production without developer intervention.

If you're interested in building autonomous development pipelines with Cursor, please reach out to our team to start a Cursor trial.

Amplitude is a Software company in North America.

60-70%

of low-risk PRs merged directly to production

1,000+

Automated agent runs every week without manual prompting

3x

Increase in weekly production commits since adopting cloud agents

Top 3

Cursor is now a top contributor by commit volume at Amplitude

Amplitude is a Software company in North America.

60-70%

of low-risk PRs merged directly to production

1,000+

Automated agent runs every week without manual prompting

3x

Increase in weekly production commits since adopting cloud agents

Top 3

Cursor is now a top contributor by commit volume at Amplitude

More customer stories

Money Forward brings Cursor’s coding agents to product, design, and QA

Mar 18, 2026

PlanetScale protects production reliability with Bugbot

Mar 2, 2026

How Stripe rolled out a consistent Cursor experience for 3,000 engineers

Feb 17, 2026

View all stories →

Blog / customers

Contact sales

Amplitude is a Software company in North America.

60-70%

of low-risk PRs merged directly to production

1,000+

Automated agent runs every week without manual prompting

3x

Increase in weekly production commits since adopting cloud agents

Top 3

Cursor is now a top contributor by commit volume at Amplitude

Amplitude is a Software company in North America.

60-70%

of low-risk PRs merged directly to production

1,000+

Automated agent runs every week without manual prompting

3x

Increase in weekly production commits since adopting cloud agents

Top 3

Cursor is now a top contributor by commit volume at Amplitude

Amplitude's engineering team wanted to build a fully autonomous development pipeline that could take software from idea to production with minimal developer intervention. With Cursor, Amplitude has now set up systems that take in context from across the software lifecycle—from customer feedback to observability tools to code reviews—and hand it off to agents for execution.

Now, when customers report bugs or feature requests in Slack, cloud agents automatically kick off to investigate, open a ticket, and write a fix. Cursor Automations run continuously in the background, migrating legacy code and classifying risk levels for every new or updated PR. Bugbot serves as the first line of review, merging low-risk changes automatically while routing high-risk PRs to the right reviewers.

Most AI coding tools give you more code. Cursor gives you more useful production software. The ability to run agents that can effectively parallelize work, test their own changes, and take a feature from idea to production is the difference.

Curtis Liu

CTO, Amplitude

#Local-only agents constrain parallelization and autonomy

Early on in its adoption of coding agents, Amplitude ran into what Adam Lohner, a staff software engineer, described as a false plateau in engineering productivity.

Real accelerants to development velocity come when agents produce genuinely useful production software, not just lots of code. We needed much better agent parallelism and autonomy for the former, which agents confined to local developer workstations don't offer.

Adam Lohner

Staff Software Engineer, Amplitude

Local agents compete for the same set of limited resources and quickly run into conflicts. Even running two or three agents at once can lead to performance degradation. Amplitude's codebase is large enough that local developer machines were hitting memory limits, even on high-end hardware with large amounts of RAM.

Local agents also do not have access to a full development environment the way an engineer would. Without it, agents cannot test or verify their own work. Developers still have to configure environments, run end-to-end tests, and manually verify changes before anything can ship.

#Cloud breaks agents out of the local ceiling

For better parallelism and autonomy, Amplitude turned to Cursor's cloud agents. A few capabilities stood out:

Parallel execution at scale: Cloud agents run in isolated, scalable VMs, removing the resource constraints that cap local parallelism.

Full dev environment: Cloud agents can test, verify, and iterate on their work just like an engineer would, with access to a complete development environment.

Long-running execution: Amplitude is delegating deeper, more ambitious tasks for cloud agents to tackle end-to-end instead of short, synchronous ones.

Always-on agents: Cursor Automations let Amplitude set up cloud agents that run in response to triggers or recurring schedules instead of manual prompting.

We're running many cloud agents at once in Cursor, each with full access to our tool stack. The ability to spin up agents that don't run into local resource constraints or require constant micromanagement has been a step-function change.

Adam Lohner

Staff Software Engineer, Amplitude

Engineers at Amplitude now move between cloud and local agents depending on the type of work. New ideas often start in the cloud, where Cursor's harness allows agents to work independently for long stretches of time. Many engineers kick off Cursor directly from Slack threads where feature ideas are being discussed.

Developers pull agents locally when they are ready to focus on more controlled iteration or get closer to the details. Cursor serves as the unified workspace across both cloud and local.

Cursor offers the best interface to orchestrate all your different parallel agents. You can stay high-level or dig into details like diffs and files when you need it.

Spencer Pauly

Head of Engineering, AI Feedback, Amplitude

Since adopting cloud agents, Amplitude has seen a 3x increase in weekly production commits. Cursor has become a top 3 contributor to Amplitude's codebase by commit volume, with over 1,000 agent runs kicked off every week without any prompting or developer intervention.

Cloud is where software is built, local is where we test and iterate. Cursor's support for seamless handoffs between the two has been the key unlock for Amplitude's product velocity.

Spencer Pauly

Head of Engineering, AI Feedback, Amplitude

#From Slack to ticket to PR

Amplitude has dedicated Slack channels where field teams relay customer bug reports and feature requests. Before Cursor, they had a dedicated team member monitor these channels, triage issues, chase down tickets, and assign work from the backlog.

Then, Pauly built a Cursor Automation to hand this entire workstream off to agents. When a new message lands in Slack, a cloud agent checks Linear to see if a ticket already exists for the issue. If one does, the agent adds the new customer context. If not, the agent explores the codebase, opens a new ticket, and opens a PR with its solution implemented.

Cursor Automations are helping us eliminate the gap between the customer and our engineers. We're addressing customer needs faster and with better solutions.

Spencer Pauly

Head of Engineering, AI Feedback, Amplitude

You can start building an automation to turn Slack reports into PRs with this template.

#Automated legacy refactoring

Amplitude's frontend codebase had accumulated years of competing patterns encompassing legacy CSS components, stale React layouts, and inconsistent styling conventions.

We have so many competing legacy patterns that agents struggle to interpret the right way forward. It's a garbage in, garbage out problem.

Adam Lohner

Staff Software Engineer, Amplitude

To fix this, Lohner built a set of cron-based Cursor Automations that run hourly to chip away at legacy migrations. One automation scans CSS files for styles directly replaceable with Tailwind classes, makes the substitutions, deletes the old files, opens a PR, and posts a Slack notification. Another works through Amplitude's 20,000-plus instances of legacy React layout components, swapping them out for native Tailwind equivalents.

Running these migrations in the cloud as automations means they happen continuously in the background without displacing other work or consuming developers' time.

Adam Lohner

Staff Software Engineer, Amplitude

#Agent-led code review

The other bottleneck slowing Amplitude's engineering velocity was manual code review. Amplitude wanted an agent-first review process that improved product reliability and resulted in fewer interruptions for developers.

Amplitude implemented Bugbot as its dedicated agentic review layer. Adoption grew organically as developers saw Bugbot catch issues that human reviewers were missing given the size and complexity of Amplitude's codebase.

Bugbot regularly catches really hard bugs and proposes solid fixes to the issues.

Spencer Pauly

Head of Engineering, AI Feedback, Amplitude

Lohner also built a Cursor Automation that judges the risk impact level of every PR. Low-risk changes can move to merge, with Bugbot reviewing and autofixing issues without developer intervention. High-risk PRs with more complex logic changes are routed to the right engineers automatically. Roughly 60-70% of low-risk PRs are merged without any additional developer work. You can start building an automation to turn Slack reports into PRs with this template.

Bugbot's track record of frequently catching real, production-threatening bugs has made it a key part of our code review process.

Adam Lohner

Staff Software Engineer, Amplitude

Next, Amplitude is focused on pushing automations into the back half of the development lifecycle: CI/CD pipelines, build validation, and deployment. The goal is to have agents take software from reviewed PR to production without developer intervention.

If you're interested in building autonomous development pipelines with Cursor, please reach out to our team to start a Cursor trial.

Amplitude is a Software company in North America.

60-70%

of low-risk PRs merged directly to production

1,000+

Automated agent runs every week without manual prompting

3x

Increase in weekly production commits since adopting cloud agents

Top 3

Cursor is now a top contributor by commit volume at Amplitude

Amplitude is a Software company in North America.

60-70%

of low-risk PRs merged directly to production

1,000+

Automated agent runs every week without manual prompting

3x

Increase in weekly production commits since adopting cloud agents

Top 3

Cursor is now a top contributor by commit volume at Amplitude

More customer stories

Money Forward brings Cursor’s coding agents to product, design, and QA

Mar 18, 2026

PlanetScale protects production reliability with Bugbot

Mar 2, 2026

How Stripe rolled out a consistent Cursor experience for 3,000 engineers

Feb 17, 2026

View all stories →
