---
id: 360028374111
title: "How to preview a flow trigger setup"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360028374111-How-to-preview-a-flow-trigger-setup"
section: "Set up flow filters and triggers"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: en
---

Learn how to use the flow trigger setup preview tool to ensure your flow is set up as you intended. This will help you understand how your flow is going to behave based on the trigger and profile filters you've added.

Since the trigger setup preview tool only reviews the trigger itself, it will not take into account any additional flow or trigger splits within your flow, or filters added to your messages as those do not determine if someone qualifies to enter the flow.

The flow trigger setup preview tool is currently only available for: list-, segment-, or metric-triggered flows. This feature is not available for date property-triggered, low inventory, or price drop flows.

![](https://fast.wistia.com/embed/medias/t6iaoyj9fp/swatch)

## Preview the flow trigger

To view the flow trigger preview:

1. Open the flow in the flow builder.
2. Click on the flow trigger.
3. In the settings panel, click ****Preview****.

![](https://klaviyo.zendesk.com/hc/article_attachments/40156480014107)

The resulting modal will show how the flow evaluates example recipients as they enter the flow.

- For metric- and price drop-triggered flows, you can preview the last 10 instances of this metric (i.e., the last 10 events)
- For list- and segment-triggered flows, you can preview the last 10 contacts added to the list/segment

  The sidebar on the right shows profiles that triggered the last 10 events that would trigger the flow and whether or not they would pass the profile filters.
- A green checkmark indicates a profile would pass.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/40156494825371)
- A red exclamation point indicates a profile would fail.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/40156480021403)

  To find a specific profile, type a name or email address into the search bar. You can search for any profile in your account to see if it would enter the flow and pass the filters.

  If the profile triggered multiple events related to the flow, the preview will only show the most recent event.

  Click on any card to see the following information:
- A link to the selected profile
- Whether or not the profile would enter the flow
- If it enters, all the flow actions that the profile will go through

  Click on 'View details' under the Trigger entry to see the following information:
- The event that triggers the flow and when it occurred
- Profile and/or trigger filters, if applicable, and whether or not the profile would pass
- Re-entry criteria, and whether or not the profile is eligible for entry

![](https://klaviyo.zendesk.com/hc/article_attachments/47733770749467)

All profile filters evaluate again when recipients reach an action step in the flow to ensure they still qualify. In cases where a recipient reaches a step in the flow and no longer qualifies, they will be skipped. For every skipped recipient, the [skipped reason](https://help.klaviyo.com/hc/en-us/articles/115002779471-Troubleshoot-Flow-Sending#is-anyone-being-skipped-1) will be displayed in the Recipient Activity tab for the individual message. Note that if someone is skipped from one message, they are skipped from the other messages in the flow.

Any filters with the “since starting this flow” timeframe specifically evaluate if an event has occurred after someone has already entered a flow. This means upon first entering the flow, everyone will always pass this profile filter by default.

For example, with the “Placed Order zero times since starting this flow” filter on your abandoned cart flow, everyone will enter the flow because they will qualify as soon as they enter the flow. If they later go on to place an order in the time between entering the flow and receiving the first abandoned cart message, they will be skipped and not receive the message.

Learn more about Klaviyo flows: