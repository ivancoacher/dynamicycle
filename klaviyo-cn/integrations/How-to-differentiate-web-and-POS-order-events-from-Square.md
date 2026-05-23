---
id: "19450345654811"
title: "如何区分 Square 中的 Web 和 POS 订单事件"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/19450345654811-How-to-differentiate-web-and-POS-order-events-from-Square"
section: "Square"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: "zh"
---
## 你将会学到

了解如何区分从 Square 同步到 Klaviyo 的销售点 (POS) 和网络订单事件。然后，根据客户是亲自下订单还是在线下订单，在 Klaviyo 中对客户进行细分，从而使您的消息传递更加个性化。

## 开始之前

在继续之前，请确保您已[将 Square 商店与 Klaviyo 集成](https://help.klaviyo.com/hc/en-us/articles/11117215837211)。

## 数据如何从 Square 同步

Klaviyo 与 Square 的集成将 Square Online 网络订单事件和 Square POS 订单事件同步到 Klaviyo。

如果客户直接与您的公司共享与订单关联的电子邮件地址和/或电话号码，Square POS 订单事件将同步到 Klaviyo。

Square 事件将有一个名为 **源名称** 的属性，该属性将显示事件是来自 POS 还是来自在线/网络，以便您可以在 Klaviyo 中对这些事件进行分段。

包含 **Source Name** 属性的 Square 事件如下：

- ****已下订单****
- **退款订单**
- **取消订单**
- **已履行的订单**
- **已履行部分订单**

要了解有关从 Square 同步的事件属性的更多信息，请阅读我们的 [Square 数据参考](https://help.klaviyo.com/hc/en-us/articles/11117271030555)。

## 如何细分 POS 和 Web 客户

您可以使用 **源名称** 属性对 Klaviyo 中的 POS 和 Web 客户进行细分。

例如，创建一个通过 POS 至少下了一个**下订单**的客户群。此细分不会排除那些也在线购买过的人，但如果您愿意，您可以选择排除他们。

1. 在 Klaviyo 中，导航至****列表和分段****。
2. 单击****新建> 创建分段****。
3. 为您的分段命名并添加任何标签。
4. 创建以下段定义：
   **某人已完成（或未完成）的操作 > 人员已下订单 > 至少一次 > 一直 > 其中源名称等于 POS**
5. 单击****创建分段****。

要创建至少在网上进行过一次购买的用户细分，请创建相同的细分，但选择 **来源名称** 等于“Square Online”。您还可以选择从该细分中排除 POS 购买者。
![Klaviyo 细分构建器与细分 Square POS 购买者](https://klaviyo.zendesk.com/hc/article_attachments/28705699357467)

## 其他资源

- [Square 入门](https://help.klaviyo.com/hc/en-us/articles/11117215837211)
- [方形数据参考](https://help.klaviyo.com/hc/en-us/articles/11117271030555)
- [分段入门](https://help.klaviyo.com/hc/en-us/articles/115005237908)