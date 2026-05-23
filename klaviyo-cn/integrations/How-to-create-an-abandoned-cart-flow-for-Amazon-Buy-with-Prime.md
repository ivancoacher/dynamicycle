---
id: "14985388418331"
title: "如何为 Amazon Buy with Prime 创建废弃购物车流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/14985388418331-How-to-create-an-abandoned-cart-flow-for-Amazon-Buy-with-Prime"
section: "Amazon Buy with Prime"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:28Z"
language: "zh"
---
## 你将会学到

了解如何创建废弃购物车流程以向您的 Buy with Prime 客户发送提醒。流程也称为自动化或点滴活动，是 Klaviyo 与客户进行个性化沟通的工具。放弃的购物车流是发送给将商品添加到购物车但未能完成购买的用户的消息或消息序列。 ## 开始之前

- 如果您尚未设置集成，请按照我们的[Prime 购买入门](https://help.klaviyo.com/hc/en-us/articles/14708088221467) 指南获取分步说明。 - 要创建流程，您还需要将 Klaviyo 与您的电子商务平台集成。要了解如何集成（如果您尚未集成），请[在我们的帮助中心查找您的电子商务平台](https://help.klaviyo.com/hc/en-us/categories/115000032731-Integrations)。 - 想要了解有关 Klaviyo 中流程如何运作的更多信息？查看[流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)。使用 Prime 购买订单数据仅同步具有电子邮件地址的个人资料。 ## 关于 Buy with Prime 流程和您的电子商务平台

要使用“Buy with Prime”数据创建流程，您还需要使用从电子商务平台同步到 Klaviyo 的数据。这是因为一些必要的数据（例如您的产品目录和直接在电子商务平台上进行的购买的数据）不会通过 Buy with Prime 集成同步。在 Klaviyo 中，您可以使用我们的流程库中的预构建流程，也可以从头开始创建流程。目前，Klaviyo 仅为 Shopify 提供预构建的 Buy with Prime 流程，但针对其他电子商务平台（例如 WooCommerce、BigCommerce 和 Adob​​e Magento）的预构建流程即将推出。非 Shopify 用户今天仍然可以创建 Buy with Prime 流程，但必须从头开始构建。我们将在本文中向您展示如何操作。 ## 如何创建废弃的购物车流程

提醒顾客注意他们的购物车可以极大地防止销售损失：平均近 70% 的购物车被放弃。对于 Buy with Prime，此流程由 **Checkout Started** 事件触发，当客户在其 Buy with Prime 购物车上点击 **Proceed to checkout** 并通过 Amazon 进行身份验证时，就会跟踪该事件。此流程也有时间延迟，它会过滤掉从您网站购买的所有用户，无论是使用“Buy with Prime”（通过“Buy with Prime **已下订单**”事件），还是直接在您网站的结账页面（通过您的电子商务平台的“**已下订单**”事件）。如果您已使用电子商务平台中的数据创建了废弃购物车流程，则应使用“Buy with Prime”数据创建第二个相同类型的流程，因为您的原始流程不会考虑使用“Buy with Prime”开始结账的客户。我们建议在您的原始废弃购物车流程中添加一个额外的流程过滤器，即自启动此流程以来 **Buy with Prime 已下订单零次**。这将排除通过 Buy with Prime 进行购买的客户收到错误消息的情况。 ## 对于 Shopify 客户

1. 在您的 Klaviyo 帐户中，选择****Flows**** 选项卡。 2. 单击右上角的****创建流****。 3. 使用下拉菜单按 **Amazon Buy with Prime** 进行筛选。 ![由 Amazon Buy with Prime 过滤的 Klaviyo 流库](https://klaviyo.zendesk.com/hc/article_attachments/28723661762971)
4. 选择流程****放弃购物车提醒****，然后在出现的窗口中单击****创建流程****。 ![使用 Prime 和 Shopify 流程以及黑色背景的创建流程预构建废弃购物车购买](https://klaviyo.zendesk.com/hc/article_attachments/28723633610907)
5. 在流程构建器中，自定义流程及其中的电子邮件以适合您的品牌。流程电子邮件将自动配置为向客户显示他们留下的商品，并通过 **返回购物车** 按钮将他们带回购物车。要了解有关废弃购物车流程最佳实践的更多信息，请阅读我们的文章[如何创建废弃购物车流程](https://help.klaviyo.com/hc/en-us/articles/115002779411)。 6. 当您准备好开始向客户发送废弃购物车消息时，您可以[将流程状态更改为实时或手动](https://help.klaviyo.com/hc/en-us/articles/115002774932#set-the-flow-action-status7)。 ## 对于非 Shopify 客户

1. 在您的 Klaviyo 帐户中，选择****Flows**** 选项卡。 2. 单击右上角的****创建流****，然后单击右上角的****从头开始创建****。 3. 为您的流程命名（例如，使用 Prime Abandoned Cart 购买）并添加任何标签，然后单击****创建流程****。 4. 设置基于指标的触发器：**结账开始（使用 Prime 购买）。**
5. 设置 2 个流量过滤器：
   a. **自开始此流程以来已下订单（使用 Prime 购买）零次**
   和
   b.自开始此流程以来，**下订单（**您的电子商务平台 - 例如 BigCommerce**）为零次。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723661769883)**
6.增加4小时的时间延迟。 7. 添加您的第一个废弃购物车电子邮件提醒。 8.增加20小时的延时。 9. 添加第二个废弃购物车电子邮件提醒。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723633614875)
10. 通过使用[动态模板变量](https://help.klaviyo.com/hc/en-us/articles/115000096232)将“Buy With Prime”产品数据拉入电子邮件[文本块](https://help.klaviyo.com/hc/en-us/articles/115005082447#text-blocks4)，个性化您的流程电子邮件以展示客户购物车中留下的商品。了解更多信息，请参阅[如何创建废弃的购物车流程](https://help.klaviyo.com/hc/en-us/articles/115002779411)。 11. 当您准备好开始向客户发送废弃购物车消息时，您可以[将流程状态更改为实时或手动](https://help.klaviyo.com/hc/en-us/articles/115002774932#set-the-flow-action-status7)。 ## 结果

您现在已经了解了如何使用“Buy with Prime”数据创建废弃购物车流程。 ## 其他资源

- 了解如何将 Amazon 和 Klaviyo 与 [Amazon Buy with Prime 入门] 集成 (https://help.klaviyo.com/hc/en-us/articles/14708088221467)
- 通过 [Buy with Prime 数据参考] 了解 Amazon 和 Klaviyo 之间同步的数据(https://help.klaviyo.com/hc/en-us/articles/14708160794779)