---
id: "115005081687"
title: "How to integrate with Zoho"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005081687-How-to-integrate-with-Zoho"
section: "Zoho"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "en"
---
## You will learn

Learn how to integrate Klaviyo with Zoho's CRM service. After completing these steps, you'll be able to use your leads' custom property data from Zoho to personalize messages in Klaviyo.

## Before you begin

Please note that Klaviyo's Zoho integration only syncs Zoho leads, and not Zoho contacts/customers.

## Add the Zoho integration

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps****, search for **Zoho**, and click the card. Then, click ****Install****.
3. Click ****Connect to Zoho****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28713333871131)
4. Log in to Zoho if needed, select the organization you want to connect, and accept the permissions.
5. Back in Klaviyo, select your Zoho CRM timezone from the dropdown. This must be the same timezone as your Zoho account.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28713333873947)
6. Add any additional fields you want to sync from Zoho by checking the box and inputting a comma-separated list. Ensure there are no spaces between commas.
   - The **Field API names** input must use the API names for the fields from Zoho. Locate the API field names by clicking on the gear in the top right-hand corner of your Zoho account. Then, under **Developer Space**, select ****APIs > API Names.**** Click on ****Leads**** to see the field names, along with their corresponding API names.
     ![List of API names in Zoho including Field Label and Data Type](https://klaviyo.zendesk.com/hc/article_attachments/28713328255515)
7. When you are done, click ****Complete setup****.

## Monitor the Zoho sync and verify data

Allow at least fifteen minutes for the Zoho sync to complete. Following the initial integration setup, your Zoho leads data syncs with Klaviyo once an hour.

Once you integrate and sync Zoho with Klaviyo, all of your Zoho leads will be imported to Klaviyo with the default customer properties, as well as any optional fields you set in the integration settings.

To verify this, create a segment of the Zoho leads using the **Lead Status** property. This will group all the profiles in your account that were imported from or updated with data from Zoho.

1. In Klaviyo, navigate to ****Audience > Lists & Segments****.
2. Click ****Create List/Segment**** and choose ****Segment****
3. Give your segment a descriptive name and any tags you'd like
4. Set the segment definition to: ****Properties about someone > Lead status > is set****.
   ![Lead Status is set segment in Klaviyo segment builder with Create Segment with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28713333864987)
5. Click ****Create Segment****.
6. Compare the people in this segment with the leads in your Zoho account; the lists should match.

## Zoho metrics

Unlike other integrations, there is no viewable metric from Zoho, but Klaviyo does sync the following information for each Zoho lead:

- Email
- First Name
- Last Name
- Company
- Phone
- City
- State
- Zip Code
- Country
- Lead Status
- Email Opt Out

![Contact, channels, and information sections of a profile in Klaviyo with customer property lead status set to Lost Lead](https://klaviyo.zendesk.com/hc/article_attachments/28713333862427)

This information is viewable in each Klaviyo profile synced from Zoho. To view all Zoho leads at once, you can use the **Lead Status** segment discussed above.

## Update to our new Zoho integration

Having issues with your Zoho integration? You may be using our old integration which has been deprecated. Klaviyo has released a new Zoho integration to improve security and stability.

To update to the new integration, you need to re-authenticate Klaviyo with Zoho:

1. In Klaviyo, click the ****Integrations**** tab.
2. Select ****Zoho**** from the list of enabled integrations.
3. In the upper right corner, click ****Manage integration****.
4. Select ****Re-authenticate****.
5. Click ****Accept**** on the Zoho permissions page.

Your integration has now been updated.

While not necessary, you may wish to remove the deprecated Klaviyo app from your **Connected Apps** in Zoho. To do so, follow [Zoho's guidance on revoking OAuth tokens](https://www.zoho.com/accounts/protocol/oauth/revoke-refresh-token.html).

## Outcome

You've now integrated with Zoho and reviewed your synced data.

## Additional resources

- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [Understanding the types of data exchanged between Klaviyo and apps](https://help.klaviyo.com/hc/en-us/articles/360030696012)