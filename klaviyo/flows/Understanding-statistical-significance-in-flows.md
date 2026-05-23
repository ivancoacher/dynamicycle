---
id: 11233978755611
title: "Understanding statistical significance in flows"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/11233978755611-Understanding-statistical-significance-in-flows"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:10Z"
language: en
---

Learn when an A/B test’s results are considered to be statistically significant in Klaviyo flows. This article will explain statistical significance for flows and when it is decided.

Statistical significance is when Klaviyo is mathematically able to determine whether a variation will produce improved performance. You can configure a flow A/B test to automatically choose a winning variation once the test results are considered statistically significant.

A/B testing is key to driving better engagement and improving your customer relationships through a data-driven approach. It’s important to understand whether the test can be considered statically significant or not. For example, if a flow email has 2 variations, and variation A has a click rate of 15% while variation B has a click rate of 14%, how do you know for sure if variation A or B performed better?

## How Klaviyo determines statistical significance in flows

For flows, Klaviyo observes both the number of people who received a message and the win probability, which is how likely a variation will yield better results based on how well it outperforms the other variation(s).

A flow message variation is considered statistically significant when:

- At least 500 recipients have received each variation.
- A variation has at least 90% win probability.
- The top variations are clearly separated: we only display statistical significance when the likely performance ranges of the leading variation and the runner-up have too little overlap (<10% overlap in credible intervals)

Win probability is calculated based on the metric you chose when configuring your A/B test. By default, this metric is the click rate of the message you’re testing. In the **Automatic Winner Selection** section, you have the option to automatically end the test once a message variation is determined to win based on the configured metric, as well as the option to end the test once a specific date is reached. You can select either or both of these options. If both are selected, the test will end based on which is reached first, statistical significance or the specified date.

For more details, see our article on [how to A/B test a flow email](https://help.klaviyo.com/hc/en-us/articles/6960371049115).

When viewing the results for a currently running or completed test, you will see the win probability in the **A/B test** section. Here, you will see whether the test results are statistically significant and which variation is likely to perform better.

![](https://klaviyo.zendesk.com/hc/article_attachments/40172449245979)

For more details, see our article on [how to review email A/B test results for flows](https://help.klaviyo.com/hc/en-us/articles/9360405808027).

## Additional resources

Check out our article on [best practices for A/B testing](https://help.klaviyo.com/hc/en-us/articles/360045012632).

Learn about other A/B tests you can run:

- [How to A/B test a flow email](https://help.klaviyo.com/hc/en-us/articles/6960371049115)
- [How to A/B test a campaign email](https://help.klaviyo.com/hc/en-us/articles/115005228148)
- [How to A/B test a sign-up form](https://help.klaviyo.com/hc/en-us/articles/360045462071)