---
id: "5379853359771"
title: "How to remove onsite tracking for Shopify"
source_url: "https://help.klaviyo.com/hc/en-us/articles/5379853359771-How-to-remove-onsite-tracking-for-Shopify"
section: "Shopify troubleshooting"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:03Z"
language: "en"
---
## You will learn

Learn how to remove Klaviyo onsite tracking from your Shopify store, which includes both **Active on Site** and **Viewed Product** tracking, and may also include **Viewed Collection**, **Submitted Search**, and **Added to Cart** tracking depending on your setup. For more context, read [our article about onsite tracking for Shopify](https://help.klaviyo.com/hc/en-us/articles/4425956184731).

## Before you begin

You may wish to remove onsite tracking for site speed performance reasons, though Klaviyo.js has recently been updated to [minimize its impact](https://klaviyo.tech/improving-forms-performance-c67c98114d49) in this regard. Note that Klaviyo’s Shopify app embed bypasses the website’s native tag manager and can result in faster loading of Klaviyo’s JavaScript. Additionally, we track some events via a Shopify Server Pixel (**Viewed Collection**, **Submitted Search**, and **Added to Cart**).

You can:

- Remove **Viewed Product** tracking
- Remove **Viewed Collection**, **Submitted Search**, and **Added to Cart** tracking
- Remove all onsite tracking

The first means you will not be able to track when someone views a product on your store, meaning you will not be able to send browse abandonment messages.

If you remove all onsite tracking, you will also no longer be able to use Klaviyo sign-up forms.

The guidance below around removing **Added to Cart** tracking refers to the Shopify-branded **Added to Cart** event synced via Shopify Server Pixel. If you wish to remove **Added to Cart** tracking that you enabled via a code snippet, check out [our guide](https://help.klaviyo.com/hc/en-us/articles/28709780787355).

## Remove Viewed Product tracking

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Shopify.****
3. Uncheck the **Track 'Viewed Product' events** setting.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28709107573275)
4. Click ****Update Settings****.

## Remove Viewed Collection, Submitted Search, and Added to Cart

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Shopify.****
3. Uncheck the **Track behavioral events** setting.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28709113412123)
4. Click ****Update Settings****.

## Remove all onsite tracking

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Shopify.****
3. Uncheck the **Track 'Viewed Product' events** and **Track behavioral events** settings.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28709113412123)
4. Click ****Update Settings****.
5. Click ****Edit**** next to **The Klaviyo app embed is enabled on your Shopify store** to be brought to Shopify.
6. Log in if prompted.
7. Toggle off the app embed.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28710075007131)
8. Click ****Save****.

## Outcome

You have now removed selected onsite tracking from your Shopify store.