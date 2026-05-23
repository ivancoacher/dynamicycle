---
id: 35283141315099
title: "Deliverability vs. delivery for each channel"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/35283141315099-Deliverability-vs-delivery-for-each-channel"
section: "Getting started with email deliverability"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:41Z"
language: en
---

Learn the difference between deliverability and delivery as well what they mean for email, SMS, and mobile push.

Please note that deliverability varies significantly by channel, so the best practices you apply to email may not have any impact on SMS.

## Deliverability vs. delivery

You may hear “deliverability” and “delivery” used interchangeably; however, there is a certain nuance between them.

- ****Delivery****
  Whether your message landed. Delivery is more straightforward than deliverability, and a failed delivery is typically due to a technical limitation (like a server being down).
- ****Deliverability****How likely your message is to land. It’s affected by things like recipient engagement and is much more nuanced than delivery.

## Email

Generally, deliverability influences your email performance more than delivery does. In fact, compared to other channels, the concept of deliverability is most strongly related to email.

Below, we provide the highlights of email delivery and deliverability. For more information, please see our [dedicated article on email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008).

### Deliverability

Deliverability for email revolves around your [sender reputation](https://help.klaviyo.com/hc/en-us/articles/115005247008), or the trustworthiness of your brand as an email sender. Inbox providers determine your sender reputation based on multiple differently weighted factors, and consider this when deciding where to place emails in a customer’s inbox (i.e., the main inbox, promotions, or spam).

Recipient engagement plays a huge role in your sender reputation and overall deliverability. If your recipients consistently interact (e.g., open, click, etc.) with your messages, it signals to inbox providers that you are a good sender. With a strong sender reputation, your messages are more likely to place better in the inbox.

The content of your email may also affect deliverability. A few factors that can hurt deliverability are using:

- Spammy subject lines (e.g., “free money”)
- A generic sender domain (e.g., @google.com or @yahoo.com) rather one specific to your business (e.g., @klaviyo.com)
- Emails comprised only of images (i.e., when the majority of the text in an email is contained within an image)

### Delivery

For email, a failed delivery is called a “bounce.” There are 2 types of bounces:

- ****Soft bounce****Temporary issue, such as an email inbox being too full or when an email server goes down.
- ****Hard bounce****Permanent issue, such as when the email address is wrong.

## SMS

Both delivery and deliverability impact SMS; however, the concept of deliverability is different for SMS than it is for email. Learn more about [SMS deliverability and how text messages are delivered](https://help.klaviyo.com/hc/en-us/articles/1260806260849).

### Deliverability

For SMS, deliverability answers the question: did wireless carriers filter my message? Ultimately, wireless carriers have full discretion about whether or not to deliver your text message. They also may not tell you if a message is filtered.

Factors that can influence whether or not carriers filter a message include:

- ****Sending number****Short codes are more likely to be trusted (i.e., not filtered) than any other number type due to their vigorous verification process.
- ****Message content****
  Carriers look for instances of possible fraudulent or prohibited content within an SMS message, both in the actual wording and on any website that text message links to.
- ****Spam complaints****
  After someone marks your messages as spam, that person is probably not going to see any future message from you. If this happens frequently, carriers may decide to filter all messages from your number.
- ****Saved contact****
  If someone saves your brand as a contact in their phone, it’s more unlikely that carriers will filter your messages to that recipient.
- [****Quiet hours****](https://help.klaviyo.com/hc/en-us/articles/4408737146651)Most countries have regulations about what time of day you can send; however, in France, carriers simply refuse to deliver marketing messages during quiet hours.

Additionally, Android devices have a spam folder. It may be that rather than the message not being delivered at all, it instead goes into the spam folder.

### Delivery

Most of the time, wireless carriers provide a delivery receipt (DLR), also called delivery report, within minutes of a text message failing or succeeding.

When an SMS isn’t delivered, it’s called a “failure” rather than a “bounce.” Like with email, delivery issues can be either temporary or permanent, but they are all grouped together under one umbrella.

Common SMS failure reasons include:

- The phone number is incorrect.
- The cellphone doesn’t have service.
- The wireless carrier’s network is down.

For a small percentage of messages, carriers can be delayed in issuing DLRs (or never provide them at all). You can know whether Klaviyo received a delivery report by looking at the **Received SMS** or **Received Automated Response SMS** metric. The **Carrier Delivery Status** for these metrics shows as either:

- **Delivered**, when carriers explicitly confirmed that an SMS was delivered.
- **Sent**, if carriers did not confirm delivery nor issue a failure.

## Mobile push notifications

Unlike SMS and email, mobile push notifications don’t have a concept of deliverability: either the push is delivered or it’s not. There’s no third-party filtering, evaluating engagement, or checking message content.

### Delivery

For mobile push notifications, the most common reasons a push won’t be delivered are:

- The recipient unsubscribed.
- The person deleted the app.
- There’s a server issue, either with Apple Push Notification Service (APNs) for iOS or Firebase Cloud Messaging (FCM) for Android.

Learn more [about push notification delivery](https://help.klaviyo.com/hc/en-us/articles/15594685536539).

## Additional resources

- Learn more about delivery and deliverability for [email](https://help.klaviyo.com/hc/en-us/articles/115005247008), [SMS](https://help.klaviyo.com/hc/en-us/articles/1260806260849), or [mobile push](https://help.klaviyo.com/hc/en-us/articles/15594685536539).
- See our [deliverability glossary](https://help.klaviyo.com/hc/en-us/articles/360039295051).