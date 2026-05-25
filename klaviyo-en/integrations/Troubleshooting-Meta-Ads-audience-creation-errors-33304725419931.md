---
id: "33304725419931"
title: "Troubleshooting Meta Ads audience creation errors"
source_url: "https://help.klaviyo.com/hc/en-us/articles/33304725419931-Troubleshooting-Meta-Ads-audience-creation-errors"
section: "Meta Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-16T22:55:27Z"
language: "en"
---
## You will learn

Learn how to resolve Meta Ads custom audience creation errors in Klaviyo.

Have you received one of the following errors when trying to create a new custom audience within your Meta Ads integration in Klaviyo?

- **Unable to create audience. Check your Facebook Ads permissions and re-authenticate.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/33304909206043)**
- **To create a Meta Ads Custom Audience, please agree to the Custom Audience Terms here.****![](https://klaviyo.zendesk.com/hc/article_attachments/35583895080091)**

These errors may indicate that you have not accepted Meta’s terms of service for your ad account. Read on to learn how to accept these permissions, and other steps you can take to solve this error.

## Before you begin

You must be an admin of your Meta Ads account in order to complete the following steps.

## Troubleshooting steps

To accept Meta’s terms of service:

1. Copy and paste the following URL into your browser, but do not hit enter:

   ```
    https://business.facebook.com/ads/manage/customaudiences/tos/?act=AdAccountID
   ```

   ![](https://klaviyo.zendesk.com/hc/article_attachments/33304903139355)
2. You'll need to update the link above by changing **AdAccountID** to your specific ad account ID from Meta. To find this ID:

1. Open a new tab and navigate to [Ad accounts in Meta’s business settings](https://business.facebook.com/settings/ad-accounts).
2. Select your ad account on the left.
3. Find the account ID, under the account name on the right.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33304903145499)
4. Copy the ID.

3. In your original tab, replace **AdAccountID** with the ID you copied from Meta, then hit enter.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33304909224987)
4. Review and accept the terms of service.

If you received the original error while integrating Klaviyo with Meta Ads for the first time, you should start over with the [integration setup process](https://help.klaviyo.com/hc/en-us/articles/115005082127#h_01HDRXKYW8JVHVNCPZ7KGEK82A).

If you received the original error while editing your existing integration, you should check if the error has resolved in Klaviyo:

1. In Klaviyo, select the ****Integrations**** tab.
2. Select ****Meta Ads**** from the list to be brought to your integration settings page.
3. Try and create a new custom audience. If it works - you’re all set! If you are still receiving the error we recommend re-authenticating your integration:

1. On the same page, click ****Manage integration****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33304909230491)
2. Select ****Re-authenticate****.

You should now be able to create custom audiences within your Meta Ads integration.

If you are still experiencing this error, try following our [authorization error troubleshooting steps](https://help.klaviyo.com/hc/en-us/articles/26909356614299). You can also reach out on the [Community](https://community.klaviyo.com/got-a-question-1) or to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

## Additional resources

[Getting started with Meta Ads](https://help.klaviyo.com/hc/en-us/articles/115005082127)