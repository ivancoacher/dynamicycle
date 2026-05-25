---
id: "23145809959707"
title: "How to enable and use email annotations for Gmail"
source_url: "https://help.klaviyo.com/hc/en-us/articles/23145809959707-How-to-enable-and-use-email-annotations-for-Gmail"
section: "Advanced template design"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-05-11T10:57:19Z"
language: "en"
---
## You will learn

Learn about email annotations, which enable you to display key information in the list view for Gmail inboxes (i.e., before someone opens the email). Email annotations allow you to highlight a deal or offer (e.g., a coupon code), or display product images directly in the inbox.

The code required to implement Gmail annotations is only supported in custom HTML or hybrid emails. It is not possible to use this code with Klaviyo’s drag-and-drop email editor.

We only recommend using email annotations for technically savvy marketers, or for anyone who has access to a developer. While our product does support this feature, our support team cannot help you build out your custom templates beyond offering the general guidance covered in this documentation. To maintain the security of your data, Klaviyo's support team is not able to open your HTML files.

## About email annotations

Email annotations are supported in Gmail mobile inboxes for users with the **Promotions** tab enabled. These annotations only appear in the **Promotions** tab, not the primary inbox.

There are 3 types of annotations:

- ****Deal/offer****
  Highlight a deal or offer, like a coupon code or free shipping, including the deal expiration date.
  ![Bolas baked goods deal annotation](https://klaviyo.zendesk.com/hc/article_attachments/28718022989339)
- ****Product carousel****
  Display a carousel of product images, optionally including product details like name and price.
  ![Product carousel annotations](https://klaviyo.zendesk.com/hc/article_attachments/28718022991771)
- ****Single image****
  Show a single image, along with optional additional text.
  ![Single image annotations](https://klaviyo.zendesk.com/hc/article_attachments/28718022993947)

Adding this code provides Gmail with the option to display annotations for your email. Even if an email contains the code for annotations, they may not be displayed to every recipient. Gmail chooses when and how to display annotations based on recipient settings and inbox density. .

## Before you begin

Google maintains an allowlist of senders who can use annotations. Before using annotations, you must request that your brand be added to this allowlist.

To request that Google add you to their annotations allowlist, [send an email to p-Promo-Outreach@google.com](mailto:p-Promo-Outreach@google.com?subject=Allowlisting%20for%20email%20annotations&body=REPLACE%20ALL%20PLACEHOLDERS%20WITH%20YOUR%20COMPANY%20INFORMATION%20BEFORE%20SENDING%0AHello%20team%2C%20%0AI'm%20a%20Klaviyo%20customer%20writing%20to%20request%20that%20www.example.com%20be%20added%20to%20your%20email%20annotations%20allowlist.%20%0AMy%20sending%20domain%20is%20www.example.com%0AWe%20use%20the%20following%20subdomains%3A%20%0A-%20send.example.com%0A-%20marketing-messages.example.com%0AOur%20landing%20page%20URL%20is%20www.example.com%0AThanks%2C%0AYOUR%20NAME) with the following information:

- All domains (e.g., example.com)
- All subdomains (e.g., send.example.com, blog.example.com, marketing-messages.example.com)
- Your landing page URL(s) (e.g., your homepage)

Any annotations code added to your messages will be ignored until you are added to the Google allowlist, which can take 7-10 business days or more.

Klaviyo does not have visibility into the allowlisting process and cannot expedite your request. If you have questions about the whitelisting process or the status of your request, reach out to [p-Promo-Outreach@google.com](mailto:p-Promo-Outreach@google.com).

## Add annotations to your emails

Add the following code within the body section of your HTML email template to add email annotations. There are 3 types of annotations available:

- [Deal annotations](#h_01HQ6P8JEGEDJR27ZSC5YYHXTX)
- [Product carousel annotations](#h_01HQ6P8JEG583BSXQXXMHHGPQN)
- [Single image annotations](#h_01HQ6P8JEGERCMEAT35S9P4CV2)

#### Deal

```
  <div itemscope itemtype="http://schema.org/DiscountOffer">
    <meta itemprop="description" content="DESCRIPTION"/>
    <meta itemprop="discountCode" content="DISCOUNT_CODE"/>
    <meta itemprop="availabilityStarts" content="START_DATE_TIME"/>
    <meta itemprop="availabilityEnds" content="END_DATE_TIME"/>
  </div>
```

![Bolas baked goods deal annotation](https://klaviyo.zendesk.com/hc/article_attachments/28718022989339)

Replace the following placeholders in the code:

- ****DESCRIPTION****
  A brief (1-2 line) text description of the offer
- ****DISCOUNT\_CODE****
  The code a recipient can enter at checkout to receive the offer
- ****START\_DATE\_TIME****The offer start date/time, using [ISO 8601 format](https://support.google.com/merchants/answer/12756212?visit_id=638424907272835479-1199962788&rd=1)
- ****END\_DATE\_TIME****
  The offer end date/time, using [ISO 8601 format](https://support.google.com/merchants/answer/12756212?visit_id=638424907272835479-1199962788&rd=1)

#### Product carousel

```
  <div itemscope itemtype="http://schema.org/PromotionCard">
    <meta itemprop="image" content="IMAGE_URL1"/>
    <meta itemprop="url" content="PROMO_URL1"/>
    // Optionally, include the following PromotionCard properties:
    <meta itemprop="headline" content="HEADLINE1"/>
    <meta itemprop="price" content="PRICE1"/>
    <meta itemprop="priceCurrency" content="PRICE_CURRENCY1"/>
    <meta itemprop="discountValue" content="DISCOUNT_VALUE1"/>
    <meta itemprop="position" content="POSITION"/>
  </div>
  // Build the second image preview in your product carousel:
  <div itemscope itemtype="http://schema.org/PromotionCard">
    <meta itemprop="image" content="IMAGE_URL2"/>
    <meta itemprop="url" content="PROMO_URL2"/>
    // Optionally, include the following PromotionCard properties:
    <meta itemprop="headline" content="HEADLINE2"/>
    <meta itemprop="price" content="PRICE2"/>
    <meta itemprop="priceCurrency" content="PRICE_CURRENCY2"/>
    <meta itemprop="discountValue" content="DISCOUNT_VALUE2"/>
    <meta itemprop="position" content="POSITION"/>
  </div>
  // To include more image previews, add additional PromotionCard objects.
  // You can include up to 10 image previews in a product carousel.
```

![Product carousel annotations](https://klaviyo.zendesk.com/hc/article_attachments/28718022991771)

Replace the following placeholders in the code:

- ****IMAGE\_URL1****, ****IMAGE\_URL2****, etc.
  The URL of a product image to display in the carousel. Supported aspect ratios are 4:5, 1:1, and 1.91:1. The aspect ratio for every image must be the same.
- ****PROMO\_URL1****, ****PROMO\_URL2****, etc.
  The URL to a landing page for recipients who click the product image.
- ****HEADLINE1, HEADLINE2, etc.****
  A short, 1-2 line description of the product.
- ****PRICE1****, ****PRICE2****, etc.
  The base price of the product (number only, no currency).
- ****PRICE\_CURRENCY1****, ****PRICE\_CURRENCY2****, etc.
  The 3-letter currency code (e.g., USD) for the item’s price.
- ****DISCOUNT\_VALUE1****, ****DISCOUNT\_VALUE2****, etc.
  If applicable, the amount an item is discounted (number only, no currency).
- ****POSITION****
  (Optional) a number indicating this item’s position in the carousel.

#### Single image

```
  <div itemscope itemtype="http://schema.org/PromotionCard">
    <meta itemprop="image" content="IMAGE_URL1"/>
    <meta itemprop="url" content="PROMO_URL1"/>
  </div>
```

![Single image annotations](https://klaviyo.zendesk.com/hc/article_attachments/28718022993947)

Replace the following placeholders in the code:

- ****IMAGE\_URL1****
  The URL of a product image to display in the carousel. Supported aspect ratios are 4:5, 1:1, and 1.91:1.
- ****PROMO\_URL1****
  The URL to a landing page for recipients who click the product image.

## About automatic annotation extraction

Sometimes, Google automatically extracts email data to add annotations, even when a sender hasn’t added the code outlined above. This is done at Google’s discretion, and cannot be controlled by the sender.

## Troubleshooting your annotations

Google enforces strict requirements for annotations, and they may not display for multiple reasons. If your annotations are not appearing after following this article's setup instructions outlined above, try the troubleshooting steps below:

### Ensure your brand is allowlisted

Google maintains a limited allowlist of approved brands that can use email annotations in order to prevent spam and abuse. If you don't have access, you may need to request it from Google:

1. [Reach out to Google](#h_01HQ6P8JEFJ8HXDR85SCV96C66) using the steps outlined above.
2. Allow 7-10 business days for a response.

There is no guarantee that your brand will be added to the allowlist once you request it, as this is managed at Google’s sole discretion.

### Check your image quality

All images used for email annotations must pass Google's quality filter. Images that don't meet the requirements will not display in the inbox. Make sure your images meet these criteria:

- High quality (i.e., greater than 500 KB)
- Have very little, if any, text
- Are rectangular (don’t use a mask to make the image round, or another shape)
- Are at least 256x256 pixels in size

### Don’t use unique images per recipient

The same image must be used for all recipients. You may add unique tracking parameters to the promo url, but not the image URL.

Avoid using tools that generate CID images (i.e., images that are unique per recipient), as annotations will not show if used.

### Consider Gmail’s density cap

Google limits the number of annotation images a user can see in their inbox at one time (i.e., a "density cap"). If a recipient’s inbox already has several recent emails with annotations, yours may not appear to prevent clutter. This cap is implemented at Google’s sole discretion and cannot be controlled by the sender.

### Note that annotations may not appear in preview email sends

Annotations typically will not appear in the inbox for test emails sent to only a few recipients. The annotations feature is designed for bulk sends, so annotations are likely to only appear when a message is sent to >100 recipients.

### Ensure you're looking in the supported Gmail tab

Annotations are supported to display only in the Gmail mobile app in the **Promotions** tab.

Annotations are not supported to display in:

- Any other tabs in the Gmail app, besides **Promotions**
- Gmail viewed in any web browser (e.g., the mobile or desktop site)
- Inboxes for users who do not have the **Promotions** tab enabled in their Gmail settings

## Additional resources

- [How to use Klaviyo’s subject line assistant](https://klaviyo.zendesk.com/hc/en-us/articles/5051278887835)
- [Understanding Gmail's tabbed inbox](https://klaviyo.zendesk.com/hc/en-us/articles/115005078307)