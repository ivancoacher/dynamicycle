---
id: 4404274419355
title: "How to set up SMS in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4404274419355-How-to-set-up-SMS-in-Klaviyo"
section: "Set up SMS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:58Z"
language: en
---

Only Owners, Admins, and Managers can set up SMS.

Learn how to enable SMS in Klaviyo. These steps apply if you have already set up email in your Klaviyo account. If you are going through the setup wizard for both email and SMS, the steps may be different.

You must turn on SMS and have a sending number before you can do any of the following:

- Import or collect SMS subscribers
- Send SMS or MMS messages

Note that [not all industries are eligible for SMS](https://help.klaviyo.com/hc/en-us/articles/4401822831771).

## Before you begin

### Number types

Depending on the country you’re sending to, you may have access to one or more different types of sending numbers.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ****Country**** | ****\*Toll-free Number**** | ****\*Branded SID**** | ****Long Code**** | ****Short Code**** | ****Short Code (Vanity)**** |
| ****AT**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****AU**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****BE**** | ✖ | ✖ | ✔ | ✖ | ✖ |
| ****CA**** | ✔ | ✖ | ✖ | ✖ | ✔ |
| ****CH**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****DE**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****DK**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****ES**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****FI**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****FR**** | ✖ | ✔ | ✖ | ✖ | ✖ |
| ****HU**** | ✖ | ✖ | ✔ | ✖ | ✖ |
| ****IE**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****IT**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****LU**** | ✖ | ✔ | ✖ | ✖ | ✖ |
| ****NL**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****NO**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****NZ**** | ✖ | ✖ | ✖ | ✖ | ✔ |
| ****PL**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****PT**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****SE**** | ✖ | ✔ | ✔ | ✖ | ✖ |
| ****UK**** | ✖ | ✔ | ✔ | ✖ | ✔ |
| ****US**** | ✔ | ✖ | ✖ | ✔ | ✔ |

An asterisk (\*) indicates that this number type:

- Is a default sending number in Klaviyo and is available for free to all accounts.
- Uses the same number for all countries where it’s available.
  - For instance, the same branded sender ID collects consent and sends SMS to the UK, Germany, Australia, etc.

Non-default sending numbers (i.e., long codes and short codes) require a paid plan. This also applies to Belgium and Hungary, where long codes are the only sending number.

****Default sending numbers****

With both branded sender IDs and toll-free numbers, the same number is used to collect consent and send to multiple countries. They do so automatically, so if you don't want to collect consent or send to a certain country, target your forms by country, create location-based segments, and split your flows.

Separating by country is also key if you want to know where to use your SMS credits. Since credits vary by country, targeting based on location helps you track how much you spent, who engaged, and your ROI on a per-message basis. This way, you'll know where and with who to send SMS messages to.

The table below lists all of the countries where these numbers will send to.

|  |  |
| --- | --- |
| ****Branded sender ID**** | ****Toll-free number**** |
| Australia | USA |
| Austria | Canada |
| Denmark |  |
| Finland |  |
| France |  |
| Germany |  |
| Ireland |  |
| Italy |  |
| Luxembourg |  |
| Netherlands |  |
| Norway |  |
| Poland |  |
| Portugal |  |
| Spain |  |
| Sweden |  |
| Switzerland |  |
| UK |  |

Klaviyo will provide you with a toll-free number and branded sender ID; you simply have to complete the SMS wizard to get these numbers. If you want to use another number, finish this setup process first so you can start collecting consent and then request the other number.

## Turn on SMS

If you didn't set up SMS during the Klaviyo setup wizard, you can turn it on in the SMS settings page.

![](https://fast.wistia.com/embed/medias/dx8q97zx8c/swatch)

1. Click on the name of your account in the lower left-hand corner.
2. Navigate to ****Settings > SMS****.
3. Click ****Set up SMS for free****.
   If you don't see this button, click ****Add country**** and choose the countries where you want to start sending.
4. In the modal that pop ups, select the countries where you want to use SMS (check all that apply).
   ![Step to choose which countries where you want to send SMS](https://klaviyo.zendesk.com/hc/article_attachments/28722596951835)
5. Click ****Next****
6. Fill out your company information.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47593800502811)
7. Review or pick your sending numbers. For a full comparison of the numbers, please see our article on [SMS sending numbers](https://klaviyo.zendesk.com/hc/en-us/articles/6637671573403), but key highlights include:

   - Sometimes, the same sending number is used for multiple countries, unless you have another number that takes precedence.
     - The same toll-free number is used in the US and Canada, except if you have a short code for one or both countries.
     - The same branded sender IDs is used for every country where it's available, except if you have a long or short code in a specific country.
     - Short codes and long codes are always tied to a specific country.
   - Some countries only offer 1 type of sending number:
     - For Belgium, the only option is to request a long code.
     - For New Zealand: the only option is to apply for a short code.![Modal to create a branded sender ID in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28722558533659)
8. Click ****Next****.
9. Certain countries require that a sending number is either verified or registered before it can be used. This includes:

   - All [short codes](https://help.klaviyo.com/hc/en-us/articles/26886941270171) (regardless of country).
   - [Toll-free numbers](https://help.klaviyo.com/hc/en-us/articles/4415873897499) in the US or Canada.
     - Note that there's no action needed to start the verification process for toll-free numbers.
   - [Branded sender IDs](https://help.klaviyo.com/hc/en-us/articles/14953787622427) in Australia and Ireland.
     - Note that Ireland requires that you register via their national registry, [ComReg](https://senderid.comreg.ie/).
   - [Long codes](https://help.klaviyo.com/hc/en-us/articles/26705180655003) in Australia, Belgium, and Ireland.
10. Choose one of the following next steps:

- Create a sign-up form (best for those who are new to SMS).
- Upload a list of previous SMS subscribers (best for those switching from another SMS provider).

Note that if you're using UTM tracking in Klaviyo already, we also recommend navigating to ****Settings > Other > UTM tracking**** and adjusting the UTM medium to be **Message type.** Otherwise, SMS message may not be tracked properly.

## Outcome

You'll now be able to start collecting SMS subscribers and sending them text messages. Before you do so, though, learn [best practices for SMS compliance](https://academy.klaviyo.com/en-us/courses/best-practices-for-sms-compliance/2011622) on the Academy.