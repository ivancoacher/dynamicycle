---
id: "115005253248"
title: "如何区分 Shopify POS 和 Shopify Web 数据"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005253248-How-to-differentiate-Shopify-POS-and-Shopify-web-data"
section: "Shopify troubleshooting"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:39Z"
language: "zh"
---
## 你将会学到

如果您使用 [Shopify 销售点 (POS)](https://www.shopify.com/pos) 系统，了解如何在 Klaviyo 中区分 POS 订单和网络订单。这是通过过滤订单或创建细分来完成的。当客户完成结账流程并在您的 Shopify 商店中创建订单时，Klaviyo 会同步“source_name”，该订单记录了订单的来源。

根据 Shopify 的文档，“source\_name”定义为：“订单来源位置。只能在创建期间设置，此后不可写入。通过官方 Shopify 渠道创建的订单具有受保护值，其他 API 客户端在订单创建期间无法分配这些值。这些受保护值是：“web”、“pos”、“iphone”和“android”。通过 API 创建的订单可以分配您选择的任何其他字符串。如果未指定 source\_name，则为新订单分配该值“API”。”

## 开始之前

####知识检查

如果您尚未阅读我们的 [Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) 指南，了解有关集成的分步说明，然后再继续阅读本文。

## 按来源过滤订单

您可以使用与给定订单关联的 source\_name 属性，按“web”、“pos”、“iphone”、“android”或其他自定义字符串过滤 Klaviyo 中的**已下订单** 事件。在 Klaviyo 中，当您构建段或流过滤器时，此属性将简单地显示为“源名称”。

要过滤并仅查看 POS **下订单** 事件：

1. 在 Klaviyo 中，选择 ****Analytics**** 下拉列表，然后单击 ****Metrics****。
2. 单击 Shopify 中的 **已下订单** 指标。
3. 选择 **Filter by** 下拉列表并选择 ****Source name,****，然后从 **equals** 下拉列表中选择 ****pos****。 **![Klaviyo 指标选项卡中按源名称筛选的 Shopify 下订单指标等于选择一个值](https://klaviyo.zendesk.com/hc/article_attachments/28713328870555)**

## 按来源细分订单

在分段构建器中，您可以根据****源名称****属性创建分段。例如，以下是已下 POS 订单的一部分客户：

1. 在 Klaviyo 中，导航至****受众 > 列表和细分****。
2. 单击****创建列表/细分****并选择****细分****
3. 创建具有以下条件的段：
   - 名称：POS 订单
   - 标签：无
   - 有些人做了什么（或没有做什么） > 已下订单 > 至少一次 > 一直以来
   - 其中源名称 > 等于 pos
     ![Klaviyo 细分生成器显示名为 POS 订单的细分，创建黑色背景细分并取消白色背景](https://klaviyo.zendesk.com/hc/article_attachments/28713328875291)

## 结果

您现在已经了解了如何区分 Shopify 网络订单和 POS 订单。

## 其他资源

- [Shopify 入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005080407)
- [分段入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005237908)