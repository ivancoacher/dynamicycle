---
id: "360015054631"
title: "如何在元广告中创建基于价值的相似受众群体"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360015054631-How-to-create-a-value-based-lookalike-audience-in-Meta-Ads"
section: "Meta Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-16T23:06:46Z"
language: "zh"
---
## 你将会学到

了解如何使用 Klaviyo 的 CLV（客户终身价值）数据在元广告中创建基于价值的相似受众群体。本质上，当您从 Klaviyo 导出列表或细分时，您可以将其作为 Facebook 自定义受众上传，并将其用作创建相似受众的来源。在这种情况下，由于您使用的是 CLV 数据，因此您的相似受众将基于价值，从而让您更好地了解向该客户群投放广告的费用。 ## 开始之前

请注意，只有满足以下要求时，CLV 数据才可以导出：

- 至少有500名客户已下订单。这并不是指活跃的个人资料，而是实际在您的企业进行过购买的人数。如果个人资料上的 CLV 部分是空白的，这意味着我们没有足够的关于该人的数据来进行预测。 - 您有电子商务集成（例如 Shopify、BigCommerce、Magento 等）或使用我们的 API 发送下订单。 - 当前集成中您至少有 180 天的订单历史记录，并且在过去 30 天内有订单。 - 您至少有一些客户下了三个或更多订单。您可以阅读有关 [Klaviyo 中的预测分析](https://help.klaviyo.com/hc/en-us/articles/115005247088-Contact-Profiles-in-Klaviyo#predictive-analytics4) 的更多信息以及我们的 [细分指南] CLV](https://help.klaviyo.com/hc/en-us/articles/360013201072)。 ## 导出您的 CLV 段

1. 根据您的业务和广告目标选择要导出的细分；例如，VIP 段。 2. 按照我们的文章[如何将列表或分段导出到 CSV 文件](https://klaviyo.zendesk.com/hc/en-us/articles/115005078687) 中概述的步骤操作。 3. 在 **导出审核** 屏幕上，包含 **电子邮件** 和 **客户生命周期总价值** 属性。如果您愿意，还可以包含更多属性。请查看[Meta 文档](https://www.facebook.com/business/help/185705781836755) 中的详细信息。 ![导出带有属性列表和选中的客户生命周期总价值的评论页面](https://klaviyo.zendesk.com/hc/article_attachments/28716054141723)
4. 您的片段将以 CSV 文件形式保存到您的计算机上。在 Meta 中创建源自定义受众时，请在下一部分中使用此 CSV。 ## 创建源自定义受众

1. 登录您的元广告帐户并创建新的自定义受众群体。 2. 在工作流程中选择****客户文件 > 使用包含客户生命周期价值 (LTV) 的文件****。 ![使用包含以白色突出显示的客户生命周期价值的文件在 Facebook 中创建自定义受众页面](https://klaviyo.zendesk.com/hc/article_attachments/28716054138651)
3. 如果您尚未接受，系统将提示您接受与基于价值的受众群体合作的服务条款。为此，请单击****我接受****。 ![在 Facebook 中使用基于价值的自定义受众协议的要求，底部为深蓝色背景的“我接受”](https://klaviyo.zendesk.com/hc/article_attachments/28716064596635)
4. 接下来，从下拉菜单中选择“**原始数据源**”和“**指定您的受众群体**”，添加要上传的 CSV 文件。 5. 在下一个屏幕上，选择您的客户价值列。从下拉列表中，选择****总客户生命周期价值****将您的 Klaviyo 总 CLV 映射到 Facebook 的 LTV。 ![在 Facebook 中使用 LTV 页面创建客户列表自定义受众](https://klaviyo.zendesk.com/hc/article_attachments/28716064597659)
6. 接下来，预览并映射您的数据；然后，完成受众的创建。现在，您可以选择创建相似的受众群体，我们将在下一节中介绍这一点。 ## 创建基于价值的相似受众

1. 创建 CLV 自定义受众群体后，从上次停下的地方继续，然后单击****创建相似受众群体。 ![后续步骤在 Facebook 中创建客户列表自定义受众页面时创建以白色突出显示的相似受众](https://klaviyo.zendesk.com/hc/article_attachments/28716064599707)****
2. 接下来，对于 **选择您的相似来源**，选择您在上一部分中创建的自定义 CLV 受众群体。 3. 输入您的受众位置和规模，然后单击****创建受众****。 ![在 Facebook 中创建相似的受众页面](https://klaviyo.zendesk.com/hc/article_attachments/28716054151835)
4. 现在，您可以在 Meta 中使用基于价值的相似受众群体进行广告定位。 在 Meta 文档中阅读有关[创建基于价值的相似受众](https://www.facebook.com/business/help/185705781836755) 的更多信息。 ## 通过 Klaviyo 连接源自定义受众

当您将 Klaviyo 列表或细分集成到源自定义受众时，添加到列表或细分的新配置文件将同步到 Meta 自定义受众。您可以将 Klaviyo 列表或细分同步到源自定义受众。如果您通过 Klaviyo 将列表或细分连接到自定义受众，CLV 信息不会自动传递到 Meta。添加到 Klaviyo 列表或细分的新客户将同步到 Meta，但由于我们本身不支持传递 CLV 数据，因此这些客户将使用默认 CLV 值添加到您的源客户受众。这可能会扭曲添加到与源受众相关的任何基于价值的相似受众的客户。 ## 结果

您现在已经了解了如何使用 Klaviyo CLV 在元广告中创建基于价值的相似受众群体。 ## 其他资源

- [通过 Klaviyo 的元广告集成拓展您的业务（Klaviyo 学院课程）](https://academy.klaviyo.com/grow-your-business-with-klaviyos-facebook-advertising-integration)
- [如何在 Facebook 和 Instagram 上启用高级定位](https://help.klaviyo.com/hc/en-us/articles/360039769672-Guide-to-Advanced-Targeting-on-Facebook-and-Instagram)