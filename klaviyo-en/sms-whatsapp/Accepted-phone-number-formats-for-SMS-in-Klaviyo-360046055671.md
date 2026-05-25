---
id: "360046055671"
title: "Accepted phone number formats for SMS in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360046055671-Accepted-phone-number-formats-for-SMS-in-Klaviyo"
section: "Import SMS contacts"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: "en"
---
## You will learn

Learn which phone number formats Klaviyo accepts when importing phone numbers for SMS marketing.

## Accepted phone number formats

You can use several different formats for phone numbers with Klaviyo.

The following applies to Klaviyo's list import tool only. If you're using an API call, note that Klaviyo only accepts the E.164 format.

|  |  |  |
| --- | --- | --- |
| ****Format**** | ****Example without country code**** | ****Example with country code**** |
| E.164 | 2345678901 | +12345678900 |
| 2-345-678-901 | +12-345-678-900 |
| 2 345 678 901 | +12 345 678 900 |
| RFC3966 | tel: 2345678901 | tel: +12345678900 |
| E.123 national notation | (234) 567 8901 | (+1234) 567 8900 |
| 2345678901 | +12345678900 |
| E.123 international notation | 2 345 678 901 | +12 345 678 900 |
| 234 567 8901 | +1 234 567 8900 |

When importing phone numbers, you must include the country. Generally, the best way to do so is by adding a column labeled **Country**.

The RFC3966 format comprises the prefix “tel:” followed by numbers. The numbers themselves do not need to be in a certain format.

Branded sender IDs are not accepted, but you will get one free with your SMS plan.

## Importing phone numbers

In order for consent to be applied to a phone number, we recommend including the following columns:

- Email (if known)
- Phone number (required)
- Country
- First name
- Last name
- [Timestamp](https://help.klaviyo.com/hc/en-us/articles/115005253428)

This way, the file contains all the necessary and helpful information. Not only will consent be applied properly, but you'll avoid creating duplicate profiles.

For more details, read [upload a list of SMS contacts](https://help.klaviyo.com/hc/en-us/articles/360035428731).

### Including a country

You must indicate the country for a phone number to be accepted for SMS. You can either:

- Include a column for the country
  or
- Add a country code at the beginning of the phone number
  - Note that you have to add an apostrophe before the plus sign (e.g., '+) in Google Sheets and Excel due to formatting issues.

For instructions on formatting countries in CSVs, please see [how to include a country for an SMS import](https://help.klaviyo.com/hc/en-us/articles/5306587861531).

|  |
| --- |
| ****With the country column**** |
| ![Sample CSV file for importing SMS consent into Klaviyo when there’s a country column](https://klaviyo.zendesk.com/hc/article_attachments/28720893303195) |

|  |
| --- |
| ****With the country code**** |
| ![Sample CSV file for importing SMS consent into Klaviyo when there’s a country code](https://klaviyo.zendesk.com/hc/article_attachments/28720848243995) |

![mceclip0.png](https://klaviyo.zendesk.com/hc/article_attachments/28720848247579)

## How Klaviyo handles symbols and spaces

Klaviyo can also handle certain typos and common symbols. For instance, if a phone number contains a symbol, extra space, or letter, Klaviyo will remove this when a phone number is added to a profile. The following will all be corrected to the E.164 format as +12345678900:

- +12/345(678)\*900
- +12()\*- 345678900
- abcde()\*()++12 345 678 900
- +1-2-3-4-5-6-7-8-9-0-0

## Additional resources

- Learn more about how to import SMS subscribers:
  - [Filter opted-out SMS contacts from CSVs](https://help.klaviyo.com/hc/en-us/articles/5302764979611)
  - [Upload a list of SMS contacts](https://help.klaviyo.com/hc/en-us/articles/360035428731)
- Find out how to [collect SMS consent](https://help.klaviyo.com/hc/en-us/articles/360035056972)