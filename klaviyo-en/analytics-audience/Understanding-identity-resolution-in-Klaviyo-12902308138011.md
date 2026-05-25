---
id: "12902308138011"
title: "Understanding identity resolution in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/12902308138011-Understanding-identity-resolution-in-Klaviyo"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:27Z"
language: "en"
---
## You will learn

Learn about identity resolution in Klaviyo, which consolidates customers’ interactions across multiple channels under a single record.

Since Klaviyo is an omnichannel marketing tool that supports email, SMS, and mobile push notifications, your customers may interact with you through either or all of these channels. To ensure that your customer profiles remain up to date with activity across all these channels, Klaviyo automatically resolves the identities of different profiles that share a common identifier based on the existing data in your account.

## What is identity resolution?

Identity resolution refers to the process of maintaining a unified customer record, regardless of the various identifiers (e.g. email, phone number, etc.) used across different touchpoints or devices. This results in a singular, comprehensive profile for each individual person, irrespective of the channels they interact through.

Identity resolution is often used as a general term that encompasses 2 key data tracking and unification processes:

- ****Identifying customers****
  Recognizing who someone is based on an identity they have provided, or other digital signals.
- ****Resolving profiles to a single identity****
  Consolidating behaviors to identities and de-duplicating records to create a unified view of the customer.

A common example of this is when a customer that has an email profile in your Klaviyo account later subscribes to SMS through a method that is not associated with their email, like a [keyword opt-in](https://help.klaviyo.com/hc/en-us/articles/360050384091). This customer action results in a separate profile for receiving SMS messages. However, if this customer later takes an action like making a purchase where they submit both their phone and email; Klaviyo will recognize that both the phone and email belong to the same customer and their profiles will be merged.

## Identifying customers

Klaviyo’s automatically cookies and captures identities from customers through a few different methods.

### Onsite JavaScript tracking

Klaviyo's [onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767) is responsible for tracking the **Active on Site** and **Viewed** Product events across your entire website for identified browsers.

### Additional Shopify tracking via Shopify Server Pixel

For Shopify users, you can also easily enable new tracking events such as **Added to Cart**, **Viewed Page**, **Viewed Collection**, and **Submitted Search** through the [Shopify pixel](https://help.klaviyo.com/hc/en-us/articles/4425956184731). These events sync server-side, providing more complete profiles with more events syncing and flows triggering in Klaviyo.

### Forms

[Sign-up forms](https://help.klaviyo.com/hc/en-us/articles/360026474752) allow you to serve targeted forms and collect customer emails and phone numbers. These are an important part of growing your list and subscriber base. When customers submit a Klaviyo form, their browser is automatically identified via Klaviyo's onsite tracking so you can view the actions that they take on your website.

### Message click-through

Unlike other data platforms, Klaviyo is responsible for sending messages. When recipient clicks a link in an email that you send, their browser is automatically identified so you can see where they land on your site, and track other onsite actions going forward.

### Checkout identification

When visitors go through checkout on your website, Klaviyo automatically identities them and collects checkout events.

This functionality can vary across different integrations.

## Resolving profiles to a single identity

Klaviyo resolves customer identities through 2 main methods.

### Anonymous visitor activity backfill

With Klaviyo’s anonymous visitor activity backfill, you can capture onsite activity for a shopper prior to identification. Once that visitor is identified in the future, you’ll have access to their historical onsite events. This allows you to have a more complete view of your customers’ journeys, and enrich customer profiles with historical data. Learn more about Klaviyo’s [anonymous visitor activity backfill](https://help.klaviyo.com/hc/en-us/articles/17928628922395).

To collect anonymous visitor activity, you must have the Klaviyo.js installed on your store (which is automatic for most integrations). Klaviyo.js allows you to publish Klaviyo sign-up forms and track shoppers’ activities on your website.

Once the Klaviyo.js is successfully installed on your website, you can enable anonymous visitor activity backfill in your account settings.

To enable anonymous visitor activity backfill:

1. Select your account name in the lower left.
2. Select ****Settings****.
3. Go to the ****Data****.
4. Check the **Enable anonymous visitor tracking** box.
   ![Data tab, showing the Anonymous visitor tracking option](https://klaviyo.zendesk.com/hc/article_attachments/34262891532059)
5. Click ****Update****.

### Deterministic profile merging

Deterministic profile merging refers to a proactive check that merges two separate profiles when an action occurs linking an email address, phone number, or device ID (iOS) together. This includes merging data across multiple devices, and allows you to effectively manage omnichannel customer data.

## How identity resolution works in Klaviyo

As customers interact with your brand across different channels, Klaviyo checks for opportunities to merge these engagements under a single customer profile.

This is based on a process called "identifier precedence,” where Klaviyo uses existing data to determine if these omni-channel engagements can be consolidated under a single, stronger identifier.

Klaviyo ranks these identifiers as:

1. ****Profile ID****
   The primary identifier Klaviyo assigns to each profile.
2. ****External ID****
   An external ID that can be used as a primary identifier on the profile, typically in place of an email address. External IDs are set through some integrations (e.g. Bigcommerce), or through [Klaviyo’s APIs.](https://developers.klaviyo.com/en/docs/update_profile_properties_via_api)
3. ****Email****
   The email address associated with a profile.
4. ****Phone number****
   The phone number associated with a profile.
5. ****Anonymous mobile app ID****
   For mobile app profiles, if Klaviyo cannot associate the user with an email address, an anonymous mobile app ID will represent the iOS or Android guest profile.

Only email and phone number are supported by Klaviyo's onsite tracking at this time.

When Klaviyo creates an anonymous mobile app ID, all of the following ID types are considered:

- IDFA or Push Token on iOS.
- Google Ad ID (GAID), Firebase ID (FID) or Device ID on Android.

For each lower-ranking identifier, Klaviyo checks if a profile exists within the account recognized only by that identifier. If such a profile is found and can be associated with a higher-ranking identifier based on an instance where they were linked together, Klaviyo will attempt to merge under the higher-ranking identifier.

To illustrate this, below is an example where Klaviyo is resolving the identity of a customer with the following set of identifiers:

|  |  |
| --- | --- |
| ****Identifier type**** | ****Value**** |
| Email | example@klaviyo.com |
| Phone number | 123-456-7890 |
| Anonymous mobile app ID | iOS:000000-0000-0000-000000 |

Once Klaviyo sees all 3 identifiers together, which indicates they all belong to the same customer, it will check if there is a profile only identified by phone number or only identified by an anonymous mobile app ID. If either is found, they will be merged into the profile with the higher-ranking identifier, in this case email.

## Data that triggers a profile merge

For Klaviyo to identify that multiple profiles belong to the same customer, the identifiers associated with each profile need to be recognized together. Often, this information comes in the form of an event, where the event data includes multiple identifiers like email and phone number. Klaviyo also merges profiles based on data that customers submit themselves (e.g., through a form that has fields for both phone and email).

Klaviyo merges profiles based on information submitted through web tracking as well, which associates an activity to an email profile using [cookies](https://help.klaviyo.com/hc/en-us/articles/360034666712). For example, if an email profile submits a phone-only form with their cookie present, then the phone number they submit will be appended to their pre-existing profile.

Actions related to click-to-text or keywords will generally not result in a merge based on cookie tracking. This is because the cookie trail is lost across applications (e.g., web to SMS) and we cannot be certain that the 2 actions were taken by the same person.

## Find a profile ID

Every profile has a unique ID that you can find by navigating to the profile and looking at the URL. Look for the 26-character ID, as illustrated in the image below.
![24-character profile ID in the URL of a profile](https://klaviyo.zendesk.com/hc/article_attachments/34262891536667)

Some older profiles in your account may have a six-character ID if you acquired them prior to this Klaviyo change. This ID is still correct and unique to their profile.

![6 character profile ID in the URL of a profile](https://klaviyo.zendesk.com/hc/article_attachments/28705664932507)

To call this ID dynamically, you can use {{ person.KlaviyoID }}.

## Manually merge profiles

If you know that a pair of profiles belongs to a single customer, you can manually merge the two. Merging a pair of profiles will result in only one profile, with one email address, for the contact. The customer ID of the most recently updated profile will be maintained.

Note that merging profiles cannot be reversed.

To manually merge a profile:

1. Navigate to the source profile you want to remove.
2. Open the ****Profile actions**** dropdown.
3. Click ****Merge profile****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34262891541403)
4. In the popup that appears, search for the destination profile (the one you want to merge into or keep).
5. Select a profile from your search results.
   - If you don’t see the destination profile you’d like to merge into, make sure there are no typos in your search. Then hit the ****Return**** or ****Enter**** button to search again.

For more information, head to our guide on [how to delete, merge, and export a profile](https://help.klaviyo.com/hc/en-us/articles/115005073847).

## Additional resources

- [Understanding profiles in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005247088)
- [Understanding when SMS profiles merge](https://help.klaviyo.com/hc/en-us/articles/360035588012)
- [Understanding cookies in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360034666712)