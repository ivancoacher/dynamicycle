---
id: "115002775212"
title: "如何创建追加销售或交叉销售流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002775212-How-to-create-an-upsell-or-cross-sell-flow"
section: "Post-purchase flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:37Z"
language: "zh"
---
## 你将会学到

了解如何创建一个流程，让您可以跟进客户，在他们购买后尝试交叉销售或追加销售类似或相关产品。 Klaviyo 具有内置的产品评论/交叉销售流程以及新客户和回头客感谢流程，您可以将其重新用作追加销售或交叉销售流程。

您还可以从头开始创建自己的追加销售或交叉销售流程。本指南将引导您了解自定义 Klaviyo 的内置流程或创建自己的流程时应记住的事项。

## 流量触发

### 交叉销售

您的流程触发器应该是**已下订单**或**已履行订单。****已下订单**事件跟踪有人对商品下订单的时间，而**已履行订单**事件则跟踪商品发货的时间。 Klaviyo 的内置产品审核/交叉销售流程使用**已履行订单**事件作为触发器，因为这更接近客户实际收到产品的时间。但是，根据您的喜好，您可以使用其中任何一个。

您的触发器应包含触发器过滤器，以**仅包含自开始此流程以来订单履行次数为零的人员**。这可以确保，如果他们购买的其他商品在流程中发货，他们不会收到电子邮件。

![触发器过滤器设置为仅包含自启动此流程以来已履行订单零次的人员的流程触发器](https://klaviyo.zendesk.com/hc/article_attachments/28715961710875)

### 追加销售

对于追加销售流程，您可能需要完全使用不同的触发器。例如，如果客户查看了一双鞋子，但您想向他们出售另一双更贵的鞋子，您将需要使用 **查看的产品** 事件来触发您的流程。可用事件触发器的完整列表取决于您的特定集成，并且可以通过单击“指标”在您帐户的[分析选项卡](https://www.klaviyo.com/analytics/metrics)中查看。

## 流量过滤器

您可能还想按类别或产品系列过滤交叉销售和追加销售流程。这将使您可以更轻松地在电子邮件内容中提供相关推荐，因为您可以更好地了解客户在触发流程时正在查看的内容。

![带有触发器过滤器的流触发器设置为过滤特定集合中的订单](https://klaviyo.zendesk.com/hc/article_attachments/28715968283291)

## 时间安排

创建追加销售或交叉销售流程时，您应该首先决定您的流程是购买前还是购买后。

如果您想对客户进行交叉销售，您可能希望在购买后发送流程 - 您甚至可能想要等到客户收到订单。这就是为什么默认产品审核/交叉销售流程设置为订单履行后 14 天发出的原因。

如果您想向客户追加销售，您可能需要发送预购流量。选择适当的流量触发器非常重要，因为在购买周期的正确时间向客户发送电子邮件非常重要。您甚至可能希望通过包含类似产品的产品 Feed 来直接在浏览放弃或放弃的购物车流程中追加销售产品。

## 内容

[产品提要](https://help.klaviyo.com/hc/en-us/articles/115005082787-An-Overview-of-Product-Feeds-and-Recommendations) 是在电子邮件中追加销售或交叉销售产品的好方法。由于您可以将产品 Feed 限制为特定类别或集合，因此您可以根据客户触发流程时与之交互（购买、查看等）的产品来提供更相关的建议。

![从源中填充并在电子邮件中以网格模式列出的一组推荐产品的示例](https://klaviyo.zendesk.com/hc/article_attachments/28715961707419)

## 其他资源

详细了解[在本指南中创建购买后流程](https://help.klaviyo.com/hc/en-us/articles/360028872611)。

了解特定类型的流，例如[浏览放弃](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow-VFB-) 或[放弃购物车](https://help.klaviyo.com/hc/en-us/articles/115002779411-Create-an-Abandoned-Cart-Flow-VFB-) 流。

获取有关[构建产品审核流程]的详细信息(https://help.klaviyo.com/hc/en-us/articles/115002779391)。

想要更深入地创建定制内容？参加这个[个性化电子邮件课程](https://academy.klaviyo.com/guide-to-email-personalization)。