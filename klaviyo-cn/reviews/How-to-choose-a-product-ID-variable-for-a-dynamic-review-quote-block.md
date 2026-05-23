---
id: "25995019549979"
title: "如何为动态审核报价块选择产品 ID 变量"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/25995019549979-How-to-choose-a-product-ID-variable-for-a-dynamic-review-quote-block"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:36Z"
language: "zh"
---
## 你将会学到

了解如何选择产品 ID 变量来显示与某人感兴趣的产品相关的动态评论报价。这些变量因事件而异，因此请确保为您的流程使用正确的变量。

## 开始之前

此块仅在使用 Klaviyo Reviews 的帐户中可用。了解如何[开始使用 Klaviyo 评论](https://help.klaviyo.com/hc/en-us/articles/15937542819355)。

## 关于动态审查块

动态评论报价块可以根据电子邮件发送时间和收件人采取的操作显示不同的评论，这与静态评论块不同，静态评论块为每个收件人提供相同的产品。

本文专门讨论动态审查块，而不是静态的。静态评论报价块不需要产品 ID 变量。

此流程仅在某些流电子邮件中受支持：事件触发流、库存返还流、低库存流和降价流。了解如何向您的电子邮件[添加动态审阅块](https://klaviyo.zendesk.com/hc/en-us/articles/18007373861915)。

在许多情况下，Klaviyo 会自动检测产品 ID。在这些情况下，您不需要手动选择产品 ID 变量。如果您看到类似下面的按钮指示您的流程的触发器，这意味着 Klaviyo 将自动检测您的产品 ID，您无需按照此处列出的步骤进行操作。

![](https://klaviyo.zendesk.com/hc/article_attachments/33237640856475)

但是，对于某些自定义流程，您可能需要手动输入产品 ID 变量。如果您看到下面屏幕截图中显示的 **产品 ID 变量** 字段，请按照以下步骤添加变量。

![](https://klaviyo.zendesk.com/hc/article_attachments/33237663341211)

## 产品 ID 变量

下表提供了用于审核报价块的最常见事件变量。除了下表中的变量之外，您还可以使用引用产品 ID 的任何其他事件变量。要查找下表中以外的产品 ID 变量：

1. 在您的流程电子邮件中，单击****预览和测试****。
2. 单击您想要在审核报价块中使用的事件变量。当您单击变量名称时，标签将被复制到剪贴板。
3. 从标签中删除所有无关信息：围绕标签的大引号以及标签信息后面的任何过滤器。例如，如果原始标签是 {{ event.product.id|default:”” }}，则删除标签中除 **event.product.id** 之外的所有内容。
4. 将此变量粘贴到**产品 ID 的事件变量**字段中。

如果触发事件包含多个项目（例如，废弃的购物车流），则在选择评论时仅考虑第一个项目。我们不建议使用第二个、第三个或任何其他项目，因为并非事件的每个实例都包含多个项目。

### Shopify 产品 ID 变量

|  |  |
| --- | --- |
| ****流量触发**** | ****事件变量**** |
|浏览废弃|事件.ProductID |
|放弃购物车（**添加到购物车**触发器）|事件.ProductID |
|放弃结帐（**结帐开始**触发器）| event.extra.line\_items.0.product.id |
|又有货了 |事件.ProductID |
|降价|事件.产品\_id |
|库存低 |事件.产品\_id |
|已下订单 | event.extra.line\_items.0.product.id |

### WooCommerce 产品 ID 变量

|  |  |
| --- | --- |
| ****流量触发**** | ****事件变量**** |
|浏览废弃 |事件.ProductID |
|放弃购物车（**添加到购物车**触发器）|事件.ProductID |
|放弃结帐（**结帐开始**触发器）| event.extra.Items.0.ProductID | event.extra.Items.0.ProductID |
|已下订单 | event.extra.Items.0.ProductId |