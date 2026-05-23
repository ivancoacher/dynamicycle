<h1>BigCommerce data reference</h1>

## You will learn

Learn what data is synced to Klaviyo when you integrate with your BigCommerce store, such as order and customer data, and how to access it in Klaviyo.

## Metrics synced from BigCommerce

After you've [integrated with BigCommerce](https://klaviyo.zendesk.com/hc/en-us/articles/115005082547), click the ****Analytics**** dropdown in Klaviyo and select ****Metrics**** to see all of the metrics in your account. Here, you can filter by BigCommerce to see which metrics are synced from the integration.
![Metrics tab in Klaviyo filtered by BigCommerce showing metrics list including Cancelled Order and Fulfilled Order](https://klaviyo.zendesk.com/hc/article_attachments/28704476453275)

Note that the top-level true/false property Discounted, which is included in many of these metrics, is determined by the discount amount from a coupon. If, for instance, you offer free shipping, but it is not reflected in the discount amount, it will not be reflected in the Discounted property, which will show as False.

### Started Checkout

BigCommerce **Started Checkout** events are tracked when a cart is created. If you have customer accounts on your site, there are some cases in which this cart will be created when the first item is added to the cart, rather than when the customer enters their contact and shipping information and clicks continue.

The event Klaviyo tracks includes all of the product information about the items in someone's cart including product names, images and category information so you can use that information in your Abandoned Cart emails.

- ****$value****The total value of the cart at time of checkout
- ****Discounted****
  Whether or not a discount code was used (true/false)
- ****Item Categories****The complete set of the categories of the products in someone's cart, e.g., **t-shirts, mens, pants** and**sale**
- ****Item Count****The number of items in the order, e.g., **2**
- ****Items****The names of the products in someone's order, e.g., **t-shirt**or **pants**
- ****Coupons****(optional array)
- ****ChannelID****
  The ID of the channel for the checkout

### Placed Order

This event is tracked when a customer completes the checkout process and creates an order in your BigCommerce store.

By default, when Klaviyo polls for new orders, any order with any of the following statuses will not sync as a Placed Order: `Incomplete`, `Pending`, `Awaiting Payment`.

The **Placed Order** event Klaviyo tracks includes all of the product information about the items someone purchased including product names, images, and category information so you can use this information in purchase follow up emails. You can filter and target **Placed Order** events based on the following criteria:

- ****$value****The total value of the cart at time of checkout
- ****Discounted****Whether or not a discount code was used (true/false)
- ****Item Categories****The complete set of the categories of the products in someone's cart, e.g., **t-shirts, mens, pants** and**sale**
- ****Item Count****The number of items in the order, e.g., **2**
- ****Items****The names of the products in someone's order, e.g., **t-shirt**or **pants**
- ****Coupons****(optional array)
- ****ChannelID****
  The ID of the channel for the order

Revenue, or **Placed Order** value, is calculated as follows: (sub-total + shipping) - any discounts.

You may see that the **Revenue**value on your Klaviyo dashboard does not always match up with the revenue value you see in BigCommerce; this is because BigCommerce subtracts refunded orders from their revenue calculation, while Klaviyo does not.

### Ordered Product

This event is tracked when a customer places an order, but one event is tracked for each item someone purchases. For example, if someone buys a t-shirt and a pair of pants, one **Placed Order** event is tracked and two **Ordered Product** events - one event for the t-shirt and one event for the pants.

The event Klaviyo tracks include detailed information about each product someone purchases. This is useful when creating behavioral segments based on product variation options and other detailed information that's not available in the **Placed Order** event. You can filter and target **Ordered Product** events based on the following criteria:

- ****Name****The name or title of the product in BigCommerce, e.g., **t-shirt**
- ****$value****The value of the item (product price minus any discounts)
- ****SKU****
- The SKU of the product variation e.g., **REDMEDIUMTSHIRT**
- ****Categories****The complete set of the categories of the product, e.g., **t-shirts, mens** and**sale**
- ****Product Price****The price of the product
- ****Product Cost****The cost of the product
- ****Price****The price of the entire order for that product
- ****Discounted****Whether or not a discount code was used (true/false)
- ****ProductID****The ID of the ordered product
- ****Quantity****The quantity of the ordered product
- ****Option (Optional)****Custom product attributes
- ****ChannelID****
  The ID of the channel for the order

### Fulfilled Order

This event is tracked when an order's status updates to either `Shipped` or `Completed`.

The **Fulfilled Order** event Klaviyo tracks includes all of the product information about the items someone purchased including product names, images and variation information so you can use that information in purchase follow up emails. You can filter and target **Fulfilled Order** events based on the following criteria:

- ****$value****The total value of the cart at time of checkout
- ****Discounted****Whether or not a discount code was used (true/false)
- ****Item Categories****The complete set of the categories of the products in someone's cart, e.g., **t-shirts, mens, pants** and**sale**
- ****Item Count****The number of items in the order, e.g., **2**
- ****Items****The names of the products in someone's order, e.g., **t-shirt**or **pants**
- ****Coupons****(optional array)
- ****ChannelID****
  The ID of the channel for the order

### Cancelled Order

This event is tracked when a customer creates an order in your BigCommerce store but then cancels the order before fulfillment (when the order status is equal to `Cancelled`). The event Klaviyo tracks include all of the product information about the items someone purchased including product names, images and variation information so you can use that information in purchase follow up emails. You can filter and target **Cancelled Order** events based on the following criteria:

- ****$value****The total value of the cart at time of checkout
- ****Discounted****Whether or not a discount code was used (true/false)
- ****Item Categories****The complete set of the categories of the products in someone's cart, e.g., **t-shirts, mens, pants** and**sale**
- ****Item Count****The number of items in the order, e.g., **2**
- ****Items****The names of the products in someone's order, e.g., **t-shirt**or **pants**
- ****Coupons****(optional array)
- ****ChannelID****
  The ID of the channel for the order

### Refunded Order

This event is tracked when a customer refunds their order. You can filter and target **Refunded Order** events based on the following criteria:

- ****$value****The total value of the refunded order
- ****Items****The names of the products in someone's order, e.g., **t-shirt**or **pants**
- ****Item Categories****The complete set of categories of the products in the order
- ****Item Count****The number of items in the order, e.g., **2**
- ****Item Brands****The brands of the products in the order
- ****Discounted****Whether or not a discount code was used (true/false)
- ****Status****The status of the order, e.g., **Refunded**
- ****ChannelID****
  The ID of the channel for the order

## Customer data synced from BigCommerce

In addition to the metrics Klaviyo syncs from BigCommerce, there are also custom properties that are added to each Klaviyo profile. You can use these properties in segments and in flows. Here are the properties that are automatically synced from BigCommerce:

- ****Email, First Name, Last Name, City, Phone Number****These built-in Klaviyo fields are automatically synced with the integration.

  Location information (City, State/Region, Zip Code, Country) is only synced to Klaviyo if the customer has placed an order.
- ****External ID****Klaviyo also syncs customers' external IDs. This means that if a customer creates an account with your BigCommerce store, we will sync this ID along with their email address. If the same customer then goes on to change the email address associated with the account, we will map the new address to their external ID and update the email address associated with their profile.
- ****BigCommerce Original Channel ID****This property lists the ID of the first storefront visited by the profile, if tracked. Storefront is tracked if you are using BigCommerce Multi-Storefront (MSF) and the customer has started a checkout or placed an order.
- ****BigCommerce Channel IDs****An array of IDs that includes the ID of each storefront visited by the profile, if tracked. Storefront is tracked if you are using BigCommerce Multi-Storefront (MSF) and the customer has started a checkout or placed an order.

If a customer does not create an account, no external ID will be created, and we will use their email address to map all data. If a customer does not create an account at first, but later creates one with the same email address, an external ID will be added to their profile.

You may have additional custom properties associated with your BigCommerce profiles. These two custom properties can also be synced to Klaviyo:

- ****Customer Group****
  [Customer Groups](https://support.bigcommerce.com/s/article/Customer-Groups) allow you to organize your customers, give them discounts, and restrict access to specific products or categories.
- ****Store Credit****

Custom properties are found in the **Information - Custom Properties** section of a Klaviyo profile:
![Information section of customer profile in Klaviyo showing custom properties synced from BigCommerce including Store Credit and Customer Group](https://klaviyo.zendesk.com/hc/article_attachments/28704476452251)

## Frequency of the BigCommerce sync

Metrics and profile properties from BigCommerce are synced in real-time. This means you should see all events appear in Klaviyo almost immediately when the event is tracked in BigCommerce.

## How to verify your synced order data

Klaviyo imports all of your BigCommerce data. When you first integrate, we will run a full historic sync. After the initial sync, Klaviyo runs hourly syncs to poll for new data. To verify this, you can compare the number of daily orders tracked within Klaviyo with the number of daily orders in BigCommerce.

1. In Klaviyo, navigate to ****Analytics > Metrics****.
2. Find the **Placed Order** metric, and click on it. This will take you to the metric chart page and show the last 30 days of data by default.
3. Mouse over yesterday's data point or look in the table of data below the chart to see how many orders you had yesterday. Compare that number to what's stored in BigCommerce and you should see they match exactly.
4. If they don't, the most likely issue is your Klaviyo account's timezone doesn't match BigCommerce's timezone. To check your timezone setting, click your account name in the lower left corner, then navigate to ****Settings > Organization.****![Graph of BigCommerce Placed Orders over time in Klaviyo metrics tab](https://klaviyo.zendesk.com/hc/article_attachments/28704476454427)

## Additional resources

- [Getting started with BigCommerce](https://klaviyo.zendesk.com/hc/en-us/articles/115005082547)
- [How to create an Added to Cart event for BigCommerce](https://klaviyo.zendesk.com/hc/en-us/articles/360024310292)
