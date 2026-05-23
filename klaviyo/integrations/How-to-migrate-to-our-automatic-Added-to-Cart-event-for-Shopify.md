---
id: 28709780787355
title: "How to migrate to our automatic Added to Cart event for Shopify"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/28709780787355-How-to-migrate-to-our-automatic-Added-to-Cart-event-for-Shopify"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: en
---

Are you new to Klaviyo? You can track Shopify **Added to Cart** events in Klaviyo automatically by [enabling onsite tracking](https://help.klaviyo.com/hc/en-us/articles/4425956184731).

Learn how to migrate from Klaviyo’s existing **Added to Cart** event for Shopify (enabled via a code snippet) to the automatically tracked **Added to Cart** event, which syncs via a Shopify Server Pixel. When migrating, you can also enable new tracking events for identified users such as **Viewed Collection** and **Submitted Search**.

These new Shopify Pixel events are branded with a Shopify icon in Klaviyo, while events enabled by a Klaviyo snippet have a gear icon.

## Before you begin

**Added to Cart** event data synced via Server Side Pixel cannot be customized. To learn what data is included with the new event, consult our [Shopify data reference](https://help.klaviyo.com/hc/en-us/articles/115005080447#h_01J6F8FWMEH250MPETV9FSDWF3).

Based on your Customer Privacy settings in Shopify, Klaviyo may not track onsite events for visitors to your Shopify store in the EU, EEA, UK and Switzerland, unless they have provided consent.

## Why migrate?

There are many reasons to migrate, including:

- The new Shopify-branded event syncs server-side, meaning site visitors are more likely to be identified and track events.
- The new event includes more top-level metadata than the snippet event, including variant info, SKUs, item quantity, and links to the variant added to the cart.
- The new event will be actively maintained by Klaviyo going forward, with future enhancements added directly.
- Enabling the new event does not require a code snippet.

We recommend migrating in the following order (as detailed in this article):

1. Enable our new **Added to Cart** tracking.
2. Update segments, flows, and more in Klaviyo.
3. Remove your old **Added to Cart** snippet.

Please note that we are not currently deprecating our **Added to Cart** snippet.

## Enable new Added to Cart tracking

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Shopify**** from the list to be brought to the integration settings page.
3. Under **Additional tracking features** in the **Onsite tracking box**, check ****Track behavioral events****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35512021815579)
4. Click ****Update Settings****.
5. If prompted: Log in to Shopify.
6. If prompted: Review the permissions and click ****Update app****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28710027741211)
7. In the confirmation modal, select ****Update integration****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28710027744667)
8. You’ll be brought back to Klaviyo and should see a green success callout.

![](https://klaviyo.zendesk.com/hc/article_attachments/28710022489755)

You should now start seeing Shopify-branded **Added to Cart** events tracked in your account.

## Update segments, flows, and more in Klaviyo

You should now replace all existing usage of the unbranded **Added to Cart** metric in your Klaviyo account with the new branded event.

### Segments

1. In the ****Lists & segments**** tab, look for segments where you’ve used the unbranded **Added to Cart** metric.
2. Edit each segment, adding an OR clause mirroring your original but using the Shopify-branded **Added to Cart** metric. For example, the segment below includes those who added to cart at least once in the last 30 days, tracked by either metric. If your conditions are entirely negative, use an AND clause.

![](https://klaviyo.zendesk.com/hc/article_attachments/28710022493467)

### Flows

Are you using the unbranded **Added to Cart** metric in an abandoned cart or other flow? To replace them:

1. Find the flows where you’re using **Added to Cart**.
2. [Clone these flows](https://help.klaviyo.com/hc/en-us/articles/24898429283739) and name them something descriptive.
3. In the new flows, replace the flow trigger with the Shopify-branded **Added to Cart** event.
4. Update any variables needed.
5. Send a test email for each new flow to make sure that everything looks good and that no variables need to be updated. If you were using our default snippet, all existing variables should be the same, except that the price is now a numeric value instead of a string (e.g., 4 vs. $4.00). You can add currency formatting like this:
   `{% currency_format event|lookup:'Price'|floatformat:2 %}`
   Additionally, please note that the new **Added to Cart** event does not currently include other items already in the cart; it just tracks a single item.
6. Turn off the old flows and set the new flows live.

### Analytics

If you’re using the unbranded **Added to Cart** metric in any analytics, such as custom reports, you should [build new custom reports](https://help.klaviyo.com/hc/en-us/articles/360047725651). If you're using the unbranded **Added to Cart** metric in metric mapping, you should [update the mapping](https://help.klaviyo.com/hc/en-us/articles/25829057055899).

## Remove your Added to Cart snippet

Are you using your existing **Added to Cart** event in a Klaviyo product feed? This means that you selected **Products a customer has added to cart** in the feed builder.

![](https://klaviyo.zendesk.com/hc/article_attachments/35512021818267)

If so, you should not remove your snippet. This is because we currently recommend using the old event with product feeds. You can use the new event for flows, segments, etc. If you are not using the event in a product feed, continue on.

You may have added your snippet in one of 2 ways:

- If your store has custom liquid blocks, your snippet will be in a custom liquid block.
- If your store does not have custom liquid blocks, your snippet will be in your theme file.

To remove your snippet:

1. At the top of the page, click the Home page dropdown.
2. Select ****Products > Default product**** to be brought to your default product page.
3. Find the custom liquid block you used for your **Added to Cart** snippet. There are multiple code snippets you may have used; look for the line `_learnq.push(['track', 'Added to Cart', cart]);` if you aren’t sure.
4. When you have the block selected, click ****Remove section****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28710027774107)
5. Click ****Save****.
6. Click the three dots at the top and select ****Edit code****.
7. Open the **theme.liquid** file.
8. Find your **Added to Cart** snippet code.
9. There are multiple code snippets you may have used; look for the line `_learnq.push(['track', 'Added to Cart', cart]);` if you aren’t sure.
10. Delete the snippet, starting with the opening <script> tag and ending with the closing </script> tag.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/28710022515099)
11. Click ****Save****.

1. In Shopify, navigate to ****Online Store > Themes****.
2. Find your theme and click ****Customize****.
3. If your store has custom liquid blocks:
4. If your store does not have custom liquid blocks:

You have now removed your **Added to Cart** snippet.

## Troubleshooting

Are you not seeing new **Added to Cart** events appear in your account?

It may take some time for profiles previously cookied by Klaviyo via the old method to be identified by Shopify.

With the new **Added to Cart** tracking (as well as with Shopify **Viewed Collection** and **Submitted Search** events), profiles will be identified if they do one of the following:

- Submit a Klaviyo form.
  - You must have enabled syncing profiles from Klaviyo to Shopify for this to work.
- Submit a Shopify form.
- Enter their information on the checkout page.
- Log in to their Shop account on checkout page.
- Log in to their customer account on the store.

You can complete one of the items above, and then add an item to your cart, in order to test your **Added to Cart** tracking.

We are working to expand functionality to include other Klaviyo identification methods (such as tracking from clicking on an email) to the new Shopify **Added to Cart** event.

## Outcome

You’ve now migrated from Klaviyo’s manually-enabled **Added to Cart** tracking to our new, server-side **Added to Cart** tracking in Shopify.