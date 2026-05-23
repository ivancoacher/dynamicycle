<h1>Frequently asked questions about push notification delivery</h1>

## You will learn

Learn the answers to common questions surrounding push notification delivery.

In the sections below, we answer the following questions:

- [Why was a profile skipped from a push notification?](#h_01HFCBTH2A0TCKJHT5YD0RBKF4)
- [If someone deletes the app from their device, will we show a relevant metric in Klaviyo?](#h_01HFCBTH2AK0QKW2N3140HJZSF)
- [Why are push notifications not being delivered to the device after sending?](#h_01HFCBTH2A7S3GFF5SRWMJBGSW)

## Why was a profile skipped from a push notification?

There could be many reasons why a push notification was skipped. However, the most likely ones are:

- [Smart sending](https://help.klaviyo.com/hc/en-us/articles/115002779311) (e.g., a push notification was recently sent to the profile)
- Profile is missing a push token due to the individual:
  - Never enabling push notifications for the app
  - Disabling push notifications for the app
  - Deleting the app (causing the push token to be revoked)

## If someone deletes the app from their device, will we show a relevant metric in Klaviyo?

There is not an “app deleted” metric in Klaviyo; however, the next time you send to someone who deleted the app, there will be a **Bounced Push** event. If the notification bounces due to an invalid token (which can happen when an app is deleted), Klaviyo removes that push token from the profile.

Note that the **Bounced Push** event appears any time a push notification fails. See other failure reasons in this [article on push notification delivery.](https://help.klaviyo.com/hc/en-us/articles/15594685536539)

## Why are push notifications not being delivered to the device after sending?

Most likely, there is an issue with the setup, either with the configuration information provided in your account’s push settings page or with the Klaviyo SDK integration. As a first step, we recommend contacting your app developer and confirming the information provided in your account’s settings.

However, there are 5 other potential issues:

1. The profile does not have a push token (i.e., **Missing Push Token**). In this case, the profile will be skipped, and Klaviyo will not attempt to send a push notification to it.
2. The token on the profile is invalid because the user deleted the app. In this case, the app invalidates the token, and Klaviyo removes it from the profile.
3. The user disabled push notifications for the app. In this case, Android or iOS may not notify Klaviyo that the user disabled notifications, so Klaviyo may show the push notification as delivered, but the user will not see it.
4. The recipient claims they don’t see the notification because the app is open on the device (i.e., the app is foregrounded) when the notification is delivered. When testing push notifications, we recommend closing the app and locking your phone. If you would like, your app developer can implement support for foreground push notifications in the [Klaviyo SDK](https://developers.klaviyo.com/en/docs/sdk_overview).
5. There’s an issue with the intended recipient’s device. **Received Push** events are triggered when Klaviyo makes a successful request to iOS or Android to send a push notification. Thus, if the request was successful but the customer never received the push, it’s likely due to their device. For example, the device may be in do not disturb mode, in low-power or battery-saving mode, or missing network connection, all of which can prevent push notifications from being displayed.
