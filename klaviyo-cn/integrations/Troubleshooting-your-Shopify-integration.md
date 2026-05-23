---
id: "4403927899291"
title: "对 Shopify 集成进行故障排除"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4403927899291-Troubleshooting-your-Shopify-integration"
section: "Shopify troubleshooting"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:58Z"
language: "zh"
---
## 你将会学到

了解如何按照下述相关故障排除方案解决 Shopify 集成设置的问题。如果您遇到的问题不在此列表中，请联系我们的[社区](https://community.klaviyo.com/got-a-question-1)或[联系我们的支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。 ## 开始之前

如果您还没有阅读我们关于[Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) 的指南，了解有关集成的分步说明，而不是继续阅读本文。 ## 目录

以下是本文将介绍的故障排除场景：

- 集成设置页面无法识别我的商店 URL
- 我的 Shopify 集成未同步
- 我收到错误：**我们目前无法更新您的集成设置。请刷新或稍后重试**
- 当我尝试将第二个 Shopify 帐户添加到我的 Klaviyo 帐户时，我无法执行此操作
- 我的 Shopify 集成似乎正常工作，但我仍然收到应用内通知，提示同步出现问题
- 现场跟踪不起作用

## 故障排除场景

### 集成设置页面无法识别我的商店 URL

如果您在“集成设置”页面上收到一条错误消息，表明您的商店 URL 不正确，请确保该 URL 遵循 **mystore.myshopify.com.** 模式。

![在 Shopify 集成设置页面上存储 URL，没有错误，URL 末尾缺少前缀或正斜杠](https://klaviyo.zendesk.com/hc/article_attachments/28723632853275)

### 我的 Shopify 集成未同步

如果您认为您的 Shopify 集成未正确同步数据，请通过完成以下步骤来更新同步：

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 选择****Shopify****。 3. 单击****更新设置****。如果您未登录 Shopify 商店，您将被重定向到 Shopify 并提示登录。 4. 单击****更新您的集成设置。**** 我们将使用 Shopify 重新进行身份验证，然后您将返回到 Klaviyo。如果您单击更新，然后单击后退按钮或在此身份验证过程完成之前导航到其他位置，这将禁用您的集成。 5. 页面顶部的 **设置已更新** 标注将确认您的集成已更新并正在重新同步。这可能需要一分钟才会出现。 ### 我收到错误：**我们目前无法更新您的集成设置。请刷新或稍后重试**

如果您在点击 **连接到 Shopify** 后收到此错误，可能有多种原因。 ![Shopify 集成设置页面，带有红色背景的错误框，我们目前无法更新您的集成设置](https://klaviyo.zendesk.com/hc/article_attachments/28723661024923)

首先，如果您在 **商店 URL** 框中提供了不正确的 Shopify URL，则可能会收到此错误。在尝试连接之前，请确保您的商店名称拼写正确。您可能收到此错误的另一个原因是您的 Shopify 商店当前被冻结。如果您需要选择计划、支付未结余额或免费试用已过期，则可能会发生这种情况。在尝试连接到 Klaviyo 之前，登录 Shopify 并解决问题。此外，如果 Shopify 删除了您的商店，或者在 Shopify 中卸载了 Klaviyo 应用程序，则可能会出现此错误。请务必检查您是否在 Shopify 中安装了 [Klaviyo 应用程序](https://apps.shopify.com/klaviyo-email-marketing)。 ### 当我尝试将第二个 Shopify 帐户添加到我的 Klaviyo 帐户时，我无法执行此操作

Klaviyo 目前不支持每个 Klaviyo 帐户拥有多个 Shopify 商店。如果您有两个 Shopify 帐户，则需要将它们连接到单独的 Klaviyo 帐户。请前往[多帐户用户权限](https://help.klaviyo.com/hc/en-us/articles/360002165611-About-Multi-Account-User-Privileges)了解更多信息。 ### 我的 Shopify 集成似乎正常工作，但我仍然收到应用内通知，提示同步出现问题

![Klaviyo 中通知 Shopify 定期同步失败](https://klaviyo.zendesk.com/hc/article_attachments/28723661030171)

如果您的 Shopify 集成问题最近得到解决，您可能仍会在应用内看到此错误。 忽略此错误，除非您继续看到集成问题，例如数据未[及时]流入您的帐户(https://help.klaviyo.com/hc/en-us/articles/115005253208-How-Often-Integrations-Sync)。 ### 现场跟踪不起作用

您最近是否在 Shopify 商店中添加了全新主题？如果是这样，在您为新主题重新启用 Klaviyo 应用程序嵌入之前，现场跟踪将无法工作。您可以[按照本文中的说明进行操作](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01HGK7749T3NPE3XKEYTDHKJ98)

## 故障排除常见问题解答

正在寻找 Shopify 常见问题解答？在我们的[社区](https://community.klaviyo.com/search?q=shopify) 上查看其他客户问题的快速解答。