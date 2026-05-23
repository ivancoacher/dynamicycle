---
id: "1260806293150"
title: "如何使用 CSV 上传导入配置文件属性"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/1260806293150-How-to-import-profile-properties-using-a-CSV-upload"
section: "Profile management"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T11:04:56Z"
language: "zh"
---
## 你将会学到

了解配置文件属性以及如何通过上传 CSV 文件导入它们。这种向 Klaviyo 添加个人资料属性的方法要求您将联系人上传到列表。如果您的文件包含未明确选择加入电子邮件或短信营销的联系人，请务必小心，确保不会向这些联系人发送不需要的消息，因为这可能会影响您的送达率。 [了解有关送达率的更多信息。](https://help.klaviyo.com/hc/en-us/articles/115005247008)

## 目录

要使用 CSV 上传导入配置文件属性：

1. [创建格式正确的 CSV 文件](#h_01G3VR2ERGP5SK3JRQDE6686XV)。 2. [上传 CSV 文件](#h_01G3VR2MDFF51K1TMDXR954279)。 3. [检查导入](#h_01G3VR2VQMPA6SZRHPEX3B1BQP)。 4. [确保合规性](#h_01G3VR33BN9G1TPV69DGT4NSNA)。 ## 创建一个 CSV 文件

将配置文件属性上传到 Klaviyo 的第一步是创建包含这些属性的格式正确的 CSV 文件。使用任何电子表格工具创建文件，例如 Excel 或 Google Sheets。 1. 在 CSV 中，标记第一列的第一行 **电子邮件。**
2. 在以下列的第一个单元格中，添加您要上传的配置文件属性的名称（例如名字、姓氏）。 3. 在以下行中，添加您要上传的电子邮件地址和个人资料属性。 ![可供上传的示例 CSV 文件](https://klaviyo.zendesk.com/hc/article_attachments/28717383030171)

确保电子表格中的所有数据均采用 Klaviyo 可以读取的格式。 [了解有关 Klaviyo 中数据类型的更多信息](https://help.klaviyo.com/hc/en-us/articles/115005237648-About-Data-Types)，包括如何格式化它们。 ## 上传配置文件属性

![演示如何将配置文件属性导入 Klaviyo 的视频](https://fast.wistia.com/embed/medias/v2e7efjdrp/swatch)

当您的 CSV 文件准备好上传后：

1. 导航至 Klaviyo 中的****受众 > 列表和细分****。 2. 在右上角选择****新建****按钮并设置列表名称和任何标签。 3. 选择****创建列表****。 - 如果您使用的是现有列表而不是新列表，请单击进入列表并打开右上角的****管理列表****下拉列表，然后****导入联系人****。 4. 单击****上传联系人****。 5. 单击“****上传****”并选择您刚刚在上传模式中创建的 CSV 文件。 6. 将 CSV 中的每一列映射到 Klaviyo 中的相应属性。 7. 如果 Klaviyo 中尚不存在该属性，请单击****选择**** ****或创建新****下拉列表，然后选择****创建新字段****。 ![地图.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717383034011)
8. 单击 ****下一步****。 9. 选择**否，导入而不更新订阅状态**。 10. 单击****导入****。不要更新同意状态来订阅这些配置文件。如果您这样做，列表中的所有个人资料都将在 Klaviyo 中标记为订阅者，即使他们之前已取消订阅。通过选择**否，导入而不更新订阅状态**，当前订阅的任何人都将保持订阅状态，取消订阅者将继续受到抑制。您的导入可能需要几秒钟到几个小时的时间，具体取决于列表的大小。您可以离开该页面，上传将继续。您的上传遇到问题吗？请参阅 Klaviyo 的[问题排除列表导入]指南(https://help.klaviyo.com/hc/en-us/articles/115005078807-How-To-Troubleshoot-List-Imports)。 ## 检查您的导入

导入完成后，打开您的列表并单击任何配置文件。导航至其个人资料的 **信息** 部分。在这里，您将找到刚刚上传的属性。许多属性将出现在**自定义属性**下，但请注意，一些默认的 Klaviyo 属性（例如电话号码或名字和姓氏）将出现在**联系人**部分中。请注意，如果在此上传过程中有任何新联系人添加到您的列表中，他们将进入与该列表关联的任何列表触发流。如果您要将新联系人添加到列表并且不希望他们触发流程，请暂时关闭您的流程。 ## 确保合规性

为了保持强大的交付能力并遵守数据隐私和营销法律，请确保您只向明确选择接受电子邮件或短信营销的人进行营销。如果您上传的列表包含未选择加入的个人资料，我们建议您采取预防措施，确保您不会意外联系到他们。 例如，您可以：

- 检查您的细分定义以确认仅包含选择加入的订户。 - 上传完成后删除列表。要删除列表，但保留配置文件，请导航至****列表和段****选项卡。找到您刚刚创建的列表，然后单击更多选项图标（三个垂直点）。单击****删除****。为了维护您的数据安全，Klaviyo 的支持团队无法打开您的 CSV 文件。如需对列表导入进行故障排除的进一步帮助，请[联系支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)，并提供问题的详细说明以及您遇到的错误的屏幕截图。 ## 其他资源

- [关于个人资料的信息部分](https://help.klaviyo.com/hc/en-us/articles/115005247028-About-The-Information-Section-of-a-Profile)
- [属性指南](https://help.klaviyo.com/hc/en-us/articles/115005074627-Guide-to-Properties)
- [关于数据类型](https://help.klaviyo.com/hc/en-us/articles/115005237648-About-Data-Types)
- [如何在文本块中插入个性化](https://help.klaviyo.com/hc/en-us/articles/115000096232)