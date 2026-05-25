---
id: "33660687711771"
title: "How to connect Gorgias to Customer Hub"
source_url: "https://help.klaviyo.com/hc/en-us/articles/33660687711771-How-to-connect-Gorgias-to-Customer-Hub"
section: "Integrate other platforms with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:39Z"
language: "en"
---
## You will learn

Learn how to enable Gorgias in Customer Hub so your customers can access Gorgias help channels directly from Customer Hub. Connecting Customer Hub and Gorgias empowers your customers to quickly and easily get the help they need for order-releated inquiries and issues.

Customer Hub for Shopify currently supports standard storefronts and Shopify Headless. For WooCommerce, navigate to https://help.klaviyo.com/hc/en-us/articles/47792369863451

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

This guide explains how to connect Gorgias and Customer Hub. Before proceeding, ensure that the [Customer Hub feature is enabled](https://klaviyo.com/try-service).

To use Gorgias and Customer Hub together, you must have:

1. [Gorgias installed on your Shopify store](https://docs.gorgias.com/en-US/shopify-101-81814).
2. [Integrated Gorgias and Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/4408023789083).
   - Check to see if you have a Gorgias integration on your [Integrations page in Klaviyo](https://www.klaviyo.com/integrations).

## How Gorgias and Customer Hub work together

When an authenticated shopper (meaning someone who has signed in to their account on your site) opens the Customer Hub drawer on your site, a summary of their recent Shopify order history displays on the **Orders** tab. They can also click on an order to view additional details and a menu of self-service help options for the order (e.g., buy again, tracking, etc.), which sync from Shopify and display by default.

In your Customer Hub settings in Klaviyo, you can choose to additionally enable a “Get help” button to display on order details pages, and connect it to Gorgias. This allows you to direct customers from the Customer Hub interface to a Gorgias support channel (live chat or ticket submission), based on your business hours or how you manage your support system in Gorgias.

![The Customer Hub drawer open on an example site and showing an order details view with the Get help button visible.](https://klaviyo.zendesk.com/hc/article_attachments/34197332785947)

****Note:**** Gorgias web chat cannot be embedded or integrated within Customer Hub. The "Get help" button is the only way to connect users to Gorgias from Customer Hub.

##

## Enable Gorgias in Customer Hub

To enable the “Get help” button and connect it to Gorgias, configure your Customer Hub support settings:

1. In Klaviyo’s left-hand navigation, select ****Customer Hub****.
2. Select ****Settings****.
3. Choose the ****Extensions**** tab in the menu bar.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40774490077211)
4. Under **Help settings**, select ****Gorgias****. You need to have integrated [Gorgias and Klaviyo](https://help.smile.io/en/articles/4036196-klaviyo-and-smile) to enable this setting. Note that if you have not yet integrated with Gorgias, you will see a prompt to do so and a **Not active** badge.
   ![CHgorgias100.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39338001635867)
5. Click ****Save****.

Once enabled, Klaviyo will monitor your Gorgias settings to identify the days, times, and channels your support representatives are available. This allows a dynamic button to be displayed in Customer Hub which, when clicked, opens the Gorgias widget to the correct support channel.

The support channel displayed is based on your business hours and the support channels that are available. Note that the text on these buttons is not currently editable:

- During your business hours, a “Start a live chat” button appears and directs users to live chat.
- Outside of business hours, a “Leave a message” button appears and directs users to a ticket submission menu. If you don’t offer live chat, this button will always be visible.

Customer Hub automatically inherits business hours changes from Gorgias. If you remove Gorgias from your site in the future, you’ll need to adjust your [help settings](https://klaviyo.zendesk.com/hc/en-us/articles/33660636674843) to use a different support option.

If you have a hub launcher enabled for your Customer Hub, be sure to [adjust the hub widget's positioning in Design settings](https://klaviyo.zendesk.com/hc/en-us/articles/33660482389659) so it doesn’t overlap with the Gorgias widget in the lower-right corner.

## Additional resources

- [Getting started with Gorgias](https://help.klaviyo.com/hc/en-us/articles/4408023789083)
- [Getting started with Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660324811675)
- [Getting started with web chat](https://help.klaviyo.com/hc/en-us/articles/33660391549211)