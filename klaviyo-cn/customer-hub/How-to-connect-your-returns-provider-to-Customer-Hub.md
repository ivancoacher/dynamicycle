---
id: "33660683592603"
title: "如何将您的退货提供商连接到客户中心"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/33660683592603-How-to-connect-your-returns-provider-to-Customer-Hub"
section: "Integrate other platforms with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:56:49Z"
language: "zh"
---
## 你将会学到

了解如何将第三方退货管理平台连接到客户中心。此设置允许客户直接从您网站上的客户中心界面开始退货，从而简化退货体验并减轻支持团队的压力。 Shopify 客户中心目前支持标准店面和 Shopify Headless。对于 WooCommerce，请导航至 https://help.klaviyo.com/hc/en-us/articles/47792369863451

有关客户中心功能的反馈，请发送电子邮件至 customerhub@klaviyo.com。 ## 开始之前

在继续之前，请确保您的 Klaviyo 帐户中启用了客户中心功能。 [了解有关客户中心的更多信息](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675)。 ## 支持的退货平台

目前支持以下退货提供商：

- 循环
- 事后
- 包裹实验室
-纳尔瓦尔

如果您不使用这些门户之一，您可以选择****其他****并提供您的退货门户的 URL，或者保持禁用此设置。 Klaviyo 未来将会将此功能扩展到其他平台。 ## 客户中心的退货流程

当登录的客户查看客户中心抽屉中的**订单**选项卡时，他们会看到自己的订单历史记录。单击订单会显示其详细信息、状态以及用于重新购买商品、发货跟踪和访问各种支持渠道的帮助选项。 ![CHreturns4.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34196954781851)

订单交付后，订单详细信息中会出现“开始退货”按钮。客户单击此按钮时的体验取决于您连接的退货提供商：

- ****循环****：
  - 通过 Loop 的深层链接 API，客户可以直接进入 Loop 中的个性化退货工作流程。他们的订单详细信息会安全传递，因此无需手动输入。 - ****Aftership，包裹实验室，纳瓦尔****：
  - Klaviyo 重定向到您平台的门户，并在 URL 中附加订单号和客户的电子邮件。如果平台支持，则会预先填写此信息，以帮助客户开始退货。 - ****其他****：
  - 客户将被发送到您的自定义门户链接，并且必须手动输入订单详细信息，因为 Klaviyo 不会传递任何信息。请注意，将退货平台连接到客户中心不会自动同步两个平台之间的数据。相反，在客户中心内提供指向外部门户的链接，使您的客户可以单击按钮并立即在退货平台内启动特定订单的退货流程。 ### 将您的退货提供商连接到客户中心

在下面选择您的提供商并按照适当的步骤操作。如果您没有看到提供商的名称，请按照“其他”的说明进行操作。

请注意，如果您的客户中心已上线，则保存后会在您的网站上实时发布此更改。如果不是，一旦您在**常规**设置菜单中设置为活动，您就会看到此更改。 ### 连接循环返回

1. 在 Loop 中，从 [**开发人员工具** 页面](https://help.loopreturns.com/en/articles/1911681#finding_api_keys) 复制 API 密钥。 2. 在 Klaviyo 中，导航至****客户中心****。 3. 选择****分机****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/40774432810139)
4. 在**退货**下，打开设置。 5. 选择 ****Loop**** 作为您的退货提供商并粘贴您的 API 密钥。 - 在 Loop 中创建 API 密钥时，确保它具有 ****Order**** 和 ****Return**** 访问权限。 - 仔细检查您的 API 密钥，因为 Klaviyo 不会验证它。如果不正确，客户在开始退货时会看到错误。 ![CHing3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39787595557659)
6. 单击****保存****。当客户单击“开始退货”时，他们将直接进入 Loop 中的个性化退货工作流程。 ### 连接 Aftership、Parcel Lab、Narvar 或其他提供商

1. 在 Klaviyo 的左侧导航中，选择****客户中心****。 2. 选择****集成****。 ![CHsub2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39787606446875)
3. 在 **退货** 下，打开设置，然后选择您的提供商（Aftership、Parcel Lab、Narvar 或其他）。 4. 粘贴​​您的退货门户 URL。 ![CHint4.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39787606455835)
5. 单击****保存****。当客户点击“开始退货”时，他们将被重定向到您的门户。如果支持，则会预先填写订单号和电子邮件以简化流程。 对于“其他”，客户必须手动输入订单详细信息。 ## 禁用您的退货平台

为了防止“开始退货”按钮出现在客户中心的已履行订单上，请断开您的退货平台：

1. 在 Klaviyo 的左侧导航中，选择****客户中心****。 2. 选择****分机****。 3. 在**退货**菜单中，关闭该设置。 4. 单击****保存****。保存此更改将从客户中心内的订单详细信息视图中删除“开始退货”按钮。 ## 其他资源

- [客户中心入门](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675)
- [如何配置客户中心的帮助设置](https://klaviyo.zendesk.com/hc/en-us/articles/33660636674843)
- [如何在客户中心创建内容块](https://klaviyo.zendesk.com/hc/en-us/articles/33660517680795)