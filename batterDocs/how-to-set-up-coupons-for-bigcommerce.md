<h1>How to set up coupons for BigCommerce</h1>

## You will learn

Learn how to set up BigCommerce coupon codes to use in Klaviyo emails and SMS so you can incentivize new subscriber and past customers to make a purchase. This guide will walk you through 2 methods for adding coupon codes to your emails:

1. Create a static code in BigCommerce to add in your Klaviyo messaging.
2. Use a third-party app to create unique coupon codes in bulk, and upload them into Klaviyo to use in your messaging.

## Before you begin

- ****Static coupons****
  Static coupon codes means that there's a single code for all customers to use (e.g., Welcome20). Every person will receive the same code and be able to use it on your website. Static codes are easier to remember and use; however, they can be shared out, which can dampen exclusivity.
- ****Unique coupons****
  Unique, also sometimes called "dynamic," coupon codes are a random series of numbers and letters that can be used one single time by one recipient. Each recipient will receive their own coupon code, and no two recipients will have the same code. Unique coupons are typically longer and more complicated than static codes.

The second method utilizes a third-party app to help you create coupons in bulk. You can then upload those bulk codes into both your Klaviyo account and your BigCommerce store, and send unique codes to each of your subscribers.

## Create and use a static coupon code

To create a static code in your Bigcommerce account:

1. Navigate to your BigCommerce admin.
2. Click on ****Marketing > Coupon Codes****.
3. Click ****Create a Coupon Code****.
4. Enter your coupon code details. In the example below, take note of:
   - ****Number of Uses****
     We set this to "1 per customer" to ensure that each customer only uses this coupon code once.
   - ****Expiry Date****
     We set the expiry date to the end of the month (in this case February), because we want to ensure our code isn't used beyond that date.
     ![The coupon details page to fill out and select the behavior after creating a new coupon in BigCommerce](https://klaviyo.zendesk.com/hc/article_attachments/28715969415963)
5. Next, copy the ****Coupon Code**** from BigCommerce.
   ![The coupon details page in BigCommerce with the coupon name copied to your clipboard.](https://klaviyo.zendesk.com/hc/article_attachments/28715962818971)
6. To share this coupon bode, simply paste it wherever you would like it to appear in your Klaviyo email template.
7. Recommended: Try displaying your coupon through a button by pasting the code in the button text box.
   ![the template editor with the static coupon name typed in to the button text box](https://klaviyo.zendesk.com/hc/article_attachments/28715969410715)

Make sure to use a large font and a color that stands out. Also, be sure to include a text block above or below the coupon to help inform your customers about what the code is, and how to use it.

There are a few things to keep in mind when using static coupons:

- If you're worried about your coupon spreading to too many customers, you can remedy this by controlling the expiry date, and changing them every few weeks. Just be sure to make this information to your customers so they understand how long their coupons are valid.
- Klaviyo doesn't manage any of the metadata about your coupons, including the code, expiration date, discount amount, etc. All of this information is managed inside of your BigCommerce store.
- If you're offering a coupon to a specific product, include a link to the product so your customers can easily click through your email to make a purchase.

## Create and upload unique coupons using a bulk upload

Using unique coupons is a great way to offer a personalized discount code to all of your individual customers. You can use a third-party app to help you create unique codes in bulk and then upload those bulk coupons into BigCommerce and then Klaviyo, so you can send unique codes to each of your subscribers.

Please keep in mind that this method requires a third party app to upload your bulk coupon codes into BigCommerce. There is no built-in method to create bulk coupon codes within BigCommerce, but you can [ask for help in this thread](https://support.bigcommerce.com/s/question/0D51B000059EPRjSAO/recommendations-for-a-bulk-coupon-code-generator).

First, you'll need to create some unique coupon codes. There are a number of ways you can do this. For this example, we are going to use the website [mockaroo.com](https://mockaroo.com/) to create 1000 coupon codes.

1. Navigate to mockaroo.com and delete the default fields.
2. Add a new field and set the type to ****Character Sequence****, then enter in a series of asterisks. In the image below our coupon code is 10 characters long, so there are 10 asterisks.
   ![A page on mockaroo.com with a new field added and the type set to character sequence, with ten astrix in the options field.](https://klaviyo.zendesk.com/hc/article_attachments/28715962822171)
3. Click ****Download Data**** and your codes will be saved to your computer in a CSV file. We will use this file to upload our coupons to both our Klaviyo account and our BigCommerce store.
4. To upload the coupons to your BigCommerce store you'll need to use a third-party app, such as [Coupon Buster](https://springmerchant.com/bigcommerce/coupon-importer-buster/).
5. Once you've installed an app that uploads coupons, import the CSV file containing your coupon codes into BigCommerce. You can monitor the progress of your upload on the ****Imports**** tab.

Now that your coupon codes have been added to your BigCommerce store, it's time to add them to your Klaviyo account.

1. Navigate to your coupons tab and click ****Add Coupon.****
2. Set the name and other metadata for your coupon within Klaviyo. If you choose to set an expiration date, make sure it matches the date of the coupons you set up in your BigCommerce store. Once your coupon is set up, click ****Create Coupon****.
   ![The create coupon page in Klaviyo where you can name your coupon and add an expiration setting.](https://klaviyo.zendesk.com/hc/article_attachments/28715969433499)
3. After you create a coupon, you have to add codes to it. On the coupons tab, click the 3-dot dropdown for your coupon, and select ****Add Codes****. This is where we will use the CSV file we just uploaded to our BigCommerce store.
   ![In the coupons list view, the 3-dot dropdown selected for one of your coupons and Add Codes selected.](https://klaviyo.zendesk.com/hc/article_attachments/28715969411995)
4. Select the CSV file containing your codes, and click ****Start Import****.

Your coupon codes will begin to import. You can check the status of your codes in the coupon tab. There are a few important things to note before sending uploaded coupons.

When sending uploaded coupon codes in emails, if your send list is larger than your available coupon codes, then the messages scheduled will be skipped.

- If the code is used in a campaign message, Klaviyo will compare the number of expected recipients to the number of available codes for the coupon used. A warning is displayed if there aren't enough codes available, and you are unable to send the campaign.
- If the code is used in a flow message, Klaviyo will compare the number of expected recipients to the number of available codes for the coupon used. Flow emails that contain coupon codes with 0 available cannot be turned live. At send time, if a flow email contains a coupon with no available codes, the email will be skipped. You can see who was skipped by clicking into the analytics of the flow email and clicking ****Recipient Activity > Other****.

Keep in mind that once you have used all of your codes in Klaviyo, you will have to upload new codes to both your BigCommerce store as well as your Klaviyo account.

## Use your unique coupon in a flow

Once you’ve created and configured your coupon, insert it into a flow message.

1. Navigate to the ****Flows**** tab in Klaviyo’s left-hand navigation.
2. Open an existing flow or [create a new one](https://help.klaviyo.com/hc/en-us/articles/115002774932).
3. Select a flow message inside your flow.
4. Open the message editor for the selected flow message.
5. Click the personalization icon. Depending on your editor, you may see a person icon, or a button labeled ****Personalization****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892582754203)
6. From the **All types** menu, select ****Coupons****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892582755995)
7. Select the coupon you'd like to add.
8. Optional: Select the ****3 dots**** on your flow email, then click ****Preview****. Note that when you preview your email directly in Klaviyo, you will not see a unique code populate. Rather, you will see your coupon’s name hyphenated to “PREVIEW.” Klaviyo will only create and share a unique code at the actual send time.
   ![An example email with a coupon tag shown in preview mode.](https://klaviyo.zendesk.com/hc/article_attachments/39892582757915)

When messages are sent out, a unique discount code, consisting of your prefix and 10 random digits, will dynamically replace the variable for each individual recipient. If you include the same coupon tag in multiple flow messages, the recipient will receive the same unique code each time.

![Unqiue 10 digit code added to the end of coupon prefix](https://klaviyo.zendesk.com/hc/article_attachments/39892582759707)

## Additional resources:

- [Getting started with coupons in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005084727)
- [How to export coupon information](https://help.klaviyo.com/hc/en-us/articles/360048071212-How-to-export-coupon-information)
