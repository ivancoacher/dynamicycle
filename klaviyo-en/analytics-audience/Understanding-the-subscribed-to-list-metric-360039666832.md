---
id: "360039666832"
title: "Understanding the subscribed to list metric"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360039666832-Understanding-the-subscribed-to-list-metric"
section: "Metrics best practices"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: "en"
---
## You will learn

Learn about the **Subscribed to List** metric, which appears on a customer’s profile whenever they subscribe to a list in Klaviyo. This includes:

- When someone fills out a Klaviyo signup form and then confirms their subscription (via double opt-in).
- When a profile is added to a list with email consent via Quick Add.
- When a profile is added to a list with email consent via CSV upload.
- When someone subscribes through a Klaviyo-built integration, or certain third-party integrations.

Because of this, it is crucial to understand best practices around using it for creating segments. In this article, you will learn what the **Subscribed to List** metric entails and when to use it.

## The subscribed to list metric

The **Subscribed to List** is a metric that appears on a customer’s profile when they subscribe to one of your lists. Below is an example of what this metric will look like in a profile.

For SMS events only, Klaviyo is able to record multiple **Subscribed to a list** events.

![Subscribed to list event on a profile](https://klaviyo.zendesk.com/hc/article_attachments/36495394610203)

If someone enters their information into the same form multiple times, they will not have multiple **Subscribed to List** metrics found under their profile, nor will they be re-added to the list multiple times.

Klaviyo will only add a **Subscribed to List** event to a given profile if they are either:

- Not in the list
- In the list, but [suppressed](https://help.klaviyo.com/hc/en-us/articles/115005246108)

## When the subscribed to list metric is added to a profile

The **Subscribed to List** metric will appear whenever someone subscribes to a list that they weren’t previously subscribed to.

To learn more about subscribers syncing from Shopify, check out [How to sync Shopify email subscribers to a Klaviyo list](https://help.klaviyo.com/hc/en-us/articles/115005080667-How-to-Sync-Shopify-Email-Subscribers-to-a-Klaviyo-List#about-the-accepts-marketing-property-and-subscribers3).

## When to use in a flow

In general, using the **Subscribed to List** metric to trigger your flow is not a best practice. Instead, if you want customers in a specific list to go through your flow when added, [create a list-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003031652).

![Available flow triggers](https://klaviyo.zendesk.com/hc/article_attachments/36495380398363)

If you do use this metric to trigger your flow, be sure to add a trigger filter identifying the specific list you are referring to with the **Subscribed to List** metric. For example, this trigger filter is: **List equals Product Review List**.

![Added to list flow trigger](https://klaviyo.zendesk.com/hc/article_attachments/36495380400155)

## When to use in a segment

Use the **Subscribed to List** metric when building a segment if you want to view how many people subscribed to a list. For example, if you want to see how many of a list's members were added in the last 2 weeks.

- If someone is or not in a list > Person is in [**List name**]
  AND
- Subscribed to list at least once in the last 14 days

![Segment using subscribed to list event](https://klaviyo.zendesk.com/hc/article_attachments/36495380401563)

## Additional resources

- [How to create and manage sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360002049952)
- [How to create a welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172)
- [Understanding flow triggers and filters](https://help.klaviyo.com/hc/en-us/articles/115002779051)
- [Understanding email metrics](https://help.klaviyo.com/hc/en-us/articles/360036974872)