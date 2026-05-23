<h1>How to add Klaviyo Reviews widgets to your mobile app using Tapcart</h1>

## You will learn

Learn how to add Klaviyo Reviews widgets to a mobile app built with Tapcart. These widgets can be added to your Tapcart app using custom blocks:

- ****Star rating widget****
  Product pages only; show a product’s overall star rating
- ****Product reviews widget****
  Product pages only; show a summary and list of all reviews for a product, plus buttons to ask a question or leave a review
- ****Featured reviews carousel widget****
  Any page; show a selection of featured reviews across several products

Tapcart is only available for stores built with Shopify.

## Before you begin

This process is only available to companies who:

- Have already built a mobile app with Tapcart
- Use a Tapcart Enterprise plan
- Have an active Klaviyo Reviews plan

If you haven’t set up Klaviyo Reviews yet, head to our article on [getting started with Klaviyo Reviews](https://help.klaviyo.com/hc/en-us/articles/15937542819355).

## Add Klaviyo Reviews widgets using a custom block in Tapcart

Follow these steps to add any reviews widget in Tapcart. You’ll need to repeat these steps (i.e., create a separate custom block) for all 3 widgets.

1. Open the Tapcart editor.
2. In **App Studio**, switch from **Design Blocks** to ****Custom Blocks****.
   ![launch blocks editor](https://klaviyo.zendesk.com/hc/article_attachments/28723685323035)
3. Click ****Launch Blocks Editor**** to create a new custom block.
4. Name the widget something clear, like **Klaviyo Star Rating custom block**.
5. In the ****JS**** tab of the block editor, add the following code snippet. Replace PUBLIC\_API\_KEY with your [6-character Klaviyo site ID](https://help.klaviyo.com/hc/en-us/articles/115005062267).

   ```
   var script = document.createElement('script');
   script.type = 'text/javascript';
   script.async = true;
   script.src = 'https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js&module=reviews';
   document.head.appendChild(script);
   ```
6. In the ****HTML**** tab of the block editor, paste the snippet for the widget you’d like to add (e.g., the star rating widget). Find the code snippets below:
   1. [Star rating widget code](https://klaviyo.zendesk.com/hc/en-us/articles/undefined#h_01HNDJ2XVMJGSX6T4QKBBDDBZ2)
   2. [Product reviews widget code](https://klaviyo.zendesk.com/hc/en-us/articles/undefined#h_01HNDJ2XVMZEZKE2MH9KF46K6M)
   3. [Featured reviews carousel widget code](https://klaviyo.zendesk.com/hc/en-us/articles/undefined#h_01HNDJ2XVMV6D8422M9NF6BSS4)
      ![Tapcart HTML tab](https://klaviyo.zendesk.com/hc/article_attachments/28723663126811)
7. Click ****Save****.
8. Click ****Close**** to exit the editor.
9. From the ****App Studio**** dropdown, select ****Product detail****.

   ![product detail page](https://klaviyo.zendesk.com/hc/article_attachments/28723663130907)

   This step is required for the star rating and product reviews widgets. You can place the featured review widget on any app page.
10. Drag the saved custom block you just created into your template.
11. The editor may not load the widget directly; instead, you’ll see the block name as plain text. This is expected.
12. Click ****Preview your app**** and navigate to the page where you added your app. Note that the widget appears correctly.

The ****Ask a question**** and ****Leave a review**** buttons will not work in preview mode. Once you publish the changes to your app, clicking these buttons in the app will open a new browser tab.

## Code snippets

### Star rating widget

```
<div class="klaviyo-star-rating-widget" data-id="{{product.id}}" data-product-title="{{product.title}}" data-product-type="{{product.type}}"></div>
```

### Product reviews widget

```
<div id="klaviyo-reviews-all" data-id="{{product.id}}"></div>
```

### Featured reviews carousel

```
<div id="klaviyo-featured-reviews-carousel"></div>
```

## Preview app widgets

The Klaviyo Reviews widgets won't automatically appear in the Tapcart preview, but will load correctly on your app. This is because the widgets require a real product ID in order to know which reviews to display. To preview the widgets, add a product ID variable in the **Variable Preview Values** field in the Tapcart editor.

1. In the Tapcart **App Studio**, select ****Custom**** to view your custom widgets.
2. Click the three dots icon next to one of your review widget blocks and click ****Launch Editor****.
3. Click ****Settings****.
   ![The settings button](https://klaviyo.zendesk.com/hc/article_attachments/28723663139099)
4. Scroll or search through the JSON to find the **id** variable within the **product** object. Note that there are other **id** variables within other objects; you only need to edit the product ID shown here.
   ![The product ID variable within the code](https://klaviyo.zendesk.com/hc/article_attachments/28723663133979)
5. Replace the sample product ID with the ID for a product in your store that has at least 1 review. To find a product ID, navigate to ****Content > Products**** in Klaviyo, then copy an item ID.
   ![An item ID in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28723663136667)
6. Click ****Save****.
7. Repeat these steps for your other review widget blocks.
8. If the previews don't appear correctly right away, refresh the editor.

## Style app widgets

Any changes made in the main widget editor will apply to both your website and your app. To apply changes to just your app, add custom CSS to the ****CSS**** tab of the custom block editor in Tapcart. Learn how to use custom CSS to style Klaviyo Reviews widgets.
