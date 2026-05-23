---
id: 115002053752
title: "How to import your contacts from a previous ESP or CRM"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002053752-How-to-import-your-contacts-from-a-previous-ESP-or-CRM"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T10:57:19Z"
language: en
---

## You will learn

Learn how to import your contacts to Klaviyo from a previous email service provider (ESP) or customer relationship management platform (CRM). Klaviyo offers built-in integrations to sync data from certain ESPs and CRMs.

## Before you begin

If you're migrating from any of the below ESPs, we have instructions specific to your use case which you should consult instead:

- [Campaign Monitor](https://help.klaviyo.com/hc/en-us/articles/115005254968)
- [Constant Contact](https://help.klaviyo.com/hc/en-us/articles/115005082727)
- [Hubspot](https://help.klaviyo.com/hc/en-us/articles/360039708512-How-to-Migrate-from-HubSpot)
- [Salesforce Marketing Cloud](https://help.klaviyo.com/hc/en-us/articles/115000267471)
- [Listrak](https://help.klaviyo.com/hc/en-us/articles/360034550591)
- [Mailchimp](https://help.klaviyo.com/hc/en-us/articles/115005254948)
- [Sailthru](https://help.klaviyo.com/hc/en-us/articles/360036945872)

If you're coming from a different service, keep reading to learn how to import your contacts and data into Klaviyo. This article specifically covers importing contacts, but for general guidelines on migrating from another service to Klaviyo, [check out our migration guide](https://help.klaviyo.com/hc/en-us/articles/115005082767).

## Turn off your welcome series

Have you already turned on your [welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172) in Klaviyo? If so, you should turn it off before importing to avoid sending welcome messaging to existing contacts. When you're finished, turn it back on.

## Identify your engaged subscribers

First, you'll want to clean your contact list from your existing platform. This involves separating engaged and unengaged subscribers. We highly recommend that you import clean lists into Klaviyo and send to an engaged list for your first send - if you intend to sync over existing email lists, or manually import existing lists into Klaviyo, your email deliverability may be at risk if you skip this step.

Your former ESP likely provides a way to analyze the engagement level of your main list, using data points such as open rates, bounce rates, etc. Before you migrate any existing subscriber lists into Klaviyo, we recommend using all data available to isolate and remove any invalid or inactive emails that will only bloat your sending and drag down your deliverability. This should all be done in advance of your first send with Klaviyo.

There are two ways that you can import your contacts into Klaviyo, depending on what information you are able to export from your existing provider:

1. Upload a main list with engagement criteria - this works for those who can export date added, last opened, and last clicked timestamps from your previous ESP
2. Upload separate main, engaged, and inactive lists - this works for those who can't export date added, last opened, and last clicked timestamps from your previous ESP

## Upload an engaged main list

Export a list of all the active emails on your list with the following information:

- Date added (when they first entered your account)
- Last opened (when they last opened an email you sent)
- Last clicked (when they last clicked a link in an email you sent)

Each ESP and CRM is different, so if you aren't sure how to export this information, we recommend contacting your service's support team.

Please note that contacts who are not on your email list but have placed an order, abandoned a cart, etc. will be synced through your integration, not via list upload.

### Format your data

1. Once you have this data in a CSV, you'll want to add these date/time values as [custom properties](https://help.klaviyo.com/hc/en-us/articles/115005074627). This will allow you to build segments in Klaviyo based on this information.
2. In order to upload these contacts, you must have at the very least an "Email Address" column. You may also want to add "First Name" and "Last Name" columns, in addition to any other custom properties, like "Gender," that you'd like to upload at the same time.
3. It's important that you input the date added, last opened, and last clicked dates in one of the following formats:
   YYYY-MM-DD HH:MM:SS
   MM/DD/YYYY HH:MM:SS
   MM/DD/YY HH:MM:SS
   MM/DD/YYYY HH:MM
   MM/DD/YY HH:MM
   YYYY-MM-DDTHH:MM:SS
   If you don't use this format, Klaviyo will not recognize the value as a timestamp. If you're using Excel, you can remove autoformatting by changing the cell format to "Text." If there's no time of day associated with a date, you can set it to midnight by using the HH:MM:SS value 00:00:00.
4. When you're finished, the format of your CSV should look something like this:
   ![Spreadsheet showing contact bob.klaviyo@example.com with fields for first name, last name, date added - old ESP, etc](https://klaviyo.zendesk.com/hc/article_attachments/28723623146907)
5. Next, you can [upload this as a main list to Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005078967).

### Build an engaged segment in Klaviyo

Once you have your main list uploaded into Klaviyo, you're ready to build an engaged segment to start sending to. Check out this our on [how to create an engaged segment](https://klaviyo.zendesk.com/hc/en-us/articles/115000200072).

## Upload separate main, engaged, and inactive lists

1. If you're unable to export date added, last open, and last click timestamps from your previous ESP or CRM, you can upload three separate lists based on engagement. In your previous platform, build segments based on the following criteria:
   - ****Main List****
     Everyone on your email list
   - ****Engaged List****Everyone on your email list who has opened or clicked an email at least once in the past 120 days, or was added to your email list in the past 120 days.
   - ****Inactive List****Everyone who has been on a list for more than 120 days, or has not opened or clicked an email in the last 120 days
2. Export these lists as CSVs and upload them to Klaviyo. Remember to only click ****Subscribe to Email Marketing**** in the **Import Review** step if everyone in your list has explicitly consented to receive email marketing from you.
3. If you're a daily sender, send your first week's worth of campaigns to your engaged list. If you're a bi-weekly sender, send your first 2-3 campaigns to this list.

## Upload suppressed contacts to your suppression list

Once you've uploaded these lists, you'll want to upload any contact addresses that have unsubscribed, hard bounced, or marked your emails as spam to your account's [suppression list](https://help.klaviyo.com/hc/en-us/articles/115005078487). This will ensure that you don't accidentally email them and harm your deliverability.

## Outcome

You've now imported your contacts from a previous ESP or CRM.

## Additional resources

- [Formatting dates for CSV files reference](https://help.klaviyo.com/hc/en-us/articles/360039859932)
- [Understanding email deliverability](https://klaviyo.zendesk.com/hc/en-us/articles/115005247008)
- [Troubleshooting list imports](https://help.klaviyo.com/hc/en-us/articles/115005078807)