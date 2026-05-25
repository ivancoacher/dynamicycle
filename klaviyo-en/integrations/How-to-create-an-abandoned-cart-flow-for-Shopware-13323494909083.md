---
id: "13323494909083"
title: "How to create an abandoned cart flow for Shopware"
source_url: "https://help.klaviyo.com/hc/en-us/articles/13323494909083-How-to-create-an-abandoned-cart-flow-for-Shopware"
section: "Shopware"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:42Z"
language: "en"
---
## You will learn

Learn how to create an abandoned cart flow for Shopware 6, in order to increase your ecommerce revenue and personalize communication to your customers. This flow will use the **Started Checkout** event synced from your Shopware store.

## Before you begin

Before you create this flow, make sure to do the following:

- Integrate Klaviyo with Shopware 6 (see [Getting started with Shopware 6](https://help.klaviyo.com/hc/en-us/articles/13001662470939) to learn how). As part of the integration process, make sure you:

- Sync **Started Checkout** and **Placed Order** events. This requires you to toggle them on in your extension settings.
  ![Track Started Checkout and Track Placed Order toggled on to blue](https://klaviyo.zendesk.com/hc/article_attachments/28705638160667)
- Sync your Shopware 6 product catalog to Klaviyo.

## Create the flow

1. In Klaviyo, select the ****Flows**** tab.
2. Click ****Create Flow****.
3. Search for **Abandoned cart**, then select the ****Abandoned cart reminder: Standard**** flow for a custom ecommerce cart.

- For Klaviyo flow purposes, Shopware is a custom ecommerce cart. Klaviyo provides pre-built flows with pre-filled data for custom ecommerce carts.
  ![Abandoned Cart Reminder: Standard flow card for a custom ecommerce cart](https://klaviyo.zendesk.com/hc/article_attachments/28705638158619)
- The window that appears will give you an overview of how the flow works, and what event triggers it (in this case, **Started Checkout**, synced from Shopware). This flow also relies on the **Placed Order** event for filtering.
- Click ****Create Flow****.
  ![Abandoned Cart Reminder Flow trigger by Started Checkout preview with create flow in white with black background](https://klaviyo.zendesk.com/hc/article_attachments/28705638162459)
- In the flow builder, customize the flow and the emails within it to fit your brand. The flow emails will be automatically configured to show customers an item they’ve left behind, and bring them back to their carts via the **Return to your cart** button. To learn more about best practice for abandoned cart flows, read our article [How to create an abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411).
  ![Klaviyo template builder showing email Thanks for stopping by and Return to your cart in white with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28705638164635)
- When you are ready to begin sending abandoned cart messages to customers, you can [change the flow status to live or manual](https://help.klaviyo.com/hc/en-us/articles/115002774932#set-the-flow-action-status7).

It is important to note that carts can only be rebuilt for 120 days from the date they were created; after that, they expire.

## Outcome

You’ve created an abandoned cart flow for Shopware 6 and can now better personalize your customer communications and drive revenue.

## Additional resources

- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [How to personalize flows with dynamic event data](https://help.klaviyo.com/hc/en-us/articles/115002779071-Personalize-Flow-Emails-with-Dynamic-Event-Data)
- [How to use abandoned cart emails to improve sales: strategies, examples, and expert advice](https://www.klaviyo.com/blog/abandoned-cart-email)