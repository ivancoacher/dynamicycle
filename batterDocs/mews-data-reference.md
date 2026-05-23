<h1>Mews data reference</h1>

Learn what data syncs from Mews to Klaviyo and where to view it. This data includes reservation, guest, and email subscriber information. If you have not already, read our guide on [getting started with Mews](https://help.klaviyo.com/hc/en-us/articles/38311148860955) for step-by-step instructions on integrating, before continuing with this article.

## Sync frequency

When you integrate with Mews, Klaviyo will sync historic guests and reservations from the last 2 years. Going forward, reservation, guest, and email subscriber data sync in real time.

## How to view your Mews data

To view your Mews data:

1. Navigate to ****Analytics > Metrics****.
2. Here, you can view all of the metrics in your account. The metrics with a Mews icon represent all of the metrics synced from your Mews integration.
3. Use the **All integrations** dropdown and select **Mews** to view only Mews metrics.

![mews.png](https://klaviyo.zendesk.com/hc/article_attachments/46891024971291)

## Room Night metrics

The following room night metrics, related to reservations, are synced from Mews:

- ****Confirmed Room Night****
  When a guest confirms a reservation in Mews, we create 1 ****Confirmed Room Night**** event per room night (e.g., a reservation with 2 rooms for 2 nights will have 4 events).
- ****Completed Room Night****
  When a guest checks out in Mews, we create 1 ****Completed Room Night**** event per room night (e.g., a reservation with 2 rooms for 2 nights will have 4 events).

  For each of these metrics, the following top-level properties are synced to Klaviyo:
- ****Value****
  The total value of the room (i.e. room revenue) for a given night.
- ****Id****
  The ID associated with the `OrderItem` in Mews.
- ****ReservationID****
  The ID associated with the Reservation in the PMS.
- ****StartDate****
  The date a night begins.
- ****EndDate****
  The date a night ends.
- ****DayOfWeek****
  The day of the week (e.g. Monday) when the night begins.
- ****AdultCounts****
  Number of adults in a room.
- ****ChildCounts****
  Number of children in a room.
- ****PersonCounts****
  Number of people in a room (i.e. sum of adults and children).
- ****BillingName****
  The billing name as it is stored in the PMS (e.g. “Night - 1/10/26”).
- ****ResourceName****
  The name of the room as stored in the PMS.
- ****PropertyID****
  ID corresponding to the hotel.
- ****PropertyName****
  Name corresponding to the hotel property.
- ****Origin****
  Shows where the reservation came from (e.g. direct, channel manager, etc.).
- ****TravelAgency****
  Shows the travel agency (often an OTA) that drove the reservation.
- ****Notes****
  Additional notes.

## Reservation metrics

The following reservation metrics are synced from Mews:

- ****Requested Reservation****
  When a guest requests a reservation but it has yet to be confirmed by your business.
- ****Inquired about Reservation****
  When a guest inquires about a reservation but it has yet to be confirmed.
- ****Confirmed Reservation****
  When a reservation is confirmed by both the customer and your business.
- ****Checked In to Reservation****
  When a guest checks in to a reservation.
- ****Checked Out of Reservation****
  When a guest checks out of a reservation.
- ****Cancelled Reservation****
  When a reservation is cancelled.

  For each of these metrics, the following top-level properties are synced to Klaviyo:
- Value
- Value Currency
- Reservation ID
- Reservation Number
- Service Name
- Account Type
- Service Sender Origin
- Commander Origin
- Used Voucher
- Check In Status
- Reservation Group Name
- Partner Company Name
- Voucher Names
- Cancellation Reason
- Release Date
- Scheduled Start Time
- Scheduled End Time
- Actual Start Time
- Actual End Time
- Reservation Purpose
- Reservation Person Counts
- Reservation Adult Counts
- Reservation Child Counts

## Reservation objects

For each Reservation object, the following top-level properties are synced to Klaviyo:

- Value
- ValueCurrency
- ReservationID (used as the ID of the object)
- ReservationNumber
- ResourceName
- ResourceDescription
- PropertyName
- ServiceName
- AccountType
- ServiceOrderOrigin
- CommanderOrigin
- UsedVoucher
- CheckInStatus
- ReservationGroupName
- PartnerCompanyName
- CancellationReason
- ReleaseDate
- ScheduledStartTime
- ScheduledEndTime
- ActualStartTime
- ActualEndTime
- ReservationPurpose
- ReservationPersonCounts
- ReservationAdultCounts
- ReservationChildCounts
- ReservationNights

## Guest data

Klaviyo syncs guest data from Mews. Please note that we do not sync any profiles associated with an online travel agency (OTA).

We sync the following guest data to Klaviyo profiles:

- Mews Customer ID
- Mews Title
- Mews Sex
- First Name
- Last Name
- Locale
- Mews Birthday
- Title
- Email
- Email consent
- Phone Number
- Mews Notes
- Mews Dietary Requirements
- Address1
- Address2
- City
- Country
- ZIP
- Mews Classifications
- Mews Company ID
- Mews Is Active
- Mews Preferred Space Features
- Organization

Please note that SMS consent is not synced from Mews.
