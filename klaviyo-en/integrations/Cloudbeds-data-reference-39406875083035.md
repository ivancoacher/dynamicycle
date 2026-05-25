---
id: "39406875083035"
title: "Cloudbeds data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/39406875083035-Cloudbeds-data-reference"
section: "Cloudbeds"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T12:54:33Z"
language: "en"
---
Learn what data syncs from Cloudbeds to Klaviyo and where to view it. This includes reservations, guest information, and email consent. If you have not already, read our guide on [getting started with Cloudbeds](https://help.klaviyo.com/hc/en-us/articles/39406849361691) for step-by-step instructions on integrating, before continuing with this article.

## Sync frequency

When you integrate with Cloudbeds, Klaviyo will sync all historic reservation and guest data. Going forward, reservation and guest data sync in real time.

## How to view your Cloudbeds data

To view your Cloudbeds data:

1. Navigate to ****Analytics > Metrics****.
2. Here, you can view all of the metrics in your account. The metrics with a Cloudbeds icon represent all of the metrics synced from your Cloudbeds integration.
3. Use the **All integrations** dropdown and select ****Cloudbeds**** to view only Cloudbeds metrics.

![Screenshot 2026-02-19 at 3.19.38 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46850854258331)

## Room Night metrics

The following room night metrics, related to reservations, are synced from Cloudbeds:

- ****Confirmed Room Night****
  When a guest confirms a reservation in Cloudbeds, we create 1 ****Confirmed Room Night**** event per room night (e.g., a reservation with 2 rooms for 2 nights will have 4 events).
- ****Completed Room Night****
  When a guest checks out in Cloudbeds, we create 1 ****Completed Room Night**** event per room night (e.g., a reservation with 2 rooms for 2 nights will have 4 events).

  For each of these metrics, the following top-level properties are synced to Klaviyo:
- ****Value****
  The total value of the room (i.e. room revenue) for a given night.
- ****Id****
  The Klaviyo-generated ID associated with the room night.
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
- ****RoomTypeName****
  The name of the room as stored in the PMS.
- ****PropertyID****
  ID corresponding to the hotel.
- ****PropertyName****
  Name corresponding to the hotel property.
- ****Source****
  Name corresponding to the hotel property.
- ****MarketCode****
  Market code for the room.

## Reservation metrics

The following reservation metrics are synced from Cloudbeds:

- ****Created Reservation****
  When a guest’s reservation is created in Cloudbeds.
- ****Confirmed Reservation****
  When a guest’s reservation is confirmed in Cloudbeds.
- ****Checked In to Reservation****
  When a guest checks in to their reservation.
- ****Checked Out of Reservation****
  When a guest checks out of their reservation.
- ****Cancelled Reservation****
  When a guest or admin cancels a guest’s reservation.
- ****No Show Reservation****
  When a guest does not show up to a reservation.

  For each of these metrics, the following top-level properties are synced to Klaviyo:
- ****Value****
  The total monetary value of the reservation.
- ****Reservation ID****
  The reservation ID from Cloudbeds.
- ****Reservation Nights****
  The number of nights of a reservation.
- ****Property ID****
  The ID of the property that the reservation was booked at (e.g., “12345”).
- ****Property Name****
  The name of the property that the reservation was booked at (e.g., “Boutique Hotel in Maine”).
- ****Property Image****
  The main image URL for the property.
- ****Source****
  The source the reservation was booked from (e.g., “Website/Booking Engine”).
- ****Source ID****
  The ID of the source of the reservation (e.g., “s-1”).
- ****Origin****
  The origin of the reservation (e.g., “Expedia”).
- ****Third Party Identifier****
  If the reservation came from an online travel agency (OTA), the ID of the reservation in that system.
- ****Estimated Arrival Time****
  The estimated time the guest will arrive at the property.
- ****Start Date****
  The start date for the reservation.
- ****End Date****
  The end date for the reservation.
- ****Allotment Block Code****
  The allotment block code that was used on the reservation.
- ****Additional Products Value****
  The value of any add-ons a guest purchased on their reservation.
- ****Additional Product Items Count****
  The total number of additional products that a guest purchased on their reservation.
- ****Reservation Person Counts****
  The total number of people included on a reservation.
- ****Reservation Adult Counts****
  The total number of adults included on a reservation.
- ****Reservation Child Counts****
  The total number of children included on a reservation.

## Reservation objects

The latest version of the Cloudbeds integration ([upgrade guide](https://help.klaviyo.com/hc/en-us/articles/39406849361691#h_01K45A8TV1MNXM2CV3TMGRSWWR)) syncs Reservation objects from Cloudbeds. These have the following fields:

- ****Value****
  The total monetary value of the reservation.
- ****ReservationID****
  The reservation ID from Cloudbeds. Used as the object ID.
- ****ReservationStatus****
  The current status of the reservation.
- ****ReservationNights****
  The number of nights of a reservation.
- ****PropertyID****
  The ID of the property that the reservation was booked at (e.g., “12345”).
- ****PropertyName****
  The name of the property that the reservation was booked at (e.g., “Boutique Hotel in Maine”).
- ****PropertyImage****
  The main image URL for the property.
- ****Source****
  The source the reservation was booked from (e.g., “Website/Booking Engine”).
- ****SourceID****
  The ID of the source of the reservation (e.g., “s-1”).
- ****Origin****
  The origin of the reservation (e.g., “Expedia”).
- ****ThirdPartyIdentifier****
  If the reservation came from an online travel agency (OTA), the ID of the reservation in that system.
- ****EstimatedArrivalTime****
  The estimated time the guest will arrive at the property.
- ****StartDate****
  The start date for the reservation.
- ****EndDate****
  The end date for the reservation.
- ****AllotmentBlockCode****
  The allotment block code that was used on the reservation.
- ****RoomTypeName****
  The name of the room type.
- ****AdditionalProductsValue****
  The value of any add-ons a guest purchased on their reservation.
- ****AdditionalProductItemsCount****
  The total number of additional products that a guest purchased on their reservation.
- ****ReservationPersonCounts****
  The total number of people included on a reservation.
- ****ReservationAdultCounts****
  The total number of adults included on a reservation.
- ****ReservationChildCounts****
  The total number of children included on a reservation.

## Guest data

Klaviyo syncs guest data from Cloudbeds. Please note that we do not sync any profiles associated with an online travel agency (OTA).

We sync the following guest data to Klaviyo profiles:

- Email
- Phone number
- First name
- Last name
- Street
- City
- State
- Zip
- Country
- Cloudbeds Guest ID
- Cloudbeds Gender
- Cloudbeds Birthday
- Cloudbeds Company Name
- Cloudbeds Special Requests
- Cloudbeds Main Guest
- Cloudbeds Custom Fields
- Cloudbeds Date Created
- Email consent

Please note that SMS consent is not synced from Cloudbeds.