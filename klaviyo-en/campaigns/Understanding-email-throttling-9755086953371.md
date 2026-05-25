---
id: "9755086953371"
title: "Understanding email throttling"
source_url: "https://help.klaviyo.com/hc/en-us/articles/9755086953371-Understanding-email-throttling"
section: "Email campaign troubleshooting"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:51:18Z"
language: "en"
---
## You will learn

Learn how and when Klaviyo throttles email campaigns, best practices to avoid throttling, and what to do if your campaign is throttled.

## About email throttling

**Email throttling** refers to when some emails cannot be sent in a given time period due to volume restrictions. Klaviyo may occasionally throttle emails for one of the following reasons:

- [Auto-upgrade and flexible sending](https://help.klaviyo.com/hc/en-us/articles/4405883690651) are disabled and a campaign exceeds your plans limits.
- There are an unexpectedly high number of recipients and not enough time to send your email to all of them. This can happen when:
  - The final recipient count is not known until after a campaign is scheduled. This can happen in rare cases for campaigns with a high volume (e.g., more than a million) of recipients and many included and excluded lists/segments.
  - More recipients were calculated at send time than at scheduling time.

If Klaviyo can tell at the time of scheduling that your campaign might be throttled (e.g., if it exceeds your plan limits), you receive an in-app warning and can't schedule the campaign.

However, the warning might not appear if, for example, many profiles were added between when the campaign was scheduled and the actual send time.

## Best practices to avoid throttling

To avoid throttling, we recommend these best practices:

- [Enable flexing sending or auto-upgrade](https://help.klaviyo.com/hc/en-us/articles/4405883690651) for your email plan, so your billing plan can automatically upgrade if needed.
- For every 1 million email recipients in a given campaign, add an hour between when you schedule the campaign and when it should send (e.g., if you are sending to 3 million recipients and want your message to send at 4 p.m., go through the scheduling steps at or before 1 p.m.).
- For particularly large sends, consider breaking the send up (e.g., [send by recipient time zone](https://help.klaviyo.com/hc/en-us/articles/360050216012) or [split your list in two](https://help.klaviyo.com/hc/en-us/articles/115001145931)).
- Avoid using the “send now” functionality for time-sensitive sends with a million or more recipients.
  - The process of preparing a message to send to a list of this size may take multiple hours.

Email content does not impact whether or not your message will be throttled.

## What to do if your campaign is throttled

If your campaign is throttled, you can manually resend the email to skipped recipients. If your campaign was throttled due to your email plan size, [upgrade your plan](https://help.klaviyo.com/hc/en-us/articles/8356575957275) before taking these steps.

1. Click ****Audience > Lists & segments**** in the Klaviyo navigation sidebar.
2. Click ****Create New****.
3. Select ****Create s********egment****.
4. Create a segment with the following definition:

   - **What someone has done (or not done) > Received Email > At least once over all time > where Campaign Name = [your campaign’s name]**![A segment of everyone who received the throttled campaign](https://klaviyo.zendesk.com/hc/article_attachments/34710144754331)
5. Click ****Create segment****.
6. Click ****Campaigns**** in the Klaviyo navigation sidebar.
7. Click the 3 dots icon next to your throttled campaign.
8. Click ****Clone****.
9. In the **Send to** field of the new campaign, add the same list(s) and segment(s) used for the original campaign.
10. In the **Don’t send to** field, add the segment of message recipients you just created.
11. Proceed through the steps to schedule and send your campaign.

## Outcome

When you resend a campaign but skip a segment of profiles who have already received it, you can be certain that your subscribers will not receive the same message twice. By following the steps outlined above, you can send your message to those who were skipped when it was throttled.