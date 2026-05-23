---
id: 115002775152
title: "How to A/B test a flow email (deprecated)"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002775152-How-to-A-B-test-a-flow-email-deprecated"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:37Z"
language: en
---

If the content of this article does not match the A/B testing experience you see in your account, this is because your account has access to the updated A/B testing experience. Learn more from our article on [How to A/B test a flow email using the updated A/B testing experience.](https://help.klaviyo.com/hc/en-us/articles/6960371049115)

## You will learn

Learn how to perform an A/B test for individual flow emails so that you can test things like subject line, discounts, and email content. You can even figure out whether, say, plain-text emails perform better than image-heavy HTML emails. Keep in mind that A/B testing cannot currently be used for SMS flow messages.

Note that you can also A/B test flow branches. For details on that, check out [How to A/B Test Flow Branches](https://help.klaviyo.com/hc/en-us/articles/360049849432).

Flow email A/B testing is the process of:

1. Creating a single flow email and scheduling this email to send after a certain number of hours or days, just as you normally would.
2. Configuring two or more email variations for this single flow email — adjusting the subject line or core email content for each variation.
3. Selecting the weight of each variation to establish the percentage of recipients that will receive each email.
4. Observing the performance of each variation over time to determine which should be considered the "winner".

## Perform a flow email A/B test

To set up A/B testing for an email in any flow, select the email card and click ****Add Variation**** in the upper right-hand corner of the sidebar. You will be taken directly to a Manage Variations window. Here, you can edit the subject line and/or content of each variation by clicking****Edit Variation.****

To add another variation, click ****Add Variation**** in the top menu or alternatively click the ****Actions****dropdown for an existing variation and select ****Duplicate Variation******.**

When you add a variation to a flow email that has already been sending, two new copies of this email are created, and the analytics for each of these copies is tracked separately. We do not continue tracking analytics for the original email once you have added a variation. The Overview report will include historical information from the original email, along with any new variations. You can view analytics for a specific variation by clicking into the Variations tab, or by checking the box to show all variations when exporting.

Lastly, choose the weight of each variation -- this will establish the percentage of recipients that will get each one. It's common practice to weight each variation equally, which you can accomplish quickly by clicking ****Equalize Weights.****

![Click 'Add Variation' to create a new A/B test variation.](https://fast.wistia.com/embed/medias/c9sqfm3072/swatch)

If you've just configured a new email and are in the Message Content view, you can quickly add a variation without returning to the main flow canvas by clicking the ****Add Variation****link below your configured message. Clicking this link will bring you directly to the Manage Variations window where you can edit the subject line and/or content of each variation.

![The Add Variation link is found at the bottom of your configured message preview.](https://klaviyo.zendesk.com/hc/article_attachments/28704484327707)

After setting your flow email with A/B testing live, you can monitor the performance of each variation across the following metrics:

- ****Recipients****: How many people received the email
- ​****Opens****: What percentage/number of people opened the email
- ****Clicks****: What percentage/number of people clicked through the email
- ****Placed Order:****
  - Total of recipients who placed an order
  - Total dollar amount that was made from each email

With the release of iOS15, macOS Monterey, iPadOS 15, and WatchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.

If you are triggering flows off of opens themselves, we suggest creating a [custom report](https://help.klaviyo.com/hc/en-us/articles/4416803987739) that includes an MPP property to review these affected opens. You can also identify these opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

Once you determine that one variation is outperforming the others over a time period that you deem significant, you can delete the other variations so that 100% of your recipients will receive the tested winner. Alternatively, you can swap out the underperforming variation with a new test and repeat the cycle.

## Additional resources

For complete information on MPP opens, visit our [iOS 15: How to Prepare for Apple’s Changes guide](https://www.klaviyo.com/blog/apple-ios15-klaviyo).

- [How to A/B test a flow branch](https://help.klaviyo.com/hc/en-us/articles/360049849432)
- [Best Practices for A/B Testing](https://klaviyo.zendesk.com/hc/en-us/articles/360045012632)