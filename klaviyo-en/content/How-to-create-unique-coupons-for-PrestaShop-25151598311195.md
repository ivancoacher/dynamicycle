---
id: "25151598311195"
title: "How to create unique coupons for PrestaShop"
source_url: "https://help.klaviyo.com/hc/en-us/articles/25151598311195-How-to-create-unique-coupons-for-PrestaShop"
section: "Coupons and ecommerce integrations"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:35Z"
language: "en"
---
## You will learn

Learn how to create unique, single-use coupons for your PrestaShop store and use them in flows to incentivize subscribers to make a purchase. To do this, you’ll first create your coupon in PrestaShop, then configure settings for the linked coupon in Klaviyo.

Unique coupon codes for PrestaShop can only be used in flow emails or SMS messages, not campaigns or forms. If you’d like to include a coupon in a campaign, consider uploading unique codes or using a [static PrestaShop coupon](https://help.klaviyo.com/hc/en-us/articles/19655157461403).

****Use cases for unique coupons in flows****

- ****Abandoned cart****
  Send a discount code that’s only active for a limited amount of time (e.g., 2 to 4 days) to cart abandoners who haven’t purchased before to create a sense of urgency and encourage conversions from casual browsers.
- ****Winback****
  Send a discount code to buyers who haven’t purchased recently to incentivize them to purchase again. Similar to the abandoned cart coupon logic, sending a coupon with a set expiration date can create a sense of urgency and prompt a purchase.
- ****Welcome series****
  Send a discount code to new subscribers as soon as they join your email list. You can send another code with an increased incentive if they still haven’t made a purchase after 2 weeks.

## Before you begin

### Klaviyo module version

To utilize unique coupons with PrestaShop, you must use Klaviyo’s PrestaShop module version 1.5.0.

To update your module to the newest version:

1. Log in to your PrestaShop admin.
2. Navigate to ****Modules > Module Manager****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35197586800923)
3. Scroll to find the Klaviyo module and select ****Upgrade****.

![Upgrade Klaviyo module in PrestaShop](https://klaviyo.zendesk.com/hc/article_attachments/28704479194139)

If you are upgrading from a version below 1.3.0, cart rebuild links that were used in abandoned cart emails sent prior to the upgrade will no longer work. However, all abandoned cart messages sent after the upgrade will function properly.

To learn about changes made in each version, head to the [Klaviyo module in PrestaShop’s Addons Marketplace](https://addons.prestashop.com/en/newsletter-sms/49837-klaviyo.html), scroll down to **What’s New**, and click ****Show changelog history****.

#### What is the **Cart Rule Limit** setting?

In the Klaviyo module for PrestaShop, the **Cart Rule Limit** setting allows you to limit how customers may combine cart rule codes on a single order. By default, this is set to **One cart rule per prefix**. This prevents a customer from adding more than one code with the same [prefix](#h_01HYDKX0A91K8ME4MZH60RXMCW) at checkout.

![Coupon usage setting in Klaviyo module for PrestaShop](https://klaviyo.zendesk.com/hc/article_attachments/28704479210395)

### Integration

Additionally, make sure that you’ve integrated Klaviyo with PrestaShop and can view the **Coupons** tab under **Content** in Klaviyo’s left-hand navigation. If you are integrated but do not see the **Coupons** tab:

1. Select your company name in the bottom left corner of Klaviyo’s left-hand navigation, then select ****Integrations****.
2. Search for PrestaShop and select the card.
3. Click ****Update settings**** to update your integration settings. You should now see the **Coupons** tab under **Content** in the left-hand navigation.

## Create your coupon in PrestaShop

Coupons in PrestaShop are called **Cart rules**.

To create a new cart rule in PrestaShop, navigate to the **Cart rules** page and select ****Add new cart rule.****

There are 3 main tabs in PrestaShop when creating a cart rule:

- ****Information****
  Set the cart rule's identifiers (e.g., name) and the main settings.
- ****Conditions****
  Set which customers the coupon should apply for.
- ****Actions****
  Set the cart rule’s discounts and promotions.

![Create cart rule UI in PrestaShop](https://klaviyo.zendesk.com/hc/article_attachments/28704487263643)

Learn more about how to create a [cart rule in PrestaShop](https://docs.prestashop-project.org/1.7-documentation/user-guide/selling/managing-catalog/managing-discounts/cart-rules) and see a description of each field.

Once you create your price rule in PrestaShop, you can link it to a coupon in Klaviyo.

## Configure your coupon in Klaviyo

Now that you’ve created your cart rule in PrestaShop, you need to set it up in Klaviyo so you can generate codes for your flows.

1. Navigate to ****Content > Coupons**** in Klaviyo’s left-hand navigation.
2. In the menu bar along the top, select the ****PrestaShop**** tab.
   ![List of created coupons in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28704487262491)
3. Select ****Create coupon****.
4. Set the following properties for your coupon in Klaviyo:

   - ****Name****
     Create a name for the PrestaShop cart rule in Klaviyo. This name will be used when specifying the coupon in messages.
   - ****Cart rule ID****
     Enter the cart rule ID from PrestaShop. Klaviyo performs a lookup to confirm the cart rule ID exists before showing additional set up options. This must match the associated cart rule ID in PrestaShop exactly.
   - ****Prefix****
     Enter an optional prefix to be applied to each cart rule generated in PrestaShop. Klaviyo will generate a random code for each person, but you can also specify a prefix to be included before every 10 digit code (e.g., the prefix **WELCOME20** will result in a code that looks like **WELCOME20-0123456789**).
   - ****Quantity****
     Specify the minimum number of codes that should be available to be sent each day. Klaviyo will use this number, which must be between 0 and 150,000, to automatically generate a daily inventory of codes. As long as the number of customers receiving coupons does not exceed the minimum number of codes you set, you will not have to replenish the codes for the coupons.
   - ****Active dates****
     Select when the cart rule from PrestaShop becomes active. By default, the coupon will be valid from the date and time a code is created. Even if a valid date in set on the **Conditions** tab of your cart rule in PrestaShop, the **Active date** in Klaviyo will overwrite the PrestaShop setting. For the end date, you can select:
     - ****After a certain number of days****
       The number of days a coupon is valid for after a customer receives it.
     - ****On a specific date****
       A specific date and time after which the coupon will no longer be valid.
5. Click ****Create coupon****.

Once you have created your coupon in PrestaShop and configured it in Klaviyo, Klaviyo will begin generating codes automatically for your flow messages. Below is an example of a correctly configured coupon in Klaviyo:

![Correctly setup PrestaShop coupon in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28704487270555)

## Use your unique coupon in a flow

Once you’ve created and configured your coupon, insert it into a flow message.

1. Navigate to the ****Flows**** tab in Klaviyo’s left-hand navigation.
2. Open an existing flow or [create a new one](https://help.klaviyo.com/hc/en-us/articles/115002774932).
3. Select a flow message inside your flow.
4. Open the message editor for the selected flow message.
5. Click the personalization icon. Depending on your editor, you may see a person icon, or a button labeled ****Personalization****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892625665947)
6. From the **All types** menu, select ****Coupons****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/39892625669787)
7. Select the coupon you'd like to add.
8. Optional: Select the ****3 dots**** on your flow email, then click ****Preview****. Note that when you preview your email directly in Klaviyo, you will not see a unique code populate. Rather, you will see your coupon’s name hyphenated to “PREVIEW.” Klaviyo will only create and share a unique code at the actual send time.

![An example email with a coupon tag shown in preview mode.](https://klaviyo.zendesk.com/hc/article_attachments/39892625671195)

When messages are sent out, a unique discount code, consisting of your prefix and 10 random digits, will dynamically replace the variable for each individual recipient. If you include the same coupon tag in multiple flow messages, the recipient will receive the same unique code each time.

![Unqiue 10 digit code added to the end of coupon prefix](https://klaviyo.zendesk.com/hc/article_attachments/39892625674395)

Unique coupon codes for live flow emails generate automatically based on how many you specify in the **Minimum Inventory** section of the **Coupon details** page. For example, if you create a coupon with a **Minimum Inventory** of 100, Klaviyo generates a batch of 100 unique codes. These automatically replenish daily; however, if you use all 100 codes before the replenishment, the 101st attempt to assign a coupon will be skipped due to insufficient codes available. This automatically triggers Klaviyo to generate another 100 codes. Because coupon codes for flows are replenished automatically, you do not need to manually add batches of coupon codes via the **Add codes** option.

## Test your flow email’s coupon

Before you send out the flow with the coupon to your audience, we recommend testing it first.

1. In the flow builder, click ****Review and turn on****.
2. Change the status to **Manual**.
3. Click ****Turn on****.
4. Trigger your flow by performing the trigger action corresponding with your flow (e.g., filling out a sign-up form to join a certain list). Your flow will automatically generate 100 coupons upon you completing the trigger action.

   The coupon may take a few minutes to generate codes. Because of this, there’s a short loading buffer, and you may see your test profile under **Skipped: Retrying generating codes**. This will go away once the coupons have finished generating.
5. When the coupons have been generated, your test email that triggered the flow will show under **Needs Review** for the email.
6. Click into the ****Needs Review**** bucket under **Recipient activity** for a flow message.
   ![Needs review group in recipient activity for a flow email](https://klaviyo.zendesk.com/hc/article_attachments/28704479202971)
7. Select ****Send Now****.
   ![Send now button for profile in flow email's need review group](https://klaviyo.zendesk.com/hc/article_attachments/28704479202203)
8. Check your inbox for the email with the unique code.

## Troubleshooting common coupon issues

If you are seeing issues with creating unique coupons for PrestaShop in Klaviyo, go through the following recommended troubleshooting steps.

#### Check your Klaviyo plugin version

Klaviyo's unique coupon feature for PrestaShop requires version 1.5.0 or higher of the Klaviyo add-on for PrestaShop. You can check the version of your Klaviyo plugin in PrestaShop under ****Modules > Module Manager****.

If you need to update your Klaviyo add-on, select ****Upgrade****.

![Upgrade Klaviyo module in PrestaShop](https://klaviyo.zendesk.com/hc/article_attachments/28704479194139)

#### Check your PrestaShop integration settings

If your integration with PrestaShop is not syncing, or your PrestaShop store is unreachable, Klaviyo will not be able to generate new coupon codes.

To view your PrestaShop integration settings:

1. Select your company name in the bottom left corner of Klaviyo’s left-hand navigation, then select ****Integrations****.
2. Search for **PrestaShop**, then select the card.
3. Click ****Update settings**** to update your integration settings.

For more assistance on configuring your Klaviyo integration with PrestaShop, see [Getting started with PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360054551492).

#### Verify the Cart Rule ID exists in PrestaShop

If you receive an error indicating that the PrestaShop Cart Rule ID cannot be found, Klaviyo is not able to match the specified Cart Rule ID to one in your PrestaShop account.

To resolve this, update the Cart Rule ID for your coupon, ensuring that it matches an existing cart rule on your PrestaShop store.