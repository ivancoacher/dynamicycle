---
id: 16319809379611
title: "How to request reviews from your customers with Klaviyo Reviews flows"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16319809379611-How-to-request-reviews-from-your-customers-with-Klaviyo-Reviews-flows"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:48:52Z"
language: en
---

## You will learn

Learn how to configure key flows in Klaviyo to start acquiring customer reviews.

If you use a different reviews platform other than Klaviyo Reviews, learn how to [request reviews using a Klaviyo flow](https://help.klaviyo.com/hc/en-us/articles/115002779391#01H46MRZ7GEJV79PZ506FSSS3A).

## Key reviews flows

There are 2 key review flows:

- ****Review request flow****
  Ask a recent purchaser to review a product from their order. Consider offering an incentive (e.g., 15% off, free shipping on their next order, additional loyalty points), which may increase conversions. This flow is triggered by the **Ready to review** event.
- ****Review follow-up flow****
  If you offer an incentive (recommended) in exchange for customer reviews, deliver that reward once a review is submitted. This flow is triggered by the **Review submitted** event.

### About the **Ready to review** event

This metric is tracked when an item is delivered or fulfilled and meets the criteria you set to indicate an item is ready to be reviewed. Learn how to [customize the](https://klaviyo.zendesk.com/hc/en-us/articles/16682549669403) [**Ready to review**](https://klaviyo.zendesk.com/hc/en-us/articles/16682549669403) [metric](https://klaviyo.zendesk.com/hc/en-us/articles/16682549669403).

**Ready to review** events are only triggered for orders placed after you begin using Klaviyo Reviews. Learn how to [populate the](https://klaviyo.zendesk.com/hc/en-us/articles/25930166202651) [**Ready to review**](https://klaviyo.zendesk.com/hc/en-us/articles/25930166202651) [metric for past orders](https://klaviyo.zendesk.com/hc/en-us/articles/25930166202651).

## Create a review request flow

1. In Klaviyo, navigate to the ****Flows**** tab.
2. Click ****Create flow****.
3. Search for “Review request,” then select one of the ****Review Request: Klaviyo Reviews**** cards.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723523744027)
4. Click ****Use template****.
5. Adjust the flow messages to your liking.
6. Click ****Review and turn on**** in the top right corner.
7. Choose ****Live**** from the dropdown.
8. Click ****Save****.

Once you’ve completed these steps, your review request flow will begin sending to your customers as they [become eligible to submit reviews](https://help.klaviyo.com/hc/en-us/articles/16682549669403).

When someone submits a review by clicking the link in this flow message, they will appear with the **Verified buyer** badge on your site.

![verified buyer badge](https://klaviyo.zendesk.com/hc/article_attachments/28723545679387)

If you delete a product after sending a review request for it, recipients who click the email's CTA will see a message indicating the product has been deleted. They will not be able to submit a review for a deleted product.

### Adjusting the review request button

If you'd like to replace the default stars in the review request email, simply add a button to your flow email with the dynamic review request link tag in the **URL** field: {{ event.review\_link }}

## Create a review follow-up flow

If you offer an incentive in exchange for reviews, you must follow through and send them the reward, regardless of the content in their review. Even if you don’t offer an incentive, consider thanking the reviewer for their feedback and offering support if they had a negative experience.

1. In Klaviyo, navigate to the ****Flows**** tab.
2. Click ****Create flow****.
3. Search for “Review follow-up,” then select the ****Review Follow-up: Klaviyo Reviews**** card.
   ![Klaviyo reviews flow card](https://klaviyo.zendesk.com/hc/article_attachments/28723545674779)
4. Click ****Create Flow****.
5. Edit the flow messages to reflect your branding and the reward you’d like to offer.
6. Once your flow is complete, click ****Update Action Statuses**** and set the flow live.

### Add a coupon code (optional)

If you’d like to include an incentive in your review follow-up flow, use a personal coupon code built in Klaviyo.

1. Create a dynamic coupon code.
   1. Learn how to [create unique coupons for Shopify](https://help.klaviyo.com/hc/en-us/articles/115006155388).
   2. Learn how to [create unique coupons for WooCommerce](https://help.klaviyo.com/hc/en-us/articles/22168739689627).
2. Navigate back to the tab with your review follow-up flow.
3. Add the coupon code tag, `{% coupon_code 'NAME_OF_YOUR_COUPON' %}`, with the name of your coupon.

## The review submission form

When your customers click the CTA in your review request flow, they’ll first see an option to select a star rating. Once they select a star rating, they’ll see a form with the following fields:

- Email address
- Review text
- Upload photo (PNG and JPG formats are supported)
- Upload video (MP4 and MOV formats are supported)
- [Custom questions](https://help.klaviyo.com/hc/en-us/articles/16319181846171), if configured

Once the review is submitted, they’ll see a confirmation page with a link to edit their review. If they ordered more than 1 product, they will see the option to review up to 3 additional products from their order. Products are selected and ordered based on your [prioritization settings](https://help.klaviyo.com/hc/en-us/articles/16681935355163).

Reviewers can return to the original review request link for up to 30 days after they submit their review to edit it.

![](https://fast.wistia.com/embed/medias/3o55h7i4wu/swatch)

## Manually request reviews

You can request a review from a customer directly with a manual review request link.

These links are specific to the selected product. You can use a manually-generated review link in a campaign to past purchasers of that product, in customer service conversations, or anywhere else you contact past purchasers of a specific product.

1. Select the ****Reviews**** tab in Klaviyo.
2. Click on the ****Products**** tab.
   ![reviews product tab](https://klaviyo.zendesk.com/hc/article_attachments/28723523738523)
3. Click the 3 dot menu to the right of the product you’d like to request a review for.
4. Click ****Copy link to manual review****.
   ![Copy link to manual review button](https://klaviyo.zendesk.com/hc/article_attachments/30500966980123)
5. Share this link with a customer directly (e.g., by emailing them).

Choose ****Copy incentivized link to review**** if you are incentivizing the reviewer in any way (e.g., exchanging free product for reviews, offering discount codes, etc.) A review submitted via this link will be marked as **Incentivized** in your review widgets.

## Get notified about new reviews

Set up email notifications whenever someone reviews one of your products.

Enabling new review notifications means you’ll also be notified whenever someone asks a question. It is not possible to subscribe exclusively to new review notifications.

1. Navigate to the ****Reviews**** tab in Klaviyo.
2. Click ****Reviews settings****.
3. Select ****Publishing rules and notifications****.
4. Under **Notifications**, check the box next to **Pending activity (reviews and Q&As)**.
5. Choose a frequency (immediately, daily, or weekly) and delivery timing.
   ![reviews notifications settings](https://klaviyo.zendesk.com/hc/article_attachments/28723545682459)
6. Choose one or more notification recipients from your list of account users
   Notifications will be sent to them when someone submits a review or product question.

   Notifications can only be sent to account users. If you’d like to send notifications to someone you don’t see in the dropdown, [invite them to join your Klaviyo account](https://help.klaviyo.com/hc/en-us/articles/360053547071).
7. Optionally, check the box next to **Weekly stats summary** for a weekly report on your product reviews. This can be sent to a different user (or users) than those who are selected for review notifications.
8. Click ****Save changes****.

Once you receive reviews, you can optionally [add a public reply](https://help.klaviyo.com/hc/en-us/articles/20817781267739) to each one (e.g., thank a reviewer for their feedback or apologize for a frustrating experience).