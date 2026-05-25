---
id: "115005082507"
title: "Getting started with Unbounce"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005082507-Getting-started-with-Unbounce"
section: "Unbounce"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: "en"
---
## You will learn

Learn how to integrate Unbounce with Klaviyo in order to help you use landing pages to add customers to your main email list, trigger a welcome series flow, and more. You can collect contact via an Unbounce landing page and then automatically send a welcome series and other personalized messaging. Enabling Klaviyo's Unbounce integration requires steps inside of both Klaviyo and Unbounce.

## Table of contents

1. Verify form fields in Unbounce
2. Enable the integration in Klaviyo
3. Set up Unbounce webhooks
4. View Unbounce data in Klaviyo
5. Use Unbounce data in Klaviyo
6. Troubleshooting

## Verify form fields in Unbounce

To pull data into Klaviyo via webhooks, your Unbounce page needs a form with a field mapped to **email**. You can verify that your form fields are set up correctly prior to connecting your webhook by following the steps outlined below.

Unbounce has two ways to build pages: their standard builder and a Smart Builder. Checking your form fields is similar in either case. For more information on either of the forms below, see Unbounce’s documentation on [setting up a form](https://documentation.unbounce.com/hc/en-us/articles/203799174).

### Standard builder

1. In Unbounce, select the page you want to view, and then click ****Edit**** at the bottom of the page.
   ![Page named first variant in Unbounce with Edit with dark blue background](https://klaviyo.zendesk.com/hc/article_attachments/28711662230043)
2. In the page editor, click on your form, and then click ****Edit Form Fields****.
   ![Form editor with form with fields First Name, Last Name, Email, and Industry](https://klaviyo.zendesk.com/hc/article_attachments/28711662215451)
3. Click on the ****Email \***** box to open the field settings. Then, verify that the **Field Name and ID** box is set to **email**. If you need to edit this text, uncheck the **Auto-generate from Field Label** and make your edits.
   ![Design your form page in Unbounce with Field Name and ID box set to email](https://klaviyo.zendesk.com/hc/article_attachments/28711674351259)
4. Once you’ve verified the field name, click ****Done****.
5. If you made any changes to the form, click ****Save**** and then ****Republish**** on the top menu bar to implement your updates.

### Smart builder

1. In Unbounce, navigate to the page you want to edit, and click ****Edit**** at the bottom of the page.
   ![Page named first variant in Unbounce with Edit with dark blue background](https://klaviyo.zendesk.com/hc/article_attachments/28711662228379)
2. Inside of the form, click into the **Email** text box dropdown and select ****Edit Field****.
   ![Form with email textbox dropdown open and Edit field highlighted in dark blue](https://klaviyo.zendesk.com/hc/article_attachments/28711674359835)
3. In the **Edit Field** menu, verify that the **Field Name/ID** box is set to **email**.
   ![Edit Field menu with Field Name/ID set to email](https://klaviyo.zendesk.com/hc/article_attachments/28711662240923)
4. Once you’ve verified the field name, click ****Submit****.
5. If you made any changes to the form, click ****Save**** and then ****Publish**** on the top menu bar to implement your updates.

## Enable the integration in Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps**** and search for **Unbounce**, then click the card.
3. Then, click ****Install****.
4. Click ****Connect to Unbounce****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28711674390939)
5. Select the checkbox next to **Add new Unbounce leads a Klaviyo list** to sync your Unbounce leads to a specific Klaviyo list. Choose the list you’d like to sync your initial leads to from the dropdown.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28711662282139)
6. Copy the Webhook URL under **Webhook Setup**. This URL will be used in the following section to create a webhook to Klaviyo in Unbounce.
7. Click ****Complete setup****.

## Set up Unbounce webhooks

1. Head to Unbounce. From the **All Pages** page in Unbounce, select the page you’d like to add your Klaviyo webhook to.
   ![All Pages page in Unbounce with Create New with dark blue background](https://klaviyo.zendesk.com/hc/article_attachments/28711662252699)
2. Click on the ****Integrations**** tab, and select ****Webhooks**** ****>**** ****Add Webhook****.
   ![Integrations tab of Test Page for Webhooks showing Webhooks tab within it](https://klaviyo.zendesk.com/hc/article_attachments/28711662248603)
3. Paste the URL from Klaviyo into the first text box under **Choose a URL to POST form data to**.
   ![Add a webhook page in Unbounce with Klaviyo webhook URL in box and Save Changes with dark blue background](https://klaviyo.zendesk.com/hc/article_attachments/28711674370075)
4. Verify that the **email** field under **Unbounce Field ID** on the left is mapped to **email** on the right. If this is mapped to any other value - such as **your\_email** - Klaviyo will not recognize this property as an email address and the webhook will be dropped. Mapping is case-sensitive and **email** should be formatted in all lowercase.
5. Once you’ve verified all fields, click ****Save Changes****.
6. Allow time for the integration to process. If the integration is successful, you’ll see the following success message letting you know **You have successfully updated your Webhook**. Click ****Done**** to finish setup.
   ![Add a webhook success message with large green check and Done with dark blue background](https://klaviyo.zendesk.com/hc/article_attachments/28711674379675)

## View Unbounce data in Klaviyo

To check your integration after you have added the Klaviyo webhook, create a new lead through your Unbounce page.

Klaviyo syncs leads through the **Filled Out Form** metric, which appears with an Unbounce icon next to it. To confirm that this is syncing properly to Klaviyo, navigate to ****Analytics > Metrics,**** and filter by **Unbounce**. Currently, Klaviyo syncs one metric with Unbounce: **Filled Out Form**. Select **Filled Out Form** to see data specific to this metric.

Click on the ****Activity Feed**** icon and you should see a new profile created for this lead in your Klaviyo account. If you see this, your leads are now syncing.

![Filled out Form metric activity feed in Klaviyo showing an event from profile named Bill Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28711674384027)

Klaviyo will only record your leads if you have **email** as a required field in your form. If a lead does not include an email address, Klaviyo will ignore it.

The Filled Out Form metric contains the following metadata, which can be used in segments and flows:

- ****Page ID****
  The unique ID of the form the user filled out
- ****Page Name****
  The name of the form in Unbounce
- ****Page Variant****
  The variant of the form in Unbounce, as used in [Unbounce’s Smart Traffic](https://documentation.unbounce.com/hc/en-us/articles/360046684972)

## Use Unbounce data in Klaviyo

### Create a segment

If you want to send a specific email campaign to customers who responded to a specific variant of your form, you can create a segment in Klaviyo using **Page Variant** data.

1. Navigate to ****Audience > Lists & Segments**** in Klaviyo.
2. Click ****Create List/Segment****, and select ****Segment****.
3. Name your new segment appropriately and add the following definitions to the segment:
   - **If someone is in or not in a list**: set to **Is**
     Set this if you’d like to only use customers from a specific list in Klaviyo; otherwise, move to the next definition.
   - **What someone has done (or not done)**: set to Unbounce’s **Filled Out Form** metric and choose the time period you want to check across.
   - Click ****Add Filter**** and select the **Page Variant** property from the dropdown, then enter the page variant into the **equals** box.
     ![Segment in segment builder in Klaviyo for someone who has filled out a form with page variant a](https://klaviyo.zendesk.com/hc/article_attachments/28711674387227)
4. Click ****Create Segment**** when you are done.

### Create a welcome flow

You can use the data from Unbounce to create a series of welcome emails that are triggered when someone enters an email on a form. The advantage of doing this through Klaviyo is that you can set up a two to three message welcome series, triggered when your leads are added to your email list. See our [guide on creating a welcome series](https://help.klaviyo.com/hc/en-us/articles/115002775172) for more information.

## Troubleshooting

### Form fields aren’t populating in my webhook setup

If your form fields aren’t appearing in your webhook setup, you may need to republish your page to resync the form fields.

To republish:

1. Click into your page in Unbounce and go to the **Edit** screen.
2. Choose anything on your page and alter it slightly, then click ****Save****.
3. Revert the change, and click ****Save**** again.
4. Click ****Publish**** (or ****Republish****, depending on which builder you’re using).
5. Go back to the ****Webhooks**** tab of your Unbounce account and attempt the setup again. You should now be able to see the form fields populated in the webhook setup.
6. If this problem persists, reach out to the [Unbounce Support Team](https://documentation.unbounce.com/hc/en-us/articles/360029477151).

## Outcome

You've now integrated Unbounce with Klaviyo and reviewed your synced data.

## Additional resources

- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [Guide to creating segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)