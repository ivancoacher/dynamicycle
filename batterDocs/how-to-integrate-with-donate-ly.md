<h1>How to integrate with Donate.ly</h1>

## You will learn

Learn how to integrate Donate.ly with Klaviyo. After completing these steps, you'll be able to personalize and target emails based on each contributor's donation and website activity. Here's some of the data we sync from Donate.ly:

- Contribution amount
- Customer information including first and last name, location and how they found your site
- Whether the donation is recurring and if so, how often in will occur
- Whether contributor wants to be anonymous

First, you'll locate your Donate.ly account slug, then you'll enable the integration in Klaviyo.

## Locate your account slug

1. Login to your Donate.ly account.
2. In the top right-hand menu bar, click on the dropdown menu labeled with your organization's name then click ****Account Settings****. This will direct you to a page where you can find your account slug.
   ![General settings page in Donate.ly showing Account Title and Account Slug](https://klaviyo.zendesk.com/hc/article_attachments/28717386426395)

## Enable the Donate.ly integration in Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Explore apps****, search for **Donate.ly**, and click the card. Then, click ****Install****.
3. Enter your Donate.ly account slug, Email, and Password. The Email and Password must have admin access, otherwise Klaviyo will not pull in all of your fundraising and campaign data. Click ****Connect to Donate.ly****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717380219803)
4. You should receive a success message.

## Monitor the Klaviyo sync and verify data

To check on your Donate.ly integration:

1. Click the ****Analytics**** dropdown in Klaviyo and select the ****Metrics**** tab.
2. Click on the ****Made Contribution**** metric to verify that there is data populated for this metric. If there is data, all you need to do is wait until your initial Donate.ly integration sync has completed; this process can take up to a couple hours depending on how much data you have in your account. Klaviyo will import all of your historic Donate.ly data. To verify this, you can compare the number of contributions on a particular day in Klaviyo with what's in your Donate.ly interface and confirm they match.
3. For example, when exploring the **Made Contribution** metric in Klaviyo, you can mouse over yesterday's data point or look at the table of data below the chart to see how many contributions were reported yesterday.
4. Compare that number to what's stored in Donate.ly from yesterday and you should see they match exactly. If they don't, the issue is most likely that your Klaviyo account's timezone doesn't match your Donate.ly timezone.
5. To check your timezone setting in Klaviyo:
   - Click your account name in the lower left.
   - Select then clicking ****Settings**** ****> Organization****.
   - Scroll down to **Timezone**.

## Understand your Donate.ly data

There is one major metric that is captured by Donatel.ly and loaded into Klaviyo: **Made Contribution.**

![Donate.ly Made Contribution metric in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28717380211739)

This event is tracked when a supporter makes a contribution in Donatel.ly. The event Klaviyo tracks includes all of the information Donatel.ly collects including the contribution amount, whether the donation is recurring, and if so, how often the donation will recur. You can filter and target **Made Contribution** events based on the following criteria:

- ****Value****
- ****Anonymous****(True or False)
- ****CampaignTitle****
- ****CampaignUniqueIdentifier****
- ****DonationType****
- ****Is Recurring**** (True of False)

Here is an example of the data we receive along with a **Made Contribution** event:

![Activity details for Donate.ly Made Contribution metric in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28717380213275)

### Customer data

In addition to the two core metrics Klaviyo syncs from Donate.ly, Klaviyo also creates a comprehensive Klaviyo profile for every contributor. Along with basic contact information, Klaviyo will also sync any additional details you might have stored in Donate.ly about a given person - these details will sync as custom properties that get added to each Klaviyo profile. You can use these properties in segments and flows.

Here are the default properties that are automatically synced from Donate.ly to built-in Klaviyo fields:

- Email
- First Name
- Last Name
- City
- State/Region
- Zip Code
- Country
- Phone Number

## Frequency of Donate.ly sync

Metrics and profile properties from Donatel.ly are synced using webhooks. This means that Donatel.ly indicates to Klaviyo when an event has occurred and Klaviyo will then pull all data for the event. This occurs almost instantaneously.

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
   ![Step 2 of set up web tracking with text box for URL and Next button with blue background](https://klaviyo.zendesk.com/hc/article_attachments/28717386435995)

## Outcome

You have now integrated with Donor.ly, verified your synced data, and added Klaviyo onsite tracking.

## Additional resources

- [Integration FAQ reference](https://help.klaviyo.com/hc/en-us/articles/115005081007)
- [How often integrations sync reference](https://help.klaviyo.com/hc/en-us/articles/115005253208)
