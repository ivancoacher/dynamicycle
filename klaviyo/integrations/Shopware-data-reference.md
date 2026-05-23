---
id: 13006716790299
title: "Shopware data reference"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/13006716790299-Shopware-data-reference"
section: "Shopware"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:27Z"
language: en
---

## You will learn

Learn what data is synced from Shopware 6 to Klaviyo, how to view this data, and what properties Shopware events contain.

## Before you begin

Read our article on [getting started with Shopware](https://help.klaviyo.com/hc/en-us/articles/13001662470939) for step-by-step instructions on how to integrate your store before continuing with this article.

## How to view your data

To view the data synced from Shopware to Klaviyo:

1. In your Klaviyo account, click ****Analytics**** in the left navigation.
2. Select ****Metrics****.
3. Filter the list of metrics by ****API****. Since the Shopware integration was not built directly by Klaviyo, events will sync with the API label and have a gear icon. Filtering by API will also show any custom metrics you’ve synced via API.
4. Click on an individual metric, such as **Placed Order**, to see a chart of activity over time. You can also view an Activity Feed, Cohorts, Best People, and Activity Map by selecting a tab along the top for an individual metric.
5. Click ****Activity Feed****, and click on the timestamp of an individual event. Here, you can view the properties associated with that event.

## Data synced from Shopware

The following types of data are synced from Shopware to Klaviyo, if you configured them within your integration settings:

- Email subscribers (subscribed via a Shopware or Klaviyo form)
- Product catalog (if you set up a custom catalog feed sync)
- Onsite events

- Active on Site
- Viewed Product/Recently Viewed Items
- Started Checkout

- Transactional events

- Added to Cart
- Placed Order
- Ordered Product
- Fulfilled Order
- Cancelled Order
- Refunded Order
- Paid Order
- Subscribed to Back in Stock

## How email subscription syncs

Email subscribers signing up via a Shopware form will be synced as subscribers in Klaviyo if you’ve selected a Klaviyo list in your Shopware extension settings.
![Klaviyo list name for subscriber sync setting with Newsletter in box](https://klaviyo.zendesk.com/hc/article_attachments/28716066677531)

If a subscriber unsubscribes in Klaviyo, they will also be unsubscribed in Shopware. In your Shopware newsletter list, those who have unsubscribed in Klaviyo will be marked with the status **Awaiting deletion**. If someone unsubscribes from an email you send from Shopware, they will not be unsubscribed in Klaviyo.

## Synced events and their top-level properties

### Active on Site

This default event Klaviyo tracks when a cookied user is active on your site. This event does not contain other properties to use in segmentation.

### Viewed Product

The **Viewed Product** event is tracked when a cookied user views a product page on your site. Recently viewed items are added to their profile. This event contains the following top-level properties:

- ProductName
- ProductID
- SKU
- Categories (array)
- ImageURL
- URL
- Brand
- Price
- CompareAtPrice

### Added to Cart

This event is tracked whenever a logged in user adds an item to their cart. Within this event, the **Items** array will list all other items currently in the cart at the time this event was created. The **CheckoutURL** in this event can be used to rebuild the current cart.

The **Added to Cart** event contains the following top-level properties:

- AddedItemProductName
- AddedItemProductID
- AddedItemSKU
- AddedItemCategories
- AddedItemImageURL
- AddedItemURL
- AddedItemPrice
- AddedItemQuantity
- ItemNames
- CheckoutURL
- Items
- $value

### Started Checkout

This event tracks when a cookied user is brought to the second checkout page after entering their email on the first checkout page. The **Started Checkout** event contains the following top-level properties:

- CheckoutURL
- ItemNames (array)
- Categories
- Items (array)
- $value": 19.99

### Placed Order

**Placed Order** is tracked when an order is placed, and includes an **Items** array containing all items in the order. **Placed Order** differs from **Ordered Product** in the way that an **Ordered Product** event is tracked for each item in an order, while **Placed Order** is tracked once for the entire order, and includes information such as the shipping address. The **Placed Order** event contains the following top-level properties:

- OrderId
- Categories
- ItemNames
- Brands
- DiscountCode
- DiscountValue
- Items
- BillingAddress
- ShippingAddress
- $value

### Ordered Product

The **Ordered Product** event, which is tracked for each item in an order, contains the following top-level properties:

- ProductName
- OrderId
- ProductID
- SKU
- Quantity
- ProductURL
- ImageURL
- Categories
- ProductBrand
- $value

### Fulfilled Order

The **Fulfilled Order** event contains the following top-level properties:

- OrderID
- Categories
- ItemNames
- Brands
- DiscountCode
- DiscountValue
- Items
- BillingAddress
- ShippingAddress

### Cancelled Order

The **Cancelled Order** event contains the following top-level properties:

- OrderID
- Categories
- ItemNames
- Brands
- DiscountCode
- DiscountValue
- Items
- BillingAddress
- ShippingAddress
- Reason
- $value

### Refunded Order

The **Refunded Order** event contains the following top-level properties:

- OrderID
- Categories
- ItemNames
- Brands
- DiscountCode
- DiscountValue
- Items
- BillingAddress
- ShippingAddress
- Reason
- $value

### Paid Order

The **Paid Order** event is triggered when an order is set to **Paid** in Shopware. It contains the following top-level properties:

- OrderID
- Categories
- ItemNames
- Brands
- DiscountCode
- DiscountValue
- Items
- BillingAddress
- ShippingAddress
- Reason
- $value

### Subscribed to Back in Stock

This event is tracked when someone subscribes to Back in Stock alerts, but does not contain other top-level properties.

## Additional resources

- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908-Guide-to-Creating-Segments)
- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-started-with-flows)