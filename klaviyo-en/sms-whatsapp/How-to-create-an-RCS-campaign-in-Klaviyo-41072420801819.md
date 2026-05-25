---
id: "41072420801819"
title: "How to create an RCS campaign in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/41072420801819-How-to-create-an-RCS-campaign-in-Klaviyo"
section: "RCS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:55Z"
language: "en"
---
RCS lets you send rich, interactive messages which can increase engagement and conversions compared with SMS.

In this guide, we’ll show you how to create a ****basic text-only RCS campaign****. If you’d like to add rich features, see our guide to [creating rich RCS messages](https://klaviyo.zendesk.com/hc/en-us/articles/41072788661531).

Once an ****RCS agent is activated in your account****, RCS becomes the ****default message format**** in any country where you have an active agent. This means:

- Messages will always be sent via RCS to RCS-capable devices
- All other recipients will automatically receive the SMS fallback

Even for text-only campaigns, RCS provides advantages over SMS:

- Messages are sent from a ****verified branded sender****, which builds trust and brand recognition
- Delivered over modern data networks, improving deliverability and throughput compared with legacy SMS networks
- You receive ****open receipts****, giving you more visibility into engagement than SMS

Because not all devices and carriers support RCS, every RCS campaign includes an SMS fallback to ensure all recipients still receive your message.

If you want to send only to contacts who can receive RCS, you can [use the RCS capability property to create an RCS segment](https://klaviyo.zendesk.com/hc/en-us/articles/41072989967515).

## ****Step 1: Create an SMS campaign****

1. Go to ****Campaigns**** in your Klaviyo account.
2. Click ****Create Campaign****.
3. Enter a campaign name.
4. Select ****Single channel**** as the campaign type.
5. Under ****Type****, choose ****SMS****.

## ****Step 2: Select your audience****

Choose the lists or segments you want to target. This works the same way as with SMS campaigns.

## ****Step 3: Create your RCS message****

1. In the message editor, select the ****RCS message**** tab.
2. Write your message content.
3. Optionally, [add rich features](https://klaviyo.zendesk.com/hc/en-us/articles/41072788661531).

You’ll see a live preview on the right-hand side of the editor.

## ****Step 4: Review the SMS fallback****

Klaviyo automatically generates an SMS fallback version of your message. Profiles that can’t receive RCS will see this SMS or MMS instead.

The fallback ensures your campaign reaches everyone, even if their device or carrier does not support RCS.

## ****Step 5: Edit the SMS fallback (optional)****

By default, your SMS fallback uses the same content as your RCS message. However, you can toggle to ****edit separately****.

Editing the fallback separately can help reduce costs and improve performance by:

- Removing emojis and special characters (which reduce the SMS character limit from 160 to 70)
- Simplifying the text to fit within one SMS segment
- Removing or replacing media

## ****Step 6: Preview and test****

Before sending, click ****Preview & test**** to see how both the RCS and SMS fallback versions will appear to recipients.

## ****Step 7: Review billing forecast****

On the campaign review page, Klaviyo shows a billing forecast where you can review:

- The total number of credits the campaign will use
- How many recipients will receive RCS vs SMS fallback and the associated credit cost
- A country-by-country breakdown

This helps you understand the cost before sending.

****Note****: RCS pricing varies by region (US vs rest of world). For pricing, please contact our [Sales team](mailto:sales@klaviyo.com).

## ****Step 8: Send or schedule your campaign****

Once you’ve reviewed everything, you can either:

- Send immediately
- Schedule for a later date and time

## ****Key things to remember****

- ****Default format:**** Once an RCS agent is activated in your account, RCS becomes the default message format in any country where you have an active agent. Therefore, text messages will always be sent via RCS to RCS-capable devices, while all other recipients will automatically receive the SMS fallback.
- ****Fallback:**** The SMS fallback ensures all recipients get your message.
- ****Segmentation:**** If you want to send to RCS-only recipients, use [segmentation](https://klaviyo.zendesk.com/hc/en-us/articles/41072989967515).
- ****Pricing:**** Sending long RCS messages or adding rich content will increase the credit cost. Check your billing forecast before sending.