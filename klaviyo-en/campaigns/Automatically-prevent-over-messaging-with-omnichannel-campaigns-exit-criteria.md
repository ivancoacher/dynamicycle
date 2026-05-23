---
id: 43671905324187
title: "Automatically prevent over-messaging with omnichannel campaigns exit criteria"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/43671905324187-Automatically-prevent-over-messaging-with-omnichannel-campaigns-exit-criteria"
section: "Getting started with campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-05-11T12:54:29Z"
language: en
---

## You will learn

Learn about exit criteria in omnichannel campaigns, including what they are and how they automatically remove customers from campaigns after they convert.

Exit criteria helps prevent over-messaging by automatically removing customers from multi-day omnichannel campaigns, such as product drops, flash sales, and loyalty pushes, once they meet the defined conversion conditions. This ensures that converted customers no longer receive promotional messages, creating a smoother experience and improving overall campaign performance.

## Before you begin

This article covers how to set up exit criteria for omnichannel campaigns. If this is your first time creating a campaign, [learn how to create and send an email campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847).

## How it works

1. Select a conversion metric for your campaign.
2. Klaviyo records the campaign start date when the earliest message in the entire omnichannel campaign is sent.
3. If a profile meets the conversion metric at any point after the first message is sent, they are automatically excluded from all remaining messages in the campaign.

## Example: Sneaker Drop Launch

- Day 1 9:00 AM Email: Early access message
- Day 1 1:00 PM SMS: Reminder message
- Day 2 9:00 AM Email: Next day follow-up message

****Exit Condition: Placed Order****

A customer who purchases at 9:15 AM is automatically excluded from future messages in the campaign, including the 1:00 PM SMS Reminder and next-day 9:00 AM Email Follow-up.

## Configure Exit Criteria

1. Open or create an omnichannel campaign
2. Open campaign settings
   1. Option 1 - Click on the options menu in the upper right corner
      ![](https://klaviyo.zendesk.com/hc/article_attachments/43671905301019)
   2. Option 2 - Click on any audience block
   3. Click on the edit button in the campaign settings component
   4. ![](https://klaviyo.zendesk.com/hc/article_attachments/43671905301915)
      ![](https://klaviyo.zendesk.com/hc/article_attachments/43671928147099)
3. Toggle exit criteria on (Setting is off by default)
   ![](https://klaviyo.zendesk.com/hc/article_attachments/43671905312795)
4. Select a Conversion metric (Placed Order recommended)
   ![](https://klaviyo.zendesk.com/hc/article_attachments/43671928160155)
5. Click on the "X" to close the campaign settings

![](https://klaviyo.zendesk.com/hc/article_attachments/43671928163611)

****Exit criteria is locked once your campaign is sent****

Once the first message in a campaign has been sent, the exit criteria becomes locked and can no longer be changed or turned off for that campaign. Conversely, if exit criteria was not turned on before the first message was sent, they cannot be enabled for the remainder of the campaign.

Additionally, exit criteria temporarily locks when a message is scheduled, but it can be unlocked by reverting the scheduled message back to draft.

## Troubleshooting

- If exit criteria is grayed out, this means at least one message is scheduled or sent and the setting is locked.
- If you want to exclude profiles that converted ****before**** the start of the campaign, exclude them using the "Do not send" fields in the audience builder
- Custom conversion metrics can’t be used as conversion metric, so they won’t appear in the dropdown menu.