---
id: "10948996125083"
title: "How to optimize your flow sending frequency"
source_url: "https://help.klaviyo.com/hc/en-us/articles/10948996125083-How-to-optimize-your-flow-sending-frequency"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:10Z"
language: "en"
---
## You will learn

Learn best practices on gradually sending multiple flow messages to subscribers. The key is to send messages to your subscribers often enough to keep them engaged, while spacing out your sends to prevent recipients from getting overwhelmed.

## Recommended sending frequency

If you are new to Klaviyo, we recommend creating your first flows using the pre-built templates found in Klaviyo’s [flow library](https://www.klaviyo.com/library/flows). These flows come with time delays set up using the recommended sending frequencies shown below.

The chart below shows recommended sending frequencies for common flow types. These recommendations are based on what we have found works best for the average brand.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Welcome series | Abandoned cart | Browse abandonment | Post purchase | Win back | Anniversary | Sunset |
| Immediately | ◉ |  |  | ◉ |  |  |  |
| 2 hours |  |  | ◉ |  |  |  |  |
| 4 hours |  | ◉ |  |  |  |  |  |
| 1 day |  | ◉ |  |  |  |  | ◉ |
| 3 days |  |  |  | ◉ |  |  |  |
| 4 days | ◉ |  |  |  |  |  |  |
| 1 week |  |  |  | ◉ |  |  | ◉ |
| 2 weeks |  |  |  |  |  |  | ◉ |
| 2 months |  |  |  |  | ◉ |  |  |
| 3 months |  |  |  |  | ◉ |  |  |
| 1 year |  |  |  |  |  | ◉ |  |

## Use A/B testing to determine frequency

Although we recommend starting out by using the frequencies shown in the chart above, optimal frequency can vary from business to business. You can use Klaviyo’s A/B testing features to test flow branches with different time delays using the conditional split component to determine the best timing for your flow.

To set up an A/B test branch:

1. Navigate to the flow you would like to A/B test in the ****Flows**** tab.
2. Drag a conditional split to where you would like to start your A/B test.
3. When configuring the split, select ****Random sample**** as the condition.
4. Select what percentage of your audience will go down the YES path, which you can think of as the control branch for the test.
5. For an even A/B test, select ****50%****. Otherwise, click the dropdown to choose a different percentage.
6. Add and configure different time delays onto the YES and NO paths.
7. Clone the email in the YES path and drag it onto the NO path so that you have 2 different emails. The content of these emails should be identical to allow you to compare the analytics in order to determine the most effective time delay.
8. If you have more emails in your flow that are past the A/B test split, drag the end of the NO path to reconnect it with the YES path after the first email.
   ![A conditional split using the 50% A/B testing condition.](https://klaviyo.zendesk.com/hc/article_attachments/28705638055195)

Learn more about A/B test configuration and how to determine the best path in our article on [how to A/B test flow branches](https://help.klaviyo.com/hc/en-us/articles/360049849432).

## Use Smart Sending to limit message frequency

Smart Sending allows you to limit the number of emails or SMS someone can receive within a set period of time. This is a good way to prevent your subscribers from receiving too many messages at once from active flows and campaigns.

Flow messages will not enable Smart Sending by default. You can choose to enable Smart Sending for an individual flow message by following these steps:

1. Click on a message within a flow.
2. In the sidebar, scroll down to the **Settings** section.
3. Click the checkbox next to **Skip recently emailed profiles** to toggle on the feature.
   ![Flow builder sidebar showing flow message settings with Smart Sending enabled.](https://klaviyo.zendesk.com/hc/article_attachments/28705638058139)
4. Click ****Save**** at the bottom of the sidebar.

Learn more in our article on [understanding Smart Sending in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115002779311).

## Additional resources

Learn about other flow message settings in our article on [how to review a flow message’s settings.](https://help.klaviyo.com/hc/en-us/articles/115002779111)

Check out other tips on A/B testing in Klaviyo:

- [How to A/B test a flow email](https://help.klaviyo.com/hc/en-us/articles/6960371049115-How-to-A-B-test-a-flow-email)
- [How to review email A/B test results for flows](https://help.klaviyo.com/hc/en-us/articles/9360405808027-How-to-review-email-A-B-test-results-for-flows)
- [Understanding what to A/B test in your flows](https://help.klaviyo.com/hc/en-us/articles/360054629031-Understanding-what-to-A-B-test-in-your-flows)