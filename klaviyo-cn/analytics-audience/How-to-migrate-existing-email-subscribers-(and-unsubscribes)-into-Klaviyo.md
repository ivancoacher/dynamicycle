---
id: "115005078487"
title: "如何将现有电子邮件订阅者（和取消订阅）迁移到 Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005078487-How-to-migrate-existing-email-subscribers-and-unsubscribes-into-Klaviyo"
section: "Build and use lists"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T11:06:51Z"
language: "zh"
---
## 你将会学到

了解如何使用 Klaviyo 的列表导入工具将前 ESP 的联系人添加到您的 Klaviyo 帐户，以及开始使用 Klaviyo 的其他最佳实践。 ## 加入之前

首先，我们建议您在帐户中[维护一个主电子邮件列表](https://klaviyo.zendesk.com/hc/en-us/articles/360043947571)，有时称为电子邮件列表。当您导入联系人并将注册表单连接到 Klaviyo 时，维护一个主要列表将使您可以轻松有效地管理和与联系人沟通。我们的[细分生成器](https://help.klaviyo.com/hc/en-us/articles/115005237908)允许您创建不需要维护的动态列表子集。例如，不要让不同的注册表单链接到多个列表，而是让所有表单都指向一个列表。然后，传递每个表单唯一的注册源属性 ([**$source**](https://help.klaviyo.com/hc/en-us/articles/115005074627-Guide-to-Properties#ask-customers-for-them5))。这样，您就可以维护一个订阅者列表并创建[基于此属性的分段](https://klaviyo.zendesk.com/hc/en-us/articles/360040841811)。 ## 同步来自其他电子邮件服务提供商 (ESP) 的联系人

如果您要从 Mailchimp、Campaign Monitor、Constant Contact 或 Salesforce Marketing Cloud（以前称为 ExactTarget）迁移，您将使用与 Klaviyo 的内置集成来导入现有订阅者列表以及取消订阅。为此，请安装相关集成：

1. 导航至****集成**** ****> E********xplore 应用程序****。 2. 单击右上角的****所有类别****。 3. 选择左侧的****电子邮件服务提供商****，然后选择您的提供商。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39460582424347)
4. 单击****安装****，然后按照步骤安装集成。 5. 安装集成后，您的列表将在几分钟内自动同步并显示在您帐户的**列表和细分**选项卡中。所有取消订阅的联系人也将同步并直接进入您帐户中的[抑制](https://klaviyo.zendesk.com/hc/en-us/articles/115005246108)列表。 - 对于 MailChimp、Campaign Monitor 和 Salesforce Marketing Cloud（以前称为 ExactTarget），我们会自动为取消订阅的用户创建排除列表。在 MailChimp 中，如果某人在任何列表中被抑制，那么他们将在 Klaviyo 中被全局抑制。在 Salesforce Marketing Cloud 中，如果配置文件处于非活动状态，则该配置文件将在 Klaviyo 中全局抑制。非活动状态包括“已退回”、“已保留”、“取消订阅”和“已删除”。 - 对于常量联系人，我们仅同步属于常量联系人列表 ID **不发邮件** 的黑名单。如果您当前没有使用我们集成的 ESP，您将需要采取更多手动方法（在[下一节](#section2)中概述）。 ## 从 CSV 文件导入联系人

如果您要从我们当前未集成的 ESP 迁移，或者您的订阅者列表已保存为 CSV 或 Excel 文件，您可以轻松地将订阅者导入到 Klaviyo。如果您将列表保存为 Excel 文件，请确保先将其保存为 CSV 文件。您的 CSV 的第一行应格式化为您要上传的列的标题。您必须有一个标有“电子邮件”或“电子邮件地址”的列。您可能想要包含的其他列包括“名字”和“姓氏”，以及您想要上传的任何其他[自定义属性](https://help.klaviyo.com/hc/en-us/articles/115005074627-Add-Custom-Properties-to-a-Contact-Profile)。从另一个 ESP 导入列表时，大多数平台都有将列表导出到 CSV 或 Excel 文件的链接。如果您遇到问题，我们建议您向当前的平台寻求帮助。导出列表后：

1. 导航至 Klaviyo 中的****列表和分段****选项卡。 2. 选择一个列表（例如，**新闻通讯**或**电子邮件列表**）。 3. 单击****管理列表> 导入联系人****。 ![Klaviyo的列表导入工具](https://klaviyo.zendesk.com/hc/article_attachments/28716301211547)
4. 单击****上传****并选择订阅者的 CSV 文件。 5. 将 CSV 中的每一列映射到 Klaviyo 中的相应属性，然后单击****下一步****。 6. 如果您的 CSV 文件中的每个人都明确同意接收您发送的营销电子邮件，请选择选项**是，将所有导入的联系人的订阅状态更新为已订阅**。 如果您的 CSV 文件同时包含电子邮件和电话号码，请选择他们订阅的频道。 7. 单击****导入****。 ## 使用 Klaviyo API

Profiles API 用于在 Klaviyo 中创建和管理列表。如果您精通技术或团队中有开发人员，则可以使用 [Klaviyo 的批量订阅 API 端点](https://developers.klaviyo.com/en/reference/bulk_subscribe_profiles)。 ## 将历史取消订阅加载到 Klaviyo

如果您没有通过我们的内置 ESP 集成之一同步订阅者，请手动将您的退回邮件和退订历史列表导入到 Klaviyo。此步骤很重要，原因如下：

- 确保您遵守垃圾邮件法
- 从一开始就发送到干净的列表，以保持[电子邮件的送达率](https://klaviyo.zendesk.com/hc/en-us/articles/115005247008)
- 为了让您的订阅者满意并确保您不会向任何选择退出的人发送电子邮件

要将您的历史取消订阅导入到 Klaviyo：

1. 准备一个包含退回邮件和退订邮件的 CSV 文件，其中一列每行包含一封电子邮件。 2. 导航至 Klaviyo 中的****受众 > 个人资料****。 3. 单击右上角的****查看抑制的配置文件****。 4. 选择****上传文件****并上传您的退订文件。 ![Upload_suppression_list.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716328580635)

## 其他资源

- [了解每个营销渠道都有一个主列表的好处](https://klaviyo.zendesk.com/hc/en-us/articles/360043947571)
- [配置文件和事件属性可接受的日期和时间戳格式](https://klaviyo.zendesk.com/hc/en-us/articles/115005253428)
- [分段入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005237908)
- [如何创建客户参与度](https://klaviyo.zendesk.com/hc/en-us/articles/360000407272)