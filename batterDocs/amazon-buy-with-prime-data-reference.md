<h1>Amazon Buy with Prime data reference</h1>

## You will learn

Learn what data syncs from Buy with Prime to Klaviyo and how to view it. This includes both order data (events such as **Placed Order**, **Ordered Product**, etc.) and customer data.

## Before you begin

If you have not already set up the integration, follow our guide on [Getting started with Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467) for step-by-step instructions.

Buy with Prime order data is only synced for profiles that have an email address.

## Table of contents

1. How to view your data
2. Buy with Prime metrics
3. Synced customer data
4. Frequency of the Buy with Prime sync

## How to view your data

1. In Klaviyo, click the ****Analytics**** dropdown in the left-hand navigation.
2. Select ****Metrics****.

Here, you can view all of the metrics in your account. The metrics with a Buy with Prime icon represent all of the metrics synced from your Buy with Prime integration.

In the upper right corner, you can filter your metrics by **Amazon Buy with Prime**.
![Metrics tab filtered by Amazon Buy with Prime showing list of metrics](https://klaviyo.zendesk.com/hc/article_attachments/28722598213915)

## Buy with Prime metrics

Below is a list of all the metrics synced from Buy with Prime and an explanation of the data included with each metric. If you are interested in learning more, read this article on how to [review the raw metric data](https://help.klaviyo.com/hc/en-us/articles/115005076747-View-Raw-Metric-or-Event-Data-in-Klaviyo) that gets synced to Klaviyo****.****

### Checkout Started

This event is tracked when a customer clicks **Proceed to checkout** on their Buy with Prime cart and authenticates with their Prime account.

The event that Klaviyo tracks includes product information about items in the cart, including product names, images, and variant information for use in personalized messaging.

You can filter and target **Checkout Started** events based on the following criteria:

- ****$value****
  The total value of the cart at the time the customer started the checkout. This may include any line prices, taxes, shipping costs, tips, and discounts.
- ****items****Information about the items in the cart, including the price, quantity, SKU, ProductID, product page URL, and more.
- ****itemNames****The item names in the order.
- ****CheckoutURL****The URL that can be clicked to return to the rebuilt checkout page (from any device), which can be used in abandoned cart emails.

### Placed Order

This event is tracked when a customer completes the checkout process using Buy with Prime. The event Klaviyo tracks includes all of the product information about the items the customer purchased including product names, images, and variant information for use in email messaging. You can filter and target **Placed Order** events based on the following criteria:

- ****$value****
  The total value of the placed order, including shipping and any applied discounts.
- ****items****Information about all the items in the order, including the price, quantity, SKU, ProductID, product page URL, and more for each item.
- ****itemNames****An array of item names in the order.
- ****categories****The complete set of categories associated with the products in someone's order, e.g., **T-shirts, mens, pants,** and **sale.**
- ****discountCode****Any discount or coupon codes used toward the order, e.g., **SPRING10.**
- ****discountValue****The total amount of any coupons or discounts if someone used a code, e.g., **10.00.**
- ****shippingAddress****The recipient’s name and shipping address for the order.
- ****billingAddress****The purchaser’s name and billing address for the order**.**

### Ordered Product

This event is tracked when a customer places an order, with a separate event for each item a customer purchases.

The event Klaviyo tracks includes detailed information about each product someone purchases. This is useful when creating behavioral segments based on product variant options and other detailed information. You can filter and target **Ordered Product** events based on the following criteria:

- ****$value****
  The total value of the item purchased; no shipping costs or discounts included.
- ****productID****
  The ID of the purchased product.
- ****SKU****The SKU of the product variant.
- ****productName****
  The name or title of the ordered product in Buy with Prime.
- ****Quantity****Quantity of the item that was purchased.
- ****productURL****The URL of the product page.
- ****imageURL****A URL hosting an image of the product.
- ****categories****The complete set of categories or categories applied to the product, e.g., **T-shirts, men's,** and **sale**.

### Fulfilled Order

This event is tracked when an order is marked as **Fulfilled** in your Buy with Prime merchant console.

The event Klaviyo tracks includes all product information about the items in the order, including product names and images for use in purchase follow-up emails. You can filter and target **Fulfilled Order** events based on the following criteria:

- ****$value****
  The total value of the fulfilled order.
- ****Items****
  The names of the products in someone's order.
- ****Collections****
  The complete set of the collections associated with the products in someone's order.
- ****Item Count****
  The count of line items in the order, e.g., **2.**
- ****Discount Codes****
  Any discount or coupon codes someone used toward the order, e.g., **SPRING10**.
- ****Total Discounts****
  The total amount of any coupons or discounts if someone used a code, e.g., **10.00**.

### Canceled Order

This event is tracked when a customer creates an order using Buy with Prime checkout but then cancels the order before fulfillment. The event Klaviyo tracks includes all of the product information about the items someone purchased including product names and images. You can filter and target **Canceled Order** events based on the following criteria:

- ****$value****
  The total value of the canceled order.
- ****Items****
  The names of the products in the order, e.g., **T-shirt** or **pants**.
- ****Collections****
  The complete set of the collections of the products in the order.
- ****Item Count****
  The count of line items in the order, e.g., **2.**
- ****Discount Codes****
  Any discount or coupon codes used toward the order, e.g., **SPRING10**.
- ****Total Discounts****
  The total amount of any coupons or discounts if someone used a code, e.g., **10.00**.

## Synced customer data

In addition to the metrics synced from Buy with Prime, Klaviyo will also create a unique profile for every customer that we sync. Along with contact information, we sync certain custom properties to the Klaviyo profile if they are present. You can use these properties in segments and flows. Here are the properties that are synced from Buy with Prime:

- ****Email, First and Last Name, City, State/Region, Zip Code, Country, Phone Number****
  These built-in Klaviyo fields are automatically populated with all available data from Buy with Prime.

The Buy with Prime platform is an “opt-out” marketing consent platform. This means that anyone who provides you their email address has not been given the opportunity to explicitly consent to your email marketing. Instead, Klaviyo will mark those who have provided their email address as “Never Subscribed.”

## Frequency of the Buy with Prime sync

Metrics and profile properties from Buy with Prime are synced in near real-time.

## Additional resources

- [Getting started with Amazon Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467)
- [How to create an abandoned cart flow for Amazon Buy with Prime](https://klaviyo.zendesk.com/hc/en-us/articles/14985388418331)
