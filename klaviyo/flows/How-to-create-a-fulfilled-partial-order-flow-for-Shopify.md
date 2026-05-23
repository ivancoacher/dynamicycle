---
id: 4401771131419
title: "How to create a fulfilled partial order flow for Shopify"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4401771131419-How-to-create-a-fulfilled-partial-order-flow-for-Shopify"
section: "Ecommerce-specific flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: en
---

## You will learn

Learn how to create a Klaviyo flow for partial orders placed through Shopify. If you often deliver orders as separate shipments rather than all at once (or your fulfillment center does), you can let customers know when each item is fulfilled via a fulfilled partial order flow. This flow lets your customers know exactly when a certain item is on its way, leading to a better overall customer experience.

In Klaviyo, you can use the **Fulfilled Partial Order** metric to trigger this flow when one or more items are fulfilled. You can also combine this with a standard fulfilled order flow, which sends only when every item in an order has been fulfilled. In this article, we go over different options for configuring your partial and full fulfillment order flows.

## Create a fulfilled partial order flow from the flow library

After you integrate your Shopify store with Klaviyo, you'll find several best practice flows populated automatically within the [flow library](https://www.klaviyo.com/library/flows), including a pre-built fulfilled partial order flow.

1. Navigate to the ****Flows**** tab.
2. Click ****Create flow.****
3. Search for **Partial Shipping Confirmation.**
4. Click on one of the pre-built flow options.

## Set up a fulfilled partial order flow from scratch

To create a fulfilled partial order flow from scratch:

1. Create a metric-triggered flow.
2. For the flow trigger, select ****Fulfilled Partial Order**** from the Shopify metrics under **Your metrics**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34376136026267)
3. Click ****Save****.
4. Add in your message(s). If you plan to send an SMS, first drag in a conditional split so that the text message only sends to those who are opted in to SMS marketing, as shown below. In this case, we recommend adding an email, so that everyone who isn’t subscribed to SMS will still get updated about their order.

![Conditional split that checks for SMS consent.](https://klaviyo.zendesk.com/hc/article_attachments/28720772234907)

## Options for sending fulfillment messages

Depending on your use case, you can set up your fulfilled and fulfilled partial order flows in several different ways. For example, you can send:

- When the entire order is fulfilled
- Each time part of the order is fulfilled
- Do both, depending on whether or not the entire order is fulfilled at the same time

### Sending only when the entire order is fulfilled

If you want to send only one message when the entire order is fulfilled, use a regular fulfilled order flow. This is essentially the same as a fulfilled partial order flow except that it is triggered by the **Fulfilled Order** metric.

![Fulfilled order email following the Fulfilled Order trigger.](https://klaviyo.zendesk.com/hc/article_attachments/28720772238747)

### Send when each part of the order is fulfilled

If you want to send messages each time part of the order is fulfilled, you can use the fulfilled partial order flow shown above.

When the last item(s) in an order are fulfilled, you have two options:

- Sending two messages, one from a fulfilled order flow and one from a fulfilled partial order flow
- Sending one message via a fulfilled order flow

For the first approach, you do not need to change either your fulfilled or fulfilled partial order flows. However, make sure to explain exactly what the difference is in your messages. For instance, the fulfilled order flow should make it clear that the entire order has been fulfilled, rather than it being partially done.

If you want to only send one message for the final item, add a trigger filter to your fulfilled partial order flow. Set the filter to be **FulfillmentStatus equals partial**.

![Trigger filter with configuration 'FulfillmentStatus equals partial'.](https://klaviyo.zendesk.com/hc/article_attachments/28720772241179)

### Send different flows based on if the entire order is fulfilled

You can also have the best of both worlds:

- Send a message each time part of an order is fulfilled
- Send a single message when the entire order is fulfilled at the same time

To set this up, you do not need to add any trigger or flow filters to your partial fulfillment flow.

In your regular fulfillment flow, add the trigger filter **HasPartialFulfillments is false**.

![Trigger filter with configuration 'HasPartialFulfillments is false'.](https://klaviyo.zendesk.com/hc/article_attachments/28720760472731)

## Additional resources

- Find out more about what syncs from Shopify in: [Shopify data reference](https://help.klaviyo.com/hc/en-us/articles/115005080447)
- Learn more about flows:
  - [How to use flows to send transactional emails](https://help.klaviyo.com/hc/en-us/articles/360003165732)
  - [How to create a post-purchase flow](https://help.klaviyo.com/hc/en-us/articles/360028872611)
  - [How to create an upsell or cross-sell flow](https://help.klaviyo.com/hc/en-us/articles/115002775212)