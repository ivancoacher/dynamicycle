---
id: 16917302437275
title: "Understanding rich push notifications"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16917302437275-Understanding-rich-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:06Z"
language: en
---

## You will learn

Learn about rich push notifications in Klaviyo. Rich push notifications are available for both campaigns and flows.

****What are rich push notifications?****

In contrast to standard text-only push notifications, rich push notifications include multimedia content, such as images, GIFs, and videos.

****Why send rich push notifications?****

Including rich content (e.g., images) in your push notifications is a great way to engage recipients and encourage them to open your app. For instance, you can show recipients that a product on their wish list is now discounted or send a fun graphic to announce major news.

## Before you begin

You must do the following before trying to use rich push notifications:

1. Set up push for iOS, Android, or both in Klaviyo.
2. For iOS only, talk with your app developer to ensure your app can send rich notifications. You may need additional setup on the app side, such as a service extension.

Want to request a feature for Klaviyo push notifications? Fill out this [Google form](https://forms.gle/7iPm6JQ4eKB6H2C4A) to tell us about it!

## Android and iOS availability

Images, static and dynamic, are available for both iOS and Android apps.

However, GIFs and videos are only available to send to iOS apps, as Android does not currently support GIFs. If you try to send a GIF to an Android device, it will appear as a static image of the first frame of the GIF. If you try to send a video to an Android device, the notification will send as text-only.

## Number of media per push

Each push notification can have 1 piece of multimedia content (e.g., an image or GIF).

Thus, you can’t send an image to Android users and a GIF to iOS users.

![Example push notification when the image is expanded](https://klaviyo.zendesk.com/hc/article_attachments/28716333130523)

## File types

Klaviyo supports the following image file types:

- JPEG
- PNG
- GIF (iOS only)
- MP4 (iOS only)

## File size

Image/GIF must be sized 1 MB or smaller. Videos must be 10 MB or smaller.

If you try to add a file that is larger than the limit, you’ll receive an error message.

Note that while certain devices can support larger file sizes, using a smaller-sized file is a best practice. A smaller file size helps ensure that the user is able to consistently see your media, even when their internet connection isn’t strong.

## Best practices for media attachments

Images and GIFs appear in 2 ways: the collapsed view (left) and expandable view (right). In the expanded view, your attached media automatically adjusts to fit the phone, scaling to the width of the screen.

When you add a GIF or video, it will not play until the recipient expands the notification. In the collapsed view, the video or GIF will appear as a static image of the first frame.

|  |  |
| --- | --- |
| ![Example push notification, showing image in the collapsed state (as the icon)](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/9b57c787dc7743bbfacd8229101616d8e4506271-474x328.png) | ![Example push notification, showing image when it's expanded](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/3a5c194f5e1fba49ba2aacfd0691e9ab52ff0366-974x1008.jpg) |

As a best practice, use media with a 2:1 ratio size. The 2:1 ratio is required in some cases, and looks good regardless of whether the recipient has an iOS or Android device. Images that are too tall or wide may appear distorted when scaled to fit the phone’s screen.

The following are the most common media sizes for rich push notifications.

- 512 x 256 px
- 1024 x 512 px
- 2048 x 1024 px