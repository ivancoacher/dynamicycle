---
id: "360053921252"
title: "How to add UTM tracking to campaigns and flows"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360053921252-How-to-add-UTM-tracking-to-campaigns-and-flows"
section: "UTM tracking"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-05-01T20:43:45Z"
language: "en"
---
## You will learn

Learn how to use UTM tracking in your Klaviyo email, text**,** WhatsApp and mobile push messages to develop insights and improve your Google Analytics conversion tracking.

UTM tracking sends data to Google Analytics (or other tracking software) about where visitors came from. Use UTM tracking in your campaigns and flows if you’d like to track conversions from your Klaviyo messages in Google Analytics.

## Before you begin

This article explains how to append UTM parameters to links you send through Klaviyo email, text**,** WhatsApp and mobile push messages. In order to use these parameters for data analysis in Google Analytics, you’ll need a fully configured Google Analytics account. Successfully using custom parameters (i.e., parameters other than the five defaults provided) requires a comfortable working knowledge of Google Analytics.

Note that **message ID** and **message variation** are different properties used in UTM tracking. **Message ID** refers to the overarching ID number of the message, while **message variation** refers to the ID associated with a specific A/B test version. Currently, only **message ID** will appear in report downloads. However, both **message ID** and **message variation** will appear in your Google Analytics data.

Reference [Google’s support documentation](https://support.google.com/analytics/?hl=en#topic=10737980) for questions related to your Google Analytics account or setup.

## Configure global UTM settings

Before configuring UTM settings for individual messages, consider turning on global UTM tracking in your account settings. You can always adjust the UTM settings for a specific message using the instructions in the following sections.

If using multiple channels, please be aware that you need to manually set the UTM medium to be omnichannel

1. Navigate to  ****Settings**** > ****Other**** > ****UTM tracking****.
2. Toggle any parameters you'd like to include on.
3. Adjust the **Campaign Value** and **Flow Value** fields

   - Campaigns and flows have different value options for dynamic values, but options are the same per parameter. In other words, all parameters have the same value options for their category.
4. Recommended: set the UTM medium to be **Message type** if you use multiple marketing channels (e.g., email and text messages).
5. Toggle **Automatically add UTM parameters to links** on.
6. Click ****Save**** to save your changes.

## Add UTM tracking to a flow message

To turn on UTM tracking for a flow message for email, text messages**,** WhatsApp, and mobile push notifications:

1. Navigate to the ****Flows**** tab.
2. Open the flow you’d like to edit..
3. Select a message in the flow builder.
4. Under **Settings**, check the box next to **Enable UTM Tracking** to automatically append UTM parameters to your links.

   ![utm tracking for flow message.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723632146843)
5. Click ****Save****.
6. Repeat for all other messages in the flow, if desired.

   When this setting is on, links are tagged in accordance with your account's default UTM tracking settings. To use different tracking parameters for a particular message:
7. Beneath the **UTM Tracking** setting, check the box for ****Use custom tracking parameters****.
8. Adjust the message’s UTM parameters as desired.
9. Click ****Save****.

Note that all links for email, text, and WhatsApp must have http:// or https:// in order to be tracked. Mobile push deep links may use custom schemes (e.g., myapp://).

Additionally, in text messages, the **Automatically shorten links** setting must remain enabled in order to use UTM parameters. Links added to URL buttons in WhatsApp messages and deep links in mobile push notifications will automatically use the UTM parameters configured at the message or account level.

## Add UTM tracking to a campaign message

To turn on UTM tracking for email, text**,** WhatsApp or mobile push campaign:

1. Navigate to the ****Campaigns**** tab.
2. Click to open an unsent campaign from the list.
3. In the **Tracking** section of **Step 1: Recipients**, enable the ****Include tracking parameters**** toggle.

   ![UTM tracking is toggled on in Klaviyo's campaign builder](https://klaviyo.zendesk.com/hc/article_attachments/28723660355867)

   Note that all links for email, text, and WhatsApp must have http:// or https:// in order to be tracked. Mobile push deep links may use custom schemes (e.g., myapp://).

   Additionally, in text messages, the **Automatically shorten links** setting must remain enabled in order to use UTM parameters. Links added to URL buttons in WhatsApp messages and deep links in mobile push notifications will automatically use the UTM parameters configured at the message or account level.

   When this setting is on, links are tagged in accordance with your account's default UTM tracking settings. To use different tracking parameters for your campaign:
4. Enable the ****Customize tracking parameters**** toggle.
5. Adjust the message’s UTM parameters as desired.
6. Click ****Continue to Content**** and continue editing your campaign as desired.

You must pause the campaign first if you’d like to adjust the UTM parameters for a message that has already been scheduled. UTM parameters cannot be edited for sent messages.

### How an attributed campaign is determined

If you use ****List or segment name(s)**** as the value for a parameter such as **utm\_source** and send a campaign to multiple lists and/or segments, the **utm\_source** value that populates for a particular recipient will be the list or segment that the recipient is a part of when the campaign is sent.

The value for ****utm\_source**** can only refer to 1 list or segment. This means that if the recipient was part of multiple lists or segments to which the campaign was sent, only one list or segment will be chosen based on whichever was selected first in the campaign wizard.

For example, let's say Jane is a subscriber in your account. She is in both the **VIP Customers** segment and the **High-Engagement** segment. When creating an email campaign, you send to both of these segments, but you select **VIP Customers** first. This means that when the campaign is sent, the value for **utm\_source** will be **VIP Customers** for Jane's email, and her activity will be attributed to this segment.

Note that this logic applies for any tracking parameter campaign value for which one of the following 3 parameter values are selected:

- List or segment id(s)
- List or segment name(s)
- List or segment name(s) (List or segment id)

## Add UTM variation letters to email A/B tests

Variation letters are available for only email, not text messaging.

UTM variation letters measure the performance and link activity between A/B tested campaigns and flow emails.

For example, if you have three variations of a campaign and want to find out which directs the most traffic to your site, use this feature to label them with letters. After sending the campaign, you’ll be able to tell whether version A, B, or C was most effective and adjust your content accordingly.

#### Email campaigns

To add a UTM variation letter to a campaign:

1. After adding UTM tracking to your campaign, click ****Continue to Content****.
2. At the bottom of this following page, click ****Create A/B test****.

   ![A cursor hovers over the option to create an A/B test in Klaviyo's campaign builder](https://klaviyo.zendesk.com/hc/article_attachments/28723660376859)
3. Check the box next to ****Track links separately in each variation****.

![In a campaign with an A/B test, the option to track links for each variation separately is toggled on](https://klaviyo.zendesk.com/hc/article_attachments/28723632158107)

#### Flow emails

To add UTM variation letters to a flow email:

1. From the flow editor, click into a flow message.
2. In the sidebar that appears, click ****Create A/B test****, or for existing A/B tests, click ****Configure test****.
3. On the following page, check the option to ****Track links separately in each variation****.

![In a Klaviyo flow message with an active A/B test, the option to track links separately for each variation is turned on](https://klaviyo.zendesk.com/hc/article_attachments/28723660368155)

Although Klaviyo links automatically get a variation parameter when UTM tracking is enabled, Google Analytics will not. To run a UTM variation test using Google Analytics, create a custom parameter for your variation in Google Analytics prior to conducting your test.