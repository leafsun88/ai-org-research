---
ticker: CURSOR
type: substack
title: ""
author: ""
date: 
url: https://prompthub.substack.com/p/what-cursors-fine-tuned-model-means
chars: 11283
credibility: S2
evidence: E2
---

# 

**Author**: 
**Date**: 
**URL**: https://prompthub.substack.com/p/what-cursors-fine-tuned-model-means

---

What Cursor’s fine-tuned model means for the AI ecosystem

Dan's Working Notes

SubscribeSign in

What Cursor’s fine-tuned model means for the AI ecosystem

How custom models and reinforcement learning could redefine the margin profile of AI startups.

Dan Cleary

Oct 31, 2025

2

3

1

Share

Earlier this week, Cursor launched Cursor 2.0 and Composer. Whenever a major AI player launches something new, it means a whole lot more than just new features, it’s a glimpse into where the AI market might next.

We’ll go over the new features, the new model, and what this means for AI companies, VCs investing in AI, and anyone using these tools.

Thanks for reading The Prompt Engineering Substack! Subscribe for free to receive new posts and support my work.

Subscribe

Composer

Composer is Cursor’s new agent model designed for software engineering intelligence and speed. It’s 4x faster similarly intelligent models. I’ve been testing it out, and the speed difference is real.

The multi-agent interface

Cursor also launched a new interface allows many agents to run in parallel, working on different tasks. It uses Git worktrees to avoid conflicts.

You can now run up to 8 agents in parallel on a single prompt.

I don’t really find the use case of having many agents running on different tasks that useful. But running multiple models on the same task is actually great. You can now run up to 8 agents in parallel on a single prompt.

For example, I had Composer-1, Haiku 4.5, and Grok 4 Fast each work on a UI task of implementing a referrals page in an app: ”in the settings panel create a referrals page to generate links and track referrals, front end only “

Haiku 4.5

Grok 4 Fast

Composer-1

Admittedly, it took me a minute to get the Git worktrees working, but I got it to a usable state.

Throwing more compute at a problem always helps increase performance.

You can now run up to 8 agents in parallel on a single prompt.

Browser tool

A low-key part of the announcement, was that the browser tool is now GA and has gotten some serious upgrades. It’s a native browser tool (MCP) that allows Cursor to test its work, look at console logs, and iterate until everything works.

You can connect it to a Chrome window, or use it via an embedded browser tab inside the editor itself.

How composer was built

Composer was trained via reinforcement learning to solve real-world engineering problems in large codebases, not just to score well on coding benchmarks. Cursor’s main goal was to build a smart model that keeps developers in the flow of coding, much like their tab-completion model. With that goal in mind, speed was a top priority. And you can feel it, the model is extremely fast.

They used their own private benchmark, Cursor bench, which consists of real agent requests from real users, to evaluate and train Composer-1. Importantly, the evaluation didn’t just check for correctness, but also for “ adherence to a codebase’s existing abstractions and software engineering practices.”

“our finding here is that RL scales.” - Sasha Rush, researcher at Cursor

In the reinforcement learning process, Cursor incentivized the model to make efficient choices in tool use and maximize parallelism where possible, leading to much faster responses. They also trained the model to minimize unnecessary fluff in responses and avoid claims made without evidence.

They also noted that during the RL process, the model learned a bunch of useful behaviors like fixing linter errors and writing and executing unit tests. This is similar to what happened in the DeepSeek R-1 training process where the model taught itself to improve its reasoning. 

Have the Chinese overtaken OpenAI? An overview on DeepSeek's R-1

Dan Cleary

·

January 24, 2025

Read full story

Quotes from Cursor

Sasha Rush, a researcher at Cursor, answered a bunch of questions on Hacker News, here are some of my favorites. Most notably he dodged multiple questions about if Composer-1 is a fine-tune of open-source base model.

Q: I prefer the approach of focusing on faster models despite their lower intelligence because I want my IDE to fly when I can see the code. I find this useful when I need to manually debug something that any model is able to do, so I know it’s going to fail but at least it will fail fast. On the other hand, if I need more intelligence I have my other CLI that doesn’t allow me to see the code but gets the planning and difficult code done.

A: Our view is that there is a now a minimal amount of intelligence that is necessary to be productive, and that if you can pair that with speed that is awesome.

Q: is Composer a fine tune of an existing open source base model?

A: Our primary focus is on RL post-training. We think that is the best way to get the model to be a strong interactive agent.

Q: Does anyone code with GPT-5? I’ve never had it work in Cursor. I mean, like, at all.

A lot of people use it! It (GPT_5) scores very well on our benchmarks, significantly better than Composer-1.

This last one seemed relevant because in the image shared in the launch, the performance gap between Composer and the best frontier models didn’t appear to be “significantly better.”

A few other takeaways in regard to the AI ecosystem.

No shortage for token demand

The new feature that lets you take a prompt, run it across many models, and see which one you like best is massive. From a user perspective, I’d love to throw a bunch of models at a problem and see what happens. Cursor is more than happy to burn tokens by running multiple calls.

The one hiccup is Git worktrees, they just don’t work well and aren’t intuitive.

Expect to see Cursor’s “one prompt many outputs” feature copied across all the coding, usage-based apps. Vibe-coding tools will adopt this quickly, and might even do it better since they can be more opinionated with managing git worktrees, since their user neither know nor care what they are.

Hello margins:

A big question around AI startups is their margin profile. Pre-AI, software companies were used to ~90% margins, but AI companies have to pay OpenAI. This slashes current day margins to to 70%, 50%, 30% or even negative in some case In Bessemer’s AI report they note the startups growing the fastest have negative margins.

The current playbook is: build a product people love, raise money, don’t worry too much about margins (even if they’re negative), expand mindshare and market share, wait for token costs to drop and competitors to die — then margins rise and profits follow. While token prices haven’t really dropped (Claude Sonnet 4.5 costs about the same as 3.5), and models now generate far more tokens per message thanks to reasoning, this strategy can still work if you eventually have your own models.

Is the next wave fine-tunes?

Could fine-tuned models via RL compete with OpenAI and Anthropic models? Composer-1 is the first real test case for this.

They don’t say it explicitly, but it’s most likely a fine-tuned version of an open-source model (Llama, Qwen, etc.). So it begs the question: as RL gets easier, will more companies follow Cursor’s path?

Remember Sasha Rush’s quote:

“Our view is that there is now a minimal amount of intelligence necessary to be productive, and that if you can pair that with speed, that’s awesome.”

If Composer’s intelligence is “good enough” and the speed is amazing, the extra few percentage points that Claude Sonnet 4.5 has over it might not matter and it might not justify the cost difference for some percentage of the market.

This made me think of Tinker, Thinking Machines’ first product (founded by former OpenAI CTO, Mira Murati).

We’re building a future where everyone has access to the knowledge and tools to make AI work for their unique needs and goals.

Today, we are launching Tinker, a flexible API for fine-tuning language models.

Tinker lets you fine-tune a range of large and small open-weight models, including large mixture-of-experts models such as Qwen-235B-A22B. Switching from a small model to a large one is as simple as changing a single string in your Python code.

Tinker is a managed service that runs on our internal clusters and training infrastructure. We handle scheduling, resource allocation, and failure recovery. This allows you to get small or large runs started immediately, without worrying about managing infrastructure.

I’ve never used Tinker, but if the cost to train a Composer-like model keeps dropping, every coding app will at least have a homegrown, fine-tuned model as an option for users.

Closing thoughts

It will be fascinating to see how the next few weeks play out and how much adoption Composer-1 gets. It will be a huge signal to the rest of the market across all layers in the stack (model providers, infra, application layer).

Thanks for reading The Prompt Engineering Substack! Subscribe for free to receive new posts and support my work.

Subscribe

2

3

1

Share

Discussion about this post

CommentsRestacks

Steve Johnson 
Oct 31

Liked by Dan Cleary

The idea of running three different models on a single prompt sounds great, but not if you're on Cursor's $20.00 plan. I have to stick to GPT5 for the complicated stuff, and Grok Code Fast 1 for all the nickle-and-dime stuff.

Reply

Share

1 reply by Dan Cleary

Pawel Jozefiak 

Jan 27

The insight about Cursor developing Composer-1 to escape API margin compression is fascinating. I've been running my own AI agent (Wiz) on Claude Code for months now, and the economics are brutal when you're paying per-token for everything. Cursor's move to train on their actual user codebase rather than synthetic benchmarks is exactly the right approach - real developer workflows look nothing like LeetCode problems.

What strikes me most is how this validates a pattern I've noticed across AI development tools: the winners are the ones who understand that raw model intelligence matters less than tight integration with how developers actually work. Cursor's 4x speed improvement probably matters more than marginal accuracy gains because it keeps you in flow state. When I was testing various AI coding assistants last year, the tools that felt fast and responsive always beat the "smarter" ones that made me wait.

The margin question you raise is the existential one for this entire category. Building on top of foundation model APIs works great until you need to scale - then you're either raising prices, cutting features, or doing what Cursor did and bringing inference in-house. I explored this tension when comparing different AI dev tools and their architectural tradeoffs. The companies betting on fine-tuned vertical models seem better positioned than pure API wrappers.

I wrote about my own journey testing Cursor against other AI development tools at thoughts.jock.pl/p/cursor-vs-google-ai-studio-antigravity-ide-comparison-2025 - the speed and integration differences between tools were more decisive than I expected.

Reply

Share

1 more comment...

TopLatestDiscussions

No posts

Ready for more?

Subscribe

© 2026 Dan Cleary · Privacy ∙ Terms ∙ Collection notice

 Start your SubstackGet the app

Substack is the home for great culture

 This site requires JavaScript to run correctly. Please turn on JavaScript or unblock scripts
