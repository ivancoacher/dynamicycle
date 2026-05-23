<h1>How to use event funnels in segmentation</h1>

## ****Overview****

Event funnels in segmentation lets you build segments based on a specific sequence of events. Previously, segmentation only allowed you to check if someone had or hadn’t done certain actions, but not the order in which those actions happened. You can now target users who completed a series of actions in a particular order, unlocking more advanced behavioral targeting and analysis.

For example, you can now create a segment of profiles who:

- Placed an order and then requested a refund
- Opened a specific campaign email and then purchased a product within 48 hours

Note: this feature is only available to customers subscribed to our Advanced KDP/Marketing Analytics product. [Learn more here](https://help.klaviyo.com/hc/en-us/articles/17655007276059).

### ****Key concepts****

- Funnel Steps: The sequence of events you want to track (e.g., Opened Email → Placed Order)
- Time period: The time period in which Klaviyo will look for qualifying events (e.g., in the last 30 days). The maximum time period we support currently is 365 days.
- Completion Window: The maximum amount of time allowed between the first and last step in the funnel (e.g., all steps must be completed within 1 week).

## ****How to create a segment with an event funnel****

1. Navigate to Audiences > Lists & segments
2. Click Create New > Create segment
3. In the condition dropdown, select ****Steps someone has taken (or not taken)********in a specific order.****
   ![](https://klaviyo.zendesk.com/hc/article_attachments/42691974756507)
4. This will create a funnel of events. From there, you can modify the events, or add any additional funnel steps (up to 5). Each event can have up to 10 filters applied to it.
   ![An example image of a typical event funnel segment](https://klaviyo.zendesk.com/hc/article_attachments/42691974758171)
5. Set the time period. This feature supports a time period of 1 year max.
6. Add a completion window if desired. Note: if you don’t add a completion window, it will default to matching the time period.
7. If you wish to add other conditions (ex. **Properties about someone** or **If someone is in or not in a list**), you can add those with and/or conditions as usual.

### ****Example use cases****

- Identify customers who received a campaign, clicked a link, and then made a purchase in the last 3 days.
  ![An example that shows how to create a funnel where customers received a campaign, clicked a link, and then made a purchase](https://klaviyo.zendesk.com/hc/article_attachments/42692001352475)
- Find users who started a checkout but did not complete a purchase within 24 hours.
  ![An example that shows how to create a funnel where customers started a checkout but did not make a purchase](https://klaviyo.zendesk.com/hc/article_attachments/42692001354907)
- Target profiles who opened a product launch email and then placed an order for the relevant product.

![An example that shows how to create a funnel where customers opened an email then placed an order](https://klaviyo.zendesk.com/hc/article_attachments/42692001356699)

### ****Feature limitations****

The following limits currently apply to this feature:

- ****Time period:**** Maximum of 1 year.
- ****Completion window:**** Adding a completion window is optional.
  - If you don’t add a completion window, it will default to matching the time period.
  - If you choose to specify a completion window, you can select from our predefined options (1 hour, 1 day, 3 days, 5 days, 1 week, 30 days, 60 days, 90 days, or 365 days).
- Only one funnel condition per segment is supported. If you try to add another funnel condition to a segment that already has one, that option will appear grayed out.
- Funnels must have a minimum of two steps, and a maximum of five steps.
- Count filters are limited to “at least once” or “zero times.”
  - More specific occurrence logic (ex. Placed Order 3 times) is not currently supported.
  - “Zero times” can only be selected as the ****last**** step in a funnel. Choosing ****zero times**** as your count filter prevents you from adding additional steps.
  - For example: You can create a segment with the criteria: “Opened Email at least once and then Placed Order zero times.” You cannot create a segment that says: “Opened Email zero times and then Placed Order at least once.”

### ****Access and availability****

- Event Funnels in Segmentation is available to customers with Marketing Analytics (MA) or Advanced Klaviyo Data Platform (AKDP) entitlements. You can create segments with event funnels from the funnel analysis report. [Learn more here](https://help.klaviyo.com/hc/en-us/articles/17798009376155).
- If your account loses access to MA/AKDP, funnel-based segments will be retained for the standard grace period of 5 days, and then archived. During the grace period, you cannot edit or update the segment definition, but it can still be used in campaigns and flows.
- If you regain access to MA/AKDP, these segments will need to be manually reactivated.
