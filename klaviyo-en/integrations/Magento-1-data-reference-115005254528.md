---
id: "115005254528"
title: "Magento 1 data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005254528-Magento-1-data-reference"
section: "Magento 1"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:40Z"
language: "en"
---
Klaviyo's Magento 1 integration is no longer accepting new installations and will reach full end-of-support in late 2027. Klaviyo Support is no longer able to assist with Magento 1–related requests.

## You will learn

Learn what Magento 1 data is imported into Klaviyo when you integrate the two platforms. Klaviyo's integration with Magento pulls in all of the historical data in your Magento store at the time of your initial historic sync. Once enabled, the integration will begin to sync metrics and customer data in near real-time. Examples of this data include the information associated with past placed orders, fulfilled orders, etc.

In Klaviyo, you can navigate to your account's ****Analytics**** tab in the left sidebar to view all of the metrics in your account; the metrics with a Magento icon are the ones synced from your Magento integration.

![The Magento 1 metrics available in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28715969069339)

Klaviyo limits the number of unique metrics you can create to 200. When you approach this threshold, you will be alerted via a warning in your account, along with an email to the account owner.

## Magento metrics

### Canceled Order

This event is tracked when a customer creates an order in your Magento store but then cancels the order before fulfillment. Klaviyo tracks associated data including all of the product information about the items someone purchased. Product information includes product names, images, and variant information that you can use in purchase follow-up emails.

You can filter and target Canceled Order events based on the following criteria:

- ****Value****: Total value of the order (sub-total + shipping cost - any discounts).
- ****Items****: The names of the products in someone's order.
  ex: **t-shirt**or **pants**. If ordered multiple times will show multiple of the same item
- ****Item Categories****: The complete set of categories of the items in someone's order; (e.g, **t-shirts, mens, pants** and sale).
- ****Item Count****: The number of items in the order (e.g., **2).**
- ****Currency Code****: The specific currency paid for an item based on country (e.g., **USD, EUR**)**.**
- ****Discounted****: If this specific item has a discount applied (i.e., true/false).
- ****Coupon****: The coupon code applied.
- ****Unique Items****: The individual item included in an order (e.g., **shirts, shorts**)**.**If multiple products are ordered, the unique item will display only once.
- ****Unique Item Categories****: The categories unique items are grouped in (e.g., **mens,** sale).
- ****Attributes (optional)****: Custom product attributes.

### Checkout Completed

This event is tracked when a customer completes a checkout in your Magento store. The Checkout Completed event does not historically sync, so is not always an accurate measure when looking at totals events over time. For tracking revenue and segmentation use the Placed Order event.

You can filter and target Checkout Completed events based on the following criteria:

- ****Value:****The total value of the order.
- ****Discount Codes****: Any coupon or discount codes applied.
- ****Items****: The names of the products in someone's cart (e.g., **t-shirt**or **pants**).
- ****Items Count****: The total amount of items in someone's cart.
- ****Total Discounts (optional)****: Total dollar value of any coupons or discounts.

### Checkout Started

This event is tracked when a customer enters their contact and shipping information on the first page of the Magento checkout process and then clicks **continue**. Klaviyo tracks related product data about items in someone's cart including product names, images and variant information that you can use in your abandoned cart emails. This event has a checkout URL property which links back to each customer’s exact cart and which can be used to rebuild the cart if a customer opens the email from a new device.

You can filter and target Checkout Started events based on the following criteria:

- ****Value****: The value of the cart at time of checkout (sub-total + shipping cost - any discounts).
- ****Items****: The names of the products in someone's cart (e.g., **t-shirt**or **pants**).
- ****Items Count****: The total amount of items in someone's cart.
- ****Discount Codes (optional)****: Any coupon or discount codes applied.
- ****Total Discounts (optional)****: Total dollar value of any coupons or discounts.

### Fulfilled Order

This event is tracked when you mark an order in your Magento store as shipped. Klaviyo tracks related product information about the items someone purchased including product names, images and variant information that can be used in purchase follow-up emails.

You can filter and target Fulfilled Order events based on the following criteria:

- ****Value****: Total value of the order (sub-total + shipping cost - any discounts).
- ****Items****: The names of the products in someone's order (e.g., **t-shirt**or **pants**). If ordered multiple times, multiples of the same item will appear.
- ****Item Categories****: The complete set of categories of the items in someone's order (e.g., **t-shirts, mens, pants** and sale).
- ****Item Count****: The number of items in the order. (e.g., **2**).
- ****Currency Code****: The specific currency paid for an item based on country (e.g., **USD, EUR**)**.**
- ****Discounted****: If this specific item has a discount applied (i.e., true/false).
- ****Coupon****: The coupon code applied.
- ****Unique Items****: The individual item created in an order (e.g., **shirts,** shorts).If multiple products are ordered, the unique item will only display once.
- ****Unique Item Categories****: The categories unique items are grouped in (e.g., **mens,** sale).
- ****Attributes (optional)****: Custom product attributes.

### Ordered Product

This event is tracked when a customer places their order. One Ordered Product event is tracked for each item someone purchases. For example, if someone buys a t-shirt and a pair of pants, one Placed Order event is tracked and two Ordered Product events are recorded - one event for the t-shirt and one event for the pants.

The Ordered Product event includes detailed information about each product someone purchases. This is useful when creating behavioral segments based on product variant options and other detailed information that's not available in the Placed Order event. You can filter and target Ordered Product events based on the following criteria:

- ****Value****: Total price of item (does not include shipping costs or any discounts taken).
- ****Name****: The name given to this specific item.
- ****SKU****: The specific SKU assigned to track an item, (e.g., **REDMEDIUMTSHIRT**)**.**
- ****Categories****: The complete set of the collections of the products in someone's order (e.g.,**t-shirts, mens, pants** and sale).
- ****Price****: The dollar value of the specific product (e.g., **shirts 25.50, shoes 50.25**)**.**
- ****Cost****: The cost to make a product (e.g., **shirts 13.85, shoes 20.00**)**.**
- ****Currency Code****: The specific currency paid for an item based on country (e.g., **USD, EUR**)**.**
- ****Discounted****: If this specific item has a discount applied (i.e., true or false).
- ****ProductID****: ID of specific product in your store.
- ****Quantity:****Quantity ordered.
- ****Attributes (optional)****: Custom product attributes.

### Placed Order

This event is tracked when a customer completes the checkout process and creates an order in your Magento store. Klaviyo tracks related data including product information about the items someone purchased including product names, images, and variant information that you can use in purchase follow-up emails. You can filter and target ****Placed Order**** events based on the following criteria:

- ****Value****: Total value of the order (sub-total + shipping - any discounts).
- ****Items****: The names of the products in someone's order, ex: **t-shirt**or **pants**. If ordered multiple times will show multiple of the same item.
- ****Item Categories****: The complete set of categories of the items in someone's order (e.g., **t-shirts, mens, pants** and **sale**)**.**
- ****Item Count****: The number of items in the order (e.g., **2**)**.**
- ****Currency Code****: The specific currency paid for an item based on country (e.g., **USD,** EUR).
- ****Discounted****: If this specific item has a discount applied (i.e., true/false).
- ****Coupon****: The coupon code applied.
- ****Unique Items****: The individual item created in an order (e.g., **shirts, shorts**)**.** If multiple products are ordered, the unique item will only display once.
- ****Unique Item Categories****: The categories unique items are grouped in, (e.g., **mens, sale**)**.**
- ****Attributes (optional)****: Up to 10 custom product attributes can be synced for placed orders  This sync needs to be enabled before custom attribute data flows into your Klaviyo account. [See the section below on how to set this up](#h_935cad58-8ae4-4df6-9b3f-c9f7ce12d53e).

### Refunded Order

This event is tracked when an order is refunded in Magento.

- ****Value****: Total value of the order (sub-total + shipping - any discounts).
- ****Coupon****: The coupon code applied.
- ****Currency Code****: The specific currency paid for an item based on country (e.g., **USD,** EUR).
- ****Discounted****: If this specific item had a discount applied (i.e., true/false).
- ****Item Categories****: The complete set of categories of the items in someone's order (e.g., **t-shirts, mens, pants** and **sale**)**.**
- ****Item Count****: The number of items in the order (e.g., **2**)**.**
- ****Items****: The names of the products in someone's order (e.g., **t-shirt**or **pants**). If ordered multiple times will show multiple of the same item.
- ****Unique Item Categories****: The categories unique items are grouped in (e.g., **mens, sale**)**.**
- ****Unique Items****: The individual item created in an order, ex: **shirts, shorts.**If multiple products are ordered, the unique item will only display once.

Revenue, or **Placed Order** value, is calculated as follows: (price of orders + shipping - discounts). To filter a segment based on $value, filter the segment using ****Revenue****.

****Payment**** is available as a second-level property under the ****extra**** field. You cannot filter off of second-level properties for segmentation, but you can [use this data as an event variable](https://help.klaviyo.com/hc/en-us/articles/115005084927-Template-Tags-and-Variable-Syntax#event-variables-) in your email templates.

## Synced customer data

Klaviyo creates a contact from the creation of an existing order, an existing customer record, or when a checkout is started. Klaviyo will create a new Klaviyo Profile for every synced contact, and will populate this profile with the following information:

- Email
- First and Last Name
- City, State/Region, Zip Code, Country
- Phone Number
- Magento Account Created (e.g., 2015-05-01 00:00:00)
- Magento Customer Group (e.g., Wholesale)
- Magento Store (e.g., US Store)
- Date of Birth (e.g., 1990-01-01)
- Gender
- website\_ID will not be pulled
- Suppressions are not copied into Klaviyo so they will not be in the Klaviyo platform

If you update the customer group in Magento, even after the original profile has been created in Klaviyo, the customer group will update in Klaviyo.

- Website\_ID will not be pulled. Suppressions are not copied into Klaviyo so they will not be in the Klaviyo platform.
- Custom image locations will not be pulled. Klaviyo cannot pull custom image locations.

## Sync custom product attributes for placed orders

Klaviyo can sync up to 10 custom product attributes for the Placed Order metric. Custom product attributes will not automatically flow into Klaviyo; however, you can request that Klaviyo to pull them in. To do this, you should collect the custom attribute ID (instructions below) and send a request to [our support team](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272).

Find the Custom Product IDs in the Magento's Admin panel by going to ****Catalog > Attributes > Manage Attributes**** and clicking on the attribute.

The ID can be found in the url like so:

![A product ID found via the Magento admin panel](https://klaviyo.zendesk.com/hc/article_attachments/28715969072795)

## Verify your synced order data

Klaviyo imports all of your Magento data. To verify this, you can compare the number of orders on a particular day with what's in the Magento interface and confirm they match. Click on **Analytics** in the left sidebar, find the Placed Order metric and click on it. This will take you to the metric chart page and show the last 30 days of data by default. You can see an example of the metric chart displayed below.

Mouseover yesterday's data point or look in the table of data below the chart to see how many orders you had yesterday. Compare that number to what's stored in Magento and you should see they match exactly. If they don't, the most likely issue is your Klaviyo account's timezone doesn't match your Magento timezone. To check your timezone setting:

1. Click your organization name in the bottom left.
2. Click ****Settings****.
3. Select ****Organization******.**

![A graph of Magento 1 placed order metrics over time](https://klaviyo.zendesk.com/hc/article_attachments/28715962468891)

You may see that the **Revenue** value on your Klaviyo dashboard does not always match up with the revenue value you see in Magento; this is because Klaviyo does not subtract cancelled and refunded orders from our revenue calculation.

## Properties for synced magento orders

Below are example JSON payloads for the Placed Order, Ordered Product, and Fulfilled Order metrics that match the properties we store for orders synced through the Magento SOAP API.

This is useful for sending the correct properties for orders that will be combined with Magento order data.

### Placed Order

```
//
// PLACED ORDER
// ------------------------------------------

{
  "token" : "PUBLIC_API_KEY",
  "service" : "magento",
  "event" : "Placed Order",
  "customer_properties" : {
    "$email" : "john.smith@test.com",
    "$first_name" : "John",
    "$last_name" : "Smith"
  },
  "properties" : {
    "$event_id" : "1234",
    "$value" : 29.98,
    "$extra" : {},
    "Currency Code" : "USD",
    "Item Count" : 2,
    "Items" : ["Winnie the Pooh", "A Tale of Two Cities"], // If an item is ordered more than once, duplicate it. For example, someone orders two t-shirts this would be: ["T-Shirt", "T-Shirt"]
    "Discounted" : true,
    "Coupon" : "COUPON123",
    "Unique Items" : ["Winnie the Pooh", "A Tale of Two Cities"],
    "Item Categories" : ["Fiction", "Classics", "Children"],
    "Unique Item Categories" : ["Fiction", "Classics", "Children"]
  },
  "time" : 1387302423
}
```

### Ordered Product

```
//
// ORDERED PRODUCT
// ------------------------------------------

{
  "token" : "PUBLIC_API_KEY",
  "service" : "magento",
  "event" : "Ordered Product",
  "customer_properties" : {
    "$email" : "john.smith@test.com",
    "$first_name" : "John",
    "$last_name" : "Smith"
  },
  "properties" : {
    "$event_id" : "123456789", // LineId (unique)
    "$value" : 9.99,
    "Currency Code" : "USD",
    "Name" : "Winnie the Pooh",
    "SKU" : "WINNIEPOOH",
    "ProductID" : "567",
    "Categories" : ["Fiction", "Classics"],
    "Price" : 9.99,
    "Discounted" : true,
    "Cost" : 5.00, // (optional),
    "Attribute: Color" : "Red" // product attributes (optional)
    "$extra" : {
        "Product URL Key" : "winnie-pooh",
        "Product URL" : "https://www.store.com/winnie-pooh",
        "Image URL" : "https://cnd.store.com/images/winnie-pooh.png",
    }
  },
  "time" : 1387302423
}
```

### Fulfilled Order

```
//
// FULFILLED ORDER
// ------------------------------------------

{
  "token" : "PUBLIC_API_KEY",
  "service" : "magento",
  "event" : "Fulfilled Order",
  "customer_properties" : {
    "$email" : "john.smith@test.com",
    "$first_name" : "John",
    "$last_name" : "Smith"
  },
  "properties" : {
    "$event_id" : "1234",
    "$value" : 29.98,
    "$extra" : {},
    "Currency Code" : "USD",
    "Item Count" : 2,
    "Items" : ["Winnie the Pooh", "A Tale of Two Cities"], // If an item is ordered more than once, duplicate it. For example, someone orders two t-shirts this would be: ["T-Shirt", "T-Shirt"]
    "Discounted" : true,
    "Coupon" : "COUPON123",
    "Unique Items" : ["Winnie the Pooh", "A Tale of Two Cities"],
    "Item Categories" : ["Fiction", "Classics", "Children"],
    "Unique Item Categories" : ["Fiction", "Classics", "Children"]
  },
  "time" : 1387302423
}
```

## Additional resources

- [How to integrate with Magento 1.x (CE and EE)](https://klaviyo.zendesk.com/hc/en-us/articles/115005082187)
- [Magento integration system requirements reference](https://klaviyo.zendesk.com/hc/en-us/articles/360048730411)