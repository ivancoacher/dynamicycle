---
id: 6202715127579
title: "Wix data reference"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/6202715127579-Wix-data-reference"
section: "Wix"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: en
---

## You will learn

Learn what data is synced from Wix to Klaviyo, how to view it, and what properties Wix events contain. Additionally, learn how to view your Wix data in Klaviyo.

## Before you begin

If you have not already, read our article on [getting started with Wix](https://help.klaviyo.com/hc/en-us/articles/6202669053723) for step-by-step instructions on how to integrate your store before continuing with this article.

## How to view your data

To check on the data sync from Wix to Klaviyo:

1. In your Klaviyo account, click on your company or organization name in the bottom left hand corner, then click ****Integrations****.
2. Select ****Wix**** on the list of **Enabled Integrations**.
3. Select the ****Data**** tab at the top.

Here, you’ll see recent data synced from Wix to Klaviyo, and a sync progress bar for your historical data sync.

If you are experiencing issues with your sync, you can select ****Restart Import**** here to restart the historical data sync.

## Data synced from Wix

The data synced from Wix to Klaviyo includes:

- Abandoned Checkout
- Placed Order
- Modified Placed Order
- Ordered Product
- Refunded Order
- Canceled Order
- Fulfilled Partial Order
- Fulfilled Order

- [Known site visitors](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Onsite-Tracking#who-klaviyo-tracks5) tracked as **Active on Site** events (if you left the onsite JavaScript setting checked)
- Email subscribers (if you chose to add them to a Klaviyo list)
- Customer information associated with order events
- Wix contact labels
- Your Wix catalog
- The following events:

## Customer information details

Customer profile information syncs from Wix to Klaviyo with the following properties:

- First name
- Last name
- Email address
- Phone number
- City
- Zip code

## Catalog item details

Catalog items sync from Wix to Klaviyo with the following properties:

- Item name
- Item ID
- Item description
- Item price
- SKU
- URL
- Image URL
- Inventory quantity
- Category
- Published
- Variants

## Synced events and their properties

### Abandoned Checkout

There is no historical sync of **Abandoned Checkout** events, only a sync going forward from the time you integrate.

An **Abandoned Checkout** event is triggered when a visitor is either logged in, or has entered their email and continued with checkout, then leaves the cart abandoned for 1 hour.

The top-level properties of the event in Klaviyo are:

- ****$value****
  Total amount in the cart
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

### Placed Order

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
- ****Source name****
  Source of the order (WEB, POS, etc.)

### Modified Placed Order

**Modified Placed Order** is tracked when an order is modified and then placed again.

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
- ****Source name****
  Source of the order (WEB, POS, etc.)

### Ordered Product

The top-level properties of the event in Klaviyo are:

- ****$value****
  Total amount for the order
- ****Name****
  Name of the product ordered
- ****SKU****
  Product SKU
- ****Product ID****
  Product identifier
- ****Quantity****
  Number of products (always 1)
- ****Collections****
  Collections linked to the product

### Refunded Order

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

### Canceled Order

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

### Fulfilled Order

The top-level property of the event in Klaviyo is:

- ****Fulfillment status****
  Fulfillment status of the order will always be “Fulfilled,” because if the order is unfulfilled this event will not be created. If the order is partially fulfilled a “Fulfilled Partial Order” event will be created instead.

### Fulfilled Partial Order

The top-level property of the event in Klaviyo is:

- ****Fulfillment status****
  Fulfillment status of the order will always be “Partially Fulfilled,” because if the order is unfulfilled this event will not be created. If the order is fully fulfilled, a “Fulfilled Order” event will be created instead.