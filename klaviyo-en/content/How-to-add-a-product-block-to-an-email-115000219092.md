---
id: "115000219092"
title: "How to add a product block to an email"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115000219092-How-to-add-a-product-block-to-an-email"
section: "Build and use products "
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:56:35Z"
language: "en"
---
## You will learn

Learn how to insert a product block into Klaviyo emails in order to dynamically show your best-selling or most popular products.

Product blocks do not support any custom HTML. If you want to custom code your product block, you'll need to use an HTML template and manually insert product information. Product blocks can display unique items from your catalog, and selects item based on the product level, not the variant level. Individual variants cannot be selected in product blocks.

The product block feature is available by default for the ecommerce platforms listed in our article [How to use product feeds and recommendations](https://help.klaviyo.com/hc/en-us/articles/115005082787-How-to-Use-Product-Feeds-and-Recommendations). If you use an ecommerce platform that is not listed there, you'll need to sync your product catalog into Klaviyo by following our guide, [Sync a custom catalog feed to Klaviyo](https://developers.klaviyo.com/en/docs/guide-to-syncing-a-custom-catalog-feed-to-klaviyo).

## Add a product block to an email

1. Open the email where you want to insert a product block.
2. Drag a product block into your email.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34829029970587)
3. Choose a product block type:

   - ****Dynamic****
     Dynamic product blocks show products based on business trends (e.g., best-sellers in the last 90 days) or customized to each recipient based on what Klaviyo predicts they will be most interested in. Learn how to create a dynamic product feed below.
   - ****Static****
     Static product blocks show a set list of items that you select.
4. Fill out the additional fields that appear based on your selection.

### Create a dynamic product feed

1. After dragging and configuring your product block, choose ****Dynamic**** as your product feed type.
2. Click ****Create product feed****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34829073480731)
3. Create a descriptive name for your product feed, like RECENTLY\_VIEWED\_PRODUCTS. Note that spaces (and other special characters) are not permitted in product feed names.
4. Set the criteria for your product feed. You can choose to show products based on overall performance (e.g., best-selling products) or recipient behavior (e.g., recently viewed items). Learn more about [product feed settings](https://help.klaviyo.com/hc/en-us/articles/115005082787-How-to-use-product-feeds-and-recommendations).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34829029974427)
5. Click ****Create product feed****.
6. Fill out the additional fields that appear.

To edit a product feed after you’ve created it, navigate to ****Content > Products > Product feed****. Then, select your feed and edit it.

This option is great for automated email flows, as it reduces the need to edit your messages frequently. With product feeds, you can curate the right items to feature based on your feed's definition, so your most popular and trending items will be included in your flow emails even as trends shift.

For Magento and Shopify stores, if a product goes out of stock, we'll hide it from your catalog so it won't appear in any feed.

When you choose a feed and save all your settings, you will still see placeholder items in your template. If you are editing your template as a draft campaign or within a flow, you can preview your email in Klaviyo to see the feed populate with real items from your catalog.

### Manually select products from your catalog

For different email campaigns, you may want to hand-pick the right products to feature in a given template. Within the product block, select the ****Static**** option, then click ****Add products****. Here, you can browse your entire product catalog and pick up to nine items to feature in your template.

![](https://klaviyo.zendesk.com/hc/article_attachments/34829073488539)

If you manually select products for a message that won't send right away (i.e., a flow email or a campaign scheduled for a future date), the item details will not update dynamically at send time, even if you make edits to the product details on your site. If you would like the products to update dynamically, first create a feed containing those items, then use the ****Dynamic**** option to display them.

When you’ve selected one or more items, click ****Add products****.

If you use custom descriptions, we recommend keeping each description under 120 characters. Keep your descriptions for each item a similar length to avoid alignment issues with this block in your email. Custom descriptions are only supported for static product feeds.

If you are using locale aware catalogs with Shopify Markets enabled, a ****Localize for recipient**** checkbox will appear in your Static product Block settings.

![](https://klaviyo.zendesk.com/hc/article_attachments/47692381022235)

When ****Localize for recipient**** is enabled, the products in your Static Product Block will automatically display localized pricing, currency, and product information that matches each recipient's language and region at send time. This means a single email can show USD pricing to a recipient in the United States, GBP pricing to a recipient in the United Kingdom, and AUD pricing to a recipient in Australia without creating separate emails or product blocks for each market.

If locale data is not available for a recipient, the product block will fall back to the default market configured in your Shopify store.

You can uncheck ****Localize for recipient**** if you want all recipients to see the same product information regardless of their region. You can manually select localized versions of your products with localized product information including title, price and URL by choosing a language and region when adding products to the block.

![](https://klaviyo.zendesk.com/hc/article_attachments/45236420399771)

After you select one or more products to feature, you may want to re-arrange how the items appear in your template. Drag the items in the product block settings to reorder them.

![productblockmove2gif.gif](https://klaviyo.zendesk.com/hc/article_attachments/34829029985691)

## Style a product block

To adjust the appearance of a product block, head to that block's ****Styles**** tab. Here, you can choose which product details appear (e.g., product name, price, original price for sale products, etc.) and how they are styled, including font style, size, and color.

![](https://klaviyo.zendesk.com/hc/article_attachments/34829029990299)

### Original price for sale products

Within a product block's **Styles** tab, check the setting ****Original price for sale products**** to display the original price with a strike-through next to the sale price.

![](https://klaviyo.zendesk.com/hc/article_attachments/34829029992219)

Please note that this setting is only available for customers using Shopify, BigCommerce, WooCommerce, and PrestaShop. The original price is detected automatically for both dynamic and static product blocks. You can style the original price in the product block separate from styling the price.

![](https://klaviyo.zendesk.com/hc/article_attachments/34829073497883)

## Show a product's rating

In the **Styles** tab, you can also choose to display the average rating and amount of ratings a product has received. This requires that you enable Klaviyo Reviews. Learn [how to show product ratings in emails with a product block](https://klaviyo.zendesk.com/hc/en-us/articles/32781276130075).

![](https://klaviyo.zendesk.com/hc/article_attachments/34829073499931)

## Additional resources

- [How to use product feeds and recommendations](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787)
- [How to create a base template](https://klaviyo.zendesk.com/hc/en-us/articles/115005083887)