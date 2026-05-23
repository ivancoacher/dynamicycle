---
id: 14477037350299
title: "How to enable PrestaShop price include VAT"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/14477037350299-How-to-enable-PrestaShop-price-include-VAT"
section: "PrestaShop"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T11:01:11Z"
language: en
---

## You will learn

Learn how to include VAT (tax) in your PrestaShop store’s listed prices and sync tax-included price data to Klaviyo. Your PrestaShop price data will sync with your Klaviyo product catalog, as well as **Viewed Product** and **Added to Cart** events.

To begin syncing VAT inclusive price data, you can update your integration [manually](https://help.klaviyo.com/hc/en-us/articles/14477037350299#manually-update-existing-prestashop-integrations3) or with the help of [Klaviyo support](https://help.klaviyo.com/hc/en-us/articles/14477037350299#support-assisted-update-existing-prestashop-integrations4).

## Before you begin

When you are re-integrating or updating your integration, you must install Klaviyo module version 1.2.10 or greater to sync VAT inclusive price data. We strongly encourage you to upgrade your PrestaShop module to version 1.4.1 or higher before June 30th, 2024, due to the [retirement of our v1/v2 APIs](https://help.klaviyo.com/hc/en-us/articles/360054551492#h_01HD6YRW7VWJQKBXTN7TGA7N88). Upgrading to version 1.4.1 or higher will let you take advantage of coupon generation and a real-time transactional event sync, which were first released on 1.3.0.

## Enable VAT included prices

### Manually update existing PrestaShop integrations

1. Remove the PrestaShop integration from within Klaviyo.
2. Remove and uninstall the Klaviyo module from within PrestaShop.
3. Update any email templates as necessary, for example, anywhere a multiplier was applied to the item price should be removed.
4. Re-integrate PrestaShop with Klaviyo, following our [Getting started with PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360054551492) guide. Make sure to install Klaviyo module version 1.2.10 or greater to sync VAT inclusive price data.

### Support-assisted update existing PrestaShop integrations

1. Turn off any flows and campaigns where the message refers to item price data from your product catalog, for example, any product blocks.
2. Update any email templates as necessary, for example, anywhere a multiplier was applied to the item price should be removed.
3. Update the Klaviyo module to version 1.2.10 or greater.
4. [Contact Klaviyo Support](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272) for assistance with backfilling your existing product catalog products with the tax-included price.
5. Your support representative will reach out when the backfill of the product catalog with VAT inclusive prices is completed.
6. Re-enable any flows and campaigns where the message refers to item price data from your product catalog.

## VAT inclusive price data

### Event data

After your integration is set up or updated with version 1.2.10 or greater, the VAT-inclusive price fields below will be included in your Viewed Product and Added to Cart events.

Viewed Product: `PriceInclTax`

Added to Cart: `AddedItemPriceInclTax`

These additional price fields will only be effective going forward. The VAT fields will not backfill in existing Viewed Product and Added to Cart events.

### Catalog data

All Prestashop integrations created after January 25, 2023 using a Klaviyo module version 1.2.10 or greater will sync the VAT **inclusive** price from PrestaShop into your product catalog.

All Prestashop integrations created before January 25, 2023 sync the VAT **exclusive** price into your product catalog.

## Outcome

Congratulations! You have successfully updated your PrestaShop integration to use VAT price included data in your product catalog. Your **Added to Cart** and **Viewed Product** events will capture VAT price included data moving forward.

## Additional resources

- [Getting started with PrestaShop](https://klaviyo.zendesk.com/hc/en-us/articles/360054551492)
- [PrestaShop data reference](https://klaviyo.zendesk.com/hc/en-us/articles/360055123191)