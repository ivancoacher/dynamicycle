---
id: 360048067932
title: "How to edit coupons in Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360048067932-How-to-edit-coupons-in-Klaviyo"
section: "Getting started with coupons"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:49Z"
language: en
---

## You will learn

Learn how to edit coupons that Klaviyo generates so that you can use them in your messaging and encourage subscribers to make a purchase on your website.

You will not be able to edit a coupon if it’s used in a campaign that is scheduled or currently sending; the campaign will need to be cancelled first. You will also not be able to edit uploaded coupons in Klaviyo.

## Edit an existing coupon

1. In Klaviyo's left-hand navigation select ****Content > Coupons****.
   ![Klaviyo's main navigation menu with the Content tab dropdown open to select Coupons](https://klaviyo.zendesk.com/hc/article_attachments/34381193246235)
2. Select the coupon that you want to edit.
3. The **Coupon details** modal will appear with the current information filled in. From here you can edit the:
   - Discount type and application details
   - Minimum purchase amount
   - Activation and expiration dates
     ![The Coupon Details menu for an example coupon where you can configure the name, prefix, discount type, application, and expiration specifics](https://klaviyo.zendesk.com/hc/article_attachments/34381193251867)
4. Once you've made your changes, click ****Update coupon**** in the top right corner.

When you generate new codes for this coupon they will contain the new information. If the coupon is used in a flow, 100 codes will auto-generate when you save. This allows flows to immediately send the latest version of any coupon.

## Information on updating coupon codes

If you change the definition of your coupon in Klaviyo:

- Previously generated codes not yet sent are deleted.
- Previously generated codes that have been sent are not impacted by the change made to the coupon. This means that all previous coupon configurations will still apply for the already sent codes.
- Only codes generated after making the update follow the new definition.

This information may differ if you plan to change a coupon's definition in Shopify directly, rather than in Klaviyo. Head to our guide on [managing Shopify coupons](https://help.klaviyo.com/hc/en-us/articles/115006155388#h_01HE8BRNWXSTTEQQP76T3EJB43) for more information.

### Example

Say that you configured a coupon that requires a minimum purchase amount of $20. You also generated 100 codes, 30 of which have been sent in a flow.

If you then edit the coupon definition in Klaviyo to require a minimum purchase amount of $40:

- The 70 codes not sent yet are deleted
- The 30 that were already sent will require a $20 purchase (not $40).

This is because any coupons that were already sent in a flow before the change will still reflect Price Rule A ($20 minimum purchase), and thus will not be impacted by the definition change.

## Additional resources

- [How to export coupon information](https://help.klaviyo.com/hc/en-us/articles/360048071212)
- [How to view coupon history](https://help.klaviyo.com/hc/en-us/articles/360048069712)
- [Getting started with coupon codes in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005084727)