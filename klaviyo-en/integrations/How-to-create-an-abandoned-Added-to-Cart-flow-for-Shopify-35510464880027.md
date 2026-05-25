---
id: "35510464880027"
title: "How to create an abandoned \"Added to Cart\" flow for Shopify"
source_url: "https://help.klaviyo.com/hc/en-us/articles/35510464880027-How-to-create-an-abandoned-Added-to-Cart-flow-for-Shopify"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:41Z"
language: "en"
---
Learn how to create an abandoned cart flow triggered by the Shopify **Added to Cart** event. The default Klaviyo abandoned cart flow is triggered by the Shopify **Checkout Started** event, whereas the **Added to Cart** abandoned cart flow targets more casual shoppers who have yet to start checkout.

## Before you begin

In order to enable this flow, you'll need to [enable the Klaviyo app embed](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01J6F7TREZM0NY2336G80MJFM3) and check the integration setting **Track behavioral events**in order to track the **Added to Cart** event in Shopify.
![](https://klaviyo.zendesk.com/hc/article_attachments/35510459309467)

## Create the flow

To enable this flow, we recommend using the pre-built flow available in Klaviyo's flow library:

1. Navigate to Klaviyo’s [flow library](https://www.klaviyo.com/library/flows).
2. Click into the "Prevent lost sales" goal section.
3. Select an ****Abandoned Cart Reminder,**** ****Shopify**** ****Added to Cart Trigger**** flow. There are two options: email only, or email and SMS.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35545007778843)
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35545007792539)
4. If you enabled behavioral tracking, this flow will be ready to go with all the recommended filters and dynamic email content ready to power personalized cart followup messaging.

## Are you using Klaviyo's Amazon Buy with Prime integration?

If you're using Buy with Prime to power payment and fulfillment for any of the products on your store, and you've [integrated Klaviyo and Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467), make sure to do the following:

For your abandoned "Added to Cart" flow, add the following flow filters to exclude customers who started checkouts or made purchases via Buy with Prime from receiving incorrect messaging:

- **Started Checkout** (Buy with Prime) **zero times since starting this flow** AND
- **Placed Order** (Buy with Prime) **zero times since starting this flow.**

## Outcome

You have now enabled an abandoned **Added to Cart** flow for Shopify.

## Additional resources

[How to create an abandoned cart flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)

[How to enable onsite tracking for Shopify](https://klaviyo.zendesk.com/hc/en-us/articles/4425956184731)