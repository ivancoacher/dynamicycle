<h1>How to use account-level mapped metrics</h1>

Only the following permissions can map or edit metrics:

- Owner
- Admin
- Manager

  The following permissions can view mapped metrics:
- Analysts

## You will learn

Learn how to use the mapped metrics tool to ensure that Klaviyo generated predictive models and default reports use the right reference metrics, aligned to your specific account’s data structure and reporting needs.This is especially important if you are using a custom integration. Mapped metrics provides the ability to match the correct integration or source-specific metric (e.g., **Placed Order**, **Refunded Order**, **Ordered Product**, etc.) to a set of semantic references predefined by Klaviyo (e.g., revenue, orders placed, canceled sales, etc.)

## Before you begin

Areas where mapped metrics will affect reporting or can be used:

- Benchmarks reports
- QGR reports
- Predictive analytics
- A/B testing
- Custom CLV dashboard (Advanced KDP and Marketing Analytics customers only)
- Product analysis (Advanced KDP and Marketing Analytics customers only)

The conversion overview dashboard, audience performance, and RFM analysis are not affected by mapped metric changes. However, you can adjust what metrics are used to calculate these within the reports themselves.

You can also use custom metrics within mapped metrics to capture the way your business model or data is measured. Learn more about [custom metrics and how to create these](https://help.klaviyo.com/hc/en-us/articles/22311085738395/).

## When to use mapped metrics

Mapped metrics can be beneficial for accounts that want to more accurately align how they measure success in Klaviyo based on their specific business or data model needs. Additionally, by using [custom metrics](https://help.klaviyo.com/hc/en-us/articles/22311085738395/) within your mappings, you can more closely align with your specific measurement needs.

The following are common use cases of when mapped metrics may be useful:

- You are using a custom integration or integration that is not recognized by Klaviyo with out-of-the-box named metrics.
- You want certain reports such as benchmarks, CLV, QGR, or benchmarks to use the metric that aligns with your needs.
- You want predictive analytics to use the metrics that align best with your business goals. For example, using predictive analytics to help define your revenue more accurately across all of your sources.

## Accessing mapped metrics

1. Head to ****Analytics > Metrics****.
2. Click on ****Edit mapped metrics**** in the upper right.

By default, Klaviyo will attempt to map your metrics automatically based on what can be detected from your integrations and data structure. However, you can adjust the assigned metric or even choose if a particular data point does not have a compatible metric.

### Current data mapping definitions

The following data mappings are currently available:

- ******Revenue******
  This represents your preferred revenue metric. There must be a value passed along with each event.
- ******Ordered product******
  This represents your metric that captures individual ordered items associated with a main revenue event.
- ******Cancelled sales******
  This represents a revenue event that happened but was canceled before fulfillment.
- ******Refunded sales******
  This represents when someone completes a revenue event, makes a payment, and requests the payment to be returned.
- ******Added to cart******
  This represents when someone is on your website and adds an item to their cart.
- ******Started checkout******
  This represents when someone starts the process of checking out on your website.
- ******Viewed product******
  This represents when someone is identifiable and views an item page on your website.

## Editing a mapped metric

If you are editing a mapped metric or using a new [custom metric](https://help.klaviyo.com/hc/en-us/articles/25829057055899) in your mapping, it may take time for this change to be reflected in your applicable reporting. Additionally, if one was recently edited in your account, you may see a banner noting that this is still updating.

1. Click on the ******Metric assigned**********dropdown**** next to the metric you want to update.
2. From here, choose the metric that should be associated with the data point. For example, you want to ensure you associate **Added to Cart** with a metric that helps you measure how many customers are putting items in their carts. If you do not have a metric that should be associated with that mapping, choose ****Unmapped****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38410161375259)

   Keep in mind that marking as **Unmapped** will remove this metric measurement entirely from your applicable reporting. It may be more beneficial for your reporting and analysis to map this measurement to another metric.
3. Click ****Save**** after you finish updating.

You can edit each assigned metric up to 2 times per day. If you want to update the mapping again, you will have to wait until the number of updates in the last 24 hours is less than 2. Additionally, metrics can only be mapped once. If you have already used a metric for a prior mapping, either adjust this or use another.
