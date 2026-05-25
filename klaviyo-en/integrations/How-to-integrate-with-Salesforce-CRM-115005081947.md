---
id: "115005081947"
title: "How to integrate with Salesforce CRM"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005081947-How-to-integrate-with-Salesforce-CRM"
section: "Salesforce CRM"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: "en"
---
## You will learn

Learn how to integrate Salesforce CRM with Klaviyo. This integration makes it easy to connect your Salesforce account, choose which objects to sync, and map fields—all through a guided, in-app setup flow.

With this integration, Klaviyo can automatically sync Salesforce data (such as Leads or Contacts) into Klaviyo profiles, allowing you to personalize messaging and segment customers using CRM data.

## Before you begin

Before you start integrating, make sure that:

- You have admin access to your Salesforce account
- Your Salesforce edition [supports API access](https://help.salesforce.com/s/articleView?language=en_US&id=000326486&mode=1&type=1)
- You have your Salesforce username, password, and security token available

## Obtain Salesforce security token

To enable the Salesforce CRM integration in Klaviyo, you first need to obtain your Salesforce security token.

You should have received your security token upon initial setup of your Salesforce account. If you’re part of a larger organization using Salesforce, reach out to your Salesforce administrator to obtain the security token.

If you have no record of a security token, you will need to reset your security token to receive a new one. The steps for resetting your security token are broken down below by Salesforce version, depending on whether you’re using the Lightning Experience or Salesforce Classic.

### Lightning Experience token reset

1. In Salesforce, click on your profile in the top right corner of your screen and select ****Settings****.
   ![Popup in Salesforce showing Settings and Log Out in blue](https://klaviyo.zendesk.com/hc/article_attachments/28723628867355)
2. This will take you to your personal information page. From the left-hand menu, click ****Reset My Security Token****.
   ![Menu including items Personal Information and Reset My Security Token higlighted in gray](https://klaviyo.zendesk.com/hc/article_attachments/28723628870171)
3. Click ****Reset Security Token****.
4. If your security token was used to connect to any other apps, update those integrations with this new security token.
   ![Reset security token page with warning in yellow and reset security token button with gray background](https://klaviyo.zendesk.com/hc/article_attachments/28723623583899)
5. You will then receive an email from Salesforce with your new security token. Make note of the security token and keep that information secure.

### Salesforce Classic token reset

1. In Salesforce, click on your name at the top right of your screen and select ****My Settings****.
   ![Menu with My Settings highlighted in blue](https://klaviyo.zendesk.com/hc/article_attachments/28723623587227)
2. From the **My Settings** menu, click ****Personal****. Then, select ****Reset My Security Token****.
   ![Personal dropdown under My Settings with Reset My Security Token higlighted in dark gray](https://klaviyo.zendesk.com/hc/article_attachments/28723623591451)
3. Click ****Reset Security Token****.
4. If your security token was used to connect to any other apps, update those integrations with this new security token.
   ![Reset security token page with warning in yellow and reset security token button with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28723628879003)
5. You will then receive an email from Salesforce with your new security token. Make note of the security token and keep that information secure.

## Connect Salesforce to Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps****, search for **Salesforce**, and click the card. Then, click ****Install****.
3. Enter your Salesforce username, password, and security token. Once you've entered these required details, click ****Connect to Salesforce****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47042695892379)
4. If the integration is successful, you should receive a success message.

## Choose a Salesforce Object to sync

After connecting, you’ll be prompted to select which Salesforce objects you want to sync into Klaviyo. Click ****Next**** to continue.

You can now choose ****up to 3 objects**** to sync into Klaviyo. Available options include:

- ****Lead -**** Potential customers who have shown interest in your Salesforce products or services
- ****Contact**** - Individuals associated with accounts in your Salesforce organization
- ****Account**** - Organizations or individuals involved with your business (such as customers, competitors, and partners)
- ****Opportunity****  - Potential sales or deals
- ****Other**** (availability depends on your Salesforce setup)

  Objects synced from Salesforce will be created or updated as Klaviyo profiles. When syncing multiple objects:
- Records from all selected objects will sync to Klaviyo.
- If a record’s email address matches an existing Klaviyo profile, that profile will be updated.
- If a record’s email address does not exist in Klaviyo, a new profile will be created.
- If the same person exists across multiple synced objects with the same email address, Klaviyo will consolidate them into a ****single profile**** based on email. (Field mappings are configured per object in the next step.)

![](https://klaviyo.zendesk.com/hc/article_attachments/47042705488411)

### Map Salesforce fields to Klaviyo properties

Next, you’ll map Salesforce fields to Klaviyo profile properties. Note that some core mappings such as ****email****, ****phone number****, ****first name****, and ****last name**** are pre-mapped. **Mapping of the Salesforce email address is required.**

When you’ve selected multiple Salesforce objects to sync, you’ll configure field mappings ****separately for each object****. This allows you to control which fields from each object become Klaviyo profile properties.

### Add or edit mappings

- Use ****Add mapping**** to map additional Salesforce fields for the **currently selected object**.
- Select a Salesforce field on the left and the corresponding Klaviyo property on the right.
- Remove mappings using the ****trash icon**** if needed.
- Repeat this process for each synced object.

If the same Klaviyo profile property (for example, **Phone Number** or **City**) is mapped from multiple Salesforce objects, Klaviyo will sync the most recently updated value from Salesforce into the profile.

![Screenshot 2026-01-20 at 3.31.46 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/45678170090523)

### Import mappings via CSV (optional)

CSV imports replace all existing field mappings for the selected object. If a field is not included in the file, it will be removed from your configuration. To avoid interruptions to syncing, confirm your CSV includes all required fields (such as ****Email****) and any additional fields you want to continue syncing.

To import your mappings via CSV:

1. Click ****Add mapping → Import mappings****.
2. Download the CSV template.
3. Add your Salesforce → Klaviyo field mapping to the CSV template.
4. Upload the completed CSV to apply mappings in bulk.

![Screenshot 2026-01-20 at 3.32.11 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/45678170093979)

### Unsubscribe handling (optional)

You can enable the option to sync the Salesforce object as unsubscribed when Email Opt Out is set to true on the Salesforce object. This will mark the profile as unsubscribed from email in Klaviyo.

## Complete setup

Once your mappings are complete, click ****Complete setup****. Klaviyo will finalize the integration (this usually takes a few seconds). You’ll see a confirmation message once your Salesforce account is successfully connected and syncing.

## Monitor Salesforce sync and verify data

The Salesforce integration syncs to Klaviyo every hour.

To check your integration:

1. Click the ****Analytics**** dropdown in Klaviyo and select ****Metrics****. Filter by Salesforce, then find the metric **Became Lead** and click on its ****Activity feed**** icon.
2. If your integration has started syncing data, you will see **Became Lead** events, with the Salesforce icon, added to this activity feed.
3. Klaviyo imports all of your Salesforce leads. To verify this, compare the number of leads being added to Klaviyo on a particular day with the number of leads being added to Salesforce and confirm they match.
4. Hover over yesterday's datapoint (on the activity feed for **Became Lead**, which you can find by clicking on the metric) or look in the table of data below the chart to see how many payments occurred yesterday and compare it to the data stored in Salesforce.
5. If the data doesn’t match, the issue is most likely that the timezone in your Klaviyo account doesn't match the timezone in your Salesforce account. To check your timezone setting in Klaviyo:

- Click your account name in the lower left.
- Select then clicking ****Settings > Organization****.
- Scroll down to **Time zone**.

## Salesforce metrics in Klaviyo

Currently, Klaviyo syncs one metric with Salesforce CRM: **Became Lead**.

![Screenshot 2026-01-20 at 3.25.16 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/45678170095131)

This metric is tracked when a new lead is created in Salesforce. The event itself does not include any data from Salesforce, but when this event is logged, Klaviyo will sync the following custom properties for each lead and attach them to the lead’s Klaviyo profile:

- Id
- FirstName
- LastName
- Title
- Company
- Street
- City
- State
- PostalCode
- Country
- Latitude
- Longitude
- Phone
- Email
- Website
- LeadSource
- Status
- Industry
- NumberOfEmployees
- HasOptedOutOfEmail
- Owner Email

You can then use these properties in segments, in flows, and to dynamically populate customer properties into your message templates.

## Troubleshooting

### Field mapping warnings and errors

Klaviyo continuously validates your Salesforce field mappings to ensure data can sync reliably. If a mapped Salesforce field becomes unavailable (for example, if it’s deleted, renamed, or permissions change), you may see a warning or error in your integration settings.

#### When a non-required field is unavailable

If a mapped Salesforce field is no longer available and it is not required, Klaviyo will:

- Display a warning indicating which field is missing.
- Continue syncing all other available fields.
- Exclude the unavailable field from future syncs until it is updated or removed.

To resolve this,

1. Navigate to your ****Salesforce integration**** in Klaviyo.
2. Open the affected object.
3. Update or remove the invalid field mapping.
4. ****Save**** your changes.

Once updated, syncing will continue as expected.

![image (10).png](https://klaviyo.zendesk.com/hc/article_attachments/45678170098075)

##

![](https://klaviyo.zendesk.com/hc/article_attachments/45678150584731)

#### When a required field (Email) is unavailable

If the Salesforce Email field is no longer available for an object (for example, due to schema changes or permissions), Klaviyo will:

- Display an error indicating the Email field is missing.
- Stop syncing data for the affected object.
- Prompt you to update your field mappings to restore syncing.

![image (17).png](https://klaviyo.zendesk.com/hc/article_attachments/45678170102171)

To resolve this,

1. Navigate to your ****Salesforce integration**** in Klaviyo.
2. Open the affected object.
3. Ensure a valid Salesforce Email field is mapped to Klaviyo’s Email property.
4. ****Save**** your changes.

Once the Email field is successfully mapped again, data syncing will automatically resume.

#### Profiles missing in Klaviyo

If Salesforce records aren’t appearing as profiles in Klaviyo, first verify that a ****valid email field is mapped**** for each object you’re syncing. Klaviyo uses the email address as the required identifier to create or update profiles; records without a mapped email field or without valid email values will not sync as profiles. Ensure that:

- A Salesforce ****email**** field is mapped to Klaviyo’s Email property for every selected object.
- The mapped email field contains actual email values in Salesforce — blank or invalid emails can prevent records from syncing as profiles.

Once a valid email field is mapped and records include email addresses, Klaviyo will create or update those profiles on the next sync.

## Outcome

You have now integrated your Klaviyo account with Salesforce CRM and reviewed your synced data.