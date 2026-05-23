<h1>Getting started with Lightspeed POS</h1>

## You will learn

Learn how to integrate Lightspeed Point of Sale with Klaviyo, and what data syncs through the integration. After integrating, you'll be able to personalize and target emails based on each customer's offline purchases and activity. The Lightspeed integration syncs with Klaviyo every hour. The data synced from from Lightspeed includes:

- Sales and order data including which products were purchased, the categories they are in, and any discounts applied
- Customer information including First Name, Last Name, and location information
- Shipped and refunded order data

## Before you begin

This integration is for Lightspeed POS R-Series only. Using Lightspeed Retail X-Series? Please refer to [Connecting Klaviyo to Retail POS](https://x-series-support.lightspeedhq.com/hc/en-us/articles/40831009276187-Connecting-Klaviyo-to-Retail-POS-X-Series) X-Series.
.

## Table of contents

- How to integrate with Lightspeed POS
- Verify your synced data
- Types of data synced from Lightspeed
- Outcome
- Additional resources

## How to integrate with Lightspeed POS

1. In Klaviyo, select the ****Integrations**** tab, then click ****Explore apps****.
2. Search for **Lightspeed** and click the card, then click ****Install****.
3. Click ****Connect to Lightspeed****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28705662705563)
4. Log in to Lightspeed if needed, then click ****Authorize Application****.
5. Back in Klaviyo, confirm that your Account ID is correct.
6. Choose whether or not you'd like to add new Lightspeed customers to a Klaviyo list, then select a list from the dropdown.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28705662707739)
7. When you're done, click ****Complete setup****. You should receive a success message.

## Verify your synced data

To check on your Lightspeed integration:

1. Click the ****Analytics**** dropdown in Klaviyo and select ****Metrics****.
2. Filter by Lightspeed and look for the **Placed Order** metric to verify that there is data populated for this metric. The initial integration data sync can take up to a couple hours depending on how much data you have in your account.
3. Klaviyo will import all of your historic Lightspeed data. To verify this, you can compare the number of placed orders from a particular day in Klaviyo with what's in your Lightspeed interface and confirm they match. For example, when exploring the **Placed Order** metric, you can mouse over yesterday's data point or look at the table of data below the chart to see how many orders were reported yesterday. Compare that number to what's stored in Lightspeed from yesterday and you should see they match exactly.
   - If they don't, the issue is most likely that your Klaviyo account's timezone doesn't match your Lightspeed account's timezone. To check your timezone setting in Klaviyo:
     - Click your account name in the lower left.
     - Select then clicking ****Settings > Organization****.
     - Scroll down to **Timezone**.

## Types of data synced from Lightspeed

Navigate to ****Analytics > Metrics****. The metrics with a Lightspeed icon are synced from the Lightspeed integration. You can use the filter feature in the upper righthand corner to filter for all Lightspeed metrics.
Metrics and profile properties from Lightspeed are synced in real-time, you should see them appear in Klaviyo within a few seconds of when an event is recorded in Lightspeed.

Below is a list of all the metrics synced from Lightspeed and an explanation of the data included along with each synced metric.

![Metrics page in Klaviyo filtered by Lightspeed showing list with metrics Ordered Product, Placed Order, Refunded Order, and Shipped Order](https://klaviyo.zendesk.com/hc/article_attachments/28705662703899)

Please note the following exceptions to the order events sync:

- Orders with a value of $0 will not sync to Klaviyo.
- Orders without an email address will not sync to Klaviyo.

### Placed Order

This event is tracked when a customer completes the checkout process and creates an order in your physical store. The event Klaviyo tracks includes key product information regarding the items included in the order (such as product names and images) so you can [use that information in purchase followup emails](http://learn.klaviyo.com/14835-email-templates-advanced-use-cases/how-to-build-a-dynamic-table). You can filter and target **Placed Order** events based on the following criteria:

- ****Categories****
  The names of all categories each product is in, e.g., **t-shirts, mens, pants** and**sale**
- ****Discount Codes****
  Any discount or coupon codes someone used in their order, e.g., **SPRING2015**
- ****Email Domain****
  The email domain of the person placing the order, e.g. **gmail.com** or **yahoo.com**
- ****Is Discounted****
  This will be TRUE or FALSE
- ****Items****
  The names of the products in someone's order, e.g., **t-shirt**or **pants**
- ****Item Count****
  The total number of items in the order, e.g., **2**
- ****Shop****
  The name of the store where the order was placed, e.g. **Klaviyo-Boston**or **Klaviyo-New York**
- ****ShopID****
  The ID of the store where the order was placed
- ****Total Discounts****
  The total amount of any applied coupons or discounts, e.g., **10.00**

### Ordered Product

This event is tracked when a customer places an order - unlike the **Placed Order** event, one **Ordered Product** event is tracked for each item someone purchases in a single order. For example, if someone buys a t-shirt and a pair of pants, one **Placed Order** event and two **Ordered Product** events are tracked - one event for the t-shirt and one event for the pants.

The **Ordered Product** event Klaviyo tracks includes detailed information about each purchased item. This detailed item data is useful for creating behavioral segments based on product variant options and other information that's not available in the **Placed Order** event. You can filter and target **Ordered Product** events based on the following criteria:

- ****Category****
  The name of the category the product is in, e.g., **sale**
- ****Email Domain****
  The email domain of the person placing the order, e.g. **gmail.com** or **yahoo.com**
- ****Name****
  The name or title of the product, e.g., **The Jungle Book DVD**
- ****Product ID****
  The Product ID of the item, e.g., **2222**
- ****Quantity****
  The quantity purchased, e.g., **2**

### Refunded Order

This event is tracked when a customer completes the checkout process and a payment is made, but the customer requests the payment to be returned. The event Klaviyo tracks includes all key product information about the items purchased including product names, images, and discount information. You can filter and target **Refunded Order** events based on the following criteria:

- ****Categories****
  The names of all categories each product is in, e.g., **t-shirts, mens, pants** and**sale**
- ****Discount Codes****
  Any discount or coupon codes someone used in their order, e.g., **SPRING2015**
- ****Email Domain****
  The email domain of the person placing the order, e.g. **gmail.com** or **yahoo.com**
- ****Is Discounted****
  This will be TRUE or FALSE
- ****Items****
  The names of the products in someone's order, e.g., **t-shirt**or **pants**
- ****Item Count****
  The total number of items in the order, e.g., **2**
- ****Total Discounts****
  The total amount of any applied coupons or discounts, e.g., **10.00**

### Shipped Order

This event is tracked when a customer order is fulfilled and is now being shipped. The event Klaviyo tracks includes all key product information about the items purchased including product names, images, and discount information. You can filter and target **Shipped Order** events based on the following criteria:

- ****Items****
  The names of all products in someone's order, e.g., **t-shirt,** **pants**
- ****Collections****
  The complete set of the collections of the products in someone's order, e.g., **t-shirts, mens, pants** and**sale**
- ****Discount Codes****
  Any discount or coupon codes someone used in their order, e.g., **SPRING2015**
- ****Total Discounts****
  The total amount of any coupons or discounts if someone used a code, e.g., **10.00**

For the **Shipped Order** metric, we will only sync orders as shipped when the order status changes to `'shipped' = true`. By default, this shipped status can only be set by clicking a button manually in Lightspeed. Furthermore, shipments not tied to a customer will not be synced. This can occur when a customer isn't specified on a Sale.

### Customer data

In addition to the metrics above, there are also properties from Lightspeed that are added to each Klaviyo profile. You can use these properties in segments and flows. Here are the Klaviyo properties that are automatically synced from Lightspeed:

- Email
- First and Last Name
- Company and Title
- City
- State/Region
- Zip Code
- Country

New profiles that are created in Klaviyo through the Lightspeed integration will not trigger a welcome series flow by default. This is to prevent situations in which a return customer may receive a welcome email through Klaviyo as if they are a first-time customer. If you would like for this functionality to change, please [reach out to Klaviyo support](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272).

## Outcome

You've integrated with Lightspeed POS and reviewed your synced data. You can now personalize and target emails based on each customer's offline purchases and activity.

## Additional resources

- [How to integrate a platform without a pre-built Klaviyo integration](https://developers.klaviyo.com/en/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration)
- [Integration FAQ](https://help.klaviyo.com/hc/en-us/articles/115005081007)
