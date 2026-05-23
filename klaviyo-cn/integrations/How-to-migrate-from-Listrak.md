---
id: "360034550591"
title: "如何从 利斯特拉克 迁移"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360034550591-How-to-migrate-from-Listrak"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T10:57:41Z"
language: "zh"
---
## 你将会学到

了解如何从 Listrak 迁移到 Klaviyo。虽然 Klaviyo 没有与 Listrak 内置集成，但您可以从 Listrak 导出数据并将其上传到 Klaviyo。 Listrak 联系人和相关数据以 CSV 格式从 Listrak 导出。 CSV 文件可以轻松格式化，以确保成功导入到 Klaviyo 列表。虽然这不是一个复杂的过程，但导出每个单独的 Listrak 列表可能会有点乏味，具体取决于您的数据量。只要保持一致性和彻底性，您的迁移就会成功。 ## 开始之前

本指南将引导您完成将数据从 Listrak 迁移到 Klaviyo 的过程。当您迁移 Listrak 列表时，请记住，迁移数据的主要目标是确保所有相关联系人和字段都在 Klaviyo 中出现，并且任何选择退出的联系人都会在 Klaviyo 中得到同样的处理。下面我们提供了一种推荐方法，允许您将 Listrak 联系人上传到 Klaviyo，并根据 Listrak 中的联系人状态将各种联系人视为取消订阅。我们建议您还查看[Listrak 如何定义这些状态](https://help.listrak.com/en/articles/1505969-view-subscribed-or-unsubscribed-contacts)，以便您可以确保 Listrak 端的数据质量，并确保这种上传联系人的方法符合您对 Klaviyo 的预期用途。本指南为您提供将数据从 Listrak 迁移到 Klaviyo 的一般准则。请联系 [Listrak 支持](https://www.listrak.com/company/contact)，获取有关导出 Listrak 数据的最新说明。 ## 清单

从 Listrak 迁移到 Klaviyo 需要几个关键步骤：

1.导出Listrak订阅的联系人列表
2. 格式化 CSV 文件
3. 将 CSV 文件导入到 Klaviyo 中的列表
4. 出口Listrak抑制名单
5. 将取消订阅导入到您的 Klaviyo 黑名单
6. 将电子邮件模板从 Listrak 迁移到 Klaviyo
7. 注销您的 Listrak 帐户

## 导出您的 Listrak 订阅的联系人列表

每个 Listrak 帐户都是唯一设置的。以下说明是导出 Listrak 数据的指南。 [联系 Listrak 支持人员](https://www.listrak.com/company/contact) 并查阅他们的[文档](https://help.listrak.com/en/) 以获取最新的导出说明。按照以下步骤下载您的每个 Listrak 列表。 1. 从 Listrak **主菜单**，导航至****联系人****。 2. 单击 ****订阅的联系人 >**** ****导出列表向导****。 ![Listrak 中的联系人菜单，导出列表向导为白色](https://klaviyo.zendesk.com/hc/article_attachments/28716352835867)
3. 选择****纯文本.CSV**** 作为导出格式，然后单击****下一步****。 ![选择导出格式，选择纯文本.CSV](https://klaviyo.zendesk.com/hc/article_attachments/28716352838555)
4. 现在选择要包含在 CSV 导出中的任何分段字段和系统字段。每次导出都会自动包含****电子邮件****、****订阅日期****和****方法****。 5. 完成后，单击****下一步****。 ![选择要导出页面的字段，下一步，绿色背景](https://klaviyo.zendesk.com/hc/article_attachments/28716329841435)
6. 选择交付方式，然后单击****下一步****。如果您要导出大型列表（超过 500K），则最好选择****电子邮件****作为传送方式，因为将大量数据上传到浏览器可能需要一些时间。 - 如果您选择****Web**** 交付方式，请单击****完成****。您的结果将显示在您的浏览器中。如果您选择****电子邮件****传送方式，请通过选择收件人来设置电子邮件选项。显示的默认电子邮件是与您的 Listrak 帐户绑定的电子邮件地址。启用****附加到电子邮件****复选框以将文件下载为电子邮件附件。然后，单击****完成****。 - 当您的 CSV 文件可供下载时，您将收到电子邮件通知。您可以查看[有关从 Listrak 导出整个 Listrak 列表的说明](https://help.listrak.com/en/articles/1509286)。 ## 格式化 CSV 文件

在将每个 CSV 文件导入 Klaviyo 之前，您需要对其进行格式化。为此，请打开 CSV 文件并梳理列表，特别注意列标题：

- 列标题应位于 CSV 文件的第一行。如果 Listrak 在列标题之前添加了额外的行，请删除这些额外的行。 - 您的 CSV 文件必须包含“电子邮件”或“电子邮件地址”列。 - 您可能需要包含“名字”和“姓氏”列。 - 包括您想要上传到 Klaviyo 的任何自定义个人资料属性，例如“性别”。 - Listrak导出一个**Method**字段，表示订阅的方式。该字段可以在 CSV 上传文件中保留完整，然后在将 CSV 上传到 Klaviyo 时映射到 Klaviyo 的 **源** 字段。 - 时间戳字段（例如“添加日期”、“上次打开”和“上次单击”）需要进行专门格式化，否则 Klaviyo 不会将它们识别为时间戳字段。确保时间戳数据采用以下格式之一：
  年-月-日 时:分:秒
  月/日/年 时:分:秒
  月/日/年 时:分:秒
  月/日/年 时:分
  月/日/年 时:分
  YYYY-MM-DDTHH:MM:SS

以下是如何设置 CSV 文件格式的示例。 ![大多数数据已模糊的 CSV 示例](https://klaviyo.zendesk.com/hc/article_attachments/28716352844699)

仔细检查您的 CSV 文件，根据需要编辑和删除列标题和联系人条目。请记住，在将 CSV 文件上传到 Klaviyo 之前解析和编辑其中的数据要容易得多。有关格式化 CSV 文件的更多详细说明，请参阅我们关于[创建联系人并将其添加到新列表](https://klaviyo.zendesk.com/hc/en-us/articles/115005078967) 的文章。 ## 将 CSV 文件导入 Klaviyo 列表

设置导出数据的格式后，您可以将其导入到 Klaviyo 中的列表中。某些 Klaviyo 流是由添加到列表中的电子邮件地址触发的。在开始将联系人上传到列表之前，请确保这些相关流程已切换为草稿或手动模式。 1. 登录您的 Klaviyo 帐户，单击****受众****下拉列表，然后选择****列表和细分****。 2. 选择您要添加联系人的列表。对于此示例，我们将向新闻通讯列表添加订阅者。 3. 在列表的右上角，从 **管理列表** 下拉列表中选择 **导入联系人****。 ![Klaviyo 中的通讯列表，管理列表下拉菜单打开](https://klaviyo.zendesk.com/hc/article_attachments/28716352847003)
4. 拖放 CSV 文件。在 Klaviyo 开始导入之前，系统将提示您检查字段映射。点击**电子邮件**行中的****订阅电子邮件营销****，表示此上传中的所有个人资料均已明确同意接收您发送的电子邮件营销。 5. 仔细检查每个导入字段/相应的 Klaviyo 字段，并进行适当修改。默认情况下，所有已识别的字段都包含在导入中。您可以通过取消选中字段名称右侧的框来忽略导入字段。 ![列出具有完全映射字段的导入页面并在右上角开始导入](https://klaviyo.zendesk.com/hc/article_attachments/28716329847579)
6. Listrak默认有一个**Method**列，表示订阅方式。我们建议将此字段映射到 Klaviyo 的 **Source** 字段。 7. 在您的 Klaviyo 帐户中没有对应字段名称的列名称将被标记为“未映射”。如果您尝试导入未映射的字段，您将收到一条错误消息，提示您映射该字段。默认情况下，所有已识别的字段都包含在导入中。您可以通过取消选中字段名称右侧的框来忽略导入字段。从下拉列表中选择现有字段名称，或通过在空白输入字段中键入名称来创建自定义字段。在字段名称右侧，从以下选项中选择数据类型：****字符串****、****布尔****、****数字****、****日期****、****列表**** 或****同意****。如果您不确定数据类型，请参阅 Klaviyo 中关于[数据类型](https://klaviyo.zendesk.com/hc/en-us/articles/115005237648) 的文章。以下是 Listrak 联系人导入的字段映射示例。 ![列表导入页面，其中未映射的字段以红色突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28716352851995)
8. 完成后，单击屏幕右上角的****开始导入****。要更深入地了解导入联系人，请参阅我们关于[将现有订阅者迁移到 Klaviyo 并取消订阅](https://klaviyo.zendesk.com/hc/en-us/articles/115002053752) 的文章。 ## 导出Listrak取消订阅

将您的 Listrak 取消订阅添加到 Klaviyo 的黑名单非常重要，以确保遵守垃圾邮件法并保持较高的送达率。这些是导出 Listrak 取消订阅列表和禁止列表的一般准则。 如需最新说明，请联系 [Listrak 支持](https://www.listrak.com/company/contact) 并查看他们的[文档](https://help.listrak.com/en/)

1. 转到您的 Listrak ****主菜单 > 联系人****。 2. 转到****查看****，然后选择****取消订阅的联系人> 导出列表向导****。 3. 选择****纯文本.CSV**** 作为导出格式，然后单击****下一步****。 4. 按照向导的其余说明下载取消订阅。除了导出您的取消订阅联系人之外，您可能还需要导出您的 Listrak 抑制列表。导航至您的 Listrak 联系人部分，然后选择****此处为禁止列表名称****列表。按照上述步骤以 CSV 格式导出此列表。 ![Listrak 中的列表列表，包括抑制列表](https://klaviyo.zendesk.com/hc/article_attachments/28716352854555)

设置黑名单的格式，使其包含单列电子邮件地址。 ## 将历史取消订阅加载到 Klaviyo

1. 导航至 Klaviyo 帐户中的****个人资料****选项卡（位于****受众****下），然后单击右上角的****禁止的个人资料****。 2. 选择****上传文件****。 3. 单击****选择文件**** 选择包含 Listrak 抑制的 CSV 文件。然后，单击****上传抑制****。 ![Klaviyo 中的上传抑制文件弹出窗口](https://klaviyo.zendesk.com/hc/article_attachments/28716352856859)
4. 您的 Klaviyo 抑制列表现在将反映您的导入。 ## 将电子邮件模板从 Listrak 迁移到 Klaviyo

Klaviyo 提供了直观的拖放模板生成器，您可以使用它来重新创建 Listrak 电子邮件模板。我们强烈建议使用此方法来重建您的模板，因为它将确保它们针对移动设备进行了优化、响应迅速且易于编辑。查看[我们的 Klaviyo 模板编辑器使用指南](https://klaviyo.zendesk.com/hc/en-us/articles/4407911841435)。如果您没有时间重新创建 Listrak 模板，可以从 Listrak 以原始 HTML 格式导出电子邮件模板，然后将更新的原始 HTML 上传到 Klaviyo。如果您选择导入原始 HTML 模板，可以参考我们关于[导入自定义 HTML 模板]的文章(https://klaviyo.zendesk.com/hc/en-us/articles/115005254068)。 ## 注销您的 Listrak 帐户

将所有数据移至 Klaviyo 后，您可以采取三个关键步骤来确保您不再需要 Listrak 帐户：

1. 确保您的注册表单和列表增长工具指向 Klaviyo，而不是 Listrak
2. 将 Listrak 工作流程重新创建为 Klaviyo 流程
3. 停止使用Listrak

### 注册表单和列表增长工具

在 Klaviyo 中重新创建任何 Listrak 注册表单，以便您的列表在 Klaviyo（而不是 Listrak）中继续增长。您可以：

1. 使用 Klaviyo [注册表单生成器](https://help.klaviyo.com/hc/en-us/articles/360026474752) 从头开始重新创建表单
2.使用与Klaviyo集成的第三方列表增长工具
3. 通过您的电子商务平台集成您的自定义表单

如果您使用第三方列表增长工具，请确保这些工具同步到 Klaviyo。 Klaviyo 与许多用于列表增长和登陆页面的工具集成。 [查看我们的应用程序市场](https://marketplace.klaviyo.com/en-us/) 以查找您正在使用的工具。如果您没有看到它列出，请考虑使用 Klaviyo 的本机注册表单生成器来创建表单，或尝试切换到其他第三方工具。请注意，默认情况下，所有 Klaviyo 列表都是双重选择加入的。要将列表更改为单一选择加入，请前往我们的[双重选择加入流程指南](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108)的该部分。如果您使用自定义编码表单，请通过让自定义表单将新订阅者直接同步到您的电子商务平台来确保您的联系人同步到 Klaviyo，并确保您的电子商务平台与您的 Klaviyo 帐户集成。将所有注册表单切换或同步到 Klaviyo 后，等待几天并在 Listrak 中查看您的列表。如果您注意到订阅者仍在添加到这些列表中，则可能至少有一种表单仍需要更换。接下来，您需要关闭 Listrak 注册表单。 [联系 Listrak 支持](https://www.listrak.com/contact) 了解如何关闭 Listrak 注册表单的信息。 ### 流量

Klaviyo 将自动化工作流程称为“流程”，它允许更高级和更有针对性的序列。在 Klaviyo 中重新创建这些内容非常重要，这样您就不需要继续使用 Listrak 发送触发式电子邮件。当您离开 Listrak 时，可能是刷新和更新自动消息传递的好时机。我们建议您尽快打开欢迎系列和废弃购物车流程。欢迎系列对于吸引新订阅者尤其重要，而废弃的购物车流比任何其他类型的流具有最高的投资回报率。一旦您的 Klaviyo 流程上线，您将需要关闭 Listrak 中的所有工作流程，以确保您不会向其他人重复发送电子邮件。 [联系 Listrak 支持](https://www.listrak.com/contact) 了解有关关闭 Listrak 工作流程的更多信息。 ### 停止使用 Listrak

一旦您将所有列表增长工具指向您的 Klaviyo 帐户、暂停您的 Listrak 工作流程并启用您的 Klaviyo 流程，您就可以停止使用 Listrak。在关闭 Listrak 帐户之前，请仔细检查一切是否按预期运行。在您的注册表单和其他列表增长工具中输入测试电子邮件，放弃购物车，然后注册您的时事通讯以触发欢迎系列。转到您的 Klaviyo 帐户中的****个人资料****选项卡（位于****受众****下），确保个人资料中的信息反映了所有正确的沟通。如果您注册的列表是双重选择加入的，请务必先确认您的电子邮件。完成这些步骤并完全迁移到 Klaviyo 后，您可以关闭您的 Listrak 帐户。 ## Klaviyo 的后续步骤

一旦您的 Klaviyo 帐户与您的商店集成，并且您的所有数据都从 Listrak 移植过来，您就可以按照我们的 [Klaviyo 入门课程](https://academy.klaviyo.com/getting-started-with-klaviyo) 进行第一次 Klaviyo 发送。如果您对从 Listrak 过渡或开始使用 Klaviyo 有疑问，请[联系我们的支持团队](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272)。 ## 结果

您现在已从 Listrak 迁移到 Klaviyo，并了解了迁移电子邮件提供商的最佳实践。 ## 其他资源

- [如何解决列表导入问题](https://help.klaviyo.com/hc/en-us/articles/115005078807)
- [了解电子邮件送达率](https://help.klaviyo.com/hc/en-us/articles/115005247008)
- [配置文件属性参考](https://help.klaviyo.com/hc/en-us/articles/115005074627)