---
id: "18194102384539"
title: "How to strategically use RFM properties in campaigns and flows"
source_url: "https://help.klaviyo.com/hc/en-us/articles/18194102384539-How-to-strategically-use-RFM-properties-in-campaigns-and-flows"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: "en"
---
## You will learn

Learn how to use RFM (recency, frequency, and monetary) properties to target specific types of campaigns and content to your customer groups. Either by using the profile properties themselves or by using a segment with the RFM properties, you can tailor your marketing even further.

## Before you begin

If you have created a [new custom metric](https://help.klaviyo.com/hc/en-us/articles/22311085738395/) to use in your RFM report, it may take up to 48 hours for this change to be reflected in your data.

You have a few options for how to use RFM segments in your campaigns and flows:

- [Segment conditions to target and tailor your campaigns.](#h_01H8HV9J7NYSK3CC79CSZMHZ3Y)
- [Variables with conditional logic in your email templates.](#h_01H8HVAAFVGHZ6JYX59WDCYT70)
- [Properties to target and tailor your flows.](#h_01H8HVCA3XCRTVTGB2VSGJA84V)

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Use segments to tailor your campaigns

You can use segments that have RFM properties (**Current RFM group** or **Previous RFM group**) to target customers of certain groups. This is especially helpful as Klaviyo has already done the work of categorizing who these customers are based on their historical purchase behavior.

Examples of using segments in campaign sends could include:

- Targeting **Loyal** and **Champion** customers to provide reviews on items
- Targeting **Loyal** or **Recent** customers with new products or product offers to cross-sell and up-sell
- Targeting **Recent** customers with a subscription so that they become a **Champion** or **Loyalist**
- Targeting **Inactive** or **At Risk** customers with winback campaigns
- Targeting **Inactive** or **At Risk** customers with entry-level or lower cost items
- Offering exclusive or time-limited discounts to **Inactive** or **At Risk** customers

## Use RFM properties as variables in your email templates

Using RFM properties (**Current RFM group** or **Previous RFM group**) as variables within email templates can help to further personalize emails to your specific customer groups. You can [dynamically display a block, text, or custom content](https://help.klaviyo.com/hc/en-us/articles/7655965301531) to a certain customer group, and even [show or hide](https://help.klaviyo.com/hc/en-us/articles/7655926841499) these based on the group.

To show or hide a block based on someone’s group membership, use the example conditional statement below.

![](https://klaviyo.zendesk.com/hc/article_attachments/30443775215131)

Examples of using variables in email sends could include:

- Personalizing the products that certain customer groups see vs. others by product value or type. For example, **Champions** or **Loyal** customers see higher value items vs. **Inactive** or **At Risk** that see more entry level items.
- Discounts appear for certain customer groups, such as **Needs Attention**, **Inactive**, or **At Risk** to encourage purchases.
- Showing a section about leaving product reviews to those only in the **Champions** or **Loyal** groups.
- Showing lower priced products to those in **Needs Attention** or **At Risk** to encourage purchases.
- Having loyalty points information:
  - For those in **Champions, Loyal, Recent, and Needs Attention** groups show their tier or status.
  - For those in **Inactive** or **At Risk** explain your loyalty program and value they will receive after purchases.

## Using RFM properties as variables in flows

### Metric-triggered flows

In your metric-triggered flows, use your RFM properties (**Current RFM group** or **Previous RFM group**) [as dynamic variables](https://help.klaviyo.com/hc/en-us/articles/4408802648731) to personalize a customer’s messaging journey with your brand. This is especially helpful to help create messaging that certain customer segments will receive vs. the others.

Examples of using variables ("personalization tags") in flows could include:

- Creating a [conditional split](https://help.klaviyo.com/hc/en-us/articles/115003883992) based on if a person is either:
  - A frequent purchaser (**Champions or Loyal).**
  - A sometimes or never purchaser (**Recent, Needs Attention, Inactive, or At Risk**).
- Creating a conditional split based on a customer group’s recent browsing behaviors.
  - For example, those in **Champions, Loyal,** or **Recent** may get a regular browse abandonment message, while those in **Needs Attention, Inactive, or At Risk** receive a browse abandonment message with an additional discount.
- Creating a flow for those in the **Champions, Loyal**, or **Recent** group highlighting new products or launches.
- Encouraging those in the **Champions, Loyal**, or **Recent** group to leave reviews of their products.

### Segment-triggered flows

Slightly different from the above, you can use [RFM-based segments to launch a segment-triggered flow](https://help.klaviyo.com/hc/en-us/articles/25408596027547) based on a group's change in status. For example, sending messages to profiles who have recently become a **Champion** or have fallen into the **Needs Attention** group.

Examples of using RFM-based segments in flows could include:

- Targeting customers in the **Needs Attention** or **At Risk** groups with time-limited discounts or welcome-back incentives.
- Reaching out to those who recently became **Champions** or Loyal customers with “thank you” messaging. You could include a special promotion just for them or welcome them to another tier of your loyalty program.
- Trying to cross-sell new or highly rated products to those who recently became **Champions** or **Loyal** customers.

Following up with post-purchase messaging for those who just entered the **Recent** group with a time-limited discount to purchase another product.

## Using custom metrics with RFM data

[Custom metrics](https://help.klaviyo.com/hc/en-us/articles/22311212640027) allow you to create metrics that align with how your business and data functions. Using custom metrics in the RFM report ensures that you are capturing all data that accurately reflects your business model and how you define your customer groups.

Below are some examples of common use cases:

- ****Combine all sources of placed orders or revenue for RFM analysis****
  Combine revenue from all of your non-Klaviyo integrations, systems (e.g., point of sale), and data tools to ensure that you have the most holistic and recent portrait of your customers spending habits.
- ****Remove subscription events from counting in RFM analysis****
  Standard Shopify integrations, WooCommerce, and BigCommerce will include subscriptions in **Placed Order** events automatically. You can set up a custom metric to remove these so that you only capture one-time orders. This may be helpful if you want to evaluate customer behaviors based only on product sales, not including recurring subscriptions.
- ****Only focus on online buying habits for RFM analysis****
  With Shopify and some custom integrations, physical retail (POS) and e-commerce orders will come through as a single event (e.g., Shopify **Placed Order** event). You may want to create a custom metric that removes these POS events, so that you can focus on online sales only. This may be helpful if you want to target customers with special online promotions, shipping information, online-only products, etc.

## Additional resources

- [Getting started with the recency, frequency, and monetary (RFM) analysis report](https://help.klaviyo.com/hc/en-us/articles/17797889315355)
- [Understanding scoring and customer groups in the recency, frequency, and monetary analysis (RFM) report](https://help.klaviyo.com/hc/en-us/articles/17797937793179)
- [How to build a segment using RFM properties](https://help.klaviyo.com/hc/en-us/articles/18193920339483)