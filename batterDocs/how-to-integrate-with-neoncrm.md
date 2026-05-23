<h1>How to integrate with NeonCRM</h1>

## You will learn

Learn how to integrate NeonCRM with Klaviyo in order to personalize and target emails based on each Contributor's donation and event registration activity. Data synced from NeonCRM to Klaviyo includes:

- When a donation occurs, with details about the contribution
- Contact information, including first and last name, location, and custom fields
- When someone registers for an event, with details about the registration

## Integrate NeonCRM with Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps****, search for **NeonCRM**, and click the card. Then, click ****Install****.
3. You will need your NeonCRM API key and Organization ID. To generate your NeonCRM API key, open a new tab and log in to your NeonCRM system.
4. Navigate to ****System Settings > System Users****.
5. Click ****New User****; you can name this user anything you like, but we recommend naming the user something that distinguishes its use, such as **Klaviyo** **API User**.
6. Specify a user name and password.
7. Enable API access for this user account by clicking the checkbox.
8. Type in an email address; this address will receive alerts and updates from the NeonCRM team related to the API.
9. Click ****Generate**** to create your API key; you will want to copy this API key to paste into Klaviyo.
10. Click ****Next**** to complete the process of creating this user.
11. Switch back to Klaviyo and paste your API key .
    ![](https://klaviyo.zendesk.com/hc/article_attachments/28722594435995)
12. To find your Organization ID, navigate to the login screen for your NeonCRM system.
13. Look at the URL in your web browser; the text after /clients/ and before /login.jsp is your Organization ID.
14. Copy and paste your Organization ID in Klaviyo.
15. Click ****Connect to NeonCRM****.
16. If you want to add NeonCRM accounts to a list in Klaviyo, check this setting and select a list.
17. Click ****Complete setup****.

## Add Klaviyo onsite tracking

The final step is to add Klaviyo's A**ctive on Site** tracking code to your website footer. This code snippet will enable Klaviyo to track an **Active on Site** metric so that you can leverage data related to the site visits and behavior of known browsers.

For example, you can use the **Active on Site** metric to create segments of people who have visited your site (while logged in), but haven't yet made a donation.

1. Copy the **Active on Site** tracking code snippet below:

   ```
   <script type="application/javascript" async src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=Public API Key"></script>
   ```
2. Paste the snippet into the main template of your app before the </body> tag.
3. Replace ‘Public API Key’ in the snippet with your own Klaviyo public API key, which can be found under ****Account name > Settings > API keys****.
4. In Klaviyo, select the ****Integrations**** tab.
5. In the upper right, click ****Manage data > Setup web tracking****.
6. A success page with a green checkmark will appear if it’s working successfully.
   ![neon.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34274027896859)

## Monitor the Klaviyo sync

To check on the data syncing through your NeonCRM integration:

1. Click the ****Analytics**** dropdown in Klaviyo, then select ****Metrics****.
2. Click on the **Made Contribution** metric to verify that there is data populated for this metric; note that your initial NeonCRM integration sync may take up to a couple hours depending on how much data you have in your account.
3. Klaviyo will import all of your historic NeonCRM data; to verify this, you can compare the number of contributions on a particular day in Klaviyo with what's in your NeonCRM account and confirm they match.
4. If they don't match, the issue is most likely that your Klaviyo account's timezone doesn't match your NeonCRM timezone.
5. To check your timezone setting in Klaviyo:
   - Click your account name in the lower left.
   - Select then clicking ****Settings**** ****> Organization****.
   - Scroll down to **Timezone**.

## Data synced from NeonCRM

There are two major metrics synced from NeonCRM to Klaviyo: **Made Contribution** and **Registered for** **Event**.

![Metrics page in Klaviyo showing NeonCRM metrics Made Contribution and Registered for Event](https://klaviyo.zendesk.com/hc/article_attachments/28722594432027)

Metrics and profile properties from NeonCRM are synced every 30 minutes.

### Made Contribution

This event is tracked when a supporter makes a contribution in NeonCRM. The event Klaviyo tracks includes all of the information NeonCRM collects, and you can filter and target **Made Contribution** events based on the following criteria:

- ****Anonymous Donation****
  Indicates whether or not this donor wishes to remain anonymous (Yes/No)
- ****Campaign End Date****
  End date of campaign (if available)
- ****Campaign Goal****
  Goal of campaign (if available)
- ****Campaign Name****
  Name of campaign
- ****Campaign Start Date****
  Start date of campaign (if available)
- ****Donation amount****
  Value of donation
- ****Donation Date****
  Timestamp of donation event
- ****Donation ID****ID associated with donation event
- ****Donation Solicitation Method****
  How the donation was solicited
- ****Donation Solicitor****
  The solicitor who assisted with this donation
- ****Donation Status****
  Transaction status of donation
- ****Donation Type****Type of donation (donation, pledge, pledge payment, match pledge)
- ****Donor Name****
  Typically used to indicate how the donor would like to be acknowledged publicly (if available)
- ****Donor Note****
  Note filled in by constituent when making donation (if any)
- ****Fund****To which fund (if any) the donation should be attributed
- ****Honor/Memory Full Name****
  Honoree for this donation (if any)
- ****Pledge Amount****
  Amount of donor pledge
- ****Pledge Status****
  Status of donor pledge
- ****Transaction ID****
  Transaction ID

### Registered for Event

This event is tracked when a supporter registers for an event in NeonCRM. The event Klaviyo tracks includes all of the information NeonCRM collects, and you can filter and target these events based on the following criteria:

- ****Campaign Code****
  Campaign code
- ****Campaign End Date****
  End date of campaign (if available)
- ****Campaign Goal****
  Goal of campaign (if available)
- ****Campaign Name****
  Name of campaign
- ****Campaign Start Date****
  Start date of campaign (if available)
- ****Event Admission Fee****Event admission fee
- ****Event Category Name****
  Event category name
- ****Event Code****
  Event code
- ****Event End Date****
  Event end date
- ****Event ID****
  Event ID
- ****Event Name****
  Event name
- ****Event Start Date****
  Event start date
- ****Fund****To which fund (if any) the event fee should be attributed

Klaviyo does not currently receive a "registered at" timestamp for each registered event. The timestamp shown for the event is when it is synced to Klaviyo.

### Customer Data

In addition to the 2 key event metrics Klaviyo syncs from NeonCRM, Klaviyo also syncs information about each contact/account you have in NeonCRM, both Individual Accounts and Organization Accounts. The default account properties that are automatically synced from NeonCRM are:

- Account Created Date/Time
- Account Type
- Address Line 1
- Address Line 2
- City
- Company Name
- Country
- Deceased
- Do Not Contact
- Email 1
- Email Opt-Out
- First Name
- Full Zip Code
- Individual Type
- Job Title
- Last Name
- Organization Type
- Phone 1
- Source
- Province
- State

Klaviyo also syncs all Custom Fields in NeonCRM surrounding a contact; these Custom Fields will appear as Custom Properties attached to a contact's Klaviyo profile.

![Profile information in Klaviyo showing associated NeonCRM contributions, contact information, and custom properties synced from NeonCRM such as account type and job title](https://klaviyo.zendesk.com/hc/article_attachments/28722556008347)

## Outcome

You’ve finished integrating NeonCRM with Klaviyo, added Klaviyo web tracking to NeonCRM, and verified your synced data. Now, you can personalize and target emails based on each Contributor's donation and event registration activity.

## Additional resources

- [Integration FAQ reference](https://help.klaviyo.com/hc/en-us/articles/115005253208)
- [How often integrations sync reference](https://help.klaviyo.com/hc/en-us/articles/115005253208)
