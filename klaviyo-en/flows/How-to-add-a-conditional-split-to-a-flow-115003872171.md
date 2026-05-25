---
id: "115003872171"
title: "How to add a conditional split to a flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115003872171-How-to-add-a-conditional-split-to-a-flow"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:14Z"
language: "en"
---
## You will learn

Learn how to add a conditional split to a flow that creates two distinct paths, branching based on defined characteristics of your recipients.

****What is a conditional split?****

A conditional split is a component in the visual flow builder that is helpful if you want to create a single flow but then curate different content for recipients based on what you already know about them (e.g., gender, location, past purchase history etc.).

For example, for a welcome series, you can use a conditional split to branch your flow based on whether or not a subscriber is already a customer. You may want to customize your content for new subscribers you want to convert to first-time buyers versus those that have already purchased from you in the past.

## Add and configure a conditional split

To add a new conditional split into a flow series:

1. Drag the conditional split component from the left sidebar and drop it where you would like to create this split.
2. Click on the split to view the details panel. Unconfigured splits will display a yellow warning label. Notice that **Yes** and **No**paths are automatically added bellow the split.
   ![An unconfigured split placed onto the flow canvas with the details sidebar open](https://klaviyo.zendesk.com/hc/article_attachments/28704476296859)
3. If you insert a conditional split midway into a flow, all components below that point will be placed on the YES path by default. If you'd like to automatically swap all components on the YES and NO paths of your split, click the settings icon (3 dots) and choose ****Flip split****.

   If profiles are already queued into a time delay and you add a new split right below the delay, the profiles that reached the time delay before the split was added will not be evaluated by the split and will go down the YES path by default.
4. In the details sidebar, you will be able to define the logic for your conditional split. The workflow here is the same as what you will find in the segment builder and when configuring flow filters. The options are:
   - What someone has done (or not done)
   - Properties about someone
   - If someone is or is not within the EU (GDPR)
   - Someone's proximity to a location
   - If someone is in or not in a list
   - If someone can or cannot receive marketing
   - Predictive analytics about someone
   - Random sample

****![](https://klaviyo.zendesk.com/hc/article_attachments/34445970181659)****

As you set the conditions for your split, keep in mind recipients that meet your conditions will go down the YES path and those that don't meet the conditions will go down the NO path.

When using a conditional split, it's important to think about the placement of your time delays. For example, if you want to split based on whether someone performs a certain action within a given timeframe (such as waiting a week to see if someone placed an order before sending an email), the time delay must go before the conditional split.

## View conditional split activity

When individuals enter your flow, they will automatically be queued in the ****Waiting****tab for the first step only. When an individual reaches a split in a flow, they will wait at this split until the scheduled evaluation time arrives. After a recipient is evaluated at a split, they will be scheduled down the YES or NO path as appropriate.

You can click on any conditional split and see who is queued to be evaluated, along with the scheduled time for this evaluation. Recipients are scheduled for these components based on the time delay directly before them.

To view conditional split activity:

1. Click on the conditional split in the flow builder.
2. In the details sidebar, you will see a snapshot count of how many people are waiting and how many have been evaluated YES and NO.
3. To dive deeper into these statistics and view those who fall into these buckets, click ****View details.****
   ![Statistics of the split in the details sidebar](https://klaviyo.zendesk.com/hc/article_attachments/28704476294811)

## Additional resources

- [How to add a trigger split to a flow](https://help.klaviyo.com/hc/en-us/articles/115003885632)
- [How to rejoin and disconnect a split](https://help.klaviyo.com/hc/en-us/articles/360002419512)
- [How contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091)