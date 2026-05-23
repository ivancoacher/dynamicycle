---
id: 14750928993307
title: "How to set up Android push notifications"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/14750928993307-How-to-set-up-Android-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:48:41Z"
language: en
---

## You will learn

Learn how to set up push notifications for Android in your Klaviyo account. After you've completed the steps in this article you'll be able to send push notifications in your flows and campaigns.

## Before you begin

There are 4 prerequisites for using push notifications in Klaviyo; you must:

1. Have your own native mobile Android app.
2. [Create a Google service account](https://help.klaviyo.com/hc/en-us/articles/19893982562203).
3. [Generate a Google service authentication key](https://cloud.google.com/iam/docs/keys-create-delete) that will be uploaded to Klaviyo (more details below).
4. Install the [Klaviyo SDK](https://github.com/klaviyo/klaviyo-android-sdk) and set up event tracking and push notifications in your Android app.

## Set up Android push

1. Click your organization name in the lower left-hand corner.
2. Navigate to ****Settings > Push notifications****.
3. On the **Mobile app settings** page, click ****Enable**** next to the Android option.
4. Fill out the required information:

   - ****Package name****
     Add in your [package name](https://support.google.com/admob/answer/9972781?hl=en#:~:text=You%20can%20find%20an%20app's,example.), which you can find in the URL of your listing in the Google Play store. It looks like: **com.yourcompany.yourproject**.
   - ****Google service authentication key****
     Create your [Google service authentication key](https://cloud.google.com/iam/docs/keys-create-delete) and then upload the JSON file to Klaviyo. The JSON file for the key should look like:
     `{ "type": "service_account",
     "project_id": "PROJECT_ID",
     "private_key_id": "KEY_ID",
     "private_key": "-----BEGIN PRIVATE KEY-----\nPRIVATE_KEY\n-----END PRIVATE KEY-----\n",
     "client_email": "SERVICE_ACCOUNT_EMAIL",
     "client_id": "CLIENT_ID",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://accounts.google.com/o/oauth2/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL"}`
5. Click ****Save**** to finish setting up push notifications for your Android app.

![Android push notification setup screen](https://klaviyo.zendesk.com/hc/article_attachments/28717853174171)

## Outcome

You’ll now be able to send push notifications to your Android app users, letting them know about their abandoned carts or special in-app deals.

## Additional resources

- [How to use deep links in push notifications](https://help.klaviyo.com/hc/en-us/articles/14750403974043)
- [How to set up iOS push notifications](https://help.klaviyo.com/hc/en-us/articles/360023213971)

Want to request a feature for Klaviyo push notifications? Fill out this [Google form](https://forms.gle/7iPm6JQ4eKB6H2C4A) to tell us about it!