---
id: "22166996219419"
title: "How to segment subscribers by assigned coupons"
source_url: "https://help.klaviyo.com/hc/en-us/articles/22166996219419-How-to-segment-subscribers-by-assigned-coupons"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:56:45Z"
language: "en"
---
## You will learn

Learn how to segment subscribers by the coupon sent to them.

The **Coupon Assigned** metric records on a profile when they receive a dynamic coupon, and logs the coupon’s key details (i.e., **Coupon ID**, **Coupon key**, **Coupon expiration date** and **Unique code**, if applicable). This allows you to easily identify and group profiles who have (or have not) received a specific coupon.

## Before you begin

You can segment based on an assigned coupon if you have delivered at least 1 coupon to a subscriber in a message or sign-up form. If you have not sent any coupons yet, head to [getting started with coupon codes in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005084727).

**Assigned coupon** events are only available for coupons assigned on or after January 9, 2024. These events cannot be backfilled.

## Key coupon details

- ****CouponID****The CouponID is an uneditable code given to a specific coupon set when it’s created. To find the **CouponID**, navigate to the ****Coupons**** tab, select the coupon, then copy the 7-digit code in the URL.
  ![The 7-digit coupon ID highlighted in the URL for an example coupon.](https://klaviyo.zendesk.com/hc/article_attachments/28720672100635)
- ****CouponKey****
  The name that you gave to the coupon set in Klaviyo. To find the **CouponKey**, navigate to the ****Coupons**** tab and copy the name from the **Coupon** column. A CouponKey is editable, and can apply to more than 1 coupon set if they have the same name
  ![The Coupon column highlighted to show an example coupon key on the Coupons tab.](https://klaviyo.zendesk.com/hc/article_attachments/28720660383387)
- ****UniqueCode****The code assigned to a unique profile. Because there is 1 unique code per profile, you can create a segment with this filter to identify which profile received a certain code. To find the **UniqueCode**, navigate to the ****Profiles**** tab, select the individual profile, then copy the code from the **Code received** column.
  ![The Coupons section on an example profile page showing a coupon's unique ID under the Code received column.](https://klaviyo.zendesk.com/hc/article_attachments/28720672093979)

## Create a segment of subscribers with a coupon assigned

In this example, we’ll create a segment of profiles who have received a specific coupon.

1. Navigate to ****Audience > List & segments****.
2. In the top right corner, select ****Create new > Segment****.
3. Name your segment.
4. Create the following definition:
   ****What someone has done (or not done) > Coupon Assigned > at least once**** and specify the timeframe in which you initially sent the coupon.
   ![Segment example](https://klaviyo.zendesk.com/hc/article_attachments/28720672096027)
5. Click ****Add Filter.****
6. Under ****Choose property****, select which property you’d like to identify and group (e.g., **CouponID**, **CouponKey**, **UniqueID**). These terms are defined above in the Key coupon details section.
7. Next to **Equals**, paste the corresponding ID, name, or code depending on which property you selected. For example:
   ****CouponID > equals > 2930901****. ****![Add filter icon](https://klaviyo.zendesk.com/hc/article_attachments/28720660392603)****

   Use the OR button to input an additional coupon if you would like the segment to include multiple coupons that a profile may have received.
8. Click ****Create segment****.

Once you’ve created one **Coupon Assigned** segment, it’s easy to create variations with different coupons specified by [cloning the segment](https://help.klaviyo.com/hc/en-us/articles/115005238248) and building upon that foundation.

## Next steps

In your future messaging you can:

- Include this segment to target subscribers who have received a certain coupon and encourage a purchase.
- Exclude this segment to avoid sending unintended, additional coupons to those who have already received one.

At this time, Klaviyo cannot verify whether or not a subscriber has used a coupon, or segment by coupon usage. Because of this, coupons can still appear **Active** on a user’s profile until its expiration date, even if they have already used the coupon.

## Additional resources

[Getting started with coupon codes in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005084727)

[Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)