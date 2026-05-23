---
id: 360052794352
title: "How to review your A/B test results for campaigns"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360052794352-How-to-review-your-A-B-test-results-for-campaigns"
section: "Analyze email results"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:56:54Z"
language: en
---

## You will learn

Learn what data you can find on the A/B test results page and what each of these indicators mean. The information in this guide applies to both A/B testing with [email campaigns](https://klaviyo.zendesk.com/hc/en-us/articles/115005228148) and [SMS campaigns](https://klaviyo.zendesk.com/hc/en-us/articles/4406796460443).

A/B testing campaigns can provide valuable insight into your audience by making it simple to determine what changes to make to your sending strategy. Not only will you know the winning variation for an A/B test, but also other important factors, like the win confidence percentage and winning metric details.

## A/B test results

To see the results of an A/B test:

1. Navigate to the campaign you are testing.
2. Select the ****A/B test results**** tab of the main campaign report.

![A/B test results tab for campaign](https://klaviyo.zendesk.com/hc/article_attachments/28723660259995)

## Test overview

In the **Test results** section, you’ll see a snapshot with the following:

- ****Winning variation****
  Once a test is complete, the variation that won.
- ****Status****
  Whether the A/B test is ongoing (i.e., collecting analytics) or complete.
- ****Win probability****
  How likely it is that the winning variation truly had the highest open, click, or placed order rate after taking random chance into account, and whether this probability is considered [statistically significant](https://help.klaviyo.com/hc/en-us/articles/360052793012).
- ****Lift****
  How much better the winning variation performed over the other variation. Calculated based on the winning metric (i.e., open rate, click rate, or placed order rate). For tests with 3+ variations, the second-best performing test is used for comparison.
- ****Winning metric****
  The winning variation's results for the metric that was used for the test. For example, if open rate was chosen as the winning metric, the open rate percentage would be shown.

Below these results, you can review the open, click, and placed order rates for every variation in the test.

### How lift is calculated

The lift percentage is different than the percentage shown for your winning variation. This is because the percentage shown next to each variation is the percentage of people who interacted with the email (open, click, placed order) whereas the lift is the percentage of improvement that the winner had over the other variation.

For example, if you are using click rate as your winning metric and Variation A has 5/100 (5%) recipients click and Variation B has 4/100 (4%) recipients click, the difference between the variations is 1 click. That means the lift was 1/5 (20%). In other words, the lift was 20% with Variation A having a 5% click rate and Variation B with a 4% click rate.

### Personalized variation results

The option to choose a test strategy is only available for accounts with more than 400,000 total profiles. If your account doesn’t qualify, Klaviyo will use the winning variation test strategy.

If you chose the option to personalize variations for each recipient, you will see slightly different metrics on the test results page, including the following:

- ****Total A/B test lift****
  How much better the best variation performed over the second best variation. Calculated based on the winning metric (i.e., open rate or click rate).
- ****Personalization lift****
  Percentage of how much more successful the personalized test was over a standard A/B test.
- ****Personalization click rate****
  The average click rate amongst all variations of profiles that received their preferred variation.
- ****Profile characteristics derived by Klaviyo AI****
  A list of the data used by the AI to determine a pattern amongst profiles who preferred a specific variation, i.e., what factors likely caused someone to prefer one variation over the other. Click on each variation to see the data used as it will differ per variation.

![](https://klaviyo.zendesk.com/hc/article_attachments/28723660264603)

### Understanding win confidence and statistical significance

Say, for instance, you want to see if adding emojis to your subject line impacts your open rate with your email list. If you only send the test to 2 subscribers and the emojis have a better open rate, you can’t say conclusively that the rest of your email list will feel the same way. If instead you tested with 100 people in your email list and found that emojis have a substantially higher open rate, you would feel much more confident that using emojis in your subject lines is better for your audience.

Under **Win probability**, you’ll see whether or not the variation shown is statistically significant. If it is deemed significant, this means that the variation has a high win probability (i.e., 90% or higher). A test might also be promising, inconclusive, or not statistically significant. Learn more about [statistical significance in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360052793012).