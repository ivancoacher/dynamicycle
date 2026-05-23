---
id: 360037527052
title: "Creating a sending schedule based on email engagement reference"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360037527052-Creating-a-sending-schedule-based-on-email-engagement-reference"
section: "List and segments best practices"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: en
---

## You will learn

Learn how to create a sending schedule based on customer engagement. This is key to achieving strong open rates and maintaining a positive relationship with your subscribers. Sending too often to unengaged profiles will hurt your sender reputation, whereas sending too infrequently to engaged customers is leaving money on the table. It's best to achieve a happy medium through the use of segments and sending schedules. In this article, you'll learn how to segment subscribers into engagement tracks that will inform your sending habits.

If your campaign analytics show a large number of iOS openers, we suggest identifying these affected opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

For complete information on MPP opens, visit our [iOS 15: How to Prepare for Apple’s Changes](https://www.klaviyo.com/blog/apple-ios15-klaviyo) guide.

## Engagement tracks

Segmenting your subscribers into engagement tracks is a great way to avoid over-sending and prevent your emails from hitting the spam folder. We categorize these tracks based on how often you send to help you identify which course of action is best for your brand.

Once you establish your tracks, begin sending campaigns that are targeted and well suited for the segments' specific email habits. You can choose to send email campaigns at the same time to all of the segments with [smart sending](https://help.klaviyo.com/hc/en-us/articles/360029794371) toggled on, or you can send separate campaigns to each segment. If you choose to do the latter, this will enable you to visualize how much money you made from each campaign, and thus each engagement track.

If you have multiple main lists, make sure those details are included in your engagement track segments with OR in the first block of conditions. Use the name of your main list rather than the sample provided here (e.g., **Newsletter** vs. **Email List**).

### If you send daily

For customers who receive emails daily, make your messages concise and to the point. Include as much targeted information as possible, as you want to engage them, while also not inundating them with any unnecessary or irrelevant material. Be cognizant that they are consistent recipients, so don't overload them with unnecessary information.

#### Track A

This group of individuals is a part of your main email list, and have opened, clicked, or been added to the email list in the 30 days.

**Sending schedule**: maintain a daily sending cadence with this segment.

![Individuals that are a part of your main newsletter list, and have opened, clicked, or been added to the newsletter list in the 30 days](https://klaviyo.zendesk.com/hc/article_attachments/28720657394843)

#### Track B

This segment includes subscribers in your main email list that were added over 30 days ago. They have opened, clicked, or been added to your email list in the last 60 days, but haven't opened or clicked in the last 30 days.

**Sending schedule**: maintain a sending cadence of 3 times per week with this segment.

![Subscribers who joined more than 30 days ago, and have opened, clicked, or susbcribed between 30 and 60 days ago](https://klaviyo.zendesk.com/hc/article_attachments/28720657397403)

#### Track C

This segment includes individuals in your main email list that were added more than 60 days ago. They have opened, clicked, or been added to your email list in the last 90 days, but haven't opened or clicked in the last 60 days.

**Sending schedule**: maintain a sending cadence of 3 times per week with this segment.

![The track C segment definition for a daily sender](https://klaviyo.zendesk.com/hc/article_attachments/28720669142939)

#### Track D

This segment includes individuals in your main email list that were added more than 90 days ago. They have opened, clicked, or been added to your email list in the last 180 days, but haven't opened or clicked in the last 90 days.

**Sending schedule**: maintain a weekly sending cadence with this segment.

![The track D segment definition for a daily sender](https://klaviyo.zendesk.com/hc/article_attachments/28720669145627)

#### Track E

This group of individuals is a part of your main email list and was added more than 180 days ago, but have never opened and clicked an email.

You should create a [sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492) or [re-engagement campaign](https://help.klaviyo.com/hc/en-us/articles/115000931551) to give these profiles some final opportunities to engage. If they do not engage with your re-engagement efforts, you should [suppress](https://help.klaviyo.com/hc/en-us/articles/115005073867) the profiles in the segment.

If at any point a profile re-engages again, they will return to the 30 days engaged segment to begin the frequency stages over again.

![subscribers that are part of your main newsletter list and were added more than 180 days ago, but have never opened and clicked an email](https://klaviyo.zendesk.com/hc/article_attachments/28720669147803)

### If you send 3 times per week

This group of recipients will receive your emails 3 times per week, so messages to them can include more information than those to daily senders, but you should still consider that they are consistent recipients. They likely want similar content to those who receive daily correspondence, but they prefer more of it at once rather than spread through each day of the week. Include plenty of targeted information to maintain their brand loyalty and potentially move them into a daily senders' segment.

#### Track A

This group of individuals is a part of your main email list and have opened, clicked, or been added to the email list in the past 60 days.

**Sending schedule**: maintain a sending cadence of 3 times per week with this segment.

![subscribers that are part of your main newsletter list and have opened, clicked, or been added to the newsletter list in the past 60 days](https://klaviyo.zendesk.com/hc/article_attachments/28720669157147)

#### Track B

This segment includes individuals in your main email list that were added over 60 days ago. They have opened, clicked, or been added to your email list in the last 90 days, but haven't opened or clicked in the last 60 days.

**Sending schedule**: maintain a sending schedule of 2 times per week with this segment.

![The track B segment definition for a brand that sends 3 times a week](https://klaviyo.zendesk.com/hc/article_attachments/28720669161755)

#### Track C

This segment includes individuals in your main email list that were added more than 90 days ago. They have opened, clicked, or been added to your email list in the last 180 days, but haven't opened or clicked in the last 90 days.

**Sending schedule**: maintain a weekly sending schedule with this segment.

![The track C segment definition for a brand that sends 3 times a week](https://klaviyo.zendesk.com/hc/article_attachments/28720657401499)

#### Track D

This group of individuals is a part of your main email list and was added more than 180 days ago, but have never opened and clicked an email.

You should create a [sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492) or [re-engagement campaign](https://help.klaviyo.com/hc/en-us/articles/115000931551) to give these profiles some final opportunities to engage. If they do not engage with your re-engagement efforts, you should [suppress](https://help.klaviyo.com/hc/en-us/articles/115005073867) the profiles in the segment.

If at any point a profile re-engages again, they will return to the 60 days engaged segment to begin the frequency stages over again.

![subscribers that are a part of your main newsletter list and were added more than 180 days ago, but have never opened and clicked an email.](https://klaviyo.zendesk.com/hc/article_attachments/28720657414043)

### If you send 2 times per week

This group of recipients will receive two times per week, so messages to them can include slightly more information than groups that receive sends more frequently. They should still be considered consistent recipients. These profiles likely want similar content to those who receive daily correspondence, but they prefer more of it at once rather than spread throughout the week. Include plenty of targeted information to maintain their brand loyalty.

#### Track A

This group of individuals is a part of your main email list and have opened, clicked, or been added to the email list in the 90 days.

**Sending schedule**: maintain a sending cadence of 2 times per week with this segment.

![Subscribers that are a part of your main newsletter list and have opened, clicked, or been added to the newsletter list in the 90 days.](https://klaviyo.zendesk.com/hc/article_attachments/28720669164443)

#### Track B

This segment includes subscribers in your main email list that were added over 90 days ago. They have opened, clicked, or been added to your email list in the last 180 days, but haven't opened or clicked in the last 90 days.

**Sending** **schedule**: maintain a weekly sending cadence with this segment.

![The track B segment definition for brands that send twice a week](https://klaviyo.zendesk.com/hc/article_attachments/28720657406875)

#### Track C

This group of individuals is a part of your main email list and was added more than 180 days ago, but have never opened and clicked an email.

You should create a [sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492) or [re-engagement campaign](https://help.klaviyo.com/hc/en-us/articles/115000931551) to give these profiles some final opportunities to engage. If they do not engage with your re-engagement efforts, you should [suppress](https://help.klaviyo.com/hc/en-us/articles/115005073867) the profiles in the segment.

If at any point a profile re-engages again, they will return to the 90 days engaged segment to begin the frequency stages over again.

![Subscribers who were added more than 180 days ago, but have never opened and clicked an email.](https://klaviyo.zendesk.com/hc/article_attachments/28720669168155)

### If you send weekly

This group of recipients will receive your emails weekly, so messages to them can include more information than those that receive emails multiple times throughout the week. They likely want similar information, but they prefer more of it at once. Include plenty of targeted information to maintain their brand loyalty and potentially move them into more frequent senders' segments.

#### Track A

This segment includes individuals in your main email list and have opened, clicked, been added to your email list in the last 180 days.

**Sending schedule**: maintain a weekly sending cadence with this segment.

![Subscribers who have opened, clicked, been added to your newsletter list in the last 180 days](https://klaviyo.zendesk.com/hc/article_attachments/28720657417243)

#### Track B

This group of individuals is a part of your main email list and was added more than 180 days ago, but have never opened and clicked an email.

You should create a [sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492) or [re-engagement campaign](https://help.klaviyo.com/hc/en-us/articles/115000931551) to give these profiles some final opportunities to engage. If they do not engage with your re-engagement efforts, you should [suppress](https://help.klaviyo.com/hc/en-us/articles/115005073867) the profiles in the segment.

If at any point a profile re-engages again, they will return to the 180 days engaged segment to begin the frequency stages over again.

![Individuals that are a part of your main newsletter list and were added more than 180 days ago, but have never opened and clicked an email.](https://klaviyo.zendesk.com/hc/article_attachments/28720669178779)

### If you send monthly

Since monthly senders do not have the same close cadence that weekly and daily senders have with your brand, it is likely that you will need to include more information in emails sent to these segments. Consider sending out a longer monthly digest with new products, deals, and promotions. Make this information as relevant as possible and include information that will jump out to subscribers to engage them even more so that they can move into a segment you send more frequently to.

#### Track A

This segment includes individuals in your main email list and have opened, clicked, been added to your email list in the last 275 days.

**Sending schedule**: maintain a monthly sending cadence with this segment.

![Subscribers who have opened, clicked, been added to your newsletter list in the last 275 days.](https://klaviyo.zendesk.com/hc/article_attachments/28720669182107)

#### Track B

This group of individuals is a part of your main email list and was added more than 275 days ago, but have never opened and clicked an email.

You should create a [sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492) or [re-engagement campaign](https://help.klaviyo.com/hc/en-us/articles/115000931551) to give these profiles some final opportunities to engage. If they do not engage with your re-engagement efforts, you should [suppress](https://help.klaviyo.com/hc/en-us/articles/115005073867) the profiles in the segment.

If at any point a profile re-engages again, they will return to the 275 days engaged segment to begin the frequency stages over again.

![Subscribers who were added more than 275 days ago, but have never opened and clicked an email.](https://klaviyo.zendesk.com/hc/article_attachments/28720657428251)

## Visual example

The graphic below shows an example of how to vary your sending cadence and volume over the course of a year. Send to track A, which includes your most engaged segments, most often. When you do, aim for open rates that are consistently above 27%.

Around most holidays or company-wide sales, extend your messaging to include track B as well. For your biggest sales, such as spring, 4th of July, or [Black Friday/Cyber Monday](https://academy.klaviyo.com/en-us/courses/land-in-the-inbox-on-black-friday-cyber-monday), expand your sending cadence to include all tracks.

![Visual example of sending schedule based on engagament](https://klaviyo.zendesk.com/hc/article_attachments/28720669138459)

## Monitor your performance

Once you collect data from your engagement tracks, it's vital to analyze how your emails perform. With this information, you can adjust content accordingly and take note of what marketing techniques work with each segment of your customer base. If you don't keep track of your sending schedule outcomes, you risk upsetting customers and diminishing their levels of engagement, which is why it's important to continuously monitor how campaigns perform over time.

As a general rule of thumb, your daily open rates across all sends should not fall below 15%. If they do, tighten your engagement criteria or alter the content of your emails. You can find more information on performance thresholds in our documentation on [monitoring deliverability](https://help.klaviyo.com/hc/en-us/articles/115000201131). You can also monitor open rates over time by engagement track with our [campaign trends report](https://help.klaviyo.com/hc/en-us/articles/115005089467).

You can monitor your daily performance using the [overview dashboard](https://help.klaviyo.com/hc/en-us/articles/4708299478427). Here, you can create cards with information and metrics that directly pertain to your business and what metrics you're interested in tracking. Otherwise, use our [custom report builder](https://help.klaviyo.com/hc/en-us/articles/360047725651) to tailor a campaign performance report to your needs or view your [benchmark](https://help.klaviyo.com/hc/en-us/articles/360050110072) performance.

## Additional resources

- [Advanced segmentation reference](https://help.klaviyo.com/hc/en-us/articles/360035312491)
- [Developing a content calendar](https://academy.klaviyo.com/developing-a-content-calendar)
- [How to build a campaign performance report](https://help.klaviyo.com/hc/en-us/articles/360047022912)