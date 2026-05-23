---
id: 41072989967515
title: "How to use the RCS capability property in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41072989967515-How-to-use-the-RCS-capability-property-in-Klaviyo"
section: "RCS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: en
---

> ****Prerequisite:**** The RCS capability property only appears for accounts that have activated RCS. If RCS is not enabled for your account, this property will not be visible.

The ****RCS capability property**** in Klaviyo helps you understand which subscribers can receive RCS (Rich Communication Services) messages. You can view this information on an individual profile, use it to create targeted segments, and apply it in flows and campaigns through conditional splits.

With the ****RCS capability property****, you can:

- Check whether an individual profile is RCS-capable in their SMS marketing subscription details
- Create RCS-only or SMS-only segments
- Use conditional splits in flows and campaigns to ensure that you deliver the right message format

## ****Viewing RCS capability on a profile****

The first step in using the RCS capability property is knowing whether a subscriber can receive RCS.

You can view this directly in the ****SMS marketing**** subscription box on a profile.

![](https://klaviyo.zendesk.com/hc/article_attachments/41072989960091)

The metadata includes an ****Is RCS capable**** field, which will display **True** or **False**.

- **True** means the subscriber’s device supports RCS.
- **False** means the subscriber’s device does not support RCS.

****Note:**** The Is RCS capable field only appears if the account has activated RCS and the profile is actively subscribed to SMS marketing.

## ****Creating an RCS segment****

You can use Klaviyo’s [segment builder](https://help.klaviyo.com/hc/en-us/articles/115005237908) to create a segment of subscribers who can receive RCS messages.

1. Navigate to Lists & segments in your Klaviyo account.
2. Select Create list / segment and choose Segment.
3. Enter a descriptive name, such as RCS.
4. In the segment builder, set the conditions as follows:
   1. Person ‘can receive’ ‘sms marketing’
   2. because person ‘Subscribed’
   3. and ‘is RCS capable’ is ‘True’

Your segment should look like this:

![](https://klaviyo.zendesk.com/hc/article_attachments/41072989961243)

Creating a dedicated RCS segment ensures that you only target contacts who have both opted in to SMS marketing and are capable of receiving RCS messages.

## ****Creating an SMS segment****

If you want to create a segment for subscribers who can receive SMS but not RCS, simply change the last condition (is rcs capable) to is ‘False’.

This segment ensures that SMS campaigns are only sent to contacts who cannot receive RCS.

## ****Using conditional splits in flows and campaigns****

You can also use the ****RCS capability property**** when creating ****conditional splits**** in flows and omnichannel campaigns. This allows you to branch your automation based on whether a contact can receive RCS, ensuring the right message type is delivered.

For example:

- If a person ****is RCS capable = True****, send an RCS message.
- Otherwise, perform another action as opposed to sending an SMS fallback.

Your split should look like this:

![](https://klaviyo.zendesk.com/hc/article_attachments/41073018903707)