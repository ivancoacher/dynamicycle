---
id: 360034336572
title: "How to use sign-up forms to offer tiered discounts"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360034336572-How-to-use-sign-up-forms-to-offer-tiered-discounts"
section: "Form best practices"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:45Z"
language: en
---

## You will learn

Learn how to use sign-up forms to offer different discounts to different types of customers, then set up your welcome series so each subscriber receives the appropriate discount. Setting specific targeting settings in your forms can help you avoid offering discounts unnecessarily and tailor the language in your emails based on what you already know about your contacts.

## Before you begin

Consider what customers you want to target and how you want to incentivize them.

For example, you may want to incentivize site visitors to sign up for your email list by offering a discount on their first purchase. You may want to offer:

- 15% off to visitors who are new to your site and have never purchased before
- 10% off to visitors who have previously browsed your site but never bought
- No discount to those who have bought from you in the past

This is something you can accomplish using a combination of segments, sign-up forms, coupons, and flows.

****Click to expand for other example use cases****

- Targeting shoppers with high-value items in their cart with larger discounts than low-value shoppers.
- Targeting VIP customers with a different welcome offer and messaging than your other customers.

## Create segments of audiences you would like to target

When building a new segment, you can identify the audiences you would like to target with offers on your sign-up forms. In our example, we're going to isolate four groups and the definition to follow in the segment builder to create each one:

1. Visitors who have been to our site fewer than 3 times and never purchased (20% off)
2. Visitors who have visited our site 3 or more times and never purchased (15% off)
3. Visitors who purchased more than 180 days ago and haven't bought since (10% off)
4. Visitors who have purchased in the last 180 days (no discount)

Navigate to ****Audience > Lists & segments > Create list / segment >  Create segment****. Name each segment after its definition so you can easily keep track of each one.

### Browsed fewer than 3 times and never purchased

You can build this segment by identifying people who have been active on your website fewer than 3 times over all time. Alternatively, you can restrict this to a specific timeframe, like 90 days, to narrow down your audience.

Browsers who are not cookied will not fall into this segment since no email address will be available. To target this group, follow the steps outlined below.

Next, you'll want to add a condition specifying that they haven't ever placed an order.

![A new segment being created for people who have browsed fewer than 3 times and never purchased.](https://klaviyo.zendesk.com/hc/article_attachments/28713335847451)

### Browsed 3 or more times and never purchased

Here, you'll want to isolate people who have been active on your website at least 3 times over all time. You may also want to include browsers who have viewed at least 3 products over all time. Again, you can also restrict this to a smaller time period, like 90 days, if you would like.

Next, add a condition specifying that they've never placed an order before. For this condition, be sure to extend the timeframe to all time.

![A new segment being created with the definition set to include those who have browsed more than 3 times and never purchased.](https://klaviyo.zendesk.com/hc/article_attachments/28713330163227)

### Purchased more than 180 days ago and haven't bought since

In this segment, you'll want to identify people who have purchased before, but not in the last 180 days. This is a good group to offer a discount that reflects the messaging you have in your [winback series](https://help.klaviyo.com/hc/en-us/articles/115002775192-Create-a-Winback-Flow).

![A new segment being created with the definition set to include those who have purchased before, but not in the last 180 days.](https://klaviyo.zendesk.com/hc/article_attachments/28713330141851)

### Purchased in the last 180 days

Lastly, you want to target people who have bought in the last 180 days to encourage them to sign up for our email list, however, we're not going to offer them a discount since they have bought somewhat recently.

![A new segment being created with the definition set to include those who have purchased in the last 180 days.](https://klaviyo.zendesk.com/hc/article_attachments/28713330146075)

## Build segment-targeted sign-up forms

Once you've built the segments you would like to target, the next step is to [create a separate form](https://help.klaviyo.com/hc/en-us/articles/360002049952) to target each group and prompt them to subscribe to your main list.

1. Navigate to the ****Sign-up forms**** tab and choose a template from the library or to build a new form form scratch.
2. Use the editor to design the form to match your brand.
3. In the ****Styles**** tab, select a form type. We recommend choosing a popup, flyout, or a full page form so that you can capture shoppers' attention.
4. In the ****Targeting &**** ****Behaviors****section, you will want to configure a couple of key settings:
   - Under ****Targeting****, you will want to show the form only to those in one of the 4 corresponding segments you just built.
   - Under ****Targeting****, you will also want to exclude those who are already on your list from seeing the form. Since we didn't include a condition that someone is not on our main list in the segments we built, this setting is particularly important.
     ![The Targeting by visitor for an example form set to include those in the tiered discount list, and exclude the main list.](https://klaviyo.zendesk.com/hc/article_attachments/28713335856283)
5. Depending on whether or not you have [double opt-in enabled](https://help.klaviyo.com/hc/en-us/articles/115005251108-The-Double-Opt-In-Process) (by default, double opt-in is enabled for all lists), be sure to update the language on your success message by clicking ****Success****. If you are choosing to use static coupons, or are a Shopify user, you can also include the coupon code directly on the success message.

   You will likely only want to do this if your list is single opt-in to prevent people from signing up to receive the discount but not confirming their email address. If your list is set to double opt-in and a subscriber does not confirm their email, they will not be added to the list or trigger the welcome series.
6. Repeat this process for each of the segments you created in the previous step so that every segment has a corresponding form.
7. Once you've built the first form, you can clone it several times and change the discount amounts and segments it's connected to.
8. To ensure that you display a form to browsers who are not cookied (and hence don't fall into any of your segments,) clone your 20% off form and configure it to display only to browsers who are not tracked. You can do this by navigating to the ****Targeting & Behaviors****section and, under ****Targeting****, selecting **Don't show to existing Klaviyo profiles.**

   ![The Targeting by visitor for an example sign-up form set to Don't show to existing Klaviyo profiles.](https://klaviyo.zendesk.com/hc/article_attachments/28713335842331)

   ## Include discounts in your welcome series

   Next, you'll want to update your [welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172-Guide-to-Creating-a-Welcome-Series). If you're using [Shopify](https://help.klaviyo.com/hc/en-us/articles/115006155388-Unique-Coupon-Codes-for-Shopify) or [Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005246547-Set-Up-Coupons-for-Magento-1-x-), you can use dynamic coupons through your integration. Otherwise, you can instead leverage the [uploaded coupons feature](https://help.klaviyo.com/hc/en-us/articles/115005084727-How-to-Use-Coupon-Codes-in-Klaviyo#upload-unique-coupon-codes2) to offer unique codes to your subscribers.

   Since we're offering different discounts for each tier, we'll need to create 3 separate coupon codes, each with different percentages off. Follow the instructions outlining in the relevant guides above to create these unique coupon codes.

   ![An example welcome series email with a coupon tag and coupon name in it.](https://klaviyo.zendesk.com/hc/article_attachments/28713330131099)

   Next, create a flow (****Flows > Create flow > Create from scratch****). In order to send different emails to different types of subscribers, we'll need to drag several [conditional splits](https://help.klaviyo.com/hc/en-us/articles/115003872171-Add-a-Conditional-Split) into our flow. These conditional splits will match the conditions that we used to build the segments outlined in the first step.

   ![A list-triggered flow built with 4 conditional split paths for the 4 corresponding tiered discounts you created, and a different email with the correct coupon sent to each one.](https://klaviyo.zendesk.com/hc/article_attachments/28713330169115)

   Depending on how you would like contacts to move through the flow after they receive the first email, you may want to [rejoin the splits](https://help.klaviyo.com/hc/en-us/articles/360002419512-Rejoin-a-Flow-Split) to streamline the experience. From here, you can follow our other [welcome series best practices](https://help.klaviyo.com/hc/en-us/articles/115002775172-Guide-to-Creating-a-Welcome-Series#take-your-welcome-series-to-the-next-level7).

   ## Additional resources

   - [How to create a welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172-Guide-to-Creating-a-Welcome-Series)
   - [How to create and target a segment of recent cart abandoners](https://help.klaviyo.com/hc/en-us/articles/360032334511-Create-a-Segment-of-Recent-Cart-Abandoners)
   - [Getting started with coupon codes in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005084727-How-to-Use-Coupon-Codes-in-Klaviyo)