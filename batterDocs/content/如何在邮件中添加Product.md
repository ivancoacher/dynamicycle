---
id: 5493
title: "如何在邮件中添加Product"
slug: "how-to-add-a-product-block-to-an-email"
category: "内容与创意（Content）"
category_slug: "content"
wp_url: "https://dynamicycle.com/docs/how-to-add-a-product-block-to-an-email/"
wp_modified: "2025-12-24T06:02:18"
---

了解如何在 Klaviyo 邮件中插入产品，以便动态展示您的畅销产品或最受欢迎的产品。

产品不支持任何自定义 HTML。如果您想自定义编写产品块代，则需要使用 HTML 模板并手动插入产品信息。产品可以展示目录中的唯一商品，且是基于Product level而非Variant level进行选择的。在产品中无法选择单个多属性。

##### ****在邮件中添加产品****

1.打开您想要插入产品的[邮件](https://www.klaviyo.com/templates/themed)。

2.将 Product模块拖入您的邮件中。

![Klaviyo 邮件编辑界面中的产品模块选项，展示可用的内容块类型，包括文本、图像、按钮和产品块等。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-106.png?resize=418%2C1024&ssl=1)

3.选择产品块类型：

Dynamic：动态产品块根据业务趋势（例如：过去 90 天内的畅销品）展示产品，或者根据 Klaviyo 预测的每位收件人最感兴趣的内容进行个性化展示。

Static： 静态产品展示由您手动选择的固定商品列表。

##### ****创建动态 [Product Feed](https://www.klaviyo.com/catalog/items)****

1.拖入并配置好产品块后，选择 Dynamic作为您的 Product Feed 类型。

2.点击 Create Product Feed。

![界面显示了在Klaviyo中选择产品的选项，包括动态和静态产品块的设置。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-107.png?resize=414%2C1024&ssl=1)

3.为您的 Product Feed 创建一个描述性名称，例如 RECENTLY\_VIEWED\_PRODUCTS。请注意，Product Feed 名称中不允许使用空格（及其他特殊字符）。

4.为您的 Product Feed 设置准则。您可以选择根据整体表现（例如：畅销产品）或收件人行为（例如：最近查看过的项目）来展示产品。

![创建产品信息流的界面，包含产品流名称、包含的目录、优先展示的产品和额外过滤器设置选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-108.png?resize=1024%2C890&ssl=1)

5.点击 Create Product Feed。

6.填写出现的额外字段。

7.若要在创建后编辑 Product Feed，请前往 Content > Products > Product Feed。然后选择您的 Feed 并进行编辑。

8.此选项非常适合自动化邮件 Flows，因为它减少了频繁编辑邮件的需求。通过使用 Product Feeds，您可以根据 Feed 的定义挑选合适的展示项目，因此即使趋势发生变化，您最受欢迎和最流行的产品仍会包含在 Flow 邮件中。

9.对于 Magento 和 Shopify 商店，如果某个产品缺货，我们会将其从您的目录中隐藏，这样它就不会出现在任何 Feed 中。

10.当您选择一个 Feed 并保存所有设置后，您在模板中仍会看到占位项目。如果您是在草稿 Campaign 或 Flow 中编辑模板，可以在 Klaviyo 中预览邮件，以查看 Feed 填充了来自您目录的真实项目。

##### ****从目录中手动选择产品****

对于不同的邮件 Campaigns，您可能希望亲手挑选特定模板中要展示的产品。在产品块中，选择 Static 选项，然后点击 Add Products。在这里，您可以浏览整个产品目录，并从中挑选最多 9 个项目展示在您的模板中。

![产品选择界面，用户可以选择最多 9 件来自目录的产品，展示相关信息，如产品名称和状态。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-109.png?resize=781%2C1024&ssl=1)

- 如果您为一封不会立即发送的邮件（例如：一封 Flow 邮件或预定在未来日期发送的 Campaign）手动选择产品，即使您在网站上修改了产品详情，这些项目信息在发送时也不会动态更新。如果您希望产品能够动态更新，请先创建一个包含这些项目的 Feed，然后使用 Dynamic 选项来展示它们。
- 当您选择了一个或多个项目后，点击 Add Products。
- 如果您使用自定义描述，我们建议将每个描述控制在 120 个字符以内。保持每个项目的描述长度相近，以避免邮件中该板块出现对齐问题。自定义描述仅支持静态 Product Feeds。
- 在选择了一个或多个要展示的产品后，您可能希望重新排列它们在模板中的显示顺序。在产品块设置中通过拖动项目即可重新排序。

![一个界面示例，展示了在邮件中选择产品的选项，包括动态和静态两种模式，并列出了可选的产品。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-110.png?resize=280%2C456&ssl=1)

##### ****设置产品样式****

若要调整产品的外观，请前往该模块的 Styles 选项。在这里，您可以选择显示哪些产品详情（例如：产品名称、价格、促销产品的原价等），并设置它们的样式，包括字体样式、大小和颜色。

![Klaviyo产品模块设置界面，显示产品名称、价格、促销原价、描述、评分和按钮的选择选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-111.png?resize=558%2C738&ssl=1)

###### ****促销产品的原价****

在产品块的 Styles 选项卡中，勾选 Original price for sale products 设置，即可在促销价旁边显示带有删除线的原价。

![一件印有蜂鸟图案的T恤，标示原价28.68美元，现价14.34美元，并带有“立即购买”的按钮。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-112.png?resize=290%2C224&ssl=1)

请注意，此设置仅适用于使用 Shopify、BigCommerce、WooCommerce 和 PrestaShop 的客户。无论是动态还是静态 Product Blocks，系统都会自动检测原价。您可以为 Product Block 中的原价单独设置样式，而不受现价样式的限制。

![产品样式设置界面，显示文本、价格和样式选项的布局](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-113.png?resize=572%2C962&ssl=1)

###### ****显示产品评分****

在 Styles 选项卡中，您还可以选择显示产品的平均评分以及该产品收到的评论数量。这需要您已启用 Klaviyo Reviews 功能。

![产品详情设置界面，包含选项如产品名称、价格、描述、评分及按钮等。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-114.png?resize=678%2C666&ssl=1)

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)