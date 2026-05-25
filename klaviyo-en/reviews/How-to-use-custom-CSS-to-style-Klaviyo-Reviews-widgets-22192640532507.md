---
id: "22192640532507"
title: "How to use custom CSS to style Klaviyo Reviews widgets"
source_url: "https://help.klaviyo.com/hc/en-us/articles/22192640532507-How-to-use-custom-CSS-to-style-Klaviyo-Reviews-widgets"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:25Z"
language: "en"
---
## You will learn

Learn about custom CSS for Klaviyo Reviews, including how to implement some basic use cases. For more advanced use cases, head to our [developer resource on custom CSS for Klaviyo Reviews](https://developers.klaviyo.com/en/docs/klaviyo_reviews_css_class_reference). Most widget customization can be implemented using [drag and drop editors](https://help.klaviyo.com/hc/en-us/articles/16691401577883); CSS is only required for advanced use cases.

Implementing custom CSS for your reviews widgets involves editing your site’s code. This is only recommended for technically savvy marketers or those who have access to a developer. While our product does support custom CSS, our support team cannot help you customize your widgets beyond the general guidance covered in this documentation. To maintain the security of your data, Klaviyo's support team is not able to open your HTML files.

## About custom CSS for Klaviyo Reviews

Klaviyo Reviews provides a wide range of CSS class selectors, which can be used to write custom CSS and apply advanced styling options to your reviews widgets. For more information, head to our [complete dictionary of Klaviyo Reviews CSS classes](https://developers.klaviyo.com/en/docs/klaviyo_reviews_css_class_reference).

## How to apply custom CSS

You can apply custom CSS to Klaviyo Reviews in the same manner you’d apply any other custom CSS:

- Add custom CSS to your site’s main CSS stylesheet.
- Insert <style> tags within a single page’s code to apply CSS to that page.
- Embed CSS in a single HTML element (e.g., a div) to apply it just to that element.
- Add custom CSS to your entire site in ****Theme Settings > Custom CSS**** (Shopify) or ****Styles > CSS**** (WooCommerce).

We’ll focus on the last option here, because it is the simplest to implement.

Note that Klaviyo Reviews, including the default styles, generally load after CSS from from your ecommerce platform. This means it’s important to use precise selectors, so your custom CSS isn’t overwritten by the defaults.

### Apply custom CSS for Shopify

1. In your Shopify admin, navigate to ****Online Store > Themes****.
2. From the additional options menu (3 dots) for your current theme, click ****Duplicate.****

   It’s not recommended to make edits to your current theme while it is live, as these edits may appear to site visitors before you can review the changes and troubleshoot any issues.
   ![duplicate your theme](https://klaviyo.zendesk.com/hc/article_attachments/28717854192283)
3. Click ****Customize**** next to the new copy of your theme.
4. Click the Theme settings icon.
   ![theme settings button](https://klaviyo.zendesk.com/hc/article_attachments/28717881714203)
5. Select ****Custom CSS**** from the menu.
   ![custom css field](https://klaviyo.zendesk.com/hc/article_attachments/28717854198427)
6. Add your custom CSS.

   Sample CSS snippets are available in the section below to copy.
7. Navigate to a page in the editor where your reviews widgets appear (e.g., ****Default product****).
8. Review the edits, then click ****Publish****.

### Add custom CSS for WooCommerce

You must use a page ID selector,`.page-id-YOUR_PAGE_ID` , to apply CSS to a specific page or pages. Learn how to [find a page ID](https://wordpress.com/support/pages/#find-the-page-id).

1. In your Wordpress admin, navigate to ****Appearance > Editor****.
2. Select ****Styles****.
   ![The Styles option](https://klaviyo.zendesk.com/hc/article_attachments/28717854201883)
3. Open the three dots (**More**) menu.
4. Select ****Additional CSS****.
   ![The Additional CSS option](https://klaviyo.zendesk.com/hc/article_attachments/28717881720347)
5. Add your custom CSS.

   Sample CSS snippets are available in the section below to copy.
6. Review the edits, then click ****Publish****.

## Custom CSS use cases

The CSS snippets below cover some basic use cases. More advanced customization requires developer support. If you don't have a developer on your team and are not comfortable writing code yourself, consider reaching out to a [Klaviyo Partner](https://connect.klaviyo.com/) for assistance.

****Rating icon (star) appearance****

Replace the URLs below with image URLs representing your preferred full star, partial star, and empty star, respectively. Note that for Shopify stores, your URLs must reference images stored in Shopify, due to their rules.

```
#klaviyo-product-reviews-wrapper {
  .kl_reviews__star {
    display: none;
  }
  .kl_reviews__full_star {
    background-image: url("https://cdn.shopify.com/s/files/1/0284/3128/6351/files/full-moon.png?v=1705073898");
    background-size: cover;
  }
  .kl_reviews__partial_star {
    background-image: url("https://cdn.shopify.com/s/files/1/0284/3128/6351/files/last-quarter-moon.png?v=1705073898");
    background-size: cover;
  }
  .kl_reviews__empty_star {
    background-image: url("https://cdn.shopify.com/s/files/1/0284/3128/6351/files/new-moon.png?v=1705073898");
    background-size: cover;
  }
}
```

****Image thumbnail size****

Set a specific width for the customer-submitted images in your review list.

`#klaviyo-product-reviews-wrapper .kl_reviews__review__image { width: 225px; }`

****Button colors and styles****

Apply styles to just the ****Write a review**** button.

```
#klaviyo-product-reviews-wrapper .kl_reviews__button:nth-child(1) {
   color: blue;
   box-shadow: 0 0 15px #9ecaed;
}
```

Apply styles to just the ****Ask a question**** button.

```
#klaviyo-product-reviews-wrapper .kl_reviews__button:nth-child(2) {
   color: blue;
   box-shadow: 0 0 15px #9ecaed;
}
```