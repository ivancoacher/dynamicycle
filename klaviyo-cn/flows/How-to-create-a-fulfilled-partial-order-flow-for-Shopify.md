---
id: "4401771131419"
title: "如何为 Shopify 创建已履行的部分订单流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4401771131419-How-to-create-a-fulfilled-partial-order-flow-for-Shopify"
section: "Ecommerce-specific flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: "zh"
---
## 你将会学到

了解如何为通过 Shopify 下的部分订单创建 Klaviyo 流程。如果您经常将订单作为单独的货件而不是一次全部交付（或者您的履行中心这样做），您可以通过已履行的部分订单流程让客户知道每件商品何时得到履行。此流程可让您的客户准确了解特定商品何时在途中，从而带来更好的整体客户体验。在 Klaviyo 中，您可以使用 **已履行的部分订单** 指标在履行一个或多个项目时触发此流程。您还可以将其与标准履行订单流程结合起来，该流程仅在订单中的每个项目均已履行时发送。在本文中，我们将介绍用于配置部分和全部履行订单流程的不同选项。 ## 从流程库创建已履行的部分订单流程

将 Shopify 商店与 Klaviyo 集成后，您会发现[流程库](https://www.klaviyo.com/library/flows) 中自动填充了几个最佳实践流程，包括预构建的已履行部分订单流程。 1. 导航至****流****选项卡。 2. 单击****创建流程。****
3. 搜索**部分发货确认。**
4. 单击预建流程选项之一。 ## 从头开始设置已履行的部分订单流程

要从头开始创建已履行的部分订单流程：

1. 创建指标触发流。 2. 对于流程触发器，从 **您的指标** 下的 Shopify 指标中选择****已履行的部分订单****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34376136026267)
3. 单击****保存****。 4. 添加您的消息。如果您打算发送短信，请首先拖入条件拆分，以便短信仅发送给选择加入短信营销的用户，如下所示。在这种情况下，我们建议添加电子邮件，以便每个未订阅短信的人仍能收到有关其订单的最新信息。 ![检查短信同意的条件分割。](https://klaviyo.zendesk.com/hc/article_attachments/28720772234907)

## 发送履行消息的选项

根据您的使用案例，您可以通过多种不同的方式设置已履行和已履行的部分订单流。例如，您可以发送：

- 当整个订单完成时
- 每次完成部分订单时
- 两者同时执行，具体取决于整个订单是否同时履行

### 仅当整个订单完成后才发送

如果您只想在整个订单履行完毕后发送一条消息，请使用常规履行订单流。这与已履行的部分订单流本质上相同，只是它是由 **已履行订单** 指标触发的。 ![已完成订单触发后的已完成订单电子邮件。](https://klaviyo.zendesk.com/hc/article_attachments/28720772238747)

### 订单各部分完成后发送

如果您想在每次履行部分订单时发送消息，您可以使用上面显示的已履行的部分订单流程。当订单中的最后一件商品完成后，您有两种选择：

- 发送两条消息，一条来自已履行的订单流，一条来自已履行的部分订单流
- 通过已履行的订单流发送一条消息

对于第一种方法，您不需要更改已履行或已履行的部分订单流。但是，请务必准确解释您的消息中的差异。例如，已履行的订单流应明确表示整个订单已履行，而不是部分完成。如果您只想为最终商品发送一条消息，请向已履行的部分订单流添加触发器过滤器。将过滤器设置为 **FulfillmentStatus 等于部分**。 ![配置为“FulfillmentStatus 等于部分”的触发过滤器。](https://klaviyo.zendesk.com/hc/article_attachments/28720772241179)

### 根据整个订单是否完成发送不同的流程

您还可以两全其美：

- 每次完成部分订单时发送一条消息
- 当整个订单同时履行时发送一条消息

要进行此设置，您无需向部分履行流程添加任何触发器或流程过滤器。在常规履行流程中，添加触发器过滤器 **HasPartialFulfillments is false**。 ![配置为“HasPartialFulfillments is false”的触发过滤器。](https://klaviyo.zendesk.com/hc/article_attachments/28720760472731)

## 其他资源

- 了解有关从 Shopify 同步内容的更多信息：[Shopify 数据参考](https://help.klaviyo.com/hc/en-us/articles/115005080447)
- 了解有关流程的更多信息：
  - [如何使用流程发送交易电子邮件](https://help.klaviyo.com/hc/en-us/articles/360003165732)
  - [如何创建购买后流程](https://help.klaviyo.com/hc/en-us/articles/360028872611)
  - [如何创建追加销售或交叉销售流程](https://help.klaviyo.com/hc/en-us/articles/115002775212)