---
id: "45224022467739"
title: "How to use Shopify Markets with Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/45224022467739-How-to-use-Shopify-Markets-with-Klaviyo"
section: "Getting started with Shopify"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:01Z"
language: "en"
---
## You will learn

Learn how to integrate Shopify Markets with Klaviyo to ensure your customers and product information, currency, and pricing from every region and language you sell in is synced into Klaviyo.

## Requirements

- You must have a Shopify store with [Shopify Markets](https://help.shopify.com/en/manual/international/managing) configured.
- Your Klaviyo account must be [integrated with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)

## Overview

If you use Shopify Markets to sell in multiple regions, you can use Klaviyo to message your customers in their preferred language and region, including pricing, currency, and URLs to the appropriate market.

Use Klaviyo to personalize across borders; sending the right language, currency, and product recommendations for every recipient with one template.

## How to enable Shopify Markets

1. In Klaviyo, select the Integrations tab.
2. Click Shopify to access the integration settings page.
3. In the Sync data from Shopify section, check Sync Shopify Markets to Klaviyo to start syncing your catalog data for every Market your storefront has. It will take time to initially sync all market catalogs
4. Save your integration settings.
5. If prompted, sign in to Shopify using the account you integrated with Klaviyo, and approve new access to sync Market data
6. Once you’ve returned to Shopify, select update integration.

![](https://klaviyo.zendesk.com/hc/article_attachments/45224022464283)

## What is synced

Klaviyo will sync locale information from Shopify profiles, events, and catalog data. Locale is a combination of language and region information. An English speaker located in the USA would have a locale of 'en-US' and a Spanish speaker in the USA would have a locale of ‘es-US’.

### Profiles

- Locale
  - The Locale property includes the profile’s locale synced from Shopify (e.g., “en-US”).
  - A Shopify synced profile may not always include language or region locale information if it is unknown by Shopify.

### Events

- Locale
  - All order related events from Shopify will include a locale. Details on each event with locale information can be found on the [Shopify data reference](https://help.klaviyo.com/hc/en-us/articles/115005080447).

### Catalog

- Locale
  - Each combination of region and language your storefront supports will be synced to Klaviyo for all products and variants on your catalog. This includes localized versions of the product and variant title, price, compare at price, status, currency, and URL.

## How to use locale aware Shopify Markets in Klaviyo

Once synced, locale data can be used across Klaviyo to power more personalized experiences for your customers.

### Smart Translations

With Shopify Markets in Klaviyo, Dynamic Product Blocks used in Smart Translations will automatically match your customers language and country with product information, currency, and pricing that match their preferences. When a product is not sold in a given country, that product will not be recommended to your customers in that country.

1. Within the Smart Translations editor, select a Fallback catalog locale. This will be used with the customers country is unknown
   1. A default Fallback catalog locale for each language can be configured from your account settings.
2. If you selected multiple languages to translate into, click the arrows at the top or use the dropdown to switch between languages.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/45224022465435)
3. When previewing the email, you are able to enter profiles of any locale to see examples of dynamic regionalization your customers will see

### Static Product Blocks

View the [full guide](https://help.klaviyo.com/hc/en-us/articles/115000219092) for using Static Product Blocks

For automatic localization, check the ****Localize for recipient**** checkbox in the block settings.

![](https://klaviyo.zendesk.com/hc/article_attachments/47692428749467)

When enabled, Static Product Blocks will automatically display localized product pricing, currency, and information based on the recipient's language and region at send time the same way that Dynamic Product Blocks work with Smart Translations. If a recipient's locale is unknown, the block will fall back to the default market configured in your Shopify store.

This eliminates the need to create separate Static Product Blocks for each region or rely on Smart Translations to handle pricing differences between regions that share a language (e.g., English-speaking customers in the US, UK, and Australia).

To manually select localized products:

1. From the Static Product Block selector, choose a locale aware catalog. For the Shopify integration, the catalog name is “Shopify: Default”
2. A language and region input will appear. Select the language and region of the products you’d like to include.
3. Select Add Products.

![](https://klaviyo.zendesk.com/hc/article_attachments/45224038988955)

### Catalog Look up Tags

View the [full guide](https://help.klaviyo.com/hc/en-us/articles/360004785571) for using catalog lookup tags

#### Filter by locale

Within the catalog tag there are two new filters for language and region. Locale language and region can be referenced with two letter country and language code using ISO 3166 and 639 standards. The regionalized version of the product includes values like title, price, and URL. This example shows a French Canadian version of a Shopify product.

```
{% catalog "SAMPLE_ITEM" integration='shopify' language='fr' region='CA' %}
{{ catalog_item.title }}
{% endcatalog %}
```

If a localized product can not be found the default product information will be used.

#### Currency template tags

The code and symbol for a localized product can be referenced with template tags. This example shows a reference to a currency symbol and currency code.

- currency\_symbol
  - The graphic symbol used to denote a currency unit
- currency\_code
  - The alphabetic code used to denote currency

```
{% catalog "SAMPLE_ITEM" integration='shopify' language='fr' region='CA' %}
{{ catalog_item.title }}
<a href="{{ catalog_item.url }}">
<img alt="Image of {{ catalog_item.title }}" src="{{ catalog_item.image_full_url }}" >
{{ catalog_item.currency_symbol }}
{{ catalog_item.price }}
{{ catalog_item.currency_code }}
{% endcatalog %}
```

### Segmentation with locale and Shopify Markets

With the Locale, Locale Language and Locale Country properties, you can segment your customers based on their Shopify Market.

****Use Case****

I want to segment my customers by those who speak Spanish language, regardless of what country they are in

****Solution****

Segment using Locale Language = ‘es’

****Use Case****

I want to segment my customers by those who have made a purchase in the UK, regardless of what language they speak

****Solution****

Segment using Locale Country = ‘GB’

****Use Case****

I want to segment my customers by those who have made a purchase in Belgium, and speak French

****Solution****

Segment using Locale = ‘fr-BE’

### Flows with locale and Shopify Markets

You can use this Locale information to personalize the content in your Flows. Most Shopify events will include Locale information in the event data that can be used in messages. Smart Translations can also be used to localize messages with product data.

Klaviyo has a set of prebuilt flow templates which will automatically reference the relevant currency and translated product information

- Add a localized [Abandoned Checkout Flow](https://www.klaviyo.com/flows/create?object_id=WvMGgv)
- Add a localized [Order Confirmation Flow](https://www.klaviyo.com/flows/create?object_id=Seu8ne)

## Troubleshooting

Why can I not enable Shopify Markets?

- Shopify Markets can only be enabled once per Shopify account. If your Shopify account is already enabled with Shopify markets on a separate Klaviyo account, you may turn off Shopify Markets on that account, then enable it on the the Klaviyo account you’d like
- Your Shopify account may be on an older version of Shopify Markets. You may enable the new version of Shopify Markets using [Shopify Test drive](https://help.shopify.com/en/manual/markets-new#markets-sp). Klaviyo recommends you reach out to Shopify before enabling the Shopify test drive.

  Why do I not see my Shopify B2B or Retail Markets?
- Klaviyo supports Shopify region markets and does not currently sync B2B or Retail Markets

  I don’t see my localized products in Klaviyo
- Depending on your catalog size, it may take multiple days for the initial sync of localized product data