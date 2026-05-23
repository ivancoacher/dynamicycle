---
id: "115005254468"
title: "如何设置 Magento Cron 作业（适用于 Magento 1.x）"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254468-How-to-Set-Up-a-Magento-Cron-Job-for-Magento-1-x"
section: "Magento 1"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:40Z"
language: "zh"
---
## 概述

必须为 Magento 设置 Cron 作业或计划任务，以保持最新状态并运行定期维护任务。 Klaviyo 的 Magento 扩展使用内置的 Magento cron 作业功能将 Magento API 无法发送的数据发送到 Klaviyo。

如果您已[安装并配置了 Klaviyo Magento 扩展程序](https://help.klaviyo.com/hc/en-us/articles/115005254308-Install-the-Klaviyo-Extension-in-Magento-for-Magento-1-0-)，但您没有在 Klaviyo 中看到结账数据，可能是因为 Magento 的 cron 作业没有显示运行。如果您有权访问安装 Magento 的服务器，则设置起来很简单。

（有关 Magento 的 cron 作业的更多详细信息，您可以在此处阅读其文档：<http://www.magentocommerce.com/wiki/1_-_installation_and_configuration/how_to_setup_a_cron_job>。）

## 在基于 UNIX 的操作系统中设置 Cron

如果您有服务器的 shell 访问权限，则可以使用 crontab 服务命令。如果您没有 shell 访问权限，您可以通过 cPanel 或类似的管理工具设置 cron 作业。 Magento cron需要每五分钟运行一次，因此时间配置为：

````
* / 5 * * * *
````

crontab 中的完整行将类似于以下之一（我们建议使用第一个版本）：

````
*/5 * * * * /bin/sh MAGENTO_PATH/cron.sh
*/5 * * * * /bin/bash MAGENTO_PATH/cron.sh
*/5 * * * * /usr/bin/php MAGENTO_PATH/cron.php
*/5 * * * * /usr/local/bin/php -f MAGENTO_PATH/cron.php
````

其中“MAGENTO_PATH”是服务器上 Magento 安装的位置。

## 使用 cPanel 设置 Cron

登录您的托管帐户的 cPanel。然后找到“高级”部分或包含“Cron Jobs”图标的部分。

![647750](https://klaviyo.zendesk.com/hc/article_attachments/28717380134939)

单击“计划任务”图标。这将显示当前 cron 作业的列表以及用于添加新作业的表单。在“添加新 Cron 作业”表单中输入以下设置。确保将“MAGENTO_PATH”替换为 Magento 安装路径。如果您不确定路径是什么或如何找到它，您可以使用 FTP 程序浏览服务器上的文件并找到包含“cron.sh”文件的目录。

![647751](https://klaviyo.zendesk.com/hc/article_attachments/28717380143515)

添加新的 cron 作业后，一切就完成了。您应该会在 15 分钟内看到 Klaviyo 的结账数据。