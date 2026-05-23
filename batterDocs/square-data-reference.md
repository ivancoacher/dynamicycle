<h1>Square data reference</h1>

## You will learn

Learn what data is synced from Square to Klaviyo, how to view it, and what properties Square events contain. Additionally, learn how to view your Square data in Klaviyo.

## Before you begin

If you have not already, read our article on [getting started with Square](https://help.klaviyo.com/hc/en-us/articles/11117215837211) for step-by-step instructions on how to integrate your store before continuing with this article.

## How to view your data

To check on the data sync from Square to Klaviyo:

1. In your Klaviyo account, select the ****Integrations**** tab.
2. Select ****Square**** on the list of **Enabled Integrations**.
3. Select the ****Data**** tab at the top.

Here, you’ll see recent data synced from Square to Klaviyo, and a sync progress bar for your historical data sync.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720659703835)

If you are experiencing issues with your sync, you can select ****Restart Import**** here to restart the historical data sync.

## Data synced from Square

Events from Square Online sync to Klaviyo in real time, and events from Square POS sync every 30 minutes.

The data synced from Square to Klaviyo includes:

- [Known site visitors](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Onsite-Tracking#who-klaviyo-tracks5) tracked as **Active on Site** events (if you left the onsite JavaScript setting checked)
- Email unsubscribes
- Customer information associated with order events
- Your Square catalog (including POS-only items)
- The following events:
  - Abandoned Checkout
  - Placed Order
  - Ordered Product
  - Refunded Order
  - Canceled Order
  - Fulfilled Partial Order
  - Fulfilled Order

Square POS order events will sync to Klaviyo (and Klaviyo profiles will be created) if there is an email address and/or phone number associated with the order which the customer directly shared with your company.

Square events will have a property called **source name** that will show whether the event is from a POS or from online/web, so that you can [segment these events in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908-Getting-started-with-segments).

## Customer information details

Customer profiles sync from Square to Klaviyo if there is an email address and/or phone number associated with the customer which the customer directly shared with your company. Profiles synced from Square to Klaviyo will be created with the following properties:

- ****Email****Email address of customer
- ****First name****
  First name of customer (required)
- ****Last name****
  Last name of customer
- ****City****
  City of customer
- ****State/Region****
  State of customer
- ****Zip Code****
  Zip Code of customer
- ****Country****
  Country of customer
- ****Phone number****
  Phone number of customer. Klaviyo will only create phone-only profiles if you have [set up Klaviyo SMS](https://help.klaviyo.com/hc/en-us/articles/4404274419355-How-to-turn-on-SMS-in-Klaviyo)
- ****Birthday****The customer’s birthdate, if provided
- ****Square Groups****
  Square Groups associated with the customer. This does not currently include Square Segments

### Email consent

The Square platform is an “opt-out” marketing consent platform. This means that anyone who provides you their email address has not been given the opportunity to explicitly consent to your email marketing. Instead, Klaviyo will mark those who have email\_unsubscribed set to false in Square as “Never Subscribed” in Klaviyo, and those who have email\_unsubscribed set to true in Square as “Unsubscribed” in Klaviyo.

### SMS consent

SMS subscribers collected in Square Online cannot currently sync to Klaviyo. You can collect SMS consent via a [Klaviyo form](https://help.klaviyo.com/hc/en-us/articles/360026474752-Getting-started-with-sign-up-forms) on your Square site.

## Catalog item details

Catalog items sync from Square to Klaviyo with the following properties:

- Item name
- Item ID
- Item description
- Item price
- SKU
- URL
- Image URL
- Inventory Quantity
- Inventory Policy
- Category
- Published
- Variants

## Synced events and their properties

### Abandoned Checkout

This event is triggered 1 hour after a cart has been abandoned in a Square Online store, and can be used in an [abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411-How-to-create-an-abandoned-cart-flow).

In order for this event to sync to Klaviyo, you must first turn off abandoned cart emails in Square. To do this:

1. Log in to Square and navigate to your [overview page](https://square.online/)
2. Select ****Communications > Abandoned Carts****
3. Select ****Disable****

The top-level properties of the event in Klaviyo are:

- ****$value****
  Total amount in the cart
- ****Items****
  Items included in the order
- ****Collections****
  Collections linked to the items included in the order
- ****Item count****
  Total number of items included in the order

### Placed Order

This event is triggered when an order event is placed on a Square Online store or POS terminal.

The top-level properties of the event in Klaviyo are:

- ****$value****
  Total amount for the order
- ****Items****
  Items included in the order
- ****Collections****
  Collections linked to the items included in the order
- ****Item count****
  Total number of items included in the order
- ****Discount codes****
  Discount codes applied to the order
- ****Total discounts****
  Total discount amount
- ****Source Name****Source of the order (Square Online, POS)
- ****Location Name****Square location name

### Ordered Product

This event is triggered when an order event is placed on a Square Online store or POS terminal. An **Ordered Product** event is triggered for each item in a **Placed Order**.

The top-level properties of the event in Klaviyo are:

- ****$value****
  Total amount for the order
- ****Name****
  Name of the product ordered
- ****Variant Name****
  Name of the product variant
- ****SKU****
  Product SKU
- ****Product ID****
  Product identifier
- ****Variant ID****Variant identifier
- ****Quantity****
  Number of products
- ****Collections****
  Collections linked to the product
- ****Variant Option****Variant option of product ordered
- ****Modifier Option****Modifier options applied to the order

### Refunded Order

This event is triggered when an order is refunded on a Square Online store or POS terminal.

The top-level properties of the event in Klaviyo are:

- ****$value****
  Total amount for the order
- ****Receipt URL****URL of the order receipt
- ****Source Name****Source of the order (Square Online, POS)
- ****Location Name****Square location name

### Cancelled Order

This event is triggered when a customer creates an order in your store but then cancels the entire order. The event Klaviyo tracks includes all of the product information about the items someone purchased including product names and images. Partial cancellations are not supported.

The top-level properties of the event in Klaviyo are:

- ****$value****
  Total amount for the order
- ****Items****Items included in the order
- ****Collections****
  Collections linked to the items included in the order
- ****Item count****
  Total number of items included in the order
- ****Discount codes****
  Discount codes applied to the order
- ****Total discounts****
  Total discount amount
- ****Source Name****Source of the order (Square Online, POS)
- ****Location Name****Square location name

### Fulfilled Partial Order

A **Fulfilled Partial Order** event will be logged if an order is shipped in multiple fulfillments, and one event will be logged for each partial fulfillment.

The top-level properties of the event in Klaviyo are:

- ****$value****
  Total amount for the fulfillment
- ****Items****
  Items included in the fulfillment
- ****Collections****
  Collections linked to the items included in the fulfillment
- ****Item count****
  Total number of items included in the fulfillment
- ****Discount codes****
  Discount codes applied to the order
- ****Total discounts****
  Total discount amount
- ****Source Name****Source of the order (Square Online, POS)
- ****Location Name****Square location name

### Fulfilled Order

This event is triggered when an order is fulfilled on a Square Online store or POS terminal. A **Fulfilled Order** event will be logged on the last fulfillment, if there are multiple tied to an order.

The top-level properties of the event in Klaviyo are:

- ****$value****
  Total amount for the order
- ****Items****
  Items included in the order
- ****Collections****
  Collections linked to the items included in the order
- ****Item count****
  Total number of items included in the order
- ****Discount codes****
  Discount codes applied to the order
- ****Total discounts****
  Total discount amount
- ****FulfillmentStatus****Status of the fulfillment
- ****Source Name****Source of the order (Square Online, POS)
- ****Location Name****Square location name

## Additional resources

- [Getting started with Square](https://help.klaviyo.com/hc/en-us/articles/11117215837211)
- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908-Guide-to-Creating-Segments)
- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-started-with-flows)
