---
id: 18410569130779
title: "Understanding how GDPR affects SMS in Europe"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18410569130779-Understanding-how-GDPR-affects-SMS-in-Europe"
section: "Europe: SMS compliance"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: en
---

## You will learn

Learn about best practices for SMS marketing in the European Union (EU).

SMS in Europe is currently available in the UK, Ireland, Germany, France, Austria, Spain, Switzerland, Denmark, Sweden, Norway, Finland, Italy, Portugal, Belgium, Poland, Hungary, and the Netherlands.

The following regulations apply to SMS marketing in Europe:

- EU General Data Protection Regulation (GDPR)
- EU ePrivacy Regulations

Please note, certain countries may have country specific laws and regulations that apply to SMS marketing and are not included in this guidance.

This information is intended solely for educational and informational purposes and should ****not**** be construed as legal advice. The content provided is general in nature and may not reflect the most up-to-date information. Klaviyo strongly advises consulting with a qualified legal counsel to ensure your compliance with applicable laws and regulations in connection with your use of our services.

## SMS compliance in the EU

There are a number of compliance dos and don’ts for SMS marketing in the EU:

- ********Do:********
  - Obtain explicit consent from recipients before messaging them.
  - Allow recipients to easily opt out.
  - Only send during daytime hours (i.e., not during quiet hours).
  - SMS should support both HELP and STOP keywords, as well as similar keywords, in the recipient’s local language.
  - Clearly identify your brand or organization in your messages.
- ****Do not:****
  - Send to recipients on do-not-call or do-not-disturb registries.
  - Include prohibited content in your messages.

The following sections explain these practices in more detail.

## Obtain explicit consent

When collecting consent in the EU, you must provide a clear and detailed explanation of how you plan to use the subscriber’s information. Under GDPR, consent needs to be “[freely given, specific, informed, and unambiguous.](https://help.klaviyo.com/hc/en-us/articles/360003536031)”

Double opt-in, where available, is always recommended as a best practice. This is particularly the case in Germany and some other E.U. countries, such as Austria and Switzerland, where double opt-in is the preferred way of demonstrating that consent has been properly and lawfully obtained. Customers on a paid plan should, therefore, consider using Smart Opt-in as a default for collecting SMS consent.

When asking for consent:

- Make it easy for recipients to opt out (e.g., via an opt-out keyword or unsubscribe link).
- Provide links to your privacy policy and terms of service.
- Be clear about what information you are collecting and how you are going to use it.
- Be clear about what subscribers are subscribing to.
- Ask for consent for each specific purpose (e.g., if you collect consent for both SMS and email, use separate fields for each channel so that someone has the option to subscribe to one and not the other).
- Make sure the subscriber has to take an active step (e.g., checking an unchecked box) to relay their consent.
- Make sure consent is not conditional on receiving a good or service.
- Do not accept consent from children under 16 unless you have permission from the holder of parental responsibility over the child.
- Keep accurate records of when, where, how, and for what purpose a subscriber gave you their consent.

Under GDPR, there are other bases (like “legitimate interest”) that may be relied on instead of explicit consent. However, when using Klaviyo SMS, you need to obtain [explicit consent](https://help.klaviyo.com/hc/en-us/articles/4404203889947) from recipients using the guidelines mentioned above.

## Only send during daytime hours

In most countries in the EU, SMS messages should not be sent too late or too early in the day.

In general, send in your recipient’s local time and avoid sending:

- Before 9 a.m.
- After 8 p.m.

In some cases, you may be able to legally send at 8 a.m. or up to 9 or 10 p.m., however, SMS engagement tends to be lower at these times.

|  |  |
| --- | --- |
| ****Country**** | ****Quiet hours**** |
| Australia  Austria  Belgium  Canada  Denmark  Finland  Germany  Hungary  Ireland  Italy  Luxembourg  Netherlands  New Zealand  Norway  Poland  Portugal  Spain  Sweden  Switzerland  United Kingdom  \*United States | Before 8 a.m.  After 8 p.m. |
| \*\*France | Before 8 a.m.  After 10 p.m.  All Sundays  Public holidays |

\* For the US, most of the country is covered by the [TCPA](https://help.klaviyo.com/hc/en-us/articles/360035055312), which allows sending from 8 a.m. to 9 p.m. However, several states (such as Florida) have enacted mini-TCPAs for their state and limit sending to between 8 a.m. and 8 p.m.

\*\* Quiet hours in France are enforced by wireless carriers. This means that you may legally be allowed to send Sundays, but your messages won’t be delivered. The carriers may also decide to filter your other messages if you continue to send outside of the quiet hours.

## Identify your brand/organization

As a best practice, each text message you send to recipients in the EU should identify you as the sender. Many companies do this by either:

- Customizing their sender ID (when using branded sender IDs)
- Including their organization name at the start of each message (when using long or short codes)

When using Klaviyo SMS, you can customize your sender ID under ****Settings > SMS**** and automatically add your organization’s name to the start of each SMS in the message editor by selecting the option in the **Compliance** tab (note that this is turned on by default).

## Do not include prohibited content

Wireless carriers may refuse to deliver SMS messages that reference or otherwise contain content relating to certain topics, including:

- Illegal substances
- SHAFT
  - Sex
  - Hate
  - \*Alcohol
  - \*Firearms
  - Tobacco (including CBD)
- Fireworks
- Gambling
- Debt collection/forgiveness
- High-risk financial services (e.g., cryptocurrency)
- Multi-level marketing

\* Alcohol and firearms may be permitted in certain countries when [age-gating](https://help.klaviyo.com/hc/en-us/articles/17252552814875) is enabled.

While not all of these topics are prohibited in every country, carriers periodically reassess what content they will allow and don't always make this information public in a timely or formal manner. It's best to avoid content related to these topics in any country you're sending to.

Anything related to these prohibited topics in either your messages or website may result in those messages getting filtered by the carrier or the carrier completely blocking the sending number. For more information, read our [article on prohibited SMS content](https://help.klaviyo.com/hc/en-us/articles/4401822831771).

## Allow people to opt out easily

Each text message you send to recipients in the EU must also include an opt-out mechanism. Many companies do this by:

- ****When using branded sender IDs:**** including an unsubscribe link in their messages.
- ****When using long or short codes:**** adding an opt-out keyword at the end of the text messages.

When creating an SMS in Klaviyo’s message editor, you can automatically add either an unsubscribe link or opt-out keyword to your messages via the option in the **Compliance** tab. Note that these options are turned on by default.

## Support HELP and STOP keywords

SMS messages should support both HELP and STOP keyword commands, as well as similar keywords in the recipient’s local language.

In Klaviyo, all the following keywords are supported automatically:

- YES and Y
- HELP and INFO
- STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, and QUIT
- START and UNSTOP

## Do not contact users on do-not-call or do-not-disturb registries

As a guideline, don’t contact anyone on do-not-call or do-not-disturb registries. Many EU countries have their own registries.

## Additional resources

- Learn more about [what explicit consent means](https://help.klaviyo.com/hc/en-us/articles/4404203889947).
- See other GDPR-related articles:
  - [Guide to collecting GDPR-compliant consent](https://help.klaviyo.com/hc/en-us/articles/360003536031)
  - [Frequently asked questions about GDPR](https://help.klaviyo.com/hc/en-us/articles/360003211651)
  - [How to handle GDPR and CCPA requests](https://help.klaviyo.com/hc/en-us/articles/360004217631)