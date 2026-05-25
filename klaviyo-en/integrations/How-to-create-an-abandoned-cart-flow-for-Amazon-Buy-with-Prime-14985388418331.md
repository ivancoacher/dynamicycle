---
id: "14985388418331"
title: "How to create an abandoned cart flow for Amazon Buy with Prime"
source_url: "https://help.klaviyo.com/hc/en-us/articles/14985388418331-How-to-create-an-abandoned-cart-flow-for-Amazon-Buy-with-Prime"
section: "Amazon Buy with Prime"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:28Z"
language: "en"
---
## You will learn

Learn how to create an abandoned cart flow to send reminders to your Buy with Prime customers. Flows, also known as automations or drip campaigns, are Klaviyo’s tools for personalized communications with your customers. An abandoned cart flow is a message or sequence of messages sent to someone who added an item to their shopping cart, but failed to complete the purchase.

## Before you begin

- If you have not already set up the integration, follow our guide on [Getting started with Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467) for step-by-step instructions.
- To create the flow, you’ll also need to have Klaviyo integrated with your ecommerce platform. To learn how to integrate if you’ve yet to do so, [find your ecommerce platform on our Help Center](https://help.klaviyo.com/hc/en-us/categories/115000032731-Integrations).
- Want to learn more about how flows work in Klaviyo? Check out [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932).

Buy with Prime order data is only synced for profiles that have an email address.

## About Buy with Prime flows and your ecommerce platform

To create a flow using Buy with Prime data, you’ll also need to use data synced to Klaviyo from your ecommerce platform. This is because some necessary data data (such as your product catalog and data from purchases made directly on your ecommerce platform) does not sync through the Buy with Prime integration.

In Klaviyo, you can use a pre-built flow from our Flows Library, or you can create a flow from scratch. Currently, Klaviyo only offers pre-built Buy with Prime flows for Shopify, but pre-built flows for other ecommerce platforms (such as WooCommerce, BigCommerce, and Adobe Magento) are coming soon. Non-Shopify users can still create Buy with Prime flows today, but have to build them from scratch. We’ll show you how in this article.

## How to create an abandoned cart flow

Reminding customers about their cart can greatly prevent lost sales: almost 70% of shopping carts are abandoned on average.

For Buy with Prime, this flow is triggered by the **Checkout Started** event, which is tracked when a customer clicks **Proceed to checkout** on their Buy with Prime cart and authenticates with Amazon. This flow also has a time delay, and it filters out everyone who has purchased from your site, either using Buy with Prime (via the Buy with Prime **Placed Order** event) or directly in your site’s checkout page (via your ecommerce platform’s **Placed Order** event).

If you’ve already created an abandoned cart flow using data from your ecommerce platform, you should create a second flow of the same type using Buy with Prime data, since your original flow will not account for customers who started a checkout using Buy with Prime. We recommend adding an additional flow filter to your original abandoned cart flow of **Buy with Prime Placed Order zero times since starting this flow.** This will exclude customers who made purchases via Buy with Prime from receiving incorrect messaging.

## For Shopify customers

1. In your Klaviyo account, select the ****Flows**** tab.
2. Click ****Create Flow**** in the upper right.
3. Use the dropdown to filter by **Amazon Buy with Prime**.
   ![Klaviyo flows library filtered by Amazon Buy with Prime](https://klaviyo.zendesk.com/hc/article_attachments/28723661762971)
4. Select the flow ****Abandoned Cart Reminder****, then click ****Create Flow**** in the window that appears.
   ![Pre built Abandoned Cart Buy with Prime and Shopify flow with Create Flow with black background](https://klaviyo.zendesk.com/hc/article_attachments/28723633610907)
5. In the flow builder, customize the flow and the emails within it to fit your brand. The flow emails will be automatically configured to show customers an item they’ve left behind, and bring them back to their carts via the **Return to your cart** button. To learn more about best practices for abandoned cart flows, read our article [How to create an abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411).
6. When you are ready to begin sending abandoned cart messages to customers, you can [change the flow status to live or manual](https://help.klaviyo.com/hc/en-us/articles/115002774932#set-the-flow-action-status7).

## For non-Shopify customers

1. In your Klaviyo account, select the ****Flows**** tab.
2. Click ****Create Flow**** in the upper right, then ****Create from Scratch**** in the upper right.
3. Name your flow (Buy with Prime Abandoned Cart, for example) and add any tags, then click ****Create Flow****.
4. Set a metric-based trigger: **Checkout Started (Buy with Prime).**
5. Set 2 flow filters:
   a. **Placed Order (Buy with Prime) zero times since starting this flow**
   AND
   b. **Placed Order (**Your ecommerce platform - e.g., BigCommerce**) zero times since starting this flow.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723661769883)**
6. Add a time delay of 4 hours.
7. Add your first abandoned cart email reminder.
8. Add a time delay of 20 hours.
9. Add your second abandoned cart email reminder.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723633614875)
10. Personalize your flow emails to feature items left in a customer’s cart by pulling Buy With Prime product data using [dynamic template variables](https://help.klaviyo.com/hc/en-us/articles/115000096232) into an email [text block](https://help.klaviyo.com/hc/en-us/articles/115005082447#text-blocks4). Learn more in [How to create an abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411).
11. When you are ready to begin sending abandoned cart messages to customers, you can [change the flow status to live or manual](https://help.klaviyo.com/hc/en-us/articles/115002774932#set-the-flow-action-status7).

## Outcome

You’ve now learned how to create an abandoned cart flow using Buy with Prime data.

## Additional resources

- Learn how to integrate Amazon and Klaviyo with [Getting started with Amazon Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467)
- Learn about data synced between Amazon and Klaviyo with the [Buy with Prime data reference](https://help.klaviyo.com/hc/en-us/articles/14708160794779)