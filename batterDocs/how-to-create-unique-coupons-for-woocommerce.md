<h1>How to create unique coupons for Woocommerce</h1>

## You will learn

Learn how to create unique, single-use coupons for your WooCommerce store and use them in flows to incentivize subscribers to make a purchase. To do this, you’ll first create your coupon in WooCommerce, then configure settings for the linked coupon in Klaviyo.

Unique coupons codes for WooCommerce can be used in flow emails only, not campaign emails. If you’d like to include a coupon in a campaign, consider [uploading unique codes](https://help.klaviyo.com/hc/en-us/articles/115005084727) or using a [static WooCommerce coupon](https://help.klaviyo.com/hc/en-us/articles/360031279471).

****Use cases for unique coupon codes in flows****

- ****Abandoned********cart****
  Send a discount code that’s only active for a limited amount of time (e.g., 2 to 4 days) to cart abandoners who haven’t purchased before to create a sense of urgency and encourage conversions from casual browsers.
- ****Winback****
  Send a discount code to buyers who haven’t purchased recently to incentivize them to purchase again. Similar to the abandoned cart coupon logic, sending a coupon with a set expiration date can create a sense of urgency and prompt a purchase.
- ****Welcome series****
  Send a discount code to new subscribers as soon as they join your email list. You can send another code with increased incentive if they still haven’t made a purchase after 2 weeks.

## Before you begin

Make sure that you’ve [integrated with WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808) and can view the **Coupons** tab under **Content** in Klaviyo’s left-hand navigation. If you’ve integrated but do not see the **Coupons** tab:

1. Select your company name in the bottom left corner of Klaviyo’s left-hand navigation, then select ****Integrations****.
2. Search for **Woocommerce**, then select the card.
3. Click ****Update settings**** to update your integration settings. You should now see the **Coupons** tab under **Content** in the left-hand navigation.

   You'll need to enable coupons in WooCommerce, if you haven't already:
4. Log in to your WooCommerce account.
5. Head to ****WooCommerce > Settings > General**** and check the box to enable the use of coupons.
   ![The Enable Coupons menu in WooCommerce showing the box checked off to Enable the use of coupon codes.](https://klaviyo.zendesk.com/hc/article_attachments/28723684837147)
6. Save your changes.

## Create your coupon in Woocommerce

1. In your WooCommerce account, navigate to ****Marketing > Coupons****.
2. Click ****Add coupon****. Or, if you have not created one yet, click ****Create your first coupon****.

   ![The Coupons page on the Marketing tab in WooCommerce where you can click the button to create your first coupon.](https://klaviyo.zendesk.com/hc/article_attachments/28723684840859)
3. Next to **Coupon Code**, name your coupon and add a description for your own use.
4. Enter your [coupon data](https://woo.com/document/coupon-management/#adding-a-coupon). This includes:

   - Discount type
   - Coupon amount
   - Allow free shipping
   - Coupon expiry date
5. If you have any **Usage restrictions** or **Usage limits**, enter them in the respective tabs under **Coupon Data**.

   To enforce uniqueness among your coupon codes, we recommend setting a **Usage limit** of 1 per coupon, and 1 per user. This is not required; however, it can help deter sharing across customers.
6. Once you’re finished editing, click ****Publish**** so your coupon is ready to use.

## Configure your coupon in Klaviyo

Now that you’ve created your coupon in WooCommerce, configure it in Klaviyo so you can generate codes for your flows.

1. Navigate to ****Content > Coupons**** in Klaviyo’s left-hand navigation.
2. In the menu bar along the top, select the ****WooCommerce Coupons**** tab.
   ![The WooCommerce Coupons tab in Klaviyo showing 3 pre-existing WooCommerce coupons and the button to Create WooCommerce Coupon.](https://klaviyo.zendesk.com/hc/article_attachments/28723684842907)
3. Select ****Create WooCommerce Coupon****.
4. Select ****Add code****, then enter the coupon code you created in WooCommerce. It should be the same code name you assigned to the linked coupon in WooCommerce.
   ![The Add Coupon Code modal where you enter the name of the coupon code you created in WooCommerce in the Add Code text box.](https://klaviyo.zendesk.com/hc/article_attachments/28723662700059)
5. Click ****Save****.
6. Set the following properties for your coupon:

   - **Prefix**
     Klaviyo will generate a random code for each person, but you can also specify a prefix to be included before every 10 digit code (e.g., JB20).

     Note that WooCommerce stores all coupon codes in lowercase. For example, if you input JB20 as the prefix, a full unique code would show as jb20h3shfr7kgs when it’s created.
   - **Quantity**
     Estimate the minimum number of codes to have on hand; Klaviyo will use this number (which must be between 0 and 150,000) to automatically generate a batch of codes daily or as needed. We recommend setting this number to the amount you'd reasonably expect to use in a day (e.g., 10).
   - **Expiry date**
     Choose when you would like your coupon to expire (either **After a certain number of days** or **On a specific date**). Klaviyo will show the timezone associated with your account by default; however, the time zone is configurable. If you set a different expiry date in WooCommerce, the expiry set in Klaviyo will overwrite it.![The Create WooCommerce Coupon menu where you can set coupon properties such as a prefix, quantity, and expiry date.](https://klaviyo.zendesk.com/hc/article_attachments/28723662706459)
7. Click ****Create coupon****.

If you change the coupon name in WooCommerce, it will affect the linkage to the coupon in Klaviyo. If the names do not match, you will see an error message that Klaviyo is **Unable to find the corresponding coupon code in WooCommerce**. You will not be able to finish configuring the coupon or generate codes until the names match.

Once you have created your coupon in WooCommerce and configured it in Klaviyo, Klaviyo will begin generating codes automatically for your flow emails.

## Use your unique coupon in a flow

Once you’ve created and configured your coupon, insert it into a flow message.

1. Navigate to the ****Flows**** tab in Klaviyo’s left-hand navigation.
2. Open an existing flow or [create a new one](https://help.klaviyo.com/hc/en-us/articles/115002774932).
3. Select a flow message inside your flow.
4. Open the message editor for the selected flow message.
5. Click the personalization icon. Depending on your editor, you may see a person icon, or a button labeled ****Personalization****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892632116891)
6. From the **All types** menu, select ****Coupons****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892625103643)
7. Select the coupon you'd like to add.
8. Optional: Select the ****3 dots**** on your flow email, then click ****Preview****. Note that when you preview your email directly in Klaviyo, you will not see a unique code populate. Rather, you will see your coupon’s name hyphenated to “PREVIEW.” Klaviyo will only create and share a unique code at the actual send time.

![An example email with a coupon tag shown in preview mode.](https://klaviyo.zendesk.com/hc/article_attachments/28723662720539)

When messages are sent out, a unique discount code, consisting of your prefix and 10 random digits, will dynamically replace the variable for each individual recipient. If you include the same coupon tag in multiple flow messages, the recipient will receive the same unique code each time.

![Unqiue 10 digit code added to the end of coupon prefix](https://klaviyo.zendesk.com/hc/article_attachments/28723662725787)

Unique coupon codes for live flow emails generate automatically based on how many you specify in the **Minimum Inventory** section of the **Coupon details** page. For example, if you create a coupon with a **Minimum Inventory** of 100, Klaviyo generates a batch of 100 unique codes. These automatically replenish daily; however, if you use all 100 codes before the replenishment, the 101st attempt to assign a coupon will be skipped due to insufficient codes available. This automatically triggers Klaviyo to generate another 100 codes. Because coupon codes for flows are replenished automatically, you do not need to manually add batches of coupon codes via the **Add codes** option.

## Test your coupon

Before you send out the flow with the coupon to your audience, we recommend testing it first.

1. In the flow builder, click ****Review and turn on****.
2. Change the status to ****Manual****.
3. Click ****Turn on****.
4. Trigger your flow by performing the trigger action corresponding with your flow (e.g., filling out a sign-up form to join a certain list). Your flow will automatically generate 100 coupons upon you completing the trigger action.

   The coupon may take a few minutes to generate codes. Because of this, there’s a short loading buffer, and you may see your test profile under **Skipped: Retrying generating codes**. This will go away once the coupons have finished generating.
5. When the coupons have been generated, your test email that triggered the flow will show under **Needs Review** for the email.
6. Click into the ****Needs Review**** bucket under **Recipient activity**.
   ![The Needs Review tab under Recipient Activity for a flow showing an example test email address.](https://klaviyo.zendesk.com/hc/article_attachments/28723662711195)
7. Select ****Send Now****.
   ![The Needs Review tab under Recipient Activity showing the button to Send Now being selected next to the test email address.](https://klaviyo.zendesk.com/hc/article_attachments/28723684865819)
8. Check your inbox for the email with the unique code.

## Troubleshooting common coupon issues

If you are seeing issues with creating unique coupons for WooCommerce in Klaviyo, go through the following recommended troubleshooting steps. If you are still seeing issues after going through the recommended steps, reach out to [Klaviyo’s support team](https://help.klaviyo.com/hc/en-us/articles/115001002272) for further assistance.

### Check your WooCommerce integration settings

If your integration with WooCommerce is not syncing, or your WooCommerce store is unreachable, Klaviyo will not be able to generate new coupon codes.

To view your WooCommerce integration settings:

1. Select your company name in the bottom left corner of Klaviyo’s left-hand navigation, then select ****Integrations****.
2. Search for **WooCommerce**, then select the card.
3. Click ****Update settings**** to update your integration settings.

For more assistance on configuring your Klaviyo integration with WooCommerce, see [Getting Started with WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808).

### Decrease the quantity set for coupon codes

In you are experiencing an error creating coupon codes, try reducing the minimum inventory number set via the **Quantity** field in your coupon settings in Klaviyo.

### Verify the coupon exists in WooCommerce

If you receive an error indicating that the coupon cannot be found in WooCommerce, Klaviyo is not able to match the specified coupon to one in your WooCommerce account.

To resolve this, update the coupon name in Klaviyo, ensuring that it matches an existing coupon code in your WooCommerce store.

### Check for potential incompatibility with the Jetpack plugin for WooCommerce

If you notice that the number of codes for your coupons are low, or failing to replenish, this may be due to an incompatibility of Klaviyo’s coupon service with the [Jetpack](https://woocommerce.com/products/jetpack/) plugin for WooCommerce. If you have this plugin installed, please disable it.
