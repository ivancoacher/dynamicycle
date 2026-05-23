---
id: 20413890435355
title: "How to warm your sending domain in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/20413890435355-How-to-warm-your-sending-domain-in-Klaviyo"
section: "Warm and ramp your domain"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-11T10:57:16Z"
language: en
---

## You will learn

Learn about how to warm your sending infrastructure in Klaviyo. Warming your sending infrastructure trains inbox providers to view you as a good sender, and is essential any time you move to a new email service provider.

## Before you begin

All Klaviyo customers sending from new dedicated infrastructure must complete the correlated domain warming. Before starting the warming process, confirm if your brand should use the [standard warming process or the alternative platform introduction process](https://help.klaviyo.com/hc/en-us/articles/360025945671). If your brand falls in the standard warming process category, follow the recommendations in this guide. Otherwise, follow the steps for the [platform introduction process](https://help.klaviyo.com/hc/en-us/articles/20414723525531).

## Guided warming

If you fall into the category of our standard warming process, you may see [guided warming](https://help.klaviyo.com/hc/en-us/articles/4402636609691) notifications appear in your account as you ramp up with Klaviyo or once you meet the requirements. During guided warming, Klaviyo will inform you of whether or not your campaign sending practices align with the stage of warming you are in. If you exceed the appropriate audience size, Klaviyo will alert you and automatically exclude unengaged audiences in an effort to adequately warm your account.

Note that if you have qualified for guided warming but did not send an email in 45 days, you will see the warming notifications dismissed. Once dismissed, guided warming cannot be re-enabled. However, you should still warm your account with the recommendations in this guide.

## Warm your infrastructure

## Migrate historic engagement data

If you are warming your infrastructure due to moving to Klaviyo from another email service provider (ESP), it's important to take historic engagement data into account so that you accurately build engaged segments.

This will allow you to introduce your new relationship with Klaviyo to the mailbox providers (MBPs) in a positive manner, as you will contact those that are already engaged with your brand, while limiting contact with those that may not want to hear from you.

Klaviyo has guides for migrating your data over from several different ESPs to facilitate the import of engagement criteria, including:

- [Mailchimp](https://help.klaviyo.com/hc/en-us/articles/115005254948)
- [Constant Contact](https://help.klaviyo.com/hc/en-us/articles/115005082727)
- [Campaign Monitor](https://help.klaviyo.com/hc/en-us/articles/115005254968)
- [Listrak](https://help.klaviyo.com/hc/en-us/articles/360034550591)
- [Sailthru](https://help.klaviyo.com/hc/en-us/articles/360036945872)
- [Salesforce Marketing Cloud](https://help.klaviyo.com/hc/en-us/articles/115000267471)

If you are using an ESP that is not listed above, use our [platform introduction](https://help.klaviyo.com/hc/en-us/articles/20414723525531) process to warm your infrastructure.

## Create engaged segments for sending campaigns

Sending to highly engaged segments over time helps to prevent any single low-performing message from damaging your overall deliverability. If you are using a brand new domain that has never been used in sending email, remember that these initial sends can greatly impact your reputation.

With the release of iOS15, macOS Monterey, iPadOS 15, and WatchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.

If your campaign analytics show a large number of iOS openers, we suggest identifying these affected opens in your individual subscriber segments.

For complete information on MPP opens, visit our [iOS 15: Everything you need to know about Apple’s changes.](https://www.klaviyo.com/blog/apple-ios15-klaviyo)

Create segments based on engagement over 30, 60, 90, 120, and 180 days. You will use these when sending over time, starting with your 30 day segment. If you send to inactive subscribers, you risk having your emails moved to spam by mailbox providers (e.g., Google, Hotmail, etc.).

If you're just starting out with Klaviyo or migrating from another platform, leverage historic engagement data from your previous platforms to create these segments.

However, if you attempt to send a campaign to more than the recommended amount of recipients during warming, Klaviyo will alert you with a warning, encouraging you to review this guide and lower the recipient count of your campaign. For your first campaign, we recommend that you send to fewer than 10,000 recipients. This recommended recipient count will then grow dynamically as you send to more people over time, so the warning will adjust accordingly, as shown below.

### Send campaigns to engaged segments

As you start to engage your 30, 60, 90, 120, and 180 day segments, you will want to aim for the open rates listed in each section below. However, it’s important to note that open rates may vary per sender and industry, so your focus should follow the guidance below along with attaining as high as possible engagement for your specific business. Learn more in our resource on [monitoring deliverability performance](https://help.klaviyo.com/hc/en-us/articles/115000201131).

### 30 day segment (initial warming and daily sending)

For your first send, aim for open rates of above 30% if possible. Getting an open rate this high will require sending to a segment of anyone who has clicked in the last 30 days, or those who subscribed within the last 15 days.

![30 day engaged segment](https://klaviyo.zendesk.com/hc/article_attachments/28718022658075)

If your 30 day engagement segment results in a very large group of profiles, consider the following:

- ****Use**** [****smart send time****](https://help.klaviyo.com/hc/en-us/articles/360029794371) ****to divide up sends****By using Smart Send Time, your email sends will be automatically divided up and sent over the course of 24 hours. This will help you send to smaller groupings of subscribers and continue to warm your domain. Additionally, you will learn the best time of day to send to these subscribers in the future. (Note that smart send time requires at least 12,000 subscribers in Klaviyo).
- ****Use batch sending to divide up sends****Use batch sending to break up your email sends into smaller groupings of users.
- ****Take random samples of the engaged segment****
  Taking a random sample of your segment will allow you to break larger sends into smaller groups.

Be conservative in your sending during this time and strive for as high of engagement as possible. For the first two weeks, focus on sending to the 30 day engaged segment. As long as your open rates remain above 20% you can relax the engagement criteria to 60 during weeks 3 and 4. After four weeks of sending with at least 20% open rates, you can relax the engagement criteria to 90 days. Continue with this strategy for two weeks at a time, and then further relax your engagement criteria. Your optimal engagement timeframe will vary depending on your individual business needs.

If your email open rates dip below 20%, continue sending to the current engagement segment, but pause ramp up to the next engagement segment. This may be a sign that your reputation is being negatively affected and you may need to [strengthen your sender reputation](https://help.klaviyo.com/hc/en-us/articles/115005250368).

### 60 day segment (for sending up to 3 times a week)

After two weeks of sending to a 30 day engaged segment and consistently seeing high engagement, you can broaden your audience to a 60 day engaged segment as long as this doesn’t substantially increase the size of your sending list. Remember to stay conservative with the number of email sends during this time. Make sure your open rates stay above 20%. If they fall below, return to your 30 day segment.

![60 day engaged segment](https://klaviyo.zendesk.com/hc/article_attachments/28718022661403)

### 90 day segment (for sending up to 2 times a week)

If you are seeing good results with your segment using a 60 day engagement window, you can move to a 90 day engaged segment instead. Again, make sure open rates are 20% or higher, and if not, then tighten your timeline.

![90 day engaged segment](https://klaviyo.zendesk.com/hc/article_attachments/28718022664859)

### 120 day segment (for sending weekly)

After sending to your 30-90 day engaged audiences for a few weeks, relax your engagement criteria to 120 or 180 days. Again, strive for high open rates above 20%.

![120 day engaged segment](https://klaviyo.zendesk.com/hc/article_attachments/28717994885531)

### 180 day segment (for sending monthly)

If you are seeing good results with sending to your more recently engaged segments, you can expand the segment to 180 days. Tighten to 120 days or lower if engagement falls below 20%.

![180 day engaged segment](https://klaviyo.zendesk.com/hc/article_attachments/28717994897819)

## Turn on high engagement flow emails

Once you have created and sent to all your engaged segments, it’s now time to turn on your automations or flows. It’s critical that you only turn on flows that have historically performed well.

There are three types of flows that you should review for high engagement:

- [Welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172)
- [Abandoned cart](https://help.klaviyo.com/hc/en-us/articles/115002779411)
- [Browse abandonment](https://help.klaviyo.com/hc/en-us/articles/115002775252)

### Determining your high engagement flows

We recommend reviewing your previous performance on these particular flows, and only turning them on if they have performed well. Below are the numbers you should look for in terms of high engagement and well-performing flows:

- Open rates above 40%
- Click rates above 1%
- Unsubscribe rates below 0.1%
- Complaint rates below 0.1%

### What to do if you do not have high performing flows

If your flows have not historically performed well, follow the below guidelines on when to turn them on:

- [Welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172): after 2 weeks of sending campaigns from Klaviyo
- [Abandoned cart](https://help.klaviyo.com/hc/en-us/articles/115002779411): after 30 days of sending campaigns from Klaviyo
- [Browse abandonment](https://help.klaviyo.com/hc/en-us/articles/115002775252): after 30-60 days of sending campaigns from Klaviyo

### High risk flows to send later

Winback, re-engagement, and sunset flows may be high risk flows to turn on, as they typically see low engagement anyhow. It is recommended not to begin with these flows below until ramping and warming are both fully complete.

For more details on deploying these flows, see the below resources:

- [Creating a winback flow](https://help.klaviyo.com/hc/en-us/articles/115002775192)
- [Creating a sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492)
- [Creating a re-engagement flow](https://help.klaviyo.com/hc/en-us/articles/115002775192)

## Monitor your performance

These tools will help you monitor your performance as you warm your sending domain:

- [Review flow analytics](https://help.klaviyo.com/hc/en-us/articles/115002779351)Check back periodically on your flows’ open, unsubscribe, and spam complaint rates to gauge the engagement with these emails.

- [Monitor campaigns using the trends report](https://help.klaviyo.com/hc/en-us/articles/115005089467)This report will show you changes over time in all the important email engagement metrics. In particular, monitor the graph showing **Marked as spam** and hard bounce rates, and look into campaigns that are responsible for any spikes in behavior. Learn more in our guide to [monitoring your deliverability and email performance.](https://help.klaviyo.com/hc/en-us/articles/115000201131)

## Additional resources

[Understanding dedicated vs. shared sending domains](https://help.klaviyo.com/hc/en-us/articles/7674941873947)

[Understanding which warming process to use in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360025945671)

[Understanding the platform introduction process in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/20414723525531)