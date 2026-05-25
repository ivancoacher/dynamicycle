---
id: "1260805704029"
title: "Troubleshooting Klaviyo.js and site speed reports"
source_url: "https://help.klaviyo.com/hc/en-us/articles/1260805704029-Troubleshooting-Klaviyo-js-and-site-speed-reports"
section: "Troubleshooting sign-up forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:56:42Z"
language: "en"
---
## You will learn

Learn about Klaviyo's onsite JavaScript (Klaviyo.js), which is the code snippet that you paste on your site to enable **Active on Site** tracking, and its impact on site speed. Klaviyo.js needs to be installed in order for you to publish Klaviyo sign-up forms on your website.

For help enabling **Active on Site** through your integration, see [how to verify that sign-up forms are enabled](https://help.klaviyo.com/hc/en-us/articles/360002035871).

## Troubleshoot site speed performance

Klaviyo.js is injected automatically through many of our [ecommerce integrations](https://help.klaviyo.com/hc/en-us/articles/115000256472-Understanding-integrations#ecommerce-integrations1), and you can manually install it for other platforms. It enables Klaviyo sign-up forms to appear, and can allow you to track when customers are active on your site.

- If you find that Klaviyo’s JavaScript is impacting your website’s performance (i.e., PageSpeed score) and it was automatically installed through an integration, you can try [manually installing it instead](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration#active-on-site-tracking-snippet).

  For Shopify, we recommend you enable**Active on Site**tracking through [Klaviyo’s Shopify app embed](https://help.klaviyo.com/hc/en-us/articles/4425956184731) rather than manually installing. This bypasses the website’s native tag manager and can result in faster loading of Klaviyo’s JavaScript.
- If you don't use Klaviyo sign-up forms (meaning you use another tool for creating and publishing sign-up forms on your website), make sure that all forms in your ****Sign-up forms**** tab are set to **Draft**.

  Navigate to the ****Sign-up forms**** tab to see the **Status** of each of your sign-up forms. **Live** indicates a published form on your site, **Editing** indicates a live form that has unpublished changes, and **Draft** indicates a form that has not been published on your site.

  ![The sign-up forms tab showing the Status column for three example live, editing, and draft forms.](https://klaviyo.zendesk.com/hc/article_attachments/28716066373403)

Regardless of which installation method you use (e.g., through an ecommerce integration, or manually installed), Klaviyo’s JavaScript is loaded asynchronously. This means it will not block other aspects of your site from loading. However, Google’s PageSpeed Insights and other site speed reports may still flag it as a contributing factor in your site’s load times.

Site speed and SEO are important to our customers, and Klaviyo is committed to minimizing the impact from our JavaScript. Learn how our [engineers have optimized klaviyo.js](https://klaviyo.tech/improving-forms-performance-c67c98114d49). You will continue to see improvements as we release new updates to make Klaviyo.js more performant and improve load times.

## Additional resources

- [Getting started with Klaviyo onsite tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Web-Tracking)
- [Third-party integrations reference](https://help.klaviyo.com/hc/en-us/articles/360049626051-Third-Party-Integrations)