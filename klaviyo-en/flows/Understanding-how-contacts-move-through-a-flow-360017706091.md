---
id: "360017706091"
title: "Understanding how contacts move through a flow"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360017706091-Understanding-how-contacts-move-through-a-flow"
section: "Understand flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:43Z"
language: "en"
---
## You will learn

Learn how contacts move through a flow. Flows are automated Klaviyo workflows that are set in motion by an initial trigger and then include one or more steps. Flows can be built to send timely communications to recipients, or they can simply apply certain actions, like [updating a specific field on a profile](https://help.klaviyo.com/hc/en-us/articles/360001768432-Update-Profile-Property-Action).

This guide explains how contacts will move through a flow, including:

- How recipients are scheduled for flow messages
- What happens when you update a time delay in an active flow
- How adding a new step affects flow recipients
- What happens when you reorder the steps in an active flow
- What happens when you delete a step in an active flow

## How recipients are scheduled for flow messages

When someone new enters a flow after qualifying based on the flow's trigger, they will immediately be scheduled for the first step in the series.

This first step could be an action, like an email, or it could be a logic assessment, like a conditional split.

- If there is no time delay before this first step, you will see the recipient quickly move through the step and be scheduled for the next step.
- If you have a time delay before this first step, the recipient will remain in a **Waiting** area until the scheduled time arrives. The "scheduled" state for a recipient is the Waiting state.

A recipient is only scheduled for one step in a flow at a time if the flow is live.

If multiple action steps follow each other without time delays between, they will all occur around the same time. This can be useful for non-message actions such as profile property update or list update actions, but it's best practice to put time delays between messages.

Let's say your flow is set up to send Email #1 in a flow after 1 hour, and Email #2 after 1 day. Someone new entering the flow will be in the **Waiting** bucket for Email #1 until an hour passes.

After this person receives Email #1, they will immediately be scheduled for Email #2. Only after this person moves past Email #1 will you see them will move to the **Waiting** bucket for Email #2.

![An example of a basic flow with a 1 hour delay followed by Email #1, then a 1 day delay followed by Email #2](https://klaviyo.zendesk.com/hc/article_attachments/28717380738587)

If you have an integration that doesn't sync immediately: Note that qualified profiles will still be scheduled for the first step in a flow as long as the information for the triggering event is synced into Klaviyo within four hours of the event occurring or, if a time delay is the first step after the trigger, as long as the sync falls within the timeframe of the time delay — whichever comes last.

If the difference in the synced (i.e., recorded) time and the actual time for an event is greater than both the four-hour default window and the time delay, they will be skipped from the flow. You can refer to [how often your integration syncs data into Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005253208).

## How changing message template or content affects received messages

Flows will use whatever is the current version of a message at send time. In other words, if you change the template and content of a message, whoever is currently scheduled to receive that message will receive the updated version when the message finally sends. This also applies to recipients with the **Needs Review** status for manual or previously manual messages.

## How a message in draft affects a recipient's progress

If all messages in a flow are set to draft, no one will enter the flow until at least one message is set to live or manual. Once people enter a flow, if a message is set to draft status, it does not stop the recipient from moving through the flow. Flow recipients will skip any draft messages and move onto the next step. They will not be scheduled for any draft messages nor will they show in the analytics for the message. If there are no steps after the draft message, they will exit the flow.

If you'd like to schedule someone for a message, but want to wait indefinitely before sending it, set the message status to manual.

## How a message in manual affects a recipient's progress

If a message is set to manual status, recipients will be put in the **Needs Review** list for the message, but it does not stop the recipient from moving through a flow.

For example, say your flow setup is similar to the one shown below, with the first message in manual mode, followed by a 3 day time delay and then the second message.

![An example of a flow with the first message after the trigger set to Manual status followed by a 5 day time delay and a second message](https://klaviyo.zendesk.com/hc/article_attachments/28717387001371)

In this case, once recipients hit the **Needs Review** stage for the first message, they'll continue in the flow. Thus, after 3 days, they'll receive the second email, even if you haven't sent them the first yet.

## Updating the time delay in an active flow

If you update the time delay before a step, those already in the flow who haven't made it to that step yet will automatically be scheduled according to the updated timing when they do get there.

Let's say you have a flow where Email #1 is set to send after 2 days, and Email #2 is set to send 5 days later.

![An example of a flow where Email #1 is set to send after 2 days, and Email #2 is set to send 5 days later](https://klaviyo.zendesk.com/hc/article_attachments/28717380749467)

Becky enters a flow and is waiting to receive Email #1 the next day. While she's scheduled for Email #1, you update Email #2 to send 2 days later (instead of 5 days later). As soon as Becky receives Email #1, she'll be scheduled for Email #2 according to the updated timing and receive this email 2 days later.

![An example of a flow where Email #1 is set to send after 2 days, and Email #2 was changed from 5 days to 2 days later](https://klaviyo.zendesk.com/hc/article_attachments/28717387007131)

For this same flow, however, Joe entered a few days before Becky and is already in the ****Waiting****bucket for Email #2. When you update the time delay before this email, Joe will not be rescheduled to receive the flow sooner. He will still receive this second email 5 days after the first because he was scheduled for this second email before you made the timing update.

If you update the time delay before a step, those already scheduled in the ****Waiting**** bucket will not be rescheduled.

Note that if you set a time delay component to wait until a specific day, you will not be able to view the expected number of days for any emails and SMS that come after this delay. Suppose you have a time delay that waits for 5 days and only sends on a Monday or Friday. In this case, Klaviyo cannot determine when a recipient will receive the following message, as each person in the flow is going to have a different number of days before they are sent the message.

## Adding a new step into an active flow

If you add a new step to an existing flow series (e.g., an email, an update profile property action, a split, etc.), recipients currently scheduled at any previous step will automatically be scheduled for the new step in the sequence.

For example, let's say you have a welcome series with 3 emails spanning 1 week after someone subscribes. You want to make this series longer and add 3 more emails at the end. Now, the flow spans 2 weeks after someone subscribes.

Recipients currently in your sequence will automatically be scheduled for the new emails. You do not need to add past profiles to your flow or take any other action. This is only true for recipients who are still moving through the flow.

Recipients who already exited the flow prior to these new emails being added will not be scheduled to receive them. In this case, you would need to [add past profiles](https://klaviyo.zendesk.com/hc/en-us/articles/360049924272) to the flow in order to ensure that those who already exited the flow, but are still within the proper timeframe for your newly added emails, receive the new emails in the proper sequence.

## Reordering steps in an active flow

Contacts are scheduled for all steps in a flow one-at-a-time, and they must move through one step before being scheduled for the next.

This means for those moving through a flow, any changes made to steps still ahead of them will impact their journey.

However, if someone is already scheduled (in **Waiting**) for a given step, they will remain scheduled for that step even if you move it elsewhere in the sequence. Additionally, say they are scheduled (in **Waiting**) for a first email or SMS, and you adjust the flow to add steps before this first touch, they will not receive these above steps unless you add past profiles.

For example, let's say you have a flow series with four emails:

- Becky received Emails #1 and #2, and is currently scheduled for Email #3. While Becky is still scheduled for Email #3, you drag this email to the top of the flow.
- New contacts entering the flow will get this email first, but Becky will still get it at her originally scheduled time.
- After Becky receives Email #3, we will attempt to schedule her for the next step (Email #1). **If a contact has already moved through a step in a sequence and arrives at it again because you've reordered the steps, the contact will not be scheduled a second time.** In this case, you placed Email #3 before Emails #1 and #2, but because Becky already received Emails #1 and #2 she won't be scheduled for them again.
- Becky will be scheduled to receive Email #4 because it is the next email in the sequence that she has not already received.
- The only way that Becky can receive any new emails added before the next email she is scheduled for is to add past profiles.

## Deleting steps in an active flow

If you delete a step that has contacts waiting, those contacts will move to the next step in your flow. When deleting a step from your flow, you will also be deleting any data associated with that step as well. For emails or SMS, you can keep that data by setting the message mode to ****Draft****. Contacts will not be scheduled for messages in draft mode, and will move on to the next step in your flow.

The only exception to this is if:

- The step being deleted is a split (conditional or trigger)
- There's no delay directly before the split

In this case, when the split is deleted, any contacts in waiting will be removed from the flow. Otherwise, they'll continue on to the next step.

## Review profile progress through a flow

There are two ways to review profiles going through a flow:

- Reviewing profiles that have gone through a specific step within your flow.
- Reviewing profiles who have completed a flow.

To view profiles who have gone through specific steps within your flow:

1. In the flow builder, click the step you want to review and select ****View details**** on the right hand side.
2. Click the **Recipient activity** tab to view all profiles who went through this step. You can view profiles who are waiting to go through, recipients that have successfully went through, and profiles who have skipped this step.

![](https://klaviyo.zendesk.com/hc/article_attachments/28717387009179)

To track profiles who complete a flow, you will need to use the update property action at the end of your flow to tag customers who have completed your flow. If you have multiple paths customers can go down, you will need to add an update property action to the end of each path.

1. In the flow builder, drag and drop the ****Profile property update**** block to the end of your flow.
2. Click ****Add step**** and under the first dropdown, select ****Create new property****.
3. Under property label, add the name of the property you want to use to track when profiles end the flow and change text to boolean. This will allow you to set the property as true or false.
4. Once profiles have been tagged with this custom property, you will be able to create a segment of all profiles who have ended the flow and were tagged by your property. If no one has been tagged yet, you will not be able to create the segment.

If your flow has flow filters on the trigger of the flow, and if profiles fail those flow filters, they will skip the profile property update action. To avoid this from happening, you can remove the flow filters from the trigger of your flow and add them directly to the emails or SMS messages within your flow.

1. Click the email or SMS message within your flow.
2. On the right side under **Settings**, click ****Add filter**** and re-add the filters to every email or SMS message within your flow. This way, the filters are checked before each email is sent but will not impact the profile property update action.

## Additional resources

- [Understanding the timing of a flow](https://help.klaviyo.com/hc/en-us/articles/360046164352-Understanding-the-Timing-of-a-Flow)
- [Understanding flow branching](https://help.klaviyo.com/hc/en-us/articles/115003883992-Introduction-to-Flow-Branching)
- [Understand flow triggers and filters](https://help.klaviyo.com/hc/en-us/articles/115002779051-About-Flow-Triggers-and-Filters)
- [Automating the customer journey with flows](https://academy.klaviyo.com/automating-the-customer-journey-with-flows)