---
id: "17797912816795"
title: "How to build a customer lifetime value (CLV) dashboard"
source_url: "https://help.klaviyo.com/hc/en-us/articles/17797912816795-How-to-build-a-customer-lifetime-value-CLV-dashboard"
section: "Predictive models"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: "en"
---
## You will learn

Learn how to build and set up the custom customer lifetime value (CLV) dashboard to understand and predict each of your customers’ purchasing behaviors over time. Custom CLV provides insights into your customers’ buying habits, including potential future purchases and opportunities for cross-selling and up-selling for impending purchases.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Navigating to the dashboard

Navigation steps to the CLV dashboard vary based on whether you are an Advanced KDP or Marketing Analytics customer.

If you are an Advanced KDP customer, navigate to ****Advanced KDP > Intelligence > Predictive models****.

If you are a Marketing Analytics customer, navigate to ****Marketing Analytics > Predictive models****.

Here you will see a default dashboard with the current data model used, followed by segments, flows, upcoming campaigns, and forms using particular CLV attributes.

## Before you begin

### Dashboard requirements

- Have at least 500 customers who have placed an order.

  This does not refer to total profiles, but rather the number of people who have actually made an order with your business. Note that if this section is on a profile but is blank, Klaviyo doesn’t have enough data on that individual to make a prediction.
- You have an ecommerce integration (e.g., Shopify, BigCommerce, Magento, etc.) or use the Klaviyo API to send placed orders.
- You have at least 180 days of order history and have orders within the last 30 days.
- You have at least some customers who have placed 3 or more orders.

### Setting up your segments

If you have not already done so, you will need to set up your CLV segments and definitions prior to reviewing your dashboard. Your segment definitions and properties will be used to populate various cards in the CLV dashboard. Learn how to [create and set up your CLV segments](https://help.klaviyo.com/hc/en-us/articles/360013201072).

Only Owners, Admins, Managers, and Analysts can access this dashboard.

## Customizing your dashboard

### Reviewing your CLV calculation

1. To review your CLV settings, click on ****Settings**** in the top right.
2. At the top of this settings card, you can see how your CLV is currently being calculated (i.e., **Placed orders**, **Refunded orders**, and **Cancelled orders** metrics). If you have insufficient data for any of these 3 metrics, you will not see that particular metric(s) appear.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30666718756635)
3. Optional: to adjust any of these metrics, click ****Update metric mapping****. From here, you will be taken to your metric mapping settings to adjust what metrics you are using. Keep in mind that updating any metric mappings will apply to all [applicable reporting in your account](https://help.klaviyo.com/hc/en-us/articles/25829057055899#h_01HZ2MPFB9V6HCZES9JCP8KV2R).

If you are editing a [mapped metric](https://help.klaviyo.com/hc/en-us/articles/25829057055899) mapping or using a [new custom metric](https://help.klaviyo.com/hc/en-us/articles/22311085738395/), it may take up to 48 hours for this change to be reflected in your report. Additionally, if one was recently edited in your account, you may see a banner noting that this is still updating.

### Adjusting your predicted time range

Your prediction window is the time range in which Klaviyo provides customer purchase forecasting. In other words, during this time frame, Klaviyo predicts how much money a particular customer is expected to spend and their total number of orders.

By default, your prediction window is set to 365 days. This means that Klaviyo provides CLV predictions for the next 365 days. However, you may find that you want to narrow in a certain time period (e.g., Black Friday and Cyber Monday), or increase the period if your buying cycle tends to be longer.

Adjusting your predicted time range will change all segments, flows, campaigns, and forms using a predicted CLV attribute.

****Updating and saving your new prediction window****

To change the time range for the prediction window:

1. Input the number of days you wish to analyze in the **days** field. Do not use any negative numbers or special characters in the field (e.g., comma to separate larger numbers).

   Note that you can analyze up to 50,000 days if you have enough data to support this.
   ![days field.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713341019419)
2. Once you add a number to your days field, it is recommended to preview your intended prediction window. By previewing, Klaviyo can provide both prediction confidence and examples of your potential data.

   - Klaviyo will provide either a **High**, **Medium**, or **Low** prediction confidence, letting you know if the time range you chose will provide accurate or inaccurate predictions.

     ![prediction confidence.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713341022491)
   - Click ****Preview**** to preview this change. You will see a banner noting that the dashboard is providing preview examples of what your data may look like. Review this example dashboard to ensure that it meets your needs and you have used the accurate number of days in your predicted date range.![preview data banner.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713385531163)
3. Click ****Save**** once you are satisfied with your prediction window.
4. An additional popup will appear confirming your changes. Click ****Save**** again to complete these updates. If you wish to discard your changes, click the “****X****” in the top right corner to discard the changes.

Changes to your prediction window may take up to 2 hours to reflect in your data.

A green success message will then appear, confirming any changes that you saved.

Learn more about [using the customer lifetime value dashboard and cards](https://help.klaviyo.com/hc/en-us/articles/17797865070235#01H8AHH3WBJTHF6H7M85PD3R43).