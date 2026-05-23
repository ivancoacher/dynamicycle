<h1>How to configure custom conversion metrics</h1>

## You will learn

Learn how to create custom metrics to more accurately track the impact of your marketing and how customers drive conversions. By default Klaviyo provides many metrics (e.g., **Placed Order**) to track your business’s success. However, if you have a custom setup or a different business use case, these default metrics may not work for you. For example, your **Placed Orders** events include recurring subscriptions, and you’d like to review only orders placed through your ecommerce website. The guide below walks you through how to set up these custom metrics for your needs.

If you need help on deciding when you should use custom metrics, head to our [strategic guide on using custom metrics](https://help.klaviyo.com/hc/en-us/articles/22311212640027/).

## Before you begin

It’s important to note when you create your own custom metrics (e.g., **Placed Order** that excludes subscriptions), they will appear as a new metric option in Klaviyo reporting (i.e., it will not replace the default **Placed Order** metric).

### Mapped metrics

You also have the option to utilize custom metrics within your [mapped metrics](https://help.klaviyo.com/hc/en-us/articles/25829057055899). This helps ensure your generated predictive models and default reports are aligned to your account’s data structure and needs. For example, you may create a custom **Placed Order** event that is then used to calculate [applicable reporting](https://help.klaviyo.com/hc/en-us/articles/25829057055899#h_01HZ2MPFB9V6HCZES9JCP8KV2R) using this metric.

### Reports that can use custom metrics

And any time you adjust a custom metric, applicable reporting will update. Reporting where you can use this custom metric includes:

- The [home dashboard](https://help.klaviyo.com/hc/en-us/articles/9974064152347) (main dashboard that greets you when logging in)
- [Business review dashboards](https://help.klaviyo.com/hc/en-us/articles/16427152766619) (within the dashboards section)
- [Overview or analytics dashboards](https://help.klaviyo.com/hc/en-us/articles/4708299478427) (within the dashboards section)
- [Flow performance reports](https://help.klaviyo.com/hc/en-us/articles/360047044892) (within custom reports)
- [Campaign performance reports](https://help.klaviyo.com/hc/en-us/articles/360047022912) (within custom reports)
- [Single](https://help.klaviyo.com/hc/en-us/articles/360046242952) and [multi-metric reports](https://help.klaviyo.com/hc/en-us/articles/360046234772) (within custom reports)
- Within flow analytics (in the flows list page itself)
- Within [campaign conversions](https://help.klaviyo.com/hc/en-us/articles/115005199947#section1) (in the campaigns list page itself)
- The [conversion overview dashboard](https://help.klaviyo.com/hc/en-us/articles/28474458127899) (Advanced KDP and Marketing Analytics customers only)
- The [customer lifetime value (CLV) dashboard](https://help.klaviyo.com/hc/en-us/articles/17797912816795) (Advanced KDP and Marketing Analytics customers only)
- The [recency, frequency, and monetary (RFM) analysis report](https://help.klaviyo.com/hc/en-us/articles/17797889315355) (Advanced KDP and Marketing Analytics customers only)
- The [product analysis dashboard](https://help.klaviyo.com/hc/en-us/articles/26685770823451) (Advanced KDP and Marketing Analytics customers only)

### Using tags

Also, tags from your ecommerce integration, as well as other integrations, may not always reliably ingest correctly into Klaviyo. It is advised to avoid using tags in your custom metrics and events setup.

## Default custom metrics

For Advanced KDP customers, Klaviyo is able to automatically detect and provide default custom metrics based on certain integrations. If you have a newly created default custom metric, you will see these appear within the **Metrics** tab. If you are not an Advanced KDP customer, head to the [next section on creating your metrics](#01HZFNAMK1BTZGXTNG4VE9427D).

The following ecommerce and partner integrations combinations will create default custom metrics:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ****Ecommerce integration**** | ****Partner integration**** | ****Default custom metric created in your account**** | ****Metrics used**** | ****Metric definition**** |
| Any ecommerce integration | Not applicable | **Placed Order - Online** | **Placed Order** via any supported integration. | **Placed Order** events not including any point of sale (POS). |
| **Placed Order - In Store** | **Placed Order** via any supported integration. | **Placed Order** events, including those made via point of sale (POS). |
| BigCommerce | w/OrderGroove | **Placed Order - One Time Purchases** | **Placed Order** via BigCommerce | **Placed Order** events made on BigCommerce, not including any from OrderGroove. |
| Shopify | w/OrderGroove | **Placed Order - One Time Purchases** | **Placed Order** via Shopify | **Placed Order** events made on Shopify, not including any subscription orders. |
| BigCommerce | w/Recharge | **Non-Recurring Order** | **Placed Order** via BigCommerce | **Placed Order** events made on BigCommerce, not including any from ReCharge. |
| **One-time product added on ReCharge**via ReCharge. | One-time product added to an order through ReCharge only. |
| **Subscription started on ReCharge via ReCharge.** | Subscriptions created on ReCharge only. |
| Shopify | w/ReCharge | **Non-Recurring Order** | **Placed Order** via Shopify | **Placed Order** events, not including any subscription orders. |
| **One-time Product Added on ReCharge** via ReCharge. | One-time product added to an order through ReCharge only. |
| **Subscription started on ReCharge** via ReCharge. | Subscriptions created on ReCharge only. |
| Shopify | w/Skio | **Non-Recurring Order** | **Placed Order** via Shopify | **Placed Order** events, not including any subscription orders. |
| **Skio: New Subscription Created** via Skio | Subscriptions created on Skio only. |

## Creating a new custom metric

For customers using Klaviyo’s marketing application, you have access to create 1 custom metric. For customers also using Klaviyo Marketing Analytics or Advanced KDP, you have increased flexibility to create up to 50 custom metrics. To learn more about adding Klaviyo Advanced KDP, head to our [billing guide.](https://help.klaviyo.com/hc/en-us/articles/115000976672)

1. Navigate to ****Analytics > Metrics****.
2. In the upper right, click ****Create custom metric****. Next, you will see the page to set up your new custom metric.
3. Under **Details**, create and enter the name of your new metric. Use a name that will help you easily identify what this metric captures (e.g., “Orders placed w/ subscriptions”).
   ![Custom metrics, details name.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723685112475)
4. Click the ****Aggregated by**** dropdown and choose how you want to calculate your metric (either by **Value** or **Count**). For example, if you want to capture revenue from **Placed Order** events, use **Value** to show the revenue output. If you want to redefine email clicks, use **Count**.
   ![aggregated by dropdown.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723685092123)
5. In the **Define** section, click the ****Metric name**** dropdown and select the metric definition to update. Note that these include Klaviyo and integration-specific events and metrics.
   ![metric naem dropdown fina;.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723662948507)
6. Once you have chosen your metric, click the ****Metric value property**** dropdown and choose from a list of properties that help you create the definition. For example, you may want **Placed Order** events to include subscriptions, so you may use **Source Name** to include subscription orders.
   ![metric value dropdown, update.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723662940827)
7. If applicable, click ****Add Filter**** to further define your filters and metric definition.

   If applying multiple filters, they must all be true for an event to qualify.
8. In the **Property** field, choose how the metric is classified. For example, it can be looked up by **Source Name**.

   Once you have chosen your property, the **Type** field will automatically determine how it will be represented (e.g., **number**, **text**, etc.).
   ![property dropdown, final.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723685097499)
9. Click the ****Relationship**** dropdown and choose how to capture the value. For example, if you want to capture all paid subscriptions into your **Placed Order** event, select **does not equal** “non-paid marketing subscription.”
   ![relationship dropdown final.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723685107483)
10. In the **Value** dropdown, find or add the actual value that this property represents.

    You can choose up to 3 filters that define how your metric or event calculates. It’s important to note that depending on what combination of properties and filters you use, you may run into instances where the configuration you chose inadvertently duplicates values. For example, a customer order includes a subscription and a retail good from your website. When a customer places this order, your Klaviyo account receives 2 unique events (one for the subscription and one for the website order). If you include a revenue value in your new definition and replicate it for the subscription, Klaviyo will count both events as a conversion and inflate the attributed revenue (as both are now mapped to the same custom event).
11. Optional: Once you are finished setting up your metric, you have the option to preview it to ensure it captures what you need. To do this, click ****Preview metric**** above. A modal will appear showing the conversion metric displayed in a bar chart on the left and profiles that fit this metric criteria on the right.
12. When you are ready to save your new metric, click ****Create Metric****.
13. Return to ****Analytics > Metrics**** to find your new metric.

## Editing a previously created custom metric definition

1. If you have previously created a custom event or metric definition and need to update it, head to ****Analytics > Metrics****.
2. From the list find the metric you want to edit and click on it.
3. Click ****Edit definition**** in the upper right. You will return to the setup page from here, where you can adjust your definition, including filters, relationships, and values. Follow the instructions above to adjust these as needed.
4. Once you finish updating, return to ****Analytics > Metrics**** to confirm that your new definitions are reflected.

## Deleting a previously created custom metric definition

1. Head to ****Analytics > Metrics****.
2. In the list, find the metric you want to edit and click the ****3 dot menu**** to the right and select ****Delete****.
   ![custom metrics, delete metric.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723662959259)
3. Once you finish updating, return to ****Analytics > Metrics**** to confirm that the custom metric has been deleted.
