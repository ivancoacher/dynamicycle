---
id: "115005255108"
title: "How to integrate with Funraise"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005255108-How-to-integrate-with-Funraise"
section: "Funraise"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "en"
---
## You will learn

Learn how to integrate Funraise with Klaviyo in order to personalize and target emails based on each contributor's donation and website activity. The data synced from Funraise to Klaviyo includes:

- When a contribution is made
- Contribution amount
- Customer information including first and last name, location, and how they found your site
- Whether the donation is recurring and if so, how often it will occur
- Whether the contributor wants to be anonymous

## Add the Funraise integration

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps****, search for **Funraise**, and click the card. Then, click ****Install****.
3. Enter your username and password, then click ****Connect to Funraise****. Note that the Email and Password must have admin access, otherwise, Klaviyo will not pull in all of your fundraising and campaign data.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723629819803)
4. On the next page, you will have the option to automatically add new supporters to a Klaviyo list, and select a list from the dropdown.
5. Click ****Complete setup****.

## Add Klaviyo onsite tracking

Klaviyo provides different types of onsite tracking, one of which tracks when known users are active on your site. This type of tracking is known as **Active on Site** tracking, and you can enable it for your Funraise site. To enable it, you must add a code snippet to your site footer.

With **Active on Site** tracking, you’ll be able to see and leverage data related to website visits and visitor behavior. For example, you can use the **Active on Site** metric to create segments of people who have visited your site (while logged in), but haven't yet made a donation.

1. Copy the **Active on Site** code snippet below:

   ```
   <script type="application/javascript" async
    src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=Public API Key"></script>
   ```
2. Navigate to your Funraise site and paste the snippet into the main template of your app before the </body> tag.
3. Replace the ‘Public API Key’ text in the snippet with your Klaviyo public API key, found in your Klaviyo account under ****Account name > Settings > API keys****.
4. Save your changes.
5. In your Klaviyo account, navigate to ****Integrations > Manage data > Setup web tracking**** in the upper right, and enter your site URL on the second step.
6. Click ****Next**** to test your tracking setup.
   ![URL text box for Klaviyo web tracking setup test with Next with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28723624474651)
7. If your tracking was set up correctly, you will receive a success message.

## Monitor the Klaviyo sync & verify donation data

To monitor and verify your Funraise integration data sync:

1. Click the ****Analytics**** dropdown in Klaviyo and select ****Metrics****.
2. Search for and click on the **Made Contribution** metric to verify that there is data populated for the metric.
3. If there is data, all you need to do is wait until your initial Funraise integration sync has completed; this process can take up to a couple hours depending on how much data you have in your account.
4. Klaviyo will import all of your historic Funraise data; to verify this, you can compare the number of contributions on a particular day in Klaviyo with what's in your Funraise interface and confirm they match.
5. If they don't match, the issue is most likely that your Klaviyo account's timezone doesn't match your Funraise timezone.
6. To check your timezone setting in Klaviyo, click your account name in the lower left, select ****Settings**** ****> Organization****.
7. Locate the **Time zone** section.

## Data synced from Funraise

There is one major metric that is captured by Funraise and synced Klaviyo: **Made Contribution**.

This event is tracked when a supporter makes a contribution in Funraise. The event Klaviyo tracks includes all of the information Funraise collects including the contribution amount, whether the donation is recurring, and if so, how often the donation will recur. You can filter and target **Made Contribution** events based on the following key criteria:

- Donation Type
- Form Name
- Form URL
- Is Anonymous (True or False)
- Is Dedication (True or False)
- Is Recurring (True of False)
- Page URL

Here is an example of all the data Klaviyo receives along with a Made Contribution event:

![Activity details for Made Contribution metric in Klaviyo showing fields such as value and donation type](https://klaviyo.zendesk.com/hc/article_attachments/28723629805851)

In addition to this core metric Klaviyo syncs from Funraise, Klaviyo also creates a Klaviyo profile for every contributor. Along with basic contact information, Klaviyo will also sync any additional details you might have stored in Funraise about a given person. These details will sync as custom properties that get added to each Klaviyo profile. You can use these properties in segments and flows.

Here are the default properties that are automatically synced from Funraise:

- Email
- First Name
- Last Name
- City
- State/Region
- Zip Code, Country
- Phone Number

## Outcome

You have completed integrating with Funraise, set up web tracking, and have verified your Funraise data in Klaviyo. Now, you'll be able to personalize and target emails based on each contributor's donation and website activity.

## Additional resources

- [Integration FAQ reference](https://help.klaviyo.com/hc/en-us/articles/115005081007)
- [How often integrations sync reference](https://help.klaviyo.com/hc/en-us/articles/115005253208)