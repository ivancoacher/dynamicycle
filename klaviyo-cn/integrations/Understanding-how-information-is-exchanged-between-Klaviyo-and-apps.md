---
id: "360030265051"
title: "了解 Klaviyo 和应用程序之间如何交换信息"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360030265051-Understanding-how-information-is-exchanged-between-Klaviyo-and-apps"
section: "All integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "zh"
---
## 你将会学到

了解如何通过应用程序编程接口 (API) 在 Klaviyo 和第三方应用程序之间同步信息。通过 Klaviyo 集成交换的大多数数据都是单向的：数据被拉入您的 Klaviyo 帐户，以便您可以利用广泛的客户数据。

## 集成如何与 Klaviyo 同步信息

Klaviyo 的 API 是一组接口，用于在 Klaviyo 和连接到您的 Klaviyo 帐户的其他应用程序之间交换数据。要最初将 Klaviyo 与其他应用程序集成，您需要通过 OAuth 进行身份验证或使用 API 密钥。 API 密钥是与您的特定帐户绑定的唯一标识符。

Klaviyo 生成两种类型的 API 密钥，这两种密钥[都可以在您的帐户中找到](https://klaviyo.zendesk.com/hc/en-us/articles/115005062267)：

- ****公共****
  您的公共 API 密钥（有时称为站点 ID）是您的 Klaviyo 帐户的唯一标识符。第三方应用程序无法使用此密钥来访问您的 Klaviyo 帐户内的私人信息。
- ****私人****
  私有 API 密钥用于从 Klaviyo 读取数据并操作敏感对象，例如列表。他们确保更新订阅和其他客户信息的过程是安全和私密的。私有 API 密钥应像您的密码一样对待：保存在安全的地方，切勿向公众公开。您可以为不同的应用程序生成新的私有 API 密钥，以跟踪添加到您的 Klaviyo 帐户的数据源。

有关 Klaviyo API 密钥类型的更多具体信息，请参阅我们的 [API 参考文档](https://developers.klaviyo.com/en/reference/api_overview#api-key-scopes)。

## Klaviyo 的 REST API

REST 是一种架构风格，为互联网上的应用程序之间的平台无关通信提供指导。 Klaviyo REST API 主要使用 JavaScript 对象表示法 (JSON) 格式进行通信，该格式为 API 消息中包含的信息提供结构化布局。您可以通过我们的 REST API 访问您的 Klaviyo 帐户的以下区域：

- 账户
- 活动
- 目录
- 优惠券
- 数据隐私
- 活动
- 流量
- 图片
- 列表
- 指标
- 个人资料
- 报告
- 细分
- 标签
- 模板

虽然上述 API 设计为从服务器端应用程序调用，但我们还有一个客户端 API，用于从客户端应用程序创建事件和订阅。

## klaviyo JavaScript 对象

[**klaviyo** 对象](https://developers.klaviyo.com/en/docs/introduction_to_the_klaviyo_object) 取代了旧版 \_**learnq** 和 **klOnsite** 对象。这些 JavaScript 对象提供了一种与我们的 API 交互并将事件发送到 Klaviyo 的快捷方式。 klaviyo 对象允许您识别已知的配置文件，并跟踪您网站上的事件和操作。

## 其他资源

- [营销人员的 API 基础知识](https://academy.klaviyo.com/en-us/collections/api-fundamentals-for-marketers)
- [了解 Klaviyo 和应用程序之间交换的信息类型](https://klaviyo.zendesk.com/hc/en-us/articles/360030696012)
- [Klaviyo API 入门](https://help.klaviyo.com/hc/en-us/articles/360045726811)
- 需要更多与 Klaviyo 集成的帮助吗？查看[Klaviyo的代理合作伙伴](https://klaviyo.partnerpage.io/)