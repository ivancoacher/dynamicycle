---
id: "33059375555099"
title: "如何为 PrestaShop 启用补货功能"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/33059375555099-How-to-enable-back-in-stock-for-PrestaShop"
section: "PrestaShop"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:39Z"
language: "zh"
---
## 你将会学到

了解如何使用 Klaviyo 为您的 PrestaShop 商店发回库存消息。这个过程有3个步骤：

1. 检查 Klaviyo 中的设置以同步 PrestaShop 变体（也称为组合）
2. 在 PrestaShop 中切换背面库存设置
3. 在 Klaviyo 中创建库存回流

## 开始之前

- 您必须使用我们的 PrestaShop 模块 1.9.0 或更高版本才能访问我们的“退货”功能。了解如何[更新模块](https://help.klaviyo.com/hc/en-us/articles/360054551492#h_01HD6YRW7VWJQKBXTN7TGA7N88)。
- 在开始阅读本文之前，请确保您已[集成 Klaviyo 和 PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360054551492)。

## 检查变体同步设置

首先，您需要检查 Klaviyo 中的设置以从 PrestaShop 同步变体：

1. 选择 PrestaShop 集成的****数据****选项卡。
2. 在标有“**同步目录数据**”的部分中，单击“****重新同步****”。您的目录将开始重新同步。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33061467587611)

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 从列表中选择****PrestaShop****。
3. 在出现的设置页面上，检查 **同步变体** 设置。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33061452698651)
4. 如果您选中了**同步变体**，则默认情况下会选中**同步库存**。此设置将定期同步每个变体的库存量，以确保库存流正常运行。如果您选中**同步变体**但取消选中**同步库存**，您将无法在库存流中使用。但是，您将可以访问用于电子邮件消息传递的变体级别数据。
5. 单击****保存****。
6. 更新款式和/或库存设置后，我们建议重新同步您的目录，以确保更改对所有产品生效。如果您选择根本不重新同步，您的目录项将随着时间的推移单独重新同步，并且仅当变体记录已更新时。目录较大且服务器资源有限的商家可能希望在网站流量较低期间重新同步，以免影响网站性能。要重新同步您的目录：

## 在 PrestaShop 中切换设置

接下来，您需要在 PrestaShop 中切换设置。在切换设置之前，请确保您已在 PrestaShop 中安装了邮件警报模块并已打开产品可用性：

1. 在 PrestaShop 管理员中，导航至****模块 > 模块管理器****。
2. 搜索**邮件警报**。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33132025202331)
3. 找到该模块并单击****安装****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33130254539291)
4. 模块安装后，单击****配置****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33130200155931)
5. 确保****产品可用性****已打开。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33130254552219)
6. 单击****保存****。
7. 导航至****配置 > Klaviyo****。
8. 启用 **电子邮件通知** 开关以在 Klaviyo 中启用库存电子邮件发送功能。请注意，启用该开关也会关闭从 PrestaShop 发送的库存电子邮件。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33130254554139)
9. 选择****保存****应用您的更改。

## 创建退货流程

接下来，您将在 Klaviyo 中设置流程以开始发回库存通知：

1. 首先，在 Klaviyo 中配置您的[返回库存流设置](https://help.klaviyo.com/hc/en-us/articles/115003872251#h_01HBBYXYTAXRW86A1XXE4FRV2T)，其中包括有关最低库存和客户通知的规则。
2. 然后，导航至 Klaviyo 中的****Flows**** 选项卡。
3. 单击****创建流程****。
4. 按 **PrestaShop** 过滤并搜索 **back in stock**。
5. 选择[PrestaShop 中预先构建的库存流程](https://www.klaviyo.com/library/flows?object_id=SEDaDq)。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33061478937883)
6. 在流程构建器中，进行您想要的任何更改并自定义电子邮件。
7. 然后，了解如何[实时设置流程](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8RVQANQHGVRJ6V4W63)。

## 结果

您现在已经为 PrestaShop 商店启用了退货消息功能。