---
id: "26922347702939"
title: "How to install Klaviyo Reviews for WooCommerce"
source_url: "https://help.klaviyo.com/hc/en-us/articles/26922347702939-How-to-install-Klaviyo-Reviews-for-WooCommerce"
section: "Getting started with reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-05-06T16:29:16Z"
language: "en"
---
## You will learn

Learn how to install Klaviyo Reviews on your WooCommerce store and add reviews widgets. To learn about all the steps required to get started, head to [Getting started with Klaviyo Reviews.](https://klaviyo.zendesk.com/hc/en-us/articles/15937542819355)

## Before you begin

There are 4 methods of installing Klaviyo Reviews for WooCommerce. The right one for you depends on your level of technical knowledge and your Wordpress setup. Use the flowchart below to select the best installation method for you.

![A flow chart indicating that users who are uncomfortable using code should add a plugin and use the visual theme editor; those without access to their theme files should use a plugin plus code snippets; those who use a third-party or custom theme should use short codes, and those with access to their site's functions.php file should modify their theme files directly. These options start with the least technically challenging, and end with the most technically challenging.](https://klaviyo.zendesk.com/hc/article_attachments/28722599957275)

When selecting an installation method, consider the following:

- Adding star ratings to collection pages is only supported for 2 installation methods: plugin with visual editor and short codes.
- Consider your level of editor access in Wordpress. Not all users have the option to edit website theme files directly. If you don’t have access to your [functions.php file](https://developer.wordpress.org/themes/core-concepts/custom-functionality/) or similar, use one of the other methods.
- Several of these methods require adding another plugin to your Wordpress site. The instructions below reference the Code Snippets plugin, but Klaviyo does not endorse any particular plugin and cannot assist with plugin-related troubleshooting.

  Once you’ve selected the right installation steps for you, proceed to the relevant instructions.

  Learn how to install Klaviyo Reviews for WooCommerce by:
- [Installing a plugin and using the visual theme editor](#h_01J1FFYXRRSR45ACAKVXCNQB91)
- [Installing a plugin, without using the visual theme editor](#h_01J1FFZZ2EHN1PKBZXEHA4MSEK)
- [Adding short codes](#h_01J1FG22Y6SERD6MYYC0T28AD9)
- [Modifying your theme files](#h_01J1FG38N26A6DCNCRG02YR0W9)

## Available reviews widgets

Once you install Klaviyo Reviews, your store will display reviews widgets, which feature rating and review details.

- ****Star rating widget****
  Displays your current star rating for a particular product, and is most often added beneath your product’s name either on the product page or a collection page.
  ![Star rating](https://klaviyo.zendesk.com/hc/article_attachments/28722611980187)
- ****Product reviews widget****
  Shows a chart breaking down all the ratings a product received, user images submitted with reviews, and the most common feedback the product has received.

  Below that is a list of all published reviews and customer questions along with a search bar, review filters, a ****Write a Review**** button, and an ****Ask a Question**** button.

  This widget is usually added near the bottom of a product page.
  ![Summary widget](https://klaviyo.zendesk.com/hc/article_attachments/28722599979035)
  ![Reviews list](https://klaviyo.zendesk.com/hc/article_attachments/28722611982363)
- ****Featured review carousel widget****
  Displays highlighted reviews from all your products. You can feature this on your homepage, on a standalone reviews page, or anywhere else on your site. You can also select the reviews that are featured in this widget. If available, customer-submitted images accompany each review; your product images are used if no image was submitted.
  ![A carousel of reviews](https://klaviyo.zendesk.com/hc/article_attachments/28722599980571)
- ****SEO / All reviews widget****
  Displays all your reviews across all products on a single page. Use this widget to improve your SEO and provide a single place for potential customers to see what your current customers love. This widget is most often added to a standalone **Reviews** page on your site.

![all reviews widget](https://klaviyo.zendesk.com/hc/article_attachments/28722599987355)

## Install a plugin and use the visual theme editor

In order to use the visual theme editor to add Klaviyo Reviews widgets to your site, you must first add a piece of code to load these drag-and-drop blocks in your theme. You can use a tool like [Code Snippets](https://wordpress.org/plugins/code-snippets/) to add the source code for these blocks, then use the visual theme editor to drag-and-drop Klaviyo Reviews widgets into your theme.

### Add reviews widget source code

These instructions assume you have already installed the [Code Snippets](https://wordpress.org/plugins/code-snippets/) plugin, but you can use a different plugin instead.

1. Select ****Snippets > Add new**** from the Wordpress sidebar.
   ![The Snippets option in the Wordpress sidebar](https://klaviyo.zendesk.com/hc/article_attachments/28722611964443)
2. In the **Enter title here** field, name the snippet something clear, like “Klaviyo Reviews Widgets Code”.
3. In the **Functions (PHP)** tab of the **Code** section, add the code snippet below.
4. Click ****Save Changes and Activate****.

#### Reviews widget source code

```
function register_klaviyo_reviews_blocks() {
    // Register the blocks
    register_block_type( 'klaviyo/product-reviews', array(
        'editor_script' => 'klaviyo-block-editor-script',
        'render_callback' => 'render_klaviyo_product_reviews',
    ));
    register_block_type( 'klaviyo/product-star-ratings', array(
        'editor_script' => 'klaviyo-block-editor-script',
        'render_callback' => 'render_klaviyo_star_ratings',
    ));
    register_block_type( 'klaviyo/featured-reviews', array(
        'editor_script' => 'klaviyo-block-editor-script',
        'render_callback' => 'render_klaviyo_featured_reviews',
    ));
    register_block_type( 'klaviyo/all-reviews', array(
        'editor_script' => 'klaviyo-block-editor-script',
        'render_callback' => 'render_klaviyo_all_reviews',
    ));
}
add_action( 'init', 'register_klaviyo_reviews_blocks' );
function enqueue_klaviyo_block_editor_assets() {
    // Register and enqueue the logo image
    wp_register_script(
        'klaviyo-block-editor-script',
        false,
        array( 'wp-blocks', 'wp-element', 'wp-editor' ),
        false,
        true
    );
    $logo_url = plugins_url( 'img/klaviyo-logo.png', 'klaviyo/klaviyo.php' );
    wp_add_inline_script( 'klaviyo-block-editor-script', '
        ( function( blocks, element ) {
            var el = element.createElement;
            // Add custom category
            blocks.updateCategory( "widgets", {
                slug: "klaviyo",
                title: "Klaviyo",
                icon: el("img", { src: "' . $logo_url . '", style: { width: "20px", height: "20px" } })
            } );
            blocks.registerBlockType( "klaviyo/product-reviews", {
                title: "Klaviyo Product Reviews",
                icon: "admin-comments",
                category: "klaviyo",
                edit: function() {
                    return el(
                        "div",
                        { className: "klaviyo-product-reviews" },
                        "Klaviyo Product Reviews will be displayed here"
                    );
                },
                save: function() {
                    return null;
                },
            });
            blocks.registerBlockType( "klaviyo/product-star-ratings", {
                title: "Klaviyo Star Ratings",
                icon: "star-filled",
                category: "klaviyo",
                edit: function() {
                    return el(
                        "div",
                        { className: "klaviyo-product-star-ratings" },
                        "Klaviyo Product Star Ratings will be displayed here"
                    );
                },
                save: function() {
                    return null;
                },
            });
            blocks.registerBlockType( "klaviyo/featured-reviews", {
                title: "Klaviyo Featured Reviews",
                icon: "admin-post",
                category: "klaviyo",
                edit: function() {
                    return el(
                        "div",
                        { className: "klaviyo-featured-reviews" },
                        "Klaviyo Featured Reviews will be displayed here"
                    );
                },
                save: function() {
                    return null;
                },
            });
            blocks.registerBlockType( "klaviyo/all-reviews", {
                title: "Klaviyo All Reviews",
                icon: "admin-page",
                category: "klaviyo",
                edit: function() {
                    return el(
                        "div",
                        { className: "klaviyo-all-reviews" },
                        "Klaviyo All Reviews will be displayed here"
                    );
                },
                save: function() {
                    return null;
                },
            });
        } )(
            window.wp.blocks,
            window.wp.element
        );
    ' );
}
add_action( 'enqueue_block_editor_assets', 'enqueue_klaviyo_block_editor_assets' );
// Callback functions to render the blocks
function render_klaviyo_product_reviews( $attributes, $content ) {
    global $product;
    if ( is_product() && isset($product) ) {
        return "<div id='klaviyo-reviews-all' data-id='" . esc_attr($product->get_id()) . "'></div>";
    }
}
function render_klaviyo_star_ratings( $attributes, $content ) {
    global $product;
    if (isset($product)) {
        return "<div class='klaviyo-star-rating-widget' data-id='" . esc_attr($product->get_id()) . "'></div>";
    }
}
function render_klaviyo_featured_reviews( $attributes, $content ) {
    return "<div id='klaviyo-featured-reviews-carousel'></div>";
}
function render_klaviyo_all_reviews( $attributes, $content ) {
    return "<div id='fulfilled-reviews-all' data-id='all'></div>";
}
```

### Add Klaviyo Reviews plugins

1. Navigate to ****Appearance > Editor****.
2. Select ****Templates****.
3. Choose your **Single Product** template. Note that it might have a slightly different name.
4. Click ****+**** to open the block menu.
   ![The + option in the Wordpress visual editor](https://klaviyo.zendesk.com/hc/article_attachments/28722599964955)
5. Navigate to the **Klaviyo** section of the **Blocks** menu.
   ![The Klaviyo section of the Wordpress visual editor blocks menu](https://klaviyo.zendesk.com/hc/article_attachments/28722599969307)
6. Drag and drop Klaviyo Reviews widgets into your theme.
7. Click ****Save****.

### Add the collections star rating widget

1. Navigate to ****Appearance > Editor****.
2. Select ****Templates****.
3. Choose a page that contains a collection of products.
4. Click ****+**** to open the block menu.
   ![The + option in the Wordpress visual editor](https://klaviyo.zendesk.com/hc/article_attachments/28722599964955)
5. Navigate to the **Klaviyo** section of the **Blocks** menu.
6. Drag the ****Star rating**** widget onto any product in the collection.
7. Click ****Save****.

Use the code snippet below to center align the star rating widget, if desired. Note that you must replace the YOUR\_PAGE\_ID placeholder with the page ID for your collection page. Learn how to [find a page ID](https://wordpress.com/support/pages/#find-the-page-id).

```
.page-id-YOUR_PAGE_ID

.klaviyo-star-rating-widget {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin: 0 auto;
}
```

## Install a plugin and add widgets with code

When using this method, widgets are added to your site based on the placement of WooCommerce [visual hooks](https://wordpress.org/plugins/woo-visual-hook-guide/). Therefore, if you don’t have WooCommerce widgets on your product page, you must use an alternate installation option.

This process requires adding a third-party code snippet tool, so you can add code to your site without directly editing your theme files. You can use a tool like [Code Snippets](https://wordpress.org/plugins/code-snippets/) to add the code for these widgets.

### Add reviews widget source code

These instructions assume you have already installed the [Code Snippets](https://wordpress.org/plugins/code-snippets/) plugin, but you can use a different plugin instead.

1. Select ****Snippets > Add new**** from the Wordpress sidebar.
   ![The Snippets menu in the Wordpress sidebar](https://klaviyo.zendesk.com/hc/article_attachments/28722599971739)
2. In the **Enter title here** field, name the snippet something clear, like “Klaviyo Reviews Widgets Code”.
3. In the **Functions (PHP)** tab of the **Code** section, add the code snippets below.
4. Click ****Save Changes and Activate****.

You must install a code snippet for each widget you plan to use. The sections below outline the code for each widget.

### Product reviews widget code snippet

To adjust the location of the widget on your site, edit the location of (`'woocommerce_after_single_product_summary'`) and priority (`15`) in the `add_action` function.

```
function klaviyo_add_product_reviews_widget() {
    global $product;
    if (is_product() && isset($product)) {
        $product_id = $product->get_id();
        echo "<div id='klaviyo-reviews-all' data-id='{$product_id}'></div>";
    }
}
add_action('woocommerce_after_single_product_summary', 'klaviyo_add_product_reviews_widget', 15);
```

### Star rating widget code snippet

To adjust the location of the widget on your site, edit the location of (`'woocommerce_single_product_summary'`) and priority (`6`) in the `add_action` function.

```
function klaviyo_add_product_star_ratings_widget() {
    global $product;
    if (is_product() && isset($product)) {
        $product_id = $product->get_id();
        echo "<div class='klaviyo-star-rating-widget' data-id='{$product_id}'></div>";
    }
}
add_action('woocommerce_single_product_summary', 'klaviyo_add_product_star_ratings_widget', 6);
```

### Additional optional code snippets

Use these code snippets to add optional widgets anywhere on your site. Note that you must add these to the HTML for a specific page; they cannot be added to your functions.php file.

#### SEO widget

`<div id='klaviyo-reviews-all' data-id='all'></div>`

#### Featured reviews carousel widget

`<div id='klaviyo-featured-reviews-carousel'></div>`

## Add short codes

This process involves first registering the short codes in your theme files and then inserting the short codes anywhere on your site.

To complete this, you must first add a third-party code snippet tool so you can add code to your site without directly editing your theme files. You can use a tool like [Code Snippets](https://wordpress.org/plugins/code-snippets/) to add the code for these widgets.

### Register the short codes and add widgets

These instructions assume you have already installed the [Code Snippets](https://wordpress.org/plugins/code-snippets/) plugin, but you can use a different plugin instead.

1. Select ****Snippets > Add new**** from the Wordpress sidebar.
   ![The Snippets menu in the Wordpress sidebar](https://klaviyo.zendesk.com/hc/article_attachments/28722611974171)
2. In the **Enter title here** field, name the snippet something clear, like “Klaviyo Reviews Widgets Code”.
3. In the **Functions (PHP)** tab of the **Code** section, add the code snippets below.
4. Click ****Save Changes and Activate****.
5. Add each widget’s short code to the page where you’d like the widget to appear.

### Code snippets and short codes

### Product Reviews Widget

Code snippet (add to the Functions (PHP) tab):

```
function klaviyo_add_product_reviews_widget() {
    global $product;
	if (isset($product)) {
        $product_id = $product->get_id();
        $tag = "<div id='klaviyo-reviews-all' data-id='{$product_id}'></div>";
		return $tag;
    }
}
add_shortcode('klaviyo-reviews-all', 'klaviyo_add_product_reviews_widget');
```

****Short code:**** [klaviyo-reviews-all]

### Star Rating Widget

Code snippet (add to the Functions (PHP) tab):

```
function klaviyo_add_product_star_ratings_widget() {
    global $product;
    if (isset($product)) {
        $product_id = $product->get_id();
        $tag = "<div class='klaviyo-star-rating-widget' data-id='{$product_id}'></div>";
		return $tag;
    }
}
add_shortcode('klaviyo_star_rating', 'klaviyo_add_product_star_ratings_widget');
```

****Short code:**** [klaviyo\_star\_rating]

Add this short code to your product page to display a single product’s star rating, or any collection page to display star ratings for all items in the collection.

### SEO / All reviews & Featured Carousel Widget

Code snippet (add to the Functions (PHP) tab):

```
function klaviyo_add_featured_reviews_widget() {
    return "<div id='klaviyo-featured-reviews-carousel'></div>";
}
function klaviyo_add_all_reviews_widget() {
    return "<div id='fulfilled-reviews-all' data-id='all'></div>";
}
```

****Short code:**** [klaviyo-featured-reviews-carousel]

****Short code:**** [fulfilled-reviews-all]

## Modify your theme files directly

If you have access to the functions.php file of your Wordpress instance, use the code snippets below to add reviews widgets.

These instructions are for developers with Wordpress PHP experience. If you aren’t familiar with Wordpress PHP, use an alternative method.

### Product reviews widget code snippet

```
// create a function that renders a dynamic div with the correct product ID
function klaviyo_add_product_reviews_widget() {
    global $product;
    if (is_product() && isset($product)) {
        $product_id = $product->get_id();
        echo "<div id='klaviyo-reviews-all' data-id='{$product_id}'></div>";
    }
}
// place the widget after the single product summary
add_action('woocommerce_after_single_product_summary', 'klaviyo_add_product_reviews_widget', 15);
```

### Star rating widget code snippet

```
// create a function that renders a dynamic div with the correct product ID
function klaviyo_add_product_star_ratings_widget() {
    global $product;
    if (is_product() && isset($product)) {
        $product_id = $product->get_id();
        echo "<div class='klaviyo-star-rating-widget' data-id='{$product_id}'></div>";
    }
}
// place the widget after the single product summary
add_action('woocommerce_single_product_summary', 'klaviyo_add_product_star_ratings_widget', 6);
```

### Additional optional code snippets

Add these code snippets to add optional widgets anywhere on your site. Note that you must add these to the HTML for a specific page; they cannot be added to your functions.php file.

#### SEO / All reviews widget

`<div id='klaviyo-reviews-all' data-id='all'></div>`

#### Featured reviews carousel widget

`<div id='klaviyo-featured-reviews-carousel'></div>`

## Outcome

After completing these steps, Klaviyo Reviews widgets will appear on your online store.