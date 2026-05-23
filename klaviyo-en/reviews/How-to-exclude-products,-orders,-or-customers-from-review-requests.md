---
id: 16684841274139
title: "How to exclude products, orders, or customers from review requests"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16684841274139-How-to-exclude-products-orders-or-customers-from-review-requests"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:48:59Z"
language: en
---

## You will learn

Learn how to avoid sending review requests to certain customers or for products that don’t require review (like gift cards or shipping insurance).

## Using the klaviyo\_reviews\_exclude tag

Klaviyo Reviews provides a tag, **klaviyo\_reviews\_exclude**, that can be applied to products, orders, and customers to stop review requests from being sent. See sample use cases and how to apply this tag in the sections below.

![The exclusion tag](https://klaviyo.zendesk.com/hc/article_attachments/28705665408795)

## Exclude a product from future review requests

Say a customer orders a guitar with shipping insurance. If you add the exclusion tag to your shipping insurance line item, they will only receive a review request for the guitar.

To exclude a product from future review requests in Shopify:

1. Navigate to a product page in your Shopify admin.
2. In the **Tags** field, add the tag **klaviyo\_reviews\_exclude**.

   To exclude a product from future review requests in WooCommerce:
3. Navigate to a product page in your WooCommerce admin.
4. In the **Product** **Tags** field, add the tag **klaviyo\_reviews\_exclude**.

Once you’ve saved this change, we will no longer request reviews for this product, even if it’s the only item in someone’s order. Note that these changes only apply to future orders; any orders that were placed before you made the change may receive review requests for this product.

## Exclude an order from your review request flow (Shopify only)

Adding this tag to an order excludes that order from review request. It is a one-time exclusion: if the same customer places another order in the future, that order will be eligible for a review request.

1. Navigate to the order in your Shopify admin.
2. In the **Tags** field, add the tag **klaviyo\_reviews\_exclude**.

## Exclude a customer from receiving review requests (Shopify only)

1. Navigate to a customer in your Shopify admin.
2. In the **Tags** field, add the tag **klaviyo\_reviews\_exclude**.
3. Save the customer’s details.

Adding this tag will exclude a customer from receiving future review requests. Note that if they have a recent order that is currently in your review request flow, they will continue receiving messages until they exit that flow.

## Billing for excluded products, orders, and customers

If an order is excluded from receiving a review request (i.e., the customer, all products in the order, or the order itself has the **klaviyo\_reviews\_exclude** tag), then the order won’t count towards your Klaviyo Reviews billing plan.