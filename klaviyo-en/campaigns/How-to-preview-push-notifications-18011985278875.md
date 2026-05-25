---
id: "18011985278875"
title: "How to preview push notifications"
source_url: "https://help.klaviyo.com/hc/en-us/articles/18011985278875-How-to-preview-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:09Z"
language: "en"
---
## You will learn

Learn how to send a preview of your push notifications to a device. By sending a preview, you can make sure your push notification looks exactly as you expect before your customers ever see it.

For testing on iOS, you must use v2.2.0 or higher of the Klaviyo Swift SDK in your app for this feature to work. For both iOS and Android, you may send preview notifications to apps in production or sandbox environments.

## Before you begin

Before you preview a notification, you need to:

- Integrate the Klaviyo SDK into your [iOS](https://github.com/klaviyo/klaviyo-swift-sdk) or [Android](https://github.com/klaviyo/klaviyo-android-sdk) mobile app.
- Configure [iOS](https://help.klaviyo.com/hc/en-us/articles/360023213971) or [Android](https://help.klaviyo.com/hc/en-us/articles/14750928993307) push notifications in your Klaviyo account.
- Create a profile in Klaviyo through the app on your test device.
- Opt in to push notifications on your test device.
- Copy the push token for your device (which you can find on your profile).

Want to request a feature for Klaviyo push notifications? Fill out this [Google form](https://forms.gle/7iPm6JQ4eKB6H2C4A) to tell us about it!

## Preview push notifications

Previewing a push notification is simple:

1. Create a campaign or flow message.
2. In the upper right corner of the push editor, click ****Preview & text****.
3. Paste in your push token.
4. Select ****Send test****.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627734554139)

You can send up to 100 preview push notifications in a 24-hour period.