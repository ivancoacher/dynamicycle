---
id: "35737275447067"
title: "How to use unsubscribe detection"
source_url: "https://help.klaviyo.com/hc/en-us/articles/35737275447067-How-to-use-unsubscribe-detection"
section: "Understanding SMS compliance settings"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-05-18T13:03:24Z"
language: "en"
---
You must be an Owner, Admin, or Manager to use this functionality. This feature is also only available for subscribers in the United States.

Learn how to either automatically unsubscribe or send unsubscribe instructions when an inbound message likely includes an opt-out request.

Using the Unsubscribe detection feature is highly recommended, as the [FCC ruled](https://help.klaviyo.com/hc/en-us/articles/35575786638107) that brands must respect opt-out requests made through “any reasonable means.”

This information is intended solely for educational and informational purposes and should ****not**** be construed as legal advice. The content provided is general in nature and may not reflect the most up-to-date information. Klaviyo strongly advises consulting with a qualified legal counsel to ensure your compliance with applicable laws and regulations in connection with your use of our services.

## How it works

This feature:

- On by default in Klaviyo
- Only affects subscribers in the United States

  **Unsubscribe detection** evaluates all inbound text messages (i.e., ones from your customer to your brand’s sending number). It also assigns an **Intent** score, which represents the likelihood that the inbound message contains an opt-out request.

  Say that someone texted "SOTP" instead of "STOP" or texted something like "Please no more messages." Clearly, the person intended to unsubscribe, but the keyword is either mis-spelled or missing.

  In these cases, the Unsubscribe detection feature would either:
- Automatically remove consent.
- Send a message with opt-out instructions (e.g., “text STOP to unsubscribe ”).

****Contains logic vs. unsubscribe detection****

2 key differences between this setting and [using contains for a keyword](https://help.klaviyo.com/hc/en-us/articles/29109965092251#h_01J7HDKF611CKXSD6ETN50EQAX) are:

- With **contains**, Klaviyo only searches for a word within a message.
- With **Unsubscribe description**, Klaviyo searches for the intent.

A good example of this is if someone texts “please cancel my order.” In this case, the subscriber will be opted out if CANCEL is set to **contains**, but they won’t be opted out if using **exact match** and unsubscribe detection.

## View or change this setting

To find the **Unsubscribe detection** feature

1. Select your account name in the lower left corner.
2. Click ****Settings > SMS****.
3. Navigate into the ****Keyword responses**** tab.
4. Scroll to the **Unsubscribe detection** feature.

   - This feature is on by default and is recommended if you have SMS subscribers in the United States.
5. Select ****On**** or ****Off**** for the unsubscribe detection feature.

   - If you picked On, you can select ****Reply with instructions on how to unsubscribe****, which sends a message with opt-out instructions if Klaviyo detects any unsubscribe intent.
     - Note that you currently cannot edit the opt-out instructions.![The setting for the Unsubscribe detection feature](https://klaviyo.zendesk.com/hc/article_attachments/37145596553755)
6. If you want to turn this feature on or off, simply select **On** or **Off**, then click ****Save****.

## Review messages that caused an opt-out

You can and should also review any message that resulted in an unsubscribe based on intent.

While Klaviyo is offering this feature to assist customers in tracking opt-out requests, tracking opt-out requests made by means other than the FCC’s mandatory opt-out keywords is still your brand’s responsibility.

You can review inbound messages (including those marked as unsubscribe requests) to:

- Confirm that those messages have been properly categorized.
- Check that other inbound messages (ones not flagged as unsubscribe requests) do not express the intent to opt out.
- See if you should remove consent from anyone who received unsubscribe instructions but did not actually opt out.

The simplest approach is to create a segment and then review the message for each profile.

### Create a segment for unsubscribes based on intent

1. Navigate to ****Audience > Lists & segments****.
2. Select ****Create New > Create segment****.
3. Name the segment (e.g., Intent unsubscribes).
4. Set the following condition:

   - **What person has or has not done > Sent SMS > at least once in the last > 30 days > where Intent 1 > equals > Ask to unsubscribe**![Example of a segment for everyone unsubscribed based on intent](https://klaviyo.zendesk.com/hc/article_attachments/35866587680411)
5. Click ****Create segment****.

### Review message that caused the unsubscribe

To see which message caused the opt-out:

1. Click 1 of the profiles in the segment.
2. On the right-hand side, filter the event to **Sent SMS**.
   ![Filtering metrics to only show Sent SMS](https://klaviyo.zendesk.com/hc/article_attachments/35866587683611)
3. Click the down arrow next to that metric.
   ![Arrow to see more details about an event](https://klaviyo.zendesk.com/hc/article_attachments/35866555498395)
4. Review what the person sent by looking at the **Message body**.

- **Intent 1** indicates that there may have been a request to unsubscribe; however, it does not mean an unsubscribe occurred.
- The **Intent 1 Confidence** indicates how confident Klaviyo is that the profile requested to unsubscribe. If this number is low, it may not result in an opt-out.