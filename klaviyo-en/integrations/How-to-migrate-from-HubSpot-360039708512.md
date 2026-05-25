---
id: "360039708512"
title: "How to migrate from HubSpot"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360039708512-How-to-migrate-from-HubSpot"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T10:57:13Z"
language: "en"
---
## You will learn

Learn how to migrate from Hubspot to Klaviyo. While Klaviyo does not have a built-in integration with HubSpot, you can export your data from HubSpot and upload it into Klaviyo.

## Before you begin

This guide will walk you through migrating your data from HubSpot to Klaviyo. As you migrate your HubSpot lists, keep in mind that the main objectives for migrating data are to ensure that all relevant contacts and fields are represented in Klaviyo, and that any opted-out contacts are treated as such in Klaviyo.

Below, we provide a recommended approach that will allow you to upload your HubSpot contacts to Klaviyo and treat various contacts as unsubscribed based on the contact's status in HubSpot. We recommend that you also review [how HubSpot defines these statuses](https://knowledge.hubspot.com/email/what-is-the-marketing-email-confirmation-status-contact-property) so you can verify data quality in HubSpot and ensure that this approach of uploading active and unsubscribed profiles aligns with your intended use of Klaviyo.

This article gives you general guidelines for migrating your data from HubSpot to Klaviyo. Contact [HubSpot support](https://help.hubspot.com/) for the most up-to-date instructions on exporting your HubSpot data.

## Migration strategy

Before migrating your data from HubSpot to Klaviyo, we suggest creating several HubSpot lists:

- Everyone - Active
- All Unsubscribes
- 7 Day - engagement
- 14 Day - engagement
- 30 Day - engagement
- 60 Day - engagement

Each of these lists will be treated differently in Klaviyo

- Everyone - Active: Add this list to your Email List or list of choice
- All Unsubscribes: Add this list to your Klaviyo Suppression List
- 7 Day, 14 Day, 30 Day, 60 Day: These lists will be retained for later use when you will begin warming your account by using these lists to send strategic campaigns

## Checklist

Migrating from HubSpot to Klaviyo requires several key steps:

1. Export active HubSpot contacts into a CSV file
2. Format the CSV file
3. Import the CSV file to a Klaviyo list
4. Export HubSpot unsubscribes
5. Upload unsubscribes to your Klaviyo Suppression List
6. Export 7-day, 14-day, 30-day, and 60-day engagement lists
7. Migrate your HubSpot email templates to Klaviyo
8. Sunset your HubSpot account
9. Send your first Klaviyo campaign

## Export your HubSpot lists

Each HubSpot account is set up uniquely. The following instructions are guidelines for exporting your HubSpot lists. [Contact HubSpot support](https://blog.hubspot.com/customers/hubspot-support-channel-contact) and consult their [documentation](https://help.hubspot.com/) for the most up-to-date export instructions.

These instructions are for both free and paid accounts.

1. From your HubSpot account, navigate to ****Contacts > All contacts****.
   ![Contacts page in Hubspot on All Contacts tab](https://klaviyo.zendesk.com/hc/article_attachments/28720847629083)
2. In the ****Options**** dropdown, choose ****Export view****.
   ![Contacts page in Hubspot on All Contacts tab with Table actions menu open](https://klaviyo.zendesk.com/hc/article_attachments/28720847624475)
3. Choose ****CSV**** as the file format, and select ****All properties on records****.
4. Since HubSpot can also serve as a CRM, you may want to export all associated contact data. Exporting all properties is also the fastest way to export your contacts. You’ll be able to map the export properties later in this process, and reference those fields for segmentation later in Klaviyo.
5. Click ****Export****. The file will be sent to the email address you logged in with.
   ![Export view in Hubspot with Export with orange background](https://klaviyo.zendesk.com/hc/article_attachments/28720892777499)

## Format CSV files

Contacts are imported into Klaviyo in CSV format. Carefully format each CSV file before it is imported into Klaviyo to ensure that your contacts are imported smoothly and accurately.

Open each CSV file. Carefully comb through each list, paying special attention to the column headings:

- Column headings should be in the first row of the CSV file. If HubSpot adds additional rows before the column headings, delete these extra rows.
- Your CSV file must include an "Email" or an "Email Address" header as the first column.
- You may want to include a "First Name" and a "Last Name" column.
- Include any custom profile properties, such as "Gender", that you'd like to upload to Klaviyo.
- Timestamp fields such as "Date Added", "Last Opened", and "Last Clicked" need to be formatted correctly or Klaviyo will not recognize them as timestamp fields. Make sure timestamp data is in one of these formats:
  YYYY-MM-DD HH:MM:SS
  MM/DD/YYYY HH:MM:SS
  MM/DD/YY HH:MM:SS
  MM/DD/YYYY HH:MM
  MM/DD/YY HH:MM
  YYYY-MM-DDTHH:MM:SS

This is an example of how your CSV file should be formatted:

![Example CSV file with fields such as first name and last name](https://klaviyo.zendesk.com/hc/article_attachments/28720892779931)

Review your CSV file carefully, editing/deleting column headings and contact entries as appropriate.

Remember that it is much easier to parse and edit data within a CSV file before it is uploaded into Klaviyo.

For more detailed instructions on formatting CSV files, head to our article on [creating and adding contacts to a new list](https://help.klaviyo.com/hc/en-us/articles/115005078967).

## Import CSV files to a Klaviyo list

After you format your exported data, import it to a list in Klaviyo.

Some Klaviyo flows are triggered by an email address being added to a list. Before you begin uploading contacts to a list, make sure these related flows are turned to draft or manual mode.

1. Log in to your Klaviyo account, click the ****Audience**** dropdown, and select ****Lists & Segments****.
2. Select the list where you would like to add your contacts. For this example, we're going to add subscribers to the Email List since they have already opted in.
3. In the upper right-hand corner of your list, choose ****Import Contact**** from the **Manage List** dropdown.
   ![Klaviyo newsletter list with manage list dropdown open](https://klaviyo.zendesk.com/hc/article_attachments/28720847643675)
4. Drag and drop your CSV file. You will be prompted to review field mapping before Klaviyo begins the import. Click ****Subscribe to Email Marketing**** in the **Email** row to denote that all profiles in this upload have explicitly consented to receive email marketing from you.
5. Carefully review each import field/corresponding Klaviyo field, and modify as appropriate. By default, all identified fields are included in the import. You can omit a field from import by unchecking the box to the right of the field name.
6. Import fields that are not automatically matched to a Klaviyo field are marked "Unmapped." If you try to import an unmapped field, you will receive an error message prompting you to add the field. From the dropdown, select an existing Klaviyo field name or create a custom field by typing a name into the blank entry field. To the right of the field name, select a data type from these options: **String, Boolean, Number, Date, or List,** or **Consent**. If you're unsure of the data type, head to our article on [data types](https://help.klaviyo.com/hc/en-us/articles/115005237648) in Klaviyo. This is a simple example of field mapping for a HubSpot contacts import:
   ![Import review page with all fields mapped and Start Import in upper right](https://klaviyo.zendesk.com/hc/article_attachments/28720892785179)
7. When you're finished, click ****Start Import**** on the upper-right corner of your screen.

For a deeper dive into importing contacts, head to our article on [migrating existing subscribers and unsubscribes into Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115002053752).

## Export HubSpot unsubscribes

It is important to import your HubSpot unsubscribes into your Klaviyo Suppression List to ensure compliance with spam laws and keep your deliverability strong. Suppressed contacts in Klaviyo cannot be sent marketing emails; however, if you use Klaviyo to send transactional emails, suppressed contacts will still receive these.

**Unsubscribed from email** is a default property in HubSpot, so you’ll export this list, format it, and upload it into your Klaviyo Suppressions List.

1. Navigate to ****Contacts > Lists > Create list****.
   ![Hubspot Lists page with Create List in upper right](https://klaviyo.zendesk.com/hc/article_attachments/28720847648027)
2. Name your new list descriptively. For **Filter type**, choose ****Contact-based****. Under **What kind of list are you creating?** choose ****Active list****.
   ![Create a list page in Hubspot with Contact-based list selected](https://klaviyo.zendesk.com/hc/article_attachments/28720892795163)
3. From the list on the left, choose ****Contact properties**** and search for **unsubscribes**. Select ****Unsubscribed from all email****.
   ![Contact properties search bar with Unsu in search](https://klaviyo.zendesk.com/hc/article_attachments/28720847655579)
4. Set ****Unsubscribed from all email > is equal to > True****, and click ****Apply filter****.
   ![Filter is unsubscribed from all email is equal to true](https://klaviyo.zendesk.com/hc/article_attachments/28720847653531)
5. Save the list.
6. Navigate to ****Lists**** and find your **Unsubscribe** list. Hover over the list options and select the ****More**** dropdown. Choose ****Export****.
   ![Unsubscribes list in Hubspot lists page with More dropdown open](https://klaviyo.zendesk.com/hc/article_attachments/28720892812059)
7. You only need to upload email addresses to your Klaviyo Suppressions list. In the search field, type **Email**. Select the ****Email**** field and click ****Next****. Follow the wizard to export your unsubscribes in the CSV format.
8. Format the CSV download so that it contains a single column of email addresses. Below is an example of how your suppression list CSV file should be formatted:
   ![CSV with example emails](https://klaviyo.zendesk.com/hc/article_attachments/28720892807323)
9. Now you're ready to upload your unsubscribes into Klaviyo.

## Upload unsubscribes to Klaviyo

1. Navigate to the ****Profiles**** tab in your Klaviyo account (under ****Audience****), and click ****Suppressed Profiles**** on the upper right.
2. Select ****Upload File****. Click ****Choose File**** and select the CSV containing your HubSpot unsubscribes.
3. Click ****Upload Suppressions****.
4. Your Klaviyo suppression List will now reflect your import.

## Export 7-Day, 14-Day, 30-Day, and 60-Day engagement lists

1. Navigate to ****Contacts > Lists > Create list****in Hubspot.
   ![Lists page in Hubspot with Create List in upper right](https://klaviyo.zendesk.com/hc/article_attachments/28720892804251)
2. Name your new list descriptively (e.g., 7-day engagement). For **Filter type**, choose ****Contact properties****. Under **What kind of list are you creating?** choose ****Active list****.
3. On the next page, select ****Last marketing email open date****.
   ![Contact properties search bar with open in search](https://klaviyo.zendesk.com/hc/article_attachments/28720892814235)
4. Click ****is after****. You’ll need to calculate your desired date. For example, if today is June 16, 2021, then 7 days prior is June 23, 2021.
   ![Filter last marketing email open date is after 06/23/2021](https://klaviyo.zendesk.com/hc/article_attachments/28720847682459)
5. Apply the filter, and then save your list.
6. Follow previous instructions to export the list.
7. Repeat these steps to create 14-day engagement, 30-day engagement, and 60-day engagement lists. You'll use these lists later to send strategic campaigns.

## Migrate email templates from HubSpot to Klaviyo

Klaviyo has an intuitive drag-and-drop template builder that you can use to recreate your HubSpot email templates. We highly recommend using this method to rebuild your templates because it will ensure that they are mobile-optimized, responsive, and easy-to-edit moving forward.

Check out [our guide to using Klaviyo's template editor](https://klaviyo.zendesk.com/hc/en-us/articles/4407911841435).

If you don't have time to recreate your HubSpot templates using Klaviyo's template builder, it is possible to export your email templates from HubSpot in raw HTML and then upload the HTML into Klaviyo. If you must import raw HTML templates, you can [import a custom HTML template](https://help.klaviyo.com/hc/en-us/articles/115005254068)

## Sunset your HubSpot account

After you've moved all your data over to Klaviyo, there are three key steps you can take to ensure that you no longer need your HubSpot account:

1. Check that your sign-up forms and list growth tools point to Klaviyo, not HubSpot
2. Recreate your HubSpot workflows as Klaviyo flows
3. Discontinue use of HubSpot

### Sign-up forms and list growth tools

Recreate any HubSpot sign-up forms in Klaviyo so that your list continues to grow in Klaviyo rather than in HubSpot. You can:

1. Use the Klaviyo [sign-up form builder](https://help.klaviyo.com/hc/en-us/articles/360026474752) to re-create your forms from scratch
2. Use a third-party list growth tool that integrates with Klaviyo
3. Integrate your custom forms through your ecommerce platform

If you are using third-party list growth tools, make sure that these sync to Klaviyo. Klaviyo integrates with a number of tools for list growth and landing pages.

Please note that all Klaviyo lists are double opt-in by default. To change a list to single opt-in, head to that section of our [guide to the double opt-in process](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108).

If you’re using a custom-coded form, you should ensure your custom form syncs new subscribers directly to your ecommerce platform and that your ecommerce store is integrated with your Klaviyo account.

After switching or syncing all your sign-up forms to Klaviyo, wait a few days and watch your lists in HubSpot. If you notice subscribers are still being added to these lists, there's probably at least one form that still needs to be swapped out.

Next, you'll want to turn off your HubSpot sign-up forms. Contact [HubSpot support](https://help.hubspot.com/) for information on how to turn off your HubSpot sign-up forms.

### Email automations

Klaviyo refers to automated workflows as "flows" which allow for more advanced and targeted sequences. It is important to recreate these in Klaviyo so that you don't need to continue to use HubSpot to send triggered emails.

As you move from HubSpot, it may be a good time to refresh and update your automated messaging. We recommend that you turn on your welcome series and abandoned cart flows as soon as possible. A welcome series is particularly important to engage new subscribers, and abandoned cart flows have the highest ROI of any other type of flow.

Once your Klaviyo flows are live, you'll want to turn off all of your workflows in HubSpot to ensure that you're not double-emailing people. [Contact HubSpot support](https://help.hubspot.com/) for more information about turning off your HubSpot workflows.

### Discontinue HubSpot use

Once you’ve pointed all of your list growth tools to your Klaviyo account, paused your HubSpot workflows, and turned your Klaviyo flows live, you can discontinue using HubSpot. Before you close your HubSpot account, double-check that everything is working as expected. Enter a test email into your sign-up form and other list growth tools, abandon a cart, and sign up for your email list to trigger a welcome series. Go to the ****Profiles**** tab (under ****Audience****) in your Klaviyo account to make sure that the information in the profile reflects all of the correct communication. If the list you sign up to is double opt-in, confirm your email first.

After you've taken these steps and are fully migrated to Klaviyo, you can close your HubSpot account.

## Send your first campaign with Klaviyo

Once your Klaviyo account is integrated with your store and all of your data is ported over from HubSpot, you can send your first campaign with Klaviyo.

For more information, check out out [Getting started with Klaviyo course](https://academy.klaviyo.com/getting-started-with-klaviyo).

## Next steps with Klaviyo

### Build an excellent sender reputation with Klaviyo

After you begin sending to your most engaged segment of customers, you can gradually send to more of your customers. This gradual sending process enhances your sender reputation and is known as warming your IP address.

Head over to our articles on deliverability to read more about [warming your sending infrastructure](https://help.klaviyo.com/hc/en-us/articles/360025945671).

### Use advanced segmentation to reach your customers

After you've engaged your most interested subscribers for the first month or so, begin reaching out to the rest of your customer base. You can create additional segments to ensure you're contacting each corner of your customer base.

- Duplicate your **Engaged (3 Months)** segment and tweak the settings, decreasing the timeframe from 3 months to 30 days
- Use historical HubSpot data, such as your 7-day, 14-day, 30-day, and 60-day engagement lists, to refine and build out your segments

For a deeper dive into segmenting and approaching the rest of your customer base, read about [creating customer engagement tiers](https://help.klaviyo.com/hc/en-us/articles/360000407272).

If you have questions about transitioning from HubSpot or getting started with Klaviyo, please [reach out to our Support team](https://help.klaviyo.com/hc/en-us/articles/115001002272).

## Outcome

You've now migrated from Hubspot to Klaviyo and have learned best practices for migrating email providers.

## Additional resources

- [How to troubleshoot list imports](https://help.klaviyo.com/hc/en-us/articles/115005078807)
- [Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)
- [Profile properties reference](https://help.klaviyo.com/hc/en-us/articles/115005074627)