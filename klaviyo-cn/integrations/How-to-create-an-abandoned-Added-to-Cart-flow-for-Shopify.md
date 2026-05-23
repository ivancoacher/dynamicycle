---
id: "35510464880027"
title: "如何为 Shopify 创建废弃的“添加到购物车”流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/35510464880027-How-to-create-an-abandoned-Added-to-Cart-flow-for-Shopify"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:41Z"
language: "zh"
---
了解如何创建由 Shopify **添加到购物车** 事件触发的废弃购物车流程。默认的 Klaviyo 放弃购物车流程由 Shopify **结账开始** 事件触发，而 **添加到购物车** 放弃购物车流程针对尚未开始结账的更多休闲购物者。

## 开始之前

为了启用此流程，您需要[启用 Klaviyo 应用嵌入](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01J6F7TREZM0NY2336G80MJFM3) 并检查集成设置 **跟踪行为事件**，以便跟踪 Shopify 中的 **添加到购物车** 事件。
![](https://klaviyo.zendesk.com/hc/article_attachments/35510459309467)

## 创建流程

要启用此流程，我们建议使用 Klaviyo 流程库中提供的预构建流程：

1. 导航到 Klaviyo 的 [流库](https://www.klaviyo.com/library/flows)。
2. 单击进入“防止销售损失”目标部分。
3. 选择****放弃购物车提醒、**** ****Shopify**** ****添加到购物车触发器**** 流程。有两个选项：仅电子邮件，或电子邮件和短信。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35545007778843)
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35545007792539)
4. 如果您启用了行为跟踪，则此流程将准备好使用所有推荐的过滤器和动态电子邮件内容，以支持个性化购物车后续消息传递。

## 您是否使用 Klaviyo 的 Amazon Buy 与 Prime 集成？

如果您使用 Buy with Prime 来支持商店中任何产品的付款和配送，并且您已[集成了 Klaviyo 和 Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467)，请确保执行以下操作：

对于已放弃的“添加到购物车”流程，请添加以下流程过滤器，以排除开始结账或通过“Buy with Prime”进行购买的客户接收到错误消息：

- **开始结账**（使用 Prime 购买）**自开始此流程以来零次**并且
- **下订单**（使用 Prime 购买）**自开始此流程以来零次。**

## 结果

您现在已为 Shopify 启用了废弃的 **添加到购物车** 流程。

## 其他资源

[如何创建废弃的购物车流程](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)

[如何为Shopify启用现场跟踪](https://klaviyo.zendesk.com/hc/en-us/articles/4425956184731)