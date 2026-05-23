---
id: 115002779231
title: "Understanding how adding past profiles works in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002779231-Understanding-how-adding-past-profiles-works-in-Klaviyo"
section: "Add past profiles to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:13Z"
language: en
---

## You will learn

Learn how to add past profiles to a flow which allows you to queue people for flow actions retroactively. This process is formerly known as back-population. This is useful when you create a new flow, as adding past profiles allows you to populate contacts into your flow that would have been queued in real-time had the flow existed earlier.

In this article, we explain details about adding past profiles to different flows in Klaviyo. For step-by-step instructions, learn [how to add past profiles to a flow](https://klaviyo.zendesk.com/hc/en-us/articles/360049924272).

## About adding past profiles

Who is queued when you add past profiles to a flow depends on the flow’s timeline as well as whether your flow trigger is a metric, list, or segment. Individuals will only be queued at actions when the action's status is manual or live.

Flows work in real-time, so if you add another step to a flow, you do not need to add past profiles if you only want recipients who are still in the flow (i.e., have not gone through the last step yet) and who haven’t passed the new step to go through it.

Due to how they queue recipients, adding past profiles is not available for date property and price drop flows.

Since back in stock flows are best without time delays (and the back in stock delay functions differently), adding past profiles won't have any effect. If you wish to reach out to those in a back in stock report, we recommend sending a campaign.

That said, if your back in stock flow does contain a time delay, adding past profiles will work similarly to how other metric-triggered flows add past profiles. The only difference is that with back in stock flows, someone in the waiting queue will be notified as soon as the product is back in stock.

## Metric-triggered flows

When you add past profiles to a metric-triggered flow, recipients will move through the flow relative to when they performed the triggering action. Adding past profiles does not cause a flow to send out messages immediately; instead, it will simply insert recipients at the step where they would be if the flow was live when they performed the triggering action. They’ll then [move through the flow](https://help.klaviyo.com/hc/en-us/articles/360017706091) like any other recipient.

Flow filters will be checked at each step of the flow while adding past profiles similar to when a profile is moving through a flow normally. Note that flow **Re-entry criteria** is only checked when someone enters the flow organically, so it will not be checked when adding past profiles.

Profiles that were in the flow and skipped a message previously will not be scheduled for the same message when adding past profiles, but they can be scheduled for new messages that were added to the flow.

Since adding past profiles for metric-based flows depends on where someone falls in the flow’s timeline, you must include at least one time delay. (Adding a flow filter before adding past profiles will not add any new recipients.) If someone falls outside the flow’s timeline (e.g., if the flow lasts for 10 days but someone performed the action 15 days ago), they will not be added to the flow.

The **Add Past Profiles** modal for metric-triggered flows displays an estimate of how far back profiles will be added based on the duration of the flow.

![Add past profiles modal that explains how adding past profiles works](https://klaviyo.zendesk.com/hc/article_attachments/28715968360219)

Suppose you want to add past profiles to a winback flow triggered by the **Placed Order** event. Directly after the trigger, you have a time delay for 75 days, followed by an email, a time delay for 10 days, and then another email.

![Customer windback flow with 75 and 10 day delays](https://klaviyo.zendesk.com/hc/article_attachments/28715961798811)

When you add past profiles to this flow, Klaviyo will insert everyone who purchased from you between 1 and 75 days ago into the first time delay. Recipients will then wait until the full 75 days pass from the time they performed the action. For instance, someone who purchased 10 days ago will have to wait 65 more days before they get the first email, whereas someone who placed an order 70 days ago will only be in this time delay for five days.

Anyone who purchased between 76 and 85 ago will not get the first email and will move straight to second time delay. They’ll then wait for the rest of the 10 days before getting the second email.

If someone purchased more than 85 days ago, they won’t be added to this flow. The only way to send to them is to build a segment targeting this group and send them a campaign.

## ****List- and segment-triggered flows****

If recipients in a list-based flow are [skipped for any reason](https://help.klaviyo.com/hc/en-us/articles/115002779471-Troubleshoot-Flow-Sending#reviewing-skipped-recipients), adding past profiles will not re-queue these recipients for the flow. Once you've entered a list-based flow you cannot be re-queued for any flow message you have already received. The best way to reach customers that have been skipped for a list-based flow is to [clone the flow](https://klaviyo.zendesk.com/hc/en-us/articles/24898429283739) and add past profiles to the cloned flow.

List- and segment-triggered flows have two options for adding past profiles:

- Throughout the flow
- At the beginning

![Add past profiles modal for a metric-triggered flow](https://klaviyo.zendesk.com/hc/article_attachments/28715961790875)

### Schedule recipients throughout the flow

Adding past profiles relative to when a recipient was added to a list or segment is similar to how metric-triggered flows add past profiles. Recipients will be inserted into a flow at different points, depending on when they joined your list or segment.

Say that you have an SMS welcome series that lasts for 14 days with three messages spaced 7 days apart.

![Example SMS welcome flow with 3 messages and 7 day delays between](https://klaviyo.zendesk.com/hc/article_attachments/28715968371867)

If you add past profiles, anyone who subscribed to SMS in the last 14 days will be added to the flow. Those who subscribed between 1 and 7 days ago will be placed at the first time delay where they’ll wait until the full 7 days have passed. They’ll then follow the flow just like any other recipient. Those who subscribed between 7 and 14 days ago will do the same, but enter the flow at the second time delay.

![Example SMS welcome flow with 3 messages and 7 day delays between](https://klaviyo.zendesk.com/hc/article_attachments/28715968377627)

### Schedule recipients at the beginning

When you schedule recipients based on when you add past profiles, this treats recipients as if they just joined your list or segment. They’ll start at the very beginning of the flow and move through it one step at a time, like any other recipient.

Suppose you have a flow triggered when someone qualifies for your VIP segment. The flow lasts for 10 days and contains 3 messages spaced 5 days apart.

![Example VIP segment flow with 3 messages and 5 day time delays between them](https://klaviyo.zendesk.com/hc/article_attachments/28715968384411)

If you add past profiles via this option, everyone who qualifies for the flow (e.g., is in your VIP segment) will start at the trigger. Those who already went through the flow will not receive the same messages again, while everyone else will start at the beginning and move through it step-by-step.

## Adding past profiles with splits

When you add past profiles to a flow, Klaviyo will insert recipients at the point that aligns with when they performed the triggering action (unless you schedule recipients based on when you click add past profiles). Also, when you add past profiles to a flow that contains any splits (i.e., a conditional or trigger split), Klaviyo will re-evaluate which path a flow recipient belongs in.

Note that if a time delay is the last component in a flow path, and you place a new message after it, you will have to add past profiles. The reason is that Klaviyo uses time delays to queue recipients for the next action (SMS, email, notification, update profile property). If there's no action following the delay, recipients won't "wait" at the delay. Instead, they exit the flow, which is why adding past profiles is necessary.

Let’s say that you edit an abandoned cart flow, changing a trigger split that divides recipients based on if their cart value is at least $100. When you add past profiles, everyone whose cart value was less than 100, and thus no longer qualifies for the Yes path, will move to the No path.

![Example abandoned cart flow with a split that checks if the value is at least $100](https://klaviyo.zendesk.com/hc/article_attachments/28715961811739)

## Adding a new action to a flow

You do not need to add past profiles if you add a new message to the end of a flow (or a single path) and want those currently moving down that path to receive that message. You would only need to add past profiles to send to those who have either exited the flow or continued past the point of the new message. Let’s examine a few cases to understand how this works.

Note that if a time delay is the last component in a flow path, and you place a new message after it, you will have to add past profiles. The reason is that Klaviyo uses time delays to queue recipients for the next action (SMS, email, notification, update profile property). If there's no action following the delay, recipients won't "wait" at the delay. Instead, they exit the flow, which is why adding past profiles is necessary.

First, let’s say that Becky was just evaluated at a split, and you add new actions to the end of the path Becky is still moving down. Becky will automatically get scheduled for the new actions in sequence without you needing to add past profiles.

![Example split that checks if someone has placed an order since starting the flow](https://klaviyo.zendesk.com/hc/article_attachments/28715968390811)

John already completed the flow. If you add a new action at the end of the path John went down, you can add past profiles to queue him for the new message. However, this will only work if John hasn’t already passed the new step. For instance, if you added an email to send 10 days after the flow’s trigger, and John triggered the flow 20 days ago, he will not receive the new email. On the other hand, if Kara triggered the flow 9 days ago, she will get the new email.

![Example split that checks if someone has placed an order since starting the flow with message added to the NO path](https://klaviyo.zendesk.com/hc/article_attachments/28715968395163)

## Changing a time delay before adding past profiles

If you add, delete, or update the configuration of a time delay before adding past profiles, people who were already scheduled to receive an email will not be affected. However, any new people brought into the flow by adding past profiles will be affected.

For example, if someone is scheduled to receive an email after a 3 day delay and they are already in the waiting list, changing the time delay to 2 days and adding past profiles will not shorten the delay for those who were previously scheduled by the 3 day delay since the send schedule has already been determined for them. Anyone who enters the flow due to adding past profiles will be scheduled according to the new 2 day delay.

To adjust the send schedule for people already in the flow, cancel the email before you add past profiles:

1. Click the email you would like to cancel.
2. In the details sidebar, click ****View details****.
   ![View details button in the details sidebar](https://klaviyo.zendesk.com/hc/article_attachments/28715968379547)
3. In the **Recipient Activity** tab, find the recipient you would like to cancel the email for.
4. Hover over a specific profile and click ****Cancel.****
5. Alternatively, click ****Cancel All**** to cancel the email for all recipients currently waiting.
   ![The Cancel button found when viewing the activity queued messages for a message.](https://klaviyo.zendesk.com/hc/article_attachments/28715961793307)

Learn more from our article on [understanding how contacts move through a flow.](https://help.klaviyo.com/hc/en-us/articles/360017706091)

## ****Additional resources****

Read this article to find out [how to add past profiles to a flow](https://help.klaviyo.com/hc/en-us/articles/360049924272).

Learn more about flows in the following articles:

- [How to create a list-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003031652)
- [How to create a segment-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003040052)
- [How to create a metric-triggered flow](https://help.klaviyo.com/hc/en-us/articles/360003057151)