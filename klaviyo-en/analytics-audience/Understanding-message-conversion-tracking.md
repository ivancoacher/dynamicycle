---
id: 115005248128
title: "Understanding message conversion tracking"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005248128-Understanding-message-conversion-tracking"
section: "Data explanations and attribution"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:22Z"
language: en
---

## You will learn

Learn how conversion tracking works for email, SMS, and mobile push messaging and how to edit these settings. For each campaign and flow sent, Klaviyo automatically tracks conversions. This allows you to analyze the performance of your marketing channels and their individual success.

## What is conversion tracking?

A conversion occurs when a recipient opens your message and then takes another action (such as placing an order) within the conversion period or the [attribution window](https://help.klaviyo.com/hc/en-us/articles/1260804504250).

Klaviyo defines conversion events that involve orders (e.g. **Placed Order**, **Fulfilled Order**, **Ordered Product**, etc.). However, this does not include if a subscriber simply opened your email or started a checkout.

While most other platforms only track revenue conversions, Klaviyo automatically computes conversion analytics for all metrics in your account. For new customers after 10/9/2024 the default window is 5 days for email and SMS and 24 hours for push, but you can adjust this in your account's [email, SMS, and push settings pages](https://help.klaviyo.com/hc/en-us/articles/11118357030555).

Note that the default Klaviyo email, SMS, and push messaging attribution windows may differ slightly from other platforms and vendors.

## How does conversion tracking work?

There are a few important notes about conversion tracking:

- ****Multi-channel or cooperative attribution****
  If you are using more than one marketing channel, Klaviyo looks at each individual channel's (SMS or email) attribution window. From here, it is determined if either of those channels should get revenue attribution at the time of purchase. For example, if an SMS attribution window has closed, but the email attribution window is still open, and the customer interacted with email during that time period, attribution will go to the email.
- ****Conversion open and click tracking****
  Conversions are tracked if someone opens or clicks, or if Apple Mail Privacy Protection (MPP) automatically opens the email. However, if you would like to exclude the MPP opens from your conversion metrics, you can [adjust this setting](https://help.klaviyo.com/hc/en-us/articles/4416803987739). Conversions are only tracked if someone opens or clicks a message, and does not include if they just received the message but made no further action.
- ****Conversion period tracking****
  The conversion period begins when a subscriber receives a message. Only follow-up actions that occur within the conversion period or attribution window count.
- ****Conversion period timing****
  For both email and SMS, Klaviyo looks at message attribution per day. As a result, whatever day you send a message will be the day where attributed rates and conversions are counted. For example, if you email all recipients on a Friday and they open this email on both Friday and Saturday, those opens will be attributed to Friday.
- ****Conversion reporting****
  The above is also important to keep in mind when viewing any [analytics reports that use message attribution](https://help.klaviyo.com/hc/en-us/articles/1260804504250-Understanding-Klaviyo-message-attribution#klaviyo-message-attribution-in-analytics-reports7). If you only view analytics for an individual day, Klaviyo will not attribute conversions associated with a message that took place on a different day. In other words, querying individual days means you are giving campaigns less time to generate revenue and your analysis will not give the bigger picture. Instead, select a broader timeframe that accounts for your conversion window.

### Why does Klaviyo track conversions in this way?

Conversion tracking that relies on pixels can be unreliable. For example, if someone reads an email on their phone but makes a purchase later from their laptop, tracking that relies on pixel tracking would miss that conversion. Klaviyo does not use pixels so the conversion analytics are more accurate. Instead, Klaviyo calculates conversions based on data directly from a built-in integration or our API.

You do not need to decide in advance which metric you want to focus on for conversion tracking. While most other platforms only track revenue conversions, Klaviyo automatically computes conversion analytics for all metrics in your account.

For example, an ecommerce business wants to know the number of purchases that occurred because of an email. However, if they're interested in how many people viewed at least one product page or started a checkout after receiving an email, they can view this conversion data as well. This allows them to compare the impact of different campaigns across different performance standards.

## Email conversion tracking

Unlike conversions, Klaviyo tracks open events by placing a tiny, invisible pixel image at the bottom of every email. This method of open tracking is the industry standard and less likely to cause issues with spam blockers or mailbox providers (MBPs). Whenever a recipient opens or clicks your email, we record this invisible pixel (web beacon) as "viewed" and mark the email as opened. We will continue to track your opens and clicks regardless of your chosen conversion window.

Learn how to [edit the location of your tracking pixel](https://help.klaviyo.com/hc/en-us/articles/360049695831) in your account’s settings.

### Potential open discrepancies

It is possible for a recipient to click an email without opening it. For instance, this may happen if they click a link before an email loads completely. Apple Mail Privacy (MPP) may also account for opens that are not made by the subscriber themselves.

To help remove MPP opens from your data, always include both open and click filters, as shown in the example segment below. This ensures that you capture any users that were tracked as having clicked but not opened the message. You can also adjust your [email conversion settings](https://help.klaviyo.com/hc/en-us/articles/360004059711) in your account to track MPP opens by default.

![Example of a non-opener segment with users receiving at least 1 email ever, and opened or clicked them zero times ever](https://klaviyo.zendesk.com/hc/article_attachments/28720770670363)

Klaviyo tracks click activity by adding unique tracking information to each URL. As a result, when hovering over a link in a Klaviyo email you may see the URL begin with the example below. Note that this may look slightly different depending on if your account has [dedicated click tracking](https://help.klaviyo.com/hc/en-us/articles/360001550572-Setting-Up-Dedicated-Click-Tracking) setup.
`[unique-account-identifier].trk.klaviyomail.com`

## SMS conversion tracking

By default, Klaviyo sets a 5-day SMS conversion window, which you can edit in your [account settings](https://help.klaviyo.com/hc/en-us/articles/11118357030555#adjusting-the-sms-attribution-window3).

Attribution for SMS occurs when an SMS is delivered to a recipient before a conversions, or when a recipient clicks a text and then takes another action (such as placing an order) within the attribution window. Thus, the conversion window is the number of hours in which any purchase is made after the SMS message was delivered or clicked.

Note that in order to track SMS click conversions for a profile, you will need to have sent an SMS message with a link and links must use the Klaviyo link shortener. When setting up your SMS messages, it’s important to have the option checked for ****Automatically shorten links**** to ensure you are using the default tracking.

Keep in mind that Klaviyo connects attribution to a customer's interaction with both channels at the time of purchase or action. Learn more about [multi-channel attribution](https://www.klaviyo.com/blog/cooperative-multi-channel-attribution) and how email and SMS attribution works together.

If you're seeing a lot of unattributed conversions, extend the SMS conversion window.

## Push conversion tracking

By default, Klaviyo sets a 24-hour attribution (also called conversion) window for push notifications. However, you can edit this window in your settings.

Attribution for push occurs when a recipient taps on a notification (i.e., opens the push) and then takes another action (such as placing an order) within the attribution window. Thus, the attribution window is the number of hours after a push notification is opened in which Klaviyo will attribute a conversion to that message.

Keep in mind that Klaviyo connects attribution to a customer's interaction with every channel (push, SMS, and email). Further, Klaviyo attributes the conversion to the last message the customer interacted with that’s still within the attribution window.

## Multi-channel conversions

What happens when you send messages via multiple channels? Which message will the conversion be attributed to?

Klaviyo uses a combination of a "last touch" model and each channel's attribution window. It attributes a conversion to whichever message was clicked or opened most recently, as long as that conversion also falls within the message's attribution window.

For example, let’s say that:

- A customer opens an email on day 1.
- The same customer opened a push notification on day 2.

If the customer buys the product on day 3, the conversion will be attributed to the push notification. The push is the “last touch” and, as long as the purchase happens within the 24-hour window, the revenue will be credited to that notification.

However, say the customer buys a product on day 4. In this case, the conversion will be attributed to the email. Since the purchase is outside the push conversion window, it can’t be attributed to push. However, the purchase does fall within the email window, so Klaviyo will attribute the conversion to the email.

## Email and SMS website tracking

When you add the Klaviyo web tracking snippet to your site, it can only track events for "known browsers."

There are a few different ways Klaviyo identifies a site visitor for web tracking purposes:

- ****Website tracking enabled****
  When you have email to website tracking enabled and have Klaviyo's main web tracking snippet on your website, Klaviyo will identify and [cookie](https://klaviyo.zendesk.com/hc/en-us/articles/360034666712) individuals that click through a Klaviyo email or SMS and end up browsing your website.
- ****Subscriber opt-in****
  When someone has, at some point, subscribed/opted-in through a Klaviyo form, web tracking code will cookie this person at the time of opt-in.

You can toggle on and off Klaviyo's ability to track email to website activity in your [account's email settings](https://help.klaviyo.com/hc/en-us/articles/11118357030555-How-to-change-your-email-and-SMS-message-attribution-settings#adjusting-the-email-attribution-window2).

Note that Klaviyo adds a parameter, known as the `_kx` parameter, to all URLs in your email or SMS message to track activity. This unique encoded parameter is then decoded by Klaviyo's web tracking, and provides the ability to identify the user that clicked through the URL.

This parameter is automatically appended and will not affect the load times of your URLs nor break any URLs based on its placement. See the example link below for an idea of how this will look in a URL:

`http://example.com/?_kx=J8fjcn003Wy6b-3ILNlOyZXabW6dcFwTyeuxrowMers%3D.McN66`

### Potential discrepancies between Klaviyo and Google Analytics

Because Google Analytics uses link clicks to track conversions and Klaviyo uses data directly from your database, it's likely the analytics between both services won't exactly align. Thus, there may be instances where Google Analytics does not record conversions when they actually occur.

For example, Google Analytics will not record a conversion if a subscriber receives an email, reads it, does not click on a link, but goes to your store. Or in another scenario, a customer receives an SMS message, opens it, but then eventually makes the purchase from their desktop; Google Analytics will not record this conversion either. However, in both scenarios, Klaviyo recognizes these conversions and stitches them together. In the first example, Klaviyo recognizes that a subscriber first opened the email, and in the second example, recognizes that the SMS message triggered an eventual purchase. Just keep in mind that Klaviyo will only recognize these within open [message attribution windows](https://help.klaviyo.com/hc/en-us/articles/1260804504250-Understanding-Klaviyo-message-attribution#klaviyo-attribution-timing-for-email-vs--sms3).

Because of this fundamental difference, we recommend deferring to Klaviyo's conversion analytics when possible.

## Appending UTM tracking to emails

When creating a flow, email, or SMS campaign in Klaviyo, you can add UTM parameters to your email. You can [customize these UTM tracking parameters at an account-level](https://help.klaviyo.com/hc/en-us/articles/115005247808-Klaviyo-and-Google-Analytics-Tracking) and you can also configure these at an email-level.

By default, Klaviyo will track:

****Emails****

- ****Source****
  List or segment name(s)
- ****Medium****
  Email
- ****Campaign****
  Campaign name including campaign id

****SMS messages****

- ****Source****
  List or segment name(s)
- ****Medium****
  SMS
- ****Campaign****
  Campaign name including campaign id

****Flows****

- ****Source****
  Flow name
- ****Medium****
  Email (note that this is the default, but you can also update your settings to reflect SMS or by campaign)
- ****Campaign****
  Flow message name, including flow id

For example, if you have a [welcome series flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002775172) and the first email is named "Intro to our Brand" and the flow email ID is A12bc3, then the following UTM parameters will append to your links:

- ****Medium****
  Email
- ****Source****
  **Welcome Series**
- ****Campaign****
  "Intro to our Brand (A12bc3)"

Keep in mind that in Google Analytics, the 5 default UTM parameters (i.e., utm\_medium, utm\_source, utm\_campaign, utm\_content, and utm\_term[Klaviyo profile ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6)) will be lowercase automatically.

### Additional parameters

Besides the default parameters noted above, you also have the option to turn on the following fields in your account-level settings:

****Emails****

- ****ID****
  You have the option to include campaign ID, campaign name with campaign ID, [external ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#i5), [Klaviyo profile ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6), or link text or alt text.
- ****Term****
  You have the option to include [external ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#i5), [Klaviyo profile ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6), or link text or alt text.

****SMS****

- ****ID****
  You have the option to include campaign ID, campaign name with campaign ID, [external ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#i5), [Klaviyo profile ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6), or link text or alt text.
- ****Term****
  You have the option to include external ID, Klaviyo profile ID, or link text or alt text.

****Flows****

- ****ID****
  You have the option to include flow ID, flow message name with flow ID, [external ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#i5), [Klaviyo profile ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6), or link text or alt text.
- ****Term****
  You have the option to include [external ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#i5), [Klaviyo profile ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6), or link text or alt text.

## Additional resources

- [How to change message attribution and conversion settings](https://help.klaviyo.com/hc/en-us/articles/11118357030555)
- [Understanding message attribution](https://help.klaviyo.com/hc/en-us/articles/1260804504250)
- [Getting started with Klaviyo onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767)
- [Understanding UTM tracking in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005247808)