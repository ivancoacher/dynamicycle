<h1>How to collect transactional SMS consent on Shopify checkout pages</h1>

Only Shopify Plus customers can collect transactional consent on their checkout pages. Non-Plus customers can collect transactional consent on thank you and order status pages.

Learn how to collect transactional SMS consent on Shopify checkout, thank you, and order status pages and sync it to Klaviyo. You can collect both transactional and marketing SMS consent on these pages via an SMS app block, which you’ll set up in Klaviyo and then install in Shopify.

## Before you begin

Before starting, make sure that you:

- Have [Klaviyo SMS enabled](https://help.klaviyo.com/hc/en-us/articles/4404274419355)
- Have [integrated Klaviyo with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)
- Have [Klaviyo onsite tracking enabled](https://help.klaviyo.com/hc/en-us/articles/4425956184731)

Are you a Shopify Plus customer currently sending [order updates via SMS](https://help.klaviyo.com/hc/en-us/articles/18389135527323)? Please note that collecting both transactional-only consent at checkout via app block and collecting consent for SMS order updates may appear repetitive to customers; you may wish to only use one feature.

## About SMS app blocks

- For Shopify Plus only: Checkout pages (billing, shipping, and credit card info pages, and one-page checkout)
- Thank you pages
- Order status pages

- You can use SMS app blocks to collect marketing consent, transactional consent, or both.
- You can create multiple SMS app blocks and place them on different pages, including:
- You can view and edit your SMS app blocks in Klaviyo, though you must add or delete them within Shopify.

## Set up your SMS app block

Follow the instructions below to set up an SMS app block. If you’d like to create multiple app blocks to collect different forms of consent in different places, simply repeat this process. You can also install the same app block on multiple Shopify pages.

- Transactional and marketing
- Transactional with optional marketing
- Transactional only
- Collect phone number without consent
  ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671634971)
- ****Input label****
  The label on the phone number field.
- ****Invalid text****
  Message displayed when the form encounters an error.
- ****Submit button text****
  The language on the submit button (e.g., “Sign up”).
- ****Success message****
  The message the user receives after submitting their phone number successfully.

1. In Klaviyo, select ****Audience > Growth tools****.
2. Next to **Add an app to your Shopify page to collect SMS subscribers**, select ****Set up****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36058710841499)
3. Name your app block something descriptive, such as the page where it will live. One app block can live on multiple pages, or you can create multiple app blocks.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36058710844571)
4. Select the list that SMS subscribers will sync to. Generally, you’ll want to select the same list you chose in your integration settings. Your customers will be sent double opt-in messaging in [accordance with the list’s settings](https://help.klaviyo.com/hc/en-us/articles/115005251108). Transactional-only subscribers will not receive double opt-in messaging.
5. Click ****Next****.
6. Under **Select a consent type**, choose one of the following:
7. Next, add the heading text for your app block, as shown in the image below. On the right, you’ll see a preview of what your app block will look like in Shopify. Please note that this preview will not reflect your Shopify theme colors, which the app block will inherit automatically when installed in Shopify.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36058710851739)
8. Click ****Next****.
9. Edit your disclosure text if needed. Then, click ****Next****.
10. Edit additional content for your app block. These fields are:
11. When you’re finished, click ****Next****.
12. On the next page, click the copy icon to copy the app block ID, and save it somewhere accessible.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/36058710852763)
13. Now, you’re ready to disable consent collection (if needed) and then install the app block in Shopify.

## Disable SMS consent collection in Shopify

Consider disabling Shopify’s native checkbox to avoid having duplicate checkboxes on your checkout page if you:

1. Are a Shopify Plus customer,
2. Previously collected marketing consent at checkout via the Shopify’s native checkbox, and
3. Want to collect marketing consent via an SMS app block at checkout.

   To do this:
4. In your Shopify admin, click ****Settings**** at the bottom of the left sidebar.
5. On the **Settings** page, click ****Checkout****.
6. Under **Marketing options**, toggle off ****SMS****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36060438161691)
7. Click ****Save****.

Please note that you’ll want to leave your Shopify integration setting **Sync your Shopify SMS subscribers to Klaviyo** checked, in order to continue syncing Shopify subscribers collected via other means (such as Shopify forms) to Klaviyo.

If you want profiles subscribed via SMS app block to sync back to Shopify, [make sure that this setting is enabled](https://help.klaviyo.com/hc/en-us/articles/360030919351#h_01HGK64RFVRENS52W53SMSC9NC).

## Install the app block in Shopify

1. In your Shopify admin, select ****Online Store****.
2. Find your Shopify theme and click ****Customize****.
3. Select the ****Home page**** dropdown and click ****Checkout and customer accounts**** to be brought to the checkout editor.
4. Select the ****Checkout**** dropdown, and then select the page where you’d like to place your app block.
5. Scroll to the section where you’d like to add your app block and click ****+ Add app block****. [Learn more](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-apps#move-place-app) about placing an app block.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671642779)
6. Click the Klaviyo app block labeled ****Opt-in at checkout****.
7. Under **Klaviyo App Block ID**, paste the ID you saved from Klaviyo.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671644059)
8. (Optional) You can toggle on **Include app block in Shop Pay** if desired.
9. Click ****Save****.
10. You should now see your app block live on the page you selected.

## Manage your SMS app blocks

To manage your app blocks:

1. Navigate to ****Audience > Growth tools****.
2. Next to **Add an app to your Shopify checkout page to collect SMS subscribers**, click ****Manage****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671645595)
3. Here, you’ll be able to view all your SMS app blocks.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671648155)
4. To create a new app block, click ****Create app****.
5. If you click the 3 dots next to an app block, you’ll see the following options:

- ****Manage list****
  Manage the list associated with your app block
- ****Rename****
  Rename your app block
- ****Edit****
  Edit your app block
- ****Install****
  View instructions about installing your app block in Shopify
- ****Clone****
  Clone your app block
- ****Delete****
  Delete your app block in Klaviyo. Please note that this will not delete it in Shopify, but it will render blank and not take up any space. You can remove your app block in Shopify by selecting it, then clicking the ****Trash**** icon.

![](https://klaviyo.zendesk.com/hc/article_attachments/36058671651483)

## Additional resources

[Getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)

[How to send order updates via SMS for Shopify](https://help.klaviyo.com/hc/en-us/articles/18389135527323)

[How to ask for transactional consent separately](https://help.klaviyo.com/hc/en-us/articles/31583129959195)
