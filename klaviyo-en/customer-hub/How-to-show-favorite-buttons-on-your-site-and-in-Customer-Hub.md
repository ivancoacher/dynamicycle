---
id: 33660543083419
title: "How to show favorite buttons on your site and in Customer Hub"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/33660543083419-How-to-show-favorite-buttons-on-your-site-and-in-Customer-Hub"
section: "Build and use Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:39Z"
language: en
---

## You will learn

Learn how to allow shoppers to save their favorite items on your site. By adding favorite buttons alongside your products, you can display shoppers' saved items in the Customer Hub drawer and send follow-up flows to drive conversions.

Customer Hub currently supports Shopify storefronts, including Shopify Headless. Additional eCommerce platform support is planned.

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

This guide covers how to enable the **Favorites** setting from the Customer Hub settings in Klaviyo, and add favorite buttons across different pages of your website. Before proceeding, ensure that the Customer Hub feature is enabled in Klaviyo.

[Learn more about Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675).

## About favorites

Favorite buttons allow shoppers to save products they're interested in. A shopper's favorited items display within the Customer Hub drawer, and can be used in flows to drive additional conversions.

When you activate the **Favorites** feature in your Klaviyo Customer Hub settings, a favorites button appears with all products shown in the Customer Hub interface. When a shopper clicks this button, the item is added to their **Favorites** section and saved to their Klaviyo profile.

![newfavorites1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36998490677787)

To increase their visibility and encourage use, you can also add favorites buttons to:

- Product detail pages
- Collections pages (also called “product list pages”)

Items favorited from either of these pages also save to shoppers' **Favorites** section in the Customer Hub drawer. Note that any visitor can add products to their favorites list, regardless of whether they are logged into a customer account. When they log in, any favorites they've saved will sync to their Klaviyo profile.

## Enable favorites to display in Customer Hub

To display favorites in the Customer Hub drawer, you must first enable the **Favorites** setting in Klaviyo.

Note that if your Customer Hub is live, saving this change publishes it on your site. If not, you’ll need to set your Customer Hub to live in the **General** settings menu to see this change.

1. In Klaviyo’s main, left-hand navigation, select ****Service - Customer Hub****.
2. Click the ****Extensions**** tab.
3. Under **Favorites,** check the box to ****Enable favorites****.
   ![CHfavorites3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39333811326491)
4. In the **Choose icon** dropdown, select which type of favorite icon to display under your products (i.e., a heart or a plus sign).

   - By default, the preview shows the unselected (i.e., not favorited) version of the icon. Click on the icon in the preview to see it change to the favorited state.
5. Click ****Save****.

A favorite button will now appears beneath any products showcased within the Customer Hub interface. Clicking it adds the item to the **Favorites** section.

Continue on to the next section for guidance on adding favorites buttons to product details pages.

## Add favorite buttons to product detail pages

Drive significantly higher engagement by adding "add to favorites" buttons to your product detail pages.

If you use a vintage Shopify theme, or a custom setup that doesn’t support app blocks, see [our instructions for manually installing the favorites button](https://help.klaviyo.com/hc/en-us/articles/33660543083419#h_01JMFW7XMD7V8YYX46ZS6KN8KF).

1. On the **Favorites** setting in Klaviyo, select ****Add app block****.
2. Doing so launches your Shopify theme editor in a new window, showing a modal indicating that the **Klaviyo Favorites** app block was added to your default product page template. Click ****Got it****.
   ![CHfavorites4.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34194825765531)
3. Click and drag the app to adjust its positioning on your product details page as needed.
4. When ready, click ****Save**** to save your changes in Shopify. At this point, favorite buttons will display beneath products on your product pages.
5. Optional: For additional styling, navigate back to Klaviyo. Using the ****App block style**** dropdown, you can customize the look of the favorites button on product pages. Choose either:

   - ****Inherit**** to sync your site’s button styles (default).
   - ****Custom**** to select a certain button font and text color.![newfavorites7.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36998506961435)
6. Save any changes.

Navigate back to your website. You should see favorites buttons populate beneath products on your product detail pages.

![newfavorites10.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006519959707)

Next, skip ahead to the [Add favorites buttons to your collections pages section](https://help.klaviyo.com/hc/en-us/articles/33660543083419#h_01JV68255SF0RFVDTENFZR7HDS).

## Manually install favorite buttons (vintage themes or custom set up)

If you use a vintage Shopify theme, or a custom setup that doesn’t support app blocks, you may need to manually install the Klaviyo Wishlist app to the pages where you’d like favoriting actions (e.g., product pages).

To do so:

1. Open your Shopify store admin.
2. Under sales channels, select ****Online store****.
3. Click the three dots menu on your current theme, then select ****Edit code****. If you would rather test it on a draft theme, duplicate your current theme first and then edit the code of the duplicate theme.
   ![CHfavorites5.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34194866098075)
4. Find the file for your product details page. This varies by theme, but typically has the word “product” in its name. For example, in the Dawn theme, this is called “main-product.liquid.”
5. Paste the following code snippet wherever you want the favorites button to appear:
   `<div class="klaviyo-wishlist-slot" data-product-id="{{ product.id }}"></div>`
6. Click ****Save****.
7. Click ****Preview store****.
8. Navigate to a product page within your store preview. The added favorites button should be visible in the designated location.

## Add favorite buttons to your collections pages

Install a small snippet of code on your Shopify site to add favorite buttons to your collections pages so shoppers can quickly save items while browsing your products. This is especially useful for shoppers on mobile devices.

To do so:

1. Open your Shopify store admin.
2. Under sales channels, select ****Online store****.
3. Next to your current theme, click the three dots menu, then select ****Edit code****.

   - If you want to test on a draft theme, duplicate your current theme first and then edit the code in the duplicate theme.
4. In the left-hand sidebar, search for and open your collections file. We’ll use the featured-collections.liquid file for this example, however your theme may use a different file.
   ![newfavorites2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36998506970651)
5. Within the collections file, use the find shortcut (Command+F on Mac or Control+F on Windows) to search the word “render” within the file. This helps you identify the snippet name containing your product grid.

   - The snippet will likely appear in a format similar to: {% render 'snippet-name'%}, where 'snippet-name' is the name of the relevant snippet file (e.g., card-product).![newfavorites3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36998490698907)
6. In the left sidebar, search for and open the snippet file identified in the previous step (e.g., card-product.liquid).
7. At the top of this file, note the object value listed under “Accepts” (e.g., “card\_product”).
   ![newfavorites6.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36998490700571)
8. Copy the following code and paste it into the snippet file:

   - Tip: Look for the first instance of the price rendering in your file and paste the code above it.
     `<div`

      `class="klaviyo-favorites-plp-slot"`

      `data-product-id="{{ OBJECT.id }}"`

      `data-product-url="{{ OBJECT.url }}"`

      `data-variant-id="{{OBJECT.selected_or_first_available_variant.id}}"`

      `></div>`
9. Within the code you pasted, replace `OBJECT` with the object value you noted earlier.

   - For example, if your file’s object value is “card\_product,” the code will look like this when pasted into the file above the price.![newfavorites5.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36998490706075)
10. Click ****Save**** in Shopify.
11. Go to your site’s collections page and refresh.

You should now see the favorite buttons appear on each product. Note these may take a few seconds to load. By default, these are positioned in the top right corner. If you wish to change the positioning, consult your developer for assistance with custom CSS.

![newfavorites11.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006575924891)

If the favorite buttons still have not appeared, try these troubleshooting steps:

- Confirm that you’ve replaced `OBJECT` in the code snippet with your file’s object value.
- Try pasting the code elsewhere in the file.
- Verify that you’ve pasted the code in the correct snippet file.

If they still don’t appear, seek assistance from [a developer](https://connect.klaviyo.com/). Klaviyo's support team is not able to directly edit your theme files.

## Next steps

Now that you've added favorite buttons to your site, set up a favorites reminder flow to drive conversions by reminding shoppers about their recently saved items.