<h1>How to add coupon codes to sign-up forms</h1>

## You will learn

Learn how to add static and unique coupon codes to your sign-up forms to drive higher submission and conversion rates, and encourage customers to spend more on your site.

It’s a best practice to add the coupon code directly to the success message of your form, as it incentivizes sign-ups and allows your shoppers to claim the coupon without leaving your site. If you’re using Shopify and unique Shopify coupons on your sign-up forms, the coupon will be automatically applied to a customer’s cart at checkout when they complete the form.

## Before you begin

There are a few types of coupons:

- ****Unique codes****
  Unique, also called "dynamic," coupon codes are a random series of numbers or letters that a recipient can use 1 time. Each recipient will receive their own coupon code, and no 2 recipients will have the same code. Unique coupon codes are typically longer and more complicated than static codes.
- ****Static coupon****
  Static coupon codes are a single code for all customers to use (e.g., Welcome20). Every person will receive the same code to use on your site. Static codes can be shared out; however, they are easier to remember and use.

The process of configuring the coupon will differ depending on the type of coupon you use (i.e., static coupon, unique Shopify coupon, or uploaded unique coupon); however the first 2 sections of this guide should be followed regardless of coupon type.

Banner forms that do not collect email or SMS consent can only include static coupons. Banners that do collect email or SMS consent must include a unique coupon block on the success step.

## Prepare your sign-up form

1. Select the ****Sign-up forms**** tab in Klaviyo's left-hand navigation.
2. From here, you have a few options for creating a form with a coupon in it.

   - Option 1: choose 1 of your existing forms to edit and add a coupon to.
   - Option 2: choose a pre-built template from the form library that has a coupon block already included. To do so, select ****Create sign-up form**** in the top right corner, then check the box for in the menu bar to filter your search in the form library.
     ![The form library with the box for Coupons & Offers checked off at the top of the page to narrow the search](https://klaviyo.zendesk.com/hc/article_attachments/28723522657819)
   - Option 3: Create a brand new form from scratch and configure it with a coupon. To do so, select ****Create sign-up form**** in the top right corner, then ****Create new sign-up form****.
3. Enter the form editor for the sign-up form you plan to add the coupon to.

With any of the options above, you can easily add a coupon block to your sign-up form in the form builder.

## Add a coupon block to the success step of your form

Once you're in the editor for your sign-up form, you can add and configure your coupon. Follow these set up instructions for both static and unique coupons:

1. In the form editor, select the submit button in the preview.
   ![The button menu showing in the form editor for an example form with the Action set to Submit Form and the After Submit set to Show Next Step](https://klaviyo.zendesk.com/hc/article_attachments/28723522654491)
2. Configure the **Button Click Action** settings to the following:

   - **Action**: ****Submit form****.
   - **List to Submit**: Choose your list.
   - **After Submit**: ****Show Next Step****.
3. At the top of the page, select ****Success**** to open your form’s success step. This is the page that visitors will see when they submit the form.
   ![The Success step selected in the menu bar of the form editor for an example form](https://klaviyo.zendesk.com/hc/article_attachments/28723522660763)
4. On the left side of the **Overview** page, select the ****Add Blocks**** tab.
5. Drag and drop a ****Coupon**** block (located under **Elements**) into the preview wherever you'd like it the coupon to appear in your form, if there is not one there already.
6. Click ****Configure Coupon**** in the form preview.

![](https://fast.wistia.com/embed/medias/psyi573645/swatch)

1. In the settings menu that appears on the left side, choose to set up either a static or unique coupon in your form.

## Set up a static coupon in your form

1. At the top of the coupon settings menu, select ****Static Coupon****.
2. Type the name of your static coupon code in the textbox (e.g. Welcome10).

   - If you do not have an existing static code ready, you will first need to [manually create one in your ecommerce platform](https://help.klaviyo.com/hc/en-us/sections/14545347290651).
3. If you just created a new static code, reload the form builder page before typing it into the textbox.
   ![The Coupon menu in the sign-up form builder showing a static coupon selected and its name typed into the textbox](https://klaviyo.zendesk.com/hc/article_attachments/28723522627227)
4. Edit the block styles (e.g., background color, corner radius, border style, border thickness, and padding) so that the coupon is large and eye-catching.
5. When you’re finished editing, click the back arrow to save the coupon.
   ![Back arrow within the Coupon block editor](https://klaviyo.zendesk.com/hc/article_attachments/38308316851867)
6. Skip to the final section to [finish editing and publish your form](https://help.klaviyo.com/hc/en-us/articles/6038674938523#h_01HA28D5B1V3AKQ76C5N6TJBGJ).

## Set up a unique coupon code in your form

At the top of the coupon settings menu, select ****Unique Coupon****. Depending on if you are using a Shopify unique coupon or an uploaded unique coupon, your setup will differ slightly.

The ability to show unique coupon codes in a success message is currently available only for Shopify coupons, uploaded coupons, and API coupons. While it is possible to create unique coupons in Klaviyo for WooCommerce, Magento 2, and PrestaShop, it's not possible to display those codes in sign-up forms at this time. As an alternative, follow the [uploaded coupons](https://help.klaviyo.com/hc/en-us/articles/6038674938523#h_01HA28D5B051GZENA8E4DCJJCR) or [API coupons](https://developers.klaviyo.com/en/docs/use_klaviyos_coupons_api) instructions to add unique coupon codes in forms.

### Shopify coupons

1. Choose ****Shopify Coupon**** as your **Unique Coupon Type.**
2. Click the dropdown next to ****Unique Coupon**** to either choose an existing coupon, or click the ****(+) Unique Shopify Coupon**** to create a new one.
   ![The Coupon menu opened in the sign-up form editor showing a unique coupon type selected](https://klaviyo.zendesk.com/hc/article_attachments/34483817889819)
3. If you chose to create a new, unique Shopify coupon code, a ****Create unique Shopify**** coupon modal will appear asking you to:

   - Name your coupon (e.g. 10OFF), and add an optional Prefix.
   - Select the type of discount that you would like to offer your customers (fixed amount, percentage, or free shipping).
   - Choose the settings for how your coupon will operate (amount, application, activation, and expiration).
     - Note that if you select ****After 1 year**** or ****On a specific date**** for **Expiration**, Klaviyo will generate an initial batch of 600 unique codes when the coupon is added to the form, and will generate more codes once the number available drops below 400. If you select After a certain number of days/hours, Klaviyo will generate a batch of 600 codes each day.![](https://klaviyo.zendesk.com/hc/article_attachments/38308326776091)
4. Click ****Create unique Shopify coupon**** in the bottom right corner. This takes you back to the form builder with the newly created coupon code selected to use in the form.
5. Add an existing static coupon as a **Fallback Coupon**. This is a static code that only appears if you run out of unique coupon codes so that your customers can still receive the same discount. You will need to create a static coupon in Shopify first to paste into the **Fallback Coupon** textbox (e.g. 10PERCENT).
6. Skip to the final section to [finish editing and publish your form](https://help.klaviyo.com/hc/en-us/articles/6038674938523#h_01HA28D5B1V3AKQ76C5N6TJBGJ).

### Uploaded coupons

If you have not already, make sure that you have enabled uploaded coupons. Navigate to ****Settings > Other > Profile maintenance****, then toggle on the **Uploaded Coupons** option.

![How the Uploaded Coupons toggle appears when this option is turned on](https://klaviyo.zendesk.com/hc/article_attachments/34483801682971)

1. In your form, choose ****Uploaded Coupon**** as your **Unique Coupon Type**.
2. Click the dropdown next to **Unique Coupon** to either choose an existing coupon, or click the ****Create uploaded coupon**** link.
   ![The Create uploaded coupon link selected from the unique coupon set up menu](https://klaviyo.zendesk.com/hc/article_attachments/28723544584091)
3. If you chose an existing coupon, make sure you've uploaded codes to this coupon.
4. If you chose to create a new uploaded coupon, the **Create Coupon** page will open in a new tab. From here:

   - Configure the following details:
     - Name (e.g. JustForYou)
     - Minimum coupon count (e.g. 500)

       The coupon count must be a value between 100 - 5000. Values outside of that range are not accepted. If no minimum is specified, the default count will be 500.
     - Expiration date
       ![](https://klaviyo.zendesk.com/hc/article_attachments/39700139947931)
   - Click ****Create coupon**** in the upper right corner. This will bring you to the **Uploaded Coupons** page.
     - On the **Uploaded Coupons** page, click the ****3 dots**** ****> Add codes**** to the right of the coupon that ‌you would like to use for your form.
       ![](https://klaviyo.zendesk.com/hc/article_attachments/38522139367451)
   - Upload your CSV file to process these codes. You can reference [our guide for uploading unique coupons](https://help.klaviyo.com/hc/en-us/articles/115005084727#h_01HMW7FB2WV5RT1T0EZ3N7TMJ9) for assistance.
   - Navigate back to the sign-up form builder tab and reload the page.
5. Select the ******Success****** step, then click ****Configure coupon**** in the preview.
6. Next to **Unique Coupon**, choose your new uploaded coupon from the dropdown.
   ![The Unique Coupon dropdown in the sign-up form editor with the coupon you just uploaded selected as the coupon option](https://klaviyo.zendesk.com/hc/article_attachments/28723522650523)
7. Add an existing static coupon as a **Fallback Coupon**. This is a static code that only appears if you run out of unique coupon codes so that your customers can still receive some coupon.

- You need to first upload a static coupon into Klaviyo to paste into the **Fallback Coupon** textbox (e.g. 10PERCENT).

![The fallback coupon message that appears after you configure a coupon for your sign-up form](https://klaviyo.zendesk.com/hc/article_attachments/28723544592795)

## Finish editing and publish your form

Once you have coupons set up for your form:

1. Make any final styling changes to the look and text of your coupon, or the other steps on your form.
2. When you're ready to set your form live, click ****Publish****.
3. Go to your site and reload the page to see your form appear.

   It may take a moment for the form to appear on your site while the unique coupon code generates.
4. Fill out the form to test that your coupon has processed correctly. Once it has, customers will receive a coupon code directly in the success message of your form to copy and use on your site.

If you use a Shopify coupon in your sign-up form, it will automatically apply to a customer's Shopify checkout page upon them reaching the form's final step.
