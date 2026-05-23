---
id: 115005076747
title: "How to view raw metric or profile activity data in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005076747-How-to-view-raw-metric-or-profile-activity-data-in-Klaviyo"
section: "Build and use metrics"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:17Z"
language: en
---

## You will learn

Learn how to view the raw event or profile activity data that Klaviyo receives from your integrations or API calls. This can be useful if you want to verify a profile's data along with a given event, or simply review this data to better understand what's being captured per metric.

## Finding raw metric data

1. To view raw metric or event data, go to the ****Analytics**** ****>**** ****Metrics.****
2. You can view your activity feed data by searching for a metric in the **Seach metrics** field above or by the clicking into a metric from the list below.
3. Once inside the metric, navigate to the ****Activity feed**** tab.
   ![activity_feed_tab.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720891621915)

   Note that if you click the activity feed button at the top of the metrics page, you will not be able to see the raw data output here. Profile activity details are only accessible from within a specific metric.
4. Find a profile that you want to review and click on the ****three dot menu**** on the right.
5. Click on ******Activity Details******.
   ![activity_details-new.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720891619483)

You will then see a modal containing all JSON information related to that metric and specific profile. For example, if you use the **Opened Email** metric you will see information on the email domain used, associated message, client type, client OS, client OS family, client name, message name, etc. The example below uses **Added to Cart** and captures information such as the product name, product ID, URL, image URL, price, etc.

![activity_details_modal-new.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720891626395)

You can then copy a JSON version of any or all of this event data if you wish.

## Understanding timestamps

Now that you retrieved data from the **Activity Details**, it’s important to understand the meaning behind the two timestamps included in this information. The two times are often but not always identical.

The first timestamp refers to the time the event is first triggered. For example, if the trigger for a flow is **Checkout Started**, then this timestamp details exactly when the checkout occurs on your ecommerce site. The second timestamp is the time in which the event appears in Klaviyo. Usually, these timestamps are the same or seconds apart, as shown in the example below.

![Activity details timestamp at top with activity and recorded timestamps as the same value](https://klaviyo.zendesk.com/hc/article_attachments/28720891616155)

Depending on your [integration](https://help.klaviyo.com/hc/en-us/categories/115000032731-Ecommerce-Integrations), the time it takes for Klaviyo to receive this information from the other source may lead to a delay. An example of this type of expected delay is displayed below.

![Activity details timestamp at top with activity and recorded timestamps as different values](https://klaviyo.zendesk.com/hc/article_attachments/28720846537371)

In the examples above, the first timestamp is the same (first image), and the second timestamp (second image) states exactly when Klaviyo registers the event from your integration. Learn more about [how often particular integrations sync](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208).

#### Why both timestamps are important

Understanding timestamps is vital to ensuring that your emails are timely and relevant. It's important to take any delay in event syncing into consideration when planning your marketing strategy, especially when creating flows. For an abandoned cart flow, if a customer begins a checkout and then completes their purchase, this event data may take an hour (as is the case for WooCommerce) for Klaviyo to register that they completed a purchase. If you set your first flow email to send out a half-hour after the **Checkout Started** event and we have not received confirmation that the checkout was completed, this customer may receive the abandoned cart flow email by mistake.

In general, if you have an integration with a sync delay, we recommend that you set your flow emails to send an hour (or later) after a trigger event to avoid unintended consequences. This is best practice, with the exception of a welcome series which often sends immediately after someone subscribes and would not be affected negatively by a time delay.

## Additional resources

- [How often integrations sync reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208)
- [Getting started with metrics](https://klaviyo.zendesk.com/hc/en-us/articles/115005076787)