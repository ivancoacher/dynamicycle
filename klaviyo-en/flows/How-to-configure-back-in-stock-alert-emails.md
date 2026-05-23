---
id: 360051612751
title: "How to configure back in stock alert emails"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360051612751-How-to-configure-back-in-stock-alert-emails"
section: "Back in stock flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:51Z"
language: en
---

## You will learn

Learn how to use pre-built templates or configure a custom template for a back in stock flow email. When creating a back in stock flow email, it's important to set up the message so that it shows the right product data. Klaviyo supports back in stock flows for accounts with Shopify, BigCommerce, Magento 2, PrestaShop, Shopware, and SFCC integrations, as well as accounts with inventory-aware catalogs sync via custom catalog feed or API. The instructions below cover Shopify, BigCommerce, and Magento 2 integrations.

If you are using a custom integration, learn [how to set up back in stock via API](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock).

## Before you begin

Before you configure back in stock emails for your back in stock flows, you must have set up back in stock for your ecommerce store:

- [Shopify back in stock instructions](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
- [BigCommerce back in stock instructions](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
- [PrestaShop back in stock instructions](https://help.klaviyo.com/hc/en-us/articles/33059375555099)
- [Magento 2 back in stock](https://developers.klaviyo.com/en/docs/set-up-back-in-stock-for-magento-2)
- [Custom catalog feeds back in stock](https://developers.klaviyo.com/en/docs/how-to-enable-back-in-stock-for-custom-catalog-feeds)
- [API back in stock](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)

## Use pre-built templates

The pre-built back in stock flows you'll find in the Flow Library come configured with default email content. If you've built your own flow, to help get you started, you will find a pre-built back in stock email template in the **Email templates** tab. Simply search "back in stock" when configuring your stock alert email.

## Create your own back in stock email

To configure your email content, you will need to use a specific set of dynamic event variables. Given it may be days, weeks, or even months before an item is restocked, we realize that details about the item (for example, images or price) may change. For this reason, Klaviyo uses a special set of dynamic event variables for this email that will look up the restocked product in your catalog at send time and populate the most up-to-date details available.

Note that the table block within the email template must be set to static, not dynamic, in order to function.

### Shopify stores

|  |  |
| --- | --- |
| ****Product Detail**** | ****Dynamic Event Variable (Shopify Stores)**** |
| **Product Title** | {% catalog event.VariantId integration='shopify' %} {{ catalog\_item.title }} {% endcatalog %} |
| **Product URL** | {% catalog event.VariantId integration='shopify' %}{{ catalog\_item.url }}{% endcatalog %} |
| **Product Price** | {% catalog event.VariantId integration='shopify' %}{% currency\_format catalog\_item.variant.price|floatformat:2 %}{% endcatalog %} |
| **Variant Image** | {% catalog event.VariantId integration='shopify' %} {{ catalog\_item.variant.featured\_image.full.src|default:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
| **Variant Title** | {% catalog event.VariantId integration="shopify" %} {{ catalog\_item.variant.title }} {% endcatalog %} |
| **Variant URL** | {% catalog event.VariantId integration='shopify' %}{{ catalog\_item.url }}?variant={{ catalog\_item.variant.id }}{% endcatalog %} |

### BigCommerce stores

If you are having an issue with incorrect items appearing in your BigCommerce back in stock emails, it could be caused by some of your products having a VariantID that matches another item's ProductID in BigCommerce. To solve this, replace VariantID with ProductID when using the dynamic event variables below in your emails. Making this replacement should solve the incorrect item issue, though variant-specific information will no longer be shown.

|  |  |
| --- | --- |
| ****Product Detail**** | ****Dynamic Event Variable (BigCommerce Stores)**** |
| **Product Title** | {% catalog event.VariantId integration='bigcommerce' %} {{ catalog\_item.title }} {% endcatalog %} |
| **Product URL** | {% catalog event.VariantId integration='bigcommerce' %}{{ catalog\_item.url }}{% endcatalog %} |
| **Product Price** | {% catalog event.VariantId integration='bigcommerce' %}{% currency\_format catalog\_item.metadata.price|floatformat:2 %}{% endcatalog %} |
| **Variant Image** | {% catalog event.VariantId integration='bigcommerce' %} {{ catalog\_item.variant.featured\_image.full.src|default:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
| **Variant Title** | {% catalog event.VariantId integration="bigcommerce" %} {{ catalog\_item.variant.title }} {% endcatalog %} |
| **Variant URL** | {% catalog event.VariantId integration='bigcommerce' %}{{ catalog\_item.url }}?variant={{ catalog\_item.variant.id }}{% endcatalog %} |

### Magento 2 stores

|  |  |
| --- | --- |
| ****Product Detail**** | ****Dynamic Event Variable (Magento 2 Stores)**** |
| **Product Title** | {% catalog event.VariantId integration='magento\_two' %} {{ catalog\_item.title }} {% endcatalog %} |
| **Product URL** | {% catalog event.VariantId integration='magento\_two' %}{{ catalog\_item.url }}{% endcatalog %} |
| **Product Price** | {% catalog event.VariantId integration='magento\_two' %}{% currency\_format catalog\_item.variant.price|floatformat:2 %}{% endcatalog %} |
| **Variant Image** | {% catalog event.VariantId integration='magento\_two' %} {{ catalog\_item.variant.featured\_image.full.src|default:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
| **Variant Title** | {% catalog event.VariantId integration="magento\_two" %} {{ catalog\_item.variant.title }} {% endcatalog %} |
| **Variant URL** | {% catalog event.VariantId integration='magento\_two' %}{{ catalog\_item.url }}?variant={{ catalog\_item.variant.id }}{% endcatalog %} |

### Example

Here's what a template will look like inside the Template Builder with dynamic event variables, with a comparison of what this same template will look like when previewed with real event data:

![An example of a content block with the image and text using dynamic event variables next to the same block populated with content in a preview](https://klaviyo.zendesk.com/hc/article_attachments/28717811792795)

## Additional resources

Check out other articles on back in stock flows

- [How to create a back in stock flow](https://help.klaviyo.com/hc/en-us/articles/115003872251)
- [Understanding how back in stock flows work](https://help.klaviyo.com/hc/en-us/articles/360051612551)
- [How to use SMS in a back in stock flow](https://help.klaviyo.com/hc/en-us/articles/7954040204827)

Learn more about dynamic variables in [Personalize flow emails with dynamic event data](https://help.klaviyo.com/hc/en-us/articles/115002779071)