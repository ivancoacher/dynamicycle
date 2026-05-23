---
id: "360045726811"
title: "Klaviyo API 入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360045726811-Getting-started-with-Klaviyo-APIs"
section: "Custom integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: "zh"
---
## 你将会学到

对 API 调用以及 Klaviyo API 如何使您的业务受益有基本的了解。在本指南中，您将了解 REST API、HTTP 方法和开发人员工具，为测试 Klaviyo 的 API 做好准备。您的第一次 API 调用从开始到结束仅需 10 分钟即可完成。如果您已经熟悉 API 调用并准备好测试我们的 API，请按照[我们的 Postman 集合使用指南](https://developers.klaviyo.com/en/docs/use_klaviyos_postman_collections) 操作。在本指南中，当引入新的技术术语时，我们将链接到术语表。如果您不确定指南中某个单词的含义，请查看[技术术语词汇表](https://klaviyo.zendesk.com/hc/en-us/articles/360045302732)。 ### 什么是 REST API？ [休息](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70N1JW33C63TB1Q7FJ1) [API](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70NQNX9BHEAWCGE4PFS) 是一组代表表述性状态传输和应用程序编程接口的首字母缩略词。这些术语可以更简单地理解为结构化请求，允许一个软件与另一个软件对话并在它们之间传递信息。当您进行 API 调用时，您将向存储信息的服务器提交请求，然后服务器返回包含 JSON（或 JavaScript 对象表示法）格式的请求数据的响应。更简单地说，REST API 允许您请求存储在 Klaviyo 中的数据，并以您和计算机可读的格式将该数据返回给您。 ![whatisanAPI_copy.png](https://klaviyo.zendesk.com/hc/article_attachments/28722557581467)

标准 API 调用只需几秒钟即可完成。在幕后，您的通话将：

1. 通过互联网向 API 发送结构化数据请求。请求通过 [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) 发送，这是互联网主要构建的基本网络请求类型。 2. API将接收请求，对其进行处理，并从Klaviyo的数据库中获取所请求的信息。 3. 然后，API 使用 JSON 结构化格式响应客户端应用程序。 4. 您将收到来自客户端应用程序的 JSON 响应。尽管这些知识有助于理解数据传输的工作原理，但没有必要开始进行 API 调用并从 Klaviyo API 提供的功能中获取价值。以下部分将介绍您开始首次 API 调用时需要了解的所有信息。 ### HTTP 方法

HTTP 方法是发送请求的“动词”。我们将在本指南中讨论 2 个 [HTTP 方法](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70NYQ9F64XV2CCK9E0Q)：GET 和 POST。尽管我们不会在这里使用它们，但值得注意的是，大多数 REST API 支持其他 HTTP 方法，例如 PUT、PATCH 和 DELETE。 #### 获取

GET 请求最容易理解为“读取”请求。 GET 请求从 API [端点](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70N6DTN4KXNP9RZ7VER) 检索信息，并以 JSON 格式的响应将其返回给您。这些请求仅允许您读取数据，这使其成为最安全的请求类型，因为您的数据无法使用此方法修改或覆盖。 #### 帖子

POST请求可以简单理解为“写”请求。 POST 允许您创建或添加新资源。例如，对列表 API 的 POST 请求可用于在您的帐户中创建新列表，而 GET 请求可用于检索所有可用列表。请注意，发布数据时，响应将根据 Klaviyo 何时可以完成您的请求而有所不同。 ### 必要的工具

API 为您的工作流程提供了足够的灵活性，并且不需要您使用特定的客户端应用程序或[语言库](https://help.klaviyo.com/hc/en-us/articles/360045302732#l8) 来实现所需的结果。由于 API 调用是使用 HTTP 请求进行的，因此几乎每种编程语言都能够以本机方式或通过广泛可用的语言库发送此类请求。 此外，根据您的计算机和操作系统，您可以使用 Apple 的 [Terminal](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/CommandLinePrimer/CommandLine.html) 或 Windows [Command Line](https://docs.microsoft.com/en-us/windows/terminal/) 等本机应用程序来进行客户端 API 调用。然而，这些应用程序需要事先了解命令行界面。我们使用名为 [Postman](https://www.postman.com/) 的免费网络和桌面应用程序。 Postman 具有多种功能，可以通过输入端点、[参数](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70NKFSQDB43945J0J18) 和[身份验证](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70NQNX9BHEAWCGE4PFS)进入有用的用户界面。 ## 测试 Klaviyo 的 API

Klaviyo 的 API 对于将数据从其他平台或服务器发送到 Klaviyo 帐户或查询 Klaviyo 帐户内的信息非常有用。现在您已经了解了 API 的工作原理，您可以开始针对您的业务用例测试我们的 API。有关 Klaviyo 可用 API 的完整列表，请查看我们的 [API 参考文档](https://developers.klaviyo.com/en/reference/api_overview)。请按照我们的[如何使用 Postman 集合的指南](https://developers.klaviyo.com/en/docs/use_klaviyos_postman_collections) 进行首次 Klaviyo API 调用。 ## 其他资源

### 开发者门户资源

Klaviyo 的[开发者门户](https://developers.klaviyo.com/en) 包含 API 指南和参考文档，可帮助您充分利用我们的 API。查看以下资源以开始使用：

- [Klaviyo API 参考文档](https://developers.klaviyo.com/en/reference/api_overview)
- [Javascript API 入门](https://developers.klaviyo.com/en/docs/javascript_api)
- [设置基于 API 的事务事件](https://developers.klaviyo.com/en/docs/guide_to_setting_up_api_based_transactional_events)

### Klaviyo 开发者课程

[Klaviyo Academy](https://academy.klaviyo.com/) 提供开发人员课程，帮助您开始使用 Klaviyo API 进行构建。查看以下课程：

- [营销人员的 API 基础知识](https://academy.klaviyo.com/en-us/collections/api-fundamentals-for-marketers)
- [Klaviyo开发者证书](https://academy.klaviyo.com/klaviyo-developer-certificate)
- [定义常用API术语](https://academy.klaviyo.com/define-common-api-terms/1955790)