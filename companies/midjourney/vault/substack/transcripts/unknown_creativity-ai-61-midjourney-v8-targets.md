---
company: "Midjourney"
research_key: MIDJOURNEY
type: substack
source: "geekycuriosity.substack.com"
title: "creativity-ai-61-midjourney-v8-targets"
url: https://geekycuriosity.substack.com/p/creativity-ai-61-midjourney-v8-targets
date: unknown
fetched_at: 2026-04-21T22:35:54
discovery_provider: "manual_url_file"
relevance_score: 7
credibility: S3-S4
evidence: E2-E3
chars: 24249
---

# creativity-ai-61-midjourney-v8-targets

**Source**: https://geekycuriosity.substack.com/p/creativity-ai-61-midjourney-v8-targets
**Discovery query**: companies/midjourney/vault/substack/metadata/manual_urls_2026-04-21.txt:6

---

Title: Creativity AI #61: Midjourney V8 targets February, Google builds explorable AI worlds, and Ideogram goes transparent

URL Source: https://geekycuriosity.substack.com/p/creativity-ai-61-midjourney-v8-targets

Published Time: 2026-02-05T10:56:50+00:00

Markdown Content:
[![Image 1](https://substackcdn.com/image/fetch/$s_!GRUK!,w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F822202e9-4795-476e-9cd8-a6b19840dd3e_1456x816.png)](https://substackcdn.com/image/fetch/$s_!GRUK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F822202e9-4795-476e-9cd8-a6b19840dd3e_1456x816.png)

[Give a gift subscription](https://geekycuriosity.substack.com/subscribe?&gift=true)

![Image 2](https://substackcdn.com/image/fetch/$s_!jZRr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbbf412bb-9489-4197-b885-70857a13a2d8_562x562.png)

Available for iOS and Android

**Creativity AI** is a free weekly publication that brings together interesting articles and recent developments in AI art and creativity.

You can also read this newsletter on the [website](https://geekycuriosity.substack.com/).

The February 4th Office Hours dropped some concrete timelines. V8 training is done at 1024×1024 resolution. Guide and mod testing starts immediately. Rating party expected within a week. Public release roughly a week after that.

February release? Actually looking solid this time.

**Native 2K is the big story**

Forget upscalers. Midjourney started training native 2K (2048×2048) resolution this week. The goal is true high-resolution output, not post-processing trickery.

The new architecture supports arbitrary resolutions from 64px all the way up to 2048px and beyond. Native 2K means better small details (especially text) and cleaner results than any upscaler could deliver.

The team is still deciding whether 2K becomes the default, an optional premium mode, or something else entirely. Strong internal push to make it the default if costs allow. But here’s the tradeoff: higher resolution means higher cost. David acknowledged that 2K default would be more expensive, but believes the quality jump justifies it.

If they can make native 2K the standard experience, that’s a significant edge over competitors still relying on upscaling pipelines. Text rendering alone would benefit massively.

**V8 is “smart but also stupid in some unexpected places”**

David’s words, not mine. The model shows major gains in coherence, language understanding, and the ability to follow complex instructions. You might not even need the --no parameter anymore because V8 can parse negations directly. “A room with no elephants” could actually work as written.

But edge cases remain. Weird behaviors that won’t all be fixed at launch. Different prompting patterns from previous versions. If you’ve built muscle memory around V6 or V7 prompting, expect an adjustment period.

**What works at launch (and what doesn’t)**

Features confirmed working:

*   Style reference (sref)

*   Personalization

*   Mood boards

*   Multiple aspect ratios

Backward compatibility planned for existing mood boards, srefs, and personalization codes. Your library should transfer over.

What’s missing or limited at launch:

*   Image prompting (not available initially)

*   Variations (partial or different behavior)

*   Multi-prompts with --no (may not be necessary anyway)

The image prompting gap is notable. If your workflow relies heavily on image references, V8 launch day might not be your migration day. Worth planning around.

**Edit model follows V8**

The edit model is in parallel development and will ship after V8. Release window: anywhere from one week to one month post-V8.

Multiple image inputs may not be available at edit launch, either. Seems like both V8 and the edit model are shipping as foundations to build on, not complete packages.

**New create interface changes everything**

This might be the most underrated announcement. A completely new creation flow is being designed specifically for V8.

The concept: rapid low-resolution iteration, then scale to high resolution when you’ve found what you want. Think 64 images at 256px, explore fast, then fan in on your winners and upscale.

The current batch-of-4 workflow? Considered obsolete in the long term.

If this works as described, it fundamentally changes how you’d approach a Midjourney session. Less waiting, more exploring, scale up only what matters. I’m curious to see how it feels in practice. But I have to admit I’m already getting used to 4 images per batch.

**The bigger picture**

V8 isn’t just a model upgrade. David framed it as three shifts happening together: a smarter core model, a new generation of UI and workflows, and the foundation for powerful editing tools.

The codebase was completely rewritten. New architecture means faster follow-up releases and easier fine-tuning. Niji version planned after V8 stabilizes. Rapid iteration post-launch is the expectation.

Mobile improvements are coming after V8, too. The goal is the first “truly strong” Midjourney mobile app. Plus ongoing work on social features.

Oh, and four hardware projects are in progress. Two long-term, two intended for near-term purchase. But don’t expect announcements until products are available and close to launch. No hype-driven reveals.

February is shaping up to be a busy month for Midjourney users. Keep an eye on the rating party announcement. That’s your signal that V8 is about a week out.

Ideogram now supports transparent backgrounds directly in generation. Set the model to “auto” and add “transparent background” to your prompt. That’s it.

The pitch is appealing: turn your idea into print-ready designs in a single session. Native transparency, 8K upscale, and editing tools all built in. No need to jump to a separate background removal tool afterward.

**My testing**

I tried it with a “Geeky Animals” text design featuring a cat illustration. Generated with transparent background, then dropped it onto a colored square in Canva. Quick and painless.

But I noticed something. The transparent outputs seem simpler and less detailed than regular non-transparent generations. The model appears to be optimizing for clean edges and easy extraction rather than complexity.

**When this works well**

For quick graphics like text treatments, logos, icons, or simple illustrations you need to composite onto other backgrounds? Does the job nicely. The workflow savings are real when you don’t have to mess with background removal tools.

For highly detailed artwork where you want transparency? I’ll need to test this more extensively to find out.

Example of Ideogram transparent PNG output

`art nouveau typography art “Geeky Animals” in blue and yellow featuring a cat on a transparent background  (aspect ratio 2:3, magic prompt off, auto model)`

[![Image 3](https://substackcdn.com/image/fetch/$s_!M3X_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea6d88e8-9d0b-4e32-b894-89ffed907eb3_688x990.png)](https://substackcdn.com/image/fetch/$s_!M3X_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea6d88e8-9d0b-4e32-b894-89ffed907eb3_688x990.png)

The edges are clean and easy to overlay onto color backgrounds.

[![Image 4](https://substackcdn.com/image/fetch/$s_!PQZ9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bce6026-fdc4-4122-86c6-45e8caffddff_1060x521.png)](https://substackcdn.com/image/fetch/$s_!PQZ9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bce6026-fdc4-4122-86c6-45e8caffddff_1060x521.png)

Left: Transparent PNG on white background. Middle: On the black background. Right: On the gray background. 

[Perplexity](https://perplexity.ai/pro?referral_code=YQGPR1B9) added [Kimi K2.5](https://www.kimi.com/ai-models/kimi-k2-5) to its model lineup, now available for Pro and Max subscribers. It is always quick to adopt new models.

But I need to be upfront about something: using Kimi K2.5 through Perplexity isn’t the same experience as using it on the official Kimi website. Not even close.

**What makes Kimi K2.5 interesting**

Moonshot AI released this open-source multimodal model on January 27, 2026. It’s designed to actually complete work rather than just chat about it.

A few standout capabilities:

*   **Visual coding** – You can feed it text, images, or video and get functional front-end code back. Full websites with animations. Page layouts that match your visual references with high accuracy.

*   **Agent Swarm** – This one’s wild. Kimi K2.5 can coordinate up to 100 AI sub-agents working in parallel. Each agent independently searches, generates, analyzes, and organizes information. Moonshot claims this cuts execution time by up to 4.5x for large-scale research and batch tasks.

*   **Production-ready outputs** – Instead of drafts you need to polish, you get deployable artifacts. Word documents. PDFs with proper LaTeX formatting. Spreadsheets with working formulas and pivot tables. Functional websites ready to publish.

The model offers four interaction modes: Instant for quick responses, Thinking for complex problems, Agent for research and content creation, and Agent Swarm for those massive parallel tasks.

**My experience: Perplexity vs native Kimi**

I tested both versions. The difference is significant.

When I asked Perplexity’s Kimi K2.5 to generate a website, I got a page of HTML code. Just code. I had to copy-paste it into a file, create the HTML document myself, and manually link all the web assets. Asking it to bundle everything into a zip file failed.

When I asked the same thing on the [official Kimi website](https://www.kimi.com/ai-models/kimi-k2-5)? It generated a live, working website I could interact with immediately, along with downloadable assets ready to go. You can see an example here: https://4dkdy66x5jdsi.ok.kimi.link/

Perplexity gives you access to the model and expands your LLM choices. That’s valuable. But you’re not getting the full Kimi K2.5 experience with all its bells and whistles.

The output by Perplexity

[![Image 5](https://substackcdn.com/image/fetch/$s_!k5sc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa96d183f-0c81-4698-b2d7-56f82f8c6bc7_740x818.png)](https://substackcdn.com/image/fetch/$s_!k5sc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa96d183f-0c81-4698-b2d7-56f82f8c6bc7_740x818.png)

Perplexity’s output

The output by Kimi K2.5

[![Image 6](https://substackcdn.com/image/fetch/$s_!_58b!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6760bfd2-3a59-4e34-babf-1ae20b8af9ec_1232x1136.png)](https://substackcdn.com/image/fetch/$s_!_58b!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6760bfd2-3a59-4e34-babf-1ae20b8af9ec_1232x1136.png)

Kimi website

You can also download the full website assets from Kimi website

[![Image 7](https://substackcdn.com/image/fetch/$s_!yJUF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbbb94313-b97f-466a-9abc-072b883c9be9_386x470.png)](https://substackcdn.com/image/fetch/$s_!yJUF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbbb94313-b97f-466a-9abc-072b883c9be9_386x470.png)

Assets for download from Kimi

Google DeepMind released [Project Genie](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/), an experimental research prototype now available to Google AI Ultra subscribers in the U.S. It launched January 29, 2026.

This caught my attention for a specific reason. Creating immersive virtual worlds is something David Holz has talked about wanting Midjourney to do eventually. A space where images and videos generate on the fly, where you can get completely lost in an AI-created environment. Google seems to share that ambition. And they’ve already started building it.

Is this one of those “secret projects” David mentions in Office Hours? Who knows. But Google isn’t waiting around.

**What Project Genie actually does**

It’s powered by Genie 3, what Google calls a general-purpose “world model.” Unlike static 3D snapshots or pre-rendered environments, Genie 3 generates the world around you as you move through it. Real-time. Dynamic physics and interactions.

Three core capabilities:

*   **World Sketching** – Create living environments using text prompts and images. Design your character, choose how you want to explore (walking, flying, driving), and pick your perspective (first-person or third-person).

*   **World Exploration** – Move through your generated world in real time. The system creates the environment ahead of you based on your actions. There’s no pre-built map. It generates as you go.

*   **World Remixing** – Build on existing worlds by modifying their prompts. Explore a gallery of curated worlds for inspiration. Download videos of your creations.

The procedural generation aspect is particularly interesting. Environments that don’t exist until you walk into them. Theoretically infinite content generated on demand.

**What this means for creative AI folks**

A few things stand out, despite its various limitations and constraints:

Building interactive 3D environments used to require teams of artists, developers, and expensive software. Now, one person can generate explorable worlds from text descriptions and reference images. That’s a significant shift in what’s possible for solo creators.

For animators, filmmakers, and game designers, this becomes a rapid prototyping tool. Visualize concepts before committing to full production. Test ideas cheaply.

Link to [video](https://www.youtube.com/watch?v=YxkGdX4WIBE)

The [Chroma Awards](https://chromaawards.com/) are back. Pre-registration for Season 2 is now open.

Season 1 made this the world’s largest AI Film, Music Video, and Games competition. The numbers: over 6,500 submissions, $1M in free tool trials given away, and $190,000 in cash prizes from sponsors.

If you’re creating AI films, music videos, or games, this is probably the biggest stage available right now.

Tsuchiya Kōitsu (1870-1949) was part of Japan’s shin-hanga (”new prints”) movement, which revived traditional ukiyo-e woodblock printing while mixing in Western techniques. He studied under Kobayashi Kiyochika, a famous Meiji-era print designer, but didn’t develop his signature landscape style until age 61. Late bloomer.

His work features precise linework and classic Japanese subjects: pagodas, temples, castles. But the colors are what grab you. Kōitsu pushed saturation to extremes. Cherry blossoms go deep rosy with purple and blue tints. Trees appear in emerald green touched with turquoise. Skies gradient from pink into deep blue.

He handled night-time scenes beautifully too. Greens, blues, and purples layered together to create quiet, almost meditative atmospheres. Rainy scenes got their own treatment: grayish-green palettes that somehow feel damp just looking at them.

Some people compare his aesthetic to manga because of those bold color choices. I can see it. There’s an illustrative quality that feels both traditional and surprisingly modern.

`Blue-hour hush over hilltop castle, dreary clouds and quiet tranquility, deep rosy shades edging stone, grayish-green pines, sky gradients drifting to indigo, shin-hanga woodblock feel, bold tones yet serene --ar 16:9 --profile ppjylid  --v 7`

[![Image 8](https://substackcdn.com/image/fetch/$s_!0El9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65686dd0-0aad-4973-be59-e4b5ae1a0af5_1456x816.png)](https://substackcdn.com/image/fetch/$s_!0El9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65686dd0-0aad-4973-be59-e4b5ae1a0af5_1456x816.png)

`Harbor skyline with shrine gate, emerald water and deep blue sky gradient, turquoise neon skims the waves, dramatic rim light after rain, woodblock textures, ukiyo-e revival palette, quintessentially Japanese sights --ar 16:9 --profile ppjylid  --v 7`

[![Image 9](https://substackcdn.com/image/fetch/$s_!na8f!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d3af4c3-7f90-4a61-b8ea-935de244e0c1_1456x816.png)](https://substackcdn.com/image/fetch/$s_!na8f!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d3af4c3-7f90-4a61-b8ea-935de244e0c1_1456x816.png)

`Tokyo night rain, pagoda silhouette rising beyond neon billboards, saturated purples and deep blues pooling in rain-slicked streets, turquoise highlights, dramatic directional light, precise linework, ukiyo-e revival with Western poster boldness --ar 16:9 --profile ppjylid  --v 7`

[![Image 10](https://substackcdn.com/image/fetch/$s_!jLbc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F694f638a-6029-41d3-a274-34cbf3453f65_1456x816.png)](https://substackcdn.com/image/fetch/$s_!jLbc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F694f638a-6029-41d3-a274-34cbf3453f65_1456x816.png)

`Pont de la Guillotière stylized like tiered pagodas, Saône shimmering with rosy highlights, emerald trees and grayish-green mist, shin-hanga precision, heightened colors, gentle rain, tranquil street silhouettes under deep blue twilight --ar 16:9 --profile ppjylid  --v 7`

[![Image 11](https://substackcdn.com/image/fetch/$s_!HWV8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36b51e59-db2d-4bc9-9738-9d90aefda497_1456x816.png)](https://substackcdn.com/image/fetch/$s_!HWV8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36b51e59-db2d-4bc9-9738-9d90aefda497_1456x816.png)

`Vieux Lyon riverside at night, lantern-glow reflecting on rain-slick cobbles, bold turquoise and deep blue palette, ukiyo-e revival with Western techniques, propulsive atmosphere yet hushed, pagoda-roof echoes in gables, sky gradient rolling in --ar 16:9 --profile ppjylid  --v 7`

[![Image 12](https://substackcdn.com/image/fetch/$s_!SiQn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1218aa45-f899-426b-b893-850be50a9fd0_1456x816.png)](https://substackcdn.com/image/fetch/$s_!SiQn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1218aa45-f899-426b-b893-850be50a9fd0_1456x816.png)

`Parc de la Tête d’Or lake at night, pavilion silhouette with temple echoes, cherry blossoms drifting, bold saturated purples and blues, reflective water textures, ukiyo-e revival composition, gentle drizzle, luminous tranquility --ar 16:9 --profile ppjylid  --v 7`

[![Image 13](https://substackcdn.com/image/fetch/$s_!U6rw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F652935f6-bbc6-4677-81b9-52c746a5bb0a_1456x816.png)](https://substackcdn.com/image/fetch/$s_!U6rw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F652935f6-bbc6-4677-81b9-52c746a5bb0a_1456x816.png)

`Basilica of Fourvière crowning Lyon above the Saône, serene evening drizzle, saturated purples and emerald greens, shin-hanga woodblock gradients, precise linework, quiet tranquility with dramatic lighting, cherry blossoms framing, timeless ukiyo-e revival poster style --ar 91:51 --profile ppjylid  --v 7`

[![Image 14](https://substackcdn.com/image/fetch/$s_!VVPE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F209390b2-ea30-4cc5-8338-7538df643b7a_1456x816.png)](https://substackcdn.com/image/fetch/$s_!VVPE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F209390b2-ea30-4cc5-8338-7538df643b7a_1456x816.png)

**Color Palette**

`bright colors, highly saturated, bold tones, heightened colors, deep rosy shades, purples, blues, emerald green, turquoise, pink, deep blue, grayish-green palette`
**Lighting & Atmosphere**

`dramatic lighting effects, propulsive atmospheres, quiet tranquility, dreary mood, evening scenes, night scenes, rainy scenes`
**Composition & Technique**

`illustrative compositions, precise linework, woodblock printing, shin-hanga, ukiyo-e revival, Western techniques`
**Subject Matter**

`Japanese landscapes, pagodas, temples, castles, cherry blossoms, trees, sky gradients, quintessentially Japanese sights``. --ar 16:9 --sref 18954037 --profile ps3mcjo --sv 6  --v 7`

[![Image 15](https://substackcdn.com/image/fetch/$s_!_5Nc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd8c001d-adec-48eb-aaec-f29ab1b886d9_1456x816.png)](https://substackcdn.com/image/fetch/$s_!_5Nc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd8c001d-adec-48eb-aaec-f29ab1b886d9_1456x816.png)

`. --ar 2:3 --sref 18954037 --profile ps3mcjo --sv 6  --v 7`

[![Image 16](https://substackcdn.com/image/fetch/$s_!VEJT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33e2c2bd-bb3e-4a6d-b1ad-0900cf80e38d_896x1344.png)](https://substackcdn.com/image/fetch/$s_!VEJT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33e2c2bd-bb3e-4a6d-b1ad-0900cf80e38d_896x1344.png)

`. --ar 2:3 --sref 18954037 --profile ps3mcjo --sv 6  --v 7`

[![Image 17](https://substackcdn.com/image/fetch/$s_!51EU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36ebbca8-6c11-42f8-9ec6-4e7a9444e75a_896x1344.png)](https://substackcdn.com/image/fetch/$s_!51EU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36ebbca8-6c11-42f8-9ec6-4e7a9444e75a_896x1344.png)

`. --ar 1:1 --sref 18954037 --profile ps3mcjo --sv 6  --v 7`

[![Image 18](https://substackcdn.com/image/fetch/$s_!Sh_z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81cd46a9-0b2f-4084-bc8a-5d522510e6a3_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!Sh_z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81cd46a9-0b2f-4084-bc8a-5d522510e6a3_1024x1024.png)

**Cover prompt:** Muscular warriors duel across alien basalt ridges, one with glowing plasma halberd, the other with scarred steel sword, heat shimmer between them, cyan ion lightning rakes the sky, cinematic low angle and dynamic motion lines --ar 16:9 --sref 18954037 --niji 7

I hope you like this article!

Thank you for reading and happy creating!

[Share](https://geekycuriosity.substack.com/p/creativity-ai-61-midjourney-v8-targets?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[Upgrade to Annual Subscription](https://geekycuriosity.substack.com/subscribe)

[Share Geeky Curiosity](https://geekycuriosity.substack.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share)
