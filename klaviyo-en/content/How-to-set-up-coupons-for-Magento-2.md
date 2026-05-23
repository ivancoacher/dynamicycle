---
id: 360041971851
title: "How to set up coupons for Magento 2"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360041971851-How-to-set-up-coupons-for-Magento-2"
section: "Coupons and ecommerce integrations"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: en
---

## You will learn

Learn how to set up a price rule in Magento 2 and create the coupons in Klaviyo so that your shoppers can easily apply a discount during the checkout process. Magento supports [shopping cart price rules.](https://docs.magento.com/user-guide/marketing/price-rules-cart.html)

Klaviyo's Coupons allow Magento 2 stores to do the following:

- Create new coupons in Klaviyo associated with pre-existing price rules in Magento.
- Include unique (also called "dynamic") coupons within flow emails, so each recipient receives a unique code.

This guide will walk you through creating a Magento 2 coupon in Klaviyo in 2 steps:

1. Setup a price rule in Magento 2.
2. Create the coupon in Klaviyo.

If you would like to send campaign emails with unique coupon codes for Magento 2, follow this guide on [uploading unique coupons into Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005084727#upload-unique-coupons-into-klaviyo3) and using them in a message.

## Before you begin

Before you begin, make sure that you've [enabled the Magento 2 integration in Klaviyo and installed the Klaviyo extension in Magento](https://help.klaviyo.com/hc/en-us/articles/115005254348-Integrate-with-Magento-2-x-CE-and-EE-).

## Setup a price rule in Magento 2

1. From your Magento 2 store navigate to ****Marketing > Cart Price Rule****.

![Video showing the marketing tab within Magento 2 and selecting Cart Price Rule.](https://fast.wistia.com/embed/medias/mbqh9crj11/swatch)

2. Create a price rule by clicking ****Add New Rule****.

![The cart price rules menu in magento 2 with add new rule selected.](https://klaviyo.zendesk.com/hc/article_attachments/28715963480987)

3. Fill in the rule information:

- ****Rule Name:**** the name of the price rule in Magento 2.
- ****Active:**** choose **Yes**. If **Yes** is not selected, the coupon will not work.
- ****Websites****: if you only have one Magento store, choose the name of your website. If you have multiple Magento stores, choose the store the coupon is associated with.
- ****Customer Groups:**** choose **NOT LOGGED IN**, or choose a different customer group.
- ****Coupon:**** choose **Specific Coupon** from the drop-down.
- ****Coupon Code:**** you don’t need to enter anything in this field; Klaviyo will automatically generate coupon codes for you.
- ****Use Auto Generation:**** you must enable this field. If you don’t enable this field, Klaviyo will not be able to generate coupon codes.
- ****Uses per Coupon:**** the number of times your coupon can be used; usually this value will be 1.
- ****Uses per Customer:**** the number of times your coupon can be used per customers; usually this value will be 1.
- ****From -- To:**** enter the date range during which the coupon will be valid; the ****To**** date will be the coupon's expiration date.

Coupons set to never expire will still show an expiry date of 1 year listed in Klaviyo, however they will not expire.

![The new cart price rule menu where you can fill in your desired rule information.](https://klaviyo.zendesk.com/hc/article_attachments/28715963487643)

4. At the bottom of your **New Cart Price Rule** screen, you’ll see additional settings. ****Conditions, Actions, and Labels**** settings are optional and will impact how coupons are applied in your Magento 2 store; these won’t affect Klaviyo Coupon generation.

![The optional Conditions, Actions, and Labels settings located at the bottom of the new cart price rule page.](https://klaviyo.zendesk.com/hc/article_attachments/28715970087067)

5. ****Manage coupon codes:**** these settings don’t need to be filled in. When Klaviyo generates coupon codes, those codes will appear in this section.

6. When you’re finished, click ****Save**** on the upper right corner of your screen.

![The save button highlighted in the upper right corner of the new cart price rule page.](https://klaviyo.zendesk.com/hc/article_attachments/28715970091163)

7. View your list of Magento 2 coupons. Each Magento 2 coupon is associated with an ID. Take note of the ID of the coupon you created. You’ll need it in the next step.

![The list view of your Magento 2 coupons with the ID of the coupon you created circled.](https://klaviyo.zendesk.com/hc/article_attachments/28715970094363)

## Create a Magento coupon in Klaviyo

Next, you’ll create a coupon in Klaviyo. For this step, you need the ID associated with the price rule you just created in your Magento 2 account. A new coupon created in Klaviyo must reference a pre-existing Price Rule in Magento.

1. Navigate to your ****Coupons**** section and select ****Magento 2 Coupons****.

![The coupons tab with Magento 2 coupons selected. ](https://klaviyo.zendesk.com/hc/article_attachments/28715963503387)

2. Click ****Add Coupon**** to create a new coupon.

3. Enter a name for your coupon in the **Coupon Name** field, and enter the Magento 2 price rule ID associated with this coupon. Again, you need to have created a price rule in Magento 2 before you create a coupon in Klaviyo. Head back to your Magento 2 account if you need to reference this ID number again.

4. When you're finished click ****Add Coupon****.

![The modal asking for the name of your newly created coupon and its Magento 2 rule ID.](https://klaviyo.zendesk.com/hc/article_attachments/28715970097435)

5. You’ve created your new coupon.

## Use your unique coupon in a flow

Once you’ve created and configured your coupon, insert it into a flow message.

1. Navigate to the ****Flows**** tab in Klaviyo’s left-hand navigation.
2. Open an existing flow or [create a new one](https://help.klaviyo.com/hc/en-us/articles/115002774932).
3. Select a flow message inside your flow.
4. Open the message editor for the selected flow message.
5. Click the personalization icon. Depending on your editor, you may see a person icon, or a button labeled ****Personalization****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892622216987)
6. From the **All types** menu, select ****Coupons****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892629350171)
7. Select the coupon you'd like to add.
8. Optional: Select the ****3 dots**** on your flow email, then click ****Preview****. Note that when you preview your email directly in Klaviyo, you will not see a unique code populate. Rather, you will see your coupon’s name hyphenated to “PREVIEW.” Klaviyo will only create and share a unique code at the actual send time.
   ![An example email with a coupon tag shown in preview mode.](https://klaviyo.zendesk.com/hc/article_attachments/39892622226843)

When messages are sent out, a unique discount code, consisting of your prefix and 10 random digits, will dynamically replace the variable for each individual recipient. If you include the same coupon tag in multiple flow messages, the recipient will receive the same unique code each time.

![Unqiue 10 digit code added to the end of coupon prefix](https://klaviyo.zendesk.com/hc/article_attachments/39892629356187)

Unique coupon codes for live flow emails generate automatically based on how many you specify in the **Minimum Inventory** section of the **Coupon details** page. For example, if you create a coupon with a **Minimum Inventory** of 100, Klaviyo generates a batch of 100 unique codes. These automatically replenish daily; however, if you use all 100 codes before the replenishment, the 101st attempt to assign a coupon will be skipped due to insufficient codes available. This automatically triggers Klaviyo to generate another 100 codes. Because coupon codes for flows are replenished automatically, you do not need to manually add batches of coupon codes via the **Add codes** option.

## Additional resources

- [How to set up coupons (for Magento 1.x)](https://help.klaviyo.com/hc/en-us/articles/115005246547-How-to-set-up-coupons-for-Magento-1-x-)
- [How to view coupon history](https://help.klaviyo.com/hc/en-us/articles/360048069712-How-to-view-coupon-history)
- [Troubleshooting your Magento 2 integration](https://help.klaviyo.com/hc/en-us/articles/5510750923035-Troubleshooting-your-Magento-2-integration)