---
id: "34331971195675"
title: "Understanding key-value pairs"
source_url: "https://help.klaviyo.com/hc/en-us/articles/34331971195675-Understanding-key-value-pairs"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:58Z"
language: "en"
---
## You will learn

Learn what key-value pairs are and how to use them with both standard and silent push notifications. Key-value pairs are custom data included with push notifications that allow you to trigger app behaviors, tag messages, customize notifications, and more.

## What are key-value pairs?

Key-value pairs are custom data that can be included with push notifications, both standard (those that display to users) and silent (those that are invisible to users).

With both silent and standard notifications, they can be used to update app content, trigger background tasks, or to tag messages for reporting purposes.

With standard push, they can also be used to build and populate custom push templates.

## How to use key-value pairs

In order to use key-value pairs, your app must be set up to recognize keys and respond to their values, so be sure to work with your app developer to ensure your app is built to support your use cases. Additionally, make sure you’ve [set up push notifications](https://help.klaviyo.com/hc/en-us/articles/360023213971) in your Klaviyo account.

You can find them in the **Behaviors** tab when creating a push notification. To use them, toggle on ****Custom data****, then add keys and values. You can add up to 10 key-value pairs per push notification.

![](https://klaviyo.zendesk.com/hc/article_attachments/36082155700123)

Let’s look at an example for an ecommerce app:

- We want to update a customer’s reward points displayed in our app after they make an online purchase. We’ll do this by sending a silent push with a rewards points profile property as a key-value pair.
- We already have a **Thank you** flow triggered by a **Placed Order** event. We add a silent push to the end of this flow to update the rewards points value displayed in our app.
- The silent push includes a key-value pair where the **Key** equals **rewardspoints** and the **Value** is set to **{{ person.rewardspoints }}**. The name of the Klaviyo profile property where we store these points is called **rewardspoints**, and our app is configured correctly to update based on this key-value pair.
- In this example, we made sure that the **rewardspoints** value was updated in Klaviyo before it was sent to our app via this flow, so that it reflects accurately.

## Use cases

There are many use cases for key-value pairs, including to:

- ****Personalize app content****
  You can send a silent push notification to personalize app content based on the recipient’s attributes (like the rewards points example above).
- ****Create tags for reporting****
  You can include key-value pairs in push notifications (standard or silent) to “tag” messages and then pull data for any messages with specific tags to aggregate. For example, these tags could be UTM parameters.
- ****Build custom push templates****
  You can define the font size and color for your push notification body or set a custom sound that will play when the push notification is delivered. Accounts can also display live data, such as the location of a delivery or a countdown until an offer expires, in their notification.

We recommend working with your app developer to build support for your specific use cases.