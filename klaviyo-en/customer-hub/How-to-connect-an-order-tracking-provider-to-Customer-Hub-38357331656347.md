---
id: "38357331656347"
title: "How to connect an order tracking provider to Customer Hub"
source_url: "https://help.klaviyo.com/hc/en-us/articles/38357331656347-How-to-connect-an-order-tracking-provider-to-Customer-Hub"
section: "Integrate other platforms with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:54Z"
language: "en"
---
Learn how to show enhanced shipment tracking in Customer Hub by connecting a supported order tracking provider. By default, Customer Hub displays tracking data from Shopify, but you can connect one of the following providers for expanded shipment details:

- Wonderment
- Malamo

If no provider is connected, tracking information from Shopify is shown by default.

Customer Hub for Shopify currently supports standard storefronts and Shopify Headless. For WooCommerce, navigate to https://help.klaviyo.com/hc/en-us/articles/47792369863451

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

Before you connect an order tracking provider, make sure:

- Customer Hub is enabled in your Klaviyo account.
- You have installed and set up Wonderment or Malamo in Shopify.
- The integration for your chosen provider is enabled in Klaviyo.

## How order tracking is handled in Customer Hub

When a customer signs in to their account on your Shopify site and opens the Customer Hub drawer, they can review their recent orders on the **Orders** tab and click any order for more shipping details.

****By default (Shopify)****:

- Customers can see the order status, date the order was placed, and order number.
- The “Track shipment” button links to Shopify’s tracking page.

****When an alternative order tracking provider (Wonderment or Malamo) is enabled****:

Customer Hub continues to show this information in the same layout, but now order shipment and delivery details are sourced from your connected order tracking provider with these enhancements:

- The “Track shipment” button links to the Wonderment or Malamo tracking page.

  If you’re using Malomo, make sure you’ve [created a branded tracking page](https://help.gomalomo.com/csc/build-with-the-malomo-tracking-page-creator) in your Malomo account before enabling the integration. Otherwise, your customers won’t be able to access tracking information via the “Track shipment” button.
- An estimated delivery date and progress bar is displayed (when available).
- Shipment status is updated based on tracking data from your provider’s event data to display 1 of the following statuses:
  - Ordered
  - Shipped
  - Out for Delivery
  - Delivered
- If there is a delay, return, or error, Customer Hub displays a descriptive status based on provider data.

  ![wonder2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38357500045723)

## Connect your order tracking provider

1. In Klaviyo, go to ****Customer Hub**** in the main navigation.
2. Select ****Extensions****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40774547199259)
3. Under **Order tracking**, toggle the switch on, then choose your provider from the dropdown:
   - ****Wonderment****
   - ****Malamo****
     ****![CHtrack1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39787027837851)****
4. Click ****Save****.

Customer Hub will now use the provider you selected for shipment tracking details.

## Fallback behavior

If Customer Hub cannot access data from Wonderment or Malamo for a specific order, it will automatically show tracking information from Shopify. This ensures your customers always see the latest available order status.

## Additional resources

- [How to show a help button on the orders tab in Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660636674843)
- [How to display product recommendations in Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660504643867)
- [How to connect your returns provider to Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660683592603)