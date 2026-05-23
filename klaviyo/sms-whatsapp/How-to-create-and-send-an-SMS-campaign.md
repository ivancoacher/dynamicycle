---
id: 360040039971
title: "How to create and send an SMS campaign"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360040039971-How-to-create-and-send-an-SMS-campaign"
section: "Send and optimize SMS campaigns"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: en
---

Learn how to create and send an SMS campaign in Klaviyo. Note that the process is almost exactly the same for MMS campaigns. The only difference is that you add an image or GIF during the content creation stage.

## What is an SMS campaign?

An SMS campaign is a one-time text message to a list or segment of subscribers, notifying them of events such as product launches, flash sales, or other promotions. You can set an SMS campaign to send either immediately or at some point in the future.

## Before you begin

Before sending an SMS campaign, you must have:

- [Turned on SMS](https://help.klaviyo.com/hc/en-us/articles/4404274419355)
- [Collected SMS consent](https://klaviyo.zendesk.com/hc/en-us/articles/360035056972)
  - Note: having someone's phone number does not count as consent; someone must have explicitly agreed to receive SMS marketing messages

You should also have a list or segment of those who you want to send to, such as [everyone who is subscribed to SMS](https://help.klaviyo.com/hc/en-us/articles/360035800811).

### Campaigns vs. flows

|  |  |
| --- | --- |
| ****Campaigns**** | ****Flows**** |
| 1-time sends that are manually scheduled | Automated and ongoing sends |
| Sent to a specific list or segment | Triggered by customer actions or profile properties |
| Content is more broad with limited personalization | Content is more specific and can be highly personalized |

### Smart send time is only available with email

Note that unlike with email, you cannot use Smart Send Time with SMS, MMS, or push notifications.

## Create an SMS campaign

[Embedded content](//fast.wistia.com/embed/iframe/uv9azawk9n)

1. Head to the ****Campaigns**** tab.
2. Click ****Create campaign**** in the upper right.
   ![Create campaign button in the Campaigns page](https://klaviyo.zendesk.com/hc/article_attachments/29895404946331)
3. Name your campaign.
4. Choose ****SMS**** as the type of campaign.
   ![Sidebar to name and select what type of campaign to send](https://klaviyo.zendesk.com/hc/article_attachments/29895429269531)
5. Click ****Continue****.
6. Under **Audience**, select the list(s) or segment(s) you want to send to.
   ![Choosing which countries the campaign should go to](https://klaviyo.zendesk.com/hc/article_attachments/29895429276059)
7. Optional:
   - - To avoid sending to certain groups, add a segment under **Don't send to**.
       ![Adding a segment to exclude from the campaign](https://klaviyo.zendesk.com/hc/article_attachments/29895429280667)
     - To avoid sending recipients too many SMS messages at once, turn on Smart Sending to skip profiles who have recently received a message. With SMS, you can specify whether to skip based on a recently received campaign message, flow message, or both.
       ![Smart Sending ensures a person doesn't receive too many SMS messages in a certain timeframe](https://klaviyo.zendesk.com/hc/article_attachments/30910488021659)

       The option to skip based on message type is only available for SMS campaigns.
8. Click ****Next****.
9. Write your content in the **Message** box at the upper left-hand corner of the screen.
   - Note that SMS content is limited to 160 characters or (if you have an emoji or special character) 70 characters.
10. Add a link to your message so that Klaviyo can track the message.
    - Do not uncheck the ****Automatically shorten links**** box.
      ![Leave the shorten links option turned on](https://klaviyo.zendesk.com/hc/article_attachments/33627680976795)
11. Note: disabling the options in the ****Compliance**** tab is not recommended.
    - Certain aspects (opt-out language/links, contact information, etc.) are required in some jurisdications.
12. Optional: Add media to your message to turn it into an MMS.
    - The [image or GIF must be under 600 KB](https://klaviyo.zendesk.com/hc/en-us/articles/360041074911).
    - MMS is not available in all countries.
    - MMS increases the character limit 1600.
    - MMS costs more credits under the [Klaviyo billing plan](https://klaviyo.zendesk.com/hc/en-us/articles/115000976672).
    - [MMS is not recommend during holiday seasons](https://klaviyo.zendesk.com/hc/en-us/articles/6456860853275).
13. Optional:
    - Click ****Preview & test**** to preview the message as a certain profile.
      ![The Preview and test button](https://klaviyo.zendesk.com/hc/article_attachments/33627680982043)
    - Select country dropdown to view how the message appears to recipients in a specific country.
      ![Country preview dropdown](https://klaviyo.zendesk.com/hc/article_attachments/38108180943643)
14. Click ****Next****.
15. On the review page, check that the campaign:
    - Is sending to the right audience.
    - Can be tracked.
    - Does not exceed the [credits in your SMS billing plan](https://help.klaviyo.com/hc/en-us/articles/13502982552347).
16. Click ****Schedule or Send**** on the bottom right when the campaign is ready to go out.
17. Select whether you want to send now or at some point in the future.
    - Note that you should not send a campaign before 9 a.m. or after 8 p.m. in the recipient's local time. Klaviyo warns you if your campaign will potentially violate quiet hours.
18. Click either ****Schedule****or ****Send Now****.

Note that any SMS or [MMS campaign](https://help.klaviyo.com/hc/en-us/articles/6456860853275) will typically time out after around 4 hours, and if someone didn’t get the message in that timeframe, they will be skipped. Due to this, you may need to break up large campaigns if your sending number is a long code, toll-free number, or branded sender ID.

## Best times and days to send

The best times and days to send depends on your audience, so you should always test what works best for your brand.

However, if you're not sure where to start, the following generally holds true:

- Weekday vs. weekend
  - Weekday campaigns lead to higher revenue.
  - Weekend campaigns have higher click rates.
- Time of day
  - 1 to 5 p.m. and 6 to 8 p.m. (in local timezones) have higher click rates than other hours.

## Additional resources

Learn more about SMS in the Help Center:

- [Getting started with Klaviyo SMS](https://academy.klaviyo.com/getting-started-with-sms/1411601)
- [How to create an SMS welcome flow](https://klaviyo.zendesk.com/hc/en-us/articles/360036122291)
- [Understand and review your SMS deliverability](https://klaviyo.zendesk.com/hc/en-us/articles/1260806260849)