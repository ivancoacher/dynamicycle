---
id: "27695838219675"
title: "Understanding revenue metrics for sign-up forms"
source_url: "https://help.klaviyo.com/hc/en-us/articles/27695838219675-Understanding-revenue-metrics-for-sign-up-forms"
section: "Build and use forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:56:47Z"
language: "en"
---
## You will learn

Learn how to configure and use form revenue metrics to gain insights into how your sign-up forms are influencing purchases on your website. Klaviyo uses a lookback window, which is a defined time period used to link the total revenue from a purchase to all form submissions that occurred within that period, to track and display these metrics in your account.

This guide is designed to help you:

- Understand how to adjust the lookback window settings for revenue calculation linked to forms
- Access and interpret revenue metrics for your forms

Revenue metrics for forms are only collected as of June 5, 2024, and are not supported for [tap-to-text](https://klaviyo.zendesk.com/hc/en-us/articles/9351341171995) forms. Note that form revenue is tracked separately from revenue attribution for messages (i.e., emails, SMS, and push). This means that if someone signs up via a form, and then receives a message, Klaviyo will link the appropriate revenue to both; however, these numbers will likely differ due to the different ways that revenue is attributed to each. [Learn more about message conversion tracking](https://help.klaviyo.com/hc/en-us/articles/115005248128).

To learn more about form performance with submission metrics (i.e., submits, views, and submit rate), see [understanding form analytics](https://help.klaviyo.com/hc/en-us/articles/360015960712).

## How form revenue metrics work

- When a visitor clicks the submit button at any step of the form, Klaviyo logs a ****Submitted form**** event on their profile.
- If the visitor reaches the form’s success step or the final step, Klaviyo logs a ****Completed form**** event.
- For example, say that a brand sets a 30-minute lookback window to link revenue with a form's final step. Once an order is placed, Klaviyo will review the last 30 minutes to check for a Completed form event. If a shopper completes the form and places an order within that 30-minute window, Klaviyo will link the total value of the order to the form.

1. Configure the lookback window to determine the time period that Klaviyo will use to link the total revenue from a purchase to form submissions that occurred within that period.
2. Decide if you want to associate revenue when a visitor clicks a submit button at any step of the form, or only when they reach the final step.
3. Based on your choices, as visitors place orders, Klaviyo uses the lookback window to link any submitted or completed form events to placed orders.
4. View associated revenue for each form on the ****Sign-up forms**** tab (under **Form Revenue)**, as well as access a more detailed breakdown of revenue metrics (e.g., total revenue, number of orders, and average order value) on the form analytics page.

Revenue metrics are only tracked when the site visitor identifies themselves during the form submission, or if they are already recognized by the system. For example, if the visitor is not already identified by Klaviyo, they must enter their email address before clicking the submit button for the revenue to be associated with the form.

## Configure revenue lookback settings

You can configure how Klaviyo associates revenue with form submissions, as well as define the time period of the lookback window.

By default, a 2-hour lookback window is used to link form submissions with revenue; however, you have the flexibility to adjust this window based on your brand's needs. To adjust the lookback window and attribution settings:

1. Select the ****Sign-up forms**** tab in Klaviyo’s left-hand navigation.
2. Click on the gear icon in the top right corner to open the **Form settings** menu.
   ![The gear icon highlighted and being selected in the top right corner of the Sign-up forms page.](https://klaviyo.zendesk.com/hc/article_attachments/28713375224731)
3. Under **Revenue lookback for multi-step forms**, decide how revenue should be associated with your form submissions. You can choose either:

   - ****When a visitor submits on any step****
     Klaviyo will associate revenue if a shopper clicks a submit button on any step of the form.
   - ****When a visitor gets to the success step****
     Klaviyo will only associate revenue if the shopper reaches the success step of the form, or last reachable step.![The Form settings menu where you can configure revenue lookback settings, such as Revenue lookback for multi-step forms, and the time period of the Revenue lookback window.](https://klaviyo.zendesk.com/hc/article_attachments/28713386161563)
4. Under **Revenue lookback window**, determine the time period that Klaviyo will use to link revenue to form submissions. You can choose from the following options:

   - 15 minutes
   - 30 minutes
   - 60 minutes
   - 2 hours (default)
   - 24 hours
5. Click ****Save**** to apply the new lookback settings.

## View form revenue metrics

In addition to existing performance metrics (i.e., submit rate, submits, and views), you can also view total revenue associated with each individual sign-up form on the **Sign-up Forms** tab, as well as view a more detailed breakdown of revenue metrics on the form’s analytics page. The sections below detail how to find each of these pages.

Klaviyo's ability to track onsite activity from shoppers' browsers (including Form submitted events and Form completed events) is limited due to privacy restrictions around cookie consent banners and tools, as well as some ad blockers. If Klaviyo is unable to track these events, it could impact metrics shown in on form analytics pages.

### Sign-up forms tab

To view the total revenue associated with each form in your Klaviyo account:

1. Navigate to the ****Sign-up forms**** tab in Klaviyo’s left-hand navigation to see a list of all live and draft forms in your account.
2. In the **Total revenue** column, view the total revenue attribution for each form.

![The Total revenue column highlighted on the Sign-up forms tab showing the total revenue associated with each form in an example Klaviyo account.](https://klaviyo.zendesk.com/hc/article_attachments/28713386156315)

The default date range for all metrics on the forms listview page is the last 30 days. The date range is not configurable on the list-view page; however, you can change it on the form analytics page.

### Form analytics page

On an individual form’s analytics page, you can visualize reports on form submission metrics and form revenue metrics, providing a comprehensive view of performance.

To view revenue metrics on a form’s analytics page:

- Click the ****Time Period**** dropdown.
- Choose your desired date range.
- The revenue metrics for the selected date range will be displayed.

1. Navigate to the ****Sign-up forms**** tab in Klaviyo’s left-hand navigation.
2. Find your form on the list, then click the 3 dots button and select ****Analytics****. Note that a form must have some data collected for analytics to be available.
   ![The 3 dots selected next to an example sign-up form on the Sign-up forms tab showing the Analytics option selected from the dropdown.](https://klaviyo.zendesk.com/hc/article_attachments/28713386163483)
3. On the **Overview** tab, make sure that ****Placed order**** is selected from the dropdown. From here, you can view a detailed analysis of revenue metrics associated with the form alongside submission metrics.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34337018347675)
4. Optional: By default, revenue metrics will show from the last 7 days. To change the date range:

#### Visualizing revenue metrics

The following revenue metrics display on the form analytics page:

- **Total revenue**
  Sum of placed orders ($) which occurred after a form submission within the lookback window.
- **Average order value**
  The store revenue attributed to this form divided by the number of orders attributed to the form.
- **Orders**
  The number of placed orders attributed to this form.

Beneath the first submit rate graph, you can monitor these revenue metrics in a graph.

![A graph of the associated revenue metrics, including total revenue, average order value, and orders, for an example form on the Overview tab.](https://klaviyo.zendesk.com/hc/article_attachments/28713375238427)

If you’re [running an A/B test on your form](https://klaviyo.zendesk.com/hc/en-us/articles/360045462071), you can evaluate performance of different form versions by reviewing revenue metrics associated with each variation on the ****A/B test results**** tab.

![The top of the A/B test results tab showing all data, including revenue metrics per variation, for an example form that just completed and A/B test.](https://klaviyo.zendesk.com/hc/article_attachments/28713386168475)

## Next steps

To improve the performance of your sign-up forms, consider [A/B testing different elements](https://help.klaviyo.com/hc/en-us/articles/360045462071) (e.g., coupons, images, etc.) to measure the impact on performance metrics such as submit rate and revenue.

Adding a [coupon to your sign-up form](https://klaviyo.zendesk.com/hc/en-us/articles/6038674938523) can offer a powerful incentive for site visitors to opt in and make a purchase.

## Additional resources

- [How to A/B test a sign-up form](https://klaviyo.zendesk.com/hc/en-us/articles/360045462071)
- [Understanding sign-up form analytics](https://klaviyo.zendesk.com/hc/en-us/articles/360015960712)
- Course: [Create strategic sign-up forms](https://academy.klaviyo.com/en-us/courses/create-strategic-sign-up-forms)