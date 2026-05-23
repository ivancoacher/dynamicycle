---
id: "7000906101019"
title: "已下订单跟踪故障排除"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/7000906101019-Troubleshooting-placed-order-tracking"
section: "Metrics troubleshooting"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:55:05Z"
language: "zh"
---
## 开始之前

**已下订单** 跟踪包含在电子商务集成中，不需要任何额外的设置。在查阅本指南之前，请确保您已正确设置、配置并启用电子商务集成。对于所有电子商务集成，**已下订单** 事件会跟踪客户何时完成结账流程并在您的商店中创建订单，但对于以下集成，Klaviyo 仅当订单达到特定状态并在电子商务平台中具有特定状态时才跟踪 **已下订单** 事件：

- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082587)
  默认情况下，任何具有以下状态的订单都不会同步为**已下订单**：**不完整**、**待处理**、**等待付款**
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115003458852)
  状态为 **待付款** 的订单将被忽略
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/360030732832)
  订单状态必须为 **处理** 才能触发 **已下订单** 事件
- [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360055123191)
  订单状态必须为 **处理** 才能触发 **已下订单** 事件
- [Shift4Shop](https://help.klaviyo.com/hc/en-us/articles/115005083107)
  订单状态必须为 **2** 或 **4** 才能触发 **已下订单** 事件

如果您使用的电子商务平台没有预构建的 Klaviyo 集成或自定义平台，请在我们的开发者网站上了解[如何启用已下订单跟踪](https://developers.klaviyo.com/en/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration#placed-order)。 ## 测试下订单事件

**已下订单** 事件通常用于设置购买后流程，例如感谢流程。如果您最近设置了帐户并尝试从 Klaviyo 的流程库创建购买后流程，您可能会遇到以下警告消息：

“我们最近没有收到任何**已下订单**事件。如果您认为可能存在问题，请联系我们的成功团队寻求帮助。”

这并不一定意味着您的帐户或集成存在问题，但可能意味着尚未触发**已下订单**事件。这可能是因为您的商店是新的。您可以按照以下步骤触发事件以使此警告消失。由于 **已下订单** 事件是从交易中触发的，Klaviyo 支持人员无法为您测试 **已下订单** 事件跟踪。 Shopify 等一些电子商务平台提供了下测试订单的方法。有关如何下测试订单的信息，请参阅您平台的帮助文档。否则，您可以下真实订单并退款以测试您的集成。要使用真实交易测试您的**已下订单**跟踪是否已正确设置，请按照以下步骤操作：

1. 导航至您的网站
2. 导航至您网站上的产品页面以获取可用产品
3.点击页面上的“添加到购物车”按钮
4. 继续结帐购物车中的商品
5. 使用真实信用卡或其他付款方式完成结帐
6. 如果您使用第三方支付提供商，请登录您的支付提供商以确保资金已得到处理
7.尽快取消并退款订单给自己退款
8. 在 Klaviyo 中搜索您结帐时使用的电子邮件地址

![搜索栏位于 Klaviyo 的右上角，您可以通过电子邮件地址搜索个人资料。](https://klaviyo.zendesk.com/hc/article_attachments/28723544866971)

您应该看到已为您创建了 Klaviyo 个人资料（如果尚不存在），并且已在您的活动源上跟踪 **已下订单** 事件。由于某些电子商务平台的限制，并非所有电子商务集成都会实时同步数据。对于某些集成，您可能需要等待 30 分钟到一个小时才能跟踪事件。请参阅我们关于[集成同步的频率](https://help.klaviyo.com/hc/en-us/articles/115005253208) 的文章以了解更多信息。 ## 故障排除场景

查看以下问题以诊断您的 **下订单** 问题的原因。请注意，某些步骤是通用的，其他步骤取决于您使用的电子商务平台。 ****您是否也遇到触发其他指标的问题？****

如果您在跟踪其他指标以及**已下订单**时遇到问题，则您的集成设置可能存在问题。 请按照以下步骤检查您的集成设置是否正确：

1. 如果按键两侧看起来匹配，请检查按键前后是否有空格。删除所有前导或尾随空格，因为它们可能会导致错误。 1. 导航至您帐户的 **集成** 页面
2. 在 **启用的集成** 选项卡中，确保您的电子商务集成位于列表中。否则，请按照本文[开始之前部分](#h_01G6W9BDQH54CC3N49MYC0PN22)中链接的相关设置指南，确保您已正确遵循设置和配置电子商务集成的所有步骤。 3. 如果您的电子商务集成已启用，请单击****查看设置****以检查是否有与集成相关的任何错误消息以及是否已填写所有必填字段。 ![集成设置链接位于“启用的集成”选项卡中每个集成的右侧。](https://klaviyo.zendesk.com/hc/article_attachments/28723522895515)
4. 如果您的集成需要使用公共 API 密钥、私有 API 密钥、消费者密钥和/或消费者秘密，请确保 Klaviyo 中的信息与您的电子商务平台中的信息匹配。 ****您最近更换过电子商务平台吗？****

迁移电子商务平台时，请确保将用于触发流和分析中的指标切换为新电子商务平台的指标。例如，如果您要从 BigCommerce 切换到 Shopify，您帐户的分析和流程可能仍会设置为使用 BigCommerce 的 **已下订单** 指标，而不是 Shopify 的 **已下订单** 指标。请参阅以下指南以获得进一步帮助：

- [切换电子商务平台后更新klaviyo](https://help.klaviyo.com/hc/en-us/articles/360003124151-Updating-Klaviyo-After-Switching-Ecommerce-Platforms)
- [如何更改流量和营销活动报告的转化指标](https://help.klaviyo.com/hc/en-us/articles/115005199947-How-to-Change-the-Conversion-Metric-for-Flow-and-Campaign-Reports)
- [如何更改流程触发器](https://help.klaviyo.com/hc/en-us/articles/115002775052-How-to-change-a-flow-trigger)

****您是否对已下订单使用自定义订单状态？****

对于某些集成，**已下订单** 事件会根据特定订单状态在 Klaviyo 中触发。请参阅本文的[开始之前部分](#h_01G6W9BDQH54CC3N49MYC0PN22)，了解具有订单状态要求的集成列表。如果您使用非标准或自定义订单状态，请[联系 Klaviyo 支持](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support) 更改您的集成配置，以允许将其他订单状态作为 **已下订单** 事件进行跟踪。 ****您的服务器上是否使用防火墙或安全软件？****

如果您启用了防火墙或安全措施，例如 Sucuri、Cloudflare 或类似的措施，这可能会无意中阻止 Klaviyo 与您的商店通信，或者限制可同步的速度和数据量。由于 Klaviyo 使用动态 IP，因此我们不提供白名单 IP 范围。相反，我们建议将我们的用户代理列入白名单，即：****Klaviyo/1.0****

如果您不确定如何将 Klaviyo 列入白名单，请查阅安全软件文档，了解如何将用户代理列入白名单。 ****对于 WooCommerce 和 Magento 用户：您是否使用最新版本的集成插件？****

如果您使用的是 WooCommerce 或 Magento，**已下订单** 跟踪问题可能与您平台的 Klaviyo 插件的其他问题有关。 1. 如果未跟踪 **已下订单** 事件，请通过在 Klaviyo 的 ****Analytics > Metrics**** 中搜索 **Started Checkout** 来检查 **Started Checkout** 事件是否正在跟踪。 2. 如果 **已下订单** 和 **开始结帐** 均未跟踪，则您的插件可能存在问题。 3. 检查您是否使用最新版本的插件进行集成。如果需要，请更新到 WooCommerce 或 Magento 中的最新版本，或者您可以从相关平台的列表中下载最新版本。 - [安装向导安装](https://marketplace.magento.com/klaviyo-magento2-extension.html)
- [Composer 安装](https://packagist.org/packages/klaviyo/magento2-extension)

- [Klaviyo WordPress (WooCommerce) 插件](https://wordpress.org/plugins/klaviyo/)
- [Klaviyo Magento 1 扩展](https://www.klaviyo.com/media/downloads/MagentoKlaviyo-Latest.tgz)
- Klaviyo Magento 2 扩展

## 联系 Klaviyo 支持

如果您在查阅此列表并测试跟踪后仍然遇到问题，请通过我们的[社区](https://community.klaviyo.com/got-a-question-1)或我们的[支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)联系。了解如何对其他指标进行故障排除：

其他资源：