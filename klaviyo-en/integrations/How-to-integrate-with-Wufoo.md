---
id: 115005254868
title: "How to integrate with Wufoo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254868-How-to-integrate-with-Wufoo"
section: "Wufoo"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: en
---

## You will learn

Learn how to integrate Wufoo with Klaviyo in order to create automated flow messages, personalize campaigns, and segment your lists based on data from Wufoo. Wufoo allows you to quickly create surveys, invitations, and contact forms to collect the data you need from your customers. Klaviyo syncs the following data from Wufoo:

- When someone filled out a form
- The name of the form the user filled out
- Data collected from the form's fields

## Before you begin

It is important to note the following before integrating with Wufoo:

- All forms must have a single field to collect a customer’s email address for Klaviyo to track form submissions. If there is no email field in the form, or if there are multiple email fields, Klaviyo may not sync the form results.
- Wufoo only supports the ability to pull in information from their forms if you have a paid subscription to their services. Make sure to resolve any issues in payment before attempting to sync with Klaviyo.
- Klaviyo cannot identify the Last Name field when you have the form configured as sub-fields. Instead, use 1 the following approaches to record your customer’s last names:
  - Create a single Name field (to include a subscriber's first and last name): Klaviyo will automatically split on the first space to create a first and last name for the subscriber.
  - Create 2 separate fields: If you create a First Name field and a Last Name field, Klaviyo will sync both separately.

## Integrate Wufoo with Klaviyo

You'll need your Wufoo site URL and your Wufoo API key to integrate with Klaviyo

1. Navigate to the **Forms** tab in Wufoo.
2. Click the 3-dot menu on the right-hand side of the form you’d like to connect to Klaviyo.
   ![The Forms tab in Wufoo showing Flowers Order Form and Create new form with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28705636351771)
3. Select ****API information**** from the dropdown.
   ![Wufoo dropdown showing Form rules, Notifications, Integrations, Analytics, and API Information highlighted in gray](https://klaviyo.zendesk.com/hc/article_attachments/28705663083803)
4. Copy the API key from the **API Information** page.
   ![API Information Wufoo with API Key blurred out and Reset button in red](https://klaviyo.zendesk.com/hc/article_attachments/28705636355483)

   This API key is a private API key. Treat private API keys like passwords; keep them in a safe place and never expose them to the public.
5. Log in to Klaviyo, select the ****Integrations**** tab.
6. Click ****Explore apps****, search for **Wufoo**, and click the card.
7. Then, click ****Install****.
8. Enter your full store URL, including “.wufoo.com”, “.wufoo.co.uk”, “.wufoo.eu”, etc.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28705636370459)
9. Enter the API key you copied earlier.
10. Click ****Connect to Wufoo****.
11. On the next page, you can specify advanced criteria:
    - **Only sync specific forms**: choose this if you only want to sync some of your Wufoo forms.
    - **Specify forms that should include checkbox fields**: if you have forms with checkboxes, make sure the data is imported into Klaviyo correctly with this option.
12. If you checked the corresponding boxes, you’ll need to provide a comma separated list of form hashes you would like to sync with Klaviyo; you can find a form's hash code on the ****Code**** page for that form.
    ![Wufoo integration settings page in Klaviyo showing checked settings Only sync specific forms and Specify forms that should include checkbox fields](https://klaviyo.zendesk.com/hc/article_attachments/28705636364699)
13. You can also check **Add Wufoo respondents to a Klaviyo list** and then specify which Klaviyo list your Wufoo form data will sync to by providing the **Form Code** and the 6-character Klaviyo list ID.
    ![Wufoo integration settings page in Klaviyo showing setting for Form Code, Email Field, and Add to Klaviyo list with Delete in blue](https://klaviyo.zendesk.com/hc/article_attachments/28705636361755)
    - To find the form code, go back into the form’s ****API Information**** and copy the form **Hash.**![API information for form in Wufoo showing multiple API ID fields and their respective titles, including Hash blurred out surrounded with red box](https://klaviyo.zendesk.com/hc/article_attachments/28705636367643)
    - To find the Klaviyo list ID, click the ****Audience**** dropdown in Klaviyo and select the ****Lists & Segments**** tab, click the list you’d like to add the Wufoo data to, and then click ****Settings****. Then, copy the list ID from the **List ID & name** section.
14. Once you’ve added any specific integration settings you need, click ****Complete setup****.

## Monitor the Wufoo sync

When you integrate with Wufoo, all available historic data will start syncing to Klaviyo within a few minutes. To check your integration:

1. Navigate to ****Analytics > Metrics****.
2. Filter by **Wufoo.**
3. Select the **Filled Out Form** metric and click on the ****Activity feed**** to view the data as it syncs.
4. If your integration has begun syncing data, you will start to see **Filled Out Form** events, with the Wufoo icon, added to this activity feed.

Klaviyo then syncs data from Wufoo once an hour going forward. Once your sync is complete, you'll see a green border around your Wufoo integration in the ****Integrations**** tab.

Currently, Klaviyo only syncs 1 metric from Wufoo: **Filled Out Form**.

This metric records all of the following information:

- Who filled out the form
- When this person filled it out
- The name of the form filled out

All data collected through the form's fields will be appended to each subscriber's profile in Klaviyo, under **Custom Properties**.

## Outcome

You’ve finished integrating Wufoo with Klaviyo and verified your synced data. Now, you can create automated flow messages, personalize campaigns, and segment your lists based on data synced from Wufoo. You can even create a [series of welcome messages](https://help.klaviyo.com/hc/en-us/articles/115002775172) that are triggered when someone submits a form.

## Additional resources

- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [How to strengthen your sending reputation](https://help.klaviyo.com/hc/en-us/articles/115005250368)
- [Types of information exchanged between Klaviyo and apps reference](https://help.klaviyo.com/hc/en-us/articles/360030696012)