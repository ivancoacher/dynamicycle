---
id: "30880678063899"
title: "How to message BigCommerce customers by storefront"
source_url: "https://help.klaviyo.com/hc/en-us/articles/30880678063899-How-to-message-BigCommerce-customers-by-storefront"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:38Z"
language: "en"
---
## You will learn

Learn how to message BigCommerce customers by storefront. If you are using BigCommerce Multi-Storefront (MSF), Klaviyo syncs a property called Channel ID with each order event that tells you which storefront a customer interacted with. This information is added to Klaviyo profiles, and can be used to segment customers in Klaviyo and send them targeted messaging.

## Before you begin

Make sure you’ve [integrated your BigCommerce store with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005082547) before continuing with this article.

Please note that not all aspects of Klaviyo’s BigCommerce integration are natively compatible with BigCommerce Multi-Storefront, including onsite tracking and sign-up forms. Klaviyo’s storefront-specific messaging capabilities are limited to profiles that have logged events with Channel ID, which are listed below.

## Data synced from BigCommerce

The Channel ID property indicates which BigCommerce storefront the customer interacted with.

Klaviyo syncs the Channel ID property from BigCommerce for the following events:

- Started Checkout
- Placed Order
- Ordered Product
- Fulfilled Order
- Canceled Order
- Refunded Order

  Any customer that has tracked one of the above events will have 2 Channel ID-related properties added to their Klaviyo profile:
- ****BigCommerce Original Channel ID****
  This property lists the ID of the first storefront visited by the profile.
- ****BigCommerce Channel IDs****
  An array of IDs that includes the ID of each storefront visited by the profile.

To determine which storefront corresponds to which Channel ID:

1. Place a test order on each of your storefronts.
2. In Klaviyo, navigate to ****Analytics > Metrics****.
3. Filter by **BigCommerce**.
4. Select the ****Placed Order**** event, then select ****Activity feed****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30880829241499)
5. For each of your test orders, click the 3-dot menu and select ****Activity details****. You’ll be able to see the Channel ID for the order.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30880829243419)
6. Make note of which test order/storefront corresponded to which Channel ID.

## Segment customers by storefront

You can create a segment for each of your storefronts by doing the following:

1. In Klaviyo, navigate to ****Audience >********Lists & segments****.
2. Select ****Create new > Create segment****.
3. Name your segment something descriptive (e.g., “[Storefront Name] Customers”).
4. For your first segment condition, select ****Properties about someone > BigCommerce Origin Channel Name > equals > [Channel ID of storefront]****. **Type** should be set to **Number**.
5. Add a second segment condition using **AND**. If you are looking to email these customers, this condition should be ****If someone can or cannot receive marketing > can receive > email marketing****. This ensures that customers in your segment can receive marketing emails.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30880829246875)
6. When you’re done, click ****Create segment****.

Please note that this segment looks at the first storefront that a customer visits.

### Customers without Channel ID tracked

You can also create another segment for BigCommerce customers where a Channel ID has not been tracked. This can happen if someone fills out a Klaviyo form on your BigCommerce site but has not started checkout, placed an order, etc. Your segment conditions will be ****Properties about someone > BigCommerce Origin Channel > is not set********AND********If someone can or cannot receive marketing > can receive > email marketing****. Make sure to set **Type** to **Text** for the first condition.

![](https://klaviyo.zendesk.com/hc/article_attachments/30880785555227)

## Message customers by storefront

If you want to only message subscribers for a specific storefront, you can create a [segment-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003040052) for one of the segments you created above, or [send a campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847) to that segment.

You can also message all of your subscribers, and customize that messaging by storefront. Below, learn how to create a set of welcome messaging by storefront, and how to create an abandoned cart flow personalized by storefront.

### Welcome series by storefront

To create a welcome series flow by storefront, you’ll want to adapt a [traditional welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172). First, you will need to create separate [segment-triggered flows](https://help.klaviyo.com/hc/en-us/articles/360003040052) welcoming customers, each triggered by one of your storefront segments above. Then, you can personalize each flow message to the specific storefront.

For customers who have subscribed to marketing but Channel ID has not been tracked, make sure to create an extra welcome series flow that is not specific to any storefront. This can happen if someone fills out a Klaviyo form on your BigCommerce site but has not started checkout, placed an order, etc.

### Abandoned cart by storefront

You can send personalized abandoned cart reminders to customers based on their associated storefront.

1. To create the flow, start with an [Abandoned Cart Reminder template](https://www.klaviyo.com/library/flows?object_id=JmMG2t). You’ll edit this template with conditional splits for each storefront.
2. After the 4 hour split, add a conditional split for the first storefront. Set the condition to ****BigCommerce Origin Channel > equals > [First Channel ID]****. Set **Type** to **Number**.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30880785557787)
3. The **Yes** path for this split should be the rest of the blocks from the original template. Customize the flow messages in this path to your first storefront. For the **No** path, you should add another conditional split with the same conditions, except it should be set to your second storefront.
4. The second **Yes** path should be a copy of the first **Yes** path’s content, except you should customize the message content to your second storefront.
5. Keep adding conditional splits in this manner for each storefront. When you get to the last one, the **No** path should end the flow with no further content. This is because each profile that tracks a **Started Checkout** event should have a Channel ID and be directed down one of the **Yes** paths.

![](https://klaviyo.zendesk.com/hc/article_attachments/30882230895387)

## Outcome

You’ve now learned how to segment your BigCommerce customers by storefront and send them targeted messaging.