---
id: "32826141659675"
title: "How to create an unengaged segment"
source_url: "https://help.klaviyo.com/hc/en-us/articles/32826141659675-How-to-create-an-unengaged-segment"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:39Z"
language: "en"
---
## You will learn

Learn how to identify your unengaged email subscribers, so you can avoid contacting them to improve and maintain your deliverability. Once you've identified your unengaged subscribers, consider excluding them from most of your campaign sends. In this article, you will learn how to create an unengaged segment.

Sending to unengaged profiles who haven't engaged with your emails in 3-6 months can result in inbox providers (e.g., Gmail, Yahoo, Outlook) placing your emails into the spam folder.

## Create an unengaged segment

To create an unengaged segment in Klaviyo:

1. Navigate to the **Lists & Segments** tab of your account
2. Select ****Create List / Segment**** > ****Segment****
3. Add the following segment definition:

   Person ****can receive email marketing****
   AND
   What someone has done > ****Received Email is at least 5 over all time****
   AND
   What someone has done > ****Opened Email 0 times in the last 90 days****
   AND
   What someone has done > ****Clicked Email 0 times in the last 90 days****

![complete.jpg](https://klaviyo.zendesk.com/hc/article_attachments/32827406962075)

You can edit the definition to best reflect your brand and how often you send emails; in this example, unengagement is defined by a 90 day (3 month) timeframe. This segment identifies contacts that have been receiving emails, but haven’t opened or clicked in 90 days.

When the segment definition best suits your business, click ****Create Segment****. Your segment will then be available for you to analyze, exclude from campaigns, re-engage, and more.

With the release of iOS15, macOS Monterey, iPadOS 15, and WatchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. This can cause open rates to be inflated.

If your campaign analytics show a large number of iOS openers, we suggest identifying these affected opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

For complete information on MPP opens, visit our iOS 15: [How to Prepare for Apple’s Changes guide](https://www.klaviyo.com/blog/apple-ios15-klaviyo).

## Additional resources

[How to market to profiles you shouldn't email](https://help.klaviyo.com/hc/en-us/articles/115002565892)
[How to create an engaged segment](https://help.klaviyo.com/hc/en-us/articles/115000200072)
[How to create a segment of VIP customers](https://help.klaviyo.com/hc/en-us/articles/115005065707)