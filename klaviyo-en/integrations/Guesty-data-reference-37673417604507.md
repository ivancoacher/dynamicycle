---
id: "37673417604507"
title: "Guesty data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/37673417604507-Guesty-data-reference"
section: "Guesty"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:55Z"
language: "en"
---
Learn what data syncs from Guesty to Klaviyo and where to view it. This includes reservation, guest, and message information. If you have not already, read our guide on [getting started with Guesty](https://help.klaviyo.com/hc/en-us/articles/37673288455323) for step-by-step instructions on integrating, before continuing with this article.

## Sync frequency

When you integrate with Guesty, Klaviyo will sync all historic reservation and guest data. Going forward, reservation, message, and guest data sync in real time.

## How to view your Guesty data

To view your Guesty data:

1. Navigate to ****Analytics > Metrics****.
2. Here, you can view all of the metrics in your account. The metrics with a Guesty icon represent all of the metrics synced from your Guesty integration.
3. Use the **All integrations** dropdown and select **Guesty** to view only Guesty metrics.

![](https://klaviyo.zendesk.com/hc/article_attachments/38042545410971)

## Reservation metrics

The following reservation metrics are synced from Guesty:

- ****Confirmed Reservation****
  When a guest’s reservation is confirmed in Guesty.
- ****Cancelled Reservation****
  When a staff member or guest cancels a confirmed reservation.
- ****Closed Reservation****
  When a staff member manually changes the status of **Inquiry** or **Reserved** to **Closed** to decline a reservation.
- ****Declined Reservation****
  When a guest declines a reservation in **Reserved** status.
- ****Expired Reservation****When the time to approve a **Reserved** reservation is over.
- ****Reserved Reservation****When a guest requests to book a property. To make the reservation **Confirmed**, a staff member has to confirm it.
- ****Inquired About Reservation****When a guest asks a general question but hasn’t submitted a formal booking request.
- ****Awaiting Payment****When a staff member has already confirmed a reservation but the guest's payment hasn't been processed yet

  For each of these metrics, the following top-level properties are synced to Klaviyo:
- ****Returning Guest****
  Whether the guest has ever made a reservation in the past (true/false).
- ****Guests Count****The total number of guests on a reservation.
- ****Number of Adults****The total number of adults on a reservation.
- ****Number of Children****The total number of children on a reservation.
- ****Number of Infants****The total number of infants on a reservation.
- ****Reservation ID****The reservation ID from Guesty.
- ****Inquiry ID****The Inquiry ID from Guesty for the **Inquired for Reservation** event.
- ****Confirmation Code****A unique ID for a guest’s reference as confirmation the reservation is booked.
- ****Reservation Status****The status of the reservation.
- ****Check-in Date****The reservation check in date in UTC format (i.e., YYYY-MM-DD).
- ****Check-in Date and Time****The reservation check-in date and time in UTC format (i.e., YYYY-MM-DDThh:mmTZD).
- ****Check-out Date****The reservation check-out date in UTC format (i.e., YYYY-MM-DD).
- ****Check-out Date and Time****The reservation check-out date and time in UTC format (i.e., YYYY-MM-DDThh:mmTZD).
- ****Nights Count****The total number of nights for a reservation.
- ****Booking Source****Where the reservation originated from (e.g. Airbnb, VRBO, manual, etc.)
- ****Accommodation Fare****The basic price of a reservation, calculated from the listing's base price. Equal to the sum of the nightly rates for the reservation dates.
- ****Accommodation Fare Discount****The discount amount (if any) applied to the **Accommodation Fare**.
- ****Currency****The type of currency used for the reservation.
- ****Cleaning Fee****The total amount charged for cleaning.
- ****Total Fees****The total amount of fees.
- ****Total Taxes****The total amount of taxes.
- ****Host Payout****The gross amount that the host is paid out on a reservation.
- ****SubTotal Price****The subtotal price.
- ****Balance Due****The amount due by the guest.
- ****Payments Due****The amount of payments due by the guest.
- ****Is Fully Paid****If the reservation is fully paid for or not.
- ****Total Paid****The total amount already paid by the guest.
- ****Total Refunded****The total amount refunded to the guest.
- ****Listing ID****The ID of the property on the reservation.
- ****Listing Address****The address of the property on the reservation.
- ****Listing Thumbnail****The thumbnail image URL of the property on the reservation.
- ****Listing Public Description Summary****The public description of the property on the reservation.
- ****Listing Amenities****The amenities available on the property on the reservation.
- ****Listing Nickname****The internal nickname of the property on the reservation.
- ****Listing Title****The public listing title of the property on the reservation.
- ****Listing Default Check-in Time****
  The default check-in time for the listing.
- ****Listing Default Check-out Time****
  The default check-out time for the listing.
- ****Listing Timezone****
  The listing's timezone.
- ****Account ID****The guests’ Guesty Account ID.

## Message metrics

Klaviyo syncs two metrics that reflect messages in Guesty:

- ****Message Sent****
  Message sent to a guest.
- ****Message Received****Message received from a guest.

### Message Sent

Each **Message Sent** metric synced to Klaviyo has the following properties:

- Reservation ID
- Confirmation Code
- Check-in Date
- Check-out Date
- Guest Name
- Guest ID
- Message Last Updated by Guest
- Message Platform
- Message Priority Rating
- Created At
- Last Modified

### Message Received

Each **Message Received** metric synced to Klaviyo has the following properties:

- Reservation ID
- Confirmation Code
- Check-in Date
- Check-out Date
- Guest Name
- Message Language
- Message Read
- Message Subject
- Message Priority Rating
- Message Snoozed Until
- Guest ID
- Message Conversation With

## Reservation objects

For each reservation object, the following top-level properties are synced to Klaviyo:

- ****Value****Value of the reservation, comes from `money.hostPayout`.
- ****GuestsCount****The total number of guests on a reservation.
- ****NumberOfAdults****The total number of adults on a reservation.
- ****NumberOfChildren****The total number of children on a reservation.
- ****NumberOfInfants****The total number of infants on a reservation.
- ****ReservationID****The reservation ID from Guesty. Used as the object ID.
- ****ConfirmationCode****A unique ID for a guest’s reference as confirmation the reservation is booked.
- ****ReservationStatus****The status of the reservation.
- ****CheckInDate****The reservation check-in date.
- ****CheckOutDate****The reservation check-out date.
- ****CheckInDateAndTime****The reservation check-in date and time in UTC format (i.e., YYYY-MM-DDThh:mmTZD).
- ****CheckOutDateAndTime****The reservation check-out date and time in UTC format (i.e., YYYY-MM-DDThh:mmTZD).
- ****NightsCount****The total number of nights for a reservation.
- ****BookingSource****Where the reservation originated from (e.g. Airbnb, VRBO, manual, etc.)
- ****Currency****The type of currency used for the reservation.
- ****CleaningFee****The total amount charged for cleaning.
- ****TotalFees****The total amount of fees.
- ****TotalTaxes****The total amount of taxes.
- ****HostPayout****The gross amount that the host is paid out on a reservation.
- ****SubTotalPrice****The subtotal price.
- ****BalanceDue****The amount due by the guest.
- ****PaymentsDue****The amount of payments due by the guest.
- ****IsFullyPaid****If the reservation is fully paid for or not.
- ****TotalPaid****The total amount already paid by the guest.
- ****TotalRefunded****The total amount refunded to the guest.
- ****ListingID****The ID of the property on the reservation.
- ****ListingAddress****The address of the property on the reservation.
- ****ListingThumbnail****The thumbnail image URL of the property on the reservation.
- ****ListingAmenities****The amenities available on the property on the reservation.
- ****ListingNickname****The internal nickname of the property on the reservation.
- ****ListingTitle****The public listing title of the property on the reservation.
- ****ListingRoomType****
  The listing's room type.
- ****ListingPropertyType****The listing's property type.

## Guest data

Klaviyo syncs guest data from Guesty. Please note that we do not sync any profiles associated with an online travel agency (OTA).

We sync the following guest data to Klaviyo profiles:

- Email
- Phone number
- First name
- Last name
- Street
- City
- State
- Country
- Guesty ID
- Guesty Tags
- Guesty Interests
- Guesty Allergies
- Guesty Dietary Preferences
- Guesty Communication Methods
- Guesty Notes
- Guesty Additional Notes
- Guesty Preferred Language
- Guesty Hometown
- Guesty Gender
- Guesty Marital Status
- Guesty Pronouns
- Guesty Number of Kids
- Guesty Nationality
- Guesty Returning Guest
- Guesty Birthday
- Email consent

Please note that SMS consent is not synced from Guesty.