---
id: 360046164352
title: "Understanding the timing of a flow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360046164352-Understanding-the-timing-of-a-flow"
section: "Understand flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: en
---

## You will learn

Learn how the timing of a flow is not only important to knowing when a certain message will send, but also to gaining insight into the customer's experience. As you build out your flow, you will want to keep two different timing considerations top-of-mind:

1. The time between components (as represented by time delays)
2. Timeline of each component from the trigger

In this article, we go over both considerations so you can better understand the timing of a flow's components.

## Time between components

Each flow represents a targeted customer experience. In order to build a series with timely touchpoints, it is important to think about the timing of each action in your flow relative to the activity or behavior that set the flow in motion.

For example, in a winback flow, you may have the first email send after 75 days. The second email may wait another 15 days, which brings the total number of days elapsed since the last purchase (the flow's trigger) to 90.

In addition, it is important to think about how time delays interact with other components, particularly conditional splits. Typically, you want to place a time delay before any conditional split to ensure that recipients have time to, for example, place an order before they're sent down a certain path. For more details, read our article on [how to use time delays near splits](https://klaviyo.zendesk.com/hc/en-us/articles/360050334651).

![Example customer winback flow](https://klaviyo.zendesk.com/hc/article_attachments/28713331842075)

## Additional resources

- [How to add a time delay to a flow](https://help.klaviyo.com/hc/en-us/articles/115003885212)
- [Understanding flow branching](https://help.klaviyo.com/hc/en-us/articles/115003883992)
- [How to use time delays near splits](https://help.klaviyo.com/hc/en-us/articles/360050334651)