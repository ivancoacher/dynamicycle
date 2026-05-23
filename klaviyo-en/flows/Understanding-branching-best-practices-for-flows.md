---
id: 360051182592
title: "Understanding branching best practices for flows"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360051182592-Understanding-branching-best-practices-for-flows"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:51Z"
language: en
---

## You will learn

Learn about targeting different groups based on what they've done in order to provide a more relevant experience for each recipient. This can be especially valuable for flows, as your communications will feel more personalized to each person. In this article, we run through various ways you can branch flows in order to create a more personalized experience for your recipients.

## Branching by purchasers vs. non-purchasers

Messaging existing customers and non-customers differently is a good practice, especially if you plan on offering an incentive in your welcome or abandoned cart flow. You don't want to over-discount, so you may want to only offer a coupon code to shoppers who have never purchased from you before to encourage them to buy for the first time.

If you take this approach, be sure to include language like, "Take 10% off your first purchase" so that recipients don't grow to expect a discount every time they abandon a cart. Additionally, use dynamic coupon codes to prevent sharing on sites like RetailMeNot, etc.

Learn more about [how to use coupon codes in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005084727).

To split your flow by purchasers versus non-purchasers:

1. Drag a conditional split into the top of your flow.
2. Set this split to be based on **What someone has done or not done >****Has Placed Order at least once over all time.** People who have never placed an order before will go down the NO path while existing customers will go down the YES path.
   ![Conditional split configured to check 'Has Placed Order at least once over all time'.](https://klaviyo.zendesk.com/hc/article_attachments/28720893467675)
3. You can include a coupon in the final message of the NO path.

## Branching by domestic vs. international shoppers

You may be able to offer special perks to domestic customers that you don't to international customers, like free shipping. Branching your flow by domestic versus international customers allows you to highlight these perks to domestic customers to persuade them to purchase.

1. Drag a conditional split to the top of the flow.
2. Set this split to be based on **Properties about someone > Country equals US.** Those who flow down the YES path will be domestic customers, and those on the NO path are international.
   ![Conditional split configured to check 'Country equals USA'.](https://klaviyo.zendesk.com/hc/article_attachments/28720848421403)

## Branching by product category or collection (metric-triggered only)

If you have a large product offering, you may want to branch a metric-triggered flow (e.g., an abandoned cart or browse abandonment) by category or collection to include more relevant copy in your emails. One key example is if you sell men's and women's products. In this case, it's also important to include a default branch in case the product in someone's cart is not in either the men's or women's collection.

1. Drag a trigger split to the top of the flow.
2. Set the collection (or "category," depending on your ecommerce integration) to contain Women's.
3. Drag another trigger split directly beneath the first one.
4. Set this collection to contain Men's. Those who flow down NO path after this trigger split should receive a more generic message.

## Additional resources

Find out more about [flow branching](https://help.klaviyo.com/hc/en-us/articles/115003883992) in this guide.

Read about flows where you can use these branching ideas:

- [Browse abandonment](https://help.klaviyo.com/hc/en-us/articles/115002775252)
- [Abandoned cart](https://help.klaviyo.com/hc/en-us/articles/115002779411)
- [Welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172)