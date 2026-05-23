<h1>How to collect SMS consent at checkout on BigCommerce</h1>

## You will learn

Learn how to start collecting SMS consent at checkout for BigCommerce. This should take about 5–10 minutes total. To make it easier, we recommend logging in to your BigCommerce and Klaviyo accounts and keeping both open.

****Why collect SMS consent at checkout?****

Gathering consent for SMS marketing on your checkout page is the simplest way to grow your list. BigCommerce stores can take advantage of this with Klaviyo, allowing you to extend your reach with text message marketing. Consent will be synced to Klaviyo when someone inputs their phone number, opts in to SMS marketing, and clicks ****Continue**** in the **Shipping** step on the checkout page, making it easy to grow your SMS list.

## Before you begin

Note that you must:

- Have [turned on SMS in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/4404274419355).
- [Create a mobile terms of service](https://klaviyo.zendesk.com/hc/en-us/articles/360049177511)
- Update your [privacy policy](https://klaviyo.zendesk.com/hc/en-us/articles/4404199571867)

Tip: Have the links for your privacy policy and terms of service ready, as you will need them when you update your Klaviyo integration settings.

You can only collect SMS consent where Klaviyo SMS is available. See this article for information on [where you can use Klaviyo SMS](https://help.klaviyo.com/hc/en-us/articles/4402914866843).

## In Klaviyo: update your integration settings

1. Click your organization name in the bottom left corner.
2. Navigate to ****Integrations > BigCommerce****.
3. Check the ****Sync your BigCommerce SMS subscribers to Klaviyo**** box.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28705664167835)
4. Select the list you want SMS subscribers to sync to. Note that you should use a different list for SMS than email if you are also collecting email subscribers. Assigning a separate list for each channel ensures that consent is properly applied to the correct channel.
5. Below the list, paste the links for your privacy policy and terms of service.
6. Copy the code snippet and keep it on hand.
7. Click ****Save**** to save these changes and go to your BigCommerce store.

## In BigCommerce: add the script via script manager

1. In your BigCommerce store, navigate to ****Storefront > Script Manager****.
2. Choose ****Footer**** for the script's location on page.
3. Select ****Checkout**** for where the script will be added.
4. Select the most applicable script category. For SMS consent at checkout, we recommend that you pick ****Targeting; Advertising****.
   ![Options for adding SMS consent at checkout in BigCommerce](https://klaviyo.zendesk.com/hc/article_attachments/28705664161563)
5. Choose ****Script**** as the script type.
6. Paste the snippet of code in the **Script Contents** box below.
   ![Field to paste the snippet of code for SMS consent at checkout](https://klaviyo.zendesk.com/hc/article_attachments/28705664162203)
7. When you have finished making your selections and have pasted the script, click ****Save****.
8. Optional: If you want to adjust the placement of the field on your checkout page
   1. Head to ****Advanced Settings > Account Sign Up Form****.
      ![Account Sign up Form page under BigCommerce's Advanced Settings](https://klaviyo.zendesk.com/hc/article_attachments/28705637369499)
   2. Click into the ****Address Fields****tab.
   3. Move the phone number field to the bottom of the list.

## Outcome

Your checkout page will now look similar to the one shown below.

![Example of a BigCommerce checkout page that can collect SMS consent](https://klaviyo.zendesk.com/hc/article_attachments/28705664165403)

Now, when someone enters their phone number, selects the checkbox to accept SMS marketing, and clicks ****Continue**** in the **Shipping** section, they will automatically sync to your designated Klaviyo list, making it easier and faster to grow your SMS list.

## Additional resources

- Learn the [basics of using SMS and email together](https://help.klaviyo.com/hc/en-us/articles/360056849631).
- Find out [how to add an embedded form to your site](https://help.klaviyo.com/hc/en-us/articles/360022594552).
- Want to stop collecting SMS subscribers? Read this [article on disabling SMS consent at checkout.](https://help.klaviyo.com/hc/en-us/articles/360058194372)
