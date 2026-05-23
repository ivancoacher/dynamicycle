<h1>Troubleshooting your WooCommerce integration</h1>

## You will learn

Learn how to solve issues with your WooCommerce integration setup by following the relevant troubleshooting scenario described below. If you are encountering issues not on this list, please reach out on the [Community](https://community.klaviyo.com/got-a-question-1) or to our [Support Team](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support).

## Before you begin

If you have not already, read our guide on [getting started with WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808) for step-by-step instructions on integrating. If you are looking to upgrade your plugin, check out our article on [how to upgrade your WooCommerce plugin](https://help.klaviyo.com/hc/en-us/articles/4418005597723).

## Troubleshooting scenarios

Consult the following scenarios based on the error message received in-app to resolve your issue.

Please note that if you choose to remove your integration and then re-integrate, your WooCommerce data will not be deleted from Klaviyo.

### "To avoid functionality disruptions, you may need to disable the following plugins: **Plugin Name(s)**"

If you have active caching plugins or redirect plugins in WordPress, these can interfere with Klaviyo’s integration and cause connection issues. We recommend disabling these plugins during the integration setup process.

![](https://klaviyo.zendesk.com/hc/article_attachments/28716055944091)

### “We can’t complete your setup”

![](https://klaviyo.zendesk.com/hc/article_attachments/28716066411035)

This message means that either your firewall is blocking Klaviyo’s requests, that you have Bot Fight Mode enabled in Cloudflare, or both.

To resolve, we recommend both allowlisting Klaviyo integration traffic and disabling Bot Fight Mode (if you have it enabled).

1. Learn how to [allowlist Klaviyo integration traffic IP addresses](https://help.klaviyo.com/hc/en-us/articles/19143781289115).
2. To disable Bot Fight Mode in Cloudflare:
   1. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/login).
   2. Select your account and domain.
   3. Go to ****Security > Bots****.
   4. For Bot Fight Mode, select **Off**.

### “Ensure your WooCommerce store has https and SSL enabled”

![](https://klaviyo.zendesk.com/hc/article_attachments/28716055952027)

Klaviyo expects your store URL to adhere to HTTPS protocols, meaning that the website has a valid SSL certificate. If your website is in HTTP rather than HTTPS, you may run into issues.

You can check if your SSL certificate is valid at [SSL Server Test (Powered by Qualys SSL Labs)](https://www.ssllabs.com/ssltest/analyze.html).

Klaviyo requires that the tests pass with A gradings.

### “Unable to access API with provided credentials”

You may receive this error if you have customizations in place to prevent API access for non-logged-in users. Typically, this is a function in the **functions.php** WordPress file, which triggers a 401 status code response.

If you have a customization like this, delete it or comment it out to eliminate the error. For more information on this error, check out [the WooCommerce REST API FAQ](https://developer.wordpress.org/rest-api/frequently-asked-questions/#require-authentication-for-all-requests).

### "Unable to access the orders API, please check connection settings and try again"

This error means that when Klaviyo tries to validate the WooCommerce integration and get an order count, their API doesn’t return a value Klaviyo expects or it returns nothing at all.

Since the integration hasn't officially connected to Klaviyo yet, this means that it needs to be resolved within WooCommerce.

To get more information about this error, you need to make an API call to the order count endpoint, which will provide more insight into what is being passed to Klaviyo. Here is an example cURL request. To use it, fill in your store URL, consumer key, and consumer secret:

```
curl https://STORE_URL/wp-json/wc/v3/orders \
-u CONSUMER_KEY:CONSUMER_SECRET
```

### “Your Klaviyo plugin is out of date”

![](https://klaviyo.zendesk.com/hc/article_attachments/33638394936859)

Occasionally, the webhook will be delayed in reaching Klaviyo, temporarily causing you to see the old settings page. This should resolve itself after a few minutes.

### 404 when connecting to Klaviyo from WordPress

To resolve this, you should confirm that you have Permalinks enabled for your WordPress site. WooCommerce authentication will not work unless Permalinks are enabled.

1. Navigate to your WordPress site and go to ****Settings**** > ****Permalinks****.
2. Under **Common Settings**, choose any link structure other than **Plain**.
3. Confirm by clicking ****Save Changes****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28716055953819)
4. When you’re done, re-integrate with Klaviyo.

### Installation Failed - We were unable to install your extension

You may encounter an "Installation Failed" error when attempting to install the integration via the [WooCommerce Marketplace](https://woocommerce.com/products/klaviyo-for-woocommerce/?utm_source=extensionsscreen&utm_medium=product&utm_campaign=wcaddons&in_app_label=promoted&wccom-site=https%3A%2F%2Fvoluntary-platypus.jurassic.ninja&wccom-back=%252Fwp-admin%252Fadmin.php%253Fpage%253Dwc-admin%2526path%253D%25252Fextensions&wccom-woo-version=10.3.5&wccom-connect-nonce=48111ee6ce&utm_group=discover-our-favorites).

![image (1).png](https://klaviyo.zendesk.com/hc/article_attachments/43279509814939)

In the event you are unable to successfully install from the WooCommerce Marketplace, you can also install the plugin from your Wordpress plugin admin.

1. Navigate to your WordPress admin and go to ****Plugins****.
2. Select ****Add Plugin****.
3. Search for **Klaviyo**in ****Search Plugins****.
4. Select ****Install Now****.
5. Select ****Activate.****
6. Select ****Marketing**** from the lefthand navigation, then click ****Klaviyo****.
7. Click ****Connect Account**** to begin, then proceed to [Enable the WooCommerce integration](https://help.klaviyo.com/hc/en-us/articles/115005255808#h_01FV97DEKASQ117J7HBFCVHBKA) in the [Getting started with WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808) article.
