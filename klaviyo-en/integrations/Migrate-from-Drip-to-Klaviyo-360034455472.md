---
id: "360034455472"
title: "Migrate from Drip to Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360034455472-Migrate-from-Drip-to-Klaviyo"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:51Z"
language: "en"
---
## Overview

This guide will walk you through migrating your data from Drip to Klaviyo. While Klaviyo does not have a built-in integration with Drip, you can export your data from Drip and upload it into Klaviyo.

Migrate your Drip profiles by creating and exporting several Drip segments of people. First, you'll create a Drip segment of people who have subscribed to email marketing. Then you'll export those profiles to be uploaded into your Klaviyo Newsletter (opt-in) list. You'll also create a Drip segment of people who have unsubscribed to email marketing and add those profiles to your Klaviyo Suppressed Profiles list.

In addition to migrating your Drip profiles, you'll also need to move your Drip email templates into Klaviyo. When all your information is migrated to Klaviyo, you can begin sunsetting your Drip account.

This guide will walk you through migrating your data from Drip to Klaviyo. As you migrate your Drip lists, keep in mind that the main objectives for migrating data are to ensure that all relevant contacts and fields are represented in Klaviyo, and that any opted-out contacts are treated as such in Klaviyo. Below we provide a recommended approach that will allow you to upload your Drip contacts to Klaviyo and treat various contacts as unsubscribed based on the contact's status in Drip. We recommend that you also review [how Drip defines these statuses](https://www.drip.com/learn/docs/manual/people) so you can verify data quality in Bronto and ensure that this approach of uploading active, unsubscribes, bounces, and suppressions aligns with your intended use of Klaviyo.

This guide gives you general guidelines for migrating your data from Drip to Klaviyo. Contact [Drip Support](https://www.drip.com/contact) for the most up-to-date instructions on exporting your Drip data.

## Checklist

Use this checklist as a guide to migrating your Drip data into Klaviyo:

1. Create a Drip segment of active people who have subscribed to email marketing. Export this list as a CSV and format it appropriately.
2. Upload this CSV to a list in Klaviyo.
3. Create a Drip segment of active people who have unsubscribed. Export this list as a CSV and format it appropriately.
4. Upload this CSV of unsubscribes to your Klaviyo Suppression List.
5. Migrate your email templates from Drip to Klaviyo.
6. Sunset your Drip account.

## Export Your Drip Active Email Subscribers People List

Since Drip's active people grouping does not directly correlate with engaged Klaviyo profiles, you'll need to create a Drip segment of active people who have subscribed to email marketing. Export that segment as a CSV so you can format it for upload to a Klavyio list.

 In your Drip account, navigate to the ****People**** section and click the ****Active**** tab.

![Drip1.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630861211)

Click the dropdown and select ****people subscribed to email marketing****. This will create a segment of all active people who are opted-in and able to receive email communications.

![Drip_Segment1.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630892955)

Click ****Actions**** and choose ****Export to CSV****. Then, click ****OK****. Drip will email the CSV file to the address listed on your ****Drip Account****, under ****General Info****.

These segmentation fields will automatically be included in your Drip CSV export file:

- Token
- Email address
- Time zone
- Status
- Created at date
- Confirmed at date
- Tags
- Custom fields
- Campaigns
- Referrer
- Landing URL
- IP address
- Lead score
- Lifetime value
- User ID

You can also view instructions on exporting your active list on the [Drip Help Center](https://www.drip.com/learn/docs/manual/people/active).

## Format the CSV for Import

You'll need to format each CSV that you import into Klaviyo. To do this, open the CSV file and comb through the list, paying special attention to the column headings:

- Column headings should be in the first row of the CSV file. If Drip adds additional rows before the column headings, delete these extra rows.
- Your CSV must include an "Email" or an "Email Address" column.
- You may want to include a "First Name" and "Last Name" column.
- Include any custom profile properties such as "Gender" that you'd like to upload to Klaviyo.
- Timestamp fields such as "date added," "last opened," and "last clicked" need to be specifically formatted or Klaviyo will not recognize them as timestamp fields. Make sure timestamp data is formatted in one of these formats:

  `YYYY-MM-DD HH:MM:SS`

  `MM/DD/YYYY HH:MM:SS`

  `MM/DD/YY HH:MM:SS`

  `MM/DD/YYYY HH:MM`

  `MM/DD/YY HH:SS`

  `YYYY-MM-DDTHH:MM:SS`

Below is an example of how your CSV file should be formatted.
 ![Drip_CSV_Formatted.png](https://klaviyo.zendesk.com/hc/article_attachments/28723625578907)

Review your CSV carefully, editing and deleting column headings and contact entries as appropriate.

For more detailed instructions on formatting CSV files, head to our article on [Creating and Adding Contacts to a New List](https://klaviyo.zendesk.com/hc/en-us/articles/115005078967).

## Import Your CSVs into Klaviyo

After you've formatted your CSV, you can import it as a list in Klaviyo.

Some Klaviyo flows are triggered by an email address being added to a list, like a welcome series. Before you begin uploading contacts to a list, make sure these related flows are turned to draft or manual mode.

In Klaviyo, navigate to the ****Lists & Segments**** tab. Select the list you would like to add your contacts to. For simplicity, we recommend adding subscribers to your Newsletter list, but you can add your opt-in email addresses to any list.

![Bronto12.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723659154331)

On the upper right-hand corner of your list, choose ****Import Contact**** from the **Manage List** dropdown.
 ![Import_Contacts_blurred.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723630868763)

Drag and drop your CSV. You will be prompted to review field mapping before Klaviyo begins the import. Carefully review each import field, corresponding to a Klaviyo field, and modify as appropriate. By default, all identified fields are included in the import. You can omit a field from import by unchecking the box to the right of the field name.

![Omit_Import_Field.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723630875163)

Import fields that are not automatically matched to a Klaviyo field are marked **Unmapped**. If you try to import an unmapped field, Klaviyo will give you an error message and prompt you to map the field. In the dropdown of each **Unmapped** field, select an existing Klaviyo field name or create a custom field by typing a name into the blank entry field. To the right of the field name, select a data type from these options: **String**, **Boolean**, **Numeric**, **Date**, or **List**. If you're unsure of the proper data type, head to our article on [the data types you can use in your import](https://klaviyo.zendesk.com/hc/en-us/articles/115005237648).

****![Map_Custom_Property.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723630865179)****Below is an example of field mapping for a Drip contacts import.
 ![Drip_Field_Mapping_2.png](https://klaviyo.zendesk.com/hc/article_attachments/28723625582875)
 When you're finished, click ****Start Import**** on the upper-right corner of your screen.![Start_CSV_Import.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630883995)

For a deeper dive into importing contacts, head to our article on [migrating existing subscribers and unsubscribes into Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115002053752).

## Export Drip Unsubscribed List

It is important to add in recipients who have unsubscribed from emails sent through Drip to your Klaviyo Suppression List to ensure compliance with spam laws and keep your deliverability high.

Since Drip's inactive people grouping does not directly correlate with suppressed Klaviyo profiles, we recommend creating a Drip segment of active people who have unsubscribed to email marketing. You can also export your Drip inactive people and add those to your Klaviyo Suppression List.

From your Drip account, navigate to the ****People**** section and click the ****Active**** tab.

![Drip1.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630861211)

Click the dropdown and select ****people unsubscribed to email marketing****. This will create a segment of all active people who are opted-out from email marketing.

![Drip_Segment1.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630892955)

Click ****Actions**** and choose ****Export to CSV****. Then, click ****OK****. Drip will email the CSV file to the address listed on your ****Drip Account****, under ****General Info****.

## Format CSV File for Suppress List

Format the CSV file containing unsubscribes so that it contains a single column of email addresses**.** Label the column **Email** for clarity.

Below is an example of how your suppression list CSV file should be formatted.

![Suppress_list_format.png](https://klaviyo.zendesk.com/hc/article_attachments/28723659146523)

As an optional step, you can also export your Drip Inactives and format that list for upload into your Suppression List in Klaviyo. To do so, navigate to ****Drip > People > Inactives****. Click ****Actions > Export to CSV****. Visit the Drip Help Center for more information on [exporting Drip Inactives](https://www.drip.com/learn/docs/manual/people/inactive).

## Load Unsubscribes into Klaviyo

Navigate to the ****Profiles**** tab in your Klaviyo account and click ****Suppressed Profiles**** on the upper right. Then, select ****Upload File****.

![Import_CSV_to_Suppressed_blurred.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723625557275)

Click ****Choose File**** to select the CSV file containing your Drip suppressions. Then, click ****Upload Suppressions****.

![Bronto21.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630906139)

Your Klaviyo Suppression List will now reflect your import.

## Migrate Email Templates from Drip to Klaviyo

Klaviyo offers an intuitive drag-and-drop template builder that you can use to recreate your Drip email templates. We highly recommend using this method to rebuild your templates because it will ensure that they are mobile-optimized, responsive, and easy-to-edit moving forward.

Check out [our guide to using Klaviyo's template editor](https://help.klaviyo.com/hc/en-us/articles/115005082447-The-Email-Template-Editor).

If you don't have time to recreate your Drip templates, it is possible to export your email templates from Drip in raw HTML and then upload the updated raw HTML into Klaviyo. However, we strongly recommend rebuilding your templates in the template editor so you don't have to update the raw HTML of your emails going forward. If you choose to import raw HTML templates, you can reference our article on [importing a custom HTML template](https://klaviyo.zendesk.com/hc/en-us/articles/115005254068).

## Sunset Your Drip Account

After you've moved all your data over to Klaviyo, there are three key steps you can take to ensure that you no longer need your Drip account:

1. Ensure that your signup forms and list growth tools point to Klaviyo, not Drip.
2. Recreate your Drip workflows as Klaviyo flows.
3. Discontinue use of Drip.

### Signup Forms and List Growth Tools

Recreate any Drip signup forms in Klaviyo so that your list continues to grow in Klaviyo, rather than in Drip. You can:

1. Use the Klaviyo [Signup Form Builder](https://help.klaviyo.com/hc/en-us/articles/360002050572-The-Signup-Form-Builder) to re-create your forms from scratch.
2. Use a third-party list growth tool that integrates with Klaviyo.
3. Integrate your custom form through your ecommerce platform.

If you are using third-party list growth tools, make sure that these sync to Klaviyo. Klaviyo integrates with a number of [tools for list growth and landing pages](https://help.klaviyo.com/hc/en-us/sections/115001509868-Tools-for-List-Growth-Landing-Pages). [Scan our list of integrations](https://help.klaviyo.com/hc/en-us/categories/115000874028-App-Integrations) to find the tool that you're using. If you don't see it listed, consider using Klaviyo's signup form builder to create your forms, or try switching to a different third-party tool.

Please note that all Klaviyo lists are [double opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108-The-Double-Opt-In-Process) by default. If you would like to change a list to single opt-in and you are on a paid plan, [reach out to support](https://help.klaviyo.com/hc/en-us/requests/new).

If you’re using a custom-coded form, there are two ways you can ensure that these contacts sync to Klaviyo. One option is to make sure that your custom form syncs new subscribers directly to your ecommerce platform and that your ecommerce store is integrated with your Klaviyo account. The second option is to point the form directly to your Klaviyo account by updating the Form Action URL. To find the Form Action URL in your Klaviyo account, go to your ****Lists & Segments**** tab and click on the list where you want to add your new subscribers. Click on the ****Subscribe Page**** tab and copy the URL in the upper right.

![Updating_Form_Action_URL.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723630915355)

After switching all your signup forms to point to Klaviyo, wait a few days and watch your lists in Drip. If you notice subscribers are still being added to these lists, there's probably at least one form that still needs to be swapped out.

Next, you'll want to turn off your Drip signup forms. [Contact Drip Support](https://www.Drip.com/contact) for information on how to turn off your Drip signup forms.

### Flows

Flows are automated communication, triggered off of customer action, that allow you to personalize your messages to each recipient. It is important to recreate these in Klaviyo so that you don't need to continue to use Drip to send triggered emails.

As you move from Drip, it may be a good time to refresh and update your automated messaging. We recommend that you turn on your [welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172-Create-a-Welcome-Series-Flow) and [abandoned cart](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow) flows as soon as possible. A welcome series is particularly important to engage new subscribers, and abandoned cart flows have the highest ROI of any other type of flow.

Once your Klaviyo flows are live, you'll want to turn off all of your workflows in Drip to ensure that you're not double-emailing people. [Contact Drip Support](https://www.Drip.com/contact) for more information about turning off your Drip workflows.

### Discontinue Drip Use

Once you’ve pointed all of your list growth tools to your Klaviyo account, paused your Drip workflows, and turned your Klaviyo flows live, you can discontinue using Drip. Before you close your Drip account, double-check that everything is working as expected. Enter a test email into your signup form and other list growth tools, abandon a cart, and sign up for your newsletter to trigger a welcome series. Go to the ****Profiles**** tab in your Klaviyo account to make sure that the information in the profile reflects all of the correct communication. If the list you sign up to is double opt-in, be sure to confirm your email first.

After you've taken these steps and are fully migrated to Klaviyo, you can close your Drip account.

## Next Steps with Klaviyo

Once your Klaviyo account is integrated with your store and all of your data is migrated over from Drip, you can work toward your first Klaviyo send by following our [Guide to Your First Send](https://klaviyo.zendesk.com/hc/en-us/articles/360027226471).

If you have questions about transitioning from Drip or getting started with Klaviyo, please [reach out to our Support Team](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272).