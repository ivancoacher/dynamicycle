---
id: "360020919731"
title: "Understanding Klaviyo's predictive analytics"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360020919731-Understanding-Klaviyo-s-predictive-analytics"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:56:51Z"
language: "en"
---
## You will learn

Learn more about the different types of predictive analytics data displayed in your account, the various ways Klaviyo computes this, and guidelines for how you can utilize this data.

If applicable, you may want to adjust what metrics are used to calculate predictive analytics and better align them with your business goals, data structure, or custom integration. To adjust what metrics map globally in your account, head to the [guide on metric-mapping](https://help.klaviyo.com/hc/en-us/articles/25829057055899).

Klaviyo applies a combination of data science and machine learning techniques to all of the data in your account to bring you useful and actionable insights.

Please note that you will only see the **Predictive Analytics** section on profiles if you meet the following conditions:

- ****At least 500 customers have placed an order.****
  This does not refer to total profiles, but rather the number of people who have actually made an order with your business. These orders cannot be cancelled or refunded, and must be non-zero value orders. If this section is on a profile but is blank, this means we don't have enough data on that individual to make a prediction.
- ****You have an ecommerce integration (e.g., Shopify, BigCommerce, Magento, or WooCommerce) or use our API to send placed orders.****
- ****You have at least 180 days of order history and have orders within the last 30 days.****
- ****You have at least some customers who have placed 3 or more orders.****

![Video explaining how to target at-risk customers with predictive analytics” aria-hidden=](https://fast.wistia.com/embed/medias/v8zch9lizh/swatch)

## The predictive analytics section of a profile

You can find the **Predictive analytics** section of a profile on the **Metrics and insights** tab of a profile.  Below is an example of the **Predictive analytics** section of a contact's profile, and the information displayed:

![Predictive analytics card on Metrics and insights tab](https://klaviyo.zendesk.com/hc/article_attachments/28705636671515)

The table below defines the predictive analytics fields shown above. Note that, CLV stands for Customer Lifetime Value.

|  |  |  |
| --- | --- | --- |
| ****Field**** | ****Definition**** | ****Example Value from Screenshot**** |
| Historic CLV | The total value of all previous orders an individual has made, taking into account any refunds and returns. | $401 |
| Predicted CLV | A prediction of how much money a particular customer will spend in the next year. | $99 |
| Total CLV | The sum of historic CLV and predicted CLV. | $500 |
| Churn Risk Prediction | The probability of a customer churning is based on their number and frequency of orders. Each time the customer makes an order, their churn probability goes down (green), but as time elapses between orders, the churn probability increases (red), with a medium churn risk represented in yellow. | 21% |
| Average Time Between Orders | The average number of days between each of a customer's orders. | 75 days |
| Predicted Gender | Predicted gender is also a part of Klaviyo's predictive analytics features, however, this will not show in a customer profile. | N/A |

## How CLV data is calculated

Klaviyo automatically builds a Customer Lifetime Value (CLV) model using your company’s data and retrains the model at least once a week.

If you're using the custom API to send placed order events, you will need to confirm that your order value passes through a $value field. This will ensure that you gain CLV data based on your placed order events. Note that the $value needs to be the actual order value in order to calculate CLV correctly.

While no one can predict the future with absolute certainty, Klaviyo's predictive analytics features are powerful tools for optimizing marketing spending and personalizing customer communication. However, predictions work best when averaged over many customers and are not expected to be exact for any single individual. While some individuals will spend more than their predicted CLV and some will spend less, as a whole, they will average each other out.

For example, the Predicted CLV value displayed in the predictive analytics box is not an exact prediction. In some cases, you may see an impossible number of predicted orders. For example, you may see 1.43 as the number of predicted orders for a particular customer. When you see this, it means we expect the customer to make one or two orders, but there’s also a chance that they'll make more or fewer. These expectations start to make sense when you group multiple customers together because you can predict the total number of orders or spend for the group. If we have five customers with a predicted number of orders of 1.43, 0.25, 3.12, 0.78, and 2.97, we can expect approximately 9 orders across this group.

## How expected date of next order is calculated

**Expected Date of Next Order** takes into account the specific customer’s order behavior and the order behavior of all of your customers. If the customer’s orders exhibit a pattern, Klaviyo recognizes this pattern and will make a prediction based on it. If the customer’s orders don’t exhibit a pattern or if we don’t have enough data on the customer, Klaviyo will make a reasonable prediction based on how your other customers behave.

### FAQ about repeat purchase nurture series flow

****Do I need to add past profiles into this flow? Do I need to tell the flow to populate with all possible profiles moving forward?****

You don’t need to add past profiles for existing profiles or tell the flow which profiles to include, it will figure this out for you. Every customer who places an order with you has an expected date of next order. Profiles who have never placed an order with you before will not have an expected date of next order.

****I saw the flow has a conditional split. How do we know the expected date for one-time purchasers?****

For one-time purchasers, since we don’t know much about their purchase behavior, we calculate their expected date of next order using data across all of your customers.

****Our brand has 3 classes of product frequency. For some products, customers come back randomly. Others are replenished between 60 and 90 days. The last group is replenished between 100 and 120 days. Can we teach the app to know what the customer purchased and send reminders based on the product?****

The app doesn’t consider what products the customer ordered, so if you have products with distinct replenishment cycles, we recommend instead creating multiple **Placed Order** triggered flows for each replenishment cycle by adding the following:

- ****Trigger filters**** to restrict each flow to products that share the same cycle
- ****Time delay**** that reflects the known cycle so you send replenishment emails at the right time

Since the predicted date won’t consider what the customer last ordered and also the likely replenishment cycle for that product, if a customer has known replenishment cycles for most of their product categories they should stick with a standard [Replenishment Flow](https://help.klaviyo.com/hc/en-us/articles/360003195232) and not use this feature.

****Things to look out for in the repeat purchase nurture series flow****

- We don’t recommend counting down to the expected date of next order as repeat customers will simply get the same sequence of emails leading up to every order which may result in unsubscribes.
- This flow shouldn’t replace the use of replenishment flows if customers know the general cycles for most of their product categories.
- If you have a high percentage of repeat buyers, you may want to only use this feature for customers who have purchased once to nurture them for their second purchase.

## How predicted gender is calculated

Klaviyo’s gender prediction algorithm uses a customer’s first name along with census data to make a gender prediction of either likely male, likely female, or uncertain.

Because predicted gender is still an approximation, make sure that, when using targeted communication, you include some information for both genders.

![example emails based on predicted gender](https://klaviyo.zendesk.com/hc/article_attachments/28705663426587)

## Additional resources

- [How to segment by customer lifetime value (CLV)](https://klaviyo.zendesk.com/hc/en-us/articles/360013201072)
- [AI-Powered customer lifetime value](https://www.klaviyo.com/blog/ai-powered-customer-lifetime-value)
- [Use predictive analytics to retain more customers](https://academy.klaviyo.com/en-us/courses/use-predictive-analytics-to-retain-more-customers)