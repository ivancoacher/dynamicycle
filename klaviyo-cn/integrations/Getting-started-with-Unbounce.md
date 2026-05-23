---
id: "115005082507"
title: "开始使用取消弹跳"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005082507-Getting-started-with-Unbounce"
section: "Unbounce"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: "zh"
---
## 你将会学到

了解如何将 Unbounce 与 Klaviyo 集成，以帮助您使用登陆页面将客户添加到您的主电子邮件列表、触发欢迎系列流程等。您可以通过 Unbounce 登陆页面收集联系信息，然后自动发送欢迎系列和其他个性化消息。启用 Klaviyo 的 Unbounce 集成需要在 Klaviyo 和 Unbounce 内部执行步骤。 ## 目录

1. 验证 Unbounce 中的表单字段
2. 在 Klaviyo 中启用集成
3. 设置 Unbounce webhook
4. 在Klaviyo中查看Unbounce数据
5. 在 Klaviyo 中使用 Unbounce 数据
6. 故障排除

## 验证 Unbounce 中的表单字段

要通过 webhook 将数据拉入 Klaviyo，您的 Unbounce 页面需要一个表单，其中的字段映射到 **电子邮件**。在连接 Webhook 之前，您可以按照下面概述的步骤验证表单字段设置是否正确。 Unbounce 有两种构建页面的方法：标准构建器和智能构建器。在这两种情况下，检查表单字段都是类似的。有关以下任一表单的更多信息，请参阅 Unbounce 关于[设置表单]的文档(https://documentation.unbounce.com/hc/en-us/articles/203799174)。 ### 标准构建器

1. 在 Unbounce 中，选择您要查看的页面，然后单击页面底部的****编辑****。 ![在 Unbounce with Edit 中以深蓝色背景命名的第一个变体的页面](https://klaviyo.zendesk.com/hc/article_attachments/28711662230043)
2. 在页面编辑器中，单击您的表单，然后单击****编辑表单字段****。 ![表单编辑器，其中包含名字、姓氏、电子邮件和行业字段](https://klaviyo.zendesk.com/hc/article_attachments/28711662215451)
3. 单击****电子邮件\*****框以打开字段设置。然后，验证 **字段名称和 ID** 框是否设置为 **电子邮件**。如果您需要编辑此文本，请取消选中**从字段标签自动生成**并进行编辑。 ![在 Unbounce 中设计表单页面，并将字段名称和 ID 框设置为电子邮件](https://klaviyo.zendesk.com/hc/article_attachments/28711674351259)
4. 验证字段名称后，单击****完成****。 5. 如果您对表单进行了任何更改，请单击顶部菜单栏上的****保存****，然后单击****重新发布****以实施更新。 ### 智能建造者

1. 在 Unbounce 中，导航到要编辑的页面，然后单击页面底部的****编辑****。 ![在 Unbounce with Edit 中以深蓝色背景命名的第一个变体的页面](https://klaviyo.zendesk.com/hc/article_attachments/28711662228379)
2. 在表单内，单击“**电子邮件**”文本框下拉列表，然后选择“****编辑字段****”。 ![表单，电子邮件文本框下拉列表打开，编辑字段以深蓝色突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28711674359835)
3. 在 **编辑字段** 菜单中，验证 **字段名称/ID** 框是否设置为 **电子邮件**。 ![编辑字段菜单，字段名称/ID 设置为电子邮件](https://klaviyo.zendesk.com/hc/article_attachments/28711662240923)
4. 验证字段名称后，单击****提交****。 5. 如果您对表单进行了任何更改，请单击顶部菜单栏上的****保存****，然后单击****发布****以实施更新。 ## 在 Klaviyo 中启用集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 单击****探索应用程序****并搜索**Unbounce**，然后单击该卡。 3. 然后，单击****安装****。 4. 单击****连接到Unbounce****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711674390939)
5. 选择 **在 Klaviyo 列表中添加新的 Unbounce 潜在客户** 旁边的复选框，将您的 Unbounce 潜在客户同步到特定的 Klaviyo 列表。从下拉列表中选择您想要将初始销售线索同步到的列表。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711662282139)
6. 复制 **Webhook 设置** 下的 Webhook URL。此 URL 将在以下部分中用于在 Unbounce 中创建指向 Klaviyo 的 Webhook。 7. 单击****完成设置****。 ## 设置 Unbounce webhook

1.前往取消弹跳。从 Unbounce 的 **所有页面** 页面中，选择您想要添加 Klaviyo webhook 的页面。 ![Unbounce 中的所有页面页面均带有深蓝色背景的“Create New”](https://klaviyo.zendesk.com/hc/article_attachments/28711662252699)
2. 单击****集成****选项卡，然后选择****Webhooks**** ****>**** ****添加 Webhook****。 ![Webhooks 测试页的集成选项卡显示其中的 Webhooks 选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28711662248603)
3. 将 Klaviyo 中的 URL 粘贴到 **Choose a URL to POST form data to** 下的第一个文本框中。 ![在 Unbounce 中添加一个 webhook 页面，并在框中使用 Klaviyo webhook URL 并以深蓝色背景保存更改](https://klaviyo.zendesk.com/hc/article_attachments/28711674370075)
4. 验证左侧 **Unbounce Field ID** 下的 **email** 字段是否映射到右侧的 **email**。如果将此属性映射到任何其他值 - 例如 **your\_email** - Klaviyo 不会将此属性识别为电子邮件地址，并且 Webhook 将被删除。映射区分大小写，并且 **电子邮件** 应采用全小写格式。 5. 验证完所有字段后，单击****保存更改****。 6. 留出时间进行集成。如果集成成功，您将看到以下成功消息，告知您**您已成功更新 Webhook**。单击****完成****完成设置。 ![添加带有大绿色勾号和深蓝色背景的“完成”的 Webhook 成功消息](https://klaviyo.zendesk.com/hc/article_attachments/28711674379675)

## 在 Klaviyo 中查看 Unbounce 数据

要在添加 Klaviyo webhook 后检查您的集成，请通过 Unbounce 页面创建新的潜在客户。 Klaviyo 通过 **填写的表单** 指标来同步销售线索，该指标旁边会显示一个取消退回图标。要确认这是否正确同步到 Klaviyo，请导航至 ****分析 > 指标，**** 并按 **Unbounce** 进行筛选。目前，Klaviyo 与 Unbounce 同步一项指标：**填写的表格**。选择**填写的表格**以查看特定于该指标的数据。单击****活动源****图标，您应该会在您的 Klaviyo 帐户中看到为此潜在客户创建的新配置文件。如果您看到此消息，则您的潜在客户现在正在同步。 ![在 Klaviyo 中填写的表单指标活动源显示来自名为 Bill Klaviyo 的个人资料的事件](https://klaviyo.zendesk.com/hc/article_attachments/28711674384027)

仅当您将**电子邮件**作为表单中的必填字段时，Klaviyo 才会记录您的销售线索。如果潜在客户不包含电子邮件地址，Klaviyo 将忽略它。填写的表单指标包含以下元数据，可在段和流中使用：

- ****页面 ID****
  用户填写的表单的唯一ID
- ****页面名称****
  Unbounce 中表单的名称
- ****页面变体****
  Unbounce 中表单的变体，如 [Unbounce 的智能流量](https://documentation.unbounce.com/hc/en-us/articles/360046684972) 中使用的

## 在 Klaviyo 中使用 Unbounce 数据

### 创建一个段

如果您想向回复表单特定变体的客户发送特定的电子邮件活动，您可以使用 **页面变体** 数据在 Klaviyo 中创建一个细分。 1. 导航至 Klaviyo 中的****受众 > 列表和细分****。 2. 单击****创建列表/段****，然后选择****段****。 3. 适当命名新段并将以下定义添加到段中：
   - **如果某人在或不在列表中**：设置为 **是**
     如果您只想使用 Klaviyo 中特定列表中的客户，请设置此选项；否则，转到下一个定义。 - **某人做了什么（或没有做什么）**：设置为 Unbounce 的 **填写表格** 指标并选择您要检查的时间段。 - 单击****添加过滤器****并从下拉列表中选择**页面变体**属性，然后在**等于**框中输入页面变体。 ![Klaviyo 中的段生成器中的段，适用于填写了页面变体 a 的表单的人](https://klaviyo.zendesk.com/hc/article_attachments/28711674387227)
4. 完成后单击****创建分段****。 ### 创建欢迎流程

您可以使用 Unbounce 中的数据创建一系列欢迎电子邮件，当有人在表单上输入电子邮件时会触发这些电子邮件。通过 Klaviyo 执行此操作的优点是，您可以设置两到三条消息欢迎系列，当您的潜在客户添加到电子邮件列表时触发。有关更多信息，请参阅我们的[创建欢迎系列指南](https://help.klaviyo.com/hc/en-us/articles/115002775172)。 ## 故障排除

### 表单字段未填充到我的 webhook 设置中

如果您的表单字段未出现在 Webhook 设置中，您可能需要重新发布页面以重新同步表单字段。重新发布：

1. 单击进入 Unbounce 中的页面，然后转到 **编辑** 屏幕。 2. 选择页面上的任何内容并稍作更改，然后单击****保存****。 3. 恢复更改，然后再次单击****保存****。 4. 单击****发布****（或****重新发布****，具体取决于您使用的构建器）。 5. 返回 Unbounce 帐户的 ****Webhooks**** 选项卡并再次尝试设置。您现在应该能够看到 webhook 设置中填充的表单字段。 6. 如果此问题仍然存在，请联系 [Unbounce 支持团队](https://documentation.unbounce.com/hc/en-us/articles/360029477151)。 ## 结果

您现在已将 Unbounce 与 Klaviyo 集成并查看了同步数据。 ## 其他资源

- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [创建细分指南](https://help.klaviyo.com/hc/en-us/articles/115005237908)