---
id: "360036945872"
title: "如何从 Sailthru 迁移"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360036945872-How-to-migrate-from-Sailthru"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T10:57:26Z"
language: "zh"
---
## 你将会学到

了解如何从 Sailthru 迁移到 Klaviyo。虽然 Klaviyo 没有与 Sailthru 内置集成，但您可以通过从 Sailthru 导出数据并将其导入到 Klaviyo 来迁移数据。此外，当您将电子商务商店与 Klaviyo 集成时，您将能够根据浏览器的现场活动触发电子邮件。 ## 开始之前

本指南将引导您完成将数据从 Sailthru 迁移到 Klaviyo。当您迁移 Sailthru 列表时，请记住，迁移数据的主要目标是确保所有相关联系人和字段都在 Klaviyo 中显示，并且任何选择退出的联系人都会在 Klaviyo 中得到同样的处理。下面我们提供了一种推荐方法，允许您将选择加入的联系人上传到 Klaviyo，并根据联系人在 Sailthru 中的选择退出状态将各种联系人视为取消订阅。我们建议您查看[Sailthru 如何定义您的联系人状态](https://getstarted.sailthru.com/audience/managing-users/user-optout-levels/)，以便您可以确保 Sailthru 端的数据质量，并确保这种上传联系人的方法符合您对 Klaviyo 的预期用途。本指南为您提供将数据从 Sailthru 迁移到 Klaviyo 的一般准则。请联系 [Sailthru 支持](https://getstarted.sailthru.com/contact/)，获取有关导出 Sailthru 数据的最新说明。 ## 清单

从 Sailthru 迁移到 Klaviyo 需要几个关键步骤：

1. 导出所有 Sailthru 选择加入
2.格式化CSV文件
3. 将 CSV 文件导入 Klaviyo 列表
4. 导出 Sailthru 选择退出
5. 将选择退出添加到您的 Klaviyo 抑制列表中
6. 迁移电子邮件模板
7. 导出额外的 Sailthru 数据
8. 设置关键 Klaviyo 直播流
9. 注销您的 Sailthru 帐户
10. 发送您的第一个 Klaviyo 活动

## 导出 Sailthru 选择加入

首先，您需要导出您的 Sailthru 选择加入联系人列表。为了增强安全性，只有已被管理员分配 PII（个人身份信息）权限的 Sailthru 席位（管理员）才能下载原始电子邮件地址。因此，在开始 Sailthru 数据导出之前，请确保您拥有必要的权限。没有 PII 权限的 Sailthru 席位只能下载无法在 Klaviyo 中使用的“哈希”电子邮件地址。要隔离选择加入的联系人，您需要使用 [Sailthru 的受众生成器](https://getstarted.sailthru.com/audience/audience-builder/using-audience-builder/) 创建包含选择加入的联系人的智能列表。例如，设置受众生成器过滤器以排除选择退出的用户。还包括导出中特定字段和 VARS（自定义字段/变量）的过滤器。 ![橙色框出的自定义字段定义](https://klaviyo.zendesk.com/hc/article_attachments/28717811443739)

创建选择加入列表后，以 CSV 格式导出列表。请按照以下 Sailthru 说明导出列表：

1. 在“我的 Sailthru”中，转至 ****用户**** ****>**** ****列表****。 2. 找到要导出的列表，然后在最右列中单击 **Excel 图标**。 3. 选择****所有电子邮件****，然后单击****导出****。 4. 文件准备好后，下载将自动开始。或者，在处理导出时，您可以离开该页面，稍后返回到 [Jobs](https://my.sailthru.com/reports/jobs) 页面：
   - 在 My Sailthru 顶部，单击 **菜单图标**。 - 在表格中找到您的工作。如果完成，请在该行的末尾单击以下载该文件。 5. 如果您在创建和导出选择加入列表方面需要帮助，请联系 [Sailthru 支持](https://getstarted.sailthru.com/account/management/support/)。 ## 格式化 CSV 文件

在将每个 CSV 文件导入 Klaviyo 之前，您需要对其进行格式化。为此，请打开 CSV 文件并梳理列表，特别注意列标题​​。 - 列标题应位于 CSV 文件的第一行。如果 Sailthru 在列标题之前添加额外的行，请删除这些额外的行。 - 您的 CSV 文件必须包含“电子邮件”或“电子邮件地址”列。 - 您可能需要包含“名字”和“姓氏”列。 - 包含您想要上传到 Klaviyo 的任何 VARS（自定义个人资料属性），例如“性别”。 - 时间戳字段（例如“添加日期”、“上次打开”和“上次单击”）需要进行专门格式化，否则 Klaviyo 不会将它们识别为时间戳字段。 确保时间戳数据采用以下格式之一：
  年-月-日 时:分:秒
  月/日/年 时:分:秒
  月/日/年 时:分:秒
  月/日/年 时:分
  月/日/年 时:分
  YYYY-MM-DDTHH:MM:SS

以下是如何设置 CSV 文件格式的示例。 ![包含名字和姓氏等字段的联系人 CSV 示例](https://klaviyo.zendesk.com/hc/article_attachments/28717851116955)

仔细检查您的 CSV 文件，根据需要编辑和删除列标题和联系人条目。请记住，在将 CSV 文件上传到 Klaviyo 之前解析和编辑其中的数据要容易得多。有关格式化 CSV 文件的更多详细说明，请参阅我们关于[创建联系人并将其添加到新列表](https://klaviyo.zendesk.com/hc/en-us/articles/115005078967) 的文章。 ## 将 CSV 文件导入 Klaviyo 列表

设置导出数据的格式后，您可以将其导入到 Klaviyo 中的列表中。某些 Klaviyo 流是由添加到列表中的电子邮件地址触发的。在开始将联系人上传到列表之前，请确保这些相关流程已切换为草稿或手动模式。 1. 登录您的 Klaviyo 帐户，选择****受众****下拉列表，然后单击****列表和细分****。 2. 选择您要添加联系人的列表。对于此示例，我们将向新闻通讯列表添加订阅者。 3. 在列表的右上角，从 **管理列表** 下拉列表中选择 **导入联系人****。 ![Klaviyo 时事通讯列表，管理列表下拉菜单打开](https://klaviyo.zendesk.com/hc/article_attachments/28717811450779)
4. 拖放 CSV 文件。在 Klaviyo 开始导入之前，系统将提示您检查字段映射。点击**电子邮件**行中的****订阅电子邮件营销****，表示此上传中的所有个人资料均已明确同意接收您发送的电子邮件营销。 5. 仔细检查每个导入字段/相应的 Klaviyo 字段，并进行适当修改。默认情况下，所有已识别的字段都包含在导入中。您可以通过取消选中字段名称右侧的框来忽略导入字段。 6. 在您的 Klaviyo 帐户中没有对应字段名称的列名称将被标记为“未映射”。如果您尝试导入未映射的字段，您将收到一条错误消息，提示您映射该字段。默认情况下，所有已识别的字段都包含在导入中。您可以通过取消选中字段名称右侧的框来忽略导入字段。从下拉列表中选择现有字段名称，或通过在空白输入字段中键入名称来创建自定义字段。在字段名称右侧，从以下选项中选择数据类型：****字符串****、****布尔****、****数字****、****日期****、****列表**** 或****同意****。如果您不确定数据类型，请参阅我们有关[数据类型]的文章(https://help.klaviyo.com/hc/en-us/articles/115005237648)。请注意，时间戳字段（例如上次打开或上次单击）必须映射为日期。以下是 Sailthru 联系人导入的字段映射示例。 ![导入已映射所有字段的评论页面](https://klaviyo.zendesk.com/hc/article_attachments/28717851128731)
7. 完成后，单击屏幕右上角的****开始导入****。要更深入地了解导入联系人，请参阅我们关于[将现有订阅者迁移到 Klaviyo 并取消订阅](https://help.klaviyo.com/hc/en-us/articles/115002053752) 的文章。 ## 导出 Sailthru 选择退出

您需要下载选择退出电子邮件通信的客户，然后将其上传到您的 Klaviyo 抑制列表。首先导出您的选择退出列表。请遵循 Sailthru 的 [导出您的选择退出数据的说明](https://getstarted.sailthru.com/audience/export/export-user-data/)：

1. 在 My Sailthru 中，转至 ****用户 >**** ****列表****。 2. 找到要导出的列表，然后在最右侧的列中单击 **Excel 图标****。**
3. 选择****退出****，然后单击****导出****。 4. 文件准备好后，下载将自动开始。或者，在处理导出时，您可以离开该页面，稍后返回到 [Jobs](https://my.sailthru.com/reports/jobs) 页面：
   - 在 My Sailthru 顶部，单击 **菜单图标**。 - 在表格中找到您的工作。如果完成，请在该行的末尾单击以下载该文件。 5. 设置选择退出列表的格式，使其包含单列电子邮件地址。 可以有“电子邮件”列标题，但这对于导入到 Klaviyo 来说不是必需的。 6. 这是禁止列表 CSV 文件格式的示例：
   ![示例电子邮件地址电子表格](https://klaviyo.zendesk.com/hc/article_attachments/28717851121947)

## 将选择退出添加到您的 Klaviyo 抑制列表中

1. 导航至 Klaviyo 帐户中的****个人资料****选项卡（位于****受众****下），然后单击右上角的****禁止的个人资料****。 2. 选择****上传文件****。 3. 单击****选择文件**** 选择包含 Sailthru Optouts 的 CSV 文件。然后，单击****上传抑制****。 4. 您的 Klaviyo 抑制列表现在将反映您的导入。 ## 将您的电子邮件模板从 Sailthru 迁移到 Klaviyo

Klaviyo 具有直观的拖放模板生成器，您可以使用它来重新创建 Sailthru 电子邮件模板。我们强烈建议使用此方法来重建您的模板，因为它将确保它们针对移动设备进行了优化、响应迅速且易于编辑。查看[我们的 Klaviyo 模板编辑器使用指南](https://klaviyo.zendesk.com/hc/en-us/articles/4407911841435)。如果您没有时间使用 Klaviyo 的模板生成器重新创建 Sailthru 模板，可以从 Sailthru 以原始 HTML 格式导出电子邮件模板，然后将更新的原始 HTML 上传到 Klaviyo。 ### 从 Sailthru 导出整个模板 HTML

要查找 Sailthru 模板的代码：

1. 单击模板，然后单击****代码****选项卡。 2. 在这里，您将可以访问给定模板的 HTML。 ![Sailthru 中电子邮件模板的 HTML](https://klaviyo.zendesk.com/hc/article_attachments/28717811462939)
3. 您可以复制整个模板代码并将其另存为 HTML 文件。 4. 请记住将任何 Sailthru 特定标签替换为适用的 [Klaviyo 标签](https://help.klaviyo.com/hc/en-us/articles/115005084927-Template-Tags-and-Variable-Syntax)（例如名字标签、取消订阅链接等）。 5. 要将文件上传到 Klaviyo，请单击 Klaviyo 中的****内容****下拉列表并选择****模板****选项卡，然后选择****创建模板****。 6. 然后，选择****导入您的模板****。在这里，系统将提示您从计算机中选择 HTML 文件，然后您可以上传刚刚保存的文件。 7. 您可以在****预览****选项卡中查看电子邮件模板的预览。请注意，今后您将必须直接编辑 HTML 才能更改模板。有关导入原始 HTML 模板的更多信息，您可以参考我们的文章[导入自定义 HTML 模板](https://klaviyo.zendesk.com/hc/en-us/articles/115005254068)。 ### 批量复制 Sailthru 模板 HTML

或者，您可以从 Sailthru 模板中导出代码块，然后将它们导入到 Klaviyo 拖放编辑器中的文本块中。为此：

1. 在您的 Sailthru 帐户中，在 ****Code**** 选项卡中找到特定模板的代码。 2. 在 Klaviyo 中，转到****模板****选项卡（****内容****下）并单击****创建模板****来创建新的拖放模板。然后，选择****基本****。在这里，您可以选择一个无样式的模板作为起点，您将使用 Sailthru 模板中的代码覆盖该模板。 ![Klaviyo 中的基本电子邮件模板选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28717811456667)
3. 单击模板中的文本块，然后单击****源代码。 ![Klaviyo 模板生成器中的文本块，源按钮突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28717811459099)****
4. 将现有文本替换为 Sailthru 模板中的 HTML，并对您想要直接迁移到 Klaviyo 的代码部分重复此过程。然后，您可以使用 Klaviyo 的拖放编辑器填充任何空白。 5. 请记住将任何 Sailthru 特定标签替换为适用的 [Klaviyo 标签](https://help.klaviyo.com/hc/en-us/articles/115005084927-Template-Tags-and-Variable-Syntax)（例如名字标签、取消订阅链接等）。 ## 导出额外的 Sailthru 数据

本文中的说明可帮助您提取在 Klaviyo 中启动和运行所需的数据。如果您需要从 Sailthru 导出未包含在这些导出中的其他数据，您可能需要考虑使用 Sailthru 的付费[数据导出器](https://getstarted.sailthru.com/analytics/exports/data-exporter/) 服务。 ## 设置关键流程

设置实时流是确保正确预热发送基础设施的关键步骤。流程是基于操作的自动化，允许您根据客户在店面的活动触发消息。因此，通过流发送的电子邮件通常比批量发送的营销活动电子邮件具有更高的参与率。首先，启用以下流程：

- [废弃的购物车](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow)
- [欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172-Guide-to-Creating-a-Welcome-Series)
- [购买后](https://help.klaviyo.com/hc/en-us/articles/360028872611-Guide-to-Creating-a-Post-Purchase-Flow)

## 注销您的 Sailthru 帐户

将所有数据移至 Klaviyo 后，您可以采取三个关键步骤来确保您不再需要 Sailthru 帐户：

1. 确保您的注册表单和列表增长工具指向 Klaviyo，而不是 Sailthru
2. 按照 Klaviyo 流程重新创建 Sailthru 工作流程
3.停止使用Sailthru

### 注册表单和列表增长工具

在 Klaviyo 中重新创建任何 Sailthru 注册表单，以便您的列表在 Klaviyo 而不是在 Sailthru 中继续增长。您可以：

1. 使用 Klaviyo [注册表单生成器](https://help.klaviyo.com/hc/en-us/articles/360026474752) 从头开始重新创建表单
2.使用与Klaviyo集成的第三方列表增长工具
3. 通过您的电子商务平台集成您的自定义表单

如果您使用第三方列表增长工具，请确保这些工具同步到 Klaviyo。 Klaviyo 与许多用于列表增长和登陆页面的工具集成。 [扫描我们的应用程序集成列表](https://help.klaviyo.com/hc/en-us/categories/115000874028-App-Integrations) 以查找您正在使用的工具。如果您没有看到它列出，请考虑使用 Klaviyo 的本机注册表单生成器来创建表单，或尝试切换到其他第三方工具。请注意，默认情况下，所有 Klaviyo 列表都是双重选择加入的。要将列表更改为单一选择加入，请前往我们的[双重选择加入流程指南](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108)的该部分。如果您使用的是自定义编码表单，请确保您的自定义表单将新订阅者直接同步到您的电子商务平台，并且您的电子商务平台与您的 Klaviyo 帐户集成，从而将这些联系人同步到 Klaviyo。将所有注册表单切换或同步到 Klaviyo 后，等待几天并在 Sailthru 中查看您的列表。如果您注意到订阅者仍在添加到这些列表中，则可能至少有一种表单仍需要更换。接下来，您需要关闭 Sailthru 注册表单。 [联系 Sailthru 支持](https://getstarted.sailthru.com/account/management/support/)，了解有关如何关闭 Sailthru 注册表单的信息。 ### 触发消息

您可能在 Sailthru 中运行一系列触发消息，并且希望在 Klaviyo 中重新创建它们。在 Klaviyo 中，这些类型的消息称为流。当您离开 Sailthru 时，是刷新和更新自动消息传递的好时机。我们建议您尽快打开欢迎系列和废弃购物车流程（见上文）。欢迎系列对于吸引新订阅者尤其重要，而废弃的购物车流比任何其他类型的流具有最高的投资回报率。一旦您的 Klaviyo 流程上线，您将需要关闭 Sailthru 中所有触发的消息，以确保您不会向他人重复发送电子邮件。请联系 [Sailthru 支持](https://getstarted.sailthru.com/contact/) 了解更多信息。 ### 注销您的 Sailthru 帐户

一旦您将所有列表增长工具指向您的 Klaviyo 帐户、暂停您的 Sailthru 触发消息并启用您的 Klaviyo 流，您就可以停止使用 Sailthru。在关闭 Sailthru 帐户之前，请仔细检查一切是否按预期运行。在您的注册表单和其他列表增长工具中输入测试电子邮件，放弃购物车，然后注册您的时事通讯以触发欢迎系列。转到您的 Klaviyo 帐户中的****个人资料****选项卡（位于****受众****下），确保个人资料中的信息反映了所有正确的沟通。如果您注册的列表是双重选择加入的，请务必先确认您的电子邮件。 完成这些步骤并完全迁移到 Klaviyo 后，您可以关闭您的 Sailthru 帐户。 ## 发送您的第一个 Klaviyo 活动

一旦您的 Klaviyo 帐户与您的商店集成，并且您的所有数据都从 Sailthru 移植过来，您就可以使用 Klaviyo 发送您的第一个营销活动。 ### 创建并发送给 30 天活跃订阅者群体

在 Klaviyo 中，建立 30 天活跃订阅者的细分。 1. 导航至****列表和细分****选项卡（位于****受众****下）并选择****创建列表/细分>细分****。 2. 按照以下标准构建细分：
   ![Klaviyo 细分构建器中的 Sailthru 30 天参与细分](https://klaviyo.zendesk.com/hc/article_attachments/28717811465243)
3. 记下您的 30 天参与段中有多少人。 - 如果您的细分中有0-50,000人，您可以立即发送，不需要使用批量发送
   - 如果您的细分中有 50,000-100,000 人，请使用批量发送并选择在 5 小时内发送至 20% 的选项
   - 如果您的细分中有超过 100,000 人，请使用批量发送并选择在 10 小时内发送至 10% 的选项
4. 导航至****营销活动****选项卡并选择****创建营销活动****。选择您的 30 天参与细分作为目标受众。 ![设置将营销活动发送到 30 天参与段](https://klaviyo.zendesk.com/hc/article_attachments/28717851146779)
5. 使用您从 Sailthru 迁移过来的模板之一填写此营销活动的内容，或者从头开始创建一个新模板。 6. 编辑完营销活动内容后，选择****查看并发送营销活动****。检查营销活动设置以确保一切正确。然后，单击****安排****或****发送****。 7. 如果您需要使用批量发送，请从计划下拉列表中选择****在几个小时内逐渐发送****，然后根据如上所述的 30 天参与段中的人数选择适当的策略。 ![准备好发送了吗？ Klaviyo 中的页面，包含“计划”和“立即发送”选项](https://klaviyo.zendesk.com/hc/article_attachments/28717851153819)

欲了解更多信息，请查看我们的[Klaviyo入门课程](https://academy.klaviyo.com/getting-started-with-klaviyo)。 ### 监控性能

发送第一个营销活动后，[监控绩效](https://help.klaviyo.com/hc/en-us/articles/115000201131) 非常重要，以确保强大的送达率阈值。请参阅下表来衡量您的表现。 |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |独特的打开率|独特点击率|跳出率 |退订率 |垃圾邮件率 |
|太棒了 | 20% 或更多 | 4% 或以上 |低于 0.5% |低于 0.3% | 0.0% |
|精通| 15-19% | 2-3.9% | 0.5-0.9% | 0.3-0.5% | 0.0% |
|改进空间| 10-14% | 1-1.9% | 1-1.9% | 0.6-0.9% | 0.1% |
|关键|低于 10% |低于 1% | 2% 或更多 | 1% 或以上 | 0.2%以上 |

如果您的表现落入“优秀”或“熟练”阈值，您可以继续向更广泛的客户群发送信息。否则，请继续发送到您的 30 天参与段，直到您的表现熟练或出色。 ## 后续步骤

### 通过 Klaviyo 建立良好的发件人声誉

一旦您开始向最活跃的客户群体发送信息，您就可以逐渐向更多的客户发送信息。这种渐进的发送过程可以提高您的发件人声誉，称为“温暖您的 IP 地址”。请参阅我们的[有关送达率的文章](https://help.klaviyo.com/hc/en-us/categories/115000873988-Email-Deliverability)，了解有关预热发送基础设施的更多信息。 ### 使用高级细分来吸引您的客户

在第一个月左右吸引了最感兴趣的订阅者后，您可以开始接触其他客户群。创建额外的细分以确保您覆盖客户群的每个角落。 - 复制您的参与（3 个月）部分并调整设置，将时间范围从 3 个月减少到 30 天
- 创建并发送至 90 天活跃订阅者群体
- 使用历史 Sailthru 数据来完善和构建您的细分市场

### 创建并发送给 90 天活跃订阅者群体

为了创建更广泛的订户群体：

1. 导航到****列表和细分****选项卡（位于****受众****下），然后选择****创建列表/细分>细分****。 2. 您的细分应具备以下条件：
   ![sail12.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717851149979)
3. 接下来，创建并安排您的营销活动发送到该组，如上面针对 30 天参与段所述。 4. 请务必密切监控您的交付能力，以确保您的绩效保持强劲。 ## 结果

您现在已从 Sailthru 迁移到 Klaviyo，并了解了迁移电子邮件提供商的最佳实践。 ## 其他资源

- [如何解决列表导入问题](https://help.klaviyo.com/hc/en-us/articles/115005078807)
- [了解电子邮件送达率](https://help.klaviyo.com/hc/en-us/articles/115005247008)
- [配置文件属性参考](https://help.klaviyo.com/hc/en-us/articles/115005074627)