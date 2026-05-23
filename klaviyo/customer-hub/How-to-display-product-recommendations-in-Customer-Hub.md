---
id: 33660504643867
title: "How to display product recommendations in Customer Hub"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/33660504643867-How-to-display-product-recommendations-in-Customer-Hub"
section: "Build and use Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:56:48Z"
language: en
---

## You will learn

Learn how to display personalized product recommendations in the Customer Hub drawer to tailor shopping experiences for your customers and drive conversions. By showing products that appeal to customers, you can improve conversion rates and provide cross-sell opportunities to increase average order value.

Customer Hub for Shopify currently supports standard storefronts and Shopify Headless. For WooCommerce, navigate to https://help.klaviyo.com/hc/en-us/articles/47792369863451

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

This guide explains how to activate product recommendations so they display in the Customer Hub drawer on your site. Before proceeding, ensure that the [Customer Hub feature is enabled](https://klaviyo.com/try-service).

[Learn more about Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660324811675).

## About product recommendations

When enabled, product recommendations display on the **For you** tab of the Customer Hub drawer on your site. These recommendations are tailored based on both the shopper’s behavior on your site and the shopper’s history within Klaviyo, increasing their likelihood of purchasing.

![A Customer Hub drawer open on an example brand's website showing the Recommended products section highlighted.](https://klaviyo.zendesk.com/hc/article_attachments/34194267469339)

For any signed-in shopper, Klaviyo analyzes their browsing history (i.e., viewed products) and past purchases from your Shopify site in order to surface relevant product recommendations.

Up to 5 recommended products are shown in an image carousel in the **Recommended products** section below your other content blocks. Within a product recommendation block, a shopper can:

- View product details, including item name, price, and size (if applicable).
- Add the item to their cart.
- Add the item to their favorites, if [**Favorites** are enabled](https://klaviyo.zendesk.com/hc/en-us/articles/33660543083419).

Shoppers can click the arrow next to the **Recommended products** section to view these items in a list view as well.

![The list view of the recommended products section in the Customer Hub interface.](https://klaviyo.zendesk.com/hc/article_attachments/34194267478171)

These products update over time based on a shopper’s activity. Note that product recommendation models are [generally trained once every 7 days](https://help.klaviyo.com/hc/en-us/articles/115005082787#h_01HA7KGGHEDAPZQZSZJJFMCX5H), depending on use. It may take a few days for the recommendation model to consider brand-new events.

If Klaviyo does not have data to determine personalized recommendations, it shows customers your best selling products from the last 90 days.

## Enable product recommendations

1. In Klaviyo’s left-hand navigation, select ****Service -**** ****Customer Hub****.
2. Select ****Extensions****.
3. Under **Product recommendations**, check the box to ****Enable product recommendations****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40774228685979)
4. Click ****Save****.

Once live, when someone clicks on a product recommendation, Klaviyo logs a **Customer Hub Clicked Recommended Product** event. You can build segments based on this metric to send targeted, behavior-driven marketing.

## Exclude certain products from recommendations

You may want to prevent certain items from appearing in the **Product recommendations**view in Customer Hub, like free gifts, shipping insurance, or out-of-stock items.

Klaviyo provides a tag, **klaviyo\_hub\_recommendation\_exclude**, which you can apply to products in Shopify that you wish to exclude. Keep in mind that products a customer has already purchased are automatically excluded from their product recommendations.

To exclude a specific product:

1. Navigate to a product page in your Shopify admin.
2. In the **Tags** field on the right, add the tag **klaviyo\_hub\_recommendation\_exclude**.
   ![The Tags field in Shopify showing the klaviyo_hub_recommendation_exclude tag added.](https://klaviyo.zendesk.com/hc/article_attachments/34972804300699)
3. Click ****Save****.

After saving this change, the product will no longer appear in product recommendations for any customer in the Customer Hub interface.

It may take up to 30 minutes for the product to be removed from product recommendations.

## Revenue attribution for product recommendations

If a shopper adds something from the **Product recommendations** section to their cart, then places an order, Klaviyo attributes the revenue for that item to Customer Hub.

This data is viewable in the **Revenue generated** column of the [Customer Hub dashboard](https://www.klaviyo.com/customer-hub/dashboard).

## Additional resources

- [Understanding the Customer Hub overview dashboard](https://help.klaviyo.com/hc/en-us/articles/33660382797595)
- [How to display favorited items in Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660543083419)
- [How to add content blocks to Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660517680795)