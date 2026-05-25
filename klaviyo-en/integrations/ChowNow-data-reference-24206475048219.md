---
id: "24206475048219"
title: "ChowNow data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/24206475048219-ChowNow-data-reference"
section: "ChowNow"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:46Z"
language: "en"
---
Learn what data syncs from ChowNow to Klaviyo and where to view it.

## Before you begin

If you have not already, read our guide, [Getting started with ChowNow](https://help.klaviyo.com/hc/en-us/articles/24206444868251), for step-by-step instructions on integrating, before continuing with this article.

## About ChowNow data

The historical sync from ChowNow looks back 2 years. The periodic sync going forward occurs every 5 minutes.

Klaviyo syncs 3 order events from ChowNow:

- Accepted Order
- Placed Order
- Cancelled Order

Klaviyo syncs the following profile data from ChowNow for profiles associated with order events:

- ChowNow ID
- First name
- Last name
- Phone number

## Email consent

Klaviyo does not currently sync email addresses and consent from ChowNow.

## SMS consent

While phone numbers are synced, SMS consent is not. This means that SMS cannot be sent to phone numbers synced from this integration without separately gathering consent.

## How to view your data

To view your ChowNow data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account.
3. Filter by **ChowNow** at the top to see all your ChowNow metrics.

## ChowNow metrics

### Placed Order

This event is triggered when a customer submits an order in ChowNow. It can be filtered by the following top-level properties:

- ****Fulfill Method****The method used to fulfill the order (either “curbside”, “delivery”, “dine\_in”, or “pickup”).
- ****Is Order Ahead****Whether the order was placed ahead of time (“TRUE” or “FALSE”).
- ****Order URL****The order details URL. This can be used to fetch the detailed information for an order.
- ****Items****An array of all the items in the order.
- ****Quantity****The quantity of all the items in the order.
- ****Discount****
  An array of all discount information.
- ****Restaurant ID****The ID of the restaurant where the customer placed the order.
- ****Restaurant Name****
  The name of the restaurant where the customer placed the order.
- ****ChowNow ID****
  The ChowNow ID for the order.
- ****Marketplace ID****
  The ID of the marketplace where the customer placed the order.
- ****Marketplace Name****The name of the marketplace where the customer placed the order.
- ****Discount Codes****An array of all discount codes applied.
- ****Total Discounts****The total value of all discounts applied.
- ****$value****The total value of the order, inclusive of any discounts.

### Accepted Order

This event is triggered when a customer’s order is accepted in ChowNow. It can be filtered by the following top-level properties:

- ****Fulfill Method****The method used to fulfill the order (either “curbside”, “delivery”, “dine\_in”, or “pickup”).
- ****Is Order Ahead****Whether the order was placed ahead of time (“TRUE” or “FALSE”).
- ****Order URL****The order details URL. This can be used to fetch the detailed information for an order.
- ****Items****An array of all the items in the order.
- ****Quantity****The quantity of all the items in the order.
- ****Discount****
  An array of all discount information.
- ****Restaurant ID****The ID of the restaurant where the customer placed the order.
- ****Restaurant Name****The name of the restaurant where the customer placed the order.
- ****ChowNow ID****
  The ChowNow ID for the order.
- ****Marketplace ID****
  The ID of the marketplace where the customer placed the order.
- ****Marketplace Name****The name of the marketplace where the customer placed the order.
- ****Discount Codes****An array of all discount codes applied.
- ****Total Discounts****The total value of all discounts applied.
- ****$value****The total value of the order, inclusive of any discounts.

### Cancelled Order

This event is triggered when a customer cancels an order in ChowNow. It can be filtered by the following top-level properties:

- ****Fulfill Method****The method used to fulfill the order (either “curbside”, “delivery”, “dine\_in”, or “pickup”).
- ****Is Order Ahead****Whether the order was placed ahead of time (“TRUE” or “FALSE”).
- ****Order URL****The order details URL. This can be used to fetch the detailed information for an order.
- ****Items****An array of all the items in the order.
- ****Quantity****The quantity of all the items in the order.
- ****Discount****
  An array of all discount information.
- ****Restaurant ID****The ID of the restaurant where the customer placed the order.
- ****Restaurant Name****The name of the restaurant where the customer placed the order.
- ****ChowNow ID****
  The ChowNow ID for the order.
- ****Marketplace ID****
  The ID of the marketplace where the customer placed the order.
- ****Marketplace Name****The name of the marketplace where the customer placed the order.
- ****Discount Codes****An array of all discount codes applied.
- ****Total Discounts****The total value of all discounts applied.
- ****$value****The total value of the order, inclusive of any discounts.

## Additional resources

[Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908-Guide-to-Creating-Segments)

[Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-started-with-flows)