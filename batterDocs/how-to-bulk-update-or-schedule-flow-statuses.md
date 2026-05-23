<h1>How to bulk update or schedule flow statuses</h1>

## You will learn

Learn how to change the statuses of multiple actions in a flow simultaneously in the flow builder. This makes it simple to, for example, set an entire flow live in 1 click or pause all activity quickly by switching actions to manual or draft.

There are 2 options when updating flow statuses:

1. Update flow statuses immediately.
2. Schedule flow statuses to update at a specific date and time.

There are several reasons to schedule flow statuses to update at a specific date and time instead of immediately. Examples include:

- Setting a flow live for a promotional event that should switch to draft after the event ends.
- Deprecating an old flow and replacing it with a new one at a specific time.
- Temporarily setting a flow to manual while your store undergoes maintenance.

You can also schedule multiple status changes across different dates and times if needed.

Flow status scheduling is not available for date-property triggered flows.

## Understand how bulk status changes affect a flow

Before changing the status of a flow’s existing actions, understand what each status means when applied in bulk.

- All statuses are ****Live****
  The flow is fully live and messages will be sent immediately after any time delays.
- All statuses are ****Draft****
  No one will enter the flow.
- All statuses are ****Manual****
  All messages and other actions require approval before sending****.**** Profiles will be scheduled in the action’s **Needs Review** queue before manual approval. They will move through the flow as normal with respect to time delays, but the messages won’t send until approved. Learn more about how to [manually send flow messages to recipients](https://help.klaviyo.com/hc/en-us/articles/115002779331).

If you are on the free email and profiles plan and are over your profile limit, you cannot send emails (or set flow emails live) until you are under your active profile limit.

For more information, learn more about the [timeline of a flow](https://help.klaviyo.com/hc/en-us/articles/360046164352).

## Update flow statuses immediately

To update all flow action statuses immediately:

1. Open the flow you want to update in the flow builder.
2. Click ****Review and turn on**** or ****Update Status**** in the top right corner.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46896000498587)
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46896000503195)
3. From the dropdown, choose the new status for all existing actions: either ****Draft****, ****Manual****, or ****Live****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29765824737691)
4. Select ****Update status now****.
5. Click ****Save****.

## Schedule flow statuses to update

To schedule a bulk status update:

1. Open the flow you want to update in the flow builder.
2. Click ****Update Status**** or ****Review and turn on**** in the top right corner.
3. From the dropdown, choose the new status for all existing actions: either ****Draft****, ****Manual****, or ****Live****.
4. Select ****Schedule****.
5. Choose a date, time, and timezone.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29765824740763)
6. Click ****Save****.

The panel will display an overview of the scheduled status changes. From here you can edit, delete, or add more status changes.

### Edit or delete a status change

To edit or delete and existing status change:

1. Click ****Update Status**** in the flow builder.
2. In the **Update status** panel, click the action button (3 dots) next to the status change.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29765808191771)
3. Choose ****Edit**** to modify details or ****Delete**** to remove the status change.

### Add another status change

To add another status change to the schedule:

1. Click ****Add status change****.
2. Choose a status from the dropdown that differs from the previous one.
3. Click ****Save****.

You can now view the updated status schedule in the **Update status** panel.

![](https://klaviyo.zendesk.com/hc/article_attachments/29765824749595)

## How to see upcoming status changes

Navigate back to the ****Flows**** tab to see any flows with upcoming status changes listed underneath the flow’s current status.

![](https://klaviyo.zendesk.com/hc/article_attachments/29765824754971)

## How to review past status changes

To review past status changes:

1. In the top bar, click the ****View flow history**** icon.

![](https://klaviyo.zendesk.com/hc/article_attachments/46896004316955)

![](https://klaviyo.zendesk.com/hc/article_attachments/46896004319643)

Learn more about [reviewing a flow's history](https://help.klaviyo.com/hc/en-us/articles/4402385748635).

## Outcome

You now understand how to change the statuses of flow actions in bulk, either immediately or by scheduling future changes. This allows you to change when subscribers enter flows.
