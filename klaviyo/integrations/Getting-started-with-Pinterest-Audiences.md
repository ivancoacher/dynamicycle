---
id: 25594493075227
title: "Getting started with Pinterest Audiences"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/25594493075227-Getting-started-with-Pinterest-Audiences"
section: "Pinterest"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:36Z"
language: en
---

## You will learn

Learn how to integrate Pinterest Audiences with Klaviyo. This integration allows you to automatically:

- Connect a Klaviyo list or segment to a Pinterest audience.
- Sync profiles (including their email addresses) from Klaviyo to Pinterest.

## Before you begin

Before you integrate with Pinterest, set up your Klaviyo account and integrate with your ecommerce platform. See our guide on [getting started with Klaviyo](https://academy.klaviyo.com/getting-started-with-klaviyo/1405979).

It's important to note the following:

- You can only integrate 1 Pinterest ad account per Klaviyo account.
- Your account must have [Audience or Ad account admin permissions](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) in order to use this integration.

![](https://klaviyo.zendesk.com/hc/article_attachments/28716356651803)

## How to integrate with Pinterest

1. Log in to your Klaviyo account.
2. Select the ****Integrations**** tab.
3. Click ****Explore apps****.
4. Search for **Pinterest Audiences** and select the card, then click ****Install****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28716333747099)
5. Click ****Connect to Pinterest Audiences****.
6. You’ll be prompted to log in to your Pinterest business account, if you have not already.
7. Review the permissions, and then click ****Give access****. You’ll be redirected to Klaviyo.
8. If you manage multiple ad accounts, you’ll need to select the one you want to integrate with. If you only manage one account, you’ll see it preselected.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28716356657691)
9. Next, set up connections between Klaviyo lists/segments and Pinterest audiences. Select a Klaviyo list or segment from the left hand dropdown, then select a Pinterest audience to connect to on the right. Please note that the Pinterest audience must be a customer list in order to connect.
10. You can create a new Pinterest audience from within Klaviyo if needed:
    1. Click the **Select an audience** dropdown, type your new audience name in the search bar.
       ![](https://klaviyo.zendesk.com/hc/article_attachments/28716333738395)
    2. Then, click ****+ Create audience: (Audience Name)****.
11. If you want to add additional connections, click ****Add connection****. Note that you can return to this settings page at any time to add additional connections. Additionally, note that this is a 1:1 sync; you cannot select the same Pinterest audience for multiple Klaviyo lists or segments, and you cannot connect the same Klaviyo list or segment to multiple Pinterest audiences.
12. When you’re done creating connections, click ****Complete setup****.
13. You’ll receive a success message that your Pinterest account is connected to Klaviyo.

![](https://klaviyo.zendesk.com/hc/article_attachments/28716356650523)

Klaviyo profiles will start syncing to Pinterest for any connections created. It may take up to 48 hours for the audience in Pinterest to populate.

## How the integration works

Sync frequency:

- If you add a new connection, it may take up to 48 hours for the audience in Pinterest to populate.
- Membership changes in your Klaviyo lists or segments (profiles being added or removed) may take up to 48 hours to be reflected in Pinterest.

  Sync behavior:
- This integration is a 1:1 sync; you cannot select the same Pinterest audience for multiple Klaviyo lists or segments, and you cannot connect the same Klaviyo list or segment to multiple Pinterest audiences.
- When a profile is added or removed from a Klaviyo list or segment, the corresponding Pinterest audience will be updated accordingly.
- The audience you see in Pinterest will likely be smaller than the Klaviyo list or segment you connected. This is because the Pinterest audience will only include people with an existing Pinterest profile that Klaviyo has matched.
- When you connect a Klaviyo list or segment to a Pinterest audience, existing members will remain in that audience (you will not “overwrite” the Pinterest audience by syncing profiles from Klaviyo).

## Integration use cases

There are many ways you can use this integration to drive your marketing strategy with Pinterest. We’ve bucketed these use cases into 3 main categories:

1. Retarget existing profiles.
2. Use existing profiles to create actalike audiences.
3. Observe and monitor how a specific audience is performing.

Below, we’ll discuss use cases for each category and provide Pinterest resources around implementation.

### Retarget existing profiles

The same segmentation used for targeted emails and texts can be used for targeted ads. Consider the following segments:

1. ****Cart abandoners****
   Target customers who started a checkout in the past 7 days, but haven't placed an order in the past 7 days. Show this group an ad that echoes the message or discount you provide in your abandoned cart flow.
2. ****Winback****
   Target customers that haven’t purchased in a while with an ad featuring popular trending items.
3. ****Re-engage****
   Target inactive subscribers with a relevant ad featuring items they’ve viewed on your site or featuring a limited time offer promotion.
4. ****Cross-sell****
   Target customers who have bought one product with a different but complementary product.
5. ****New customers****
   Target those that have visited your site but never purchased to encourage first-time conversions.
6. ****Cross-channel****
   Target those you're already reaching by email with a relevant ad that reinforces the message and has a similar call-to-action.
7. ****Potential brand enthusiasts****
   These customers purchased recently, but not frequently and not at a high monetary value. Focus on increasing their purchase frequency or average order value by promoting bestsellers and popular or related products.
8. ****Unengaged VIPs****
   If customers who were once on your VIP list haven’t engaged with your brand recently, you can target them on a different platform to bring them back to your brand.
   1. Navigate to the ****Lists & segments**** tab under **Audience**.
   2. Click ****Create New > Create segment****.
   3. Design your segment to match the group you want to target.

   Here’s how to target one of these segments in Pinterest:
9. Create your segment in Klaviyo.
10. When integrating with Pinterest, connect your segment to a new Pinterest audience, as described in the **How to Integrate** section above.
11. Once you’ve integrated, head to your Pinterest business account. When you [create your ad group](https://help.pinterest.com/en/business/article/create-ad-group) for a campaign, you’ll be able to target the audience synced from Klaviyo. You can view the audiences synced from Klaviyo in Pinterest under ****Business > Audiences****.

### Exclude existing profiles from future ads

If there is a list or segment you want to exclude from future ads (for instance, exclude customers who have bought from you recently and may be unlikely to repurchase soon), you can:

1. Create that list or segment in Klaviyo.
2. Sync it to an audience in Pinterest.
3. Exclude it from an ad group.

To learn how to exclude a specific audience from an ad group, check out [Pinterest’s documentation](https://developers.pinterest.com/docs/ads/targeting/#Customer%20lists).

### Use existing profiles to create actalike audiences

You can take a VIP list or segment in Klaviyo and then create an actalike audience in Pinterest to reach leads that resemble your best customers. Create a segment in Klaviyo, or use an existing VIP segment, and sync it to a Pinterest audience through the integration. Then, in Pinterest, you’ll create an actalike audience. Learn [how to create actalike audiences in Pinterest](https://help.pinterest.com/en/business/article/audience-targeting)

### Observe and monitor how a specific audience is performing

Reporting can help you understand how your ads are performing and make targeted changes. Check out Pinterest’s help article [Review reporting](https://help.pinterest.com/en/business/article/reporting-dashboard-overview) to learn about reporting in Pinterest.

## Outcome

You’ve finished integrating Pinterest with Klaviyo, and can now begin using Klaviyo to help drive your advertising strategy on Pinterest.