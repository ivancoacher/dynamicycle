---
id: "13323494909083"
title: "如何为 Shopware 创建废弃购物车流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/13323494909083-How-to-create-an-abandoned-cart-flow-for-Shopware"
section: "Shopware"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:42Z"
language: "zh"
---
## 你将会学到

了解如何为 Shopware 6 创建废弃购物车流程，以增加您的电子商务收入并实现与客户的个性化沟通。此流程将使用从您的 Shopware 商店同步的 **开始结帐** 事件。

## 开始之前

在创建此流程之前，请确保执行以下操作：

- 将 Klaviyo 与 Shopware 6 集成（请参阅 [Shopware 6 入门](https://help.klaviyo.com/hc/en-us/articles/13001662470939) 了解具体操作方法）。作为集成过程的一部分，请确保：

- 同步**开始结账**和**下订单**事件。这需要您在扩展程序设置中打开它们。
  ![跟踪已开始结帐和跟踪已下订单切换为蓝色](https://klaviyo.zendesk.com/hc/article_attachments/28705638160667)
- 将您的 Shopware 6 产品目录同步到 Klaviyo。

## 创建流程

1. 在 Klaviyo 中，选择****流程****选项卡。
2. 单击****创建流****。
3. 搜索 **放弃的购物车**，然后选择 ****放弃的购物车提醒：自定义电子商务购物车的标准**** 流程。

- 出于 Klaviyo 流程的目的，Shopware 是一种定制的电子商务购物车。 Klaviyo 为自定义电子商务购物车提供带有预填充数据的预构建流程。
  ![废弃购物车提醒：自定义电子商务购物车的标准流程卡](https://klaviyo.zendesk.com/hc/article_attachments/28705638158619)
- 出现的窗口将向您概述流程的工作原理以及触发该流程的事件（在本例中为 **开始结账**，从 Shopware 同步）。此流程还依赖 **已下订单** 事件进行过滤。
- 单击****创建流程****。
  ![通过开始结帐预览触发废弃购物车提醒流程，并以白色和黑色背景创建流程](https://klaviyo.zendesk.com/hc/article_attachments/28705638162459)
- 在流程构建器中，自定义流程及其中的电子邮件以适合您的品牌。流程电子邮件将自动配置为向客户显示他们留下的商品，并通过 **返回购物车** 按钮将他们带回购物车。要了解有关废弃购物车流程最佳实践的更多信息，请阅读我们的文章[如何创建废弃购物车流程](https://help.klaviyo.com/hc/en-us/articles/115002779411)。
  ![Klaviyo 模板生成器显示电子邮件，感谢您的光临并以蓝色背景白色返回您的购物车](https://klaviyo.zendesk.com/hc/article_attachments/28705638164635)
- 当您准备好开始向客户发送废弃购物车消息时，您可以[将流程状态更改为实时或手动](https://help.klaviyo.com/hc/en-us/articles/115002774932#set-the-flow-action-status7)。

需要注意的是，购物车只能在创建之日起 120 天内重建；之后，它们就会过期。

## 结果

您已经为 Shopware 6 创建了废弃购物车流程，现在可以更好地个性化您的客户沟通并增加收入。

## 其他资源

- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [如何使用动态事件数据个性化流](https://help.klaviyo.com/hc/en-us/articles/115002779071-Personalize-Flow-Emails-with-Dynamic-Event-Data)
- [如何利用废弃购物车电子邮件来提高销量：策略、示例和专家建议](https://www.klaviyo.com/blog/abandoned-cart-email)