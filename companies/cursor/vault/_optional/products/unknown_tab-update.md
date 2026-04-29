---
company: "Anysphere"
research_key: CURSOR
type: products
source: "cursor.com"
title: "tab-update"
url: https://cursor.com/blog/tab-update
date: unknown
fetched_at: 2026-04-20T17:55:49
credibility: S2-S4
evidence: E2-E3
chars: 6960
---

# tab-update

**Source**: https://cursor.com/blog/tab-update
**Channel**: products

---

Blog / product

Today, we are announcing Fusion, our next generation Cursor Tab model.

Cursor Tab predicts both edits near your cursor and suggestions for where to move next (“jumps”). The Fusion model produces nearly instant, much higher quality cursor jumps while improving edit quality as well. Our proximate goal with Tab is to eliminate tedium from code editing, and Fusion is a significant improvement in that direction, taking us further on the path to our ultimate goal of in-flow Next Action Prediction.

#The most useful copilot

Beginning in March of 2024, Tab has been powered by a custom sparse language model trained to predict edits on billions of tokens. Since then, we’ve improved nearly every aspect of Tab, making it faster, more intelligent, and more useful over the course of dozens of model updates and infrastructure improvements.

We’ve found Tab has become more useful as we’ve continued developing it, and we’re delighted our users have too. Tab has become much bigger; it now produces over a billion edited characters per day, and the request rate has grown ~100x since our original model launch. At this point, our Tab model generates more code than almost any LLM in the world.

We’ve long since realized that inserting text is a tiny part of editing code. While other copilots only insert text at your cursor location, Cursor Tab suggests both full edits around your cursor and jumps you to the next place you want to go.

By quickly suggesting accurate edits and jumps, Tab is much more useful than other copilots. Of course, Tab can do the typical copilot tasks well too — it is good at writing small functions and following inline instructions at low latency.

#Improvements since March

Our first Tab model was trained and shipped in March 2024. Compared to this original model release, Fusion accurately predicts over 25% more difficult edits per line, while also suggesting over 10x longer stretches of changes. Fusion also improves on our original model in several other ways:

Model versionServer latency (p50)Cursor jumpsContext length (tokens)

Original475msNone5500

Fusion260msInstant, accurate13000

Fusion vastly outperforms the March model on suggestion accuracy, while providing nearly instant and higher quality cursor jumps, longer context, and lower latency.

Gains in model quality come from:

Cleaner, higher quality, and higher quantity data

Longer context windows with much more editor state and file content in the prompt

Carefully training for larger edits, resulting in the Bigger Edits model

Synthetic data for instruction following

Training recipe and base model improvements

Gains in latency come from inference improvements, performance engineering, and better base models.

#Looking forward

Fusion is rolling out to all users with our new client release (0.45.0).

Our next suite of Tab improvements will bring much better codebase context, better tab-tab-tab sequences, and further integrate Supermaven technology into Tab.

If you’re interested in eliminating all tedium from code editing, working on one of the most useful models for writing code, or modeling the action trajectories of programmers, please reach out at hiring@cursor.com.

Related posts

Oct 29, 2025·Product

Introducing Cursor 2.0 and Composer

Cursor Team · 3 min read

Jul 4, 2025·Product

Clarifying our pricing

Michael Truell · 3 min read

Jun 16, 2025·Product

Updates to Ultra and Pro

Michael Truell · 1 min read

View more posts →

Blog / product

Today, we are announcing Fusion, our next generation Cursor Tab model.

Cursor Tab predicts both edits near your cursor and suggestions for where to move next (“jumps”). The Fusion model produces nearly instant, much higher quality cursor jumps while improving edit quality as well. Our proximate goal with Tab is to eliminate tedium from code editing, and Fusion is a significant improvement in that direction, taking us further on the path to our ultimate goal of in-flow Next Action Prediction.

#The most useful copilot

Beginning in March of 2024, Tab has been powered by a custom sparse language model trained to predict edits on billions of tokens. Since then, we’ve improved nearly every aspect of Tab, making it faster, more intelligent, and more useful over the course of dozens of model updates and infrastructure improvements.

We’ve found Tab has become more useful as we’ve continued developing it, and we’re delighted our users have too. Tab has become much bigger; it now produces over a billion edited characters per day, and the request rate has grown ~100x since our original model launch. At this point, our Tab model generates more code than almost any LLM in the world.

We’ve long since realized that inserting text is a tiny part of editing code. While other copilots only insert text at your cursor location, Cursor Tab suggests both full edits around your cursor and jumps you to the next place you want to go.

By quickly suggesting accurate edits and jumps, Tab is much more useful than other copilots. Of course, Tab can do the typical copilot tasks well too — it is good at writing small functions and following inline instructions at low latency.

#Improvements since March

Our first Tab model was trained and shipped in March 2024. Compared to this original model release, Fusion accurately predicts over 25% more difficult edits per line, while also suggesting over 10x longer stretches of changes. Fusion also improves on our original model in several other ways:

Model versionServer latency (p50)Cursor jumpsContext length (tokens)

Original475msNone5500

Fusion260msInstant, accurate13000

Fusion vastly outperforms the March model on suggestion accuracy, while providing nearly instant and higher quality cursor jumps, longer context, and lower latency.

Gains in model quality come from:

Cleaner, higher quality, and higher quantity data

Longer context windows with much more editor state and file content in the prompt

Carefully training for larger edits, resulting in the Bigger Edits model

Synthetic data for instruction following

Training recipe and base model improvements

Gains in latency come from inference improvements, performance engineering, and better base models.

#Looking forward

Fusion is rolling out to all users with our new client release (0.45.0).

Our next suite of Tab improvements will bring much better codebase context, better tab-tab-tab sequences, and further integrate Supermaven technology into Tab.

If you’re interested in eliminating all tedium from code editing, working on one of the most useful models for writing code, or modeling the action trajectories of programmers, please reach out at hiring@cursor.com.

Related posts

Oct 29, 2025·Product

Introducing Cursor 2.0 and Composer

Cursor Team · 3 min read

Jul 4, 2025·Product

Clarifying our pricing

Michael Truell · 3 min read

Jun 16, 2025·Product

Updates to Ultra and Pro

Michael Truell · 1 min read

View more posts →
