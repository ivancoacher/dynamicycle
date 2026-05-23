---
id: 7956171032091
title: "Basics: SMS compliance"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/7956171032091-Basics-SMS-compliance"
section: "Understand SMS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:05Z"
language: en
---

## You will learn

Get an overview of 7 important aspects of SMS compliance.

This advice is for informational purposes only and is neither intended as nor should be substituted for consultation with appropriate legal counsel and/or your organization’s regulatory compliance team.

## The 7 compliance basics for SMS

1. [Always get consent for SMS before texting anyone](#h_01GEF803FZAHSWR1NT8DY3NTJX)
2. [Make it easy to unsubscribe](#h_01GEF808VXF1H327ZJHCQK5HY4)
3. [Avoid prohibited content](#h_01GEF80EBYX8CW2VG05KRMYK80)
4. [Don't send too early or late](#h_01GEF80QCKS1CPTNK12FKZNQEW)
5. [Indicate your company or brand in every SMS](#h_01GEF80XJSXE43JT7NJNG8GD4F)
6. [Follow rules for cart abandonment flows (US only)](#h_01GEF815SDBRSSXHQYSZ9XQM0V)
7. [Add other message requirements (Canada only)](#h_01GEF81DGVPCB3VSXF2B2FBCWG)

****See an infographic for the 7 compliance basics****

![Details for each of the 7 compliance basics for SMS, which are also discussed later in this article](https://klaviyo.zendesk.com/hc/article_attachments/28717880202651)

### Why do I need to know these compliance basics?

SMS is a strictly regulated channel. Most countries have laws governing the use of SMS, and failing to follow these laws may result in heavy filtering or hefty fines. To avoid this for your business, it's important to know the dos and don'ts surrounding SMS.

![](https://fast.wistia.com/embed/medias/r8h8be6hd2/swatch)

## Always get consent for SMS before texting anyone

When it comes to SMS, you must have someone's [express consent](https://help.klaviyo.com/hc/en-us/articles/4404203889947) in order to message them. Written consent is best, as there’s a record of someone agreeing to SMS.

To get proper SMS consent, there are 4 key best practices you should keep in mind.

****Only send SMS to people who are currently opted in****

Don't send SMS to anyone who is not a current subscriber. This applies to all message types, including:

- Flows
- 1-on-1 conversations
- Campaigns

Even if someone previously opted into SMS but is now opted out, you cannot text them because they are not currently a subscriber.

****Make sure the consent is for SMS specifically****

When it comes to getting consent, someone must agree to receive SMS messages, so keep the following in mind:

- SMS opt-in must be separate from email
  - You can't use the same checkbox for both
- Consent for email or marketing in general doesn't count

****Use disclosure language anywhere you collect SMS consent****

SMS also requires that people understand what they're opting into. You must include disclosure language to tell people about your SMS program anywhere you collect SMS consent, including:

- Popups
- Flyout
- Embed forms
- Printouts with QR codes
- Instagram stickers
- Checkout page
- Emails with opt-in links

Want an example? Go to this article for an [example of disclosure language](https://help.klaviyo.com/hc/en-us/articles/4412878737051).

![Example of a signup form with disclosure language](https://klaviyo.zendesk.com/hc/article_attachments/28717880184603)

****Make sure that consent was provided directly to your company****

A single consent cannot be provided to multiple brands or organizations. Customers must provide consent to receive messages from your company explicitly. Lead generation, affiliate related, or purchased lists are not valid SMS consent.

## Make it easy to unsubscribe

Always include a way for subscribers to opt out of your SMS campaign and flow messages.
Depending on what sending number you're using, you can include one of the following in your SMS messages:

- Opt-out keyword (e.g., STOP)
- Unsubscribe link

These are the simplest options, although any other reasonable opt-out method may also be allowed (e.g., providing your customer support phone number or email address in the SMS).

|  |  |
| --- | --- |
| ****Example of an opt-out keyword**** | ****Example of an unsubscribe link**** |
| ![Example SMS that includes Stop as the opt-out keyword](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/0c8bbc27139ceeb318890bda35056c57ad0cec57-640x434.png) | ![Example SMS that includes an unsubscribe link](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/a38eb8613c8c2d7e4fc1eead5466117f17a7da8d-646x436.png) |

## Avoid prohibited content

There are certain topics that wireless carriers refuse to deliver to recipients.

Anything related to these [prohibited topics](https://help.klaviyo.com/hc/en-us/articles/4401822831771) in either your messages or website may result in your messages getting filtered by the carrier or the carrier completely blocking the sending number.

- Illegal substances
- SHAFT
  - Sex
  - Hate
  - \*Alcohol
  - \*Firearms (including other weapons)
  - Tobacco (including CBD)
- Fireworks
- Gambling
- Debt collection/forgiveness
- High-risk financial services (e.g., cryptocurrency)
- Multi-level marketing

\* Messaging from [Alcohol, Firearms, Tobacco, and Sex-related brands may be allowed with age-gating](https://help.klaviyo.com/hc/en-us/articles/17252552814875) in certain countries.

While not all these topics are prohibited in every country, carriers reassess what content they will allow and don't always make this information public in a timely or formal manner. It's best to avoid them no matter which country you're sending to.

## Don't send too early or late

There are certain times when it's illegal to send SMS. These hours are known as [quiet hours](https://help.klaviyo.com/hc/en-us/articles/4408737146651), and they vary based on the country and region you're sending to.

In general, send in your recipient’s local time and avoid sending:

- Before 9 a.m.
- After 8 p.m.

In some cases, you may be able to legally send at 8 a.m. or up to 9 or 10 p.m., however, SMS engagement tends to be lower at these times. For more info, review [country-specific laws for SMS](https://help.klaviyo.com/hc/en-us/sections/29514448877467).

|  |  |
| --- | --- |
| ****Country**** | ****Quiet hours**** |
| \*United States  Canada  United Kingdom  Ireland  Germany  Netherlands  Australia  New Zealand | Before 8 a.m.  After 8 p.m. |
| \*\*France | Before 8 a.m.  After 10 p.m.  All Sundays  Public holidays |

\* For the US, most of the country is covered by the [TCPA](https://help.klaviyo.com/hc/en-us/articles/360035055312), which allows sending from 8 a.m. to 9 p.m. However, several states (such as Florida) have enacted mini-TCPAs for their state and limit sending to between 8 a.m. and 8 p.m.

\*\* Quiet hours in France are enforced by wireless carriers. This means that you may legally be allowed to send Sundays, but your messages won’t be delivered. The carriers may also decide to filter your other messages if you continue to send outside of the quiet hours.

## Indicate your company/brand in your SMS

It's important for your subscribers to know who your messages are from. Otherwise, your recipients may think the texts are just spam.

There's a couple different ways you can tell customers who you are in your text messages:

- Include an organization prefix at the beginning of the message
  ![Example SMS that has an organization prefix](https://klaviyo.zendesk.com/hc/article_attachments/28717880196891)
- Reference your brand somewhere in the body of the text message
  ![Example SMS where the organization name is within the body of the text message](https://klaviyo.zendesk.com/hc/article_attachments/28717852716059)
- Use a branded sender ID (UK or Australia only)
- Send a [virtual contact card](https://help.klaviyo.com/hc/en-us/articles/8458786130331) as part of your welcome series (US and Canada only)

****Follow guidelines for abandonment flows (US only)****

In the US, follow these guidelines for any shopping cart abandonment flow:

- Always use double opt-in
- Only send 1 SMS per recipient
- Send the SMS within 48 hours of the individual abandoning a cart session

Otherwise, wireless carriers may audit or block your SMS program.

Following these guidelines is also a best practice for other abandonment flows (such as browse abandonment), although it's not required by carriers.

****Add other message requirements (Canada only)****

We recommend the following elements when texting anyone in Canada, particularly when using a short code:

- Program name (e.g., for Klaviyo, it might be “Klaviyo SMS”)
- A call to action
- A way to get help, such as "Text HELP for help"
- A way to opt out, such as "Reply STOP to opt out"
- “Std. Msg&Data rates may apply” (if you include a link)

For example, a message about a new product might look like this: “Bridge Designs: Fall season is here! Check out our new pieces here: [LINK] Text HELP for help. Text STOP to opt out. Std. Msg&Data rates may apply.”

![Example SMS that includes all Canadian message requirements](https://klaviyo.zendesk.com/hc/article_attachments/28717880199323)