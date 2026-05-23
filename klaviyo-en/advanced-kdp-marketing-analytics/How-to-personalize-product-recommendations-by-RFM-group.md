---
id: 26365073803675
title: "How to personalize product recommendations by RFM group"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/26365073803675-How-to-personalize-product-recommendations-by-RFM-group"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:36Z"
language: en
---

## You will learn

Learn how to use RFM (recency, frequency, and monetary) properties to target customers with product recommendations.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Create RFM segments

If you have created a [new custom metric](https://help.klaviyo.com/hc/en-us/articles/22311085738395/) to use in your RFM report, it may take up to 48 hours for this change to be reflected in your data.

Creating segments of customers based on their RFM group allows you to easily target groups with different sets of products that are most relevant to their shopping patterns.

Once created, these segments can be used to send personalized campaigns to different groups, and trigger flows when a customer enters a particular RFM group. For example, you may want to include discounted products in emails going to your current **At Risk** or **Inactive customers**, or use cross-selling content with customers in your **Recent** group.

To create a segment based on RFM group use the following condition, with your desired group set as the value (i.e., **Champions** in the example below).

- Properties about someone > Current RFM group > equals > RFM group name

![Segmeny using the current RFM group property](https://klaviyo.zendesk.com/hc/article_attachments/28717418753947)

Learn more about [building segments based on RFM group](https://help.klaviyo.com/hc/en-us/articles/18193920339483).

Some additional use cases for segments based on RFM group include:

- Targeting **Loyal** and **Champion** customers to provide reviews on items.
- Targeting **Loyal** or **Recent** customers with new products or product offers to cross-sell and up-sell.
- Targeting **Recent** customers with a subscription so that they become a **Champion** or **Loyal**.
- Targeting **Inactive** or **At Risk** customers with winback campaigns.
- Targeting **Inactive** or **At Risk** customers with lower cost items.
- Offering exclusive or time-limited discounts to **Inactive** or **At Risk** customers.

## Using show/hide logic based on RFM group

You can dynamically show different content in your emails based on a profile’s RFM group using Klaviyo’s [show/hide logic in templates](https://help.klaviyo.com/hc/en-us/articles/7655965301531). This feature allows you to personalize your email content based on information you have gathered about your subscribers, so each recipient has a highly relevant marketing experience.

Show/hide conditions based on profile data (i.e., profile or custom properties) can be used in any Klaviyo email. In this case, you can use the **Current RFM group** or **Previous RFM group** properties to show product recommendations based on the recipient’s RFM group.

For example, to the **Champions** or **Loyal customers** groups, consider sending higher value items. Meanwhile, for customers in the **Inactive** or **At Risk** groups, send lower-cost products or best sellers. Alternatively, you can send profiles in the **Loyal** or **Champions** groups early access or new products to see if they perform better with them.

Learn [how to show or hide template blocks and sections based on dynamic variables](https://help.klaviyo.com/hc/en-us/articles/7655965301531).

The condition you need to show a piece of content to a specific RFM group is **Current RFM group > equals > Champions**.

![](https://klaviyo.zendesk.com/hc/article_attachments/30443751496475)

In this example, **Current RFM group** is the property being referenced in the condition, and the property value is **Champions**. You can replace **Champions** with the RFM group you are targeting.

Similarly, to hide a piece of content for a specific RFM group, use the condition **Current RFM group > does not equal > Champions**.

![](https://klaviyo.zendesk.com/hc/article_attachments/30443751503515)

This condition only displays content to recipients that are not in the **Champions** RFM group.

### Send personalized campaigns with show/hide logic

When sending campaigns in Klaviyo, you can use show/hide logic in Klaviyo to include personalized product recommendations based on a profile’s RFM group (i,e., **Current RFM group** or **Previous RFM group**).

You can include multiple products in your email, and create the show/hide rules so profiles in different groups see the appropriate product in their emails.

Some examples include:

- Targeting **Loyal** or **Recent** customers with new products or product offers to cross-sell and up-sell.
- Targeting **Recent** customers with a subscription so that they become a **Champion** or **Loyal**.
- Targeting customers in the **Needs Attention** or **At risk** groups with lower cost items they are more likely to purchase.
- Targeting **Champions** or **Loyal** customers groups with higher value items.

Learn [how to add a product block to an email](https://help.klaviyo.com/hc/en-us/articles/115000219092).

## Send personalized flows

You can also use RFM properties to send more relevant content with your flows. In addition to dynamically displaying content using show/hide logic, you can [create conditional splits](https://help.klaviyo.com/hc/en-us/articles/115003872171) based on a profile’s RFM group to send different group members down different flow paths.

You can include different product recommendations or other content in each path’s flow email. When profiles go through the flow, they will go down the relevant path based on their RFM group.

Learn [how to create conditional splits in flows](https://help.klaviyo.com/hc/en-us/articles/115003872171).

![Flow with branches split by RFM group](https://klaviyo.zendesk.com/hc/article_attachments/28717391505051)

In flows, you can try to cross-sell or up-sell specific products based on the details of the action they took to enter a flow and their RFM group.

For example, if you have a post-purchase flow with conditional splits based on RFM group, you can target **Loyal** or **Champions** with a product review request. Meanwhile with customers in the **Recent** group, you can target them with new products that are complementary to their purchase.

Learn [how to create a retention flow triggered off of RFM groups and customer behavior changes](https://help.klaviyo.com/hc/en-us/articles/25408596027547).

Additional examples of using RFM groups in flows include:

- Creating a conditional split based on if a person is:

- A frequent purchaser (**Champions** or **Loyal**)
- Or if they are a sometimes or never purchaser (**Recent**, **Needs Attention**, **Inactive**, or **At Risk**).

- Creating a conditional split based on a customer group’s recent browsing behaviors.

- For example, those in **Champions**, **Loyal**, or **Recent** may get a regular browse abandonment message, while those in **Needs Attention**, **Inactive**, or **At Risk** receive a browse abandonment message with an additional discount.

- Create a flow for those in the **Champions**, **Loyal**, or **Recent group** highlighting new products or launches.
- Encourage those in the **Champions**, **Loyal**, or **Recent** group to leave reviews of their products.

## Additional resources

[Understanding scoring and customer groups in the recency, frequency, and monetary analysis (RFM) report](https://help.klaviyo.com/hc/en-us/articles/17797937793179)

[How to create a retention flow triggered off of RFM groups and customer behavior changes](https://help.klaviyo.com/hc/en-us/articles/25408596027547)

[How to strategically use RFM properties in campaigns and flows](https://help.klaviyo.com/hc/en-us/articles/18194102384539)