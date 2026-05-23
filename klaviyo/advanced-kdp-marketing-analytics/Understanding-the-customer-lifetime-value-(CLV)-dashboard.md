---
id: 17797865070235
title: "Understanding the customer lifetime value (CLV) dashboard"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/17797865070235-Understanding-the-customer-lifetime-value-CLV-dashboard"
section: "Predictive models"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: en
---

## You will learn

Learn how to use the custom customer lifetime value (CLV) dashboard to understand and predict each of your customers’ purchasing behaviors over time. Custom CLV provides insights into your customers’ buying habits, including potential future purchases and opportunities for cross-selling and up-selling for impending purchases. In addition, you can use custom CLV insights to better personalize the customer buying journey, including around key times of year and events that matter to certain customer segments.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Strategically using the CLV dashboard

The CLV dashboard can be used in various ways to understand, predict, and target customers based on their purchasing behaviors or potentially mitigate churn of other customers.

Below are some examples of common use cases:

****Using predicted CLV data****

- ****Rewards programs****
  Target those customers expected to spend more on purchases in the near future with coupons or to join a rewards program.
- ****Up-sell/cross-sell higher value items****
  Target those customers expected to purchase in the near future and offer up similar or higher value products.
- ****Offer lower value items****
  Especially for those customers that may churn, use the predicted CLV data to offer lower value items to encourage purchases.

****Using total CLV data****

- ****Reward customers who spend a certain amount****
  Encourage or reward customers who reach a certain spend threshold.
- ****Redefine segments****
  Once a customer reaches a certain spend threshold, make sure they are in the most accurate customer segment (e.g., VIP). This way, they are aligned with the marketing strategies that match their behaviors.

****Using predicted number of orders data****

- ****Encourage customer to surpass minimum order amounts****
  Encourage customers to hit or exceed this expected number with special offers, coupons, free giveaways, or exclusive sales.
- ****Offer bundling****
  Offer bundle discounts if customers hit or exceed this expected order number.
- ****Offer subscription or replenishment discount options****
  Provide easy options to save money by subscribing or auto-replenishing future orders.

****Using expected date of next order data****

- ****Trigger automations to line up before their next order****
  Create and trigger a flow a few days before their expected next order date. You can also include a feed of suggested or new products, or offer discounts to encourage purchase.
- ****Offer exclusive, time-sensitive discounts****
  For customers expected to purchase within a certain number of days, use a time-sensitive discount that only they can use that expires soon.

****Using custom metrics with CLV data****
[Custom metrics](https://help.klaviyo.com/hc/en-us/articles/22311212640027) allow you to create metrics that align with how your business and data functions. Using custom metrics in the CLV dashboard ensures that you are capturing all data that accurately reflects your business model and how your customers interact with your brand.

Below are some examples of common use cases:

- ****Combine all sources of placed orders or revenue****
  Combine revenue from all of your non-Klaviyo integrations, systems (e.g., point of sale), and data tools to ensure that you have the most accurate portrait of your customers current and future spend.
- ****Remove subscription events from counts towards total CLV data****
  Standard Shopify integrations, WooCommerce, and BigCommerce will include subscriptions in Placed Order events automatically. You can set up a custom metric to remove these so that you only capture one-time orders. This may be helpful if you want to evaluate customer behaviors based only on product sales, not including recurring subscriptions.
- ****Exclude $0 or free products from order number data****
  Set up a custom metric to exclude purchases that do not have monetary value (e.g., free giveaways, trials, etc.) so that they are not included in order count history.
- ****Only focus on online buying habits****
  With Shopify and some custom integrations, physical retail (POS) and e-commerce orders will come through as a single event (e.g., Shopify Placed Order event). You may want to create a custom metric that removes these POS events, so that you can focus on online sales only. This may be helpful if you want to target customers with special online promotions, shipping information, online-only products, etc.

## Navigating to the dashboard

Navigation steps to the CLV dashboard vary based on whether you are an Advanced KDP or Marketing Analytics customer.

If you are an Advanced KDP customer, navigate to ****Advanced KDP > Intelligence > Predictive models****.

If you are a Marketing Analytics customer, navigate to ****Marketing Analytics  > Predictive models****.

Here you will see a default dashboard with the current data model used, followed by segments, flows, upcoming campaigns, and forms using particular CLV attributes.

If you have not yet set up a customer lifetime value (CLV) dashboard or wish to make edits to it, head to our guide on [building and customizing the dashboard](https://help.klaviyo.com/hc/en-us/articles/17797912816795).

## Attributes and definitions

All data cards in your dashboard will have a column noting the particular CLV attribute(s) that apply to that marketing channel or strategy.

For more information on setting up CLV attributes in your segments, head to our [guide on predictive analytics](https://help.klaviyo.com/hc/en-us/articles/360020919731).

CLV attributes will show as one of the following options:

- ****Predicted customer lifetime value****
  A prediction of how much money a particular customer will spend in your prediction time range. The monetary value of this prediction will be derived from the segment definition you created.
- ****Historic customer lifetime value****
  The total value of all previous orders an individual has made, taking into account any refunds and returns. The monetary value of this will be derived from the segment definition you created.
- ****Total customer lifetime value****
  The sum of historic CLV and predicted CLV. The monetary value of this will be derived from the segment definition you created.
- ****Predicted number of orders****
  A prediction of how many orders a particular customer will complete in your prediction time range. The number of orders will be derived from the segment definition you created.
- ****Historic number of orders****
  The total number of all previous orders an individual has made, taking into account any refunds and returns. The monetary value of this will be derived from the segment definition you created.
- ****Average order value****
  The expected average value of a particular customer’s order. The monetary value of this will be derived from the segment definition you created.
- ****Average days between orders****
  The average number of days between each of a customer's orders. The number of days will be derived from the segment definition you created.

## Reviewing cards in your dashboard

### Current model card

At the top of your dashboard, it notes historic date range, predicted date range, and last updated information.
![current model card.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722559993115)

If you have recently updated your predicted time range settings, you will see a note here indicating this may take up to 2 hours to update all of your data.

These terms refer to the following:

- ****Historic date range****
  Refers to the number of days from which you can pull and analyze CLV. For example, if your historic date range is 1,500 days, you can analyze CLV from the last 1,500 days.
- ****Predicted date range****
  The upcoming time frame in which Klaviyo can predict the purchase behaviors of your customers or CLV. For example, if your predicted date range is 90 days, Klaviyo shows the potential purchases or CLV for the next 90 days.
- ****Last updated****
  Refers to the last time that the dashboard was updated or changed by a user in your account. At the bottom of this card is a section of 5 example profiles and data. These profiles are from your own segments and lists, and are meant to model how Klaviyo determines each profile’s CLV based on their buying habits.

Profiles are automatically pre-selected and cannot be changed. However, they will update weekly.

![current model profiles-update.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598413979)

Klaviyo will always use the following purchasing data to pull in your examples: Profile example #1: Has made 3+ orders and placed their last order within the last 90 days. Profile example #2: Has made 2 orders and placed their last order within the last 90 days. Profile example #3: Has placed 1 order and placed their last order in the last 60 days Profile example #4: Has placed 3+ orders, but their last order was placed over 180 days ago. Profile #5: Has placed 1 order, but their last order was placed over 60 days ago.

### Segments using CLV card

The segments using CLV card displays all of your segments by specific CLV attribute(s) using the predictive analytics definitions. You can use this information to help you focus your efforts on the segments and attributes that align best with your marketing strategies.

![segments using clv card-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722559995803)

If you do not have any segments using CLV attributes, then this table appears blank until you create at least one.

The table will contain:

- The segment name
- The total number of profiles in that segment.
- The specific CLV attribute(s) used in the segment (e.g., Historic number of orders).
- When the segment was last updated or adjusted.

You can also use the arrows beside any of the applicable columns to sort by name, total profiles, or when the segment was last updated.

![segments arrows sorting.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598416795)

More importantly, by clicking on any of the segments from the Segment name column, you will see all the profiles that fit the specific CLV attribute. You can then decide how to use these profiles and this attribute in your marketing strategies.

****Editing and reviewing your segment definition****

Once you click into a segment and land on the Lists & segments page, you can choose to edit the definition of segment and adjust/review any values or definitions. Click on ****Edit Definition**** to update your segments as you need.

![CLV_segment edit definition.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722560001179)

****Creating new segments****

Clicking on the ****Create**** button on the top right of the card will bring you to the segment builder. Here, you can create new segments that use the CLV attributes and [predictive analytics](https://help.klaviyo.com/hc/en-us/articles/360013201072) definitions.

![create button segment card.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722560002331)

### Upcoming campaigns using CLV card

The upcoming campaigns using CLV card displays all of your impending campaigns (email, SMS, or push) by specific CLV attribute(s) using the [predictive analytics](https://help.klaviyo.com/hc/en-us/articles/360013201072) definitions. Here, you see all upcoming campaigns that contain a CLV attribute(s) somewhere in the lists or segments they are using. These insights are especially helpful in monitoring specific sends that will track CLV data.

![upcoming campaigns card.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598422811)

If you do not have any upcoming campaigns containing a list or segment using a CLV attribute, then this table will appear blank until you have created or scheduled at least one.

The table will contain:

- The campaign name with the list or segment using a CLV definition noted below
- Campaign status (**Scheduled** or **Sending**)
- The types of messages used (email, SMS, or push)
- The specific CLV attributes in the campaign (e.g., **Historic number of orders**, **Predicted Customer Lifetime Value**, etc.)
- When the campaign is scheduled to start sending

You can also use the arrows beside any of the applicable columns to sort by campaign name, status, type, or scheduled date.

![upcoming campaigns arrows sorting.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722560005403)

By clicking on any of the campaigns from the **Campaign name** column it will take you to that specific campaign’s review page. You can then decide if you need to pause and edit or reschedule your campaign if you need to adjust anything.

****Creating new campaigns****

Clicking on the ****Create**** button on the top right of the card will bring you to the first step of the campaign creation process. Here, you can create new campaigns that use the CLV attributes using the [predictive analytics](https://help.klaviyo.com/hc/en-us/articles/360013201072) definitions.

![upcoming campaigns create button.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722560006683)

### Flows using CLV card

The flows using CLV card displays all of your flows by specific CLV attribute(s) using the predictive analytics definitions. Here, you see all flows that contain a CLV attribute(s) somewhere in the lists or segments they are using.

![flows using clv card.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598430363)

If you do not have any flows containing a CLV attribute(s), then this table will appear blank until you have at least one.

The table contains:

- The flow name with the list or segment using a CLV definition
- Flow status (**Live**, **Manual**, or **Draft**)
- The types of messages contained in the flow (email, SMS, or push)
- The specific CLV attributes in the flow (e.g., **Historic number of orders**, **Predicted Customer Lifetime Value**, etc.)
- When the flow was last updated or adjusted

You can also use the arrows beside any of the applicable columns to sort by name or when the flow was last updated.

![flows using, arrows sorting.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598432027)

By clicking on any of the flows from the Flow name column, it will take you to that specific flow’s builder view. You can then decide how to use or adjust this flow as part of your marketing strategies.

****Creating new flows****

Clicking on the ****Create**** button on the top right of the card brings you to the flows library. Here, you can create new flows that use the CLV attributes and predictive analytics definitions.

![flows using clv, create button.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722560016667)

### Forms using CLV card

The forms using CLV card displays all of your forms by specific CLV attribute(s) using the [predictive analytics](https://help.klaviyo.com/hc/en-us/articles/360013201072) definitions. Here, you see all forms that are connected to a list or segment that contain a CLV attribute(s).

![forms using clv card.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722560012955)

If you do not have any forms connected to a list or segment using a CLV attribute(s), then this table appears blank until you have created at least one.

The table contains:

- The form name with the connected list or segment using a CLV definition noted below
- Form status (**Live**, **Manual**, or **Draft**)
- The types of form (**Popup**, **Flyout**, **Embed**, or **Full Page**)
- The specific CLV attributes in the lists or segments connected to the form (e.g., **Historic number of orders**, Predicted Customer Lifetime Value, etc.)

You can also use the arrows in the top of the table to sort by name or form type.

![forms card, arrow sorting.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722560014747)

By clicking on any of the forms from the Form name column, you can see that form’s analytics and editing view. You can then choose to adjust this form as part of your marketing strategies.

****Creating new forms****

Clicking on the ****Create**** button on the top right of the card brings you to the forms library. Here, you can create new forms that use the CLV attributes and predictive analytics definitions.

![forms card, create button.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598445595)

## Additional resources

[How to build a customer lifetime value (CLV) report](https://help.klaviyo.com/hc/en-us/articles/17797912816795)

[How to segment by customer lifetime value (CLV)](https://help.klaviyo.com/hc/en-us/articles/360013201072)

[Understanding Klaviyo's predictive analytics](https://help.klaviyo.com/hc/en-us/articles/360020919731)