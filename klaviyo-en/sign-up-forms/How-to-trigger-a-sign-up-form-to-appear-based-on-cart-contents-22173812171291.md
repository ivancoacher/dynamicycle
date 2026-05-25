---
id: "22173812171291"
title: "How to trigger a sign-up form to appear based on cart contents"
source_url: "https://help.klaviyo.com/hc/en-us/articles/22173812171291-How-to-trigger-a-sign-up-form-to-appear-based-on-cart-contents"
section: "Build and use forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:33Z"
language: "en"
---
## You will learn

Learn how to trigger a sign-up form to appear when a shopper’s cart meets certain attributes. You can show the form based on total cart value, number of items in cart, or specific product criteria to target highly engaged shoppers on your site and encourage purchases.

****Alternative use cases for triggering forms based on cart contents****

Triggering a sign-up form to appear based on specific cart attributes provides an opportunity to cross-sell or upsell shoppers. For example:

- Promote another product or bundle when a shopper adds a certain product to their cart.
- Promote upgrade options for shoppers who add specific products to their cart (e.g., a newer model or larger size).
- Tease a discount when a shopper's total cart value is lower than a certain amount to encourage increased average order values (e.g., "You're $20 away from 25% off").
- Offer a "surprise" discount, free product, or free shipping when total cart value exceeds a certain amount. This offer wouldn't be advertised on your site so it feels unexpected.
- Target customers that have a high-ticket item in their cart or a high-ticket cart value with a reminder of your installation payment options.
- If you're a clothing or accessory brand, show a reminder about your size guides or alternative stying ideas based on the product or category that a shopper adds to their cart.

## Target a form based on cart contents

Targeting a sign-up form by cart contents is currently available for Shopify users only; however it is not supported if you are adding items to the cart using Shopify's GraphQL API. Use the [AJAX API](https://shopify.dev/docs/api/ajax/reference/cart) to ensure support.

If you have not already done so, [integrate your Shopify store](https://help.klaviyo.com/hc/en-us/articles/115005080407).

1. Select ****Sign-up forms**** from the left-hand navigation.
2. Create a new sign-up form, or choose an existing form by selecting the ****3 dots > Edit form**** next to the one you’d like to set the trigger on.


   ![Clicking the 3dots followed by Edit form next to an example sign-up form on the Sign-up forms tab.](https://fast.wistia.com/embed/medias/ab7vh5o1hd/swatch)
3. Make any edits to the [content and styles](https://help.klaviyo.com/hc/en-us/articles/360026474752#h_01HAAJKYJ2G0D4XR17NQ0EN7RX) so your sign-up form fits your goal (e.g., add a coupon block if you plan on offering a discount code to shoppers with certain cart attributes).
4. Select the ****Targeting & behaviors**** tab.
   ![The Targeting & behaviors tab being selected within the form editor.](https://klaviyo.zendesk.com/hc/article_attachments/28722611611163)
5. ****Toggle to the Targeting**** menu and scroll down to **Cart contents**.
   ![The Cart contents section of the Targeting tab highlighted in the form editor.](https://klaviyo.zendesk.com/hc/article_attachments/28722611607963)
6. From here, choose what cart attributes will trigger the sign-up form to appear. Check 1 or more of the following options:
   - ****Show based on total cart value****
     Select a comparison operator (i.e., **is greater than**, **is less than**, **equals**) and input a currency value. The currency value will automatically match the currency type set for your Shopify store (e.g., USD). For example, if the definition is ****Show based on total cart value > greater than > 100**** for a store set to USD, then the sign-up form will appear when a shopper has a cart value of any number higher than $100.

     If you use **Equals** as a qualifying option, the shopper must meet the exact value criteria set in order for the sign-up form to show (e.g., have a cart value of exactly $100). Because cart value will likely be less exact, we suggest using **is greater than** or **is less than** operators here.
   - ****Show based on total number of items in cart****Select a comparison operator and input a certain number of items. For example, if the definition is set to ****Show based on total number of items in cart > equals > 3****, then the sign-up form will show when a shopper’s cart has 3 items in it.
   - ****Show based on product in cart****
     Select a comparison operator and input a corresponding value. For any of these options, the sign-up form will show when the products in a shopper’s cart meet your specified criteria. You can show the form based on:
     - ****Brand****The specific vendor from which the product is sold (e.g., Beantown Coffee).
     - ****Category****The product type (e.g., mugs). Note that this cannot be a user defined category, such as a special collection name.
     - ****Name****The unique name of a product (e.g., Beantown holiday mug). Note that the name entered must exactly match the product's name.
     - ****Price****The price of a product (e.g., 10). Do not include a currency symbol.
     - ****ProductID****The unique ID of a product (e.g., 123456789).

       If you select multiple options for targeting by cart contents, Klaviyo will use OR logic to determine when the form should trigger. For example, if you choose to ****Show based on cart value > is greater than > 10**** and ****Show based on total number of items in cart > equals > 3****, then the sign-up form will appear when any 1 of those conditions is satisfied.
7. When you’re satisfied with your sign-up form, click ****Publish****.

Your sign-up form will now appear when a shopper meets the cart attributes that you set.

## Next steps

To test that your form is targeting shoppers as expected, open an incognito browser and take the necessary actions to meet your configured cart contents trigger.

Keep in mind that your cart contents trigger settings will use AND logic with any other [display or targeting settings](https://help.klaviyo.com/hc/en-us/articles/4413544555547) for the form. For example, if the form is set to show after 10 seconds, and also when total cart value is greater than 100, then the sign-up form will show after both of those conditions are satisfied.

## Additional resources

- [How to create an abandoned cart flow](https://help.klaviyo.com/hc/en-us/articles/115002779411)
- [Understanding targeting & behavior settings for a sign-up form](https://help.klaviyo.com/hc/en-us/articles/4413544555547)
- [Course: Create strategic sign-up forms](https://academy.klaviyo.com/create-strategic-sign-up-forms)