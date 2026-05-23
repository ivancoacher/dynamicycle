---
id: 41073540219547
title: "RCS Pricing"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41073540219547-RCS-Pricing"
section: "RCS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: en
---

## ****RCS Agent Registration Fees****

Klaviyo does not currently charge any RCS agent fees in any country. However, fees may be introduced in the future for agents registered in the US only.

## ****RCS Message Rates****

#### Pricing Categories

RCS messages are priced based on content type and region. There are two pricing categories:

- ****Basic RCS**** - for basic, text-only messages (limits vary by region)
- ****Single RCS**** - for rich messages with interactive elements

To break down pricing categories, we've laid out all the types of RCS messages you can send via Klaviyo and how they are priced. Note that pricing for text-only messages that are longer than 160 characters or contain quick actions varies slightly by region.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ****Text-only**** | ****Text-only with quick actions**** | ****Card**** | ****Card Carousel**** |
| ****Description**** | A text-only message | A text-only message with up to 11 quick actions.  Quick Actions appear as suggestion chips below the message. Actions supported:   - Visit link - Quick reply - allowing the recipient to send a predefined response back to you. | A card template with at least one following elements:   - Title - Description - Media attachment (image or video)   A card can contain up to 4 of its own quick actions. When a quick action is attached to a card, it's called a button. | Up to 10 cards in a swipe-able carousel. |
| ****Pricing category**** | US: Basic RCS  Rest of World:   - up to 160 chars: Basic RCS - >160 chars: Single RCS | US: Basic RCS  Rest of World: Single RCS | Single RCS | Single RCS |
| ****Text character limit**** | up to 3,072 chars per message | up to 3,072 chars per message | Title: up to 200 chars  Description: up to 2,000 chars | Title: up to 200 chars  Description: up to 2,000 chars |
| ****Buttons**** | No | No | Yes  Up to 4 per card. Labels can be up to 25 chars. | Yes  Up to 4 per card. Labels can be up to 25 chars. |
| ****Quick Actions**** |  | Yes  Up to 11 per message. Labels can be up to 25 chars. | Yes  Up to 11 per message. Labels can be up to 25 chars. | Yes  Up to 11 per message. Labels can be up to 25 chars. |
| ****Media**** | No | No | Yes (image or video) | Yes (image or video) |

#### RCS Message Rates

Credit usage varies by message type and country, but all RCS messages will draw from your existing SMS credit balance.

****The table below outlines credit usage and estimated costs.****

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ****Country**** | ****SMS**** | ****MMS**** | ****Basic RCS**** | ****Single RCS**** |
| Austria | 4 | N/A | 6 | 6 |
| Denmark | 7 | N/A | 8 | 11 |
| France | 7 | N/A | 10 | 10 |
| Germany | 12 | N/A | 9 | 10 |
| Netherlands | 12 | N/A | 12 | 15 |
| Norway | 8 | N/A | 8 | 22 |
| Italy | 7 | N/A | 1 | 2 |
| Poland | 3 | N/A | 4 | 7 |
| Spain | 5 | N/A | 5 | 12 |
| Sweden | 6 | N/A | 6 | 9 |
| United Kingdom | 5 | N/A | 6 | 8 |
| United States | 1 | 3 | 1\* | 3 |

**\*Basic RCS in the US is billed in 160-character segments, similar to SMS. This means longer messages will consume more credits. For example, a Basic RCS message with 161 characters will be charged as 2 credits.**

****Notes:****

1. All credits are deducted from your SMS credit balance.
2. Fallback to SMS/MMS occurs automatically when RCS is not supported on the recipient’s device or network.
3. Pricing is subject to change if carrier or network costs increase, but we will always provide at least 30 days’ notice before any price updates go into effect.
4. These are all the countries where both RCS is supported and Klaviyo currently supports SMS. We’ll add RCS in the remaining countries as it becomes available.

#### ****More characters available per message****

One of the key advantages of RCS over SMS is the additional characters available within each message. Since RCS messages include built in branding and opt-out functionality, there is no need to include an org-prefix or opt-out instructions in the message body. This gives you roughly 40 additional characters per message.

In addition, unlike SMS, emojis in RCS do not reduce the character limit from 160 to 70. This allows you to create richer, more engaging messages without sacrificing space for your core content.

****Example 1 (text-only)****

****SMS message:****

- ****Recipients:**** 100,000 US recipients
- ****Copy:****
  - Klaviyo: Your summer essentials are here! Enjoy 25% OFF across all categories until midnight. Free shipping on orders over £50. Shop now at https://kav4.io/XXXXXX. Reply STOP to opt out.
- ****Characters:**** 185 (2 x SMS segments)
- ****Credits used:**** 200,000 (2 x 100,000)
  - **Note: Credit usage in these examples is based on US rates. Actual credits may vary by country.**

    ****RCS message:****
- ****Recipients:**** 100,000 US recipients
- ****Copy:****
  - Your summer essentials are here! Enjoy 25% OFF across all categories until midnight. Free shipping on orders over £50. Shop now at https://kav4.io/XXXXXX.
- ****Characters:**** 153 (1 x Basic RCS)
- ****Credits used:**** 100,000 (1 x 100,000)
  - **Note: Credit usage in these examples is based on US rates. Actual credits may vary by country.**

    ✅ ****Result:**** Sending the same content over SMS costs twice as much, since each message must include an org prefix and opt-out instructions.

    ****Example 2 (emojis & special characters)****

    ****SMS message:****
- ****Recipients:**** 100,000 US recipients
- ****Copy:****
  - Klaviyo: 🏖️ Your summer essentials are here! Enjoy 25% OFF across all categories until midnight ⏰. Free shipping on orders over £50. Shop now 👉 https://kav4.io/XXXXXX. Reply STOP to opt out.
- ****Characters:**** 191 (3 x SMS segments)
  - **Note: Emojis and special characters reduce the SMS segment character limit to 70.**
- ****Credits used:**** 300,000 (3 x 100,000)
  - **Note: Credit usage in these examples is based on US rates. Actual credits may vary by country.**

    ****RCS message:****
- ****Recipients:**** 100,000 US recipients
- ****Copy:****
  - 🏖️ Your summer essentials are here! Enjoy 25% OFF across all categories until midnight ⏰. Free shipping on orders over £50. Shop now 👉 https://kav4.io/XXXXXX.
- ****Characters:**** 159 (1 x Basic RCS)
  - **Note: Emojis and special characters don’t reduce the RCS segment character limit.**
- ****Credits used:**** 100,000 (1 x 100,000)
  - **Note: Credit usage in these examples is based on US rates. Actual credits may vary by country.**

✅ ****Result:**** Sending the same content over SMS costs three times as much, since emojis and special characters reduce the SMS character allowance.