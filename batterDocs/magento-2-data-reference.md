<h1>Magento 2 data reference</h1>

Learn what data Klaviyo imports from your Magento 2 store when you integrate the two platforms. Klaviyo's integration with Magento 2 pulls in all of the historical data in your Magento 2 store with the initial historic sync. Once enabled the integration will also begin to sync order and customer data every 30 minutes. Examples of this data include the information associated with past placed orders, fulfilled orders, etc.

In Klaviyo, you can navigate to your account's **Analytics tab** in the left sidebar to view all of the metrics in your account; the metrics with a Magento 2 icon are the order events synced from your Magento 2 integration. You will also see Klaviyo onsite tracking events with a gear icon; these are also tracked through the integration.

![](https://klaviyo.zendesk.com/hc/article_attachments/35507590825499)

****![](https://klaviyo.zendesk.com/hc/article_attachments/35507597379867)****

## How Klaviyo determines Magento 2 metrics

### Order metrics

Magento 2 order metrics are determined by the **Status** field in an order in your Magento 2 store.

Each time an order is created, or its status is updated, it will be evaluated against the matrix below to determine which events should be triggered.

|  |  |
| --- | --- |
| ****Magento Order Status**** | ****Metric Triggered in Klaviyo**** |
| complete | Fulfilled Order |
| canceled, cancelled | Canceled Order |
| pay\_aborted | Canceled Payment |
| closed | Refunded Order |
| All other order statuses | Placed Order |

If you have custom order statuses that should not trigger a **Placed Order** metric, or do not align with the table above, [please let us know](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272) and we can adjust the order status mapping accordingly in your integration.

Orders with a status of “pending\_payment” will be ignored.

### Started Checkout metric

With a standard Magento checkout, this event is triggered when a customer enters their contact and shipping information on the first page of the Magento checkout process and clicks **Continue**.

The **Started Checkout** event relies on a “Quote” being created and having an email address associated with it. This happens after the customer has entered their email address at the “Shipping Information” stage of checkout. If a customer does not complete the checkout, this quote is synced to Klaviyo as a **Started Checkout** event.

If the customer proceeds to complete the order, this quote is converted to an “invoice” in Magento’s database. As a result a **Started Checkout** event is not sent to Klaviyo. Instead, a **Placed Order** event is sent. Note that it may take up to 1 hour for **Started Checkout** events to sync to Klaviyo.

### Fulfilled Shipment metric

This metric is triggered when a new Shipment is created in your Magento 2 store.

## Magento 2 metric data

This section covers each of the Magento 2 metrics and the data that is available for filtering when creating segments and flows.

### Cancelled Order

This event is triggered when an order status is changed to **cancelled** or **canceled** in your Magento 2 store.

- ****ProductCategories****The categories of the products in the cancelled order.
- ****Value****The value of the cancelled order.
- ****Discounted****(True or False) The discount state of the cancelled order.
- ****OrderedProducts****The names of the products in the cancelled order.
- ****OrderedProductCount****The number of products in the cancelled order.
- ****OrderCurrencyCode****The currency code used with the cancelled order.
- ****CartPriceRuleIDs****An array of Cart Price Rule IDs (numeric id strings) which include automatically applied rules and the rule for an applied coupon.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.

### Fulfilled Order

This event is tracked when you set an order status to **complete** in your Magento 2 store.

- ****ProductCategories****The categories of the products in the order.
- ****Value****The value of the order.
- ****Discounted****Whether the order is discounted or not.
- ****OrderedProducts****The names of the products in the order.
- ****OrderedProductCount****The number of products in the order.
- ****OrderCurrencyCode****The currency code used with the order.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.

### Fulfilled Shipment

This event is tracked when a new **Shipment** is created in your Magento 2 store.

- ****StoreName****The name of the store where the order was placed.
- ****StoreID****The ID of the store where the order was placed.
- ****BillingAddress****The billing address for the order.
- ****Tracks****Information on shipment tracking.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.

### Ordered Product

This event is tracked once for every product a user orders when they place an order.

- ****SKU****The SKU of the product.
- ****OrderCurrencyCode****The currency code of the product.
- ****Price****The value of the product.
- ****Categories****The category of the product.
- ****Discounted****Any discounts applied to the product.
- ****Quantity****The number of products.
- ****Value****The value of the product.
- ****ProductID****The ID of the product.
- ****RootProductID****The ID of the parent product.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.

Ordered Product metric has a number of other data fields available for tracking. [View the raw data](https://help.klaviyo.com/hc/en-us/articles/115005076747-View-Raw-Metric-or-Event-Data-in-Klaviyo) of an individual Ordered Product event to see all of the available data for this event.

### Placed Order

This event is tracked when a user places an order.

- ****ProductCategories****The categories of the products in the order.
- ****Value****The value of the order.
- ****Discounted****Whether the order is discounted or not.
- ****OrderedProducts****The names of the products in the order.
- ****OrderedProductCount****The number of products in the order.
- ****OrderCurrencyCode****The currency code used with the order.
- ****CartPriceRuleIDs****An array of Cart Price Rule IDs (numeric id strings) which include automatically applied rules and the rule for an applied coupon.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.

### Refunded Order

This event is triggered when a customer refunds an order.

- ****Value****The value of the order.
- ****Discounted****Whether the order is discounted or not.
- ****OrderedProducts****The names of all the products in the order.
- ****OrderedProductCount****The number of products in the order.
- ****OrderCurrencyCode****The currency code used with the order.
- ****ProductCategories****The categories of the products in the order.
- ****CartPriceRuleIDs****An array of Cart Price Rule IDs (numeric id strings) which include automatically applied rules and the rule for an applied coupon.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.

### Started Checkout

This event is triggered when a customer with a known email address begins a checkout. On a standard checkout page this event is triggered when a customer enters their contact and shipping information on the first page of the Magento checkout process and clicks **Continue**. A **Started Checkout** event is not sent to Klaviyo if the user completes checkout. Instead, a **Placed Order** event is logged.

- ****Value****The value of the order during the checkout.
- ****ItemCount****The number of items in the order.
- ****Items****The items in the order.
- ****ProductCategories****The categories of the products in the order.
- ****ProductNames****The names of the products in the order.
- ****StoreName****The name of the store where the order was started.
- ****StoreID****The ID of the store where the order was started.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.

### Added To Cart

Please note that this metric is only tracked if you are using Klaviyo extension version 4.0.0 and above. This metric is tracked when a customer who has been cookied by Klaviyo adds an item to their cart.

It includes detailed information about the item that was added. This is useful when creating segments based on what products users have added to cart, or when building an abandoned cart flow. You can filter and target **Added To Cart** metrics based on the following criteria:

- ****MaskedQuoteId****MaskedQuoteId or Unique identifier for logged in customers.
- ****AddedItemCategories****The categories to which the item belongs.
- ****AddedItemProductName****The name of the product in your store (e.g., Red T-shirt).
- ****AddedItemDescription****The description of the item.
- ****AddedItemImageURLKey****The URL of the image of the item.
- ****AddedItemPrice****The price of the item.
- ****AddedItemProductID****The custom ID in your Magento 2 store of the product, e.g., 1234.
- ****AddedItemSKU****The SKU of the item in your store (e.g., REDMEDIUMTSHIRT).
- ****AddedItemURL****The URL of the item.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.
- ****integration\_key****
  Your eCommerce platform (Magento 2).

Klaviyo generates a key, the cart rebuild key, that allows you to create a link that rebuilds the customer's cart in case they return to their cart via an email triggered by this event on another device. This key can be found within the ‘extra’ property array. You can create this link using the following URL:

```
{{ organization.url|trim_slash }}reclaim/checkout/cart?quote_id={{ event.MaskedQuoteId }}
```

### Viewed Product

This metric is tracked when a customer views a product on your site. You can filter and target **Viewed Product** metrics based on the following criteria:

- ****ProductID****
  The ID of the product.
- ****Name****
  The name of the product.
- ****SKU****
  The SKU for the product.
- ****URL****
  The URL for the product.
- ****Price****
  The price of the product.
- ****FinalPrice****
  The final price after any discounts.
- ****Categories****
  An array containing the categories the product belongs to.
- ****ImageURL****
  The URL for the product's image.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.
- ****integration\_key****
  Your eCommerce platform (Magento 2).

### Active on Site

This metric is tracked when a customer is active on your site. You can filter and target **Active on Site** metrics based on the following criteria:

- ****utm\_medium****
  The medium for the utm tracking parameter (e.g., campaign).
- ****kx\_present****
  (True or False) Whether the [kx parameter](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACCVC5TX5932PQ2AZA) is present.
- ****os****
  The operating system of the user's device.
- ****initial\_page\_path****
  The URL path of the initial page the user landed on.
- ****browser****
  The user's browser type.
- ****page****
  The URL of the page the user was active on.
- ****utm\_campaign****
  The UTM tracking parameter for the campaign.
- ****utm\_source****
  The UTM source (e.g., Klaviyo).

### Synced customer data

Klaviyo creates a contact from the creation of an existing order, an existing customer record, or when a checkout is started. Klaviyo will create a new Klaviyo Profile for every synced contact, and will populate this profile with the following information:

- Email
- First and Last Name
- City, State/Region, Zip Code, Country
- Phone Number
- Magento Account Created (e.g., YYY-mm-dd hh:mm:ss; 2015-05-21 13:04:00)
- Magento Customer Group (e.g., Wholesale)
- Magento Store (e.g., US Store)
- Date of Birth (e.g., YYYY-mm-dd; 1990-03-25)
- Gender

If you update the customer group in Magento 2, even after the original profile has been created in Klaviyo, the customer group will update in Klaviyo.

Website\_ID will not be pulled. Suppressions are not copied into Klaviyo so they will not be in the Klaviyo platform.

Klaviyo cannot pull custom image locations.

## Revenue value

You may see that the **Revenue** value on your Klaviyo dashboard does not always match up with the revenue value you see in Magento; this is because Klaviyo does not subtract cancelled and refunded orders from our revenue calculation.

## Additional resources

- [How to integrate with Magento 2.x (CE and EE)](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348)
- [Troubleshooting your Magento 2 integration](https://klaviyo.zendesk.com/hc/en-us/articles/5510750923035)
