---
id: 41072788661531
title: "How to create rich interactive RCS messages in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41072788661531-How-to-create-rich-interactive-RCS-messages-in-Klaviyo"
section: "RCS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:56:56Z"
language: en
---

Klaviyo allows you to create rich RCS messages that include text, media, and interactive elements within both campaigns and flows. These richer messages help drive higher engagement and conversion rates by providing a more interactive customer experience.

## ****Getting started****

When creating an RCS message in Klaviyo, you can choose between two message types:

1. ****Text only**** – A simple text message similar to SMS, with the option to include up to 11 Quick Actions.
2. ****Rich cards**** – A richer message format that supports images, videos, buttons, and up to 10 cards per message, plus up to 11 Quick Actions across the message.

You can access both options in the message editor when creating or editing a text message within a campaign or flow.

![](https://klaviyo.zendesk.com/hc/article_attachments/42826305366427)

## ****Text-only messages****

Text-only RCS messages function like SMS but can include Quick Actions, which make your message interactive.

#### Quick Actions

Quick Actions appear as suggestion chips below the message. You can include up to 11 Quick Actions per message.

Quick actions support:

- ****Visit link -**** a URL attachment linking to an external webpage.
- ****Quick reply**** - allowing the recipient to send a predefined response back to you.

Quick Actions are only displayed on the most recent message in a conversation. When a new message is sent in the thread, the previous Quick Actions will disappear. They are designed to prompt an immediate response, not to persist permanently in the conversation like card buttons.

Quick Actions can be used to drive engagement, such as linking to a promotional page, or to capture feedback from customers and trigger [automated conversations](https://klaviyo.zendesk.com/hc/en-us/articles/34158391513627).

![](https://klaviyo.zendesk.com/hc/article_attachments/42826329942299)

## ****Rich Cards****

Rich cards let you create visually engaging, interactive messages that combine media, text, and buttons. You can send a single card or a carousel of up to 10 cards within one RCS message.

#### Card Components

Each card can contain the following elements:

- ****Media****: An image or a video (up to 10 MB)
- ****Title:**** Up to 200 characters
- ****Description****: Up to 2,000 characters
- ****Buttons****: Up to 4 buttons per card, with 25 characters per label

Each card must include ****at least one**** of the following: ****media, title, or description.**** You can choose to include just one of these elements, or combine them depending on how you want your message to appear.

You can also add Quick Actions (up to 11 total) across the entire message. These are not tied to individual cards but appear as global suggestion chips at the bottom of the message.

****Note****: If you do not include a title in a card, iOS will display “One Message” as the message preview. If a title is included, that title will appear in the preview. For multi-card messages, the title from the first card will appear in the preview.

#### Media guidelines

Follow these recommendations to achieve the most consistent media display across devices. RCS media rendering differs between Android and iOS, so results may vary.

****Images:****

- Supported formats: PNG, JPG, JPEG, GIF, WebP (****note****: GIFs are not supported on iOS and will render as static images)
- Aspect ratio: 16:9
- Optimal resolution: 1440 × 720 px
- Maximum file size:
  - RCS: ≤2 MB
  - MMS fallback: ≤600 KB (recommended)
  - Klaviyo platform upload limit: 10 MB

    These guidelines apply to RCS Rich Cards with a medium sized media asset displayed at the top of the card.

    ****Video:****
- Supported formats: MP4, MPEG
- There are no published Google guidelines for optimal video resolution, aspect ratio, or bitrate equivalent to image specs
- Rendering and playback behaviour is device dependent

#### Button attachments

Similar to Quick Actions, each button supports:

- ****Visit link -**** a URL attachment linking to an external webpage.
- ****Quick reply**** - allowing the recipient to send a predefined response back to you.

You can use dynamic URL links, but dynamic button labels are not supported, as dynamic values may exceed the 25-character limit.

#### Important considerations for iOS

iOS renders RCS cards differently to Android and does not follow Google’s layout rules. As a result, customers may see:

- More aggressive cropping than on Android
- Extra cropping when titles or descriptions are long
- Visible differences in image height between cards in the same carousel
- GIFs displayed as static images (GIFs do not animate on iOS)

  To keep all images the same size in a carousel on iOS, you must keep the card titles and descriptions roughly the same length across every card. iOS dynamically adjusts image height based on the total text in each card, so inconsistent text lengths will lead to inconsistent image sizes.

  ****To maximise consistency across Android and iOS:****
- Keep important content away from the edges
- Use clean images with minimal embedded text
- Keep title and description lengths similar across all cards in a carousel
- Preview and test messages on both Android and iOS before sending

Apple is working to improve RCS rendering on iOS, but there is no confirmed timeline.