---
id: "20776984621083"
title: "How to create espresso shot segments"
source_url: "https://help.klaviyo.com/hc/en-us/articles/20776984621083-How-to-create-espresso-shot-segments"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:33Z"
language: "en"
---
## You will learn

Learn how to create espresso shot segments for email, SMS, and mobile push.

Espresso shot campaigns are a great way to re-engage those who recently expressed interest in your brand but haven’t purchased. Using these segments, you can resend a campaign to capture excess revenue, boost click rate, and improve deliverability.

## Before you begin

Here, we discuss 3 segments you can create:

- Email
- SMS
- Push notifications

We also include some strategies for when and how to use these segments.

****Can I use flows to send to those in my espresso shot segment?****

Technically yes, but we don’t recommend it for a few reasons:

- Contacts can only receive a [segment-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003040052) once.
- Re-targeting via espresso shot segments works best when the content is similar to that of the original message.
  For instance, if you sent a campaign about a new product, the espresso shot campaign should also be about that new product. While it’s possible to do this with flows, it would be difficult and time consuming to set up.

## Email espresso shot segment

Include the following conditions:

- ****If someone can or cannot receive marketing > Can receive email marketing** > **Because person subscribed****AND
- **What someone has done (or not done) > Opened email is at least once in the last 72 hours**
  OR
- **What someone has done (or not done) > Clicked email is at least once in the last 72 hours**AND
- **What someone has done (or not done) > Placed order > zero times in the last 72 hours**
  ![Email espresso shot segment](https://klaviyo.zendesk.com/hc/article_attachments/34258517000219)

****Use cases****

After creating this segment, we recommend doing one of the following:

- Re-send your most recent email campaign after making a few tweaks (e.g., changing the subject line).
- Create a similar campaign and offer an incentive (e.g., free shipping).
- Target this segment via SMS or push.
  - Note: for this, add a condition such as **If someone can or cannot receive marketing > can receive** and then choose either SMS or push marketing.

## SMS espresso shot segment

For the SMS segment, add the following conditions:

- ****If someone can or cannot receive marketing > Can receive SMS marketing****AND
- **What someone has done (or not done) > Clicked SMS is at least once in the last 72 hours**AND
- **What someone has done (or not done) > Placed order > zero times in the last 72 hours
  ![SMS espresso shot segment](https://klaviyo.zendesk.com/hc/article_attachments/34258501993243)**

****Use cases****

You can use this segment to:

- Target this segment via an ad.
- Text an offer (such as free shipping) to incentivize them to purchase.
- Send them a similar email or push notification to follow up.
  - Note: add a condition, such as **If someone can or cannot receive marketing > can receive** and then choose either email or push marketing.

Unlike email and mobile push, we don’t recommend resending an SMS. As a channel, SMS is considered more intrusive, so texting the exact same message may be seen as too much.

## Push espresso shot segment

As for push, add these conditions:

- ****If someone can or cannot receive marketing > Can receive mobile push marketing****AND
- **What someone has done (or not done) > Opened push is at least once in the last 72 hours**AND
- **What someone has done (or not done) > Placed order > zero times in the last 72 hours
  ![Mobile push notificaiton espresso shot segment](https://klaviyo.zendesk.com/hc/article_attachments/34258501995163)**

If available, we also recommend including an app-related condition (e.g., **AND** **What someone has done (or not done) > Opened app at least once in the last 72 hours**).

****Use cases****

- Resend the push campaign to this segment.
- Send a similar push campaign that creates a sense of urgency, includes an incentive, or otherwise encourages recipients to buy.
- Follow up via email or SMS to direct users to your website.
  - Note: for this, add a condition, such as **If someone can or cannot receive marketing > can receive** and then choose either SMS or email.
- Target an ad or banner in your app to this segment.

## Outcome

These segments help you increase your click rate, boost deliverability, and recover revenue by reaching out to those who almost bought from you. You can resend emails to these segments or follow up with a similar message to encourage people to buy.

You can also adapt these segments to your needs, such as by:

- Temporarily shortening the timing for special holidays and events.
- Checking if someone consented to another channel.
- Filtering by which collections someone browsed.
- Only including those active on your app (for push notifications).

## Additional resources

- Learn the [difference between AND versus OR](https://help.klaviyo.com/hc/en-us/articles/360036534631).
- Find inspiration for other segments you can build:
  - [Advanced segmentation reference](https://help.klaviyo.com/hc/en-us/articles/360035312491)
  - [Recommended SMS segments reference](https://help.klaviyo.com/hc/en-us/articles/360047879512)