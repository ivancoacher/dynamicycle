---
id: "19736852757915"
title: "How to remove onsite tracking for BigCommerce"
source_url: "https://help.klaviyo.com/hc/en-us/articles/19736852757915-How-to-remove-onsite-tracking-for-BigCommerce"
section: "Getting started with BigCommerce"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:33Z"
language: "en"
---
## You will learn

Learn how to remove Klaviyo onsite tracking from your BigCommerce site. Onsite tracking encompasses both **Active on Site** and **Viewed Product** tracking.

**Active on Site** tracking is enabled via Klaviyo’s onsite JavaScript, also known as Klaviyo.js, so removing **Active on Site** tracking requires removing Klaviyo.js. Klaviyo.js was automatically added to your site when integrating BigCommerce with Klaviyo, but can be toggled off in Klaviyo.

**Viewed Product** tracking for BigCommerce is enabled via a snippet you added to your site [during the integration process](https://help.klaviyo.com/hc/en-us/articles/115005082547#h_01HAQ99C0AKXHH3PH3ZY2V4TS8), so removing **Viewed Product** tracking requires removing this snippet.

## Before you begin

You may wish to remove onsite tracking for site speed performance reasons, though Klaviyo.js has recently been updated to [minimize its impact](https://klaviyo.tech/improving-forms-performance-c67c98114d49) in this regard.

If you no longer wish to have Klaviyo onsite tracking enabled on your store, you can:

- Remove **Viewed Product** tracking only.
- Remove both **Active on Site** and **Viewed Product** tracking. Note that removing **Active on Site** tracking without removing **Viewed Product** tracking causes **Viewed Product** tracking to no longer function.

It is important to note that:

- Removing **Active on Site** tracking will also cause Klaviyo sign-up forms to no longer work.
- Removing **Viewed Product** tracking means you will not be able to track when someone views a product on your store, so you will no longer be able to send browse abandonment messages.
- Removing onsite tracking will cause Klaviyo’s [Added to Cart functionality](https://help.klaviyo.com/hc/en-us/articles/360024310292) (if you’ve set this up for BigCommerce) to no longer work.

## Remove Active on Site tracking

Removing **Active on Site** tracking from your BigCommerce site requires unchecking an integration setting in Klaviyo.

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****BigCommerce**** from the list.
3. Uncheck the **Automatically add Klaviyo onsite javascript** setting.
   ![BigCommerce onsite tracking setting](https://klaviyo.zendesk.com/hc/article_attachments/28723684603547)
4. Click ****Update Settings****.

**Active on Site** tracking will now be removed from your BigCommerce store.

## Remove Viewed Product tracking

Removing **Viewed Product** tracking from your BigCommerce site requires removing the code snippet you [added during integration](https://help.klaviyo.com/hc/en-us/articles/115005082547#h_01HAQ99C0AEYNSZ7YKNX9PX6C9) from your site code.

1. To view the snippet for reference:

1. In your Klaviyo account, select the ****Integrations****tab.
2. In the upper right corner, click ****Manage data > Set up web tracking****. From here, you can view the **Viewed Product** snippet to see what needs to be removed from your site.
   ![Add viewed product tracking step in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28723684608667)

2. In a new tab, log in to your BigCommerce dashboard and navigate to ****Storefront > My Themes****.
3. From the Current Theme, click the ****Advanced Settings**** dropdown and click ****Edit Theme Files****. Note that if you are working with a default theme, the option to edit theme files will not appear. You’ll want to make a copy of the theme, and then make your edits to the copy. Any edits you make will only apply to the theme you are editing.
4. In the editor, navigate to ****Templates > Pages****, scroll down, and click to open the ****product.html**** page.
5. At the bottom of this page, you’ll see the **Viewed Product** code snippet. Delete the snippet, then click ****Save all files****.
   ![Product page template in BigCommerce with Viewed Product snippet](https://klaviyo.zendesk.com/hc/article_attachments/28723684606107)

**Viewed Product** tracking has now been removed from your BigCommerce site.

## Additional resources

- [Getting started with Klaviyo onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767)
- [Getting started with BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547)
- [How to add a Klaviyo embedded form to your BigCommerce site](https://help.klaviyo.com/hc/en-us/articles/360022594552)