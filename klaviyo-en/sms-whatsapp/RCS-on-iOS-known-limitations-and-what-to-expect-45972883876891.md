---
id: "45972883876891"
title: "RCS on iOS: known limitations and what to expect"
source_url: "https://help.klaviyo.com/hc/en-us/articles/45972883876891-RCS-on-iOS-known-limitations-and-what-to-expect"
section: "RCS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:02Z"
language: "en"
---
RCS is a carrier-backed messaging standard that has matured primarily on Android. Apple has only recently added support for RCS on iOS, and that implementation is still evolving.

As a result, some RCS features may behave differently or inconsistently on iOS compared to Android. These limitations are dictated by Apple’s OS-level RCS implementation and are outside the control of Klaviyo, Google, carriers, or Klaviyo’s RCS partners.

This article explains:

- Why RCS behaves differently on iOS
- The known iOS-specific issues we are aware of
- What to do if you encounter an issue
- How fixes are prioritised and rolled out

## Why RCS behaves differently on iOS

RCS messages are rendered and handled entirely by the native Messages app on each operating system and Apple’s RCS implementation does not yet offer full parity with Android.

As a result, Klaviyo cannot control or override:

- Message layout and rendering
- Button placement and behaviour
- Media rendering
- Thread preview text and caching behaviour

  These behaviours are dictated by Google & Apple’s OS-level RCS support and may vary by:
- OS version
- Device model
- Carrier configuration

## Known RCS issues on iOS

Below is a list of known issues that have been observed on some iOS devices. This list will change over time as Apple releases fixes, but some users on older OS versions may still experience these behaviours.

#### Agent (sender ID)

- The agent ID may be displayed instead of the agent name
- Banners do not display on the agent information page

#### Rich cards

- On Android, image height can be set explicitly. On iOS, images are automatically resized based on text size and length, which can cause images to appear squashed.
- Button colour appears grey and lacks visual prominence.
- Button labels may be cached incorrectly and display the wrong text in message threads.
- When multiple buttons are present, they are included in a dropdown and the label defaults to “options”.
- Quick action URL links appear inside card buttons instead of in a separate bubble below the card.
- Quick reply buttons appear in a separate bubble below the card where quick actions are expected.
- If a card has no title, the preview text will display as “one message”.

#### Media and content

- GIFs render as static images rather than animated

#### URLs and previews

- URLs placed at the end of a message with no trailing text will be sent as a separate bubble with “tap to preview”
  - ****Workaround****: add a full stop or other character after the link.

#### Important notes about these issues

- These issues do not occur on all devices or iOS versions
- Some issues may already be fixed in the latest iOS releases
- Users on older OS versions may still experience problems

Our goal is to make brands aware of all known limitations so they can design RCS experiences defensively.

## How do avoid most issues

Please send a preview to both an iOS and an Android device before scheduling a campaign or activating a flow to confirm that the message behaves as expected on both platforms. This will catch most issues, but behaviour can still vary across iOS versions, device models, and carrier configurations.

## What to do if you encounter an issue

If you encounter any of the issues listed above, or discover a new iOS-specific RCS issue:

#### 1. Submit feedback to Apple

All RCS rendering and behaviour issues on iOS must be reported directly to Apple using their feedback system.

1. Go to the [Apple feedback page for Messages](https://apple.com/feedback/messages-ios-ipados/). ￼
2. Select your country or region.
3. Choose the feedback type (select Bug Report ). ￼
4. In the comments field, explain the RCS behaviour you observed, the OS version, the device model, and steps to reproduce the issue. Screenshot examples also help.
5. In the 'What Messages feature is your feedback about?⁠\*' field, select 'Other'.
6. Submit the form and note the Feedback ID. Apple may not respond directly, but all submissions are logged. ￼

This is the only channel through which these issues can be fixed.

#### 2. Share the Apple Feedback ID with Klaviyo

Once you have submitted feedback to Apple, share the Feedback ID with Klaviyo Support.

This allows us to:

- Track the issue
- Aggregate feedback across customers
- Actively raise and escalate the issue with Apple where possible

## Issue resolution

Klaviyo does not have visibility into Apple’s RCS roadmap, timelines, or prioritisation.

We cannot:

- Commit to fix dates
- Influence release schedules
- Patch or workaround OS-level behaviour

The only effective lever is volume and consistency of feedback. The more feedback Apple receives on a specific issue, the more likely it is to be prioritised.

## Summary

- RCS on iOS is still maturing and does not yet match Android behaviour
- All rendering and interaction issues are controlled by Apple
- Known issues may vary by OS version and device
- Brands should submit feedback directly to Apple and share the Feedback ID with Klaviyo
- Increased feedback improves the likelihood of prioritisation and fixes

We will continue to monitor, document, and communicate any new iOS-specific RCS issues as we become aware of them.