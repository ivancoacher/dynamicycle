---
id: 15752146245403
title: "Olo data reference"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15752146245403-Olo-data-reference"
section: "Olo"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: en
---

## You will learn

Learn what data that is synced when you integrate Olo with your Klaviyo account.

## How to view your data

To view your Olo data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. The metrics with a Olo icon represent all of the metrics synced from your Olo integration.
3. Filter this view to see only Olo metrics by using the filter selector next to the search bar.
   ![List of Olo metrics found within Klaviyo.](https://klaviyo.zendesk.com/hc/article_attachments/28715972048155)

Third party deliveries (Uber Eats, DoorDash, etc.) sync from Olo to Klaviyo if they include a valid email address and/or phone number.

## Placed Order

This event is tracked when an order was placed (submitted) to Olo and includes all of the product information about the items purchased, store information and order details that can be used in follow up emails, SMS, and other messages.

You can filter and target **Placed Order** events based on the following criteria:

- ****Value****
  The total value of the order, inclusive of fees and any applied discounts.
- ****Brand Name****
  Configured name for the restaurant.
- ****Client Platform****
  The associated platform used to place the order; e.g., Web or MobileWeb.
- ****Fulfillment Method****
  The handoff mode for the order; e.g., pickup or delivery.
- ****Item Count****
  The total quantity of line items in the order.
- ****Item Names****
  The names of the products in the order.
- ****Items****
  The details of each item including name, quantity, description, price, image URL.
- ****Order ID****
  The unique ID for each placed order.
- ****Ordering Provider****
  The interface used to place the order; e.g., Olo or DoorDash.
- ****Store Number****
  Reference to the restaurant’s store.

## Closed Order

This event is tracked when an order has reached its estimated ready time and is considered complete in Olo.

You can filter and target **Closed Order** events based on the following criteria:

- ****Value****
  The total value of the order, inclusive of fees and any applied discounts.
- ****Brand Name****
  Configured name for the restaurant.
- ****Client Platform****
  The associated platform used to place the order; e.g., web or mobile.
- ****Fulfillment Method****
  The handoff mode for the order; e.g., pickup or delivery.
- ****Item Count****
  The total quantity of line items in the order.
- ****Item Names****
  The names of the products in the order.
- ****Items****
  The details of each item including name, quantity, description, price, image URL.
- ****Order ID****
  The unique ID for each placed order.
- ****Ordering Provider****
  The interface used to place the order; e.g., Olo or DoorDash.
- ****Store Number****
  Reference to the restaurant’s store.

## Ordered Product

This event is also tracked when an order is considered complete in Olo, but a separate event is tracked for each item purchased. The events Klaviyo tracks includes detailed information about each product someone purchases. This is useful when creating behavioral segments based on specific products.

You can filter and target **Ordered Product** events based on the following criteria:

- ****Value****
  The total value of the item purchased.
- ****Name****
  The name of the ordered product in Olo.
- ****Product ID****
  The ID associated with the product.
- ****Quantity****
  The total quantity ordered of the product
- ****Store Number****
  Reference to the restaurant’s store.

## Adjusted Order

This event is tracked when an order has been fully or partially adjusted or refunded.

You can filter and target **Adjusted Order** events based on the following criteria:

- ****Value****
  The total value of the order, inclusive of fees and any applied discounts.
- ****Adjustment Reason****
  The reason for the adjustment.
- ****Adjustment Type****
  The type of adjustment; e.g., a full or partial refund.
- ****Brand Name****
  Configured name for the restaurant.
- ****Client Platform****
  The associated platform used to place the order; e.g., web or mobile.
- ****Fulfillment Method****
  The handoff mode for the order, e.g., pickup or delivery.
- ****Item Count****
  The total quantity of line items in the order.
- ****Item Names****
  The names of the products in the order.
- ****Items****
  The details of each item including name, quantity, description, price, image URL.
- ****Order ID****
  The unique ID for each placed order.
- ****Ordering Provider****
  The interface used to place the order; e.g., Olo or DoorDash.
- ****Store Number****
  Reference to the restaurant’s store.

## Canceled Order

This event is tracked when an order was canceled by a user or the system.

You can filter and target **Canceled Order** events based on the following criteria:

- ****Value****
  The total value of the order, inclusive of fees and any applied discounts.
- ****Brand Name****
  Configured name for the restaurant.
- ****Canceled Reason****
  The reason for the cancellation.
- ****Client Platform****
  The associated platform used to place the order; e.g., web or mobile.
- ****Fulfillment Method****
  The handoff mode for the order; e.g., pickup or delivery.
- ****Item Count****
  The total quantity of line items in the order.
- ****Item Names****
  The names of the products in the order.
- ****Items****
  The details of each item including name, quantity, description, price, image URL.
- ********Order ID********The unique ID for each placed order.
- ********Ordering Provider********The interface used to place the order e.g., Olo or DoorDash.
- ********Store Number********Reference to the restaurant’s store.

## Track sign-ups

This event is tracked when a user has created an account in Olo (not applicable to guests).

If the user chooses to allow email, the user will also be subscribed to the configured email list with a **Subscribed to List** event in Klaviyo.

## Synced guest data

In addition to the metrics Klaviyo syncs from Olo, Klaviyo also creates a unique profile for every customer that syncs with a valid email address and/or phone number. When Klaviyo syncs contact information, there are also certain custom properties that may get added to each Klaviyo profile. You can use these properties in segments and in flows.

Here are the properties that are automatically synced from Olo:

- ****Email, first and last Name, phone number****
  These built-in Klaviyo fields are automatically populated with all available data from Olo.
- ****Olo customer****
  Indicates that a profile is present within Olo.
- ****Email consent****
  Consent for email marketing.
- ****SMS consent****
  Consent for SMS marketing.

## Additional resources

[Getting started with Olo](https://klaviyo.zendesk.com/hc/en-us/articles/15751697785883)

[How to create a post-purchase flow](https://help.klaviyo.com/hc/en-us/articles/360028872611)