---
id: "40116442241179"
title: "Understand WhatsApp billing in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/40116442241179-Understand-WhatsApp-billing-in-Klaviyo"
section: "Understand WhatsApp with Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-05-11T12:54:37Z"
language: "en"
---
Find out how Klaviyo bills for WhatsApp, including the cost of messages and how to purchase sends in Klaviyo.

It’s important to know that unlike channels like email or SMS, WhatsApp is privately owned by Meta. This means that Meta decides on the entire WhatsApp experience: from who can use it to the base pricing model.

## What type of messages are charged?

As of July, 2025, Meta is moving away from charging by conversation toward charging by template. However, they still charge different prices based on the type of message (marketing vs. transactional) as well as what country the message is being sent to.

So what is the per-template system? It means that there is a charge for any delivered marketing or utility/transactional template message.

## About the billing system in Klaviyo

In Klaviyo, WhatsApp messages are billed as credits using the same system as SMS. After you purchase a plan with credits, you can use all of them for SMS, WhatsApp, or any combination of both.

### How many credits are WhatsApp messages?

The credit per WhatsApp message varies based on:

- The country you’re sending to.
- The type of message it is:
  - Marketing (also called “promotional”)
  - Transactional (also called “utility”)
  - Service

| ****Country**** | ****Marketing**** | ****Transactional**** |
| --- | --- | --- |
| Argentina | 11 | 7 |
| Brazil | 12 | 2 |
| Chile | 16 | 4 |
| Colombia | 3 | 1 |
| Egypt | 20 | 1 |
| France | 26 | 6 |
| Germany | 25 | 10 |
| India | 2 | 1 |
| Indonesia | 7 | 4 |
| Israel | 7 | 1 |
| Italy | 13 | 6 |
| Malaysia | 16 | 3 |
| Mexico | 8 | 2 |
| Netherlands | 30 | 9 |
| Nigeria | 10 | 2 |
| Pakistan | 9 | 1 |
| Peru | 13 | 4 |
| Saudi Arabia | 9 | 3 |
| South Africa | 7 | 2 |
| Spain | 11 | 4 |
| Turkey | 2 | 1 |
| United Arab Emirates | 7 | 3 |
| United Kingdom | 10 | 4 |

If your country is not listed in the table above, it falls under one of the following regions, which were grouped by Meta. Click on the region name to see the specific countries that are in that group.

****North America****

| ****Country**** | ****Marketing**** | ****Transactional**** |
| --- | --- | --- |
| Canada | 5 | 1 |
| United States |

****Africa****

| ****Country**** | ****Marketing**** | ****Transactional**** |
| --- | --- | --- |
| Algeria | 4 | 1 |
| Angola |
| Benin |
| Botswana |
| Burkina Faso |
| Burundi |
| Cameroon |
| Chad |
| Republic of the Congo (Brazzaville) |
| Eritrea |
| Ethiopia |
| Gabon |
| Gambia |
| Ghana |
| Guinea-Bissau |
| Ivory Coast |
| Kenya |
| Lesotho |
| Liberia |
| Libya |
| Madagascar |
| Malawi |
| Mali |
| Mauritania |
| Morocco |
| Mozambique |
| Namibia |
| Niger |
| Rwanda |
| Senegal |
| Sierra Leone |
| Somalia |
| South Sudan |
| Sudan |
| Swaziland |
| Tanzania |
| Togo |
| Tunisia |
| Uganda |
| Zambia |

****Asia Pacific****

| ****Country**** | ****Marketing**** | ****Transactional**** |
| --- | --- | --- |
| Afghanistan | 14 | 3 |
| Australia |
| Bangladesh |
| Cambodia |
| China |
| Hong Kong |
| Japan |
| Laos |
| Mongolia |
| Nepal |
| New Zealand |
| Papua New Guinea |
| Philippines |
| Singapore |
| Sri Lanka |
| Taiwan |
| Tajikistan |
| Thailand |
| Turkmenistan |
| Uzbekistan |
| Vietnam |

****Central and Eastern Europe****

| ****Country**** | ****Marketing**** | ****Transactional**** |
| --- | --- | --- |
| Albania | 16 | 7 |
| Armenia |
| Azerbaijan |
| Belarus |
| Bulgaria |
| Croatia |
| Czech Republic |
| Georgia |
| Greece |
| Hungary |
| Latvia |
| Lithuania |
| Moldova |
| North Macedonia |
| Poland |
| Romania |
| Serbia |
| Slovakia |
| Slovenia |
| Ukraine |

****Latin America****

| ****Country**** | ****Marketing**** | ****Transactional**** |
| --- | --- | --- |
| Bolivia | 14 | 2 |
| Costa Rica |
| Dominican Republic |
| Ecuador |
| El Salvador |
| Guatemala |
| Haiti |
| Honduras |
| Jamaica |
| Nicaragua |
| Panama |
| Paraguay |
| Puerto Rico |
| Uruguay |
| Venezuela |

****Middle East****

| ****Country**** | ****Marketing**** | ****Transactional**** |
| --- | --- | --- |
| Bahrain | 7 | 3 |
| Iraq |
| Jordan |
| Kuwait |
| Lebanon |
| Oman |
| Qatar |
| Yemen |

****Western Europe****

| ****Country**** | ****Marketing**** | ****Transactional**** |
| --- | --- | --- |
| Austria | 11 | 6 |
| Belgium |
| Denmark |
| Finland |
| Ireland |
| Norway |
| Portugal |
| Sweden |
| Switzerland |

## Service messages

Klaviyo does not bill for service messages, since these are not sent using WhatsApp templates. This includes messages sent through Keywords, [Automations](https://help.klaviyo.com/hc/en-us/articles/40116727375771) and [Inbox](https://help.klaviyo.com/hc/en-us/articles/360059002271).

However, if you use [a follow-up template](https://help.klaviyo.com/hc/en-us/articles/40116778911259) in Inbox to extend a conversation, that message will be billed as a template message.

****Example: Using free sending in an automation****
Let’s say you send a marketing message through a Campaign using a WhatsApp template that promotes a new product. Because this is a template message, it will be billed.

However, if that template includes a Quick Reply button (for example, “Show me more options”), and the customer taps it, this can trigger an Automation—such as a product recommendation flow. The messages sent through this Automation are service messages, not template messages, so they’re free.

## When you won’t be charged for WhatsApp messages

Some types of messages and delivery outcomes are not billable. These exceptions ensure you’re only charged for successful, billable template messages.

These billing exceptions are based on Meta’s current WhatsApp pricing policies and may change at any time. Klaviyo cannot guarantee that these message types will remain free if Meta updates its billing rules. [Learn more.](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)

- ****A message fails to deliver.****
  For example, failed delivery errors such as **Message Undeliverable** or **In order to maintain a healthy engagement ecosystem, the message failed to be delivered** are not billed.
- ****You send service messages.****
  Messages sent through Keywords, Automations, or Inbox that are not WhatsApp templates are free. However, if you use a follow-up template in Inbox to extend a conversation, that message is billed as a template message.
- ****You send a utility template within an active service window.****
  Utility templates that continue an existing customer conversation within the 24-hour service window are not billed again.
- ****A user starts a new conversation via a Click to WhatsApp Ad.****
  Any templates sent during the first 72 hours after the user’s initial message from a [Click to WhatsApp Ad](https://help.klaviyo.com/hc/en-us/articles/42146376607003) are free.

## Purchase credits for WhatsApp

To send WhatsApp messages through Klaviyo, you need credits. Every account starts with a free plan that includes 150 credits.

For contracted customers (those who are [manually billed](https://help.klaviyo.com/hc/en-us/articles/18745921973915)), reach out to your Klaviyo success representative to add credits to your plan. If you have credits already, you can use them to send WhatsApp messages.

If you’re not on a contract, you can get credits at any time. If you have an Mobile plan already, simply start using your credits to send WhatsApp messages or [get more credits by upgrading](https://help.klaviyo.com/hc/en-us/articles/8356575957275).