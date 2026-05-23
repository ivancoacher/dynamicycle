<h1>Getting started with Thanx</h1>

## You will learn

Learn how to integrate with Thanx, a guest engagement platform for on-brand loyalty focused on access, exclusivity, and personalization.

Ensure you have a completed Thanx datashare agreement before installing this integration. For assistance, contact your Thanx representative.

## Integrate Thanx with Klaviyo

To integrate with Thanx:

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps****.
3. Search for **Thanx** and select the card.
4. Click ****Install****.
5. On the next page, enter your Thanx Merchant ID and click ****Connect****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36941375955995)
6. Review the permissions and select ****Allow****. You'll be redirected to Klaviyo.
7. Check the box to sync Thanx email subscribers to a Klaviyo list, and then select a list from the dropdown.
8. Check the box to sync Thanx SMS subscribers to Klaviyo, and select a list from the dropdown. We recommend keeping separate lists for email and SMS subscribers.
9. When you're done, click ****Save****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36949720268571)

You have now successfully integrated Thanx with Klaviyo.

## Update your Thanx integration

To update the integration in Klaviyo:

1. Log in to Klaviyo.
2. Select the Integrations tab.
3. Select ****Thanx****.
4. Click the ****Update**** button in the banner.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/49424451336219)
5. Review the permissions in Klaviyo and click Allow.
6. Review the permissions and select ****Allow****. You'll be redirected to Klaviyo.
7. Check the box to sync Thanx email subscribers to a Klaviyo list, and then select a list from the dropdown.
8. Check the box to sync Thanx SMS subscribers to Klaviyo, and select a list from the dropdown. We recommend keeping separate lists for email and SMS subscribers.
9. When you're done, click ****Save.****

![](https://klaviyo.zendesk.com/hc/article_attachments/36949720268571)

## Understand your Thanx data

Klaviyo syncs real time Thanx transaction data via the **Placed Order** and **Earned Reward**metrics.

To view your Thanx data:

1. In Klaviyo, click the ****Analytics**** dropdown in the left-hand navigation.
2. Select ****Metrics****. Here, you can view all the metrics in your account.
3. To filter this view to see only Thanx metrics, use the filter selector next to the search bar and select ****Thanx****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/49424479272091)
4. Click on a metricto view detailed metric info.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717994779547)
5. To view your Thanx objects (note: requires the latest version of the integration): Navigate to Content > Objects. Here, you can view all of the objects in your account. The objects with a Thanx icon represent all of the objects synced from your Thanx integration.

Learn more about [your Thanx data](https://help.klaviyo.com/hc/en-us/articles/19457831690139).

## Use Thanx data in segments

You can create segments in Klaviyo that include data from across metrics (**Placed Order, Earned Reward)** and objects (**Reward)**.

For example, using objects, you can create a segment of guests who have a reward that expires in the next 7 days:

1. Navigate to ****Audience > Lists & segments.****
2. Click ****Create New**** and choose ****Create new segment****.
3. Name your segment and select tags if desired.
4. Select the following definition and filter:
   1. Properties about someone > Reward (Thanx) > has
   2. where > CampaignRedeemableTo > in the next > 7 days
5. Click ****Create segment****.

![](https://klaviyo.zendesk.com/hc/article_attachments/49424451338267)

## Use Thanx data in flows

You can use Thanx metrics and objects to trigger flows, or sequences of automated actions. Klaviyo offers multiple pre-built flows using Thanx data. To view these pre-built flows:

1. In Klaviyo, select the Flows tab.
2. Click Create flow.
3. Filter by **Thanx** to see all Thanx flows.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/49424451339291)

You can also create your own flows from scratch. For example, you can send messages to someone immediately when they sign up for your loyalty program.

To create the flow:

1. Click the ****Flows**** tab from the left-hand navigation.
2. Click ****Create flow**** in the top right.
3. Click ****Build your own**** in the top right.
4. Name your flow and select tags if desired.
5. Click ****Create Flow****.
6. In the flow builder, choose ****Metric**** as the trigger.
7. From the dropdown, select ****Placed Order****(with the Thanx icon).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28718022542875)
8. Click ****Save****.
9. Add time delays and email messages relevant to the triggering action.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28718022549531)
10. Once your content is ready, click ****Update Action Statuses****in the top right of the flow builder to set the flow live.

You can also use your Thanx **Reward** object to trigger Flows. For example you can send a message to someone 3 days before their Reward is scheduled to expire.

To create the flow:

1. Click the ****Flows**** tab from the left-hand navigation.
2. Click ****Create flow**** in the top right.
3. Click ****Build your own**** in the top right.
4. Name your flow and select tags if desired.
5. Click ****Create Flow****.
6. In the flow builder, navigate to ****All triggers > Date property.****
7. From the dropdown, select ****Reward: CampaignRedeemableTo****from your Thanx integration.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/49424451340955)
8. Set the amount of time before the expiration date you want to send your message (e.g. 3 days) and the time of day you would like to deliver the message. Click ****Next.****
9. Click ****Save****.
10. Add time delays and email messages relevant to the triggering action.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/49424451343003)
11. Once your content is ready, click ****Review and turn on****in the top right of the flow builder to set the flow live.

## Outcome

You've now integrated Thanx with Klaviyo, learned about Thanx data in Klaviyo, and used Thanx data in flows.

## Additional resources

- [How to manage and distribute Thanx rewards via Klaviyo](https://help.klaviyo.com/hc/en-us/articles/48577674406683).
- Take our course on [enhancing restaurant guest relationships](https://academy.klaviyo.com/en-us/courses/enhance-restaurant-guest-relationships).
- Learn more about [Klaviyo-built integrations](https://help.klaviyo.com/hc/en-us/articles/115000256472).
- Learn [how often integrations sync data](https://help.klaviyo.com/hc/en-us/articles/115005253208).
