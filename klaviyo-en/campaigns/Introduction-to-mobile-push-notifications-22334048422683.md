---
id: "22334048422683"
title: "Introduction to mobile push notifications"
source_url: "https://help.klaviyo.com/hc/en-us/articles/22334048422683-Introduction-to-mobile-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:26Z"
language: "en"
---
## You will learn

Get familiar with mobile push notifications, including what they are, what they look like, and what information you need to start sending.

## What are push notifications?

First, let’s clarify what we mean by push notifications, as there are actually 2 types:

1. ****Mobile push notifications**** are messages that are sent by a mobile app to users and that typically appear on the lock screen of a mobile device.
2. ****Web push notifications****, also called “browser notifications.” These are sent by a website to a browser and can appear even when that website is not open. Web push notifications are available on desktop and mobile devices. Klaviyo does not support web push at this time, although you can [trigger web notifications via API calls](https://medium.com/klaviyo-developers/solution-recipe-25-how-to-trigger-web-push-notifications-through-klaviyo-14a8361eb9f4).

In both cases, the notifications appear as clickable messages that take the user directly to an app or website.

These 2 types are often talked about together; however, they are actually quite different from each other in terms of setup, requirements, and even how they look.

Here, we only focus on 1 type of push notification: mobile.

### How are mobile push notifications used?

Mobile push notifications are highly effective at driving people into your app. Just like with SMS, app users almost always see push notifications. The difference is that push notifications are:

- Often seen as less sales-driven by recipients
- Helpful in a wider range of use cases
- Usually less expensive to send

  Mobile push notifications are great for:
- Reminders (e.g., to exercise, practice a language, watch a show)
- App-only deals or collections
- Time-sensitive alerts
- Product alerts
- Asks for information (e.g. “fill out your profile”)

Someone must have app notifications turned on in order to receive push notifications.

![Example of a opt-in message for an app](https://klaviyo.zendesk.com/hc/article_attachments/28720762464795)

### How often should I send mobile push notifications?

The answer depends on how often your app users want notifications. Here are a few examples:

- Health, wellness, or educational brands might send daily reminders (e.g., to take medicine, work out, study, etc.).
- For apparel and accessory companies, it can depend on how often customers are likely to shop:
  - Weekly or bi-weekly for frequent and high-value shoppers.
  - Monthly to all other customers.
  - Most might send weekly or bi-weekly.
  - Luxury brands may split their sending by audience.
- Furniture stores may send out push notifications less frequently: for new product launches or the holidays, for example.

Generally, though, don’t send more than 3–5 push notifications per week unless you see high engagement from customers. Sending more than that can overload subscribers and cause them to unsubscribe.

## Structure of a push notification

Let’s examine the anatomy of a push notification when it is delivered. Below is an example Android push notification, although iOS notifications will look similar.

From left to right:

1. App logo
2. Title
3. Timestamp
4. Message body
5. [Rich media](https://help.klaviyo.com/hc/en-us/articles/16917302437275)

   - Android: image only
   - iOS: image or GIF
6. Arrow to expand

![Example of a push notification as it appears on an Android device's lock screen](https://klaviyo.zendesk.com/hc/article_attachments/28720762467739)

Note that the look of notification changes based on whether there’s an image or GIF attached, how long the message is, and the recipient’s device.

### Character limit

As a general rule, you want to keep your push notifications clear and concise.

If you exceed the character limit, your mobile push notification may get cut off, and the recipient won't see the full message.

To avoid this, you want to adhere to the following character limits. However, keep in mind that the limits may vary by:

- The phone's software version (e.g., older versions may allow for more characters than newer ones, or vice versa).
- The message content:
  - Emojis take up more space than regular characters
  - When you include rich media, push notifications tend to display fewer characters.

|  |  |  |
| --- | --- | --- |
|  | ****Title**** | ****Description**** |
| Android | 65 | 240 |
| iOS | 178 | |

## What you need to send push notifications

The first thing you need for push notification marketing is an app.

If you don’t have an app yet, we recommend [contacting a developer](https://connect.klaviyo.com/) or other third party to create one for you.

A developer is usually required to set up push notifications as well as your app. To connect your app with a push provider, someone must use an SDK (recommended) or create a custom integration.

****What’s an SDK?****

SDK stands for a software development kit, and it is a set of tools, libraries, and programs used to develop apps for a specific platform or service. Basically, it’s a developer’s toolkit for connecting an app with any other platform (e.g., Klaviyo).

### Decide what features you want

An app must be able to actually send out a push notification. The most basic requirement is the title and message body of the push. However, there are other, optional features that you may need to work with your app developer to include:

- ****Rich media****
  Allows you to include images and (for iOS) GIFs in your push notifications.
- ****Deep linking****
  Deep linking is the ability to link directly to a page in your app. Without a deep link, all your push notifications will take recipients to the app’s home screen.

  For deep linking, your developer needs to give you the URI scheme for your app. This is custom to your app, but your developer can help you get these links.

  Further, you may want to consider what information you want to use in your push notifications. Your developer will need to include these when setting up the connection between your app and push provider. For instance, some helpful custom metrics are:
- **Opened app**
- **Completed profile**
- **Set store location**

### Provide key information to your push provider

After everything is set up in your app, you’ll have to connect it to your push provider.

To do this, you must provide certain information about your app. While the requirements may slightly change depending on the provider, the table below shows what you need in Klaviyo, and other providers should be similar.

You may need to work with your app developer to get this information.

|  |  |
| --- | --- |
| ****Platform**** | ****Required information**** |
| [Android](https://help.klaviyo.com/hc/en-us/articles/14750928993307) | Package name, Google service authentication key (JSON private key file) |
| [iOS](https://help.klaviyo.com/hc/en-us/articles/360023213971) | APNs authentication key (via a .p8 certificate), key ID, team ID, bundle ID |

Note that if your app is listed in both the Apple App and Google Play stores, you’ll have to set each up individually.

### Test via your push token

****What’s a push token?****

A push token is a unique anonymous ID to identify a certain app on a certain device, and it’s generated by the Apple Push Notification Service (iOS) or Firebase Cloud Messaging (Android). Your token for that app and device combination will be the same no matter which push platform you use.

Once you connect your app and push platform, it’s important to test that:

- Your app can send push notifications.
- A push notification can deep link or include media (if you intend to use these features).
- Your push provider is properly receiving information from your app.

See the sections below for details on what to do.

#### Opt in to push

1. Open your app from your personal device.
2. Opt in to push notifications.
   If you’re not automatically prompted to enable push, go into your app settings and turn notifications on.

#### Create a list to test your push notifications

1. Go to your push provider. Here, we use Klaviyo as an example.
2. Create a list to preview your push notifications by:

   - Navigate to ****Audience > Lists & segments > Create new > Create list****.
   - Name the list (e.g., “Push preview”) and select ****Create list****.
3. Find your push token. In Klaviyo, navigate to ****Audience > Profiles**** and either search for your profile, or review the recently updated profiles.
   ![Searching for recent push profiles in an accpimt](https://klaviyo.zendesk.com/hc/article_attachments/28720762463259)
4. Click into that profile.
5. Go to the ****Lists and segments**** tab within the profile and click ****Add to list****.
   ![List and segments tab within a profile, showing the option to add that profile to a list](https://klaviyo.zendesk.com/hc/article_attachments/28720762474395)
6. Find the list you created and then select ****Add to list****.

If you have both an Android and iOS app, we recommend adding a push token for each type of device to the preview list. This will allow you to see how your push notifications appear on both systems, as they tend to look slightly different from each other.

#### Perform your tests and checks

We recommend [performing several separate tests](https://help.klaviyo.com/hc/en-us/articles/18011985278875):

1. Send a simple push notification (i.e., content only).
2. Add an image to test rich push.
3. Include a deep link.

Also, go into your app and click around to test your custom metrics (e.g., if you added a custom metric for **Completed profile**, fill out your profile in your app). Then, go back to your push provider to see if these metrics and events are being logged properly.

## Additional resources

- [Push notification glossary](https://help.klaviyo.com/hc/en-us/articles/21997060301979)
- [Basics: push notification best practices](https://help.klaviyo.com/hc/en-us/articles/16853367294747)
- Getting set up with mobile push on [Android](https://help.klaviyo.com/hc/en-us/articles/14750928993307) or [iOS](https://help.klaviyo.com/hc/en-us/articles/360023213971).