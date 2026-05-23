---
id: 18523292380187
title: "How to resolve AT&T spam traps"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18523292380187-How-to-resolve-AT-T-spam-traps"
section: "SMS deliverability best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: en
---

## You will learn

Learn about AT&T spam traps, how Klaviyo notifies you if it detects that you may have been caught in the spam trap, and the steps you can take to rebuild your reputation with AT&T.

## AT&T spam traps

Carriers such as AT&T in the US may place SMS senders into a 30 day probationary period when they identify the sender is not following SMS messaging best practices. During this time, senders may see less than 5% deliverability on this particular network with all errors being returned as **Device Unreachable - Vendor code 30003**.

If a sender continues to send to devices on the network during the probationary period, this results in the accumulation of errors that can lead to indefinite delivery issues on the network.

## AT&T spam trap alerts in Klaviyo

If Klaviyo detects that your account may be potentially caught in the AT&T’s 30 day spam trap, you’ll receive notifications alerting you of the issue in:

- Your email inbox
- An in-app notification on the home page
- An in-app notification on the campaigns list-view page

## Exclude delivery failures from sends

To prevent the accumulation of errors during the probationary period, Klaviyo recommends excluding profiles that experienced a send failure from your future sends during this time.

To exclude customers that experienced failures, use the following segment:

- **If someone can or cannot receive marketing > Person can receive SMS marketing**

AND

- **What someone has done (or not done) >**

  **Failed to Deliver SMS at least once in the last 30 days**

  WHERE **Failure Type equals Device disconnected**

OR

- **What someone has done (or not done) > Failed to Deliver SMS at least once in the last 30 days**

  WHERE **Failure Type equals Device unreachable**

OR

- **What someone has done (or not done) > Failed to Deliver SMS at least once over all time**

  WHERE **Failure Type equals Message blocked**

OR

- **What someone has done (or not done) > Failed to Deliver SMS is at least once over all time**

  WHERE **Failure Type equals Device incapable of receiving SMS**

OR

- **What someone has done (or not done) > Failed to Deliver SMS is at least once over all time**

  WHERE **Failure Type equals Invalid mobile number**

OR

- **What someone has done (or not done) > Failed to Deliver SMS at least 2 over all time**

  WHERE **Failure Type equals Device disconnected**

OR

- **What someone has done (or not done) > Failed to Deliver SMS at least 6 over all time**

  WHERE **Failure Type equals Device unreachable**

OR

- **What someone has done (or not done) > Failed to Deliver SMS is at least 5 over all time**

  WHERE **Failure Type equals Unknown error**

![ATT spam trap segment](https://klaviyo.zendesk.com/hc/article_attachments/28705699337371)

## What if my sending list is too small following the implementation of the recommended SMS error segment?

The SMS error segment is designed to eliminate profiles with recurring delivery errors from your SMS send lists. If the segment is too strict and too many of your subscribers are being filtered out, consider updating the criteria below to a higher number and monitor deliverability based on the send results:

- **What someone has done (or not done) >**

  **Failed to Deliver SMS is at least X over all time**

  WHERE **Failure Type equals Device disconnected**

OR

- **What someone has done (or not done) >**

  **Failed to Deliver SMS is at least X over all time**

  WHERE **Failure Type equals Device unreachable**

With an effective SMS error segment, you should see about 95% or more of SMS messages delivered successfully.

## Follow SMS best practices

In addition to capturing failed sends in an error segment, you should follow SMS best practices to maintain strong SMS deliverability.

- Check that the call to action [disclosures](https://help.klaviyo.com/hc/en-us/articles/4412878737051) are clear and accurately describe the SMS program users are signing up to. This helps keep opt-out rates down and ensures people are aware of the program they are subscribing to.
- Consider implementing [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108). This helps minimize failures like erroneous number sign ups, landlines, and devices incapable of receiving SMS.
- [Segment your subscribers](https://help.klaviyo.com/hc/en-us/articles/360047879512) to ensure content is personalized to their interests. This increases deliverability and reduces opt-out rates.
- Aim for opt-out rates of less than 1% per campaign.
- Ensure that opt-out information is available on campaigns.

See more [SMS best practices](https://help.klaviyo.com/hc/en-us/articles/13288640663579).

## Outcome

After 30 days without issues, the SMS subscribers who experienced errors will no longer meet the criteria for your exclusion segment and exit. At this point, you can send them SMS messages and expect successful deliveries

During this recalibration period, the expected SMS delivery rate is 85% - 90%. Outside of the recalibration period, the expected delivery rate is 95% and above.

## Additional resources

[Basics: SMS best practices](https://help.klaviyo.com/hc/en-us/articles/13288640663579)

[Understanding and reviewing your SMS deliverability](https://help.klaviyo.com/hc/en-us/articles/1260806260849)

[How to create and send an SMS campaign](https://help.klaviyo.com/hc/en-us/articles/360040039971)