---
id: 115002779391
title: "How to create a third-party product review flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002779391-How-to-create-a-third-party-product-review-flow"
section: "Post-purchase flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:37Z"
language: en
---

## You will learn

Learn how to use flow messages to ask customers for their feedback on a recent purchase. This is a great way to build social proof and drive customer engagement with your brand.

To send product review emails, you can use Klaviyo's built-in product review/cross-sell flow as a starting point, or you can build your own from scratch.

If you use Klaviyo Reviews, learn how to [request reviews using Klaviyo Reviews flows](https://klaviyo.zendesk.com/hc/en-us/articles/16319809379611).

Klaviyo does not support in-email product reviews, meaning customers cannot write reviews directly within the product review email they receive from you.

## Third-party vs. Klaviyo Reviews

You can use Klaviyo to send review requests no matter which reviews platform you use. This resource provides instructions for third-party reviews platform.

A key differentiator between Klaviyo Reviews and other tools is review request timing. With other reviews tools, you have to trigger your flow when an order is fulfilled, and then add a time delay to allow the package time to arrive. With Klaviyo, you can send review requests based on when a package is delivered, so you can be certain you aren’t sending review requests to customers whose packages are delayed.

## Build a third-party review flow in Klaviyo

To create a review flow in Klaviyo with a third-party reviews app:

1. In Klaviyo, navigate to the ****Flows**** tab.
2. Click ****Create flow****.
3. Search for the **Product review / cross-sell** template in the flow library.
   ![third](https://klaviyo.zendesk.com/hc/article_attachments/28704476264475)
4. Select ****Fulfilled Order**** as the trigger metric.
5. Use a time delay that is longer than your average delivery time (e.g., 14 days), to increase the likelihood of the package arriving before the review request is sent.
6. Once you’re satisfied with the flow, set it live.

### Link customers to the review area on a page

Klaviyo’s template review flow uses [anchor links](https://help.klaviyo.com/hc/en-us/articles/360043506852). As a result, when someone clicks through your email, they will be brought directly to a specific area of your webpage where they can submit reviews, rather than having to scroll down and find it.

The template flow uses a #reviews anchor, but you can adjust this. Note that the directions below may be slightly different depending on your particular ecommerce integration.

Open the template editor for your site’s product page code. Scroll to the area in the code where your product reviews are displayed. Here, paste the following code:

`<a id="reviews"></a>`

This serves as an identifier, so when someone clicks a link to a product page with the #reviews anchor, they arrive at the correct location.

### Third-party review apps

Klaviyo integrates with several different product review apps, including [Judge.me](https://www.klaviyo.com/integrations/01J9V8Q5GDH7JVJ4HAV819VNV1/details) and [REVIEWS.io](https://www.klaviyo.com/integrations/01HWYW81ATNHZEXT7KNRTRY14C/details). If you use either of these apps and would like to integrate them with Klaviyo, check out the linked pages for more information.

## Additional resources

- [How to create an upsell or cross-sell flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002775212)
- [How to create a replenishment flow](https://klaviyo.zendesk.com/hc/en-us/articles/360003195232)
- [How to create a sunset flow](https://klaviyo.zendesk.com/hc/en-us/articles/360017518492)
- [How to adjust review request timing](https://klaviyo.zendesk.com/hc/en-us/articles/16682549669403)