---
id: "115003492771"
title: "支持多个 Magento 商店的指南（适用于 Magento 2.x）"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115003492771-Guide-to-supporting-multiple-Magento-stores-for-Magento-2-x"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:14Z"
language: "zh"
---
## 概述

如果您有一台 Magento 2 服务器托管多个商店，那么在设置 Klaviyo 时您有两种选择：

1. ****为每个 Magento 2 商店创建单独的 Klaviyo 帐户****如果您有兴趣为每个 Magento 2 商店创建单独的 Klaviyo 帐户，请单击 Magento 2 集成页面上的高级选项以检索商店列表，然后选择要同步到正在使用的 Klaviyo 帐户的商店。 2.****将所有商店数据同步到单个 Klaviyo 帐户****此选项要求您使用 Klaviyo 的细分生成器和流过滤器功能来单独利用每个商店的数据。由于 Klaviyo 目前尚未针对在单个帐户中支持多个品牌进行优化，因此我们建议仅对同一品牌的多种语言（例如英语和法语商店）或您拥有同一品牌的在线/离线商店时使用此方法。 ## 为每个 Magento 商店创建单独的 Klaviyo 帐户

如果您有兴趣为每个 Magento 2 商店创建单独的 Klaviyo 帐户，您可以在 Magento 2 集成页面上选择要连接到帐户的特定 Magento 2 商店。 [与 Magento 集成](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348) 时，如果您选中设置****仅同步特定的 Magento 2 商店****，Klaviyo 将为您提供要同步的选项。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711673376155)

此处选择一家或多家商店意味着 Klaviyo 将专门同步这些所选商店的客户和订单数据。如果您不选中此设置，并且将来添加了新商店，则来自该新商店的数据此时也将开始同步到 Klaviyo。 ## 将所有商店数据同步到单个 Klaviyo 帐户

当您将一台拥有多个商店的 Magento 2 服务器集成到一个 Klaviyo 帐户时，我们会将每个商店的所有配置文件和订单数据同步到该帐户中。此外，我们将为创建的每个配置文件同步 **Magento 商店名称** 和 **Magento 网站 ID** 属性，以便您知道该配置文件来自哪个商店。然后，您将能够在逐个站点级别配置我们的扩展，以选择将订阅者添加到哪个列表，并且您可以使用 Magento 2 商店名称过滤流和段，以分隔商店之间的流。然而，如上所述，Klaviyo 目前尚未优化以支持单个帐户中的多个商店。这意味着不可能在单个 Klaviyo 帐户中完全隔离每个商店的数据。 ## 将 Klaviyo Magento 扩展范围限制为单个商店视图

当您安装 Klaviyo Magento 扩展时，您将能够在特定配置范围内启用它。如果您想在逐个站点级别配置我们的扩展，您只需移动范围并为每个视图设置正确的 Klaviyo API 密钥即可。确保在网站级别以及商店视图级别设置这些 API 密钥。下面的屏幕截图显示了所有可用的商店范围。在这里，您还可以看到英语商店关联的 Klaviyo 帐户的 API 密钥。 ![2021-03-22_10-50-19.png](https://klaviyo.zendesk.com/hc/article_attachments/28711661193755)

同时，下面的屏幕截图使用相同的站点，只是现在选择了法国商店。还会添加该商店关联的 Klaviyo 帐户的 API 密钥。 ![2021-03-22_13-37-59.png](https://klaviyo.zendesk.com/hc/article_attachments/28711661199131)

## 查找您的 Magento 商店的商店 ID

您的 Klaviyo 帐户中的每个 Magento 商店都会分配一个唯一的**商店 ID**。使用此属性可以使每个 Magento 商店的流程保持不同。要查找您的 Magento **商店 ID**，请导航到 Klaviyo 并选择 **集成**** 选项卡。选择****Magento 2**** 并向下滚动到**高级**设置。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711673378459)

请注意，每个商店都与一个不同的商店 ID 相关联，您可以使用该 ID 来过滤流。 ## 多个 Magento 2 商店的流程

您可能想要为多个 Magento 商店设置不同的消息传递。例如，如果您的 Magento 商店支持多种语言，您可能需要创建一个购买后流程，并为法语商店和英语商店创建不同的流程分支。您可以通过根据 **MagentoStore** 配置文件属性创建条件拆分来实现此目的。 这是一个基于 **MagentoStore** 配置文件属性进行条件分割的购买后流程示例。此流程拆分为 Magento 2“French”商店创建流程分支：

![](https://klaviyo.zendesk.com/hc/article_attachments/29859702292251)

可以根据等于 **English-UnitedStates** 的 **MagentoStore** 值创建另一个分支。 ## 多个 Magento 商店的注册表单

您需要为每个 Magento 商店自定义注册表单。 - 您可以为每个 Magento 商店设计独特的形式
- 您可以使用一张注册表单并[根据动态变量显示或隐藏块](https://klaviyo.zendesk.com/hc/en-us/articles/115005258208)

除了自定义样式之外，您还可以选择仅向特定 URL 显示表单：

在****注册表单****中，导航至****定位和********行为****选项卡。在“**定位**”下，选中“**URL**”选项，然后输入您要定位的具体网址。 ![mceclip0.png](https://klaviyo.zendesk.com/hc/article_attachments/28711673372955)

您可能还需要考虑在注册表单中包含隐藏字段（https://klaviyo.zendesk.com/hc/en-us/articles/360040841811），以传递自定义语言属性。这将确保每个订阅者都与一个隐藏的语言属性相关联，您稍后可以使用该属性来细分您的客户。 ## Klaviyo 帐户支持多种语言

您可能有多个不同语言的 Magento 商店。您可以自定义电子邮件模板并根据客户的位置和/或语言偏好来定位客户。有关 Klaviyo 帐户中支持多种语言的更多信息，请访问 [Klaviyo 对多种语言的支持](https://klaviyo.zendesk.com/hc/en-us/articles/115005239028)