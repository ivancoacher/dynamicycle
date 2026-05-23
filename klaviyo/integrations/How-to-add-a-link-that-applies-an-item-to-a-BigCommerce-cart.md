---
id: 115005082747
title: "How to add a link that applies an item to a BigCommerce cart"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005082747-How-to-add-a-link-that-applies-an-item-to-a-BigCommerce-cart"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:39Z"
language: en
---

## You will learn

Learn how to add a link to an email that applies an item to a BigCommerce cart. If you are prompting someone to view and purchase a specific product, such as a sale item, you can provide a link that they can click to add the item to their shopping cart.

## Before you begin

Make sure that you’ve [already integrated your Klaviyo account with BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce), and have created an email where you want to add your link.

Note that this process only works for BigCommerce products without variations.

## Add your item link

1. Find and copy the Product ID for the relevant item in BigCommerce. You can find this ID by [exporting the product from BigCommerce](https://support.bigcommerce.com/articles/Public/Exporting-Products) and checking the Product ID column.

Alternatively, you can do this by editing the product and locating the Product ID in the URL, as shown in the image below.

![BigCommerce admin product editing page for a sample product, with the Product ID highlighted in blue within the URL](https://klaviyo.zendesk.com/hc/article_attachments/28716328734363)

2. In Klaviyo, find the email template you'd like to edit and drag a Button block into your template; you can use whatever button text you'd like.

3. Within the button block, enter the following string in the Link URL box:
`{{ organization.url }}cart.php?action=add&product_id=##`

![Email template editor in Klaviyo with button and button block setting Link URL highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28716301371547)

4. Where you see ##, replace these double hashes with the BigCommerce Product ID you copied.

5. Click ****Save**** to save your content.

When the recipient clicks the button, they will be taken directly to their shopping cart on your site with the specified product already added. If you don't want to use a button, you can hyperlink any text in your email and use the same URL string.

## Outcome

You've now added a link to an email that applies an item to a BigCommerce cart.

## Additional resources

- [Getting started with BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce)
- [How to use coupons with BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360022884472-Guide-to-Using-Coupons-with-BigCommerce)