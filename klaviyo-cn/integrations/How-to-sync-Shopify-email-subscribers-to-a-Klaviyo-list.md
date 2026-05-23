---
id: "115005080667"
title: "如何将 Shopify 电子邮件订阅者同步到 Klaviyo 列表"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005080667-How-to-sync-Shopify-email-subscribers-to-a-Klaviyo-list"
section: "Getting started with Shopify"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "zh"
---
## 你将会学到

了解如何将 Shopify 电子邮件订阅者同步到 Klaviyo 列表、同步的工作原理以及最佳实践。此外，了解谁被添加到您的列表中以及原因。将您的 Shopify 订阅者同步到 Klaviyo 列表非常重要，以便构建同意发送的订阅者列表。 ## 开始之前

如果您尚未阅读我们的 [Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) 指南，了解有关集成的分步说明，然后再继续阅读本文。集成时，请务必检查设置以将 Shopify 电子邮件订阅者同步到 Klaviyo 列表。 ## 如何将订阅者同步到列表

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 从列表中选择****Shopify**** 以进入您的 Shopify 集成设置页面。 3. 在 **同步设置** 下的 **从 Shopify** 选项卡上，选中 **将您的 Shopify 电子邮件订阅者同步到 Klaviyo** 旁边的框。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32924400693147)
4. 选择您想要添加订阅者的列表；作为最佳实践，请将它们添加到您的主列表中，例如您的电子邮件列表。请注意，您无法选择段；您必须将您的订阅者添加到列表中。 5. 如果您没有看到任何列表填充：
   1. 单击****受众****下拉列表并选择****列表和细分****。 2. 单击****创建列表/段****，然后选择****列表**** 创建新列表。 3. 导航回您的 Shopify 集成设置，以查看下拉列表中显示的新列表。 6. 单击****保存。****

当您选中 **将您的 Shopify 电子邮件订阅者同步到 Klaviyo** 时，Klaviyo 会自动同步历史电子邮件订阅者。对于历史订阅者同步，Klaviyo 会根据是否在 Shopify 中订阅配置文件来订阅配置文件，除非该配置文件已存在于 Klaviyo 中。如果配置文件已存在，Klaviyo 将根据其时间戳使用更新的同意状态。 ## 如何将客户添加到我的列表中？ ### 持续的订阅者同步行为

以下信息描述了正在进行的 Shopify 订阅者同步的行为（与集成时最初发生的历史同步相反）。以下是 Shopify 结帐页面上的电子邮件订阅复选框的示例。作为最佳实践，我们建议默认情况下不要选中此框。 ![KlaviyoTees 商店，勾选并以白色突出显示“随时更新新闻和独家优惠”](https://klaviyo.zendesk.com/hc/article_attachments/28716063268763)

在 Klaviyo 中的 Shopify 设置页面上选中 **将 Shopify 电子邮件订阅者同步到 Klaviyo** 设置（如上一节所述）后，您就可以开始收集订阅者。订阅作品的方式如下：

- 订阅者通过 Shopify 的订阅模型从 Shopify 同步到 Klaviyo。 - 首次在 Shopify 中创建的联系人在提供电子邮件并选中复选框后（本质上是在 **结账开始** 步骤）在 Klaviyo 中订阅。 - Shopify 中的现有联系人需要下订单才能订阅。 - 通过任何 Shopify 注册表单（例如页脚表单）订阅的客户也将同步到您的列表。 - 可以在 Klaviyo 中的个人资料中查看电子邮件订阅状态，并且 Klaviyo 中还会记录 **订阅列表事件**。取消订阅的工作方式如下：

- 如果在 Shopify 中取消订阅个人资料，则不会在 Klaviyo 中取消订阅。 - 如果 Klaviyo 个人资料已订阅但在结帐时不同意，则不会在 Klaviyo 中取消订阅（不会发生任何更改）。 - 如果在 Klaviyo 中取消订阅个人资料，然后在结帐时重新订阅，则它们将在 Klaviyo 中重新订阅。 Shopify 将客户资料实时同步到 Klaviyo。请注意，在 Klaviyo 中删除的个人资料不会在 Shopify 中相应删除，反之亦然。 ### Shopify 一页结账

Klaviyo 的 Shopify 集成与 Shopify 一页结帐完全兼容。无论您使用的是一页结帐还是多页结帐，**结帐开始** 事件都会在客户填写电子邮件后触发。如果您自定义了结账，客户可能仍需要进入结账流程的下一步才能触发 **结账开始** 事件。在 Shopify 中创建客户后，其他客户信息将在 Klaviyo 中更新。 ## 最佳实践

### 默认情况下不选中订阅框

我们强烈建议您在 Shopify 结帐页面上保留电子邮件订阅框默认处于未选中状态，以避免积累被动订阅者而损害您的发件人声誉。可以通过在 Shopify 商店管理员中导航至****设置 > 结帐****来调整此选项。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36060405741851)

默认情况下预先选择此框并不是推荐的做法，因为它可能会导致不希望收到您的营销信息的人被添加到您的列表中。他们更有可能取消订阅、忽略您的电子邮件或将您的电子邮件标记为垃圾邮件。如果这些联系人忽略您的电子邮件，他们最终会被过滤为垃圾邮件。如果您的列表中很大一部分由通过这种方式添加的被动订阅者组成，并且您的电子邮件参与度较低，那么您就会[将电子邮件送达率置于风险之中](https://help.klaviyo.com/hc/en-us/articles/115005250368-Strengthen-Your-Sender-Reputation-to-Alleviate-Deliverability-Issues)。通过增加参与订阅者的名单并关注潜在客户的质量而不是数量，您可以为自己做好准备，以实现强大的电子邮件送达率和更高的转化率。 ### 电子邮件订阅者和您的欢迎系列流程

如果通过注册默认 Shopify 注册表单将客户添加到您的电子邮件列表，并且设置了您的欢迎流程（以及您的 Shopify 集成），则该客户将排队等待您的[欢迎系列流程](https://help.klaviyo.com/hc/en-us/articles/115002775172-How-to-Create-an-Email-Welcome-Series)。如果客户在结账时通过单击“**订阅新闻通讯**”框添加到您的电子邮件列表中，他们也会排队等待您的欢迎系列流程。您可以在欢迎系列流中使用流过滤器来过滤掉您希望从该行为中排除的客户组。 ## Shopify Checkout 扩展性兼容性

Checkout Extensibility 是 [Shopify 的新结帐基础](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility)，取代了现已弃用的 **checkout.liquid** 文件。 Klaviyo 的 Shopify 集成已经与 Checkout Extensibility 完全兼容，并且由于您尚未进行任何 checkout.liquid 自定义，因此不需要集成更新。 ## 寻找有关接受营销财产的信息？ 2022 年 12 月 14 日，Klaviyo 发布了一项更新，更改了电子邮件订阅者从 Shopify 同步到 Klaviyo 的方式。此同步以前依赖于 Shopify 的 **接受营销** 标签，但现在，订阅者通过 Shopify 的订阅模型进行同步。对于希望使用它的客户，此属性仍会同步到 Klaviyo，但它不再确定 Klaviyo 中的订阅状态，并且[自已被弃用] Shopify]（https://shopify.dev/changelog/removal-of-accepts-marketing-fields-in-admin-api-customer-resources#:~:text=As%20of%20API%20version%202024，emailMarketingConsent%20should%20be%20used%20。）。要了解订阅者如何在 2022 年 12 月 14 日之前从 Shopify 同步到 Klaviyo，请查看我们的 [Shopify 接受营销订阅者参考](https://help.klaviyo.com/hc/en-us/articles/25184578360603)。 ## 结果

您现在已经了解了如何将 Shopify 电子邮件订阅者同步到 Klaviyo 列表以及管理电子邮件订阅者的最佳实践。 ## 其他资源

- [集成同步参考频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)
- [Shopify数据参考](https://help.klaviyo.com/hc/en-us/articles/115005080447)
- [如何使用Shopify标签过滤客户](https://help.klaviyo.com/hc/en-us/articles/115005080907)