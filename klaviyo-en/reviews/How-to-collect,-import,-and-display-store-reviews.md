---
id: 27291102795547
title: "How to collect, import, and display store reviews"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/27291102795547-How-to-collect-import-and-display-store-reviews"
section: "Getting started with reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:40Z"
language: en
---

## You will learn

Learn about store reviews, also called site reviews, which reflect your entire brand rather than a single product, and how to feature them in your store.

## About store reviews

There are 2 types of reviews in Klaviyo:

- ****Product reviews****
  Reviews associated with a particular product
- ****Store reviews****
  Reviews of your entire company/brand.

## Collect store reviews

To enable store review collection:

1. Navigate to ****Reviews > Review settings > Review submission page****.
2. In the **Success page** section, select the **Ask for store review** option.
3. Select ****Save changes****.

Once you select this option, the review submission success page will include an option for reviewers to leave a store review, if they haven't left a store review before.

![The store review prompt](https://klaviyo.zendesk.com/hc/article_attachments/28881040890395)

Store reviews appear in the [SEO / All reviews widget](https://help.klaviyo.com/hc/en-us/articles/16691401577883). Add this widget to a standalone page on your site to improve SEO and provide a single location for shoppers to view all your reviews across products and your store as a whole.

### Moderate store reviews

Store reviews can be [moderated](https://help.klaviyo.com/hc/en-us/articles/19351110471323), just like product reviews. To moderate your store reviews:

1. Navigate to ****Reviews > All reviews****.
2. Under **Type**, select ****Store**** and deselect ****Product****, if it is selected.
   ![The Type menu filtered to only include Store reviews](https://klaviyo.zendesk.com/hc/article_attachments/28881024889883)
3. Review any pending store reviews. Publish or reject them as needed.

### Convert a product review into a store review

If a product review is relevant to your store as a whole, you can convert it into a store review.

1. Navigate to ****Reviews > All reviews****.
2. Select the three dots (additional options) icon next to the review.
3. Select ****Save as store review****.
   ![The Save as store review option](https://klaviyo.zendesk.com/hc/article_attachments/28881024890395)
4. In the modal that appears, select ****Both store and product review**** or ****Store review only****.
5. Select ****Save review****.

Once saved as a store review, it will appear in your SEO / All reviews widget. If you chose to save it as both a store and product review, it will remain on the applicable product review widget as well.

You cannot convert a product review with no text into a store review.

### Convert a store review into a product review

To convert a store review into a product review:

1. Navigate to ****Reviews > All reviews****.
2. Select the three dots (additional options) icon next to the review.
3. Select ****Save as product review...****
   ![The Save as product review... option](https://klaviyo.zendesk.com/hc/article_attachments/28881040893211)
4. If the review is not yet connected to a product, select a product from the modal that appears.
5. Choose whether the review should be both a product and store review, or a product review only.

Select ****Save review****.

## Import store reviews

Importing store reviews is currently supported for Yotpo, Stamped, and Okendo. For custom uploads (i.e., uploads from another provider), follow the steps in [the section below](#h_01HS15C65Q8NZ2HNVTHR66R0PH). You can import store reviews to feature directly on your site (i.e., in the SEO / All reviews widget).

To import store reviews:

1. Export reviews from your previous provider.
2. Click ****Reviews**** from the Klaviyo sidebar.
3. Navigate to the ****All reviews**** tab.
4. Select ****Options****.
5. Click ****Import Reviews****.
   ![The Import reviews button](https://klaviyo.zendesk.com/hc/article_attachments/28711732172315)
6. Select ****Stamped****, ****Yotpo****, or ****Okendo**** as your previous reviews provider.
7. Follow the steps in the import modal.

Once you’ve completed these steps, any reviews that were marked as store reviews in your import will appear as store reviews in Klaviyo.

## Import store reviews from another platform

To import store reviews from a platform other than those listed above, use the template below.

[Download a copy of this template to import reviews from another platform.](https://drive.google.com/file/d/1rVwBtGtYvlv1Os-Z2de7ZvEoztHjUYR3/view?usp=sharing)

Note that you’ll need to adjust your CSV file to match this sample format, or the upload will not work.

Include these required columns:

- ****Product ID (product\_id)****
  Must exactly match the ID of a product in your [Klaviyo product catalog](https://help.klaviyo.com/hc/en-us/articles/115005082787) (max 255 characters); alternately, use ****product\_handle****, ****product\_sku****, or ****product\_name**** as your product identifier
- ****Reviewer Email (reviewer\_email)****
  Must be a valid email address (max 3,000 characters)
- ****Review Score (rating)****
  A number, 1-5, representing the rating submitted by a customer
- ****Review Creation Date (review\_date)****
  The review submission date formatted using an [accepted date format](https://help.klaviyo.com/hc/en-us/articles/360039859932)
- ****Review Status (status)****
  Status of the review (i.e., **Published**, **Unpublished**); unpublished reviews are marked as **Pending** in Klaviyo until you approve and publish them

  The product ID column is required, even if your reviews are only for your store. If the reviews are not associated with a product, leave the product ID column blank.

  Optionally, include these columns if desired:
- ****Reviewer Display Name (reviewer\_name)****
  Generally first name + last initial (e.g., **Mark R.**) (max 300 characters)
- ****Review Content (review\_content)****
  The review submitted by a customer (max 10,000 characters)
- ****Published Image URL (image\_urls)****
  A valid, publicly-accessible image URL (or multiple comma-separated URLs); Klaviyo will save and store these images
- ****Review Title (review\_title)****
  A brief title for the review (max 3,000 characters)
- ****Review Is Verified Buyer (Yes / No) (verified)****
  Whether the reviewer is a verified purchaser; only **Yes** and **No** are accepted
- ****Reviewer Country (reviewer\_location)****
  E.g., US, UK, Canada, Australia (max 3,000 characters)
- ****Reply Content (reply\_content)****
  Your brand’s reply to the customer review (max 3,000 characters)
- ****Reply Date (reply\_date)****
  The date your brand replied to the customer review
- ****Store review (true/false) (is\_store\_review)****
  Whether or not the review is for your store as a whole. Accepts "true" or "false."

Once you’ve formatted your file to match [Klaviyo’s template](https://drive.google.com/file/d/1D5Flq0J4Y_XytJRiBgZemyIoqMDDXhUk/view?usp=drive_link), upload it:

1. Export reviews from your previous provider.
2. Click ****Reviews**** from the Klaviyo sidebar.
3. Navigate to the ****All reviews**** tab.
4. Select ****Options****.
5. Click ****Import Reviews****.
   ![The Import reviews button](https://klaviyo.zendesk.com/hc/article_attachments/28711732172315)
6. Select ****Other/Not sure****as your previous reviews provider.
7. Follow the steps in the import modal.

## Display store reviews

Once you’ve imported store reviews, you must turn on a setting so they appear in your SEO / All reviews widget alongside product reviews.

1. Navigate to ****Reviews**** in Klaviyo.
2. Click ****Reviews settings****.
3. Select ****Onsite widgets****.
   ![The onsite widgets setting card](https://klaviyo.zendesk.com/hc/article_attachments/28711703158683)
4. Select the ****SEO / All reviews widget**** card.
5. Click ****Store reviews****.
6. Toggle on the **Show store reviews** setting.
7. Choose where store reviews should appear: **A single list with product reviews** or **A separate tab for store reviews**.
   ![The store reviews setting is toggled on](https://klaviyo.zendesk.com/hc/article_attachments/28711732178843)
8. Click ****Publish changes****.