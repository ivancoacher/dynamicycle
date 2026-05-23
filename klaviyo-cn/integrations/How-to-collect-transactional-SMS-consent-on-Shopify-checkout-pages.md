---
id: "35067557759771"
title: "如何在 Shopify 结帐页面上收集交易短信同意"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/35067557759771-How-to-collect-transactional-SMS-consent-on-Shopify-checkout-pages"
section: "Getting started with Shopify"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-20T17:29:56Z"
language: "zh"
---
只有 Shopify Plus 客户可以在其结帐页面上收集交易同意。非 Plus 客户可以在致谢和订单状态页面上收集交易同意。了解如何在 Shopify 结帐、谢谢和订单状态页面上收集交易短信同意并将其同步到 Klaviyo。您可以通过短信应用程序块在这些页面上收集交易和营销短信同意，您将在 Klaviyo 中设置该应用程序块，然后在 Shopify 中安装。 ## 开始之前

在开始之前，请确保您：

- 启用[Klaviyo SMS](https://help.klaviyo.com/hc/en-us/articles/4404274419355)
- [将 Klaviyo 与 Shopify 集成](https://help.klaviyo.com/hc/en-us/articles/115005080407)
- [启用 Klaviyo 现场跟踪](https://help.klaviyo.com/hc/en-us/articles/4425956184731)

您是目前正在发送[通过短信发送订单更新](https://help.klaviyo.com/hc/en-us/articles/18389135527323) 的 Shopify Plus 客户吗？请注意，在结帐时通过应用程序块收集仅限交易的同意以及收集短信订单更新的同意可能对客户来说可能是重复的；您可能只想使用一项功能。 ## 关于短信应用程序块

- 仅适用于 Shopify Plus：结帐页面（账单、运输和信用卡信息页面以及一页结帐）
- 感谢页面
- 订单状态页面

- 您可以使用短信应用程序块来收集营销同意、交易同意或两者。 - 您可以创建多个短信应用块并将它们放置在不同的页面上，包括：
- 您可以在 Klaviyo 中查看和编辑 SMS 应用程序块，但您必须在 Shopify 中添加或删除它们。 ## 设置您的短信应用程序块

按照以下说明设置短信应用程序块。如果您想创建多个应用程序块以在不同位置收集不同形式的同意，只需重复此过程即可。您还可以在多个 Shopify 页面上安装相同的应用程序块。 - 交易和营销
- 具有可选营销的交易
- 仅限交易
- 未经同意收集电话号码
  ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671634971)
- ****输入标签****
  电话号码字段上的标签。 - ****无效文字****
  表单遇到错误时显示的消息。 - ****提交按钮文本****
  提交按钮上的语言（例如“注册”）。 - ****成功消息****
  用户成功提交电话号码后收到的消息。 1. 在 Klaviyo 中，选择****受众 > 增长工具****。 2. 在 **将应用程序添加到 Shopify 页面以收集 SMS 订阅者** 旁边，选择 ****设置****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36058710841499)
3. 使用描述性的名称为您的应用程序块命名，例如其所在的页面。一个应用程序块可以存在于多个页面上，或者您可以创建多个应用程序块。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36058710844571)
4. 选择短信订阅者要同步的列表。通常，您需要选择在集成设置中选择的相同列表。您的客户将[根据列表的设置](https://help.klaviyo.com/hc/en-us/articles/115005251108) 收到双重选择加入的消息。仅交易订阅者将不会收到双重选择加入消息。 5. 单击****下一步****。 6. 在 **选择同意类型** 下，选择以下选项之一：
7. 接下来，添加应用程序块的标题文本，如下图所示。在右侧，您将看到应用程序块在 Shopify 中的预览。请注意，此预览不会反映您的 Shopify 主题颜色，应用程序块在 Shopify 中安装时将自动继承该颜色。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36058710851739)
8. 单击****下一步****。 9. 如果需要，编辑您的披露文本。然后，单击****下一步****。 10. 编辑应用程序块的附加内容。这些字段是：
11. 完成后，单击****下一步****。 12. 在下一页上，单击复制图标复制应用程序块 ID，并将其保存在可访问的位置。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36058710852763)
13. 现在，您已准备好禁用同意收集（如果需要），然后在 Shopify 中安装应用程序块。 ## 在 Shopify 中禁用短信同意收集

如果您满足以下条件，请考虑禁用 Shopify 的本机复选框以避免结帐页面上出现重复的复选框：

1. 是 Shopify Plus 客户，
2. 之前在结帐时通过 Shopify 的本机复选框收集了营销同意书，以及
3. 希望在结帐时通过短信应用程序块收集营销同意。为此：
4. 在 Shopify 后台中，单击左侧边栏底部的****设置****。 5. 在**设置**页面上，单击****结帐****。 6. 在 **营销选项** 下，关闭 ****短信****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36060438161691)
7. 单击****保存****。请注意，您需要保留 Shopify 集成设置 **将您的 Shopify SMS 订阅者同步到 Klaviyo** 处于选中状态，以便继续将通过其他方式（例如 Shopify 表单）收集的 Shopify 订阅者同步到 Klaviyo。如果您希望通过 SMS 应用程序块订阅的个人资料同步回 Shopify，[请确保启用此设置](https://help.klaviyo.com/hc/en-us/articles/360030919351#h_01HGK64RFVRENS52W53SMSC9NC)。 ## 在 Shopify 中安装应用程序块

1. 在您的 Shopify 后台中，选择****在线商店****。 2. 找到您的 Shopify 主题并单击****自定义****。 3. 选择****主页****下拉列表，然后单击****结帐和客户帐户****以进入结帐编辑器。 4. 选择 ****Checkout**** 下拉列表，然后选择您要放置应用程序块的页面。 5. 滚动到您要添加应用程序块的部分，然后单击****+ 添加应用程序块****。 [了解更多](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-apps#move-place-app)有关放置应用程序块的信息。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671642779)
6. 单击标记为****结帐时选择加入****的 Klaviyo 应用程序块。 7. 在 **Klaviyo 应用程序块 ID** 下，粘贴您从 Klaviyo 保存的 ID。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671644059)
8. （可选）如果需要，您可以打开 **在 Shop Pay 中包含应用程序块**。 9. 单击****保存****。 10. 您现在应该会在您选择的页面上看到您的应用程序块。 ## 管理您的短信应用程序块

要管理您的应用程序块：

1. 导航至****受众 > 增长工具****。 2. 在 **将应用添加到 Shopify 结账页面以收集 SMS 订阅者** 旁边，单击 ****管理****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671645595)
3. 在这里，您将能够查看所有短信应用程序块。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671648155)
4. 要创建新的应用程序块，请单击****创建应用程序****。 5. 如果单击应用程序块旁边的 3 个点，您将看到以下选项：

- ****管理列表****
  管理与您的应用程序块关联的列表
- ****重命名****
  重命名您的应用程序块
- ****编辑****
  编辑您的应用程序块
- ****安装****
  查看有关在 Shopify 中安装应用程序块的说明
- ****克隆****
  克隆您的应用程序块
- ****删除****
  删除 Klaviyo 中的应用程序块。请注意，这不会在 Shopify 中将其删除，但会呈现空白且不占用任何空间。您可以通过选择 Shopify 中的应用程序块，然后单击****垃圾桶****图标来删除该应用程序块。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36058671651483)

## 其他资源

[Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407)

[如何通过Shopify短信发送订单更新](https://help.klaviyo.com/hc/en-us/articles/18389135527323)

[如何单独请求交易同意](https://help.klaviyo.com/hc/en-us/articles/31583129959195)