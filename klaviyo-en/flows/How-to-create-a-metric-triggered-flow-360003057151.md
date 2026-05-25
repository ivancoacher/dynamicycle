---
id: "360003057151"
title: "How to create a metric-triggered flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360003057151-How-to-create-a-metric-triggered-flow"
section: "Ecommerce-specific flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:50Z"
language: "en"
---
## You will learn

Learn how to create a metric-triggered, also called event-triggered, flow that is used to email subscribers when they take a certain action. These actions correspond with "metrics," or events, in Klaviyo. Available metrics are found under Metrics in the [Analytics tab](https://www.klaviyo.com/analytics/metrics) in your account and are typically synced through your ecommerce integration or as custom events. However, it's important to note that clicks, opens, and received email metrics are not available for selection to trigger a flow.

Some common examples of metric-triggered flows include:

- Abandoned cart (triggered by the **Started****Checkout** metric)
- Post-purchase (triggered by the **Placed Order** metric)
- Browse abandonment (triggered by the **Viewed Product** metric)
- Product review (triggered by the **Placed Order** metric)

Contacts will receive a metric-triggered flow every time they complete the corresponding action unless you add [filters](https://help.klaviyo.com/hc/en-us/articles/115002779051) to the flow that specify otherwise. For example, if someone places an order and receives your post-purchase flow, and then places another order a month later, they will re-trigger the flow and receive the same emails again.

## Configure a metric-triggered flow

To create a metric-triggered flow:

1. Create a new flow.
2. Select ****Metric**** in the sidebar.
   ![In the trigger setup menu of the flow builder, the Metric option can be found in the middle of the list](https://klaviyo.zendesk.com/hc/article_attachments/28717850836891)

Next, you will be prompted to select the metric that will trigger the flow. Available metrics will vary from account to account and depend primarily on the integrations you are using and any custom metrics you have set up. Most integrations come with their own metrics. Below, you can find the metrics that are synced with popular ecommerce integrations:

- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080447)
- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082587)
- [Magento](https://help.klaviyo.com/hc/en-us/articles/115005254528)
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115003458852)
- [Woocommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808)

If you'd like to create custom metrics, visit our [developer portal](https://developers.klaviyo.com/en/docs/custom_event_tracking).

For more information on which metrics are synced with your integration, [how often those metrics are synced](https://help.klaviyo.com/hc/en-us/articles/115005253208), and what metric data is available, you can find the corresponding help documentation in the Klaviyo Help Center or in the integration's help center.

Performance metrics such as **Opened Email** and **Clicked** **Email**cannot be used to trigger flows.

Optionally, you can add [trigger and flow filters](https://help.klaviyo.com/hc/en-us/articles/115002779051) to further refine who is added to the flow — for example, restrict your post-purchase series to:

- People who bought a specific product
- People who are first-time customers (have never placed an order before)
- People who bought a certain number of items
- People who bought from a specific category/collection
- People who spent a specific amount of money

![Example of a trigger using the Placed Order metric and a trigger filter with configuration 'And Items contains Wrinkle Free Off White Tee'](https://klaviyo.zendesk.com/hc/article_attachments/28717850840347)

Once you set a particular metric to trigger the flow, you will not be able to change it to a different one. In order to do this, you will need to [clone the flow](https://help.klaviyo.com/hc/en-us/articles/115002775052) and change the metric that triggers the flow.

## How a metric-triggered flow works

Whenever someone takes the action (metric) that triggers the flow, they will be queued up to receive the email sequence. For a post-purchase, for example, you would select the **Placed Order** metric, and then everyone who places an order will be queued up.

Contacts will receive a metric-triggered flow every time they take the associated action. If someone takes an action and later repeats this action, they will re-trigger the flow. If you would like to narrow the scope of your flow, you can set up [flow and trigger filters](https://help.klaviyo.com/hc/en-us/articles/115002779051).

If you are relying on an integration for a metric — e.g., the **Placed Order** event from Magento 2, which syncs with the integration every half-hour — you will want to pay attention to how often the integration syncs when configuring the timing of your flow. If you have a metric-triggered flow that is set to send immediately, recipients may not actually receive the email immediately, depending on the frequency of the sync. Shopify and BigCommerce metrics sync in real time.

## Additional resources

See how to create metric-triggered flows:

- [Abandoned cart](https://help.klaviyo.com/hc/en-us/articles/115002779411)
- [Browse abandonment](https://help.klaviyo.com/hc/en-us/articles/115002775252)
- [Post-purchase](https://help.klaviyo.com/hc/en-us/articles/360028872611)
- [Upsell or cross-sell](https://help.klaviyo.com/hc/en-us/articles/115002775212)