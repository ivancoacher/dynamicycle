---
id: 115005254468
title: "How to Set Up a Magento Cron Job (for Magento 1.x)"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254468-How-to-Set-Up-a-Magento-Cron-Job-for-Magento-1-x"
section: "Magento 1"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:40Z"
language: en
---

## Overview

Cron jobs, or scheduled tasks, must be set up for Magento to stay up-to-date and run periodic maintenance tasks. Klaviyo's Magento Extension uses the built-in Magento cron job functionality to send data to Klaviyo that can't be sent by the Magento API.

If you've [installed and configured the Klaviyo Magento Extension](https://help.klaviyo.com/hc/en-us/articles/115005254308-Install-the-Klaviyo-Extension-in-Magento-for-Magento-1-0-), but you're not seeing checkout data show up in Klaviyo, it might be because Magento's cron job isn't running. It's straightforward to set up if you have access to the server Magento is installed on.

(For more detailed information about Magento's cron jobs, you can read their documentation here: <http://www.magentocommerce.com/wiki/1_-_installation_and_configuration/how_to_setup_a_cron_job>.)

## Setting up Cron In a UNIX Based Operating System

If you have shell access to your server, you can use the crontab service command. If you don't have shell access, you can set up the cron job through cPanel or similar admin. The Magento cron needs to run every five minutes, so the time configuration is:

```
*/5 * * * *
```

The full line in crontab will look like one of these (we suggest the first version):

```
*/5 * * * * /bin/sh MAGENTO_PATH/cron.sh
*/5 * * * * /bin/bash MAGENTO_PATH/cron.sh
*/5 * * * * /usr/bin/php MAGENTO_PATH/cron.php
*/5 * * * * /usr/local/bin/php -f MAGENTO_PATH/cron.php
```

where `MAGENTO_PATH` is the location of your Magento installation on the server.

## Setting up Cron Using cPanel

Log into cPanel for your hosting account. Then find the Advanced section or the section that contains the "Cron Jobs" icon.

![647750](https://klaviyo.zendesk.com/hc/article_attachments/28717380134939)

Click on the "Cron Jobs" icon. That'll show a list of current cron jobs as well as a form to add a new one. Enter the following setting in the "Add New Cron Job" form. Make sure to replace `MAGENTO_PATH` with the path to your Magento installation. If you're not sure what the path is or how to find it, you can an FTP program to browse the files on your server and find the directory that contains the `cron.sh` file.

![647751](https://klaviyo.zendesk.com/hc/article_attachments/28717380143515)

After you add the new cron job, you're all set. You should see checkout data in Klaviyo within 15 minutes.