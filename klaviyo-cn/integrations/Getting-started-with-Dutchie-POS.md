---
id: "22698258709531"
title: "开始使用 Dutchie POS"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/22698258709531-Getting-started-with-Dutchie-POS"
section: "Dutchie POS"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: "zh"
---
## 你将会学到

了解如何将 Klaviyo 与 Dutchie 销售点 (POS) 集成，以便将客户资料和订单数据同步到 Klaviyo。有了这些数据，您将能够通过细分、营销活动和流程，通过有针对性的消息传递来吸引客户。与 Dutchie POS 集成后，客户资料和订单数据将同步到您的 Klaviyo 帐户。请注意，Klaviyo 的集成目前不会将任何 Web 数据从 Dutchie Ecommerce 同步到 Klaviyo（例如 **开始结账**、**订单提交** 等）。仅 Dutchie POS 事件（即 **已下订单** 和 **已订购****产品**）可以同步。如果没有 **Started Checkout** 等网络事件，您将无法使用 **Abandoned Cart** 等 Klaviyo 流程。 ## 开始之前

- 您有责任确保遵守您经营所在地区以及您所营销的客户所在地区的任何大麻相关法律。 - 在 Dutchie 中，产品图像可以从 POS 流向电子商务，但不能从电子商务流向 POS。为确保 Klaviyo 可以同步产品图像，请确保您通过 Dutchie POS 更新图像。 - 在典型的 Dutchie 设置中，每个州级零售商（母公司）都有多个单独的地点（子公司）。子位置是 Dutchie 中的单独实例，每个实例都有自己的 API 密钥。当 Klaviyo 代表您进行集成时，我们可以将您指定的子位置（来自单亲）连接到一个 Klaviyo 帐户。 - 配置文件和交易数据在父级别统一，但我们在同步订单数据中指定 locationName。 ## 如何与 Dutchie POS 集成

Dutchie 目前尚未在 Klaviyo 应用市场上列出。您必须联系 Dutchie 支持人员获取 API 密钥，然后联系 Klaviyo，我们将代表您进行集成。您还需要允许 Klaviyo 团队访问您的帐户。 1. 首先，您需要从 Dutchie 获得 API 密钥。 API 密钥由其支持团队直接提供。让您的帐户管理员联系 [possupport@dutchie.com](mailto:possupport@dutchie.com) 以获取您的 API 密钥。向 Dutchie 提出此请求时，您可以使用以下模板：

   - **荷兰队，**
     **[客户帐户名称] 将与 Klaviyo 集成 - 请提供以下位置的 Dutchie API 密钥：**
     **位置名称 1、位置名称 2 等**
2. 然后，发送一封电子邮件至 [wellness@klaviyo.com](mailto:wellness@klaviyo.com)，主题为 **Dutchie Integration setup**，并包括：

   - 包含您在步骤 1 中获得的 Dutchie API 密钥的安全链接。您可以使用 [onetimesecret.com](https://onetimesecret.com) 等网站生成安全链接。如果您选择其中之一，请确保在电子邮件中包含密码。 - 您想要集成的 Klaviyo 帐户的 [Klaviyo 公共 API 密钥](https://www.klaviyo.com/settings/account/api-keys)。 3.登录Klaviyo并导航至[账户安全页面](https://www.klaviyo.com/settings/account/security)。在“**Klaviyo 远程访问**”下，选择至少一周后的日期，然后单击“****保存****”。这将使 Klaviyo 团队能够完成您的 Dutchie 设置。 ## 数据从 Dutchie POS 同步到 Klaviyo

要检查从 Dutchie POS 到 Klaviyo 的数据同步：

1. 在您的 Klaviyo 帐户中，选择****分析 > 指标****。 2. 在顶部，按 **Dutchie** 进行过滤。在这里，您将看到从 Dutchie POS 同步到 Klaviyo 的订单事件列表：

![](https://klaviyo.zendesk.com/hc/article_attachments/28705638982683)

从 Dutchie 同步到 Klaviyo 的数据包括：

- 与订单事件相关的个人资料信息。 - 以下订单事件：
  - **已下订单**
  - **订购的产品**

Klaviyo 只会同步具有电子邮件地址的个人资料。我们建议在 Dutchie Ecommerce 中打开设置 **需要电子邮件地址进行访客结帐**，该设置可以在****设置 > 选项 > 结帐**** 下找到。电子邮件地址将同步到 Dutchie POS。有关与 Dutchie 同步的事件相关的属性的更多信息，请查看我们的文章 [Dutchie POS 数据参考](https://help.klaviyo.com/hc/en-us/articles/22698234676507)。 ## 添加现场跟踪（可选）

您可以选择通过 Google 跟踪代码管理器手动将 Klaviyo 的现场 JavaScript（称为 Klaviyo.js）添加到您的 Dutchie 网站。 Klaviyo.js 支持**活跃站点**跟踪和 Klaviyo 注册表单的使用。 Dutchie 和 Klaviyo 均支持 Google 跟踪代码管理器。 了解[如何使用 Google 跟踪代码管理器添加 Klaviyo 现场跟踪](https://help.klaviyo.com/hc/en-us/articles/360015392131)。 ## Dutchie 和电子邮件发送

在 Dutchie Ecommerce 结账期间同意电子邮件营销的客户不会同步到 Dutchie POS。目前，Klaviyo 仅同步来自 Dutchie POS 的数据，因此，从 Dutchie POS 同步到 Klaviyo 的个人资料均不会明确同意您的电子邮件营销。例如，可能会发生以下情况：

1. 您的客户在线下订单并在结账时提供电子邮件。他们选择通过复选框订阅电子邮件。 2. 在线结帐时提供的电子邮件附在订单中。 3. 订单已交付，客户使用 POS 结账。 4. 下订单信息以及附加的电子邮件地址会同步到 Klaviyo，但在线结帐的电子邮件订阅信息不会同步到 Klaviyo。 Klaviyo 将在 Klaviyo 中将 Dutchie 的同步个人资料标记为 **从未订阅**。标记为**从未订阅**的个人资料在技术上可以接收电子邮件，尽管他们没有提供明确的同意。要了解有关营销同意及其最佳实践的更多信息，请阅读我们关于[显式同意与隐式同意](https://help.klaviyo.com/hc/en-us/articles/4404203889947)的指南。请注意，对于目录项，Klaviyo 无法从 Dutchie 捕获产品 URL。建议在电子邮件中[将产品设置为未链接](https://help.klaviyo.com/hc/en-us/articles/115000219092#h_01HA9YF09BS80CBMQC520PW9KR)。您可以选择手动将产品链接或指向您网站上任意位置的链接添加到您的电子邮件中。 ## Dutchie 和短信发送

Klaviyo 不允许向 Dutchie 商家发送短信。这是因为移动运营商禁止发送有关[某些物质](https://help.klaviyo.com/hc/en-us/articles/4401822831771#h_01H1VHNYQEWZBEB38FKFHT4DEK)的短信和彩信，其中包括大麻/大麻。 ## Dutchie 用例

以下是使用 Dutchie 数据发送电子邮件的一些示例用例：

- ****产品推荐****
  使用 [Klaviyo 产品源](https://help.klaviyo.com/hc/en-us/articles/115005082787) 根据客户之前的订单向他们发送建议。 - ****VIP客户消息****
  [创建 VIP 细分](https://help.klaviyo.com/hc/en-us/articles/115005065707) 以定位最有价值的客户。 - ****产品教育****
  通过新闻通讯或定向发送向您的客户介绍您提供的产品。 - ****销售和促销通知****
  让您的客户知道促销何时发生，并使用细分来定位客户的首选产品类别。 - ****忠诚度计划沟通和优惠****
  通过[与 Klaviyo 建立 VIP 忠诚度计划](https://academy.klaviyo.com/create-a-vip-loyalty-program) 进一步吸引您的 VIP 客户。 ## 结果

您已将 Dutchie 与 Klaviyo 集成并验证了您的同步数据。现在，您可以根据 Dutchie POS 同步的数据创建自动流消息、个性化营销活动、细分列表等。 ## 为什么我会看到通知“您的帐户正在调用已停用的修订版”？您是否在 Klaviyo 中看到一条通知，上面写着“[需要采取行动]您的帐户正在调用已停用的修订版本”，如下所示？ ![](https://klaviyo.zendesk.com/hc/article_attachments/31085307999771)

请忽略此通知；您目前无需采取任何行动。您的 Dutchie POS 集成由 Klaviyo 管理，并将继续按预期工作。