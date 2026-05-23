---
id: 30101956634523
title: "How to add a list update action to a flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/30101956634523-How-to-add-a-list-update-action-to-a-flow"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:38Z"
language: en
---

## You will learn

Learn how to add a list update action to a flow to add or remove a profile from a list once they reach a specific part of the flow.

With this flow action you can:

- Add to list
- Remove from list
- Create list

  By using the list update action, you can change what targeted lists someone is in without needing to manually update them or create segments. This allows a profile to start a new journey after completing their current one, and can reduce the amount of lists and segments used in your account.

  You can use this action for various cases such as:
- Adding customers to a re-engaged list after they’ve opened emails in a winback flow.
- Adding customers to a VIP list after they’ve opened emails in a post-purchase flow.
- Adding subscribers to different lists after they’ve interacted with emails requesting content preferences.

## Before you begin

Make sure you're aware of the following effects of the list update action:

- Adding a profile to a list through a list update action will trigger any flows related to that list, such as a welcome series. As with all list-triggered flows, the profile will only enter the flow if they’ve never been in it before.
- The list update action does not affect consent status.
- The list update action will add someone to a list regardless of the list's opt-in settings, i.e., even if the list is set to double opt-in, the list update action will still add the profile to the list.

## Add the list update action

- An existing list from your account that you want to add or remove the profile from.
- To create a new list. Choose a name and tags for the list. Once you’ve created the new list, it will be selected in the sidebar.

![](https://klaviyo.zendesk.com/hc/article_attachments/30165367183515)

1. Navigate to a specific flow.
2. From the **Actions** sidebar, drag and drop a ****List update**** action into the flow.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30165367179163)
3. In the side panel, name the update action and choose either ****Add to a list**** or ****Remove from a list****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30165355171867)
4. From the dropdown choose either:
5. Change the status from ****Draft**** to ****Live****, or select ****Manual**** if you’d like to review the profiles before changing their list membership. You can change the status later, but profiles will skip this step if it is left as draft status.
6. Click ****Save**** to finalize the action.

If you delete a list after it was selected for a list update action, the action will become unconfigured and will require you to set it up again. Otherwise, profiles will skip the unconfigured action.

## View activity

You can see a summary of who is waiting and who has moved through this step in the details sidebar after clicking on the action.

In the **Performance** section on the sidebar, you can see the following:

- How many profiles are scheduled or in **Waiting**
- How many profiles are in **Review** (if the flow component is/was in manual mode)
- How many profiles have successfully moved through the action, and had their profile updated

Click ****View details**** to see the activity page for more information on the profiles that will or have reached this action.

![](https://klaviyo.zendesk.com/hc/article_attachments/30165355175835)

## Additional resources

Learn about other flow actions:

- [How to add an update profile property action to a flow](https://help.klaviyo.com/hc/en-us/articles/360001768432)
- [How to add an internal alert action to a flow](https://help.klaviyo.com/hc/en-us/articles/360050242251)