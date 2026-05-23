---
id: "360034455472"
title: "从 Drip 迁移到 Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360034455472-Migrate-from-Drip-to-Klaviyo"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:51Z"
language: "zh"
---
## 概述

本指南将引导您完成将数据从 Drip 迁移到 Klaviyo。虽然 Klaviyo 没有与 Drip 内置集成，但您可以从 Drip 导出数据并将其上传到 Klaviyo。通过创建和导出多个 Drip 人员细分来迁移您的 Drip 配置文件。首先，您将创建订阅电子邮件营销的人员的水滴细分。然后，您将导出这些配置文件以上传到您的 Klaviyo Newsletter（选择加入）列表中。您还可以为已取消订阅电子邮件营销的人员创建一个 Drip 细分受众群，并将这些个人资料添加到您的 Klaviyo 隐藏个人资料列表中。除了迁移您的 Drip 配置文件之外，您还需要将您的 Drip 电子邮件模板移至 Klaviyo。当您的所有信息迁移到 Klaviyo 后，您就可以开始注销您的 Drip 帐户。本指南将引导您完成将数据从 Drip 迁移到 Klaviyo。当您迁移 Drip 列表时，请记住，迁移数据的主要目标是确保所有相关联系人和字段都在 Klaviyo 中显示，并且任何选择退出的联系人都会在 Klaviyo 中得到同样的处理。下面我们提供了一种推荐的方法，允许您将 Drip 联系人上传到 Klaviyo，并根据 Drip 中的联系人状态将各种联系人视为取消订阅。我们建议您还查看[Drip 如何定义这些状态](https://www.drip.com/learn/docs/manual/people)，以便您可以验证 Bronto 中的数据质量，并确保这种上传活跃、退订、退回和禁止的方法符合您对 Klaviyo 的预期用途。本指南为您提供将数据从 Drip 迁移到 Klaviyo 的一般准则。请联系 [Drip 支持](https://www.drip.com/contact)，获取有关导出 Drip 数据的最新说明。 ## 清单

使用此清单作为将 Drip 数据迁移到 Klaviyo 的指南：

1. 创建订阅电子邮件营销的活跃用户的水滴细分。将此列表导出为 CSV 并适当设置格式。 2. 将此 CSV 上传到 Klaviyo 中的列表。 3. 创建已取消订阅的活跃用户的滴灌细分。将此列表导出为 CSV 并适当设置格式。 4. 将此取消订阅的 CSV 上传到您的 Klaviyo 禁止列表。 5. 将您的电子邮件模板从 Drip 迁移到 Klaviyo。 6. 注销您的 Drip 帐户。 ## 导出您的 Drip Active 电子邮件订阅者名单

由于 Drip 的活跃人群分组并不与参与的 Klaviyo 个人资料直接关联，因此您需要创建订阅了电子邮件营销的活跃人群的 Drip 细分。将该片段导出为 CSV，以便您可以将其格式化以上传到 Klavyio 列表。在您的 Drip 帐户中，导航至 ****People**** 部分，然后单击 ****Active**** 选项卡。 ![Drip1.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630861211)

点击下拉菜单并选择****订阅电子邮件营销的人员****。这将创建一个由所有选择加入并能够接收电子邮件通信的活跃人员组成的部分。 ![Drip_Segment1.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630892955)

单击****操作****并选择****导出为 CSV****。然后，单击****确定****。 Drip 会将 CSV 文件通过电子邮件发送到您的 ****Drip 帐户**** ****常规信息****下列出的地址。这些分段字段将自动包含在您的 Drip CSV 导出文件中：

- 代币
- 电子邮件地址
- 时区
- 状态
- 创建日期
- 确认日期
- 标签
- 自定义字段
- 活动
- 推荐人
- 登陆网址
- IP地址
- 领先分数
- 终生价值
- 用户ID

您还可以在 [Drip 帮助中心](https://www.drip.com/learn/docs/manual/people/active) 上查看有关导出活动列表的说明。 ## 设置 CSV 格式以供导入

您需要格式化导入到 Klaviyo 的每个 CSV。为此，请打开 CSV 文件并梳理列表，特别注意列标题：

- 列标题应位于 CSV 文件的第一行。如果 Drip 在列标题之前添加了额外的行，请删除这些额外的行。 - 您的 CSV 必须包含“电子邮件”或“电子邮件地址”列。 - 您可能需要包含“名字”和“姓氏”列。 - 包括您想要上传到 Klaviyo 的任何自定义个人资料属性，例如“性别”。 - 时间戳字段（例如“添加日期”、“上次打开”和“上次单击”）需要进行专门格式化，否则 Klaviyo 不会将它们识别为时间戳字段。 确保时间戳数据采用以下格式之一：

  `YYYY-MM-DD HH:MM:SS`

  `月/日/年 时:分:秒`

  `月/日/年时:分:SS`

  `月/日/年 时:分`

  `月/日/年时:SS`

  `YYYY-MM-DDTHH:MM:SS`

以下是如何设置 CSV 文件格式的示例。 ![Drip_CSV_Formatted.png](https://klaviyo.zendesk.com/hc/article_attachments/28723625578907)

仔细检查您的 CSV，根据需要编辑和删除列标题和联系人条目。有关格式化 CSV 文件的更多详细说明，请参阅我们关于[创建联系人并将其添加到新列表](https://klaviyo.zendesk.com/hc/en-us/articles/115005078967) 的文章。 ## 将您的 CSV 导入 Klaviyo

格式化 CSV 后，您可以将其作为列表导入到 Klaviyo 中。某些 Klaviyo 流程是通过将电子邮件地址添加到列表中来触发的，例如欢迎系列。在开始将联系人上传到列表之前，请确保这些相关流程已切换为草稿或手动模式。在 Klaviyo 中，导航至****列表和细分****选项卡。选择您想要添加联系人的列表。为简单起见，我们建议将订阅者添加到您的新闻通讯列表，但您可以将您选择加入的电子邮件地址添加到任何列表。 ![Bronto12.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723659154331)

在列表的右上角，从 **管理列表** 下拉列表中选择 **导入联系人****。 ![Import_Contacts_blurred.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723630868763)

拖放您的 CSV。在 Klaviyo 开始导入之前，系统将提示您检查字段映射。仔细检查与 Klaviyo 字段相对应的每个导入字段，并进行适当的修改。默认情况下，所有已识别的字段都包含在导入中。您可以通过取消选中字段名称右侧的框来忽略导入字段。 ![Omit_Import_Field.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723630875163)

未自动与 Klaviyo 字段匹配的导入字段被标记为“**未映射**”。如果您尝试导入未映射的字段，Klaviyo 会给您一条错误消息并提示您映射该字段。在每个 **未映射** 字段的下拉列表中，选择现有的 Klaviyo 字段名称或通过在空白输入字段中键入名称来创建自定义字段。在字段名称右侧，从以下选项中选择数据类型：**字符串**、**布尔**、**数字**、**日期**或**列表**。如果您不确定正确的数据类型，请参阅我们关于[可在导入中使用的数据类型](https://klaviyo.zendesk.com/hc/en-us/articles/115005237648) 的文章。 ****![Map_Custom_Property.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723630865179)****以下是 Drip 联系人导入的字段映射示例。 ![Drip_Field_Mapping_2.png](https://klaviyo.zendesk.com/hc/article_attachments/28723625582875)
 完成后，单击屏幕右上角的****开始导入****。！[Start_CSV_Import.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630883995)

要更深入地了解导入联系人，请参阅我们关于[将现有订阅者迁移到 Klaviyo 并取消订阅](https://klaviyo.zendesk.com/hc/en-us/articles/115002053752) 的文章。 ## 导出滴滴退订列表

将取消订阅通过 Drip 发送的电子邮件的收件人添加到您的 Klaviyo 抑制列表非常重要，以确保遵守垃圾邮件法并保持较高的送达率。由于 Drip 的不活跃人群分组与受抑制的 Klaviyo 个人资料没有直接关联，因此我们建议为已取消订阅电子邮件营销的活跃人群创建 Drip 细分。您还可以导出 Drip 不活跃人员并将其添加到您的 Klaviyo 抑制列表中。从您的 Drip 帐户中，导航至 ****People**** 部分，然后单击 ****Active**** 选项卡。 ![Drip1.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630861211)

点击下拉菜单并选择****取消订阅电子邮件营销的人员****。这将创建一个由所有选择退出电子邮件营销的活跃用户组成的细分市场。 ![Drip_Segment1.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630892955)

单击****操作****并选择****导出为 CSV****。然后，单击****确定****。 Drip 会将 CSV 文件通过电子邮件发送到您的 ****Drip 帐户**** ****常规信息****下列出的地址。 ## 将 CSV 文件格式化为禁止列表

设置包含取消订阅的 CSV 文件的格式，使其包含单列电子邮件地址**。** 为清楚起见，标记该列 **电子邮件**。以下示例说明了禁止列表 CSV 文件的格式。 ![Suppress_list_format.png](https://klaviyo.zendesk.com/hc/article_attachments/28723659146523)

作为可选步骤，您还可以导出 Drip Inactives 并格式化该列表，以便上传到 Klaviyo 中的抑制列表中。为此，请导航至 ****Drip > People > Inactives****。单击****操作 > 导出到 CSV****。请访问 Drip 帮助中心，了解有关[导出 Drip Inactives](https://www.drip.com/learn/docs/manual/people/inactive) 的更多信息。 ## 将取消订阅加载到 Klaviyo

导航至 Klaviyo 帐户中的****个人资料****选项卡，然后单击右上角的****禁止的个人资料****。然后，选择****上传文件****。 ![Import_CSV_to_Suppressed_blurred.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723625557275)

单击****选择文件**** 选择包含滴水抑制的 CSV 文件。然后，单击****上传抑制****。 ![Bronto21.png](https://klaviyo.zendesk.com/hc/article_attachments/28723630906139)

您的 Klaviyo 禁止名单现在将反映您的进口情况。 ## 将电子邮件模板从 Drip 迁移到 Klaviyo

Klaviyo 提供了直观的拖放模板生成器，您可以使用它来重新创建 Drip 电子邮件模板。我们强烈建议使用此方法来重建您的模板，因为它将确保它们针对移动设备进行了优化、响应迅速且易于编辑。查看[我们的 Klaviyo 模板编辑器使用指南](https://help.klaviyo.com/hc/en-us/articles/115005082447-The-Email-Template-Editor)。如果您没有时间重新创建 Drip 模板，可以从 Drip 导出原始 HTML 格式的电子邮件模板，然后将更新后的原始 HTML 上传到 Klaviyo。但是，我们强烈建议您在模板编辑器中重建模板，这样您以后就不必更新电子邮件的原始 HTML。如果您选择导入原始 HTML 模板，可以参考我们关于[导入自定义 HTML 模板]的文章(https://klaviyo.zendesk.com/hc/en-us/articles/115005254068)。 ## 关闭您的滴灌帐户

将所有数据移至 Klaviyo 后，您可以采取三个关键步骤来确保您不再需要 Drip 帐户：

1. 确保您的注册表单和列表增长工具指向 Klaviyo，而不是 Drip。 2. 将您的 Drip 工作流程重新创建为 Klaviyo 流程。 3. 停止使用滴注剂。 ### 注册表单和列表增长工具

在 Klaviyo 中重新创建任何 Drip 注册表单，以便您的列表继续在 Klaviyo（而不是在 Drip 中）增长。您可以：

1. 使用 Klaviyo [注册表单生成器](https://help.klaviyo.com/hc/en-us/articles/360002050572-The-Signup-Form-Builder) 从头开始重新创建表单。 2.使用与Klaviyo集成的第三方列表增长工具。 3. 通过您的电子商务平台集成您的自定义表单。如果您使用第三方列表增长工具，请确保这些工具同步到 Klaviyo。 Klaviyo 集成了许多[用于列表增长和登陆页面的工具](https://help.klaviyo.com/hc/en-us/sections/115001509868-Tools-for-List-Growth-Landing-Pages)。 [扫描我们的集成列表](https://help.klaviyo.com/hc/en-us/categories/115000874028-App-Integrations) 以查找您正在使用的工具。如果您没有看到它列出，请考虑使用 Klaviyo 的注册表单生成器来创建表单，或尝试切换到其他第三方工具。请注意，默认情况下，所有 Klaviyo 列表都是[双重选择加入](https://help.klaviyo.com/hc/en-us/articles/115005251108-The-Double-Opt-In-Process)。如果您想将列表更改为单一选择加入并且您使用的是付费计划，请[联系支持人员](https://help.klaviyo.com/hc/en-us/requests/new)。如果您使用自定义编码表单，有两种方法可以确保这些联系人同步到 Klaviyo。一种选择是确保您的自定义表单将新订阅者直接同步到您的电子商务平台，并且您的电子商务商店与您的 Klaviyo 帐户集成。第二个选项是通过更新表单操作 URL 将表单直接指向您的 Klaviyo 帐户。要在您的 Klaviyo 帐户中查找表单操作 URL，请转到您的****列表和细分**** 选项卡，然后单击要添加新订阅者的列表。 单击****订阅页面****选项卡并复制右上角的 URL。 ![Updating_Form_Action_URL.gif](https://klaviyo.zendesk.com/hc/article_attachments/28723630915355)

将所有注册表单切换到 Klaviyo 后，等待几天并在 Drip 中查看您的列表。如果您注意到订阅者仍在添加到这些列表中，则可能至少有一种表单仍需要更换。接下来，您需要关闭 Drip 注册表单。 [联系 Drip 支持](https://www.Drip.com/contact)，了解有关如何关闭 Drip 注册表单的信息。 ### 流量

流程是自动通信，由客户操作触发，允许您向每个收件人个性化您的消息。在 Klaviyo 中重新创建这些内容非常重要，这样您就不需要继续使用 Drip 发送触发电子邮件。当您离开 Drip 时，可能是刷新和更新自动消息传递的好时机。我们建议您打开[欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172-Create-a-Welcome-Series-Flow) 和[废弃cart](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow) 尽快流动。欢迎系列对于吸引新订阅者尤其重要，而废弃的购物车流比任何其他类型的流具有最高的投资回报率。一旦您的 Klaviyo 流程上线，您将需要关闭 Drip 中的所有工作流程，以确保您不会向他人重复发送电子邮件。 [联系 Drip 支持](https://www.Drip.com/contact)，了解有关关闭 Drip 工作流程的更多信息。 ### 停止使用滴注

一旦您将所有列表增长工具指向您的 Klaviyo 帐户、暂停您的 Drip 工作流程并启用您的 Klaviyo 流程，您就可以停止使用 Drip。在关闭 Drip 帐户之前，请仔细检查一切是否按预期运行。在您的注册表单和其他列表增长工具中输入测试电子邮件，放弃购物车，然后注册您的时事通讯以触发欢迎系列。转到您的 Klaviyo 帐户中的****个人资料****选项卡，确保个人资料中的信息反映了所有正确的通信。如果您注册的列表是双重选择加入的，请务必先确认您的电子邮件。完成这些步骤并完全迁移到 Klaviyo 后，您可以关闭您的 Drip 帐户。 ## Klaviyo 的后续步骤

一旦您的 Klaviyo 帐户与您的商店集成，并且您的所有数据都从 Drip 迁移过来，您就可以按照我们的[首次发送指南](https://klaviyo.zendesk.com/hc/en-us/articles/360027226471) 进行第一次 Klaviyo 发送。如果您对从 Drip 过渡或开始使用 Klaviyo 有疑问，请[联系我们的支持团队](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272)。