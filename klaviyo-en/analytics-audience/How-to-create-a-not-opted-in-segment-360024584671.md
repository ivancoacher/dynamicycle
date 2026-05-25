---
id: "360024584671"
title: "How to create a not-opted-in segment"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360024584671-How-to-create-a-not-opted-in-segment"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "en"
---
## You will learn

Learn how to use segments to identify active profiles in your account that aren't explicitly opted in to marketing. When sending campaigns, it can be useful to exclude this segment from some campaign sends. This can be done in place of adding conditions to your target segment to only include opted-in subscribers.

## Create a not-opted-in segment

## Email

Because there are a number of ways [active profiles](https://klaviyo.zendesk.com/hc/en-us/articles/115005246968), or emailable contacts, are added to your account, it is important to exclude not opted-in contacts so that you don't receive high unsubscribe or spam complaint rates. Contacts who are not opted in and are not [suppressed](https://help.klaviyo.com/hc/en-us/articles/115005246108) can still trigger flows. Learn more about [how contacts are added to your Klaviyo account](https://help.klaviyo.com/hc/en-us/articles/115005246968).

This segment contains anyone who is suppressed for email (i.e., cannot be emailed, perhaps because they unsusbcribed) as well as anyone who is emailable, but hasn't given explicit consent to receive marketing. These profiles may have been added through general engagement (e.g., by initiating a checkout but not completing it).

To create a not-opted-in segment:

1. Navigate to ****Audience > Lists & segments****.
2. Click ****Create New > Create segment****.
3. Use the following segment definition:
   - **If someone can or cannot receive marketing > cannot receive > email marketing**
     OR
   - **If someone can or cannot receive marketing > can receive > email marketing > because person > never subscribed.
     ![Segment of people who are did not consent to email marketing](https://klaviyo.zendesk.com/hc/article_attachments/33130558099995)**

### SMS or push notifications

You can create similar segments for other channels, like SMS or push. With these channels, "never subscribed" contacts are unreachable for that channel, so you can simply use this segment definition:

**If someone can or cannot receive marketing > cannot receive > SMS marketing/mobile push marketing**

**![Segment for those not opted in to SMS marketing](https://klaviyo.zendesk.com/hc/article_attachments/33130558103835)**

## Outcome

When sending campaigns, use the [don't send to feature](https://help.klaviyo.com/hc/en-us/articles/115005227808) to ensure that this segment is excluded from your sends. Then, when you're ready to send your next campaign, [clone the previous one](https://help.klaviyo.com/hc/en-us/articles/115006199048). Cloned campaigns inherit the same recipient groups, so you don't have to worry about excluding this segment every single time you create a campaign.

## Additional resources

- [Create customer engagement tiers](https://klaviyo.zendesk.com/hc/en-us/articles/360000407272)
- [Understanding frequently asked questions about GDPR](https://klaviyo.zendesk.com/hc/en-us/articles/360003211651)
- [How to segment on channel consent](https://klaviyo.zendesk.com/hc/en-us/articles/19514751281307)