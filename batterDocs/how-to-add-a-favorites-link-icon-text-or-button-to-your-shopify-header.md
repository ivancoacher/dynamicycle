<h1>How to add a Favorites link (icon, text, or button) to your Shopify header</h1>

Adding a specific "Favorites" icon to your site's navigation bar ("header") drives more engagement by reducing friction for your customers to find their favorites within Customer Hub. By giving shoppers a dedicated launch point for their saved items, you encourage them to build bigger baskets and return to your store more often.

You can implement this as an ****icon**** (e.g., a heart), a simple ****text link**** (e.g., "Favorites"), or a ****button****. This guide covers how to insert the necessary code into your site's header using Shopify's Liquid code.

![](https://klaviyo.zendesk.com/hc/article_attachments/43956692602011)

This guide covers how to upload a heart icon to your theme assets and insert the code link into your site's header using Shopify's Liquid code.

> ****Notice**** This process involves editing your Shopify theme code. If you are not comfortable writing code or do not have a developer on your team, we recommend reaching out to a [Klaviyo Partner](https://www.google.com/search?q=https://connect.klaviyo.com/directory) for assistance. Klaviyo support is unable to troubleshoot custom code implementations.

## Before you begin

We strongly recommend duplicating your live theme before making changes. This allows you to test the new icon in a safe environment without affecting your live store.

1. In Shopify, go to ****Online Store > Themes****.
2. Click the ****three dots menu (...)**** next to your live theme.
3. Select ****Duplicate****.

## Step 1: Prepare your assets (if you want to use an icon)

First, upload the icon file that will serve as the button. Using an SVG file is best because it scales to any screen size without losing quality and can inherit your theme's colors.

1. You need to find an icon you want to use. This can be any icon, but we recommend using an SVG to avoid pixelation. You can download a standard (MIT licensed) version here: [****Heroicons heart.svg****](https://raw.githubusercontent.com/tailwindlabs/heroicons/refs/heads/master/src/24/outline/heart.svg).
2. In your Shopify Admin, navigate to ****Online Store > Themes****.
3. Find your theme and click the ****three dots menu (...) > Edit code****.
4. In the left sidebar, scroll down to the ****Assets**** folder and click ****Add a new asset****.
5. Upload your icon file.

## Step 2: Insert the header (top navigation bar) link

Next, add the code snippet that displays the icon and links it to the Customer Hub.

1. In the theme code editor, locate the file that controls your header.

   - ****Online Store 2.0 themes (e.g., Dawn):**** Search for `sections/header.liquid`.
   - ****Vintage themes:**** Search for `snippets/header-icons.liquid` or `header-bar.liquid`.
2. ****Find the insertion point:**** Press `Ctrl+F` (or `Cmd+F` on Mac) and search for the word `cart` or `account`. You want to paste your new code inside the same container (usually a `<div>` or `<ul>`) that holds these existing icons.
3. Paste ****one**** of the code options below where you want the link to appear (e.g., right before the Cart icon).

###

### Option A: The Icon Link

Use this code if you completed Step 1 and want to display a heart icon, assuming it's named icon-heart.svg in our example:

```
<a href="#k-hub/favorites"
   id="favorites-icon-bubble"
   aria-label="Open Favorites"
   title="Favorites"
   style="display:flex;align-items:center;justify-content:center;height:4.4rem;width:4.4rem;">
  <span style="height:20px;width:20px">
    {{ 'icon-heart.svg' | inline_asset_content }}
  </span>
</a>
```

### Option B: Text Link or Button

Use this code if you prefer a text link or a button. You do not need to upload any assets for this.

****For a simple text link:****

```
<a href="#k-hub/favorites" class="header__menu-item header__menu-item--list" style="text-decoration: none;">
  Favorites
</a>
```

****For a button:****

```
<a href="#k-hub/favorites" class="button button--primary">
  Favorites
</a>
```

1. Click ****Save****.

> ****Tip: Matching your Theme's Style**** If your theme uses a specific CSS class for header icons (e.g., `header__icon` or `icon-link`), you can replace the inline `style=` attribute in the code above with that class (e.g., `class="header__icon"`). This ensures the spacing and hover effects match your other buttons perfectly.

## Outcome

Once saved, open your store in a ****new Incognito/Private window**** to bypass any browser caching. You should see the heart icon in your navigation bar. Clicking this icon will now open the ****Favorites**** tab within the Customer Hub.

## Troubleshooting

If the icon does not appear or looks incorrect:

- ****Icon is a broken image:**** Ensure you uploaded the file to the ****Assets**** folder and named it exactly `icon-heart.svg`. The filenames are case-sensitive.
- ****Icon is misaligned:**** You may need to adjust the `height` and `width` values in the code snippet's `style` attribute to match your theme's navigation bar height.
- ****Changes not showing:**** Shopify themes cache aggressively. Try previewing the theme in an Incognito window or appending `?preview_theme_id=` to your URL if working on a draft theme.
