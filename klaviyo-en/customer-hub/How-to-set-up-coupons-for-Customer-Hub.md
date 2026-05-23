---
id: 39273771656987
title: "How to set up coupons for Customer Hub"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/39273771656987-How-to-set-up-coupons-for-Customer-Hub"
section: "Build and use Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:54Z"
language: en
---

Learn how to enable unique coupons and add static coupons so they are visible for shoppers in Customer Hub.

Customer Hub currently supports Shopify storefronts, including Shopify Headless. Additional eCommerce platform support is planned.

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

To set up coupons for Customer Hub, you must have the Customer Hub feature enabled.

For a detailed explanation of how Klaviyo determines which coupons are available to shoppers, see [Understanding how coupons work in Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660581127963).

## Types of coupons in Customer Hub

Klaviyo supports 2 types of coupons for your customers:

- Unique coupons: one-time, one-per-person discount codes created in Klaviyo and delivered individually (e.g., through flows, campaigns, or forms).
- Static coupons: general-use discount codes created in Shopify that can be shared across a broad audience.

## Unique coupons in Customer Hub

Unique coupons are enabled for Customer Hub by default; you don’t need to set anything up.

This means that if a profile has received a unique coupon from you, it automatically appears on their **Coupons** page in the Customer Hub interface if it’s [active and available](https://klaviyo.zendesk.com/hc/en-us/articles/33660581127963).

To re-enable unique coupons (if you previously disabled them):

1. In Klaviyo, navigate to the ****Customer Hub**** tab.
2. Click ****Extensions****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40774267636891)
3. Select ****Coupons****.
4. Toggle **Show unique coupons** on.

![](https://klaviyo.zendesk.com/hc/article_attachments/40774299315739)

## Add static coupons to Customer Hub

****Static coupons must be created in Shopify first****, then added manually to Customer Hub. You can target static coupons to specific lists or segments when you adding them.

To add a static coupon:

1. Create the coupon code in Shopify if you haven’t already. Copy the exact code for later.
2. In Klaviyo, navigate to the ****Customer Hub**** tab.
3. Click ****Extensions****.
4. Find the ****Coupons**** card.
5. Click ****Create static coupon****.
   ![hubcoupon8.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39273765150363)
6. Fill in the coupon details:

   - ****Coupon code****: Paste the exact code you created in Shopify.
   - ****Description**** (optional): Add details about the offer or eligibility.
   - ****Targeting**** (optional): Use the **Show to** and **Don’t show to** dropdowns to to specify which lists or segments see the coupon. Leave blank to show to everyone.
7. Click ****Create****.

![hubcoupon10.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39273765154459)

Your static coupon now appears in Customer Hub for eligible customers, under the **Available coupons** section.

## Disable or hide all coupons in Customer Hub

Tip: to prevent any coupons from showing in Customer Hub, disable unique coupons and either deactivate or delete any static coupons you've added.

To hide all coupons in Customer Hub:

1. Go to the ****Customer Hub**** tab in Klaviyo.
2. Click ****Extensions****.
3. Find ****Coupons****.
4. Set the **Show unique coupons** switch to ****Off**** (grey).
5. For static coupons either:

- Set the toggle next to each coupon to ****Off**** (grey).
  ![hubcoupon11.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39273979636507)
- Delete each static coupon by clicking the three dots menu next to it and selecting ****Delete coupon****.

No coupons will be visible to any shoppers in Customer Hub once all coupons are disabled or removed.

## Next steps

You can track how many customers are using these coupons via the **Coupon applied** event on the [**Service interactions**](https://www.klaviyo.com/customer-hub/dashboard) [chart](https://www.klaviyo.com/customer-hub/dashboard). Learn more about the [Customer Hub metric dashboard](https://klaviyo.zendesk.com/hc/en-us/articles/33660382797595).