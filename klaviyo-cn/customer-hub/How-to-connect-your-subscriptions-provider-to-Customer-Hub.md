---
id: "39786250669083"
title: "如何将您的订阅提供商连接到客户中心"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/39786250669083-How-to-connect-your-subscriptions-provider-to-Customer-Hub"
section: "Integrate other platforms with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:55Z"
language: "zh"
---
了解如何通过连接 Recharge、Skio 或 Shopify 订单数据在客户中心显示订单的订阅详细信息。

客户中心目前支持 Shopify 店面，包括 Shopify Headless。计划提供更多电子商务平台支持。

有关客户中心功能的反馈，请发送电子邮件至 customerhub@klaviyo.com。

## 开始之前

- 确保您的 Klaviyo 帐户中启用了客户中心。
- 如果您要连接受支持的订阅应用程序（Recharge 或 Skio）：
  - 确保 [Recharge 应用程序](https://apps.shopify.com/subscription- payments) 或 [Skio 应用程序](https://apps.shopify.com/skio) 已在您的 Shopify 商店中设置并处于活动状态。
  - 确保应用程序与 Klaviyo 集成
- 如果您使用 Shopify 订单数据，则无需额外设置。

## 订阅信息如何在客户中心显示

当客户在您的 Shopify 网站上登录其帐户并打开客户中心抽屉时，他们可以在 **订单** 选项卡上查看最近的订单。通过连接订阅提供商，您可以在订单中每个适用产品旁边显示订阅详细信息，以便客户轻松识别哪些产品是订阅的一部分，哪些是独立购买的产品。

订阅设置默认处于关闭状态。如果订阅应用程序和 Shopify 订单数据均未连接，则客户中心中不会显示任何订阅信息。

订阅详细信息的显示方式有所不同，具体取决于您启用的连接：

****支持的订阅应用程序（Recharge、Skio）****：

- 作为订阅的一部分购买的产品会在这些项目旁边显示带有订阅名称（例如“每月”）的徽章。
- 显示**管理订阅**链接，引导客户直接进入订阅应用程序体验以查看或管理他们的订阅。
  ![CHsub1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39786233689499)

  ****Shopify 订单数据****：
- 作为订阅的一部分购买的产品会在这些项目旁边显示带有订阅名称的徽章。
- 没有管理订阅的按钮或选项。

对于一次性购买的产品，不会显示订阅徽章或订阅管理链接。如果订单同时包含订阅和非订阅产品，则只有订阅商品才会显示这些详细信息。

## 连接您的订阅提供商

1. 在 Klaviyo 中，转到主导航中的****服务 - 客户中心****。
2. 选择****分机****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/40774370368283)
3. 在 **订阅** 下，打开设置，然后选择以下选项之一：

   - ****充电****
   - ****斯基奥****
   - ****Shopify 订单数据****
   - ****Ordergroove****！[图片 (32).png](https://klaviyo.zendesk.com/hc/article_attachments/47652072240027)
4. 单击****保存****。

客户中心现在将使用您选择的选项在客户订单中的适用产品旁边显示订阅详细信息。

## 可选：添加订阅内容块

与将配置文件数据写入 Klaviyo 的所有集成一样，您可以使用[内容块](https://klaviyo.zendesk.com/hc/en-us/articles/33660517680795) 来显示动态信息。请注意，对于某些内容块，例如我们为充值提供的模板，没有默认链接集。您必须设置内容块的链接并将其链接到您的订阅登录页面。在您设置此链接之前，虽然内容块可以显示活动订阅计数等数据，但单击内容块不会执行任何操作，因为未设置链接。

## 其他资源

- [如何在客户中心显示产品推荐](https://klaviyo.zendesk.com/hc/en-us/articles/33660504643867)
- [如何将您的评论提供商连接到客户中心](https://help.klaviyo.com/hc/en-us/articles/33660618974491)
- [如何向客户中心订单选项卡添加帮助按钮](https://help.klaviyo.com/hc/en-us/articles/33660636674843)