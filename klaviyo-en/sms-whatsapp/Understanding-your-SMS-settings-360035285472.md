---
id: "360035285472"
title: "Understanding your SMS settings"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360035285472-Understanding-your-SMS-settings"
section: "Understand SMS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:45Z"
language: "en"
---
Klaviyo SMS can only be set up by account Owners, Admins, and Managers.

## You will learn

Learn about your SMS settings and how to edit them to fit your business needs.

Please note that SMS is available only in certain countries. See the [list of countries where Klaviyo SMS is available](https://help.klaviyo.com/hc/en-us/articles/4402914866843).

## Before you begin

Before you can get started, you need to have [set up SMS](https://help.klaviyo.com/hc/en-us/articles/4404274419355). Once done, the SMS settings page will populate.

For information about credits per country, see [understanding the SMS credit system](https://help.klaviyo.com/hc/en-us/articles/13502982552347).

## Review the SMS settings page

1. Click your account name in the bottom left corner.
2. From the dropdown, click ****Settings****.
   ![pening the account menu by clicking the organization name](https://klaviyo.zendesk.com/hc/article_attachments/28717381367707)
3. Click ****SMS****.

Here, you'll be able to access the following tabs:

- Sender information
- Sender preferences
- Tracking
- Keyword responses
- Short links
- Terms of Service

To find or change your SMS attribution settings, head to the ****Attribution**** tab instead.

## Sender information

### Countries

Your SMS numbers are listed in the **Countries** section.  This section includes information on the region, specific number currently used, the status, or if the regional number still needs to be added or activated.

For details about these numbers, check out this [article on SMS sending numbers](https://help.klaviyo.com/hc/en-us/articles/6637671573403).

![countries sms setting.png](https://klaviyo.zendesk.com/hc/article_attachments/30080346534427)

### Company information

The **Company Information**section contains an option to [turn on virtual contact cards](https://help.klaviyo.com/hc/en-us/articles/8458786130331) and the following details about your organization:

- Company or organization name
- URL for your website
- Company email address
- Logo
- Company phone number
- Address

![Company info fields including name, URL, email address, phone number, address, and to add a logo](https://klaviyo.zendesk.com/hc/article_attachments/28717387673115)

### SMS message add-ons

There are 2 sections that you can edit within **Message Add-Ons**: organizational prefix and opt-out language. These are added to the beginning or end of your SMS messages, respectively.

- ****Organizational prefix****
The organizational prefix is your business name. It should be the word or phrase customers recognize as your business title. Prefixes are optional (except in France, where they're required). However, these prefixes are highly recommended because, unlike emails, text messages don't have a built-in way to identify the sender. This prefix allows customers to understand that this text came directly from your store.- ****Opt-out language****
Opt-out language is the phrase added to the end of a message that gives customers the option to opt out of further SMS communication. This is similar to the unsubscribe language in emails, which helps to limit negative customer experiences and make sure you don't get marked as spam.

Opt-out language must include STOP in the message and is required in some jurisdictions.

![](https://klaviyo.zendesk.com/hc/article_attachments/30080346536987)

## Sender preferences

There are a few aspects to the settings for SMS sending:

- Smart Sending
- SMS quiet hours
- Unsubscribe known SMS litigators

Klaviyo warns you if your campaign will potentially violate quiet hours.

### Smart Sending

Smart Sending allows you to limit the number of SMS messages someone will receive in a given period of time.

Klaviyo sets the default window of time to 24 hours, although you can adjust this, as shown below.

![Smart sending field with 12 hours chosen](https://klaviyo.zendesk.com/hc/article_attachments/28717381393947)

It is best practice to enable Smart Sending to ensure that customers are not overwhelmed with messages from your business, especially if you're sending emails in addition to text messages.

SMS Smart Sending and email Smart Sending are treated separately. For instance, after you send an email, you can still send an SMS the same day when Smart Sending is on. The SMS Smart Sending window only applies to SMS, and the email window only applies to emails. If you are looking to learn more, check out our article on [understanding Smart Sending](https://klaviyo.zendesk.com/hc/en-us/articles/115002779311).

### SMS quiet hours

Klaviyo's [SMS quiet hours](https://help.klaviyo.com/hc/en-us/articles/4408737146651) limit when flows can send SMS messages to recipients.

![SMS quiet hours set up to not send between 8pm and 11am](https://klaviyo.zendesk.com/hc/article_attachments/28717381396763)

This is beneficial for 2 key reasons:

- ****Providing a better customer experience****
  Text messages actively ping the recipient's phone, so they're more intrusive than email or social media messages. Quiet hours help you avoid texting subscribers at odd hours of the day, leading to more positive customer interactions.
- ****Sending at only compliant times****
  Quiet hours is also a key part of SMS compliance. In the US, for example, the [TCPA](https://help.klaviyo.com/hc/en-us/articles/360035055312) forbids sending anytime before 8 a.m. and after 9 p.m., and in [Florida](https://help.klaviyo.com/hc/en-us/articles/4405332994843), it is further restricted to between 8 a.m. and 8 p.m. The default window ensures that your messages can only send at compliant times, regardless of where the recipient lives and their time zone.

Quiet hours are based on the recipient's phone number: typically on the country code, but in the US and Canada, you have the option to base quiet hours on area code.

By default, Klaviyo's SMS quiet hours are from 8 p.m. to 11 a.m. (using Eastern Time in the US and Canada, BST for the UK, and Australian Eastern Time in Australia).

### Unsubscribe known SMS litigators

By default, you will not collect SMS consent from a known litigators, reducing the risk of complaints or lawsuits for your brand. Anyone who is a known SMS litigator is automatically unsubscribed by Klaviyo.

Turning off this setting and collecting consent from known SMS litigators is not recommended.

![Setting to automatically remove consent from known SMS litigators](https://klaviyo.zendesk.com/hc/article_attachments/28717387693339)

## Tracking

Check this box to exclude bot clicks from your account's reporting data. You can filter bot clicks from email, SMS, or both channels.

Enabling this setting will exclude bot clicks in calculations of click rate, total clicks, and unique clicks across most reporting surfaces. Learn more about [excluding and monitoring bot clicks](https://help.klaviyo.com/hc/en-us/articles/22981852783899) in your account.

![The Tracking section within the SMS settings menu for an example account showing the box checked to exclude bot clicks from SMS reporting.](https://klaviyo.zendesk.com/hc/article_attachments/28717387698971)

Note that any A/B tests created after this setting is enabled will use a click rate that excludes bot clicks, which may impact the winning variant. For this reason, we recommend not enabling this setting during an ongoing A/B test that uses click rate as a metric.

## Keyword responses

### Compliance keywords

[Compliance keyword](https://help.klaviyo.com/hc/en-us/articles/29928896469531) responses are SMS messages that are automatically toggled on to respond to customers who answer one of your messages. Note that:

- Keyword responses do not apply to branded sender IDs.
- You cannot add links to editable responses.
- Keyword and their responses are available in a variety of languages.

|  |  |  |  |
| --- | --- | --- | --- |
| ****Keyword(s)**** | ****English default text**** | ****Can you edit the response?**** | ****Details**** |
| YES, Y | [Organization name]: Thanks for signing up for updates! Text HELP for help; STOP to opt-out. Msg & data rates may apply, frequency varies. | Yes | Only applies with double opt-in after someone confirms they want to subscribe. This message does not apply to branded sender IDs. |
| HELP and INFO | [Organization name]: For help reach us at [your email]. | Yes | This message sends when someone requests more information or help from you via text. |
| STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, and QUIT | NETWORK MSG: You replied with the word "stop" which blocks all texts sent from this number. Text back "unstop" to receive messages again. | No, but you can [configure when opt-out keywords result in an unsubscribe](https://help.klaviyo.com/hc/en-us/articles/29109965092251) | The recipient’s carrier sends this message after someone opts out. |
| START, UNSTOP | NETWORK MSG: You have replied "unstop" and will begin receiving messages again from this number. | No | The recipient’s carrier sends this message when someone who previously unsubscribed opts back in.  ****Note****: You must have a list titled "SMS Subscribers" for the keywords to work. |

[Certain keyword responses can be edited](https://help.klaviyo.com/hc/en-us/articles/29928896469531) to fit your brand and desired content.

### Subscribe keywords

A subscribe keyword is any keyword that allows someone to opt in to your SMS marketing program (e.g., JOIN)

Subscribe keywords are different from compliance keywords (e.g., HELP, STOP, START). Subscribe keywords are an opt-in method, while compliance keywords must, by law, provide certain information or perform a certain action (such as removing SMS consent).

You can [create custom subscribe keywords](https://help.klaviyo.com/hc/en-us/articles/360050384091) that match your branding. These custom keywords:

- Must be between 3 and 20 characters
- Include only alphanumeric characters \*A–Z and 0–9)
  - Do not use any other special symbols.
- Should not be words:
  - Related to sex, hate, \*alcohol, \*firearms, or tobacco (SHAFT).
    \*Alcohol and firearms may be allowed with age-gating in certain countries.
  - That are too common (i.e., could be used in a normal text conversation), such as “the,” "that," "are," "can," "here," "about," or “and,”

## Short links

### Custom links

[Custom links](https://help.klaviyo.com/hc/en-us/articles/17649677926299) allow you to brand shortened links in your SMS messages, either by adding the brand as a prefix to Klaviyo's link (i.e., a branded Klaviyo link) or by branding the entire link (i.e., branded custom link).

|  |  |
| --- | --- |
| ****Link type**** | ****Example company: James Black**** |
| Branded Klaviyo link | jblck.klv3.io/382aNpW5 |
| Branded custom link | sms.jamesblack.com/382aNpW5 |

Learn how to [brand shortened links for SMS](https://help.klaviyo.com/hc/en-us/articles/17649597637147).

### Subscribe links

After you post an SMS subscribe link, anyone who clicks on it can easily opt in to your text message program. Those on mobile devices can opt in with tap-to-text, while those on desktop are directed to a subscribe page.

Learn how to [create an SMS subscribe link](https://help.klaviyo.com/hc/en-us/articles/14104388043931).

## Terms of service

Whenever you collect SMS consent, you should link to your mobile terms of service (TOS). You can use Klaviyo to:

- Generate a mobile TOS that you can customize to fit your needs.
- Either:
  - Host the TOS for you and add a link to your TOS anywhere (like forms where you collect SMS consent)
    Or
  - Copy the text in the TOS and paste into another page, like your existing TOS page.

![Section to create a mobile terms of service](https://klaviyo.zendesk.com/hc/article_attachments/28717387666459)

### SMS opt-in disclosure

Including SMS disclosure language on your popups, website, and any other consent-collection method is extremely important. Many countries require that companies inform potential SMS subscribers of exactly what they are agreeing to if they opt in to SMS marketing.

In Klaviyo, you can create default disclosure language to add to your sign-up forms and subscribe pages.

![Account-level disclosure language to use when gathering SMS subscribers](https://klaviyo.zendesk.com/hc/article_attachments/28717387660315)

## Import SMS unsubscribes

You can bulk unsubscribe people from SMS by uploading a CSV file. This is useful when cleaning your SMS list, as it's better to unsubscribe someone than delete their profile.

This is not located within the SMS settings, but rather under ****Settings > Other > Profile maintenance****.

![Import SMS unsubscribes within the other settings](https://klaviyo.zendesk.com/hc/article_attachments/28717387664155)

Read this article on [how to bulk unsubscribe SMS profiles](https://help.klaviyo.com/hc/en-us/articles/5227452906523).

## Tip: target by country

With both branded sender IDs and toll-free numbers, the same number is used to collect consent and send to multiple countries. They do so automatically too, so if you don't want to collect consent or send to a certain country, target your forms and campaigns by country, and add location-based splits your flows.

Separating by country is also key if you want to know where to use your SMS credits. Since credits vary by country, targeting based on location helps you track how much you spent, who engaged, and your ROI on a per-message basis. This way, you'll know where and with who to send SMS messages to.

The table below lists all of the countries where these numbers could send to.

|  |  |
| --- | --- |
| ****Branded sender ID**** | ****Toll-free number**** |
| Australia | United States |
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
| United Kingdom |  |

## Additional resources

- [Understand SMS sending numbers](https://help.klaviyo.com/hc/en-us/articles/6637671573403)
- [Understand Klaviyo's SMS credit system](https://help.klaviyo.com/hc/en-us/articles/13502982552347)
- [Basics: multi-national SMS sending with Klaviyo](https://help.klaviyo.com/hc/en-us/articles/23740503987099)