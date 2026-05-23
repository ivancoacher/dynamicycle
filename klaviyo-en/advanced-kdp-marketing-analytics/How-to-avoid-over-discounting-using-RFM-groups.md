---
id: 26978522793627
title: "How to avoid over-discounting using RFM groups"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/26978522793627-How-to-avoid-over-discounting-using-RFM-groups"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: en
---

## You will learn

Learn how to use RFM (recency, frequency, and monetary) groups to avoid over-discounting and losing potential revenue.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

## Identifying groups that benefit most from coupons

While coupons are a great way to incentivize customers to make a purchase, it is important to tailor your discounting strategy for different RFM groups, since coupons can impact your brand’s revenue and margins.

Consider prioritizing larger or more frequent discounts for RFM groups that are less likely to engage with emails or make purchases without a discount code, like **At risk** or **Needs attention**. Meanwhile, you can use smaller discounts for more engaged groups like **Champions** or **Loyal**, or use discounts as an incentive to take other actions like leaving a review.

To analyze the engagement of your RFM groups, you can:

- Build [RFM segments](#h_01J1G0EZ9JAGACKQG282QB7MHW) and run an [engagement report](https://help.klaviyo.com/hc/en-us/articles/115005906848) to see a breakdown of how engaged each group is.

- Use the [audience performance report](https://help.klaviyo.com/hc/en-us/articles/17798068936219) to compare the conversion rates and revenue across your RFM segments.

## Examples of discounts to use for RFM groups

### **Champions** and **Loyal**

The **Champions** and **Loyal** groups contain some of your best customers, that don’t always require discounts to make purchases. In order to maximize margins, consider removing or lowering discounts to these cohorts of customers who are already brand loyal.

However, discounts can still be valuable for these groups. You can send these customers coupons that incentivize them to take certain actions like starting a subscription, referring a friend, or leaving a product review. Coupons can also be a good way to keep these customers in their usual buying cycles, and encourage purchases if they start to deviate.

Learn how to [create a winback flow](https://help.klaviyo.com/hc/en-us/articles/115002775192) that automatically targets customers deviating from their usual buying cycles.

### **At risk** and **Needs attention**

The **At risk** and **Needs attention** RFM groups contain customers that have not recently purchased, and do not engage with your brand very frequently. Coupons for these groups should incentivize customers to make purchases by providing a discount that is generally larger than your standard welcome series (if applicable). Consider targeting these groups with coupons for your best-sellers and other items they make like. Additionally, take advantage of coupons in [abandoned cart flows](https://help.klaviyo.com/hc/en-us/articles/115002779411) to provide discounts at key moments during the purchase process.

## Send coupons to specific RFM groups

### Create RFM segments

By creating segments based on a profile’s RFM group, you can target the specific groups with a discount or send different discounts to each RFM group. These segments can be used to send personalized campaigns. For example, you may want to include a coupon in emails going to your current **At Risk** or **Inactive customers** to incentivize them to purchase.

To create a segment based on an RFM group, use the following condition with your desired group set as the value (i.e., **Champions** in the example below).

****Properties about someone > Current RFM group > equals > RFM group name****

![RFM segment for Champions group](https://klaviyo.zendesk.com/hc/article_attachments/28715973114907)

### Using Show/Hide logic

You can also dynamically show different content in your emails based on a profile’s RFM group using Klaviyo’s [show/hide logic in templates](https://help.klaviyo.com/hc/en-us/articles/7655965301531). This feature allows you to personalize your email content based on information you have gathered about your subscribers, so each recipient has a highly relevant marketing experience.

Show/hide conditions based on profile data (i.e., profile or custom properties) can be used in any Klaviyo email. In this case, you can use the **Current RFM group** or **Previous RFM group** properties to dynamically display discounts based on the recipient’s RFM group.

For example, you can send the same email to a group of customers, but display different discounts based on the recipients’ RFM group. Note that you can only base show/hide logic on event data (e.g., based on past purchases, started checkout data, etc.) in flows.

Learn [how to show or hide template blocks and sections based on dynamic variables](https://help.klaviyo.com/hc/en-us/articles/7655965301531).

The condition you need to show a piece of content to a specific RFM group is:

```
person|lookup:'Current RFM group' == 'Champions'
```

In this example, **Current RFM group** is the property being referenced in the condition, and the specific property value is **Champions**. You can replace **Champions** with the specific RFM group you are targeting in your messaging.

Similarly, to hide a piece of content for a specific RFM group, use the condition:

```
person|lookup:'Current RFM group' != 'Champions'
```

**!=** means "does not equal", so this condition only displays content to recipients that are not in the **Champions** RFM group.

![Show/Hide logic to show coupon only to Champions group](https://klaviyo.zendesk.com/hc/article_attachments/28715973112603)

### Using flow branching

You can also use RFM properties to send discounts to specific RFM groups in your flows. In addition to dynamically displaying content using show/hide logic, you can [create conditional splits](https://help.klaviyo.com/hc/en-us/articles/115003872171) based on a profile’s RFM group to send different group members down different flow paths. When profiles go through the flow, they will go down the relevant path based on their RFM group.

Learn [how to create conditional splits in flows](https://help.klaviyo.com/hc/en-us/articles/115003872171).

![Flow with different paths based on RFM group](https://klaviyo.zendesk.com/hc/article_attachments/28715966580891)

For example, if you have a flow with conditional splits based on RFM group, you can prioritize coupons in emails going to the **Needs attention** or **At risk** groups so they are incentivized to purchase. Meanwhile, since groups like **Champions** or **Loyal** are more likely to purchase without a discount, you can target them with other content like special offers (e.g., limited drops, events, etc.)

Learn [how to create a retention flow triggered off of RFM groups and customer behavior changes](https://help.klaviyo.com/hc/en-us/articles/25408596027547).

## Measure performance

### Funnel analysis

To identify the RFM groups that are the most receptive to discounts, you can use Klaviyo’s [funnel analysis report](https://help.klaviyo.com/hc/en-us/articles/17798009376155) paired with RFM group properties.

Before setting up a funnel, send a campaign or flow with a coupon code to your desired RFM groups. Receiving this email will act as the beginning of the funnel, so you can monitor which groups are most likely to convert to a purchase.

Create a funnel with the following suggested steps per RFM group. This funnel view will allow you to monitor the customer journey after sending out an email or SMS with a coupon code.

1. ****Received Email**** (or SMS)
2. ****Clicked Email**** (or SMS)
3. ****Added to Cart****
4. ****Placed Order****


Filter the **Received Email** and **Clicked Email** events to only include the email or SMS that contained your coupon.

![Received email to placed order funnel](https://klaviyo.zendesk.com/hc/article_attachments/28715966585627)

By creating this funnel for each RFM group you can then compare performance across groups and identify which group is most likely to convert when presented with a coupon code.

This funnel does not track coupon usage and may include orders placed without the coupon.

You can also create another version of this funnel for each group without the message filters. This allows you to compare the number of people in an RFM group that make a purchase after receiving an email or SMS with a coupon, compared to the number of people that make a purchase after receiving an email or SMS without a coupon.

If you see that the funnel with the email or SMS that contains a coupon has a strong increase in conversion, it is a good indicator that using the coupon is worth the impact on margins associated with discounts.

### Custom reports

You can also measure the value of providing RFM groups with a discount code by using Klaviyo’s custom reports.

To use custom reports to analyze the value of providing a coupon code, send a different [static coupon code](https://help.klaviyo.com/hc/en-us/articles/115005084727) to each RFM group. For example send a code like “Welcome10AR” to the **At risk** group and “Welcome10C” to the **Champions** group.

Once your RFM groups have received a coupon, you can create a [single metric deep dive report](https://help.klaviyo.com/hc/en-us/articles/360046242952) for your placed order event that is grouped by discount code. This report shows the placed order value associated profiles that were assigned a particular discount code.

![Custom report showing placed orders grouped by discount codes](https://klaviyo.zendesk.com/hc/article_attachments/28715973122203)

## Other use cases

In addition to sending different discounts to profiles based on their RFM groups, you can also send other personalized messaging or visuals. Consider the following use cases:

- Personalize the products that certain customer groups see vs. others by product value or type. For example, **Champions** or **Loyal customers** see higher value items while **Inactive** or **At Risk** that see lower cost items.
- Show a section about leaving product reviews to those only in the **Champions**, **Loyal, or Recent** groups.
- Present loyalty points information:

- For those in **Champions**, **Loyal**, **Recent**, and **Needs Attention** groups, show their loyalty status or a call to action to join the program.
- For those in **Inactive** or **At Risk** explain your loyalty program and value they will receive after purchases.

- Target **Recent** customers with a subscription, refill, or complementary product so that they become a **Champion** or **Loyal**.

## Additional resources

[How to personalize product recommendations by RFM group](https://help.klaviyo.com/hc/en-us/articles/26365073803675)

[How to create a retention flow triggered off of RFM groups and customer behavior changes](https://help.klaviyo.com/hc/en-us/articles/25408596027547)

[How to strategically use RFM properties in campaigns and flows](https://help.klaviyo.com/hc/en-us/articles/18194102384539)