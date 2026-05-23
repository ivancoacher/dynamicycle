---
id: 16318891028635
title: "How to install Klaviyo Reviews on Shopify (vintage themes and headless)"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16318891028635-How-to-install-Klaviyo-Reviews-on-Shopify-vintage-themes-and-headless"
section: "Getting started with reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:48:48Z"
language: en
---

## You will learn

Learn how to install Klaviyo Reviews with a vintage Shopify theme or headless architecture. This process involves copying several code snippets and pasting them into your site’s code.

If you are using a Shopify 2.0 theme, you can install Klaviyo Reviews without using code. Head to our article on [getting started with Klaviyo Reviews](https://help.klaviyo.com/hc/en-us/articles/15937542819355) to learn more. If you use WooCommerce, learn how to [install Klaviyo Reviews for WooCommerce](https://help.klaviyo.com/hc/en-us/articles/26922347702939).

This process requires directly editing your theme files in Shopify. If you aren’t comfortable doing this yourself, reach out to your developer or [contact a Klaviyo partner](https://connect.klaviyo.com/) for assistance.

## Before you begin

Before you paste these code snippets in your site’s code, [add the Klaviyo Reviews app](https://apps.shopify.com/klaviyo-reviews) to your Shopify store. For vintage themes, [enable Klaviyo's onsite tracking](https://help.klaviyo.com/hc/en-us/articles/4425956184731).

## Installing with headless architecture on Shopify

To integrate Klaviyo Reviews with a headless Shopify store, add Klaviyo's JavaScript tracking snippet, also known as Klaviyo.js, to all pages where you’d like to add reviews widgets (e.g., product pages). You may have already installed this snippet if you've configured Klaviyo's onsite tracking or sign-up forms.

Learn how to [install Klaviyo.js for Shopify stores](https://help.klaviyo.com/hc/en-us/articles/360020342232).

Once you’ve added this script to your site, proceed by copying the code snippets in the steps below into your site's code.

## Add the code snippets

The code snippets below allow certain reviews widgets to appear in different areas of your store.

- The ****star rating widget**** displays the current star rating for a particular product, and is most often installed beneath your product’s name.
- The ****review summary widget**** shows a chart breaking down all the ratings selected for a product, user images submitted with reviews, and the most common feedback the product has received. It’s usually installed near the bottom of a product page.
- The ****product reviews widget**** is a combination of the reviews summary and review list widgets. If you add the product reviews widget to your site, you don’t need to add the review list and review summary widgets separately.
- The ****review list widget**** displays a list of all published reviews and customer questions, along with a search bar, filters, a ****Write a Review**** button, and an ****Ask a Question**** button. It’s typically installed immediately below the review summary widget.
- The ****featured review carousel widget**** displays highlighted reviews from all your products. This can be featured on your homepage, on a standalone reviews page, or anywhere else on your site. You can select the reviews that are featured in this widget. If available, customer-submitted images accompany each review; your product images are used if no image was submitted alongside the review.
- The ****SEO / All reviews widget**** displays all your reviews across all products on a single page. Use this widget to improve your SEO and provide a single place for potential customers to see what your current customers love. This widget is most often added to a standalone **Reviews** page on your site.

### Star rating widget

Use the star rating widget to prominently feature a product’s average rating and the number of reviews it has received.

![The star rating widget](https://klaviyo.zendesk.com/hc/article_attachments/28715965547163)

To install this widget beneath your product’s title:

1. Open your Shopify store admin.
2. Under **Sales channels** click ****Online Store****.
3. Click the three dots menu next to your current theme > ****Duplicate**** to create a clone of your current theme.
4. From the three dots menu, click ****Edit code****.
   ![The Edit code button](https://klaviyo.zendesk.com/hc/article_attachments/28715972087707)
5. Search “product” in the file search bar and locate the file used for your product page content. It might be **product.liquid**, **product-template.liquid**, or something similar. (If you use a custom product page template, select that instead.)
   ![Searching for the product page content](https://klaviyo.zendesk.com/hc/article_attachments/28715965535899)
6. Select the file, then search for {{ product.title }} to locate the code that displays your product’s title.
   ![Product title code](https://klaviyo.zendesk.com/hc/article_attachments/28715972092955)
7. Add a new line beneath this code.
8. On the new line, paste this code snippet:
   `<div class="klaviyo-star-rating-widget" data-id="{{product.id}}" data-product-title="{{product.title}}" data-product-type="{{product.type}}"></div>`
   ![The star rating code snippet](https://klaviyo.zendesk.com/hc/article_attachments/28715972095899)
9. Click ****Save****.
10. Click ****Preview store****.
11. Navigate to a product page within your store preview. You should see a star widget beneath the product’s title.

### Product reviews widget

Use the review summary and review list widget (or just the product review widget) to add a summary and list of all published reviews for each product on your site.

![Review summary with images](https://klaviyo.zendesk.com/hc/article_attachments/28715972112795)

To install the summary and list widgets separately, head to the [separate review summary and review list widgets](#h_01H3W6P97SQ00C8CRMYP66RBZX) section below.

To install this widget:

1. Open your Shopify store admin.
2. Under **Sales channels** click ****Online Store****.
3. Click ****Customize**** next to your current theme to edit it, or click the three dots menu > ****Duplicate**** if you’d like to edit a draft theme instead of your live one.
4. From the three dots menu, click ****Edit code****.
   ![The Edit code option](https://klaviyo.zendesk.com/hc/article_attachments/28715972087707)
5. Search “product” in the file search bar and locate the file used for your product page content. It might be **product.liquid**, **product-template.liquid**, or something similar. (If you use a custom product page template, select that instead.)
   ![Locating the product page content](https://klaviyo.zendesk.com/hc/article_attachments/28715965535899)
6. Select the file, then navigate to the very bottom (or wherever you’d like the reviews summary and list widget to appear).
7. Add a new line, then paste this code snippet:
   `<div id="klaviyo-reviews-all" data-id="{{product.id}}"></div>`
   ![The all reviews code snippet](https://klaviyo.zendesk.com/hc/article_attachments/28715965542555)
8. Click ****Save****.
9. Click ****Preview store****.
10. Navigate to a product page within your store preview for a product that has reviews. You should see a reviews summary and list view widget near the bottom of the page.

### Separate review summary and review list widgets

If you’d prefer to install the review summary and review list widgets separately (rather than together, as outlined in the section above), use the following code snippets:

#### Review summary widget

`<div id="klaviyo-reviews-summary" data-id="{{product.id}}"></div>`

#### Review list widget

`<div id="klaviyo-reviews-list" data-id="{{product.id}}"></div>`

### Featured review carousel widget (optional)

The featured reviews carousel displays hand-selected reviews on any page you choose (e.g., your home page).

![The featured reviews carousel widget](https://klaviyo.zendesk.com/hc/article_attachments/28715965550363)

To add a carousel displaying all your featured reviews, you must first select reviews to feature.

1. In Klaviyo’s main navigation, select ****Reviews****.
2. Click ****All Reviews****.
3. Beside a review you’d like to feature, click ****Feature****.

![The option to feature a review](https://klaviyo.zendesk.com/hc/article_attachments/28715972110235)

Once you’ve selected several reviews to feature on your site, you can install a review carousel widget on any page. Navigate to the page where you’d like the carousel to appear, then paste the following snippet in that page’s code:

`<div id="klaviyo-featured-reviews-carousel"></div>`

## SEO / All reviews widget (optional)

The SEO / All reviews widget displays all published reviews across every product. Add this to a standalone Reviews page, or to your About page.

`<div id="klaviyo-reviews-all" data-id="all"></div>`

![all reviews widget](https://klaviyo.zendesk.com/hc/article_attachments/28715972114843)

## Outcome

Once you’ve installed the widgets outlined in this article and set the new theme live, your reviews will appear across product pages (as well as any other pages on your site where you’ve installed them).