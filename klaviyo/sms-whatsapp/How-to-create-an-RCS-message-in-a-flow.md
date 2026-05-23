---
id: 41072681350555
title: "How to create an RCS message in a flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41072681350555-How-to-create-an-RCS-message-in-a-flow"
section: "RCS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:55Z"
language: en
---

In this guide, we’ll show you how to add a ****basic text-only RCS message**** to a flow. If you’d like to add rich features, see our guide to [creating rich RCS messages/a.](https://klaviyo.zendesk.com/hc/en-us/articles/41072788661531)

Once an ****RCS agent is activated in your account****, RCS becomes the ****default message format**** in any country where you have an active agent. This means:

- Messages will always be sent via RCS to RCS-capable devices
- All other recipients will automatically receive the SMS fallback

  Even for text-only flow messages, RCS offers advantages over SMS:
- Sent from a ****verified branded sender ID (SID)****, which builds trust and brand recognition
- Delivered over ****modern data networks****, improving deliverability and sending speed compared with SMS networks
- Provides ****open receipts****, giving you more visibility into engagement than SMS

Because not all devices and carriers support RCS, every RCS message includes an SMS fallback to ensure all recipients still receive your message.

If you want to send only to contacts who can receive RCS, you can [use the RCS capability property to create an RCS segment](https://klaviyo.zendesk.com/hc/en-us/articles/41072989967515).

## ****How RCS works in flows****

When RCS is enabled in your account, it becomes the ****default format for text messages****. This means:

- Anyone who is RCS-capable will automatically receive flow text messages via RCS instead of SMS.
- Contacts who are not RCS-capable will automatically receive the SMS fallback.

If you want more control over when to send RCS or SMS, you can [use conditional splits in your flows/a.](https://klaviyo.zendesk.com/hc/en-us/articles/41072989967515)

## ****Step 1: Create or edit a flow****

1. Go to ****Flows**** in your Klaviyo account.
2. Either create a new flow or open an existing one.

## ****Step 2: Add an SMS action****

1. In the flow builder, drag the ****SMS action**** into your flow.
2. If you are editing an existing flow, click on the existing SMS action to edit it.

## ****Step 3: Edit the content****

1. Click ****Edit**** on the SMS content.
2. In the message editor, select the ****RCS message**** tab.
3. Enter your message content. You’ll see a live preview on the right-hand side.
4. Optionally, [add rich features/a.](https://klaviyo.zendesk.com/hc/en-us/articles/41072788661531)

## ****Step 4: Review the SMS fallback****

Klaviyo automatically generates an SMS fallback version of your message. Profiles that can’t receive RCS will see this SMS or MMS instead.

The fallback ensures your campaign reaches everyone, even if their device or carrier does not support RCS.

## ****Step 5: Edit the SMS fallback (optional)****

By default, your SMS fallback uses the same content as your RCS message. However, you can toggle to ****edit separately****.

Editing the fallback separately can help reduce costs and improve performance by:

- Removing emojis and special characters (which reduce the SMS character limit from 160 to 70)
- Simplifying the text to fit within one SMS segment
- Removing or replacing media

## ****Step 6: Set the message live****

Unlike campaigns, there is no review page or scheduling step. Once you’ve finished editing:

1. Save your message.
2. Set the message status to ****Active**** so it can send when the flow runs.

## ****Notes for existing flows****

- We’ve automatically ****copied your existing SMS content into the RCS version****, since RCS is now the default message format. This ensures all recipients continue to receive your messages. You can now edit the RCS version to take advantage of rich features.
- Any edits you make to the RCS version will also be copied into the SMS fallback unless you choose to edit the fallback separately.
- ****Contact cards are not supported on RCS.**** Because you cannot save an RCS agent as a contact, these cards are irrelevant in RCS flows. If your flow includes a contact card, make sure to update the RCS version of the message.