---
id: "360003057151"
title: "如何创建指标触发的流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360003057151-How-to-create-a-metric-triggered-flow"
section: "Ecommerce-specific flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:50Z"
language: "zh"
---
## 你将会学到

了解如何创建指标触发（也称为事件触发）流，用于在订阅者执行特定操作时向他们发送电子邮件。这些操作与 Klaviyo 中的“指标”或事件相对应。可用指标可在您帐户的[分析选项卡](https://www.klaviyo.com/analytics/metrics) 的“指标”下找到，并且通常通过电子商务集成或作为自定义事件进行同步。但是，请务必注意，点击次数、打开次数和收到的电子邮件指标不可用于选择来触发流程。指标触发流的一些常见示例包括：

- 废弃的购物车（由 **Started****Checkout** 指标触发）
- 购买后（由 **已下订单** 指标触发）
- 浏览放弃（由 **查看的产品** 指标触发）
- 产品审核（由 **已下订单** 指标触发）

联系人每次完成相应操作时都会收到指标触发的流，除非您将[过滤器](https://help.klaviyo.com/hc/en-us/articles/115002779051)添加到另有指定的流中。例如，如果有人下订单并收到您的购买后流程，然后一个月后下另一个订单，他们将重新触发流程并再次收到相同的电子邮件。 ## 配置指标触发流

要创建指标触发的流：

1. 创建新流程。 2. 在侧栏中选择****公制****。 ![在流程构建器的触发器设置菜单中，可以在列表中间找到“Metric”选项](https://klaviyo.zendesk.com/hc/article_attachments/28717850836891)

接下来，系统将提示您选择将触发流程的指标。可用指标因账户而异，主要取决于您正在使用的集成以及您设置的任何自定义指标。大多数集成都有自己的指标。您可以在下面找到与流行的电子商务集成同步的指标：

- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080447)
- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082587)
- [Magento](https://help.klaviyo.com/hc/en-us/articles/115005254528)
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115003458852)
- [Woocommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808)

如果您想创建自定义指标，请访问我们的[开发者门户](https://developers.klaviyo.com/en/docs/custom_event_tracking)。有关哪些指标与您的集成同步、[这些指标同步的频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)以及可用指标数据的更多信息，您可以在 Klaviyo 帮助中心或集成的帮助中心找到相应的帮助文档。 **打开的电子邮件**和**点击** **电子邮件**等性能指标不能用于触发流。或者，您可以添加[触发器和流过滤器](https://help.klaviyo.com/hc/en-us/articles/115002779051)，以进一步细化添加到流中的人员 - 例如，将您的购买后系列限制为：

- 购买特定产品的人
- 初次顾客（以前从未下过订单）
- 购买一定数量商品的人
- 购买特定类别/系列的人
- 花费了特定金额的人

![使用已下订单指标和配置为“且商品包含无皱白色 T 恤”的触发器过滤器的触发器示例](https://klaviyo.zendesk.com/hc/article_attachments/28717850840347)

一旦您设置了特定指标来触发流程，您将无法将其更改为其他指标。为此，您需要[克隆流](https://help.klaviyo.com/hc/en-us/articles/115002775052)并更改触发流的指标。 ## 指标触发的流程如何工作

每当有人采取触发流程的操作（指标）时，他们就会排队等待接收电子邮件序列。例如，对于购买后，您可以选择 **已下订单** 指标，然后每个下订单的人都会排队。联系人每​​次执行相关操作时都会收到指标触发的流。如果有人执行某个操作并随后重复此操作，他们将重新触发流程。如果您想缩小流程范围，可以设置[流程和触发器过滤器](https://help.klaviyo.com/hc/en-us/articles/115002779051)。 如果您依赖于指标的集成 - 例如，Magento 2 中的**已下订单** 事件，它每半小时与集成同步一次 - 在配置流程时间时，您将需要注意集成同步的频率。如果您将指标触发的流程设置为立即发送，则收件人实际上可能不会立即收到电子邮件，具体取决于同步频率。 Shopify 和 BigCommerce 指标实时同步。 ## 其他资源

See how to create metric-triggered flows:

- [废弃的购物车](https://help.klaviyo.com/hc/en-us/articles/115002779411)
- [浏览废弃](https://help.klaviyo.com/hc/en-us/articles/115002775252)
- [购买后](https://help.klaviyo.com/hc/en-us/articles/360028872611)
- [追加销售或交叉销售](https://help.klaviyo.com/hc/en-us/articles/115002775212)