---
id: 1260804504250
title: "Understanding Klaviyo message attribution"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/1260804504250-Understanding-Klaviyo-message-attribution"
section: "Attribution"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:26Z"
language: en
---

## You will learn

Learn about Klaviyo's event and message attribution or the ability to review which of your messages or channels led to customer actions.

## Why is attribution important?

Attribution assesses customer actions and revenue across each marketing channel and message and helps you to identify which channel, message, or strategy was most successful, so you can effectively allocate resources to those activities or adjust them as needed.

## How does Klaviyo assign attribution?

Every platform or vendor may define event or message attribution slightly differently, and it’s important to be aware of these potential differences.

In Klaviyo, event attribution follows a cooperative, multi-channel model. This means that we give each Klaviyo owned channel their own distinct configurable window and non-Klaviyo channels a single configurable window. Klaviyo will only attribute a customer event (e.g., placed order) to messages within one of these open windows.

## Default message attribution settings

By default, Klaviyo uses a last touch attribution model with the following lookback window for all new accounts

- 5 days for email clicks
- 5 days for email opens
- 5 days for text messages clicks
- 1 day for text message opens
- 12 hours for text message deliveries
- 24 hours for push opens
- 5 days for Whatsapp clicks
- 12 hours for Whatsapp opens
- 1 day Active on Site (Advanced KDP and Marketing Analytics customers only)

To adjust your attribution windows and machine or bot clicks settings, refer to our guide on[configuring your email, SMS, and push attribution settings](https://help.klaviyo.com/hc/en-us/articles/11118357030555).

## Attribution model updates

Klaviyo’s attribution model will recalculate historical data after attribution settings in account are updated, so past and future data remains consistent. Updates to attribution models may take up to 36 hours to be reflected within your account.

## Window for calculating attribution

Klaviyo’s model will attribute conversion events within 3 hours of receiving the event. The attribution model will also update attribution within 5 days if there are late arriving message interaction events

Event vs. message attribution

Event attribution refers to when Klaviyo attributes events to specific messages and customer actions. For example, a customer receives an email, clicks a link, and then purchases an item via that link. Klaviyo looks to see if an attributable action has taken place (i.e., opens, clicks, or deliveries) and if the attribution window is open. The event attribution window will start when the profile initially receives the message.

On the other hand, message attribution looks at when a message is first sent. For example, say you schedule a message for 9am on March 10th in your recipient's local time and your[Klaviyo account is in the eastern timezone](https://help.klaviyo.com/hc/en-us/articles/115005232388). A recipient in Australia receives your email at 9am their local time, which is 5pm the previous day for you. This means that when viewing your reporting, the data would be attributed to the day the email was sent from your account (based on your account timezone). In the example above, the attributed open, clicks, and unsubscribes for your Australian recipients is March 10th (i.e., the day before aligned to your timezone).

Because message attribution looks at when a message is first sent based on your account timezone, attributed events may not exactly align with the local date/time that a specific recipient opened. Klaviyo will still attribute these events to the message in relevant reporting.

## Klaviyo event attribution timing

### Single source lookback window example

By default, the lookback window for email opens and clicks is 5 days, but you can[adjust these windows](https://help.klaviyo.com/hc/en-us/articles/11118357030555#adjusting-the-email-attribution-window2) in your account's attribution settings if you choose.

The example below illustrates how email attribution works. Note that the example is using the default 5-day email open and click lookback windows.

- Day 1
  You email your subscriber and they open it.
- Day 2
  The subscriber opens this email again and clicks on a link to a product offer.
- Day 4
  They ultimately come back and purchase that product.

In this example, it would attribute revenue to email since it's within the 5-day attribution window. However, if the customer were to make the purchase on day 12, then this would not be attributed to the original email.

### Multiple sources lookback window examples

In both examples above, email, SMS, and push messages are sent separately with their own lookback windows. However, the example below illustrates what would happen if you sent both an email and SMS message around the same time.

The example below uses the default 5 day email clicked and opened lookback window and 1 day SMS click lookback window.

- Day 1
  You send both an email and SMS message to your subscriber, and they open both messages.
- Day 3
  The subscriber clicks into SMS again but does not purchase.
- Day 4
  They open the email again.
- Day 5
  They come back, click on the SMS, and then purchase.

In this example, it would attribute the revenue to email because the email was the last message that Klaviyo attributed to a specific subscriber event. Even though the customer clicked on the SMS message last, since you set the SMS attribution window at 5 days, it is outside the lookback window. Thus, it’s important to be mindful of both your email and SMS attribution window settings together and how this may affect your data.

## Klaviyo message attribution in analytics reports

Many of the Klaviyo analytics reports that focus on campaign and flow reporting use the email, SMS, and push message attribution models. However, it’s important to know that not all reports use these attribution windows to sort their data.

Reports ****that use message attribution**** to sort their data and rates include:

- [Home dashboard](https://help.klaviyo.com/hc/en-us/articles/9974064152347)
- [Overview dashboard](https://help.klaviyo.com/hc/en-us/articles/4708299478427)
- [Campaign performance report](https://help.klaviyo.com/hc/en-us/articles/360047022912)
- [Flows performance report](https://help.klaviyo.com/hc/en-us/articles/360047044892)
- [Campaign](https://help.klaviyo.com/hc/en-us/articles/115005258568) and[flow](https://help.klaviyo.com/hc/en-us/articles/115002779351) overview reports
- [Portfolio reporting](https://help.klaviyo.com/hc/en-us/articles/25185047957275)
- [Benchmarks](https://help.klaviyo.com/hc/en-us/articles/360050110072)
- [Audience performance report](https://help.klaviyo.com/hc/en-us/articles/17798068936219) (Advanced KDP and Marketing Analytics customers only)

  For those reports that do not use the message attribution windows, any event data (e.g., opens and clicks) will group based on the date those specific events happen. The data will not be based on the day an attributed message was sent.

  Analytics reports ****that do not sort data and rates by attributed message**** send date include:
- [Single metric report](https://help.klaviyo.com/hc/en-us/articles/360046242952)
- [Multi-metric report](https://help.klaviyo.com/hc/en-us/articles/360046234772)
- [Metrics](https://help.klaviyo.com/hc/en-us/articles/115005076787)
- [Funnel analysis report](https://help.klaviyo.com/hc/en-us/articles/17798009376155) (Advanced KDP and Marketing Analytics customers)
- [Custom monitors](https://help.klaviyo.com/hc/en-us/articles/27160071187739) (Advanced KDP customers)