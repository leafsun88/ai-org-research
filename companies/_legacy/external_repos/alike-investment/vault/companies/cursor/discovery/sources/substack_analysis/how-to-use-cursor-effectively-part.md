---
ticker: CURSOR
type: substack
title: ""
author: ""
date: 
url: https://andybrandt.substack.com/p/how-to-use-cursor-effectively-part
chars: 8132
credibility: S2
evidence: E2
---

# 

**Author**: 
**Date**: 
**URL**: https://andybrandt.substack.com/p/how-to-use-cursor-effectively-part

---

How to Use Cursor Effectively (Part 1) - by Andy Brandt

Andy's Mind

SubscribeSign in

How to Use Cursor Effectively (Part 1)

Andy Brandt

May 17, 2025

1

Share

Since December '24, I've switched from GitHub Copilot to Cursor and definitely don't regret it. It enables very convenient use of various AI model support while working on code, significantly increasing a programmer's capabilities and work speed. However, making good use of this tool's power requires skillful utilization of its functions and adherence to one very important rule.

You're Still in Charge of the Code

This is the most important rule! You still need to understand what you're doing and know how the code you're creating works and why. This requires at least basic programming knowledge and some hands-on experience. Without these fundamentals, AI will quickly lead a "vibe-coder" astray.
Example: I'm creating an application where I deliberately don't use ORM, instead using my own class that handles the database through SQL queries. When creating one of the functions, AI generated code for me that included the introduction of a specific ORM. If I didn't understand what was happening, what ORM is (and also why I didn't want it in this project at that moment), I obviously wouldn't have noticed anything because the proposed code was coherent and worked. Except that it wasn't consistent with my decision and with how the rest of the application was written, which would lead to problems in the future.
So when using AI support, you must maintain a "leadership role" and control what's happening.

Of course, the level of this control doesn't have to be the same throughout the application. I've learned to divide my project into three "zones":

core, where I want to understand every line of code (I still use AI to generate code here, but I only accept it when I fully understand what it does),

an intermediate area, where I want to understand how all methods/functions work but don't need to know the details, and

the rest, where I go full - as they say nowadays - "vibe coding."
Example: in the application I'm currently developing, the core is an AI agent system based on the AG2 framework. There I maintain full control, examining every line of generated code before accepting it and writing significant amount of code myself. I also use AI support to help find bugs or suggest solutions, but I thoroughly review everything before implementation. The intermediate zone includes classes handling user interaction logic - there I know how they work, but do not analyze them line by line. And "the rest" is HTML and JavaScript code that forms the application interface - there I don't even know which JS functions are used and for what, because it's not really important - what matters is that it works.
Planning Actions

For minor changes - such as fixing a small bug or making a slight change to existing functionality - you can use AI support simply in "Agent" mode by telling it what you need.

For larger changes, however, it's essential to separate planning from implementation. This applies especially when adding major functionality or restructuring application logic while using AI to help write code.

When tackling a larger change, I follow this process:

Step 1: I begin with a comprehensive prompt describing the background (current state and general goals). Then I outline in it the intended steps to achieve my objective - what to introduce or change, architectural considerations, and any new solutions to incorporate.

During this initial phase, I engage in dialogue with the models - seeking opinions, exploring alternatives, and refining ideas. Here, the AI isn't generating code but helping design the change. For this purpose, I typically use Cursor's "Ask" mode or my custom "Analysis" mode.

Step 2: Once I've developed a satisfactory plan, I have the model document it along with the overall goal and a numbered list of implementation stages. Each stage description includes what will be accomplished and sometimes pseudocode or actual code showing key structures. I ensure each stage concludes with something verifiably complete and functional.

After receiving this document, I carefully review and edit it as needed before saving it to the project's documentation directory (usually /doc).

Step 3: For code creation, I switch to Cursor's "Agent" mode and point the model to my plan document (using Cursor's context selection feature). I request code generation for specific stages, and we collaborate until each stage works correctly, including tests. This stage-by-stage approach consistently yields excellent results for substantial changes.

This structured process prevents AI assistants from getting lost during complex changes. The problem typically occurs because they lose context - as new messages in the chat accumulate our initial instructions scroll out of the context window, causing the model to "forget" the purpose of the changes. Consequently, it begins generating inconsistent or off-target solutions. With a reference plan in the chat context (thanks to the plan file being kept in the context by Cursor) and clear stage-by-stage direction, the AI maintains understanding of both the current task and the broader goal.

The earlier planning phase also leverages the models' knowledge at a higher abstraction level, discussing solution options conceptually before implementation. This collaborative planning produces higher quality designs and, ultimately, better results.

AI Needs Documentation Too

We typically assume that AI models' training data includes comprehensive knowledge about programming languages, libraries, and tools. This is generally true, especially since most documentation and much source code is freely available online, making it an accessible part of training datasets.

However, remember that with such massive amounts of data, finding the relevant information presents challenges even for sophisticated models. Additionally, while programming languages evolve slowly and rarely break backward compatibility, many libraries and frameworks develop rapidly. As a result, the information our model draws from its training data about them will very quickly simply become outdated!

Fortunately, Cursor addresses this by allowing us to create a RAG (vector store) with documentation of our choice. In Cursor preferences under the Features tab, after scrolling down, you'll find a Docs section. The Add new doc button lets you incorporate additional documentation for your libraries.

Cursor attempts to process indicated pages comprehensively, including their subpages. It's helpful to verify what's been processed by clicking the open book icon, confirming what's available to the models.

Sometimes - depending on how source pages are structured - you'll need to add documentation manually page by page, but this effort is worthwhile for libraries and tools central to your project. Once added, all Cursor models that support client databases will effectively utilize this documentation.

Keep two important points in mind:

The documentation database isn't project-specific or stored in project files. This can be inconvenient when working across multiple projects that require different documentation sets.

Cursor doesn't automatically update documentation when newer versions become available or links change. When using tools or libraries that receive updates, you'll likely need to remove outdated documentation and add the current version manually.

In the Next Episode: About Modes

This article has grown quite long, so I've decided to split it into parts. In the next installment, I'll explore how to effectively use Cursor's various working modes, including how to create and leverage your own custom modes.

Subscribe

1

Share

Discussion about this post

CommentsRestacks

TopLatestDiscussions

No posts

Ready for more?

Subscribe

© 2026 Andy Brandt · Privacy ∙ Terms ∙ Collection notice

 Start your SubstackGet the app

Substack is the home for great culture

 This site requires JavaScript to run correctly. Please turn on JavaScript or unblock scripts
