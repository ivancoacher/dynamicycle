<h1>Shopify data reference</h1>

## You will learn

Learn what data syncs from Shopify to Klaviyo and where to view it. This includes both order data (such as **Placed Order**, **Ordered Product**, etc.), delivery data, onsite tracking data, and customer data. If you have not already, read our guide on [getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating, before continuing with this article.

## About the initial data sync

When you first integrate with Shopify, Klaviyo will sync the last 90 days of your Shopify data so you can start engaging your most recent customers. After the sync of the last 90 days of data, Klaviyo will begin your complete historical data sync. Depending on how many orders, customers, and products your store has, it can take anywhere from a few minutes to several days to sync all of your data, and a green progress bar will show the progress of your sync.

Once this historical sync is complete, new data will sync to Klaviyo in real time.

## How to view your data

Click the ****Analytics**** dropdown in the left-hand navigation sidebar and select ****Metrics****. Here, you can view all of the metrics in your account. The metrics with a Shopify icon represent all of the metrics synced from your Shopify integration. You can filter this view to see only Shopify metrics by using the filter selector in the upper right-hand corner. The metrics synced from Shopify are:

- Checkout Started
- Placed Order
- Ordered Product
- Fulfilled Order
- Fulfilled Partial Order
- Cancelled Order
- Refunded Order
- Confirmed Shipment
- Delivered Shipment
- Marked Out for Delivery
- Active on Site
- Viewed Product
- Viewed Collection
- Submitted Search
- Added to Cart

All of the events above are branded with the Shopify icon when they sync to Klaviyo, with the exception of **Active on Site** and **Viewed Product**, which have a gear icon. These events are tracked by Klaviyo via an installed snippet, while Shopify-branded events are natively tracked by Shopify.

**Confirmed Shipment**, **Delivered Shipment**, and **Confirmed Out for Delivery** events will only sync to Klaviyo if they are available in Shopify. Please note that Shopify only provides these notifications for [certain shipping carriers](https://help.shopify.com/en/manual/shipping/understanding-shipping/shipping-carriers).

## Checkout Started

Klaviyo's Shopify integration is fully compatible with Shopify One-page Checkout. Whether you're using one-page checkout or multi-page checkout, the **Checkout Started** event is triggered after the customer fills out their email. If you've customized your checkout, customers may still need to progress to the next step in the checkout process for the **Checkout Started** event to be triggered. Additional customer information will be updated in Klaviyo once the customer is created in Shopify.

The event that Klaviyo tracks includes all of the product information about the items in someone's cart including product names, images, and variant information so you can use this information in your abandoned cart emails.

This event syncs with a checkout URL property, which links back to each customer’s unique cart. If someone opens an abandoned cart email from a new device, this link will rebuild the person's cart when clicked through. You can filter and target **Checkout Started** events based on the following criteria:

- ****$value****
  The total value of the cart at time of started checkout. This may include any line prices, taxes, shipping costs, tips, and discounts.
- ****Items****
  The names of the products in someone's order, e.g., **t-shirt** or **pants**.
- ****Collections****
  The complete set of the collections of the products in someone's order, e.g., **t-shirts, men's, pants** and **sale**.
- ****Item Count****
  The count of line items in the order, e.g., **2.** Note that this does not account for the quantity of items. Additionally, it is possible to add the same item to a cart multiple times and have it counted as multiple line items in Shopify; Klaviyo does not check for uniqueness or merge these for Item Count.
- ****Discount Codes****
  Any discount or coupon codes someone used towards the order, e.g., **SPRING2015**.
- ****Total Discounts****
  The total amount of any coupons or discounts if someone used code, e.g., **10.00**.
- ****Customer Locale****
  The customer’s locale when placing the order, e.g., **en-US**.
- ****$extra****
  Additional data including localized product information.

If there is billing address information available, we will also capture all relevant address details. If there is a referring site captured by Shopify, we will sync this as well.

### Checkout Started vs Abandoned Checkout

Shopify's**Abandoned Checkout**metric is different from its **Checkout Started**metric. Klaviyo's Abandoned Cart flow is triggered by the**Checkout Started**metric, while Shopify's Abandoned Cart flow is triggered by the**Abandoned Cart**metric.

### Do I need to disable the Abandoned Checkout notification in Shopify or will Klaviyo do this automatically?

You will need to do this manually. To turn off Shopify’s Abandoned Cart Recovery head over to ****Settings > Checkout**** and then scroll down until you see ****Abandoned checkouts****, under the **Email Marketing** section. You will need to uncheck the box that says "Automatically send abandoned checkout emails."

## Placed Order

This event is tracked when a customer completes the checkout process and creates an order in your Shopify store. The event Klaviyo tracks includes all of the product information about the items someone purchased including product names, images and variant information so you can use that information in purchase follow up emails. You can filter and target **Placed Order** events based on the following criteria:

- ****$value****
  The total value of the placed order, inclusive of shipping and any applied discounts.
- ****Items****
  The names of the products in someone's order, e.g., **t-shirt** or **pants**.
- ****Collections****
  The complete set of the collections of the products in someone's order, e.g., **t-shirts, mens, pants,** and **sale.**
- ****Item Count****
  The count of line items in the order, e.g., **2.** Note that this does not account for the quantity of items. Additionally, it is possible to add the same item to a cart multiple times and have it counted as multiple line items in Shopify; Klaviyo does not check for uniqueness or merge these for Item Count.
- ****Discount Codes****
  Any discount or coupon codes someone used towards the order, e.g., **SPRING2015;** while this isn't synced as a specific metric, there will be a **Discount Codes** property for each order that will allow you to see who purchased using particular codes.
- ****Total Discounts****
  The total amount of any coupons or discounts if someone used a code, e.g., **10.00.**
- ****Customer Locale****
  The customer’s locale when placing the order, e.g., **en-US**.
- ****$extra****
  Additional data including localized product information.
- ****Source Name****
  POS, Mobile etc.
- ****OptedInToSmsOrderUpdates****
  This value (True or False) indicates that the shopper has provided their phone number with their shipping information during checkout.

### Triggering off of Placed Order events

**Placed Order** and **Ordered Product** events are synced to Klaviyo seconds apart. For this reason, it is important to be consistent with the metric you use to trigger and filter your flows and segments. For example, if your flow is triggered by the **Placed Order** event and you add a filter to exclude anyone who **Ordered Product** since starting the flow, all recipients will be skipped because the two events are separate, but sync seconds apart. As a best practice, use the **Placed Order** event to trigger and filter flows and segments.

## Ordered Product

This event is also tracked when a customer places an order, but a separate event is tracked for each item someone purchases. For example, if someone buys a t-shirt and a pair of pants, one **Placed Order** event will be tracked along with two **Ordered Product** events; one **Placed Order** event for the purchase as a whole, and then one **Ordered Product** event for the t-shirt and one **Ordered Product** event for the pants.

The events Klaviyo tracks includes detailed information about each product someone purchases. This is useful when creating behavioral segments based on product variant options and other detailed information that's not available in the **Placed Order** event. You can filter and target **Ordered Product** events based on the following criteria:

- ****$value****
  The total value of the item purchased; no shipping costs or discounts included.
- ****Name****
  The name or title of the ordered product in Shopify, e.g., **t-shirt**.
- ****Variant Name****
  The name or title of the product variant in Shopify, e.g., **red, size medium t-shirt**.
- ****SKU****
  The SKU of the product variant, e.g., **REDMEDIUMTSHIRT**.
- ****ProductID****
  The ID associated with the product in your store.
- ****Quantity****
  The quantity will always be 1, since we track an **Ordered Product** event for each individual item in the order, including multiples of the same item.
- ****Collections****
  The complete set of collections or categories applied to the product, e.g., **t-shirts, men's** and **sale**.
- ****Tags****
  Any tags applied to the product in your store.
- ****Variant Option: <OptionName>****
  The name and value of any variant options for the variant ordered, e.g., **Variant Option: Size** would be **Medium** and **Variant Option: Color** would be **Red**.
- ****Attribute: <AttributeName>****
  The name and value of any product attributes for the product ordered, e.g., **Attribute: Season** would be **Spring**.
- ****Variant ID: <Variant ID>****
  The ID associated with the product variant on your store.
- ****Customer Locale****
  The customer’s locale when placing the order, e.g., **en-US**.
- ****$extra****
  Additional data including localized product information.

## Fulfilled Order

This event is tracked when an order is marked as "fulfilled" in your Shopify store. Klaviyo will track a **Fulfilled Order** event specifically when we sync an order with a `Fulfillment Status` of "fulfilled."

The event Klaviyo tracks includes all product information regarding the items someone purchased including product names and images so you can use that information in purchase follow up emails. You can filter and target **Fulfilled Order** events based on the following criteria:

- ****$value****
  The total value of the fulfilled order.
- ****Items****
  The names of the products in someone's order, e.g., **t-shirt** or **pants**.
- ****Collections****
  The complete set of the collections of the products in someone's order, e.g., **t-shirts, men's, pants,** and **sale**.
- ****Item Count****
  The count of line items in the order, e.g., **2.** Note that this does not account for the quantity of items. Additionally, it is possible to add the same item to a cart multiple times and have it counted as multiple line items in Shopify; Klaviyo does not check for uniqueness or merge these for Item Count.
- ****Discount Codes****
  Any discount or coupon codes someone used towards the order, e.g., **SPRING2015**.
- ****Total Discounts****
  The total amount of any coupons or discounts if someone used a code, e.g., **10.00**.
- ****Customer Locale****
  The customer’s locale when placing the order, e.g., **en-US**.
- ****$extra****
  Additional data including localized product information.
- ****OptedInToSmsOrderUpdates****
  This value (True or False) indicates that the shopper has provided their phone number with their shipping information during checkout.

## Fulfilled Partial Order

This event is tracked when an order that has been placed is partially fulfilled. For example, if you opt to ship order items in multiple shipments and want to send transactional emails for each stage in the fulfillment of an order, **Fulfilled Partial Order** events can be leveraged such that customers are notified when their items will be delivered. View our guide for more information on [setting up flows based on](https://help.klaviyo.com/hc/en-us/articles/4401771131419) [**Fulfilled Partial Order**](https://help.klaviyo.com/hc/en-us/articles/4401771131419) [events](https://help.klaviyo.com/hc/en-us/articles/4401771131419).

## Cancelled Order

This event is tracked when a customer creates an order in your Shopify store but then cancels the order before fulfillment. The event Klaviyo tracks includes all of the product information about the items someone purchased including product names and images. You can filter and target **Cancelled Order** events based on the following criteria:

- ****$value****
  The total value of the canceled order.
- ****Items****
  The names of the products in someone's order, e.g., **t-shirt** or **pants**.
- ****Collections****
  The complete set of the collections of the products in someone's order, e.g., **t-shirts, men's, pants** and **sale**.
- ****Item Count****
  The count of line items in the order, e.g., **2.** Note that this does not account for the quantity of items. Additionally, it is possible to add the same item to a cart multiple times and have it counted as multiple line items in Shopify; Klaviyo does not check for uniqueness or merge these for Item Count.
- ****Discount Codes****
  Any discount or coupon codes someone used towards the order, e.g., **SPRING2015**.
- ****Total Discounts****
  The total amount of any coupons or discounts if someone used a code, e.g., **10.00**.
- ****Customer Locale****
  The customer’s locale when placing the order, e.g., **en-US**.
- ****$extra****
  Additional data including localized product information.
- ****OptedInToSmsOrderUpdates****
  This value (True or False) indicates that the shopper has provided their phone number with their shipping information during checkout.

## Refunded Order

This event is tracked when a customer completes the checkout process in your Shopify store and a payment is made, but the customer requests the payment to be returned. Klaviyo only receives events from fully refunded orders (not partially refunded orders). The event Klaviyo tracks includes all of the product information about the items someone purchased including product names, images, and variant information. You can filter and target **Refunded Order** events based on the following criteria:

- ****$value****
  The total value of the refunded order.
- ****Items****
  The names of the products in someone's order, e.g., **t-shirt** or **pants**.
- ****Collections****
  The complete set of the collections of the products in someone's order, e.g., **t-shirts, men's, pants** and **sale**.
- ****Item Count****
  The count of line items in the order, e.g., **2.** Note that this does not account for the quantity of items. Additionally, it is possible to add the same item to a cart multiple times and have it counted as multiple line items in Shopify; Klaviyo does not check for uniqueness or merge these for Item Count.
- ****Discount Codes****
  Any discount or coupon codes someone used towards the order, e.g., **SPRING2015**.
- ****Total Discounts****
  The total amount of any coupons or discounts if someone used a code, e.g., **10.00**.
- ****Customer Locale****
  The customer’s locale when placing the order, e.g., **en-US**.
- ****$extra****
  Additional data including localized product information.
- ****OptedInToSmsOrderUpdates****
  This value (True or False) indicates that the shopper has provided their phone number with their shipping information during checkout.

## Confirmed Shipment

This event is tracked when the carrier is made aware of the shipment but hasn't received it yet. You can filter and target **Confirmed Shipment** events based on the following criteria:

- ****$value****
  The sum of product prices, including discounts, for item(s) in the shipment.
- ****Collections****
  The product collections for product(s) in the shipment.
- ****Customer Locale****
  The customer’s locale when placing the order, e.g., **en-US**.
- ****Estimated Delivery****
  The estimated delivery date for the shipment.
- ****Fulfillment Service****
  The fulfillment service associated with the shipment, e.g., **manual**.
- ****Items****
  An array of the product(s) in the shipment.
- ****Item Count****
  The total number of items in the shipment.
- ****Shipment Status****
  The status of the shipment, e.g., **confirmed**.
- ****Source Name****
  The source of the order, e.g., **web**.
- ****Tracking Company****
  The name of the tracking company.
- ****Tracking Numbers****
  The tracking number(s) of the shipment.
- ****OptedInToSmsOrderUpdates****
  This value (True or False) indicates that the shopper has provided their phone number with their shipping information during checkout.

## Delivered Shipment

This event is tracked when a fulfillment’s shipping status is marked as **delivered** on your Shopify store. You can filter and target **Delivered Shipment** events based on the following criteria:

- ****$value****
  The sum of product prices, including discounts, for item(s) in the shipment.
- ****Collections****
  The product collections for product(s) in the shipment.
- ****Customer Locale****
  The customer’s locale when placing the order, e.g., **en-US**.
- ****Delivery Hours****
  The number of hours the shipment took to be delivered after it was created.
- ****Estimated Delivery****
  The estimated delivery date for the shipment.
- ****Fulfillment Service****
  The fulfillment service associated with the shipment, e.g., **manual**.
- ****Items****
  An array of the product(s) in the shipment.
- ****Item Count****
  The total number of items in the shipment.
- ****Transit Hours****
  The number of hours the shipment has been in transit.
- ****Shipment Status****
  The status of the shipment, which is **delivered**.
- ****Source Name****
  The source of the order, e.g., **web**.
- ****Tracking Company****
  The name of the tracking company.
- ****Tracking Numbers****
  The tracking number(s) of the shipment.
- ****OptedInToSmsOrderUpdates****
  This value (True or False) indicates that the shopper has provided their phone number with their shipping information during checkout.

## Marked Out for Delivery

This event is tracked when a fulfillment’s shipping status is marked as **out\_for\_delivery** on your Shopify store. You can filter and target **Marked Out for Delivery** events based on the following criteria:

- ****$value****
  The sum of product prices, including discounts, for item(s) in the shipment.
- ****Collections****
  The product collections for product(s) in the shipment.
- ****Customer Locale****
  The customer’s locale when placing the order, e.g., **en-US**.
- ****Estimated Delivery****
  The estimated delivery date for the shipment.
- ****Fulfillment Service****
  The fulfillment service associated with the shipment, e.g., **manual**.
- ****Items****
  An array of the product(s) in the shipment.
- ****Item Count****
  The total number of items in the shipment.
- ****Transit Hours****
  The number of hours the shipment has been in transit.
- ****Shipment Status****
  The status of the shipment, which is **out\_for\_delivery**.
- ****Source Name****
  The source of the order, e.g., **web**.
- ****Tracking Company****
  The name of the tracking company.
- ****Tracking Numbers****
  The tracking number(s) of the shipment.
- ****OptedInToSmsOrderUpdates****
  This value (True or False) indicates that the shopper has provided their phone number with their shipping information during checkout.

## Active on Site

This event tracks when an identified user is active on your site. The top-level properties are:

- ****Browser****
  User agent for the originating browser (e.g., “Chrome”).
- ****Os****
  User agent for the originating operating system (e.g., “Mac”).
- ****Page****
  The URL of the visited page.
- ****utm\_medium****
  The marketing channel the user comes from to the website.
- ****utm\_source****
  The source of traffic to the website.
- ****utm\_campaign****
  The name of the marketing campaign associated with the traffic.
- ****utm\_id****
  The unique identifier for the marketing campaign associated with the traffic.
- ****utm\_term****
  This is an optional UTM parameter that marketers can set to track paid search terms.
- ****Fragments****
  Any other items in the URL, like an anchor tag that indicates where the user would have landed on the page. If there are no fragments on the URL, no values are set.
- ****Identity\_source****
  The event that triggered Klaviyo to receive the on-site event.
- ****Parameters****
  Each of the first 10 parameters present in the URL as their own piece of event data, except for **\_kx** and UTMs. If there are no parameters on the URL, no values are set. Parameters beyond the first 10 are not captured.
- ****First\_page\_path****
  The path of the first page a customer lands on. If there is no path on the first page view, no value is set.
- ****Kx\_present****
  If \_kx is present on the URL, **true** is returned for the dimension. If not, **false** is returned. This highlights whether or not the session could be associated with a click on a link in a Klaviyo message.

For each of the [UTM parameters](https://help.klaviyo.com/hc/en-us/articles/115005247808), Klaviyo will return the first value in the URL’s query parameters. If the UTM parameter is not present on a URL, then no values are provided in the event.

## Viewed Product

This event tracks when an identified user views a product on your site. The top-level properties are:

- ****URL****
  URL of the product.
- ****Activity ID****
  Activity ID for the event.
- ****Product****
  Name of the product.
- ****ProductID****
  ID of the product.
- ****ImageURL****
  URL for the product image.
- ****Brand****
  Product’s vendor name.
- ****Categories****
  The categories that the product belongs to.
- ****Price****
  Product variant’s price.
- ****CompareAtPrice****
  Price before discounts.

## Viewed Collection

This event tracks when an identified user views a collection your site. The top-level properties are:

- ****URL****
  Collection URL.
- ****Activity ID****
  Activity ID for the event.
- ****CollectionName****
  Name of the collection.
- ****CollectionID****
  ID for the collection.
- ****\_ip\_country\_code****
  ISO 3166-1 alpha-2 (two-letter) country code (e.g., “US”).
- ****\_ip\_region\_code****
  ISO 3166-2 region code (e.g. province, state such as “MA”).

## Submitted Search

This event tracks when an identified user submits a search on your site. The top-level properties are:

- ****URL****
  URL for the search query.
- ****Activity ID****
  Activity ID for the event.
- ****SearchQuery****
  Contents of search query (e.g., “Mens Large Tshirts”).
- ****SearchQueryParts****
  List including contents of search query (e.g., "Mens \"Large\" Tshirts”).
- ****\_ip\_country\_code****
  ISO 3166-1 alpha-2 (two-letter) country code (e.g., “US”).
- ****\_ip\_region\_code****
  ISO 3166-2 region code (e.g. province, state such as “MA”).

## Added to Cart

This event tracks when an identified user adds an item to their cart. This event tracks 1 product at a time within its top-level properties. The top-level properties are:

- ****URL****
  URL of the item added to the Cart.
- ****Browser****
  User agent for originating browser (e.g., “Chrome”).
- ****OS****
  User agent for the originating operating system (e.g., “Mac”).
- ****$value****
  Total value of product variant added to the cart.
- ****Product Name****
  Name of the product.
- ****ProductID****
  ID of the product.
- ****VariantID****
  ID for the product variant.
- ****Variant Name****
  Name of the product variant.
- ****Categories****
  Categories applied to the product.
- ****ImageURL****
  URL for the product image, or the product variant image if available.
- ****Brand****
  Product’s vendor name.
- ****Price****
  Product variant’s price.
- ****CompareAtPrice****
  Price before discounts.
- ****$currency****
  Currency code for the price.
- ****Product Type****
  Product type specified by the merchant.
- ****Variant SKU****
  SKU associated with the variant.
- ****Quantity****
  Quantity for the product.
- ****\_ip\_country\_code****
  ISO 3166-1 alpha-2 (two-letter) country code (e.g., “US”).
- ****\_ip\_region\_code****
  ISO 3166-2 region code (e.g. province, state such as “MA”).

## Synced customer data

In addition to the metrics Klaviyo syncs from Shopify, Klaviyo will also create a unique profile for every customer that we sync. When we sync contact information, there are also certain custom properties that may get added to each Klaviyo profile. You can use these properties in segments and in flows. Here are the properties that are automatically synced from Shopify:

- ****Email, First and Last Name, City, State/Region, Zip Code, Country, Phone Number****
  These built-in Klaviyo fields are automatically populated with all available data from Shopify.
- ****Locale information****
  The **Locale** property includes the profile’s locale synced from Shopify (e.g., “en-US”). The **Locale: Language** and **Locale: Country** properties are derived from **Locale** and contain the language and country information, respectively.
- ****Marketing consent****
  Whether or not a customer has opted-in to receive email and/or SMS marketing.
- ****Shopify Tags****
  Any custom tags assigned to that customer in Shopify, e.g., **Wholesale** or **VIP**.

Please note that profiles deleted in Shopify are not correspondingly deleted in Klaviyo.

## Frequency of the Shopify sync

Metrics and profile properties from Shopify are synced in real-time. You should see event data appear in your Klaviyo account within a few seconds of when the event is tracked in your Shopify store.

Because we sync all metrics in real-time, any tags - such as Order Tags - that might be added to an order after it is processed will not sync into Klaviyo. Klaviyo does not re-sync metrics after the initial event takes place, so no tags or adjustments made to an order after-the-fact will be updated in Klaviyo.

## How we calculate revenue

**Revenue**, or **Placed Order value**, is calculated as follows: (sub-total + shipping) - any discounts.

You may see that the **Revenue** value on your Klaviyo dashboard does not always match up with the revenue value you see in Shopify; this is because Shopify subtracts canceled and refunded orders from their revenue calculation, while Klaviyo does not.

Note that if you're looking to create a condition (like in a segment or flow) based on revenue for a customer over a certain period, you should use the **Revenue** metric and not the **Placed Order** metric.

![Segment definition in Klaviyo for what someone has done (or not done) has revenue is greater than 50 over all time](https://klaviyo.zendesk.com/hc/article_attachments/28704476411675)

## Segmenting based on value

If you want to segment customers based on the value of products they've ordered, checkouts they've started, etc., there's a specific way to do this in Klaviyo. In our segment builder, select **What someone has done (or not done) > Person has > [Event] Value**, then set your desired value and conditions. In the example below, we use **Ordered Product Value**.

![](https://klaviyo.zendesk.com/hc/article_attachments/31625849320219)

Note that you should not use the $value event property to segment customers in this way.
