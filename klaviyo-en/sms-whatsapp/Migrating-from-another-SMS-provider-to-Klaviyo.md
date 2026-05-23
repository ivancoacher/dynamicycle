---
id: 360035511812
title: "Migrating from another SMS provider to Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360035511812-Migrating-from-another-SMS-provider-to-Klaviyo"
section: "Migrate SMS providers"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:46Z"
language: en
---

## You will learn

Learn the steps for migrating from another SMS provider to Klaviyo.

****Why use Klaviyo for SMS?****

There are a few key benefits of using Klaviyo for SMS compared to other platforms.

The first is that Klaviyo is an all-in-one platform to communicate with customers. Since both email and text messages are available in Klaviyo, you can send customers messages via the channel they prefer without over-messaging them. This is particularly true for flows, as they show SMS and email in the same view, making it easy to avoid sending a text and email at the same time.

Klaviyo’s segmentation capabilities also allow you to be more granular in grouping your SMS subscribers. This helps you build a personal connection with each individual, making your interactions feel like a conversation. Since data from your ecommerce platform syncs to Klaviyo, you can create segments based on any event passed to us as well as profile properties you collect.

## Before you begin

****Klaviyo SMS best practices****

|  |  |
| --- | --- |
| ****Dos**** | ****Don’ts**** |
| Provide value in every message | Text anyone who has not opted into SMS |
| Keep SMS messages short and concise | Use abbreviations or text-speak unless you know your audience will understand and appreciate them |
| Send only between 9 a.m. and 8 p.m. in the recipient’s local timezone | Send too frequently (i.e., more than six times per month) |
| Let recipients know who the messages are coming from (e.g., mention your brand name) | Send an SMS for everything — be strategic and intentional |
| Include opt-out instructions in your messages | Include any spam-like content or phrases related to sex, hate, alcohol, firearms, or tobacco (SHAFT) or CBD |
| Include a link and use the Klaviyo link shortener | Neglect other channels, such as email, as it’s important to use SMS and email together for the best results |
| US and Canada: do not collect consent or message anyone until you have a short code or verified toll-free number |  |
| \*Use double opt-in for your lists |  |
| Cap your SMS messages to 157 characters (dynamic content and shortened links don't have a solid character count, so it's important to have extra characters so that you don't accidentally exceed the 160 character limit) |  |

\*Double opt-in is skipped for subscribers in the UK and Australia. This is because branded sending IDs, which are used for Klaviyo SMS in these countries, don’t allow recipients to text back.

MMS is not available in all countries (e.g., the UK and Germany). If you send an MMS to a recipient in a country where MMS is not supported, the message text will send, but the image or GIF will not.

## Klaviyo SMS migration steps

Below, we list out what to do when migrating as well as where these steps fall within the Getting Started with SMS course.

- In Orientation:
  1. [Send a final message from your provider](#h_01GMTHKVJWZFY7XH159YRK0BT6) (2 minutes)
  2. [Export data from previous SMS provider](#h_01GF3JMX7AAG25H0WDXZ05AGCP) (11 minutes)
  3. [Port phone number (optional)](#h_01GF3JMGEWQ3R9X2KX7AN2X1KS) (2 minutes)
- In Add subscribers:
  1. [Import SMS contacts](#h_01GF3JN7Q77P6PTR6TPW2ERSQY) (6 minutes)
  2. [Create SMS subscribers segment](https://help.klaviyo.com/hc/en-us/articles/360035511812#create-an-sms-subscribers-segment12) (2 minutes)
- In Build relationships:
  1. [Send a campaign from your new number](#h_01GMTFJDM0XNNRA0XV1N7J06ZT) (3 minutes)

## Orientation

### Send a final message from your previous provider

It's a best practice to tell subscribers when you're about to change your number, and this is required for US short codes and some US wireless carriers.

If you are not changing numbers (i.e., you're porting your number), skip to the [section on exporting your data](#h_01GF3JMX7AAG25H0WDXZ05AGCP).

A week before changing numbers, send a final message from your previous SMS provider. Some carriers require this, and failure to comply may result in an audit or deliverability issues.

Include the following in the message:

- Your organization’s/brand’s name
- Your new phone number
- Key details about the transition, like support/contact care information (e.g., “Reply HELP for help”)
- Opt-out language (e.g., “Text STOP to unsubscribe”)

### Export data from previous SMS provider

After completing the Orientation action steps, you'll need to export your existing data. The steps for migrating vary depending on your previous SMS provider. In general, though, you will need to:

1. [Export SMS contacts](https://help.klaviyo.com/hc/en-us/articles/360035428731)
2. Export any additional data you want

If possible, when exporting contacts, we recommend separating subscribers by:

- Country (if you send to more than one country)
- Opt-in status

The first makes it easier when you’re importing consent, while the second ensures that you don’t accidentally send to non-consented subscribers and risk breaching compliance.

Migrating from Yotpo? Check out our [Yotpo Email & SMS Migration integration](https://help.klaviyo.com/hc/en-us/articles/39598076123547).

### Port phone number (optional)

When switching SMS providers, keeping the same number makes for a smoother transition for your subscribers. They’ll recognize the number as being from your brand, so you’ll be able to pick up exactly where you left off.

Note that porting a number results in the loss of any voice capabilities.

You can port toll-free numbers and short codes; however, porting is not available for shared short codes or branded sender IDs.

The porting process takes time to complete; allow up to 4 weeks for the number to port into Klaviyo.

|  |  |
| --- | --- |
| ****How to port a phone number**** | |
| 1. Click your organization name in the bottom left. 2. Navigate to ****Settings > SMS****. 3. Select ****Port an Existing Number****. 4. Click ****Submit Port Request****. 5. Check your email for a message from the SMS team at Klaviyo. 6. Fill out the relevant application for your number type. 7. Allow up to 4 weeks processing time. | ![SMS_sender_information.jpeg](https://klaviyo.zendesk.com/hc/article_attachments/28716330099483) |

## Add subscribers

### Import SMS contacts (7 minutes)

#### 1. Format your CSV

It’s time to import your contacts into Klaviyo. Before uploading the data, check that it’s formatted correctly; otherwise, the import won’t work.

In your CSV, you must include:

- Phone number
- [Country](https://help.klaviyo.com/hc/en-us/articles/5306587861531) (either through the country code ****or**** as a separate column)

Some providers put both opt-outs and opt-ins in the same CSV. If this is the case for your CSV, it's important to [remove all unsubscribed SMS profiles from your CSV](https://help.klaviyo.com/hc/en-us/articles/5302764979611).

|  |  |
| --- | --- |
| ![Indicating the country via a country code](https://klaviyo.zendesk.com/hc/article_attachments/28716353105819) | ![Indicating the country via a column with the country's name](https://klaviyo.zendesk.com/hc/article_attachments/28716353114011) |

****Recommended information****

The following columns are recommended but not required:

- Email
- First name and last name
- Consent timestamp

If email is available, make this the first column in your CSV. If email is not available, make phone number the first column.

If you don’t have the consent timestamp, make sure you have explicit consent for all phone numbers in the list. When importing, you’ll need to verify that you have consent; if this isn’t true, you risk falling out of compliance.

#### 2. Remove opted-out contacts

Before importing your SMS contacts, remove anyone who is no longer subscribed.

To do so, you'll need to filter your CSV to show only those who are opted out, copy them to a new spreadsheet, and then delete them from the original CSV. For more detailed instructions, see [how to filter out unsubscribed contacts from your SMS CSVs](https://help.klaviyo.com/hc/en-us/articles/5302764979611).

#### 3. Upload a CSV of SMS contacts

|  |  |
| --- | --- |
| 1. Format and check your CSV.  2. Turn any list-triggered flows (e.g., your welcome series) to manual.  3. Navigate to ****Audience >**** ****Lists & Segments****.  4. Choose the list to import to (e.g., your main subscriber list).  5. Click the ****Manage List**** dropdown.  6. Choose ****Import Contacts****.  7. Select your CSV.  8. Map your data to fields within Klaviyo.   - If you have the consent timestamp, map this to **SMS Consent. Timestamp** - If you don’t have the consent timestamp, click ****Update SMS Consent****, check the box acknowledging all phone numbers have given you their consent, and then click ****Update SMS Consent****.   9. Click ****Import Review****.  10. Click ****Start Import****.  11. Wait at least 4 hours before you turn your list-triggered flow live again. | [Embedded content](//fast.wistia.com/embed/iframe/9xczkyuscy) |

****Tip: Formatting phone numbers****

Your phone number must be in one of the following formats:

- E.164
  - +12345678900
  - +12-345-678-900
  - +12 345 678 900
- RFC3966
  - tel: 12345678900
- E.123 national notation
  - (1234) 567 8900
  - 12345678900
- E.123 international notation
  - +12 345 678 900
  - +1 234 567 8900

****Tip: Including the country****

The best way to include the country varies depending on how many countries your SMS subscribers live in. Below are instructions for the most common use cases.

For more details, see [How to indicate the country for an SMS import](https://help.klaviyo.com/hc/en-us/articles/5306587861531).

****One country****

|  |  |
| --- | --- |
| 1. Make the first column in the CSV email (if available) or phone number.  2. Add in a column named **Country.**  3. Input the name of the country in the first cell in this column.  4. Copy and paste the country’s name into the rest of that column’s cells. | [Embedded content](//fast.wistia.com/embed/iframe/k0omtudiao) |

****Only the US and Canada****

|  |  |
| --- | --- |
| 1. Make the first column in the CSV email (if available) or phone number.  2. Add a column to the left of your phone number column.  3. Insert ‘+1 in the first cell of the new column.  4. Copy the cell with ‘+1.  5. Highlight all blank cells in this column.  6. Paste the copied cell; this will populate the ‘+1 in every highlighted cell.  7. Add a column to the right of the phone number column .  8. Name the new column **Phone Numbers.**  9. Add the following in the first cell of the new column:   - =Concat(first cell with ‘+1,first cell with phone numbers)   OR   - =Concatenate(first cell with ‘+1,first cell with phone numbers)   10. Click either the bottom right corner or the bottom middle of the cell and hold.  11. Drag straight down that column to apply the formula to all cells.  12. Delete the name of the original phone numbers column so that only the column with the joined cells is labeled **Phone Numbers** | [Embedded content](//fast.wistia.com/embed/iframe/jdvjosjgoe) |

****Multiple countries****

In this instance, the simplest approach depends on your previous SMS provider. Ideally, they will include the country or country code as part of the export, in which case you can follow the steps for US and Canada, but use a '+ rather than a '+1.

If that’s not the case, the next best thing is to segment by country in your previous SMS provider, and then export the segment. If this is the case, follow the steps listed under **One Country**.

For other cases, you may need to manually identify the country and input it into your CSV before uploading.

****Tip: Formatting the consent timestamp (optional)****

If you have the consent timestamp, it must be in one of the accepted date/time formats. The following are examples of accepted formats for September 30, 2014 at 1:34:08 pm:

- 2014-09-30 13:34:08
- 2014-09-30 13:34:08+00:00
- 09/30/2014 13:34:08
- 09/30/14 13:34:08
- 09/30/2014 13:34
- 09/30/14 13:34
- 2014-09-30T13:34:08
- 2014-09-30 13:34:08.000001
- 2014-09-30T13:34:08.000001
- 2014-09-30 13:34:08.000001-04:00
- 1412098448 (Unix)

#### 4. Import opted-out contacts

If you want to add in the information for opted-out contacts, you can upload them into Klaviyo and mark them as unsubscribed. This way, you'll have the data you've already collected but won't risk texting them.

The first step is creating a list of opted-out contacts. You can do this by filtering your unsubscribed contacts from your CSV and adding them to a new list, as discussed above. Note that you'll need to have the phone number and country in order to upload opted-out contacts.

Once that's done, follow these steps:

1. Format and check your CSV.
2. Turn any list-triggered flows (e.g., your welcome series) to manual.
3. Navigate to ****Audience >**** ****Lists & Segments****.
4. Choose the list to import to (e.g., your main subscriber list).
5. Click the ****Manage List**** dropdown.
6. Choose ****Import Contacts****.
   ****![Manage List dropdown where you can select Import Contacts](https://klaviyo.zendesk.com/hc/article_attachments/28716353116187)****
7. Select your CSV.
8. Map your data to fields.
9. ****Important:**** Do not apply SMS consent.
10. Click ****Import Review****.
11. Click ****Start Import****.
12. Wait at least 10 minutes for the profiles to import.
13. Open the dropdown under your account name.
14. Click ****Settings > Other > Profile maintenance****.
15. Scroll to the **Import SMS Unsubscribes** section.
16. Click ****Browse Files**** and upload your CSV file of SMS contacts to unsubscribe.
    ![In Klaviyo's SMS settings page, a cursor hovers over the Browse Files button](https://klaviyo.zendesk.com/hc/article_attachments/28716330119067)
17. Click ****Unsubscribe Phone Numbers****.
18. Confirm your selection in the modal that appears.

The import process may take a few minutes to complete.

### Create an SMS subscribers segment

Segments update automatically; profiles will enter or leave the segment when they meet or fail to meet the segment’s conditions. This is different from lists, which are static.

Without a segment, it can also be difficult to know how many SMS subscribers you have, as subscribers may be spread throughout different lists or you may have a list that shows both your email and SMS subscribers together. An SMS segment will show you everyone who is consented to your SMS marketing, letting you see all of your subscribers at once.

Keep a list titled “SMS Subscribers” in your account, as it’s beneficial to have in certain use cases (e.g., consent at checkout and signup forms). However, we recommend only sending to your SMS segment.

|  |  |
| --- | --- |
| ****How to create an SMS subscribers segment**** | |
| 1. Go to ****Audience > Lists & Segments > Create List/Segment > Segment****. 2. Name your segment 3. Add the condition: **If someone is or is not consented to receive SMS.** 4. Keep the condition as: **Person is** **consented to receive SMS.** 5. Click ****Save****. | ![Segment of anyone currently opted in to SMS](https://klaviyo.zendesk.com/hc/article_attachments/28716330121371) |

## Build relationships

### Send an SMS campaign

What you want to send depends on your audience as well as if you kept the same number when you migrated to Klaviyo.

Journey Check: Click the link that best fits your situation:

- [I changed my sending number](https://help.klaviyo.com/hc/en-us/articles/360035511812#if-you-switched-numbers-or-ported-a-short-code14)
- [I ported a toll-free number](https://help.klaviyo.com/hc/en-us/articles/360035511812#if-you-kept-the-same-number15)
- [I ported a short code](https://help.klaviyo.com/hc/en-us/articles/360035511812#if-you-switched-numbers-or-ported-a-short-code14)
- [I previously only used an branded sender ID](https://help.klaviyo.com/hc/en-us/articles/360035511812#if-you-kept-the-same-number15)

### If you switched numbers or ported a short code

If you ported a short code or switched SMS sending numbers, your first campaign from your new number should act as a follow-up to your last message from your old number, informing subscribers about the change and how you’ll be texting them going forward.

In the text, you’ll want to let subscribers know certain information, including:

- Your brand’s name
- The recurring-SMS program’s name or product description
- Support/customer care information (e.g., “Reply HELP for help”)
- Opt-out instructions (e.g., “Text END to unsubscribe”)
- Disclosure that message and data rates may apply
- Disclosure for message frequency

Example text: "[Organization Name]: Hi from our new number! Thanks for sticking with us.[Add offer, if desired]. Text STOP to opt out, HELP for help. Msg & data rates may apply. Msgs are recurring."

|  |  |
| --- | --- |
| ****How to send an SMS campaign (number change)**** | |
| 1. Navigate to the ****Campaigns**** tab. 2. Click ****Create Campaign****. 3. Select ****SMS**** in the modal. 4. Click ****Create Campaign**** in the modal. 5. Name the campaign. 6. Choose which list(s) or segment(s) to send to. 7. Click ****Save & Continue to Content****. 8. Write out your text in the **Message Content** box. 9. Click ****Save & Continue to Review****. 10. Review the settings for the campaign, confirming that the message will send to the right audience and tracking is enabled. 11. Click ****Schedule or Send****. 12. Choose ****Schedule**** to send the campaign at a later date, or ****Send Now**** to send the campaign immediately. | ![Example of a first text from a new number](https://klaviyo.zendesk.com/hc/article_attachments/28716353112347) |

### If you kept the same number

If you kept the same number (and it’s not a short code) or previously only used a branded sender ID, you’ll want to continue your previous SMS strategy. Were you sending out text alerts every Thursday? If so, keep the same cadence and content. In the first message, though, we recommend including a reminder about who you are and how to opt out.

For future sends, think about how you can use your data in Klaviyo to better target your audience, such as personalizing your messages and creating segments around location, purchase history, gender, etc.

****Tips: Message content****

Keep these best practices in mind when creating an SMS or MMS campaign:

- Reference your brand name
- Make the message as short as possible
- Only send between 9 a.m. and 8 p.m. in the recipient’s local timezone
- Include a link and use the Klaviyo link shortener
- Cap messages to 157 characters to leave room for dynamic content

Note that if you're sending to a country where MMS is not available, the message will send, but the image or GIF attached won't.

****Tips: Message count****

When creating messages, keep in mind how long the message is:

- MMS messages can be up to 1,600 characters.
- SMS messages are limited to 160 characters.
  If you include an emoji, it will shorten the character count from 160 to 70 characters.

The message type and number is shown on the left-hand side so that you can know how this message will affect your plan. Further, consider who will receive this message. For the example below, this message equals two SMS. For recipients in the US, this will count as two credits; however, it will count as six credits for anyone in the UK.

Note that even if a message counts as multiple messages, due to the way text messages are displayed, it will show as a single message both in the Klaviyo preview and on the recipient’s phone.

## Additional resources

- Learn the basics of Klaviyo SMS: see [Getting Started with SMS](https://academy.klaviyo.com/getting-started-with-sms/1411601)
- Find out [how to collect SMS subscribers](https://klaviyo.zendesk.com/hc/en-us/articles/360035056972)
- [Understand and review your SMS deliverability](https://help.klaviyo.com/hc/en-us/articles/1260806260849)