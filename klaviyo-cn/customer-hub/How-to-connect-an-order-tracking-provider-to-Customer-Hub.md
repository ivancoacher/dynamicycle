---
id: "38357331656347"
title: "如何将订单跟踪提供商连接到客户中心"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/38357331656347-How-to-connect-an-order-tracking-provider-to-Customer-Hub"
section: "Integrate other platforms with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:54Z"
language: "zh"
---
了解如何通过连接受支持的订单跟踪提供商在客户中心显示增强的发货跟踪。默认情况下，客户中心显示来自 Shopify 的跟踪数据，但您可以连接以下提供商之一以获取更多货件详细信息：

- 奇迹
- 马拉莫

如果未连接提供商，则默认显示来自 Shopify 的跟踪信息。

Shopify 客户中心目前支持标准店面和 Shopify Headless。对于 WooCommerce，请导航至 https://help.klaviyo.com/hc/en-us/articles/47792369863451

有关客户中心功能的反馈，请发送电子邮件至 customerhub@klaviyo.com。

## 开始之前

在连接订单跟踪提供商之前，请确保：

- 您的 Klaviyo 帐户中已启用客户中心。
- 您已在 Shopify 中安装并设置 Wonderment 或 Malamo。
- 您选择的提供商的集成已在 Klaviyo 中启用。

## 如何在客户中心处理订单跟踪

当客户在您的 Shopify 网站上登录其帐户并打开客户中心抽屉时，他们可以在 **订单** 选项卡上查看最近的订单，并单击任何订单以获取更多运输详细信息。

****默认情况下（Shopify）****：

- 客户可以查看订单状态、下订单日期和订单号。
- “跟踪发货”按钮链接到 Shopify 的跟踪页面。

****当启用替代订单跟踪提供商（Wonderment 或 Malamo）时****：

客户中心继续以相同的布局显示此信息，但现在订单发货和交货详细信息来自您连接的订单跟踪提供商，并具有以下增强功能：

- “跟踪发货”按钮链接到 Wonderment 或 Malamo 跟踪页面。

  如果您使用 Malomo，请确保您在启用集成之前已在 Malomo 帐户中[创建了品牌跟踪页面](https://help.gomalomo.com/csc/build-with-the-malomo-tracking-page-creator)。否则，您的客户将无法通过“跟踪货件”按钮访问跟踪信息。
- 显示预计交付日期和进度条（如果可用）。
- 货件状态根据提供商事件数据的跟踪数据进行更新，以显示以下状态之一：
  - 已订购
  - 已发货
  - 发货
  - 已交付
- 如果出现延迟、退货或错误，客户中心会根据提供商数据显示描述性状态。

  ![wonder2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38357500045723)

## 连接您的订单跟踪提供商

1. 在 Klaviyo 中，转到主导航中的****客户中心****。
2. 选择****分机****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40774547199259)
3. 在 **订单跟踪** 下，打开开关，然后从下拉列表中选择您的提供商：
   - ****奇迹****
   - ****马拉莫****
     ****！[CHtrack1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39787027837851)****
4. 单击****保存****。

客户中心现在将使用您选择的提供商来获取货件跟踪详细信息。

## 后备行为

如果客户中心无法访问 Wonderment 或 Malamo 中特定订单的数据，它将自动显示 Shopify 的跟踪信息。这可确保您的客户始终看到最新的可用订单状态。

## 其他资源

- [如何在客户中心的订单选项卡上显示帮助按钮](https://help.klaviyo.com/hc/en-us/articles/33660636674843)
- [如何在客户中心显示产品推荐](https://help.klaviyo.com/hc/en-us/articles/33660504643867)
- [如何将您的退货提供商连接到客户中心](https://help.klaviyo.com/hc/en-us/articles/33660683592603)