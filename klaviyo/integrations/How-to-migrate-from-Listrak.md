---
id: 360034550591
title: "How to migrate from Listrak"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360034550591-How-to-migrate-from-Listrak"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T10:57:41Z"
language: en
---

## You will learn

Learn how to migrate from Listrak to Klaviyo. While Klaviyo does not have a built-in integration with Listrak, you can export your data from Listrak and upload it into Klaviyo. Listrak contacts and related data are exported from Listrak in CSV format. CSV files can be easily formatted to ensure successful import to a Klaviyo list. While this is not a complicated process, exporting each individual Listrak list may be a bit tedious depending on your volume of data. With consistency and thoroughness, your migration will be successful.

## Before you begin

This guide will walk you through migrating your data from Listrak to Klaviyo. As you migrate your Listrak lists, keep in mind that the main objectives for migrating data are to ensure that all relevant contacts and fields are represented in Klaviyo, and that any opted-out contacts are treated as such in Klaviyo.

Below we provide a recommended approach that will allow you to upload your Listrak contacts to Klaviyo and treat various contacts as unsubscribed based on the contact's status in Listrak. We recommend that you also review [how Listrak defines these statuses](https://help.listrak.com/en/articles/1505969-view-subscribed-or-unsubscribed-contacts) so you can ensure data quality on the Listrak side and also ensure that this approach of uploading contacts aligns with your intended use of Klaviyo.

This guide gives you general guidelines for migrating your data from Listrak to Klaviyo. Contact [Listrak Support](https://www.listrak.com/company/contact) for the most up-to-date instructions on exporting your Listrak data.

## Checklist

Migrating from Listrak to Klaviyo requires several key steps:

1. Export Listrak Subscribed Contacts list
2. Format CSV files
3. Import CSV files to a list in Klaviyo
4. Export Listrak Suppression List
5. Import unsubscribes to your Klaviyo suppression list
6. Migrate your email templates from Listrak to Klaviyo
7. Sunset your Listrak account

## Export your Listrak subscribed contacts list

Each Listrak account is set up uniquely. The following instructions are guidelines for exporting your Listrak data. [Contact Listrak support](https://www.listrak.com/company/contact) and consult their [documentation](https://help.listrak.com/en/) for the most up-to-date export instructions.

Follow these steps to download each of your Listrak lists.

1. From your Listrak **Home Menu**, navigate to ****Contacts****.
2. Click ****Subscribed Contacts >**** ****Export List Wizard****.
   ![Contacts menu in Listrak with Export List Wizard in white](https://klaviyo.zendesk.com/hc/article_attachments/28716352835867)
3. Choose ****Plain Text .CSV**** as your export format, and click ****Next****.
   ![Select the export format with plain text .CSV selected](https://klaviyo.zendesk.com/hc/article_attachments/28716352838555)
4. Now choose any segmentation fields and system fields to include with your CSV export. ****Email****, ****Subscribe Date****, and ****Method**** are automatically included with each export.
5. When you're finished, click ****Next****.
   ![Select fields to export page with Next with green background](https://klaviyo.zendesk.com/hc/article_attachments/28716329841435)
6. Choose a delivery method, and then click ****Next****. Choosing ****Email**** as your delivery method is best if you are exporting a large list (over 500K) because uploading a large amount of data into a browser may take some time.
   - If you chose the ****Web**** delivery method, click ****Finish****. Your results will display in your browser.If you chose the ****Email**** delivery method, set email options by selecting recipients. The default email displayed is the email address tied to your Listrak account. Enable the ****Attach to Email**** checkbox to download the file as an email attachment. Then, click ****Finish****.
   - You'll be notified by email when your CSV file is ready for download.

You can view [instructions on exporting your entire Listrak list from Listrak](https://help.listrak.com/en/articles/1509286).

## Format CSV files

You'll need to format each CSV file before importing it into Klaviyo. To do that, open the CSV file and comb through the list, paying special attention to the column headings:

- Column headings should be in the first row of the CSV file. If Listrak adds additional rows before the column headings, delete these extra rows.
- Your CSV file must include an "Email" or an "Email Address" column.
- You may want to include a "First Name" and "Last Name" column.
- Include any custom profile properties such as "Gender" that you'd like to upload to Klaviyo.
- Listrak exports a **Method** field, indicating the method of subscription. This field can be left intact on the CSV upload file and later mapped to Klaviyo's **Source** field when you upload the CSV to Klaviyo.
- Timestamp fields such as "date added," "last opened," and "last clicked" need to be specifically formatted or Klaviyo will not recognize them as timestamp fields. Make sure timestamp data is formatted in one of these formats:
  YYYY-MM-DD HH:MM:SS
  MM/DD/YYYY HH:MM:SS
  MM/DD/YY HH:MM:SS
  MM/DD/YYYY HH:MM
  MM/DD/YY HH:MM
  YYYY-MM-DDTHH:MM:SS

Below is an example of how your CSV file should be formatted.

![Example CSV with most data blurred out](https://klaviyo.zendesk.com/hc/article_attachments/28716352844699)

Review your CSV file carefully, editing and deleting column headings and contact entries as appropriate.

Remember, it's much easier to parse and edit data within a CSV file before it is uploaded into Klaviyo.

For more detailed instructions on formatting CSV files, head to our article on [creating and adding contacts to a new list](https://klaviyo.zendesk.com/hc/en-us/articles/115005078967).

## Import CSV files to a Klaviyo list

After you've formatted your exported data, you can import it to a list in Klaviyo. Some Klaviyo flows are triggered by an email address being added to a list. Before you begin uploading contacts to a list, make sure these related flows are turned to draft or manual mode.

1. Log in to your Klaviyo account, click the ****Audience**** dropdown, and select ****Lists & Segments****.
2. Select the list where you would like to add your contacts. For this example, we're going to add subscribers to the Newsletter list.
3. On the upper-right hand corner of your list, choose ****Import Contact**** from the **Manage List** dropdown.
   ![Newsletter list in Klaviyo with Manage List dropdown open](https://klaviyo.zendesk.com/hc/article_attachments/28716352847003)
4. Drag and drop your CSV file. You will be prompted to review field mapping before Klaviyo begins the import. Click ****Subscribe to Email Marketing**** in the **Email** row to denote that all profiles in this upload have explicitly consented to receive email marketing from you.
5. Carefully review each import field/corresponding Klaviyo field, and modify as appropriate. By default, all identified fields are included in the import. You can omit a field from import by unchecking the box to the right of the field name.
   ![List import page with fully mapped fields and Start Import in upper right](https://klaviyo.zendesk.com/hc/article_attachments/28716329847579)
6. By default, Listrak includes a **Method** column, denoting the method of subscription. We recommend mapping this field into Klaviyo's **Source** field.
7. Column names that have no corresponding field name in your Klaviyo account are marked "Unmapped." If you try to import an unmapped field, you will receive an error message prompting you to map the field. By default, all identified fields are included in the import. You can omit a field from import by unchecking the box to the right of the field name. From the dropdown, select an existing field name or create a custom field by typing a name into the blank entry field. To the right of the field name, select a data type from these options:****String****, ****Boolean****, ****Numeric****, ****Date****,****List****, or ****Consent****. If you're unsure of the data type, head to our article on [data types](https://klaviyo.zendesk.com/hc/en-us/articles/115005237648) in Klaviyo. Below is an example of field mapping for a Listrak contacts import.
   ![List import page with unmapped field highlighted in red](https://klaviyo.zendesk.com/hc/article_attachments/28716352851995)
8. When you're finished, click ****Start Import**** on the upper-right corner of your screen.

For a deeper dive into importing contacts, head to our article on [migrating existing subscribers and unsubscribes into Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115002053752).

## Export Listrak unsubscribes

It is important to add your Listrak unsubscribes to Klaviyo's suppression list to ensure compliance with spam laws and keep your deliverability high. These are general guidelines for exporting your Listrak unsubscribe list and suppression list. For the most up-to-date instructions reach out to [Listrak support](https://www.listrak.com/company/contact) and review their [documentation.](https://help.listrak.com/en/)

1. Go to your Listrak ****Home menu > Contacts****.
2. Go to ****View**** and then select ****Unsubscribed Contacts > Export List Wizard****.
3. Choose ****Plain Text .CSV**** as your export format, and click ****Next****.
4. Follow the rest of the Wizard instructions for downloading your unsubscribes.

In addition to exporting your Unsubscribed Contacts, you may also want to export your Listrak Suppression list. Navigate to your Listrak contacts section and select the ****Suppression List Name Here**** list. Follow the steps above to export this list in CSV format.

![List of lists in Listrak including suppression list](https://klaviyo.zendesk.com/hc/article_attachments/28716352854555)

Format the suppression list so that it contains a single column of email addresses.

## Load historic unsubscribes into Klaviyo

1. Navigate to the ****Profiles**** tab in your Klaviyo account (found under ****Audience****) and click ****Suppressed Profiles**** on the upper right.
2. Select ****Upload File****.
3. Click ****Choose File**** to select the CSV file containing your Listrak suppressions. Then, click ****Upload Suppressions****.
   ![Upload Suppressions File popup in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28716352856859)
4. Your Klaviyo suppression list will now reflect your import.

## Migrate email templates from Listrak to Klaviyo

Klaviyo offers an intuitive drag-and-drop template builder that you can use to recreate your Listrak email templates. We highly recommend using this method to rebuild your templates because it will ensure that they are mobile-optimized, responsive, and easy-to-edit moving forward.

Check out [our guide to using Klaviyo's template editor](https://klaviyo.zendesk.com/hc/en-us/articles/4407911841435).

If you don't have time to recreate your Listrak templates, it is possible to export your email templates from Listrak in raw HTML and then upload the updated raw HTML into Klaviyo. If you choose to import raw HTML templates, you can reference our article on [importing a custom HTML template](https://klaviyo.zendesk.com/hc/en-us/articles/115005254068).

## Sunset your Listrak account

After you've moved all your data over to Klaviyo, there are three key steps you can take to ensure that you no longer need your Listrak account:

1. Ensure that your sign-up forms and list growth tools point to Klaviyo, not Listrak
2. Recreate your Listrak workflows as Klaviyo flows
3. Discontinue use of Listrak

### Sign-up forms and list growth tools

Recreate any Listrak sign-up forms in Klaviyo so that your list continues to grow in Klaviyo, rather than in Listrak. You can:

1. Use the Klaviyo [sign-up form builder](https://help.klaviyo.com/hc/en-us/articles/360026474752) to re-create your forms from scratch
2. Use a third-party list growth tool that integrates with Klaviyo
3. Integrate your custom form through your ecommerce platform

If you are using third-party list growth tools, make sure that these sync to Klaviyo. Klaviyo integrates with a number of tools for list growth and landing pages. [Check out our app marketplace](https://marketplace.klaviyo.com/en-us/) to find the tool that you're using. If you don't see it listed, consider using Klaviyo's native Sign-up Form Builder to create your forms, or try switching to a different third-party tool.

Please note that all Klaviyo lists are double opt-in by default. To change a list to single opt-in, head to that section of our [guide to the double opt-in process](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108).

If you’re using a custom-coded form, ensure your contacts sync to Klaviyo by having your custom form sync new subscribers directly to your ecommerce platform, and make sure your ecommerce platform is integrated with your Klaviyo account.

After switching or syncing all your sign-up forms to Klaviyo, wait a few days and watch your lists in Listrak. If you notice subscribers are still being added to these lists, there's probably at least one form that still needs to be swapped out.

Next, you'll want to turn off your Listrak sign-up forms. [Contact Listrak support](https://www.listrak.com/contact) for information on how to turn off your Listrak sign-up forms.

### Flows

Klaviyo refers to automated workflows as "flows," which allow for more advanced and targeted sequences. It is important to recreate these in Klaviyo so that you don't need to continue to use Listrak to send triggered emails.

As you move from Listrak, it may be a good time to refresh and update your automated messaging. We recommend that you turn on your welcome series and abandoned cart flows as soon as possible. A welcome series is particularly important to engage new subscribers, and abandoned cart flows have the highest ROI of any other type of flow.

Once your Klaviyo flows are live, you'll want to turn off all of your workflows in Listrak to ensure that you're not double-emailing people. [Contact Listrak support](https://www.listrak.com/contact) for more information about turning off your Listrak workflows.

### Discontinue Listrak use

Once you’ve pointed all of your list growth tools to your Klaviyo account, paused your Listrak workflows, and turned your Klaviyo flows live, you can discontinue using Listrak. Before you close your Listrak account, double-check that everything is working as expected. Enter a test email into your sign-up form and other list growth tools, abandon a cart, and sign up for your newsletter to trigger a welcome series. Go to the ****Profiles**** tab in your Klaviyo account (found under ****Audience****) to make sure that the information in the profile reflects all of the correct communication. If the list you sign up to is double opt-in, be sure to confirm your email first.

After you've taken these steps and are fully migrated to Klaviyo, you can close your Listrak account.

## Next steps with Klaviyo

Once your Klaviyo account is integrated with your store and all of your data is ported over from Listrak, you can work toward your first Klaviyo send by following our [Getting started with Klaviyo course](https://academy.klaviyo.com/getting-started-with-klaviyo).

If you have questions about transitioning from Listrak or getting started with Klaviyo, please [reach out to our Support Team](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272).

## Outcome

You've now migrated from Listrak to Klaviyo and have learned best practices for migrating email providers.

## Additional resources

- [How to troubleshoot list imports](https://help.klaviyo.com/hc/en-us/articles/115005078807)
- [Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)
- [Profile properties reference](https://help.klaviyo.com/hc/en-us/articles/115005074627)