<h1>Salesforce Commerce Cloud data reference</h1>

## You will learn

Learn what data syncs from Salesforce Commerce Cloud to Klaviyo after you [enable Klaviyo's Salesforce Commerce Cloud integration](https://help.klaviyo.com/hc/en-us/articles/360033744951), and how you can view it.

## View your Salesforce Commerce Cloud metrics

In your Klaviyo account, click the ****Analytics**** dropdown and select ****Metrics****. Here, you can view all of the metrics in your account, including those synced from Salesforce Commerce Cloud.

If you enabled **Label Events as SFCC** when integrating, the following events will appear with an SFCC icon:

- Viewed Category
- Viewed Product
- Searched Site
- Added to Cart
- Started Checkout
- Placed Order
- Ordered Product
- Order Confirmation

Otherwise, SFCC events will appear with a gear icon. The **Active on Site** metric will always appear with gear icon, whether you've enabled branding or not.

## Salesforce Commerce Cloud metrics

Below is a list of all the metrics synced from Salesforce Commerce Cloud and an explanation of the data included with each metric. You can also [view the raw data for each metric](https://help.klaviyo.com/hc/en-us/articles/115005076747-View-Raw-Metric-or-Event-Data-in-Klaviyo) within Klaviyo.

### Active on Site

This metric is tracked when a cookied visitor is active on your site.

### Searched Site

This metric is tracked when a cookied visitor initiates a search.

### Viewed Product

This metric is tracked when a cookied visitor views a product page on your site.

### Viewed Category

This metric is tracked when a cookied visitor views a category page on your site.

### Add to Cart or Added to Cart

This metric is tracked when a cookied visitor adds or modifies an item in their cart. If you are using our cartridge version 23.7.0 or later, this metric will be called **Added to Cart**. If you are using a cartridge prior to 23.7.0, this metric will be called **Add to Cart**. If you upgraded your cartridge configured the corresponding setting, it will still be called **Add to Cart** for continuity purposes. Note that using the name **Added to Cart** will allow for the use of future pre-built Klaviyo flows relying on this metric.

This metric tracks each time someone adds something to their cart, and logs each item in the cart at that time (the first **Added to Cart** event tracks the first item, the second event tracks the first and second item, etc.).

### Started Checkout

This event is tracked when someone enters their email at checkout, then tabs or clicks away from the email field. This event includes a cartRebuildingLink property that can be used to link customers back to their carts.

### Order Confirmation

This metric is similar to **Placed Order** but syncs in real time, as opposed to hourly, and is segmentable using the **itemCategories** property.

Note that while Klaviyo may sync many details about a given metric, not all synced properties are available for segmentation. For data management purposes, only the primary details of a metric are synced as "top-level" properties, and only these top-level properties are segmentable. Commerce Cloud's **Placed Order** and **Ordered Product** metrics do not sync with a top-level **itemCategories** property. If you wish to segment using the **itemCategories** property, you will need to use the **Order Confirmation** metric to do so. This is ideal for real-time order confirmation emails.

### Placed Order

This metric is tracked when a customer completes the checkout process and orders from you in your Salesforce Commerce Cloud store. The event will list all of the product information about the items someone purchased, including product names and variant information. You can then use that information in purchase follow-up emails. You can filter and target **Placed Order** events based on the following criteria:

- ****$value****The total order value, including shipping and any applied discounts.
- ****ItemNames****
  The names of the ordered products (e.g., t-shirt or pants).
- ****ItemCount****The number of items in the order (e.g., 2).
- ****OrderNumber****The order number associated with your store.
- ****SiteID****
  The ID of the site.
- ****Status****
  The status of the order.
- ****external\_catalog\_id****
  Set to your SiteID; used in catalog organization in Klaviyo.

### Ordered Product

This metric is also tracked when a customer places an order, but a separate event is tracked for each item someone purchases. For example, if someone buys a t-shirt and a pair of pants, one **Placed Order** event will be tracked for the purchase as a whole along with 2 **Ordered Product** events: 1 for the t-shirt and 1 for the pants.

The metrics Klaviyo tracks include detailed information about each product someone purchases. This is useful when creating behavioral segments based on product variant options and other detailed information that's not available in the **Placed Order** event. You can filter and target **Ordered Product** events based on the following criteria:

- ****$value****
  The total value of the item purchased; no shipping costs or discounts included.
- ****Name****
  The name or title of the ordered product (e.g., t-shirt).
- ****Price****
  The price of the item.
- ****SKU****
  The SKU of the product variant.
- ****ProductID****
  The ID associated with the product in your store.
- ****Quantity****
  The total quantity ordered of the product.
- ****SiteID****
  The ID of the site.
- ****CurrencyCode****
  The currency code used to purchase the product (e.g., USD).
- ****external\_catalog\_id****
  Set to your SiteID; used in catalog organization in Klaviyo.

**Placed Order** and **Ordered Product** events are synced to Klaviyo seconds apart. For this reason, it is important to be consistent with the metric you use to trigger and filter your flows and segments. For example, if a flow is triggered by the **Placed Order** metric and you add a filter to exclude anyone who **Ordered Product** since starting the flow, all recipients will be skipped because the two events are separate, but sync seconds apart. As a best practice, use **Placed Order** to trigger and filter flows and segments.

## Salesforce Commerce Cloud metric sources

Different Salesforce Commerce Cloud metrics flow into Klaviyo in different ways: some through the Klaviyo cartridge, and some through the OCAPI integration. When you integrated with Salesforce Commerce Cloud, you should have both installed the Klaviyo cartridge in SFCC and enabled the SFCC OCAPI integration in Klaviyo. For more information on these steps, see our article on [integrating with Salesforce Commerce Cloud](https://help.klaviyo.com/hc/en-us/articles/360033744951).

The metrics that flow in through the cartridge are the following:

- Order Confirmation
- Searched Site
- Viewed Category
- Viewed Product
- Added to Cart
- Started Checkout

The metrics that flow in through OCAPI are the following:

- Placed Order
- Ordered Product

Historical data syncs every hour from OCAPI. Your catalog should sync every 8 hours, and all other metrics will sync in real time.

## Additional resources

- [Getting started with Salesforce Commerce Cloud](https://help.klaviyo.com/hc/en-us/articles/360033744951)
- [How to upgrade your Salesforce Commerce Cloud cartridge](https://help.klaviyo.com/hc/en-us/articles/16708128591259)
- [Klaviyo Developer Portal](https://developers.klaviyo.com/en)
