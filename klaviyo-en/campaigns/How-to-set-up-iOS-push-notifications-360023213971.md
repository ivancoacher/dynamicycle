---
id: "360023213971"
title: "How to set up iOS push notifications"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360023213971-How-to-set-up-iOS-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:50:07Z"
language: "en"
---
You must be an Owner or Admin to set up mobile push notifications

## You will learn

Learn how to set up push notifications in your Klaviyo account. After you've completed the steps in this article you'll be able to send push notifications in your flows and campaigns.

## Before you begin

There are 3 prerequisites for using push notifications in Klaviyo:

1. You must have your own native mobile iOS app.
2. You must generate an APNs authentication key from Apple that will be uploaded to Klaviyo (more details below).
3. You must install the [Klaviyo SDK](https://github.com/klaviyo/klaviyo-swift-sdk) and set up event tracking and push notifications in your iOS app.

## Set up push notifications in Klaviyo

1. Click your organization name in the bottom left corner.
2. Navigate to ****Settings >**** ****Push Notifications****.
3. Click ****Enable**** in the iOS section.
   ![ios push notifications can be turned on by clicking enable button](https://klaviyo.zendesk.com/hc/article_attachments/28717387111323)
4. Fill out the required information.
   Note that you need the correct role to access your APNs Notification Key and your Key ID. You can [review Apple's roles and permissions here](https://developer.apple.com/support/roles/).

   1. Log into your [App Store Connect](https://appstoreconnect.apple.com/apps) or [Apple Developer](https://developer.apple.com/account) account.
   2. Click ****My Apps****.
   3. Select your app and your Bundle ID is available on the ****App information**** tab.
      Note that the bundle ID is case sensitive and should be similar to the following:
      **com.YOUR\_APP\_NAME.**
      ![Required information to set up iOS push notifications](https://klaviyo.zendesk.com/hc/article_attachments/28717380841243)

   - ****APNs Authentication Key****
     If you don't already have it, [create an APNs authentication key](https://developer.apple.com/account/ios/authkey/create). Be sure to set the key type to **APNs**.
     After creating your key, download the .p8 file, and upload it to your Klaviyo account.
   - ****Key ID****
     To find your key ID, [navigate to your list of keys](https://developer.apple.com/account/ios/authkey/). Click your key to expand the details, and copy the key ID.
   - ****Team ID****
     Find your [team ID here](https://developer.apple.com/account/#/membership).
   - ****Bundle ID****
     To find your Bundle ID:
5. After filling out all of the required information, click ****Setup iOS Push****.

A green success callout confirms that your app has been connected to your Klaviyo account.

## Additional resources

- Also have an Android app? Learn [how to set up push for Android](https://help.klaviyo.com/hc/en-us/articles/14750928993307).
- Learn how to [use push notifications for campaigns](https://help.klaviyo.com/hc/en-us/articles/360006653972).
- Check out how to [use deep links in push notifications](https://help.klaviyo.com/hc/en-us/articles/14750403974043).

Want to request a feature for Klaviyo push notifications? Fill out this [Google form](https://forms.gle/7iPm6JQ4eKB6H2C4A) to tell us about it!