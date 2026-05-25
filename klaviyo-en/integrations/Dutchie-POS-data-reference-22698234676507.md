---
id: "22698234676507"
title: "Dutchie POS data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/22698234676507-Dutchie-POS-data-reference"
section: "Dutchie POS"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: "en"
---
This reference is about the Dutchie v1 integration, which was built by Klaviyo and is no longer allowing new installations. New customers should use the [Dutchie integration in Klaviyo’s app marketplace](https://marketplace.klaviyo.com/en-us/apps/01KHYQR9B6SBS6Z9WY49PVNYX4), built by KAV Labs. Learn more on [KAV Labs’ help center](https://kavlabs.co/documentation/dutchie).

## You will learn

Learn what data is synced from Dutchie POS to Klaviyo, how to view it and what properties Dutchie events contain. Additionally, learn how to view your Dutchie data in Klaviyo.

If you have not already, read our article [Getting started with Dutchie POS](https://help.klaviyo.com/hc/en-us/articles/22698258709531) for step-by-step instructions on how to integrate, and other considerations, before continuing with this article.

## Data synced from Dutchie POS to Klaviyo

To check on the data sync from Dutchie POS to Klaviyo:

1. In your Klaviyo account, select ****Analytics > Metrics****.
2. At the top, filter by **Dutchie**.

![](https://klaviyo.zendesk.com/hc/article_attachments/28716118875035)

The data synced from Dutchie to Klaviyo includes:

- Profile information associated with order events.
- The following order events:
  - **Placed Order**
  - **Ordered Product**

## Customer information details

Klaviyo will only sync profiles that have an email address. We recommend turning on the setting **Require email address for guest checkout** in Dutchie Ecommerce, which can be found under ****Settings > Options > Checkout****. The email address will sync to Dutchie POS.

Customers consenting to email marketing during an ecommerce checkout are not synced to Dutchie POS, and thus:

- No profiles synced from Dutchie POS to Klaviyo show as being explicitly consented to email marketing.
  - Klaviyo marks synced profiles from Dutchie as **Never Subscribed**.
  - Profiles marked as **Never Subscribed** can technically receive emails, though they have not provided explicit consent.

    Customer profile information syncs from Dutchie to Klaviyo with the following properties:
- email
- phone\_number
- first\_name
- last\_name
- dateOfBirth
- Dutchie createdAtLocation
- Dutchie creationDate
- Dutchie customerId
- Dutchie customerType
- Dutchie isLoyaltyMember
- Dutchie lastModifiedDateUTC
- Dutchie status

## Synced events and their properties

### Placed Order

The **Placed Order** event syncs from Dutchie POS to Klaviyo with the following properties:

- OrderId
- items
- transactionType
- locationName
- $event\_id
- $value

### Ordered Product

The following properties will only be received if they have been [added in Dutchie POS Backoffice catalog](https://support.dutchie.com/hc/en-us/articles/12882361852563-Add-products-to-Catalog). It is recommended to review the catalog to ensure all information is complete.

The Ordered Product event syncs from Dutchie POS to Klaviyo with the following properties:

- strain
- strainType
- brandName
- transactionId
- productId
- totalPrice
- quantity
- unitPrice
- unitCost
- packageId
- sourcePackageId
- totalDiscount
- unitId
- unitWeight
- unitWeightUnit
- flowerEquivalent
- flowerEquivalentUnit
- discounts
- taxes
- returnDate
- isReturned
- returnedByTransactionId
- returnReason
- batchName
- transactionItemId
- locationName
- vendor
- isCoupon
- customerId
- transactionDate
- $event\_id
- $value