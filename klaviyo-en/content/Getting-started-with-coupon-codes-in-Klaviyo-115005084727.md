---
id: "115005084727"
title: "Getting started with coupon codes in Klaviyo"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005084727-Getting-started-with-coupon-codes-in-Klaviyo"
section: "Getting started with coupons"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-05-11T12:54:53Z"
language: "en"
---
## You will learn

Learn how to create and upload unique and static coupon codes in Klaviyo to incentivize customers to engage with your brand. Offering an incentive can help you improve the customer experience, resulting in higher sales and increased lifetime value.

This guide will cover how to upload and manage static and unique coupons in Klaviyo; however, if you have a [Shopify](https://help.klaviyo.com/hc/en-us/articles/115006155388), [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/22168739689627), [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/25151598311195), [Magento 1.x](https://help.klaviyo.com/hc/en-us/articles/115005246547), or [Magento 2](https://klaviyo.zendesk.com/hc/en-us/articles/360041971851) store, you can also generate new unique coupon codes in Klaviyo (and do not need to upload them).

## Before you begin

There are multiple ways to use coupon codes in Klaviyo. This guide covers:

- Creating and using static coupon codes.
- Uploading unique coupon codes.
- Adding coupons to your emails, SMS messages and sign-up form success messages.
  - Displaying your coupons as barcodes for your brick-and-mortar stores.
- Setting up coupon reminders for customers that haven't used a coupon code.
- Seeing who used specific discount codes (Shopify and Magento 1.x stores).

## Unique vs. static coupon codes

There are 2 types of coupon codes that you can use: static and unique.

- A static coupon code is a single phrase or alphanumeric string that unlocks a specific discount (e.g., Welcome20). Every person will receive the same code to use on your site so they can be widely shared; however, they are easier to remember and use.
- Unique, also called "dynamic," coupon codes are a random series of numbers or letters that a recipient can use 1 time. Each recipient will receive their own coupon code, and no 2 recipients will have the same code. Unique codes are typically longer and more complicated than static codes; however, they limit oversharing of discounts.

## Create and use static coupons

Static codes are quick to generate, and you can add them into any Klaviyo email, SMS message, or sign-up form success message once the coupon is created. To create and use a static coupon:

1. Create the coupon in your ecommerce store.
2. Add your static coupon code directly in your message.

- For emails and SMS templates, drag and drop a text block wherever you want to display the coupon in the template editor. Then, type your static code in the text block, making sure it's large and easy to see.
  ![An example email template displaying a static coupon written in large, eye-catching font.](https://klaviyo.zendesk.com/hc/article_attachments/28711675012635)
- For sign-up forms, we suggest adding the coupon in the success message (the last step of the form) to incentivize site visitors to fill out the form. See [how to add coupon codes to sign-up forms](https://help.klaviyo.com/hc/en-us/articles/6038674938523) for more details.

Static codes are the same for everyone, so you do not need to take any other steps in Klaviyo.

## Upload unique coupons into Klaviyo

Unique coupons work well when you're rewarding a recipient for taking a specific action (e.g., signing up for your email newsletter). To upload unique coupons into Klaviyo to use in your email and SMS messages, you'll need to

1. Prepare a list of unique codes
2. Upload the unique coupon codes into Klaviyo

The following sections will walk you through each of these processes, or you can follow the video below.

![](https://fast.wistia.com/embed/medias/w3qfjowdix/swatch)

Klaviyo will send low coupon notifications when you are running low on available coupon codes. If a coupon was sent in the last 24 hours and there are less than 500 codes available, the account owner will be notified via email.

### Prepare your list of coupon codes

First, prepare a list of unique coupon codes. Use a third-party tool of your choice to generate a number of unique coupons and save it as a .csv file.

Verify that:

- Each code is unique.
- You've generated enough codes for all of the subscribers who will receive the message.
- The list of codes is saved as a CSV file.
- One column in the list has `Coupon` or `Coupon Code` as the header.

Below is an example of what a list of coupon codes look like in a spreadsheet.

![An example spreadsheet showing ten unique coupon codes listed under a heading that says Coupon.](https://klaviyo.zendesk.com/hc/article_attachments/28711675019547)

### Upload the unique codes into Klaviyo

1. Navigate to ****Coupons****.
2. Toggle to ****Uploaded Coupons.****
   ![The Uploaded Coupons tab on the Coupons page where you can click the Create Uploaded Coupon button.](https://klaviyo.zendesk.com/hc/article_attachments/28711662887579)
3. Click ****Create Uploaded Coupon**** to add a new coupon code. If you've uploaded coupons in the past, this button will be in the top right corner.
4. Choose a name, minimum coupon count, and an expiration date for your coupon (e.g., ****After 1 year**** or ****On a specific date**** and specify the date).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39700440015131)

   The minimum coupon count must be a value between 100 - 5000. Values outside of that range are not accepted. If no minimum is specified, the default count will be 500.
5. Click ****Create Coupon**** to save your coupon.
6. On the **Uploaded Coupons** tab, select the ****3 dots > Add codes**** next to your coupon.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38522703232411)
7. Upload your list of coupon codes either by dragging and dropping your file or selecting it from your computer.
8. Review the first few rows of your CSV file to confirm you've chosen the right coupons.
   ![The review page that appears after you upload a CSV file where you can review the first few coupon codes added.](https://klaviyo.zendesk.com/hc/article_attachments/28711662908699)
9. Click ****Import Coupons****.
10. After your coupons finish importing, you can see how many coupon codes uploaded successfully and how many were skipped because of duplicates or a lack of data.
    ![The Recent Coupon Uploads table showing the details and status for an example uploaded unique coupon that was just imported.](https://klaviyo.zendesk.com/hc/article_attachments/28711675047451)
11. Click ****Done****.

Keep in mind that you must always have enough coupon codes to send to recipients. If you send a campaign or flow message without enough available coupon codes, the messages will be skipped.

****Tips on uploading unique coupon codes****

You can generate your own set of unique coupon codes outside of Klaviyo, upload them to your Klaviyo account, and reference them in your campaign or flow messages. This is a useful method if you're using point of sale software that can generate and manage coupon codes. There are some important things to note when uploading coupons using this method.

- Klaviyo doesn't maintain any metadata on your coupons. This means we don't know how much the code is worth, what the expiration period is, which restrictions there are on the code's use.
- You are responsible for ensuring the validity and expiration dates that these codes will work at your point of sale system.
- You can set an expiration date when adding coupon codes, but this date only applies to how long the coupon codes are available in your Klaviyo account. Please note that dates are in the UTC time zone.
- By default, uploaded coupon codes will be stored in Klaviyo for one year. After that year, unsent codes will expire automatically, and you will need to upload new codes. To extend the expiration date beyond one year, select your preferred expiration date.
- Uploaded coupon codes will be stored in Klaviyo for one year by default. To extend coupons expiration beyond one year, use a custom expiration date. Once codes expire, unsent ones will be invalid and must be re-uploaded.

## Use coupons in messages

To add a unique coupon code in any message:

1. Open the personalization menu from a text field. This may look like a small person icon, or a button labeled ****Personalization****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892633181467)
2. From the **All types** menu, select ****Coupons****.
3. Select your coupon.
4. The coupon will be inserted into the text field. If you'd like the use a coupon in a text field that doesn't show the personalization menu (e.g., a button block), you can insert the tag into a text block, then copy and paste it elsewhere.

![The template tag with an example coupon name pasted on an example email template.](https://klaviyo.zendesk.com/hc/article_attachments/28711675053211)

If a coupon is included in a block that is hidden with [show/hide logic](https://help.klaviyo.com/hc/en-us/articles/7655965301531), codes will still be generated.

### Email

You can include multiple codes per email (but only 1 code per SMS). If you use multiple coupons in a message, make sure you have enough codes for every recipient to receive 1. With email, you also have the option to use [hidden blocks](https://help.klaviyo.com/hc/en-us/articles/7655965301531) to send different coupons based on where someone lives or what they've done. We recommend exercising caution with this feature, because codes may be assigned to all recipients (even if they end up hidden in your message) and block your send if there aren't enough codes.

After sending your email, you can check the total coupon codes by clicking into the ****Coupons**** tab and checking the ****Available/Total**** column.

![](https://klaviyo.zendesk.com/hc/article_attachments/38523965821467)

When sending uploaded coupon codes in emails, if your send list is larger than your available coupon codes, then the messages scheduled will be skipped.

- If the code is used in a campaign message, Klaviyo will compare the number of expected recipients to the number of available codes for the coupon used. A warning is displayed if there aren't enough codes available, and you are unable to send the campaign. When A/B testing, you will need enough available codes to cover the full send, even if your code is only being sent to a part of the list or segment you are sending to.
- If the code is used in a flow message (e.g., a welcome series or abandoned cart flow) you will need to upload more unique codes on a regular basis. Since flows are sent on a recipient-by-recipient basis, Klaviyo cannot check to make sure that enough codes are available. Flow emails that contain coupon codes with 0 available cannot be turned live. At send time, if a flow email contains a coupon with no available codes, the email will be skipped. You can see who was skipped by clicking into the analytics of the flow email and clicking ****Recipient Activity > Other****.

### SMS or MMS

Mobile messages may only contain a single coupon code. Any SMS/MMS containing multiple coupons will display an error message and will not send.

![Error message for when two dynamic coupons are included in an SMS](https://klaviyo.zendesk.com/hc/article_attachments/28711674998427)

You can also [add a unique coupon code to the success step of a sign-up form](https://help.klaviyo.com/hc/en-us/articles/6038674938523#h_01HA28D5B0W8N9E9B1AQSSCB2N) to encourage viewers to opt in to your messaging.

### Push notifications

Coupons can be added to both the title and body of a push notification.

![Push notification with coupon in title](https://klaviyo.zendesk.com/hc/article_attachments/31567376584731)

## Send coupons as barcodes (email only)

If you also have brick-and-mortar stores, you can save your customers (and your cashiers) time by providing a barcode coupon that can quickly be scanned at your point of sale system.

To display a barcode in an email template, use the following template tag:

`{% barcode_code 'CouponName' height=100 width=200 %}`

The height is measured in pixels and can be adjusted to serve the design requirements for your template.

Below is a preview of the email with this barcode.

![Preview of an email with a coupon in a barcode](https://klaviyo.zendesk.com/hc/article_attachments/28711674984731)

Some point-of-sale systems required you to add special characters to your coupon code before it is rendered into a barcode. If you need more control over the code before being rendered, adding the `cut` parameter to your coupon template tag removes a specific character or characters from alllocations in the code displayed.

For example, let's say your point of sale system requires that you render your barcodes from coupon codes that begin with a hashtag. For your site, you need to remove this hashtag. You can use the `cut` parameter to pass one version of this code as a barcode, and a separate version that does not include the hashtag for your other code. For the code `#GREATdoggo12345`, the following tags display these values for a user:

```
{% coupon_code 'CouponName' cut=# %} == GREATdoggo12345
{% coupon_code 'CouponName' cut=G %} == #REATdoggo12345
{% coupon_code 'CouponName' cut=g %} == #GREATdoo12345
{% coupon_code 'CouponName' cut=5 %} == #GREATdoggo1234
{% coupon_code 'CouponName' cut=#Gg5 %} == REATdoo1234
```

The `cut` parameter has the following limitations:

- This is case sensitive. For example, using `cut=i` will remove `i` but not `I`.
- Multiple items can be combined with a single `cut` parameter tag.

If you're using the `cut` parameter, ensure that you fully understand how characters are removed from your rendered code so that customers do not receive corrupted codes.

## Previewing coupon codes in messages

If you send a preview of a coupon to your email or phone number, it will use 1 of your generated coupon codes.

For a coupon to preview with a real code in an inbox, you must have coupon codes available. The same preview code will be shown across inboxes for 1 minute, after which sending another preview will show a new code.

However, if you preview the coupon within Klaviyo (i.e., looking at it in-app), the preview will show the coupon name followed by "-PREVIEW." In this case, the preview does not show an actual coupon code or use one of your available codes. Additionally, when previewing coupons placed in flows, you will also see the **PREVIEW** text displayed.

![preview of coupon within Klaviyo showing coupon name followed by -PREVIEW.](https://klaviyo.zendesk.com/hc/article_attachments/28711675004059)

## Set up coupon / discount code reminders

A great use of Klaviyo's automated flows is to automatically follow up with people who haven't used a coupon code to remind them about it.

Add an additional email or SMS to the same flow that was triggered to give out the initial coupon, but set this additional message to go out a few days later.

For unique (also called "dynamic") coupons, instead use either a split or an additional filter so that the follow-up message only goes to those who have placed an order 0 times since starting this flow.

For static or uploaded coupons, include an [additional filter for this new message](https://help.klaviyo.com/hc/en-us/articles/115002779091) that checks whether or not that person has placed an order that used that discount code. Only allow this follow-up email to send if someone hasn't placed an order since starting this flow.

![Setting a additional filter so only those who haven't used the coupon receive a reminder email](https://klaviyo.zendesk.com/hc/article_attachments/28711662865179)

One person can only receive 1 unique coupon code per coupon. If you resend an email or SMS message to 1 of your customers using the same coupon, they will receive the same unique coupon code as long as the code has not expired.

## See who used discount codes in Shopify and Magento

For Shopify and Magento stores, Klaviyo has the ability to pull in specific coupon codes being used for each purchase. This only works for static coupons or a singular unique coupon code; you cannot segment, split, or filter by a set of unique coupon codes (meaning a unique coupon's name or prefix).

You can create a dynamic segment of everyone who used a particular coupon code.

1. Create a new segment and name it "Used a coupon."
2. Select ****What someone has done (or not done)**** from the dropdown.
3. Select the ****Placed Order**** event and then click the ****Add Filter**** option to specify the discount codes to select.

This is a great way to understand if coupons are getting forwarded on to others, shared among friends, etc.

If you are using a custom platform or a platform like Volusion, BigCommerce, Symphony, or others, you may also be able to pull coupon information. Use the ****Add Filter**** option to see if a "Coupon" or "Discount Codes" option appears.