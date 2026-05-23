---
id: 33660482389659
title: "How to style your Customer Hub"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/33660482389659-How-to-style-your-Customer-Hub"
section: "Build and use Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:39Z"
language: en
---

## You will learn

Learn about design options for styling your Customer Hub drawer, and how you can design it to match your brand. Because the Customer Hub interface is ingrained in the customer experience, it’s best practice to style it to appear as an extension of your website.

Customer Hub currently supports Shopify storefronts, including Shopify Headless. Additional eCommerce platform support is planned.

For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

## Before you begin

This guide explains how to customize the style of your Customer Hub interface. Before proceeding, [ensure that the Customer Hub feature is enabled](https://klaviyo.com/try-service).

[Learn more about Customer Hub](https://help.klaviyo.com/hc/en-us/articles/33660324811675).

## Customer Hub design options

The Customer Hub drawer has multiple customizable tabs:

- **For you**
- **Orders**
- **Profile**
- **Chat** (only visible when web chat is enabled)

![Cutomer Hub.png](https://klaviyo.zendesk.com/hc/article_attachments/42778703530011)

You have various options for customizing the design across each of these tabs, including editing text, colors, fonts, and more. Style customization selections cascade across each tab in the Customer Hub drawer to ensure a consistent, on-brand experience for your site visitors.

While the appearance of most elements in Customer Hub drawer can be adjusted, their positions cannot. Only general layout options are currently available.

As you edit the design settings for your Customer Hub in Klaviyo, use the ****View live**** button to see the changes made to the hub interface on your website. Note that if your Customer Hub is live, saved changes are published to your site.

## Customize a main call to action for each tab

By default, when a shopper signs into their customer account, Klaviyo displays “Welcome, first.name” as the main heading on the **For you** tab of the Customer Hub drawer. This text is not editable.

For unauthenticated shoppers, however, you can write your own call-to-action heading to display above the “Sign in” button before they log in. This can be helpful for incentivizing unauthenticated visitors to sign in and engage with your Customer Hub interface.

In the example below, the main call to action reads “Earn rewards, track orders, and save your shopping history.”

![Screenshot 2025-10-30 at 10.49.04 AM.png](https://klaviyo.zendesk.com/hc/article_attachments/42778703532315)

****Note****: the "rewards available" indicator shows automatically if you have either:

1. A [static coupon](https://klaviyo.zendesk.com/hc/en-us/articles/39273771656987) set up within Customer Hub, OR
2. If you have a loyalty integration enabled (such as [Smile](https://klaviyo.zendesk.com/hc/en-us/articles/36271755028507)).

   To update the **Main call to action** for your Customer Hub interface:
3. Open ****Service -********Customer Hub**** tab in Klaviyo’s left-hand navigation.
4. Click ****Settings****.
5. Under **Welcome messages**, customize a call to action to display above the "sign in" button for unauthenticated shoppers. You can do this for each tab of the Customer Hub drawer:

   - **For you**
   - **Orders**
   - **Profile**![The Welcome messages menu in Customer Hub Content settings.](https://klaviyo.zendesk.com/hc/article_attachments/36252136471707)
6. Click ****Save****.

## Design your Customer Hub

For design options to customize your Customer Hub interface:

1. Navigate to ****Customer Hub**** in Klaviyo's left-hand navigation.
2. Select ****Design****.
3. Select ****Hub**** at the top of the preview.


   ![Screenshot 2025-10-30 at 10.27.45 AM.png](https://klaviyo.zendesk.com/hc/article_attachments/42778709623963)
4. From the **Style** menu you can adjust Display Language, Fonts, Color and Style settings and preview how these adjustments will look in the Customer Hub interface canvas
5. You can optionally apply advanced styling with Custom CSS. See the [Custom CSS section](https://help.klaviyo.com/hc/en-us/articles/33660482389659#h_01JMFRS7N5CXGMQB6F2C3HAZVB) below for more details.
6. See the [Language and locale support in Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/41537373957787) article for more information on selecting another language.
7. Click ****Save**** to set your changes live.

## Customize the Customer Hub widget

Aside from designing Customer Hub itself, you can also customize the hub widget, which is a small, floating element on your website that visitors can click to quickly open Customer Hub interface. The widget presents timely information to your shopper such as incoming chat messages and feedback when adding items to their Favorites list. We recommend enabling the widget UI to drive meaningful engagement with customers, especially when Web Chat and Favorites are enabled.

To customize the hub widget:

1. Select ****Customer Hub**** in Klaviyo's left-hand navigation.
2. Select ****Design****.
3. Select ****Widget**** at the top of the preview.
   ![Screenshot 2025-10-31 at 12.41.54 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/42823654668827)
4. From the **General** menu you can adjust which shoppers should see the widget and which Customer Hub View should open when the widget is clicked.

   - Choose which shoppers should see the widget on your site:
     - ****All shoppers (recognized, logged in and logged out) –**** The widget appears for everyone.
     - ****Recognized or logged in shoppers –**** The widget only appears if Klaviyo recognizes the person (Identified) or if they are logged in (Authenticated). This is ideal for reducing clutter for brand-new visitors while maintaining a high-touch experience for returning ones.
     - ****Logged in shoppers only –**** The widget only appears for those with an active Shopify session.
5. From the **Style** menu you can adjust Color and Style settings and preview how these adjustments will look in the Customer Hub Widget interface canvas
6. From the **Layout** menu you can adjust how the widget is positioned on your website.
7. Click ****Save**** to set your changes live.

## Customize Additional Widget States

You can customize additional widget states by selecting the caret next to ****Icon**** and navigating to another widget state.

- The **Add to Cart** state is visible on product detail pages. The customizable widget encourages shoppers to make a purchase or save a product for later when they have scrolled below the top of the Product Detail Page when the traditional Add to Cart button is no longer visible. Learn more about [How to set up the Add to Cart Widget in Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/42782506830107).

## Custom CSS for Customer Hub

If your branding needs aren’t met by the Customer Hub design options, you can apply advanced styling with Custom CSS.

While Customer Hub uses CSS resets to avoid collision with your site’s CSS, you may need to add custom CSS to address edge cases or apply unique styling, such as floating drawer or custom border radius values.

Implementing custom CSS for your Customer Hub involves editing your site’s code. This is only recommended for technically savvy marketers or those who have access to a developer. While our product does support custom CSS, our support team cannot help you add custom CSS to Customer Hub beyond the general guidance covered in this documentation. To maintain the security of your data, Klaviyo's support team is not able to open your HTML files.

### Apply custom CSS

Add any custom CSS directly to the **Custom CSS** section of the in your Customer Hub design settings, and make sure to save your changes.

![The Custom CSS section at the bottom of the Customer Hub Design settings menu in Klaviyo.](https://klaviyo.zendesk.com/hc/article_attachments/34192092471579)

All basic elements within the Customer Hub have class names prefixed with `kl-hub-`:

- All text elements have the class `kl-hub-text`, while headings have the class `kl-hub-heading`
- Buttons have the class `kl-hub-button`, and also include their variants (e.g., `kl-hub-button-primary`, `kl-hub-button-secondary`, etc.)
- The Customer Hub drawer itself has the class `kl-hub-drawer`
- Text inputs have the class `kl-hub-input`
- All content blocks have the class `kl-hub-content-block`, and also include their block **Internal name** (e.g., `kl-hub-content-block-reward-program` for a content block named "Reward program")

This is not an exhaustive list; you can find more by inspecting the Customer Hub with your browser’s debugger. If an element has a class that starts with `kl-hub-`, it’s safe to use for custom CSS.

### CSS example

If you wanted to make all buttons and headings in the Customer Hub uppercase, you could write the following custom CSS:

```
.kl-hub-button, .kl-hub-heading {

    text-transform: uppercase;
}
```