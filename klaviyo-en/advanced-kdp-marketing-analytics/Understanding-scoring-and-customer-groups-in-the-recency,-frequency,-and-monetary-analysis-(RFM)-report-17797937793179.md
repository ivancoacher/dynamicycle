---
id: "17797937793179"
title: "Understanding scoring and customer groups in the recency, frequency, and monetary analysis (RFM) report"
source_url: "https://help.klaviyo.com/hc/en-us/articles/17797937793179-Understanding-scoring-and-customer-groups-in-the-recency-frequency-and-monetary-analysis-RFM-report"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:56:44Z"
language: "en"
---
## You will learn

Learn how to understand the recency, frequency, and monetary scores and customer groups are derived in the RFM report.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

For more information about building and customizing your report, head to our guide on [getting started with the RFM report](https://help.klaviyo.com/hc/en-us/articles/17797889315355).

## Before you begin

To qualify for this report, your account must:

- Have at least 500 customers who have placed an order.

  This does not refer to total profiles, but rather the number of people who have actually made an order with your business. Note that if this section is on a profile but is blank, Klaviyo doesn’t have enough data on that individual to make a prediction.
- Have an ecommerce integration (e.g., Shopify, BigCommerce, Magento, etc.) or use the Klaviyo API to send placed orders.
- Have at least 180 days of order history and have orders within the last 30 days.
- Have at least some customers who have placed 3 or more orders.

Only Owners, Admins, Managers, and Analysts can access this report. Additionally, if you have created a [new custom metric](https://help.klaviyo.com/hc/en-us/articles/22311085738395/) to use in your RFM report, it may take up to 48 hours for this change to be reflected in your data.

## RFM definitions

RFM metrics are common terms used in marketing and data strategies. Within Klaviyo, they are defined and calculated as the following:

- ****Recency****
  How long ago a customer purchased from your company. Recency is expressed as the elapsed time (measured in the number of days) since a last purchase within your report’s time frame.
- ****Frequency****
  How often a customer purchases from your company within your report’s time frame.
- ****Monetary value****
  How much a customer has spent in your account (past purchases).

If you need to refer back to these definitions, you can find them in the RFM report's advanced settings by navigating to ****Advanced settings > About RFM****from the RFM report.

## Understanding percentiles, scoring, and customer groups

### Percentiles and scoring

For a given customer, Klaviyo will determine their percentile among all customers for recency, frequency, and monetary value. Once those percentiles are determined, Klaviyo then assigns the customer a score of 1-3 for each (recency, frequency, and monetary).

Note that only Klaviyo only looks at orders with a positive value. If an order is free (e.g., has 100% discount), it is not considered in the RFM analysis.

By default, scores will be assigned using thresholds that are unique to your account. These include:

- ****Recency scoring****
  - Customer’s most recent purchase was within the last 180 days: 3 score assigned
  - Customer’s most recent purchase was within the last 365 days: 2 score assigned
  - Customer’s most recent purchase was outside of the last 365 days and indicates that they are unlikely to ever purchase again: 1 score assigned
- ****Frequency scoring****
  - Top 33% (usually 3 or more purchases): 3 score assigned
  - Middle 33%, but less than the 66 percentile (usually 2 purchases): 2 score assigned
  - Bottom 33% of users (usually a single purchase): 1 score assigned
- ****Monetary scoring****
  - Top 33%: 3 score assigned
  - Middle 33%: 2 score assigned
  - Bottom 33%: 1 score assigned

### Customer groups

Once a score is determined for each RFM metric, these scores are brought together to determine the customer group.

The model below visualizes how these 3 scores are blended together to determine your potential customer buying group. All RFM metrics and their scores (1-3) can be visualized on this cube and where they fall within each of its sides or quadrants. For example, the top green corner of the model illustrates a customer who has earned the top score of 3 for all RFM metrics.

![rfm cube.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716057240219)

Once Klaviyo brings these 3 scores together, they are then categorized and lined up to a customer group. This customer group describes their present buying habits and is a helpful way to understand which customers are repeat buyers, who may need a nudge for future purchases, who is potentially a churn-risk, etc. The chart below illustrates this logic including:

- Customer group name
- Groups split (i.e., what individual RFM scores contribute to this group)
- General description of the customers in this group
- Suggested actions for this customer group

If you ever need to refer to these customer groups and definitions, you can find them within the RFM report itself. Click ****Advanced settings**** > ****About RFM**** for more information.

|  |  |  |  |
| --- | --- | --- | --- |
| ****Group name**** | ****Possible score breakouts (listed from left to right in RFM order)**** | ****Description**** | ****Examples of potential actions/strategies for this group**** |
| ****Champions**** | 333, 332, 323 | ****Your best customers**** They purchased recently. They also purchase often, and spend the most. | - Invite them to a customer advisory board. - Send them rewards or coupons for their loyalty. - Get reviews from them. - Make sure they are in your “VIP” or similar segment. - Invite them first to sales, promotions, etc. |
| ****Loyal**** | 321, 322, 331, 232, 233 | ****Valuable customers that are engaged**** They purchased somewhat recently or purchase often. but they spend less than their **Champion** counterparts. | - Send them rewards or coupons for their loyalty. - Use cross-selling or up-selling of similar past purchases or popular products. - Get reviews from them. - Invite them to sales, promotions, etc. right after your **Champions**. - Encourage or remind them to restock items or past purchases. - Make sure they are signed up for SMS/MMS. |
| ****Recent**** | 312, 313, 311, 222, 223 | ****Recent customers**** They may have purchased recently, but they do not tend to purchase frequently. | - Convert them to a subscription so that they become a **Champion** or **Loyalist**. - Offer them a promotion to order and try to convert them. - Encourage or remind them to restock items or past purchases. - Use cross-selling or up-selling of similar past purchases. - Provide testimonials or reviews from your **Champions** or **Loyal** to encourage purchases. |
| ****Needs attention**** | 213, 221, 123, 132, 133 | ********A valuable customer that has not******** ****purchased recently**** They may have spent a lot or bought frequently in the past, but have not purchased recently. | - Let them know about new product releases. - Try a winback campaign to re-engage them. - Offer them an exclusive promotion or coupon (especially time-limited promotions). - Personalize product recommendations based on what they purchased in the past. - Encourage or remind them to restock items or past purchases. |
| ****At risk**** | 231, 212, 122, 131, 211 | ****A customer that has not purchased recently and/or tend to spend less overall**** They may have purchased in the past, but have not purchased recently. They spent less than their **Needs attention** counterparts. | - Try a winback campaign to re-engage them. - Offer them an exclusive promotion or coupon (especially time-limited promotions). - Personalize product recommendations based on what they purchased in the past. - They may be more price sensitive than the **Needs attention** group**,** so target with more affordable products. - Try not to over-message as they are a churn-risk. |
| ****Inactive**** | 111, 112, 113, 121 | ****A lapsed customer**** An infrequent customer who hasn’t purchased in a long time. | - Try a winback campaign to re-engage them. - Offer them an exclusive promotion or coupon (especially time-limited promotions). - If they are unengaged (especially if they do not interact with your winback or promotional emails), consider list-cleaning and removing them before they harm your deliverability. |

## Additional resources

[Getting started with the recency, frequency, and monetary (RFM) analysis report](https://help.klaviyo.com/hc/en-us/articles/17797889315355)

[How to build a segment using RFM properties](https://help.klaviyo.com/hc/en-us/articles/18193920339483)

[How to strategically use RFM properties in campaigns and flows](https://help.klaviyo.com/hc/en-us/articles/18194102384539)