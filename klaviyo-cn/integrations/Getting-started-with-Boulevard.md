---
id: "16131320434459"
title: "开始使用大道"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16131320434459-Getting-started-with-Boulevard"
section: "Boulevard"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: "zh"
---
了解如何与 Boulevard 集成，这是一款帮助沙龙和水疗品牌进行预订、日程安排、营销、付款、报告等的工具。 ## 开始之前

在开始之前，请确认您有权访问 Boulevard API。此集成依赖于 Boulevard Webhooks 和 API，这需要订阅 Boulevard API 包。如果您不确定是否有此包裹，请联系您的 Boulevard CSM 进行确认。 ## 将 Boulevard 与 Klaviyo 整合

要将 Boulevard 与 Klaviyo 集成：

- 从这些订户的下拉列表中选择 Klaviyo 列表。 - 从这些订户的下拉列表中选择 Klaviyo 列表。我们建议为电子邮件和短信保留单独的列表。 1. 在 Boulevard 控制台中，导航至****管理业务 > 应用程序和集成****。 2. 滚动到**自定义应用程序**并单击****安装****。 3. 输入 Klaviyo 应用程序 ID：

   ````
   0d2168f5-934c-4586-85b0-03ef0f5c54be
   ````
4. 在 Klaviyo 中，选择****集成****选项卡。 5. 单击****探索应用程序****，然后搜索 **Boulevard** 并选择该卡。 6. 在下一页上，单击****安装****。 7. 输入您的 Boulevard 公司 ID，然后单击****连接****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37276456067483)
8. 检查权限并单击****允许****。 9. 在下一页上，选中复选框 **将 Boulevard 电子邮件订阅者同步到 Klaviyo**。 10. 选中复选框**将 Boulevard SMS 订阅者同步到 Klaviyo**。 11. 完成后，单击****保存****。您现在已将 Boulevard 与 Klaviyo 集成。 ## 了解您的 Boulevard 数据

Klaviyo 同步 Boulevard 中与约会和会员资格相关的许多不同活动。当您集成时，我们会同步 Boulevard 中存储的所有历史数据，然后实时同步正在进行的数据。要在 Klaviyo 中查看 Boulevard 数据：

1. 单击左侧导航侧栏中的****分析****下拉列表。 2. 选择****指标****。在这里，您可以查看帐户中的所有指标。带有 Boulevard 图标的指标代表从 Boulevard 集成同步的所有指标。 3. 使用搜索栏旁边的过滤器选择器过滤此视图以仅查看 Boulevard 指标。 ![在 Klaviyo 的“指标”页面上找到的 Boulevard 指标列表。](https://klaviyo.zendesk.com/hc/article_attachments/28720671545755)

详细了解[您的 Boulevard 数据](https://klaviyo.zendesk.com/hc/en-us/articles/16130796656667)。 ## 使用 Boulevard 数据细分客户

您可以使用 Boulevard 的指标来细分客户并针对他们开展营销活动。例如，您可以创建过去 30 天内完成约会的每个人的细分并向该细分发送营销活动。 ![检查某人在过去 30 天内是否完成约会的示例片段。](https://klaviyo.zendesk.com/hc/article_attachments/28720659737371)

要创建上面所示的示例段：

1. 单击左侧导航边栏中的****受众**** 下拉列表。 2. 单击****列表和段****。 3. 单击右上角的****创建列表/细分****。 4. 选择****段****。 5. 为您的分段命名并根据需要选择标签。 6. 在 **定义** 下，选择 ****某人已完成（或未完成）的操作**** > ****已完成的约会**** > ****至少一次**** > ****过去**** > ****30**** > ****天****。如果您有多个集成，请确保选择带有 Boulevard 徽标的 **已完成约会** 指标。 7. 单击****创建段****。在此示例中，如果您想确保该细分仅包含首次完成预约的人员：
8. 单击****AND**** 添加新的排除条件。 9. 添加条件 ****某人已完成（或未完成）的操作**** > ****已完成的约会**** > ****等于**** > ****1**** > ****一直以来****。这将排除多次完成预约的任何人。 ![检查某人是否一直只完成一次约会的示例片段。](https://klaviyo.zendesk.com/hc/article_attachments/28720671540507)

## 在流中使用 Boulevard 数据

您可以使用 Boulevard 指标来触发流量。例如，使用 **完成的约会** 指标来触发流程，以便在某人完成约会时立即向其发送消息。如果您使用 Boulevard 发送电子邮件和短信通知，请确保关闭您希望通过 Klaviyo 流发送的消息，以便您的客户不会收到重复的消息。 有关如何禁用电子邮件和短信通知的更多信息，请参阅 [Boulevard 的支持文档](https://support.boulevard.io/)。要使用 Boulevard 指标创建流：

1. 从左侧导航侧栏导航至****Flows**** 选项卡。 2. 单击右上角的****创建流程****。 3. 单击右上角的****从头开始创建****。 4. 为流程命名并根据需要选择标签。 5. 单击****创建流****。 6. 在流程构建器中，选择****Metric**** 作为触发器。 7. 从下拉列表中，选择 Boulevard 指标，例如****已完成的约会****，由 Boulevard 图标指示。 ![选择“完成的约会”指标作为流程构建器左侧边栏中的触发器。](https://klaviyo.zendesk.com/hc/article_attachments/28720671552539)
8. 单击****完成****。 9. 添加与触发操作相关的消息，例如感谢消息。 ![使用“已完成预约”指标作为触发器的示例流程。](https://klaviyo.zendesk.com/hc/article_attachments/28720671554203)
10. 内容准备就绪后，单击流程构建器右上角的****更新操作状态****以将流程设置为活动状态。 ## 结果

现在，您已将 Boulevard 与 Klaviyo 集成，并了解了 Klaviyo 中的 Boulevard 数据、使用 Boulevard 数据对客户进行细分以及在流中使用 Boulevard 数据。