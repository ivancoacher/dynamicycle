---
id: "45769973148571"
title: "Understanding Skills"
source_url: "https://help.klaviyo.com/hc/en-us/articles/45769973148571-Understanding-Skills"
section: "Customer Agent"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-29T20:10:56Z"
language: "en"
---
## You will learn

What skills are, which ones Customer Agent comes with out of the box, what each one does, and what prerequisites unlock which skills. By the end, you’ll know which skills are running for your brand and which integrations you’d need to add to enable more.

## What skills are

A ****skill**** is a scoped capability that lets Customer Agent handle a specific type of shopper request — like tracking an order, processing a return, or recommending a product. Customer Agent comes with skills out of the box; you don’t write or configure them.

Skills are ****automatically active when their prerequisites are met****. For example, the Order tracking skill turns on as soon as your Shopify store is connected. You can disable any skill if you don’t want Customer Agent to handle that type of request.

Creating fully custom skills from scratch is currently in closed beta. Editing existing skills (changing instructions, swapping tools) is coming soon.

## How a skill handles a request

When a shopper sends a message, Customer Agent runs through a few steps:

1. ****Receives the message**** from the shopper across web chat, SMS, email, or WhatsApp.
2. ****Adds context**** — pulls in the shopper’s profile, brand summary, and any active Guidance.
3. ****Routes**** — picks the best skill for the request based on what the shopper is asking.
4. ****Responds**** — the chosen skill uses its tools, content, and instructions to generate a response.
5. ****Hands off if needed**** — escalates to a human if the request matches an escalation rule or the skill can’t resolve it.

## The skills Customer Agent comes with

Customer Agent ships with 8 skills today.

|  |  |  |  |
| --- | --- | --- | --- |
| ****Procedure**** | ****What it does**** | ****Prerequisites**** | ****Example shopper question**** |
| Product Recommendations | Suggests products based on shopper preferences and browsing context. | Shopify | "What do you recommend for sensitive skin?" |
| Order tracking | Looks up order status, shipping info, and tracking links. | Shopify | "Where is my order?" |
| General Q&A | Answers brand and product questions using your indexed content. | None | "What's your return policy?" |
| Coupon & discount retrieval | Retrieves existing discount codes the shopper is eligible for. Does not generate new codes. | Shopify, Coupons configured in Content | "Do I have any active discounts?" |
| Returns & exchanges | Initiates returns and exchanges through your returns provider. | Loop or Aftership | "I want to return this jacket." |
| Order editing | Updates shipping addresses, swaps items, and changes quantities on existing orders. | Shopify with order-edit permissions | "Can I change the address on my order?" |
| Subscription editing | Pauses, resumes, skips, and updates subscriptions. | Recharge or Skio (Skio: active subscriptions only) | "Skip my next delivery." |
| Loyalty | Looks up loyalty point balances, redemptions, and rewards. | Yotpo or Smile.io | "How many points do I have?" |

## Prerequisites

Each skill needs specific data or integrations to work. Customer Agent automatically activates a skill once its prerequisites are met.

- ****Shopify connection**** — Unlocks Product Recommendations, Order tracking, and Coupon & discount retrieval.
- ****Order editing requires Shopify**** with order-edit permissions enabled.
- ****Returns & exchanges requires a returns provider**** — Loop or Aftership.
- ****Subscription editing requires a subscriptions provider**** — Recharge (full data visibility) or Skio (active subscriptions only).
- ****Loyalty requires a loyalty provider**** — Yotpo or [Smile.io](http://Smile.io).

A skill won’t activate if its prerequisites aren’t met. To turn on a skill that isn’t currently active, connect the required integration.

### How shoppers interact across channels

Different channels render skill responses differently:

- ****Web chat**** — Rich product cards, order cards, inline buttons (e.g., “Track shipment,” “Edit order”).
- ****SMS & WhatsApp**** — Deep links to product pages, tracking pages, and the customer hub.
- ****Email**** — Plain text plus links; no interactive components.

The same skill logic runs across channels — only the response formatting differs.

## Skill-specific notes

A few skills have behavior worth knowing about:

- ****Coupon & discount retrieval**** retrieves existing codes from your Coupons content; it does not generate new codes.
- ****Subscription editing**** with Skio shows active subscriptions only — paused or canceled subscriptions aren’t available to the skill.
- ****Order editing**** lets shoppers update shipping addresses, swap items, or change quantities directly in web chat (subject to Shopify’s edit window).

## Customizing skills

Customer Agent comes with skills out of the box. You can disable any skill you don’t want active from the Skills page. Creating fully custom skills from scratch is currently in closed beta, and editing existing skills is coming soon.

If you need different behavior than what an existing skill provides today, you have a few paths:

- ****Disable the skill**** if you don’t want Customer Agent to handle that type of request at all
- ****Build a fully custom skill**** (beta) for new workflows or specialized handling
- ****Use Guidance**** for global behavior changes — tone, communication style, escalation triggers

## Next steps

- ****Create a skill**** if you need behavior the skills Customer Agent comes with don’t cover
- ****Set up Guidance**** to control how all skills behave
- ****Add content**** so skills like General Q&A have material to draw from
- ****Monitor performance**** on the Performance dashboard