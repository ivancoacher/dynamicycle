---
id: "360007016571"
title: "How to exclude lists or segments from a campaign send"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360007016571-How-to-exclude-lists-or-segments-from-a-campaign-send"
section: "Getting started with campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:50:06Z"
language: "en"
---
## You will learn

Learn how to exclude certain groups (i.e., lists or segments) when sending campaigns.

If you would like to exclude specific individuals from a campaign, you will first need to add them to a dedicated list or group them in a segment.

## Use cases

In addition to selecting who you want to **send to**, there's also **don't send to**, which you can use to exclude any number of lists or segments from your send, for example:

- Don't send an evergreen newsletter to your unengaged subscribers segment in-between [regular list cleaning](https://help.klaviyo.com/hc/en-us/articles/115005078347).
  - This avoids having unengaged recipients damage your sender reputation.
- Don't send to subgroups of people that may not be interested in a specific campaign's content, or may engage better with a personalized message through a separate campaign.
  - For example, when launching a new collection, you may want to send your VIP Customers an advance sneak peak. When the time comes for your general announcement, you may want to exclude those VIPs you've already notified.
- Add groups to not send to when your audience for similar campaigns may overlap.
  - This makes sure recipients don't receive multiple or duplicative messages.

## How to exclude lists and segments from a campaign

1. Navigate to the ****Campaigns**** tab in Klaviyo.
2. Select ****Create campaign****.
3. In the sidebar that appears, set the campaign’s name and choose a channel (i.e., email, SMS, or push).
4. Click ****C********ontinue****.
5. In the **Audience** section, choose the list(s) or segment(s) you’d like to send to in the **Send to** section.
6. Select the ****+ Don't send to**** button.
   ![Audience step of the campaign wizard, showing the don't send to button](https://klaviyo.zendesk.com/hc/article_attachments/34696440424731)
7. Select the segment you want to exclude from this campaign.
   ![Excluding a list or segment from a campaign](https://klaviyo.zendesk.com/hc/article_attachments/34696440425371)
8. Click ****Next**** to create and [send the campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847).

## How to calculate expected recipients

Next to the lists and segments you've chosen, you can your **Expected recipient count**. The number shown estimates how many people will receive your campaign. When calculating this number, Klaviyo:

- Adds together all profiles that exist in the lists/segments you've chosen to include
- Subtracts duplicate profiles that may exist in multiple lists/segments you've chosen to include
- Subtracts profiles within any included groups that also exist in lists/segments you've chosen to exclude
- Subtracts unsubscribed contacts and global suppressions from all included lists and segments

Klaviyo automatically skips [suppressed profiles](https://help.klaviyo.com/hc/en-us/articles/115005246108-Suppressed-Profiles-in-Klaviyo) at send time. By excluding these profiles from the expected recipient count, you can see an accurate count of who will receive your campaign.

If none of the lists you have chosen to exclude contain any recipients that are also on lists chosen to be included, you won't see the expected recipient count be dramatically different from the number of members in the included lists.