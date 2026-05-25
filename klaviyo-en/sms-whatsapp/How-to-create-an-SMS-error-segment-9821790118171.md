---
id: "9821790118171"
title: "How to create an SMS error segment"
source_url: "https://help.klaviyo.com/hc/en-us/articles/9821790118171-How-to-create-an-SMS-error-segment"
section: "Segment your SMS subscribers"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:06Z"
language: "en"
---
Learn how to create a segment of SMS subscribers who are currently unable to receive your messages. This segment will be based on SMS errors, and it’s important to exclude the segment from your campaigns.

****What is an SMS error segment?****

This segment groups together profiles with bad SMS data: people who were sent an SMS message, but didn’t receive it due to an error.

It’s a best practice to exclude the SMS error segment from your campaigns so that you avoid sending to those who likely won’t receive them. This is beneficial for 2 reasons:

1. Better SMS deliverability
2. More efficient use of your SMS credits

****Why aren’t these users unsubscribed automatically?****

In many cases, the SMS errors mentioned below are temporary, so you don’t want to unsubscribe someone right away. However, there are other [errors when Klaviyo will unsubscribe the profile from SMS](https://help.klaviyo.com/hc/en-us/articles/4404710011035).

Instead, you should exclude profiles with these errors from campaigns, but allow flows (and SMS conversations) to send.

## Create an SMS error segment

1. Navigate to ****Audience > Lists & segments****.
2. Click ****Create New > Create segment****.
3. Name the segment (e.g., SMS errors).
4. Add the following conditions:

   - **If someone can or cannot receive SMS > can receive > SMS**
     AND
   - ****What someone has done (or not done)****
     ****> Failed to Deliver SMS at least once in the last 30 days****
     ****Where Failure Type equals Device unreachable****
     OR
   - **What someone has done (or not done)**
     **> Failed to Deliver SMS at least once in the last 30 days**
     **Where Failure Type equals Device disconnected**
     OR
   - **What someone has done (or not done)**
     **> Failed to Deliver SMS is at least 2 over all time**
     **Where Failure Type equals Device unreachable**
     OR
   - **What someone has done (or not done)**
     **> Failed to Deliver SMS is at least 2 over all time**
     **Where Failure Type equals Device disconnected**
     OR
   - **What someone has done (or not done)**
     **> Failed to Deliver SMS at least once over all time**
     **Where Failure Type equals Invalid mobile number**
     OR
   - **What someone has done (or not done)**
     **> Failed to Deliver SMS is at least 5 over all time**
     **Where Failure Type equals Unknown error**
5. Click ****Create Segment****.

## SMS error segment and list cleaning

The SMS error segment is a key part of the list cleaning process for SMS. This segment should be excluded from most campaigns on an ongoing basis. Once profiles have demonstrated a longer, sustained period with errors, you can consider removing SMS consent from the profiles.

Learn more about [SMS list cleaning and the long-term error segment](https://help.klaviyo.com/hc/en-us/articles/6155416998555).

## Outcome

You now have a segment of everyone who’s recently received an SMS error that indicates they currently can’t receive text messages.

When creating SMS campaigns, add this segment under **Recipients > Don’t send to (Optional)**.

![Campaign wizard where the Don't send to field is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28720895162011)