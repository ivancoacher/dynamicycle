---
id: 12995016978075
title: "How to strengthen your sender reputation for a specific country"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/12995016978075-How-to-strengthen-your-sender-reputation-for-a-specific-country"
section: "Deliverability best practices and tools"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-11T10:53:58Z"
language: en
---

## You will learn

Learn best practices to strengthen your sender reputation if you are seeing deliverability issues limited to specific countries. With the [campaign deliverability tab](https://help.klaviyo.com/hc/en-us/articles/12695416712219), you can can see campaign specific performance by country.

If your deliverability issues are not limited to specific countries, see our guide on [repairing your sender reputation.](https://help.klaviyo.com/hc/en-us/articles/8983758025883)

## Before you begin

If you're a brand new sender, it is important to [establish a good reputation upfront](https://help.klaviyo.com/hc/en-us/articles/360025945671) before diagnosing any issues related to sending to specific countries. This will allow you to gradually send to a broader audience while maintaining a good reputation and high open rates. However, if you've damaged your sending reputation, these best practices will help you get back on track and rebuild engagement.

## Strengthening your sender reputation for a specific country

As a multinational brand, you may observe different engagement patterns across your customers in different regions. Including recipients from low-performing countries in your usual sends can negatively impact your deliverability.

The key engagement rates to keep track of are:

- Open rates
- Click rates
- Bounce rates
- Spam complaint rates
- Unsubscribe rates

If you are seeing issues with these key deliverability performance metrics in specific countries, you can isolate these subscribers so you can target them with different content than your usual sends.

To improve your sender reputation in a country that is not performing well, you’ll need to do the following for your next 3-5 marketing campaigns:

- Remove all subscribers in the low-performing country from your regular sending lists.
- Create segments of subscribers in the country that have recently engaged with your campaigns and send separately to this segment.

### How to exclude all subscribers in a specific country from a sending list

If you have a main list that you are planning to email, create a segment based on this list that excludes subscribers from the country experiencing performance issues:

- **If someone is in or not in a list > Person is in [insert list name],**AND
- **Properties about someone > Country doesn’t equal [insert country]**

![Segment of profiles in main list tht are not in the low performing country](https://klaviyo.zendesk.com/hc/article_attachments/28716332801947)

If you have an existing segment that you plan to target with a campaign, add the following condition to exclude all subscribers from the country:

- AND**Properties about someone > Country doesn’t equal [insert country]**

After creating your segment of users in low-performing countries, it may be tempting to try to regain unengaged users with a winback campaign right away. However, we recommend waiting until you've sent to your engaged audiences for at least 3 weeks. If you try to send a campaign to these inactive profiles before attempting to improve your sender reputation, it's likely that this campaign will end up in spam for most recipients. Instead, consider [creating a winback flow](https://help.klaviyo.com/hc/en-us/articles/115002775192) to reach out to unengaged profiles.

### How to build an engaged segment of subscribers from a specific country

Now that you excluded all subscribers in a country from your regular sends, you can isolate the engaged customers located there and send to them separately.

You’ll need to create segments with the profiles from the low-performing countries that have recently engaged with your campaign and include this segment in your next sends.

When repairing reputation, it is important that you contact the right engagement cohort based on how often you send. Use the segment structure below, paired with the values that match your sending practices:

- ****If someone is in or not in a list > Person is in [insert list name],**AND**
- **Properties about someone > Country equals [insert country]**AND
- **What someone has done (or not done) > has Opened Email at least X times in the last X days**Where **Apple Privacy Open equals False**

![Segment of engaged users in the low performing country](https://klaviyo.zendesk.com/hc/article_attachments/28716332808091)

****If you send daily****

- Week 1: Send to **Very Highly Engaged** audience with 5 or more opens in the last 30 days
- Week 2: Send to **Highly Engaged** audience with 3 or more opens in the last 30 days
- Week 3+: Send to **Engaged** audience with 1 or more opens in the last 30 days

If you see a drop in performance, you can go back to **Highly** or **Very Highly** to repair your reputation again.

****If you send 3 times per week****

- Week 1: Send to **Very Highly Engaged** audience with 5 or more opens in the last 60 days
- Week 2: Send to **Highly Engaged** audience with 3 or more opens in the last 60 days
- Week 3+: Send to **Engaged** audience with 1 or more opens in the last 60 days

If you see a drop in performance, you can go back to **Highly** or **Very Highly** to repair your reputation again.

****If you send 2 times per week****

- Week 1: Send to **Very Highly Engaged** audience with 5 or more opens in the last 90 days
- Week 2: Send to **Highly Engaged** audience with 3 or more opens in the last 90 days
- Week 3+: Send to **Engaged** audience with 1 or more opens in the last 90 days

If you see a drop in performance, you can go back to **Highly** or **Very Highly** to repair your reputation again.

****If you send weekly****

- Week 1: Send to **Very Highly Engaged** audience with 5 or more opens in the last 180 days
- Week 2: Send to **Highly Engaged** audience with 3 or more opens in the last 180 days
- Week 3+: Send to **Engaged** audience with 1 or more opens in the last 180 days

If you see a drop in performance, you can go back to **Highly** or **Very Highly** to repair your reputation again.

****If you send monthly****

- Week 1: Send to **Very Highly Engaged** audience with 5 or more opens in the last 275 days
- Week 2: Send to **Highly Engaged** audience with 3 or more opens in the last 275 days
- Week 3+: Send to **Engaged** audience with 1 or more opens in the last 275 days

If you see a drop in performance, you can go back to **Highly** or **Very Highly** to repair your reputation again.

If you typically send to a segment, you can add two new conditions to only include engaged addresses from the country:

- ****Properties about someone > Country equals [insert country]
  AND****
- ****What someone has done (or not done) > has Opened Email at least X times in the last X days****

With the release of iOS15, macOS Monterey, iPadOS 15, and WatchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.

If your campaign analytics show a large number of iOS openers, we suggest identifying these affected opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

For complete information on MPP opens, visit our [iOS 15: How to Prepare for Apple’s Changes](https://www.klaviyo.com/blog/apple-ios15-klaviyo) guide.

If you attempt to re-engage unengaged subscribers and are unsuccessful, we recommend [suppressing them](https://help.klaviyo.com/hc/en-us/articles/115005078347-A-Guide-to-List-Cleaning) or otherwise ensuring they remain isolated from your main sending list moving forward.

## Additional resources

- [How to ramp and warm your sending infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671)
- [How to set up a dedicated sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752)
- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/360021849952)