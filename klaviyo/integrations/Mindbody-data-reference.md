---
id: 15344283585819
title: "Mindbody data reference"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15344283585819-Mindbody-data-reference"
section: "Mindbody"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:43Z"
language: en
---

## You will learn

Learn what data syncs from Mindbody to Klaviyo and where to view it. This includes customer profiles and data related to appointments, classes, membership, and purchases.

If you have not already, read our guide on [getting started with Mindbody](https://help.klaviyo.com/hc/en-us/articles/15348624462747) for step-by-step instructions on integrating, before continuing with this article.

Email consent is synced from Mindbody to Klaviyo. Please note that we do not sync SMS consent from Mindbody.

## Historical sync

After the Mindbody integration is enabled, it runs a historical sync of customer data from the past 2 years. No event data is synced historically.

## How to view your data

To view your Mindbody data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. The metrics with a Mindbody icon represent all of the metrics synced from your Mindbody integration.
3. Filter this view to see only Mindbody metrics by using the filter selector next to the search bar.

![](https://klaviyo.zendesk.com/hc/article_attachments/37302863537435)

Please note that only the metrics you use in Mindbody will sync to Klaviyo, so you may not see all of the metrics listed above in your account.

## Appointment metrics

The following appointment metrics are tracked:

- ****Scheduled Appointment****
  When a customer schedules an appointment through Mindbody.
- ****Confirmed Appointment****
  When a staff member confirms an appointment with a customer through Mindbody.
- ****Arrived for Appointment****
  When a customer arrives for an appointment and a staff member checks them in.

  For each of these metrics, the following information is included:
- ****Location ID****
  The location ID of the appointment.
- ****Staff ID****
  The ID of the staff member or team associated with the appointment.
- ****Staff Name****
  The name of the staff member or team associated with the appointment.
- ****Start Time****
  The timestamp of when the appointment begins in UTC format; i.e., **YYYY-MM-DDThh:mmTZD.**
- ****End Time****
  The timestamp of when the appointment ends in UTC format; i.e. **YYYY-MM-DDThh:mmTZD.**
- ****Duration****
  The duration of the appointment in minutes.
- ****Resources****
  A list of any additional information associated with the appointment.
- ****Staff Provider ID****
  The ID of the staff provider.
- ****Name****
  The name of the staff provider.

## Class metrics

### Booked Class

This event is tracked when a customer books a class through Mindbody.

- ****Location ID****
  The location ID of the class.
- ****Staff ID****
  The ID of the staff member or team associated with the class.
- ****Staff Name****
  The name of the staff member or team associated with the class.
- ****Item ID****
  The ID of the class or class pass.
- ****Item Name****
  The name of the customer’s pass or membership, i.e., **Day Pass.**

### Signed In to Class

This event is tracked when a customer signs into a class through Mindbody.

- ****Staff ID****
  The ID of the staff member or team associated with the class.
- ****Item ID****
  The ID of the customer’s pass or membership.
- ****Item Name****
  The name of the customer’s pass or membership; i.e,. **Day Pass.**

### Cancelled Class

This event is tracked when a customer cancels a class through Mindbody.

- ****Staff ID****
  The ID of the staff member or team associated with the class.
- ****Item ID****
  The ID of the customer’s pass or membership.
- ****Item Name****
  The name of the customer’s pass or membership; i.e,. **Day Pass.**
- ****Cancel Type****
  The type or reason of the cancellation; e.g. **Late Cancelled.**

### Joined Waitlist

This event is tracked when a customer joins the waitlist for a class through Mindbody.

- ****Start Time****
  The timestamp of when the class begins in UTC format, i.e., YYYY-MM-DDThh:mmTZD.
- ****End Time****
  The timestamp of when the class ends in UTC format, i.e., YYYY-MM-DDThh:mmTZD.
- ****Class ID****
  The ID of the class associated with the waitlist.
- ****Waitlist Max Size****
  The maximum amount of people that can be added to the waitlist.

## Membership metrics

### Activated Membership

This event is tracked when a customer activates their membership through Mindbody.

- ****Membership ID****
  The ID associated with the membership plan, represented by a string of numbers.
- ****Membership Name****
  The name of the membership plan; e.g., **All Access Month-to-Month Membership.**

## Other metrics

### Placed Order

This event is tracked when a customer completes the checkout process and creates an order.

- ****Sold By****
  The name of the sales staff member who made the sale.
- ****Location****
  The ID of the location associated with the order.
- ****Items****
  The list of items associated with the order including the following fields:
  - ****itemId****
    The ID of the purchased item.
  - ****Type****
    The type of purchased item; i.e., product or service.
  - ****Name****
    The name of the purchased item.
  - ****amountPaid****
    The cost of the item inclusive of any applied discounts.
  - ****amountDiscounted****
    The amount discounted from the cost of the item.
- ****Quantity****
  The quantity of the purchased item.
- ****recipientClientId****
  The ID assigned to the customer.
- ****paymentReferenceId****
  The ID assigned to the payment event.
- ****giftCardBarcodeId****
  The ID of the gift card if one was used.
- ****$value****
  The total monetary value of the order inclusive of shipping and any applied discounts

### Ordered Product

This event is also tracked when a customer places an order, but a separate event is tracked for each item someone purchases.

- ****Item ID****
  The ID of the purchased item.
- ****Type****
  The type of purchased item; e.g., product or service**.**
- ****Name****
  The name of the purchased item****.****
- ****Price****
  The price of the purchased item.
- ****Discount****
  The amount of the total discounts applied to the purchase.
- ****Quantity****
  The quantity of the purchased item.

### Created Contract

This event is also tracked when a customer creates a contract through Mindbody.

- ****Sales Staff ID****
  The ID of the sales staff member associated with the contract.
- ****Sales Staff Name****
  The name of the sales staff member associated with the contract.
- ****Origination Location****
  The ID of the location where the contract was created, represented as a number.
- ****Contract ID****
  The ID of the contract, represented as a string of numbers.
- ****Contract Start****
  The timestamp of when the contract goes into effect in UTC format, i.e. **YYYY-MM-DDThh:mmTZD.**
- ****Contract End****
  The timestamp of when the contract ends in UTC format, i.e., **YYYY-MM-DDThh:mmTZD.**
- ****Auto Renewal****
  Whether or not the contract is set to automatically renew. (**true/false**).

## Synced client data

Klaviyo creates or updates profiles for every client with the following information:

- Email
- First name
- Last name
- Phone number
- Mindbody Account Balance
- Mindbody Active
- Mindbody ClientID
- Mindbody First Appointment Date
- Mindbody First Class Date
- Mindbody Home Location (Number)
- Mindbody Home Location Name
- Mindbody Liability Released
- Mindbody Number of Visits
- Mindbody Referral
- Mindbody Status
- Email consent is synced from Mindbody to Klaviyo. Please note that we do not sync SMS consent from Mindbody.