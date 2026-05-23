---
id: 5510750923035
title: "Troubleshooting your Magento 2 integration"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/5510750923035-Troubleshooting-your-Magento-2-integration"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:03Z"
language: en
---

## You will learn

Learn how to solve issues with your Magento 2 OAuth setup by following the troubleshooting steps described below. If you are still encountering issues after running through these steps, please reach out on our [Community](https://community.klaviyo.com/got-a-question-1) or [to our Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

## Before you begin

If you have not already, read our guide on [Getting started with Magento 2](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-) for step-by-step instructions to set up your Magento 2 integration.

Klaviyo uses the OAuth protocol to generate an access token and retrieve data from your Magento 2 store. If you’ve customized your Magento 2 installation, it can cause Klaviyo’s OAuth procedure to fail. This article will guide you through a series of troubleshooting steps to identify where the failure is occurring.

## General troubleshooting steps

### Ensure your site is publicly accessible with a valid SSL certificate

Klaviyo’s OAuth procedure requires that your website is publicly accessible, otherwise the necessary API calls to generate the access tokens will fail.

1. Ensure you have not password protected or IP restricted access to your store.
2. Ensure that your store is accessible via HTTPS with a valid SSL certificate. You can test your certificate [here](https://www.ssllabs.com/ssltest/analyze.html).

### Ensure your firewall is not blocking Klaviyo’s requests

All outbound Klaviyo integration traffic is behind a set of predictable, static IP addresses so that you can have a high level of confidence that this traffic is coming from Klaviyo. Read our article to learn [how to allowlist Klaviyo integration traffic IP addresses](https://help.klaviyo.com/hc/en-us/articles/19143781289115).

### Check your Magento 2 and Klaviyo extension versions

1. If you are using Magento v2.2.0, you'll need to [manually enable OAuth](https://help.klaviyo.com/hc/en-us/articles/4403350880411).
2. Make sure you’ve installed the correct Klaviyo extension (you may need to [upgrade](https://help.klaviyo.com/hc/en-us/articles/115005254348#h_01HNZMK310HQPFJWZ2NB1C6NSC)).

### Ensure OAuth endpoints are accessible

You may have extra or missing rewrite rules which can make the default Magento 2 OAuth endpoints inaccessible. Klaviyo needs to access these endpoints to generate the necessary credentials for the authorization process.

Ensure that URLs below are accessible for your store:

```
https://[Store URL]/oauth/token/request
```

```
https://[Store URL]/oauth/token/access
```

1. You can validate that they’re accessible by making a POST request like this:

   ```
   curl --location --url 'https://[Store URL]/oauth/token/request' --request 'POST' -v
   ```

   ```
   curl --location --url 'https://[Store URL]/oauth/token/access' --request 'POST' -v
   ```
2. You should expect a response similar to the following. It is normal to see an error when making a request in this manner, and it validates the endpoints are responding correctly.
   ![curloauthendpoint.png](https://klaviyo.zendesk.com/hc/article_attachments/28713384135323)
3. If you do not receive a response related to OAuth, you should check that there are no redirects, invalid rewrite rules, or internal server errors preventing access to these URLs.

This can be caused by a store subpath in your URL. Test for a store subpath issue by accessing the endpoints at:

```
https://[Store URL]/[Store Path]/oauth/token/request
```

```
https://[Store URL]/[Store Path]/oauth/token/access
```

If these endpoints resolve, then include the below rewrite rules in your .htaccess file to solve the issue.

```
RewriteEngine on
RewriteRule /oauth/token/request$ https://%{HTTP_HOST}/[Store Path]/oauth/token/request [L,R=301]
RewriteRule /oauth/token/access$ https://%{HTTP_HOST}/[Store Path]/oauth/token/access [L,R=301]
```

### Delete the integration and re-create it

If you’ve made changes after a previous failed integration attempt, it is a good idea to delete the original OAuth integration. The keys used may be invalid and will need to be regenerated.

1. Within Magento, navigate to ****Systems****
2. Select ****Integrations****
3. Locate the Klaviyo integration record and delete it

Once the integration record is deleted, follow the steps in our [how to integrate with Magento 2](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-#setup-oauth7) guide to create a new integration record and try again.

## Magento version-specific issues

### Failure specific to Magento 2.4.2

If you’re using Magento 2.4.2, there is a known issue where OAuth activations fail. Upon activating the integration, you may see an error message like the one shown below. Even if you don’t receive the error, the OAuth activation may have failed. Normally, the error can be found in your Magento logs.

![m2oauthfailed.png](https://klaviyo.zendesk.com/hc/article_attachments/28713384127643)

In order to resolve this error, you will need to either:

- Upgrade to Magento 2.4.3. View Magento 2's documentation to [upgrade your version](https://devdocs.magento.com/cloud/project/project-upgrade.html).
- Apply a patch as described [on Klaviyo's github repository](https://github.com/klaviyo/magento2-klaviyo/issues/122) for Magento 2.

### Authentication failure specific to Magento 2.4.6

Are you on Magento 2.4.6 and experiencing a 401 authentication error after integrating with Klaviyo? This could be due to a known Magento bug affecting Magento version 2.4.6. To solve this, you'll need to enable bearer token authentication so that Klaviyo can make requests using it (instead of OAuth 1.0). To enable bearer token authentication:

1. In your Magento admin, navigate to ****Stores > Configuration > Services > OAuth > Consumer Settings****.
2. For the setting **Allow OAuth Access Tokens to be used as stand-alone Bearer tokens**, select **Yes**.
3. Click ****Save Config****.

![](https://klaviyo.zendesk.com/hc/article_attachments/28713384150683)

After making this update, your previous authentication errors should resolve and integration syncs will resume.