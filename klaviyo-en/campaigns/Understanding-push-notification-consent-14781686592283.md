---
id: "14781686592283"
title: "Understanding push notification consent"
source_url: "https://help.klaviyo.com/hc/en-us/articles/14781686592283-Understanding-push-notification-consent"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:48:43Z"
language: "en"
---
## You will learn

Learn about [push notification](https://help.klaviyo.com/hc/en-us/articles/360023213971) consent and best practices for compliance. These guidelines can help you be compliant in your consent collection practices and maintain a positive relationship with your customers.

The information provided here is intended to be educational and should not be construed as legal advice. Klaviyo encourages all of our customers to seek legal advice from their counsel on how they specifically should comply with applicable privacy and marketing laws.

## What counts as push notification consent

In order to send a push notification to a profile, you must collect their [explicit consent](https://help.klaviyo.com/hc/en-us/articles/4404203889947) first.

For push notifications, granting consent generates a push token (also called a device token) that is stored on a Klaviyo profile. A push token is valid for only 1 device, and a profile can have multiple push tokens. If someone consents to push notifications on both their phone and tablet, that profile will have 2 different push tokens, one for each device.

Further, consenting to push notifications on one device means you can only send push notifications to that device. It does not mean you can send push notifications to any other device, even if you know it's for the same profile.

Push notification consent is also collected separately from email and SMS consent. If you have consent for a different channel, that does not mean that you can send push notifications to that contact until they specifically opt in to receive push notifications.

### Where to see if a profile consented to push notifications

To see if an individual subscribed to receive push notifications, go to their profile page. Then, check the **Channels** section.

If a user has consented to receive push notifications, a section for “IOS App” or "Android App" will appear with a green checkmark next to it.

![Subscribed to mobile push marketing on a profile](https://klaviyo.zendesk.com/hc/article_attachments/35811315409435)

****What does it mean when there are multiple push tokens on a profile?****

If a profile has multiple push tokens, the user likely has consented to receive notifications for the app on multiple devices. For example, a profile may have an iPhone and an iPad.

It is also possible that multiple tokens are for the same device, but this only temporary. What happens is:

1. A user deletes an app, causing the app service station to invalidate the token.
2. The user later re-downloads the app, so the app service station issues them a new token. (At this time, both the old and new tokens will show on the user's profile.)
3. When you try to send a push notification to this profile, the app service station provides an error about the invalid token.
4. Klaviyo removes the invalid token from the profile.

## Best practices for push notifications

### Permission primer

This permission primer (also known as an opt-in prompt) is an in-app message; it is not a form you design in Klaviyo.

To collect push consent, you must prompt customers to enable push notifications using native iOS and Android prompts.

It is also a best practice to explain why you want to send users notifications first. This push "primer" should outline the types of notifications you send and why users should opt in:

- ****What types of notifications your brand sends****
  Include details about the different push notifications your brand plans to send (for example, account changes, account changes, reminders, and special discounts).
- ****Why users should opt in****
  Include information around why a customer should provide permissions (for example, to receive important updates or early access to sales).

![Example pre-permission prompt to collect push notification consent](https://klaviyo.zendesk.com/hc/article_attachments/28704486353051)

Apple’s native iOS permission prompt will follow your own, where users can provide permission for your app to send push notification to their device.

![Natitve IOS permission prompt for push notifications](https://klaviyo.zendesk.com/hc/article_attachments/28704478241947)

### Example opt-in language

It is best practice for your pre-permission prompt to include details regarding the specific push notifications you plan to send. This lets app users know exactly what they can expect to receive, and builds trust with potential subscribers.

An example of such language is:

“**[Company/We] would like to send you notifications about special discounts, product releases, and shipping updates. You can opt out at any time.”**

However, you can also choose for your pre-permission prompt to more broadly describe the types of notifications you plan to send:

"**[Company/We]** **located in XXX** **would like to send you notifications with marketing and service-related messages. You can opt out at any time.**”

### Notification content

Unlike channels like SMS that have prohibited topics, push notifications do not have regulations that restrict specific types of content. Similarly, no explicit restrictions exist for push notifications based on Apple’s and Android’s terms and conditions. Ensure that the content of your push notifications complies with Klaviyo’s [acceptable use policy](https://www.klaviyo.com/legal/acceptable-use-policy).

### Quiet hours

Push notifications generally do not have any requirements for quiet hours, although in certain countries, quiet hours apply for all marketing communications, including push notifications. As such, it is good practice to avoid sending notifications between the hours of 8 p.m. and 8 a.m. in the recipient's local time zone.

### Notification preferences

It is best practice for your app to further explain what type of content customers might receive when they subscribe to push notifications. This allows customers to reference the types of push notifications they can expect to receive after the initial opt-in disclosure, and opt in to push notifications at a later date if they did not do so during the app setup.

You can build a notification preferences section in your app that displays the notification types that a customer has opted into and allows a user to control their preferences.

Additionally, it is always best practice to send relevant notifications to customers by [collecting information around their interests](https://help.klaviyo.com/hc/en-us/articles/115000250912) and creating targeted [segments](https://help.klaviyo.com/hc/en-us/articles/115005237908).

Note that Klaviyo does not support the creation of a push notification preference center. Klaviyo recommends working with your app’s development team to build this section into your app. If you have additional questions about managing your customers’ push notification preferences with Klaviyo, reach out to our [support team](https://help.klaviyo.com/hc/en-us/requests/new) or on our [community forum](https://community.klaviyo.com/).

## Additional resources

- [Understanding your push notification settings](https://help.klaviyo.com/hc/en-us/articles/12932500186907)
- [How to set up iOS push notifications](https://help.klaviyo.com/hc/en-us/articles/360023213971)
- [How to send a push notification campaign](https://help.klaviyo.com/hc/en-us/articles/360006653972)

Want to request a feature for Klaviyo push notifications? Fill out this [Google form](https://forms.gle/7iPm6JQ4eKB6H2C4A) to tell us about it!