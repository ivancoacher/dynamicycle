---
id: "15156331062171"
title: "如何为 Amazon Buy with Prime 创建赢回流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15156331062171-How-to-create-a-winback-flow-for-Amazon-Buy-with-Prime"
section: "Amazon Buy with Prime"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:43Z"
language: "zh"
---
## 你将会学到

了解如何创建赢回流程以向您的 Buy with Prime 客户发送提醒。流程也称为自动化或点滴活动，是 Klaviyo 与客户进行个性化沟通的工具。赢回流程会重新吸引过去购买过但一段时间没有再次购买的客户。 ## 开始之前

- 如果您尚未设置集成，请按照我们的[Prime 购买入门](https://help.klaviyo.com/hc/en-us/articles/14708088221467) 指南获取分步说明。 - 要创建流程，您还需要将 Klaviyo 与您的电子商务平台集成。要了解如何集成（如果您尚未集成），请[在我们的帮助中心查找您的电子商务平台](https://help.klaviyo.com/hc/en-us/categories/115000032731-Integrations)。 - 想要了解有关 Klaviyo 中流程如何运作的更多信息？查看[流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)。使用 Prime 购买订单数据仅同步具有电子邮件地址的个人资料。 ## 关于 Buy with Prime 流程和您的电子商务平台

要使用“Buy with Prime”数据创建流程，您还需要使用从电子商务平台同步到 Klaviyo 的数据。这是因为一些必要的数据（例如您的产品目录和直接在电子商务平台上进行的购买的数据）不会通过 Buy with Prime 集成同步。在 Klaviyo 中，您可以使用我们的流程库中的预构建流程，也可以从头开始创建流程。目前，Klaviyo 仅为 Shopify 提供预构建的 Buy with Prime 流程，但针对其他电子商务平台（例如 WooCommerce、BigCommerce 和 Adob​​e Magento）的预构建流程即将推出。非 Shopify 用户今天仍然可以创建 Buy with Prime 流程，但必须从头开始构建。我们将在本文中向您展示如何操作。 ## 如何创建赢回流程

赢回流程可根据客户购买的产品及其购买数量进行定制。如果您已经使用电子商务平台中的数据创建了赢回流程，则应使用“Buy with Prime”数据创建第二个相同类型的流程，因为您的原始流程不会考虑使用“Buy with Prime”下原始订单的客户。我们还建议在您的原始赢回流程中添加额外的流程过滤器，以便在您的 Klaviyo 帐户中考虑现在的“使用 Prime 购买”数据：

- **下订单**（使用 Prime 购买）**自开始此流程以来零次**。 ### 对于 Shopify 客户

1. 在您的 Klaviyo 帐户中，选择****Flows**** 选项卡。 2. 单击右上角的****创建流****。 3. 使用下拉菜单按 **Amazon Buy with Prime** 进行筛选。 ![Klaviyo 中的 Flows 选项卡由 Amazon Buy with Prime 过滤](https://klaviyo.zendesk.com/hc/article_attachments/28720896431643)
4. 选择流程****客户赢回****，然后在出现的窗口中单击****创建流程****。 ![使用 Prime Shopify Winback 流程预览购买](https://klaviyo.zendesk.com/hc/article_attachments/28720901772443)
5. 在流程构建器中，自定义流程及其中的电子邮件以适合您的品牌。要了解有关赢回流程最佳实践的更多信息，请阅读我们的文章[如何创建赢回流程](https://help.klaviyo.com/hc/en-us/articles/115002775192)。 6. 当您准备好开始向客户发送废弃购物车消息时，您可以[将流程状态更改为实时或手动](https://help.klaviyo.com/hc/en-us/articles/115002774932#set-the-flow-action-status7)。 ### 对于非 Shopify 客户

1. 在您的 Klaviyo 帐户中，选择****Flows**** 选项卡。 2. 单击右上角的****创建流****，然后单击右上角的****从头开始创建****。 3. 为您的流程命名（例如，使用 Prime Winback 购买）并添加任何标签，然后单击****创建流程****。 4. 在流程构建器中，设置基于指标的触发器：**已下订单（使用 Prime 购买）。**
5. 设置 2 个流量过滤器：

1. **自开始此流程以来下订单（使用 Prime 购买）零次**
   和
2. 自开始此流程以来，**下订单（**您的电子商务平台 - 例如 BigCommerce**）为零次。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720901774619)**

6. 增加75天的时间延迟。 7. 添加您的第一封客户赢回电子邮件。 8. 增加15天的时间延迟。 9. 添加您的第二个客户赢回电子邮件。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720901779355)
10. 个性化您的流程电子邮件和功能更新，例如新产品或热门产品。 了解更多信息，请参阅[如何创建赢回流程](https://help.klaviyo.com/hc/en-us/articles/115002775192)。 11. 当您准备好开始向客户发送赢回消息时，您可以[将流程状态更改为实时或手动](https://help.klaviyo.com/hc/en-us/articles/115002774932#set-the-flow-action-status7)。 ## 结果

您现在已经了解了如何使用“Buy with Prime”数据创建赢回流程。 ## 其他资源

- 了解如何将 Amazon 和 Klaviyo 与 [Amazon Buy with Prime 入门] 集成 (https://help.klaviyo.com/hc/en-us/articles/14708088221467)
- 通过 [Buy with Prime 数据参考] 了解 Amazon 和 Klaviyo 之间同步的数据(https://help.klaviyo.com/hc/en-us/articles/14708160794779)