<h1>How to use product feeds and recommendations</h1>

Learn how to create a product feed in Klaviyo in order to use product recommendations in your messaging. Product feeds take in data from your product catalog and customer behavior (e.g., the products they’ve viewed or purchased in the past) and use this information to provide custom product recommendations for your subscribers.

Product blocks are only supported in Klaviyo's drag-and-drop and hybrid email editors. To add a product block to a custom HTML email, [create a hybrid email](https://klaviyo.zendesk.com/hc/en-us/articles/115005254188).

![](https://fast.wistia.com/embed/medias/k77fbjpjog/swatch)

## Key terms

- ****Catalog****
  A catalog is a list of your products synced from your ecommerce integration into Klaviyo. View your catalog by clicking ****Content > Products**** in the Klaviyo sidebar.

****Product catalog limits****

- Item limit: 250000
- Product variant limit: 500000
- Category limit: 2500

To request a limit raise, reach out to the [Klaviyo support team](https://help.klaviyo.com/hc/en-us/articles/115001002272).

- ****Custom catalog****
  A custom catalog is any catalog synced to Klaviyo through the [custom catalog process](https://developers.klaviyo.com/en/docs/guide_to_syncing_a_custom_catalog_feed_to_klaviyo) or via API, rather than through a built-in Klaviyo ecommerce integration.
- ****Product feed****
  Product feeds are sets of products selected based on rules you set in Klaviyo. You can choose to include or exclude products from a feed based on category, price, stock level, and how your customers have engaged with your products.
- ****Product block****
  A product block is a type of block used in a Klaviyo email template. When you add a product block to a template, you can choose which product feed it should display products from, or manually select specific products.

## Before you begin

Product feeds do not support OAuth authentication.

Product feeds are available by default for the following ecommerce integrations:

- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-Guide-to-Integrating-with-Shopify)
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808-How-to-Integrate-with-WooCommerce)
- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce)
- Magento [1](https://help.klaviyo.com/hc/en-us/articles/115005082187-How-to-Integrate-with-Magento-1-x-CE-and-EE-) and [2](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-)
- [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360054551492-How-to-Integrate-with-PrestaShop)
- For all PrestaShop integrations created after January 25, 2023, product prices synced to your Klaviyo product catalog via the PrestaShop integration include VAT.
- [Salesforce Commerce Cloud](https://help.klaviyo.com/hc/en-us/articles/360033744951-How-to-Integrate-with-Salesforce-Commerce-Cloud)
- [Spree](https://help.klaviyo.com/hc/en-us/articles/115005255448-How-to-Integrate-with-Spree)
- [Square](https://help.klaviyo.com/hc/en-us/articles/11117215837211)
- [Wix](https://klaviyo.zendesk.com/hc/en-us/articles/6202669053723)
- [Mi9](https://klaviyo.zendesk.com/hc/en-us/articles/360020156011)
- [Salesforce Commerce Cloud](https://help.klaviyo.com/hc/en-us/articles/360033744951)
- [Shift4Shop](https://help.klaviyo.com/hc/en-us/articles/115005083107)

  If you use an ecommerce platform that is not listed above, sync your product catalog into Klaviyo by following our guide on [how to sync a custom catalog feed to Klaviyo](https://developers.klaviyo.com/en/docs/guide_to_syncing_a_custom_catalog_feed_to_klaviyo), or via [API](https://developers.klaviyo.com/en/reference/create_catalog_item).

  The following will not appear in product recommendations:
- Items without associated images
- Items that have already been purchased by the recipient
- Out of stock items
- Items in the flow trigger event for a given email

Recommendations based on viewed products are not available if you have not yet set up **Viewed Product** tracking. Learn [how to set up Viewed Product tracking for your ecommerce store](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Onsite-Tracking#viewed-product-tracking3).

The option to base recommendations on “Products customer has added to cart” is informed by either the **Added to Cart** or **Checkout Started** metric in your account. If you have not set up **Added to Cart** tracking (which is tracked automatically for most ecommerce platforms, but must be manually enabled for [Shopify](https://help.klaviyo.com/hc/en-us/articles/115001396711-How-to-create-an-Added-to-Cart-event-for-Shopify) and [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360024310292-Guide-to-Creating-an-Added-to-Cart-Event-for-BigCommerce)) those recommendations will only rely on **Checkout Started**.

## Configure a product feed

1. In Klaviyo, select ****Content**** in the left hand menu.
2. In the dropdown, click ****Products****.
3. Select the ****Product feed**** tab, then click ****Create Product Feed****.
4. Name your feed.
5. If you have more than one catalog in your Klaviyo account, select the catalog you intend to use. If you only have one catalog, you will not see this option.
6. Under **What products should the customers view first?**, select an option from the dropdown. You can choose an option that is **Classic** or **Personalized for each customer**. Note that **Products a customer has recently viewed** and **Products a customer has added to cart** will look at the last 90 days.
   ![Personalized product feeds](https://klaviyo.zendesk.com/hc/article_attachments/25803026546459)
7. Depending on what option you select, you may be prompted to choose an additional filter. For instance, **Product customers may also like** can be informed by a number of metrics, such as a customer’s view or purchase history. For some other options (such as **Best-selling products**) you can choose the timeframe to be over the last 3 days or over the last 90 days.
8. If you selected an option under **Personalized for each customer**, you’ll be prompted with an additional question: If the customer has limited history, what should they view instead? Choose an option from the dropdown for this default. Note that these defaults are across all customers and are not personalized.
   ![Dropdown labeled If the customer has limited history, what should they view instead? with Classic options such as Best-selling items](https://klaviyo.zendesk.com/hc/article_attachments/9038637974683)
9. Optionally, select filters under **What additional filters would you like to apply?**

   - You can filter based on **category includes** or **category excludes**. When selecting **category includes** or **category excludes**, you can select one or multiple categories for the input. When selecting either option, you can also choose whether to match **any of** or **all of** the selected categories.
     - **Any of** means items that match **at least one** of the selected categories will be included or excluded (an **OR** condition).
     - **All of** means items that match **every** selected category will be included or excluded (an **AND** condition).
   - You can select one or multiple categories for each filter input. When multiple categories are selected and **any of** is chosen, any item belonging to at least one of the selected categories will be included. When **all of** is selected, only items that belong to all selected categories will be included.
     In the **includes** and **all of** example below, any item in both the Tshirts and Grey category will be included.

     In the **excludes** and **any of** example below, if an item is either a Tshirt or Grey, it will be excluded. For example, both grey pants and red tshirts would be excluded, but red pants would be included.
     ![Screenshot 2025-10-09 at 2.35.18 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/41949116242843)
     ![Screenshot 2025-10-09 at 2.41.04 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/41949116246299)
   - You can filter based on **stock level** and set a minimum and maximum. For both **stock level** and **price** you can leave either the minimum or the maximum blank (indicating a minimum of 0 or no maximum, respectively) but you must set either the minimum or maximum.
   - You can filter based on **price** and set a minimum and maximum.
   - You can add multiple filters by clicking ****Add filter**** and making another selection.
10. When you’re finished configuring your feed, click ****Save Product Feed****.
11. You will be prompted to name your feed. Use a name that is descriptive, contains no spaces or special characters, and does not begin with an underscore (\_).
12. Click ****Save Product Feed****.

## Use a product feed in an email

1. Open an email in Klaviyo (i.e., an email template, unsent campaign, or flow email).
2. Drag a **Product** block into your email.
   ![A product block](https://klaviyo.zendesk.com/hc/article_attachments/16744753461019)
3. Leave the content type set to **Dynamic** (which is the default setting).
4. From the **Product feed** menu, choose a product feed.
   ![A product block with a product feed selected in the email template editor](https://klaviyo.zendesk.com/hc/article_attachments/12125647454491)
5. Choose which product details to display. Options include the item’s title, item’s price, and a customizable button. If all of these options are toggled off, each product’s image will appear without accompanying text. For more details on all available settings, check out our article [How to insert a product block.](https://help.klaviyo.com/hc/en-us/articles/115000219092-How-to-insert-a-product-block)
6. Choose how many products should appear under **Layout** by selecting a number of rows and a number of items per row. Multiply the number of rows by the number of items per row to calculate how many products will appear (e.g., 2 rows with 3 items per row will display 6 items, 1 row with 1 item per row will display 1 item).
7. Adjust any other color, font, and style settings as desired, then click ****Done****.
8. Click ****Preview and Test**** to see a preview of your message with products from your catalog. If you aren’t seeing the results you expect, head to the FAQs section below for troubleshooting help.

You can select any existing product feed or create a new one from within the template editor. To make edits to an existing product feed, navigate to ****Content > Products > Manage Product Feeds****, then select a feed and edit it.

## Product feed use cases

Below are examples of how you can use a product feed in your emails.

### Product feed above footer

Consider including a small product feed (e.g., 1 row with 3 items) at the end of your email content. These recommendations can serve as a final opportunity for a recipient to click through to your website if they’ve read to the bottom of your email and still haven’t converted. Use a feed based on products a customer may also like, or a feed of your most popular products.

![Product recommendations in an email footer](https://klaviyo.zendesk.com/hc/article_attachments/12041842908699)

### Browse abandonment flow email

Use a product feed based on the items someone has recently viewed in your browse abandonment flow. This can encourage casual site visitors to return and complete an order they were considering previously. Learn how to [insert recently viewed items into an email](https://help.klaviyo.com/hc/en-us/articles/360019921772-How-to-insert-recently-viewed-items-into-an-email).

### Welcome email featuring bestsellers

Consider adding a product feed with your best-selling products to your welcome flow. This can help introduce new subscribers to the products your customers love the most. Because you’re using a dynamic feed (rather than manually inserting products), the items shown will automatically update throughout the year based on stock levels and customer trends.

## FAQs

****My feed is set to be personalized for each customer. Why is my product block showing the same product to all recipients?****

When dynamic recommendations aren’t available, Klaviyo falls back to the secondary recommender you’ve selected (i.e., best-selling or most viewed products). This can happen when:

- An email recipient doesn’t have enough data for us to provide personalized recommendations.
- The feed was created recently, and hasn’t yet been fully trained. It typically takes 2 days to a week for Klaviyo’s systems to train the model.
- Your **Viewed product** or **Ordered product** events are very recent. Your product feed recommendation models are generally trained once every 2-7 days, depending on use. It may take a few days for the recommendation model to consider brand-new events.

****What integrations support the price and inventory filters?****

We support price and inventory filters for the following integrations:

- Shopify
- BigCommerce
- Magento 2

Price and inventory filters are available for variants in custom catalogs as well.

****How does the “Newest products” recommender work? What date does it use to sort products?****

We use a “created\_at” timestamp that is specific to Klaviyo. This means that when you first sync your catalog, every product in the catalog will have the same “created\_at” value, so the newest products recommender will not be useful at first. Once you’ve added some new items to your catalog after the initial sync, you should start to see the expected behavior.

This also means that items will not be prioritized by the recommender just because they’ve been “updated” or have recently come back in stock. This recommender will only prioritize net new products added to your catalog.

****I applied a price or inventory filter, but I see an item in the product block that is outside the range I specified. Why is this?****

Filters apply to variants, but product blocks render items. If the sum of the inventory for all variants of a product is above the threshold of the filter, it is eligible to show within a product block. Items have default images and prices, so it’s possible an item will show an image and price of a variant that doesn’t exactly match the price or inventory filter.

****What currency do the price filters use?****

It depends on how the item was configured in your ecommerce platform. Klaviyo will use whatever currency value the catalog uses.

****Where are web feeds?****

If you are looking to set up a web feed (instead of a product feed), click your account name in the lower left corner, then navigate to ****Settings > Other >********Web Feeds****. From here, you can add a new web feed.

****What happened to “trending?”****

The "trending" option is now expressed as a look back window of "3 days." Any option that uses "over the past 3 days" will be a version of the old "Trending" order.

****I’m using some custom statistics to power product recommendations. Will these be compatible with the new experience?****

Yes. For details, please refer to our developer portal article, [Sync a custom catalog feed to Klaviyo](https://developers.klaviyo.com/en/docs/guide_to_syncing_a_custom_catalog_feed_to_klaviyo).

****How does the “Recently viewed” recommender work?****

We use a model that weighs both recency and frequency of views to order the products. This means that if a customer viewed a product 5 times yesterday, and a different product once today, we may still prioritize the product they viewed 5 times because we take view frequency into account.

****How is "Best-selling" calculated?****

Best-selling products are identified based on the number sold, with more weight given to more recent purchases. An item's purchase price is not taken into consideration when identifying best-selling products.

****How are "Products a customer may also like" determined?****

"Products a customer may also like" uses AI to recommend exactly the right product in your emails. Klaviyo uses collaborative filtering to predict what a recipient is likely to buy next, based on what they have ordered in the past and how they're similar to other customers. While the model may include products someone has viewed, it doesn't exclusively show these products. The model takes a look at the behavior of other customers in your account - for instance, if Klaviyo sees customers have commonly viewed products A, B, and C together, and a given customer has only viewed A and B, then we'll show them product C.
