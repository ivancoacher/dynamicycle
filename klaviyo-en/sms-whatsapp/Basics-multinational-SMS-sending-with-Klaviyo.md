---
id: 23740503987099
title: "Basics: multinational SMS sending with Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/23740503987099-Basics-multinational-SMS-sending-with-Klaviyo"
section: "Sending best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:35Z"
language: en
---

## You will learn

Learn tips for using Klaviyo to send SMS in multiple different countries.

SMS is a global mobile marketing channel. Other mobile channels require an app, whereas SMS is built into every phone, making it automatically accessible.

In this article, learn best practices for sending in multiple countries as well as how sending works when you have multiple numbers.

This article is also recommended if you use a branded sender ID or toll-free number and don’t want to send to every country the number can send to. Since these number types use the same number to automatically collect consent and send to multiple countries, you’ll need to target your forms and messages based on the user’s location.

## What’s so different about sending SMS in multiple countries?

Depending on which countries you’re sending to, you may need to be aware of things like your messaging frequency, local regulations, or your recipient’s language.

For instance, some parts of Canada use French as their first language, while others use English. Also, the US and Canada both have 6 time zones. If you’re not located in North America, it may be hard to know when your recipients will actually get your message.

Credits vary by the recipient's country. When sending multi-nationally, it's important to segment your audience by country so you have a more accurate estimate of how much a campaign will cost.

There are also differences in functionality, such as the ability to send MMS or receive text messages from subscribers. Additionally, you can use some sending numbers across multiple countries, while others are country-specific. For a full breakdown of differences, see our [guide on sending numbers](https://help.klaviyo.com/hc/en-us/articles/6637671573403).

## Best practices for sending in multiple countries

 When sending in multiple countries, there are a few best practices to follow:

- [Segment by country, engagement, and interests](#h_01HRSTJJB0AYP4K6XGFD3HT7AD).
- [Target by location and language in your forms, flows, and campaigns](#h_01HRSTJJB0DECV62NWYA5VK86J).
- [Focus on high-engagement or revenue-generating flows](#h_01HRSTJJB06BN0B30WDGPR1GRM).
- [Be aware of your character count](#h_01HRSTJJB1Q7JJY1M1RHMXEX12).

### Segment by country, engagement, and interests

It's always important to maximize your ROI, but it’s even more important to think about this when sending SMS multi-nationally. Not every individual in every country will want to engage with the same content, in the same language, and at the same frequency.

For the best results, get as specific as possible so that you can target only those who would be interested in a particular text message.

To get started, you can segment by:

- Language (e.g., German speakers).
- [SMS error](https://help.klaviyo.com/hc/en-us/articles/9821790118171)

With a language-based segment, you can make sure you’re sending in the right language. This can be especially important when sending to a country that commonly uses multiple languages, such as Switzerland.
**![Example of a language-based segment where the language is Irish](https://klaviyo.zendesk.com/hc/article_attachments/28717881827227)**

As for the SMS error segment, exclude it from most campaigns so you can avoid using credits with any unavailable profiles (i.e., the ones who won’t receive the SMS message). Only send to this error segment around once a month so you can see if the error is resolved.

As your SMS subscriber list grows, use other engagement segments to better personalize your messages:

- Engaged
- VIPs
- Marketing preference (e.g., product alerts, sale-only, etc.)
- Product collection/hobby/interest
- Prefers SMS

![Simple segment example of engaged German SMS subscribers](https://klaviyo.zendesk.com/hc/article_attachments/28717881814555)

### Target by location in your forms, flows, and campaigns

Similarly to creating country-based segments, you want to make sure your forms, flows, and campaigns get directed to the right audience.

For campaigns, you want to send in the recipient’s local timezone whenever possible.

Targeting by location also helps ensure your content is in the right language, or simply using the right spelling, for your audience. However, it’s also important if you **don’t** want to send to a certain country.

Let’s run through some scenarios where you need location targeting:

- Showing Canadians in Quebec a form in French.
- Sending a campaign to those in Ireland and the UK for Boxing day.
- Splitting a flow so that Germans receive a text in German.
- Not collecting consent in a certain country when using either a branded sender ID or toll-free number.
- Avoiding sending MMS in Australia.
- Using a tap-to-text forms (in most cases).
  While you can use the same tap-to-text form for both the US and Canada, this only works if you’re using a toll-free number for both countries. If you purchase a short code for at least 1 country, you need to change the form to target 1 country, clone the form, and then change the targeted location and sending number for the new form.

The sections below show examples of how you can target the right audience using a mix of segments and built-in targeting functionality.

****Forms****

If you need to create a form in 2 or more different languages, you must create multiple versions of that form and change the targeting.

To do this:

1. Navigate to ****Targeting & behavior****.
2. Select the ****Targeting**** tab.
3. Scroll down to the **Location** section.
4. Select the region or country where the form should or should not display.
   ![Targeting a form to show only in Canada](https://klaviyo.zendesk.com/hc/article_attachments/28717887857691)

In general, Smart Opt-in is recommended over tap-to-text, particularly when sending to multiple countries. However, if you do decide to use tap-to-text forms, you must also change the **Sending region** by:

1. Clicking on the ****tap-to-text button****.
2. Scrolling to the **SMS Settings** section.
3. Next to the **Sending Region**, choose the country where you want to use this form.
   ![Choosing Canada and the United States as the sending region for a tap-to-text
       form](https://klaviyo.zendesk.com/hc/article_attachments/28717887859611)

Keep in mind that the only time the sending region can be multiple countries is if you’re using a toll-free number for both the US and Canada. In all other cases, including if you have a short code for either the US or Canada, you must have a separate tap-to-text form for each country.

****Campaigns****

You can target SMS campaigns by country, so you do don’t need to create separate, country-based segments everywhere you send.

Simply select the country (or countries) you want to send to in the SMS campaign wizard.

![Multi-country.jpg](https://klaviyo.zendesk.com/hc/article_attachments/29895323867419)

You can also preview how your message will appear to recipients in different countries when creating your message.

![](https://klaviyo.zendesk.com/hc/article_attachments/38114965871003)

****Flows****

The 2 best ways to split recipients in flows are using:

- Phone number country code.
- Profile’s language (if available).
  - This only works if you have collected someone’s preferred language.

The table below shows how to split recipients in flows using each of these methods.

|  |  |
| --- | --- |
| ****Phone number country code**** | ****Profile’s language**** |
| 1. Add a conditional split to your flow. 2. Set the condition as: **Properties about someone > country code in** 3. Select the country you want for your split. | 1. Add a conditional split to your flow. 2. Set the condition using your custom language property (e.g., Language): **Properties about someone > Language > equals** 3. Select the language you want to split by. |
| ![Conditional split to send those with a German country code down a different flow path](https://klaviyo.zendesk.com/hc/article_attachments/28717887851291) | ![Conditional split to send those who speak German down a different flow path](https://klaviyo.zendesk.com/hc/article_attachments/28717887863195) |

You can also preview how your message will appear to recipients in different countries when creating your message.

![](https://klaviyo.zendesk.com/hc/article_attachments/38114965871003)

### Focus on high-engagement and revenue-generating flows

SMS is a relatively new marketing channel. While it’s gaining popularity, audiences in different countries may not be as receptive to text message marketing as others.

For example, in the US, subscribers expect texts about sales, promotions, product announcements, reviews, and more. In Europe, SMS is less common and mainly used by businesses. Because of this, people in Europe typically want to be texted only for things they deem important, like deals or transactional messages. They also prefer more infrequent texts compared to the US.

In general, it’s best to let your subscriber’s actions drive your SMS efforts. By using the following high-engagement and high-revenue flows, you can maximize your ROI while providing subscribers with content that interests them:

- [Welcome series](https://help.klaviyo.com/hc/en-us/articles/360036122291)
- [Abandoned cart](https://help.klaviyo.com/hc/en-us/articles/9352115400219)
- [Back in stock](https://help.klaviyo.com/hc/en-us/articles/7954040204827)
- [Price drop](https://help.klaviyo.com/hc/en-us/articles/4404249033755)
- [Birthday](https://help.klaviyo.com/hc/en-us/articles/360054242492)

You can also use SMS in transactional flows. However, know that these flows are more to build the relationship between the subscriber and your brand, not generate revenue.

### Be aware of SMS character count

It is always a good idea to keep your SMS messages short, especially when you’re sending in multiple languages and when you’re trying to get the most out of your credits.

As a best practice:

- Always check the estimated character count before sending.
- Limit your messages to around 155 characters.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/33627734980379)

Note that SMS messages typically allow for 160 characters, but a few things shorten the count:

- [Special characters](https://help.klaviyo.com/hc/en-us/articles/17275332265627) and emojis shorten the limit to 70 characters.
  - Special characters can appear almost identical to normal characters.
  - Non-Latin letters (including á, â, ç, ê, î, í, ô, ó, and ú) may be counted as special characters.
- Any type of dynamic or personalized content means the actual character count will vary from person to person.
  - For example, if you include the first name tag, the message to someone named “Ana” will have fewer characters than the same message to “Anastasia.”

## How sending works for multi-national accounts

You can have 1 Klaviyo account with several sending numbers. Klaviyo automatically detects where each recipient is located and then sends to them using a number for that country.

Say that you have a toll-free number for the US and a long code for the UK. To send to all of your subscribers, you don't have to set up multiple campaigns. Instead, you only need 1 campaign, as Klaviyo will automatically use your toll-free number for recipients with a US number and your long code for recipients with a UK number.

You can only have 1 sending number per country.

Learn more about [SMS sending numbers](https://help.klaviyo.com/hc/en-us/articles/6637671573403).

## Additional resources

- Learn how to [get started with Klaviyo SMS](https://academy.klaviyo.com/getting-started-with-sms/1411601)
- Get advice for building your SMS program:
  - Blog post: [SMS marketing strategies for all levels [+12 Pro tips]](https://www.klaviyo.com/blog/sms-marketing-strategies)
  - Guide: [your strategic guide to Klaviyo SMS success](https://help.klaviyo.com/hc/en-us/articles/25220861016091)