---
id: 45231714007323
title: "Drive performance with right time delivery using Personalized Send Time"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/45231714007323-Drive-performance-with-right-time-delivery-using-Personalized-Send-Time"
section: "Predictive models"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-05-11T12:54:50Z"
language: en
---

## ****You will learn****

- What Personalized Send Time is and how it differs from [Smart Send Time](https://help.klaviyo.com/hc/en-us/articles/360029794371).
- When to use Personalized Send Time in your campaigns.
- How to set up a campaign with Personalized Send Time.
- How to view and interpret Personalized Send Time performance reports.
- Eligibility, supported channels, and current limitations.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## ****What is Personalized Send Time?****

Personalized Send Time automatically schedules each campaign message at every recipient’s predicted best time within a delivery window you choose. You set a send date and time window, and Klaviyo delivers in each recipient’s local time at the time most likely to drive engagement and conversions.

Unlike [Smart Send Time](https://help.klaviyo.com/hc/en-us/articles/360029794371), which finds a single optimal time for your entire audience, Personalized send time optimizes delivery at the profile level, so different recipients can receive the same campaign at different times within your window.

## ****When you should use Personalized Send Time****

Use Personalized Send Time when:

- You’re sending non-urgent campaigns where maximizing opens, clicks, or orders is more important than everyone receiving the message at the exact same moment.
- You’re comfortable delivering over a send window and in the recipient's local time zone rather than all at once.

  Avoid Personalized send time for:
- ****Time-sensitive content****, such as flash sales, expiring offers, or urgent announcements where all customers must receive the message by a specific clock time.
- ****Same-day sends****, since same-day scheduling is not supported yet (only future dates starting tomorrow).

## ****Who can use Personalized Send Time****

Personalized Send Time is available with the following scope:

- ****Plans:**** Available to customers on the Marketing Analytics or Advanced Klaviyo Data Platform (Advanced KDP) packages.
- ****Channels:**** Email, SMS, push, and WhatsApp campaigns. Personalized Send Time is not available yet in flows.

## ****How to use Personalized Send Time in campaigns****

Before you start, note that Personalized Send Time:

- Works in both single-channel and omnichannel campaigns
- Requires scheduling at least one day in advance (no same-day sending).

### ****1. Create a single-channel campaign****

- Create a campaign (email, SMS, push, or WhatsApp).
- Build your content as usual.
- Do not add an A/B test. Personalized Send Time is not available for A/B test campaigns at this time.

### ****2. Go to Review & schedule****

- From the campaign builder, proceed to the Review step.
- Click Schedule or send to open scheduling options.

### ****3. Enable Personalized Send Time****

- In the scheduling modal, click on the schedule options dropdown and select Personalized Send Time.
- Choose the send date: Select any future date starting tomorrow. Same-day scheduling is not available currently.
  - If a recipient cannot be scheduled on that date (for example, their valid time window has already passed), Klaviyo will send the next day during your defined window. See the FAQ section for details.
- Set your optimization window (optional): Klaviyo automatically selects the optimal delivery window to maximize performance. You can adjust the start and end times in recipient local time for the selected date if needed.

Klaviyo will determine each recipient’s best send time inside your chosen window.

![](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/b1792ddde9dce45c76d7d6cdf89d37acae5814cb-852x1230.png)

### ****4. Schedule your message****

- Review your settings and click Schedule. Klaviyo will queue each recipient to send at their predicted best time within your window, in their local time zone.

## ****How Personalized Send Time works****

Behind the scenes, Personalized Send Time uses reinforcement learning to intelligently choose send times when each profile is most likely to open, click, or place an order, based on past engagement behavior and similar profiles.

- Each recipient is assigned a best send time within your defined delivery window, in their local time.
- If a recipient’s exact best time is not available (for example, it has already passed on the scheduled date), Klaviyo chooses the next-best remaining time that still falls within your window.

  Personalized send time uses the following signals and behavior:
- Engagement and profile property data in your account. The model looks at opens, clicks, and placed order events across your campaigns (and channels where available) to learn when similar recipients are most likely to respond.
- Hour-level predictions inside your window. For each recipient, Klaviyo chooses an hour within your delivery window in their local time. For SMS, Personalized Send Time respects SMS quiet hours, so sends may be further constrained to compliant hours.
- First Personalized Send Time in your account. When you use Personalized Send Time for the first time, the model starts from a pre‐tuned default send‐time pattern that has been calibrated through prior testing and analysis.
- New profiles. When a new profile is added and doesn’t yet have engagement history, we start by using send-time patterns from similar profiles in your account so they still receive messages at reasonable times. If we don’t have enough information about similar profiles in your accounts, we fall back to what’s generally best for your account. As each person interacts with your messages, recommendations will gradually adapt and become more individualized.

### Time zone handling

- For email, push and Whatsapp: Personalized Send Time uses the profile’s local time zone.
- For SMS: Personalized Send Time uses the recipient’s phone number and area code together to determine the local time zone

## ****Measure performance for Personalized Send Time****

Campaigns sent with Personalized Send Time include an informational note in the campaign overview page indicating that Personalized send time was used and providing a link to an aggregate performance view.

![](https://klaviyo.zendesk.com/hc/article_attachments/45231714003995)

Personalized send time analytics are included in the performance view after a campaign has been finished for at least 24 hours. This buffer lets Klaviyo capture late opens, clicks and orders automatically, so you don’t need to take any extra steps before checking results.

### ****Account-level performance lift****

To help you understand long-term impact, Klaviyo surfaces an account-level Personalized Send Time performance view.

- For each campaign that uses Personalized Send Time, a randomly selected portion of eligible recipients is automatically held out in a control group. These recipients receive the same campaign on a non-personalized schedule that follows your recent send-time distribution within the window you chose (that is, how you typically send today for that channel).
- Everyone else in the campaign receives the Personalized Send Time treatment. When we report performance, we compare recipients who received Personalized Send Time against this control group.
- The control group size is automatically managed by Klaviyo and may change over time; you do not need to configure or maintain it.
- Metric-level lift is calculated as the relative difference between the Personalized Send Time group and the control group for a given metric. For example, if open rate is 20% with Personalized Send Time and 18% in control, lift in open rate is (20% − 18%) ÷ 18% ≈ 11%.

****Note on open and click rates:**** Open and click rates in Personalized Send Time reports exclude bot activity, including Apple Mail Privacy Protection (MPP) opens and automated bot clicks. Because of this, these metrics may differ from open and click rates shown in other areas of your account.

![](https://klaviyo.zendesk.com/hc/article_attachments/48072292200347)

### ****View send time distributions****

You can use send time distributions to understand when messages were delivered across your audience. Send time distributions show:

- The number of recipients who received a message at each hour
- Send times based on each recipient’s local time zone
- The time window (time restrictions) selected when scheduling the campaign

  This helps you visualize how messages were distributed within your selected send window.

  You can also filter the distribution to compare:
- Personalized recipients, who received messages at their individually optimized times
- Control recipients, who received messages based on the control group timing

This makes it easier to understand how send times differ between groups and how Personalized Send Time used your selected time restrictions.

Send time distributions are available on the Overview page, in the Engagement over time section.

![](https://klaviyo.zendesk.com/hc/article_attachments/48072292205339)

## ****Identify Personalized Send Time campaigns****

You can quickly identify and filter campaigns that used Personalized Send Time from the campaign list.

- Campaigns sent with Personalized Send Time are marked with a ✨ (sparkle) icon in the Campaign type column.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/48072292210587)
- You can also use the filters in the campaign list to view only campaigns that used Personalized Send Time.

![](https://klaviyo.zendesk.com/hc/article_attachments/48072321541659)

## ****Limitations and best practices****

Use these guidelines to get the most from Personalized Send Time:

- ****Campaign types and channels.**** Personalized send time works for email, SMS, push, and WhatsApp campaigns. It is not available for flows yet.
- ****Scheduling.**** You must schedule campaigns at least one day in advance. Same-day scheduling is not supported; choose a future date starting tomorrow.
- ****Smart Sending.**** Smart Sending is evaluated at the actual send time for each message, just like standard campaigns. If a recipient has already received another message within your Smart Sending window, they may be skipped from a Personalized Send Time campaign.
- ****SMS quiet hours.**** For SMS, Personalized Send Time follows a more restricted sending window to respect SMS quiet hours.

## ****Personalized send time FAQs****

### ****What does Personalized Send Time optimize for?****

Personalized send time optimizes for opens, clicks, and placed order rate, using these signals to determine the best time to send to each recipient.
****Note:**** Personalized Send Time uses standard placed order events for optimization and does not support custom or combined placed order metrics.

### ****Can I schedule a Personalized Send Time campaign for the same day?****

No. Currently, same-day scheduling is unavailable. You must schedule a future date starting tomorrow.

### ****What happens if a recipient’s best time has already passed on the scheduled date?****

If a recipient’s best time within your delivery window has already passed by the time the campaign is scheduled: Klaviyo will send at the next-best time remaining within your window that day.

### ****What if no valid time remains for a recipient on the scheduled date?****

If there are no valid times left for a recipient in their local time on the scheduled date (for example, the campaign is scheduled late in the day and the window has already passed), Klaviyo will deliver the campaign the next day during your configured window.

### ****Can I use Personalized Send Time with A/B testing?****

No. Personalized Send Time is not supported on campaigns that use any form of A/B test at the moment.

### ****How does Personalized Send Time work with Smart Sending?****

Smart Sending is evaluated at the moment each message is sent, just like standard campaigns. If a recipient has already received another message within your Smart Sending window, they may be skipped from that Personalized Send Time campaign.

### ****Does Personalized Send Time respect SMS quiet hours?****

Yes. For SMS, Personalized Send Time uses a more restricted sending window to respect SMS quiet hours.

### ****Can I use Personalized Send Time on multiple campaigns or channels in the same day?****

Yes. For overlapping audiences, keep in mind Personalized Send Time delivers recipients at different times of day, which can cause messages to land close together or be affected by Smart Sending. When possible, leave a modest gap between campaigns to reduce this risk. If Smart Sending is enabled, it may skip or delay messages that arrive too close together. These are recommendations, not hard requirements.

### ****Are Apple Privacy Opens / Bot Clicks used when determining the best send time?****

No - we remove bot events when training our models.