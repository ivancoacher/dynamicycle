---
id: "13913401149595"
title: "了解 Klaviyo 如何监控流量的指标活动"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/13913401149595-Understanding-how-Klaviyo-monitors-metric-activity-for-flows"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:27Z"
language: "zh"
---
了解 Klaviyo 如何通过用于触发 Klaviyo 帐户中的流量的电子商务指标来监控异常活动并提醒您。当某个指标的活动突然下降时，您会收到警报，以便您解决潜在问题。这种类型的监控也称为异常检测。 ### 监控哪些指标？指标警报支持电子商务指标，例如**已下订单**、**已完成订单、已开始结帐**和**添加到购物车**，还支持使用 Klaviyo 的 [指标 API](https://developers.klaviyo.com/en/reference/metrics_api_overview) 和 [事件 API](https://developers.klaviyo.com/en/reference/events_api_overview) 设置自定义指标。 ## 开始之前

如果您尚未这样做，请在您的帐户中启用并配置电子商务集成。要开始使用，请参阅 Klaviyo 的[电子商务集成列表](https://help.klaviyo.com/hc/en-us/articles/115000256472)。否则，与开发人员合作[使用 Klaviyo 的 API 创建自定义集成](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration)。 ## 指标监控的工作原理

如果您的某一电子商务指标的活动与您账户的历史活动相比突然下降，Klaviyo 会向您发出提醒。当检测到指标活动异常下降时，您将收到多种不同方式的通知：

- 向帐户所有者、管理员和经理发送电子邮件
- 应用内通知
- 在**主页**选项卡的顶部
  ![](https://klaviyo.zendesk.com/hc/article_attachments/40155941349147)
- 在受影响流标题旁边的 **流** 选项卡上
  ![](https://klaviyo.zendesk.com/hc/article_attachments/40155941352731)
- 单击流程触发器时在流程构建器的侧栏中

![](https://klaviyo.zendesk.com/hc/article_attachments/40155941354907)

## 消除或抑制警报

如果活动下降是预期的或已经在调查中，您可以忽略或抑制警报以防止它们显示在您的帐户中。 - 解除警报将导致警报消息消失，直到再次触发为止。 - 抑制警报将防止该指标再次触发警报，直到指定的时间。 - ****抑制30天****
  - ****抑制 60 天****
  - ****抑制120天****
  - ****压制365天****

  要消除警报：

  1. 如果您位于 **主页** 选项卡，请通过单击指标警报上的****查看受影响的流****导航到受影响的流。否则，从 **流** 选项卡导航到受影响的流。 2. 单击流程的触发器。 3. 在触发器设置侧栏中，单击****关闭****。要抑制警报：
  4. 如果您位于 **主页** 选项卡，请通过单击指标警报上的****查看受影响的流****导航到受影响的流。否则，从 **流** 选项卡导航到受影响的流。 5. 单击流程的触发器。 6. 单击“****关闭****”按钮旁边的箭头。 7. 单击以下选项之一：

选择抑制选项后，将显示一条成功消息，并显示抑制到期的日期。抑制期结束后，如果仍然检测到活动下降，警报将继续触发，直到您再次抑制它们。 ## 解决活动突然下降的问题

虽然活动突然下降可能令人震惊，但对于这种现象有一些常见的解释。您的电子商务商店的具体原因包括：

- 维护您的商店或托管您商店的服务器
- 您的电子商务平台的服务器暂时中断

  检查商店的设置或内部日志以了解任何计划的维护。如果您托管在 Shopify 或 BigCommerce 等付费平台上，请检查其公开状态页面以获取有关服务器中断和停机时间的信息。状态页面通常由服务的主 URL 和添加到开头的状态子域组成，如下例所示：
- [https://status.shopify.com](https://status.shopify.com/)
- <https://status.bigcommerce.com>

有关 Klaviyo 的具体原因，请查看以下部分。单击与您的问题相关的部分以了解更多信息。 ****您最近是否切换到其他电子商务平台？****

迁移电子商务平台时，请确保将用于触发流的指标更新为新电子商务平台的指标。 例如，如果您要从 BigCommerce 切换到 Shopify，您帐户的现有流程可能仍会设置为使用 BigCommerce 的 **已下订单** 指标，而不是 Shopify 的 **已下订单** 指标。请参阅以下指南以获得进一步帮助：

- [如何更改流程触发器](https://help.klaviyo.com/hc/en-us/articles/115002775052-How-to-change-a-flow-trigger)
- [切换电子商务平台后更新 Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360003124151-Updating-Klaviyo-After-Switching-Ecommerce-Platforms)
- [如何更改流量和营销活动报告的转化指标](https://help.klaviyo.com/hc/en-us/articles/115005199947-How-to-Change-the-Conversion-Metric-for-Flow-and-Campaign-Reports)

****对于 BigCommerce，您更改了商店的主题吗？****

某些指标（例如**查看的产品**和**添加到购物车**）需要将代码片段安装到商店的主题文件中。如果您更改了商店的主题，请确保重新安装这些代码片段。对于 **查看的产品**，请参阅此集成的设置指南：

- [BigCommerce 入门](https://help.klaviyo.com/hc/en-us/articles/115005082547#add-viewed-product-tracking4)

  对于 **添加到购物车**，请参阅这篇文章：
- [如何为 BigCommerce 创建“添加到购物车”事件](https://help.klaviyo.com/hc/en-us/articles/360024310292-How-to-create-an-Added-to-Cart-event-for-BigCommerce)

****您使用的是自定义集成还是第三方集成？****

虽然 Klaviyo 为定制和第三方集成的开发提供资源，但这些类型的集成是在没有 Klaviyo 直接参与的情况下创建和管理的。如果您在此类集成中遇到问题，请联系您的开发团队或与第三方集成相关的支持团队以获得进一步帮助。有关 API 调用的更多信息，请参阅我们关于 [Klaviyo API 入门](https://help.klaviyo.com/hc/en-us/articles/360045726811#make-your-first-call4) 的文章。 ****您的电子商务集成是否在 Klaviyo 中启用并配置？****

有一些常见情况可能会导致之前正在运行的集成停止：

- 如果您正在使用电子商务平台的免费试用版，并且试用版已过期。 - 如果您商店的 URL 已更改但未在 Klaviyo 中更新。 - 如果您重新安装了集成但未完全配置它。如果您使用的是 Klaviyo 的预构建集成之一，请按照以下步骤确认您的电子商务集成已安装并启用：

1. 选择****集成****选项卡。 2. 查找您的电子商务平台的名称。 3. 检查并确保**状态**列将集成列为**已启用**。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720896311451)
4. 如果您的电子商务集成未列为已启用，请[在 Klaviyo 帮助中心搜索设置指南](https://help.klaviyo.com/hc/en-us/articles/115000256472) 以获取进一步说明。 5. 如果您的电子商务集成已启用，请选择它以查看其配置。 6. 查看集成设置页面的内容。根据集成情况，
   确保在与您的商店 URL 或任何凭据相关的字段中输入正确的信息。 7. 如有必要，更正设置页面上的任何信息，然后单击页面底部的****更新设置****、****保存****或****连接****。 ****您的服务器上是否使用防火墙或安全软件？****

如果您有防火墙或安全措施，例如 Sucuri、Cloudflare 或类似的措施，这可能会无意中阻止 Klaviyo 与您的商店通信，或限制可同步的速度和数据量。了解如何[将 Klaviyo 集成流量列入白名单](https://help.klaviyo.com/hc/en-us/articles/19143781289115)。 ### 查看我们的故障排除指南以了解特定指标

如果您在前面的部分中找不到解决方案，请参阅以下文章，了解有关特定指标的其他故障排除步骤：

- [已查看商品跟踪问题排查](https://help.klaviyo.com/hc/en-us/articles/4416172774939-Troubleshooting-Viewed-Product-tracking)
- [添加到购物车跟踪的疑难解答](https://help.klaviyo.com/hc/en-us/articles/6985692431259-Troubleshooting-Added-to-Cart-tracking)
- [疑难解答开始结帐跟踪](https://help.klaviyo.com/hc/en-us/articles/6998274713371-Troubleshooting-Started-Checkout-tracking)
- [已下订单跟踪问题排查](https://help.klaviyo.com/hc/en-us/articles/7000906101019-Troubleshooting-Placed-Order-tracking)