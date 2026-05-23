---
id: "360035540251"
title: "了解如何在活动和流程中使用 WooCommerce 订阅数据"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360035540251-Understanding-how-to-use-WooCommerce-subscriptions-data-in-campaigns-and-flows"
section: "WooCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:52Z"
language: "zh"
---
## 你将会学到

了解如何在 Klaviyo 中使用 WooCommerce 订阅数据来触发面向订阅者的流程并创建针对订阅者的活动。 WooCommerce 提供了一个 WooCommerce 订阅插件，可用于管理订阅。

您可以从 WooCommerce 扩展商店启用 [WooCommerce 订阅插件](https://woocommerce.com/products/woocommerce-subscriptions/)。

## 将 WooCommerce 订阅同步到 Klaviyo

[Tribe](https://www.madebytribe.com/) 开发了一个插件，可将 Wordpress 订阅与 Klaviyo 集成，以便您可以在购买或取消 WooCommerce 订阅时向 Klaviyo 发送自定义事件。

Tribe 于 2021 年 1 月弃用了他们的免费 WooCommerce 订阅插件。要继续，请转到他们的新 [高级 WooCommerce 订阅插件](https://www.madebytribe.com/products/klaviyo-toolkit/)。您需要 [Klaviyo 公共 API 密钥/站点 ID](https://help.klaviyo.com/hc/en-us/articles/115005062267) 来激活该插件。

## 数据同步到 Klaviyo

Tribe 的插件将以下数据从 WooCommerce 订阅同步到 Klaviyo：

- 订阅价格
- 订阅计划名称
- 订阅试用
- 订阅计划 ID

这是通过 Tribe 插件同步到 Klaviyo 的个人资料数据示例：
![Klaviyo 指标中的 WooCommerce 订阅信息](https://klaviyo.zendesk.com/hc/article_attachments/28723541915675)

## 使用 WooCommerce 订阅数据创建活动

WooCommerce 订阅指标可用于细分客户并在特定活动中针对他们。例如，创建**订阅了 PlanID = 1066** 的计划的客户细分。

![依赖 WooCommerce 订阅数据的细分](https://klaviyo.zendesk.com/hc/article_attachments/28723519994139)

创建针对这部分客户的营销活动。例如，如果您的订阅 Plan1099 是可生物降解卫生纸的半月订阅，请向最近订阅 Plan1066 的客户发送您新的可生物降解清洁产品系列的产品发布活动。

## 使用 WooCommerce 订阅数据创建流程

您可以使用任何 WooCommerce 订阅指标来触发 Klaviyo 中的流。例如，您可以使用 **订阅计划** 指标来触发 Klaviyo 中的“欢迎订阅者”流程。

## 其他资源

- [WooCommerce 入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005255808)
- [WooCommerce 数据参考](https://klaviyo.zendesk.com/hc/en-us/articles/360030732832)