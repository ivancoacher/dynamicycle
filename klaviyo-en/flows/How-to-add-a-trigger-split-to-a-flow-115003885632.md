---
id: "115003885632"
title: "How to add a trigger split to a flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115003885632-How-to-add-a-trigger-split-to-a-flow"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:15Z"
language: "en"
---
## You will learn

A trigger split is a component in the visual flow builder that creates two distinct paths in a flow, branching based on a filter applied to the flow trigger. It is only available for metric- and price drop-triggered flows.

A trigger split is helpful if you want to create a single flow based on a given activity (e.g., **Started**C**heckout**) but then curate different content for recipients based on characteristics of that activity (e.g., the cart value). For example, for an abandoned cart flow triggered by a **Started Checkout** event, you can use a trigger split around cart value where high-value cart abandoners receive a discount, and lower-value cart abandoners do not.

This article goes over how to add, configure, and view the activity of a trigger split.

## Add and configure a trigger split

To add a new trigger split into a flow series:

1. From the left sidebar, drag the trigger split component and drop it where you would like to create this split. After you drop the trigger split component into your flow, you will automatically see YES and NO paths appear below it.
   ![Example of an unconfigured trigger split with YES and NO paths](https://klaviyo.zendesk.com/hc/article_attachments/28722594143899)

   If you insert a trigger split midway through a flow, by default, all components below that point will be placed on the YES path. If you'd like to automatically swap all components on the YES and NO paths of your split, click the ****Settings**** icon (three dots) and select ****Flip Split****.
2. Click on the split to view the details sidebar to define the logic for your trigger split. All key details related to your flow's trigger metric will be available for use in this split. First, choose a dimension you want to base your split on, then choose your value.

As you set the conditions for your split, keep in mind recipients who meet your conditions will go down the YES path and those who don't meet the conditions will go down the NO path.

## View trigger split activity

When individuals enter your flow, they are automatically queued in the ****Waiting**** tab for the first step. When an individual reaches a split in a flow, they will wait at this split until the scheduled evaluation time arrives. After a recipient is evaluated at a split, they will then be scheduled for the first step down the appropriate YES or NO path.

You can click on any trigger split and view the details sidebar to see who is queued to be evaluated, along with the scheduled time of this evaluation. Recipients are scheduled for these components based on the time delay directly before it.

You will also see a snapshot of how many people are waiting and how many have been evaluated to go down the YES and NO paths.

![In the left sidebar you will see the trigger split activity log which shows how many profiles are waiting or went down the YES or NO paths.](https://klaviyo.zendesk.com/hc/article_attachments/28722594146587)

To dive deeper into these metrics and view who, specifically, is falling into these buckets, click ****View details.**** You will be taken to an ****Evaluation Activity****page. To return to the main flow canvas, click ****Done**** in the upper right-hand corner.

![The trigger split activity page has tabs for profiles that are waiting to go through the split as well as those that went down the YES and NO paths.](https://klaviyo.zendesk.com/hc/article_attachments/28722555691035)

## Additional resources

- [How to add a conditional split to a flow](https://help.klaviyo.com/hc/en-us/articles/115003872171)
- [How to rejoin and disconnect a split](https://help.klaviyo.com/hc/en-us/articles/360002419512)
- [How contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091)