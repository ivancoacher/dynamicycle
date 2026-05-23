---
id: 39786250669083
title: "How to connect your subscriptions provider to Customer Hub"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/39786250669083-How-to-connect-your-subscriptions-provider-to-Customer-Hub"
section: "Integrate other platforms with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:55Z"
language: en
---

Learn how to display subscription details on orders in Customer Hub by connecting Recharge, Skio, or Shopify order data.

Customer Hub currently supports Shopify storefronts, including Shopify Headless. Additional eCommerce platform support is planned.

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

- Make sure Customer Hub is enabled in your Klaviyo account.
- If you’re connecting a supported subscription app (Recharge or Skio):
  - Ensure the [Recharge app](https://apps.shopify.com/subscription-payments) or [Skio app](https://apps.shopify.com/skio) is set up and active on your Shopify store.
  - Ensure the app is integrated with Klaviyo
- If you’re using Shopify order data, no extra setup is needed.

## How subscription information displays in Customer Hub

When customers log in to their account on your Shopify site and open the Customer Hub drawer, they can view recent orders on the **Orders** tab. By connecting a subscriptions provider, you can show subscription details next to each applicable product in an order, making it easy for customers to identify which products are part of a subscription versus standalone purchases.

The subscriptions setting is off by default. If neither a subscription app nor Shopify order data are connected, no subscription information will appear in Customer Hub.

Subscription details appear differently, depending on which connection you have enabled:

****Supported subscription apps (Recharge, Skio)****:

- Products purchased as part of a subscription display a badge with the subscription name (e.g., "Monthly") next to those items.
- A **Manage subscription** link is shown, guiding customers directly into the subscription app experience to view or manage their subscription.
  ![CHsub1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39786233689499)

  ****Shopify order data****:
- Products purchased as part of a subscription display a badge with the subscription name next to those items.
- There is no button or option to manage subscriptions.

For products purchased as a one-time purchase, no subscription badge or subscription management link is shown. If an order contains both subscription and non-subscription products, only the subscription items display these details.

## Connect your subscription provider

1. In Klaviyo, go to ****Service - Customer Hub**** in the main navigation.
2. Select ****Extensions****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40774370368283)
3. Under **Subscriptions**, toggle the setting on, then choose 1 of the following options:

   - ****Recharge****
   - ****Skio****
   - ****Shopify order data****
   - ****Ordergroove****![image (32).png](https://klaviyo.zendesk.com/hc/article_attachments/47652072240027)
4. Click ****Save****.

Customer Hub will now use your selected option to display subscription details next to applicable products in your customers’ orders.

## Optional: adding a content block for subscriptions

Like with all integrations that write profile data into Klaviyo, you can use [content blocks](https://klaviyo.zendesk.com/hc/en-us/articles/33660517680795) to surface dynamic information. Note that for some content blocks, such as the template we provide for Recharge, there is no default link set. You must set the link for the content block and link it to your subscription landing page. Until you set this link, while the content block can display data like active subscription count, clicking the content block will not do anything because the link is not set.

## Additional resources

- [How to display product recommendations in Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660504643867)
- [How to connect your reviews provider to Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660618974491)
- [How to add a help button to the Customer Hub orders tab](https://help.klaviyo.com/hc/en-us/articles/33660636674843)