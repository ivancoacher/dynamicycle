---
id: "15752724401691"
title: "Zenoti data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/15752724401691-Zenoti-data-reference"
section: "Zenoti"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:43Z"
language: "en"
---
This article covers the data that is synced when you integrate Zenoti with your Klaviyo account.

## Understand your Zenoti data

Klaviyo syncs many different events from Zenoti related to appointments and membership. We sync 1 year of historic Zenoti data.

To view your Zenoti data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. The metrics with a Zenoti icon represent all of the metrics synced from your Zenoti integration.
3. Filter this view to see only Zenoti metrics by using the filter selector next to the search bar.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39059634128155)

## Appointment metrics

### Booked Appointments

This event is tracked when a new group of appointments is booked.

- ****Value****The value of the item, i.e., price of appointments package.
- ****Appointment Group ID****The ID of the group to which the appointments belong.
- ****Appointment Names****The list of names for each appointment.
- ****Appointments****The list of appointment details, e.g., **start time, end time, creation date**.
- ****Categories****The list of categories for the appointments.
- ****Center ID****
  The ID of the location where the appointments take place.
- ****Center Name****The name of the location where the appointments take place.
- ****Center Address****The street address of the location where the appointments take place.
- ****Center City****The city of the location where the appointments take place.
- ****Center State****The state of the location where the appointments take place.
- ****Center Zip****The zip code of the location where the appointments take place.
- ****Center Email****The email address of the location where the appointments take place.
- ****Center Phone****The phone number of the location where the appointments take place.
- ****Invoice ID****The ID of the invoice for the appointments.
- ****Invoice Number****The unique number associated with the invoice.
- ****Invoice Number Prefix****The prefix displayed before the invoice number.
- ****Therapist Names****The list of names for therapists performing the appointment.

### Cancelled Appointments

This event is tracked when a guest cancels their group of appointments.

- ****Appointment Group ID****
  The ID of the group to which the appointments belong.
- ****Appointment Group Status****The status of the appointment group, represented by a numerical value, e.g., **-1.**
- ****Appointment Group Status Name****Name of appointment group status, e.g., **Canceled.**
- ****Appointment Names****The list of names for each appointment.
- ****Categories****The list of categories for the appointments.
- ****Therapist Names****The list of names for therapists performing the appointment.
- ****Center ID****
  The ID of the location where the appointments take place.
- ****Center Name****The name of the location where the appointments take place.
- ****Center Address****The street address of the location where the appointments take place.
- ****Center City****The city of the location where the appointments take place.
- ****Center State****The state of the location where the appointments take place.
- ****Center Zip****The zip code of the location where the appointments take place.
- ****Center Email****The email address of the location where the appointments take place.
- ****Center Phone****The phone number of the location where the appointments take place.
- ****Cancellation Fee Required****(Yes/No)
- ****No Show Fee Required****(Yes/No)

### Checked In to Appointments

This event is tracked when a guest checks in for their appointments.

- ****Appointment Group ID****
  The ID of the group to which the appointments belong.
- ****Appointment Group Status****Status of the appointment group, represented by a numerical value, e.g., **2.**
- ****Appointment Group Status Name****Name of appointment group status, e.g., **Checkin.**
- ****Appointment Names****The list of names for each appointment.
- ****Categories****The list of categories for the appointments.
- ****Therapist Names****The list of names for therapists performing the appointment.
- ****Center ID****
  The ID of the location where the appointments take place.
- ****Center Name****The name of the location where the appointments take place.
- ****Center Address****The street address of the location where the appointments take place.
- ****Center City****The city of the location where the appointments take place.
- ****Center State****The state of the location where the appointments take place.
- ****Center Zip****The zip code of the location where the appointments take place.
- ****Center Email****The email address of the location where the appointments take place.
- ****Center Phone****The phone number of the location where the appointments take place.
- ****Cancellation Fee Required****(Yes/No)
- ****No Show Fee Required****(Yes/No)

### Closed Appointments

This event is tracked when a guest closes their appointments.

- ****Appointment Group ID****
  The ID of the group to which the appointments belong.
- ****Appointment Group Status****Status of the appointment group, represented by a numerical value, e.g., **1.**
- ****Appointment Group Status Name****Name of appointment group status, e.g., **Closed.**
- ****Appointment Names****The list of names for each appointment.
- ****Categories****The list of categories for the appointments.
- ****Therapist Names****The list of names for therapists performing the appointment.
- ****Center ID****
  The ID of the location where the appointments take place.
- ****Center Name****The name of the location where the appointments take place.
- ****Center Address****The street address of the location where the appointments take place.
- ****Center City****The city of the location where the appointments take place.
- ****Center State****The state of the location where the appointments take place.
- ****Center Zip****The zip code of the location where the appointments take place.
- ****Center Email****The email address of the location where the appointments take place.
- ****Center Phone****The phone number of the location where the appointments take place.
- ****Cancellation Fee Required****(Yes/No)
- ****No Show Fee Required****(Yes/No)

### Completed Appointment

This event is tracked when a guest completes a specific appointment.

- ****Value****The value of the item, i.e., price of appointments package.
- ****Appointment Group ID****The ID of the group to which the appointments belong.
- ****Appointment Names****The list of names for each appointment.
- ****Appointments****The list of appointment details, e.g., **start time, end time, creation date.**
- ****Center ID****The ID of the location where the appointments take place.
- ****Center Name****The name of the location where the appointments take place.
- ****Invoice ID****The ID of the invoice for the appointments.
- ****Invoice Number****The unique number associated with the invoice.

### Confirmed Appointments

This event is tracked when a guest confirms their appointments.

- ****Appointment Group ID****
  The ID of the group to which the appointments belong.
- ****Appointment Group Status****Status of the appointment group, represented by a numerical value, e.g., **4.**
- ****Appointment Group Status Name****Name of appointment group status, e.g., **Confirm.**
- ****Appointment Names****The list of names for each appointment.
- ****Categories****The list of categories for the appointments.
- ****Therapist Names****The list of names for therapists performing the appointment.
- ****Center ID****
  The ID of the location where the appointments take place.
- ****Center Name****The name of the location where the appointments take place.
- ****Center Address****The street address of the location where the appointments take place.
- ****Center City****The city of the location where the appointments take place.
- ****Center State****The state of the location where the appointments take place.
- ****Center Zip****The zip code of the location where the appointments take place.
- ****Center Email****The email address of the location where the appointments take place.
- ****Center Phone****The phone number of the location where the appointments take place.
- ****Cancellation Fee Required****(Yes/No)
- ****No Show Fee Required****(Yes/No)

### Missed Appointments

This event is tracked when a guest is a no show for their appointments.

- ****Appointment Group ID****
  The ID of the group to which the appointments belong.
- ****Appointment Group Status****Status of the appointment group, represented by a numerical value, e.g., **-2.**
- ****Appointment Group Status Name****Name of appointment group status, e.g., **NoShow.**
- ****Appointment Names****The list of names for each appointment.
- ****Categories****The list of categories for the appointments.
- ****Therapist Names****The list of names for therapists performing the appointment.
- ****Center ID****
  The ID of the location where the appointments take place.
- ****Center Name****The name of the location where the appointments take place.
- ****Center Address****The street address of the location where the appointments take place.
- ****Center City****The city of the location where the appointments take place.
- ****Center State****The state of the location where the appointments take place.
- ****Center Zip****The zip code of the location where the appointments take place.
- ****Center Email****The email address of the location where the appointments take place.
- ****Center Phone****The phone number of the location where the appointments take place.
- ****Cancellation Fee Required****(Yes/No)
- ****No Show Fee Required****(Yes/No)

### Started Appointment

This event is tracked when a guest starts a specific appointment.

- ****Value****The value of the item, i.e., price of the appointment.
- ****Appointment Group ID****The ID of the group to which the appointments belong.
- ****Appointment Names****The list of names for each appointment.
- ****Appointments****The list of appointment details, e.g., **start time, end time, creation date.**
- ****Center ID****The ID of the location where the appointments take place.
- ****Center Name****The name of the location where the appointments take place.
- ****Invoice ID****The ID of the invoice for the appointments.
- ****Invoice Number****The unique number associated with the invoice.

## Membership metrics

### Activated Membership

This event is tracked when a guest activates a membership.

- ****Value****
  The value of the item, i.e., price of the appointment.
- ****Auto Renewal****List of details associated with renewal, e.g., **renew\_status, is\_expired.**
- ****Center ID****The ID of the location associated with the membership.
- ****Center Name****The name of the location associated with the membership.
- ****Credit Balance****The numerical balance of the membership.
- ****Expiry Date****The date the membership expires.
- ****Grace Period Date****The date the grace period starts.
- ****Grace Period Days****The length of the grace period in days.
- ****Group User Membership ID****The Id of the membership group.
- ****Has Digital Form****(true/false)
- ****Invoice****The list of details associated with the invoice, e.g., **item\_id, receipt\_no, status.**
- ****Member Code****The unique code associated with the membership.
- ****Members****List of the names of members associated with the membership.
- ****Membership****List of details associated with the membership, e.g., **OTP\_required, guestpass\_total.**
- ****Membership Name****The name of the membership.
- ****Next Collection Date****The date of the next membership payment.
- ****Payments****List of payment details, e.g., **payment\_type, default\_payment\_info.**
- ****Pending Waive Collections****The amount of payments that will be waived.
- ****Purchase****The price of the membership purchase.
- ****Recurrence Status****The numerical status of the membership.
- ****Recurrence Status Name****The name of the recurring payment plan, e.g., **Default**
- ****Recurring Details****Any additional details related to the recurring payment plan.
- ****Refunded****
  (true/false)
- ****Service Balance****
  The amount the guest owes for membership-related services.
- ****Status****The status of the guest’s membership represented by a numerical value, e.g., **1** for active membership.
- ****Status Name****
  The name of status of the guest’s membership, e.g., **Active.**
- ****User Membership ID****The ID of the guest’s membership.

### Canceled Membership

This event is tracked when a guest cancels a membership.

- ****Cancel Date****
  The date on which the cancellation will take effect.
- ****Cancel Initiated Date****The date on which the cancellation was issued.
- ****Cancel Reason****The selected reason for the cancellation.
- ****Canceled By****The name of the guest who issued the cancellation.
- ****Center ID****The ID of the location associated with the membership.
- ****Center Name****The name of the location associated with the membership.
- ****Expiry Date****The date the membership expires.
- ****Grace Period Date****The date the grace period starts.
- ****Grace Period Days****The length of the grace period in days.
- ****Member Code****The unique code associated with the membership.
- ****Recurrence Status****
  The numerical status of the membership.
- ****Recurrence Status Name****The name of the recurring payment plan, e.g., **Default.**
- ****Status****The status of the guest’s membership represented by a numerical value, e.g., -**1** for canceled membership.
- ****Status Name****
  The name of the status of the guest’s membership, e.g., **Canceled.**
- ****Termination Date****The date the cancellation goes into effect.

### Froze Membership

This event is tracked when a guest freezes a membership to be reactivated at a later time.

- ****Center ID****
  The ID of the location associated with the membership.
- ****Center Name****The name of the location associated with the membership.
- ****Comments****Any comments left by the guest related to why they are freezing their membership.
- ****Expiry Date****The date the membership expires.
- ****Freeze Fee****The total cost to freeze the membership.
- ****Freeze Fee Type****The freeze fee type represented by a numerical value.
- ****Freeze Start Date****The date the freeze goes into effect.
- ****Freeze End Date****The date the membership unfreezes.
- ****Freeze Type****
  The type of freeze represented by a numerical value.
- ****Froze By****The name of the guest who froze the membership.
- ****Group User Membership ID****The Id of the membership group.
- ****Member Code****The unique code associated with the membership.
- ****Next Collection Date****
  The date of the next membership payment.
- ****Recurrence Status****The status of the guest’s membership represented by a numerical value, e.g., **3** for frozen membership.
- ****Recurrence Status Name****The name of the recurrence status, e.g., **Frozen.**
- ****Status****The status of the guest’s membership represented by a numerical value, e.g., **3** for frozen membership.
- ****Status Name****
  The name of the status of the guest’s membership, e.g., **Frozen.**
- ****User Membership ID****The ID of the guest’s membership.

### Unfroze Membership

This event is tracked when a guest unfreezes a membership.

- ****Center ID****
  The ID of the location associated with the membership.
- ****Center Name****The name of the location associated with the membership.
- ****Expiry Date****The date the membership expires.
- ****Member Code****The unique code associated with the membership.
- ****Next Collection Date****The date of the next membership payment.
- ****Recurrence Status****Numerical status of the membership.
- ****Recurrence Status Name****The name of the recurring payment plan, e.g., **Active.**
- ****Status****The status of the guest’s membership represented by a numerical value, e.g., **1** for active membership.
- ****Status Name****
  The name of the status of the guest’s membership, e.g., **Active.**

## Other metrics

### Closed Invoice

This event is tracked when an invoice is closed.

- ****Value****
  The value of the item (total value of all items on the invoice).
- ****Appointment Group ID****The ID of the appointment group associated with the invoice.
- ****Appointment Names****The list of names for each appointment associated with the invoice.
- ****Appointments****The list of appointment details, e.g., **start time, end time, creation date.**
- ****Center ID****The ID of the location where the invoice was closed.
- ****Center Name****The name of the location where the invoice was closed.
- ****Closed****(true/false)
- ****Invoice Date****
  The date the invoice was created.
- ****Invoice ID****The ID of the invoice for the appointments.
- ****Invoice Items****The list of items that appear on the invoice.
- ****Invoice Number****The unique number associated with the invoice.
- ****Invoice Number Prefix****The prefix displayed before the invoice number.
- ****Lock****(true/false)
- ****Receipt Number****The receipt number printed on the invoice.
- ****Refund****(true/false)
- ****Total Price****The price listed on the invoice, including tax.
- ****Transactions****The list of transactions printed on the invoice.

### Ordered Giftcard

This event is tracked when a guest orders a new gift card.

- ****Value****
  Total value of the gift card at time of purchase.
- ****Center ID****The ID of the location where the gift card was ordered.
- ****Center Name****The name of the location where the gift card was ordered.
- ****Code****The code displayed on the gift card.
- ****Comments****Comments left by the purchaser of the gift card.
- ****Current Balance****The current monetary balance of the gift card.
- ****Expiration Date****The date on which the gift card expires.
- ****Expiration Days****The number of days until the card expires.
- ****Invoice ID****The ID of the invoice for the appointments.
- ****Invoice Number****The unique number associated with the invoice.
- ****Notes****Any notes associated with the gift card purchase.
- ****One time Use****Whether or not the gift card is 1 time use.
- ****Restrict Usage to Sale Center****(true/false)

### Submitted Feedback

This event is tracked when a guest submits feedback after an appointment.

- ****Appointment Group ID****
  The ID of the group of the appointment associated with the feedback.
- ****Center ID****The ID of the location where the feedback was submitted.
- ****Center Name****The name of the location where the feedback was submitted.
- ****Comments****Feedback comments left by the guest.
- ****Guest Feedback Tags****Tags associated with the feedback, e.g., **Check-in, Ambiance, Cleanliness, Check-out**.
- ****Rating Value****The numerical rating of the feedback out of 5.
- ****Source****The source of the feedback represented by a numerical code.
- ****Version****The version of Zenoti used when the feedback was submitted.

### Created Package

This event is tracked when a guest purchases a package.

- ****Value****
  The total value of the package at time of creation.
- ****Can Transfer Benefits****(Yes/No)
- ****Center ID****The ID of the location associated with the membership.
- ****Center Name****The name of the location associated with the membership.
- ****Date****The date when the package was created.
- ****Discounts****Any discounts applied to the package.
- ****Expiration Days****The number of days left until the package expires.
- ****Has First Redemption****(true/false)
- ****Invoice****The list of details associated with the invoice, e.g., **item\_id, receipt\_no, status.**
- ****Never Expires****(true/false)
- ****Package****The list of details related to the package.
- ****Package Name****The name of the package, e.g., **Class Pack.**
- ****Products****The list of products in the package.
- ****Purchase****The list of price information including currency, tax, and final price.
- ****Refunded****(true/false)
- ****Returned****
  (true/false)
- ****Sale Invoice****
  The list of invoice information including ID, item ID, and invoice number.
- ****Schedule****
  The list of schedule information associated with the package.
- ****Services****
  The list of services associated with the package.
- ****Start Validity at First Redemption****
  (true/false)
- ****Status****
  The status of the package represented by a numerical value.
- ****User Package ID****
  The ID of the guest’s package.
- ****User Package State****
  The state of the guest’s package represented by a numerical value.

### Redeemed Package

This event is tracked when a guest redeems a package.

- ****Value****The total value of the gift card at time of redemption.
- ****Can Transfer Benefits****Whether or not benefits can be transferred between guests.
- ****Center ID****The ID of the location associated with the package.
- ****Center Name****The name of the location associated with the package.
- ****Date****The start and end dates when the package is in effect.
- ****Discounts****Any discounts applied to the package.
- ****Expiration Days****The number of days left until the package expires.
- ****Has First Redemption****(true/false)
- ****Invoice****The list of details associated with the invoice, e.g., **item\_id, receipt\_no, status.**
- ****Never Expires****
  (true/false)
- ****Package****The list of details related to the package.
- ****Package Name****
  The name of the package, e.g., **Signature Spa Package.**
- ****Product Redemptions****The list of redeemed products included with the package.
- ****Purchase****
  The purchase details include tax and final price.
- ****Refunded****
  (true/false)
- ****Returned****
  (true/false)
- ****Sale Invoice****The list of details associated with the sale invoice, e.g., **id, item\_id, no.**
- ****Schedule****Scheduling details associated with the package.
- ****Service Redemptions****
  The list of redeemed services included with the package.
- ****Start Validity at First Redemption****
  (true/false)
- ****Status****The status of the package represented by a numerical value.
- ****User Package ID****
  ID associated with the user package in Zenoti.
- ****User Package State****The state associated with the user package represented by a numerical value.

### Raw data

This event tracks any other data sent by Zenoti. Its properties will vary.

## Synced guest data

The data sync with Zenoti is one-way from Zenoti to Klaviyo. This means that editing profile information in Klaviyo will not update information in Zenoti.

Klaviyo creates or updates profiles for every guest with Email, First and Last Name, Phone Number, and will set a custom profile properties of:

- ****Zenoti ID****
  ID assigned to the guest in Zenoti.
- ****Receive Marketing Email****
  Whether or not a guest has opted-in to receive marketing emails. (true/false)
- ****Receive Marketing SMS****
  Whether or not a guest has opted-in to receive marketing SMS. (true/false)
- ****Receive Transactional Email****
  Whether or not a guest can receive transactional emails. (true/false)
- ****Receive Transactional SMS****
  Whether or not a guest can receive transactional SMS. (true/false)
- ****Zenoti Guest Tags****Guest tags.
- ****Birthday****The guest's birthday.

Klaviyo syncs email consent from Zenoti as consent records. While we sync the above SMS-related custom profile properties from Zenoti, we do not sync SMS consent from Zenoti as consent records.

## Additional resources

[Getting started with Zenoti](https://klaviyo.zendesk.com/hc/en-us/articles/15752461211547)