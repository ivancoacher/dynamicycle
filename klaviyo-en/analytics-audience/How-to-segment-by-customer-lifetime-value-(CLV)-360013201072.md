---
id: "360013201072"
title: "How to segment by customer lifetime value (CLV)"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360013201072-How-to-segment-by-customer-lifetime-value-CLV"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:56:50Z"
language: "en"
---
## You will learn

Learn how to create a customer lifetime value (CLV) segment and export any key CLV information. CLV is part of Klaviyo's [predictive analytics](https://help.klaviyo.com/hc/en-us/articles/360020919731-Guide-to-Klaviyo-s-Predictive-Analytics) and can be a powerful tool to use in segmentation. It is the total amount, both past and predicted, that a customer will purchase from your brand over time. CLV segments allow you to group customers based on this amount so that you can send them relevant content and trigger segment-based flows. For example, you can use historic CLV to build a VIP welcome flow or use predicted CLV to send targeted campaigns to customers who will likely spend a certain amount over the course of a year.

## Before you begin

Please note that you will only be able to segment based on CLV if:

- At least 500 customers have placed an order. This does not refer to Active Profiles, but rather the number of people who have actually made a purchase with your business. If this section is on a profile but is blank, this means we don't have enough data on that individual to make a prediction.
- You have an ecommerce integration (e.g. Shopify, BigCommerce, Magento) or use our API to send placed orders.
- You have at least 180 days of order history and have orders within the last 30 days.
- You have at least some customers who have placed 3 or more orders.

## Create a CLV segment

To create a segment based on any of the available CLV properties (i.e., historic, predicted, and total CLV), use the **Predictive analytics about someone** condition. Then, select your desired metric and value.

![A segment of customers with a CLV over 100](https://klaviyo.zendesk.com/hc/article_attachments/28722556838299)

### Example

Let's say your average order value for customers is around $15. You may want to target customers who are unlikely to reach this average order value with discounts to push them toward their next purchase.

To accomplish this, create a segment of customers who are predicted to spend no more than $5 and target them with a discount campaign or flow — similar to a [winback](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192) or re-engagement campaign. When targeting via email, you will want to include the following conditions:

- They belong to your main email list (in this case, a newsletter list)
- They have opened an email in a given amount of time to ensure that you send to engaged subscribers (in the example below, the timeline is the last 90 days)

![Low predicted CLV.png](https://klaviyo.zendesk.com/hc/article_attachments/28722556847515)

## Export CLV segments

[Exporting CLV data](https://help.klaviyo.com/hc/en-us/articles/115005078687) can allow you to further analyze and predict the behavior of different groups of customers. In addition to your CLV and predictive analytics values, you'll be able to export **Churn Risk Prediction**. Churn risk will be exported into your CSV as a number between 0 and 1. For example, 0.45 would correspond to a 45% churn risk.

![Select CLV metrics.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722556850459)

If you have a large number of one-time purchasers, you may have a high average churn risk. To lower your average churn risk, you may want to focus your marketing efforts on retaining customers after their first purchase. You can use Klaviyo's Predicted CLV metric to identify people who are not likely to purchase again as outlined in the example above.

Once you export this data as a CSV, you'll be able to run your own analyses. Some calculations you may be interested in include:

- ****Average CLV****You can calculate the average customer value of a segment by averaging Historic CLV and Total CLV.
- ****Predict future spending of a segment****Sum the Predicted CLV of all members of a segment and you will get the expected revenue from customers in this segment for the next year.
- ****Estimate the number of returning customers****First, average the values for Churn Risk Prediction. Then, subtract this average from 1. Multiply the result by the number of people in the segment. This will yield the number of customers who are predicted to return.

## Additional resources

- Course: [Mitigate churn with predictive insights and custom CLV](https://academy.klaviyo.com/mitigate-churn-with-predictive-insights-and-custom-clv/1791769)
- [Guide to Klaviyo's predictive analytics](https://klaviyo.zendesk.com/hc/en-us/articles/360020919731)