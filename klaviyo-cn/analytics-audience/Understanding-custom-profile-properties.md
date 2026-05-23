---
id: "115000250912"
title: "了解自定义配置文件属性"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115000250912-Understanding-custom-profile-properties"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:11Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 中的自定义属性，您可以使用它来存储帐户中联系人的信息。以下是如何使用自定义属性的几个示例：

- 收集有关您的联系人的其他信息，例如性别、体型、优惠券代码等。 - 收集联系人的偏好，例如电子邮件频率、内容类型等。 - 收集联系人对调查问卷的回复

您几乎可以使用自定义属性收集您想要的有关联系人的任何类型的信息，然后使用此信息来定制内容、创建细分或过滤流。可添加到一个配置文件中的自定义属性的数量没有限制。 ## 如何向配置文件添加自定义属性

您可以通过两种主要方式将自定义属性添加到联系人的个人资料中：

1. 自行添加此信息（例如，手动添加或[上传 CSV](https://klaviyo.zendesk.com/hc/en-us/articles/1260806293150)）
2. 要求联系人提供此信息

### 自己添加自定义属性

上传列表时，“电子邮件”列之后的任何列都可用于将自定义属性附加到配置文件。例如，您可以有一个与联系人性别相对应的“性别”列。 ![上传过程中添加头发颜色自定义属性](https://klaviyo.zendesk.com/hc/article_attachments/28720891154075)

如果任何 Klaviyo 配置文件中尚不存在该属性，您需要在上传过程中创建一个新属性。为此，请在新属性行的 **Klaviyo Field** 列中键入您要使用的属性名称，然后选择 **创建选项****。请勿在“**导入审核**”步骤中点击“****订阅电子邮件营销****”，以便上传中的所有个人资料将在 Klaviyo 中保留其现有订阅状态。 ![在 Klaviyo 中的配置文件上创建配置文件属性选项](https://klaviyo.zendesk.com/hc/article_attachments/28720846056603)

您还可以将自定义属性直接添加到联系人的个人资料中。首先，导航到您想要添加自定义属性的配置文件。在这里，您将看到一个标记为“自定义属性”的区域，其中包含“添加自定义属性”选项。单击此按钮并添加您想要的自定义属性。 ![添加自定义配置文件属性按钮](https://klaviyo.zendesk.com/hc/article_attachments/28720846060059)

### 收集自定义配置文件属性数据

当订阅者使用订阅页面、注册表单或[第三方列表增长集成](https://connect.klaviyo.com/integrations) 进行注册时，您可以直接从订阅者那里收集自定义属性。您还可以使用管理首选项页面从现有订阅者收集自定义属性。 - [通过注册表单收集自定义属性](https://help.klaviyo.com/hc/en-us/articles/4413550187035)
- [通过订阅或管理首选项页面收集自定义属性](https://help.klaviyo.com/hc/en-us/articles/115005251848-Edit-Opt-in-Related-Pages-for-a-List)

您添加到订阅页面或注册表单的任何其他字段都将作为自定义属性收集。如果您想根据收到的响应来过滤细分或流，您甚至可以将这些方法用作调查问卷。 ## 注册表单中的个人资料属性

如果您使用注册表单收集配置文件属性信息，并且任何 Klaviyo 配置文件中尚不存在自定义属性，则您可能必须为配置文件属性名称和值创建选项。首先，输入您的属性的标签标题和值标题。添加值后，它们将显示为选项。每个属性标签应该是唯一的。有关更广泛的说明，请参阅[注册表单中的属性](https://help.klaviyo.com/hc/en-us/articles/115005074627#h_01HA32RZBB2RB125E2K2RH7A55)。所有自定义字段都可以在发布表单之前或之后进行编辑。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39652942794651)

不同的表单字段创建具有[不同数据类型]的属性(https://help.klaviyo.com/hc/en-us/articles/115005237648)。例如，布尔数据类型只能表示两个值：true 或 false。布尔数据的一个示例是当某人接受您的营销时存储的属性。要同时查看表单中提交的所有内容，请[将配置文件导出为 CSV](https://help.klaviyo.com/hc/en-us/articles/115005078687-How-to-Export-a-List-or-Segment-to-a-CSV-File) 以及表单中的属性。 请注意，只能存储和导出连接到配置文件的表单提交。在单个表单中多次收集相同的配置文件属性将设置与最后一个收集步骤关联的属性值。此外，如果有人多次填写同一张表格，则只会保存最近提交的内容。如果您需要单独跟踪和存储每个表单提交，我们建议使用 [Typeform](https://help.klaviyo.com/hc/en-us/articles/115000107112) 等调查工具。 ## 如何使用自定义属性

您可以使用自定义属性来细分受众、过滤流量以及在电子邮件中包含动态内容。创建自定义属性并且该属性至少出现在 1 个个人资料中后，当您选择 **有关某人的属性** 时，它将填充在分段构建器中。同样，当您[向流添加过滤器](https://help.klaviyo.com/hc/en-us/articles/115002779051-Flow-Triggers-and-Filters)时，也会发生这种情况。 ![基于名为“头发颜色”的自定义属性的分段](https://klaviyo.zendesk.com/hc/article_attachments/28720891157659)

您还可以使用“查找”过滤器使用自定义属性动态填充您的电子邮件：

|  |  |
| --- | --- |
|您的头发颜色是：{{ person|lookup:'头发颜色' }} |您的头发颜色是： 金发 |

## 其他资源

- [配置文件和属性术语表](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary)
- [配置文件属性参考](https://help.klaviyo.com/hc/en-us/articles/115005074627-Guide-to-Properties)