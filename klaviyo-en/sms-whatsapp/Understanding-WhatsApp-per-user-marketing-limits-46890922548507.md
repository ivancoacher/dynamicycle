---
id: "46890922548507"
title: "Understanding WhatsApp per-user marketing limits"
source_url: "https://help.klaviyo.com/hc/en-us/articles/46890922548507-Understanding-WhatsApp-per-user-marketing-limits"
section: "Understand WhatsApp with Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:51:10Z"
language: "en"
---
Understand how Meta applies marketing limits at the individual user level and why some WhatsApp marketing templates may fail.

Meta enforces per-user marketing limits on WhatsApp to protect the user experience. These limits apply to each recipient individually, not to your account as a whole. As a result, a marketing template will fail even if you have not recently messaged that user.

This article explains how per-user limits work, which messages are affected, and how to identify impacted profiles in Klaviyo.

## What are WhatsApp per-user limits?

Meta evaluates marketing message eligibility at the ****user level****, not the business level.

If a user:

- Has recently received marketing template messages, and
- Has not replied or meaningfully engaged,

Meta may block additional marketing templates to that user.

These limits apply across all businesses on WhatsApp, not just your brand. If multiple businesses send marketing messages to the same person, Meta considers that total exposure when deciding whether to allow another marketing template.

Meta uses engagement signals and recent marketing exposure to determine whether another marketing template can be delivered.

## Which WhatsApp messages are affected?

Not all WhatsApp message types are subject to per-user marketing limits.

| Message type | Subject to per-user limits? |
| --- | --- |
| ****Marketing templates**** | Yes. May be blocked if the user recently received marketing messages and has not engaged. |
| ****Utility templates**** | No. Includes order updates, shipping confirmations, appointment reminders, and other service notifications. |
| ****Free-form messages (within 24-hour session)**** | No. You can send free-form messages within 24 hours after a user replies. |

In Klaviyo, marketing templates are the only WhatsApp message type affected by these engagement-based limits.

## How enforcement works

Meta evaluates marketing template eligibility at send time.

A marketing template may fail if:

- The user has recently received marketing templates that day
- The user did not reply or interact
- Engagement signals are low

Because enforcement happens at the user level across all businesses, your message may be blocked even if you have not messaged that user earlier in the day.

When this occurs, the message fails delivery.

## Error code 131049: Maintain healthy ecosystem engagement

If a marketing template is blocked due to Meta’s engagement protections, you may see this error:

****Error code 131049 – Maintain healthy ecosystem engagement****

## Marketing messages to US phone numbers

As of April 1, 2025, Meta blocks delivery of all WhatsApp marketing template messages to recipients with a United States phone number.

This applies to any WhatsApp user whose phone number:

- Uses the +1 country dialing code, and
- Has a United States area code.

Starting on this date, attempting to send a marketing template to a US phone number results in a delivery failure.

Meta has stated that this pause is temporary and is intended to improve the consumer experience in the United States. During this period, marketing templates cannot be delivered to US WhatsApp users.

This restriction is enforced by Meta and cannot be overridden within Klaviyo. [Learn more](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits).

## How to identify impacted profiles

You can create a segment of profiles who have received this error to understand how often marketing templates are blocked.

Build a segment based on the relevant WhatsApp failure event and error code:

- Error code equals ****131049****

  Segmenting by this error allows you to:
- Monitor how frequently marketing templates are blocked
- Suppress affected profiles from immediate follow-up campaigns
- Refine targeting toward more recently engaged users

We recommend using [this error segment](https://help.klaviyo.com/hc/en-us/articles/42141066963355) to exclude in campaigns.

## Best practices

While you cannot override Meta’s per-user limits, you can reduce the likelihood of blocked marketing sends by focusing on engagement.

- Target users who have recently engaged on WhatsApp
- Encourage replies to open a 24-hour session window
- Avoid sending multiple promotional campaigns to the same audience in a short timeframe

Strong engagement improves deliverability over time. Repeated unengaged marketing messages increase the likelihood of future blocks.