---
id: "23112971772699"
title: "OpenTable 入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/23112971772699-Getting-started-with-OpenTable"
section: "OpenTable"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: "zh"
---
## 你将会学到

了解如何与 OpenTable（高级餐厅实时在线预订网络）集成。 ## 开始之前

要与 OpenTable 集成，您需要将 Klaviyo 命名为第三方处理器，以便访问 Sync API，这是 OpenTable 的 API，允许我们将数据直接提取到 Klaviyo 中。 1. 请联系您的 OpenTable 客户经理，了解将 Klaviyo 命名为第三方处理器的事宜。 2. OpenTable 为您的餐厅创建 DocuSign 后，请提供以下信息：

   ****由接收者访问的 API****：同步 API
   ****收件人姓名****：Klaviyo, Inc. ****与客户的关系****：供应商/服务提供商

   ****收件人地址****
   夏季街125号10楼
   波士顿, 马萨诸塞州 02110

   ****联系方式****
   克拉维约团队
   [restaurants@klaviyo.com]（邮件至：restaurants@klaviyo.com）
   +1 800-338-1744
   （无传真）

   您还必须在 Klaviyo 中为通过 OpenTable 选择加入的任何人创建一个列表。 3. 导航至****受众**** > ****列表********和********分段****。 4. 单击右上角的****新建**** > ****创建列表****。 5. 将列表命名为使其目的显而易见的名称，例如“OpenTable Subscribers Ongoing”。 6. 单击****创建列表****。 7. 查看新列表时，选择****设置****选项卡。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723524398491)
8. 复制该列表的列表ID。稍后您将需要这个。 9. 导航至左侧的****同意****选项卡，并将列表设置为****单一选择加入****。重要的是，该列表是单一选择加入的，以防止订阅者在安装集成后收到确认电子邮件。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723524413083)

## 将 OpenTable 与 Klaviyo 集成

与 OpenTable 集成：

1. OpenTable 客户端 ID（可以在[此处](https://dev.opentable.com/partner-portal/profile/credentials) 找到）
2. OpenTable Secret ID（可以在[此处](https://dev.opentable.com/partner-portal/profile/credentials)找到）
3. Klaviyo 列表 ID（如本文**开始之前**部分所述）
4. OpenTable 餐厅 ID 和餐厅名称

1. 登录您的 OpenTable 帐户，确保下面的某些链接有效。 2. 在 Klaviyo 中，单击 ****集成 > 探索应用程序****。 3. 搜索**OpenTable**，然后单击该卡。然后，单击****安装****。 4. 在设置页面上，输入以下信息：
   1. 无论名称是什么，您都可以稍后进行过滤，因此如果您有多个位置，则应该将其放在名称中。 5. 单击****完成设置****开始集成。这将启动 OpenTable 访客和预订数据的 2 年历史同步。今后，我们将每 30 分钟定期同步一次，以提取宾客和预订数据，以便您的帐户始终保持最新状态。 ## 了解您的 OpenTable 数据

Klaviyo 同步 OpenTable 中与成员身份和 OpenTable 属性相关的不同事件。我们从 OpenTable 同步 2 年的历史数据。 Klaviyo 同步来自 OpenTable 的电子邮件地址和电子邮件同意书。请注意，只有订阅会从 OpenTable 同步，取消订阅则不会。虽然电话号码已同步，但短信同意并未同步。这意味着短信无法发送到从此集成同步的电话号码。要查看您的 OpenTable 数据：

1. 单击左侧导航侧栏中的****分析****下拉列表。 2. 选择****指标****。在这里，您可以查看帐户中的所有指标。标记为“OpenTable”的指标代表从 OpenTable 集成同步的所有指标。 3. 使用搜索栏旁边的过滤器选择器过滤此视图以查看 OpenTable 指标，然后选择 ****OpenTable****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723524415515)

详细了解您的 [OpenTable 数据](https://help.klaviyo.com/hc/en-us/articles/23113172847259)。 ## 使用 OpenTable 数据细分客户

您可以使用 OpenTable 的指标来细分客户并针对他们开展营销活动。例如，您可以创建之前完成预订的每个人的细分。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723546329499)

要创建上面所示的示例段：

1. 单击左侧导航边栏中的****受众**** 下拉列表。 2. 单击****列表和段****。 3. 单击右上角的****创建列表/细分****。 4. 选择****段****。 5. 为您的分段命名并根据需要选择标签。 6. 在“定义”下，选择 ****某人已完成（或未完成）的操作**** > ****已完成的预订**** > ****至少一次**** > ****始终****。 7. 单击****创建段****。 ### 按预订价值细分

如果您想按预订金额进行细分，则需要将 POS 连接到 OpenTable。如果您的 POS 未连接到 OpenTable，金额将不会从 OpenTable 同步到 Klaviyo。例如，如果您同时使用 OpenTable 和 Square，并将 Square 连接到 OpenTable，您将看到一个名为 **Completed Reservation Value** 的 OpenTable 事件，您可以在分段和过滤中使用该事件。请注意，此指标不会出现在 **指标** 选项卡中。 ## 在流程中使用 OpenTable 数据

您可以使用 OpenTable 指标来触发流。例如，您可以使用 **完成的预订** 指标来触发流程，以便在某人完成预订时立即向其发送消息。要使用 OpenTable 指标创建流：

1. 从左侧导航侧栏导航至****Flows**** 选项卡。 2. 单击右上角的****创建流程****。 3. 单击右上角的****从头开始创建****。 4. 为流程命名并根据需要选择标签。 5. 单击****创建流****。 6. 在流程构建器中，选择“指标”作为触发器。 7. 从侧边栏中，选择****您的指标**** > ****OpenTable**** > ****已完成的预订**** 或****所有触发器**** > ****指标**** > ****已完成的预订****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723524404251)
8. 单击****完成****。 9. 添加与触发操作相关的时间延迟和消息。详细了解[如何创建指标触发流](https://help.klaviyo.com/hc/en-us/articles/360003057151)。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723546333467)
10. 内容准备就绪后，单击流程构建器右上角的****更新操作状态****以将流程设置为活动状态。 ## 结果

现在，您已将 OpenTable 与 Klaviyo 集成，并了解了 Klaviyo 中的 OpenTable 数据、使用 OpenTable 数据细分客户以及在流程中使用 OpenTable 数据。 ## 为什么我会看到通知“您的帐户正在调用已停用的修订版”？您是否在 Klaviyo 中看到一条通知，上面写着“[需要采取行动]您的帐户正在调用已停用的修订版本”，如下所示？ ![](https://klaviyo.zendesk.com/hc/article_attachments/31085192132251)

请忽略此通知；您目前无需采取任何行动。您的 OpenTable 集成由 Klaviyo 管理，并将继续按预期工作。