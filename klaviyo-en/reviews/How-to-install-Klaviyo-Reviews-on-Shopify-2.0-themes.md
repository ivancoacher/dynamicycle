---
id: 16318951826331
title: "How to install Klaviyo Reviews on Shopify 2.0 themes"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16318951826331-How-to-install-Klaviyo-Reviews-on-Shopify-2-0-themes"
section: "Getting started with reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:48:49Z"
language: en
---

## You will learn

Learn how to install Klaviyo Reviews on your Shopify 2.0 store by installing the app and adding reviews widgets.

If your Shopify store uses a vintage theme, you must copy and paste a few code snippets in order to add reviews widgets. Learn how to [install Klaviyo Reviews on a vintage Shopify theme](https://help.klaviyo.com/hc/en-us/articles/16318891028635). If you use WooCommerce, learn how to [install Klaviyo Reviews for WooCommerce](https://help.klaviyo.com/hc/en-us/articles/26922347702939).

## Before you begin

Before you add these widgets to your Shopify store:

- [Add the Klaviyo Reviews app](https://apps.shopify.com/klaviyo-reviews) on your Shopify store.
- [Enable the Klaviyo app embed](https://help.klaviyo.com/hc/en-us/articles/4425956184731) in your Shopify integration.

## Available reviews widgets

Klaviyo Reviews provides several widgets you can add to your Shopify store:

- The ****star rating widget**** displays your current star rating for a particular product, and is most often added beneath your product’s name.
  ![The star rating widget](https://klaviyo.zendesk.com/hc/article_attachments/28715972345115)
- The ****product reviews widget**** shows a chart breaking down all the ratings a product received, user images submitted with reviews, and the most common feedback the product has received.

  Below that is a list of all published reviews and customer questions along with a search bar, review filters, a ****Write a Review**** button, and an ****Ask a Question**** button.

  It’s usually added near the bottom of a product page.
  ![Review summary with images](https://klaviyo.zendesk.com/hc/article_attachments/28715965787291)
  ![The reviews list](https://klaviyo.zendesk.com/hc/article_attachments/28715972347547)
- The ****featured review carousel widget**** displays highlighted reviews from all your products. This can be featured on your homepage, on a standalone reviews page, or anywhere else on your site. You can select the reviews that are featured in this widget. If available, customer-submitted images accompany each review; your product images are used if no image was submitted alongside the review.
  ![The featured reviews carousel widget](https://klaviyo.zendesk.com/hc/article_attachments/28715972351387)
- The ****SEO / All reviews widget**** displays all your reviews across all products on a single page. Use this widget to improve your SEO and provide a single place for potential customers to see what your current customers love. This widget is most often added to a standalone **Reviews** page on your site.

![all reviews widget](https://klaviyo.zendesk.com/hc/article_attachments/28715965791259)

## Add reviews widgets to your site

These steps outline how to add Klaviyo Reviews widgets on a Shopify store using a Shopify 2.0 theme. If you use a Shopify vintage theme, you’ll need to [manually install code snippets](https://help.klaviyo.com/hc/en-us/articles/16318891028635) to add these widgets instead.

1. In Klaviyo, navigate to ****Reviews****.
2. Click ****Reviews settings**** in the top right corner.
3. Select ****Onsite widgets****.
4. Click the widget you'd like to install (e.g., ****Product reviews widget****).
5. Select ****Installation****.
6. In the **Shopify 2.0** tab, click ****Install****.
7. You'll be directed to the editor for your current Shopify theme, with the widget added.
8. Check the placement of the widget and adjust in the Shopify editor if needed.
9. Click ****Save**** to publish your updates and set the widget live on your site.
10. Repeat with additional widgets (e.g., star rating widget, featured review carousel widget) as desired.

### Manually install widgets through your Shopify theme editor

If you'd prefer to manually install the reviews widgets rather than using the automatic installer, you can do so within your Shopify theme editor.

****Manual installation steps****

1. In your Shopify Admin, navigate to ****Online Store > Themes****.
   ![Shopify's online store themes](https://klaviyo.zendesk.com/hc/article_attachments/28715972353947)
2. Click the three dots icon beneath your current theme.
3. Click ****Duplicate**** to make a copy.
4. Next to the new copy of your theme, click ****Customize****.
5. Follow the steps for each widget below.

### Add a product reviews summary and list

1. Click the dropdown menu labeled ****Home Page****.
2. Click ****Products > Default product**** (or whichever template you use for your product pages).
   ![The default products template](https://klaviyo.zendesk.com/hc/article_attachments/28715972349211)
3. In the sidebar, click ****Add Section****.
   ![Add a section](https://klaviyo.zendesk.com/hc/article_attachments/28715972355355)
4. Select ****Product Reviews**** from the list.

![product reviews widget](https://klaviyo.zendesk.com/hc/article_attachments/28715972363419)

### Add a star rating under the product title

1. Click the dropdown menu at the top of your Shopify site editor.
2. Click ****Products > Default product**** (or whichever file you use for your product pages).
   ![The default product page in Shopify](https://klaviyo.zendesk.com/hc/article_attachments/28715972349211)
3. In the **Product information** section, click ****Add block****.
   ![Add a block](https://klaviyo.zendesk.com/hc/article_attachments/28715972364827)
4. Choose the ****Star Rating**** block.
   ![star rating app](https://klaviyo.zendesk.com/hc/article_attachments/28715965782427)
5. Use the icon to the right of the block name to reorder the block. The star rating widget is most commonly placed directly above the product price.
   ![star rating placement](https://klaviyo.zendesk.com/hc/article_attachments/28715972371483)
6. Once you’re happy with the placement of your reviews widgets, click ****Save****.

### Display featured reviews anywhere on your site

1. Navigate to the template for any page in your Shopify store.
2. Click ****Add section****.
3. Click ****Apps****.
4. Select the ****Featured Reviews Carousel**** block.
   ![Featured reviews carousel widget block](https://klaviyo.zendesk.com/hc/article_attachments/28715972357531)
5. This block will display reviews you’ve chosen to feature in your Klaviyo Reviews admin.

![Feature reviews carousel widget](https://klaviyo.zendesk.com/hc/article_attachments/28715965774363)

If you'd like to add star ratings under a product name on a collection page, you'll need to edit your theme files and add the code snippet below within the product grid.

`<div class="klaviyo-star-rating-widget" data-id="{{product.id}}" data-product-title="{{product.title}}" data-product-type="{{product.type}}"></div>`

This may require the help of a developer. Klaviyo's support team is not able to directly edit your theme files.

## Outcome

Once you’ve added the widgets outlined in this article and set the new theme live, your reviews will appear on your site.