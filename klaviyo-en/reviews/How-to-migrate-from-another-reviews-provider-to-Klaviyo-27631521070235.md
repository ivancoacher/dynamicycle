---
id: "27631521070235"
title: "How to migrate from another reviews provider to Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/27631521070235-How-to-migrate-from-another-reviews-provider-to-Klaviyo"
section: "Getting started with reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:43Z"
language: "en"
---
## You will learn

Learn how to migrate from a previous reviews provider to Klaviyo Reviews. This guide covers the entire migration process, from importing your data to setting up widgets, choosing a plan, and reviewing your results. Klaviyo Reviews is currently supported for those using Shopify or WooCommerce as their ecommerce platform.

## Overview

If you choose to follow the in-app onboarding wizard, it will walk you through the initial steps outlined below. Skip ahead to the first step you haven’t yet completed.

1. [Integrate your ecommerce platform](#h_01J3FXGG9SYS0RNVA554MN7QR1)
2. [Import data from your past provider](#h_01J3FXGG9S4AE7XR6TXEKVP7HN)
3. [Create reviews flows](#h_01J3FXGG9SKNET9BDV5YXZGM1C)
4. [Test your setup](#h_01J3FXGG9S4F4WTKSA0H4YATGP)
5. [Cut over to Klaviyo Reviews](#h_01J3FXGG9SVB6SCS27NV20E1NH)
6. [Implement best practices](#h_01J3FXGG9S3TXTD2AJ5C2NF5V4)
7. [Review your performance](#h_01J3FXGG9SNJVTCSDE7XE41K08)

## 1. Integrate your ecommerce platform

Integrating with your ecommerce platform involves 2 steps:

1. Adding the Klaviyo Reviews app.
2. Installing reviews widgets on your site.

Before installing Klaviyo Reviews, make sure you are logged in to the correct accounts.

Installing the app allows Klaviyo Reviews to exchange information with your store, like order activity and site traffic. If you don’t see your ecommerce platform listed below, Klaviyo Reviews is not yet available for your store.

- [Install the Klaviyo Reviews app for Shopify](https://apps.shopify.com/klaviyo-reviews)
- [Install the Klaviyo Reviews plugin for WooCommerce](https://help.klaviyo.com/hc/en-us/articles/26922347702939)

  Once you’ve installed the app, add Klaviyo Reviews widgets to your store. Widgets display reviews information to site visitors, like a product’s star rating or reviews from past customers.

  Follow the widget installation instructions for your platform and theme type:
- [How to install Klaviyo Reviews widgets on Shopify 2.0 themes](https://help.klaviyo.com/hc/en-us/articles/16318951826331)
- [How to install Klaviyo Reviews widgets on Shopify (vintage themes and headless)](https://help.klaviyo.com/hc/en-us/articles/16318891028635)
- [How to install Klaviyo Reviews widgets on WooCommerce](https://help.klaviyo.com/hc/en-us/articles/26922347702939)

Tip: Install these widgets on a draft theme so you have the opportunity to test them before setting them live. Note that Klaviyo cannot detect widgets on draft themes, so you may see an in-app message indicating your widgets are not yet installed until you set the draft theme live.

## 2. Import reviews from your past provider

Import past reviews so you don’t lose any data when you migrate. First, export data from your current platform:

- [Yotpo](https://support.yotpo.com/docs/exporting-reviews-from-yotpo)
- [Okendo](https://help.octaneai.com/en/articles/7932726-exporting-reviews-from-okendo)
- [Stamped](https://stampedsupport.stamped.io/hc/en-us/articles/8839244356891-Exporting-Reviews-Checkout-Comments-or-NPS)
- [Reviews.io](https://support.reviews.io/en/articles/9185047-how-to-export-your-reviews)
- [Judge.me](https://help.judge.me/en/articles/8236266-exporting-reviews)
- [Loox](https://help.loox.io/article/21-how-do-i-export-my-reviews)

If your current platform isn’t listed here, you can reference their support documentation to learn how to export your reviews.

To import your reviews to Klaviyo:

1. Select ****Reviews**** from the Klaviyo sidebar.
2. Navigate to the ****All reviews**** tab.
3. Select ****Options****.
4. Select ****Import Reviews****.
   ![The Import Reviews button](https://klaviyo.zendesk.com/hc/article_attachments/28705639211931)
5. Choose your previous reviews platform from the options provided. If you don’t see your platform listed, select ****Other/not sure****.

   If you select ****Other/not sure****, you must format your CSV using [our sample template](https://help.klaviyo.com/hc/en-us/articles/16318811222555#h_01HS15C65Q8NZ2HNVTHR66R0PH) before proceeding.
6. Select ****Choose file**** or drag and drop your CSV file into the upload tool.
7. If accurate, check the box next to **I confirm that the imported reviews are genuine**. Only legitimate reviews may be uploaded to Klaviyo.
8. Review the mapping of fields from your upload and make adjustments as needed.
9. Select ****Next****.

If you have trouble importing, head to our article covering [how to import reviews data from another platform](https://help.klaviyo.com/hc/en-us/articles/16318811222555) for more information and troubleshooting help.

## 3. Create reviews flows

There are 2 key review flows:

- ****Review request flow****
  Ask a recent purchaser to review a product from their order. Consider offering an incentive (e.g., 15% off, free shipping on their next order, additional loyalty points), which may increase conversions. This flow is triggered by the **Ready to review** event.
- ****Review follow-up flow****
  We recommend offering an incentive in exchange for customer reviews. Deliver the reward once a review is submitted using a flow triggered by the **Review submitted** event.

You can find templates for these flows by navigating to ****Flows > Create flow**** and searching **Review** in the Flow Library. All reviews with the **Klaviyo Reviews** tags use Klaviyo Reviews metrics.

![Reviews flows](https://klaviyo.zendesk.com/hc/article_attachments/28705699645595)

Learn [how to request reviews from your customers with Klaviyo Reviews flows](https://help.klaviyo.com/hc/en-us/articles/16319809379611).

Additionally, you can create a [flow to submit a customer service ticket for every negative review](https://help.klaviyo.com/hc/en-us/articles/16680027976731) you receive. This proactively enables your support team to resolve issues and converts unhappy reviewers into loyal long-term customers.

## 4. Test your setup

To ensure you’re ready to cut over to Klaviyo Reviews, test the following:

- Check that all reviews widgets appear correctly on your draft theme and display any reviews you’ve imported.
- Preview the messages in your review request and review follow-up flows to ensure they match your branding and appear as desired.
- Confirm your [review timing settings](https://help.klaviyo.com/hc/en-us/articles/16682549669403) make sense for your products. By default, review requests are sent 7 days after an order is delivered.

## 5. Cut over to Klaviyo Reviews

Once you’ve tested everything and are ready to set Klaviyo Reviews live, follow this checklist:

1. Select the right [Klaviyo Reviews plan](https://help.klaviyo.com/hc/en-us/articles/115000976672#01H84M7N01NF4JEY8DJC88PC31) for your order volume.
2. Optional: if several days or more have passed since you originally imported reviews from your previous platform, [import any new reviews](https://help.klaviyo.com/hc/en-us/articles/16318811222555) you’ve received since then.
3. Turn your reviews flows from **Manual** or **Draft** to ****Live****.
4. Publish the draft store theme where your reviews widgets are installed.
5. Cancel your previous reviews platform and turn off any automations.
6. Optional: [request reviews from past orders](https://help.klaviyo.com/hc/en-us/articles/25930166202651) so your review request flow begins sending right away.

## 6. Implement best practices

Once you’ve set up the core Klaviyo Reviews functionality, consider using advanced features:

- Ask reviewers [custom questions](https://help.klaviyo.com/hc/en-us/articles/16319181846171) about themselves or their experience with your brand.
- [Sync your reviews](https://help.klaviyo.com/hc/en-us/articles/16681460907035) to a Google Shopping feed.
- Learn how to [moderate reviews](https://help.klaviyo.com/hc/en-us/articles/19351110471323).
- [Create a customer service ticket](https://help.klaviyo.com/hc/en-us/articles/16680027976731) when you receive a negative review.
- [Highlight positive reviews](https://help.klaviyo.com/hc/en-us/articles/18007373861915) in your emails.
- Use [custom CSS to implement advanced styling options](https://developers.klaviyo.com/en/docs/use_css_to_style_klaviyo_reviews_widgets).

## 7. Review your performance

A few weeks after you begin using Klaviyo Reviews, head to ****Reviews > Performance**** to [evaluate the success of your reviews program](https://help.klaviyo.com/hc/en-us/articles/22567673911707). Here, you can check how many reviews you’ve requested and received, and see how your site visitors interact with reviews content.