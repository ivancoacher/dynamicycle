---
id: "360035661191"
title: "Guide to crafting SMS and MMS messages"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360035661191-Guide-to-crafting-SMS-and-MMS-messages"
section: "Format your SMS messages"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:46Z"
language: "en"
---
## You will learn

Learn about building your SMS messages in Klaviyo, including configuring the content, SMS limitations, and best practices.

Check out [getting started with SMS](https://academy.klaviyo.com/getting-started-with-sms/1411601) to learn how to start using SMS.

## Before you begin

Before you start creating and sending SMS messages in Klaviyo, you need to:

- Turn on SMS in your account.
- Have an [SMS sending number](https://help.klaviyo.com/hc/en-us/articles/6637671573403) for the country you want to send to.

## How to create an SMS or MMS message

Create SMS content by clicking a specific flow or campaign name.

- For SMS campaigns: choose the name and recipients and then navigate to the **Content** step.
- For flows: add in an SMS component and select ****Edit****.

![Blank SMS in a flow](https://klaviyo.zendesk.com/hc/article_attachments/28717992270875)

### SMS

SMS are plain-text messages with no images or GIFs. Like all text messages, an SMS can contain emojis and [special characters](https://help.klaviyo.com/hc/en-us/articles/17275332265627); however, note that they shorten the character limit.

The character limit for SMS is:

- 160 characters
  or
- 70 characters with an emoji or special character

### MMS

You can use GIFs and static and [dynamic images](https://help.klaviyo.com/hc/en-us/articles/1260806102230) in your text messages. Virtual contact cards also count as MMS messages.

MMS is only available with:

- US toll-free numbers and short codes
- Canadian toll-free numbers
- Australian long codes

To include an image or GIF, click ****Add Image/GIF**** and choose your media.

Note that when you add an image or GIF, the message becomes an MMS, which counts as more credits than SMS.

[MMS messages](https://help.klaviyo.com/hc/en-us/articles/360041075091) can have up to 1600 characters and the media must be in one of the following formats:

- PNG
- JPEG
- GIF

You also have the the option to upload a WebP file, which Klaviyo can convert to a PNG file for you. Other file types, such as MP4, are not supported for MMS.

If you choose to upload an image, Klaviyo's [automatic image compression](https://help.klaviyo.com/hc/en-us/articles/115005253688#h_01JVN2QQXD9N2QT2MQ9D7PGX6S) tool optimizes clarity and ensure fast load times. For more details on using graphics, check out [MMS image and GIF best practices](https://help.klaviyo.com/hc/en-us/articles/360041074911).

## Best practices for SMS

When it comes to crafting your message, it's important to follow these dos and don'ts.

|  |  |
| --- | --- |
| ****Dos**** | ****Don'ts**** |
| Keep SMS messages short (under 153 characters) | Use acronyms or text-speak (unless you know your audience understands them) |
| Include a link shortened by Klaviyo | Assume images/GIFs are always better |
| Add personalization via template variables | Rely too much on emojis |
| Follow compliance regulations | Don't send before 9 a.m. or after 8 p.m. in a recipient's local time |
| Always get consent before texting |  |
| Limit text to between 2 and 6 times per month |  |

### Dos

****Why keep SMS under 153 characters?****

You only have a matter of seconds to make an impression on your recipients. When you keep your message short, your recipients can see the value of a text immediately.

Further, SMS messages are limited to:

- 160 text characters normally
- 70 characters if there are any symbols, emojis, or special characters
  - Symbol examples: © and ™
  - Special character examples: λ and ń

If you have any personalization or event variables, your messages won't all have the same number of characters in them. For instance, let's say you want to include someone's first name using the variable {{ first\_name|default:'friend' }}, and Klaviyo estimates 6 characters for a first name. However, if your recipient's name is "Alexander," the actual character count is 9. Thus, it's important to leave a few extra characters in your SMS.

Note that when an SMS extends beyond 1 message, Klaviyo includes a header on the backend so that carriers know the 2 sends go together. The header takes around 7 characters for every message segment, meaning that 2 SMS segments have a total character limit of 306.

****Why include a link using the Klaviyo link shortener?****

As a best practice, always include a link in your SMS messages and use Klaviyo's link shortener.

A key metric for SMS is click rate, as almost all SMS messages are opened. If there's no link in the message or the link is not shortened, you won't have insight into how your SMS and MMS messages are performing, as Klaviyo won't be able to track the messages. Shortened links are typically 24–25 characters, but this can vary.

If you want iOS 10+ users to see a preview of your link, you need to do two things:

- Include http:// or https:// at the start of the link
- Place the link at the very beginning or end of the message

Note that for this to work, the link cannot be followed by any other text (including opt-out language). Further, this only works when there is only one link per message.

****Why add personalization via template variables?****

Just like with email, SMS messages tend to perform better the more they are personalized to the recipient. However, note that when using variables, the exact character count will vary depending on the recipient.

To add personalization via profile properties, you can use any of the properties in the ****Personalization**** dropdown, which shows all of the [custom and profile variables](https://help.klaviyo.com/hc/en-us/articles/115005084927-Template-Tags-and-Variable-Syntax) available in Klaviyo. Using this, you can, for example, address the recipient by their first name, if it's known. If it's not, you can use a generic term, such as "friend."

In flows, you also have the option of adding event tags. For instance, in an abandoned cart flow, you can show the name of the first item someone left behind.

****Why follow compliance regulations?****

SMS is more heavily regulated than most other marketing channels, so it's especially important to be mindful of compliance. Failure to adhere to these laws may result in anything from carriers blocking your messages to fines.

Depending on your recipient's location, different rules may apply. To make it easier, we recommend not adjusting the settings in the ****Compliance**** tab. These option will apply only to recipients in the countries listed below the option, and are considered to be the best practice for those areas.

Note that either [unsubscribe instructions or an opt-out link is typically required](https://help.klaviyo.com/hc/en-us/articles/360035055312).

****Why do I need to get consent before texting?****

You need to have the proper permission to text someone. In most countries, it's illegal to send an SMS or MMS to anyone who hasn't explicitly opted into SMS marketing. Just having someone's phone number is not enough.

Make sure you’ve obtained a customer’s phone number from a legal source (i.e., signup form, in-person event, opt-in on a checkout page). Klaviyo will never send an SMS to a profile that doesn’t have consent. For more information head to the article on [how to collect SMS consent](https://help.klaviyo.com/hc/en-us/articles/360035056972).

****Why should I limit the number of texts per month?****

It’s best practice to text a single SMS recipient anywhere from 2 to 6 times a month. Like your emails, you’ll want to make sure that you stick to a regular schedule when sending out your SMS messages.

Additionally, create a customer journey for someone who signs up for your welcome series or abandons a cart, and figure out how often you’re communicating with that person. You don’t want to communicate too little or too much with a customer. Anywhere between 2 and 6 messages a month is a good cadence to start.

### Don'ts

****Why shouldn't I use text-speak or acronyms?****

While it may be tempting to use text-speak or acronyms to make your messages shorter, it's not recommended.

Unless you know your audience both understands and prefers them, using acronyms may confuse your recipients.

If your audience will know and appreciate text-speak, still be careful of overusing it (i.e., don't use it for the majority of the message).

****Aren't GIFs and images always better?****

While each audience is different, typically MMS performs similarly to SMS. In terms of performance, SMS tends to perform better than MMS in most cases.

MMS is also not available in every country. When it is available (e.g., US and Canada), MMS messages more credits than SMS.

That being said,GIFs and static and [dynamic images](https://help.klaviyo.com/hc/en-us/articles/1260806102230) can enhance your text messages. They can be good for product launches or abandoned cart reminders. We recommend testing how MMS perform for you to see where MMS makes the biggest impact.

****Why shouldn't I rely too much on emojis?****

Emojis can make an impact, but like acronyms and text-speak, should be used sparingly. Overusing them may annoy your audience, and not every audience responds to emojis positively. Emojis can take the place of words, but having an entire message be emojis may confuse recipients.

We recommend testing emojis on your audience to see if they prefer them and find out how often you should send them.

Keep in mind that using just 1 emoji reduces the character count for an SMS from 160 to 70.

****Why shouldn't I send before 9 a.m. or after 8 p.m.?****

As you send out your texts, you’ll want to send them between 9 a.m. and 8 p.m. in the recipient's local time. Most likely, sending an SMS too early in the morning or too late at night will lead to fewer conversions and more people unsubscribing from communication with you.

For flows, there are quiet hours, which restrict the times when SMS messages can go out based on the country code for the recipient's phone number. For campaigns, you must segment your subscribers by country and be conscious of their local time. Klaviyo warns you if your campaign will potentially violate quiet hours.

Test when your recipients like to hear from you. For instance, many ecommerce businesses find that sending around noon on Sunday leads to better performance.

## Preview your messages

To preview your messages, you can do either of the following:

- View your message as a certain recipient in the SMS editor
- Send a test message to your phone

### View your message as a certain recipient

As you begin creating your message, you'll see how the message will look once it's delivered to a certain recipient in a specific country. The country is selectable from directly above the preview.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627678843675)

To see which profile you're previewing as, or select a different profile, click ****Preview & test**** in the top right corner. For list- and segment-triggered flows, you can search any profile in your account or choose from the 10 most recent profiles added to the list or segment.

Date property-based flows are similar except that they will only show a profile that has the date property that triggers the flow.

When it comes to metric-triggered flows, the modal will show the 10 most recent events for the flow's trigger along with the associated [event variables](https://help.klaviyo.com/hc/en-us/articles/115002779071-Personalize-Flow-Emails-with-Dynamic-Event-Data). Like with the profile properties, you can simply click on one of the variables to copy it to your clipboard.

### Send a test message to a personal phone

You can also send previews of a message your phone number. For paid accounts, there's a limit of 200 previews per account per day, while the limit is 25 previews for free accounts.

To send a preview:

1. Click ****Preview & test**** in the upper right.
2. Select your country code.
3. Add in your phone number.
4. Optionally, select the option **Save phone number as your default test recipient** if you plan to use that number for testing in the future.
5. Click ****Add phone number**** and repeat these steps if you'd like to send previews to multiple people at once.
6. Click ****Send test****. ****![](https://klaviyo.zendesk.com/hc/article_attachments/33627692521883)****

## Additional resources

- Course: [Getting started with SMS](https://academy.klaviyo.com/getting-started-with-sms/1411601)
- Get advice for building your SMS program:
  - Blog post: [SMS marketing strategies for all levels [+12 Pro tips]](https://www.klaviyo.com/blog/sms-marketing-strategies)
  - Guide: [your strategic guide to Klaviyo SMS success](https://help.klaviyo.com/hc/en-us/articles/25220861016091)