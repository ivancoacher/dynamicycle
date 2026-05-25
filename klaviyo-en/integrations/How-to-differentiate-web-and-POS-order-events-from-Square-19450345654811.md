---
id: "19450345654811"
title: "How to differentiate web and POS order events from Square"
source_url: "https://help.klaviyo.com/hc/en-us/articles/19450345654811-How-to-differentiate-web-and-POS-order-events-from-Square"
section: "Square"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: "en"
---
## You will learn

Learn how to differentiate Point of Sale (POS) and web order events synced from Square to Klaviyo. Then, segment customers in Klaviyo based on whether they made orders in person or online to bring more personalization to your messaging.

## Before you begin

Before continuing, make sure you’ve [integrated your Square store with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/11117215837211).

## How data syncs from Square

Klaviyo’s integration with Square syncs both Square Online web order events and Square POS order events to Klaviyo.

Square POS order events will sync to Klaviyo if there is an email address and/or phone number associated with the order which the customer directly shared with your company.

Square events will have a property called **source name** that will show whether the event is from a POS or from online/web, so that you can segment these events in Klaviyo.

The Square events that include the **Source Name** property are as follows:

- ****Placed Order****
- **Refunded Order**
- **Cancelled Order**
- **Fulfilled Order**
- **Fulfilled Partial Order**

To learn more about event properties synced from Square, read our [Square data reference](https://help.klaviyo.com/hc/en-us/articles/11117271030555).

## How to segment POS and web customers

You can segment POS and web customers in Klaviyo using the **Source Name** property.

For example, create a segment of customers who have made at least one **Placed Order** via POS. This segment won’t exclude those who have also purchased online, but you can choose to exclude them if you want.

1. In Klaviyo, navigate to ****Lists & segments****.
2. Click ****Create new > Create segment****.
3. Name your segment and add any tags.
4. Create the following segment definition:
   **What someone has done (or not done) > Person has Placed Order > at least once > over all time > where Source Name equals POS**
5. Click ****Create segment****.

To create a segment of those who have made at least one purchase online, create the same segment but instead choose **Source Name** equals “Square Online”. You could also choose to exclude POS purchasers from this segment.
![Klaviyo segment builder with segment Square POS purchasers](https://klaviyo.zendesk.com/hc/article_attachments/28705699357467)

## Additional resources

- [Getting started with Square](https://help.klaviyo.com/hc/en-us/articles/11117215837211)
- [Square data reference](https://help.klaviyo.com/hc/en-us/articles/11117271030555)
- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)