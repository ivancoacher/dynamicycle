---
id: 44813293727131
title: "Customer Agent event data reference"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/44813293727131-Customer-Agent-event-data-reference"
section: "Customer Agent"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-29T21:11:23Z"
language: en
---

## You will learn

What events Customer Agent emits to your Klaviyo account, what data each event carries, and how to use those events to build segments and flows.

## How Customer Agent events work

Events fire automatically — there’s no configuration needed. Every Customer Agent conversation emits events that show up alongside your other Klaviyo profile activity. You can use them to build segments, trigger flows, and reference in reports.

To verify events are firing for a profile, navigate to ****Analytics > Metrics****, find the Customer Agent metric, or open a profile’s ****Activity Feed**** to see events on a specific shopper.

## Events

|  |  |  |
| --- | --- | --- |
| ****Event**** | ****Fires when**** | ****Key properties**** |
| Started Conversation | A shopper opens a new Customer Agent conversation | Conversation ID, Channel, First message, Profile |
| Conversation Resolved | Customer Agent fully resolves a conversation without escalation | Conversation ID, Channel, Skill, Tags, Resolution time, Profile |
| Conversation Escalated | A conversation hands off to a human | Conversation ID, Channel, Escalation reason, Skill, Tags, Profile |
| Received Product Recommendation | Customer Agent surfaces product recommendations | Conversation ID, Channel, Product IDs / SKUs, Profile |

### Started Conversation

Fires when a shopper opens a new Customer Agent conversation.

****Properties:****

- Conversation ID
- Channel (web chat, email, SMS, WhatsApp)
- First message
- Profile (if linked)

### Conversation Resolved

Fires when Customer Agent fully resolves a conversation without escalation.

****Properties:****

- Conversation ID
- Channel
- Skill that handled the conversation
- Tags
- Resolution time
- Profile

### Conversation Escalated

Fires when a conversation hands off to a human — either via an escalation rule or a shopper request.

****Properties:****

- Conversation ID
- Channel
- Escalation reason (rule name, shopper-requested, etc.)
- Skill that was active at escalation
- Tags
- Profile

### Received Product Recommendation

Fires when Customer Agent surfaces product recommendations to a shopper.

****Properties:****

- Conversation ID
- Channel
- Product IDs / SKUs recommended
- Profile

## Example segments

Three common ways to use these events:

### Re-engage shoppers who got a product recommendation

> Profile has at least 1 **Received Product Recommendation** in the last 14 days ****AND**** has not placed an order since

Use this to trigger a follow-up flow with a soft nudge or discount.

### Exclude recently escalated shoppers from automated outreach

> Profile has at least 1 **Conversation Escalated** in the last 7 days

Add this as an exclusion to your campaign or flow targeting to avoid contacting shoppers who are already in an open service conversation.

### Identify high-value resolved conversations

> Profile has at least 1 **Conversation Resolved** in the last 30 days ****AND**** has placed an order in the last 30 days

Use this to measure post-conversation conversion or as a positive signal for VIP segmentation.

## Next steps

- ****Build segments**** in Klaviyo using these events — see [Segmentation in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115003078711)
- ****Trigger flows**** off Customer Agent events for follow-up campaigns
- ****Review the dashboard**** for aggregate trends — see **Understanding the performance dashboard**