---
id: "4406796460443"
title: "How to A/B test SMS campaigns"
source_url: "https://help.klaviyo.com/hc/en-us/articles/4406796460443-How-to-A-B-test-SMS-campaigns"
section: "Send and optimize SMS campaigns"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:59Z"
language: "en"
---
## You will learn

Learn how to A/B test SMS campaigns and what aspects to test in this article.

With A/B testing for Klaviyo SMS, you can gain insight into your audience and use that information to optimize your messages and send times. SMS A/B testing is currently only available for campaigns, but you can [test your SMS flow messages using splits](https://help.klaviyo.com/hc/en-us/articles/360049849432).

## Best practices for A/B testing SMS

Like with email, there are several best practices for A/B testing SMS:

- Test 1 aspect at a time.
- Include a link and use the Klaviyo link shortener.
- For MMS: keep any images or GIFs under 600 KB.
- Optimize your CTA and message text.

### What to test

Here are a few ides for what to A/B for SMS:

- ****MMS versus SMS****
  SMS tends to perform the same or better than [MMS](https://help.klaviyo.com/hc/en-us/articles/6456860853275). Since MMS costs more credits, it's worth finding out if sending MMS messages makes sense for your brand.
- ****Emojis****
  Like MMS, SMS without emojis tend to have the same or better performance. In addition, [emojis shorten the character limit](https://help.klaviyo.com/hc/en-us/articles/17275332265627) for SMS from 160 to 70, often leading to you needing to use more credits for that send.
- ****Message length****
  Shorter SMS messages also tend to have higher engagement, but it's worth testing how your subscribers respond to longer-form SMS messages.
- ****Language (in a certain area/country)****
  Depending on your audience, you may want to test which language performs best for a certain segment, region, or country. This can be helpful if there are multiple official languages for a country (like in Switzerland) or when determining whether to send in a different language to a certain segment or area (e.g., Montreal).

You should also test different types of SMS campaigns; e.g., product promotion, newsletter, sale, etc. What performs well for one type of message may not perform well for another. Further, a campaign might yield different results than a flow message, so do not apply the results of an A/B test to every message you send.

## Before you begin

Klaviyo gives you the option to either test message content (e.g., the call-to-action, emojis, and images/GIFs) or send times.

## A/B test SMS messages

Regardless of whether you want to test message content or send times, start by following these steps:

1. Click ****Campaigns > Create > SMS****.
2. Choose your campaign name, recipients.
3. Click ****Next****.
4. In the **Message content** box, craft your message (you will not be able to create an A/B test until you add content).
5. Click ****Create A/B Test**** to create a copy of your existing message (including any images, GIFs, personalization, etc.)
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627735482011)
6. Next, decide if you want to:
   1. [A/B test the SMS content](#h_01G2DEC06H1ZXJ28CWNA532G69)
   2. [A/B test SMS send times](#h_01G2DEC83SZWVSQBJN352Z2X81)

### Test SMS content

1. Click the dropdown menu for the variations.
2. Choose the variation you want to change for the test.
3. Change only one aspect from the original (e.g., if you add an image, do not change anything else about the message).
4. Click ****Continue to Test Settings**** in the upper right.
5. [Review your A/B test settings](#h_01G2DEQ9E8PPKEMGPF9FBEKZV0) (click the link to skip to that section).

If you are A/B testing content and would like to send your message based on each recipient’s timezone, set your test size to 100%. When scheduling your campaign, you’ll have the option to choose ****Recipient’s Local Timezone**** as the timezone for your send.

![SMS recipient local time zone.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717993828763)

### Test SMS send times

1. Segment your audience by [location](https://help.klaviyo.com/hc/en-us/articles/115005065887) or [country](https://help.klaviyo.com/hc/en-us/articles/4402954226459).
2. Choose which segment you want to A/B test.
   Note: you should only send the A/B test to one of these segments so that you don’t risk messaging someone too late at night or early in the morning. Klaviyo warns you if your campaign will potentially violate quiet hours.
3. Keep the message content exactly the same.
4. Select ****Continue to Test Settings**** in the upper right.
5. In the A/B test settings page, click ****Test send times****.

   ![Test send time option.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717993831451)
6. Choose the times you want to A/B test.
7. Configure the rest of the A/B test’s settings, which is discussed in the next section.

## Select a test strategy

The option to choose a test strategy is only available for accounts with more than 400,000 total profiles. If your account doesn’t qualify, Klaviyo will use the winning variation test strategy.

If your account qualifies, decide on your testing strategy from the following options:

- Winning variation (Standard A/B test)
- Personalized variations for each recipient

![](https://klaviyo.zendesk.com/hc/article_attachments/28717988042267)

### The difference between winning variation and personalized variations

Both test strategy options will send variations to a test group composed of a percentage of the campaign’s total recipients and test message success based on a metric of your choosing, e.g., open rate. However, there are some key differences for how each strategy sends messages to the rest of the recipients after the test period is over:

- ****Winning variation**** - the default option for A/B tests, which will determine 1 winning variation and send it to the rest of the campaign's recipients after the test period is over.
- ****Personalized variations**** - uses AI to search for patterns amongst the test recipients who interact with each variation. After the testing period is over, Klaviyo will predict which variation will perform better for each recipient and send the rest of the recipients their preferred variation.

### Personalize variations for each recipient

If you’d like to personalize which variation each recipient receives on an individual basis, select ****Personalized variations for each recipient****.

Klaviyo will use information about each profile to determine which variation is most likely to succeed in converting that profile. This profile information includes, but is not limited to:

- Historical engagement rates
- Customer lifetime value (CLV)
- Location

For example, if you have chosen open rate as your winning metric and profiles in the test group with a CLV of 100 or more open variation A more frequently, but profiles with a CLV of less than 100 open variation B more frequently, the rest of the campaign's recipients will receive SMS based on which variation they are most likely to open according to their CLV. This is a simplified example, as Klaviyo will use many data points to determine personalized variations.

## Adjust an A/B test’s settings (optional)

You can view the settings for your test and adjust:

- The test's winning metric (click rate or placed order rate)
- What percentage of people receive each variation
- The test duration

Once a winning variation is selected, the winner will be sent to the rest of the audience.

![SMS AB test settings.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717988034331)