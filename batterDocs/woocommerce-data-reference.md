<h1>WooCommerce data reference</h1>

## Data Synced with the WooCommerce Integration

This article covers the data that is synced when you integrate your WooCommerce store with your Klaviyo account.

Klaviyo syncs with WooCommerce in real time.

In your Klaviyo account, navigate to your [Analytics](https://www.klaviyo.com/analytics/metrics) tab and select Metrics to see all of the metrics in your account. All WooCommerce metrics will have a WooCommerce icon, with the exception of the Added to Cart metric, which will have a gear icon. Each metric is covered individually below.
 ![](https://klaviyo.zendesk.com/hc/article_attachments/33638284951835)![mceclip0.png](https://klaviyo.zendesk.com/hc/article_attachments/28716329763867)

Klaviyo limits the number of unique metrics you can create to 200. When you approach this threshold, you will be alerted via a warning in your account, along with an email to the account owner.

## Started Checkout

This event tracks when one of the following occurs:

- A customer is logged into their account, has added something to their cart, then views the checkout page
- A customer adds something to their cart, views the checkout page, enters a billing email address

You can filter and target Started Checkout metrics based on the following criteria:

- ****$value****: The value of the cart
- ****Categories****: The categories of the items in the cart
- ****Currency****: The currency type for the cart
- ****CurrencySymbol****: The currency symbol for the cart
- ****ItemNames****: An array containing the names of the items in the cart

Klaviyo captures the value of a cart at time of checkout, as well as other pertinent details of a customer's cart that you can leverage for personalized Abandoned Cart emails. There are two possible Abandoned Cart flows for WooCommerce: a flow triggered by the Started Checkout metric, or the Added to Cart metric. Both metrics allow you to leverage the cart rebuild key, a key that allows you to create a link that rebuilds the customer's cart in case they return to their cart via an email triggered by this event on another device. This key can be found within the 'extra' property array. You can create this link using the following URL:

`{{ organization.url|trim_slash }}/cart?wck_rebuild_cart={{ event.extra.CartRebuildKey }}`

## Added to Cart

This metric is tracked whenever a customer who has been cookied by Klaviyo adds an item to their cart.

It includes detailed information about the item that was added. This is useful when creating segments based on what products users have added to their carts, or when building an abandoned cart flow. You can filter and target Added to Cart metrics based on the following criteria:

- ****$value****: Value of the item
- ****AddedItemCategories****: The categories to which the item belongs
- ****AddedItemDescription****: The description of the item
- ****AddedItemImageURL****: The URL of the image of the item
- ****AddedItemPrice****: The price of the item
- ****AddedItemProductID****The custom ID in your WooCommerce store of the product, e.g., **1234**
- ****AddedItemProductName****: The name of the product in your store, e.g., **Red T-shirt**
- ****AddedItemQuantity****: The quantity of the item
- ****AddedItemSKU****: The SKU of the item in your store, e.g., **REDMEDIUMTSHIRT**
- ****AddedItemTags****: Any tags associated with the item
- ****AddedItemURL****: The URL of the item
- ****Categories****: The categories of all the items in the cart
- ****ItemCount****: The count of the total items in the cart
- ****ItemNames****: The names of all the items in the cart
- ****Tags****: The tags of all the items in the cart

Klaviyo generates a key, the cart rebuild key, that allows you to create a link that rebuilds the customer's cart in case they return to their cart via an email triggered by this event on another device. This key can be found within the ‘extra’ property array. You can create this link using the following URL:

`{{ organization.url|trim_slash }}/cart?wck_rebuild_cart={{ event.extra.CartRebuildKey}}`

The ‘extra’ property array, while not segmentable, contains useful information in addition to the cart rebuild key, such as: line items for the cart, the cart’s grand total, the cart’s subtotal, and the cart’s tax total.

## Placed Order

This event tracks when a customer completes the checkout process and creates an order in your WooCommerce store. Klaviyo records a Placed Order event when we sync an order with the status of processing.

The event Klaviyo tracks includes all product information captured by WooCommerce so that you can use this detailed data in purchase follow up emails. You can filter and target Placed Order events based on the following criteria:

- ****$value:****The value of the order
- ****ItemNames****: The names of the products in someone's order, e.g., **t-shirt** or **pants**
- ****IsDiscounted****: Order has been discounted; **true** or **false**
- ****UsedCoupon****: A coupon was used on the order, e.g., **true** or **false**
- ****ItemCategories:**** The categories to which the items in the cart belong
- ****ShippingMethods (if any)****
- ****Coupons (if any)****

Revenue, or **Placed Order** value, is calculated as follows: (sub-total + shipping) - any discounts.

You may see that the **Revenue** value on your Klaviyo dashboard does not always match up with the revenue value you see in WooCommerce; this is because WooCommerce subtracts refunded orders from their revenue calculation, while Klaviyo does not.

## Fulfilled Order

This event tracks when an order moves to "Complete" in your WooCommerce store.

The event Klaviyo tracks includes all of the product information about the items someone purchased including product names, images, and variable product information so you can use that information in purchase follow up emails. You can filter and target **Fulfilled Order** events based on the following criteria:

- ****$value:****The value of the order
- ****ItemNames****: The names of the products in someone's order, e.g., **t-shirt** or **pants**
- ****IsDiscounted****: Order has been discounted; **true** or **false**
- ****UsedCoupon****: A coupon was used on the order, e.g., **true** or **false**
- ****ItemCategories:**** The categories to which the items in the cart belong
- ****ShippingMethods (if any)****
- ****Coupons (if any)****

## Ordered Product

This event is tracked when a customer places an order, but one event is tracked for each item someone purchases. For example, if someone buys a t-shirt and a pair of pants, one Placed Order event is tracked and two Ordered Product events -- one event for the t-shirt and one event for the pants.

The event Klaviyo tracks includes detailed information about each product someone purchases. This is useful when creating behavioral segments based on product options and other detailed information that's not available in the Placed Order event. You can filter and target Ordered Product events based on the following criteria:

- ****$value:****Value of the item
- ****ProductId****: The custom ID of a product in your WooCommerce store, e.g., **1321**
- ****SKU****: The SKU of the product in your store, e.g., **REDMEDIUMTSHIRT**
- ****Name****: The name of a product in your store, e.g., **Red T-shirt**
- ****Quantity:****The quantity of the item ordered
- ****Categories****: List of categories

## Cancelled Order

This event is tracked when a customer creates an order in your WooCommerce store but then cancels the order before fulfillment. You can filter and target **Cancelled Order** events based on the following criteria:

- ****$value:****The total value of the cancelled order
- ****IsDiscounted:**** Order has been discounted; **true** or **false**
- ****ProductNames:****The names of the different products in the order
- ****UsedCoupon:**** A coupon was used on the order, e.g., **true** or **false**
- ****ItemCategories:**** The categories to which the items in the cart belong
- ****ItemNames:**** The names of the products in someone's order, e.g., **t-shirt** or **pants**
- ****Coupons (if any)****
- ****ShippingMethods (if any)****

## Refunded Order

This event is tracked when a customer refunds their order. You can filter and target **Refunded Order** events based on the following criteria:

- ****$value:****The total value of the refunded order
- ****IsDiscounted:**** Order has been discounted; **true** or **false**
- ****ProductNames:**** The names of the different products in the order
- ****UsedCoupon:**** A coupon was used on the order, e.g., **true** or **false**
- ****ItemCategories:**** The categories to which the items in the cart belong
- ****ItemNames:**** The names of the products in someone's order, e.g., **t-shirt** or **pants**
- ****Coupons (if any)****
- ****ShippingMethods (if any)****

## Viewed Product

This event is tracked when a customer (previously cookied by Klaviyo) views a product. This is useful if you'd like to set up a [Browse Abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow) or build segments based on product browsing data.

## Active on Site

This event is tracked when a customer (previously cookied by Klaviyo) is active on your site.

## Customer Data

For each customer in your WooCommerce account, a profile is created in your Klaviyo account. Customer information including first name, last name, and location is added to this profile.
