<h1>Troubleshooting a flow</h1>

Learn how to troubleshoot a flow when you notice it behaving differently from expected.

Flows are highly customizable and can vary in complexity. Troubleshooting resources are designed to be broad, and cover common issues that can apply to most Klaviyo accounts.

## Understand flow alerts

Depending on the issue, you may see a red or yellow warning icon next to your flow in the **Flows**tab or on specific flow components in the flow builder. If you are not seeing any alert icons, skip to the next section.

For alerts on the **Flows** tab, hover over the icon to view a description of the issue.

![](https://klaviyo.zendesk.com/hc/article_attachments/29108306914331)

For alerts in the flow builder, click on the ****Alerts**** icon button on the right side of the header bar to view a list of issues with flow components.

![](https://klaviyo.zendesk.com/hc/article_attachments/46630156351771)

For more information, see our article on [understanding flow alerts](https://klaviyo.zendesk.com/hc/en-us/articles/29091293276187).

## What is your experience level?

Click on the sections below if they are relevant to your issue:

### For new accounts

For new accounts, before you begin troubleshooting, please make sure
you have fully read our guide on
[getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)
to understand the essential components of a flow and how to set your
first flow live.

To avoid issues with common flow types such as welcome series and
abandoned cart, we recommend creating your first flows using the
pre-built templates from our
[flows library](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-started-with-flows#choose-a-pre-built-flow-from-the-library3)
and editing the pre-built content to match your branding.

### For previously working flows

#### Review the flow’s changelog

If your flow was working previously, but you have recently noticed
changes in behavior, you should first look at the flow’s changelog
to view a history of changes made. This is especially important for
older flows and accounts with multiple users. If you notice that
a flow’s behavior has changed after a certain date and time, the
changelog will be able to tell you the following:

- What changed
- Who made the change
- When the change took place (date and time in your account’s timezone)

If a change coincides with when you started experiencing issues with
your flow, it is likely that the change is the source of the issue.


![](https://fast.wistia.com/embed/medias/qksjoa5aq4/swatch)

Follow these steps to view a flow’s history:

1. In the header bar, click the ****View flow history****
   icon button.
   ![View flow history option in the header bar.](https://klaviyo.zendesk.com/hc/article_attachments/46630172148763)
2. Selecting ****View flow history**** will open the
   **Flow history** panel on the right-hand side of the screen.
   ![The Flow History panel, also called the changelog.](https://klaviyo.zendesk.com/hc/article_attachments/46630172153243)

Find out more about the **Flow history** panel in our article
on
[how to review a flow's history](https://help.klaviyo.com/hc/en-us/articles/4402385748635).

## Troubleshooting resources

### Flow triggers

If the metric used to trigger your flow suddenly sees a drop in activity, you will receive an alert like the one shown below, and you must troubleshoot the issue to make sure the flow is triggering properly.
![Name of a flow in the flows list view with a warning about a drop in activity displayed below it.](https://klaviyo.zendesk.com/hc/article_attachments/28720621452699)

For **Viewed Product**, **Added to Cart**, **Started Checkout**, and **Placed Order** tracking, see the articles below for troubleshooting steps:

- [Troubleshooting viewed product tracking](https://help.klaviyo.com/hc/en-us/articles/4416172774939-Troubleshooting-viewed-product-tracking)
- [Troubleshooting added to cart tracking](https://help.klaviyo.com/hc/en-us/articles/6985692431259-Troubleshooting-added-to-cart-tracking)
- [Troubleshooting started checkout tracking](https://help.klaviyo.com/hc/en-us/articles/6998274713371-Troubleshooting-started-checkout-tracking)
- [Troubleshooting placed order tracking](https://help.klaviyo.com/hc/en-us/articles/7000906101019-Troubleshooting-placed-order-tracking)

For all other metrics, [understand how Klaviyo monitors metric activity for flows](https://help.klaviyo.com/hc/en-us/articles/13913401149595-Understanding-how-Klaviyo-monitors-metric-activity-for-flows).

### Scheduled and skipped messages

If you are seeing a significant amount of skipped profiles in your flow, learn about [troubleshooting why a flow message skipped a profile](https://help.klaviyo.com/hc/en-us/articles/1260805003210-Troubleshooting-why-a-flow-message-skipped-a-profile).

If you are seeing profiles scheduled in a flow multiple times, learn about [troubleshooting why a profile is queued in a flow multiple times](https://help.klaviyo.com/hc/en-us/articles/115002779491-Troubleshooting-why-a-profile-is-queued-in-a-flow-multiple-times).

If you are unsure how or why profiles are moving through a flow, learn [how contacts move through a flow](https://help.klaviyo.com/hc/en-us/articles/360017706091-Understanding-how-contacts-move-through-a-flow).

### Deliverability

If you are receiving notifications about sudden drops in flow performance, see [how Klaviyo monitors metric activity for flows](https://help.klaviyo.com/hc/en-us/articles/13913401149595-Understanding-how-Klaviyo-monitors-metric-activity-for-flows).

If you are having issues with flow messages going to spam, learn about [troubleshooting why emails go to spam](https://help.klaviyo.com/hc/en-us/articles/12034571748251-Troubleshooting-why-emails-go-to-spam).

### Troubleshooting specific flow types

If you are having issues with specific types of flows, see the articles below on further troubleshooting steps.

- [Troubleshooting a list- or segment-triggered flow](https://help.klaviyo.com/hc/en-us/articles/12414318812827-Troubleshooting-a-list-or-segment-triggered-flow)
- [Troubleshooting a metric-triggered flow](https://help.klaviyo.com/hc/en-us/articles/12278373016603-Troubleshooting-a-metric-triggered-flow)

If you aren’t sure which type of flow you are having trouble with, you can tell based on the flow’s trigger.

1. Click on the trigger of the flow in the flow builder.
2. View the top section of the right sidebar to see if the flow is triggered by a list, segment, or a metric.
3. Determine what type of flow you are viewing:
   - List- or segment-triggered flows are triggered when someone is added to a particular list or segment. Common examples include welcome series and VIP segment flows.
   - Metric-triggered flows are triggered by metrics from your integrations such as your ecommerce platform. Common examples include abandoned cart and post-purchase flows.

## Help us improve this article

If you believe helpful information is missing from the troubleshooting scenarios listed above, please provide us with feedback so that we can improve the Help Center experience and provide better support for you and other customers.

If you were not satisfied with the troubleshooting steps provided in this article, select ****No**** from the prompt at the bottom of the article. The following form will ask you for more information to improve this article.

![Feedback modal asking if the article was helpful.](https://klaviyo.zendesk.com/hc/article_attachments/28720666788379)

When providing feedback, please include the following:

1. What type of flow you are troubleshooting (welcome flow, abandoned cart, etc.)
2. Details of the issue with your flow that you could not find information about from this article

## Contact Klaviyo support

If you are still encountering issues after consulting this article and reviewing your flow’s history, please reach out in our [Community](https://community.klaviyo.com/got-a-question-1) or to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).
