---
id: "37673288455323"
title: "开始使用 Guesty"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/37673288455323-Getting-started-with-Guesty"
section: "Guesty"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-20T17:29:57Z"
language: "zh"
---
了解如何将 Klaviyo 与短期租赁物业管理平台 Guesty 集成。 Klaviyo 同步来自 Guesty 的宾客、预订和消息，让您可以个性化向宾客发送的消息。 ## 将 Klaviyo 与 Guesty 集成

首先，您需要从 Guesty 获取 API 密钥：

1. 登录您的 Guesty 管理员。 2. 选择****集成 > 市场****。 3. 搜索 **Klaviyo**，然后选择 Klaviyo 列表。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043405531035)
4. 单击****连接****。 5. 复制新生成的Guesty API Key。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390294299)

   然后，您需要在 Klaviyo 中设置集成：
6. 登录 Klaviyo。 7. 选择****集成****选项卡。 8. 单击****探索应用程序****。 9. 搜索 **Guesty** 并选择该卡。 10. 单击****安装****。 11. 将您复制的 Guesty API 密钥粘贴到框中。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390298011)
12. 单击****连接****。 13. 检查 Klaviyo 中的权限并单击****允许****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390299931)
14. 在下一页上，选中复选框**将您的 Guesty 电子邮件订阅者同步到 Klaviyo**（如果您愿意）。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043405546139)
15. 如果您选择了上述设置，请从下拉列表中选择要添加 Guesty 电子邮件订阅者的列表。确保此列表设置为[单一选择加入](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT)，以避免触发从 Guesty 同步的向访客发送选择加入电子邮件。 16. 完成后，单击****完成设置****。 17. 您将收到一条成功消息，确认您的 Guesty 集成现已连接。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390305819)

## 更新您的 Guesty 集成

要更新您的集成：

1. 登录 Klaviyo。 2. 选择****集成****选项卡。 3. 单击****来宾.****
4. 单击横幅中的****更新****按钮。 ![屏幕截图 2026-01-30 下午 4.27.40.png](https://klaviyo.zendesk.com/hc/article_attachments/46089570265499)
5. 单击****连接****。 6. 检查 Klaviyo 中的权限并单击****允许****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390299931)
7. 在下一页上，选中复选框**将您的 Guesty 电子邮件订阅者同步到 Klaviyo**（如果您愿意）。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043405546139)
8. 如果您选择了上述设置，请从下拉列表中选择要添加 Guesty 电子邮件订阅者的列表。确保此列表设置为[单一选择加入](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT)，以避免触发从 Guesty 同步的向访客发送选择加入电子邮件。 9. 完成后，单击****完成设置****。 10. 您将收到一条成功消息，确认您的 Guesty 集成现已连接。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390305819)

## 添加现场跟踪

如果您使用的是 Guesty 的预订引擎，则可以通过安装自定义代码片段将 Klaviyo 现场跟踪添加到您的网站。此代码段还允许在您的网站上使用 [Klaviyo forms](https://help.klaviyo.com/hc/en-us/articles/360026474752)。要在您的网站上安装代码：

1. 在 Klaviyo 中，在左下角选择您的帐户名。 2. 选择****设置****。 3. 单击****API 密钥****。 4. 复制您的公共 API 密钥。 1. 登录Guesty。 2. 选择顶部的****操作****下拉列表，然后选择****增长 > 分布****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/49254970231323)
3. 选择****宾客预订引擎****。 4. 单击预订引擎旁边的三个点，然后选择****编辑预订引擎****。 5. 滚动到 **自定义代码片段** 部分，并确保****打开自定义代码片段**** 已打开。 6. 从 Github 复制 [GuestyEvents 代码](https://gist.github.com/cbarley10/64ebafb5c8043ef5b2c8cb61145d9f5e) 并将其粘贴到自定义代码片段框中。 ![](https://klaviyo.zendesk.com/hc/article_attachments/49254970233115)
7. 在代码片段中，将 COMPANY\_ID 替换为您的 Klaviyo 公共 API 密钥。要查找您的 Klaviyo 公共 API 密钥：
8. 单击****下一步****，直到到达编辑器的最后一步。 9. 选择****保存预订引擎。****

您现在已经为 Guesty 安装了现场跟踪。 此代码跟踪[已知浏览器](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACVVC4BXQ0ES5Y50TC)的以下事件并将它们同步到Klaviyo：

- 现场活跃
- 查看列表
- 开始结账

## 查看您的 Guesty 数据

要查看您的 Guesty 数据：

1. 导航至****分析 > 指标****。在这里，您可以查看帐户中的所有指标。带有 Guesty 图标的指标代表从 Guesty 集成同步的所有指标。 2. 使用 **所有集成** 下拉列表并选择 **Guesty** 以仅查看 Guesty 指标。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390310043)

   要查看您的 Guesty 对象（注意：需要最新版本的集成）：
3. 导航至****内容 > 对象****。在这里，您可以查看帐户中的所有对象。带有 Guesty 图标的对象代表从 Guesty 集成同步的所有对象。了解[有关您的 Guesty 数据的更多信息](https://help.klaviyo.com/hc/en-us/articles/37673417604507)。 ## 使用 Guesty 数据对客人进行细分

您可以使用 Guesty 指标来细分客人。例如，使用指标，您可以创建已在特定位置确认预订的客人细分：

1.某人做过（或未做过）的事情 > 确认预订（客人） > 至少一次 > 一直以来
2.其中>列表标题>等于>（您的标题）
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38043390311835)

1. 导航至****受众 > 列表和细分****。 2. 单击****新建****并选择****创建新段****。 3. 为您的分段命名并根据需要选择标签。 4. 选择以下定义和过滤器：
5. 单击****创建分段****。使用对象，您可以创建一组预订开始日期从明天开始的客人：

   ![屏幕截图 2026-01-28 下午 5.38.24.png](https://klaviyo.zendesk.com/hc/article_attachments/46002390175131)
6. 导航至****受众 > 列表和细分****。 7. 单击****新建****并选择****创建新段****。 8. 为您的分段命名并根据需要选择标签。 9. 选择以下定义和过滤器：
   1. 关于某人的属性> 预订（客人）> 至少有一个
   2.其中>开始日期>接下来>5200周
10. 单击****创建分段****。 ## 在流程中使用 Guesty 数据

您可以使用 Guesty 指标来触发流程或自动化操作序列。 Klaviyo 使用 Guesty 数据提供多个预构建流程。这些流程包括预订确认、入住前流程等。要查看这些预构建的流程：

1. 在 Klaviyo 中，选择****流程****选项卡。 2. 单击****创建流程****。 3. 按 **Guesty** 过滤以查看所有 Guesty 流。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38043405558555)

您还可以使用 Guesty 对象创建流。例如，要创建到达前流程，您可以：

- 导航到流程 > ****创建流程**** > ****构建您自己的流程。****
- 为流程命名并选择标签（可选）。 - 选择 **日期属性** 触发器。 ![屏幕截图 2026-01-28 下午 5.10.42.png](https://klaviyo.zendesk.com/hc/article_attachments/46002390176155)
- 从日期属性下拉列表中选择 Guesty、Reservation：CheckInDateAndTime。 - 选择您想要开始流程的时间。 - 添加相关消息。您还可以从头开始创建自己的流程。