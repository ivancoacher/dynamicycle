---
id: "360030919351"
title: "如何将数据从 Klaviyo 同步到 Shopify"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360030919351-How-to-sync-data-from-Klaviyo-to-Shopify"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "zh"
---
## 你将会学到

了解如何将客户信息（例如个人资料信息、自定义属性、电子邮件和短信订阅状态以及事件）从 Klaviyo 同步到 Shopify。您可以从 Klaviyo 中的 Shopify 集成设置页面进行这些更改。您可以选择是同步所有现有和新的 Klaviyo 配置文件的更新，还是仅同步 Shopify 已知配置文件的更新。 ## 开始之前

- 如果您还没有阅读我们关于[Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) 的文章，了解有关集成的分步说明，然后再继续阅读本文。 - 在 Klaviyo 中删除个人资料不会导致它在 Shopify 中被删除，反之亦然。 ## 可同步数据

您可以通过集成设置页面自定义要同步的数据。配置这些设置后，以下字段仅在之前对于 Shopify 中的现有客户为空时才会同步：

- 名字
- 姓氏
- 电子邮件
- 电话号码

Klaviyo 中将更新 Shopify 中现有字段的字段包括：

- 电子邮件订阅状态
- 短信订阅状态

将在 Shopify 中创建的新字段包括：

- 自定义配置文件属性。 - 您可以选择同步 Klaviyo 中存在的任何自定义配置文件属性，包括从其他平台引入的属性。这些属性将在 Shopify 中创建为元字段定义，并且它们的值将在 Shopify 中的相应客户上更新。 - Shopify 中每个对象的元字段定义数量限制为 250 个，因此您只能同步不超过该限制的自定义属性。 - 如果您尝试使用与最初在 Shopify 中创建元字段定义不同的数据类型（例如，字符串而不是数组）将自定义属性从 Klaviyo 同步回 Shopify，则元字段将不会在 Shopify 中更新。 - 收到的电子邮件（由 Klaviyo 个人资料接收，即由 Klaviyo 客户发送）、打开和单击事件。 - 收到的 SMS 消息（由 Klaviyo 配置文件接收，即由 Klaviyo 客户发送）和点击事件。请注意，Klaviyo 电子邮件接收、打开和点击事件以及 SMS 消息接收和点击事件在 Shopify 中无法单独查看，但[包含在营销归因报告中](https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/app-data-sharing)。我们建议同步所有配置文件和所有可能的字段，以便在平台之间实现更好的数据一致性。 Klaviyo 数据可用于在 Shopify 内创造更多价值，包括通过增强的归因报告和业务自动化。 ## 将字段从 Klaviyo 同步到 Shopify

1. 在 Klaviyo 中，前往 [Shopify 集成设置页面](https://www.klaviyo.com/integration/shopify)。 2. 滚动到 **同步设置** 部分，然后单击 **至 Shopify** 选项卡。 3. 检查设置：****同步配置文件、配置文件数据和自定义属性**** ****从 Klaviyo 到 Shopify****。 4. 选择是同步所有 Klaviyo 配置文件的更新还是仅同步 Shopify 中已存在的配置文件的更新。如果您选择所有配置文件，Klaviyo 将在 Shopify 中为 Klaviyo 中创建的所有配置文件（现有的和新的）创建新客户。这包括从其他 Klaviyo 集成同步的配置文件，或通过列表导入添加的配置文件，即使它们尚未与您的 Shopify 商店交互。 5. 接下来，您可以选择将哪些更新同步到 Shopify：
   - ****姓名、电子邮件地址和电话号码****如果您选择此选项（并且选择同步所有配置文件），则在集成（或更新集成）后将回填所有范围内的配置文件，以确保 Klaviyo 和 Shopify 同步。今后，将使用在 Klaviyo 中创建的数据在 Shopify 中创建新的配置文件（如果 Shopify 中尚不存在）。 - ****电子邮件订阅状态****
     选择此设置不会提示回填电子邮件订阅状态。展望未来，Klaviyo 中的电子邮件同意状态更新（即订阅和取消订阅）将触发 Shopify 中的更新。请注意，Klaviyo 中的抑制状态不会同步到 Shopify，也不会影响 Shopify 中的同意状态。 - ****短信订阅状态（如果您启用了短信）****
     如果您选择此选项（并且选择同步所有配置文件），则在集成（或更新集成）后将回填所有 SMS 订阅状态和关联的电话号码，以确保 Klaviyo 和 Shopify 同步。展望未来，Klaviyo 中的 SMS 同意状态更新将触发 Shopify 中的更新。 - ****电子邮件收到、打开和单击事件****
     选择此选项不会提示回填此数据。 - ****收到短信并单击事件（如果您启用了短信）****选择此选项将不会提示回填此数据。 - ****自定义属性****单击 ****选择属性**** 选择要同步到 Klaviyo 的属性。然后，您可以搜索属性并单击加号来添加它们，或者单击****添加全部****来添加所有属性。选择完属性后，单击****保存****。您可以随时编辑、添加或删除这些属性。选择自定义属性将提示回填这些属性。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717381154843)
6. 单击****保存****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717387436699)

更新设置后，Klaviyo 将开始将任何必要的回填同步到 Shopify。 ## 同步频率

****姓名、电子邮件地址、电话号码、订阅状态和自定义属性****：当对您的指定配置文件进行新更改时（在任何初始回填后），这些更改将在 Klaviyo 中进行更改后 30 分钟内反映在 Shopify 中，但大多数更改应在一分钟内反映。 ****电子邮件接收、打开和点击事件，以及短信接收和点击事件****：这些更改会在 24 小时内同步到 Shopify。 ## 结果

Shopify 配置文件现在将根据您选择的设置使用 Klaviyo 数据进行更新。 ## 其他资源

- [Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407)
- [如何将 Shopify 电子邮件订阅者同步到 Klaviyo 列表](https://help.klaviyo.com/hc/en-us/articles/115005080667)
- [如何在 Shopify 结帐时收集短信同意](https://help.klaviyo.com/hc/en-us/articles/360056824732)