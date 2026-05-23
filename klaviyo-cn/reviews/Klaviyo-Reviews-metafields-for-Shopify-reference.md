---
id: "23730830399515"
title: "Klaviyo 评论元字段供 Shopify 参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/23730830399515-Klaviyo-Reviews-metafields-for-Shopify-reference"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:33Z"
language: "zh"
---
## 你将会学到

了解如何使用元字段自定义您网站上的 Klaviyo 评论内容。元字段是 Shopify 的工具，用于存储自定义变量以供在整个网站（包括产品页面）上使用。

该资源适用于开发人员。使用 Shopify 元字段需要熟悉 Shopify 的模板语言 [Liquid](https://www.shopify.com/partners/blog/115244038-an-overview-of-liquid-shopifys-templated-language)。您可以使用[可自定义的评论小部件](https://help.klaviyo.com/hc/en-us/articles/16691401577883) 在您的网站上显示评论，而无需编码。

默认情况下启用 Shopify 的 Klaviyo Reviews 元字段。元字段不适用于 WooCommerce。

## 关于评论元字段

将元字段直接插入产品页面将显示存储在元字段中的变量。如果您将 {{product.metafields.reviews. rating.value }} 添加到产品页面，并且该产品的评分为 4.7，则页面加载时元字段的位置将显示“4.7”。

您还可以使用元字段进行更复杂的工作，包括：

- 允许其他 Shopify 应用访问和使用您网站上的 Klaviyo 评论数据。
- 使用条件动态显示具有特定评级的产品的内容。
- 编写您自己的星级评定显示，而不是使用 Klaviyo Reviews 星级评定小部件。

在 **Shopify 产品元字段定义** 页面中，Klaviyo 评论元字段名为 **产品评分计数** 和 **产品评分**。

## 使用主题编辑器添加评论元字段

如果您的[主题支持添加元字段](https://help.shopify.com/en/manual/online-store/themes/theme-struct/sections-and-blocks#metafields-and-dynamic-sources)，请使用动态源图标添加评论元字段。产品页面的产品信息部分支持使用主题编辑器添加评论元字段。

1. 导航至产品页面。
2. 打开（或添加）支持文本的字段。
3. 选择动态源图标。
   ![动态图像图标](https://klaviyo.zendesk.com/hc/article_attachments/30241810707099)
4. 选择评论元字段。
   ![评论元字段选项](https://klaviyo.zendesk.com/hc/article_attachments/30241810710299)
5. 单击****保存****。

## 使用自定义液体添加评论元字段

以下元字段可用于产品页面和产品对象内（例如，集合页面上的产品图块内）。它们在产品对象之外不受支持（例如，您的 **关于** 页面）。

|  |  |  |
| --- | --- | --- |
| ****梅塔菲尔德**** | ****内容**** | ****数据类型**** |
| {{ 产品.metafields.reviews. rating.value }} |产品的平均评分。 |浮动（例如 3.5、4.7）|
| {{ 产品.metafields.reviews. rating\_count }} |为产品提交的评级数量。 |整数（例如 10、45、721）|
| {{product.metafields.reviews. rating.scale\_min }} |可能的最低评级（即 1）。 |整数；总是 1 |
| {{product.metafields.reviews. rating.scale\_max }} |可能的最高评级（即 5）。 |整数；总是 5 |

## 禁用审查元字段

默认情况下启用审阅元字段。要禁用元字段：

1. 导航至 Klaviyo 中的****评论****选项卡。
2. 选择****评论设置****。
3. 选择****常规****。
4. 在 **Shopify** 下，关闭标记为 **将评论元字段同步到 Shopify** 的设置。
5. 单击****保存更改****。