---
id: "115005083387"
title: "Getting started with GoFundMe Pro"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005083387-Getting-started-with-GoFundMe-Pro"
section: "Classy"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:21Z"
language: "en"
---
## You will learn

Learn how to integrate GoFundMe Pro with Klaviyo. After completing these steps, you'll be able to personalize and target emails based on each Contributor's donation and website activity.

## Before you begin

In order to integrate GoFundMe Pro with Klaviyo, you will need access to GoFundMe Pro's API which requires a paid GoFundMe Pro subscription. To learn more about accessing the GoFundMe Pro API, visit their [Getting Started with the GoFundMe Pro API](https://support.classy.org/s/article/getting-started-with-the-classy-api) article and Developer site [Requesting Access](https://developers.classy.org/overview/request-access) article.

## Create an app in GoFundMe Pro

In order to integrate GoFundMe Pro with Klaviyo, you will first need to create a new API app in GoFundMe Pro. This is because you will need a GoFundMe Pro Client ID and a Client Secret in order to integrate, and the way to generate these credentials is by creating an API app in GoFundMe Pro.

1. Log in to your GoFundMe Pro admin account.
2. In the left-hand menu, click on ****Apps & integrations****
   ![API + Apps tab in Classy showing Classy API enabled](https://klaviyo.zendesk.com/hc/article_attachments/28713328533787)
3. Click on ****GoFundMe Pro API****. You'll be brought into the app creation page, where you'll be asked to name your app and enter you Oauth2 Redirect URI. You can name your app Klaviyo API and enter your website's URL under Oauth2 Redirect URI. Then, click ****Create App****.
   ![Create new app in Classy with fields for Application Name and Oauth2 Redirect URI, create app grayed out](https://klaviyo.zendesk.com/hc/article_attachments/28713334167195)
4. Once you've created your new app, it will be listed in your GoFundMe Pro account. By clicking ****Edit**** next to your app, you can view your Client ID and Client Secret, which you should store securely in order to copy-paste them into Klaviyo.
   ![Edit API application page in Classy Client ID and Client Secret fields blurred out](https://klaviyo.zendesk.com/hc/article_attachments/28713328545819)

## Locate your Organization ID

You'll also need to find your Organization ID in GoFundMe Pro.

1. Navigate to your GoFundMe Pro Dashboard.
2. Here, you’ll see the Organization ID at the end of the URL. This will be a numeric value found after "/admin" as can be seen in the screenshot below. This ID will need to be copied and pasted into Klaviyo when you configure your GoFundMe Pro integration.
   ![URL of Classy dashboard with a part of the URL, the number 55770, highlighted in gray](https://klaviyo.zendesk.com/hc/article_attachments/28713328548763)

## Add the GoFundMe Pro integration

Now, you'll add the GoFundMe Pro integration in Klaviyo.

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Explore apps****, search for **GoFundMe Pro**, and click the card. Then, click ****Install****.
3. Enter your Client ID, Client secret, and Organization ID from GoFundMe Pro.

   ![Screenshot 2026-02-02 at 7.44.26 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46213955465755)
4. Click ****Connect to GoFundMe Pro**********.******
5. On the next page, you can choose to **Add all GoFundMe** **Pro supporters to a Klaviyo list**, and select a list from the dropdown.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28713328579355)
6. When you're done, click ****Complete setup****.

## Monitor the Klaviyo sync

To check on your GoFundMe Pro integration:

1. Click the ****Analytics**** dropdown in Klaviyo and select the ****Metrics**** tab.
2. Click on the **Made Contribution** metric to verify that there is data populated for this metric. If there is data, all you need to do is wait until your initial GoFundMe Pro integration sync has completed; this process can take up to a couple hours depending on how much data you have in your account. Klaviyo will import all of your historic GoFundMe Pro data.
3. To verify this, you can compare the number of contributions on a particular day in Klaviyo with what's in your GoFundMe Pro interface and confirm they match. For example, when exploring the **Made Contribution** metric, you can mouse over yesterday's data point or look at the table of data below the chart to see how many contributions were reported yesterday.
4. Compare that number to what's stored in GoFundMe Pro from yesterday and you should see they match exactly. If they don't, the issue is most likely that your Klaviyo account's timezone doesn't match your GoFundMe Pro timezone.
5. To check your timezone setting in Klaviyo:
   - Click your account name in the lower left.
   - Select then clicking ****Settings > Organization****.
   - Scroll down to **Time zone**.

## Data synced from GoFundMe Pro

There are several Metrics that are captured by GoFundMe Pro and loaded into Klaviyo. All of these metrics can be viewed by filtering for GoFundMe Pro.

![Klaviyo metrics tab filtered by Classy showing list of metrics including Created Fundraising Team](https://klaviyo.zendesk.com/hc/article_attachments/28713334189467)

GoFundMe Pro periodically syncs data to your Klaviyo account every 30 minutes.

### The Made Contribution metric

This event is tracked when a supporter makes a contribution in GoFundMe Pro. The event Klaviyo tracks includes all of the information GoFundMe Pro collects including the contribution amount, whether the donation is recurring, and if so, how often the donation will recur. You can filter and target **Made Contribution**events based on the following criteria:

- Value
- Campaign End
- Campaign Goal
- Campaign ID
- Campaign Name
- Campaign Start
- Campaign Type (ex. peer\_to\_peer)
- Campaign Venue
- Comment
- Fees
- If Anonymous (true or false)
- Organization ID
- Price
- Product ID
- Product Name (ex. Offline Donation)
- Quantity
- Whether or not it's a dedication email (true or false)
- Transaction ID
- Type of donation

Here is an example of the data we receive along with a **Made Contribution**event:

![Popup in Klaviyo showing Activity details for a Made Contribution event including value](https://klaviyo.zendesk.com/hc/article_attachments/28713334195099)

### The Registered for Event metric

This event is tracked when a supporter has registered for an event in GoFundMe Pro. The event Klaviyo tracks includes all of the information GoFundMe Pro collects when an event registration takes place. You can filter and target **Registered for Event**events based on the following criteria:

- Value
- Campaign End
- Campaign Goal
- Campaign ID
- Campaign Name
- Campaign Start
- Campaign Type (ex. peer\_to\_peer)
- Campaign Venue
- Comment
- Fees
- If Anonymous (true or false)
- Organization ID
- Price
- Product ID
- Product Name (ex. Offline Donation)
- Quantity
- Recurring Plan ID
- Whether or not it's a dedication email (true or false)
- Transaction ID
- Type (registration)

Here is an example of the data we receive along with a Registered for Event event:

![Popup in Klaviyo showing activity details for a Registered for Event event including value](https://klaviyo.zendesk.com/hc/article_attachments/28713334199835)

### Fundraising team and page metrics

In addition to the primary **Made Contribution**and **Registered for Event**metrics that Klaviyo syncs to track how supporters engage with your organization, we will also sync the following events around the creation of Fundraising Teams and Pages, and goal progress:

- ****Created Fundraising Team****
  Recorded when someone creates a fundraising team page.
- ****Fundraiser reached 25% of Goal****
  Recorded when a Fundraising Team has reached 25% of its goal.
- ****Fundraiser reached 50% of Goal****
  Recorded when a Fundraising Team has reached 50% of its goal.
- ****Fundraiser reached 75% of Goal****
  Recorded when a Fundraising Team has reached 75% of its goal.
- ****Fundraiser reached 100% of Goal****
  Recorded when a Fundraising Team has reached 100% of its goal.

Here is a list of the details received along with each of these metrics:

- Status
- Total Raised
- Fundraiser Team Name
- Average Donation
- Largest Donation
- Campaign ID
- Organization ID
- Total Donors
- Total Donations
- Campaign Name
- Team Lead ID
- Percent to Goal
- Fundraiser Team ID
- Fundraiser Zip Code
- Fundraiser State
- Total Fundraisers

Here is an example of what these tracked events might look like on a Fundraiser's Klaviyo Profile:

![Klaviyo profile for Daniel Esrig showing a timeline of different Classy events](https://klaviyo.zendesk.com/hc/article_attachments/28713334204187)

### Customer data

Klaviyo will create a comprehensive Klaviyo profile for every contributor. Along with basic contact information, Klaviyo will also sync any additional details you might have stored in GoFundMe Pro about a given person. These details will get synced as custom properties that get added to each Klaviyo profile. You can use these properties in segments and flows. Here are the properties that are automatically synced from GoFundMe Pro:

- Email
- First Name
- Last Name
- City
- State/Region
- Zip Code
- Country
- Phone Number

## Outcome

You've now finished integrating GoFundMe Pro with Klaviyo and reviewed your synced data.

## Additional resources

- [How to set up Classy campaigns and flows](https://klaviyo.zendesk.com/hc/en-us/articles/115005255868)
- [How often integrations sync reference](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208)