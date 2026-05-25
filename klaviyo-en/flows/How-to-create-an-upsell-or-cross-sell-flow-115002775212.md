---
id: "115002775212"
title: "How to create an upsell or cross-sell flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115002775212-How-to-create-an-upsell-or-cross-sell-flow"
section: "Post-purchase flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:37Z"
language: "en"
---
## You will learn

Learn how to create a flow that allows you to follow up with customers to try to cross-sell or upsell similar or related products after they make a purchase. Klaviyo has a built-in product review/cross-sell flow as well as new and repeat customer thank you flows that you can repurpose as upsell or cross-sell flows.

You can also create your own upsell or cross-sell flows from scratch. This guide will walk you through what you should keep in mind when customizing Klaviyo's built-in flows or creating your own.

## Flow trigger

### Cross-sell

Your flow trigger should be either **Placed Order** or **Fulfilled Order.**The **Placed Order** event tracks when someone places an order for an item, while the **Fulfilled Order**event tracks when an item is shipped. Klaviyo's built-in product review / cross-sell flow uses the **Fulfilled Order**event as the trigger because this is closer to when a customer actually receives a product. However, depending on your preferences, you can use either.

Your trigger should include the trigger filter to **Only include people if they have Fulfilled Order zero times since starting this flow**. This ensures that if another item they purchased ships while they are in the flow, they don't receive the emails.

![Flow trigger with trigger filter set to Only include people if they have Fulfilled Order zero times since starting this flow](https://klaviyo.zendesk.com/hc/article_attachments/28715961710875)

### Upsell

For an upsell flow, you may want to use a different trigger altogether. If, for example, a customer views a pair of shoes, but you'd like to sell them a different, more expensive pair of shoes, you'll want to use the **Viewed Product** event to trigger your flow. The full list of available event triggers depends on your particular integration and can be viewed in the [Analytics tab](https://www.klaviyo.com/analytics/metrics) of your account by clicking into Metrics.

## Flow filters

You may also want to filter your cross-sell and upsell flows by category or collection. This will make it easier to provide relevant recommendations in the content of your emails since you'll have a better idea of what a customer was looking at when they triggered the flow.

![Flow trigger with trigger filter set to filter for orders from a specific collection](https://klaviyo.zendesk.com/hc/article_attachments/28715968283291)

## Timing

When creating an upsell or cross-sell flow, you should first decide whether you want your flow to be pre- or post-purchase.

If you'd like to cross-sell a customer, you probably want to send your flow post-purchase — you might even want to wait until your customer has received their order. This is why the default product review / cross-sellflow is set to go out 14 days after an order is fulfilled.

If you'd like to upsell a customer, you may want to send your flow pre-purchase instead. Choosing the appropriate flow trigger is important since it's important that you email customers at the right time during the buying cycle. You might even want to upsell products directly within a browse abandonment or abandoned cart flow by including a product feed of similar products.

## Content

[Product feeds](https://help.klaviyo.com/hc/en-us/articles/115005082787-An-Overview-of-Product-Feeds-and-Recommendations) are a great way to upsell or cross-sell products within an email. Since you can constrain product feeds to a specific category or collection, you can provide more relevant recommendations based on what product a customer was interacting with (purchased, viewed, etc.) when they triggered the flow.

![Example of a set of recommended products populated from a feed and listed in a grid pattern within an email](https://klaviyo.zendesk.com/hc/article_attachments/28715961707419)

## Additional resources

Learn more about [creating post-purchase flows in this guide](https://help.klaviyo.com/hc/en-us/articles/360028872611).

Learn about specific types of flows such as [browse abandonment](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow-VFB-) or [abandoned cart](https://help.klaviyo.com/hc/en-us/articles/115002779411-Create-an-Abandoned-Cart-Flow-VFB-) flows.

Get details on [building a product review flow](https://help.klaviyo.com/hc/en-us/articles/115002779391).

Want to dive deeper into creating tailored content? Take this [course on personalizing your emails](https://academy.klaviyo.com/guide-to-email-personalization).