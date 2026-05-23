<h1>How to import product reviews data from another platform</h1>

## You will learn

Learn how to import reviews and custom questions from your prior platform into Klaviyo Reviews. There are 2 ways to import reviews:

- Export reviews and directly upload them to Klaviyo (supported providers only)
- Format your CSV file and upload to Klaviyo (all other providers)

Only import valid reviews exactly as submitted by real customers. Do not edit reviews between exporting them from your prior platform and uploading them to Klaviyo.

This article covers importing product reviews. If you have reviews for your brand as a whole, [learn how to import store reviews](https://help.klaviyo.com/hc/en-us/articles/27291102795547).

## Export reviews from your previous reviews platform

The steps required to export reviews from your prior reviews platform depend on which platform you used previously. Head to their support documentation to learn how to export your reviews as a CSV. Make sure to export individual reviews, not review summaries.

Learn how to export reviews from:

- [Yotpo](https://support.yotpo.com/docs/exporting-reviews-from-yotpo)
- [Okendo](https://help.octaneai.com/en/articles/7932726-exporting-reviews-from-okendo)
- [Stamped](https://stampedsupport.stamped.io/hc/en-us/articles/8839244356891-Exporting-Reviews-Checkout-Comments-or-NPS)
- [Reviews.io](https://support.reviews.io/en/articles/9185047-how-to-export-your-reviews)
- [Judge.me](https://help.judge.me/en/articles/8236266-exporting-reviews)
- [Loox](https://help.loox.io/article/21-how-do-i-export-my-reviews)

## Import requirements

For most reviews platforms, you just need to export your reviews and import them directly into Klaviyo. It’s unlikely that you’ll need to make edits to the CSV file.

Your CSV file must contain columns with the following information:

- Product IDs that exactly match the product IDs synced to Klaviyo from your store
  - When importing store reviews that aren't associated with a product, this field may be blank; the product ID column is still required
- Review text
- Reviewers’ emails

## Identify whether your previous reviews provider is supported

Klaviyo provides an automatic upload tool for a variety of reviews providers. If your past reviews provider is supported, ****don’t make any edits**** to the CSV file of reviews you exported. To check which reviews providers are supported:

1. Click ****Reviews**** from the Klaviyo sidebar.
2. Navigate to the ****All reviews**** tab.
3. Select ****Options****.
4. Click ****Import Reviews****.

Here, you’ll see all supported reviews providers.

- If you see your provider here, learn how to [import your reviews](#h_01HS15C65QTH13PSHJRXGNGB5V).
- If you don’t see your provider, learn how to [format your CSV before uploading](#h_01HS15C65Q8NZ2HNVTHR66R0PH).

## Import your reviews from a supported provider

Most reviews can be directly uploaded to Klaviyo Reviews.

1. Click ****Reviews**** from the Klaviyo sidebar.
2. Navigate to the ****All reviews**** tab.
3. Select ****Options****.
4. Click ****Import Reviews****.
5. Choose your previous reviews platform from the options provided. If you don’t see your platform listed, select ****Other/not sure****.

   If you select ****Other/not sure****, you must format your CSV using [the template in the section below](#h_01HS15C65Q8NZ2HNVTHR66R0PH) before proceeding.
6. Click ****Choose file**** or drag and drop your CSV file into the upload tool.
7. If accurate, check the box next to **I confirm that the imported reviews are genuine**. Only legitimate reviews may be uploaded to Klaviyo.
8. Review the mapping of fields from your upload and make adjustments as needed.
9. Click ****Next****.

During the upload, you’ll see a modal with a status bar. Once the upload is complete, that modal will display the number of successful and failed review uploads from the CSV.

## Import video reviews

Video reviews can be imported if your CSV contains a column for video URLs. The following platforms provide this column:

- Yotpo
- Okendo
- Stamped

  Klaviyo accepts the following file types:
- MP4
- MOV

Each video has a maximum file size of 200 MB.

### Import custom questions (Yotpo only)

If your previous reviews provider was Yotpo and you used their Custom Questions feature, you can import a reviewer’s answers directly into Klaviyo.

To upload custom questions, follow the steps in the section above. Then, map your Yotpo custom questions to custom questions in Klaviyo. Follow these tips to make sure your questions import correctly:

- Don’t edit the CSV file you export from Yotpo; Klaviyo automatically detects your custom questions and suggests which Klaviyo custom questions to map them to.
- Make sure to select ****Yotpo**** as your previous reviews provider.
- If you decide not to import a custom question, use the checkbox to deselect it.
- On the mapping page, a tag icon indicates that the custom question is only related to certain products. You can update this in your Klaviyo custom questions settings.

If you’ve previously imported a review and attempt to reimport it, that review will be skipped, even if it didn’t include custom questions during the initial import.

When uploading your reviews, you’ll have the opportunity to configure your custom questions in Klaviyo, if they haven’t been set up already. To import custom questions:

1. Follow the standard upload steps outlined above, selecting ****Yotpo**** as your previous provider.
2. After mapping the standard review fields, click ****Next****.
3. For each custom question, select an existing custom question or click ****Add question****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33630036170523)
4. After completing these steps for all custom questions, click ****Next**** and continue with the import process.

## Import your reviews from another platform

To import reviews from a platform other than those listed on the upload page, use the template below.

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

1. Click ****Reviews**** from the Klaviyo sidebar.
2. Navigate to the ****All reviews**** tab.
3. Select ****Options****.
4. Click ****Import Reviews****.
5. Select ****Other/not sure****.
6. Click ****Choose file**** or drag and drop your CSV file into the upload tool.
7. If accurate, check the box next to **I confirm that the imported reviews are genuine**. Only legitimate reviews may be uploaded to Klaviyo.
8. Review the mapping of fields from your upload and make adjustments as needed.
9. Click ****Next****.

## Troubleshoot a failed upload

If your CSV upload of reviews from another platform fails, check the product IDs included in the CSV. They must exactly match product IDs found in Klaviyo, which are automatically pulled in from your ecommerce platform.

To check whether a product ID from your CSV is synced to Klaviyo:

1. Navigate to ****Content > Products**** in the Klaviyo sidebar.
2. In the catalog search bar on the **Items** tab, search for a product ID from your CSV.
3. If no results are found, replace the product ID in your CSV with the correct product ID found in Klaviyo/Shopify, then retry your upload.

Make sure your spreadsheet software hasn't converted your product IDs to scientific notation.

![Product IDs in scientific notation](https://klaviyo.zendesk.com/hc/article_attachments/30005015803419)

If it has, replace the scientific notation product IDs with corrected ones.
