---
id: "25930166202651"
title: "How to collect reviews from past orders"
source_url: "https://help.klaviyo.com/hc/en-us/articles/25930166202651-How-to-collect-reviews-from-past-orders"
section: "Getting started with reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:35Z"
language: "en"
---
## You will learn

Learn how to queue up recent purchases for review requests while getting started with Klaviyo Reviews. This guide covers requesting reviews from anyone who purchased before you started using Klaviyo Reviews; anyone who places an order or has one fulfilled after you begin using Klaviyo Reviews will receive a review request through your [review request flow](https://klaviyo.zendesk.com/hc/en-us/articles/16319809379611).

This process can only be completed 1 time, and must be completed within 60 days of starting to use Klaviyo Reviews. A maximum of 1,000 orders can receive retroactive review requests. If you have more than 1,000 orders in the selected time period, the oldest 1,000 will be used. If you select the option to collect reviews from past orders during the initial setup of Klaviyo Reviews, you will not be able to repeat this process later.

## Who will receive a review request?

Verified review requests are sent using a flow triggered by the Klaviyo Reviews **Ready to review** event. This event fires for a profile several days after an order is either fulfilled or delivered, based on your reviews settings and ecommerce platform. Normally, these events are created in real time as fulfillments and deliveries occur. When you collect reviews from past orders, Klaviyo retroactively looks back at recent fulfillments and deliveries to generate these events.

### Review requests for Shopify

When you opt to collect reviews from past orders, a **Ready to review** event will fire in the following scenarios:

|  |  |
| --- | --- |
| ****Scenario**** | ****When the review request will be sent (relative to when you request reviews from past orders)**** |
| **Fulfilled order** event occurred between 8 and up to 30 days before you set up Klaviyo Reviews. | Immediately |
| Order fulfilled and delivered before (<8 days) starting Klaviyo Reviews. | 8 days after fulfillment. |
| Order fulfilled before (<8 days) starting Klaviyo Reviews, but delivered after. | Sent based on settings; default is 7 days after delivery. If shipment metrics aren’t available, requests are sent 8 days after fulfillment. The 8-day timeline is not customizable. |
| Order fulfilled after starting Klaviyo Reviews. | Sent based on settings; defaults are 7 days after delivery or 8 days after fulfillment, if shipment metrics aren't available. |

### Review requests for WooCommerce

When you opt to collect reviews from past orders, a Ready to review event will fire in the following scenarios:

|  |  |
| --- | --- |
| ****Scenario**** | ****When the review request will be sent (relative to when you request reviews from past orders)**** |
| Fulfilled order event occurred between 8 and up to 30 days before you set up Klaviyo Reviews. | Immediately |
| Order fulfilled less than 8 days before starting Klaviyo Reviews. | 8 days after fulfillment. |
| Order fulfilled after starting Klaviyo Reviews. | Sent based on settings; default is 7 days after fulfillment. |

## Before you begin

This process is often completed during your Klaviyo Reviews setup. If you did not choose this option during setup, you can add past orders to your review flow now. Before you begin:

- Make sure your [review request flow](https://help.klaviyo.com/hc/en-us/articles/16319809379611) is configured prior to starting these steps.
- [Import reviews from your previous provider](https://help.klaviyo.com/hc/en-us/articles/16318811222555) to avoid sending requests to anyone who has already submitted a review.

## Request reviews from past orders

1. Navigate to ****Reviews****.
2. Select ****Reviews settings > Reviews requests****.
3. In the **Request reviews from past orders** card, click ****Get started****.

   If you don’t see this card, you either completed this step already (e.g., when you set up Klaviyo Reviews), or you’ve been using Klaviyo Reviews for more than 60 days.
4. If you have not yet imported reviews from your previous provider, you’ll be prompted to import them now.
5. Select a **Request period** (i.e., how far back Klaviyo should look for fulfilled orders). You can choose a lookback period of up to 30 days.
   ![Collect reviews from past orders settings](https://klaviyo.zendesk.com/hc/article_attachments/28717882159259)
6. Click ****Request reviews****.
7. **Ready for review** events will begin firing immediately for up to 1,000 eligible orders. As additional orders become eligible, they will trigger additional review requests.

## How billing works for requesting reviews from past orders

Reviews requested from past customers do not count towards your [Klaviyo Reviews plan](https://help.klaviyo.com/hc/en-us/articles/115000976672#01H84M7N01NF4JEY8DJC88PC31).

## Outcome

After completing this process, past purchasers will immediately queue up to receive review requests. Depending on when their order was fulfilled or delivered, they may receive a request immediately or over the course of the next 14 days. You will see reviews and analytics flowing into your Klaviyo account within a few days.

If you’d like to send a review request to someone outside of the lookback window, you can [manually request a review from an individual](https://help.klaviyo.com/hc/en-us/articles/16319809379611#h_01HAA27922MBGSFSZ6JXD2WSAV).

## Additional resources

- [How to customize review widgets](https://klaviyo.zendesk.com/hc/en-us/articles/16691401577883)
- [Understanding reviews performance](https://klaviyo.zendesk.com/hc/en-us/articles/22567673911707)