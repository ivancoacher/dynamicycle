---
id: 28114865573915
title: "How to use a campaign to request reviews"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/28114865573915-How-to-use-a-campaign-to-request-reviews"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:44Z"
language: en
---

## You will learn

Learn how to use a campaign to request verified reviews from past purchasers. This process involves creating a segment of people who purchased a product, then sending them a campaign with a review request link.

Only request reviews for one product per campaign. The review request link used in this process is product-specific, so make sure to send your campaign to people who purchased that product. If you’d like to request reviews for multiple products, use multiple campaigns.

## Create a segment of potential reviewers

In order to build your segment, you’ll first need to locate the product ID.

1. Navigate to ****Content > Products****.
2. Find the product you’d like to request reviews for.

   You can only request reviews for one product per campaign. If you’d like to request reviews for multiple products, send multiple campaigns to different segments.
3. Copy the product ID from the **Item ID** column.
   ![The item ID column in the reviews product tab](https://klaviyo.zendesk.com/hc/article_attachments/28717888604443)

   Then, create your segment:
4. Navigate to ****Lists & segments****.
5. Select ****Create new****.
6. Select ****Create segment****.
7. Give the segment a descriptive name, like “Potential reviewers for [product name]”
8. Create this segment:
   What someone has done (or not done) > Fulfilled Order > at least once in the last 90 days > where Items contains [your item]
   AND
   What someone has done (or not done) > Submitted review > zero times over all time > where product\_external\_id = [your product ID]
   ![A segment of people who have ordered a certain product in the last 90 days but haven't ever left a review](https://klaviyo.zendesk.com/hc/article_attachments/28717888598683)
9. Click ****Create segment****.

You can adjust the time frame for this segment based on your business needs. Use a time frame that includes anyone who might have helpful feedback, but excludes those who purchased the product too long ago to recall details about their experience.

## Send a campaign to request reviews

To create a campaign, first copy the manual review request link. You’ll use this for your campaign’s CTA.

1. Navigate to ****Reviews****.
2. Select ****Products****.
3. Find the product you’d like to request reviews for. Make sure to use the same product used in your segment definition.
4. Open the three dots (additional options) menu.
5. Select ****Copy link to manual review****.

![Option to copy a link to leave a manual review](https://klaviyo.zendesk.com/hc/article_attachments/28717882522907)

Once you’ve copied the review request link, [create a campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847) and use this link in your CTA (e.g., a featured button or text link). Then, send the campaign to the segment you created in the last step.

If you’re sending multiple review request campaigns around the same time, make sure to exclude segments you’ve sent to recently so that subscribers aren’t bombarded with review requests.

## How are reviews verified?

It’s important to send review request campaigns only to people who actually purchased the product you’re requesting a review for. When someone submits a review after clicking the link in your campaign, Klaviyo will check their order history to see if they actually purchased the product they reviewed. If they have not purchased the product (or if their order hasn’t yet been fulfilled), the review will ****not**** be verified. If they have purchased the product within the last 5 years, the review ****will**** be verified.

## Follow up on campaign reviews

If you offer an incentive in your review request campaign, use a flow to deliver that incentive and thank them for their review. If the incentive you offered is the same as your standard review request flow, you don’t have to take any additional action: all reviewers will be routed to your review follow-up flow. However, if you offered a different incentive, you’ll need to create a separate flow.

In your standard review follow up flow, add this profile filter:

What someone has done > Received email > where Campaign Name = [your campaign name] > zero times over all time

![A flow filter to exclude those who have received your review request campaign](https://klaviyo.zendesk.com/hc/article_attachments/28717882527003)

This filter will exclude recipients of your campaign from receiving your standard review follow up flow.

Then, [clone your review follow-up flow](https://help.klaviyo.com/hc/en-us/articles/24898429283739). Change the profile filter to use this criteria instead:

What someone has done > Received email > where Campaign Name = [your campaign name] > at least once over all time

![A flow filter to include those who have received your review request campaign](https://klaviyo.zendesk.com/hc/article_attachments/28717882517787)

Adjust the flow message(s) to use the incentive offered in your review request campaign, then set it live. A few weeks after your campaign is sent, turn the new flow off and remove the filter from the old flow; that way, campaign recipients who submit a later review for a different product won’t receive the wrong flow message.