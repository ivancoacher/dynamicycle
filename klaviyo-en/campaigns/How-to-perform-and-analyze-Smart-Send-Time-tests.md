---
id: 360049073691
title: "How to perform and analyze Smart Send Time tests"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360049073691-How-to-perform-and-analyze-Smart-Send-Time-tests"
section: "Test and analyze campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:50:12Z"
language: en
---

## You will learn

Learn how to create Smart Send Time tests in Klaviyo and use the Smart Send Time reporting page to understand your results.

By carrying out a Smart Send Time test, you can gain insight into your audience to improve the performance of your campaigns. If your brand has 2 or more distinct audiences, the best time to send to one group might not be the best for another. For this reason, you can either run one or multiple Smart Send Time tests in Klaviyo.

This feature is currently available only for email; it cannot be used for SMS or push campaigns.

## Create a Smart Send Time test

You can create as many Smart Send Time tests as you want as well as reset the results so that the test starts from scratch. There are 2 ways to create a Smart Send Time test in Klaviyo: on the Smart Send Time reporting page or as you create and send a campaign.

To create your first Smart Send Time test:

1. Navigate to ****Campaigns**** tab in Klaviyo's left-hand navigation.
2. Click the additional options (3 dots) menu at the top, then select ****Smart Send Time report****.
   ![sendtime1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37121246678683)
3. In the upper right-hand corner, click ****Create new test****.
   ![sendtime2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37121246681243)
4. Name the experiment and add notes as needed.

   If you have multiple tests set up, you can select an existing test or create a new test through the Campaign Wizard:
5. [Create a campaign](https://help.klaviyo.com/hc/en-us/articles/115005054847) as normal.
6. Before sending it, choose ****Smart Send Time**** from the **Choose time or strategy** dropdown.
7. Choose an existing test or select ****Create test**** to create a new test.
   ![Smart Send Time test selection.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723542540187)
8. If creating a new test, input a name and any notes you want.
9. Click ****Send****.

## Smart Send Time phases

You must complete 3 phases for each Smart Send Time test:

| Phase | Description |
| --- | --- |
| Exploratory | Send a campaign to at least 12,000 recipients and select ****Smart Send Time > Exploratory**** as the sending strategy. Depending on your audience size, you may need to sent multiple exploratory sends.  The campaign will send out over a 24-hour period. Recipients are randomly assigned an hour and receive the email in their local time. |
| Focused | Once your exploratory send(s) are complete, send a campaign and select ****Smart Send Time > Focused**** as the sending strategy.  Based on your exploratory send results, emails are sent at the best time based on your exploratory send, as well as 2 hours before and 2 hours after. This validates the data and identifies your optimal send time. |
| Optimal | Once the optimal time is determined, choose ****Smart Send Time > Optimal**** to send messages at the ideal time for your audience, according to each recipient's local time zone. Sending future campaigns at the optimal time doesn’t impact the optimal send time for that test. |

You must complete the exploratory step before you can run a focused send, which must finish before the optimal send.

However, during the focused and optimal phases, you can continue to run the earlier step(s) in order to gather more information for the Smart Send Time model. For instance, when an optimal send time has been reached, you can run either an exploratory or focused send.

For more information on these phases, check out our guide to [understanding Smart Send Time in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360029794371).

## Smart Send Time reporting

To view the aggregate data gathered by the Smart Send Time test:

1. Navigate to ****Campaigns**** tab in Klaviyo's left-hand navigation.
2. Click the additional options (3 dots) menu at the top, then select ****Smart Send Time report****.
   ![sendtime1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37121246678683)
3. If you have multiple tests, use the dropdown under **Test name** on the left-hand side to find the one you want.

Below this, view the overall open rate by hour for all campaigns in this Smart Send Time test.

![sst test results.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723520576411)

Select one of the campaigns in this test from either the **Smart Send Time reporting** page or the reporting page from the ****Campaigns**** tab. Clicking into a campaign will show you:

- How each email campaign performed (based on the time it was sent)
- The associated click and conversion rates
- If a campaign was sent as part of an exploratory, focused, or optimal send