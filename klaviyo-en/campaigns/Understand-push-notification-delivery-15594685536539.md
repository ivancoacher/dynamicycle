---
id: "15594685536539"
title: "Understand push notification delivery"
source_url: "https://help.klaviyo.com/hc/en-us/articles/15594685536539-Understand-push-notification-delivery"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:48:44Z"
language: "en"
---
Learn about push notification delivery, including how it is delivered and why it might fail.

## Push notification delivery

Push notification delivery refers to when a push notification is successfully delivered to a recipient’s device.

A profile may have more than 1 push token if they have your mobile app installed on multiple devices. Push notifications will be attempted for all the devices with a token stored on the profile.

The concept of [deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008) does not apply to push notifications like it does for email, as there is no sorting performed once the recipient’s device successfully receives the notification.

When you send a push notification through a campaign or flow, Klaviyo checks the push and then sends it to Apple Push Notification Service (APNs) for iOS, or Android’s push notification service, Firebase Cloud Messaging (FCM) for delivery to the recipient’s device. You may see some push notifications skipped if there is an issue with delivery.

APNs and FCM will either accept the notification and attempt to deliver it to the recipient's device, or reject the notification with a series of possible errors.

Klaviyo only has insight into whether these services accept the notification or reject it. Klaviyo cannot confirm if the notification fails after APNs or FCM accepts the push.

Want to request a feature for Klaviyo push notifications? Fill out this [Google form](https://forms.gle/7iPm6JQ4eKB6H2C4A) to tell us about it!

## Reasons for rejection

If Klaviyo receives an error response from APNs or FCM after sending a notification, an event called **Bounced push** is created for each token affected by the failed delivery. This will appear in the receiving profile’s activity feed along with the recipient activity for the respective flow or campaign the notification was sent from.

The **Bounced push** event includes metadata that shows the error code message (e.g., ExpiredToken) returned by APNs or Firebase. If you are seeing delivery issues, work with your app developer to resolve the error based on the description in the event.

To view the metadata for an event, click on ****Activity details**** for the event on the profile’s activity log.

### Silent push

You are able to see the delivery rate and bounce rate for an individual silent push notifications; however, silent push notifications are excluded from all aggregated performance reporting in Klaviyo. This includes things like mobile push open rates over time, since they do not have opens or conversions.

Please note that you will see different events for silent push than for standard push, namely **Received Silent Push** and **Bounced Silent Push**.

If you are having issues with silent push notifications being delivered on iOS, note that iOS does not guarantee the delivery of silent push notifications. They may not deliver them [based on the device's current state](https://developer.apple.com/library/archive/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23), like battery level and network connection.

### iOS

For iOS push notifications sent through APNs, rejections may occur for at least one of the reasons listed in Apple’s reference for [handling notification responses from APNs](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/handling_notification_responses_from_apns).

|  |  |  |
| --- | --- | --- |
| ****Status code**** | ****APNs error string**** | ****APNs description**** |
| 400 | BadDeviceToken | The specified device token was bad. Verify that the request contains a valid token and that the token matches the environment. |
| 400 | BadTopic | The apns-topic value is invalid. |
| 400 | DeviceTokenNotForTopic | The device token does not match the specified topic. |
| 400 | DuplicateHeaders | One or more headers were repeated. |
| 400 | IdleTimeout | Idle time out. |
| 400 | InvalidPushType | The apns-push-type value is invalid. |
| 400 | PayloadEmpty | The message payload was empty. |
| 403 | BadCertificate | The certificate was bad. |
| 403 | BadCertificateEnvironment | The client certificate was for the wrong environment. |
| 403 | InvalidProviderToken | The provider token is not valid or the token signature could not be verified. |
| 404 | BadPath | The request contained a bad :path value. |
| 405 | MethodNotAllowed | The specified :method was not POST. |
| 410 | ExpiredToken | The device token has expired. |
| 410 | Unregistered | The device token is inactive for the specified topic. |
| 429 | TooManyProviderTokenUpdates | The provider token is being updated too often. |
| 500 | InternalServerError | An internal server error occurred. |
| 503 | ServiceUnavailable | The service is unavailable. |

### Android

For Android push notifications sent through FCM, rejections may occur for at least one of the reasons listed in Google’s reference for [FCM error codes.](https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode)

|  |  |  |
| --- | --- | --- |
| ****Status code**** | ****FCM error string**** | ****FCM description**** |
| 400 | INVALID\_ARGUMENT | Check the format of the registration token you pass to the server. Make sure it matches the registration token the client app receives from registering with Firebase Notifications. Do not truncate or add additional characters. |
| 400 | INVALID\_ARGUMENT | Make sure the message was addressed to a registration token whose package name matches the value passed in the request. |
| 400 | INVALID\_ARGUMENT | Check that the total size of the payload data included in a message does not exceed FCM limits: 4096 bytes for most messages, or 2048 bytes in the case of messages to topics. This includes both the keys and the values. |
| 400 | INVALID\_ARGUMENT | Check that the payload data does not contain a key (such as from, or gcm, or any value prefixed by google) that is used internally by FCM. Note that some words (such as collapse\_key) are also used by FCM but are allowed in the payload, in which case the payload value will be overridden by the FCM value. |
| 400 | INVALID\_ARGUMENT | Check that the value used in ttl is an integer representing a duration in seconds between 0 and 2,419,200 (4 weeks). |
| 400 | INVALID\_ARGUMENT | Check that the provided parameters have the right name and type. |
| 403 | SENDER\_ID\_MISMATCH | The authenticated sender ID is different from the sender ID for the registration token. |
| 404 | UNREGISTERED | App instance was unregistered from FCM. This usually means that the token used is no longer valid and a new one must be used. |
| 429 | QUOTA\_EXCEEDED | Sending limit exceeded for the message target. An extension of type google.rpc.QuotaFailure is returned to specify which quota was exceeded. |
| 500 | INTERNAL | An unknown internal error occurred. |
| 503 | UNAVAILABLE | The server is overloaded. |

You will also see a **Bounced push** event if the recipient is missing or has an invalid push token.

## Best practices

### Collect user consent

In order to send a standard push notification to a profile, you must collect their [explicit consent](https://help.klaviyo.com/hc/en-us/articles/4404203889947) first.

To collect push notification consent, you must provide customers with a permission screen prompt during their first interaction with your mobile app.

It is best practice for your permission screen prompt to include consent language that provides the following information and allows them to opt in or opt out:

- ****What types of notifications your brand sends****
  Include details about the different push notifications your brand plans to send (for example, account changes, account changes, reminders, and special discounts).
- ****Why users should opt in****
  Include information around why a customer should provide permissions (for example, to receive important updates or early access to sales).

Learn more about collecting [push notification consent.](https://help.klaviyo.com/hc/en-us/articles/14781686592283)

### Send relevant notifications

When sending push notification campaigns, it is important to take advantage of Klaviyo’s [segmentation](https://help.klaviyo.com/hc/en-us/articles/115005237908) to send content that is personalized and relevant to your subscribers.

For example, if you know that you have a segment of dedicated repeat customers, you could use push notifications to alert them to new deals or promotions before anyone else.

By ensuring that the content you send customers is relevant to their interests and preferences, you can reduce the likelihood of customers opting out and maximize your ability to reach your customers with push notifications.

### Monitor and analyze performance

It is essential to continually monitor your push notification performance with Klaviyo to quickly identify delivery issues and drops in key [push metrics](https://help.klaviyo.com/hc/en-us/articles/15307358769051).

The best way to do so is to monitor the following push notification events:

- Received push
- Opened push
- Bounced push

You can set up a [multi-metric report](https://help.klaviyo.com/hc/en-us/articles/360046234772) in Klaviyo to monitor how your performance with these events changes over time.