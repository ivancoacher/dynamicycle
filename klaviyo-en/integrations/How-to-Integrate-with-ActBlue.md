---
id: 115005255208
title: "How to Integrate with ActBlue"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005255208-How-to-Integrate-with-ActBlue"
section: "ActBlue"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:40Z"
language: en
---

## You will learn

Learn how to integrate ActBlue with Klaviyo. After completing these steps, you'll be able to personalize and target emails based on each Contributor's donation and website activity. Here's some of the data we sync from ActBlue:

- Amount of the contribution
- Contributor information including first and last name, location, and how they found your site
- Whether the donation is recurring and if so, how often in will occur
- The Committee to which the donation was made
- The EntityID and FecID

## Add the ActBlue integration

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps****, search for **ActBlue**, and click the card. Then, click ****Install****.
3. Select ****Connect to ActBlue****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723518757659)
4. On the next page, copy the Webhook URL, Username, and Password and send it to your ActBlue Account Manager. If you don't have a contact at ActBlue, please [contact our Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272) and we will forward it to ActBlue (this process usually takes less than 24 hours).
5. Click ****Complete setup****.

## Monitor the Klaviyo sync

To check on your ActBlue integration (once you've fully integrated):

1. Click the ****Analytics**** dropdown in your Klaviyo account and select the ****Metrics**** tab.
2. Click on the ****Made Contribution**** metric (identifiable with an ActBlue icon) to verify that there is data populated for this metric.
3. If there is data, all you need to do is wait until your ActBlue integration's historical sync has completed; this process can take up to a couple hours depending on how much data you have in your account.
4. Klaviyo will import all of your historic ActBlue data. To verify this, you can compare the number of orders on a particular day in Klaviyo with what's in your ActBlue interface and confirm they match. For example, when exploring the **Made Contribution** metric**,** you can mouse over yesterday's data point or look at the table of data below the chart to see how many orders were reported yesterday.
5. Compare that number to what's stored in ActBlue from yesterday and you should see they match exactly. If they don't, the issue is most likely that your Klaviyo account's timezone doesn't match your ActBlue timezone.
6. To check your timezone setting in Klaviyo:
   - Click your account name in the lower left.
   - Select then clicking ****Settings**** ****> Organization****.
   - Scroll down to **Timezone**.

## Data synced from ActBlue

There is one major metric that is captured by ActBlue and synced into Klaviyo: **Made Contribution**.

![Metrics tab in Klaviyo filtered by ActBlue showing Made Contribution metric](https://klaviyo.zendesk.com/hc/article_attachments/28723518748571)

### Made Contribution

This event is tracked when a customer completes the checkout process and makes a contribution in ActBlue. The event Klaviyo syncs includes all the information ActBlue collects including the contribution amount, whether the donation is recurring, and if so, how often the donation will recur. You can filter and target **Made Contribution** events based on the following criteria:

- ****Amount****
- ****Recurring****This is either True or False.
- ****Recurring Period****This will be "Once" if the donation is not recurring, otherwise it will indicate how often the donation recurs.
- ****Committee Name****The name of the committee to which the contribution was made.
- ****EntityID****
- ****FecID****

Here is an example of the data we receive along with a **Made Contribution**event:

![Event details popup in Klaviyo for a Made Contribution event](https://klaviyo.zendesk.com/hc/article_attachments/28723507080091)

### Customer data

In addition to the two core metrics Klaviyo syncs from ActBlue, Klaviyo also creates a comprehensive Klaviyo Profile for every contributor. Along with basic contact information, Klaviyo will also sync any additional details you might have stored in ActBlue about a given person - these details will sync as Custom Properties that get added to each Klaviyo profile. You can use these properties in segments and flows. Here are the default properties that are automatically synced from ActBlue:

- Email
- First Name
- Last Name
- City
- State/Region
- Zip Code
- Country
- Phone Number

### Frequency of ActBlue sync

The Made Contribution metric and custom profile properties from ActBlue are synced using webhooks. This means that ActBlue indicates to Klaviyo when an event has occurred and Klaviyo will then pull all relevant data for the event. This occurs almost instantaneously.

## Add Klaviyo onsite tracking

The final step here is adding Klaviyo's **Active on Site** tracking code to your website footer. This Klaviyo tracking code will allow us to track an **Active on Site** metric for you so that you can see and leverage data related to site visits and visitor behavior. Through this metric, Klaviyo will track website activity for known browsers.

For example, you can use the **Active on Site** metric to create segments of people who have visited your site (while logged in), but haven't yet made a donation.

1. The following tracking script can be found in Klaviyo by selecting the ****Integrations**** tab, then clicking ****Manage data > Set up web tracking**** in the upper right corner.
2. We've also included the Klaviyo **Active on Site** tracking script here, which you can paste into the main template of your app before the `</body>` tag. Remember to add your own API key, found under ****Settings > API keys****, where you see 'Public API Key':

   ```
   <script type="application/javascript" async
    src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=Public API Key"></script>
   ```
3. You will then need to enter your site URL on the **Set Up Web Tracking** page. Once you have entered your URL, click ****Next**** to test the tracking setup. You should receive a success message if it's working correctly.
   ![Step 2 of set up web tracking with text box for URL and Next button with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28723507087771)

## Outcome

You have now integrated with ActBlue, verified your synced data, and added Klaviyo onsite tracking.

## Additional resources

- [Integration FAQ reference](https://help.klaviyo.com/hc/en-us/articles/115005081007)
- [How often integrations sync reference](https://help.klaviyo.com/hc/en-us/articles/115005253208)