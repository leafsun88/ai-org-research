---
type: youtube_transcript
ticker: DDOG
title: "Olivier Pomel and Alexis Lê-Quôc on Datadog’s origin, AI, and more | This Month in Datadog"
channel: "Datadog"
date: 2026-04-07
video_id: RRl9KM6QM8c
url: https://www.youtube.com/watch?v=RRl9KM6QM8c
transcript_method: youtube-transcript-api
credibility: S2
evidence: E2
---

# Olivier Pomel and Alexis Lê-Quôc on Datadog’s origin, AI, and more | This Month in Datadog

**Channel**: Datadog  
**Date**: 2026-04-07  
**URL**: https://www.youtube.com/watch?v=RRl9KM6QM8c

## Transcript

Hello, and welcome to another episode of 
This Month in Datadog. This month we have   a very special episode for you. It's one 
I've been looking forward to for a while.   Today, I'm going to sit down with our co-founders, 
Olivier and Alexis. Thank you both for joining us.   And we're live from New York City. Exciting. It's 
exciting. So one issue I had when preparing for   this episode was there's far more that I want 
to ask than we have time for, realistically,   so let's just get started. And let's start 
at the beginning, where did you first meet?   We met, we actually half met, right? We 
didn't fully meet. This was I think what ‘96? Yeah, let's not reveal our ages too much. But 
you know we were in college, not the same year.   Yeah. And the story is interesting, because I 
was part of the team that ran the campus network,   and Alexis was caught hacking into the 
campus network. So he was court marshaled by   the team of students and then sentenced 
to disconnection from the internet. And I   carried out the sentence. So that was the extent 
of our relationship then. Yeah, so he knew of me   because I had done something, allegedly, done 
something bad. But I was like, I just showed up   you know in my dorm room. It's like, oh there's 
no internet in my computer. What's wrong? And   only much later did I realize 
that this was a premeditated act.   It's definitely an interesting first meeting. 
And the second time you met, I realized, it's a   little cathartic for me to know that I wasn't the 
only one in a windowless room early in my career.   And the windowless room I was in was also the 
server room for the dev servers. So it was a   trifecta of no natural light, unbelievably 
cold, and really, really loud. So when was   the first time you actually worked together? We 
worked together at IBM. So this was, I guess,   upstate in Hawthorne and it was in research. Yes. 
Yeah. R&D. It was a windowless office. It was not   particularly cold. But we were working on email 
protocols back then. So that's when we actually   formally met and worked together the first time. 
It was not so cold because, I don't know if you   remember, we blocked the AC vent. I don't remember 
that. So do we have you to blame for POP3?   Close, close, but not completely. Yes. More IMAP. 
IMAP. Oh, okay. Got it. So they say third time’s   the charm, and viewers might be thinking this 
is where the Datadog story begins, but it's not.   But to me, it is where the Datadog origin story 
really begins. So can you tell us a little bit   about Wireless Generation? Yes, so Wireless 
Generation is, I think it was the third startup   we worked for or something like that. So we work 
for a few startups. We worked together at the,   how you call it, the tail end of the dot com boom 
and the full extent of the dot com bust. So we've   been through that, which was you know very 
interesting in many ways. It was crazy. Yes.   In ways that you know are fairly familiar with 
what we see today, you know? So we learned a   number of things about you know what it looks like 
when you start a company, also a number of things   about you know what can go wrong, and you know the 
mistakes you can make as you, especially as you   try and build new products to market. And so we 
spent a few years there, then we started working   together at this education software company called 
Wireless Generation. And it's a startup that   actually worked in the world of education, which 
is a fantastically interesting space but also   I would call it a brutal space you know to build 
a business and build a company. And you know we,   that's where the idea of Datadog was born. The 
backdrop is that Alexis run the operations team   and I run the development team and we built the 
team pretty much from scratch. And we were very   good friends, it was our third or fourth company 
together already. We hired everybody on our teams.   We tried not to hire any jerks, and yet you 
know the teams are fighting. Yeah. Yeah. And   this was one of the early sort of real SaaS you 
know businesses, because you know back then, early   2000, you had you know everybody's trying to use 
Hotmail and so on, but this was very B2C. So B2B   as SaaS was fairly new, so everybody was trying 
to figure out how to run it. And this was still,   we were still operating as you know the dev 
team, like you know build the code, write it,   it runs on my machine, that means it's okay, 
throw it over the wall. The ops team’s like, okay,   we have this, we have to run it in production, 
oh, it doesn't work, it crashed, what do we do?   And a lot of fingerpointing naturally happened. So 
that thing gave us early inspiration for Datadog.   And so the inspiration was not to build systems 
management monitoring, any of that. Like we didn't   come from that world. The inspiration was let's 
bring dev and ops together, let's get the teams to   talk to each other, you know. Let's not have you 
know the dev team coming to complain to me that   you know the ops people don't know what they're 
doing. Or the ops team complaining to Alexis   that you know the devs are cowboys who you 
know ship anything and they don't understand   the applications. Yeah and they're–They don't 
have to be on call for it. Exactly, yeah, they   don't wake up in the middle of the night to fix 
it. So it's, those were the days, I guess. Yes.   And so the initial vision was we bring them into 
one platform, have them speak the same language,   and work together. It was also at 
the time when DevOps was nascent,   and you know I think the, in retrospect, the 
thing we didn't fully understand then was that,   so cloud was going to explode, obviously. And at 
the heart of the cloud explosion there would be a   movement to bring together dev and ops much 
closer than it used to be, some disintermediation   of the work of provisioning and managing hardware, 
and all of that stuff. And that what we were   doing, which is bring both dev and ops in the 
same platform was actually going to central   to cloud adoption. So I would like to say it was 
all a beautiful plan that worked out. Turns out   I think we're also pretty lucky in that we didn't 
fully understand the implications of what we were   doing at the time. Yeah. Unless you did. You did? 
I wish I could say it wasn't a master plan. Though   I looked at the slides we put together 
at the very beginning of the company, and   we haven't veered too much. I mean we've built 
much more than we had planned, but we didn't do   some you know 180 or something like that. So 
I think the way we thought it could work out   ended up not being too far from what 
happened. Interesting. So one lesson   you said you learned there was, we believe in 
learning over knowing. Can you expand on that?   So when you start a company I think there are two 
ways you can go about it, two extremes. There's   one extreme where you say, we need to build 
everything from scratch, absolutely everything,   right? And the other extreme is more you know 
the you cargo cult everything. It's like, oh,   this big company that's successful they do it 
this way, thus we should do it the exact same way.   I think we try to find kind of a happy medium but 
always going back to what we can see, what the   reality is telling us. I think we tried to be 
very pragmatic but not sufficiently grounded in   what we had learned early on in you know Wireless 
Generation you know the way you run teams, the way   you think about product, and stuff like that. So 
I think that we found our way effectively. That's   how my interpretation of learning over knowing. 
And on the product side you know again if you look   back at our influences, so we spent eight years 
building and shipping software and SaaS that was   used by teachers. And the one thing we realized 
at the time was that we're not a good proxy for   the customer. We have to learn from the customer 
and the user what actually matters, what we need   to build, what's valuable. And we have to be 
very humble in that conversation like our ideas,   maybe they're interesting, but really what matters 
the most is to understand the problem, and what we   can do, and who we can make life better for, for 
these customers. So we didn't have that, most of   the folks who go into building dev 
tooling, or you know ops tooling,   or security, or you know all the things 
we do, start from their own problems.   We started from an experience that was building 
for others. So we were, when we started Datadog,   the biggest fear was to build something 
that would not solve a real problem,   a really valuable problem. And so we started from 
day one with that focus on the customer, the user,   what their life was, what their problems 
were, and how we could solve those problems.   So that brings us to Datadog. You mentioned that 
Datadog was not founded to solve the monitoring   problem. What problem were you really trying 
to solve? What were you building? We had to   basically look for people who we thought had 
a similar problem. So the way we did that,   we looked up a bunch of conferences, and 
they were pretty low-key conferences,   not like the big commercial events. I remember 
going in a kind of a semi-abandoned office space   in the valley on a Saturday morning, just finding 
a bunch of other folks who were also interested in   solving the problem of how do you get dev and ops 
to work together to operate these software stacks,   you know, to basically support the entire 
software life cycle. And so the way, we didn't   go there and say, oh, we have this, we figured 
out everything, and then, do you want to buy it?   We went there with the humility to ask, okay, this 
is, we think we have this problem, do you have a   similar problem? Please tell us more about it. 
And the interesting discovery I think we made is,   because we didn't start the conversation with 
basically a sales pitch, or the only question is,   tell us about your problem, then it was people 
were really extremely eager to share, to explain,   okay, this is what I have, this is I'd love to 
have something that solves the problem I have,   and so on. So it really get us to start 
the conversation and to try to understand,   they weren't customers, but folks that may become 
customers at one point, what their actual pain   points were, not something you know mediated 
by some marketing or something, but really.   And we discovered that those pain points were not 
unlike the ones we had. So it gave us some amount   of confidence like, okay, maybe there's 
something there, we got to keep digging.   But it was really like these small, 
initially fairly small, fairly deep events,   you know deep as in like practitioners, not, you 
know, no theory, just battle scars, and you know   war stories, as it were. And Alexis makes 
it sound like we're really humble people and   just looking to learn. Turns out like we were 
forced to be humble, because, as Alex said,   we were not very successful in fundraising, you 
know? So the vision when we started Datadog was,   hey, we'll create this platform. It's going to 
be a collaborative data platform that is going   to bring together many different teams across 
dev and ops. And we pitched it to investors,   nobody wanted to invest in it. We applied to 
Y Combinator, we presented to the team there,   we got rejected from Y Combinator. I have an 
email from Paul Graham that says a platform   is only as valuable as its first product, and 
we don't have a product. So you know that was   basically all the feedback we were getting was, 
hey, it is not good enough. The idea is too broad,   and you need to focus. So we went back and we 
talked to everybody we could to try and validate   that we were going to build something that was 
going to be useful. To be honest the reason why   we got things right when we started building the 
product was that we were so scared of getting it   wrong that we spent all our time trying to get 
validation from the end market and the end user   that we were going to build the right thing. 
And I think if we look at you know what   remains today the Datadog culture of that time, I 
think that fear of getting it wrong, that focus on   the end market, that early conversation with the 
user and the customer to make sure that we solve   a real problem and not something that we imagine, 
I think we kept that as a value in the company.   And we kept it ingrained in all of our product 
engineering teams in terms of you know how we   build, how we think about ourselves and the 
product. Yep and definitely still shows.   So especially back then, but even now, 
founding a company like this in New York City,   not the obvious choice. What impact do you think 
that had, and does it remain today or was it just   the initial difficulties? I think it's, in a 
way, it kept us away from the a bit of the echo   chamber you can find in the Bay Area. So when we 
started it was also very hard to raise money in   New York City for an infrastructure company. 
Today it's changed. Today there's many great   infrastructure companies in our state, in New 
York City, started in New York City. You can   scale a company pretty much anywhere in the world. 
That was not so much the case 10 or 15 years ago.   But I would say culturally it reinforced our focus 
on the customer, the end problem, as opposed to   the peers and the rest of the ecosystem. It 
focused us on building and building a business   also that can be sustainable as opposed to raising 
capital. And I think it's a it created the right   conditions for the company to emerge, I think, at 
the time. And we keep a lot of that again today.   I think today you can build a company anywhere, 
really. And we see and work with great companies   you know in New York, in Europe, you know in 
the Bay Area, you know pretty much anywhere.   So when I think of Datadog, if it's the 
product, I think powerful but really,   really usable. But when I think of the 
company, I think humble, which you mentioned,   and enthusiastic. I'm curious when both of 
you think of Datadog, what do you think of? I mean, personally, I think, I mean it's about the 
people, right? So that's the I mean you'll know,   well you can't notice because you're not going 
to shoot the entire office, but we don't have   you know we don't have these posters on the wall 
that says you know do this, do that, be that,   you know because it's not at least 
you know I don't think we think, A,   it's particularly important, B, what's companies 
that put these values in the wall usually it's   they don't necessarily live up to them. And we 
think it's the way we behave that's ultimately   embodies the value of the company it is, or 
you know of us, initially. So we've tried to   I guess lead by example if I were to think about 
the way to characterize it. Like we you know we've   by virtue of founding the company I think we've 
done most of the jobs that you know anybody has.   I've handled HR, accounting, filled the fridge. 
You've probably–I’ve plunged a toilet. Plunged   a toilet. Like I don't do it anymore. But 
the reality is, you know, when it's two,   three, five people, you do what you have to do. 
And there's no notion of, oh, I'm so-and-so,   and so I can't stoop down to that. So I think 
that's been true. And because we did not,   you know, sort of formalize, oh, to be at Datadog 
means you're this, this, and that. That meant that   the only way we could show people those values 
is to behave you know according to them. So we   have to believe in them deeply because that's how 
we're going to behave. And that's what I mean by   leading by example. It's like we want to, at 
least I think what we've been good at, is to   show other people this is what good looks like. 
This is what we think good looks like and this   is what we should shoot for. In general, if you 
zoom out and look at the company and the business,   the way I think about it is I want to build it the 
right way for the long term. Which means it needs   to be a good business. It needs to be a profitable 
business, because you don't last if you're not   a profitable business. It needs to be a business 
that invests in itself and invests into the future   you know, especially in tech. You know if you 
stop investing, if you slow down innovation,   you're typically not long or you're not going to 
be relevant very long. And so we're trying to do a   lot. We don't, typically we don't take shortcuts. 
We don't look for quick wins. We don't look for,   you know, instant gratifications on social 
media. Like that's not our characters at all.   That's why you probably don't see us much 
on the networks. But we really focus on   what it is we can build that is high value, 
and is going to be sustainable, and is going   to get us to be an even more relevant company, you 
know, two years, three years, five years from now.   So, I do want to take this opportunity to thank 
you both. I don't know if you remember this,   Alexis, hard to believe nine years ago during 
my interview, we were talking about Datadog,   and you said, "the best way to proceed in good 
times and in bad is to be honest and trusted   long-term partners to our customers and 
community." And I could tell you meant it.   And it's one of the reasons I joined 
Datadog. And I think it's as true today   as it was then. So thank you for building, 
not just a great product, but a great company.   So along that journey, what's 
been the most surprising?   So some things still matter. Like you know 
everything's moving faster today. I mean we,   sure we'll get to talk about AI at some point 
but, or AI we get to talk about us, but the   building like solving real problems, solving 
valuable problems, being long-term oriented,   being good partners you know to customers, 
these are the things that matter   and that doesn't change. So you know I speak very 
often to you know investors or entrepreneurs,   and everybody's wondering you know what it takes, 
or what changes as you scale and as you need to   reach the next level. And do you need to 
do everything differently? And my answer   is usually that, no it's the same. Like the first 
principles are the same, the basics are the same,   the idea doesn't change. There's more complexity, 
maybe. Maybe you get more velocity or maybe it's   harder to get velocity as you scale. But in 
all cases like the focus remains the same.   Yeah, I think maybe I don't know if it's 
particular in the tech world, but it's easy to   kind of you know focus on the thing you're 
building, the technology, the innovation, and so   on, and kind of forget that you know the business 
is at the heart. You're building something. You're   trying to solve somebody else's problem, and 
in exchange they'll give you money. That's   the basics, right? And that never changes, because 
you know sure the tool, the platform that evolves,   that has to evolve, and it has to move pretty 
fast. But fundamentally somebody who comes to   you as a business, comes to you because they have 
a problem to solve and they think you can solve it   for them. And that continues, that keeps going on, 
because they have you solve a problem for them,   and they come to you with the next problem, 
and then they again, and again, and again,   and again. So I think yeah the history of 
the company has been the repetition of that,   slightly different or sometimes very different. 
But fundamentally that exchange between two people   effectively I think is what you know undergirds 
the whole thing. So that doesn't change.   So that brings us to the present and, as you 
mentioned, we're going to talk about AI. So   curious how both of you are using AI today. Has it 
materially changed your workflows? Mostly, look,   I've been working for more than 20 years without 
AI. And so I have a way of doing everything, you   know I had a way of doing everything, that didn't 
involve you know asking a bot or you know trying   to run an agent, you know? So a lot of it has to 
do with today just trying. Okay, maybe let me try   and have the machine do it for me. How does that 
work? What's happening? What’s this new tool? The   most complex part is trying over and over again 
because things that were not working three months   ago now might be working perfectly. And so, if you 
stick to your training from the past decades, you   internalize that certain approach is working or 
working. Actually that changes very, very fast, so   you need to try again. I think the biggest benefit 
for me today, selfishly, is that I can code again.   Before that, just stating the environment, 
updating everything, you know was taking forever,   and was taking more time than I had available. 
And now with a coding agent you know you can   paper over all the details and have some fun 
again, which I think is pretty cool. Yeah.   Yeah. You know, as for me, I've, for instance, in 
a weird way, I'm starting to use many more text   files, right? So, because that's what–Markdown 
is cool again. No, exactly, right? Because that's   what agents, generally it's easier for them to 
work with that than having the, you know, a bunch   of content that's here and there. And even though 
it's doable, and you can build the code to get all   the contents, they're currently well-versed to do 
some things, so whether it's summarize, expand,   you know, I've tried, for instance, to give it an 
outline and have it, based on what I had written   by hand before you know speaking, expand and 
speak in the same tone, it's really good at   what we call the deep research piece, where 
if you kind of know a particular field enough,   but you want to really build some thorough 
analysis, you know, answer a particular question,   I think it's really good. It can search a lot 
of data much faster than you can and so on. So   I think, for me, it's been a lot of that. But 
I agree with Olivier, experimentation is key.   There's just no, I have no idea what my workflow's 
going to look like you know six months from now.   I'm just desperately trying to see, 
okay, what can work? I would say though,   the one caveat, for me, is I still haven't reached 
AI breakeven. So I still spend more time every day   catching up about AI, learning new stuff, learning 
what changed, you know, since the day before,   than it saves me. But I hope we'll get there at 
some point. Yeah. And I have not had this much   fun coding in years. It's been great. So, as you 
mentioned, you're talking to a lot of founders   right now, which means you're hearing a lot of 
different ways AI is being used and utilized.   Given all of those discussions, 
what are you most excited about?   I mean, everybody's building so much, in so 
many directions. And we can see the explosion   of, I would say, software in general, but you 
know it's going to be services, companies,   all sorts of things you know that are going to be 
built on top of that. So the most exciting to me   is the explosion of creativity that you 
can see everywhere. And you see it on the,   you know, using the models for you know creating 
images and videos, and things like that. The   barrier to creating is getting a lot lower. 
You see it on creating code, you see it on   experimenting with different ideas for businesses. 
You see creativity coming from many different   parts in companies. Like you know now you have 
you know people inside support or sales teams   that are you know if they're really motivated, 
interested in like create pretty elaborate tools   and have and turn their ideas into reality. 
So that's super exciting you know. I think   it has a lot of implications in terms of what 
ecosystem you need to build around that, how you   make all those innovations sustainable, you know, 
what's the new normal for the way people work.   But I think this redefining of everything and this 
explosion of new possibilities is super exciting.   So we've mentioned agent coding a few times. 
Alexis, what impact do you think agentic coding   is going to have on engineering organizations like 
Datadog, but also like our customers? Yeah, I mean   I think what we've seen internally, and externally 
as well, is if you know how to use agents well,   meaning you understand what they're good at, what 
they're not good at, you could, your productivity,   as it were, meaning how fast you can write code 
that runs and that does what you want it to do,   is multiplying by orders of magnitude. And so that 
supports the creativity that Olivier is talking   about, right? And it can range from, okay, I want 
to vibe code a relatively simple internal app,   to fairly complex systems, or very complex 
systems. I think the speed, the ability you have   to experiment, to build prototypes, to validate, 
invalidate ideas, it just didn't exist before. So   it's a I don't think we've even started to fully 
understand the impact it's going to have at least   on the, you know, on the coding side. The analogy 
that I keep coming back to is, which I think   holds true for you know on many fronts, is 
it's like we you know until the 50s people were   controlling computers by writing machine 
language. It was doable, somewhat tedious.   The complexity of the ideas you could express 
was limited by how much you could, you know, how   much space you had in your brain, as it were. And 
then some folks figured out, well, we got to build   tools to express these ideas, but in a language 
that's closer to the way we think. And the   higher level languages were born, compilers 
were born. And we couldn't foresee, really,   I don't think at least they could foresee 
when they built it, what it would,   what it will enable down the road. And I think 
it's not an exact one for one, but I suspect   that the magnitude of the impact is going to 
be similar if not greater. So this feels like   this is only the beginning. And you know, to wit, 
every week somebody comes up with a new way to   an improvement on you know how to use agents, 
build harnesses, skills, et cetera, et cetera.   Something that didn't exist three months 
ago and that truly changes the game. So   we're in a sense, I think, globally the industry 
is catching up to what agents can do in terms of   building software. And behind building 
software is the problem you solve. That's   crazy right now. It's crazy. Yeah. So moving 
on to research a little bit. The work that our   research team is doing on Toto is super, 
super interesting. Can you tell us more?   Yeah, so for those who are not familiar, Toto 
is our sort of first-party time series model,   so a foundational model. And a few things that 
I think set it apart is, one, the corpus of   data it's trained on is vastly superior to what 
has been available you know publicly. And it's,   I think it's the first model, the first step 
we see towards you know Datadog building more   and more of its own foundational models, and 
specifically designed to solve and to answer   questions that have to do with the world of 
software. So we're not talking about a general   purpose something that can you know speak 250 
languages, and analyze medical imagery, and   all that stuff that the frontier labs are doing 
really well. We're talking about something much   more specific to the world of software, the rules 
of the road, the way software is built, and so on.   And so when we marry telemetry and these models, 
our goal is to be able to have very powerful   predictive power, very powerful predictions. And 
so that's, Toto is the first step. We have many   more, we're working on many more. To zoom out a 
bit, Toto was open source. The first version of   it that we released, it's on Hugging Face. It's 
been downloaded millions of times. We trained it   largely on observability data, but it also you 
know when it came out it was state-of-the-art   on any kind of time series and all the time 
series benchmarks you know. So you could use   it for weather forecasting and other things, for 
example. And the reason it's so good, is so part   of it is the power of deep learning, which, I 
think, we've all learned scales extremely well.   But also the incredible dataset we have, you know? 
So we, as a platform, we ingest several billions   of records a second. And we have a really, really 
good idea of which ones of those time series   are high quality, or interesting, or impactful 
because we know which one of these time series   are looked at by our customers, which ones 
are being used to wake people up at night.   And those tend to be high quality. And so we could 
actually train models using really, really high   you know really, really powerful evaluations 
basically for what was valuable or not, you know.   And by the way the open source version of Toto 
is trained purely on our own internal data. So   we don't use any customer data for that. It's only 
data that Datadog submits to Datadog that we can   use for it. We are busy scaling that up right 
now. So we're scaling it up to a lot more data.   We're scaling it up also to include, not just you 
know the metric data, but also logs and traces,   and all of the various other pieces of data 
we gather inside of the platform. And the   end goal here really is to build a, really 
a self-driving system for the infrastructure   you know, so we can have an end-to-end model that 
take telemetry in and output you know what needs   to change in the infrastructure, basically 
to prevent from any issues and auto fix it.   And I think five years ago it was science fiction. 
But you know five years ago we were barely seeing   the first you know self-driving cars and all 
of that. I think today it's pretty clear that   that's achievable and we're hard at work on that. 
And that's what customers want too, right? They   want their system to work. That's ultimately 
the goal. So that's, we think that, yeah,   we can see how to get from here to there. It's 
not going to happen overnight. And the path to   that is building more and more models that 
are really tuned to the world of software.   That's a great segue to our final question, 
which is things are moving very rapidly, so   it's impossible to predict too far out. But let's 
say a year from now, where do you think this goes?   What I'd love to be able to say a year from 
now is we've that sort of self-driving for   software you know we'd be able to demonstrate 
it you know end to end. Not for all the cases,   but we could show that, yes look it is 
actually possible and here's a proof. Yeah,   and the way we frame it is throughout the 
life of the company, you know, we've seen that   the world of software software writing 
and running has become way more productive   and as developers become more productive, 
they create more complexity. By that I mean   people write more than they can understand 
and so, because they do it faster and they   spend less time on it, and so we've seen 
this explosion of complexity over time.   The table stakes for what we've been doing as a 
company has been, okay, we need to keep up with   complexity. So as complexity increases like we 
bring the humans up you know so we're not, we   don't get too far behind, and we can sort of keep 
up with all of the stuff you know we've created.   I think the complexity is going to explode even 
faster and so we better keep up. That's one thing,   but, two, as we were saying with the end-to-end 
models, we finally have a chance to not only   keep up, but maybe also start catching up with the 
complexity a little bit and do a lot more without   involving the humans, so that we can all focus 
on building, you know, instead of waking up in   the middle of the night and fixing things. And so 
I think that's something to look forward to. And   there's quite a bit more that needs to be 
built, but I think we can get there. Yeah.   Amazing. So Olivier, Alexis, thanks again 
for joining. Really appreciate it. Thank you.   And that wraps up another episode of This 
Month in Datadog. We'll see you next month
