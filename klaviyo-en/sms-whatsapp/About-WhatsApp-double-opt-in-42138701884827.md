---
id: "42138701884827"
title: "About WhatsApp double opt-in"
source_url: "https://help.klaviyo.com/hc/en-us/articles/42138701884827-About-WhatsApp-double-opt-in"
section: "Getting started with WhatsApp"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:50:43Z"
language: "en"
---
Learn about WhatsApp double opt-in, which helps you collect explicit consent from subscribers to receive WhatsApp messages from your business.

This two-step process helps you stay compliant with WhatsApp’s messaging policies and improves message deliverability.

Requires a paid ****Mobile Messaging**** plan.
Double opt-in templates are free to create and use, but you need an active plan to access this feature.

## ****Before you begin****

Before setting up a double opt-in process, confirm that you have an approved WhatsApp sender and message template.

## ****How the double opt-in process works****

The double opt-in process includes two confirmation messages sent to a subscriber when they provide their phone number.

1. ****Double opt-in confirmation message****
   Sent when a subscriber submits their number.
   Example:
   “By replying YES to this message, you agree to receive marketing messages from **[Company]**.”
   This message must be a Meta pre-approved template since it’s initiated by your brand.
2. ****Subscription confirmation message****
   Sent after the subscriber replies with the appropriate keyword (for example, YES, JA, or OUI).
   Example:
   “You have successfully subscribed to WhatsApp updates.”
   This is a free text/service message — no Meta approval is required.

Once the subscription confirmation message is sent, the subscriber is fully opted into your WhatsApp program.

****Understanding WhatsApp templates****

WhatsApp messages fall into two categories based on how they’re triggered and whether Meta approval is required.

|  |  |  |  |
| --- | --- | --- | --- |
| ****Message type**** | ****Triggered by**** | ****Requires Meta approval?**** | ****Example**** |
| Double opt-in confirmation | Brand | ✅ Yes (template) | “By replying YES to this message, you agree to receive marketing and/or informational messages from **[your company name]**.” |
| Subscription confirmation | Subscriber | ❌ No | “You have successfully subscribed to WhatsApp updates.” |

Meta requires pre-approval for brand-initiated messages (templates). Messages triggered by a subscriber reply do not need pre-approval.

## ****Recommended template language****

Klaviyo creates an English transactional message template on your behalf for the double opt-in confirmation message.

Recommended wording:
“By replying YES to this message, you agree to receive marketing and/or informational messages from **[your company name]**.”

You can customize this message, and we recommend following [Meta’s opt-in requirements](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in) and [best practices](https://business.whatsapp.com/policy#best_practices_for_optin) to ensure compliance.

If you want to align more closely with WhatsApp’s best practices, consider expanding your template:
“By replying YES to this message, you agree to receive marketing and/or informational messages from **[your company name]**, including [categories of messages]. Reply STOP to opt out.”

Use a transactional template to avoid per-user marketing message limits imposed by Meta. Learn more in [Meta’s documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits).

## ****Compliance and WhatsApp requirements****

To comply with [WhatsApp’s Business Policy](https://business.whatsapp.com/policy?fbclid=IwY2xjawOv14NicmlkETExVUZtTjZFdWxrS01SZkE1c3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHu-b3HPKCi_fpRdCznvx5iVLTa7mrOoX2-OFbSv-vlPLpKkxONmjx8-pXIUt&brid=N4xsxNLZ1BCerZUxcpDGuw), you must ensure that all subscribers have opted in and provided valid consent.

A business can only contact people who:

- Have provided their mobile phone number.
- Have opted in to receive messages.

  Your opt-in process must:
- Clearly state that the subscriber is enrolling in a WhatsApp messaging program.
- Identify your business name.

## ****WhatsApp best practices****

Follow these best practices to maintain compliance and build trust with subscribers.

- Be transparent about the types of messages subscribers will receive.
- Provide clear instructions for how a subscriber can opt-out (for example, “Reply STOP to opt out”).
- Ensure that your opt-in and opt-out flows are clear and intuitive for users.
  Set clear expectations around message frequency and purpose.

## Learn more about language support

If you manage audiences in multiple regions, [Klaviyo automatically sends compliance and confirmation messages in supported local languages](https://help.klaviyo.com/hc/en-us/articles/42138426687003).