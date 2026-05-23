---
id: 18631098703515
title: "Understanding the experiments section"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18631098703515-Understanding-the-experiments-section"
section: "A/B tests"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: en
---

## You will learn

Learn how to easily analyze the success of your A/B tests using the experiments section. The experiments section gathers all A/B tests conducted in campaigns and flows, and offers insights into the tested elements, the marketing channels used, success rates, and other data.

## Navigating to the experiments tab

Head to ****Analytics > Experiments > A/B tests****.

Once you are in the **Experiments** section, you will see the **Campaigns** tab by default. However, you can click between the **Campaigns** tab or the **Flows** tab to review A/B tests specific to each of these channels. Only owners, admins, managers and analysts have access to the experiments section.

Only owners, admins, managers and analysts have access to the experiments section.

## Using the search and settings options

At the top of the **Campaigns** or the **Flows** tab, there are options for customizing your A/B tests view and the ability to search for a specific test.

![settings and search menu.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723545845915)

### Searching for a test

Within the search field on the top left, enter the name of your test or a keyword associated with your test (e.g., “Testing BFCM welcome” or “welcome”). Once you enter a search and press enter, your view will narrow to a list of results that match your criteria.

The search functionality is for the **Campaigns** and **Flows** tabs independently. In other words, your searches will be limited to results in each tab.

### Adjusting settings options

The dropdown menus at the top of each tab provide more ways to narrow and customize which A/B test results you see for either campaigns or flows.

Settings changes only apply to the **Campaigns** and **Flows** tabs independently. In other words, any choices from these dropdowns will be limited to results in each tab.

****Timeframe settings****
In the dropdown under **Timeframe**, you can choose to review your A/B tests results from:

- ******Today******
  This includes all tests that had a start date within the last day.
- ******Last 7 days******
  This includes all tests that had a start date within the last 7 days.
- ******Last 30 days******
  This includes all tests that had a start date within the last 30 days.
- ******Last 90 days******
  This includes all tests that were run or are currently running within the last 90 days.
- ******This year******
  This includes all tests that had a start date within the present calendar year to date.
- ******Last year******
  This includes all tests that had a start date in the prior calendar year. For example, if it’s currently 2023, this would be all tests with start dates from 2022.
- ******All time******
  This includes all tests that were run or are currently running.

  Note that “All tests” in the above definitions include currently running, ended, or cancelled tests.

  ****Marketing channel settings****
  In the dropdown under **Channel**, you can choose to narrow your results from:
- ******All******
  This option shows both email and SMS A/B tests.
- ******Email******
  This option shows just email A/B tests.
- ******SMS******
  This option shows just SMS A/B tests.

  ****Metric settings****
  In the dropdown under **Winning metric**, you can choose to narrow your results to those only containing certain winning metrics, including:
- ******Open rate******
  Only see those A/B tests using **Open rate** as the winning metric.
- ******Click rate******
  Only see those A/B tests using **Click rate** as the winning metric.
- ******Placed order rate******
  Only see those A/B tests using **Placed order** rate as the winning metric.
- ******All******
  See all winning metric options together (**Open rate**,**Click rate**, and **Placed order).**

  Learn more about configuring A/B tests for [emails](https://help.klaviyo.com/hc/en-us/articles/115005228148), [SMS](https://help.klaviyo.com/hc/en-us/articles/4406796460443), or [flows](https://help.klaviyo.com/hc/en-us/articles/6960371049115), including what winning metric to use for your particular testing needs.

  ****Filter settings****
  In the dropdown under **More filters**, you have options to further narrow in on the particular test types, including:
- ******Test type****** (only on the **Campaigns** tab)
  In this secondary dropdown, choose **All** to see all types of tests. Otherwise, choose either **Content test** for A/B tests related to content or elements of your emails (e.g., tests run on using different preview text and subject lines), or **Send time test** for emails where you test the best send time.
- ******Status******
  In this secondary dropdown, choose either **In progress** to only see those A/B tests currently running or **Completed** to see those tests that are finished.

If you wish to clear any of the search results or settings you may have adjusted, click on ****Clear****.

![clear option.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723545856155)

## Reviewing your collected A/B test results

By default, both the **Campaigns** and **Flows** tab will gather all finished, currently running, or cancelled A/B tests.

The table will not have individual listings for specific variations of an email, SMS, or flow A/B test. Instead, data for each main campaign or flow will be listed. You can click on the test name itself from the table to see the variations in more detail.

These table will contain the following columns:

- ******Test name******
  The actual name of your campaign. For flows this will instead be the name of your test. This column will also include the winning metric used in the test for both campaigns and flows.
  Note that by clicking on the test name you will be taken to the A/B testing results page to see more details on your specific variations, data, and win result.
- ******Channel******
  The marketing channel being tested, either SMS (as indicated by the speak bubble icon) or email (as indicated by the envelope icon).
  Note that push notifications cannot currently be A/B tested.
- ******Test type****** (only on the **Campaigns** tab)
  This will show whether the test is a [content test](https://help.klaviyo.com/hc/en-us/articles/115005228148#how-to-a-b-test-campaign-emails1) (as indicated by the pencil icon) or a [send time test](https://help.klaviyo.com/hc/en-us/articles/115005228148#how-to-a-b-test-campaign-emails1) (as indicated by the clock icon).
- ******Start date******
  When the A/B test was originally started.
- ******Test size******
  How many profiles were included in the A/B test across all variations.
- ******Win probability******
  How likely it is a variation will yield better results based on how well it outperforms the other variation(s). This percentage represents one of those variations.
  Note that a flow message variation is considered [statistically significant](https://help.klaviyo.com/hc/en-us/articles/11233978755611) when at least 500 recipients have received each variation, and the variation has at least 90% win probability. While a campaign is considered [statistically significant](https://help.klaviyo.com/hc/en-us/articles/360052793012) when at least 50 recipients have received each variation, and the variation has at least 90% win probability.
- ******Status******
  Either a green status showing that a test completed or gray status showing that it’s still in progress.

By default, this table will sort by the most recently started test. However, you can use the arrows next to **Test name**, **Channel**, **Test type**, **Start date**, or **Status** to sort by ascending or descending order in each of these columns.