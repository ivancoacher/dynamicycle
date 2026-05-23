---
id: 28307942477211
title: "How to use in-email review collection"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/28307942477211-How-to-use-in-email-review-collection"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:46Z"
language: en
---

Learn how to allow your customers to submit a review directly from their email. With this option configured, reviewers won’t need to open a new window to leave a review.

This feature is currently available only to accounts with their language set to **English** in ****Reviews > Reviews settings > General****.

## Enable in-email review collection

1. In Klaviyo, navigate to ****Reviews****.
2. Select ****Review settings > Review requests****.
3. In the **In-email review collection** card, select ****Enable****, then confirm your choice in the modal that appears.

If the ****Enable**** button is not visible, you’ve already enabled this feature; proceed to the next section.

Once you complete this step, Klaviyo will add a universal content block to your account. You must add this block to the email(s) in your review request flow.

## Add a review collection block to a flow email

This block is only supported in flows triggered by the **Ready to review** event. If you add this block to any other flow or a campaign, it will not render correctly.

1. Navigate to your review request flow.
2. Open an email template in the flow.
3. From the **Content** tab, select ****Universal****.
   ![The universal content tab](https://klaviyo.zendesk.com/hc/article_attachments/28722600135067)
4. Search for ****In-email review collection - Klaviyo Reviews****.
5. Click and drag the in-email review request block into your email.
6. Delete the previous star rating block from your message.

Before making edits to the in-email review request block, [save a copy](https://help.klaviyo.com/hc/en-us/articles/115005413888) of it first. There is no way to revert your block to its original settings after making changes. Editing this block requires making direct edits to the code, and is only recommended for developers or code-savvy marketers.

### In-app email block code

If you need to revert to the original version of the in-email review collection block, copy your preferred code snippet below and paste it into an HTML block or a text block’s source code field:

****Without review headline****

```
<div class="kl_reviews__email_submission" style="display: block; margin: auto; padding: 24px;"><!--[if !mso]><!--><form action="{{ event.review_link }}" method="GET">
    <h4 class="kl_reviews__email_submission__header" style="font-weight: bold;">Rating</h4>
    <table class="kl_reviews__email_submission__ratings" style="width: 100%; margin-bottom: 32px;">
        <tbody>
            <tr>
                <td style="width: 20%;"><input id="rating1" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="1"> <label style="display: block; cursor: pointer;" for="rating1">1 ★</label></td>
                <td style="width: 20%;"><input id="rating2" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="2"> <label style="display: block; cursor: pointer;" for="rating2">2 ★</label></td>
                <td style="width: 20%;"><input id="rating3" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="3"> <label style="display: block; cursor: pointer;" for="rating3">3 ★</label></td>
                <td style="width: 20%;"><input id="rating4" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="4"> <label style="display: block; cursor: pointer;" for="rating4">4 ★</label></td>
                <td style="width: 20%;"><input id="rating5" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="5"> <label style="display: block; cursor: pointer;" for="rating5">5 ★</label></td>
            </tr>
        </tbody>
    </table>
    <h4 class="kl_reviews__email_submission__header" style="font-weight: bold;">Your review</h4>
    <textarea class="kl_reviews__email_submission__content" style="display: block; width: 99%; height: 120px; border: 1px solid #d9d9d9; border-radius: 4px; margin-bottom: 32px; font-size: 16px;" name="content">&#8203;</textarea> <button class="kl_reviews__email_submission__submit" style="display: block; width: 100%; border-radius: 2px; background-color: #000; color: #fff; cursor: pointer; border: none; height: 50px; font-size: 16px; margin-bottom: 32px;" type="submit"> Submit review </button></form><!--<![endif]-->
   <h4 class="kl_reviews__email_submission__fallback" style="text-align: center; font-weight: bold;">Having trouble with the form?</h4>
   <a class="kl_reviews__email_submission__fallback_link" href="{{ event.review_link }}" style="display: block; text-align: center; cursor: pointer; font-size: 14px; font-weight: 400;">Write review on the web</a>
</div>
```

****With review headline****

```
<div class="kl_reviews__email_submission" style="display: block; margin: auto; padding: 24px;"><!--[if !mso]><!--><form action="{{ event.review_link }}" method="GET">
    <h4 class="kl_reviews__email_submission__header" style="font-weight: bold;">Rating</h4>
    <table class="kl_reviews__email_submission__ratings" style="width: 100%; margin-bottom: 32px;">
        <tbody>
            <tr>
                <td style="width: 20%;"><input id="rating1" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="1"> <label style="display: block; cursor: pointer;" for="rating1">1 ★</label></td>
                <td style="width: 20%;"><input id="rating2" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="2"> <label style="display: block; cursor: pointer;" for="rating2">2 ★</label></td>
                <td style="width: 20%;"><input id="rating3" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="3"> <label style="display: block; cursor: pointer;" for="rating3">3 ★</label></td>
                <td style="width: 20%;"><input id="rating4" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="4"> <label style="display: block; cursor: pointer;" for="rating4">4 ★</label></td>
                <td style="width: 20%;"><input id="rating5" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="5"> <label style="display: block; cursor: pointer;" for="rating5">5 ★</label></td>
            </tr>
        </tbody>
    </table>
    <h4 class="kl_reviews__email_submission__header" style="font-weight: bold;">Your review</h4>
    <textarea class="kl_reviews__email_submission__content" style="display: block; width: 99%; height: 120px; border: 1px solid #d9d9d9; border-radius: 4px; margin-bottom: 32px; font-size: 16px;" name="content">&#8203;</textarea>
    <h4 class="kl_reviews__email_submission__header" style="font-weight: bold;">Review headline</h4>
    <input class="kl_reviews__email_submission__headline" style="display: block; width: 99%; height: 36px; border: 1px solid #d9d9d9; border-radius: 4px; margin-bottom: 32px; font-size: 16px;" name="headline" type="text">
    <button class="kl_reviews__email_submission__submit" style="display: block; width: 100%; border-radius: 2px; background-color: #000; color: #fff; cursor: pointer; border: none; height: 50px; font-size: 16px; margin-bottom: 32px;" type="submit"> Submit review </button></form><!--<![endif]-->
    <h4 class="kl_reviews__email_submission__fallback" style="text-align: center; font-weight: bold;">Having trouble with the form?</h4>
    <a class="kl_reviews__email_submission__fallback_link" href="{{ event.review_link }}" style="display: block; text-align: center; cursor: pointer; font-size: 14px; font-weight: 400;">Write review on the web</a>
</div>
```

### About the in-email review block

The in-email review block contains 3 fields:

- ****Review rating****
  A radio button option to select 1-5 stars
- ****Review content****
  An open text field for review content
- ****Review headline****
  An open text field for a review headline or title (only visible if selected in the review submission page editor)

These fields are not editable. Custom questions will not appear in the in-email review block.

![An example of the in-email review collection form](https://klaviyo.zendesk.com/hc/article_attachments/28722600137371)

## Limitations

This functionality relies on the HTML <form> element, which is [not supported by all inbox providers](https://www.caniemail.com/features/html-form/). If a recipient opens your review request email in an inbox that doesn’t support the form element, they will see a link to submit a review instead.

Custom questions are not supported for in-email review collection. If you have custom questions, reviewers will only see them in certain scenarios.

- If you have ****required**** custom questions, submitting the in-email review form will redirect reviewers to a new tab where they must complete the custom questions to submit their review. Partial review submissions will not be stored.
- If you have ****non-required**** custom questions, reviewers will see a success page after submitting their review from their inbox. Only those who navigate to the product page and click the ****Write a review**** button will see your custom questions.

## Outcome

Once you complete these steps, your customers can submit reviews directly in email, without needing to open another tab or window to access your review request form.