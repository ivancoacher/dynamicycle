---
id: "115005078347"
title: "How to create a never engaged segment"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005078347-How-to-create-a-never-engaged-segment"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T11:00:09Z"
language: "en"
---
## You will learn

Learn how to identify your least engaged email subscribers, so you can avoid contacting them to improve and maintain your deliverability. Once you’ve identified them, consider excluding them from your marketing initiatives, sending them one final re-engagement attempt, or suppressing them during list cleaning. In this article, you will learn how to create this segment.

Note that regularly sending to profiles who don't engage with your emails can cause providers (e.g., Gmail, Yahoo, Outlook) will start placing your emails in spam.

Profiles that never engage are the most likely to erode your sender reputation over time. Stopping sends to them is the single most effective way to address all deliverability concerns, such as:

- Emails landing in the spam folder
- Low open rate
- Low click rate
- Low conversions
- [High spam rate](https://help.klaviyo.com/hc/en-us/articles/360057985791)
- High bounce rate
- High unsubscribe rate

## Create a never engaged segment

### Create a never engaged segment with 1 click

If you have not already created this segment, you can also quickly create a never engaged segment from the [deliverability hub](https://help.klaviyo.com/hc/en-us/articles/18378819907995) in Klaviyo.

To access the page, navigate to the **Deliverability** tab under **Analytics**in Klaviyo. Select ****Create segment****on the action center for the **Create a Never engaged segment**recommendation.

![Button to create a never engaged segment on the action center](https://klaviyo.zendesk.com/hc/article_attachments/31754094987547)

After creating the segment on the deliverability hub, you'll see it on the **Lists & Segments** page in Klaviyo.

### Create a never engaged segment manually

Follow the steps below to create a **Never Engaged** segment in Klaviyo manually.

1. Navigate to ****Audience**** > ****Lists & segments in**** your account.
2. Select ****Create New > Create Segment.****
3. You can name it, **Never Engaged.**
4. Add the following conditions, and select ****Create****.

- If someone can or cannot receive marketing > ****Person**** ****can receive email marketing****
  AND
- What someone has done (or not done) > ****Person has Received Email is at least 5 in the last 180 days****
  AND
- What someone has done (or not done) > Person has ****Opened Email 0 times over all time****
  AND
- What someone has done (or not done) > Person has ****Clicked Email 0 times over all time****
  AND
- What someone has done (or not done) > Person has ****Placed Order 0 times over all time****

![Never engaged segment](https://klaviyo.zendesk.com/hc/article_attachments/33252379034267)

## Bulk suppress the segment to optimize deliverability

Suppression only applies to the email channel.

1. Navigate to ****Audience**** > ****Lists & segments in**** your account.
2. Click the 3 dots next to the segment you wish to suppress.
3. Click ****Suppress current members.****

![suppress_current members.jpeg](https://klaviyo.zendesk.com/hc/article_attachments/31754094989851)

With the release of iOS15, macOS Monterey, iPadOS 15, and WatchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.

If your campaign analytics show a large number of iOS openers, we suggest identifying these affected opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

## Additional resources

- [How to manage email suppressions and delete profiles in bulk](https://help.klaviyo.com/hc/en-us/articles/24312135764251#h_01HT5F82SYQGF8XH34ATAEF0YA)
- [Guide to list cleaning](https://klaviyo.zendesk.com/hc/en-us/articles/115005078347)
- [How to create an engaged segment](https://klaviyo.zendesk.com/hc/en-us/articles/115000200072)
- [How to create a segment of VIP customers](https://klaviyo.zendesk.com/hc/en-us/articles/115005065707)