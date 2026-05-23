---
id: "115005254868"
title: "如何与Wufoo集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254868-How-to-integrate-with-Wufoo"
section: "Wufoo"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "zh"
---
## 你将会学到

了解如何将 Wufoo 与 Klaviyo 集成，以便创建自动化流消息、个性化营销活动以及根据 Wufoo 的数据对列表进行细分。 Wufoo 允许您快速创建调查、邀请和联系表单，以从客户那里收集所需的数据。 Klaviyo 从 Wufoo 同步以下数据：

- 当有人填写表格时
- 用户填写的表格名称
- 从表单字段收集的数据

## 开始之前

在与 Wufoo 集成之前，请务必注意以下几点：

- 所有表单必须有一个字段来收集客户的电子邮件地址，以便 Klaviyo 跟踪表单提交情况。如果表单中没有电子邮件字段，或者有多个电子邮件字段，Klaviyo 可能不会同步表单结果。 - 如果您付费订阅了他们的服务，Wufoo 仅支持从其表单中提取信息的功能。在尝试与 Klaviyo 同步之前，请确保解决所有付款问题。 - 当您将表单配置为子字段时，Klaviyo 无法识别姓氏字段。相反，请使用 1 以下方法来记录客户的姓氏：
  - 创建单个姓名字段（包括订阅者的名字和姓氏）：Klaviyo 将自动在第一个空格上分割，为订阅者创建名字和姓氏。 - 创建 2 个单独的字段：如果您创建名字字段和姓氏字段，Klaviyo 将分别同步这两个字段。 ## 将 Wufoo 与 Klaviyo 集成

您需要 Wufoo 站点 URL 和 Wufoo API 密钥才能与 Klaviyo 集成

1. 导航到 Wufoo 中的 **表单** 选项卡。 2. 单击您想要连接到 Klaviyo 的表单右侧的三点菜单。 ![Wufoo 中的“表格”选项卡显示鲜花订购表格并创建蓝色背景的新表格](https://klaviyo.zendesk.com/hc/article_attachments/28705636351771)
3. 从下拉列表中选择****API 信息****。 ![Wufoo 下拉列表以灰色突出显示表单规则、通知、集成、分析和 API 信息](https://klaviyo.zendesk.com/hc/article_attachments/28705663083803)
4. 从 **API 信息** 页面复制 API 密钥。 ![API 信息 Wufoo，API 密钥模糊，重置按钮为红色](https://klaviyo.zendesk.com/hc/article_attachments/28705636355483)

   此 API 密钥是私有 API 密钥。将 API 私钥视为密码；将它们保存在安全的地方，切勿将其暴露给公众。 5. 登录 Klaviyo，选择****集成****选项卡。 6. 单击****探索应用程序****，搜索**Wufoo**，然后单击该卡。 7. 然后，单击****安装****。 8. 输入完整的商店网址，包括“.wufoo.com”、“.wufoo.co.uk”、“.wufoo.eu”等！[](https://klaviyo.zendesk.com/hc/article_attachments/28705636370459)
9. 输入您之前复制的 API 密钥。 10. 单击****连接到 Wufoo****。 11. 在下一页上，您可以指定高级条件：
    - **仅同步特定表单**：如果您只想同步某些 Wufoo 表单，请选择此选项。 - **指定应包含复选框字段的表单**：如果您的表单带有复选框，请确保使用此选项将数据正确导入到 Klaviyo 中。 12. 如果您选中了相应的框，则需要提供您想要与 Klaviyo 同步的表单哈希值的逗号分隔列表；您可以在该表单的 ****Code**** 页面上找到该表单的哈希代码。 ![Klaviyo 中的 Wufoo 集成设置页面显示选中的设置仅同步特定表单和指定应包含复选框字段的表单](https://klaviyo.zendesk.com/hc/article_attachments/28705636364699)
13. 您还可以选中 **将 Wufoo 受访者添加到 Klaviyo 列表**，然后通过提供 **表单代码** 和 6 个字符的 Klaviyo 列表 ID 来指定您的 Wufoo 表单数据将同步到哪个 Klaviyo 列表。 ![Klaviyo 中的 Wufoo 集成设置页面显示表单代码、电子邮件字段和添加到 Klaviyo 列表并删除（蓝色）的设置](https://klaviyo.zendesk.com/hc/article_attachments/28705636361755)
    - 要查找表单代码，请返回表单的 ****API 信息**** 并复制表单 **Hash.**![Wufoo 中表单的 API 信息，显示多个 API ID 字段及其各自的标题，包括用红色框包围的模糊的哈希](https://klaviyo.zendesk.com/hc/article_attachments/28705636367643)
    - 要查找 Klaviyo 列表 ID，请单击 Klaviyo 中的****受众****下拉列表，然后选择****列表和细分****选项卡，单击要添加 Wufoo 数据的列表，然后单击****设置****。然后，从 **列表 ID 和名称** 部分复制列表 ID。 14. 添加所需的任何特定集成设置后，单击****完成设置****。 ## 监控 Wufoo 同步

当您与 Wufoo 集成时，所有可用的历史数据将在几分钟内开始同步到 Klaviyo。要检查您的集成：

1. 导航至****分析 > 指标****。 2. 按 **Wufoo.** 过滤
3. 选择 **填写的表单** 指标，然后单击****活动源**** 以查看同步数据。 4. 如果您的集成已开始同步数据，您将开始看到添加到此活动源的 **填写表单** 事件以及 Wufoo 图标。然后，Klaviyo 每小时从 Wufoo 同步一次数据。同步完成后，您将在 ****Integrations**** 选项卡中看到 Wufoo 集成周围有一个绿色边框。目前，Klaviyo 仅从 Wufoo 同步 1 个指标：**填写的表格**。该指标记录以下所有信息：

- 谁填写了表格
- 当此人填写时
- 填写的表格名称

通过表单字段收集的所有数据都将附加到 Klaviyo 中每个订阅者的个人资料中的**自定义属性**下。 ## 结果

您已完成 Wufoo 与 Klaviyo 的集成并验证了您的同步数据。现在，您可以创建自动流消息、个性化营销活动，并根据从 Wufoo 同步的数据对列表进行细分。您甚至可以创建[一系列欢迎消息](https://help.klaviyo.com/hc/en-us/articles/115002775172)，当有人提交表单时会触发这些消息。 ## 其他资源

- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [如何增强您的发送声誉](https://help.klaviyo.com/hc/en-us/articles/115005250368)
- [Klaviyo 和应用程序之间交换的信息类型参考](https://help.klaviyo.com/hc/en-us/articles/360030696012)