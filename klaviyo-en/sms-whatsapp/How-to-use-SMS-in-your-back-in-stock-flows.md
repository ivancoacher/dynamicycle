---
id: 7954040204827
title: "How to use SMS in your back in stock flows"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/7954040204827-How-to-use-SMS-in-your-back-in-stock-flows"
section: "Revenue-generating SMS flows"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:05Z"
language: en
---

## You will learn

Learn how to use SMS in your back in stock flows with Klaviyo.

By adding an SMS to your back in stock flow, you can immediately alert subscribers about products they’re interested in. Back in stock messages create a sense of urgency, prompting your recipients to buy as soon as they get the text. Text messages are typically read within 3 minutes and are seen much quicker than emails, making them the best option for back in stock messages.

## Before you begin

Before you add SMS to your back in stock flows, note the following:

- You must have already [turned on SMS](https://help.klaviyo.com/hc/en-us/articles/4404274419355) in your Klaviyo account.
- Individuals must be current SMS subscribers to receive text messages from a back in stock flow
- SMS back in stock flows are only available for Shopify, BigCommerce, PrestaShop, and Magento 2 stores, as well as stores with inventory-aware catalogs synced via custom catalog feed or API.
- You must have set up back in stock for your ecommerce store:
  - [Shopify back in stock instructions](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
  - [BigCommerce back in stock instructions](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
  - [PrestaShop back in stock instructions](https://help.klaviyo.com/hc/en-us/articles/33059375555099)
  - [Magento 2 back in stock](https://developers.klaviyo.com/en/docs/set-up-back-in-stock-for-magento-2)
  - [Custom catalog feeds back in stock](https://developers.klaviyo.com/en/docs/how-to-enable-back-in-stock-for-custom-catalog-feeds)
  - [API back in stock](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)
- Limit the number of text messages in your back in stock flow to 1 or 2 SMS.

## Use SMS in your back in stock flows

There are 2 options for using SMS in your back in stock flows:

- Use SMS and email together in a flow (recommended)
- Make a separate, SMS-only back in stock flow

  These options have a similar setup; the main differences are that:
- The first method is more omnichannel, and it will be easier to analyze how your audience responds to SMS versus email
- For SMS-only flows, you need to configure the [back in stock flow’s settings](https://help.klaviyo.com/hc/en-us/articles/115003872251) (e.g., minimum inventory and customer notification rules)

Since the omnichannel approach is easier to maintain, analyze, and improve, we only go over that approach in this article.

### Add SMS into a back in stock flow

1. Navigate to the ****Flows**** tab.
2. Either:
   1. Locate your existing back in stock flow (if you made one previously).
   2. Search for a back in stock flow template:
      1. Click ****Create flow****
      2. Search “back in stock”
      3. Select one of the back in stock flows
      4. Name the flow in the modal
      5. Click ****Use template****
3. Add a conditional split after the Back in Stock Delay.
   ![A conditional split placed directly below the Back in Stock delay](https://klaviyo.zendesk.com/hc/article_attachments/28715964512667)
4. Set the split to **If someone can or cannot receive marketing > cannot receive > SMS marketing**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33955881875483)
5. Click ****Save**** for the conditional split.
6. Drag an SMS message onto the **No** path.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33955881878427)
7. Select the SMS and next to **Content**, click ****Edit .****
8. Add in your content:

   - Example: “[Name of item] is back in stock! Grab yours before they’re gone again:
     - To dynamically insert the name of the product, you must use an event variable. Check out this article for instructions on [finding event variables and examples.](https://help.klaviyo.com/hc/en-us/articles/115002779071)![](https://klaviyo.zendesk.com/hc/article_attachments/33955910919067)
9. After the text, insert catalog tags for the item that’s back in stock.

   - Note: catalog tags are specific to your integration; for examples, click on the name of your ecommerce platform below:

****BigCommerce****

|  |  |
| --- | --- |
| ****Product Detail**** | ****Dynamic Event Variable (BigCommerce Stores)**** |
| **Product Title** | {% catalog event.VariantId integration='bigcommerce' %} {{ catalog\_item.title }} {% endcatalog %} |
| **Variant Image** | {% catalog event.VariantId integration='bigcommerce' %} {{ catalog\_item.variant.featured\_image.full.src|default:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
| **Product URL** | {% catalog event.VariantId integration='bigcommerce' %}{{ catalog\_item.url }}{% endcatalog %} |
| **Product Price** | {% catalog event.VariantId integration='bigcommerce' %}{% currency\_format catalog\_item.metadata.price|floatformat:2 %}{% endcatalog %} |
| **Variant Title** | {% catalog event.VariantId integration="bigcommerce" %} {{ catalog\_item.variant.title }} {% endcatalog %} |
| **Variant URL** | {% catalog event.VariantId integration='bigcommerce' %}{{ catalog\_item.url }}?variant={{ catalog\_item.variant.id }}{% endcatalog %} |

- ****Shopify****

  |  |  |
  | --- | --- |
  | ****Product Detail**** | ****Dynamic Event Variable (Shopify Stores)**** |
  | **Product Title** | {% catalog event.VariantId integration='shopify' %} {{ catalog\_item.title }} {% endcatalog %} |
  | **Variant Image** | {% catalog event.VariantId integration='shopify' %} {{ catalog\_item.variant.featured\_image.full.src|default:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
  | **Product URL** | {% catalog event.VariantId integration='shopify' %}{{ catalog\_item.url }}{% endcatalog %} |
  | **Product Price** | {% catalog event.VariantId integration='shopify' %}{% currency\_format catalog\_item.variant.price|floatformat:2 %}{% endcatalog %} |
  | **Variant Title** | {% catalog event.VariantId integration="shopify" %} {{ catalog\_item.variant.title }} {% endcatalog %} |
  | **Variant URL** | {% catalog event.VariantId integration='shopify' %}{{ catalog\_item.url }}?variant={{ catalog\_item.variant.id }}{% endcatalog %} |
- ****Magento 2****

|  |  |
| --- | --- |
| ****Product Detail**** | ****Dynamic Event Variable (Magento 2 Stores)**** |
| **Product Title** | {% catalog event.VariantId integration='magento\_two' %} {{ catalog\_item.title }} {% endcatalog %} |
| **Variant Image** | {% catalog event.VariantId integration='magento\_two' %} {{ catalog\_item.variant.featured\_image.full.src|default:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
| **Product URL** | {% catalog event.VariantId integration='magento\_two' %}{{ catalog\_item.url }}{% endcatalog %} |
| **Product Price** | {% catalog event.VariantId integration='magento\_two' %}{% currency\_format catalog\_item.variant.price|floatformat:2 %}{% endcatalog %} |
| **Variant Title** | {% catalog event.VariantId integration="magento\_two" %} {{ catalog\_item.variant.title }} {% endcatalog %} |
| **Variant URL** | {% catalog event.VariantId integration='magento\_two' %}{{ catalog\_item.url }}?variant={{ catalog\_item.variant.id }}{% endcatalog %} |

1. Click ****Preview & test**** to test the back in stock SMS.
2. Once you confirm that the back in stock message appears as expected, click ****Save & continue**** in the upper right.
3. Select ****Update Action Statuses****.
4. Choose ****Live**** from the dropdown and then click ****Update****.

![Modal to update all flow action statuses when Live is selected](https://klaviyo.zendesk.com/hc/article_attachments/28715971073051)

## Outcome and next steps

You can now send back in stock flow messages via SMS.

### Optimizing the flow

We recommend keeping an eye on how your audience responds to these messages, as it’s important to make sure you’re seeing high engagement.

If engagement is low, test whether your audience prefers email or SMS. Each business is unique, and so is their audience. Your audience may prefer to receive back in stock alerts via email rather than SMS.