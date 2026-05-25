---
id: "6353315757211"
title: "Getting started with Google Ads"
source_url: "https://help.klaviyo.com/hc/en-us/articles/6353315757211-Getting-started-with-Google-Ads"
section: "Google Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: "en"
---
## You will learn

Learn how to integrate Google Ads with Klaviyo. This integration allows you to automatically:

- Connect a Klaviyo list or segment to a Google Audience.
- Sync profiles from Klaviyo to Google.

Drive your Google Ads strategy more easily with the help of Klaviyo. After integrating, you’ll be able to re-target existing customers, optimize targeting, and exclude profiles from advertising campaigns based on criteria such as purchase data.

## Before you begin

Before you integrate with Google Ads, set up your Klaviyo account and integrate with your ecommerce platform. See our guide on [getting started with Klaviyo](https://academy.klaviyo.com/getting-started-with-klaviyo/1405979).

It's important to note the following:

- Access via manager and MCC (My Client Center) accounts is not supported, so before you integrate make sure that you are a direct admin of the Google Ads account you want to connect.
- Klaviyo's Google Ads integration will only work properly if your Google Ads account is eligible for Customer Match. To learn more, read [Google's Customer Match policy](https://support.google.com/adspolicy/answer/6299717).

## How to integrate with Google Ads

1. If you need to create a new list in Klaviyo, navigate to the ****Lists & Segments**** tab under ****Audience****.
2. Click ****Create List/Segment****.
3. Name the list and assign any tags.
4. Click ****Create List****.

1. Log in to your Klaviyo account.
2. Select the ****Integrations**** tab.
3. Click ****Explore apps****.
4. Search for **Google Ads** and click the card, then click ****Install****.
5. Click ****Connect to Google****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720659468443)
6. Log in to your Google account. Note that the Google account you log in with needs to have direct admin permissions for the Google Ads account you wish to connect. Access via manager/MCC accounts is not supported.
7. Agree to the permissions and click ****Allow**** to be brought back into Klaviyo.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720659471899)
8. Select the Google Ads account you want to integrate with from the dropdown. Don’t see the right account available in the dropdown? Confirm that you have admin permissions for that account, then try again.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720659473819)
9. Select whether you market to people in the European Economic Area (or EEA, which currently includes EU countries and also Iceland, Liechtenstein and Norway) or in the United Kingdom (UK).
10. If you market to people in the EEA or UK, in compliance with the Digital Markets Act, you must agree to only send audiences to Google that have granted consent to ad targeting.
11. Under **Connections**, select a Klaviyo list or segment to connect with an audience.
12. Select a Google Audience to connect with your list or segment. If you need to create a new Google Audience, type the new name in the search box and click ****+ Create audience: [Audience Name]****.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/28720659476123)
13. If you want to add additional connections, click ****Add Connection****. Note that you can return to this settings page at any time to add additional connections. Additionally, note that this is a 1:1 sync; you cannot select the same Google Audience for multiple Klaviyo lists or segments, and you cannot connect the same Klaviyo list or segment to multiple Google Audiences.
14. Once you are finished adding connections, click ****Complete setup.****
15. A success message will appear, letting you know that your Google Ads account is now connected to Klaviyo.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/28720671293467)
16. After integrating, you'll see a Google Ads manager linking request from google.integrations@klaviyo.com in your inbox, which you should accept.

## How the integration works

When connecting Klaviyo lists or segments to Google Audiences, you can:

- Create 1:1 syncs between a Klaviyo list or segment and a Google Audience. Note that you cannot select the same Google Audience for multiple Klaviyo lists or segments, and you cannot connect the same Klaviyo list or segment to multiple Google Audiences.
- Create a new Google Audience from within Klaviyo to connect a new list or segment to.

When you create a new connection from Klaviyo to Google Ads, it can take up to 48 hours for the custom audience in Google Ads to populate. The ongoing sync from Klaviyo to Google Ads to update profile list/segment membership is in real-time, though it may take Google Ads up to 48 hours to process the data received from Klaviyo. This is due to a delay in Google accepting and processing profiles from Klaviyo.

Only profiles associated with a Google account will appear in the Google Audience. Therefore, you may see that your Google Audience sizes are smaller than their corresponding lists or segments in Klaviyo, which is to be expected. Additionally, Google [removes profiles from these audiences](https://ads-developers.googleblog.com/2025/02/update-to-customer-match-membership.html) after 540 days.

## Manage your ad integrations from the Lists & Segments tab

You can create or update Google audience syncs (or syncs for any other advertising platform) from within Klaviyo’s **Lists & Segments** tab.

To do this:

1. In Klaviyo, select ****Lists & Segments**** in the left hand navigation.
2. You’ll see ad platform icons in the **Integrations** column for each list and segment connected to an ad integration audience.
3. To see more details for a given list or segment, click the three dots and select ****Linked integrations****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720671274139)
4. You’ll be brought to the **Integrations** tab found within the list or segment’s **Settings** tab.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28720671279387)
5. Here, you’ll be able to do the following:

   - Connect a new ad integration.
   - Activate or deactivate a sync for the list or segment.
   - Add a new sync for the list or segment, and select the corresponding Google audience.
6. After making any changes, click ****Save****.

## Integration use cases

There are many ways you can use this integration to drive your marketing strategy with Google Ads. We’ve bucketed these use cases into 4 main categories:

1. Retarget existing profiles.
2. Exclude certain segments from future ads.
3. Use existing segments to optimize targeting.
4. Observe and monitor how a specific audience is performing.

Below, we’ll discuss use cases for each category and provide Google resources around implementation.

### Retarget existing profiles

The same segmentation used for targeted emails and texts can be used for targeted ads. Consider the following segments:

1. ****Cart abandoners****
   Target customers who started a checkout in the past 7 days, but haven't placed an order in the past 7 days, with an ad that echoes the message or discount you provide in your abandoned cart flow.
2. ****Winback****
   Target customers that haven’t purchased in a while with an ad featuring popular trending items.
3. ****Re-engage****
   Target inactive subscribers with a relevant ad featuring items they’ve viewed on your site or featuring a limited time offer promotion.
4. ****Cross-sell****
   Target customers who have bought one product with a different but complementary product.
5. ****New customer****
   Target those that have visited your site but never purchased to encourage first-time conversions.
6. ****Cross-channel****
   Target those you're already reaching by email with a relevant ad that reinforces the message and has a similar call-to-action.
7. ****Potential brand enthusiasts****
   These customers purchased recently, but not frequently and not at a high monetary value. Focus on increasing their purchase frequency or average order value by promoting bestsellers and popular or related products.
8. ****Unengaged VIP****
   If customers who were once on your VIP list haven’t engaged with your brand recently, you can target them on a different platform to bring them back to your brand.
   1. Navigate to the ****Lists & Segments**** tab under ****Audience****.
   2. Click Create ****List/Segment****, then select ****Segment****.
   3. Design your segment to match the group you want to target.

   Here’s how to target one of these segments by applying the audience to an ad group or campaign in Google Ads:
9. Create your segment in Klaviyo.
10. When integrating with Google Ads, connect your segment to a new Google Audience, as described in the how to integrate section above.
11. Once you’ve integrated, head to Google Ads. There, use the targeting setting to narrow your ad group or target your campaign to the audience you synced from Klaviyo. To learn more about targeting, check out the Google Ads [implementation guide](https://support.google.com/google-ads/answer/7374253).

### Exclude existing profiles from future ads

If there is a list or segment you want to exclude from future ads (for instance, exclude customers who have bought from you recently and may be unlikely to repurchase soon), you can create that list or segment in Klaviyo, sync it to a custom audience in Google Ads, and exclude it from an adgroup or campaign.

This is similar to the process described for targeting a segment, and the only difference is that within Google Ads, you exclude the segment. To learn how to exclude a specific audience list from an ad group or campaign in Google Ads, consult [Google's implementation guide for exclusions](https://support.google.com/google-ads/answer/2549058).

### Use existing segments to optimize targeting

You can take a VIP list or segment in Klaviyo and then use optimized targeting in Google to reach new leads that resemble your best customers. You’ll need to create a segment in Klaviyo, or use an existing VIP segment, then sync it to a Google audience through the integration. Then, in Google Ads, you’ll use optimized targeting and add the segment as a targeting signal for your campaign.

- Learn about [optimized targeting in Google Ads](https://support.google.com/google-ads/answer/10537509?sjid=7203013319057182442-NA), which can help you reach new audiences that are likely to convert.
- Learn [how to use optimized targeting](https://support.google.com/google-ads/answer/10538014?sjid=7203013319057182442-NA).

### Observe and monitor how a specific audience is performing

You can also decide to only monitor how ads are performing for selected audiences (reporting) while your campaign is running without changing the reach of your campaign or adgroup. Based on the reporting/observation of your profiles, you may decide to create a new adgroup or campaign to target these profiles or to make bid adjustments.

- Learn [how to observe and monitor how an audience is performing](https://support.google.com/google-ads/answer/7374253) in Google Ads.

## EEA consent requirements

Beginning March 6, 2024, Google will begin enforcement of the [Digital Marketing Act](https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/digital-markets-act-ensuring-fair-and-open-digital-markets_en) (DMA) in the European Economic Area (EEA) and the United Kingdom (UK). As a result, they are updating their [EU user consent policy](https://www.google.com/about/company/user-consent-policy/?sjid=15416941068016224808-NA) to require platforms that integrate with Google Ads to include advertising consent when syncing EEA or UK profiles to Google.

Klaviyo’s Google Ads integration includes the option to sync the necessary consent markers to Google by selecting the option “**I agree to only send audiences to Google that have granted consent for ad targeting**” when setting up the integration.

![](https://klaviyo.zendesk.com/hc/article_attachments/28720671271707)

When you select this option, Klaviyo automatically sets ad personalization and ad user data consent for the profiles included in the sync, so you are able to market to them through Google Ads. This includes automatically setting the consent status in Google Ads. Thus, it is important that your brand actually collects this consent to be compliant if you serve ads to EEA or UK profiles.

As a reminder, advertising consent is separate from marketing consent used to send communications, and must be collected outside of Klaviyo if you plan to target EEA or UK profiles with ads. Typically, this is done through a [CMP](https://support.google.com/admanager/answer/13554116?hl=en#zippy=%2Cgoogle-certified-cmps) (consent management platform) like [OneTrust](https://www.onetrust.com/), and your brand should work with your CMP for more insight on how to best manage your advertising consent data and options to export it to other platforms.

Enforcement of this new requirement is forward-facing beginning March 6th, and profiles previously synced through the integration don't need to be updated with advertising consent data.

Klaviyo recommends working with your legal counsel to confirm that your advertising consent collection practices are compliant, and that you are meeting Google’s updated EU user consent policy.

## Manage advertising consent data in Klaviyo

While syncing advertising consent data to Klaviyo from your CMP is not required for consent to be sent to Google Ads, it is recommended. The following solution can help OneTrust users more easily manage their advertising consent in Klaviyo. Klaviyo recommends working with a developer to implement this solution.

Advertising consent data isn’t natively synced to Klaviyo from CMPs, but you can use a Javascript snippet that sets custom profile properties in Klaviyo to represent advertising consent from OneTrust. This script only works with OneTrust/CookiePro, but can be modified to work with your own CMP.

Before getting started, map the consent preferences in OneTrust to the consent fields required by Google (i.e., **ad\_user\_data** and **ad\_personalization**).

To implement this solution, add the following script to your site (generally, this is added to the <head> HTML tag).

Ensure the [Klaviyo object has been loaded](https://developers.klaviyo.com/en/docs/introduction_to_the_klaviyo_object#how-to-load-the-klaviyo-object) so updates are recorded successfully, as the consent code executes first on page load.

[“Example](https://www.napkin.io/api/embed/c1e26f659b834bd0)

Within this script, replace **///OneTrust\_CookiePro scripts** with your existing consent scripts from OneTrust/CookiePro.

Additionally, replace **category\_ID** with your own [cookie categorization in OneTrust](https://my.onetrust.com/articles/en_US/Knowledge/UUID-66bcaaf1-c7ca-5f32-6760-c75a1337c226).

Once added to your site, this script will automatically set the **ad\_user\_data** and **ad\_personalization** profile properties in Klaviyo, with a value of **denied**.

![ad_personalization and ad_user_data properties set to denied on profile in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28720659447963)

As customers provide the necessary consent through the OneTrust cookie banner on your site, the script will update the values for the **ad\_user\_data** and **ad\_personalization** properties in Klaviyo to **granted**.

This script will only update profile properties for profiles Klaviyo has identified, and if you have loaded the Klaviyo tracking scripts.

Once you have the **ad\_user\_data** and **ad\_personalization** properties set in Klaviyo, update your segments in Klaviyo that are being synced to Google Ads, so they only include profiles that have provided advertising consent.

![Example segment limiting group to profiles that have provded ad consent based on ad_personalization and ad_user_data properties](https://klaviyo.zendesk.com/hc/article_attachments/28720671268763)

## Outcome

You’ve finished integrating Google Ads with Klaviyo, and can now begin using Klaviyo to help drive your advertising strategy on Google Ads.

Google Ads resources:

Klaviyo resources: