---
id: 115005255168
title: "How to integrate with DonorPerfect"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005255168-How-to-integrate-with-DonorPerfect"
section: "DonorPerfect"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:25Z"
language: en
---

## You will learn

Learn how to integrate DonorPerfect with Klaviyo. After completing these steps, you'll be able to personalize and target emails based on each Contributor's donation and website activity. Here's some of the data we sync from DonorPerfect:

- Amount of contribution
- Contributor information, including first and last name, location, and how they found your site
- Whether the donation is recurring and, if so, how often in will occur
- Whether the contributor wants to be anonymous

First, you'll need to find your DonorPerfect API key, then you'll enable the integration in Klaviyo.

## Find your API key

You can retrieve your API Key from your DonorPerfect Account Manager. Send your account manager an email requesting your API Key and they will send it to you shortly.

## Add the DonorPerfect integration in Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. On the next page, click ****Explore apps****, search for **DonorPerfect**, and click the card.
3. Then, click ****Install****.
4. Add your DonorPerfect API Key and click ****Connect to DonorPerfect****.
5. On the next page, choose to ****Add all DonorPerfect donors to a Klaviyo list****, and then select a list from the dropdown that appears.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28704476528923)
6. Click ****Complete setup****.

## Monitor the Klaviyo sync and verify data

To check on your DonorPerfect integration once you've integrated:

1. Click the ****Analytics**** dropdown in Klaviyo and select the ****Metrics**** tab.
2. Click the ****Made Contribution**** metric to verify that there is data populated for this metric. If there is data, all you need to do is wait until your initial DonorPerfect integration sync has completed; this process can take up to a couple hours depending on how much data you have in your account. Klaviyo will import all of your historic DonorPerfect data. To verify this, you can compare the number of contributions on a particular day in Klaviyo with what's in your DonorPerfect interface and confirm they match.
3. For example, when exploring the ****Made Contribution**** metric in Klaviyo, you can hover over yesterday's data point or look at the table of data below the chart to see how many contributions were reported yesterday.
4. Compare that number to what's stored in DonorPerfect from yesterday and you should see they match exactly. If they don't, the issue is most likely that your Klaviyo account's timezone doesn't match your DonorPerfect's account timezone.
5. To check your timezone setting in Klaviyo:
   1. Click your account name in the lower left.
   2. Select then clicking ****Settings**** ****> Organization****.
   3. Scroll down to **Timezone**.

## DonorPerfect data

There is 1 major metric that is captured by DonorPerfect and loaded into Klaviyo: ****Made Contribution****.

![DonorPerfect Made Contribution metric in Klaviyo in Metrics tab](https://klaviyo.zendesk.com/hc/article_attachments/28704476521755)

### The Made Contribution metric

This event is tracked when a supporter makes a contribution in DonorPerfect. The event Klaviyo tracks includes all of the information DonorPerfect collects, including the contribution amount, whether the donation is recurring and, if so, how often the donation will recur. You can filter and target **Made Contribution**events based on the following criteria:

- ****Value****
- ****Campaign****
- ****First Gift****
- ****Gift Type****
- ****In Memory Of****
- ****Is Recurring**** (True of False)

Here is an example of the data we receive along with a Made Contributionevent:

![Made Contribution metric activity details popup in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28704484671643)

### Customer data

In addition to the metric Klaviyo syncs from DonorPerfect, there are also custom properties that are added to each Klaviyo profile. You can use these properties in segments and flows. Here are the properties that are automatically synced from DonorPerfect:

- Email
- First Name
- Last Name
- City
- State/Region
- Zip Code
- Country
- Phone Number

### How often DonorPerfect data syncs

Metrics and profile properties from DonorPerfect are synced using webhooks. This means that DonorPerfect indicates to Klaviyo when an event has occurred and Klaviyo will then pull all data for the event. This occurs almost instantaneously.

## Add Klaviyo onsite tracking

The final step here is adding Klaviyo's **Active on Site** tracking code to your website footer. This Klaviyo tracking code will allow us to track an **Active on Site** metric for you so that you can see and leverage data related to site visits and visitor behavior. Through this metric, Klaviyo will track website activity for known browsers.

For example, you can use the **Active on Site** metric to create segments of people who have visited your site (while logged in), but haven't yet made a donation.

1. The following tracking script can be found in Klaviyo by selecting the ****Integrations**** tab, then clicking ****Manage data > Set up web tracking**** in the upper right corner.
2. We've also included the Klaviyo **Active on Site** tracking script here, which you can paste into the main template of your app before the `</body>` tag. Remember to add your own API key, found under ****Account name > Settings > API keys****, where you see 'Public API Key':

   ```
   <script type="application/javascript" async
    src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=Public API Key"></script>
   ```
3. You will then need to enter your site URL on the **Set Up Web Tracking** page. Once you have entered your URL, click ****Next**** to test the tracking setup. You should receive a success message if it's working correctly.
   ![Step 2 of set up web tracking with text box for URL and Next button with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28704484675867)

## Outcome

You have now integrated with DonorPerfect, verified your synced data, and added Klaviyo onsite tracking.

## Additional resources

- [Integration FAQ reference](https://help.klaviyo.com/hc/en-us/articles/115005081007)
- [How often integrations sync reference](https://help.klaviyo.com/hc/en-us/articles/115005253208)