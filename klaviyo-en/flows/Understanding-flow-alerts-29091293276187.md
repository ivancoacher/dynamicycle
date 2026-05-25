---
id: "29091293276187"
title: "Understanding flow alerts"
source_url: "https://help.klaviyo.com/hc/en-us/articles/29091293276187-Understanding-flow-alerts"
section: "Troubleshooting flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: "en"
---
## You will learn

Learn about the different alerts and warning messages you may see when setting up a flow. These messages appear when setup is incomplete or a feature is changing and the setup is not longer valid.

Alerts will appear with a red icon for issues that stop a flow from functioning or a yellow icon for issues that need to be addressed but will still allow the flow to function. Any related text will be highlighted in the respective color.

Flow alerts can appear in 2 different places which will be covered in this article:

- The **Flows** tab - where you go to see the list of all the flows in your account.
- The flow builder - the editor you use when building a flow.

## Flows tab alerts

When viewing the **Flows** tab there are 2 types of alerts:

1. The name of the flow in red indicates that the flow cannot function without proper action. This appears when a flow was created but the trigger has not been set up yet.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29091559904283)
2. A yellow warning icon in the **Status** column indicates that the flow will still function, but some elements may be skipped unless proper action is taken. Hover over the icon for more information on the issue. This can include messages or other actions that have been added without being set up yet or have invalid settings.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29091569069595)

## Flow builder alerts

Elements in the flow builder that have not been set up or have an invalid setup will display a respective warning message on the action card. A warning means that the element will be skipped until it is properly set up.

To view all alerts:

1. Click the ****Alerts**** icon button on the right side of the header bar to open the flow action center. The badge indicates the number of active alerts in your flow.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/46630158161819)
2. In the list of alerts, you have several options:

   ![](https://klaviyo.zendesk.com/hc/article_attachments/46630158169371)

   - Click the prompt (such as ****Set up****) to view the setup panel for the affected flow element.
   - Click ****Dismiss**** to move the alert to the **Dismissed** tab.
   - Click on the **Dismissed** tab to view any previously dismissed alerts which you can move back to the **Active** tab.

Otherwise, you can view unconfigured states and other alerts directly on the flow canvas, displayed on the card for each action. Click on the flow card to view the changes that need to be made.

![](https://klaviyo.zendesk.com/hc/article_attachments/46630158173083)

Make sure to save any changes you make to flow elements. The warning will remain if you exit the setup panel without saving changes.

Click on the subsections below to learn about alerts for each flow element.

### Messages

Messages require the following in order to send:

- Subject line (email)
- Valid sender address using a business domain (email)
- Template (email) or message content (SMS and push)

For the example email below, there are 2 setup issues that must be addressed:

1. The flow message is using an email with an inbox provider domain (@gmail.com) which isn’t a valid sender address. The sender address must be changed to an email that uses the domain of your website. This also applies to internal alerts.
2. The flow message doesn’t have a template selected yet. Messages require a template in order to send.

![](https://klaviyo.zendesk.com/hc/article_attachments/29091569079195)

### Internal alerts

Internal alerts require the following in order to send:

- At least 1 recipient in the **Send to** field
- Valid sender address
- Subject
- Message content

### Time delays

Time delays require a number entered into the **Set time delay** field.

### Splits

Splits require at least 1 condition set up in order to function.

Splits may have a warning if a condition is no longer valid. For example, if a specific property is no longer usable in split conditions, a warning message will appear in the split’s setup panel.

### Filters

Filters applied to a trigger or individual flow message are optional. They may have a warning if a condition is no longer valid. For example, if a specific property is no longer usable in filter conditions, a warning message will appear in the filter’s setup panel.

## Additional resources

Still encountering issues with your flow?

- Learn about [troubleshooting a flow](https://help.klaviyo.com/hc/en-us/articles/115002779471).
- Learn about different [skip reasons for flow messages](https://help.klaviyo.com/hc/en-us/articles/1260805003210).