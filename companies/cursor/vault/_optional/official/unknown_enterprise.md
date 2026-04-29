---
company: "Anysphere"
research_key: CURSOR
type: official
source: "cursor.com"
title: "enterprise"
url: https://cursor.com/enterprise
date: unknown
fetched_at: 2026-04-20T17:57:30
credibility: S2-S4
evidence: E2-E3
chars: 18936
---

# enterprise

**Source**: https://cursor.com/enterprise
**Channel**: official

---

Coding agents for the full software lifecycle

The choice for ambitious engineering teams.

Talk to the team
→

Trusted by the world's leading enterprises.

Your engineering knowledge base

Architected for complex codebases built by thousands of developers.

Across roles and levels, we're seeing an increase of over 25% in PR volume and over 100% in the average PR size. Together, that means we're shipping about 50% more code.

Anton Andreev Principal Software Engineer, Upwork

This element contains an interactive demo for sighted users. It's a demonstration of Cursor's IDE showing AI-powered coding assistance features. The interface is displayed over a subtle, solid brand background.

Cursor

Get Cursor

In Progress 3

Build Landing Page

Reading docs

Analyze Tab vs Agent Usage Patterns

Fetching data

Plan Mission Control

Generating plan

Ready for Review 3

PyTorch MNIST Experiments

10m

PyTorch MNIST Experiments

Set up Cursor Rules for Dashboard

30m

Set up Cursor Rules for Dashboard

Bioinformatics Tools

45m

+135-21·Bioinformatics Tools

Autonomous Fleet Dispatch

Implement a dispatcher pattern for ride matching with geofence validation, Result-based error handling, and fluent builder API

Agent Composer 2 

Ship better software, faster

Cursor helps your entire team deliver ambitious products.

I've never, as a CTO, received so many texts or Slack messages from employees just saying "Thank you for getting this technology here." 

Melody Hildebrandt CTO, Fox

This element contains an interactive demo for sighted users. It's a demonstration of Cursor's IDE showing AI-powered coding assistance features. The interface is displayed over a subtle, solid brand background.

Cursor

acme-labs

src
domain
ride.rs
geo
mod.rs
dispatch
mod.rs
builder.rs
repository
mod.rs
service
matching.rs
tests
dispatch_tests.rs
Cargo.toml

builder.rs

dispatch_tests.rs

mod.rs

use chrono::{Duration, Utc};

use uuid::Uuid;

use super::{DispatchError, DispatchResult, MatchingStrategy, RideDispatcher};

use crate::domain::{PricingTier, RideRequest, RideStatus};

use crate::geo::{Coordinate, Waypoint};

use crate::service_area::ServiceArea;

use crate::vehicle::VehicleRequirements;

impl<S: MatchingStrategy> RideDispatcher<S> {

 pub fn for_rider(mut self, rider_id: Uuid) -> Self {

 self.rider_id = Some(rider_id);

 self

 }

}

impl<S: MatchingStrategy> RideDispatcher<S> {

 pub fn add_waypoint(mut self, waypoint: Waypoint) -> Self {

 // TODO: validate waypoint distance

 self.waypoints.push(waypoint);

 self

 }

}

impl<S: MatchingStrategy> RideDispatcher<S> {

 pub async fn dispatch(self) -> DispatchResult<RideRequest> {

 todo!("implement dispatch")

 }

}

Loved by developers

In head-to-head evaluations, 93% of engineers select Cursor as their preferred AI coding tool.

What used to be a weeks-long ramp-up, navigating complex repos and scheduling handoffs across global teams, is now a structured process built around Cursor from day one.

Roni Avidov Senior R&D Team Lead, Monday

Interactive demo showing cursor.com/dashboard. The interface is displayed over a subtle, solid brand background.

cursor.com/dashboard

Get Cursor

Agent Requests

426,891+23%

Tabs

61,204

Chats

10,482

Users

122

User

Model

Tabs

Requests

Diffs

Agent Lines

1Massimo

Composer 2

12,482

8,241

6,847

142,891

2Tadao Ando

GPT-5.2 High Fast

11,847

7,623

5,912

128,445

3Sarah Chen

Opus-4.6

10,294

6,918

5,403

115,672

4Erik Lindqvist

Gemini 3 Pro

9,761

6,442

4,821

98,234

5Priya Sharma

Composer 2

8,943

5,817

4,256

87,109

AI is changing how software is built.

64%

Fortune 500 companies using Cursor.

50,000+

Enterprises choose to build with Cursor.

100M+

Lines of enterprise code written per day with Cursor.

Powerful, yet customizable

Standardize your engineering team on the same tools and best practices.

Contact sales
→

Total control

Globally configure model access, MCP controls, and system-level agent rules.

View enterprise controls ↗

Access the best models

Choose between frontier models from OpenAI, Anthropic, Gemini, and xAI.

View available models ↗

AutoSuggestedComposer 2Codex 5.3High FastSonnet 4.5Opus 4.6Gemini 3 ProGrok Code

Ship with confidence

When enabled, Bugbot automatically runs in the background on new PRs.

Learn more about Bugbot ↗

swhitmore7 minutes ago

lgtm!

swhitmorecommitted

Some checks pending

3 in progress

Cursor / Policy Check

Cursor / Security Scan

Cursor Bugbot

Merge pull request

Trusted by companies worldwide

Built with security and compliance at the core.

Dedicated guidance

Deploy AI at scale with professional expertise.

Premium support

Tailored support for teams with specialized needs.

Zero data retention

No training on your data by Cursor or LLM providers.

Identity management

SAML-based SSO integration for secure user access.

SCIM user provisioning

Easily create, update, and remove users and groups.

Centralized security controls

Configure model access, MCPs, and agent rules.

Global compliance standards

Compliant with the requirements of GDPR and CCPA.

Third-party security certifications

SOC 2 Type 2 certified and annual penetration testing.

Robust data protection

AES-256 encryption at rest and TLS 1.2+ in transit.

Visit our Trust Center
↗
Read about our security
→

Modern engineering teams are powered by Cursor.

Cursor quickly grew from hundreds to thousands of extremely enthusiastic Stripe employees. We spend more on R&D and software creation than any other undertaking, and there's significant economic outcomes when making that process more efficient and productive.

Patrick Collison Co‑Founder & CEO, Stripe

My favorite enterprise AI service is Cursor. Every one of our engineers, some 40,000, are now assisted by AI and our productivity has gone up incredibly.

Jensen Huang President & CEO, NVIDIA

By February 2025, every Coinbase engineer had utilized Cursor, which has become the preferred IDE for most of our developers. Single engineers are now refactoring, upgrading, or building new codebases in days instead of months.

Brian Armstrong CEO, Coinbase

Cursor has transformed the way our engineering teams write and ship code, with adoption growing from 150 to over 500 engineers (~60% of our org!) in just a few weeks.

Albert Strasheim CTO, Rippling

JetBrains has always seen its mission as bringing the best of the industry to our users. I'm very excited about Cursor becoming a special guest in the family of ACP-compliant agents in JetBrains IDEs. This collaboration looks like a win for Cursor, for JetBrains, and most importantly for developers.

Aleksey Stukalov Head of IDEs Division, JetBrains

Watching a dozen agent branches merge every day has become normal, and that freed-up velocity shows up everywhere from release cadence to bug-backlog burn-down. Cursor isn't a convenience add-on; it's a scale-multiplier for the whole org.

Cody De Arkland Senior Director, Sentry

Bring Cursor to your team
→

Customer stories

Amplitude ships 3x more production code with Cursor

Apr 15, 2026

PlanetScale protects production reliability with Bugbot

Mar 2, 2026

Box chooses Cursor for enterprise-grade quality, security, and control

Feb 13, 2026

NVIDIA commits 3x more code across 30,000 developers with Cursor

Feb 6, 2026

View all stories →

Questions & Answers

How do usage limits work for enterprises?↓↑

Enterprise plans are priced per seat with an included usage allotment. Organizations can pre-commit additional usage for high-volume teams, while administrators maintain full cost control through configurable limits at both the team and individual user level.

How does Cursor handle large-scale codebases and monorepos?↓↑

Cursor is architected for enterprise scale, efficiently indexing and navigating codebases with millions of lines across hundreds of thousands of files. Our codebase intelligence learns your team's patterns, conventions, and architecture, ensuring AI suggestions match your coding standards and understand your system's unique context.

How does Cursor use my data?↓↑

With Privacy Mode enabled org-wide, your code is never used for training. Cursor also maintains zero data retention agreements with all our model providers.

What security certifications does Cursor have?↓↑

Cursor is SOC 2 Type II certified, with regular penetration testing. Reports are available in our Trust Center.

Does Cursor support SSO and SCIM?↓↑

Yes, we support major IdPs (Okta, Azure AD, Google Workspace, and more). Admins can enforce SSO, disable local login, and provision/deprovision users with SCIM.

Does Cursor support on-premises or VPC deployment?↓↑

Cursor currently operates on SOC 2 Type II compliant AWS infrastructure. While we don't offer on-premises deployment today, our cloud architecture delivers enterprise-grade security controls, data isolation, and performance.

What admin controls are available?↓↑

Enterprise admins can set role permissions, whitelist or blocklist repos, models, and MCP servers, and configure global agent run settings.

How can I track AI adoption across my organization?↓↑

Enterprise administrators have access to comprehensive analytics dashboards showing adoption rates, usage patterns by team and individual, AI-assisted code metrics, and productivity insights. Data can be exported through our API for integration with your existing analytics platforms.

Get started with Cursor Enterprise.

Contact sales
→

Coding agents for the full software lifecycle

The choice for ambitious engineering teams.

Talk to the team
→

Trusted by the world's leading enterprises.

Your engineering knowledge base

Architected for complex codebases built by thousands of developers.

Across roles and levels, we're seeing an increase of over 25% in PR volume and over 100% in the average PR size. Together, that means we're shipping about 50% more code.

Anton Andreev Principal Software Engineer, Upwork

This element contains an interactive demo for sighted users. It's a demonstration of Cursor's IDE showing AI-powered coding assistance features. The interface is displayed over a subtle, solid brand background.

Cursor

Get Cursor

In Progress 3

Build Landing Page

Reading docs

Analyze Tab vs Agent Usage Patterns

Fetching data

Plan Mission Control

Generating plan

Ready for Review 3

PyTorch MNIST Experiments

10m

PyTorch MNIST Experiments

Set up Cursor Rules for Dashboard

30m

Set up Cursor Rules for Dashboard

Bioinformatics Tools

45m

+135-21·Bioinformatics Tools

Autonomous Fleet Dispatch

Implement a dispatcher pattern for ride matching with geofence validation, Result-based error handling, and fluent builder API

Agent Composer 2 

Ship better software, faster

Cursor helps your entire team deliver ambitious products.

I've never, as a CTO, received so many texts or Slack messages from employees just saying "Thank you for getting this technology here." 

Melody Hildebrandt CTO, Fox

This element contains an interactive demo for sighted users. It's a demonstration of Cursor's IDE showing AI-powered coding assistance features. The interface is displayed over a subtle, solid brand background.

Cursor

acme-labs

src
domain
ride.rs
geo
mod.rs
dispatch
mod.rs
builder.rs
repository
mod.rs
service
matching.rs
tests
dispatch_tests.rs
Cargo.toml

builder.rs

dispatch_tests.rs

mod.rs

use chrono::{Duration, Utc};

use uuid::Uuid;

use super::{DispatchError, DispatchResult, MatchingStrategy, RideDispatcher};

use crate::domain::{PricingTier, RideRequest, RideStatus};

use crate::geo::{Coordinate, Waypoint};

use crate::service_area::ServiceArea;

use crate::vehicle::VehicleRequirements;

impl<S: MatchingStrategy> RideDispatcher<S> {

 pub fn for_rider(mut self, rider_id: Uuid) -> Self {

 self.rider_id = Some(rider_id);

 self

 }

}

impl<S: MatchingStrategy> RideDispatcher<S> {

 pub fn add_waypoint(mut self, waypoint: Waypoint) -> Self {

 // TODO: validate waypoint distance

 self.waypoints.push(waypoint);

 self

 }

}

impl<S: MatchingStrategy> RideDispatcher<S> {

 pub async fn dispatch(self) -> DispatchResult<RideRequest> {

 todo!("implement dispatch")

 }

}

Loved by developers

In head-to-head evaluations, 93% of engineers select Cursor as their preferred AI coding tool.

What used to be a weeks-long ramp-up, navigating complex repos and scheduling handoffs across global teams, is now a structured process built around Cursor from day one.

Roni Avidov Senior R&D Team Lead, Monday

Interactive demo showing cursor.com/dashboard. The interface is displayed over a subtle, solid brand background.

cursor.com/dashboard

Get Cursor

Agent Requests

426,891+23%

Tabs

61,204

Chats

10,482

Users

122

User

Model

Tabs

Requests

Diffs

Agent Lines

1Massimo

Composer 2

12,482

8,241

6,847

142,891

2Tadao Ando

GPT-5.2 High Fast

11,847

7,623

5,912

128,445

3Sarah Chen

Opus-4.6

10,294

6,918

5,403

115,672

4Erik Lindqvist

Gemini 3 Pro

9,761

6,442

4,821

98,234

5Priya Sharma

Composer 2

8,943

5,817

4,256

87,109

AI is changing how software is built.

64%

Fortune 500 companies using Cursor.

50,000+

Enterprises choose to build with Cursor.

100M+

Lines of enterprise code written per day with Cursor.

Powerful, yet customizable

Standardize your engineering team on the same tools and best practices.

Contact sales
→

Total control

Globally configure model access, MCP controls, and system-level agent rules.

View enterprise controls ↗

Access the best models

Choose between frontier models from OpenAI, Anthropic, Gemini, and xAI.

View available models ↗

AutoSuggestedComposer 2Codex 5.3High FastSonnet 4.5Opus 4.6Gemini 3 ProGrok Code

Ship with confidence

When enabled, Bugbot automatically runs in the background on new PRs.

Learn more about Bugbot ↗

swhitmore7 minutes ago

lgtm!

swhitmorecommitted

Some checks pending

3 in progress

Cursor / Policy Check

Cursor / Security Scan

Cursor Bugbot

Merge pull request

Trusted by companies worldwide

Built with security and compliance at the core.

Dedicated guidance

Deploy AI at scale with professional expertise.

Premium support

Tailored support for teams with specialized needs.

Zero data retention

No training on your data by Cursor or LLM providers.

Identity management

SAML-based SSO integration for secure user access.

SCIM user provisioning

Easily create, update, and remove users and groups.

Centralized security controls

Configure model access, MCPs, and agent rules.

Global compliance standards

Compliant with the requirements of GDPR and CCPA.

Third-party security certifications

SOC 2 Type 2 certified and annual penetration testing.

Robust data protection

AES-256 encryption at rest and TLS 1.2+ in transit.

Visit our Trust Center
↗
Read about our security
→

Modern engineering teams are powered by Cursor.

Cursor quickly grew from hundreds to thousands of extremely enthusiastic Stripe employees. We spend more on R&D and software creation than any other undertaking, and there's significant economic outcomes when making that process more efficient and productive.

Patrick Collison Co‑Founder & CEO, Stripe

My favorite enterprise AI service is Cursor. Every one of our engineers, some 40,000, are now assisted by AI and our productivity has gone up incredibly.

Jensen Huang President & CEO, NVIDIA

By February 2025, every Coinbase engineer had utilized Cursor, which has become the preferred IDE for most of our developers. Single engineers are now refactoring, upgrading, or building new codebases in days instead of months.

Brian Armstrong CEO, Coinbase

Cursor has transformed the way our engineering teams write and ship code, with adoption growing from 150 to over 500 engineers (~60% of our org!) in just a few weeks.

Albert Strasheim CTO, Rippling

JetBrains has always seen its mission as bringing the best of the industry to our users. I'm very excited about Cursor becoming a special guest in the family of ACP-compliant agents in JetBrains IDEs. This collaboration looks like a win for Cursor, for JetBrains, and most importantly for developers.

Aleksey Stukalov Head of IDEs Division, JetBrains

Watching a dozen agent branches merge every day has become normal, and that freed-up velocity shows up everywhere from release cadence to bug-backlog burn-down. Cursor isn't a convenience add-on; it's a scale-multiplier for the whole org.

Cody De Arkland Senior Director, Sentry

Bring Cursor to your team
→

Customer stories

Amplitude ships 3x more production code with Cursor

Apr 15, 2026

PlanetScale protects production reliability with Bugbot

Mar 2, 2026

Box chooses Cursor for enterprise-grade quality, security, and control

Feb 13, 2026

NVIDIA commits 3x more code across 30,000 developers with Cursor

Feb 6, 2026

View all stories →

Questions & Answers

How do usage limits work for enterprises?↓↑

Enterprise plans are priced per seat with an included usage allotment. Organizations can pre-commit additional usage for high-volume teams, while administrators maintain full cost control through configurable limits at both the team and individual user level.

How does Cursor handle large-scale codebases and monorepos?↓↑

Cursor is architected for enterprise scale, efficiently indexing and navigating codebases with millions of lines across hundreds of thousands of files. Our codebase intelligence learns your team's patterns, conventions, and architecture, ensuring AI suggestions match your coding standards and understand your system's unique context.

How does Cursor use my data?↓↑

With Privacy Mode enabled org-wide, your code is never used for training. Cursor also maintains zero data retention agreements with all our model providers.

What security certifications does Cursor have?↓↑

Cursor is SOC 2 Type II certified, with regular penetration testing. Reports are available in our Trust Center.

Does Cursor support SSO and SCIM?↓↑

Yes, we support major IdPs (Okta, Azure AD, Google Workspace, and more). Admins can enforce SSO, disable local login, and provision/deprovision users with SCIM.

Does Cursor support on-premises or VPC deployment?↓↑

Cursor currently operates on SOC 2 Type II compliant AWS infrastructure. While we don't offer on-premises deployment today, our cloud architecture delivers enterprise-grade security controls, data isolation, and performance.

What admin controls are available?↓↑

Enterprise admins can set role permissions, whitelist or blocklist repos, models, and MCP servers, and configure global agent run settings.

How can I track AI adoption across my organization?↓↑

Enterprise administrators have access to comprehensive analytics dashboards showing adoption rates, usage patterns by team and individual, AI-assisted code metrics, and productivity insights. Data can be exported through our API for integration with your existing analytics platforms.

Get started with Cursor Enterprise.

Contact sales
→
