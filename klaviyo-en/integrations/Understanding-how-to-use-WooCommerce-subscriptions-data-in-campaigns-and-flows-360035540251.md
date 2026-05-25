---
id: "360035540251"
title: "Understanding how to use WooCommerce subscriptions data in campaigns and flows"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360035540251-Understanding-how-to-use-WooCommerce-subscriptions-data-in-campaigns-and-flows"
section: "WooCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:52Z"
language: "en"
---
## You will learn

Learn how WooCommerce subscription data can be used in Klaviyo to trigger flows geared towards subscribers and create campaigns that target subscribers. WooCommerce offers a WooCommerce Subscription plugin that can be used to manage subscriptions.

You can enable the [WooCommerce subscription plugin](https://woocommerce.com/products/woocommerce-subscriptions/) from the WooCommerce Extensions Store.

## Sync WooCommerce subscriptions to Klaviyo

[Tribe](https://www.madebytribe.com/) has developed a plugin that will integrate Wordpress Subscriptions with Klaviyo so that you can send custom events to Klaviyo when a WooCommerce subscription is purchased or cancelled.

Tribe deprecated their free WooCommerce Subscriptions plugin in January 2021. To continue, head over to their new [premium WooCommerce Subscriptions plugin](https://www.madebytribe.com/products/klaviyo-toolkit/). You'll need your [Klaviyo public API key/site ID](https://help.klaviyo.com/hc/en-us/articles/115005062267) to activate the plugin.

## Data synced to Klaviyo

Tribe's plugin syncs the following data from WooCommerce Subscriptions to Klaviyo:

- Subscription price
- Subscription plan name
- Subscription trials
- Subscription plan id

This is an example of profile data which is synced into Klaviyo by the Tribe plugin:
![WooCommerce subscription information in Klaviyo metrics](https://klaviyo.zendesk.com/hc/article_attachments/28723541915675)

## Create a campaign using WooCommerce subscriptions data

WooCommerce Subscriptions metrics can be used to segment customers and target them in a specific campaign. For example, create a segment of customers who have **Subscribed to Plan where PlanID = 1066**.

![A segment relying on WooCommerce subscription data](https://klaviyo.zendesk.com/hc/article_attachments/28723519994139)

Create a campaign targeting this segment of customers. For example, if your subscription Plan1099 is a semi-monthly subscription for biodegradable toilet paper, send customers recently subscribed to Plan1066 a product launch campaign for your new biodegradable cleaning products line.

## Create a flow using WooCommerce subscriptions data

You can use any WooCommerce Subscriptions metric to trigger a flow in Klaviyo. For example, you could use the **Subscribed to Plan** metric to trigger a "Welcome Subscriber" flow in Klaviyo.

## Additional resources

- [Getting started with WooCommerce](https://klaviyo.zendesk.com/hc/en-us/articles/115005255808)
- [WooCommerce data reference](https://klaviyo.zendesk.com/hc/en-us/articles/360030732832)