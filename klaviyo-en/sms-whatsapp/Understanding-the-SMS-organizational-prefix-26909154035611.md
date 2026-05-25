---
id: "26909154035611"
title: "Understanding the SMS organizational prefix"
source_url: "https://help.klaviyo.com/hc/en-us/articles/26909154035611-Understanding-the-SMS-organizational-prefix"
section: "Understanding SMS compliance settings"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: "en"
---
## You will learn

Learn about the organizational prefix for SMS messages, including what it is, how to change it, when it’s enforced, and more.

This information is intended solely for educational and informational purposes and should ****not**** be construed as legal advice. The content provided is general in nature and may not reflect the most up-to-date information. Klaviyo strongly advises consulting with a qualified legal counsel to ensure your compliance with applicable laws and regulations in connection with your use of our services.

## What is an organizational prefix?

The organizational prefix (also called a brand prefix) is a feature that includes your business name at the beginning of a text message.

![Example text message showing an organizational prefix](https://klaviyo.zendesk.com/hc/article_attachments/28716058451611)

Using an organizational prefix is highly recommended, as many countries require that you identify your brand within an SMS. Unlike email, an SMS message doesn’t usually have the identifier built into it. The organizational prefix allows customers to understand that a text came directly from your brand.

If the sender identity is unknown or unnecessarily hard to locate, it can create user mistrust, leading to higher opt-out, spam complaints, and lower conversion rates.

## How the prefix works in Klaviyo

You can only have 1 organizational prefix per account, and it is not translated. If you’re sending to multiple countries, make sure the prefix you choose is recognizable to all of your recipients.

The organizational prefix is typically on by default and may be enforced as well. See the table below for details.

|  |  |  |
| --- | --- | --- |
| ****Sending number**** | ****On by default**** | ****Enforced with sending number**** |
| Toll-free number | ✖ Canada  ✔ United States | ✖ Canada  ✔ United States |
| Branded sender ID | ✔ | ✖ |
| Long code | ✔ | ✖ |
| Short code | ✖ Canada  ✔ All other countries | ✖ Canada and United States  ✔ All other countries |

You have the option to turn off the organizational prefix in certain cases. However, if the prefix is marked as “enforced” in the table above, note that SMS sent via that number will still include the prefix, even if you toggle off this option.

To turn the organizational prefix on or off for a message, navigate to the ****Compliance**** tab in the SMS message editor.

****Why can’t I turn off the organizational prefix for my long code or short code?****

Klaviyo seeks to protect users by implementing platform guardrails to ensure SMS compliance.

The UK, Australia, and other countries require that brands clearly identify themselves in every SMS marketing message.

Unlike branded sender IDs, numeric sender IDs (e.g., long codes and short codes) do not allow for identification of the brand. For this reason, Klaviyo adds the organizational prefix so that your SMS recipients always have a way to identify your brand in any country where this is strictly required.

![Compliance tab, showing the organizational prefix option](https://klaviyo.zendesk.com/hc/article_attachments/36918604273691)

### Important note about France

In France, a number of small wireless carriers do not supported branded sender IDs, so they replace the IDs with a random local number.

In order to comply with GDPR regulations, it's a best practice to use an organizational prefix for all messages to France. That way, consumers will always be able to identify your brand.

## When to use the organizational prefix

The organizational prefix is strongly recommended in:

- Responses to subscribe keywords
- Order updates

Even in countries where the organizational prefix isn’t enforced, it’s important to include your full prefix regularly or some reference to your brand in almost every message. For instance, if you are sending messages once a week in the US, you may want to include the organizational prefix in at least 1 SMS per month, and identify your brand in other ways for the rest of the messages.

### When the organizational prefix is not needed

You don’t need to use the organizational prefix when:

- Sending to anyone in Canada, as Canadian texts include a [company information link](https://help.klaviyo.com/hc/en-us/articles/4402922558235) that acts as the identifier
- Using a branded sender ID (in most cases)
- Including another clear reference to your brand within the SMS; however, this may not apply for every country (such as in countries where the prefix is enforced)

## View or change the prefix in Klaviyo

By default, Klaviyo uses your sender name (in the **Organization** settings tab) as your organizational prefix.

When you change your organizational prefix, it will update in any SMS message containing the prefix, including:

- Flow messages
- Scheduled campaigns
- All newly created messages

Changing the prefix may add more characters to your SMS messages, which could lead to the messages exceeding the character limit and using more of your plan’s credits.

To view or change your organizational prefix:

1. Select your account name in the bottom left.
2. Select ****Settings > SMS****.
3. Scroll down to the **SMS message add-ons** section.
   ![SMS settings, showing the section to edit the unsubscribe instructions](https://klaviyo.zendesk.com/hc/article_attachments/36918604276635)
4. Optional: change the prefix by editing the text field under **Organizational prefix**, then click ****Save****.

## Additional resources

- [How to change your quiet hours settings for SMS flows](https://help.klaviyo.com/hc/en-us/articles/22711363273627)
- [How to A/B test SMS campaigns](https://help.klaviyo.com/hc/en-us/articles/4406796460443)
- [Basics: SMS best practices](https://help.klaviyo.com/hc/en-us/articles/13288640663579)