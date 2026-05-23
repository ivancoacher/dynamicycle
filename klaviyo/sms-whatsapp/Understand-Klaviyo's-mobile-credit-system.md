---
id: 13502982552347
title: "Understand Klaviyo's mobile credit system"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/13502982552347-Understand-Klaviyo-s-mobile-credit-system"
section: "Set up SMS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:27Z"
language: en
---

Learn about Klaviyo’s billing system for text messages, such as why countries and channels have different credit values and what’s included in these credits.

If you are trying to understand how many SMS or MMS messages you receive when purchasing credits, please use the [mobile messaging credit calculator on Klaviyo's pricing page](https://www.klaviyo.com/pricing).

## Before you begin

Depending on where you send, the credit per text message varies.

Note that text messages can be either an SMS or MMS. The main difference is that MMS messages contain either an image or GIF and allow for more characters than SMS messages.

### North America

|  |  |  |
| --- | --- | --- |
|  | ****SMS**** | ****MMS**** |
| Canada | 3 | 5 |
| United States | 1 | 3 |

###

### Europe

|  |  |  |
| --- | --- | --- |
|  | ****SMS**** | ****MMS**** |
| Austria | 4 | N/A |
| Belgium | 11 |
| Denmark | 7 |
| Finland | 9 |
| France | 7 |
| Germany | 12 |
| Hungary | 8 |
| Ireland | 9 |
| Italy | 7 |
| Luxembourg | 11 |
| Norway | 8 |
| Poland | 3 |
| Portugal | 3 |
| Spain | 5 |
| Sweden | 6 |
| Switzerland | 5 |
| The Netherlands | 12 |
| United Kingdom | 5 |

### Oceania

|  |  |  |
| --- | --- | --- |
|  | ****SMS**** | ****MMS**** |
| Australia | 4 | 15 |
| New Zealand | 10 | N/A |

When it comes to this system, you may have questions. We answer all of these in the following sections:

- [What are credits?](#h_01GV61X9VB7RTJEQ3N3KRJTDZJ)
- [Why does Klaviyo use credits rather than a price?](#h_01GV61Y1NGB4D8Z8CVF77PDEVB)
- [Why does the credit differ by country?](#h_01GV61Y8RFVWC3XJZ9P3EYHHQ1)
- [Why is MMS higher than SMS?](#h_01GV61YK1P9BH5GBDYZNVE95HD)
- [What messages cost credits with Klaviyo?](#h_01GV61YT08JVT1SRSEFYKMNPXQ)

## What credits are

Credits are the cost per SMS or MMS for a single recipient.

Say that you want to send 1 SMS to 10 people in Australia. In that case, that send will cost 40 credits.

****When do credits renew?****

Credits renew on a monthly basis. The exact date depends on your personal billing cycle.

To view when your billing cycle renews:

1. Click your organization name in the lower-left corner.
2. Click ****Billing****.
3. Review the dates for your cycle, which are at the top of the Overview tab.

****Do credits roll over?****

No, you have a set amount of credits per month, and these credits do not roll over.

However, you can upgrade or downgrade each month to suit your business needs. If you find that you have credits left over at the end of the month, simply downgrade to a lower plan. Or, if you’re not planning any promotions for the upcoming month, you can downgrade before then so that you’re not paying for credits that you don’t need.

### Message character limits

SMS allows up to 160 characters, or 70 characters when there's an [emoji or special character](https://help.klaviyo.com/hc/en-us/articles/17275332265627). MMS always allows 1600 characters (the limit does not change if you have an emoji or special character).

If you exceed this character amount for a send, your SMS will have multiple segments, despite still showing a single message on the recipient's phone. To render these segments in the correct order, an invisible header of about 7 characters is added to all message segments. This means that rather than 160 characters, you'll instead have a 153 character limit.

### Calculate the total credits for a send

The formula for determining the total number of credits is:

Number of credits x Recipients x Message segments

Say you're sending to 100 people: 50 are in Ireland and 50 in the UK. Your message also counts as 2 message segments. In this case, the math would look like:

- 9 (Ireland credit) x 50 x 2 = 900
  +
- 5 (UK credit) x 50 x 2 = 500
  =
- 1400 total credits

****Why is my SMS showing as more credits than the table lists?****

This has to do with how SMS messages are transmitted.

The limit for SMS messages is 160 characters normally, and 70 characters if the text has an emoji or special character.

When you send an SMS that exceeds the limit, it is automatically broken up into smaller messages (called message segments) that are sent individually. Most carriers will reassemble the messages so that they appear as one text or “bubble” on the recipient’s device.

So while it appears like the SMS is a single message, it can actually be 2 (or more) message segments, making it cost more credits.

You can see how many segments your SMS is for each country using the **i** button from the message creation screen.

![A menu displaying the credit counts for several countries](https://klaviyo.zendesk.com/hc/article_attachments/33627691473819)

****Where can I see how many credits I used?****

You can see how many credits you’ve used in your account overview:

1. Click your organization name in the lower-left corner.
2. Click ****Billing****.
3. View your remaining credits in the **SMS** section.

   ![SMS credit usage for an example account](https://klaviyo.zendesk.com/hc/article_attachments/28704478202651)

There, look for the SMS section to see how many credits you’ve used this billing cycle and how many you have left.

## Why Klaviyo uses credits rather than price

Klaviyo uses credits to provide a transparent experience. It includes all carrier fees, so you don't pay anything on top of the credit itself. In addition, you don't need to pay to unlock additional features in Klaviyo.

Other SMS providers offer a price per message rather than using a credit system. However, usually there are separate carrier or platform fees, which are additional fees on top of the price per message.

These extra fees vary depending on the platform, carrier, region, and even phone number type. Carrier fees, for instance, can jump 20% per year. This makes it difficult to know exactly how much a campaign will cost you or plan your budget for the month.

Since Klaviyo includes these carrier fees, you know exactly how many credits you’ll use before you send.

### What are carrier fees?

Carrier fees are surcharges that mobile carriers (e.g., Verizon, Vodafone, etc.) apply to a business’s outbound and, in some cases, inbound text messages.

These fees change depending on:

- If the message is an SMS or MMS
- Whether the sending number is a toll-free number or short code
- Which country the message was sent to (UK, US, etc.)

Think of it like paying for a plane ticket, but after arriving at the airport, you realize you need to pay for a carry-on bag as well.

****Do I need to pay carrier fees with Klaviyo?****

No, the only thing you need to pay for is the credit itself. There are no extra message fees with Klaviyo. Carrier fees are included in the credit, and there are no platform fees.

## Why the credits are different in each country

In every country, carriers charge differently for SMS. Think of it like mailing a package. The price to mail a box in Canada is different than it is for the same box in New Zealand.

For SMS, the reasons are based on which carriers are available in that country, the network itself, and other factors. For instance, in 2022, the carrier fees in Australia and New Zealand were:

- Australia: $ 0.0515
- New Zealand: $0.1050

As you can see, New Zealand was more than double the price of Australia.

This is why the credits Klaviyo charges have to change from country to country. If carrier pricing increases or decreases in the future, credit amounts will change accordingly.

## Why MMS is higher than SMS

No matter what SMS platform you’re using, MMS always costs more to send than SMS. MMS includes multimedia content, which consumes a lot more data than a plain-text message.

Extra infrastructure is needed to send a multimedia message. This is why an MMS message not only costs more, but it also has different [sending limits](https://help.klaviyo.com/hc/en-us/articles/6456860853275-) than an SMS message.

Using Klaviyo, MMS simply requires more credits. With that, you can send images or GIFs under 600 KB and up to 1600 characters. However, not all SMS providers include the text in the cost of an MMS.

## What messages cost credits with Klaviyo

Whether or not a message uses credits depends on what type of message it is. For instance, certain auto-responses and keyword responses cost credits, while others don’t.

The table below lists each message type and whether or not it costs credits.

|  |  |  |
| --- | --- | --- |
| ****Message type**** | | ****Does it cost credits?**** |
| Inbound messages (SMS messages sent by the customer to your business’ number) | | No |
| Campaign | | Yes |
| Flow | | Yes |
| Conversation (outbound only) | | Yes |
| Auto-responses and keyword responses | When no keyword is recognized | Yes |
| Opt-in messages sent after someone signs up for SMS (e.g., one-time code, double opt-in confirmation, etc.) | No |
| YES, Y, OUI, O | No |
| HELP, INFO, AIDE | No |
| STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT, ARRET, DESABONNER, ANNULER, FIN | No |
| START, UNSTOP, NONARRET | No |
| Skipped messages (i.e., Klaviyo didn’t send the message) | Smart sending, no SMS consent, etc. | No |
| [Failed to deliver messages](https://help.klaviyo.com/hc/en-us/articles/1260806260849#evaluate-your-failed-deliveries6) (i.e., the message was sent, but not delivered) | Message blocked, device disconnected, etc. | Yes |
| [SMS preview](https://help.klaviyo.com/hc/en-us/articles/360035661191#h_01HCJKFZS85112S8YE4PNCRW2F) messages | | No |

## Find the cost of an SMS plan

To check the cost of other SMS plans:

1. Select your account name in the bottom left.
2. Navigate to ****Billing > Change plan****.
3. Scroll down to the **Mobile Messaging** section.
4. Open the dropdown.
   ![View of SMS plans in Klaviyo's checkout page](https://klaviyo.zendesk.com/hc/article_attachments/28704478204699)
5. Select a plan to view its cost.

## Additional resources

- [Understand how Klaviyo billing works](https://help.klaviyo.com/hc/en-us/articles/115000976672)
- [How to change your plan in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/8356575957275)