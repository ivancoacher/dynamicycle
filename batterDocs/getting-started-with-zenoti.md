<h1>Getting started with Zenoti</h1>

## You will learn

Learn how to integrate with Zenoti, a tool that assists beauty, wellness, and fitness brands with booking, scheduling, marketing, payments, reporting, inventory, and more.

## Before you begin

- This integration relies on Zenoti Webhooks and APIs, which require a subscription to Zenoti's Klaviyo Integration Package. To verify whether you have this package, access the Zenoti dashboard as the owner and navigate to ****Admin > Setup > App****. If you are unable to see this option in the sidebar, please contact your Zenoti CSM or Zenoti Support to confirm your subscription to the package.
- You must have Owner credentials in Zenoti to set up this integration.

## Integrate Zenoti with Klaviyo

### Generate a Zenoti API key

To integrate Zenoti with Klaviyo, you'll first need to generate an API key in Zenoti:

1. In your Zenoti account, navigate to ****Configuration > Integration > Apps****.
2. In the top right, select ****Add****.
3. On the next screen, enter the following information:
   - ****Name****
     Klaviyo
   - ****URI****
     (Leave blank)
   - ****Description****
     Klaviyo integration
   - ****Login User Type****
     Employee
   - ****Source App****
     ClientApp
4. Select ****Next****.
5. On the next page, scroll to the bottom and click ****Select All**** for both **JWT Groups** and **APIKEY Groups** columns, then select ****Next****.
6. On the next page, select ****Generate API Key****. Make sure to store this information somewhere secure for use in the next steps.
7. Select ****Finish****.

### Add the integration in Klaviyo

Next, add the integration in Klaviyo:

1. Log in to Klaviyo and select the ****Integrations**** tab.
2. Click ****Explore apps****.
3. Search for ****Zenoti**** and click the card.
4. On the next page, click ****Install****.
5. Paste your API key from Zenoti and click ****Connect****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38368623578011)
6. Review the permissions and click ****Allow****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38368577930267)
7. On the next page, copy the Webhook URL and save it somewhere secure for use later.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38368623583259)
8. Under **Email subscribers**, check ****Sync your Zenoti email subscribers to Klaviyo**** if you wish to do so.
9. If you selected the setting above, choose a Klaviyo list for these subscribers to be added to.
10. When you are done, click ****Save****.

### Create a Zenoti webhook

Lastly, you'll need to create a webhook in Zenoti:

1. Back in Zenoti, navigate to ****Configuration > Integration > Webhooks****.
2. Select ****Create a webhook****.
3. On the **Create a new webhooks listener** page, select all options under **Appointment**, **AppointmentGroup**, **Class** (if you are using classes), **Guest**, and **Invoice**, then click ****Next****.
4. On the next screen, enter the following information:
   - ****Name****
     Klaviyo
   - ****Description****
     Klaviyo/Zenoti Integration
   - ****Request Type****POST
   - ****URL****Paste the webhook URL copied from Klaviyo.
5. In the top right corner, click ****Complete****.

## Understand your Zenoti data

Klaviyo syncs many different events from Zenoti related to appointments and membership. We sync 1 year of historic Zenoti data.

To view your Zenoti data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. The metrics with a Zenoti icon represent all of the metrics synced from your Zenoti integration.
3. Filter this view to see only Zenoti metrics by using the filter selector next to the search bar.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38368577931675)

Learn more about [your Zenoti data](https://help.klaviyo.com/hc/en-us/articles/15752724401691).

## Segment customers using Zenoti data

You can use Zenoti’s metrics to segment customers and target them with a campaign. For example, you can create a segment of everyone who has activated a membership in the last 30 days and send a campaign to that segment.
![](https://klaviyo.zendesk.com/hc/article_attachments/38368623589659)

To create the example segment shown above:

1. Click the ****Audience**** dropdown in the left-hand navigation sidebar.
2. Click ****Lists & segments****.
3. Click ****Create List / Segment**** in the top right.
4. Select ****Segment****.
5. Name your segment and select tags if desired.
6. Under Definition, select **What someone has done (or not done) > Activated Membership > at least once > in the last > 30 > days**.
7. Click ****Create Segment****.

For this example, if you’d like to make sure the segment only includes people who activated a membership for the first time:

1. Click ****AND**** to add a new exclusive condition.
2. Add the condition: **What someone has done (or not done) > Activated Membership > equals > 1 > over all time**. This will exclude anyone who has activated a membership more than once

![](https://klaviyo.zendesk.com/hc/article_attachments/38368577934491)

## Use Zenoti data in flows

You can use Zenoti metrics to trigger flows. For example, use the Activated Membership metric to trigger a flow to send messages to someone immediately when they activate their membership. You can also use the flow to send a series of messages letting them know how to get the most out of their membership.

If you are using Zenoti to send email and SMS notifications, make sure to turn off messages that you would rather send through Klaviyo flows so that your customers aren’t receiving repetitive messages. See [Zenoti’s support documentation](https://help.zenoti.com/) for more information on how to disable email and SMS notifications.

To create a flow using Zenoti metrics:

1. Navigate to the ****Flows**** tab from the left-hand navigation sidebar.
2. Click ****Create flow**** in the top right.
3. Click ****Create from scratch**** in the top right.
4. Name your flow and select tags if desired.
5. Click ****Create Flow****.
6. In the flow builder, choose ****Metric**** as the trigger.
7. From the dropdown, select a Zenoti metric, such as **Activated Membership**, indicated by the Zenoti icon.
8. Click ****Done****.
9. Add time delays and messages relevant to the triggering action. For the Activated Membership example, you can create messages to:

1. Thank the customer for activating their membership.
2. Inform the customer about the benefits of their membership.
3. Send promotional material relevant to their membership.

10. Once your content is ready, click ****Update Action Statuses**** in the top right of the flow builder to set the flow live.

## Outcome

You've now integrated Zenoti with Klaviyo and learned about Zenoti data in Klaviyo, segmenting customers using Zenoti data, and using Zenoti data in flows.

## Zenoti API key expiry

Please note that Zenoti's API keys currently expire every 12 months and must be updated in Klaviyo for the integration sync to continue.

Every 12 months, you will need to create a new API key in Zenoti and re-integrate with Klaviyo following these steps:

1. Remove your current Zenoti integration in Klaviyo.

1. In Klaviyo, select the ****Integrations**** tab
2. Find Zenoti on the list of enabled integrations.
3. Click the triple dots, then select ****Remove integration****.

2. Re-integrate following the steps in this article.

## Additional resources

- Learn more about [Klaviyo-built integrations](https://help.klaviyo.com/hc/en-us/articles/115000256472).
- Learn [how often integrations sync data](https://help.klaviyo.com/hc/en-us/articles/115005253208).
- Learn about [data synced from the Zenoti integration](https://help.klaviyo.com/hc/en-us/articles/15752724401691).
