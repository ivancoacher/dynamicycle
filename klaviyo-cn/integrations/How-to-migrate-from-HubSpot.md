---
id: "360039708512"
title: "如何从 HubSpot 迁移"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360039708512-How-to-migrate-from-HubSpot"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T10:57:13Z"
language: "zh"
---
## 你将会学到

了解如何从 Hubspot 迁移到 Klaviyo。虽然 Klaviyo 没有与 HubSpot 内置集成，但您可以从 HubSpot 导出数据并将其上传到 Klaviyo。 ## 开始之前

本指南将引导您完成将数据从 HubSpot 迁移到 Klaviyo 的过程。当您迁移 HubSpot 列表时，请记住，迁移数据的主要目标是确保所有相关联系人和字段都在 Klaviyo 中显示，并且任何选择退出的联系人都会在 Klaviyo 中得到同样的处理。下面，我们提供了一种推荐的方法，允许您将 HubSpot 联系人上传到 Klaviyo，并根据 HubSpot 中的联系人状态将各种联系人视为取消订阅。我们建议您还查看 [HubSpot 如何定义这些状态](https://knowledge.hubspot.com/email/what-is-the-marketing-email-confirmation-status-contact-property)，以便您可以验证 HubSpot 中的数据质量，并确保这种上传活动和取消订阅配置文件的方法符合您对 Klaviyo 的预期用途。本文为您提供将数据从 HubSpot 迁移到 Klaviyo 的一般指南。请联系 [HubSpot 支持](https://help.hubspot.com/)，获取有关导出 HubSpot 数据的最新说明。 ## 迁移策略

在将数据从 HubSpot 迁移到 Klaviyo 之前，我们建议创建多个 HubSpot 列表：

- 每个人 - 活跃
- 所有退订
- 7 天 - 订婚
- 14 天 - 订婚
- 30 天 - 订婚
- 60 天 - 订婚

每个列表在 Klaviyo 中都会受到不同的对待

- 每个人 - 活跃：将此列表添加到您的电子邮件列表或选择列表中
- 所有取消订阅：将此列表添加到您的 Klaviyo 抑制列表中
- 7 天、14 天、30 天、60 天：这些列表将保留供以后使用，当您开始使用这些列表发送战略营销活动来预热您的帐户时

## 清单

从 HubSpot 迁移到 Klaviyo 需要几个关键步骤：

1. 将活跃的 HubSpot 联系人导出到 CSV 文件
2. 格式化 CSV 文件
3. 将 CSV 文件导入到 Klaviyo 列表
4.导出HubSpot退订
5. 将取消订阅上传到您的 Klaviyo 抑制列表
6.导出7天、14天、30天和60天的参与列表
7. 将您的 HubSpot 电子邮件模板迁移到 Klaviyo
8. 注销您的 HubSpot 帐户
9. 发送您的第一个 Klaviyo 活动

## 导出您的 HubSpot 列表

每个 HubSpot 帐户都是唯一设置的。以下说明是导出 HubSpot 列表的指南。 [联系 HubSpot 支持](https://blog.hubspot.com/customers/hubspot-support-channel-contact) 并查阅他们的[文档](https://help.hubspot.com/) 以获取最新的导出说明。这些说明适用于免费和付费帐户。 1. 在您的 HubSpot 帐户中，导航至****联系人 > 所有联系人****。 ![Hubspot 中“所有联系人”选项卡上的“联系人”页面](https://klaviyo.zendesk.com/hc/article_attachments/28720847629083)
2. 在****选项****下拉列表中，选择****导出视图****。 ![Hubspot 中“所有联系人”选项卡上的“联系人”页面，表格操作菜单已打开](https://klaviyo.zendesk.com/hc/article_attachments/28720847624475)
3. 选择****CSV**** 作为文件格式，然后选择****记录上的所有属性****。 4. 由于 HubSpot 还可以用作 CRM，因此您可能希望导出所有关联的联系人数据。导出所有属性也是导出联系人的最快方法。稍后您将能够在此过程中映射导出属性，并稍后在 Klaviyo 中引用这些字段进行分段。 5. 单击****导出****。该文件将发送到您登录时使用的电子邮件地址。 ![Hubspot 中的导出视图，带有橙色背景的导出](https://klaviyo.zendesk.com/hc/article_attachments/28720892777499)

## 格式化 CSV 文件

联系人以 CSV 格式导入到 Klaviyo。在将每个 CSV 文件导入 Klaviyo 之前，请仔细格式化每个 CSV 文件，以确保顺利、准确地导入您的联系人。打开每个 CSV 文件。仔细梳理每个列表，特别注意列标题：

- 列标题应位于 CSV 文件的第一行。如果 HubSpot 在列标题之前添加了额外的行，请删除这些额外的行。 - 您的 CSV 文件必须包含“电子邮件”或“电子邮件地址”标题作为第一列。 - 您可能需要包含“名字”和“姓氏”列。 - 包括您想要上传到 Klaviyo 的任何自定义个人资料属性，例如“性别”。 - 时间戳字段（例如“添加日期”、“上次打开”和“上次单击”）需要正确格式化，否则 Klaviyo 不会将它们识别为时间戳字段。确保时间戳数据采用以下格式之一：
  年-月-日 时:分:秒
  月/日/年 时:分:秒
  月/日/年 时:分:秒
  月/日/年 时:分
  月/日/年 时:分
  YYYY-MM-DDTHH:MM:SS

这是 CSV 文件格式的示例：

![包含名字和姓氏等字段的示例 CSV 文件](https://klaviyo.zendesk.com/hc/article_attachments/28720892779931)

仔细检查您的 CSV 文件，根据需要编辑/删除列标题和联系人条目。请记住，在将 CSV 文件上传到 Klaviyo 之前，解析和编辑 CSV 文件中的数据要容易得多。有关格式化 CSV 文件的更多详细说明，请参阅我们关于[创建联系人并将其添加到新列表](https://help.klaviyo.com/hc/en-us/articles/115005078967) 的文章。 ## 将 CSV 文件导入 Klaviyo 列表

设置导出数据的格式后，将其导入到 Klaviyo 中的列表中。某些 Klaviyo 流是由添加到列表中的电子邮件地址触发的。在开始将联系人上传到列表之前，请确保这些相关流程已切换为草稿或手动模式。 1. 登录您的 Klaviyo 帐户，单击****受众****下拉列表，然后选择****列表和细分****。 2. 选择您要添加联系人的列表。在此示例中，我们将把订阅者添加到电子邮件列表，因为他们已经选择加入。 3. 在列表的右上角，从 **管理列表** 下拉列表中选择 **导入联系人****。 ![Klaviyo 时事通讯列表，管理列表下拉菜单打开](https://klaviyo.zendesk.com/hc/article_attachments/28720847643675)
4. 拖放 CSV 文件。在 Klaviyo 开始导入之前，系统将提示您检查字段映射。点击**电子邮件**行中的****订阅电子邮件营销****，表示此上传中的所有个人资料均已明确同意接收您发送的电子邮件营销。 5. 仔细检查每个导入字段/相应的 Klaviyo 字段，并进行适当修改。默认情况下，所有已识别的字段都包含在导入中。您可以通过取消选中字段名称右侧的框来忽略导入字段。 6. 未自动与 Klaviyo 字段匹配的导入字段被标记为“未映射”。如果您尝试导入未映射的字段，您将收到一条错误消息，提示您添加该字段。从下拉列表中选择现有的 Klaviyo 字段名称，或通过在空白输入字段中输入名称来创建自定义字段。在字段名称右侧，从以下选项中选择数据类型：**字符串、布尔值、数字、日期或列表**或**同意**。如果您不确定数据类型，请参阅 Klaviyo 中有关[数据类型](https://help.klaviyo.com/hc/en-us/articles/115005237648) 的文章。这是 HubSpot 联系人导入的字段映射的简单示例：
   ![导入已映射所有字段的审阅页面并在右上角开始导入](https://klaviyo.zendesk.com/hc/article_attachments/28720892785179)
7. 完成后，单击屏幕右上角的****开始导入****。要更深入地了解导入联系人，请参阅我们关于[将现有订阅者迁移到 Klaviyo 并取消订阅](https://help.klaviyo.com/hc/en-us/articles/115002053752) 的文章。 ## 导出 HubSpot 退订

将您的 HubSpot 取消订阅导入您的 Klaviyo 抑制列表非常重要，以确保遵守垃圾邮件法并保持强大的投递能力。 Klaviyo 中被抑制的联系人无法发送营销电子邮件；但是，如果您使用 Klaviyo 发送交易电子邮件，被抑制的联系人仍会收到这些电子邮件。 **取消订阅电子邮件**是 HubSpot 中的默认属性，因此您将导出此列表、格式化它，然后将其上传到您的 Klaviyo 抑制列表中。 1. 导航到****联系人 > 列表 > 创建列表****。 ![Hubspot 列表页面，右上角有创建列表](https://klaviyo.zendesk.com/hc/article_attachments/28720847648027)
2. 描述性地命名新列表。对于**过滤器类型**，选择****基于联系人****。在 **您要创建什么类型的列表？** 选择 ****活动列表****。 ![在 Hubspot 中创建一个列表页面，并选择基于联系人的列表](https://klaviyo.zendesk.com/hc/article_attachments/28720892795163)
3. 从左侧列表中，选择****联系人属性****并搜索**取消订阅**。选择****取消订阅所有电子邮件****。 ![在搜索中使用 Unsu 联系属性搜索栏](https://klaviyo.zendesk.com/hc/article_attachments/28720847655579)
4. 设置****取消订阅所有电子邮件>等于> True****，然后单击****应用过滤器****。 ![过滤器取消订阅所有电子邮件等于 true](https://klaviyo.zendesk.com/hc/article_attachments/28720847653531)
5. 保存列表。 6. 导航至****列表****并找到您的**取消订阅**列表。将鼠标悬停在列表选项上，然后选择****更多****下拉列表。选择****导出****。 ![在 Hubspot 列表页面中取消订阅列表，并打开更多下拉菜单](https://klaviyo.zendesk.com/hc/article_attachments/28720892812059)
7. 您只需将电子邮件地址上传到您的 Klaviyo Suppressions 列表。在搜索字段中，输入 **电子邮件**。选择****电子邮件****字段并单击****下一步****。按照向导以 CSV 格式导出您的取消订阅。 8. 设置 CSV 下载的格式，使其包含单列电子邮件地址。以下是禁止列表 CSV 文件格式的示例：
   ![带有示例电子邮件的 CSV](https://klaviyo.zendesk.com/hc/article_attachments/28720892807323)
9. 现在您已准备好将取消订阅上传到 Klaviyo。 ## 将取消订阅上传到 Klaviyo

1. 导航至 Klaviyo 帐户中的****个人资料****选项卡（****受众****下），然后单击右上角的****禁止的个人资料****。 2. 选择****上传文件****。单击****选择文件****并选择包含您的 HubSpot 取消订阅的 CSV。 3. 单击****上传抑制****。 4. 您的 Klaviyo 抑制列表现在将反映您的导入情况。 ## 导出 7 天、14 天、30 天和 60 天的参与列表

1. 在 Hubspot 中导航至****联系人 > 列表 > 创建列表****。 ![Hubspot 中的列表页面，右上角有创建列表](https://klaviyo.zendesk.com/hc/article_attachments/28720892804251)
2. 描述性地命名您的新列表（例如，7 天参与度）。对于 **过滤器类型**，选择 ****联系人属性****。在**您要创建什么类型的列表？**下选择****活动列表****。 3. 在下一页上，选择****上次营销电子邮件打开日期****。 ![在搜索中打开的联系人属性搜索栏](https://klaviyo.zendesk.com/hc/article_attachments/28720892814235)
4. 单击****在****之后。您需要计算您想要的日期。例如，如果今天是 2021 年 6 月 16 日，则 7 天前就是 2021 年 6 月 23 日。 ![过滤上次营销电子邮件打开日期是在 06/23/2021 之后](https://klaviyo.zendesk.com/hc/article_attachments/28720847682459)
5. 应用过滤器，然后保存您的列表。 6. 按照前面的说明导出列表。 7. 重复这些步骤以创建 14 天参与度、30 天参与度和 60 天参与度列表。稍后您将使用这些列表来发送战略营销活动。 ## 将电子邮件模板从 HubSpot 迁移到 Klaviyo

Klaviyo 具有直观的拖放模板生成器，您可以使用它来重新创建 HubSpot 电子邮件模板。我们强烈建议使用此方法来重建您的模板，因为它将确保它们针对移动设备进行了优化、响应迅速且易于编辑。查看[我们的 Klaviyo 模板编辑器使用指南](https://klaviyo.zendesk.com/hc/en-us/articles/4407911841435)。如果您没有时间使用 Klaviyo 的模板生成器重新创建 HubSpot 模板，可以从 HubSpot 以原始 HTML 格式导出电子邮件模板，然后将 HTML 上传到 Klaviyo。如果必须导入原始 HTML 模板，可以[导入自定义 HTML 模板](https://help.klaviyo.com/hc/en-us/articles/115005254068)

## 注销您的 HubSpot 帐户

将所有数据移至 Klaviyo 后，您可以采取三个关键步骤来确保您不再需要 HubSpot 帐户：

1. 检查您的注册表单和列表增长工具是否指向 Klaviyo，而不是 HubSpot
2. 按照 Klaviyo 流程重新创建 HubSpot 工作流程
3.停止使用HubSpot

### 注册表单和列表增长工具

在 Klaviyo 中重新创建任何 HubSpot 注册表单，以便您的列表在 Klaviyo 而不是 HubSpot 中继续增长。您可以：

1. 使用 Klaviyo [注册表单生成器](https://help.klaviyo.com/hc/en-us/articles/360026474752) 从头开始重新创建表单
2.使用与Klaviyo集成的第三方列表增长工具
3. 通过您的电子商务平台集成您的自定义表单

如果您使用第三方列表增长工具，请确保这些工具同步到 Klaviyo。 Klaviyo 与许多用于列表增长和登陆页面的工具集成。 请注意，默认情况下，所有 Klaviyo 列表都是双重选择加入的。要将列表更改为单一选择加入，请前往我们的[双重选择加入流程指南](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108)的该部分。如果您使用自定义编码表单，则应确保自定义表单将新订阅者直接同步到您的电子商务平台，并且您的电子商务商店已与您的 Klaviyo 帐户集成。将所有注册表单切换或同步到 Klaviyo 后，等待几天并在 HubSpot 中查看您的列表。如果您注意到订阅者仍在添加到这些列表中，则可能至少有一种表单仍需要更换。接下来，您需要关闭 HubSpot 注册表单。请联系 [HubSpot 支持](https://help.hubspot.com/)，了解有关如何关闭 HubSpot 注册表单的信息。 ### 电子邮件自动化

Klaviyo 将自动化工作流程称为“流程”，它允许更高级和更有针对性的序列。在 Klaviyo 中重新创建这些邮件非常重要，这样您就不需要继续使用 HubSpot 发送触发式电子邮件。当您离开 HubSpot 时，可能是刷新和更新自动消息传递的好时机。我们建议您尽快打开欢迎系列和废弃购物车流程。欢迎系列对于吸引新订阅者尤其重要，而废弃的购物车流比任何其他类型的流具有最高的投资回报率。一旦您的 Klaviyo 流程上线，您将需要关闭 HubSpot 中的所有工作流程，以确保您不会向他人重复发送电子邮件。 [联系 HubSpot 支持](https://help.hubspot.com/)，了解有关关闭 HubSpot 工作流程的更多信息。 ### 停止使用 HubSpot

一旦您将所有列表增长工具指向您的 Klaviyo 帐户、暂停您的 HubSpot 工作流程并启用您的 Klaviyo 流程，您就可以停止使用 HubSpot。在关闭 HubSpot 帐户之前，请仔细检查一切是否按预期运行。在您的注册表单和其他列表增长工具中输入测试电子邮件，放弃购物车，然后注册您的电子邮件列表以触发欢迎系列。转到您的 Klaviyo 帐户中的****个人资料****选项卡（在****受众****下），以确保个人资料中的信息反映了所有正确的通信。如果您注册的列表是双重选择加入的，请先确认您的电子邮件。完成这些步骤并完全迁移到 Klaviyo 后，您可以关闭您的 HubSpot 帐户。 ## 使用 Klaviyo 发送您的第一个营销活动

一旦您的 Klaviyo 帐户与您的商店集成，并且您的所有数据都从 HubSpot 移植过来，您就可以使用 Klaviyo 发送您的第一个营销活动。欲了解更多信息，请查看【Klaviyo入门课程】(https://academy.klaviyo.com/getting-started-with-klaviyo)。 ## Klaviyo 的后续步骤

### 通过 Klaviyo 建立良好的发件人声誉

在开始向最活跃的客户群发送信息后，您可以逐渐向更多的客户发送信息。这种渐进的发送过程可以提高您的发件人声誉，称为“温暖您的 IP 地址”。请参阅我们有关送达率的文章，了解有关[预热您的发送基础设施]的更多信息(https://help.klaviyo.com/hc/en-us/articles/360025945671)。 ### 使用高级细分来吸引您的客户

在第一个月左右吸引了最感兴趣的订阅者后，开始接触其他客户群。您可以创建其他细分，以确保您联系到客户群的各个角落。 - 复制您的 **参与（3 个月）** 细分并调整设置，将时间范围从 3 个月减少到 30 天
- 使用 HubSpot 历史数据（例如 7 天、14 天、30 天和 60 天的参与列表）来完善和构建您的细分

要更深入地细分和接近其他客户群，请阅读[创建客户参与层](https://help.klaviyo.com/hc/en-us/articles/360000407272)。如果您对从 HubSpot 转换或开始使用 Klaviyo 有疑问，请[联系我们的支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272)。 ## 结果

您现在已从 Hubspot 迁移到 Klaviyo，并了解了迁移电子邮件提供商的最佳实践。 ## 其他资源

- [如何解决列表导入问题](https://help.klaviyo.com/hc/en-us/articles/115005078807)
- [了解电子邮件送达率](https://help.klaviyo.com/hc/en-us/articles/115005247008)
- [配置文件属性参考](https://help.klaviyo.com/hc/en-us/articles/115005074627)