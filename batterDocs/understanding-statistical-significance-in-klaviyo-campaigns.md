<h1>Understanding statistical significance in Klaviyo campaigns</h1>

## You will learn

Learn how to tell whether or not an A/B test is considered statically significant or not. For instance, if a campaign variation A has an open rate of 15% and variation B has an open rate of 14%, how do you know for sure if variation A or B performed better?

## Note about Apple Mail Privacy Protection

With the release of iOS15, macOS Monterey, iPadOS 15, and WatchOS 8, Apple Mail Privacy Protection (MPP) changed the way that we receive open rate data on your emails by prefetching our tracking pixel. With this change, it’s important to understand that open rates will be inflated.

With regard to A/B testing, we anticipate that our tools should account for these inflated open rates; however, you may need a higher threshold to reach statistical significance. If you regularly conduct A/B testing AND have greater than ~45% of opens on Apple Mail, we suggest creating a [custom report](https://help.klaviyo.com/hc/en-us/articles/4416803987739) that includes an MPP property. You can also identify these opens in your individual [subscriber segments](https://help.klaviyo.com/hc/en-us/articles/4416791883163).

For complete information on MPP opens, visit our [iOS 15: How to Prepare for Apple’s Changes](https://www.klaviyo.com/blog/apple-ios15-klaviyo) guide.

## Categories of statistical significance

Statistical significance is when Klaviyo is mathematically able to determine whether a variation will produce improved performance. For campaigns, Klaviyo observes both the number of people who received a message and the win probability, which is how likely a variation will yield better results based on how well it outperforms the other variation(s).

When A/B testing, you should [avoid any factor that can significantly influence your audience](https://help.klaviyo.com/hc/en-us/articles/360045012632); for instance, don’t retest near a holiday weekend, when your audience is much more likely to be looking for your emails.

When it comes to A/B testing campaigns, there are four categories for statistical significance:

- Statistically significant
- Promising
- Not statistically significant
- Inconclusive

In the next few sections, we will go over when a test falls into each of these categories.

Don’t have time to read? Check out the [decision tree at the bottom of this article](#h_01HXYNWGTTK728X3B734D7676E).

## Statistically significant

The statistically significant tag on your A/B test means that a certain variation of your test is highly likely to win over the other option(s). It also indicates that you would be able to reproduce the results and could apply what you learned to your future sends.

![Statistically significant AB test results.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716353898011)

For Klaviyo campaigns, an A/B test result is deemed statistically significant when:

- 50 people have received each variation.
- The win probability is at least 90%.

This ensures that a large enough sample size of recipients have seen the A/B test, and that the winning variation largely outperformed the other(s) for the chosen winning metric (which, for campaigns, is either open rate, click rate, or placed order rate).

For example, say you’re testing whether or not an emoji in the subject line affects open rate. The test results show the winning variation is the one with the emoji and there’s a green statistical significance tag. In this case, you can be confident that a subject line with an emoji will consistently perform better than one without: and there’s no need for retesting.

However, you should always use your best judgment when acting on the results of the test. If you’re sending out a more serious or somber message, for instance, an emoji might not be appropriate to use.

## Promising

When the results are promising, one variation looks like it’s performing better than the other(s), but the evidence isn’t strong enough from the test by itself. If a test is deemed promising, no tag will appear indicating this; however, you will see an alert indicating that you should rerun the test.

![Promising AB test results.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716330885787)

For a test result that’s promising, you should perform another A/B test so you have more certainty. For example, going back to the emoji example above, if the results are promising, perform this test again. If you continue to see promising results in favor of the emoji after several A/B tests, you can trust that emojis have a slight but positive impact on your audience, and you should continue to use them in campaigns.

For campaigns, an A/B test result is considered promising when:

- 50 people have received each variation.
- The win probability is between 75% and 89%.

## Not statistically significant

If something is not statistically significant, one variation beats the other(s) in the test by only a slight amount and you may not be able to replicate the result in a further test.

For our example, this may mean that the variation with the emoji beat the no-emoji variation(s), but only by a very slight amount; not enough for the test result to be meaningful.

In this case, we recommend retesting this factor 2 or 3 more times and keeping a close eye on the results.

If you continue to see that the test result is deemed not statistically significant, do not continue to test; instead, move on to A/B testing a different topic. If a test falls into this category, a gray tag saying **Not statistically significant** will appear on the A/B test results page.

![Not statistically significant AB test results.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716330888219)

For campaigns, an A/B test result is considered not statistically significant when either:

- The probability is less than 75% and at least 1,800 people received each variation.
  Or
- Fewer than 1,800 have received each variation, the percentage difference between the leading variation and second-place variation is 4% or less, and the win probability is less than 60%.

## Inconclusive

If a test is inconclusive, it means that there’s not enough information to determine whether or not something is statistically significant. If the test results don’t match any of the criteria for the options above, it will fall into the inconclusive bucket. You can visualize this using the decision tree shown in the next section. Note that inconclusive tests won’t show a tag indicating whether or not the test was statistically significant on the results page.

![Inconclusive AB test results.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716353907355)

In this case, you may want to expand your audience for any followup tests. If you have a small group that you’re testing with, interpret the results as you see fit and retest to check that what you’ve found is accurate. Further, focus on learning about your subscribers through other means; e.g., surveys, polls, etc.

## Statistical significance decision tree

The following decision tree shows when an A/B test will fall into each category. The green lines indicate that the answer is “yes” while red represents “no.”

![A decision tree outlining possible A/B test outcomes](https://klaviyo.zendesk.com/hc/article_attachments/28716330879387)
