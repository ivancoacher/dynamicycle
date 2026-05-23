---
id: 15348624462747
title: "Getting started with Mindbody"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15348624462747-Getting-started-with-Mindbody"
section: "Mindbody"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: en
---

## You will learn

Learn how to integrate with Mindbody, a tool that assists health and wellness brands with booking, scheduling, marketing, payments, reporting, and more.

Email consent is synced from Mindbody to Klaviyo. Please note that we do not sync SMS consent from Mindbody.

## Integrate Mindbody with Klaviyo

1. In Klaviyo, select the ****Integrations**** tab.
2. Click ****Explore apps**** in the top right.
3. Search for **Mindbody**, click the card, and click ****Install****.
4. Input your Mindbody site ID (also known as a client ID) and click ****Connect to Mindbody****.

   - If you need help finding this ID, check out Mindbody's help center article on [how to find my client ID](https://support.mindbodyonline.com/s/article/206398178-How-do-I-find-my-Client-ID?language=en_US).
5. If you have multiple site or client IDs, you can input them as a comma-separated list.
6. Next, click ****Generate Activation Links****.
7. Click the generated link(s) to activate your sites, and follow the instructions in Mindbody.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28716056289435)
8. After all sites have been activated (with the activation statuses showing as green), navigate back to Klaviyo. It may take a few minutes for the statuses to turn green.
9. Check the box to sync Mindbody email subscribers to a Klaviyo list, and then select a list from the dropdown.
10. Click ****Connect**** and you'll see what information will pass between Mindbody and Klaviyo.
11. To continue with the integration, select ****Allow****. You’ll be redirected to the page where you will be able to see all of your integrations.

    You cannot add more site/client IDs without re-integrating. If you ever need to add another site ID:
12. In Klaviyo, select your account name in the lower left. Then, click ****Integrations.****
13. Find **Mindbody** on the list and click the 3-dot menu.
14. Select ****Remove integration****, then confirm in the modal.
15. Re-integrate following the instructions above and include all site IDs.

- Note that when re-integrating, you must wait for the activation statuses for the site IDs from your previous installation to turn green. Then, only click the activation links for any new site IDs you've added.
- If you receive an error in Mindbody, exit and try again.

## Understand your Mindbody data

Klaviyo syncs both customer profiles and different events from Mindbody related to appointments and membership.

To view your Mindbody event data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account. The metrics with a Mindbody icon represent all of the metrics synced from your Mindbody integration.
3. Filter this view to see only Mindbody metrics by using the filter selector next to the search bar.

![](https://klaviyo.zendesk.com/hc/article_attachments/37303645882779)

Please note that only the metrics you use in Mindbody will sync to Klaviyo, so you may not see all of the metrics listed above in your account. Learn more about [your Mindbody data](https://help.klaviyo.com/hc/en-us/articles/15344283585819).

## Segment customers using Mindbody data

You can use Mindbody’s metrics to segment customers and target them with a campaign. For example, you can create a segment of everyone who has activated a membership in the last 30 days and send a campaign to that segment.

To create the example segment shown above:

1. Click the ****Audience**** dropdown in the left-hand navigation sidebar.
2. Click ****Lists & segments****.
3. Click ****Create New**** in the top right.
4. Select ****Create segment****.
5. Name your segment and select tags if desired.
6. Under **Definition**, select ****What someone has done (or not done)**** > ****Activated Membership**** > ****at least once**** > ****in the last**** > ****30**** > ****days****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37303645885595)
7. If you want this to only include people who activated a membership for the first time:

   - Click ****AND**** to add a new exclusive condition.
   - Add the condition ****What someone has done (or not done)**** > ****Activated Membership**** > ****equals**** > ****1**** > ****over all time****. This will exclude anyone who has activated a membership more than once.![](https://klaviyo.zendesk.com/hc/article_attachments/37303645887515)
8. Click ****Create segment****.

## Use Mindbody data in flows

You can use Mindbody metrics to trigger flows. For example, you can use the **Activated Membership** metric to trigger a flow to send messages to someone immediately when they activate their membership. You can also use the flow to send a series of messages letting them know how to get the most out of their membership.

If your Mindbody package includes the ability to send automatic emails, make sure to turn off emails that you would rather send through Klaviyo flows so that your customers aren’t receiving repetitive messages. See [Mindbody’s support documentation](https://support.mindbodyonline.com/) for more information on how to disable automatic emails.

To create a flow using Mindbody metrics:

1. Navigate to the ****Flows**** tab from the left-hand navigation sidebar.
2. Click ****Create flow**** in the top right.
3. Click ****Build your own**** in the top right.
4. Name your flow and select tags if desired.
5. Click ****Create flow****.
6. In the flow builder, choose the ****All triggers**** tab.
7. From the dropdown, select a Mindbody metric, such as ****Activated Membership****, indicated by the Mindbody icon.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37303645889051)
8. Click ****Save****.
9. Add time delays and messages relevant to the triggering action. For the **Activated Membership** example, you can create messages with content such as:

   - Thank the customer for activating their membership.
   - Inform the customer about the benefits of their membership.
   - Send promotional material relevant to their membership.![An example of a flow triggered by the Activated Membership metric with emails sent regarding the guest's membership](https://klaviyo.zendesk.com/hc/article_attachments/28716056282395)
10. Once your content is ready, [set your flow live](https://help.klaviyo.com/hc/en-us/articles/360048376172).

## Outcome

You've now integrated Mindbody with Klaviyo and learned about Mindbody data in Klaviyo, segmenting customers using Mindbody data, and using Mindbody data in flows.