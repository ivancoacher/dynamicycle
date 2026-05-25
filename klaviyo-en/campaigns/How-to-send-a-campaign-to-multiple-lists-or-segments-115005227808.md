---
id: "115005227808"
title: "How to send a campaign to multiple lists or segments"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005227808-How-to-send-a-campaign-to-multiple-lists-or-segments"
section: "Getting started with campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:48:27Z"
language: "en"
---
## You will learn

See how to send to multiple lists or segments. This allows you to hone the sending pool of your campaign by including recipients from specific lists while excluding recipients from others. For instance, you could:

- Notify segments of your customer-base in advance for promotions like flash sales (e.g., rewarding VIP customers with special updates.
- Let certain segments of customers know about a new product or collection.
- Target customers who previously purchased during a holiday to tell them about this year's sales or products.
- Create a segment of [inactive subscribers](https://klaviyo.zendesk.com/hc/en-us/articles/360044054732) and launch a re-engagement effort, excluding this segment from your regular campaign sending.

## How to send to multiple lists

1. Select ****Campaigns > Create campaign****.
2. Name the campaign, select the channel, then click ****Continue****.
3. Under **Send to**, add all the lists or segments you want to include.

   Klaviyo automatically deduplicates any profiles that appear more than once so that none of your users receive the campaign more than once.

   - You can include a maximum of 15 groups (lists or segments).![adding a list or segment to a campaign](https://klaviyo.zendesk.com/hc/article_attachments/28716301554971)
4. Optional: select ****+ Don't send to**** to exclude a certain segment or list.

![Adding and excluding lists and segments for a campaign](https://klaviyo.zendesk.com/hc/article_attachments/28716301557659)

You can send a single campaign to a maximum of 15 lists or segments. If you'd like to send a campaign to more groups, [clone it](https://help.klaviyo.com/hc/en-us/articles/115006199048).

## Calculating expected recipients

On the right, you can see the **Estimated recipient count**. The number shown estimates the number of people who will receive your campaign. When calculating this number, Klaviyo:

- Adds together all profiles that exist in the lists and segments you've chosen to include.
- Subtracts duplicate profiles that may exist in multiple lists/segments you've chosen to include.
- Subtracts profiles within any included groups that also exist in lists and segments you've chosen to exclude.
- Subtracts unsubscribed contacts and global suppressions from all included lists and segments.

Klaviyo automatically skips [suppressed profiles](https://help.klaviyo.com/hc/en-us/articles/115005246108) at send time. By excluding these profiles from our expected recipient calculation, you can see an accurate count of who will receive your campaign.

If none of the lists you have chosen to exclude contain any recipients that are also on lists chosen to be included, you won't see the expected recipient count be dramatically different from the number of members in the included lists.

You may also see the expected recipient count be different from the actual number of recipients due to Klaviyo's [reputation repair AI](https://help.klaviyo.com/hc/en-us/articles/28311927819163). The reputation repair AI helps improve your sender reputation and overall deliverability by automatically excluding unengaged profiles from your sends, impacting the number of recipients a campaign is sent to.