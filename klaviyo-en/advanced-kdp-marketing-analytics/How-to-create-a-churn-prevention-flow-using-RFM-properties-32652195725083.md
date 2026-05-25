---
id: "32652195725083"
title: "How to create a churn prevention flow using RFM properties"
source_url: "https://help.klaviyo.com/hc/en-us/articles/32652195725083-How-to-create-a-churn-prevention-flow-using-RFM-properties"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:38Z"
language: "en"
---
## You will learn

Learn how to build a churn prevention flow based on RFM properties to target customers who are extremely lapsed. Retention flows are useful drivers in helping to win back customers, reaching them at the right time with the right message. You can automatically reach these subscribers at the point in which their customer group changes, potentially decreasing revenue and churn risks.

## Before you begin

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Create a churn risk prevention flow

To create a churn risk prevention flow, you'll first need to create a segment of profiles in the **Inactive** RFM group to use as the trigger for your flow.

### Create your segment

If you have not already done so, you will first need to create a segment that includes your Inactive customers. To create this segment:

1. If you are an Advanced KDP customer, navigate to ****Advanced KDP**** > ****Intelligence**** > ****Customer insights**** > ****RFM analysis****. Alternatively, if you are a Marketing Analytics customer navigate to ****Marketing Analytics**** > ****Customer insights**** > ****RFM analysis****.
2. Scroll to find the **RFM Segments** card and select ****Create segment****.
   ![Create segment button on RFM card](https://klaviyo.zendesk.com/hc/article_attachments/32672459322651)
3. Name your segment and apply any tags if relevant.
4. Set the following definition for your segment:

   Properties about someone > **Current RFM group** equals **Inactive**
   ![Segment of profiles in inactive RFM group](https://klaviyo.zendesk.com/hc/article_attachments/32672450004763)
5. Optional: The **Inactive** RFM group includes profiles that have made at least 1 purchase in the past. If you’d like to target customers who have purchased a specific number of times in the past (e.g., only one-time buyers), but are now in the inactive group, you can add the following condition to your segment:

   What someone has (or has not done) > **Person has Placed Order** equals X over all time

### Set up your flow

You can quickly create a churn prevention flow using the prebuilt flow in the flow library.

1. Navigate to the **Flows** tab.
2. Click ****Create Flow****.
3. Search for and select ****Churn Prevention**** in the flow library.
   ![Churn prevention flow in flow library](https://klaviyo.zendesk.com/hc/article_attachments/32672459333531)
4. Name your flow and select the segment you just created for inactive RFM profiles.
5. Select ****Create flow****.
6. Customize your flow emails.
7. Optional: if you want to add additional messages to your flow, add another time delay between them. Make sure this is at least 2-3 days after your last message.
8. When you are done creating your flow, click ****Update status**** in the upper right and select **Live**. If you’d like to manually approve sends to each profile that enters the flow, select the **Manual** status.
9. Once you have set your flow status, click ****Save****.

## Additional resources

[Getting started with Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059)

[How to strategically use RFM properties in campaigns and flows](https://help.klaviyo.com/hc/en-us/articles/18194102384539)