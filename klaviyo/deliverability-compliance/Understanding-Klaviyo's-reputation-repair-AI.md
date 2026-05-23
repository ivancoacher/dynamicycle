---
id: 28311927819163
title: "Understanding Klaviyo's reputation repair AI"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/28311927819163-Understanding-Klaviyo-s-reputation-repair-AI"
section: "Deliverability best practices and tools"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-11T12:54:54Z"
language: en
---

## You will learn

Learn about the reputation repair AI and how to qualify. The reputation repair AI helps improve your sender reputation and overall deliverability by automatically excluding unengaged profiles from your sends.

## Prerequisites for reputation repair AI

To qualify for the reputation repair AI, your account must meet the following prerequisites:

- [Mailchimp](https://help.klaviyo.com/hc/en-us/articles/115005254948)
- [Constant Contact](https://help.klaviyo.com/hc/en-us/articles/115005082727)
- [Campaign Monitor](https://help.klaviyo.com/hc/en-us/articles/115005254968)
- [ExactTarget](https://help.klaviyo.com/hc/en-us/articles/115005082767)

- A [deliverability score](https://help.klaviyo.com/hc/en-us/articles/18378819907995) below 50 (i.e., poor).
- Are not actively in [guided warming](https://help.klaviyo.com/hc/en-us/articles/4402636609691).
- Have at least 5,000 active profiles.
- Have engagement event data (i.e., at least 100 email clicks or opens within the last 30 days) in Klaviyo. For new accounts, this data can be synced from the following ESPs:
- Have sent at least 1 campaign with 1000 or more recipients in the last 30 days (including those sent on any of the 4 qualifying ESPs mentioned above).

## Reputation repair AI process

The reputation repair AI process revolves around sending campaigns only to specific engaged segments (i.e., profiles that have recently clicked or opened emails, or subscribed), with the criteria expanding over time as your deliverability score improves.

Throughout the process, Klaviyo automatically removes unengaged profiles from your sends. You’ll move to the next phase by sending a certain number of qualifying campaigns, or having a 30 day deliverability score above 75.

To be a qualifying campaign, a sent campaign must have at least 1000 recipients and a deliverability score of at least 75.

- ****Phase 1****
  Sends are limited to profiles that engaged in the last 30 days OR subscribed in the last 30 days
- ****Phase 2****
  Sends are limited to profiles that engaged in the last 60 days OR subscribed in the last 60 days
- ****Phase 3****
  Sends are limited to profiles that engaged in the last 90 days OR subscribed in the last 90 days
- ****Phase 4****
  Sends are limited to profiles that engaged in the last 120 days OR subscribed in the last 120 days

The number of qualifying campaigns you must send to advance to the next phase of the reputation process depends on how frequently you send. More frequent senders have to send a larger number of high-performing campaigns in order to reach the next phase and ultimately complete the reputation repair process.

****See the requirements to complete the repair process based on sending frequency****

- 5 qualifying campaigns in each phase (i.e., total of 20)
- OR current 30 day deliverability score is above 75.
- 3 qualifying campaigns in each phase (i.e., total of 12)
- OR current 30 day deliverability score is above 75.
- 2 qualifying campaigns in each phase (i.e., total of 8)
- OR current 30 day deliverability score is above 75.
- 1 qualifying campaigns in each phase (i.e., total of 4)
- OR current 30 day deliverability score is above 75.
- 1 qualifying campaigns in each phase (i.e., total of 4)
- OR current 30 day deliverability score is above 75

- Daily senders (20+ days/month):
- 3x week senders (12-19 days/month):
- 2x week senders (8-11 days/month):
- Weekly senders (4-7 days/month):
- Monthly senders (1-3 day/month):

## Start the reputation repair process

If your account qualifies for the reputation repair AI, you’ll see the following modal on the campaign wizard when you create a new campaign.

![Reputation repair AI modal](https://klaviyo.zendesk.com/hc/article_attachments/28312441722651)

When selecting the recipients for your campaign, you’ll see an additional section where you can view your reputation repair plan and automatically exclude unengaged profiles.

![Reputation repair option in campagin wizard](https://klaviyo.zendesk.com/hc/article_attachments/28969272299803)

The **Exclude unengaged profiles** box is checked by default so that unengaged profiles are automatically excluded from your campaign.

Klaviyo measures engagement based on profile opens (excluding Apple Mail Privacy Protection opens) and clicks within the engagement period.

### Reputation repair AI drawer

When you select **View repair plan,** the reputation repair drawer will open with the following information:

- ****Reputation repair progress****
  The phase of the reputation repair progress you are in.

  The timeline displayed (e.g., 30 day, 60 day, etc.) refers to the engagement period for the profiles included in your sends.
- ****Current deliverability score****
  Your current deliverability score based on the last 30 days of data and change over time.
- ****Unengaged profiles removed****
  The engagement period of profiles being excluded from your send and the breakdown of engaged vs. unengaged profiles.

![Reputation repair AI drawer](https://klaviyo.zendesk.com/hc/article_attachments/28969272301723)

## Outcome

After completing the reputation repair process, you’ll end with a deliverability score of 75 or above. This score is representative of strong deliverability performance and inbox providers will view sends from your brand more favorably, so emails are more likely to land in recipients’ main inbox.