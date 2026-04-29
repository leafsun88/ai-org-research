---
ticker: CURSOR
type: substack
title: ""
author: ""
date: 
url: https://whynowtech.substack.com/p/cursor-beyond-the-hype
chars: 14252
credibility: S2
evidence: E2
---

# 

**Author**: 
**Date**: 
**URL**: https://whynowtech.substack.com/p/cursor-beyond-the-hype

---

Cursor - beyond the hype - by Alex Mackenzie - Why Now

Why Now

SubscribeSign in

Cursor - beyond the hype

I’m only human, and perhaps LLMs are too

Alex Mackenzie

Sep 16, 2024

9

2

2

Share

Add to the discussion on Twitter & LinkedIn here and here. Thanks for reading!

Last Friday a friend and I were sipping one of the Lore of the Land’s finest stouts when he asked: “why Cursor?”. 

You see, I shared with him that I’ve tried the gamut of IDEs and VS Code extensions: PyCharm to Zed, Codium to Copilot, but that Cursor has been the only one to truly.. “stick”. When expounding on my answer, I noticed myself rather haphazardly listing off product features that I enjoy vs. providing him with a crisp response. 

As I’ve thought more about this moment, I’ve realised that within this feature list actually lies an explanation I’m ok with. Many of my most beloved products and brands [1][2][3] string together seemingly inconsequential product decisions that, in aggregate, make them truly different. Par example, I didn’t expect Nothing’s glyph interface to change my life, but it kinda has.

In Cursor’s case, these small decisions are derived from the LLM being a first-class citizen as opposed to an afterthought. For example, the fact that Cursor’s activity bar is horizontal vs. vertical is trivial, but it likely means that they’ve found another 100+ ways to create space and context for Cursor Chat. The collective is far less trivial. 

Herein lies another learning. The word “native” (cloud-native, LLM-native, etc) gets thrown around a lot in tech, but it’s a genuine source of advantage if you know what to look for. My high-level framework is that being “native” (i.e. building from the ground-up with) to a technology should enable you to either:

Deliver an existing feature far better than your competitive set who’re built on alternative technologies or architectures. E.g. code linters have been a thing for a long time, but Cursor understands what you’re doing-next vs. do-ing.

Offer an entirely new feature that can’t be provided by your competitive set who’re built on alternative technologies or architectures. E.g. with a `@web`declaration, Cursor can visit the docs of a given api. 

As is evident from the above, Cursor benefits from both types of “native” advantage. Nice. Puff pieces are a little boring though.. so I decided to try and test the limits of Cursor and write something a little more critical (and more constructive, I hope!) by attempting to build Next.js Conf’s beautiful new website (partially built by my talented friend Facundo) without writing a line of code myself.

Below is a stream of product observations and requests derived from this experiment. Enjoy! Critique! Frame on your wall! Oh & say hi if you like: alex@tapestry.vc

tab tab tab subscribe tab tab tab

Subscribe

Observation 1 - 80% feels like 100%

Typically, when we read our favourite newspapers we find them insightful. But, have you noticed that when the publication writes about something you consider yourself an “expert” on their perspective is a little.. lacking?

This same phenomenon seems to be occurring with Cursor. For someone that’s never built a navbar before, doing so with a single prompt is an absolute game-changer (just ask Positive_Box_69). But, it took me 10+ prompts to get my navbar remotely close to Next.js’ (& I’ve built a few too many navbars in my time). For the uninitiated, getting 80% of the way there feels like they’ve completed it mate. 

Now, perhaps I’m a poor prompt designer. So, see below my system prompt or, “Rules for AI” (note the use of role-playing), as well as my attempt to create said navbar via Chain-of-Thought prompting. 

Note: I’m sure there are many ways that I could improve my prompt (e.g. specifying the inclusion of Next.js “Geist” font) but as you’ll see below, my prompt is reasonably extensive.
// Rules for AI

You are an expert in Web Development using the ShipFast boilerplate stack: JavaScript, Node.js, React, Next.js App Router, Tailwind
CSS, DaisyUl, NextAuth, MongoDB and Mongoose.

Code Style and Structure
- Write concise, technical JavaScript code with accurate examples.
- Use functional and declarative programming patterns; avoid classes.
- Prefer iteration and modularization over code duplication.
- Use descriptive variable names with auxiliary verbs (e.g., isLoading, hasError).

- Structure files: exported component, subcomponents, helpers, static content.

Naming Conventions
- Use kebab-case for directories.
- Use camelCase for variables and functions.
- Use PascalCase for components.
- File names for components should be in PascalCase. Rest of the files in kebab-case.
- Prefix component names with their type (e.g. ButtonAccount.jsx and ButtonSignin.jsx, CardAnalyticsMain jsx and CardAnalyticsData.jsx, etc.)

Syntax and Formatting
- Use the "function" keyword for pure functions.
- Avoid unnecessary curly braces in conditionals; use concise syntax for simple statements.
- Use declarative JSX.

Ul and Styling
- Use DaisyUl and Tailwind CSS for components and styling.
- Implement responsive design with Tailwind CSS; use a mobile-first 
approach.

Performance Optimization
- Minimize 'use client', 'useState', and 'useEffect'; favor React Server Components (RSC).
- Wrap client components in Suspense with fallback.
- Use dynamic loading for non-critical components.
- Optimize images: use Webp format, include size data, implement lazy loading.

Key Conventions
- Optimize Web Vitals (LCP, CLS, FID).
- Limit 'use client':
- Favor server components and Next.js SSR.
- Use only for Web API access in small components.
- Avoid for data fetching or state management// Prompt
// Includes screenshot of the navbar from next.js site

I would like for you to recreate the image I have attached to this prompt.

Context:
- We currently have a "default" next.js site that's generated by running 'npx create-next-app@latest'.
- We're using an "src" file with @layout.js and @page.js .
- The image is of a "navbar" on the @https://nextjs.org/conf website.

Instructions:
1. Let's start from left to right on the navbar elements. Describe the navbar image.
2. Describe each element within the navbar. Including the elements' colors, specific shapes, likely border radii in pixels, etc.
3. First, create the "Next.js" text and the div that contains the "CONF24" text. The div should have a black border of .5px.
4. This "Next.js" text and div should be aligned left, about a "third" of the way across the page.
5. Next, create the "box" (a "short" rectangle) that contains the text "/". The border color of the box should be light grey.
6. Ensure that this "box" is at the centre of the navbar.
7. Next to this "box" should be the text "CHAT".
8. The "NEXT.JS On [insert black triangle]", "LOG IN" text should be aligned right. In the final "third" of the page. 
9. Finally, there should be a button to the right of the "LOG IN" text. It should have a dark blue background color, its border should be transparent with a 0px radius, its text should read "GET TICKETS" and the text's color should be white.
10. Please note that next to the "GET TICKETS" text is a white arrow with a circle around it with a white border color. 
See my result here. I mean, it’s pretty impressive, but it’s about “20%” off of the end result. Would I be able to discern where it’s wrong if: 1) if I didn’t have a reference image, and more importantly, 2), if I wasn’t comfortable with frontend dev? Would I have the “vocabulary” to make small padding or margin refinements? It’d be tricky.

Observation 2 - Cursor is nothing without its people models

Stripe is an incredibly important piece of infrastructure for many companies new and old. But, if you asked me to describe, say, Linear’s core value props, I likely wouldn’t throw “payment processing” into the mix. 

Perhaps when describing something like Airbnb I would allude to Twilio’s involvement, but again, is receiving a text message about your upcoming stay in Azenhas do Mar what makes you use or switch over to Airbnb? Unlikely. 

There is, however, a class of companies where their underlying infrastructure is a core component of the product experience: Vimeo is a video platform that uses Mux, Tide is a bank that leverages ClearBank. This isn’t necessarily a bad product trait, although it can increase a company’s platform or “steamroll” risk. 

Cursor, and many LLM-native companies fall into this bucket. So much so that when folk say “Cursor helped me build X” they should be passing at least ~50% of this praise onto Claude et al. Though, Cursor is already astutely addressing this risk with cursor small. 

As the company continues to add product depth by focusing on some v interesting problems [1][2] I think this 50% attribution rate will begin to shift. In fact, Cursor’s increasing ability to inject the “Optimal Context” into LLMs may end up flipping their relationship with LLM providers on its head. Will be an interesting watch.

Observation 3 - In-Context Editing

When working on my Next.js clone I often found myself hopping into Cursor Chat to make minor edits (think changing padding, easing animations, etc). As someone that’s very comfortable with CSS this was strange, why didn’t I just change 1px to 2px or #87CEEB to #000080? 

The thing is, you kinda get used to “writing code” in English, so my instinct was to continue to do so: “move that div a little to the left”. This isn’t a big deal when you’re familiar with the language/library that you’re using as you have the vocab: “move the <div className=”example”> 10px to the left”, or, if all else fails, you can just jump into the code and fix things.

But what if you don’t have the words? If someone has never worked with three.js before, they’ll have no clue how “alphaMap” impacts the opacity of their 3D object. Thankfully, three.js (& more specifically, lil-gui) might suggest an answer here.

lil-gui allows you to edit certain variables graphically so that you build a sense for how they impact your 3D scene: threejs.org/examples/#webgl_animation_skinning_morph.

What if Cursor could generate similar “ephemeral” and/or “malleable” UIs, but in real-time? Having briefly thought about how you’d scale this, it seems plausible given that Cursor can crawl third party docs, etc. This would be very cool.

Observation 4 - Selective Memory

Admittedly, I thought that Bill Gurley was erring on the side of bloviation when discussing the memory challenges of SOTA models [1][2][3]. Unsurprisingly, he’s totally right. But I’ll add one slight caveat — LLMs have “selective memory”. 

Let’s dig into some examples. I was recently working with Twitter’s API (which, btw, is now extortionate) and authenticated via OAuth 2.0. Sweet, all was going great. But, as I iterated through other errors within my codebase, I ran into an auth issue. Odd? 

At some point, the LLM decided to replace my OAuth 2.0 boilerplate with OAuth 1.0. I.e. the model, despite having the context that Cursor provides, “forgot” that I strictly asked for it to work within the OAuth 2.0 spec. This is likely due to the bulk of twitter API code on the internet using OAuth 1.0 (Twitter’s V2 endpoint that uses OAuth 2.0 was only released in 2021). 

Now, before anyone says it. Yes, I did accept the change that Cursor suggested, so the blame is technically, on me, but either way, the code suggested was incorrect. I’m only human, and perhaps LLMs are too.

What do I mean by “selective” though? Well, I’ve found that there are certain prompts/instructions that models treat as sacrosanct, even as your latter prompts contradict them (or even cancel them out entirely). In these cases, the model’s long-term memory is nearly “too good”.

Observation 5 - Local Optimum Loop (LOL)

I was trading notes on Cursor with a friend who summed up my own experience pretty well:

“I've had similar experiences with trying to do complex animations. Very easy for the output to get stuck in a local optimum and just loop. I find that I often have to "jump start" it by rewriting the existing code more significantly.”

For me, this issue was most apparent when attempting to implement the “NEXT grid”. Cursor did a truly awesome job of creating a crude “NEXT” outline by using CSS grid, but no matter what I tried (including using three.js instead), it couldn’t get anywhere near the finished product. Instead, I entered the “loop” described above.

Given my “experiment” involved writing no code myself, my attempt at “jump starting” the LLM came via narrowing the aperture of the task. So, my prompt went from detailing how the entire “NEXT” grid should look, to focusing on a single letter, and eventually, a single square within a letter. 

This approach initially improved results, but its efficacy decayed and I gradually found myself back at the “local optimum loop”. This did get me thinking about how much I still have to learn about prompting though! 

Ok, that’s a wrap to my “addendum” of problems that I’m equally excited to see Cursor solve. Never having to read a wall of stack traces again sounds like a pretty ideal end state to me. I’d love to say hi/spar with others who’ve been playing around with Cursor: alex@tapestry.vc. Thanks for reading, folk.

Observation 6 - You Should Subscribe

Subscribe

9

2

2

Share

Discussion about this post

CommentsRestacks

Ben Saltiel 
Sep 26, 2024

Liked by Alex Mackenzie

Really enjoyed this. Haven't played around with Cursor yet but everyone seems to be enamored. 

My guess is it's great for people like me that never built stuff but forsure for the more craftsman mindset builders, they will want more control. 

Reply

Share

liz 

Dec 2, 2024

I'm hands-on writing a lot more code these days, often in codebases where I have little context. It blows my mind how much faster I'm able to wrap my head around what's going on and the code suggestions sometimes feel truly like magic. I'm sold.

Reply

Share

TopLatestDiscussions

No posts

Ready for more?

Subscribe

© 2026 Alex Mackenzie · Privacy ∙ Terms ∙ Collection notice

 Start your SubstackGet the app

Substack is the home for great culture

 This site requires JavaScript to run correctly. Please turn on JavaScript or unblock scripts
