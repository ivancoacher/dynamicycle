---
id: 360044054732
title: "How to clean your email list to maintain good deliverability"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360044054732-How-to-clean-your-email-list-to-maintain-good-deliverability"
section: "Getting started with lists and segments"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: en
---

## You will learn

You will learn
Learn how to clean your email lists to avoid sending to contacts who aren’t interested in your content. This process allows you to keep in touch with the subscribers who are most engaged with your messages, so you are seen as a trusted sender with a good reputation.

The process of list cleaning for deliverability involves 3 steps:

1. Create a segment of unengaged contacts.
2. Exclude that segment from sends.
3. Suppress the **Never engaged** segment.

## Why list cleaning is important

List cleaning is key to maintaining good deliverability and making sure your emails land in recipients' inboxes. List cleaning allows you to accomplish the following:

- ****Increase open and click rates****By pre-emptively excluding unengaged contacts, you are prioritizing sends to those who do open and click. This brings up your overall open and click rates. In turn, anti-spam reporting agencies recalculate your sending reputation (much like a credit score), and more of your emails are put into inboxes as a result. Just as your credit score increases your chances of getting a loan, so too does your probability of being placed in the inbox increase with a better open and click rate.
- ****Reduce unsubscribe rates and spam complaint rates****By pre-emptively excluding unengaged contacts from your sends, you also reduce the need for contacts to unsubscribe from unwanted emails, or worse, mark them as spam. By removing unengaged contacts ahead of time, you prevent unsubscribes and spam reports that would hurt your sending reputation in the future.
- ****Improve your sender reputation with inbox providers****Most major email service providers (like Google and Yahoo) track how recipients interact with emails from your domain (e.g., how many emails are marked as spam, how many are opened, etc.) ESPs use this information to determine whether to classify your messages as spam. Having a lot of unengaged profiles on your list hurts your efforts to reach those that actually do want to receive your emails.
- ****Retain and engage customers****By learning when people start to disengage with your brand, you can know when to send targeted campaigns to re-engage them.
- ****Personalize content based on your best customers****By knowing that your list is full of real, active, and interested potential customers, you can start to personalize content and analyze data based on those most likely to encourage and promote your brand.

## Identify unengaged profiles

Identify your unengaged customers by creating a segment that captures profiles who are receiving your emails, but not opening or clicking them. This segment is a general recommendation. Depending on your audience and sending frequency, you can increase or decrease the time frames and message thresholds. For example, if you send emails daily or several times a week, consider using a 30-day range rather than 90-day in your unengaged email segment.

To create a segment:

1. Navigate to ****Audience**** > ****Lists & segments****.
2. Click ****Create New**** > ****Create segment.****
3. Build a segment using the definitions outlined below:

- Person can receive email marketing
  AND
- What someone has done > Received Email is at least 5 over all time
  AND
- What someone has done > Opened Email 0 times in the last 90 days
  AND
- What someone has done > Clicked Email 0 times in the last 90 days

In this example segment, we only include Klaviyo event data. If you integrated your prior ESP (e.g., Mailchimp) or manually imported historical open and click data during the time frame used in the segment, you should add conditions to your segment to filter on this data as well. For example, if you migrated from Mailchimp 1 month ago, make sure to use Mailchimp open and click data in a 90-day unengaged segment.

## Exclude unengaged contacts from sends

Klaviyo recommends excluding unengaged contacts from the majority of your campaigns. Since these contacts aren’t opening or clicking your messages, continuing to send to them can damage your deliverability.

In addition to excluding these contacts from campaigns, consider excluding them from your most high-volume flows as well, like browse abandonment. It’s fine to allow these contacts to enter flows for certain key touchpoints, like a re-engagement or abandoned cart flow.

You may choose to include unengaged contacts in certain high-priority campaigns, like new product announcements or Black Friday/Cyber Monday.

### Exclude unengaged contacts from campaigns

1. Navigate to the ****Campaigns**** tab in Klaviyo.
2. Select ****Create campaign****.
3. In the modal that appears, set the campaign’s name and choose a channel (i.e., email, SMS, or push).
4. Click ****Save and continue****.
5. In the Recipients section, choose the list(s) or segment(s) you’d like to send to in the **Send to** section.
6. In the **Don’t send to (optional)** section, select the unengaged segment for the channel you’re sending to.
7. Click **Continue** to content to create and send the campaign.

![](https://klaviyo.zendesk.com/hc/article_attachments/34714297502747)

### Exclude unengaged contacts from a flow

Flows are triggered by customer actions like subscribing to a list or abandoning a cart. These are key lifecycle touchpoints, and a great opportunity to re-engage a contact who has lapsed.

In general, you should continue to send these flows to customers, even if they become unengaged.

However, if you have certain high-volume flows (e.g., flows that an unengaged contact might reasonably trigger multiple times in a month), you may consider excluding unengaged contacts from it to avoid damaging your sender reputation.

To exclude contacts from high-volume flows:

1. Navigate to the ****Flows**** tab in Klaviyo.
2. Choose an existing flow or create a new one.
3. If the flow sends via a single channel:
   1. Click the flow’s trigger to open the trigger menu.
   2. Next to Flow filters, click ****Add****.
   3. Select ****Add flow filter****.
   4. Add a flow filter that matches your unengaged segment.
   5. Click ****Save****.

## Never engaged segment

The **Never engaged** segment contains your least engaged email subscribers. You should avoid contacting them to improve and maintain your deliverability. Once you’ve identified them, you can send them one final re-engagement attempt through a [sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492), and then suppress them if they don't engage.

You can either manually create a segment of profiles that never engaged, or automatically create a **Never Engaged** segment from the deliverability hub in Klaviyo.

To access the page:

1. Navigate to ****Analytics**** > ****Deliverability****.
2. In the Action Center, locate the **Create a Never engaged segment** recommendation.
3. Select ****Create segment****.

![](https://klaviyo.zendesk.com/hc/article_attachments/34714305950107)

A segment will be automatically created with all of the following criteria (including any email integrations associated with your account).

- If someone can or cannot receive marketing > can receive email marketing
  AND
- What someone has done or not done > Received email is at 5 in the last 180 days
  AND
- What someone has done or not done > Opened email 0 times over all time
  AND
- What someone has done or not done > Clicked email 0 times over all time
  AND
- What someone has done or not done > Viewed Product 0 times over all time
  AND
- What someone has done or not done > Placed Order 0 times over all time

After creating the segment on the deliverability hub, you'll see it on the **Lists & segments** page in Klaviyo. The segment will be called **Never Engaged (Email)**.

### Suppress profiles

Once you have created your segment, you can suppress those that did not engage with your sunset flow.

To suppress the segment:

1. Go to the **Lists & segments** tab.
2. Click the **Never engaged** segment and click the 3 dots to the far right.
3. Click ****Suppress current members**** to suppress all of the unengaged profiles in bulk.
4. On the confirmation modal, confirm the number of profiles you’d like to suppress.

Learn more about [how to suppress emails in bulk](https://help.klaviyo.com/hc/en-us/articles/24312135764251).

## Outcome

After completing these steps, contacts who are not engaging with your emails will receive significantly fewer sends, which can improve your deliverability over time.

You must continue excluding your unengaged segments from your campaigns on an ongoing basis.

These contacts may still receive occasional high-priority messages, like abandoned cart flows, re-engagement messages, or occasional important campaigns (like new product releases) if you choose not to exclude unengaged contacts from those sends.

## Additional resources

- [How to create a sunset flow](https://help.klaviyo.com/hc/en-us/articles/360017518492)
- [Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)
- [How to create an engaged segment](https://help.klaviyo.com/hc/en-us/articles/115000200072)