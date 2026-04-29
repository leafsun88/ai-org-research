---
ticker: CURSOR
type: substack
title: ""
author: ""
date: 
url: https://mbideepdives.substack.com/p/cursors-conundrum
chars: 10190
credibility: S2
evidence: E2
---

# 

**Author**: 
**Date**: 
**URL**: https://mbideepdives.substack.com/p/cursors-conundrum

---

Cursor's Conundrum - MBI Deep Dives

MBI Deep Dives

SubscribeSign in

Cursor's Conundrum

MBI Deep Dives

Aug 15, 2025

∙ Paid

6

1

Share

I don’t quite follow private companies closely. OpenAI and Anthropic are perhaps the only exceptions; I had to make the exception because they are simply too big to ignore and likely will have profound impact on how AI shapes the broader tech industry in the next 5-10 years. Cursor isn’t quite that big, but still is currently “valued” ~$10 Billion. What really caught my attention is despite being just a three year old company, other startups were starting to pitch “Cursor for X”, and yet when I spent some time on Cursor, I was slightly confused why this company is considered a blueprint for success for other startups! 

I came across this Edward Zitron piece “AI is a Money Trap” that made me wonder about Cursor’s long-term future. To be frank, I read half of the article and gave up because the piece was getting progressively weaker. However, the way I read any content on the internet is to not look for all the weaker points an author makes, rather only look for the interesting and good arguments that make me think. So, while I think Zitron makes a lot of weak arguments in his piece, he did outline Cursor’s conundrum well: 

“Cursor makes — before, at least, their massive changes to their service — $500 million in annualized revenue, so around $42 million a month. This makes it the single-highest earning generative AI company that isn’t called OpenAI or Anthropic, and the highest-earning company built on top of (primarily) Anthropic’s technology. Its success is symbolic to the greater movement, and just as it hit its peak, Anthropic (and OpenAI, to a lesser extent) decided to add priority processing and priority service tiers, demanding more money up front and causing Cursor to have to massively degrade its service. I explain in detail in my premium piece from a few weeks ago.

To explain in short, Cursor’s AI-powered coding editor used to have fairly unrestrained access to the various models provided by these companies. In mid-June — a few weeks after Anthropic introduced “priority tiers” that required companies to pay up-front and guarantee a certain throughput of tokens and increased costs on using prompt caching, a big part of AI coding — Cursor massively changed the amount its users could use the product, and introduced a $200-a-month subscription.

As an aside to this, Anthropic also competes with Cursor’s AI coding product with their own service, Claude Code.

Cursor, as Anthropic’s largest client (the second largest being Github Copilot), represents a material part of its revenue, and its surging popularity meant that they were sending more and more revenue Anthropic’s way.

Anthropic used this opportunity to raise prices on accessing its models to continue providing service at an acceptable level to Cursor’s customers by introducing “Priority Tier” access on May 30 2025.

This has allowed Anthropic to juice its revenues, and due to the upfront nature of these contracts, Cursor is locked-in regardless of how well it does. The net result of these cost increases means that Cursor’s product is less attractive to its customers, and will thus make it less money.”

Chris Paik yesterday also wrote a piece on Cursor that highlighted the double whammy Cursor faces:

Cursor’s users expect the best coding performance, which is currently delivered by the frontier labs. That pins Cursor’s COGS to OpenAI/Anthropic price cards. Cursor doesn’t control two critical dials:

Model performance frontier (what users demand).

Model input/output pricing (what Cursor pays).

If Cursor steps down to cheaper, weaker models, the users who care about performance will notice and churn; those who can tolerate weaker models can get them cheaper elsewhere. If it stays at the frontier while keeping prices flat, the variable, real cost to service their heaviest users will explode. In an effort to combat this, Cursor has been forced to raise prices and institute usage caps leading to user outrage and churn.

While Cursor is indeed structurally exposed to supplier power on both axes that matter (frontier capability and token economics), Cursor understandably has a slightly different perspective to this conundrum. In an interview with Ben Thompson (BT), Cursor co-founder Michael Truell (MT) hinted at what he thinks is Cursor’s differentiator (emphasis mine): 

BT: Is that a real sustainable advantage for you going forward, where you can really dominate the space because you have the usage data, it’s not just calling out to an LLM, that got you started, but now you’re training your own models based on people using Cursor. You started out by having the whole context of the code, which is the first thing you need to do to even accomplish this, but now you have your own data to train on.

MT: Yeah, I think it’s a big advantage, and I think these dynamics of high ceiling, you can kind of pick between products and then this kind of third dynamic of distribution then gets your data, which then helps you make the product better. I think all three of those things were shared by search at the end of the 90s and early 2000s, and so in many ways I think that actually, the competitive dynamics of our market mirror search more than normal enterprise software markets.

BT: Yeah, I do want to come back to that point, I think that’s really interesting.

What role do the large LLMs still play in Cursor today? Obviously that was what mattered to start, but where do they make a difference in the experience given that you use your own models to do some of this work that you’re talking about?

MT: They definitely still play a big role. So sometimes we’re using custom models entirely without any of the big API models, as an example, Tab, in the prediction side of things, that’s because that’s a task that’s very specialty, those models need to be incredibly fast to deliver suggestions within 200 milliseconds, 300 milliseconds, but then the API models are an important feature of Cursor. Often they’re used not on their own, but with our own models on the input side of things and on the output side of things.

BT: So you’re writing custom prompts and deciding where to go to, it’s like an AI orchestration layer.

MT: Yeah. On the input side of things, we have a whole suite of models that is picking the best parts of a code base to show these models and optimizing things on the input, and then on the output side of things, the API models are very slow, and so to make an actual change across the code base, the API model gives us kind a sketch of the change. Then it gets turned into a multi-thousand line diff by a specialty model and some inference tricks that takes that plan and then does the actual text editing.

So even in the cases where we use the API models, which are an important feature of Cursor and we definitely benefit from those getting better, and are excited by all the recent developments and for progress to continue there, there’s custom models around them.

Why might Cursor’s “custom” models beat Claude/OpenAI/Google? Cursor doesn’t need to dominate at broad reasoning; Cursor needs to outperform on narrow, code‑specific tasks under hard latency constraints. Nonetheless, I do think the concerns are pretty real. In some sense, it reminds me of a tweet I saw (I tried to look for it but cannot find it) that lamented why Shopify chooses at times to compete with third party developers on its ecosystem by providing a competing solution. Someone from Shopify replied (like I said, I can’t find any of these but I don’t think I’m hallucinating this) which left an impression on my mind how any platform approaches these decisions. 

So, someone from Shopify essentially implied Shopify can’t (and shouldn’t) build for every edge case. That’s what the ecosystem is for. But for something like checkout/Shop Pay? These must be fast, secure, and universal, so they’re native. If it’s table-stakes for nearly all merchants (he may have mentioned ~80% of merchants), Shopify builds and hardens it; partners extend it for edge cases. If it’s a broad need but fragmented in implementation, Shopify may ship a baseline while encouraging 3P depth. If partners already deliver superior depth and the category isn’t core to Shopify’s moat, Shopify defers to 3P partners. 

I think the challenge for Cursor is coding is such an incredibly good product market fit for these SOTA model developers and particularly a massive revenue driver for Anthropic, it’s hard to imagine Anthropic not doubling down in perfecting Claude Code! 

In a recent interview, Anthropic Co-founder Dario Amodei said the following: 

…I think there was quite a lot of uncertainty two or three years ago. But I think we might be relatively close to the final set of players, if not necessarily the final market structure or the roles of the players. I would say there's probably somewhere between three and six players, depending on how you count, and those are the players that are capable of building frontier models and have enough capital to plausibly bootstrap themselves.

If I were Cursor, I would be praying the number of players turns out to be closer to six!

In addition to "Daily Dose" (yes, DAILY) like this, MBI Deep Dives publishes one Deep Dive on a publicly listed company every month. You can find all the 61 Deep Dives here.

Subscribe

Current Portfolio:

Please note that these are NOT my recommendation to buy/sell these securities, but just disclosure from my end so that you can assess potential biases that I may have because of my own personal portfolio holdings. Always consider my write-up my personal investing journal and never forget my objectives, risk tolerance, and constraints may have no resemblance to yours.

My current portfolio is disclosed below:

This post is for paid subscribers

Subscribe

Already a paid subscriber? Sign in

© 2026 MBI Deep Dives · Privacy ∙ Terms ∙ Collection notice

 Start your SubstackGet the app

Substack is the home for great culture

 This site requires JavaScript to run correctly. Please turn on JavaScript or unblock scripts
