---
id: "360035428731"
title: "How to upload a list of SMS contacts"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360035428731-How-to-upload-a-list-of-SMS-contacts"
section: "Import SMS contacts"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:46Z"
language: "en"
---
To import consent, you must:

- Be an Owner or Admin
- Have set up SMS

Find out how to add and remove SMS transactional or marketing consent in Klaviyo. Importing your SMS subscribers is an essential part of migrating providers or simply consolidating your data.

## Before you begin

### General requirements to import SMS consent

To import a list of phone number contacts with consent, you should:

1. [Set up SMS](https://help.klaviyo.com/hc/en-us/articles/4404274419355) and have an SMS sending number for each country that you are importing.
   - Note: you can only import consent for countries [where Klaviyo SMS is available](https://help.klaviyo.com/hc/en-us/articles/4402914866843).
2. Turn off any welcome flows (those triggered by the **Consented to receive SMS** metric or the list you’re importing to).
   - Also, wait at least 2 hours after importing before you turn your flow live again.

****Why do I need to set up SMS first and have a sending number?****

Klaviyo cannot add SMS consent if:

- SMS isn’t set up in Klaviyo
- You’re trying to add consent for a country where SMS isn’t available
- Don’t have an SMS sending number for a country.

The profiles are imported with phone numbers, but they wouldn’t have consent for SMS.

To check your SMS setup and sending numbers, navigate to ****Settings > SMS****.

****Why should I turn off welcome flows?****

If you don’t, every new contact from the CSV you uploaded will be added to any welcome flow. Thus, you should set your welcome flows to manual mode before importing. Welcome flows include those triggered by either:

- The **Consented to receive SMS** metric (which is the best option for any SMS welcome series)
- The list you’re uploading to.

You should also wait at least 2 hours after the import finishes to turn these flows live again.

## Obtain your list of contacts

Depending on your SMS provider, you may need to build in time to get a list of your SMS subscribers.

At minimum, you need:

- Phone number
- Opt-in status (i.e., whether they are currently subscribed or not)

Additionally, you may want to include aspects like name, email, consent timestamp, etc.

### Attentive

Attentive requires that you reach out to your account representative to receive an export of your SMS subscribers as a CSV file. It is not currently possible to export the file yourself. When migrating to Klaviyo, plan for turnaround time for Attentive to complete this request.

If the CSV file you receive contains contacts who have opted out of SMS messaging, as indicated in the **opt\_out** column of your export:

1. Add a column labeled "SMS Marketing Consent."
2. Mark any contacts that have opted out as "Unsubscribed" in this column.

### Emotive

Emotive does not allow you to export a list of all SMS subscribers directly from your account. You must contact them to get this list.

### Postscript

Postscript allows you to export a list of all SMS subscribers directly from your account into a CSV file. This list simplifies the import process into Klaviyo.

For Postscript specifically, consider exporting information like:

- subscriber\_created\_at\_utc (this is the SMS marketing consent timestamp)
- Customer\_id
- Last\_keyword\_subscribed\_to
- Automation\_and\_campaign\_texts\_sent\_count

To learn how to export this segment in Postscript, consult [their help doc on exporting subscriber data](https://help.postscript.io/hc/en-us/articles/1260804630310-). You will need to export each segment separately.

### Retention Rocket

Retention Rocket requires that you contact your account representative to receive an export of your SMS subscribers as a CSV file. It is not currently possible to export this file yourself. When migrating to Klaviyo, plan for turnaround time for your Retention Rocket representative to complete this request.

### Yotpo / SMSBump

Use Klaviyo's [Yotpo Email & SMS Migration integration](https://help.klaviyo.com/hc/en-us/articles/39598076123547) to easily bring both SMS and email subscribers into Klaviyo.

## Prepare your CSV for importing

For an example CSV, see this [template](https://docs.google.com/spreadsheets/d/1cqJb4hH4Kbv0xw_yf14vKS4CyKlzDNY7toG_nqUrhPI/edit?gid=0#gid=0).

### Include a phone number as the first or second column

Klaviyo uses either email or phone number as a profile’s unique identifier.

When importing:

- Use email as the first column if you have an email address for each person
- Otherwise, use phone number as the first column

### Indicate the SMS subscriber’s country

You need to indicate the country for each person you’re importing either by:

- Adding the country code before the phone number
- Including a column labeled “Country”

|  |  |
| --- | --- |
| ****Example with country code**** | ****Example with country column**** |
| ![Indicating the country via a country code](https://klaviyo.zendesk.com/hc/article_attachments/28711677302683) | ![Example with country column.png](https://klaviyo.zendesk.com/hc/article_attachments/28711698750619) |

Watch the video or check out this article for [instructions on indicating the SMS subscriber’s country](https://help.klaviyo.com/hc/en-us/articles/5306587861531).


![](https://fast.wistia.com/embed/medias/ld30gq77eh/swatch)

### Indicate if consent is for SMS marketing or transactional

Say your CSV has a mix of marketing- and transactional-only profiles.

You can use 2 columns to indicate the type (transactional or marketing) of someone’s SMS consent. Label the columns:

- **SMS Marketing Consent**
  - Marketing consent allows you to send any type of SMS: both promotional (product announcement, abandonment reminder, etc) and transactional messages.
  - This is required if you want to import profiles with only SMS marketing consent.
- **SMS Transactional Consent**
  - SMS transactional consent means you can only send messages marked as transactional in Klaviyo, like post-purchase flow messages.
  - This column is only needed if you have transactional-only profiles, as you can send transactional messages to anyone who consented to SMS marketing.

### Add consent status (subscribe, unsubscribed, never subscribed)

Including the consent status is key if your CSV includes a mix of either:

- Subscribed and unsubscribed subscribers
- Marketing- and transactional-only subscribers

There are 3 consent statuses available:

- ****Subscribe****
  Person is opted in to receive messages.
- ****Unsubscribed**** Person used to be subscribed but has since opted out. You cannot send messages if they are unsubscribed for that channel (e.g., you cannot send an SMS to someone who’s unsubscribed, but you may be able to send an email).
- ****Never subscribed**** Person never consented to receiving messages. This is also the default value if a cell in a consent column is blank. You cannot send mobile (SMS, push, etc.) messages to people marked as never subscribed; however, you can send emails and these are considered active profiles.

Klaviyo will not apply SMS marketing consent if someone is marked as either **unsubscribed** or **never subscribed**. However, if they are marked as subscribed for marketing consent, they are always marked as subscribed for transactional consent.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ****SMS marketing consent**** | ****SMS transactional consent**** | ****Is consent added to the profile?**** |
| Profile A | Subscribe | Subscribe | Yes, they are consented to both SMS marketing and transactional consent. |
| Profile B | Subscribe | Never subscribed | Yes, but only for SMS marketing consent. The profile will show “never subscribed" for transactional consent. |
| Profile C | Never subscribed | Subscribe | Yes, but the profile is only consented to SMS transactional consent. |
| Profile D | Unsubscribed | Never subscribed | No, and the profile is marked "unsubscribed" for SMS marketing and "never subscribed” for SMS transactional. |

The way SMS providers export this information varies, so you may have to reformat the spreadsheet you received from your previous SMS provider to indicate the consent status.

### Optional: add consent timestamp

While optional, the timestamp is usually good to include if it’s available. To do so, check that:

- The timestamp is in an [accepted date/time format](https://developers.klaviyo.com/en/docs/acceptable_date_and_timestamp_formats_for_profile_and_event_properties).
- The column is labeled either:
  - **SMS Marketing Timestamp**
  - **SMS Transactional Timestamp** (if also importing transactional consent)

If you choose not to include the timestamp, you will need to check a box to confirm that all profiles are currently opted into SMS.

Adding the consent timestamp is not recommended in certain cases. Mostly, this occurs if you try to re-upload consent for a profile and the opt-out date is more recent than the consent timestamp. In this case, SMS consent won't be re-added to the profile.

### Recommended information

Some information is "recommended" because it's helpful, but not required to add SMS consent. There are also columns you may think are helpful, but could cause errors in the import process.

See the table below for details of other information you may want to (or not want to) include.

|  |  |
| --- | --- |
| ****Do include**** | ****Don't include**** |
| Email address (if included, this should be the first column in the CSV) | "Subscribed to SMS" column |
| First name | A “consent” column to indicate whether someone is subscribed to SMS marketing, SMS transactional, email, etc. |
| Last name |  |

## Import a list of phone numbers with SMS consent

1. Navigate to ****Audience > Lists & segments****.
2. Select the list you want to add your contacts to (e.g., SMS Subscribers).
3. Open the ****Manage List**** dropdown in the upper right.
4. Choose ****Import contacts**** from the dropdown.
   - Note that you must be an Owner or Admin to see this option.
     ![](https://klaviyo.zendesk.com/hc/article_attachments/34691454053147)
5. Click ****Upload**** and select your CSV file of SMS subscribers.
6. Click ****Next****.
7. Map each column from your CSV to an appropriate property in Klaviyo, then click ****Next****.
8. If your CSV includes columns indicating the type of consent or include the consent timestamp, the import will add the consent accordingly.
   - Example: if you include an **SMS Transactional Consent** column (but not one for marketing consent).
     - Profiles marked as “Subscribe” are imported with only SMS transactional consent.
     - All other profiles (those marked as “Unsubscribed” or “Never subscribed”) are imported without consent.
9. If you don't have a consent timestamp or a column indicating consent (e.g., **SMS Marketing Consent**), you’ll see the following:
   - Under **Did these contacts subscribe to messaging**, select ****Yes**** to add consent.
     ![](https://klaviyo.zendesk.com/hc/article_attachments/34691454056859)
   - Check the boxes for the types of consent to apply: ****Email****, ****SMS****, or both.
     ![](https://klaviyo.zendesk.com/hc/article_attachments/34691454061083)
   - Choose the type of consent to apply. The option you pick depends on the consent types in your CSV:
     - If every profile is consented only to SMS transactional, choose ****Only transactional messages****.
     - If every profile should be consented to both SMS marketing and transactional, choose ****Marketing and transactional messages****.
     - To import only SMS marketing, you must format your CSV so that it includes a column labeled **SMS Marketing consent**, then re-upload the CSV.
10. When ready to proceed, click ****Import****.

The import process can take up to a couple of hours to complete.

Once all the numbers are imported, Klaviyo will either create a new profile or associate the data to an existing profile. For instance, if you import a phone-number-only CSV, Klaviyo will look for profiles with the same phone number, update that profile's SMS consent status, and include any other profile properties attributed to that contact.

If the phone number provided is invalid, the row will be skipped and the profile will not be imported, even if a valid e-mail address is included in a different column.

## Bulk remove SMS consent

If you want to remove consent for profiles, you can use essentially the same import process.

The only differences are that you must:

- Have a column for **SMS Marketing Consent** or **SMS Transactional Consent** (depending on the type of consent you want to remove).
- Add “Unsubscribed” for each profile within that column.
  - Note that you cannot reset profiles in bulk to “Never Subscribed.”

## Additional resources

- [Indicate the country for an SMS CSV](https://help.klaviyo.com/hc/en-us/articles/5306587861531)
- [Remove opted-out SMS profiles from CSVs](https://help.klaviyo.com/hc/en-us/articles/5302764979611)
- [Bulk unsubscribe SMS contacts](https://help.klaviyo.com/hc/en-us/articles/5227452906523)