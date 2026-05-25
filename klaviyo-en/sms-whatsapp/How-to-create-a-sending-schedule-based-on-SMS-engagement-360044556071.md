---
id: "360044556071"
title: "How to create a sending schedule based on SMS engagement"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360044556071-How-to-create-a-sending-schedule-based-on-SMS-engagement"
section: "Send and optimize SMS campaigns"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: "en"
---
## You will learn

Learn how to create engagement tracks based on your sending schedule for your SMS subscribers.

The advice in this article is simply a starting point. Your ideal sending frequency, engagement, etc. all depend on a number of factors, including industry, audience, and the types of messages you send.

## Sending schedule best practices

For those first starting out with SMS, we recommend sending between 2-4 times a month. Then, slowly ramp up your sending to between 4-7 times per month, depending on your desired sending schedule.

The following are all best practices for creating your sending schedule:

- Send to SMS subscribers at least 1 to 2 times a week, as sending often leads to more revenue-generating opportunities.
  - Do not send SMS every day unless the subscriber knowingly opted in to daily reminders (e.g., for taking medicine).
- If you explicitly collect your customers’ communication frequency or content preferences,  tailor your communications to those preferences.
  - For instance, if someone asked to only receive information about events, do not send them promotional material. After some time, and if they are highly engaged, ask if they’d like to update their preferences to receive more information.
- Monitor your unsubscribe rate to make sure it doesn’t rise above 2% per campaign.
- Use Smart Sending and send in the recipient’s local times to avoid over-messaging or sending at odd times of day.
- Build familiarity into your sending schedule, such as by:
  - Sending at a certain time and day each week, so subscribers know when to expect your message
    Or
  - Establishing a pattern when you send certain content, so subscribers know what they can expect (e.g., Promotion Tuesdays or launching products the last week of the month)
- Provide a variety of different types of SMS messages to subscribers.

****What do you mean by a variety of different SMS?****

It’s important to mix up the type of SMS you send. Otherwise, your messaging can become predictable, and your recipients may no longer find value in being an SMS subscriber.

Sending 1-2 of each of the following in a month helps you create that variety:

- Announcements for promotions, new products, or holiday deals.
- Early access or last messages for major announcements.
- Targeted campaigns for specific segments, such as:
  - People who viewed a certain product or category: send price drop or cross-sell messages.
  - VIPs: send exclusive content like blogs or podcasts, offer sneak peeks, or reminders for reward points.
  - Non-purchasers: offer assistance or send a reminder for first purchase discounts.

****What to do if your unsubscribe rate is 2% or more****

If you have a high unsubscribe rate, review the following:

- Check that you’re using double opt-in.
- Make sure you clearly explain what to expect from your SMS program wherever you collect consent.
- Look at your content to see if it’s providing value to subscribers.

If you do all of the above and still have a high unsubscribe rate, consider slowing down your sending to only once every other week.

[Embed](//fast.wistia.com/embed/iframe/ngtp5l1oy0)

## Before you begin

When planning your sending schedule and setting up your engagement, please keep the following in mind:

- Brands or industries with long buying cycles may need to send less frequently or to a more targeted audience.
  - For instance, luxury clothing brands may only send weekly to their most frequent shoppers.
- If you don’t always include Klaviyo shortened links in your messages, you may need to extend the engagement criteria or base the segments on something other than **Clicked SMS** (such as **Active on Site**), since clicks can’t be recorded without a link.

## Create your engagement tracks

There are 3 engagement tracks you want to set up:

- Track A: new subscribers or high engagement (e.g., engaged 1 of the last 3 sends)
- Track B: medium engagement (e.g., engaged between 4 and 8 sends ago)
- Track C: low engagement (e.g., engaged more than 8 sends ago)

Below, we show how to set up these tracks for the example of a weekly sending schedule.

### Track A: high engagement

Send weekly to everyone who is either a new subscriber or has engaged recently. For a weekly sending schedule, we’re defining this as anyone who has clicked an SMS in the last 90 days.

For this, you need to create the following segment:

- If someone can or cannot receive marketing > can receive > SMS marketing
  AND
- What someone has done > Subscribed to SMS marketing > at least once > in the last 30 days
  OR
- What someone has done > Clicked SMS > at least once > in the last 90 days
  ![track A.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716330698395)

****Recommendation****: Send to this group every week.

### Track B: medium engagement

This group contains anyone who is less engaged with your texts, but has not completely unengaged with you.

For this segment, use the following condition:

- If someone can or cannot receive marketing > can receive > SMS marketing
  ****Add filter****
  And subscribed date is at least 30 days ago
  AND
- What someone has done > Clicked SMS > at least once > between 91 and 150 days ago
  ![Track b.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716330697115)

****Recommendations****:

- Send to this group every other week.
- Try to re–engage these subscribers, such as by:
  - Offering a special coupon.
  - Asking for their preferences (e.g., if they prefer email or what type of SMS message they want).

### Track C: low to no engagement

If you’re sending weekly, anyone who hasn’t engaged with your SMS messages in the past 150 days is unengaged with your brand and should be excluded from most campaigns.

For this segment, use the following condition:

- If someone can or cannot receive marketing > can receive > SMS marketing
  ****Add filter****
  And subscribed date is at least 30 days ago
  AND
- What someone has done > Clicked SMS > zero times > in the last 150 days
  ![Track C.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716353716123)

****Recommendations:****

- While you should exclude these profiles from most of your campaigns, send to them at least 1 time per month to keep the contacts warm. Additionally, consider including them in more important sends like:
  - Your biggest sales (e.g., Black Friday/Cyber Monday).
  - Large or exciting product launches.
- Only flows to send SMS messages to this group.
- You may want to set up a flow to add a profile property to anyone who falls into this segment more than 1 time, then add that property as a condition in this segment.

### Adjust the tracks for a different sending schedule

The table below shows how the conditions for Track A may change depending on your sending schedule.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ****Engagement criteria for track A**** | ****Sending schedule**** | | | |
| ****Twice a week**** | ****Weekly**** | ****Every other week**** | ****Monthly**** |
| ****Subscribed to SMS in the last**** | 30 days | 30 days | 60 days | 90 days |
| ****Clicked SMS in the last**** | 60 days | 90 days | 120 days | 150 days |

## SMS error segment

In addition to following a sending based on SMS engagement, you can create an SMS error segment to capture profiles currently unable to receive SMS messages. You can exclude this segment on an ongoing basis to maintain strong deliverability and better utilize your SMS credits.

## Additional resources

- Check out other articles on segments that help you target your subscribers:
  - See [recommended segments for SMS](https://help.klaviyo.com/hc/en-us/articles/360047879512)
  - Learn how to [clean your SMS lists](https://help.klaviyo.com/hc/en-us/articles/6155416998555)
- Get advice for building your SMS program:
  - Blog post: [SMS marketing strategies for all levels [+12 Pro tips]](https://www.klaviyo.com/blog/sms-marketing-strategies)
  - Guide: [your strategic guide to Klaviyo SMS success](https://help.klaviyo.com/hc/en-us/articles/25220861016091)