---
id: 360043947571
title: "Understanding the benefits of having a main list for each marketing channel"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360043947571-Understanding-the-benefits-of-having-a-main-list-for-each-marketing-channel"
section: "Getting started with lists and segments"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: en
---

## You will learn

Learn about the benefits of using one main list per marketing channel (e.g., SMS and email) and how to organize your lists in Klaviyo. Additionally, see the tools you can use to identify and target subscribers based on their behavior or how they subscribed.

## How to use your lists

Lists allow you to organize your contacts and keep track of who has subscribed to each of your marketing channels (e.g., email and SMS). Klaviyo recommends using 1 list per marketing channel:

- ****Email list****
  A list for all email contacts who have subscribed. Direct any email sign-up forms to this list.
- ****SMS list****
  A list for everyone who has opted in to receive SMS. Direct any SMS sign-up forms or subscribe keywords to this list.
- ****Additional lists as needed****
  For example, create a list for push notification subscribers.

## Benefits of a single main list for each channel

Using a single list for each channel has several benefits. Learn more about how this practice is helpful below.

****Easily find all your opted-in contacts****

When you use a single list per channel, it’s easy to identify everyone who has opted in to that channel. Note that when people unsubscribe from your messages, they may remain in your list (depending on how they unsubscribed). Unsubscribed profiles will always be skipped from any emails you send, even if they remain in the list.

To see the number of people in your list who have not unsubscribed, use this segment:

- **If someone is in or not in a list > is in > [your list]**
  AND
- **If someone can or cannot receive > cannot receive > [channel] marketing > because person Manually suppressed ![A segment of list members who are not suppressed](https://klaviyo.zendesk.com/hc/article_attachments/34337220586139)**

When someone unsubscribes from a message sent to a segment or through a metric-triggered flow, they may be suppressed from receiving emails but remain in your list.

If you’d like to remove these profiles from a list, click ****Manage List > Remove suppressed profiles****.

The first time you click this button, you may see a substantial drop in the list’s size. Klaviyo recommends removing these profiles once per month for the most accurate list growth report results.

****Maintain good data hygiene****

Maintaining good data hygiene means ensuring your Klaviyo data is error-free and up to date. Having more than 1 main list in your account may lead to the same profiles existing in multiple lists. As a result, if you consistently message these lists using separate campaigns, you may end up repeating messages and overwhelming subscribers with too much content.

Note that if you send a single campaign to multiple lists and the same profile is in more than 1 list, they will not receive the same email twice.

To learn more about creating segments, head to our resource on [getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908) and learn how [segments differ from lists](https://klaviyo.zendesk.com/hc/en-us/articles/115005061447).

****Access list growth visibility****

For every list in Klaviyo, you can access a growth report to capture data around your list's growth over time. Having a single main list for each channel allows you to see these changes on a larger scale, gaining insight into how your subscribers behave overall rather than only seeing growth for small portions of your audience.

To find this report, click into your main list and navigate to the ****List growth**** tab.
![List growth tab for a list](https://klaviyo.zendesk.com/hc/article_attachments/34337220587547)

****Optimize deliverability****

[Cleaning your lists](https://help.klaviyo.com/hc/en-us/articles/115005078347) is key to good deliverability. Having 1 main list per channel makes list cleaning easier by streamlining the process to remove outdated, unengaged profiles more efficiently.

In addition to regular list cleaning, target [engaged profiles](https://help.klaviyo.com/hc/en-us/articles/115000200072) in your account with email content and continually monitor your deliverability performance.

To do so, create an engaged segment based on a list. When you create a segment to identify engaged subscribers, add the segment criteria **If someone is in or not in a list > is in > [your list]**. By using this criterion, you can narrow your segment to focus on subscribers for a particular channel. For more information on handling consent, head to our article on [understanding consent in profiles](https://help.klaviyo.com/hc/en-us/articles/360037101072-Understanding-consent-in-profiles).

## How to target subscribers with segments

Using a single list for each marketing channel doesn’t limit your ability to target your subscribers. Rather than importing contacts into multiple lists, import them into a single list and use segments to personalize each recipient’s experience.

For example, use the **$source** property to identify profiles who subscribed through a certain source with the segment condition **Properties about someone > $source equals [subscriber\_source]**. The source name could be the name of the sign-up form the subscriber used, the integration they were synced through, etc.

## Additional resources

- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908-Getting-started-with-segments).
- [How to add subscribers to an existing list](https://help.klaviyo.com/hc/en-us/articles/115005251128-How-to-add-subscribers-to-an-existing-list)
- [How to clean your list to maintain good deliverability](https://help.klaviyo.com/hc/en-us/articles/115005078347)