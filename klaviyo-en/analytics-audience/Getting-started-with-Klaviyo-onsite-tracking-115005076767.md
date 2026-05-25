---
id: "115005076767"
title: "Getting started with Klaviyo onsite tracking"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005076767-Getting-started-with-Klaviyo-onsite-tracking"
section: "Getting started with metrics"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-15T08:50:35Z"
language: "en"
---
## You will learn

Learn about the different ways that Klaviyo can support onsite tracking on your ecommerce site. There are 2 key types of onsite tracking:

- ******Active on Site****** ****tracking****
  This metric is tracked whenever an identifiable browser visits your website.
- ******Viewed Product****** ****tracking****
  This metric is tracked whenever an identifiable browser views a product page on your website (for ecommerce stores).

**Active on Site** tracking can help segment your contacts based on engagement level, while **Viewed Product** tracking can enable you to send product reminders in a [browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252).

For Shopify, we also offer [additional types of onsite tracking](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01J6F7TREZAJM7M3R3DFVZSDGT).

## Before you begin

Enabling onsite tracking is different for each ecommerce integration. In this article, you will learn how to do this and who Klaviyo tracks.

The code snippet for onsite tracking is known as Klaviyo’s onsite JavaScript or “Klaviyo.js." You do not need to add Klaviyo.js separately if you enabled active onsite tracking through one of the ecommerce integrations below:

- [****Shopify****](https://help.klaviyo.com/hc/en-us/articles/115005080407)
  **Active on Site** tracking is added automatically through the integration or through the [Klaviyo app embed](https://help.klaviyo.com/hc/en-us/articles/4425956184731) if it's toggled on.
- [****BigCommerce****](https://help.klaviyo.com/hc/en-us/articles/115005082547)
  **Active on Site** tracking is added when you integrate if you also check the setting **Automatically add Klaviyo onsite javascript.**
- [****WooCommerce****](https://help.klaviyo.com/hc/en-us/articles/115005255808)
  **Active on Site** tracking is added automatically when you integrate.
- [****Magento****](https://help.klaviyo.com/hc/en-us/articles/115005254348)
  **Active on Site** tracking is added automatically when you integrate.
- [****Wix****](https://help.klaviyo.com/hc/en-us/articles/6202669053723)
  **Active on Site** tracking is added when you integrate if you check the setting **Automatically add Klaviyo onsite javascript**.
- [****PrestaShop****](https://help.klaviyo.com/hc/en-us/articles/360054551492)
  **Active on Site** tracking is added automatically when you integrate.
- [****Salesforce Commerce Cloud****](https://help.klaviyo.com/hc/en-us/articles/360033744951)
  **Active on Site** tracking is added automatically when you integrate.
- [****Square Online****](https://help.klaviyo.com/hc/en-us/articles/11117215837211)
  **Active on Site** tracking is added when you integrate if you check the setting **Automatically add Klaviyo onsite javascript.**
- [****Shopware****](https://help.klaviyo.com/hc/en-us/articles/13001662470939)
  **Active on Site** tracking is added automatically when you integrate.

If you are using another ecommerce platform, or a custom platform, you can [install Klaviyo.js manually.](#h_01GMEAQZXKADF4FR7P1FMNC7EB)

Because pasting this code requires access to your site's HTML and ecommerce platform, our support team cannot offer hands-on assistance. If you don't have a developer resource on your team and aren't comfortable adding the code, consider [reaching out to a Klaviyo partner for assistance](https://klaviyo.partnerpage.io/).

## Active on site event data

The **Active on site** event captures the following information about identified visitors, and is represented in the event data.

Event data beyond **Browser**, **OS**, and **Page** is only available on **Active on Site** events captured after 1/3/2025.

- ****Browser****
  User agent for the originating browser (e.g., “Chrome”).
- ****Os****
  User agent for the originating operating system (e.g., “Mac”).
- ****Page****
  The URL of the visited page.
- ****utm\_medium****
  The marketing channel the user comes from to the website.
- ****utm\_source****
  The source of traffic to the website.
- ****utm\_campaign****
  The name of the marketing campaign associated with the traffic.
- ****utm\_id****
  The unique identifier for the marketing campaign associated with the traffic.
- ****utm\_term****
  This is an optional UTM parameter that marketers can set to track paid search terms.

  For each of the [UTM parameters](https://help.klaviyo.com/hc/en-us/articles/115005247808), Klaviyo will return the first value in the URL’s query parameters. If the UTM parameter is not present on a URL, then no values are provided in the event.
- ****Fragments****
  Any other items in the URL, like an anchor tag that indicates where the user would have landed on the page. If there are no fragments on the URL, no values are set.
- ****Identity\_source****
  The event that triggered Klaviyo to receive the on-site event.
- ****Parameters****
  Each of the first 10 parameters present in the URL has their own piece of event data, except for **\_kx** and UTMs. If there are no parameters on the URL, no values are set. Parameters beyond the first 10 are not captured.
- ****First\_page\_path****
  The path of the first page a customer lands on. If there is no path on the first page view, no value is set.
- ****Kx\_present****
  If \_kx is present on the URL, **true** is returned for the dimension. If not, **false** is returned. This highlights whether or not the session could be associated with a click on a link in a Klaviyo message.

## Add onsite tracking manually

1. Copy the following **Active on Site** code snippet, also known as Klaviyo.js:

   ```
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
   ```
2. In Klaviyo, click your account name in the lower left corner and navigate to ****Settings > Account > API Keys****, then note your Public API Key.
3. Paste the code snippet in the main template of your site. Where you see PUBLIC\_API\_KEY in the snippet, replace this with your key.
4. Save and publish your site template.

Now that you've installed **Active on Site** tracking, Klaviyo will track whenever an identifiable person visits your website.

## Understanding **Viewed Product** tracking

**Viewed Product** tracking in Klaviyo is specifically designed for ecommerce stores, and can enable you to send product reminders in a [browse abandonment flow](https://help.klaviyo.com/hc/en-us/articles/115002775252). Once **Viewed Product** is installed, it will record a metric whenever an identifiable person views a product page on your website.

Enabling **Viewed Product** tracking is different for each ecommerce platform. If you are not seeing data captured from this metric, double-check that it's installed correctly.

Learn how to enable **Viewed Product** tracking for these ecommerce platforms:

- ****Shopify****
  Enable **V****iewed Product** tracking through the [Klaviyo app embed in Shopify](https://help.klaviyo.com/hc/en-us/articles/4425956184731).
- ****BigCommerce****
  [Learn how to add viewed product tracking](https://help.klaviyo.com/hc/en-us/articles/115005082547#add-viewed-product-tracking4) to your BigCommerce store.

  **Viewed Product** tracking is automatically installed through these ecommerce integrations:
- [Magento 1 Integration](https://help.klaviyo.com/hc/en-us/articles/115005082187)
- [Magento 2 Integration](https://help.klaviyo.com/hc/en-us/articles/115005254348)
- [WooCommerce Integration](https://help.klaviyo.com/hc/en-us/articles/115005255808)
- [PrestaShop integration](https://help.klaviyo.com/hc/en-us/articles/360054551492)
- [Salesforce Commerce Cloud integration](https://help.klaviyo.com/hc/en-us/articles/360033744951)
- [Shopware integration](https://help.klaviyo.com/hc/en-us/articles/13001662470939)

**Viewed Product** tracking can also be added to other ecommerce platforms and custom carts. For instructions on how to do this, head to our [guide detailing how to add Viewed Product tracking for custom ecommerce stores](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration#viewed-product-tracking-snippet).

## Test your onsite tracking

After enabling tracking on your site, you can test that tracking is set up properly by following these steps:

1. Navigate to your website.
2. Add the following to the end of your store url, replacing example@gmail.com with your email address:
   ****?utm\_email=example@gmail.com****
3. After you reload the page, search in Klaviyo for your email address.
4. You should see that a Klaviyo profile has been created for you (if one didn't exist already) and that this site visit has been tracked on your activity feed.
5. To see a feed of all tracked activity for the **Active on Site** and **Viewed Product** metrics, navigate to ****Analytics > Metrics****. You can click on each metric to analyze tracked data through an activity feed, activity map, charts, best people, and cohort reports. You can also filter by source. Filter by ****API**** to see active on site and viewed product events (these events have a gear icon).

![Metrics tab in Klaviyo filtered by API showing Active on Site and Viewed Product in list with gear icons](https://klaviyo.zendesk.com/hc/article_attachments/28723623317403)

## Who Klaviyo tracks

By enabling basic onsite tracking on your website, you can collect helpful information around browsing activity that can be leveraged for your marketing strategies.

When you add Klaviyo's onsite tracking to your site, it only tracks the browsing activity of "known browsers" (i.e. browsers that have visited or engaged on your site, submitted a form through a certain action, reached the success step of a form, reached the final reachable step for tap-to-text for SMS, or have been identified or "cookied").

If an email is forwarded and then opened and clicked on by a subsequent person, this will result in that device being linked to an open/click. It could also update and overwrite the profile information of the person who originally received that email.

![An example subscriber profile named Johan with Logged In and Active on Site events on timeline](https://klaviyo.zendesk.com/hc/article_attachments/28723623315867)

There are multiple ways Klaviyo will identify a site visitor for onsite tracking:

- If someone has, at some point, clicked through a Klaviyo email or SMS to your website.
- If someone has, at some point, subscribed/opted-in through a Klaviyo form.
- If someone has, submitted a Klaviyo form through a certain action.

  In order for a submitted form to be tracked, the visitor must submit a form step that has a submit action tied to it (e.g., **Submit and Go to next step**, **Submit opt-in code**, **Submit form and Go to UR**L); it won't count if the form step's submit action is only **Go to URL** or **Close form**. If a form has both a **Submit Form** and **Go to URL** actions, it will only count the event when someone submits the form.
- If someone has reached the success step of a form, or reached the final reachable step for tap-to-text (**Subscribe via SMS**) forms.
- If someone has, at some point, logged in to your site (and you have installed [custom tracking for logged in users](https://developers.klaviyo.com/en/docs/javascript_api#identify-people), which is not included with Klaviyo's native ecommerce integrations).

As a result, until you send emails or messages with Klaviyo and grow your lists, you probably won't see a lot of tracked onsite activity. Over time, Klaviyo will identify more and more of your contact-base and your onsite tracking data will become more comprehensive.

For Shopify stores, based on your Customer Privacy settings in Shopify, Klaviyo may not track onsite events for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent.

## Examples of how to use onsite tracking

Ways to use onsite tracking include:

- ****Segment your contacts based on engagement level.****
  By gaining insight into which contacts interact with your website and how often, you can build a more personal communication strategy that drives deeper engagement.
- ****Trigger an automated flow email or SMS to those that browse several times without purchasing.****
  While you don't want to send someone an email or SMS every time they visit your website, you might want to send a light touchpoint to those who visit several times in a short period of time, but don't engage further. For example, you can trigger a flow to those who have been **Active on Site** at least 4 times in the last 30 days, but haven't started or completed a checkout.

It's important to note that for **Active on Site** events in particular, while you can segment on the event itself, the data inside of it cannot be used for segmentation or flow filtering.

## The \_kx parameter

When you have **Email to Website** tracking enabled and have Klaviyo.js on your website, Klaviyo will identify individuals who click through a Klaviyo email and then end up browsing your website. This is one of the fundamental ways Klaviyo can identify new site visitors and cookie them so they get identified during all future visits to your page.

SMS messages click and conversion tracking is dependent on having a link, and this link must use the Klaviyo link shortener. When setting up your SMS messages, it’s important to have the option checked for ****Automatically shorten links**** to ensure you are using the default tracking.

Klaviyo's email website tracking works by adding an additional parameter to all the URLs you send (i.e., the **\_kx** parameter). The unique encrypted value is then decrypted by the **Active on Site** snippet and allows us to identify the user that clicked through the URL. See the example link below for an idea of how this will look in the URL:

`http://example.com/?_kx=J8fjcn003Wy6b-3ILNlOyZXabW6dcFwTyeuxrowMers%3D.McN66`

This parameter is automatically appended when live emails are sent and should not affect the load times of your links or break any links based on its placement. Note that when previewing emails, the value set for the \_kx parameter will just be a placeholder to prevent being cookied as the recipient.

However, if you use URLs that contain query parameters to inform your server to automatically download a file, the \_kx parameter could cause your link to break. In order for the download to function properly, either toggle off email to website tracking in your account email settings or configure your server to ignore this parameter. As of now, you can only toggle this off across your account; you cannot turn it off for individual campaigns.