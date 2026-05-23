---
id: 115005073907
title: "Understanding when and how Klaviyo sets a profile's location"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005073907-Understanding-when-and-how-Klaviyo-sets-a-profile-s-location"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-18T18:44:56Z"
language: en
---

## You will learn

Learn where to find location information for a profile, how it is used and updated, and more. When syncing or creating a new profile, Klaviyo determines the location and timezone information based on the profile's billing address. If a profile hasn't purchased, location and timezone are determined based on IP geolocation.

## Find location information in a profile

You can find the location for a profile by navigating to their profile page in Klaviyo, where the location is displayed in the header along with any contact information.

![Top of the profile page](https://klaviyo.zendesk.com/hc/article_attachments/33101716556571)

## How locations are used and updated in Klaviyo

A profile's location and timezone are used when [sending based on recipients' timezones](https://help.klaviyo.com/hc/en-us/articles/115005054847#schedule-and-send-your-campaign6), [creating location-based segments](https://help.klaviyo.com/hc/en-us/articles/115005065887), or adding location- or timezone-specific filters to flows.

Here is an example outline of how a profile's location and timezone information are set and updated:

1. ****A profile visits your website or submits a form.**** The request includes their IP address but no address data, so Klaviyo estimates their location and timezone from the IP.
2. ****The profile places an order through Shopify.**** Klaviyo's Shopify integration extracts the billing address from the order and updates the profile's location and timezone. Because this
   address data is more authoritative than an IP-based estimate, it takes priority.
3. ****The profile continues browsing your site.**** Even though these interactions include an IP address, the profile's location is now protected — IP-based estimation will not overwrite address
   data set by Shopify.
4. ****A customer update syncs from Shopify.**** If the customer's default address in Shopify differs from the billing address on their last order, the profile's location will be updated to reflect the customer record. Both sources carry the same authority, so the most recently synced data is what appears on the profile.
   Note that email opens and clicks do not update a profile's location or timezone, even if the profile has no other location data.

![Example of where location and timezone are displayed in a profile](https://klaviyo.zendesk.com/hc/article_attachments/33101716559387)

If you are using a custom integration, billing address is not used to determine location. You'll need to set profiles' locations with the location object in the Profiles API. Learn more about [custom integrations](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration) and Klaviyo's [Profiles API](https://developers.klaviyo.com/en/reference/create_profile).

When collecting phone numbers, the number's area code does not affect the location saved on the profile. However, area code can be used to determine a recipient's [quiet hours](https://help.klaviyo.com/hc/en-us/articles/22711363273627).

## IP geolocation

Klaviyo uses IP geolocation to set a profile's location when a billing address has not been received. Klaviyo can identify a person via their IP and sets a location when that profile:

- Click through a message
- Subscribe via a Klaviyo sign-up form
- Are captured by Klaviyo's web tracking snippet

  Although IP geolocation is used as the industry standard, it can sometimes be inaccurate. Here are a few reasons you might see discrepancies between a profile's IP geolocation and where they are actually located:
- Klaviyo checks someone's IP whenever they open an email or are captured via web tracking. For example, if someone is on a trip to China when they open the email, their IP will reflect this, even if their typical location is in California.
- IPs are not static, and the location affiliated with an IP is also not static; this makes IP geolocation imperfect.

  If a user's internet service provider assigns an IPv6 address to their connection, their location may not be captured correctly.

  This is most relevant when you want to schedule a campaign that sends to each recipient in their own timezone. Depending on where a recipient was the last time they opened an email or opted-in via a sign-up form, it's possible that the timezone Klaviyo has recorded for a recipient at send time will not be the same timezone the recipient is in when they receive your next campaign.

  Additional situations where Klaviyo won't be able to get accurate IP data from email open events:
- If the **Opened Email** event, when tracked, goes through a proxy; this is true of emails opened in Gmail.
- If the **Opened Email** event is synced to Klaviyo through an integration, like Mailchimp. In this case, the IP we assess will be a Mailchimp server IP and not the actual email recipient's IP.

## Update location information yourself

If you want to update any location-related properties for one or more profiles (either by [manually importing](https://help.klaviyo.com/hc/en-us/articles/115005074627#add-a-custom-property-yourself2) this location data or [using the API](https://developers.klaviyo.com/en/reference/update_profile)), you need to reference the relevant Klaviyo property name:

- ****City:**** the city where they live
- ****State/Region:**** the state/region where they live
- ****Country:**** the country where they live
- ****Zip Code:**** the postal code where they live

For more information about properties and how to manage and update them, head to our [guide on properties](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627).