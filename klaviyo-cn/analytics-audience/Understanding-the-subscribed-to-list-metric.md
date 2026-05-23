---
id: "360039666832"
title: "了解订阅列表指标"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360039666832-Understanding-the-subscribed-to-list-metric"
section: "Metrics best practices"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: "zh"
---
## 你将会学到

了解 **订阅列表** 指标，每当客户订阅 Klaviyo 中的列表时，该指标就会显示在客户的个人资料中。这包括：

- 当有人填写 Klaviyo 注册表单然后确认订阅（通过双重选择加入）时。
- 当通过快速添加将个人资料添加到经过电子邮件同意的列表时。
- 当通过 CSV 上传的电子邮件同意将个人资料添加到列表中时。
- 当有人通过 Klaviyo 构建的集成或某些第三方集成订阅时。

因此，了解使用它来创建细分的最佳实践至关重要。在本文中，您将了解**订阅列表**指标的含义以及何时使用它。

## 订阅列表指标

**订阅列表**是当客户订阅您的某个列表时显示在客户个人资料上的一项指标。以下是此指标在配置文件中的示例。

仅对于 SMS 事件，Klaviyo 能够记录多个 **订阅列表** 事件。

![订阅个人资料上的列表事件](https://klaviyo.zendesk.com/hc/article_attachments/36495394610203)

如果某人多次将其信息输入同一表单，他们将不会在其个人资料下找到多个**订阅列表**指标，也不会多次将其重新添加到列表中。

Klaviyo 只会将 **订阅列表** 事件添加到给定的配置文件，如果它们是：

- 不在列表中
- 在列表中，但[被抑制](https://help.klaviyo.com/hc/en-us/articles/115005246108)

## 当订阅列表指标添加到配置文件时

每当有人订阅了他们之前未订阅过的列表时，就会出现“订阅列表”指标。

要了解有关从 Shopify 同步订阅者的更多信息，请查看[如何将 Shopify 电子邮件订阅者同步到 Klaviyo 列表](https://help.klaviyo.com/hc/en-us/articles/115005080667-How-to-Sync-Shopify-Email-Subscribers-to-a-Klaviyo-List#about-the-accepts-marketing-property-and-subscribers3)。

## 何时在流程中使用

一般来说，使用 **订阅列表** 指标来触发您的流程并不是最佳实践。相反，如果您希望特定列表中的客户在添加时浏览您的流程，请[创建列表触发的流程](https://help.klaviyo.com/hc/en-us/articles/360003031652)。

![可用的流程触发器](https://klaviyo.zendesk.com/hc/article_attachments/36495380398363)

如果您确实使用此指标来触发流程，请务必添加一个触发过滤器，用于标识您使用 **订阅列表** 指标引用的特定列表。例如，此触发过滤器是：**列表等于产品评论列表**。

![添加到列表流触发器](https://klaviyo.zendesk.com/hc/article_attachments/36495380400155)

## 何时在段中使用

如果您想查看订阅列表的人数，请在构建细分时使用 **订阅列表** 指标。例如，如果您想查看过去 2 周内添加了多少列表成员。

- 如果某人在或不在列表中 > 此人在 [**列表名称**] 中
  和
- 过去 14 天内至少订阅列表一次

![使用订阅列表事件进行分段](https://klaviyo.zendesk.com/hc/article_attachments/36495380401563)

## 其他资源

- [如何创建和管理注册表单](https://help.klaviyo.com/hc/en-us/articles/360002049952)
- [如何创建欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172)
- [了解流触发器和过滤器](https://help.klaviyo.com/hc/en-us/articles/115002779051)
- [了解电子邮件指标](https://help.klaviyo.com/hc/en-us/articles/360036974872)