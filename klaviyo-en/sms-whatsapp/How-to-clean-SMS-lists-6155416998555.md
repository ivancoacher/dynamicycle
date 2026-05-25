---
id: "6155416998555"
title: "How to clean SMS lists"
source_url: "https://help.klaviyo.com/hc/en-us/articles/6155416998555-How-to-clean-SMS-lists"
section: "SMS deliverability best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:03Z"
language: "en"
---
## You will learn

Learn about list cleaning for SMS, including why list cleaning is important, how to list clean, and when to clean your lists.

List cleaning for SMS revolves around making sure that you are sending to profiles that are actually able to receive your texts. SMS message delivery can fail for a number of reasons, and it is important to exclude profiles consistently experiencing errors from your usual sends. Once a profile is unable to receive a message for an extended period of time, you can consider removing SMS consent from their profile.

## Why clean SMS lists?

Wireless carriers don’t evaluate your SMS performance like email providers do, meaning list cleaning doesn’t hold the same weight for SMS as it does for [email](https://help.klaviyo.com/hc/en-us/articles/115005078347).

As long as you have consent from a profile, you can continue to send them SMS messages. However, make sure to include a way to opt out regularly (i.e., at least once a month) so anyone who wants to unsubscribe can do so.

These requirements may vary according to local legislation in different countries.

However, there are times when you might want to unsubscribe profiles from SMS. Specifically, it’s a good idea to unsubscribe profiles who simply aren’t receiving SMS messages over a period of several months.

It’s a best practice to keep your list clean from profiles experiencing delivery errors for 2 main reasons:

- ****Better SMS deliverability****
  Sending to profiles already experiencing errors can be viewed negatively by carriers and cause them to block your sends.
- ****More efficient use of your SMS credits****
  Sending to profiles that are experiencing errors still uses your SMS credits, but they may not be able to receive your messages.

## How to clean an SMS list

The best way to list clean for SMS is:

1. Create an SMS error segment to capture profiles that are unable to receive messages and exclude them from sends.
   These profiles can still receive messages from flows and SMS conversations.
2. Send an SMS campaign to this group at least once every month to keep them “warm.”
   If possible, choose only your most high-value campaigns, such as sales or other major promotions. Exclude this segment from every other campaign.
3. Create another segment to capture profiles that are unable to receive a message for an extended period of time (i.e., 3 to 6 months).
4. Remove SMS consent from profiles in the long-term SMS error segment, or exclude them from all future campaign sends.

### Double opt-in

To help keep your SMS list clean from profiles that are unable to receive SMS messages because of errors, it is highly recommended to take advantage of double opt-in. Double opt-in is a process through which a new subscriber must confirm their subscription before being subscribed to a given list. Profiles that are not able to receive the confirmation SMS (e.g., invalid phone numbers, device like a landline that is incapable of receiving SMS, etc.) won’t be added to your list, helping with the process of maintaining a clean list.

Additionally, double opt-in prevents customers from being able to subscribe invalid numbers (e.g., numbers that are incorrect due to a typo or numbers that are unable to receive messages like landlines). Customers also won’t be able to submit someone else's number, which lacks the express written consent required for SMS.

Learn more about [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108).

## Create an SMS error segment

To identify unengaged SMS contacts, use the following segment:

- If someone can or cannot receive SMS > can receive > SMS
  AND
- What someone has done (or not done) > Failed to Deliver SMS at least once in the last 30 days
  Where Failure Type equals Device unreachable
  OR
- What someone has done (or not done) > Failed to Deliver SMS at least once in the last 30 days
  Where Failure Type equals Device disconnected
  OR
- What someone has done (or not done) > Failed to Deliver SMS is at least 2 over all time
  Where Failure Type equals Device unreachable
  OR
- What someone has done (or not done) > Failed to Deliver SMS is at least 2 over all time
  Where Failure Type equals Device disconnected
  OR
- What someone has done (or not done) > Failed to Deliver SMS at least once over all time
  Where Failure Type equals Invalid mobile number
  OR
- What someone has done (or not done) > Failed to Deliver SMS is at least 5 over all time
  Where Failure Type equals Unknown error

In many cases, SMS errors are temporary, so you don’t want to unsubscribe someone right away.

### When Klaviyo automatically removes consent

Note that there are cases where Klaviyo automatically removes SMS consent from a number to help maintain the cleanliness of your SMS lists. Klaviyo automatically removes consent in the following cases:

Usually, someone is automatically unsubscribed from SMS for the following reasons:

- The subscriber has opted out
- The subscriber changed phone numbers or carriers
- The subscriber is a known litigator
- Klaviyo detects a landline number
- Wireless carriers block a message

Learn more about [when Klaviyo automatically removes SMS consent](https://help.klaviyo.com/hc/en-us/articles/4404710011035).

### Exclude error segment from sends

Once you create your SMS error segment, [exclude it from most SMS campaigns](https://help.klaviyo.com/hc/en-us/articles/360007016571) on an ongoing basis.

![](https://klaviyo.zendesk.com/hc/article_attachments/32528280633115)

As customers fall out of the segment they will be included in SMS sends again. If they experience another error, they will enter the error segment again and once again be excluded.

### Keep contacts “warm”

While you should exclude unengaged SMS contacts from most of your regular sends, it is important to occasionally text them to keep the contacts warm.

In regards to SMS contacts, “warm” refers to maintaining a consistent sending schedule with your audience (i.e., so that they receive messages from you periodically).

While the engagement doesn’t have to be frequent, sending at least once a month can help prevent contacts from becoming inactive and forgetting about your brand. Contacts that receive a text after a long period without sends are more likely to unsubscribe or report your texts, which leads to deliverability issues and a higher likelihood of being filtered by carriers.

For example, say you have a group of SMS subscribers that you haven't messaged in 3 months. If you message them for Black Friday, some may react negatively and opt out of your texts, or flag your messages as spam.

To prevent unengaged contacts from becoming “cold” over time:

- These campaigns should be the most important messages of the month, like product launches and major sales

- Include your unengaged SMS contacts in 1 or 2 sends per month, depending on how frequently you send.
- Rely on your flows to re-engage contacts.

## Identify profiles with long-term errors

While most SMS errors are temporary, when a profile experiences delivery errors for an extended period of time, they are unlikely to be able to receive messages again. You can capture these profiles with the following segment.

- If someone can or cannot receive SMS > can receive > SMS
  AND
- What someone has done (or not done) > Received SMS > 0 times in the last 26 weeks
  AND
- What someone has done (or not done) > Failed to Deliver SMS at least 5 in the last 26 weeks
  Where Failure Type equals Device unreachable
  OR
- What someone has done (or not done) > Failed to Deliver SMS at least 5 in the last 26 weeks
  Where Failure Type equals Device disconnected
  OR
- What someone has done (or not done) > Failed to Deliver SMS is at least 2 over all time
  Where Failure Type equals Device unreachable
  OR
- What someone has done (or not done) > Failed to Deliver SMS is at least 2 over all time
  Where Failure Type equals Device disconnected
  OR
- What someone has done (or not done) > Failed to Deliver SMS at least once over all time
  Where Failure Type equals Invalid mobile number
  OR
- What someone has done (or not done) > Failed to Deliver SMS is at least 5 over all time
  Where Failure Type equals Unknown error

## Remove SMS consent

Once an SMS contact is no longer generating any revenue for your business in Klaviyo because they are unable to receive messages for an extended period of time, you have 2 options:

- Keep them as a subscriber and continue texting them regularly
- Remove SMS consent completely

If you’d prefer, you can keep SMS consent on your SMS profiles and exclude them from sends. This gives you the opportunity to send texts if they engage again in the future. However, you should continue to text them monthly to maintain your relationship with them, and decrease the risk of them unsubscribing or marking a message as spam. Continuing to send messages to them can also help identify if an error was temporary or permanent.

If you instead choose to remove SMS consent, you will no longer be able to send texts to a contact unless they resubscribe.

Once you have created your long-term error segment, remove SMS consent from the profiles included with the following steps:

Note that if you remove SMS consent, profiles will be completely unsubscribed from the channel. You will not be able to message them unless they resubscribe.

1. On your segment, select ****Manage Segment****.
2. Select ****Export Segment to CSV****.
3. In the export wizard, check the **Phone number** and **Country** fields.
4. Click ****Start Export****.
5. In the bottom left corner of Klaviyo, click your brand name.
6. Select ****Settings**** > ****Other**** > ****Profile maintenance****.
7. Scroll to the **Import SMS Unsubscribes section**.
8. Click ****Browse Files**** and upload your CSV file of SMS contacts to unsubscribe.
9. Click ****Unsubscribe Phone Numbers****.
10. Confirm your selection in the modal by clicking ****Unsubscribe Phone Numbers****

It may take a few minutes for the process to complete.

## Outcome

After you finish unsubscribing your contacts that are not able to receive messages due to errors, you’ll be left with only those that can successfully receive SMS.