---
id: 115005253248
title: "How to differentiate Shopify POS and Shopify web data"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005253248-How-to-differentiate-Shopify-POS-and-Shopify-web-data"
section: "Shopify troubleshooting"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:39Z"
language: en
---

## You will learn

Learn how to distinguish between your POS and web orders in Klaviyo, if you use the [Shopify point of sale (POS)](https://www.shopify.com/pos) system. This is done through filtering orders or creating segments. Klaviyo syncs the `source_name` when a customer completes the checkout process and creates an order in your Shopify store, which records the source of the order.

According to Shopify's documentation, "source\_name" is defined as: "Where the order originated. May only be set during creation, and is not writeable thereafter. Orders created through official Shopify channels have protected values that cannot be assigned by other API clients during order creation. These protected values are: "web", "pos", "iphone", and "android". Orders created via the API may be assigned any other string of your choice. If source\_name is unspecified, new orders are assigned the value "api"."

## Before you begin

#### Knowledge check

If you have not already, read our guide on [getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating, before continuing with this article.

## Filter orders by source

You can filter **Placed Order** events in Klaviyo by "web," "pos," "iphone," "android," or other custom strings by using the source\_name property associated with a given order. In Klaviyo, this property will appear as simply "Source Name" when you are building a segment or flow filter.

To filter and view exclusively POS **Placed Order** events:

1. In Klaviyo, select the ****Analytics**** dropdown and click ****Metrics****.
2. Click on the **Placed Order** metric from Shopify.
3. Select the **Filter by** dropdown and choose ****Source name,**** then choose ****pos**** from the **equals** dropdown. **![Shopify Placed Order metric in Klaviyo's Metrics tab filtered by Source Name equals Select a Value](https://klaviyo.zendesk.com/hc/article_attachments/28713328870555)**

## Segment orders by source

In the segment builder, you can create segments based on the ****Source Name****property. For example, here is a segment of customers who have placed a POS order:

1. In Klaviyo, navigate to ****Audience > Lists & Segments****.
2. Click ****Create List/Segment**** and select ****Segment****
3. Create a segment with the following conditions:
   - Name: POS Orders
   - Tags: None
   - What some has done (or not done) > Has Placed Order > at least once > over all time
   - Where Source name > equals pos
     ![Klaviyo segment builder showing segment named POS Orders, Create Segment with black background and Cancel with white background](https://klaviyo.zendesk.com/hc/article_attachments/28713328875291)

## Outcome

You've now learned how to differentiate Shopify web orders from POS orders.

## Additional resources

- [Getting started with Shopify](https://klaviyo.zendesk.com/hc/en-us/articles/115005080407)
- [Getting started with segments](https://klaviyo.zendesk.com/hc/en-us/articles/115005237908)