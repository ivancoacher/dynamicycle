---
id: 115005250368
title: "How to strengthen your sender reputation for a specific inbox provider or email domain"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005250368-How-to-strengthen-your-sender-reputation-for-a-specific-inbox-provider-or-email-domain"
section: "Deliverability best practices and tools"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-11T10:53:55Z"
language: en
---

Learn best practices to strengthen your sender reputation if you are seeing deliverability issues with specific inbox providers or email domains. If your deliverability issues are not limited to specific inbox providers or domains, see our guide on [repairing your sender reputation.](https://help.klaviyo.com/hc/en-us/articles/8983758025883)

## Before you begin

If you're a brand new sender, it is important to [establish a good reputation upfront](https://help.klaviyo.com/hc/en-us/articles/360025945671) before diagnosing any issues related to sending to specific domains. This will allow you to gradually send to a broader audience while maintaining a good reputation and high open rates. However, if you've damaged your sender reputation, these best practices will help you get back on track and rebuild engagement.

Note that most mailbox providers use the same metrics to determine sending reputation, so if you are noticing a low reputation with one mailbox provider then it will inevitably be an issue for all of the other mailbox providers as well. Therefore, we advise you to perform list cleanup on all mailbox providers if you notice a sign that you have a low sending reputation. To do this please consult our guide, [How to create an unengaged segment](https://klaviyo.zendesk.com/hc/en-us/articles/360044054732), and suppress the members of that segment.

## Strengthening your sender reputation for an inbox provider or email domain

Most major email clients (e.g., Gmail and Yahoo) track how recipients interact with emails from your domain.

Specifically they look at positive and negative engagements including but not limited to:

- Open rates
- Click rates
- Bounce rates
- Spam complaint rates
- Unsubscribe rates

Inbox providers use this information to determine where your emails will be placed. This means that low performance in these areas increase the likelihood of your next campaign landing in the spam folder.

Creating [segments](https://help.klaviyo.com/hc/en-us/articles/115005237908) in Klaviyo makes it easy to isolate engaged and [unengaged profiles](https://help.klaviyo.com/hc/en-us/articles/360044054732#h_01HC35WR6A0ZKH4M7MNG9RN8T3) so that you know which audience to target with email content.

If you notice that your open rates only suffer for customers using a specific inbox provider or email domain, you can take steps to improve your sender reputation for this group.

Note that you can filter customers based on both inbox provider and email domain when segmenting and analyzing data in Klaviyo. The domain of an email address is what comes after the @ (i.e., "yourname@domain.com"). Klaviyo recommends using the inbox provider when troubleshooting deliverability issues, as multiple email domains can rely on the sorting performed by a single inbox provider.

To expedite the process of improving your sender reputation, you will need to do the following for your next 3-5 campaigns:

- Remove all email addresses with the low-performing inbox provider or domain from your regular sending lists.
- Create a segment of email addresses using the inbox provider or domain that have recently engaged with your campaigns, and separately send to this segment alongside your regular sending list.

### How to exclude low-performing email addresses from a sending list

If you have a main list that you are planning to email, create a segment based on the list that excludes subscribers using the inbox provider experiencing performance issues. By sending to this segment in place of the main list, you can contact all the list members that are not using the inbox provider facing deliverability issues, allowing you to protect your sender reputation.

To do this, create a segment with two conditions:

- **If someone is in or not in a list > Person is in [insert list name]**,
  AND
- **What someone has done > Received Email zero times over all time**,
  WHERE **Inbox Provider equals [inbox provider]**

![Segment of customers on list excluding those from low performing inbox](https://klaviyo.zendesk.com/hc/article_attachments/28716064420635)

If you are filtering based on the customer email domain, use the two conditions:

- **If someone is in or not in a list > Person is in [insert list name],**AND
- **Properties about someone > Email doesn’t contain [email domain]**

**![Segment of profiles in the main mailing list that are not using the low performing domain](https://klaviyo.zendesk.com/hc/article_attachments/28716064412827)**

If you have an existing segment that you plan to target with a campaign, add the following condition to exclude all subscribers from the low-performing inbox provider:

- AND
  **What someone has done > Received Email zero times over all time**,
  WHERE **Inbox Provider equals [inbox provider]**

For email domain, this would be:

- AND
  **Properties about someone > Email doesn’t contain [email domain]**

After creating your segment of customers using low-performing inbox providers or domains, it may be tempting to try to regain unengaged users with a winback campaign right away. However, we recommend waiting until you've sent to your engaged audiences for at least 3 weeks. If you try to send a campaign to these inactive profiles before attempting to improve your sender reputation, it's likely that this campaign will end up in spam for most recipients. Instead, consider [creating a winback flow](https://help.klaviyo.com/hc/en-us/articles/115002775192) to reach out to unengaged profiles.

### How to isolate engaged subscribers from a low-performing inbox provider or email domain

Now that you excluded all subscribers using the low-performing inbox provider or domain from your regular sends, you can isolate the domain’s engaged customers so you can send to them separately.

You’ll need to create segments with the profiles from the domain that have recently engaged with your campaign and include this segment in your next sends.

When repairing reputation, it is important that you contact the right engagement cohort based on how often you send. Use the segment structures below, paired with the values that match your sending frequency:

- **If someone is in or not in a list > Person is in [insert list name]**,
  AND
- **What someone has done > Received Email at least once over all time**,
  WHERE **Inbox Provider equals [inbox provider]**
  AND
- **What someone has done (or not done) > has Opened Email at least X times in the last X days**
  WHERE **Apple Privacy Open equals False**

![Segment of engaged profiles using low performing inbox provider](https://klaviyo.zendesk.com/hc/article_attachments/28716064417435)

For email domains, this segment would use the following conditions:

- ****If someone is in or not in a list > Person is in [insert list name],**AND**
- **Properties about someone > Email contains [email domain]**AND
- **What someone has done (or not done) > has Opened Email at least X times in the last X days**Where **Apple Privacy Open equals False**

**![Segment of engaged users using the low performing email domain](https://klaviyo.zendesk.com/hc/article_attachments/28716064415259)**

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

If you typically send to a segment, you can add two new conditions to only include engaged addresses from the inbox provider:

- **What someone has done > Received Email at least once over all time**,
  WHERE **Inbox Provider equals [inbox provider]**
  AND
- **What someone has done (or not done) > has Opened Email at least X times in the last X days**
  WHERE **Apple Privacy Open equals False**

For email domain, add the conditions:

- **Properties about someone > Email contains [email domain]**AND
- ****What someone has done (or not done) > has Opened Email at least X times in the last X days****WHERE **Apple Privacy Open equals False**

With the release of iOS15, macOS Monterey, iPadOS 15, and WatchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.

If your campaign analytics show a large number of iOS openers, we suggest identifying these affected opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

For complete information on MPP opens, visit our [iOS 15: How to Prepare for Apple’s Changes](https://www.klaviyo.com/blog/apple-ios15-klaviyo) guide.

If you attempt to re-engage unengaged subscribers and are unsuccessful, we recommend [suppressing them](https://help.klaviyo.com/hc/en-us/articles/115005078347) or otherwise ensuring they remain isolated from your main sending list moving forward.

## Additional resources

- [How to ramp and warm your sending infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671)
- [How to set up a dedicated sending domain](https://help.klaviyo.com/hc/en-us/articles/115000357752)
- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)