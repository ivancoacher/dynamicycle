<h1>Understanding how Klaviyo converts currency in Benchmarks</h1>

## You will learn

Learn more about how Klaviyo converts and displays currency information in benchmarking revenue reporting in US dollars (USD). This conversion allows you to make better comparisons between your benchmarking results and for customers that transact in currencies different from your own.

Currently, the Benchmarks tab is the only place in Klaviyo that converts currency.

## How Klaviyo converts revenue data

In Benchmarks, revenue data is converted based on the exchange rate for that date. More specifically, for each individual **Placed Order** event, Klaviyo will convert this revenue into USD using the up-to-date exchange rate for the day of the transaction.

Most major ecommerce integrations (e.g., Shopify, BigCommerce, Magento, WooCommerce v3+, Salesforce Commerce Cloud) as well as many custom integrations pass currency as a field in the Placed Order event. For integrations that do not include currency information for each order, Klaviyo will default to the [default currency for your account](https://help.klaviyo.com/hc/en-us/articles/115005061007-Change-the-Currency-for-Your-Account) even if you transact in multiple currencies.

### Exceptions to this conversion

There is one exception to the conversion procedures outlined above. Klaviyo does not currently convert attributed revenue in benchmarks or anywhere else in the platform. For revenue per recipient, Klaviyo restricts the [peer group](https://klaviyo.zendesk.com/hc/en-us/articles/360050180151) to only include companies that do not need currency conversions to provide accurate benchmarks. As a result, your restricted peer group will only contain companies that also pass a currency field set to “USD” in all of their **Placed Order** events.

When reviewing your revenue per recipient performance indicator, you’ll receive a warning that your account's revenue per recipient may be inaccurate due to currency conversion issues if your account has not passed USD currency in all **Placed Order** events.

This scenario will arise when:

- Your ecommerce integration doesn't pass a currency field, so Klaviyo defaults to your [default currency](https://help.klaviyo.com/hc/en-us/articles/115005061007-Change-the-Currency-for-Your-Account).
- You have transactions in multiple currencies.

## Common currency scenarios

Reference the following table to learn more about how currency will appear in Klaviyo based on different currency scenarios.

Key:

- Accurate currency conversion ✔
- Warning about currency conversion ****Ɵ****
- Inaccurate but no warning in UI ✖
- Inaccurate and warning about currency conversion  ****Ɵ****

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ****Currency scenario**** | ****Revenue**** | ****Growth Rate**** | ****Average Item Value**** | ****Average Order Value**** | ****Email Revenue Percent**** | ****Revenue per Recipient**** |
| **Placed Orders** are all in USD | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| **Placed Orders** are all in one currency that is not USD | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| **Placed Orders** are in multiple currencies | ✔ | ✔ | ✔ | ✔ | ****Ɵ**** | ****Ɵ**** |
| No currency defined for **Placed Orders**, USD is the default account currency | ✔ | ✔ | ✔ | ✔ | ****Ɵ**** | ****Ɵ**** |
| No currency defined for **Placed Orders**, the default account currency is not USD | ✔ | ✔ | ✔ | ✔ | ****Ɵ**** | ****Ɵ**** |
| No currency defined for **Placed Orders**, the default account currency is not USD, and the store transacts in multiple currencies | ✖ | ✖ | ✖ | ✖ | ****Ɵ**** | ****Ɵ**** |

Note that, within the chart above, **Revenue**, **Growth Rate**, and **Average Item Value** are all peer criteria found in the peer group selection cards within your benchmarks pages. Meanwhile, **Average Order Value**, **Email Revenue Percent**, **Revenue per Recipient** are all performance indicators which you will find in the various tables within your benchmarks pages.

## Additional resources

- [How to use benchmarks reports](https://klaviyo.zendesk.com/hc/en-us/articles/360050110072)
- [Understanding peer groups, benchmarks, and how Klaviyo uses your data](https://klaviyo.zendesk.com/hc/en-us/articles/360050180151)
- [How to change the currency for your account](https://klaviyo.zendesk.com/hc/en-us/articles/115005061007)
