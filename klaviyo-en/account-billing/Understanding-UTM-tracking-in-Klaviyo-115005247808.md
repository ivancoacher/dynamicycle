---
id: "115005247808"
title: "Understanding UTM tracking in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005247808-Understanding-UTM-tracking-in-Klaviyo"
section: "UTM tracking"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:54:22Z"
language: "en"
---
## You will learn

Learn what UTM tracking is, how it works, and how you can use it in your Klaviyo messages to gain a deeper understanding of your marketing performance.

Looking to add UTM parameters to Klaviyo messages? Head to our article on [how to add UTM tracking to campaigns and flows](https://help.klaviyo.com/hc/en-us/articles/360053921252).

As of June 2, 2025, the default values of utm\_medium have changed from **campaign** and **flow** to **Message type** which includes email, SMS**,** WhatsApp and push. If you customized and saved your UTM settings before June 2, you will see the old values in your account, otherwise the new values will be set. No other values have been changed.

## What is UTM tracking?

UTM parameters are small codes added to the end of links that help Google Analytics and other site traffic tracking tools to identify where your visitors originated from. By adding UTM parameters to your Klaviyo email, SMS**,** WhatsApp and push, you can better understand how the messaging you send through Klaviyo contributes to your overall traffic and conversions.

There are 2 default UTM parameters that are always turned on: ****utm\_source**** and ****utm\_medium****. In addition to these two, Google Analytics accepts an additional three parameters by default: ****utm\_campaign****, ****utm\_id****, and ****utm\_term****. Toggle these parameters on or off in Klaviyo as you wish.

![](https://klaviyo.zendesk.com/hc/article_attachments/37700477750299)

For each of the 5 prebuilt UTM parameters, choose between a built-in Klaviyo option (e.g., “Message type” for utm\_medium) or add a custom value by typing in a new value to the **Search or add new** field within the dropdown.

In addition, you can create up to 5 fully custom UTM parameters by clicking **Add a custom UTM parameter** and filling out the fields that appear.

## Configure your account's default UTM tracking

To customize your account's global UTM tracking settings

1. Click your account name in the bottom left of your screen.
2. Select ****Settings**** in the dropdown.
3. Click ****Other > UTM tracking****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28716329294491)
4. Choose which parameters to include using the toggle next to each option.
5. Select an option under **Campaign Value** and **Flow Value** for each parameter.
6. Recommend: set the UTM medium as **Message type** if using (or planning to use) multiple channels (e.g., email, SMS**,** WhatsApp and push).
7. Toggle on ****Automatically add UTM parameters to links**** to apply these parameters across all future messages you send from Klaviyo.
8. Click ****Save**** to save your changes.

If you want to disable this for a particular campaign or flow email, you can do so at the message level by checking ****Do not use UTM tracking for this campaign**** (campaigns) or toggling off UTM Tracking (flows). Alternatively, you can leave ****Automatically add UTM parameters to links**** toggled off in your settings, and manually turn on UTM tracking for individual messages.

When you make changes to your global UTM settings, messages that currently use your global UTM settings will reflect the changes. Messages with custom UTMs or with UTM tracking disabled will not use the new global settings until UTM tracking is turned on and the ****Customize Tracking Parameters**** setting is disabled within the message settings.

### How an attributed campaign is determined

If you use ****List or segment name(s)**** as the value for a parameter such as **utm\_source** and send a campaign to multiple lists and/or segments, the **utm\_source** value that populates for a particular recipient will be the list or segment that the recipient is a part of when the campaign is sent.

The value for ****utm\_source**** can only refer to 1 list or segment. This means that if the recipient was part of multiple lists or segments to which the campaign was sent, only one list or segment will be chosen based on whichever was selected first in the campaign wizard.

For example, let's say Jane is a subscriber in your account. She is in both the **VIP Customers** segment and the **High-Engagement** segment. When creating an email campaign, you send to both of these segments, but you select **VIP Customers** first. This means that when the campaign is sent, the value for **utm\_source** will be **VIP Customers** for Jane's email, and her activity will be attributed to this segment.

Note that this logic applies for any tracking parameter campaign value for which one of the following 3 parameter values are selected:

- List or segment id(s)
- List or segment name(s)
- List or segment name(s) (List or segment id)

## About Klaviyo’s UTM parameter options

For most UTM parameters, you can choose between a dynamic, static, or custom value. In addition, you can choose different default values for campaign and flow messages.

### Static values

Static values remain the same for all messages, but you can choose a different static value for campaigns and flows. All custom values are static, but you can also choose a default static value from the options provided by Klaviyo.

Static values include:

- ****klaviyo****
- ****email****
- ****sms****
- ****whatsapp****
- Either ****campaign**** or ****flow****

### Dynamic values

Dynamic values change based on what kind of message you send (e.g., email, sms, whatsapp and push, or flows and campaigns). For example, if you set the utm\_medium parameter to **Message Type**, then links in SMS messages you send will include `utm_medium=sms` and links in emails will include `utm_medium=email`.

Campaigns and flows have different value options for dynamic values, but options are the same per parameter. In other words, all parameters have the same value options for their category.

Note that dynamic UTM parameters cannot be applied to product blocks or data feeds. However, they can be manually added to static product blocks if needed.

### Custom values

To add a custom value to any UTM parameter:

1. Click to open the dropdown of the value you’d like to add.
2. In the **Search or add new...** field, type the value you’d like to use. In the screenshot below, the parameter for all messages will be "campaign+message".
   ![A user adds a custom static value to their UTM parameters](https://klaviyo.zendesk.com/hc/article_attachments/28716329288603)
3. Click ****Create “Option”****.

These parameters will be used exactly as they appear in your UTM settings.

### Global vs. message-level UTM parameter settings

Global UTM parameters (set in ****Settings > Other > UTM tracking****) set the defaults that are use in your messages across Klaviyo. You can apply these default parameters to all messages by turning them on globally in your settings, or apply your global settings to a particular message by toggling UTM parameters on within that message's settings.

Message-level UTM parameters are fully customizable and don't necessarily match your global UTM settings. Changes to your global UTM settings will not apply to messages that have customized message-level UTM parameters.

## UTM variation letters

UTM variation letters are available for email, not SMS.

UTM variation letters allow you to compare the performance and link activity when A/B testing your campaign and flow emails. For example, if you have three variations of a campaign and want to find out which directs the most traffic to your site, label them with letters — such as a, b, and c. Then, Klaviyo will generate data from the link within each varied email so that you can test, analyze, and adjust your content accordingly.

Although Klaviyo links automatically get a variation parameter when UTM tracking is enabled, Google Analytics will not. To run a UTM variation test using Google Analytics, you will need to create a custom parameter in Google Analytics for your variation prior to conducting your test.

To learn how to add UTM variation letters to campaigns and flows, head to [How to add UTM tracking to campaigns and flows](https://help.klaviyo.com/hc/en-us/articles/360053921252).

## Comparing Klaviyo conversion tracking and Google Analytics

Because Google Analytics uses link clicks to track conversions and Klaviyo uses data directly from your database (e.g., ecommerce store), it's likely the analytics between both services won't exactly align. In general, Klaviyo’s conversion tracking is more accurate than Google Analytics.

For example, Google Analytics will not record a conversion if a subscriber receives an email, reads it, does not click on a link, but goes to your store. Or in another scenario, a customer receives an SMS message, opens it, but then eventually makes the purchase from their desktop; Google Analytics will not record this conversion either. However, in both scenarios, Klaviyo recognizes these conversions and stitches them together. In the first example, Klaviyo recognizes that a subscriber first opened the email, and in the second example, recognizes that the SMS message triggered a purchase. Just keep in mind that Klaviyo will only recognize these within the [message attribution windows](https://help.klaviyo.com/hc/en-us/articles/1260804504250-Understanding-Klaviyo-message-attribution#klaviyo-attribution-timing-for-email-vs--sms3).

Because of this fundamental difference, we recommend deferring to Klaviyo's conversion analytics when possible.