---
id: "115002775052"
title: "How to change a flow trigger"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115002775052-How-to-change-a-flow-trigger"
section: "Set up flow filters and triggers"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:36Z"
language: "en"
---
## You will learn

Learn how to create a copy of a flow in order to create a new version with a different trigger. A copy of the original flow must be created because once you have set the trigger for a flow, you cannot change it. Trigger filters, profile filters, additional email filters, and dynamic content in emails are all reliant on the specific trigger you set for a flow. Most likely, if you change the trigger for an existing flow, this will cause conflicts with your filters and content that are challenging to identify and correct.

While you cannot change a flow trigger directly, you can clone a flow and change the trigger for this new, cloned flow. Then, you can delete the previous flow.

![Instructional video of how to clone a flow and change the trigger](https://fast.wistia.com/embed/medias/qgxmoayc87/swatch)

## Clone a flow to change the trigger

There are several types of changes you might like to make:

- Connect a list-triggered flow to another list
- Change an event-triggered flow from one event to another
- Change a list-triggered flow to an event-triggered flow
- Change an event-triggered flow to a list-triggered flow

Cloning a flow allows you to tackle the first 2 scenarios on the above list.

When you clone a flow, you will have the option to edit the name for the cloned version as well as the trigger specifics. For a list- or segment-triggered flow, you can pick any other list or segment to trigger your cloned version. For an event-triggered flow, you can pick a different event to trigger your clone.

To clone a flow:

1. Navigate to the ****Flows**** tab and find the flow that you would like to change the trigger for.
2. On the right of the flow, click the ****Edit Flow**** button to reveal the dropdown and select ****Clone.
   ![Clicking the arrow next to the Edit Details button on the right side of a flow will show the Clone option](https://klaviyo.zendesk.com/hc/article_attachments/28713327408411)****
3. In the **Clone Flow**modal, choose a new trigger for the flow by selecting the **Trigger** dropdown. Change the name of the flow if desired.
   ![Clone Flow modal with a text box to edit the flow name and a dropdown that can be used to change the trigger](https://klaviyo.zendesk.com/hc/article_attachments/28713333043995)
4. After you clone a flow to update the trigger, you can delete the original flow. Only do this if you don't mind losing the historic analytics associated with it — the cloned version of a flow starts with a clean slate in terms of analytics.
5. On the ****Flows**** tab, find your original flow.
6. Click the ****Edit Flow****button to reveal the dropdown and select ****Delete.****

## Change a list-triggered flow to an event-triggered flow (or vice versa)

To change a list-triggered flow to an event-triggered flow, or vice versa, you cannot simply clone the flow. Instead, you'll have to create a brand new flow. You can speed up this process, however, by first saving all the flow emails as templates so they can be added into your new flow with a few clicks.

In our example, we're going to change a list-triggered flow to an event-triggered flow. Here are the steps to follow:

1. Open the flow builder for your list-triggered flow.
2. Next, [save all the emails as templates](https://help.klaviyo.com/hc/en-us/articles/115000102752#save-an-email-as-a-template). It is helpful to name these templates something clear so you can find them easily when you make your new flow.
   ![Clicking the arrow next to the Edit Details button on Message Content screen for a flow email will show the Save as Template option.](https://klaviyo.zendesk.com/hc/article_attachments/28713333053723)
3. Once you've saved all the emails associated with the flow, create a new flow by navigating back to the ****Flows****tab.
4. When you are building out the content for your new flow, find your previously saved templates by selecting  by choosing ****Email: saved**** when selecting a flow template.
5. Once you've done this for all the emails, you're safe to delete your original flow and use the new version with an updated trigger.

## Additional resources

Find out more about [flow triggers and filters](https://help.klaviyo.com/hc/en-us/articles/115002779051).

See how to [preview a flow trigger's setup](https://help.klaviyo.com/hc/en-us/articles/360028374111-).