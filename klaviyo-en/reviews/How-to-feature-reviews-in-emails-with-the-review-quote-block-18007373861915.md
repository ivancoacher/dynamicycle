---
id: "18007373861915"
title: "How to feature reviews in emails with the review quote block"
source_url: "https://help.klaviyo.com/hc/en-us/articles/18007373861915-How-to-feature-reviews-in-emails-with-the-review-quote-block"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:08Z"
language: "en"
---
## You will learn

Learn how to feature a product review within a campaign or flow email via the **Review quote** block. With Klaviyo Reviews, you can use this block to feature customer testimonials and ratings to build trust in your brand and create social proof.

## Before you begin

This block is only available in accounts that use Klaviyo Reviews. Learn how to [get started with Klaviyo Reviews](https://help.klaviyo.com/hc/en-us/articles/15937542819355).

There are 2 types of review blocks you can add:

- ****Static reviews****
  Show the same featured review to everyone who receives your email.
- ****Dynamic reviews****
  Highlight a review based on a product someone has recently interacted with (e.g., a positive review for an item in their abandoned cart reminder). This option is available only in event-triggered flow emails with product information.

## Add a static review

Follow these steps to feature a single review in an email. The same review is shown to all recipients.

1. Navigate to any email in Klaviyo (i.e., a flow email, draft campaign email, or email template).
2. Drag a **Review quote** block into the email.
   ![The review quote block](https://klaviyo.zendesk.com/hc/article_attachments/28717418162075)
3. Click ****Add review quote****.
4. If prompted, choose ****Static**** under **Quote selection**.

   When selecting a review quote in certain types of emails (e.g., campaigns, list-triggered flows, and other messages that don’t have access to event data), all review quotes are static, so this step is skipped.
5. Click ****Add review quote****.
6. Select a quote or highlight to feature.

   - You can toggle between product reviews and store reviews, filter by various criteria (e.g., rating, product, verification status, and more), or choose between full reviews and AI-selected highlights using the filter menu.![](https://klaviyo.zendesk.com/hc/article_attachments/31922796519707)
7. If desired, adjust the colors, fonts, and sizes used in the block in the ****Styles**** tab.
8. In the ****Content**** tab, change the selected quote and block styles.
9. Click ****Done****.

## Add a dynamic review

Follow these steps to dynamically highlight different reviews and different products for different recipients. You can choose to highlight featured reviews or the most recent 5-star review for a selected product. You can also choose whether to highlight reviews from the same product for all recipients, or to dynamically display reviews for an item the recipient viewed or added to cart recently.

Dynamic reviews are supported for event-triggered flows, back in stock flows, low inventory flows, and price drop flows.

1. Navigate to a supported flow email in Klaviyo.
2. Drag a **Review quote** block into the email.
   ![Review format options](https://klaviyo.zendesk.com/hc/article_attachments/28717418162075)
3. Choose ****Dynamic**** under **Quote selection**. If you do not see this option, then the message you are editing doesn’t support dynamic quote blocks. Head to an event-triggered flow.
4. Depending on your flow’s trigger, the product may be automatically selected.

   - If the product is auto-selected, you’ll see your flow’s trigger event under **Product selection**. Click the trigger button to choose how products will be prioritized if there are multiple products within the trigger event.
     ![](https://klaviyo.zendesk.com/hc/article_attachments/33237606082459)
   - If the product is not auto-selected, you’ll need to manually input a product ID variable. Learn how to [select the right variable](https://help.klaviyo.com/hc/en-us/articles/25995019549979).
5. Under **Review selection**, click ****Manage fallback options**** to choose a fallback review. This will appear in the event that no review is available for the selected product.
6. Under **Product selection**, select ****Add product****, or if this message is part of an event-triggered flow, choose ****Manual**** or ****Automatic****.

   - If you choose ****Automatic****, add an event variable that references a product’s ID. This is only supported in certain flows. Learn how to [choose the right event variable](https://help.klaviyo.com/hc/en-us/articles/25995019549979).
7. If desired, adjust the format in the **Review formats** section, or change the colors, fonts, and sizes in the ****Styles**** tab.
8. Click ****Done****.

If you select ****Featured reviews**** and ****Automatic**** product selection, make sure you have a minimum of 1 featured review for every product in your store. To feature a review, click the ****Feature**** button next to it by navigating to ****Reviews > All reviews**** in Klaviyo. If no featured reviews are available, high-rated reviews are used as a fallback.

### How reviews are selected

The **Review quote** block can only display reviews submitted by a verified purchaser. Unverified reviews cannot be selected or displayed in this block type. Additionally, only 4- and 5-star reviews appear in the selection modal by default, but you can adjust this filter.

If you aren’t yet able to select a review or if your dynamic review block appears blank, it may be because:

- ****There aren’t enough high-quality reviews in your account to select from.****
  Check back at a later date for a selection of reviews.
- ****Your reviews haven’t yet been processed.****
  If you’d like to feature a brand-new review, wait a few hours before trying again.
- ****The reviews in your account aren’t verified.****
  To be verified, a review must be submitted through a personalized link in a [Klaviyo review request flow](https://help.klaviyo.com/hc/en-us/articles/16319809379611) or marked as verified in an uploaded CSV of reviews from another platform. Unverified reviews, including reviews submitted directly to your site, are not eligible for inclusion in a review quote block. Wait until you’ve collected verified reviews, or [upload verified reviews](https://help.klaviyo.com/hc/en-us/articles/16318811222555).
- ****There are no reviews for the selected product that meet the criteria to be displayed.****
  Change your settings or collect more reviews.

### Review quote block example use cases

#### Browse abandonment or abandoned cart

Highlight a relevant product review in reminder emails to those who have left a cart behind.

![An example review quote block in a browse abandonment flow email](https://klaviyo.zendesk.com/hc/article_attachments/29493060090011)

#### Product launch campaign

When releasing a new color or design for an existing product, highlight past reviews from similar items.

![An example review quote block in an email campaign](https://klaviyo.zendesk.com/hc/article_attachments/29493060095515)

## Additional resources

- [Getting started with Klaviyo Reviews](https://help.klaviyo.com/hc/en-us/articles/15937542819355)
- [Guide to the email template editor](https://help.klaviyo.com/hc/en-us/articles/4407911841435)
- [How to add a countdown timer to an email](https://help.klaviyo.com/hc/en-us/articles/115000780232)