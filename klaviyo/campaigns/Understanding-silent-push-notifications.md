---
id: 34331926591003
title: "Understanding silent push notifications"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/34331926591003-Understanding-silent-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:57Z"
language: en
---

## You will learn

Learn what silent push notifications are and how to use them in your campaigns and flows, along with specific use cases.

## What are silent push notifications?

Silent push notifications are push notifications that are invisibly sent to a device. They have no content or sound and are not displayed to the user. With silent push, you can trigger content updates or tasks without notifying the user or requiring them to update your app. Common use cases include:

- Displaying new content in your app
- Personalizing the app interface
- Downloading information from a server

To trigger app tasks via silent push, utilize [key-value pairs](https://help.klaviyo.com/hc/en-us/articles/34331971195675). Key-value pairs are custom data that can be included with push notifications, both silent and standard.

## How to use silent push notifications

Silent push notifications, like standard push notifications, can be used in both campaigns and flows:

- Learn how to [send a push notification campaign](https://help.klaviyo.com/hc/en-us/articles/360006653972)
- Learn how to [add a push notification to a flow](https://help.klaviyo.com/hc/en-us/articles/12932504108571)

First, make sure you’ve [set up push notifications](https://help.klaviyo.com/hc/en-us/articles/360023213971) in your Klaviyo account.

Sending a silent push involves setting the push type to **Silent** and then configurating any key-value pairs (found in the **Custom data** setting on the **Behaviors** tab).

![](https://klaviyo.zendesk.com/hc/article_attachments/36082188321947)

Key-value pairs enable many use cases for silent push notifications but are not required.

In order to use key-value pairs, your app must be set up to recognize keys and respond to their values, so be sure to work with your app developer to ensure your app is built to support your use cases.

## Example use cases

The benefit of silent push notifications (along with key-value pairs) is that you can use them in a variety of use cases.

You can send a silent push notification to personalize app content based on the recipient’s attributes, such as profile properties stored in Klaviyo. For example, if you have an ecommerce app, you could use silent push and key-value pairs to display a customer’s updated rewards points in their app after they’ve made a purchase.

## iOS-specific guidance

If you are having issues with silent push notifications being delivered, note that iOS does not guarantee the delivery of silent push notifications. They may not deliver them [based on the device's current state](https://developer.apple.com/library/archive/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23), like battery level and network connection.

## Do silent push notifications affect Klaviyo performance reporting?

You are able to see the delivery rate and bounce rate for an individual silent push notifications; however, silent push notifications are excluded from all aggregated performance reporting in Klaviyo. This includes things like mobile push open rates over time, since they do not have opens or conversions.

Please note that you will see different events for silent push than for standard push, namely **Received Silent Push** and **Bounced Silent Push**.