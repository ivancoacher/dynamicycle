---
id: "115005246968"
title: "Understanding active email profiles in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005246968-Understanding-active-email-profiles-in-Klaviyo"
section: "Getting started with profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:22Z"
language: "en"
---
## You will learn

Learn about active email profiles, including how they differ from [suppressed email profiles](https://help.klaviyo.com/hc/en-us/articles/115005246108), and how you can contact the people represented by these profiles.

![](https://fast.wistia.com/embed/medias/h8mec2r6d0/swatch)

## What is an active profile?

Any profile that can be emailed through Klaviyo is considered an active email profile. There are 2 main categories of active profiles:

- ****Subscribers****
  Subscribers have filled out a sign-up form or otherwise explicitly consented to receive email marketing.
- ****Profiles added by general engagement****
  It is possible for someone to share their email with you without explicitly consenting to ongoing email marketing. For example, someone who placed an order or abandoned a checkout on your site may have added their email address during the checkout process, but never explicitly opted in.

Ecommerce integrations like Shopify and WooCommerce can add both types of active profiles to Klaviyo, depending on the actions a visitor takes while on your site.

## Viewing a profile’s consent status

To see if a profile is able to receive messages and has provided consent, navigate to their profile.

At the top of the **Details** tab of a profile page, you'll see the profile’s consent status and ability to receive messages by channel. The different statuses you may see are:

- ****A green checkmark****
  This symbol indicates that the profile is able to receive marketing because they have subscribed for the corresponding channel and are not suppressed.![profile that is subscribed to email](https://klaviyo.zendesk.com/hc/article_attachments/28723624379035)
- ****A red indicator****
  This symbol indicates that the profile is unable to receive marketing through the channel. This may be because they opted out of marketing, or they are suppressed for a different reason. Note that consent status and suppression status are separate from each other. For example, a profile that is subscribed can be manually suppressed.
  ![profile that is suppressed for email](https://klaviyo.zendesk.com/hc/article_attachments/28723624375963)![profile that is unsubscribed from email](https://klaviyo.zendesk.com/hc/article_attachments/28723629703579)
- ****A yellow checkmark****
  If there is a yellow checkmark next to a person’s email information, it means the profile has neither subscribed nor opted out of email marketing. They are able to receive emails (e.g., an abandoned cart flow email), but you should exercise caution when contacting them.

  ![Profile that is never subscribed for email](https://klaviyo.zendesk.com/hc/article_attachments/28723629708187)

## Profiles that never subscribed

There are certain methods of adding a profile to Klaviyo that result in consent status of **Never Subscribed** (with a yellow checkmark). If a profile has **Never Subscribed** and is also not a member of any lists, they were likely added to Klaviyo due to general engagement with your brand.

For example, this can include profiles synced through certain third-party integrations, or customers that started a checkout without subscribing on your ecommerce platform.

These profiles may have “implicit consent” depending on your local regulations, meaning you may be permitted to email them. They are eligible for campaign and flow emails, but we recommend exercising caution when contacting them. Make sure you’re only sending them emails you know they’ll be interested in, like abandoned cart flow messages or follow-up information from a recent order. Additionally, [use good list cleaning practices](https://help.klaviyo.com/hc/en-us/articles/115005078347-Guide-to-List-Cleaning) and consider each contact’s [engagement](https://help.klaviyo.com/hc/en-us/articles/115000200072-How-to-create-an-engaged-segment) when deciding whether to send to them.

For mobile marketing channels (e.g., SMS or push), profiles need to provide express consent in order to receive messages. Profiles with a status of **Never Subscribed** for SMS are not able to receive messages through the channel until they opt-in, and will have a red indicator instead of a yellow checkmark.

## Contacting active profiles

It is possible to contact all active profiles in your account using both campaign and flow emails.

When sending campaigns, make sure you’re sending to engaged profiles or subscribers only, to avoid being marked as spam or hurting your deliverability.

If you use segments to send emails, make sure your segment requires either engagement (e.g., Opened email in the last 30 days), subscription (e.g., Person can receive email marketing because person subscribed), or both.

Both subscribers and profiles added through general engagement are eligible for certain flow emails. Some types of messaging, like abandoned cart flows, can serve as helpful reminders for recipients and are generally well received. However, keep in mind your local email compliance legislation and subscriber engagement. If needed, you can add the following flow filter to your flows to filter out profiles who haven’t explicitly opted in (i.e., general engagement profiles):

**If someone can or cannot receive marketing  > Person can receive email marketing > Because person subscribed.**

## Additional resources

- [Understanding suppressed email profiles in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005246108)
- [Guide to list cleaning](https://help.klaviyo.com/hc/en-us/articles/115005078347-Guide-to-List-Cleaning)
- [Understanding deliverability best practices](https://klaviyo.zendesk.com/hc/en-us/articles/115005247008)