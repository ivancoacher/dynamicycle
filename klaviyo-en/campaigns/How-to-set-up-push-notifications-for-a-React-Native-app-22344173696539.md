---
id: "22344173696539"
title: "How to set up push notifications for a React Native app"
source_url: "https://help.klaviyo.com/hc/en-us/articles/22344173696539-How-to-set-up-push-notifications-for-a-React-Native-app"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:27Z"
language: "en"
---
## You will learn

Learn about using Klaviyo’s React Native SDK to send mobile push notifications.

****What is an SDK?****

An SDK provides all the necessary tools, libraries, and programs so that your app can talk to a third-party software (e.g., like a mobile push provider). The SDK framework must match the framework used to build your app.

## Benefits of React Native SDK

The React Native SDK allows you to connect Klaviyo to apps using React Native.

React Native is a framework that allows you to create mobile apps that work on both iOS and Android. It’s written in JavaScript and allows you to utilize a single code base for multiple platforms. React Native apps look like any other apps.

React Native’s hybrid framework means developers can code an app only once and more easily maintain it for both iOS and Android.

React Native is different from native apps, which are apps written in a language specific to iOS (Swift or Objective-C) or Android (Kotlin or Java). Having native apps for iOS and Android is essentially double the effort of using React Native because you have to build and maintain 2 distinct apps.

## Requirements for setup

Before you can set up push notifications for your React Native app, you must:

- Have your own React Native app for iOS, Android, or both.
- Install the [React Native SDK](https://github.com/klaviyo/klaviyo-react-native-sdk?tab=readme-ov-file).

  We also recommend the following:
- Set up profile identification in your app. We recommend you create profiles for app users with a profile identifier (email address, phone number, or external ID), especially if you want to personalize push notifications. Otherwise, all profiles will be anonymous in Klaviyo.
- Configure event tracking in your app.

Note that you will also need to set up parts of the native [iOS SDK](https://github.com/klaviyo/klaviyo-swift-sdk) and [Android SDK](https://github.com/klaviyo/klaviyo-android-sdk) where applicable.

## Set up push notifications

Once you fulfill the requirements above, you have to connect Klaviyo to your iOS and Android apps.

For instructions on how to do so, see our setup guides for:

- [iOS](https://help.klaviyo.com/hc/en-us/articles/360023213971)
- [Android](https://help.klaviyo.com/hc/en-us/articles/14750928993307)

## Test push notifications

It’s important to test your push notifications before you start sending to customers. Here are a few suggestions of things to test:

- Your app can handle push notifications from Klaviyo.
- You can display an image or deep link to a screen in your app through a push notification (if you intend to use these features).
- Klaviyo is properly creating profiles and receiving information from your app.

Make sure you have notifications for your app turned on before testing.

The simplest way to test is by [sending a preview](https://help.klaviyo.com/hc/en-us/articles/18011985278875) from either a campaign or flow.