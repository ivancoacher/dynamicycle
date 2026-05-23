<h1>How to migrate from Sailthru</h1>

## You will learn

Learn how to migrate from Sailthru to Klaviyo. While Klaviyo does not have a built-in integration with Sailthru, you can migrate your data over by exporting it from Sailthru and importing it into Klaviyo. Additionally, when you integrate your ecommerce store with Klaviyo, you will be able to trigger emails based on a browser's on site activities.

## Before you begin

This guide will walk you through migrating your data from Sailthru to Klaviyo. As you migrate your Sailthru lists, keep in mind that the main objectives for migrating data are to ensure that all relevant contacts and fields are represented in Klaviyo and that any opted-out contacts are treated as such in Klaviyo.

Below we provide a recommended approach that will allow you to upload opt-in contacts to Klaviyo and treat various contacts as unsubscribed based on the contact's opt-out status in Sailthru. We recommend that you review [how Sailthru defines your contacts' status](https://getstarted.sailthru.com/audience/managing-users/user-optout-levels/) so you can ensure data quality on the Sailthru side and ensure that this approach of uploading contacts aligns with your intended use of Klaviyo.

This guide give you general guidelines for migrating your data from Sailthru to Klaviyo. Contact [Sailthru support](https://getstarted.sailthru.com/contact/) for the most up-to-date instructions on exporting your Sailthru data.

## Checklist

Migrating from Sailthru to Klaviyo requires several key steps:

1. Export all Sailthru Opt-ins
2. Format CSV file
3. Import CSV files to a Klaviyo list
4. Export Sailthru Opt-outs
5. Add Opt-outs to your Klaviyo Suppression list
6. Migrate email templates
7. Export additional Sailthru data
8. Set key Klaviyo flows live
9. Sunset your Sailthru account
10. Send your first Klaviyo campaign

## Export Sailthru opt-ins

First, you’ll want to export your Sailthru opt-in contact list.

For enhanced security, only Sailthru seats (admins) that have been assigned PII (Personally Identifiable Information) permissions by their administrator are able to download raw email addresses. As such, be sure that you have the necessary permissions before you begin your Sailthru data export. Sailthru seats who do not have PII permissions are only able to download “hashed” email addresses which cannot be used in Klaviyo.

To isolate your opt-in contacts, you’ll need to use [Sailthru’s audience builder](https://getstarted.sailthru.com/audience/audience-builder/using-audience-builder/) to create a Smart List containing contacts who have opted in. For example, set up your Audience Builder filters to exclude users who have opted out. Also include filters for specific fields and VARS (custom fields/variables) in your export.

![Custom field definition outlined in orange](https://klaviyo.zendesk.com/hc/article_attachments/28717811443739)

Once you’ve created your opt-in list, export your list in CSV format. Follow these Sailthru instructions for exporting your list:

1. In My Sailthru, go to ****Users**** ****>**** ****Lists****.
2. Locate the list you want to export, and in the rightmost column, click the **Excel icon**.
3. Select ****All Emails****, and click ****Export****.
4. When your file is ready, the download begins automatically. Or, while your export is processing, you can navigate away from the page, and return later to the [Jobs](https://my.sailthru.com/reports/jobs) page:
   - At the top of My Sailthru, click the **Menu icon**.
   - Find your job in the table. If it is complete, at the end of its row, click to download the file.
5. Contact [Sailthru support](https://getstarted.sailthru.com/account/management/support/) if you need assistance creating and exporting your opt-in list.

## Format CSV files

You'll need to format each CSV file before importing it into Klaviyo. To do that, open the CSV file and comb through the list, paying special attention to the column headings.

- Column headings should be in the first row of the CSV file. If Sailthru adds additional rows before the column headings, delete these extra rows.
- Your CSV file must include an "Email" or an "Email Address" column.
- You may want to include a "First Name" and "Last Name" column.
- Include any VARS (custom profile properties), such as "Gender," that you'd like to upload to Klaviyo.
- Timestamp fields such as "date added," "last opened," and "last clicked" need to be specifically formatted or Klaviyo will not recognize them as timestamp fields. Make sure timestamp data is formatted in one of these formats:
  YYYY-MM-DD HH:MM:SS
  MM/DD/YYYY HH:MM:SS
  MM/DD/YY HH:MM:SS
  MM/DD/YYYY HH:MM
  MM/DD/YY HH:MM
  YYYY-MM-DDTHH:MM:SS

Below is an example of how your CSV file should be formatted.

![Example CSV of contacts containing fields such as first and last name](https://klaviyo.zendesk.com/hc/article_attachments/28717851116955)

Review your CSV file carefully, editing and deleting column headings and contact entries as appropriate.

Remember, it's much easier to parse and edit data within a CSV file before it is uploaded into Klaviyo.

For more detailed instructions on formatting CSV files, head to our article on [creating and adding contacts to a new list](https://klaviyo.zendesk.com/hc/en-us/articles/115005078967).

## Import CSV files to a Klaviyo list

After you've formatted your exported data, you can import it to a list in Klaviyo. Some Klaviyo flows are triggered by an email address being added to a list. Before you begin uploading contacts to a list, make sure these related flows are turned to draft or manual mode.

1. Log in to your Klaviyo account, select the ****Audience**** dropdown, then click ****Lists & Segments****.
2. Select the list where you would like to add your contacts. For this example, we're going to add subscribers to the Newsletter list.
3. On the upper right-hand corner of your list, choose ****Import Contact**** from the **Manage List** dropdown.
   ![Klaviyo Newsletter list with manage list dropdown open](https://klaviyo.zendesk.com/hc/article_attachments/28717811450779)
4. Drag and drop your CSV file. You will be prompted to review field mapping before Klaviyo begins the import. Click ****Subscribe to Email Marketing**** in the **Email** row to denote that all profiles in this upload have explicitly consented to receive email marketing from you.
5. Carefully review each import field/corresponding Klaviyo field, and modify as appropriate. By default, all identified fields are included in the import. You can omit a field from import by unchecking the box to the right of the field name.
6. Column names that have no corresponding field name in your Klaviyo account are marked as "Unmapped." If you try to import an unmapped field, you will receive an error message prompting you to map the field. By default, all identified fields are included in the import. You can omit a field from import by unchecking the box to the right of the field name. From the dropdown, select an existing field name or create a custom field by typing a name into the blank entry field. To the right of the field name, select a data type from these options: ****String****, ****Boolean****, ****Numeric****, ****Date****, ****List****, or ****Consent****. If you're unsure of the data type, head to our article on [Data Types](https://help.klaviyo.com/hc/en-us/articles/115005237648). Please note that timestamp fields, like last opened or last clicked, must be mapped as a date. Below is an example of field mapping for a Sailthru contacts import.
   ![Import review page with all fields mapped](https://klaviyo.zendesk.com/hc/article_attachments/28717851128731)
7. When you're finished, click ****Start Import**** on the upper right corner of your screen. For a deeper dive into importing contacts, head to our article on [migrating existing subscribers and unsubscribes into Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115002053752).

## Export Sailthru opt-outs

You’ll want to download customers who have opted out of email communications and then upload these to your Klaviyo Suppression list. First export your opt-out list.

Follow these Sailthru’s [instructions for exporting your opt-out data](https://getstarted.sailthru.com/audience/export/export-user-data/):

1. In My Sailthru, go to ****Users >**** ****Lists****.
2. Locate the list you want to export, and in the rightmost column, click the **Excel icon****.**
3. Select ****Optouts****, and click ****Export****.
4. When your file is ready, the download begins automatically. Or, while your export is processing, you can navigate away from the page, and return later to the [Jobs](https://my.sailthru.com/reports/jobs) page:
   - At the top of My Sailthru, click the **Menu icon**.
   - Find your job in the table. If it is complete, at the end of its row, click to download the file.
5. Format the opt-out list so that it contains a single column of email addresses. There can be an "Email" column heading, but this is not necessary for the import into Klaviyo.
6. This is an example of how your Suppression list CSV file should be formatted:
   ![Spreadsheet of sample email addresses](https://klaviyo.zendesk.com/hc/article_attachments/28717851121947)

## Add opt-outs to your Klaviyo suppression list

1. Navigate to the ****Profiles**** tab in your Klaviyo account (found under ****Audience****), and click ****Suppressed Profiles**** on the upper right.
2. Select ****Upload File****.
3. Click ****Choose File**** to select the CSV file containing your Sailthru Optouts. Then, click ****Upload Suppressions****.
4. Your Klaviyo suppression list will now reflect your import.

## Migrate your email templates from Sailthru to Klaviyo

Klaviyo has an intuitive drag-and-drop template builder that you can use to recreate your Sailthru email templates. We highly recommend using this method to rebuild your templates because it will ensure that they are mobile-optimized, responsive, and easy-to-edit moving forward.

Check out [our guide to using Klaviyo's template editor](https://klaviyo.zendesk.com/hc/en-us/articles/4407911841435).

If you don't have time to recreate your Sailthru templates using Klaviyo's template builder, it is possible to export your email templates from Sailthru in raw HTML and then upload the updated raw HTML into Klaviyo.

### Export your entire template HTML from Sailthru

To find the code for your Sailthru templates:

1. Click on the template and then click the ****Code**** tab.
2. Here, you will have access to the HTML of a given template.
   ![HTML for an email template in Sailthru](https://klaviyo.zendesk.com/hc/article_attachments/28717811462939)
3. You can copy the template code in its entirety and save it as an HTML file.
4. Remember to swap out any Sailthru-specific tags with the applicable [Klaviyo tags](https://help.klaviyo.com/hc/en-us/articles/115005084927-Template-Tags-and-Variable-Syntax) (e.g., first name tags, the unsubscribe link, etc.).
5. To upload your file to Klaviyo, click the ****Content**** dropdown in Klaviyo and select the ****Templates**** tab, then select ****Create Template****.
6. Then, select ****Import your Template****. Here, you will be prompted to select the HTML file from your computer and you can upload the file you just saved.
7. You can see a preview of what your email template will look like in the ****Preview**** tab. Please note that, going forward, you will have to directly edit the HTML in order to change the template.

For more information about importing raw HTML templates, you can reference our article on [importing a custom HTML template](https://klaviyo.zendesk.com/hc/en-us/articles/115005254068).

### Copy Sailthru template HTML in batches

Alternatively, you can export chunks of code from your Sailthru templates, and then import them into text blocks in Klaviyo's drag-and-drop editor. To do this:

1. In your Sailthru account, find the code of a particular template in the ****Code**** tab.
2. In Klaviyo, create a new drag-and-drop template by going to the ****Templates**** tab (under ****Content****) and clicking ****Create Template****. Then, select ****Basic****. Here, you can choose an unstyled template as a starting point that you will overwrite with the code from your Sailthru template.
   ![Basic email templates tab in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28717811456667)
3. Click the text block in the template, then click ****Source code.
   ![Text block in Klaviyo template builder with source button higlighted](https://klaviyo.zendesk.com/hc/article_attachments/28717811459099)****
4. Replace the existing text with the HTML from your Sailthru template, and repeat this process for the parts of the code you would like to migrate directly to Klaviyo. You can then fill in any blanks using Klaviyo's drag-and-drop editor.
5. Remember to swap out any Sailthru-specific tags with the applicable [Klaviyo tags](https://help.klaviyo.com/hc/en-us/articles/115005084927-Template-Tags-and-Variable-Syntax) (e.g., first name tags, the unsubscribe link, etc.).

## Export additional Sailthru data

Instructions in this article help you extract the data you’ll need to get up and running in Klaviyo. If you need to export additional data from Sailthru that is not included in these exports, you may want to consider using Sailthru’s paid [Data Exporter](https://getstarted.sailthru.com/analytics/exports/data-exporter/) service.

## Set key flows live

Setting flows live is a key step in ensuring that you properly warm your sending infrastructure. Flows are action-based automations that allow you to trigger messages based on customers' activity on your storefront. Because of this, emails sent through flows typically have much higher engagement rates than campaign emails, which are sent in bulk.

To start, turn the following flows live:

- [Abandoned cart](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow)
- [Welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172-Guide-to-Creating-a-Welcome-Series)
- [Post-purchase](https://help.klaviyo.com/hc/en-us/articles/360028872611-Guide-to-Creating-a-Post-Purchase-Flow)

## Sunset your Sailthru account

After you've moved all your data over to Klaviyo, there are three key steps you can take to ensure that you no longer need your Sailthru account:

1. Ensure that your sign-up forms and list growth tools point to Klaviyo, not Sailthru
2. Recreate your Sailthru workflows as Klaviyo flows
3. Discontinue use of Sailthru

### Sign-up forms and list growth tools

Recreate any Sailthru sign-up forms in Klaviyo so that your list continues to grow in Klaviyo rather than in Sailthru. You can:

1. Use the Klaviyo [sign-up form builder](https://help.klaviyo.com/hc/en-us/articles/360026474752) to re-create your forms from scratch
2. Use a third-party list growth tool that integrates with Klaviyo
3. Integrate your custom form through your ecommerce platform

If you are using third-party list growth tools, make sure that these sync to Klaviyo. Klaviyo integrates with a number of tools for list growth and landing pages. [Scan our list of app integrations](https://help.klaviyo.com/hc/en-us/categories/115000874028-App-Integrations) to find the tool that you're using. If you don't see it listed, consider using Klaviyo's native Sign-up Form Builder to create your forms, or try switching to a different third-party tool.

Please note that all Klaviyo lists are double opt-in by default. To change a list to single opt-in, head to that section of our [guide to the double opt-in process](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108).

If you’re using a custom-coded form, sync these contacts to Klaviyo by ensuring that your custom form syncs new subscribers directly to your ecommerce platform, and that your ecommerce platform is integrated with your Klaviyo account.

After switching or syncing all your sign-up forms to Klaviyo, wait a few days and watch your lists in Sailthru. If you notice subscribers are still being added to these lists, there's probably at least one form that still needs to be swapped out.

Next, you'll want to turn off your Sailthru sign-up forms. [Contact Sailthru support](https://getstarted.sailthru.com/account/management/support/) for information on how to turn off your Sailthru sign-up forms.

### Triggered messages

You may have a sequence of triggered messages running in Sailthru that you will want to recreate in Klaviyo. In Klaviyo, these types of messages are referred to as flows. As you move from Sailthru, it’s a good time to refresh and update your automated messaging. We recommend that you turn on your welcome series and abandoned cart flows as soon as possible (see above). A welcome series is particularly important to engage new subscribers, and abandoned cart flows have the highest ROI of any other type of flow.

Once your Klaviyo flows are live, you'll want to turn off all of your triggered messages in Sailthru to ensure that you're not double-emailing people. Contact [Sailthru support](https://getstarted.sailthru.com/contact/) for more information.

### Sunset your Sailthru account

Once you’ve pointed all of your list growth tools to your Klaviyo account, paused your Sailthru triggered messages, and turned your Klaviyo flows live, you can discontinue using Sailthru. Before you close your Sailthru account, double-check that everything is working as expected. Enter a test email into your sign-up form and other list growth tools, abandon a cart, and sign up for your newsletter to trigger a welcome series. Go to the ****Profiles**** tab in your Klaviyo account (found under ****Audience****) to make sure that the information in the profile reflects all of the correct communication. If the list you sign up to is double opt-in, be sure to confirm your email first.

After you've taken these steps and are fully migrated to Klaviyo you can close your Sailthru account.

## Send your first Klaviyo campaign

Once your Klaviyo account is integrated with your store and all of your data is ported over from Sailthru, you can send your first campaign with Klaviyo.

### Create and send to a 30-day engaged subscriber segment

In Klaviyo, build a segment of your 30-day engaged subscribers.

1. Navigate to the ****Lists & Segments**** tab (found under ****Audience****) and select ****Create List/Segment > Segment****.
2. Build a segment with the following criteria:
   ![Sailthru 30 day engaged segment in Klaviyo segment builder](https://klaviyo.zendesk.com/hc/article_attachments/28717811465243)
3. Take note of how many people are in your 30-day engaged segment.
   - If there are between 0-50,000 people in your segment, you can send immediately and don't need to use batch sending
   - If there are between 50,000-100,000 people in your segment, use batch sending and select the option to deliver to 20% over the course of 5 hours
   - If there are 100,000+ people in your segment, use batch sending and select the option to deliver to 10% over the course of 10 hours
4. Navigate to the ****Campaigns**** tab and select ****Create Campaign****. Select your 30-day engaged segment as the target audience.
   ![Setting to send campaign to 30-day engaged segment](https://klaviyo.zendesk.com/hc/article_attachments/28717851146779)
5. Fill in the content of this campaign using one of the templates you migrated over from Sailthru, or create a new one from scratch.
6. When you are finished editing the content of the campaign, select ****Review & Send Campaign****. Review the campaign settings to ensure that everything is correct. Then, click ****Schedule**** or ****Send****.
7. If you need to use batch sending, from the scheduling dropdown, select ****Send gradually over several hours**** and then select the appropriate strategy for the number of people in your 30-day engaged segment as outlined above.
   ![Ready to send? page in Klaviyo with Schedule and Send now options](https://klaviyo.zendesk.com/hc/article_attachments/28717851153819)

For more information, check out our [Getting started with Klaviyo course](https://academy.klaviyo.com/getting-started-with-klaviyo).

### Monitor performance

After sending your first campaign, it's incredibly important to [monitor the performance](https://help.klaviyo.com/hc/en-us/articles/115000201131) to ensure strong deliverability thresholds. Refer to the table below to benchmark your performance.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Unique Open Rate | Unique Click Rate | Bounce Rate | Unsubscribe Rate | Spam Rate |
| Great | 20% or more | 4% or more | Less than 0.5% | Less than 0.3% | 0.0% |
| Proficient | 15-19% | 2-3.9% | 0.5-0.9% | 0.3-0.5% | 0.0% |
| Room for Improvement | 10-14% | 1-1.9% | 1-1.9% | 0.6-0.9% | 0.1% |
| Critical | Less than 10% | Less than 1% | 2% or more | 1% or more | 0.2% or more |

If your performance falls into either the "great" or "proficient" thresholds, you may proceed to sending to a broader subset of customers. Otherwise, continue sending to your 30-day engaged segment until your performance is proficient or great.

## Next steps

### Build an excellent sender reputation with Klaviyo

Once you begin sending to your most engaged segment of customers, you can gradually send to more of your customers. This gradual sending process enhances your sender reputation and is known as warming your IP address.

Head over to our [articles on deliverability](https://help.klaviyo.com/hc/en-us/categories/115000873988-Email-Deliverability) to read more about warming your sending infrastructure.

### Use advanced segmentation to reach your customers

After you've engaged your most interested subscribers for the first month or so, you can begin reaching out to the rest of your customer base. Create additional segments to ensure you're reaching each corner of your customer base.

- Duplicate your Engaged (3 Months) segment and tweak the settings, decreasing the timeframe from 3 months to 30 days
- Create and send to a 90-day engaged subscriber segment
- Use historical Sailthru data to refine and build out your segments

### Create and send to a 90-day engaged subscriber segment

To create a broader segment of engaged subscribers:

1. Navigate to your ****Lists & Segments**** tab (found under ****Audience****) and select ****Create List/Segment > Segment****.
2. Your segment should have the following conditions:
   ![sail12.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717851149979)
3. Next, create and schedule your campaigns to send to this group as outlined above for the 30-day engaged segment.
4. Be sure to closely monitor your deliverability to ensure that your performance remains strong.

## Outcome

You've now migrated from Sailthru to Klaviyo and have learned best practices for migrating email providers.

## Additional resources

- [How to troubleshoot list imports](https://help.klaviyo.com/hc/en-us/articles/115005078807)
- [Understanding email deliverability](https://help.klaviyo.com/hc/en-us/articles/115005247008)
- [Profile properties reference](https://help.klaviyo.com/hc/en-us/articles/115005074627)
