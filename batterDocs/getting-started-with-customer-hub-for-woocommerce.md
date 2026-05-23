<h1>Getting started with Customer Hub for WooCommerce</h1>

# Getting started with Customer Hub for WooCommerce

**Estimated 10 minute read**

## Table of contents

- [About Customer Hub](https://www.google.com/search?q=%23about-customer-hub)
- [Before you begin](https://www.google.com/search?q=%23before-you-begin)
- [1. Enable Customer Hub](https://www.google.com/search?q=%231-enable-customer-hub)
- [2. Connect your WooCommerce store](https://www.google.com/search?q=%232-connect-your-woocommerce-store)
- [3. Update your account page link](https://www.google.com/search?q=%233-update-your-account-page-link)
- [4. Enable extensions to tailor the shopping experience](https://www.google.com/search?q=%234-enable-extensions-to-tailor-the-shopping-experience)
- [5. Link your privacy policy and terms of service](https://www.google.com/search?q=%235-link-your-privacy-policy-and-terms-of-service)
- [6. Set Customer Hub live](https://www.google.com/search?q=%236-set-customer-hub-live)
- [7. Analyze your performance](https://www.google.com/search?q=%237-analyze-your-performance)
- [Frequently asked questions](https://www.google.com/search?q=%23frequently-asked-questions)
- [Additional resources](https://www.google.com/search?q=%23additional-resources)

---

## About Customer Hub

Customer Hub is the one place for your customers to manage their relationship with your brand. It consolidates traditional account functionality with personalized shopping experiences—such as saving products to favorites, surfacing unique coupons, and showing product recommendations. Customer Hub drives revenue and reduces support burden by bringing everything into one place, increasing engagement with your most valuable marketing tools, including loyalty programs, subscriptions, and more.

Customer Hub supports WooCommerce storefronts via the WooCommerce extension. Because WooCommerce does not use Klaviyo's native Shopify app, setup requires a few additional steps compared to Shopify—specifically, connecting your store credentials and redirecting your account page link.

> ****Note:**** For feedback about Customer Hub functionality, email customerhub@klaviyo.com.

---

## Before you begin

Before setting up Customer Hub for WooCommerce, confirm that:

- You have an active WooCommerce store integrated with Klaviyo.
- You have access to your WooCommerce ****Consumer key**** and ****Consumer secret**** (generated from your WooCommerce REST API settings).
- You have admin access to both your Klaviyo account and your WooCommerce store.

---

## 1. Enable Customer Hub

1. Navigate to the ****Customer Hub**** tab under ****Service**** in Klaviyo's main navigation.
2. Click ****Get started**** to begin your free trial and onboarding process.

In the guided workflow that follows, you will:

- Customize the design and branding of your Customer Hub.
- Customize your on-site widget to help shoppers discover your Hub.
- Add personalized content to your Hub from a library of pre-built content blocks, including partner-built blocks that display dynamic data such as loyalty points and subscription statuses.
- Target shoppers based on three distinct authentication states:

| ****Authentication state**** | ****Description**** |
| --- | --- |
| ****Logged out**** | New visitors with no tracking history |
| ****Recognized**** | Returning shoppers identified via a `_kx` token but not yet logged in |
| ****Logged in**** | Shoppers who have fully authenticated into their account |

After completing the onboarding workflow, you will land on the Customer Hub dashboard. ****Do not set Customer Hub live yet****—complete steps 2 and 3 first to ensure your WooCommerce store is properly connected.

---

## 2. Connect your WooCommerce store

Because Customer Hub connects to your store data through the WooCommerce REST API, you must provide your store credentials before going live. This allows Customer Hub to display order history, customer profiles, and other store data within the Hub experience.

### Generate your WooCommerce API credentials

1. In your WordPress admin panel, navigate to ****WooCommerce > Settings > Advanced > REST API****.
2. Click ****Add key****.
3. Set the Permissions to ****Read/Write**** and assign a descriptive name (e.g., "Klaviyo Customer Hub").
4. Click ****Generate API key****.
5. Copy your ****Consumer key**** and ****Consumer secret****—these will only be shown once.

> ****Important:**** Store your Consumer key and Consumer secret securely before leaving this page. WooCommerce will not display the Consumer secret again after you navigate away.

### Add your credentials to Klaviyo

1. In Klaviyo, navigate to ****Customer Hub > Extensions****.
2. Click on the ****Extension settings**** tab.
3. Under the WooCommerce section, enter:

   - ****Store URL domain**** — your store's base domain (e.g., `example.com`)
   - ****Consumer key**** — the key generated in WooCommerce
   - ****Consumer secret**** — the secret generated in WooCommerce
4. Click ****Save****.

Once saved, Klaviyo will use these credentials to fetch order and customer data from your WooCommerce store and surface it within Customer Hub.

---

## 3. Update your account page link

Unlike Shopify, WooCommerce does not automatically redirect your `/my-account` page to open Customer Hub. You must manually update the account page link on your site so that it points to the Customer Hub experience.

### How Customer Hub is triggered

Customer Hub opens when a shopper navigates to a URL ending in `#k-hub`. To replace the default WooCommerce account experience with Customer Hub, update any links on your site that point to your `/my-account` page so that they redirect to:

`https://your-store-domain.com/#k-hub`

### Where to update account links

Common locations to update include:

- ****Navigation menus**** — the "My Account" or "Log In" link in your site's header or footer.
- ****Theme templates**** — any hardcoded links to `/my-account` in your theme files.
- ****Widgets or shortcodes**** — any WooCommerce account widgets embedded in sidebars or page templates.

> ****Tip:**** You can use your theme's customizer, a page builder, or edit template files directly to update these links. If you're unsure where account links appear on your site, search your theme files for references to `/my-account`.

### Preserving the default WooCommerce account experience for specific links

If you have a link that should open the standard WooCommerce account page directly instead of Customer Hub, add the `data-k-hub-ignore` attribute to that link:

HTML

```
<a href="/my-account" data-k-hub-ignore>View my account</a>
```

This tells Customer Hub to skip that specific link and allow the default behavior.

---

## 4. Enable extensions to tailor the shopping experience

Extensions are additional features that drive greater engagement and revenue via Customer Hub. Open the ****Extensions**** menu to enable the following:

- ****Product recommendations**** — surface personalized product recommendations based on Klaviyo's AI.
- ****Favorites**** — give shoppers the ability to save products and display them in Customer Hub.
- ****Coupons**** — surface unique and static coupons to shoppers, including segment-targeting, to drive more conversions.
- ****FAQs**** — create a list of commonly asked questions to display in the Chat tab before shoppers initiate a conversation.
- ****Web chat**** — add the Chat tab and allow shoppers to chat with Klaviyo's Customer Agent and/or human agents via Klaviyo Helpdesk or a supported helpdesk provider.
- ****Support**** — allow shoppers to click "get help" from order detail pages by directing them to Klaviyo Helpdesk, an external help page link, Gorgias chat, or by hiding the option entirely.

> ****Note:**** Reviews, Loyalty (Smile.io / Yotpo), Subscription management, Order tracking (third-party), and Returns management are not currently supported for WooCommerce storefronts.

---

## 5. Link your privacy policy and terms of service

To maintain compliance and inform shoppers about the terms governing their interactions with Customer Hub, add links to your site's privacy policy and terms of service in the Customer Hub settings menu.

These links appear before a shopper signs in, as well as before they send a web chat message.

---

## 6. Set Customer Hub live

Before publishing, use the ****View live**** button to preview and test that all added functionality is working as expected—especially order data from your WooCommerce store.

When you're ready to publish:

1. Navigate to the ****Customer Hub settings**** menu.
2. Under **Customer Hub visibility**, select ****Live > Save****.

Once live, all saved changes apply immediately to the on-site experience.

---

## 7. Analyze your performance

Once Customer Hub is live, monitor its performance on the Customer Hub dashboard. Review key revenue metrics and reports to understand the value of the customer account experience, and use this data to inform how you tailor Customer Hub for your specific customer base.

---

## Frequently asked questions

### How do my customers discover or open Customer Hub?

When Customer Hub is set to "live" and your account page links have been updated (see step 3), any link pointing to `/#k-hub` will open Customer Hub. We also recommend enabling the Customer Hub widget to drive ongoing engagement.

### Why doesn't Customer Hub open automatically when shoppers click "My Account"?

Unlike Shopify, WooCommerce does not use a native Klaviyo app that can automatically intercept account page links. You need to manually update your account page links to point to `/#k-hub` instead of `/my-account`. See step 3 for details.

### Why can some shoppers see their name and recent orders without logging in?

Customer Hub uses Klaviyo's "Identified State" to recognize returning shoppers via browser tokens. This allows a personalized experience—like showing a Favorites list—for up to 28 days. Sensitive information like full addresses and payment methods remains hidden until the shopper completes a full login.

### What order data does Customer Hub pull from WooCommerce?

Customer Hub uses the WooCommerce REST API to fetch order history, order status, and customer profile data. Ensure your Consumer key has Read/Write permissions to allow Customer Hub to display this data accurately.

### Where do I find my WooCommerce Consumer key and Consumer secret?

In your WordPress admin panel, navigate to ****WooCommerce > Settings > Advanced > REST API****. If you haven't generated credentials yet, click ****Add key**** and follow the prompts. Note that the Consumer secret is only displayed once at the time of generation.
