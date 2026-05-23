---
id: 360049849432
title: "How to A/B test flow branches"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360049849432-How-to-A-B-test-flow-branches"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-22T10:29:57Z"
language: en
---

## You will learn

Learn how you can A/B test flow branchesusing the conditional split component to test things like timing, discounts, and number of emails within a flow. In this article, we run through how to set up and end an A/B test for a flow branch.

You can also A/B test a single flow email. Read [how to A/B test flow emails](https://klaviyo.zendesk.com/hc/en-us/articles/6960371049115) for guidance.

## Set up a test branch

1. Navigate to the flow you would like to A/B test in the ****Flows****tab.
2. Drag a conditional split to where you would like to start your A/B test.
3. When configuring the split, select ****Random sample**** as the condition. Here, you will be prompted to select what percentage of your audience will go down the YES path, which you can think of as the control.
4. For an even A/B test, select 50%. Otherwise, click the dropdown to choose a different percentage.

The split will randomly choose a branch per profile. Because this is completely random, you may not see a completely even amount of profiles in each branch with a 50% split, but it will be close.

For example, you may want to test sending an additional email to one branch of your welcome series. To do this, you would drag a split to the end of your flow, add a time delay, and then configure the email content.

![](https://klaviyo.zendesk.com/hc/article_attachments/46986105243931)

Once you have your split configured, you can build out the content of your test branch. Depending on what you're testing, this could be several emails or different timing from what you have in your control branch.

When running an A/B test, bear in mind that testing more than one variable at a time can skew results and make it difficult to determine how to attribute any differences in revenue, open rates, etc. For this reason, it's a best practice to test variables one at a time after you've determined a winner.

Apple Mail Privacy Protection (MPP), which was released with iOS15 and updates to other Apple devices, may lead to inflated open rates due to changes in how we receive open rate data.

If you are triggering flows off of opens themselves, we suggest creating a [custom report](https://help.klaviyo.com/hc/en-us/articles/4416803987739) that includes an MPP property to review these affected opens. You can also identify these opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

## Determine the best branch

To determine which time delay is best, review the analytics for each message. Depending on the flow, decide which branch is best based on the open rate, click rate, and conversion rate.

To quickly view the flow analytics for messages in your flow:

1. Click the ****Show Analytics**** icon button located on the bottom right toolbar
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46986105248155)
2. Review the metrics of the messages in each flow branch and decide which branch you prefer.
   ![Message performance metrics shown for two messages side-by-side in different flow paths.](https://klaviyo.zendesk.com/hc/article_attachments/28711678107547)

Learn more from our article on [understanding flow analytics](https://help.klaviyo.com/hc/en-us/articles/115002779351).

## End the A/B test

After deciding which branch is better for your audience:

1. Click on the conditional split.
2. To have all of the recipients go down the Yes path, set the percentage to 100%; If you want everyone to go down the No path, set it to 0% (as shown in the example below). This way, those who were already in the **Waiting** queue still receive the old message rather than being taken out of the flow like they would if you delete the branch.
3. In whichever branch is no longer in use, set the messages to **Draft**.

![](https://klaviyo.zendesk.com/hc/article_attachments/46986105251227)

## Additional resources

- [How to A/B test a flow email](https://help.klaviyo.com/hc/en-us/articles/6960371049115)
- [Understand best practices for A/B testing](https://help.klaviyo.com/hc/en-us/articles/360045012632)
- [Mastering Email A/B Testing: Klaviyo’s Proven Tips & Tricks to Boost Revenue](https://www.klaviyo.com/blog/ab-testing-email)