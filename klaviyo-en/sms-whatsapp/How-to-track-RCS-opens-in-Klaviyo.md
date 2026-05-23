---
id: 41073297828379
title: "How to track RCS opens in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41073297828379-How-to-track-RCS-opens-in-Klaviyo"
section: "RCS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: en
---

RCS (Rich Communication Services) campaigns and flows now support tracking when a recipient opens your message. This helps you better understand engagement and target audiences more effectively.

It’s important to note that ****opens are only available for RCS messages****. SMS and MMS do not support open tracking.

Klaviyo reports opens in two ways:

1. ****Open rates**** – shown in campaign and flow reports as an aggregated percentage.
2. ****Opened Text event**** – a profile-level event that can be used in segmentation, conditional splits, and is visible in the activity feed.

## ****Where to find RCS opens****

### 1. Report overview

In the ****Deliverability**** table of a campaign or flow report overview, open rates are shown alongside delivery rate, failed deliveries, and unsubscribe rate (see below).

![](https://klaviyo.zendesk.com/hc/article_attachments/41073297798555)

### ****2. Recipient activity tab****

****I****n the recipient activity tab of a campaign or flow report you can see which profiles opened your RCS message (see below).

![](https://klaviyo.zendesk.com/hc/article_attachments/41073326083227)

### ****3. Profile activity feed****

Opens also appear directly on a profile’s timeline so you can understand how each individual is engaging with your RCS campaigns.

![](https://klaviyo.zendesk.com/hc/article_attachments/41073297804315)

## ****How RCS open events work****

- When a recipient opens an RCS message, an ****Opened Text event**** is logged on their profile timeline.
- Klaviyo records an ****Opened Text event**** only once per message, the first time it is opened.
  - ****Note****: In some cases, a device may send a duplicate open event. If you see two open events recorded at the same time, they represent the same open, not multiple opens.
- The timestamp shown reflects the exact moment the device reports the open.
- If multiple RCS messages remain unread in a thread, the next time the recipient opens the conversation we will receive one open event covering all of those messages. For attribution, this open will be applied only to the most recent message.

## ****Using the Opened Text event****

The Opened Text event can be used for segmentation, flows, and attribution.

## ****Segmentation****

Build segments of subscribers based on whether they have opened an RCS message. For example:

- Create a segment of people who ****have not opened**** an RCS message in the last 30 days and re-engage them with a different channel.
  - ****Note****. Some recipients may have read receipts turned off. In these cases, they could have opened the RCS message, but an open event will not be received.
- Target highly engaged recipients who ****open most RCS messages**** with VIP offers.

![](https://klaviyo.zendesk.com/hc/article_attachments/41073326096283)

## ****Conditional splits in flows****

Use RCS open behaviour to adjust a recipient’s path through a flow. For example:

- Send a reminder RCS message to people who ****did not open**** the first one.
  - ****Note****. Some recipients may have read receipts turned off. In these cases, they could have opened the RCS message, but an open event will not be received.
- If someone ****opened**** but did not click, send a stronger follow-up incentive.

You can also specify a particular message when setting up your split by clicking the filter button next to ****Opened Text****.

![](https://klaviyo.zendesk.com/hc/article_attachments/41073297809691)

## ****Attribution****

Opened Text events are also available as attributable events for text messages:

- By default, Klaviyo uses a ****24-hour attribution window****.
- You can adjust this in your attribution settings if you want a longer or shorter window.

This allows you to measure revenue influenced by recipients opening your RCS campaigns.

## ****Important considerations****

- ****RCS only****: Opens are not available for SMS or MMS. Open rates in aggregate reports only apply to RCS sends.
- ****Device settings****: RCS read receipts must be enabled for opens to be tracked.
  - ****Android**** – On by default.
  - ****iOS**** – Off by default (users must turn them on).
- ****Not all recipients will report opens****, so use them alongside other engagement signals such as clicks and conversions.

## ****Summary****

RCS open rates provide another layer of insight into message performance:

- View open rates in campaign and flow reports.
- Drill into recipient-level opens and see them on profile timelines.
- Use the “Opened Text” event for segmentation, conditional splits, and attribution.

Remember that open events depend on device settings, and not all recipients will report them. Use them as one part of your engagement strategy alongside clicks and conversions.