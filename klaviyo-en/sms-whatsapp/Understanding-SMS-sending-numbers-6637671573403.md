---
id: "6637671573403"
title: "Understanding SMS sending numbers"
source_url: "https://help.klaviyo.com/hc/en-us/articles/6637671573403-Understanding-SMS-sending-numbers"
section: "About sending numbers"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: "en"
---
Please note that only account Owners, Admins, and Managers have the ability to add and manage sending numbers.

## You will learn

Learn about the SMS sending numbers for every country that Klaviyo can send to, including what each number type can do.

## Sending number availability

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

Non-default sending numbers (i.e., long codes and short codes) require a paid plan. This also applies to Belgium & Hungary, where long codes are the only sending number.

## Sending number features

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ****MMS supported**** | ****\* Able to receive SMS**** | ****Verification or registration needed**** | ****Branded**** |
| Toll-free number | ✔ | ✔ | ✔ | ✖ |
| Branded sender ID | ✖ | ✖ | ✖ in most countries | ✔ |
| ✔ in some contries |
| Long code | ✖ in most countries | ✔ | ✖ in most countries | ✖ |
| ✔ in Australia | ✔ in some countries |
| Short code | ✔ | ✔ | ✔ | ✖ |
| Short code (vanity) | ✖ in most countries | ✔ | ✔ | \*\*Ɵ |
| ✔ in the US |

\* A sending number must be able to receive SMS in order to use:

- Double opt-in
- Keywords (including opt-out keywords like STOP)
- Tap-to-text
- Two-way messaging and conversations

****Social Auto-replies tap-to-text:**** Tap-to-text in [****Social Auto-replies****](https://help.klaviyo.com/hc/en-us/articles/41741460845339)requires a ****2-way**** sending number that can receive inbound SMS.

\*\* Vanity short codes allow you to pick your number, so you can pick numbers that work with your brand; however, they are still strings of numbers, meaning customers won’t know who’s texting them without some other indicator.

### Verification/registration

In many countries, wireless carriers require that you either register or verify your sending number. This is so carriers can check if you're a trusted sender.

The time it takes to verify or register your number varies by both the number type and the country. As examples:

- [Toll-free numbers](https://help.klaviyo.com/hc/en-us/articles/4415873897499) take 2 to 5 business days.
- [Long codes](https://help.klaviyo.com/hc/en-us/articles/26705180655003) take 1 to 3 business days in Australia, Ireland, and Belgium.
- [Branded sender IDs](https://help.klaviyo.com/hc/en-us/articles/14953787622427) take 7 to 10 business days in Australia and Ireland.
- [Short codes](https://help.klaviyo.com/hc/en-us/articles/26886941270171) take the longest amount of time, anywhere from:
  - 5 to 6 weeks (New Zealand).
  - 12 to 16 weeks (Canada).

Except for short codes, verifying or registering typically takes no more than 7 to 10 business days.

## Sending number costs

Toll-free numbers, branded sender IDs, and long codes are all included free of charge.

Short codes and vanity short codes are the only sending numbers that require an additional monthly cost, which varies depending on the country.

## Toll-free numbers

Toll-free numbers are the default sending numbers in Klaviyo for the US and Canada. They are automatically created as soon as you set up SMS.

The same toll-free number is used to send to both countries.

You should use a toll-free number if any of the following apply:

- You are new to SMS marketing.
- You send fewer than 300,000 messages at a time.
- You are mostly sending texts via flows or to small, segmented groups.
- You want to send images or GIFs to Canada.
  - Note: toll-free numbers are the only Canadian sending number that can send MMS.

Toll-free numbers must be [verified](https://help.klaviyo.com/hc/en-us/articles/4415873897499), although not all industries are eligible. We do not recommend sending from unverified toll-free numbers. Toll-free number verification typically takes 2 to 5 business days.

****How to get a toll-free number verified****

When you turn on SMS, you will be asked for [information](https://help.klaviyo.com/hc/en-us/articles/4415873897499) in order to receive a toll-free number. After you fill out this information, Klaviyo will assign you a number and automatically submit it for verification.

****Releasing a toll-free number****

Releasing a toll-free number is not recommended. Released toll-free numbers cannot be recovered.

The same toll-free number is used for both the US and Canada. If you release the toll-free number shown for the US, it will remove the number for Canada as well.

The only time when you might want to release your toll-free number is if you already have a short code for both the US and Canada.

## Branded sender IDs

[Branded sender IDs](https://help.klaviyo.com/hc/en-us/articles/14953787622427) (also known as alphanumeric IDs) are the default option in Klaviyo for the UK, Ireland, Germany, France, Austria, Spain, Switzerland, Denmark, Norway, Finland, Sweden, Italy, Portugal, Poland, and Australia. The same branded sender ID is used in all countries.

A branded sender ID is best for your business if branding is important to you.

There are 3 main benefits of branded sender IDs; they:

- Can be customized to fit your brand, so recipients always know who their messages are coming from.
- Are available to more countries than long codes.
- Send faster than long codes, so they are better for larger campaigns.

There is a registration process for branded sender IDs in Australia, which takes 7–10 days to complete. You will not be able to send to Australian subscribers until your number is registered; however, you can still use the branded sender ID to send to recipients in other countries (such as the UK).

With branded sender IDs, your customers can opt out via an unsubscribe link.

### Branded sender ID limitations

The downside of this ID is that it cannot receive messages, so your recipients cannot text you back. This means that you cannot use the following Klaviyo functionality with a branded sender ID:

- Click-to-text forms and email banners
- Subscribe and unsubscribe keywords
- SMS conversations/two-way messaging
- Double opt-in

## Long codes

A [long code](https://help.klaviyo.com/hc/en-us/articles/26705180655003) is only good for reaching subscribers in 1 specific country. As an example, if you only have an Australian long code, you cannot use this number to send to Ireland.

Unlike branded sender IDs, long codes are able to receive inbound messages, which gives you more flexibility in what you can do with SMS.

You will be able to use:

- Double opt-in
- Click-to-text forms and email banners
- Subscribe keywords
- SMS conversation/two-way messaging
- Can send MMS in Australia
- Can send to Belgium

This allows your customers to opt-in using subscribe keywords, get 1-to-1 support, share their preferences and interests, etc.

### Long code limitations

Compared to branded sender IDs, long codes have a few cons, including:

- They are not branded. The number will look like any other number, and customers won’t automatically know who’s texting them.
- Long codes send slower than branded sender IDs.
- In Australia and Ireland, long codes must undergo a verification process. This process takes 1–3 business days, and you cannot send until the number is approved.

## Short codes (vanity and non-vanity)

All [short codes](https://help.klaviyo.com/hc/en-us/articles/26886941270171) are exactly the same, except for 2 things:

- Vanity short codes allow you to choose your number (as long as it’s available).
  Note that each country keeps its own list of available vanity short codes.
- Non-vanity short codes are only available in the US, whereas vanity short codes are available in the US, Canada, the UK, and New Zealand.

To keep things simple, we’ll use “short codes” to discuss both of these number types.

Short codes only send to recipients in 1 specific country. If you plan to send to multiple countries, you will need to get a separate short code and have it approved for each new country where you want to send. For instance, if you have a short code for the UK, you cannot use the same short code in Australia, New Zealand, etc.

### Who should get a short code

Short codes are best for high-volume senders, like those who meet either of the following conditions:

- If you send SMS campaigns to more than 30,000 people.
- You send more than 300,000 messages at a time (e.g., via flows or multiple, simultaneous campaigns).

Learn more about [when to get a short code](https://help.klaviyo.com/hc/en-us/articles/14476797072795).

Not all businesses and industries are eligible for a short code. You must apply for them and be approved. This approval process takes several weeks, so even if you are eligible, you cannot instantly start sending on a short code.

## FAQs

### What happens when you have multiple sending numbers?

You can have 1 Klaviyo account with multiple sending numbers. Klaviyo automatically detects where each recipient is located and then sends to them using a number for that country.

Say that you have a toll-free number for the US and a long code for the UK. To send to all of your subscribers, you don't have to set up multiple campaigns. Instead, you only need 1 campaign, as Klaviyo will automatically use your toll-free number for recipients with a US number and your long code for recipients with a UK number.

### What happens if you change numbers to a short code?

When you get a short code, it becomes the primary sending number for the country where it was approved. For instance, if you're only sending to the US, your short code will replace the toll-free number as the primary sending number.

Note that if you use a tap-to-text form in either the US, Canada, or both, you’ll need to update the form to apply only to 1 country. For example:

- Update the **Sending region** to **United States** (not **United States, Canada**).
- Change the targeting behaviour to show the form only in the United States.

You can then clone the form and change these aspects to apply only to Canada.

### What happens if you have a toll-free number and a short code?

In this case, the short code will send all messages to the country where it was approved, while the toll-free number will send to other countries.

### What happens if you have a long code and branded sender ID?

If you have both a long code and branded sender ID, the long code typically takes precedence.

The only exception is in Australia when the branded sender ID is registered and the long code is not. However, once the long code is registered, it takes precedence.