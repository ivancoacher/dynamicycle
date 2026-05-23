---
id: 20582984332059
title: "Frequently asked questions about push profiles and tokens"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/20582984332059-Frequently-asked-questions-about-push-profiles-and-tokens"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:21Z"
language: en
---

## You will learn

Learn the answers to common questions surrounding push profiles and tokens.

In the sections below, we answer the following questions:

- Push profiles
  - [How does Klaviyo identify mobile app profiles?](#h_01HFSRKVWE24ESV2Z19GH1CJVG)
  - [Why do I have anonymous profiles (i.e., profiles without an email or phone number)?](#h_01HFSRKVWERVC37FK8HJA7VBDZ)
  - [Why do I see a lot of](#h_01HFSRKVWE8GMGAW0G5PA0TRPA) [**Merged Profile**](#h_01HFSRKVWE8GMGAW0G5PA0TRPA) [events on a profile?](#h_01HFSRKVWE8GMGAW0G5PA0TRPA)
- Push tokens/consent
  - [Why was a push token removed from a profile?](#h_01HFSRKVWENNMPR6JGCZD7E0YX)
  - [When are new push tokens generated?](#h_01HFSRKVWEDBKK3V5HGSXN7H0T)

## FAQs for push profiles

### How does Klaviyo identify mobile app profiles?

Installing the Klaviyo SDK in a mobile app allows Klaviyo to identify profiles and track events, just as adding [Klaviyo’s](https://help.klaviyo.com/hc/en-us/articles/360020342232) [**Active on Site**](https://help.klaviyo.com/hc/en-us/articles/360020342232) [tracking snippet](https://help.klaviyo.com/hc/en-us/articles/360020342232) to a website does.

Once the SDK is installed, Klaviyo begins creating or updating profiles for people using your app.

When a new user enters your app, Klaviyo checks if there’s any identifying information (e.g., an email). If so, Klaviyo looks for any existing profile that includes the same information.

If Klaviyo finds a profile with a matching identifier, the app profile merges with the existing profile.

If there’s no profile with that identifier (or if the user is not identified in the app), Klaviyo creates an anonymous profile.

Your app developer must have set up your app to create profiles in Klaviyo. If no profiles are being created (either identified or anonymous), you should reach out to your app developer.

### Why do I have anonymous profiles (i.e., profiles without an email or phone number)?

Profiles that don’t have an email or phone number are known as “anonymous profiles.”

These profiles are created when the following 3 things all occur:

- A user opens an app for the first time.
- Klaviyo recognizes that it is a new user or device.
- No other unique identifier (email, phone number, or external ID) is provided for the user.

Note that anonymous profiles can be created even when a user does not consent for push notifications so that you are able to track user activity in your app.

### Why do I see a lot of “Merged Profile“ events for the profile?

You will see a merged profile event if Klaviyo matches an anonymous profile to one with an email, phone number, or external ID.

Multiple merged profile events may occur if a user downloads an app on multiple devices. In this case, Klaviyo creates an anonymous ID for each device. However, the profiles merge if Klaviyo later identifies the user on each device via an email or phone number.

## FAQs for push tokens/consent

### Why was a push token removed from a profile?

Klaviyo removes push tokens from profiles when iOS or Android notifies Klaviyo that the tokens are not valid.

The process of how a token is removed is as follows:

1. You try to send a push notification (via a flow or campaign) to a token.
2. Android or iOS sends a response saying the token is invalid.
3. Klaviyo removes the push token.

Note that a user may have multiple push tokens on their profile because they have enabled push notifications on multiple devices (e.g., their phone and tablet). In this case, only the invalid token is removed, and you can continue to send push notifications to the user’s other devices.

If the token is the only one on the profile, the profile will be skipped from future push notifications.

### When are new push tokens generated?

Android and iOS determine when a new token is generated. Klaviyo simply accepts the token that will be passed via FCM or APNs. Typically, Android and iOS generate new tokens when a person downloads an app on a device, whether for the first time or after deleting the app and then redownloading it.