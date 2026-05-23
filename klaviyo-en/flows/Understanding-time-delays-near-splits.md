---
id: 360050334651
title: "Understanding time delays near splits"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360050334651-Understanding-time-delays-near-splits"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:50Z"
language: en
---

## You will learn

Learn when to place time delays before a split, and when to place them after.

When placing time delays near a split in a flow, it's important to be mindful about where you place the delay, as it can dramatically effect how a flow behaves.

## Time delays and splits

Conditional and trigger splits in a flow allow you to create two parallel paths for recipients based on a definition you establish. A conditional split can be defined based on any recipient properties or activity. As for trigger splits, which are only available for event-triggered flows, they are based on data from the metric you selected as the flow's trigger.

After you drag in and set the condition(s) for your split, it functions as a decision point — when recipients reach this split they are evaluated as "yes" or "no" and are sent down the appropriate path.

If you add a time delay right before a split, recipients will wait at the split until it's time for them to be evaluated. The time delay you set before a split is important, because a split is a point-in-time evaluation.

For example, let's say you have a conditional split that is defined as: **has Placed Order zero times over all time**. If this is true for someone (a non-purchaser), they will go down the YES path. For those where this is false (existing customers), they will go down the NO path. It's possible, at any point, that someone in this flow may purchase from you and become a customer, so the timing of when this split is evaluated in your series is important.

## Place time delays before a split

Conditional splits divide recipients based on their actions or profile properties. If you split recipients by their actions, you need to allow time for them to take those actions. Further, If you intend to place messages on both the YES and NO paths of a conditional split, we usually recommend setting these emails or SMS to send immediately after the split itself by not adding time delays directly after it. This way, right after your split is evaluated, recipients will receive a relevant message. If you put an additional time delay after a split, before a message, it's possible that, after this additional wait period, the recipient will no longer qualify for that path.

With trigger splits, the timing doesn't matter. Trigger splits divide recipients based on [data associated with the event triggering the flow](https://help.klaviyo.com/hc/en-us/articles/115002779071). Since this information is synced into Klaviyo at the same time as the event, you don't have to allow time for the recipient to complete a certain action in order to qualify.

In the below example of an abandoned cart flow, the goal is to send shoppers an email four hours after they initiated a checkout if they didn't end up completing the order. Here, we want to create two parallel paths based on whether or not this cart-abandoner has ever purchased in the past. To achieve this, set the time delay component to wait four hours after the trigger. Before sending the first abandoned cart reminder email, add a conditional split to evaluate whether or not someone moving through this flow has bought before. After four hours, someone will either get email #1a or #1b depending on whether or not they bought at least once in the past.

![Conditional split that checks if a profile has Placed an Order at least once over all time.](https://klaviyo.zendesk.com/hc/article_attachments/28720759972123)

## Placing time delays after a split

While typically it's better to add the time delay before the split, there are some cases where you may want to have a delay after. The most prevalent example is when you're [testing the timing of a message](https://help.klaviyo.com/hc/en-us/articles/115003883992).

For example, say you have an abandoned cart flow and you want to determine whether sending the first message after 3 or 4 hours is better. In this case, create a 50% random sample using a conditional split. Then, add a time delay to each of the paths, one set to 3 hours and the other to 4. Note that the first message should be exactly the same; when A/B testing, you should only test one variable at a time. With this setup, you'll be able to see how the two timings compare side-by-side.

![Random sample conditional split with time delays in each path.
](https://klaviyo.zendesk.com/hc/article_attachments/28720771792155)

## Additional resources

- [How to add a time delay to a flow](https://help.klaviyo.com/hc/en-us/articles/115003885212)
- [How to add a trigger split to a flow](https://help.klaviyo.com/hc/en-us/articles/115003885632)
- [How to add a conditional split to a flow](https://help.klaviyo.com/hc/en-us/articles/115003872171)