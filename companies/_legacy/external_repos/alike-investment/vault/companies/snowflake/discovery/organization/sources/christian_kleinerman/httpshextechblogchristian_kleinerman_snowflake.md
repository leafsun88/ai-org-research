---
type: org_person_source
person: "Christian Kleinerman"
title: "Executive Vice President of Product"
date: 2026-04-08
url: https://hex.tech/blog/christian-kleinerman-snowflake/
chars: 12817
credibility: S3
evidence: E2
---

# https://hex.tech/blog/christian-kleinerman-snowflake/

Skip to main content

June 18, 2025

Christian Kleinerman, Snowflake: mapping the next era for data and AI 

Share:twitterlinkedin

On the third day of Snowflake Summit, inside of Club Hex, Barry sat down for a fireside chat with Christian Kleinerman, Snowflake’s Executive Vice President of Product.

Christian brings a rare perspective shaped by decades at the helm of some of the most foundational data and infrastructure products in tech. He started his career on the SQL Server team at Microsoft and later led infrastructure for YouTube at Google; now he steers product strategy at Snowflake. Along the way, he’s seen the data ecosystem evolve from on-prem relational systems to cloud-scale platforms — and now, into the AI era.

We talked with him about the surprises he’s encountered with AI’s rapid ascent, what he finds valuable about ecosystem partnerships, and why he thinks the next big opportunity for Snowflake — and the broader ecosystem — lies in becoming trusted custodians of enterprise data. 

This transcript has been edited for clarity.

What's the biggest lesson you’ve internalized about building products?

You have to be a user of the product. Even to this day, I use Snowflake — even for things that I should not be using Snowflake for. This is embarrassing, but my wine cellar at home runs on Snowflake. It's very different when you're trying to do a demo.

The simple answer is to use the product. Use the product, but not in the 'I clicked on a couple of things, and I think I know it now' way. Use it in the way that it's intended. Find the problem and use it from beginning to end to answer the question, and then you're going to realize what works and what doesn't work as well.

What have been the biggest surprises for you about AI in the last few years?

I have no problem admitting that I underestimated the potential and impact of AI. One of our board members, Mike Speiser, started sounding the alarm about three years ago. He was saying this thing is bigger than the Internet. We were like, 'What are you talking about?' In my mind, it was generative AI, so it was all about, 'What can you create?' Yeah, you can have an editor that helps you write SQL. That was the main use case that we focused on and it is still a legitimate use case.

I remember telling him that this was not going to be as impactful to the world of data. That's how naive I was. The piece that I missed was its ability to understand, synthesize, reason, and even think, which is a strong word. But that was not clear two years ago. Two years ago, we built Document AI, which lets you extract fields from documents, and we built Snowpark Container Services, where you can host your own LLM. At the time, hosting LLMs was like doing inference in a machine learning model. These days, it’s like a fancy cluster, which is very complex and there is a lot of Python code around it. The models have gotten really, really advanced.

What’s unclear about the immediate future?

A lot of things are up in the air. Everyone is now an agent platform. And because nobody wants to be in a silo, everyone's agents could potentially talk to everyone else's agents. Everyone then repeats MCP and A2A as if they need to be buzzword compliant.

The reality is that there's going to be next-generation workflows and next-generation chains of operations. There's going to be interoperability between the systems. I was at a dinner last night, and someone was talking about, 'Oh, you remember WSDL?' That was how SOAP services used to discover SOAP services. That's a similar thing, 'Hey, what can I do with you?' And then there's a standard calling convention.

I think some of those things are going to get reincarnated. What agents do you know about? And how do I invoke your agent? And how do I know what you can do? This is literally an MCP type of protocol. There's a lot that is going to evolve.

At this point, I am very careful about making any predictions on AI and how things play out. It's moving very fast. But the thing that’s most interesting to me is that the technology right now is way more capable than what most people are already using — and that's the opportunity.

How do we map the next couple of years for AI?

It's complicated, and whatever I say might change a couple of months from now. I think one thing that is clearer is that pure-play model companies are not viable. The way the models monetize is through the application of the models and the experiences. OpenAI’s money comes from ChatGPT more so than pure API, which is trending toward becoming a) a commodity, and b) pricing-wise, a semi-race to the bottom. Not all the way to zero, but that's where it trends — its application is replacing entire industries.

In many ways, Google search itself is a formidable franchise, a very profitable franchise, and it's getting threatened. So, I think that's how it happens: application and moving up for the model products. All of them will either build and buy apps or they'll get acquired by an apps company, an application of AI.

In the enterprise world, I think everything will revolve around enterprise data. Yes, there are some use cases for ChatGPT for the enterprise, and OpenAI is selling it incredibly aggressively, and I think they're getting traction. But the true value is when you can understand enterprise data — and enterprise data, as many people have realized in the last couple of months, is easy until things like security, compliance, and governance kick in. That's where I think we, and even Databricks, and the cloud providers are in a good position, because we have become trusted custodians of data. I think what we're trying to do, which is bringing AI and building value on top of AI while preserving and respecting governance, is an opportunity for us.

You all are leaning hard into Iceberg – which on its face is about data portability, which is traditionally something database vendors are trying to avoid! Why? 

This is what customers want. You can
