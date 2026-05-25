---
id: "115005082847"
title: "How to integrate with Bloomerang Fundraising"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005082847-How-to-integrate-with-Bloomerang-Fundraising"
section: "Bloomerang Fundraising"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:21Z"
language: "en"
---
## You will learn

Learn how to integrate Bloomerang Fundraising with Klaviyo. After completing these steps, you'll be able to personalize and target emails based on each Contributor's donation and website activity. Here's some of the data we sync from Bloomerang Fundraising:

- Amount of each contribution
- Contributor information including first and last name, location, and how they found your site
- Whether each contribution is recurring and if so, how often in will occur

First, you'll need to generate an API token in Bloomerang Fundraising, and then enable the integration in Klaviyo.

## Generate your Bloomerang Fundraising API token

1. Log in to your Bloomerang Fundraising account.
2. Click on ****Data Tools**** in the left sidebar of your account then click on ****API Access******.**
3. Click ****Create API Token******.**
4. You will then be prompted you to create a token name and establish a token type. Under **Token Type**, select "Permanent".

   ![Screenshot 2026-01-29 at 7.11.22 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46052097347867)
5. Once you select "Permanent" as the **Token Type**, select the forms that you want to make accessible in Klaviyo. If you want all your donation data, select all your campaigns.
6. Bloomerang Fundraising will then provide you with your API Token**.**This is what you will need in the next step to integrate Bloomerang Fundraising with Klaviyo.

## Add the Bloomerang Fundraising integration in Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Explore apps****, search for Bloomerang Fundraising, and click the card.
3. Then, click ****Install****.
4. Enter your API Token and click ****Connect to**** ****Bloomerang********Fundraising********.****
   ![Screenshot 2026-01-29 at 7.05.43 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46052097349787)
5. You should receive a success message.

## Monitor the Klaviyo sync and verify data

To check on your Bloomerang Fundraising integration:

1. Click the ****Analytics**** dropdown in Klaviyo and select ****Metrics****.
2. Click on the **Made Contribution** metric to verify that there is data populated for this metric. If there is data, all you need to do is wait until your initial Bloomerang Fundraising integration sync has completed; this process can take up to a couple hours depending on how much data you have in your account.
3. Klaviyo will import all of your historic Bloomerang Fundraising data. To verify this, you can compare the number of orders on a particular day in Klaviyo with what's in your Bloomerang Fundraising interface and confirm they match. For example, when exploring the **Made Contribution** metric in Klaviyo, you can mouse over yesterday's data point or look at the table of data below the chart to see how many orders were reported yesterday.
4. Compare that number to what's stored in Bloomerang Fundraising from yesterday and you should see they match exactly. If they don't, the issue is most likely that your Klaviyo account's timezone doesn't match your Bloomerang Fundraising timezone.
5. To check your timezone setting in Klaviyo:
   - Click your account name in the lower left.
   - Select then clicking ****Settings > Organization****.
   - Scroll down to **Time zone**.

## Data synced from Bloomerang Fundraising

There are two metrics captured by Bloomerang Fundraising and synced to Klaviyo: **Made Contribution**and **Registered for Event**.

### Made Contribution

This event is tracked when a donor makes a contribution in Bloomerang Fundraising. You can filter and target **Made Contribution** events based on the following criteria:

- DonationSource
- Restriction
- OptedIn
- Type
- IsAnonymous
- FormName
- FormID
- $value

### Registered for Event

This event is tracked when a peer-to-peer event registration form is submitted. You can filter and target **Registered for Event** events based on the following criteria:

- FormID
- RegistrationID
- TransactionID
- Title
- FundraisingGoal
- DonationSource
- TeamCaptain
- $event\_id
- $value

### Customer data

In addition to the metrics Klaviyo syncs from Bloomerang Fundraising, there are also custom properties that are added to each Klaviyo profile. You can use these properties in segments and in flows. The following properties are built-in Klaviyo fields that will be automatically synced:

- Email
- First Name
- Last Name
- City
- State/Region
- Zip Code
- Country
- Phone Number

### Frequency of the Bloomerang Fundraising sync

Metrics and profile properties from Bloomerang Fundraising are synced using webhooks. This means that Bloomerang Fundraising indicates to Klaviyo when an event has occurred and Klaviyo will then pull all data. This occurs almost instantaneously.

## Add Klaviyo onsite tracking

The final step here is adding Klaviyo's **Active on Site** tracking code to your website footer. This Klaviyo tracking code will allow us to track an **Active on Site** metric for you so that you can see and leverage data related to site visits and visitor behavior. Through this metric, Klaviyo will track website activity for known browsers.

For example, you can use the **Active on Site** metric to create segments of people who have visited your site (while logged in), but haven't yet made a donation.

To enable onsite tracking:

1. In Klaviyo, select the ****Integrations**** tab.
2. Selct ****Manage data > Set up web tracking****.
3. Copy the code under **Step 1** and paste it in your website's main template, before the </body> tag. Make sure you paste it on the website associated with the Klaviyo account you're in.
   ![The Enable onsite tracking modal showing steps to install onsite tracking.](https://klaviyo.zendesk.com/hc/article_attachments/34456524887835)
4. After you've pasted the code snippet, click ****Confirm**** under **Step 2** to test the tracking setup. You should receive a success message if it's working correctly.
   ![The success message informing  you that onsite tracking was enabled.](https://klaviyo.zendesk.com/hc/article_attachments/34456509068443)

## Outcome

You have now integrated with Bloomerang Fundraising, verified your synced data, and added Klaviyo onsite tracking.

## Additional resources

- [Integration FAQ reference](https://help.klaviyo.com/hc/en-us/articles/115005081007)
- [How often integrations sync reference](https://help.klaviyo.com/hc/en-us/articles/115005253208)