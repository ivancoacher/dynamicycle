---
id: 37659376435483
title: "Understanding the performance dashboard"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/37659376435483-Understanding-the-performance-dashboard"
section: "Customer Agent"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-29T20:10:55Z"
language: en
---

## You will learn

What each metric on the Customer Agent performance dashboard means, how to filter the data, and how to use it to find opportunities to improve Customer Agent’s behavior.

## Before you begin

You’ll need:

- An ****Owner****, ****Admin****, ****Manager****, or ****Analyst**** role
- Customer Agent live on at least one channel — there’s nothing to measure until you’ve launched

## Where to find it

Navigate to ****Customer Agent > Performance****, or open it directly at [klaviyo.com/kagent/performance](https://www.klaviyo.com/kagent/performance).

## Top-level metrics

The dashboard shows six headline metrics:

- ****Total resolved by AI**** — Count of conversations Customer Agent fully resolved (no escalation, no human intervention).
- ****% resolved by AI**** — Percentage of total conversations resolved without escalation.
- ****AI-generated sales**** — Revenue from orders attributed to Customer Agent. Web chat attribution uses a 24-hour window. SMS attribution follows your Klaviyo SMS attribution settings (KAV).
- ****Add to carts**** — ATC events generated from Customer Agent conversations.
- ****Link clicks**** — Clicks on links Customer Agent shared in responses.
- ****Avg order value**** — Average order value of AI-generated sales.

  These metrics fall into two lenses:
- ****Resolution metrics**** (Total resolved, % resolved) — Tells you if Customer Agent is doing the job.
- ****Revenue metrics**** (AI-generated sales, ATC, Link clicks, AOV) — Tells you if Customer Agent is driving commerce alongside service.

Most brands optimize for both.

## Filters

Use filters to scope the data:

- ****Date range**** — Pick a window (last 7 days, 30 days, custom). Date ranges are inclusive on both ends.
- ****Channel**** — Filter by web chat, email, SMS, or WhatsApp.

All metrics on the dashboard reflect your account’s timezone, set in account settings.

## Skills performance

The Skills Performance section breaks down conversation volume and resolution rate per skill — both skills Customer Agent comes with and any custom skills you’ve created. Use this to spot:

- Skills handling high volume but low resolution (likely needs better content or instructions)
- Skills rarely getting picked (likely the “When to use this skill” content needs sharpening)
- Skills that are firing on the wrong types of requests (visible when resolution rate is low and shoppers escalate often)

## Conversations table

Below the metrics, the Conversations table lists every conversation Customer Agent has handled. Columns:

- ****First Question**** — The shopper’s opening message
- ****Profile**** — Klaviyo profile, if linked
- ****Channel**** — Web chat, email, SMS, or WhatsApp
- ****Status**** — Conversation outcome (see below)
- ****Tags**** — Any tags applied (e.g., skill that handled it, escalation rule that fired)
- ****Messages**** — Total message count
- ****Last updated**** — When the conversation last had activity

### Conversation status

Status reflects how the conversation ended (or where it is):

- ****Resolved**** — Customer Agent fully resolved without escalation
- ****Routed**** — Escalated to a human (via escalation rule or shopper request)
- ****Closed**** — Conversation ended without resolution (shopper left, timed out)
- ****Open**** — Still in progress

## Acting on the data

A few common patterns and how to investigate:

- ****Low % resolved**** — Likely a content gap or a skill that’s underperforming. Filter the Conversations table by escalated status, look at common first questions, and patch with content or skill adjustments.
- ****Low AI-generated sales**** — Shopping skills (Product Recommendations, General Q&A) may not be active or surfacing well. Confirm they’re enabled and that your product catalog is connected.
- ****Low link clicks**** — Customer Agent isn’t surfacing PDP or help links in responses. Check that your content includes URLs where relevant; review communication style rules to make sure responses aren’t suppressing links.
- ****High volume on a single skill with low resolution**** — Drill into that skill’s conversations, identify common failure modes, fix at the source (content, “How to respond” content for custom skills, or adjust the skill’s tools).

## Next steps

- ****Test in the test sidebar**** to validate fixes before they reach more shoppers
- ****Iterate on Guidance and content**** based on patterns you see
- ****Review the event data reference**** to build segments from conversation data — see **Customer Agent event data reference**