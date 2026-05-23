---
id: 23113172847259
title: "OpenTable data reference"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/23113172847259-OpenTable-data-reference"
section: "OpenTable"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: en
---

## You will learn

Learn what data syncs from OpenTable to Klaviyo and where to view it. This includes data related to reservation creation, confirmation, and cancellation.

If you have not already, read our guide on [getting started with OpenTable](https://help.klaviyo.com/hc/en-us/articles/23112971772699) for step-by-step instructions on integrating, before continuing with this article.

OpenTable allows for the import of guests into the restaurant's systems. These guest would not have any reservation dates until one was made to that profile.

Klaviyo syncs email addresses and email consent from OpenTable. While phone numbers are synced, SMS consent is not. This means that SMS cannot be sent to phone numbers synced from this integration.

## How to view your data

To view your OpenTable data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. The metrics labeled “OpenTable” represent all of the metrics synced from your OpenTable integration.
3. Filter this view to see OpenTable metrics by using the filter selector next to the search bar and select ****OpenTable****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28722599679515)

## Metrics

For each metric, a **$value** property will be added if you are also using a POS system, e.g., Square, Toast, Lightspeed, etc. and have that POS connected to OpenTable. If your POS is not connected to OpenTable, **$value** will not sync.

### Created Reservation

This event occurs when a guest starts the reservation process through OpenTable.

- ****Created Date****
  The timestamp of when the reservation was created in UTC format, i.e., **YYYY-MM-DDThh:mmTZD**.
- ****Scheduled Time****
  The timestamp of the scheduled reservation date in UTC format, i.e., **YYYY-MM-DDThh:mmTZD**.
- ****Table Number****
  The table number associated with the reservation, assigned by the restaurant in OpenTable.
- ****Party Size****
  The party size specified by the guest.
- ****Visit Tags****
  Any tags associated with the visit such as those related to specific types of service or seating, e.g., **birthday**, **anniversary**, **window** **seating**, etc.
- ****Reservation Origin****
  The source of the reservation, i.e., **Phone, Walk-in,** or **Web**.
- ****Guest Request****
  Any requests specified by the guest during the reservation process.
- ****Table Category****
  The table category associated with the reservation, assigned by the restaurant in OpenTable, i.e., **Bar, Hightop, Outdoor,** etc.
- ****Server****
  The name of the server associated with the reservation.
- ****Currency Code****
  The currency code associated with the reservation if the reservation required payment.
- ****Restaurant ID****
  The ID of the restaurant associated with the reservation.
- ****Restaurant Name****
  The name of the restaurant associated with the reservation.

### Confirmed Reservation

This event occurs when a guest confirms the reservation through OpenTable.

- ****Created Date****
  The timestamp of when the reservation was confirmed in UTC format, i.e., **YYYY-MM-DDThh:mmTZD**.
- ****Scheduled Time****
  The timestamp of the scheduled reservation date in UTC format, i.e., **YYYY-MM-DDThh:mmTZD**.
- ****Table Number****
  The table number associated with the reservation, assigned by the restaurant in OpenTable.
- ****Party Size****
  The party size specified by the guest.
- ****Visit Tags****
  Any tags associated with the visit such as those related to specific types of service or seating, e.g., **birthday**, **anniversary**, **window** **seating**, etc.
- ****Reservation Origin****
  The source of the reservation, i.e., **Phone, Walk-in,** or **Web**.
- ****Guest Request****
  Any requests specified by the guest during the reservation process.
- ****Table Category****
  The table category associated with the reservation, assigned by the restaurant in OpenTable, i.e., **Bar, Hightop, Outdoor,** etc.
- ****Server****
  The name of the server associated with the reservation.
- ****Currency Code****
  The currency code associated with the reservation if the reservation required payment.
- ****Restaurant ID****
  The ID of the restaurant associated with the reservation.
- ****Restaurant Name****
  The name of the restaurant associated with the reservation.

### Completed Reservation

This event occurs when a guest is checked into the restaurant after arriving for their reservation.

- ****Created Date****
  The timestamp of when the reservation was completed in UTC format, i.e., **YYYY-MM-DDThh:mmTZD**.
- ****Scheduled Time****
  The timestamp of the scheduled reservation date in UTC format, i.e., **YYYY-MM-DDThh:mmTZD**.
- ****Table Number****
  The table number associated with the reservation, assigned by the restaurant in OpenTable.
- ****Party Size****
  The party size specified by the guest.
- ****Visit Tags****
  Any tags associated with the visit such as those related to specific types of service or seating, e.g., **birthday**, **anniversary**, **window** **seating**, etc.
- ****Reservation Origin****
  The source of the reservation, i.e., **Phone, Walk-in,** or **Web**.
- ****Table Category****
  The table category associated with the reservation, assigned by the restaurant in OpenTable, e.g., **Bar, Hightop, Outdoor,** etc.
- ****Guest Request****
  Any requests specified by the guest during the reservation process.
- ****Server****
  The name of the server who checked the guest into the restaurant.
- ****Currency Code****
  The currency code associated with the reservation if the reservation required payment.
- ****Restaurant ID****
  The ID of the restaurant associated with the reservation.
- ****Restaurant Name****
  The name of the restaurant associated with the reservation.

### Cancelled Reservation

This event occurs when a guest cancels a reservation through OpenTable.

- ****Created Date****
  The timestamp of when the reservation was canceled in UTC format, i.e., **YYYY-MM-DDThh:mmTZD**.
- ****Scheduled Time****
  The timestamp of the scheduled reservation date in UTC format, i.e., **YYYY-MM-DDThh:mmTZD**.
- ****Table Number****
  The table number associated with the reservation, assigned by the restaurant in OpenTable.
- ****Party Size****
  The party size specified by the guest.
- ****Visit Tags****
  Any tags associated with the visit such as those related to specific types of service or seating, e.g., **birthday**, **anniversary**, **window** **seating**, etc.
- ****Reservation Origin****
  The source of the reservation, i.e., **Phone, Walk-in,** or **Web**.
- ****Table Category****
  The table category associated with the reservation, assigned by the restaurant in OpenTable, e.g., **Bar, Hightop, Outdoor,** etc.
- ****Guest Request****
  Any requests specified by the guest during the reservation process.
- ****Server****
  The name of the server who checked the guest into the restaurant.
- ****Currency Code****
  The currency code associated with the reservation if the reservation required payment.
- ****Restaurant ID****
  The ID of the restaurant associated with the reservation.
- ****Restaurant Name****
  The name of the restaurant associated with the reservation.

### No Showed Reservation

This event occurs when a guest is not checked in for their reservation at the restaurant after the specified reservation time.

- ****Created Date****
  The timestamp of when the no show event occurred in UTC format, i.e., **YYYY-MM-DDThh:mmTZD**.
- ****Scheduled Time****
  The timestamp of the scheduled reservation date in UTC format, i.e., **YYYY-MM-DDThh:mmTZD**.
- ****Table Number****
  The table number associated with the reservation, assigned by the restaurant in OpenTable.
- ****Party Size****
  The party size specified by the guest.
- ****Visit Tags****
  Any tags associated with the visit such as those related to specific types of service or seating, e.g., **birthday**, **anniversary**, **window** **seating**, etc.
- ****Reservation Origin****
  The source of the reservation, i.e., **Phone, Walk-in,** or **Web**.
- ****Table Category****
  The table category associated with the reservation, assigned by the restaurant in OpenTable, e.g., **Bar, Hightop, Outdoor,** etc.
- ****Guest Request****
  Any requests specified by the guest during the reservation process.
- ****Server****
  The name of the server who checked the guest into the restaurant.
- ****Currency Code****
  The currency code associated with the reservation if the reservation required payment.
- ****Restaurant ID****
  The ID of the restaurant associated with the reservation.
- ****Restaurant Name****
  The name of the restaurant associated with the reservation.

## Synced guest data

In addition to the metrics Klaviyo syncs from OpenTable, Klaviyo will also create a unique profile for every guest that we sync. When we sync contact information, there are also certain custom properties that may get added to each Klaviyo Profile. You can use these properties in segments and in flows. Here are the properties that are automatically synced from OpenTable:

- Email
- Phone Number
- First Name
- Last Name
- Birthday
  - Note: If OpenTable does not include the year associated with a guest's birthday, the birthday year will default to 1904.
- OpenTable Birthday Month
- OpenTable Birthday Day
- OpenTable Guest IDs
- OpenTable Restaurants Visited

Klaviyo syncs email consent from OpenTable. Please note that only subscribes are synced from OpenTable, and unsubscribes are not.

While phone numbers are synced, SMS consent is not. This means that SMS cannot be sent to phone numbers synced from this integration.