---
id: 28264156063899
title: "How to use portfolio-level mapped metrics"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/28264156063899-How-to-use-portfolio-level-mapped-metrics"
section: "Portfolio"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: en
---

Only the following permissions can map or edit metrics:

- Portfolio Owner
- Portfolio Admin

  The following permissions can view mapped metrics:
- Portfolio Manager
- Portfolio Analyst

## You will learn

Learn how to use the portfolio mapped metrics tool to ensure that Klaviyo generated predictive models and default reports use the right metrics, aligned to your specific portfolio accounts’ data structure, reporting needs, or custom integrations.

Portfolio mapped metrics automatically provides predefined metrics (e.g., **Placed Order**, **Refunded Order**, **Ordered Product**, etc.) without having to set these up individually across each account, as well as the option to set up any custom metric definitions as needed.

## Before you begin

Areas where mapped metrics will appear or can be used:

- [Benchmarks reports](https://help.klaviyo.com/hc/en-us/articles/360050110072)
- Quarterly growth reports (QGR)
- [Customer lifetime value reports (CLV)](https://help.klaviyo.com/hc/en-us/articles/17797865070235) (Advanced KDP and Marketing Analytics customers)
- [Predictive analytics](https://help.klaviyo.com/hc/en-us/articles/360020919731)

To modify metrics for an individual account or make adjustments to any of the default portfolio metrics, please refer to our [guide on account-level mapped metrics](https://help.klaviyo.com/hc/en-us/articles/25829057055899).

## When to use mapped metrics

Mapped metrics can be beneficial for accounts that want to more accurately align how they measure success in Klaviyo based on their specific business or data model needs.

The following are common use cases for portfolio mapped metrics:

- You want all accounts under your portfolio to use the same metrics and align all data.
- One or more of the accounts in your portfolio is use custom integrations or integrations that is not recognized by Klaviyo with out-of-the-box named metrics.
- You want certain reports such as CLV, QGR, or benchmarks to use the metric that aligns with your needs.
- You want predictive analytics to use the metrics that align best with your business goals. For instance, utilizing predictive analytics can assist in accurately defining your revenue across all sources and accounts.

## Accessing mapped metrics

Head to ****Manage > Metrics****.

If you cannot see **Manage**, you do not have the permission to adjust your portfolio’s metrics. Contact an Owner or an Admin to adjust these.

### Default portfolio metrics

Default portfolio metrics are metrics that are automatically created on your behalf across all of your accounts. Klaviyo automatically maps your metrics and sets your default metrics when you set up your portfolio, based on what it can detect from your integrations and data structure. If you have an existing portfolio prior to 8/22/24, Klaviyo will automatically backfill and create your default metrics.

A Klaviyo flag icon next to each will denote these default metrics, along with the number of accounts this metric applies to, and when the metric was created.

You can only edit default metrics from the [account level](https://help.klaviyo.com/hc/en-us/articles/25829057055899) and not the portfolio. If you edit the same metric across multiple accounts, the same portfolio metric will respect both.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720904356763)

Where applicable, the default data mappings are:

- ****Placed order****
  Represents all revenue-generating events related to orders. There must be a value passed along with each event.
- ****Ordered product****
  Represents all individually ordered items associated with a main revenue event.
- ****Cancelled sales****
  Represents a revenue event that happened but was canceled before fulfillment.
- ****Refunded sales****
  Represents when someone completes a revenue event, makes a payment, and requests the payment to be returned.
- ****Added to cart****
  Represents when someone is on your website and adds an item to their cart.
- ****Started checkout****
  Represents when someone starts the process of checking out on your website.
- ****Viewed product****
  Represents when someone is identifiable and views an item page on your website.

### Creating a new mapped metric

In addition to the default metrics, you also have the option to create new metrics from scratch and aggregate this definition to all selected accounts. This allows you to associate together data or metrics across all accounts into one defined metric. For example, you may want to pull together all metrics for how you track onsite users or how you tally revenue from your custom integration.

1. If you are not already there, head to ****Manage > Metrics****. Click on ****Create metric****.
2. In the **Metric Name** field, enter the name of your metric. It’s important to use a name that is both recognizable to all users and encompasses the metrics or data associated with it.
3. In the **Type** field, choose how you wish to express the value of your metric. Use **Monetary Value** for metrics that capture revenue and express it, or use **Event Count** for metrics that numerically total.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720899051547)
4. In the **Definition** section on the left-hand side, select all accounts that you want to include as part of this definition.

   If you are not seeing all of your accounts displayed, click on the **Show 25** option below to expose more options.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720904361627)
5. In the **Metric choice** dropdowns select the metric you want to aggregate (e.g., **Fulfilled Order**). Once you choose this metric, it populates across all selected accounts where it can be found. If you decide to change your metric, an option for **Apply to All** will appear allowing you to apply a chosen metric to all selected accounts.
   ![metric mapping defi.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720899055771)
6. Select ****Save and exit**** in the upper right corner when you are done.