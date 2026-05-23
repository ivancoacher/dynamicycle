---
id: 26977831996315
title: "Understanding the opt-out options for an SMS message"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/26977831996315-Understanding-the-opt-out-options-for-an-SMS-message"
section: "Understanding SMS compliance settings"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: en
---

Learn about the 2 opt-out options for an SMS: unsubscribe instructions or unsubscribe link. This article describes both options, including how they work and when each can be used.

It’s always important to include a way for recipients to opt out of SMS in your messages. In addition to being a best practice for any marketing channel, it is required for SMS in most countries. Some countries also require that you provide a way to opt out in every SMS you send.

## About Klaviyo’s opt-out options for SMS

Klaviyo includes 2 built-in ways for SMS recipients to unsubscribe within a message:

- Unsubscribe instructions
- Unsubscribe link

Only 1 of these options is included in a single SMS at any given time. The option that is used depends on the [sending number](https://help.klaviyo.com/hc/en-us/articles/6637671573403). See the table below for details on which option is used for each sending number.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ****Sending number for this option**** | ****\*Number of characters**** | ****Able to be turned off in Klaviyo**** |
| Unsubscribe instructions | Toll-free numbers  Long codes  Short codes | 21 characters, by default | Yes |
| Unsubscribe link | Branded sender IDs | ~31 to 34 characters, by default | No |

\* The exact character counts may vary. With unsubscribe instructions, you can edit the message in the SMS settings page. As for unsubscribe links, the length of the link may change depending on whether you’re using the default Klaviyo link or a [branded shortened link](https://help.klaviyo.com/hc/en-us/articles/17649597637147).

When a customer unsubscribes via either option, it automatically removes consent for both SMS transactional and promotional consent. Currently, your subscribers cannot opt out of only transactional or only promotional SMS.

****Why are unsubscribe instructions not available for branded sender IDs?****

Unsubscribe instructions rely on the subscriber texting a keyword to your brand’s number. However, branded sender IDs cannot receive incoming messages. Even if a subscriber tries to text you STOP, the branded sender ID will never receive this message. Thus, unsubscribe instructions simply don’t work for branded sender IDs.

Always preview your message to check the character count if you are using a branded sender ID and have any other number type. Unless you specifically filter or [segment by country](https://help.klaviyo.com/hc/en-us/articles/4402954226459), a single message may use an unsubscribe link for some recipients and instructions for others. This alters the character count and possibly causes you to use more credits than expected.

The opt-out options are always toggled on by default for every SMS campaign and flow message in Klaviyo.

****Why can’t I turn off the unsubscribe link?****

Many countries have strict rules that require companies to add a way to opt out in every SMS. This is not easy with branded sender IDs. Other number types all respect STOP as a way to immediately unsubscribe; however, there’s no universal unsubscribe link for branded sender IDs.

To protect users, Klaviyo automatically adds the unsubscribe link to messages sent from branded sender IDs.

### Unsubscribe instructions

In Klaviyo, the unsubscribe instructions provide recipients with a keyword they can text to opt out of SMS.

As a best practice, we recommend sending opt-out instructions at least once a month.

By default, the unsubscribe instructions are: “Text STOP to opt-out.”

Unsubscribe instructions:

- Are not available for branded sender IDs.
- Can be edited.
- Stays the same for every recipient (i.e., it is not automatically translated to other languages).
  ![Example of a text with the default unsubscribe instructions](https://klaviyo.zendesk.com/hc/article_attachments/28716334419483)

For anyone using a toll-free number, if a subscriber unsubscribes using the keyword “STOP,” they must resubscribe using the keyword UNSTOP or START. Otherwise, wireless carriers will block messages to the recipient’s number, even if that person has opted back in using a form, other keyword, etc.

#### Edit the unsubscribe instructions

You must be an Owner or Admin to change the unsubscribe instructions in an account.

1. Select your account name in the lower left.
2. Navigate to ****Settings > SMS****.
3. Scroll down to the **Message add-ons** section.
   ![opt-out instructions.jpg](https://klaviyo.zendesk.com/hc/article_attachments/30080400115611)
4. Edit the text.
   Note: you must include “STOP” in the message.
5. Click ****Save****.

Once you save, it will update the unsubscribe instructions in any SMS flow or scheduled campaign messages.

### Unsubscribe link

The unsubscribe link allows recipients to click a link to opt out of SMS. As soon as the recipient clicks the link, they are redirected to a page to confirm the opt-out via an **Unsubscribe** button. Please note that the customer will need to click the **Unsubscribe** button to opt-out, not just click the link.

This option is only used for messages sent from branded sender IDs, since unsubscribe instructions don’t work with this number type. Keep in mind that unsubscribe links add more characters to the message compared to unsubscribe instructions.

This link:

- Is only available for branded sender IDs.
- Does not count toward the message’s click rate.
- Cannot be edited (i.e. change the word "STOP", or choose a different domain)

![Example of a text with an unsubscribe link](https://klaviyo.zendesk.com/hc/article_attachments/28716334421659)

Further, this link directs to a page that:

- Is translated automatically to the following languages based on the browser’s settings:
  - English (default if browser language is not set or is not supported)
  - French
  - German
  - Dutch
- Cannot be manually edited (i.e., you cannot change the text, colors, etc.)

Below is an example of the page users are linked to when they select the unsubscribe link.

![Page that the unsubscribe link directs users to](https://klaviyo.zendesk.com/hc/article_attachments/28716334423707)

## Additional resources

- [Basics: SMS compliance](https://help.klaviyo.com/hc/en-us/articles/7956171032091)
- [Understanding the SMS organizational prefix](https://help.klaviyo.com/hc/en-us/articles/26909154035611)
- [Configure when an SMS opt-out keyword results in an unsubscribe](https://help.klaviyo.com/hc/en-us/articles/29109965092251)
- [Add a dynamic image to a text message](https://help.klaviyo.com/hc/en-us/articles/1260806102230)