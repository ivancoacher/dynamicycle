---
id: 115005258268
title: "Troubleshooting skipped profiles in email campaigns"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005258268-Troubleshooting-skipped-profiles-in-email-campaigns"
section: "Email campaign troubleshooting"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:48:33Z"
language: en
---

## You will learn

Learn the possible reasons why a campaign wasn't sent to everyone in the list(s) or segment(s) you sent it to. When you review a campaign's analytics, you may notice that it did not send to your complete list or segment.

## Removal of globally suppressed contacts (email)

If you have the global unsubscribe feature enabled and someone becomes globally suppressed, this person is notautomatically removed from all the lists they have subscribed to. In order for someone to be globally suppressed, they must unsubscribe from a flow email or a campaign email sent to a segment.

This suppressed person's existing subscriptions will remain intact, but the suppressed tag will ensure that this person doesn't receive any emails moving forward. If someone reaches out asking to opt back in, you can remove the suppressed tag and this person will begin receiving the same emails as before — this person won't have to worry about re-subscribing.

For example, your email list may have 500 people on it, but it's possible that 5% of those people are actually globally suppressed. If you send a campaign to this email list, Klaviyo will automatically skip all suppressed users and you'll notice that only 475 emails were successfully sent.

To test this out, use the segment builder to view a cross-section of your list that is suppressed. This segment should include the following two conditions:

****If someone is in or not in a list > Person is in [Choose List]****

****AND****

****If someone is or is not suppressed > Person is suppressed****

![A segment of profiles that are in a list and not suppressed](https://klaviyo.zendesk.com/hc/article_attachments/28720892242203)

Find out how to [remove suppressed profiles from a list](https://help.klaviyo.com/hc/en-us/articles/115005077307-Clean-Global-Suppressions-from-a-List).

## Recipient activity: skipped recipients

As a starting point, navigate to the campaign's overview report. The left-hand area below the graph has summary information for the sent campaign.

![Sending_details.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720892245275)

For email campaigns, this gray box displays the subject, from email, list or segment the campaign was sent to, and the date/time the campaign was sent. This will be similar for SMS campaigns, but those will show the campaign cost and not the from email. There is also a section that groups people into key buckets based on why they were skipped.

If your campaign has Smart Sending enabled, this section will show you how many people were skipped because they received another email or SMS too recently. People also may be skipped if they have a missing or invalid email address.

Here are the key reasons why someone may not have received your campaign despite being on the send list:

- ****User Has Unsubscribed****
  When someone unsubscribes, they won't receive any more messages from you.
- ****User Has Marked an Email as Spam (email only)****
  If someone complains that an email from you is spam, they won't receive any more emails from you to keep your email deliverability strong.
- ****Emails to User Have Hard Bounced (email only)****
  If an email to someone hard bounces (this happens most often when the email address is invalid) they won't receive any more emails from you to keep your email deliverability strong.
- ****User Has an Invalid Email (email only)****
  If someone is on your send list, but his/her email address proves to be invalid, your email will not be successfully delivered. Certain [role-based email addresses](https://help.klaviyo.com/hc/en-us/articles/17976334449947) (shared email addresses, often used by groups within an organization rather than an individual) are automatically skipped in Klaviyo for this reason.
- ****User Was Manually Excluded****
  If you've manually excluded certain people from receiving your emails or SMS, we won't message them.
- ****Smart Sending****
  If certain people have already received another email SMS or email within your established **Smart Sending Period**, and **Smart Sending** is enabled for your campaign, they will be skipped.
- ****Lack of Funds (SMS only)****
  If your funds run out before a campaign finishes sending, anyone who hasn't yet received the campaign will be skipped.
- ****Suspicious Email****
  If the email address associated with this profile has historically led to bounces and is thus suspected as being fake or inactive.

If you navigate to the ****Recipient Activity**** tab and click on the ****Other****dropdown, you can also view activity around skipped recipients.

## Scheduled campaigns and target send lists

When you schedule an email campaign to send at a future date/time, you may see an option to determine recipients based on members of your list at send time instead of right now.

When you schedule a campaign, we take a snapshot of the list or segment you've selected. When scheduling a campaign that won't be sent for several days or weeks, it's likely that this target list may grow or shrink during the scheduled period.

If enabled, this option will prompt Klaviyo to take a newsnapshot of your target list or segment right before the scheduled campaign sends. This will ensure you're sending to an up-to-date list or segment. If this option is not enabled your campaign will send to the snapshot captured at the time you scheduled the email.