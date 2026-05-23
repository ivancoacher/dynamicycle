---
id: "115000219092"
title: "如何将产品块添加到电子邮件中"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115000219092-How-to-add-a-product-block-to-an-email"
section: "Build and use products "
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:56:35Z"
language: "zh"
---
## 你将会学到

了解如何在 Klaviyo 电子邮件中插入产品块，以便动态展示您最畅销或最受欢迎的产品。产品块不支持任何自定义 HTML。如果您想对产品块进行自定义编码，则需要使用 HTML 模板并手动插入产品信息。产品块可以显示目录中的唯一项目，并根据产品级别（而不是变体级别）选择项目。无法在产品块中选择单个变体。默认情况下，产品区块功能适用于我们的文章[如何使用产品 Feed 和推荐](https://help.klaviyo.com/hc/en-us/articles/115005082787-How-to-Use-Product-Feeds-and-Recommendations) 中列出的电子商务平台。如果您使用此处未列出的电子商务平台，则需要按照我们的指南[将自定义目录源同步到 Klaviyo](https://developers.klaviyo.com/en/docs/guide-to-syncing-a-custom-catalog-feed-to-klaviyo) 将产品目录同步到 Klaviyo。 ## 将产品块添加到电子邮件中

1. 打开要插入产品块的电子邮件。 2. 将产品块拖到您的电子邮件中。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34829029970587)
3. 选择产品块类型：

   - ****动态****
     动态产品块根据业务趋势（例如过去 90 天内的畅销产品）显示产品，或者根据 Klaviyo 预测每个收件人最感兴趣的内容为每个收件人定制产品。了解如何创建动态产品源。 - ****静态****
     静态产品块显示您选择的一组项目列表。 4. 根据您的选择填写显示的附加字段。 ### 创建动态产品提要

1. 拖动并配置产品块后，选择****动态****作为产品 Feed 类型。 2. 单击****创建产品源****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34829073480731)
3. 为您的产品 Feed 创建一个描述性名称，例如 RECENTLY\_VIEWED\_PRODUCTS。请注意，产品 Feed 名称中不允许使用空格（和其他特殊字符）。 4. 设置产品 Feed 的标准。您可以选择根据整体表现（例如最畅销的产品）或收件人行为（例如最近查看的商品）来显示产品。详细了解[产品 Feed 设置](https://help.klaviyo.com/hc/en-us/articles/115005082787-How-to-use-product-feeds-and-recommendations)。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34829029974427)
5. 单击****创建产品源****。 6. 填写出现的附加字段。要在创建产品源后对其进行编辑，请导航至****内容 > 产品 > 产品源****。然后，选择您的提要并对其进行编辑。此选项非常适合自动化电子邮件流，因为它减少了频繁编辑消息的需要。借助产品 Feed，您可以根据 Feed 的定义来策划合适的商品，这样即使趋势发生变化，您最受欢迎和最热门的商品也将包含在您的流电子邮件中。对于 Magento 和 Shopify 商店，如果产品缺货，我们会将其从您的目录中隐藏，这样它就不会出现在任何 Feed 中。当您选择 Feed 并保存所有设置时，您仍会在模板中看到占位符项目。如果您将模板作为草稿营销活动或在流程中进行编辑，则可以在 Klaviyo 中预览电子邮件，以查看目录中填充的真实项目。 ### 从目录中手动选择产品

对于不同的电子邮件营销活动，您可能需要手动选择合适的产品以在给定模板中展示。在产品块中，选择****静态****选项，然后单击****添加产品****。在这里，您可以浏览整个产品目录并选择最多九个项目以在模板中展示。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34829073488539)

如果您为不会立即发送的消息（即流电子邮件或计划在未来日期进行的营销活动）手动选择产品，则即使您在网站上对产品详细信息进行编辑，项目详细信息也不会在发送时动态更新。如果您希望产品动态更新，请首先创建包含这些项目的提要，然后使用****动态****选项来显示它们。选择一项或多项后，单击****添加产品****。如果您使用自定义描述，我们建议将每个描述的长度控制在 120 个字符以内。 使每个项目的描述保持相似的长度，以避免与电子邮件中的此块出现对齐问题。仅静态产品 Feed 支持自定义描述。如果您使用启用了 Shopify Markets 的区域设置感知目录，****本地化收件人**** 复选框将出现在您的静态产品阻止设置中。 ![](https://klaviyo.zendesk.com/hc/article_attachments/47692381022235)

启用****为收件人本地化****后，静态产品块中的产品将自动显示与发送时每个收件人的语言和区域相匹配的本地化定价、货币和产品信息。这意味着一封电子邮件可以向美国收件人显示美元定价，向英国收件人显示英镑定价，向澳大利亚收件人显示澳元定价，而无需为每个市场创建单独的电子邮件或产品块。如果收件人无法获得区域设置数据，则产品块将回退到您的 Shopify 商店中配置的默认市场。如果您希望所有收件人看到相同的产品信息，无论其所在地区如何，您可以取消选中****为收件人本地化****。在将产品添加到区块时，您可以通过选择语言和区域来手动选择产品的本地化版本，以及包含标题、价格和 URL 等本地化产品信息的产品。 ![](https://klaviyo.zendesk.com/hc/article_attachments/45236420399771)

选择要展示的一种或多种产品后，您可能需要重新排列这些项目在模板中的显示方式。拖动产品块设置中的项目以重新排序。 ![productblockmove2gif.gif](https://klaviyo.zendesk.com/hc/article_attachments/34829029985691)

## 设置产品块的样式

要调整产品块的外观，请转到该块的****样式****选项卡。在这里，您可以选择显示哪些产品详细信息（例如产品名称、价格、销售产品的原价等）以及它们的样式，包括字体样式、大小和颜色。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34829029990299)

### 销售产品原价

在产品块的 **样式** 选项卡中，检查设置****促销产品的原价****，以在促销价格旁边显示带有删除线的原价。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34829029992219)

请注意，此设置仅适用于使用 Shopify、BigCommerce、WooCommerce 和 PrestaShop 的客户。动态和静态产品块的原始价格都会自动检测。您可以在产品块中设置原始价格的样式，与设置价格的样式分开。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34829073497883)

## 显示产品的评级

在 **样式** 选项卡中，您还可以选择显示产品已收到的平均评分和评分数量。这需要您启用 Klaviyo Reviews。了解[如何在带有产品块的电子邮件中显示产品评级](https://klaviyo.zendesk.com/hc/en-us/articles/32781276130075)。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34829073499931)

## 其他资源

- [如何使用产品源和推荐](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787)
- [如何创建基本模板](https://klaviyo.zendesk.com/hc/en-us/articles/115005083887)