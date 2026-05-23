---
id: 28753430257435
title: "Understanding mobile push notification performance"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/28753430257435-Understanding-mobile-push-notification-performance"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:47Z"
language: en
---

## You will learn

Learn about the key performance indicators (KPIs) for mobile push, including how they’re defined, what they indicate, and what to do to improve them.

## 3 KPIs for mobile push

There are 3 KPIs for mobile push notifications:

1. Delivery rate
2. Open rate
3. Conversion rate

Each channel is unique, so don’t expect your mobile push KPIs to be the same as those for any other channel.

For instance, many marketers see lower open rates for mobile push than for email and think their push marketing efforts are performing poorly. However, lower open rates for push are expected because they work differently than opens for other channels.

### Delivery rate

Push delivery rate is calculated as: the number of messages that were delivered divided by the number that were sent.

![push delivery rate definition](https://klaviyo.zendesk.com/hc/article_attachments/28753430238107)

Delivery rate tells you how many messages are reaching your subscribers.

Push is different from email and SMS because it doesn’t have the concepts of deliverability, filtering, or sender reputation. Instead, a push’s delivery only looks at consent and whether the recipient’s phone received the notification.

Typically, you’ll look at delivery rate to understand if:

- Your messages are being delivered (or if there’s a problem between your app and mobile push provider)
- There's any sudden dropoff in subscribers or deliveries
- A specific segment of your audience didn’t receive a notification.

While a high delivery rate is always good to have, this metric alone doesn’t provide a comprehensive look at your mobile push performance. If you want to know how well recipients are responding to your push marketing efforts, consider looking at your push open and conversion rates.

****What affects delivery rate?****

Unlike with email or SMS, push doesn’t have a concept of sender reputation or deliverability: either the notification is delivered or it’s not.

The main factors that affect a push’s delivery rate are if:

- The recipient has removed consent for push notifications or uninstalled the app.
- Your app is properly connected to Klaviyo (or other push marketing provider).
- The recipient’s phone is temporarily unavailable (e.g., turned off, not connected to the internet, etc.)

Delivery rate is not a perfect measurement. Phones and other mobile devices don’t always report when a push notification was delivered or not. For instance, Klaviyo shows messages as “sent” when the notification is successfully passed to Apple or Google’s messaging service; however, it does not guarantee that these services delivered the notification to all intended devices.

****What if I have a low deliverability rate?****

If your delivery rate is low, it could indicate that there is an issue with how your app and mobile push provider are connected, or that your subscribers are deleting your app or removing consent.

As next steps, check on your delivery rate for multiple campaigns or flows.

- If the delivery rate was low only once (and not consistently), it may have been a temporary issue (such as with a server).
- If it is consistently low, investigate how many times your messages are failing:
  - Review the recipient activity, particularly the ****Bounced**** tab, and address the reason why that specific campaign or flow message wasn’t delivered.
  - Consider excluding recipients who frequently bounce by:

    - If your delivery rate increases, your subscribers may simply experience more temporary issues with their phones. Things to try are:
      - Sending to this group at different times of the day or week.
      - Asking this group about their notification preferences.
      - Re-sending campaigns to anyone that didn’t receive a notification.
    - If your delivery rate is still low, see to the next bullet point.

    1. Creating a segment of people where a mobile push notification bounced 2 or more times.
    2. Excluding this segment in your next campaign.
    3. Reviewing your delivery rate once this segment is excluded.
  - Work with a developer to investigate why notifications are failing.

### Open rate

Push open rate is calculated as: the number of profiles that opened a message divided by the number of profiles that received the message.

For push, an open occurs when a profile taps on the notification and “opens” the app.

![Push open rate definition](https://klaviyo.zendesk.com/hc/article_attachments/28753454760859)

Open rate for push often seems low, especially when compared to email, because they show more intent to convert than opens for other channels. In fact, a push open is more similar to an email click than an email open.

Open rate tells you how recipients felt about the content of your push notification. You can look at open rate to find out:

- What type of notification performs best (sale alert, product drop, etc.)
- What is the best audience to send to, in general and for specific types of content
- If your message tone and writing is engaging recipients.

Learn tips for [improving push notification opens](https://help.klaviyo.com/hc/en-us/articles/13769219837083).

****Why is my open rate so low?****

Open rate may seem low, but it’s important to remember that an open for push is tracked differently than it is for email.

- Email open: recipient opens the email to see the full message.
- Push open: recipient sees the full message and then taps the message to open the app.

![Showing the difference between an email and a push open](https://klaviyo.zendesk.com/hc/article_attachments/28753454765467)

****What’s the difference between opens for Android and iOS?****

The main difference between Android and iOS push notifications is how they are displayed:

- Android: notifications remain visible on the lock screen until a user opens or dismisses the notification.
- iOS: notifications display on the lock screen until a user unlocks their phone. Then notifications display only in the notification center until a user opens or dismisses the message.

In general, this difference doesn’t significantly influence your open rates.

### Conversion rate

Push conversion rate is calculated as: the number of profiles that converted divided by the number of profiles that received the notification.

![push conversion rate definition](https://klaviyo.zendesk.com/hc/article_attachments/28753454766491)

Conversion rate is the most important KPI for every marketing channel. It answers the question: “Are people taking the desired action?”

Many times, the desired action is a purchase, but depending on the scenario, you may want a different event. For instance, a conversion can be viewing a product, starting checkout, or providing certain information.

Tips for increasing conversions include:

- Personalizing your push notifications by customizing the content to specific segments (e.g., favorite color, viewing a product)
- Making sure the call-to-action sets the right expectations for people who open the message.
- Checking that recipients are landing on the right page of your app.
  - If you haven’t already, we suggest contacting your developer so you can use [deep linking](https://help.klaviyo.com/hc/en-us/articles/14750403974043).
- Using [browse abandonment](https://help.klaviyo.com/hc/en-us/articles/115002775252) or [cart abandonment](https://help.klaviyo.com/hc/en-us/articles/115002779411) flows