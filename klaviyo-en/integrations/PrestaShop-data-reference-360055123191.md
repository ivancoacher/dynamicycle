---
id: "360055123191"
title: "PrestaShop data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360055123191-PrestaShop-data-reference"
section: "PrestaShop"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-15T09:56:47Z"
language: "en"
---
## You will learn

Learn about the metrics and customer data synced from PrestaShop to Klaviyo. 3 types of events sync from PrestaShop to Klaviyo:

- Order events sync every 30 minutes (e.g., **Placed Order**).
- Transactional order events sync in real time, if you choose to enable them in your module settings (e.g., **Placed Order Transactional**).
- Klaviyo onsite events (**Active on Site**, **Viewed Produc**t, and **Added to Cart**).

![](https://klaviyo.zendesk.com/hc/article_attachments/35198021096347)

![List of PrestaShop API metrics in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28717851526427)

## Transactional versus non-transactional metrics

If you toggled on ****Send real-time order events to Klaviyo****[when integrating](https://help.klaviyo.com/hc/en-us/articles/360054551492), a second set of order events labeled as transactional will sync to Klaviyo in real time. For instance, you’ll see a metric in Klaviyo labeled **Placed Order Transactional**, which will sync in real time, in addition to a metric labeled **Placed Order,** which will sync every 30 minutes. The real-time transactional events that sync to Klaviyo are:

- Placed Order Transactional
- Fulfilled Order Transactional
- Cancelled Order Transactional
- Refunded Order Transactional

![Transactional events toggle on in Klaviyo plugin settings in PrestaShop](https://klaviyo.zendesk.com/hc/article_attachments/28717851531163)

## PrestaShop metrics

You can view all PrestaShop metrics in Klaviyo by navigating to ****Analytics > Metrics****. Filter by **PrestaShop** to see order and transactional order events (they will have a PrestaShop icon) or filter by **API** to see Klaviyo onsite events (they will have a gear icon).

### Active on Site

This event is created when a customer is active on your PrestaShop store.

### Viewed Product

Klaviyo tracks this event when a customer views a product on your PrestaShop store. This is useful if you'd like to set up a [browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow) or provide customers with [personalized product recommendations](https://help.klaviyo.com/hc/en-us/articles/115005082787) based on product browsing data.

### Added to Cart

This event is created when a customer adds an item to their cart.

### Started Checkout

The **Started Checkout** metric is created when:

- A customer logs in to their account, adds something to their cart, and navigates to the checkout page.
- Without logging in, or using guest checkout, a customer adds something to their cart, navigates to the checkout page, and enters their email address.

  Klaviyo captures the value of a cart at the time of checkout, as well as other pertinent details of a customer's cart that you can leverage for personalized abandoned cart emails. You can filter and target each event based on the following criteria:
- ****Language****
  The language used.
- ****CartID****
  An ID assigned to the cart.
- ****Items****
  The names of the products in the cart, e.g., Red T-shirt or Blue Pants.
- ****ItemCount****
  The number of items in the cart.
- ****TotalDiscounts****
  The total amount of any coupons or discounts if someone used a code, e.g., 10.00.
- ****Categories****
  The complete set of categories for the products in the cart, e.g., t-shirts, men's, pants and sale.
- ****Tags****
  The list of meta keywords for the products in the cart.
- ****ShopId****
  The ID of the shop associated with the order.
- ****ReclaimCartUrl****
  A URL that can be used to rebuild the customer’s cart, for instance in an abandoned cart email.
- ****$event\_id****
  The ID of this Started Checkout event.
- ****$value****
  The value of the cart.
- ****$extra****
  An array of extra data.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.
- ****integration\_key****
  Your eCommerce platform (PrestaShop).

### Placed Order, Fulfilled Order, Cancelled Order, and Refunded Order

All of these events are created based on the order status mapping you configured when integrating. Each event includes product information about the items purchased, including product names, categories, etc. You can filter and target each event based on the same criteria:

- ****$value****
  The total value of the order.
- ****$extra****
  An array of extra data.
- ****Categories****
  The complete set of categories the products in the order, e.g., t-shirts, men's, pants and sale.
- ****ItemCount****
  The number of items in the order, e.g., 2.
- ****Items****
  The names of the products in the order, e.g., Red T-shirt or Blue Pants.
- ****ShopID****
  The ID of the shop associated with the order.
- ****LanguageID****
  Shop language ID as a two-letter code e.g., EN.
- ****TotalDiscounts****
  The total amount of any coupons or discounts if someone used a code, e.g., 10.00.
- ****DiscountCodes****
  Any discount or coupon codes someone used towards the order, e.g., SPRING10.
- ****Tags****
  The list of meta keywords for products in the order.
- ****OrderStatus****
  The status of the order, as configured in order status mapping, e.g., **Payment Accepted**.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.

### Ordered Product

By default, this event is tracked once for every product a user orders when they place an order. For example, if a customer buys a t-shirt and a pair of jeans, one **Placed Order** event is tracked along with two **Ordered Product** events.

The event Klaviyo tracks includes detailed information about each product someone purchases. This is useful when creating behavioral segments based on product options and other detailed information that's not available in the **Placed Order** event. You can filter and target **Ordered Product** events based on the following criteria:

- ****Name****
  The name of the ordered product.
- ****SKU****
  The SKU of the ordered product.
- ****ProductId****
  The ID of the ordered product.
- ****Quantity****
  The quantity of the ordered product.
- ****Categories****
  The complete set of categories for the product, e.g., t-shirts, men's, and sale.
- ****Tags****
  The list of meta keywords for the product.
- ****$event\_id****
  An ID associated with this **Ordered Product** event.
- ****$value****
  The value of the ordered product.
- ****$extra****
  An array of extra data.
- ****external\_catalog\_id****
  Used in catalog organization in Klaviyo.

## Synced customer data

In addition to the metrics Klaviyo syncs from PrestaShop, Klaviyo will also create a unique profile for every customer that we sync. When we sync contact information, there are also certain custom properties that may get added to each Klaviyo profile. Here are the properties automatically synced from PrestaShop:

- ****Email, First and Last Name, City, State/Region, Zip Code, Country, Phone Number****
  These built-in Klaviyo fields are automatically populated with all available data from PrestaShop.
- ****$locale****
  The language and country tag of the store the customer interacted with (e.g., "en-us").
- ****$locale-language****
  The language tag derived from the **$locale** property (e.g., "en").
- ****$locale-country****
  The country tag derived from the **$locale** property (e.g., "us").
- ****Last Order Currency****
  The currency of the customer's last order.
- ****Birthday****
  The customer's birthday.
- ****Gender****
  The customer's gender.
- ****PrestaShop Account Created Date****
  The date on which the customer created their PrestaShop account.
- ****PrestaShop Default Group****
  The default PrestaShop group that the customer belongs to.
- ****PrestaShop Groups****
  All PrestaShop groups that the customer belongs to.
- ****PrestaShop Shops****
  The shop(s) with which a customer has interacted.