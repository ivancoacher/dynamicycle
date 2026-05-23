---
id: "115005082727"
title: "如何从持续联系迁移"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005082727-How-to-migrate-from-Constant-Contact"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T10:57:35Z"
language: "zh"
---
只有 Klaviyo 帐户所有者或管理员才能从 Constant Contact 执行完整迁移。 ## 你将会学到

了解如何从 Constant Contact 迁移到 Klaviyo。虽然 Klaviyo 没有与 Constant Contact 预先构建的集成，但您可以从 Constant Contact 导出数据并将其上传到 Klaviyo。 ## 开始之前

本指南将引导您完成将数据从 Constant Contact 迁移到 Klaviyo 的过程。迁移时，请确保您：

- 上传您的所有订阅者和联系人，以及有关他们的任何重要信息。 - 记录任何选择退出的联系人（即，在 Klaviyo 中将其保留为取消订阅状态）。 ## 清单

下面，我们提供了一系列步骤，帮助您从 Constant Contact 迁移到 Klaviyo。虽然并非所有这些任务都可能与您相关，但我们建议您查看每个部分：

1. 更改短信发送号码
2. 迁移您的电子邮件和短信订阅列表
3. 迁移您的电子邮件和短信取消订阅列表
4. 迁移您的电子邮件参与度数据
5.导出其他相关数据
6. 设置注册表单并列出增长工具
7. 重新创建您的电子邮件模板
8. 重新创建营销活动和电子邮件自动化
9.停止持续接触使用

## 更改您的短信发送号码

您是否通过 Constant Contact（或其他提供商）发送短信并希望迁移到 Klaviyo？ Constant Contact [仅提供本地号码](https://knowledgebase.constantcontact.com/email-digital-marketing/guides/KnowledgeBase/46718-Getting-started-with-SMS-Marketing?lang=en_US)，这些号码无法移植到 Klaviyo，因此您需要更改发送号码。使用 Klaviyo，有[多种类型的号码可供选择](https://help.klaviyo.com/hc/en-us/articles/6637671573403)。您需要尽早开始，因为请求新号码可能需要时间。您还应该参考[要求和最佳实践](https://help.klaviyo.com/hc/en-us/articles/4403980438555)，了解如何通知订阅者您的号码变更。 ## 迁移您的电子邮件和短信订阅者列表

### 从 Constant Contact 中导出您的电子邮件和短信列表

首先，您需要将订阅者从 Constant Contact 导出到电子表格中。在 [Constant Contact 帮助中心](https://knowledgebase.constantcontact.com/email-digital-marketing/articles/KnowledgeBase/33114-Export-Contacts-Out-of-Constant-Contact-and-into-a-Spreadsheet?lang=en_US#ContactStatus) 了解如何导出它们：

- 您需要使用上面链接的文章中的 **通过电子邮件或短信状态导出联系人** 方法，为电子邮件订阅者导出一份电子表格，为短信订阅者导出一份电子表格。 - 如果联系人同时订阅了电子邮件和短信，他们最终将出现在两个列表中，并且这些个人资料将自动合并到 Klaviyo 中（但同时存在于两个列表中）。 - 当您从 Constant Contact 导出列表时，我们建议对电子邮件使用“**所有已订阅**”状态，对短信使用“**短信已订阅**”状态。 - 确保在导出中包含电子邮件地址和电话号码。您还应该包括您想要带入 Klaviyo 的任何其他客户数据；有关可以上传哪些数据以及如何格式化数据的详细信息，请参阅下一节。 ### 设置 CSV 文件的格式

在将每个 CSV 文件导入 Klaviyo 之前，您需要对其进行格式化：

- 列标题应位于 CSV 文件的第一行。 - 如果有电子邮件地址：第一列应为 **电子邮件** 或 **电子邮件地址**。 - 如果没有电子邮件地址：第一列应为**电话号码**。 - 您可能希望包含以下列：
  - ****名字.****
  - **姓氏**。 - 任何自定义配置文件属性（例如，**生日）**。如果您要包含包含多个值的自定义属性，则应将其格式化为数组（即 [“值 1”、值 2、“值 3”]）。 - 对于电子邮件：参与数据（例如，最后点击）。 - 您可以在Constant Contact中导出**联系来源**字段，指示订阅方式。将此字段保留在 CSV 文件中不变 - 当您将 CSV 上传到 Klaviyo 时，您应该将其映射到 Klaviyo 的 **来源** 字段。 - 对于短信：确保每个电话号码都包含国家/地区代码或包含国家/地区的单独列，并且采用[接受的格式](https://help.klaviyo.com/hc/en-us/articles/360046055671)。如果您只发送到一个国家/地区，您可以轻松地[添加一列](https://help.klaviyo.com/hc/en-us/articles/5306587861531#h_01G0CXAWXCFS6ZRAGTP9JGFWWQ)，为每个联系人提供相同的信息。 以下是电子邮件订阅者格式正确的 CSV 文件的示例：
![](https://klaviyo.zendesk.com/hc/article_attachments/31505833398555)

仔细检查您的 CSV 文件，根据需要编辑和删除列标题和联系人条目。请记住，在将 CSV 文件上传到 Klaviyo 之前解析和编辑其中的数据要容易得多。有关格式化 CSV 文件的更多详细说明，请参阅我们关于[创建联系人并将其添加到新列表](https://help.klaviyo.com/hc/en-us/articles/115005078967) 的文章。有关上传短信联系人的更多具体信息，请查看我们的[短信上传文章](https://help.klaviyo.com/hc/en-us/articles/360035428731)。 ### 将您的 CSV 文件导入 Klaviyo 列表

设置数据格式后，您可以将其导入到 Klaviyo 中的列表中。您应该在 Klaviyo 中创建 2 个单独的列表 - 一个用于电子邮件，一个用于短信。 Klaviyo 有现场直播吗？当您上传 CSV 时，由列表或订阅指标触发的任何流都将开始发送给新上传的订阅者。为了防止这种情况，请在导入之前将流程设置为手动。导入完成后，等待几个小时，然后再返回流程，取消导入联系人的所有待处理发送，然后将流程切换回实时状态。 1. 导航至****受众 > 列表和细分****。 2. 选择您要添加订阅者的列表。这应该分别是您的电子邮件的主电子邮件列表和短信的主短信列表。 - 如果需要，您可以通过单击****新建>列表****在**列表和细分**选项卡中创建新列表。 3. 单击列表右上角的****管理列表****下拉列表。 - 您必须是 Klaviyo 的所有者或管理员才能看到此选项。 4. 单击****导入联系人****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36398782987035)
5. 单击****上传****并选择订阅者的 CSV 文件。 6. 将 CSV 中的每一列映射到 Klaviyo 中的相应属性。 7. 如果 Klaviyo 中尚不存在某个属性，请输入新属性名称并单击****创建新字段****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/31505816096411)
8. 单击****下一步****。 9. 在 **这些联系人是否订阅消息** 下，选择 **** 是**** 以添加同意。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36398782997915)
10. 勾选同意申请类型的复选框：****电子邮件**** 或****短信****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36398753659547)
11. 对于短信：选择要申请的同意类型。您从 Constant Contact 导出的内容包含对 SMS 营销消息的同意，这也意味着对交易消息的同意。因此，我们建议选择****营销和交易消息****
12. 准备好继续后，单击****导入****。 ## 迁移您的电子邮件和短信取消订阅列表

### 电子邮件

将您的 Constant Contact 取消订阅添加到 Klaviyo 的黑名单非常重要，以确保遵守垃圾邮件法并保持较高的送达率。要从 Constant Contact 导出取消订阅：

1. [按电子邮件状态导出联系人列表](https://knowledgebase.constantcontact.com/email-digital-marketing/articles/KnowledgeBase/33114-Export-Contacts-Out-of-Constant-Contact-and-into-a-Spreadsheet?lang=en_US#ContactStatus) 到电子表格，就像您对电子邮件列表所做的那样。 2. 在**电子邮件状态**下，选择**取消订阅**。 3. 您只需要 **电子邮件地址** 字段。设置黑名单的格式，使其包含单列电子邮件地址。然后，将您的取消订阅导入到 Klaviyo：

1. 在 Klaviyo 中导航至****受众 > 个人资料****，然后单击右上角的****查看隐藏的个人资料****。 2. 选择****导入****。 3. 单击****上传**** 选择包含您的 Constant Contact 退订信息的 CSV 文件。然后，单击****上传****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/31505833413659)
4. 您的 Klaviyo 抑制列表现在将反映您的导入。 ### 短信

要完成格式化短信退订并将其上传到 Klaviyo，[按照我们的短信退订指南中的步骤操作](https://help.klaviyo.com/hc/en-us/articles/5227452906523)。首先执行以下操作：

1. [按 SMS 状态导出联系人列表](https://knowledgebase.constantcontact.com/email-digital-marketing/articles/KnowledgeBase/33114-Export-Contacts-Out-of-Constant-Contact-and-into-a-Spreadsheet?lang=en_US#ContactStatus) 从 Constant Contact 导出到电子表格，就像您为订阅者所做的那样。 2. 在**短信状态**下，选择**短信取消订阅**。 3. 您需要在一列中输入电话号码（带有国家/地区代码），并在另一列中输入联系人的国家/地区。 4. 根据上面链接的 Klaviyo 指南设置 CSV 的格式。 5. 将您的取消订阅上传到 Klaviyo。 ## 迁移您的电子邮件参与度数据

要将电子邮件参与度数据迁移到 Klaviyo，您需要执行以下操作：

1. 从 Constant Contact 中导出您的[预先构建的互动细分](https://knowledgebase.constantcontact.com/email-digital-marketing/articles/KnowledgeBase/26475-Export-a-Segment-of-Contacts?lang=en_US#Prebuilt)。确保导出参与度最高、参与度较高和参与度最低的细分。 2. [格式化每个 CSV 并将其作为列表上传到 Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005078967)。这些需要是新列表，与您上面创建的电子邮件和短信订阅者列表分开。这些列表将临时用于根据参与度创建 Klaviyo 细分，因为细分无法直接上传到 Klaviyo。 3. 在 Klaviyo 中[创建细分](https://help.klaviyo.com/hc/en-us/articles/115005237908)，其中包含来自 Constant Contact 的每个参与层中主电子邮件列表中的成员。例如，您在 Klaviyo 中参与度最高的电子邮件段可能如下所示：

- 如果某人在或不在列表中 > 位于 > 主电子邮件列表中并且
- 如果某人在或不在列表中 > 在 > 持续联系 最活跃的人
  ![](https://klaviyo.zendesk.com/hc/article_attachments/31505816105243)

然后，您可以使用这些分段来[温暖 Klaviyo 中的发送域](https://help.klaviyo.com/hc/en-us/articles/20413890435355)。将来，您将能够根据 Klaviyo 中收集的数据创建新的参与细分。我们建议您在开始使用 Klaviyo 发送后 1 到 2 个月内为自己设置一个提醒 - 那时，开始使用 Klaviyo 数据制作新的[参与片段](https://help.klaviyo.com/hc/en-us/articles/20413890435355#h_01HF9W4VVWZE4CZNFXGS5FVPBK)。 ## 导出其他相关数据

您可能还想从 Constant Contact 中导出其他相关数据：

1. 虽然我们在上一节中迁移了参与细分，但如果您希望将来参考，您还可以从 Constant Contact 中[按营销活动下载电子邮件报告](https://knowledgebase.constantcontact.com/email-digital-marketing/articles/KnowledgeBase/6413-export-bounced-email-addresses-to-a-file?lang=en_US)。 2. 如果您想要上传到 Klaviyo 的特定联系人列表（除了我们上面导出的联系人列表之外）：了解如何[从 Constant 导出列表联系](https://knowledgebase.constantcontact.com/email-digital-marketing/articles/KnowledgeBase/33114-Export-Contacts-Out-of-Constant-Contact-and-into-a-Spreadsheet?lang=en_US#SingleList)，然后按照我们的指导[将订阅者添加到新列表中] Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005078967)。 3. 除了参与细分之外，您是否还有在 Constant Contact 中创建的联系人细分想要在 Klaviyo 中使用？我们建议使用 [Klaviyo 的分段生成器](https://help.klaviyo.com/hc/en-us/articles/115005237908) 重新创建 Constant Contact 中的任何分段，因为分段无法上传到 Klaviyo。由于您在上一步中上传了电子邮件和短信订阅者，因此您将能够在 Klaviyo 中对这些订阅者进行细分。 ## 设置注册表单并列出增长工具

您应该在 Klaviyo 中重新创建任何 Constant Contact 注册表单，以便您的列表在 Klaviyo（而不是 Constant Contact）中继续增长。您可以使用 Klaviyo [注册表单生成器](https://help.klaviyo.com/hc/en-us/articles/360026474752) 从头开始​​重新创建表单，或使用与 Klaviyo 集成的第三方列表增长工具。如果您已经在使用第三方列表增长工具，请确保这些工具同步到 Klaviyo。 Klaviyo 与许多用于列表增长和登陆页面的工具集成。查看我们的 [Klaviyo 构建的集成目录](https://www.klaviyo.com/integrations/add) 以查找您正在使用的工具。 如果您没有看到它列出，请考虑使用 Klaviyo 的本机注册表单生成器来创建表单，或尝试切换到其他第三方工具。如果您使用自定义编码表单，请通过让自定义表单将新订阅者直接同步到您的电子商务平台来确保您的联系人同步到 Klaviyo，并确保您的电子商务平台与您的 Klaviyo 帐户集成。如果您使用短信，您还需要设置[短信关键字](https://help.klaviyo.com/hc/en-us/articles/360050384091)和[短信订阅链接](https://help.klaviyo.com/hc/en-us/articles/14104388043931)。最后，您需要[停用您的 Constant Contact 注册表单](https://knowledgebase.constantcontact.com/email-digital-marketing/articles/KnowledgeBase/20547-Activate-or-deactivate-a-sign-up-form-installed-on-your-website?lang=en_US)。 ## 重新创建电子邮件模板

Klaviyo 提供了直观的拖放模板生成器，您可以使用它来重新创建 Constant Contact 电子邮件模板。我们强烈建议使用此方法来重建您的模板，因为它将确保它们针对移动设备进行了优化、响应迅速且易于编辑。您可以在 Klaviyo 的流程和营销活动中使用电子邮件模板。查看[我们的 Klaviyo 模板编辑器使用指南](https://help.klaviyo.com/hc/en-us/articles/4407911841435)。 ## 重新创建电子邮件自动化和营销活动

Klaviyo 将自动化工作流程称为“流程”，它允许更高级和更有针对性的序列。在 Klaviyo 中重新创建这些内容非常重要，这样您就不需要继续使用 Constant Contact 来发送自动消息。当您摆脱持续联系时，可能是刷新和更新自动消息传递的好时机。我们建议您尽快打开欢迎系列和废弃购物车流程。欢迎系列对于吸引新订阅者尤其重要，而废弃的购物车流比任何其他类型的流具有最高的投资回报率。我们还建议您从 Klaviyo 中的 Constant Contact 帐户重新创建高性能流程。一旦您的 Klaviyo 流程上线，您将需要[关闭 Constant Contact 中的所有自动消息传递](https://knowledgebase.constantcontact.com/email-digital-marketing/articles/KnowledgeBase/44328-Editing-and-stopping-Automated-Customer-Journeys?lang=en_US)，以确保您不会向其他人重复发送电子邮件。此外，如果您即将开展任何活动，您还需要[在 Klaviyo 中重新创建这些活动](https://help.klaviyo.com/hc/en-us/articles/115005054847)。 ## 停止使用持续接触

完成上述步骤并开始使用 Klaviyo 发送后，您可以停止使用 Constant Contact。在关闭 Constant Contact 帐户之前，请仔细检查一切是否按预期运行：

- 在您的注册表单和其他列表增长工具中输入测试电子邮件和电话号码，然后查看您的双重选择加入和欢迎消息。 - 放弃购物车，看看您的电子邮件和短信是否包含正确的信息。 - 转到 Klaviyo 帐户中的 **个人资料** 选项卡（位于 **受众** 下），以确保个人资料中的信息准确反映。完成这些步骤后，您可以关闭您的 Constant Contact 帐户。 ## Klaviyo 的后续步骤

从 Constant Contact 迁移数据后，您可以按照我们的 [Klaviyo 入门课程](https://academy.klaviyo.com/getting-started-with-klaviyo) 进行第一次 Klaviyo 发送。 ## 结果

您现在已从 Constant Contact 迁移到 Klaviyo 并了解了迁移的最佳实践。 ## 其他资源

[如何解决列表导入问题](https://help.klaviyo.com/hc/en-us/articles/115005078807)

[了解电子邮件送达率](https://help.klaviyo.com/hc/en-us/articles/115005247008)