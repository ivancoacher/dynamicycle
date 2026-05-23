<h1>Understanding variant support for reviews</h1>

## You will learn

Learn about variant support for Klaviyo Reviews, which allows product variants to be stored and displayed in addition to titles. Variant support is enabled by default, but you must update a setting if you want variants to appear in your review widgets.

## Use cases for displaying variants

When variant support is enabled, Klaviyo will track which version of a product was reviewed, and you have the option to display that information to site visitors. Use this feature when variant-level information is relevant to the content of a review. Note that variants can only be tracked and displayed for verified reviews.

Displaying variant support might be useful for:

- ****Cosmetics****
  Reviewers will likely comment on the shade of a lip gloss or blush, which is generally stored at the variant level.
- ****Flavored items****
  Reviewers may have opinions on the taste of various flavors, and purchasers want to know which flavor to buy.
- ****Clothing****
  Reviewers often want to understand how a garment will fit them, and seeing reviews from others who wear their size can help them decide whether a piece is right for them.

When choosing whether to display variants in your widgets, ask yourself: do the variants I offer differ in functionality? Variant details are likely not important for items where the only difference between variants is size (e.g., king versus queen mattresses, different sized containers of sunscreen, etc.) or color/pattern (e.g., different colored t-shirts or umbrellas). Consider what your customers want to know when deciding whether to make a purchase from you.

## How to disable variant support

Variant support is enabled by default. If you’d like to disable this feature (i.e., stop tracking variants as part of review metadata):

1. Navigate to ****Reviews**** in Klaviyo.
2. Click ****Reviews settings****.
3. Select ****General****.
4. In the **Variants** section, turn off the setting **Enable product variant support**.
   ![The option to enable or disable variant support](https://klaviyo.zendesk.com/hc/article_attachments/28711732299547)
5. Select ****Save changes****.

When you disable this feature, new review requests will not include variant information in these locations:

- The review request email
- The moderation page within Klaviyo
- Review widgets

  If you’d like to hide variant details in your review request email, without disabling variant support entirely, use the variable {{ event.structured\_product.product\_name }} alone in your flow. By default, your flow messages use one of the variables below, both of which include variant information:
- {{ event.structured\_product.title }}
- {{ event.structured\_product.product\_name }} – {{ event.structured\_product.variant\_name }}

## How to display variant information in reviews widgets

You can add variant information to reviews widgets, so each review lists which variant was purchased. Variant support is enabled by default, but displaying variant information in reviews widgets is off by default.

1. Navigate to ****Reviews**** in Klaviyo.
2. Click ****Reviews settings****.
3. Select ****General****.
4. In the **Variants** section, check ****Display on review collection**** and/or ****Display on onsite widgets****.
   ![Variant support widget settings](https://klaviyo.zendesk.com/hc/article_attachments/28711732303643)
5. Select ****Save changes****.

If you check the option to ****Display on review collection****, reviewers will see the variant they purchased directly under the item name while leaving a review.

If you check the option to ****Display on onsite widgets****, the variant name will appear within each review card in the **Product reviews** widget and **SEO / All reviews** widget. It is not possible to display variants for one widget but not the other.

Klaviyo only collects variant information when a review is submitted in response to a review request. Reviews submitted by navigating to a product page and manually clicking the ****Write a review**** button will not include variant information.

## Understanding account differences when variant support is disabled

The variant support setting does not apply retroactively to event metadata. Any reviews activity while the setting is off will not contain variant information; any reviews activity while the setting is on will include variant information.

When variant support is enabled, you’ll see variant information in these locations:

- ****The metadata for reviews events****
  The **title** field (nested within **structured\_product**) will contain the product title and variant title, separated by an em dash (e.g., Vintage wash t-shirt – Charcoal heather). Your event metadata will also include **variant\_name**.
- ****The**** ******All reviews****** ****tab and**** ******Review details****** ****page of your Klaviyo admin****
  When reviewing and moderating reviews, you’ll be able to see which variant a reviewer purchased for verified reviews.
