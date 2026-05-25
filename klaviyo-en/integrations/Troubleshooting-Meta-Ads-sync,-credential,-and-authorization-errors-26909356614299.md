---
id: "26909356614299"
title: "Troubleshooting Meta Ads sync, credential, and authorization errors"
source_url: "https://help.klaviyo.com/hc/en-us/articles/26909356614299-Troubleshooting-Meta-Ads-sync-credential-and-authorization-errors"
section: "Meta Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-16T22:46:51Z"
language: "en"
---
## You will learn

Learn how to resolve sync, credential, and authorization errors with your Meta Ads integration.

Have you received one of the following error messages or emails?

- **Your Meta Ads integration is no longer syncing as expected. Klaviyo is no longer authorized to connect to Meta Ads.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/28981090659867)**
- **Your credentials have expired. Check your Meta Ad Manager permissions and re-authenticate to resume syncing.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/28981077652763)**
- **Klaviyo is no longer authorized to connect to Meta Ads. Please check Meta Ads and update your settings to re-enable sync.
  ![](https://klaviyo.zendesk.com/hc/article_attachments/35587393816859)**

To solve these errors, we recommend updating your permissions, accepting Meta's terms of service, and then re-authenticating your Meta Ads integration by following the steps below. These errors can occur from a variety of root causes. Even if you’re not sure of the root cause, the steps below can solve a variety of issues.

## Troubleshooting steps

### Review your Meta account and settings

First, confirm you have complete control of your Meta Business Account, Facebook page, and Advertising account.

1. Visit your [Meta Business settings](https://business.facebook.com/latest/settings/).
2. At the link, click your user name under **People.**
3. If you are using Lead Ads: make sure the Facebook page you wish to connect to Klaviyo has **Full control** permissions. If it does not, click ****Manage**** and adjust the permissions. Once you have full control, you can continue.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715966407579)
4. If you are using Custom Audiences: make sure the Ad account you wish to connect to Klaviyo has **Full control** permissions. If it does not, click ****Manage**** and adjust the permissions. Once you have full control, you can continue.

### Accept Meta’s terms of service

To accept Meta's terms of service:

1. Copy and paste the following URL into your browser, but do not hit enter:

   ```
    https://business.facebook.com/ads/manage/customaudiences/tos/?act=AdAccountID
   ```

   ![](https://klaviyo.zendesk.com/hc/article_attachments/35584051538715)
2. You'll need to update the link above by changing **AdAccountID** to your specific ad account ID from Meta. To find this ID:

1. Open a new tab and navigate to [Ad accounts in Meta’s business settings](https://business.facebook.com/settings/ad-accounts).
2. Select your ad account on the left.
3. Find the account ID, under the account name on the right.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35584051541659)
4. Copy the ID.

3. In your original tab, replace **AdAccountID** with the ID you copied from Meta, then hit enter.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35584051545755)
4. Review and accept the terms of service.

### Re-authenticate Klaviyo and Meta Ads

1. In Klaviyo, select the ****Integrations**** tab.
2. Find **Meta Ads** on the list and select it.
3. On your settings page, click ****Manage integration > Re-authenticate**** in the upper right corner.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35584028377371)

Your integration should now start syncing normally.

If you are still experiencing issues, try reaching out on the [Community](https://community.klaviyo.com/got-a-question-1) or to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

## Additional resources

[Getting started with Meta Ads](https://help.klaviyo.com/hc/en-us/articles/115005082127)