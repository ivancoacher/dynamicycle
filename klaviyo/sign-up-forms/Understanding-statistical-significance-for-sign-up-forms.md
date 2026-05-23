---
id: 25187312302747
title: "Understanding statistical significance for sign-up forms"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/25187312302747-Understanding-statistical-significance-for-sign-up-forms"
section: "Test forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:36Z"
language: en
---

## You will learn

Learn when an A/B test’s results are considered to be statistically significant for Klaviyo sign-up forms. This guide will explain statistical significance for sign-up forms and when it’s decided.

Klaviyo decides when an A/B test has reached statistical significance once 1 variation has mathematically proven to perform better than another. You can configure an A/B test to automatically choose the winning form variation and end once the test results are considered to be statistically significant.

A/B tests allow you to measure how different elements of your forms perform to ensure they’re resonating well with your site visitors and driving strong engagement. It’s important to understand whether or not a test can be considered statistically significant so you can effectively analyze results and determine what improvements to make. If the test results are not statistically significant, then it’s more difficult to confirm that a particular variation will drive improved performance at scale.

## How Klaviyo determines statistical significance for forms

In order to achieve statistical significance, a sign-up form’s A/B test must meet the following conditions:

1. A minimum of 90% win probability for the leading variation
2. A minimum of 1,000 form views per variation

See below for a more detailed explanation of how Klaviyo considers each of these factors.

- Win probability of the leading variation
  - This is the probability that the form submit rate for the leading variation is truly higher than the form submit rate for all other variations. High win probability means there is strong evidence that the leading variation will win due to the form being better, rather than due to random chance.
- Form views
  - A form needs to collect an ample number of views to ensure that the results are not skewed by any early-test anomalies.

## Ending an A/B test after statistical significance is reached

In the **Winner Selection** setting, you can configure the test to end automatically when there is 1 variation that outperforms the other(s) at a statistically significant level, or when it reaches a particular date. Or, you can select both boxes to end the test when 1 of the 2 conditions are met (meaning the test either achieves statistical significance or reaches the end date).

![The Winner selection section of the A/B test settings page where you can choose how a winning form variation will be chosen showing both the statistical significance and date boxes checked.](https://klaviyo.zendesk.com/hc/article_attachments/28716119103643)

Alternatively, if you choose to end your test manually by unchecking both boxes under **Winner Selection**, you will need to monitor the results independently and manually choose both the winner and end date.

When viewing the results for an in-progress test, you can monitor the win probability as well as the current data per each variation on the **Overview** menu of the **A/B test results** tab.

![The A/B test results page for an example, in-progress A/B test where you can see the current win probability as well as a data breakdown and graph of the current metrics per variation.](https://klaviyo.zendesk.com/hc/article_attachments/28716058336155)

For more details, head to our [guide on reviewing A/B test results](https://help.klaviyo.com/hc/en-us/articles/360045462071#h_01HAT3ZEQ7PRAVW32X3G0NTRTC).

## Additional resources

- [How to A/B test a sign-up form](https://klaviyo.zendesk.com/hc/en-us/articles/360045462071)
- [Best practices for A/B testing](https://klaviyo.zendesk.com/hc/en-us/articles/360045012632)
- [Understanding sign-up form analytics](https://klaviyo.zendesk.com/hc/en-us/articles/360015960712)