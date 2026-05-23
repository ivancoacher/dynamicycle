---
id: 15156331062171
title: "How to create a winback flow for Amazon Buy with Prime"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15156331062171-How-to-create-a-winback-flow-for-Amazon-Buy-with-Prime"
section: "Amazon Buy with Prime"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:43Z"
language: en
---

## You will learn

Learn how to create a winback flow to send reminders to your Buy with Prime customers. Flows, also known as automations or drip campaigns, are Klaviyo’s tools for personalized communications with your customers. A winback flow re-engages customers who purchased in the past, but haven’t bought again in a while.

## Before you begin

- If you have not already set up the integration, follow our guide on [Getting started with Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467) for step-by-step instructions.
- To create the flow, you’ll also need to have Klaviyo integrated with your ecommerce platform. To learn how to integrate if you’ve yet to do so, [find your ecommerce platform on our Help Center](https://help.klaviyo.com/hc/en-us/categories/115000032731-Integrations).
- Want to learn more about how flows work in Klaviyo? Check out [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932).

Buy with Prime order data is only synced for profiles that have an email address.

## About Buy with Prime flows and your ecommerce platform

To create a flow using Buy with Prime data, you’ll also need to use data synced to Klaviyo from your ecommerce platform. This is because some necessary data data (such as your product catalog and data from purchases made directly on your ecommerce platform) does not sync through the Buy with Prime integration.

In Klaviyo, you can use a pre-built flow from our Flows Library, or you can create a flow from scratch. Currently, Klaviyo only offers pre-built Buy with Prime flows for Shopify, but pre-built flows for other ecommerce platforms (such as WooCommerce, BigCommerce, and Adobe Magento) are coming soon. Non-Shopify users can still create Buy with Prime flows today, but have to build them from scratch. We’ll show you how in this article.

## How to create a winback flow

Winback flows are customizable based on the products customers have purchased and how many purchases they've made.

If you’ve already created a winback flow using data from your ecommerce platform, you should create a second flow of the same type using Buy with Prime data, since your original flow will not account for customers who placed their original order using Buy with Prime. We also recommend adding an additional flow filter to your original winback flow in order to account for the Buy with Prime data now in your Klaviyo account:

- **Placed Order** (Buy with Prime) **zero times since starting this flow**.

### For Shopify customers

1. In your Klaviyo account, select the ****Flows**** tab.
2. Click ****Create Flow**** in the upper right.
3. Use the dropdown to filter by **Amazon Buy with Prime**.
   ![Flows tab in Klaviyo filtered by Amazon Buy with Prime](https://klaviyo.zendesk.com/hc/article_attachments/28720896431643)
4. Select the flow ****Customer Winback****, then click ****Create Flow**** in the window that appears.
   ![Buy with Prime Shopify Winback flow preview](https://klaviyo.zendesk.com/hc/article_attachments/28720901772443)
5. In the flow builder, customize the flow and the emails within it to fit your brand. To learn more about best practices for winback flows, read our article [How to create a winback flow](https://help.klaviyo.com/hc/en-us/articles/115002775192).
6. When you are ready to begin sending abandoned cart messages to customers, you can [change the flow status to live or manual](https://help.klaviyo.com/hc/en-us/articles/115002774932#set-the-flow-action-status7).

### For non-Shopify customers

1. In your Klaviyo account, select the ****Flows**** tab.
2. Click ****Create Flow**** in the upper right, then ****Create from Scratch**** in the upper right.
3. Name your flow (Buy with Prime Winback, for example) and add any tags, then click ****Create Flow****.
4. In the flow builder, set a metric-based trigger: **Placed Order (Buy with Prime).**
5. Set 2 flow filters:

1. **Placed Order (Buy with Prime) zero times since starting this flow**
   AND
2. **Placed Order (**Your ecommerce platform - e.g. BigCommerce**) zero times since starting this flow.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720901774619)**

6. Add a time delay of 75 days.
7. Add your first customer winback email.
8. Add a time delay of 15 days.
9. Add your second customer winback email.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720901779355)
10. Personalize your flow emails and feature updates such as new or trending products. Learn more in [How to create a winback flow](https://help.klaviyo.com/hc/en-us/articles/115002775192).
11. When you are ready to begin sending winback messages to customers, you can [change the flow status to live or manual](https://help.klaviyo.com/hc/en-us/articles/115002774932#set-the-flow-action-status7).

## Outcome

You’ve now learned how to create a winback flow using Buy with Prime data.

## Additional resources

- Learn how to integrate Amazon and Klaviyo with [Getting started with Amazon Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467)
- Learn about data synced between Amazon and Klaviyo with the [Buy with Prime data reference](https://help.klaviyo.com/hc/en-us/articles/14708160794779)