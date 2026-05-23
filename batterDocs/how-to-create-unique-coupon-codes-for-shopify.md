<h1>How to create unique coupon codes for Shopify</h1>

## You will learn

Learn how to create single-use coupon codes for your Shopify store so that each customer receives their own unique coupon code for a given promotion on your site. This feature provides an alternative to creating a generic, also known as a static, coupon code, so you don't have to worry about codes being shared.

Shopify enforces a limit of 20 million unique discount codes for each Shopify store. If you reach this limit, you will need to delete unique codes from your Shopify admin before Klaviyo can resume generating new unique codes.

## Before you begin

If you have not already, read our guide on [How to Integrate with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating before continuing with this article.

Make sure that you’ve [integrated with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407) and can view the ****Coupons**** tab in your Klaviyo dashboard.

If you are having trouble accessing it:

1. Navigate to the ****Integrations**** tab in Klaviyo
2. Search for Shopify, and click on the integration to bring you to your **Integration Settings** page.
3. Click ****Update Settings**** to update your integration settings (you may need to re-authenticate with Shopify to then be brought back to Klaviyo)
4. Navigate back to your ****Coupons**** tab.

## When to use unique coupon codes

Unique coupon codes can be used in email campaigns, flow emails, and SMS messages. Examples of unique coupon codes in campaigns include:

- ****Discount codes for email subscribers****
  Reward your subscribers by sending them an exclusive, email-only promotion using coupon codes.
- ****Pre-sale discounts for VIP customers****
  Send your VIPs unique codes that they can use to purchase from a brand-new collection.
- ****Shipping delay discounts****
  If certain items are back-ordered or you're experiencing fulfillment delays, send impacted customers a unique code to thank them for their patience.

  Examples of unique coupon codes in flows include:
- ****Abandoned cart****
  Send a discount code to cart abandoners who haven't bought before that is only active for 2 to 4 days. This will create a sense of urgency and help convert casual browsers into paying customers.
- ****Winback****
  Send a discount to buyers who haven't purchased recently, incentivizing them to purchase again. Like with abandoned cart coupons, a code with a set expiry will create a sense of urgency and can prompt a purchase.
- ****Welcome series****
  Send new subscribers a discount code as soon as they join your email list — you can send another code with increased savings if they haven't bought after 2 weeks.

Klaviyo coupon codes only work for nonrecurring orders, and not subscription orders such as those enabled by Recharge.

## Create your coupon code in Klaviyo

1. Navigate to ****Content > Coupons**** in Klaviyo.
2. Click ****Create Shopify Coupon**** in the upper right-hand corner.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/38522852480155)
3. For each coupon, set the following properties in Klaviyo:

   - ****Name****
     Setting a name will help you identify the coupon in Klaviyo. Note that you will need to use this exact name when including the coupon in a message.
   - ****Prefix****
     Klaviyo will generate a random code for each person, but you can also specify a prefix to be included in every code (e.g., WELCOME).
   - ****Discount type****
     Choose whether the coupon is a fixed amount off, a percentage off, or free shipping.
   - ****Free shipping****
     For free shipping coupons, you can limit the coupon so it only applies to certain shipping rates, or only to specific countries.
   - ****Fixed amount and percentage****
     For coupons that offer a fixed amount or percentage off, you can specify that the coupon only applies to certain products or collections.
   - ****Applies to****
     Pick whether customers can apply the coupon to the entire order, specific products, or specific collections.
   - ****Require minimum purchase****
     Choose if the coupon can only be used if the customer’s cart reaches a specific amount. Note that if the code is only for a specific product, the minimum purchase amount only applies to that specific product.

     ![The Coupon Details menu where you can name a coupon, set a prefix, and define the coupon's functionality including type and application specifics.](https://klaviyo.zendesk.com/hc/article_attachments/28722594901147)
   - ****Coupon combinations****Choose the types of discounts this coupon can be combined with in a single order.
     ![](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/98d45b39a9a810e1a9535235de52f115c132922b-1662x446.png)
   - ****Activation date****
     This is the date the coupon becomes active — you can choose a specific date or select an option where generated coupon codes activate at send time. Please note that dates are set in the UTC time zone, so you may see a different activation date in Shopify.
   - ****Expiration****
     Choose when you would like your coupon to expire. There are different options for coupons used in campaign messages versus flow messages. Please note that, in Klaviyo, dates are set in the UTC time zone. However, Shopify sets the expiration date and time based on the Shopify store’s timezone, so you may see different expiration dates in Klaviyo and Shopify for the same coupon.
     - Campaigns
       You have 2 choices for expiration
       - Generated coupon codes will expire after 1 year.
       - If you want your discount to have a defined end date, after which generated codes will expire, you can select a specific expiration date.
     - Flows
       You have 3 choices for expiration:
       - Generated coupon codes will expire after 1 year.
       - Generated coupon codes will expire after a certain number of days/hours.
       - If you want your discount to have a defined end date, after which generated codes will expire, you can select a specific expiration date.![](https://klaviyo.zendesk.com/hc/article_attachments/38308277012251)
4. Click ****Create coupon****.

- Coupons that expire after a certain number of days/hours have variable expiration dates. Although you **can** create coupons with variable expiration dates for flows, you **cannot** create coupons with variable expiration dates for campaigns.

Note that your coupon's actual expiration will always be 24 hours beyond what you set in the expiration date field. This is to ensure that the coupon can still be used by the recipient in case there is a delay in sending or delivery.

For example, if you set a 8/15/2024 at as the expiration date for your coupon, it will actually expire on 8/16/2024. Similarly, a coupon set to expire in 4 hours will still be valid for a 24 hour period after the initial 4 hours.

It's also important to note that if you update coupon settings, such as discount type and percentage, within Shopify, all codes generated with those price settings will have the new price settings. If you update coupon settings in Shopify that are not available in Klaviyo's coupon creation, those changes will not be reflected. See [information on updating coupon codes](#h_01HE8BRNWXSTTEQQP76T3EJB43) for more details.

## Generate codes after creating your coupon

Klaviyo generates coupon codes for flow emails automatically. If you plan to use your coupon in a flow you do not need to generate coupons manually and can skip this section; however, if you plan to use your codes in campaign emails, you must manually generate coupon codes.

Once you've configured your coupon's definition, you'll next need to specify the number of coupon codes that you want to generate for your campaign. This must be done before you schedule your campaign. To generate coupons:

1. Navigate back to the ****Coupons**** tab.
2. Click the 3 dot dropdown next to the coupon you just created and select ****Add Codes****.

   ![The dropdown menu on the far right side showing Add Codes being selected.](https://klaviyo.zendesk.com/hc/article_attachments/28722556461595)

   Coupons with variable expiration dates cannot be used in campaigns. As such, you will not see the option to manually add codes if you have selected a variable expiration date for your coupon.
3. Keep in mind that:

   - You must generate at least as many codes as expected recipients. This means that if you generate fewer codes than the number of estimated recipients, you will not be able to schedule or send the campaign.
   - If your scheduled campaign is set to "Determine recipients at send time," and the actual number of recipients is greater than the number of codes you generate at send time, the extra recipients will be skipped and will not receive the email.
   - If you generate a large number of codes, allow time between your campaign's desired send time and when you create the codes. Generating a large number of coupon codes may take up to several hours. Because of this, use the estimated number of recipients of the campaign as a framework and do not significantly overestimate the number of codes you need.
4. Input the number of codes you would like to generate in the box and click ****Add Codes****. Again, be sure to generate at least as many codes as you have expected recipients for your campaign, otherwise, you will not be able to send or schedule it.

   ![Add Codes modal where you can specify how many more codes to add to a coupon](https://klaviyo.zendesk.com/hc/article_attachments/28722594876827)
5. Klaviyo will begin generating coupon codes for your campaign. Monitor the progress bar that appears beneath the coupon name to display progress, or track the number of codes that have been created in the **Available/Total** column.

You are able to include multiple codes per email (but only 1 code per SMS). If you use multiple coupons in a message, make sure you have enough codes for every recipient to receive one of each code. With email, you have the option to use [hidden blocks](https://help.klaviyo.com/hc/en-us/articles/115005258208) to send different coupons based on where someone lives or what they’ve done. We recommend exercising caution with the hidden blocks feature because codes may be assigned to all recipients (even if they end up hidden in your message) and block your send if there aren’t enough codes.

Now that you've generated your codes, use them in an email campaign or SMS message to incentivize site visitors to make a purchase.

## Using your coupon in a campaign email

After the coupon codes have been generated, you can include the coupon tag in your campaign template.

1. Drag and drop a text block wherever you want the coupon to appear in your campaign.
2. Click the personalization icon. Depending on your editor, you may see a person icon, or a button labeled ****Personalization****.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892630420891)
3. From the **All types** menu, select ****Coupons****.
4. Select the coupon you'd like to add.
5. When emails are sent out, this variable will be dynamically replaced with a unique discount code for each recipient.
6. Note that when you preview your email directly in Klaviyo, you will not see a unique code populate. Rather, you will see your coupon’s name hyphenated to “PREVIEW.” Klaviyo will only create and share a unique code at the actual send time.

### Test your campaign's coupon

Before you send out the campaign and coupon to your audience, we suggest testing first. To test the coupon in your campaign email, make sure that you have added codes from within the **Coupons** tab. As long as you have sufficient codes, you can send a preview email to yourself or a member of the team and a live code will be generated. Note that the code will not actually be used.

- If you preview the email directly in Klaviyo, you will not see a unique coupon code populate. It will appear as COUPON\_NAME-preview.
- If multiple people are included in the preview send, they will all receive the same code.

Once you're ready to send or schedule your campaign, click ****Review & Send Campaign****. Here, you will see a **Coupon Codes** area. If you have fewer coupon codes available than expected recipients, you will not be able to schedule or send your campaign and will need to add more codes.

After your campaign is sent, you can see which code an individual recipient received by navigating to their profile and scrolling to the **Coupons** section.

## Use your unique coupon in a flow

Once you’ve created and configured your coupon, insert it into a flow message.

1. Navigate to the ****Flows**** tab in Klaviyo’s left-hand navigation.
2. Open an existing flow or [create a new one](https://help.klaviyo.com/hc/en-us/articles/115002774932).
3. Select a flow message inside your flow.
4. Open the message editor for the selected flow message.
5. Click the personalization icon. Depending on your editor, you may see a person icon, or a button labeled ****Personalization****.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892630420891)
6. From the **All types** menu, select ****Coupons****.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892630426139)
7. Select the coupon you'd like to add.
8. Optional: Select the ****3 dots**** on your flow email, then click ****Preview****. Note that when you preview your email directly in Klaviyo, you will not see a unique code populate. Rather, you will see your coupon’s name hyphenated to “PREVIEW.” Klaviyo will only create and share a unique code at the actual send time.

![An example email with a coupon tag shown in preview mode.](https://klaviyo.zendesk.com/hc/article_attachments/39892630428443)

When messages are sent out, a unique discount code, consisting of your prefix and 10 random digits, will dynamically replace the variable for each individual recipient. If you include the same coupon tag in multiple flow messages, the recipient will receive the same unique code each time.

![Unqiue 10 digit code added to the end of coupon prefix](https://klaviyo.zendesk.com/hc/article_attachments/39892630430235)

Unique coupon codes for live flow emails generate automatically. These automatically replenish daily; however, if you use all codes before the replenishment, the next attempt to assign a coupon will be skipped due to insufficient codes available. This automatically triggers Klaviyo to generate additional codes. Because coupon codes for flows are replenished automatically, you do not need to manually add batches of coupon codes via the **Add codes** option.

### Test your flow email's coupon

Before you send out the flow and coupon to your audience, we suggest testing it first.

#### Test a coupon with a variable expiration date (e.g., 7 days)

1. In the flow builder, click ****Review and turn on****.
2. Change the status to ****Manual****.
3. Click ****Turn on****.
4. Trigger your flow by performing the trigger action (e.g., filling out a sign-up form to join a certain list). Your flow will automatically generate 100 coupons once it reaches the email step including the code in the flow.

   Note that the initial coupon may take about 3 minutes to generate. Because of this, there is a short loading buffer, and you may see your test profile under **Skipped: Retrying Generating Coupon Codes**. This will go away once the coupons have finished generating.
5. When the coupons are generated, your test email that triggered the flow will be under **Needs Review** for the email.

   ![An example flow open in the flow builder showing the flow email selected and one pending alert in the Needs Review tab.](https://klaviyo.zendesk.com/hc/article_attachments/28722556515355)
6. Click into the ****Needs Review**** bucket under **Recipient activity**.
7. Select ****Send Now****.

   ![The Needs Review tab open under showing the option to Send Now being selected.](https://klaviyo.zendesk.com/hc/article_attachments/28722556517659)
8. Check your inbox for the email with the unique code.

## Using your coupon in a signup form

You can also use unique coupon codes for Shopify in your signup forms. Make sure to have a signup form with a coupon block created. You can create your coupon in advance, or directly when building your form.

Learn [how to create a signup form with a coupon block](https://help.klaviyo.com/hc/en-us/articles/6038674938523).

On your form's coupon block, take the following steps to add a unique coupon for Shopify:

1. Choose ****Shopify Coupon**** as your **Unique Coupon Type.**
2. Click the dropdown next to ****Unique Coupon**** to either choose an existing coupon, or click the ****plus sign (+)**** to create a new Shopify coupon.

   ![The Coupon menu opened in the sign-up form editor showing a unique coupon type selected.](https://klaviyo.zendesk.com/hc/article_attachments/30321443741851)
3. If you chose to create a new, unique Shopify coupon code, a ****Create unique Shopify**** coupon modal will appear asking you to:

   - Name your coupon (e.g. 10OFF), and add an optional Prefix.
   - Select the type of discount that you would like to offer your customers (fixed amount, percentage, or free shipping).
   - Choose the settings for how your coupon will operate (amount, application, activation, and expiration).![](https://klaviyo.zendesk.com/hc/article_attachments/38308277013403)

   Note that if you select ****After 1 year**** or ****On a specific date**** for **Expiration**, Klaviyo will generate an initial batch of 600 unique codes when the coupon is added to the form, and will generate more codes once the number available drops below 400. If you select **After a certain number of days/hours**, Klaviyo will generate a batch of 600 codes each day.
4. Click ****Create coupon**** in the top right corner. This will take you back to the form builder with the newly created coupon code selected to use in the form.
5. Add an existing static coupon as a **Fallback Coupon**. This is a static code that will only appear if you run out of unique coupon codes, so that your customers will still receive some coupon.

   You will need to create a static coupon in Shopify first to paste into the **Fallback Coupon** textbox (e.g. 10PERCENT).
6. Skip to the final section to [finish editing and publish your form](https://help.klaviyo.com/hc/en-us/articles/6038674938523#h_01HA28D5B1V3AKQ76C5N6TJBGJ).

## Unique coupons for SMS

Unique coupons are also available for [SMS/MMS messages](https://help.klaviyo.com/hc/en-us/articles/360044863132).

1. Generate the codes just like you would for email.
2. Use the template tag below to add the coupon code to your SMS or MMS message:
   `{% coupon_code 'CouponName' %}.`
3. In the snippet, change **CouponName** to the name of the coupon you’re using and add it to the message (for either a flow or campaign).

![Example of an SMS message with a 20 percent off coupon](https://klaviyo.zendesk.com/hc/article_attachments/28722556499099)

Unlike with emails, you can only use 1 coupon code per SMS message. If you try to add multiple coupons to an SMS, you will see an error message.

## Information on updating coupon codes

If you change the definition of your coupon, the impact on already sent codes will depend on where you made the changes to the coupon definition:

- If you change the coupon definition in Klaviyo, then it will create a new price rule and the coupons already sent to customers will not be impacted. This means that all previous coupon configurations will still apply for the already sent codes.
  - For example, if a coupon code was previously set to require a minimum purchase amount of $20, Price Rule A is created in Shopify for this definition. If that coupon definition is later changed in Klaviyo to require a minimum purchase amount of $40, a brand new price rule will be created in Shopify (Price Rule B). This means that any coupons that were already sent in a flow before the change will still reflect Price Rule A ($20 minimum purchase), and thus will not be impacted by the definition change.
- If you change the coupon definition in Shopify, then coupon codes that have already been sent will be impacted.
  - For example, if a coupon code was previously set to require a minimum purchase amount of $20, Price Rule A is created in Shopify for this definition. If you later make a change to Price Rule A in Shopify, so a $40 minimum purchase is now required, coupon codes that were already sent in a flow before the change will be impacted. The changes to the coupon's definition will not be reflected in Klaviyo, however, the previously sent coupon codes will be updated to the new definition ($40 minimum purchase).

If the coupon is used in a flow, 100 codes will auto-generate when you save. This allows flows to immediately send the latest version of any coupon.

Head to our article on [viewing a coupon’s history](https://help.klaviyo.com/hc/en-us/articles/360048069712-How-to-view-coupon-history) to learn more.

## Best practices

If you use unique coupons in campaigns and flow messages, there are a few best practices we recommend:

- Don't use the same coupon for flows and campaigns. Because you need to specify the number of codes to be generated for campaigns, but not flows, it's best to use different coupons for each.
- Create a separate coupon for each campaign. This way, it will be easier to specify the number of codes you will need for each campaign, and you won't risk running out of codes, which would result in some recipients being skipped.
- Create a separate coupon when changing the categories or products applicable for the coupon. Klaviyo will try to assign all pre-existing codes by default, so customers may receive and use codes with outdated rules.
