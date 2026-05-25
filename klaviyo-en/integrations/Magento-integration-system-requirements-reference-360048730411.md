---
id: "360048730411"
title: "Magento integration system requirements reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360048730411-Magento-integration-system-requirements-reference"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:49Z"
language: "en"
---
## You will learn

Learn about the system requirements for optimal syncing with Magento 1 or 2. The administrator of your Magento store is responsible for system specifications and configuration. Ensuring that your system is configured to work with Klaviyo will enable a smooth integration experience.

## Configure API user permissions

In the process of integrating your Magento store with Klaviyo, you will create a new [SOAP](https://help.klaviyo.com/hc/en-us/articles/115005082187#set-up-magento-api-credentials1) (for Magento 1) or [REST](https://help.klaviyo.com/hc/en-us/articles/115005254348-Integrate-with-Magento-2-x-CE-and-EE-%23setup-your-magento-api-credentials2) (for Magento 2) role with full resource access and assign a new user to this role. Ensure **Resource Access** is set to **All**.

Without the necessary permissions for this API user, Klaviyo will not be able to properly interact with your Magento store’s APIs, which will prevent the integration from retrieving data from your store.

## Enable access to required API endpoints

Klaviyo requests data from specific endpoints. Your system configurations must allow access to these endpoints; consider the impact of security controls or URL redirection logic on the accessibility of these endpoints to Klaviyo. If Klaviyo does not have access to the expected API endpoints, some or all Magento data will be unable to sync and you will see error reporting in the application.

All outbound Klaviyo integration traffic is behind a set of predictable, static IP addresses so that you can have a high level of confidence that this traffic is coming from Klaviyo; we recommend [allowlisting these addresses](https://help.klaviyo.com/hc/en-us/articles/19143781289115).

## System capacity for historical data sync API requests

When you activate the integration, Klaviyo automatically queues API requests to sync historical data including customer records, order records, and the product catalog. We attempt to do this quickly to empower marketers to use this data in their accounts as soon as possible. We also attempt to do this responsibly by limiting concurrency and by gracefully handling retries. If your store has a high volume of historical data, limited resource capacity, or other applications that make substantial API requests, we recommend consulting your Magento administrator to ensure your infrastructure is equipped to support the historical data sync. Your administrator may want to consider temporarily increasing resources or applying auto-scaling.

If you have concerns about the volume of historical data or the server's ability to handle a temporary increase of API requests to fetch this data, consider temporarily scaling up server resources, applying auto-scaling.

## Verify SSL certificate validity

An SSL certificate digitally authenticates the identity of a website and enables an encrypted connection between a web browser and a web server. Your website’s SSL certificate is hosted by the site’s origin server. A valid SSL certificate is critical to accepting payment securely, protecting password logins, and securing web forms. [This tool](https://www.ssllabs.com/ssltest/analyze.html?viaform=on&d=) can be used to verify a website’s SSL certificate.

Magento integrations may become disabled if your website’s SSL certification expires. In this case, the domain and intermediate certifications must be updated on the hosting provider. If you are unsure of the location of your certifications, reach out to your host provider for assistance

## Sufficient server memory allocation

The amount of disk space required by an ecommerce website depends on a variety of factors, including the number of products, the number of images for each product, the quality of the images, the number of emails stored on the server, and static content pages.

We recommend over 1 gigabyte of memory allocated to your Klaviyo integration, but 512 megabytes is the required minimum. If your server cannot allocate sufficient resources to respond to Klaviyo’s requests, integration errors will occur. The Klaviyo-Magento integration begins with a sync of historical data, so it is recommended you verify memory settings in Magento and your server before activating the integration.

The default Magento PHP memory setting is 128 megabytes. This setting can be updated in the php.ini file, by changing the value of the “memory\_limit” variable to the recommended 1024 megabytes.

## Set timezone to UTC

Coordinated Universal Time, or UTC, has been the world’s primary time standard since the 1960s. Klaviyo relies on UTC to schedule syncs of your most recent data.

If your Magento instance uses a different timezone, it will be more difficult for Klaviyo to determine which data is most recent and should be synced. Your timezone should be [updated to UTC](https://www.simicart.com/blog/set-configure-timezone-magento/) in both your Magento backend and in the app/Mage.php as well as app/code/local/Mage/Core/Model/Locale.php files.

## Additional resources

- [How to Integrate with Magento 1.x (CE and EE)](https://klaviyo.zendesk.com/hc/en-us/articles/115005082187)
- [How to integrate with Magento 2.x (CE and EE)](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348)