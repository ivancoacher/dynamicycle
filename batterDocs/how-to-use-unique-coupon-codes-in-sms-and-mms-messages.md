<h1>How to use unique coupon codes in SMS and MMS messages</h1>

## You will learn

Learn how to use unique coupons in your SMS/MMS messages so that you can send one-time-use coupons to your SMS subscribers and encourage them to make a purchase.

You cannot use unique coupon codes (also called dynamic coupons) for the autoresponder message under****Settings > SMS****.

## Before you begin

There are several best practices for using unique coupon codes for SMS and MMS messages:

- Add more codes than strictly needed; having 50 extra coupon codes is recommended.
- Upload or generate coupon codes in advance; this process takes time, especially for a large number of codes, so it is best to do it 1 or 2 days before you start sending.
- If you upload your coupon codes and use them in a flow, check that you have a buffer of 50 codes on a routine basis.
- Use separate coupon codes for each campaign and flow. Having a different coupon code for each of your sends makes it easier to generate/upload the right number of codes as well as track where people saw the coupons.
- Allow for at least 5 extra characters in your SMS or MMS when you include a unique coupon.

****Why should I leave space for more characters when using a unique coupon?****

Anytime there is dynamic content involved (such as with a unique coupon), Klaviyo can only provide an estimate, not an exact character length, for the SMS.

The default length for a code is 8 characters; however, the actual length varies. Say that you include a unique coupon in a campaign that is exactly 160 characters. If the coupon code's actual character count is 10, your campaign will send as 2 SMS (not 1), costing you more credits than you likely planned for.

## Add coupon codes to Klaviyo

The process for creating a unique coupon code for SMS is the same as for email. Klaviyo can generate these codes for [Shopify](https://help.klaviyo.com/hc/en-us/articles/115006155388), [Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005246547), and [Magento 2](https://help.klaviyo.com/hc/en-us/articles/360041971851).

![In the coupons tab click create coupon in the top right corner to create a new coupon.](https://fast.wistia.com/embed/medias/xfixhpcuc5/swatch)

For all other ecommerce integrations, including [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360022884472) and [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/360031279471), you can generate the coupons outside of Klaviyo and then [upload the coupon codes](https://help.klaviyo.com/hc/en-us/articles/115005084727#upload-unique-coupon-codes2) to your account.

![The coupons tab with an arrow pointing to the uploaded coupons tab in the menu bar](https://klaviyo.zendesk.com/hc/article_attachments/28713331515163)

## Send an SMS campaign with a coupon

Once you have coupons generated or uploaded to Klaviyo, you can start including coupons in SMS or MMS campaigns sent to your subscribers. Only 1 coupon code can be added to a single SMS message.

1. Navigate to ****Campaigns****
2. Click ****Create Campaign****.
3. Select ****SMS****, name the campaign, and then choose your recipients.
4. Build out your message in the Content screen. To add the coupon code, include the following template tag. Remember to change "CouponName" to the name of your coupon:

`{% coupon_code 'CouponName' %}`

The coupon will appear differently when sent to a subscriber than in the preview window. Displaying an actual coupon within preview would use one of your coupon codes. To avoid this, you’ll instead see the name of the coupon code followed by “-PREVIEW.”

The example below shows how the preview will appear for a coupon named “SummerSale”.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627679377691)

After configuring the content, click ****Next****.

Klaviyo will check that the coupon has enough codes for the recipients, and you won’t be able to send until you have enough for all of your recipients. It is a best practice to add more coupon codes than you need in case you’re scheduling the campaign to send later and more people join the list or segment you’re sending to.

![An error message from Klaviyo telling you that the coupon does not have enough codes for the recipients.](https://klaviyo.zendesk.com/hc/article_attachments/28713331519515)

Once you’ve confirmed you have enough coupon codes, schedule the SMS campaign or send it immediately.

## Use coupon codes in SMS flows

Flow messages that use the same coupon will send the same coupon code to a recipient. For instance, if an SMS and an email include the same 20% off coupon, the coupon code will be the same.

To add a coupon code to an SMS message in a flow:

1. Navigate to the specific flow and message where you want the coupon.
2. Next, add the following snippet to the message, replacing CouponName with the name of your coupon:

`{% coupon_code 'CouponName' %}`

![](https://klaviyo.zendesk.com/hc/article_attachments/33627693014427)

It’s extremely important that you have enough coupons available for flows. Unlike campaigns, there isn’t a review stage where you can check that you have enough. Flows will automatically send as people qualify for them, so you want to verify that there are plenty of coupons available.

For Shopify, Magento 1, and Magento 2, Klaviyo will automatically generate 100 codes if the number of coupon codes ever drops below 100. However, for other integrations, you have to manually upload new codes; thus, we recommend routinely checking on the number of coupons available.

## Error messages

There are 3 types of errors you can receive when using coupons in SMS messages. These errors will display for both campaigns and flows on the left-hand side of your screen.

The first error is that Klaviyo cannot find the coupon code matching the coupon name. For instance, if the name is missing a number, spelled incorrectly, etc. In this case, check that the name you inputted is the same as the one in **Coupons**.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627693020315)

The second type of error is that the template tag is formatted incorrectly. For example, if it has extra spaces or missing brackets. Make sure that the tag is formatted as:

`{% coupon_code 'CouponName' %}`

![](https://klaviyo.zendesk.com/hc/article_attachments/33627679398171)

You will also receive an error if you have multiple coupons in a single text. Only 1 coupon is allowed per SMS, so check that you haven’t used 2 different ones by accident.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627693036571)

## Additional resources

- [Getting started with coupon codes in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005084727)
- [How to create and send an SMS or MMS campaign](https://help.klaviyo.com/hc/en-us/articles/360040039971)
- [SMS marketing strategies for all levels [+12 Pro tips]](https://www.klaviyo.com/blog/sms-marketing-strategies)
