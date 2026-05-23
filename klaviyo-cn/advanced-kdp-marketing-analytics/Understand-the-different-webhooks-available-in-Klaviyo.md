---
id: "18622300908955"
title: "了解 Klaviyo 中可用的不同 webhooks"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18622300908955-Understand-the-different-webhooks-available-in-Klaviyo"
section: "Webhooks"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:56:44Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 中提供的 Webhook 解决方案之间的差异，以及何时应使用每种解决方案。 ## 开始之前

[高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672)，了解如何购买此计划。 ## 什么是 webhook？ Webhooks 允许 Klaviyo 通过 HTTP 请求传递信息或“调用”其他应用程序、工具和服务器。他们可以发送有关已发生事件的信息（例如下的订单、新客户订阅等）或通知您的外部系统事件已发生。 Webhook 由几个关键组件组成：

- ****主题****导致 webhook 触发的事件。 - ****主体****（或“有效负载”）
  Webhook 发送的数据。 - ****标题****
  传递附加信息（例如身份验证）的地方。 ## 流网络钩子

您可以添加[流中的 webhooks](https://help.klaviyo.com/hc/en-us/articles/4534329515931) 作为流到达特定阶段或步骤时发生的操作。一旦流到达 Webhook 操作，就会根据您构造有效负载的方式发送 POST 请求，其中包含有关触发该流的事件或接收者的数据。流 webhook 只能基于流触发的事件（即可用作流触发器的事件）进行发送。此外，流 Webhook 不支持与消息相关的事件（例如，**收到的电子邮件**、**单击的电子邮件**、**将电子邮件标记为垃圾邮件**），因为流通常以消息接收结束。取消订阅电子邮件营销可用作流触发器和流 Webhook 的主题。 ### Flow Webhook 的用例示例

Flow Webhooks 最有效的一些示例用例包括：

- 发送基于订阅者被添加到分段或列表而触发的消息或 POST 请求。 - 当配置文件进入未参与的段时自动抑制。 - 当客户购买时，通过 Whatsapp 或 Facebook Messenger 等服务发送个性化的感谢信息。 ## 高级 KDP 中的 Webhooks

高级 KDP 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的计费指南，了解有关将此功能添加到您的计划中的更多信息，或者如果您是新客户，请开始使用。高级 KDP 中的 Webhook 允许您通知外部系统以响应事件，而无需依赖导致 Webhook 操作的一系列步骤。高级 KDP Webhook 不需要您手动构建或指定 Webhook 请求的正文。如果您想在不进行任何自定义开发的情况下通知外部系统发生了事件，则高级 KDP 中的 Webhook 最为有效。高级 KDP Webhook 还支持更广泛的主题来触发请求，并允许您发送信息以响应可通过 [获取事件 API](https://developers.klaviyo.com/en/reference/get_events) 查询的任何事件。这些包括：

- 电子邮件事件（例如，收到的电子邮件、点击的电子邮件、将电子邮件标记为垃圾邮件）
- 短信事件（例如，发送短信、收到短信）
- 推送通知事件（例如，已接收推送、退回推送）
- 来自集成的事件（即来自 Klaviyo 创建的第一方集成的事件）
- API 事件（例如，通过 Klaviyo 的 API 同步的事件）

这包括流 Webhook 不支持的消息相关事件，例如 **取消订阅**、**收到的电子邮件**或 **点击的电子邮件**。此外，高级 KDP Webhook 允许您一次订阅多个触发器，这与依赖于单触发器流的流 Webhook 不同。目标 URL 必须是可公开访问的 HTTP 端点。 ### 高级 KDP webhook 的示例用例

- 将客户的**取消订阅**事件同步到外部系统。 - 向服务台软件报告**收到的电子邮件**事件，以便代理可以查看电子邮件历史记录，从而更好地为客户服务。 - 将所有电子邮件发送、打开和点击同步到 Klaviyo 的[数据仓库同步](https://help.klaviyo.com/hc/en-us/articles/17759932376475) 不支持的数据仓库中。 ## 代码

代码是 Klaviyo Advanced KDP 中包含的一项功能。它不包含在 Klaviyo 的标准营销应用程序中，需要高级 KDP 订阅才能访问相关功能。 请参阅我们的计费指南，了解有关将此功能添加到您的计划中的更多信息，或者如果您是新客户，请开始使用。代码利用 Webhooks 来执行自定义函数以响应事件触发器。您可以直接在 Klaviyo 的编辑器中编写代码，Klaviyo 管理代码执行、监控和日志记录。如果您想在不托管公共 HTTP 端点的情况下向外部系统发送请求，则可以使用 Code。此外，如果您想执行自定义函数来响应发生的事件，您应该使用 Code 而不是 Klaviyo 中提供的其他 Webhook 解决方案。代码还支持高级 KDP 中通过 Webhook 进行事件触发器的更细粒度。您可以选择单个指标作为主题，而不是所有集成或 API 事件。请注意，代码不支持以下事件作为主题：

- 电子邮件已打开
- 收到电子邮件

### 示例代码用例

- 导入 Python JSON 库来解析事件有效负载并提取某些内容。 - 使用 [Klaviyo 的 API](https://developers.klaviyo.com/en/reference/api_overview) 根据事件元数据设置自定义配置文件属性。 - 导入 chatGPT 库，并根据个人资料和购物车中的商品为每个废弃的购物车创建自定义消息。 ## 其他资源

[了解流中的 webhook](https://help.klaviyo.com/hc/en-us/articles/4534329515931)
[了解高级 KDP 中的 webhooks](https://help.klaviyo.com/hc/en-us/articles/17760478970907)
[代码入门](https://help.klaviyo.com/hc/en-us/articles/18620644491035)