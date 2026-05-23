<h1>Understanding review statuses and types</h1>

## You will learn

Learn about review verification and publication statuses. These indicators determine whether and how a review appears on your website and product pages.

## Understanding reviews and ratings

When someone reviews a product from your store, they can choose to leave a review that consists of a rating only, a rating and a text review, or a rating and any combination of the following elements:

|  |  |
| --- | --- |
| ****Review element**** | ****Required?**** |
| Rating | Always required |
| Text | Can be required; can set minimum word count |
| Title | Always required if collected |
| Media | Never required |
| Custom questions | Can be required |

To require that all reviews include a title or text:

1. Navigate to ****Reviews > Reviews settings****.
2. Select ****Review submission**** ****page****.
3. Under **Submission page**, select the settings you’d like to enable:
   1. Require a review title by selecting ****Ask for review title****.
   2. Require review text by selecting ****Require review text for submission****.
   3. Optionally, select ****Set minimum word count**** and select a number to set a minimum word count for text reviews.
4. Click ****Save changes****.

### Reviews without text

As of September 26, 2024, all reviews (including reviews without text) appear in the ****All reviews**** tab. If a review does not include text, you will see the label **This review does not contain text**. Learn how to [moderate rating-only reviews](https://help.klaviyo.com/hc/en-us/articles/19351110471323).

![A review without text](https://klaviyo.zendesk.com/hc/article_attachments/29583042165915)

To see only reviews with text, select ****Show only > Includes text**** in the filters sidebar.

![Option to only view reviews with text](https://klaviyo.zendesk.com/hc/article_attachments/29583042168603)

This change increases your visibility into your customers' feedback and your control over what appears on your site.

## Verified reviews

If Klaviyo can determine confidently that a true purchaser of the product submits a review, it will mark the review as verified. In the Klaviyo **All reviews** list, verified reviews have a small checkmark next to the reviewer's display name.

![Reviews list checkmark](https://klaviyo.zendesk.com/hc/article_attachments/28720790272283)

Additionally, verified reviews will have a **Verified buyer** badge on your site when published.

![Public verified buyer badge](https://klaviyo.zendesk.com/hc/article_attachments/28720761771931)

Klaviyo marks a review as verified when:

- A customer submits a review by clicking a link in a [Klaviyo Review request flow](https://help.klaviyo.com/hc/en-us/articles/16319809379611).
- A user uploads a list of verified reviews from a past platform.
- A customer submits a review manually (i.e., by clicking the ****Write a review**** button on a product page) using an email addresses attached to a previous order containing that product.

Verification occurs at the time a review is submitted. If 2 profiles are merged, one containing the review event, and the other containing a placed order event for the reviewed product, the review will ****not**** retroactively be marked as verified.

### Importing verified reviews

Note that Klaviyo only supports verified uploaded reviews from certain platforms. Your upload file must contain a column indicating whether the review is verified or not.

- Verified reviews ****are supported**** for reviews uploaded from Yotpo, Stamped, Okendo, Loox, and Fera.
- Verified reviews are ****not supported**** for reviews uploaded from Yelp, Shopify Product Reviews, and Judge.me. However, you can manually [edit your CSV file to match Klaviyo's template](https://help.klaviyo.com/hc/en-us/articles/16318811222555#h_01HS15C65Q8NZ2HNVTHR66R0PH) and import using the ****Other/Not Sure**** option to import reviews from these platforms as verified.

It is not possible to manually mark a review as verified after is has been imported into Klaviyo.

## Publication statuses

Every review you receive has a publication status (i.e., pending, published, or rejected). By default, Klaviyo will automatically publish 4- and 5-star reviews, while 1-, 2-, and 3-star reviews are pending until you approve or reject them. To adjust your reviews auto-publish settings:

1. Select the ****Reviews**** tab in Klaviyo.
2. Click ****Reviews settings****.
3. Click ****Publishing rules and notifications****.
4. Make adjustments as desired, then click ****Save changes****.

The default status for reviews imported from another platform is **Pending**. However, if your CSV contains a column indicating approval status, approved reviews will be imported as **Published**. The following statuses import as **Published**:

- Fera: **state** column = "approved"
- Judge.me: **curated** column = "ok"
- Loox: **status** column = "Active"
- Okendo: **isApproved** column = "true"
- Shopify Product Reviews: **state** column = "published"
- Stamped: **published** column = "published"
- Yotpo:
  - **Review Status** column = "Published", or
  - **Review Is Published (Yes / No)** column = "Yes", or
  - **Published** column = "TRUE"

All reviews imported from Yelp are automatically published.

### Pending

All other reviews that do not meet your auto-publish requirements remain in **Pending** status until you publish or reject them. As a best practice, approve or reject any pending reviews at least once per week.

To publish all pending reviews at once:

1. Navigate to ****Reviews**** in Klaviyo.
2. In the **Overview** tab, scroll to the **Pending activity** card.
3. Open the additional options (3 dots) menu.
4. Select ****Publish all pending reviews****.
   ![Publish all pending reviews button](https://klaviyo.zendesk.com/hc/article_attachments/29565147729563)
5. In the modal that appears, confirm that you’re ready to publish all pending reviews.

****Note: When you publish all pending reviews, the system disregards any rules including any flagged words and publishes everything. You should reject reviews that violate rules before publishing all pending reviews.****

### Published

All approved reviews are marked as **Published**. These reviews are visible within the Klaviyo Reviews widgets on your site.

If desired, you can publicly reply to a published review by clicking the reply arrow next to it in Klaviyo.

Replies are visible in the reviews list, so site visitors can see your response. Review replies are not automatically sent to the reviewer.

### Rejected

Use caution when rejecting reviews, as regulators have limitations on moderating reviews to ensure the integrity and accuracy of the reviews-related practices followed by businesses. Reviews may be rejected for the following reasons:

- ****Profanity / inappropriate****
  Contains inappropriate, crude, or sexual language
- ****Contains private information****
  Contains identifying or otherwise private information like phone numbers, email addresses, etc.
- ****Unrelated to the product or service****
  Complaints related to shipping delays, or otherwise unrelated to the product/service being reviewed
- ****False or misleading****
  Contains inaccurate information that could mislead a potential customer
- ****Fake****
  Reviews submitted by bots or people who have never used the product/service

Learn more about [reviews regulations and best practices](https://help.klaviyo.com/hc/en-us/articles/16685026123035).

## Featured reviews

Featured reviews appear in the featured review carousel widget, if you choose to install it on your site. Note that only reviews containing text can be featured.

To feature a review:

1. Navigate to ****Reviews > All reviews**** in Klaviyo.
2. Select the ****Feature**** button next to your desired review.

The option to ****Feature review highlight**** will appear if the review has an AI highlight. You can tell there is an AI highlight if there is a purple underline within the text review.

## Incentivized reviews

Any review that was provided in exchange for something, like a discount code or free product, is incentivized. [Indicate which reviews are incentivized](https://klaviyo.zendesk.com/hc/en-us/articles/26652098724123) in your review widgets by manually adding an incentivized tag or automatically noting this through your review request flows.

![Incentivized review](https://klaviyo.zendesk.com/hc/article_attachments/28720790274459)

## Product and store reviews

There are 2 types of reviews in Klaviyo:

- ****Product reviews****
  Reviews associated with a particular product.
- ****Store reviews****
  Reviews of your entire company/brand. Store reviews are only supported when imported from another provider, like Stamped, Yotpo, or Okendo.

Learn more about [store reviews](https://help.klaviyo.com/hc/en-us/articles/27291102795547).
