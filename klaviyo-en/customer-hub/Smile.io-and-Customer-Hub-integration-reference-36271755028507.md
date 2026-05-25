---
id: "36271755028507"
title: "Smile.io and Customer Hub integration reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/36271755028507-Smile-io-and-Customer-Hub-integration-reference"
section: "Integrate other platforms with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:53Z"
language: "en"
---
Learn how data syncs between Smile.io and Customer Hub and how customers can interact with your loyalty program directly through the Customer Hub interface.

By enabling Smile.io data in Customer Hub, you can increase engagement with your loyalty program and deliver personalized content to your customers based on their loyalty status.

Customer Hub for Shopify currently supports standard storefronts and Shopify Headless. For WooCommerce, navigate to https://help.klaviyo.com/hc/en-us/articles/47792369863451

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

This article explains about the integration between Customer Hub and Smile.io. If you have not already, read our guide on [how to connect Smile.io and Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660672085019) for step-by-step instructions on integrating, before continuing with this article.

## How customer loyalty data displays

You can connect Smile.io to Customer Hub in the Customer Hub settings in Klaviyo. When connected, Klaviyo surfaces individual customer loyalty data from Smile.io at the top of the **For you** tab in the Customer Hub drawer.

The data shown in the Customer Hub interface varies based on the whether the customer’s login status (i.e., whether they’ve logged into their customer account on your site) and loyalty membership:

- ****Signed-in loyalty members with more than one point****:
  - View their personal loyalty data, rewards progress, and loyalty tier.
  - Access a preview of available coupons and rewards, which expands to a full **Rewards** page when clicked.
    ![CHsmile100.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36271755023771)
- ****Signed-in site visitors who have have zero points****:
  - See an empty progress bar.
  - Receive a prompt to join the loyalty program with a "Start earning rewards" message.
- ****Visitors who have not logged in:****
  - Receive a prompt to sign in to view loyalty information.
  - Once logged in, see the loyalty data relevant to their status.

Specific profiles excluded from your Smile.io loyalty program do not see loyalty data within the Customer Hub interface. Similarly, profiles who are not rewards members do not see any loyalty data.

## Synced data from Smile.io to Customer Hub

Upon enabling Smile.io in your Customer Hub settings, Klaviyo syncs the following loyalty data for display:

- VIP tier icon (e.g., Silver VIP).
- Number of loyalty points.
- Best available reward (e.g., "Redeem 100 points for free shipping"). If the profile is not currently eligible for a reward, the next best reward displays with the number of points required to reach it.
- Progress bar indicating progress to the next best reward.
- Available rewards.
- Individual referral link.
- Configured [ways to earn](https://help.smile.io/en/articles/4036267-configure-ways-to-earn-points) options (configured in Smile.io).

## How customers can manage and redeem loyalty rewards in Customer Hub

Logged-in loyalty program members can manage and redeem rewards through the Smile.io component in the Customer Hub interface. Selecting any loyalty component on the **For you** tab expands to a detailed **Rewards** page, where they can manage rewards and available coupons.

![CHSMILE101.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36271762209691)

Rewards redemption:

- A progress bar indicates progress toward next best reward.
- Rewards that the customer is eligible (i.e., has enough points) to redeem appear in the "Redeem your points" section (e.g., 10% off for 100 points). Customers can click into any reward to view, redeem, and apply it to their cart.
  - If the customer does not use the code after applying it to their cart, it is moved to their available coupons section for future use.

Coupons:

- A preview of the number of the profile's available coupons also appears on the **Rewards** page. This preview expands to a detailed **Coupons** page for redemption.
  - When a customer redeems points for a coupon, the coupon is automatically applied to their cart. Unused coupons remain in the available coupons section. Note that customers who do not have loyalty can still see their [available coupons in the Customer Hub interface](https://klaviyo.zendesk.com/hc/en-us/articles/33660581127963).
    ![CHSMILE102.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36271755026843)

Customers can also find their individual referral link and an expandable "Ways to earn" menu below the redeemable rewards and coupons. The "Ways to earn" menu shows the [earning options you configured in Smile.io](https://help.smile.io/en/articles/4036267-configure-ways-to-earn-points). Note that you can only edit these earning options in Smile.io, not in Customer Hub settings****.****

****![CHSMILE103.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36271762210715)****

## Additional resources

- [How to connect Smile.io and Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660672085019)
- [Getting started with Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675)
- [How to create content blocks for Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660517680795)