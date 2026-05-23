---
id: 23730830399515
title: "Klaviyo Reviews metafields for Shopify reference"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/23730830399515-Klaviyo-Reviews-metafields-for-Shopify-reference"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:33Z"
language: en
---

## You will learn

Learn how to use metafields to customize Klaviyo Reviews content on your site. Metafields are Shopify’s tool for storing custom variables for use across your site, including on product pages.

This resource is intended for developers. Using Shopify metafields requires familiarity with [Liquid](https://www.shopify.com/partners/blog/115244038-an-overview-of-liquid-shopifys-templating-language), Shopify’s templating language. You can display reviews on your site without coding by using the [customizable review widgets](https://help.klaviyo.com/hc/en-us/articles/16691401577883).

Klaviyo Reviews metafields for Shopify are enabled by default. Metafields are not available for WooCommerce.

## About review metafields

Inserting metafields directly into a product page will display the variable stored within the metafield. If you add {{ product.metafields.reviews.rating.value }} to your product page, and that product’s rating is 4.7, “4.7” will appear in place of the metafield upon page load.

You can also use metafields for more complex work, including:

- Allowing other Shopify apps to access and use Klaviyo Reviews data on your site.
- Dynamically display content for products with certain ratings using conditionals.
- Code your own star rating display, rather than using the Klaviyo Reviews star rating widget.

In your **Shopify Product metafields definitions** page, the Klaviyo Reviews metafields are named **Product rating count** and **Product rating**.

## Add review metafields with the theme editor

If your [theme supports adding metafields](https://help.shopify.com/en/manual/online-store/themes/theme-structure/sections-and-blocks#metafields-and-dynamic-sources), use the dynamic source icon to add reviews metafields. Adding reviews metafields with the theme editor is supported in the product info section of a product page.

1. Navigate to a product page.
2. Open (or add) a field that supports text.
3. Select the dynamic source icon.
   ![The dynamic image icon](https://klaviyo.zendesk.com/hc/article_attachments/30241810707099)
4. Select a reviews metafield.
   ![Reviews metafields options](https://klaviyo.zendesk.com/hc/article_attachments/30241810710299)
5. Click ****Save****.

## Add review metafields with custom liquid

The following metafields can be used on product pages and within product objects (e.g., within a product tile on a collection page). They are not supported outside of product objects (e.g., your **About** page).

|  |  |  |
| --- | --- | --- |
| ****Metafield**** | ****Content**** | ****Data type**** |
| {{ product.metafields.reviews.rating.value }} | A product’s average rating. | Float (e.g., 3.5, 4.7) |
| {{ product.metafields.reviews.rating\_count }} | The number of ratings submitted for a product. | Integer (e.g., 10, 45, 721) |
| {{ product.metafields.reviews.rating.scale\_min }} | The lowest possible rating (i.e., 1). | Integer; always 1 |
| {{ product.metafields.reviews.rating.scale\_max }} | The highest possible rating (i.e., 5). | Integer; always 5 |

## Disable review metafields

Review metafields are enabled by default. To disable metafields:

1. Navigate to the ****Reviews**** tab in Klaviyo.
2. Select ****Reviews settings****.
3. Select ****General****.
4. Under **Shopify**, toggle off the setting labeled **Sync review metafields to Shopify**.
5. Click ****Save changes****.