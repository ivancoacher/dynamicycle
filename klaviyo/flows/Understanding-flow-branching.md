---
id: 115003883992
title: "Understanding flow branching"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115003883992-Understanding-flow-branching"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:14Z"
language: en
---

## You will learn

Learn how flow branching helps you personalize flows so that you can send individuals down different parallel paths depending on what you already know about them.

Flows allow you to automate timely touchpoints with your contacts without losing any of the relevance and personalization required to build an impactful marketing strategy. For example, an abandoned cart flow doesn't just send a generic follow-up email to all cart abandoners — using Klaviyo's default abandoned cart flow, all shoppers will receive an email personalized with each item they left behind.

Flow branching helps you take this personalization to the next level. Klaviyo supports 2 unique splits that offer powerful ways to branch your flows.

## The trigger split and conditional split

With both the trigger split and conditional split components, you create a logical statement that will either be true or false for each recipient entering your flow. In this way, these splits look similar to flow filters and they use the same logic you see in our segment builder. Unlike with flow filters and segments, however, with splits aren't keeping certain people in your flow and completely filtering the rest out — you are instead creating 2 parallel paths for these recipients where you can better customize the journey for each group.

In the visual flow builder, these splits are a configurable component. After you define your split, you will then see a YES and NO path on your canvas. Those who meet the definition of your split (where the statement evaluates true) will go down the YES path, while those that don't meet this definition (the statement evaluates false) will go down the NO path.

When using splits, it's important to think about the placement of your time delays. For instance, if you want to change the time someone receives a message depending on what path the profile goes into, place a time delay directly after the split in each branch. However, you may want to split based on whether someone performs a certain action within a given timeframe, such as waiting a week to see if someone placed an order before sending an email. In this case, the time delay must go before the split.

### Trigger split

The [trigger split](https://help.klaviyo.com/hc/en-us/articles/115003885632) component creates 2 distinct paths in your flow, branching based on a defined characteristic of the trigger. Trigger splits branch flows at the event level, meaning only metric and price drop flows can have trigger splits.

For example, for an abandoned cart flow triggered by a **Started Checkout** event, you can create 2 parallel paths in your flow split around a shopper's cart value — where high-value cart abandoners receive an email with a discount, and lower value cart abandoners do not.

Trigger splits are only supported in event-triggered flows, where the flow is triggered off a given event metric in your account. This component is not available in list or segment-triggered flows.

### Conditional split

The [conditional split](https://help.klaviyo.com/hc/en-us/articles/115003872171) component creates 2 distinct paths in your flow, branching based on defined recipient profile properties and/or activity.

For example, for a welcome series, you can create 2 parallel paths in your flow split around whether a recipient has purchased from you before in the past — existing customers may not need the same introductory content you might otherwise send to new subscribers that have never bought before.

## Best practices

### Abandoned cart flow

Let's say we'd like to create unique paths for those that have over a certain value left behind in their cart.

![Example of a trigger split that checks for 'value is less than 100'](https://klaviyo.zendesk.com/hc/article_attachments/28711661308443)

For those who left behind high-value carts, you may want to offer a greater incentive for recovery — for example, free shipping, or a percentage off their order if they complete their purchase. For shoppers that left less valuable carts behind, you certainly want to follow up, but you may not want to offer a discount given the expected ROI.

By adding a trigger split into an abandoned cart flow, you can immediately create 2 paths for cart abandoners based on their cart. This data point (cart value) is captured in the **Started****Checkout** event that serves as the flow's trigger.

### Post-purchase flow

Let's say we'd like to create unique paths for first-time buyers and repeat purchasers in our post-purchase flow.

![Example of a flow with 2 conditional splits forming 3 branches](https://klaviyo.zendesk.com/hc/article_attachments/28711673466523)

When someone buys from you, this is a great time to reach out and strengthen your relationship.

When a customer buys from you for the first time, it is important to recognize they've just gone through a process of discovering your business, evaluating your products, and making a decision to purchase from you. Follow-up that validates this choice and fosters a positive customer experience is essential.

Those who place an order but have already ordered before in the past are farther along in their relationship with you. In the customer lifecycle, you're working to retain them and inspire them to become not only loyal customers but also loyal promoters and advocates. Your content in a post-purchase series should be different for these repeat purchasers than for your first-time buyers.

By adding a conditional split within a post-purchase flow, you can increase your engagement with customers the first time they buy while also nurturing your repeat customers strategically based on where they are at in their lifecycle with you.

### Browse abandonment

In your browse abandonment flow, you may want to create unique paths for those who viewed under 3 products in the last several days and those who viewed more than 4 different items.

![Example of conditonal split which checks 'Has Viewed Product is greater than 3 in the last 5 days'](https://klaviyo.zendesk.com/hc/article_attachments/28711661314459)

There are 2 key types of visitors to your website: those who know exactly what they want when they get there, and those who are there to browse. Targeting your site visitors with the right messaging based on their browsing behavior can yield high returns.

Those who only visited a single product page may have arrived through a direct search or otherwise knew how to land right where they wanted — your follow-up should focus mainly on that specific item, with the goal to get that shopper to come back and buy it (or a similar recommended item).

Those who viewed over 4 items, on the other hand, may be window shopping. Don't focus as much on the most recently viewed individual item, but use this as a chance to promote your most popular items, show more of a specific collection, or provide social proof for why this shopper should come back and take a second look at your store. The stakes are higher to spark interest in what you have to offer more broadly, as the visitor hasn't indicated they know exactly what they want.

If you create a browse abandonment series and add a conditional split to target these 2 primary types of visitors, you can put your data to work early to drive deeper engagement starting with the very first page view.

## Troubleshooting

If a flow branch is not behaving as expected, such as if profiles are going down the wrong path, check the following:

### Make sure that the split has a condition set up

An unedited split will show a warning message asking you to finish setting it up. Profiles will default to going down the YES path if the split has no condition.
![](https://klaviyo.zendesk.com/hc/article_attachments/28711661316251)

Click on the split to edit its condition in the settings sidebar.

### Make sure there is enough time for the split to check the profile

If you're encountering problems where your conditional split fails to evaluate actions like profile clicks or data additions such as custom properties, it's often because there isn't sufficient time between the action processing or data being added to the customer profile by the time the customer meets the conditional split.

In order to make sure there's enough time before your customers are evaluated by the conditional split, you will need to add a time delay right before the conditional split. For example, if you want to add a conditional split to filter customers who clicked a link in your email, there needs to be a long enough time delay to allow the customer a chance to click. If the customer clicks after they were already evaluated by the split, they will go down the path for customers not clicking the link.

![](https://klaviyo.zendesk.com/hc/article_attachments/28711673477147)

If you are seeing profiles going down the wrong path, we recommend reviewing when the customer took the action or when the data was added to their profile relative to when they went through the conditional split. To view when the customer went through the split, click the conditional split and select ****View details**** in the top right. Next, open the profile you want to review and compare the timestamp of when they took the action you are evaluating. If you are reviewing when data was added to the customer profile, such as a custom property, you will need to compare when the action took place that added the property to their profile.

### Make sure that the YES and NO paths have the correct messages

If you accidentally put messages for the YES path in the NO path or vice versa, drag and drop individual messages into the correct path. If all messages are in the wrong path, flip the split by clicking the action button on the right of the split and selecting ****Flip split****.

When you flip a split, all components on the YES path will be switched with those on the NO path. Your components will remain in the same order and scheduling will remain the same.

Any recipients already scheduled and waiting will not be impacted. Only new people entering your flow will be scheduled on the flipped paths.

![](https://klaviyo.zendesk.com/hc/article_attachments/28711661318939)

### Make sure that the condition of the split says exactly what you intended

Click on the split to view the settings sidebar. Review the split conditions to confirm that it is set up to check for exactly what you intended. For example, if you want to check if someone has placed an order at any point in the past, make sure the condition is set to ****over all time**** and not ****in the last 30 days****, which is the default setup.
![](https://klaviyo.zendesk.com/hc/article_attachments/28711661322523)

## Additional resources

Find out more about flows:

- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [Understand how contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091)
- [How to rejoin a flow split](https://help.klaviyo.com/hc/en-us/articles/360002419512)