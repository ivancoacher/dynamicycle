---
id: "25408596027547"
title: "How to create a retention flow triggered off of RFM groups and customer behavior changes"
source_url: "https://help.klaviyo.com/hc/en-us/articles/25408596027547-How-to-create-a-retention-flow-triggered-off-of-RFM-groups-and-customer-behavior-changes"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:36Z"
language: "en"
---
## You will learn

Learn how to build a retention flow based on RFM properties to target customers who have not recently purchased. Retention flows are useful drivers in helping to win back customers, reaching them at the right time with the right message. You can automatically reach these subscribers at the point in which their customer group changes, potentially decreasing revenue and churn risks.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Before you begin

Your RFM report needs to:

- Have at least 500 customers who have placed an order.
  Note that this does not refer to total profiles, but rather the number of people who have actually made an order with your business. Note that if this section is on a profile but is blank, Klaviyo doesn’t have enough data on that individual to make a prediction.
- You have an ecommerce integration (e.g., Shopify, BigCommerce, Magento, etc.) or use the Klaviyo API to send placed orders.
- You have at least 180 days of order history and have orders within the last 30 days.
- You have at least some customers who have placed 3 or more orders.
- Note that only Owners, Admins, Managers, and Analysts can access this report.

If you have created a [new custom metric](https://help.klaviyo.com/hc/en-us/articles/22311085738395/) to use in your RFM report, it may take up to 48 hours for this change to be reflected.

## How to create the flow

You can explore the [flows library](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8Q0PAF1FY71QDZBJ7M) to use one of the pre-built templates or follow the guide below to create a custom retention flow. In either case, it's important to trigger your flows based on your RFM group segments.

### Create your segment

If you have not already done so, you will need to create a segment that includes your **At Risk** or **Needs Attention** customers. If you have already set up your segment, skip ahead to the [section on creating your flow below](#h_01JCNG895SY86NN11V59RY58SJ).

1. If you are an Advanced KDP customer, navigate to ****Advanced KDP**** > ****Intelligence**** > ****Customer insights**** > ****RFM analysis****. Alternatively, if you are a Marketing Analytics customer navigate to ****Marketing Analytics**** > ****Customer insights**** > ****RFM analysis****.
2. Scroll to find the **RFM Segments** card and click on ****Create segment****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682037019)
3. Once inside the segment builder, name your segment and add any applicable tags from the **Tags** dropdown. For example, you could name your flow “Needs Attention or At risk segment” or “Needs Attention or At risk segment- one time buyer only” depending on how you plan to set up your flow.
4. In the **Definitions** dropdown, choose ****Properties about someone****.
5. Under the **Dimension** dropdown, choose the ****Current RFM group**** option. Make sure that **Equals** is chosen in the second dropdown.
6. In the **Enter a value** field, find and choose ****At Risk****. Make sure that **Type** is set to **Text**. Your segment should look like the image below.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30931707859227)
7. ****Select +Add condition****. Make sure that your connector is set to **OR**.
8. From here, repeat steps 4-6 above and instead of choosing **At Risk**, choose ****Needs Attention**** as your RFM group.
   Once done, the first 2 steps of your segment should look like the below and include anyone who is in your **Needs Attention** or **At Risk** groups.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30931707861403)
9. Optional: **At Risk** and **Needs Attention** groups can include those who have made at least once purchase in the past. However, if you would like to target customers who have purchased a certain number of times in the past  (e.g., only one-time buyers), but are now in the **At Risk** or **Needs Attention** groups, you can use the ****+Add condition**** to add an **AND** connector.
10. Optional: choose ****What someone has (or has not done)****.
11. Optional: select your **Placed Order** metric.
12. Options: choose **equals** and whatever numbers of orders you choose. Then select o**ver all of time**. This should look like the example below.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/30931707863067)

### Set up your flow

1. Head to the ****Flows**** tab.
2. Click ****Create Flow****.
3. Click ****Build your own.****
4. In the **Create flow** side panel, name your flow something recognizable and select any tags you want it to have. For example, something like “At Risk or Needs Attention flow.”
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682047259)
5. Click ****Create manually****.
6. In the right-hand trigger panel, select ****Added to segment****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682048411)
7. In the **Added to segment** section, find and select your segment. This should be the segment that includes your **At Risk** or **Needs Attention** groups. Your trigger should look similar to the example below.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682050715)
8. Click ****Save**** when you are done creating your trigger. Then click ****Confirm and save**** on the pop-up to save your trigger.
9. Drag in your first retention-style email message from the left-side panel. This should be a message welcoming back your customers.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682051867)
10. Drag in a time delay after this first message so that your customers do not immediately receive all messages in the flow. It is suggested to wait at least 2-3 days before a customer receives their next message.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682055323)
11. Drag in your second retention-style email message from the left-side panel. This should be a message that is different from your first email and encourages your customers to come back and visit your store.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682057883)
12. Optional: if you want to add further messages to your flow, add another time delay. Make sure this is at least 2-3 days after your last message.
13. Optional: drag in your third email message from the left-side panel. This message should be different from your first two messages and could include things like time-sensitive discounts or offers.
14. When you are done creating your flow, click ****Update status**** in the upper right and either choose **Live** or **Manual**. A live flow and all its messages are sent automatically, while a manual flow requires you to manually review and send all scheduled messages. Learn more about [flow statuses](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8RVQANQHGVRJ6V4W63).
15. Once you have set your flow status, click ****Save****.

## Retention email best practices

### Conditional splits

It is optional but you can use a [conditional split](https://help.klaviyo.com/hc/en-us/articles/115003872171) based on the types of products you show to your customers. This way you can target customers with products related to what they have previously purchased or highlighting best-selling products that they may be interested in based on their RFM group (e.g., lower cost or entry-level items).

### Use template tags

It’s important that customers feel as though the email they are receiving is completely relevant and personal to them. Consider using [templates tags](https://help.klaviyo.com/hc/en-us/articles/4408802648731) to pull in information from the customer’s profile to personalize the email to them. Pull in simple items like first name or region, or use more advanced techniques to pull in items they may have recently viewed, especially for emails later in the flow once you have initially re-engaged them. Additionally, if you need to better align your data and make it more actionable, consider [data transformation](https://help.klaviyo.com/hc/en-us/articles/17760400736539) to standardize these profile properties.

### Use Show/Hide logic in existing emails

You can also [use the template editor’s **Show/Hide Logic** feature](https://help.klaviyo.com/hc/en-us/articles/7655965301531) to tailor individual blocks or sections within your existing emails and target those just in the **Needs Attention** or **At Risk** RFM groups.

#### **Needs Attention** content

Since customers in this group are more likely to engage than **At Risk** customers, and may have more moved into this group after being a prior **Loyal** or **Recent** member, you may want‌ to consider the following campaign blocks:

- Discounts or incentives
- Show their current loyalty points status
- Similar or adjacent products to ones they have purchased before
- Your most viewed products
- Your highest rated products
- Your newest products

#### **At Risk** content

**At Risk** customers are more highly susceptible to churn and it may be a longer time since their only purchase than **Needs Attention** members. In addition to the above types of messages, you may want‌ to consider the following for customers in the **Needs Attention** group:

- Lower cost or entry level items, including those that also are:
  - Similar or adjacent products to ones they have purchased before
  - Your most viewed products
  - Your highest rated products

### Run A/B tests

Use A/B tests to continue to refine what email content is motivating your **Needs Attention** or **At Risk** RFM groups to purchase and move out of these groups.

For example, you may want to test different product recommendations based on:

- Your best-selling products
- Similar or adjacent products to ones they have purchased before
- Refills or reorders of previously purchased products, if applicable
- Your most viewed products
- Your highest rated products
- Your newest products

Additionally, make sure to test things like your subject line, send time, and how many emails you send in a specific period, to see what may help motivate these customer groups. You may want to use subject lines along with your content that creates a sense of urgency.

Learn more about [A/B testing your flow emails](https://help.klaviyo.com/hc/en-us/articles/6960371049115).

## Additional resources

[How to build a segment using RFM properties](https://help.klaviyo.com/hc/en-us/articles/18193920339483)

[How to strategically use RFM properties in campaigns and flows](https://help.klaviyo.com/hc/en-us/articles/18194102384539)

[Ruffwear uses Klaviyo CDP to drive incremental revenue and improve margins (case study)](https://www.klaviyo.com/customers/case-studies/ruffwear-cdp)