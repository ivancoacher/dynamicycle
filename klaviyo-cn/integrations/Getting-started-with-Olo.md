---
id: "15751697785883"
title: "开始使用 Olo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15751697785883-Getting-started-with-Olo"
section: "Olo"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: "zh"
---
## 你将会学到

了解如何与 Olo 集成，Olo 是一种帮助餐厅在线订购的工具。 ## 开始之前

- 在 Olo 中，确认您有权访问 Olo 控制台仪表板中的开发工具。请参阅 [概述仪表板](https://olosupport.zendesk.com/hc/en-us/articles/115000076446) 上的 Olo 文档，了解最新信息。 - 确保您在单独的选项卡中登录 Klaviyo 和 Olo，以简化安装。 ## 将 Olo 与 Klaviyo 集成

### 在 Klaviyo 中安装 Olo 集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 单击****探索应用程序****。 3. 搜索 **Olo** 并选择该卡。 4. 在下一页上，单击****安装****。 5. 在下一页上，单击****连接到 Olo。****
6. 检查权限并单击****允许****。 7. 复制为您生成的 Webhook URL 并将其保存到安全位置。 ![](https://klaviyo.zendesk.com/hc/article_attachments/41573712736411)

### 在 Olo 中配置 webhook

1. 在 Olo 中，选择左侧导航栏中的****开发工具 > Webhooks****。 2. 单击右上角的****添加 Webhook****。 ![Olo 中的“添加 Webhook”按钮。](https://klaviyo.zendesk.com/hc/article_attachments/28716056424091)
3. 填写表格以下内容：
   1. 选择所有**订单事件**和**用户事件**。 1. Webhook 名称：Klaviyo。 2. 目标 URL：您在安装****Olo 集成到 Klaviyo 部分****的步骤 7 中复制的 URL。 3. 开发合作伙伴：Klaviyo（从下拉列表中选择）。 4. 事件类型。 4. 单击****发布 Webhook****。 ### 完成 Klaviyo 中的安装

1. 检查设置以将 Olo 电子邮件订阅者同步到 Klaviyo。然后，从下拉列表中选择您的主电子邮件列表（或其他列表，如果需要）。我们建议将此列表设置为[单一选择](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT)。 ![](https://klaviyo.zendesk.com/hc/article_attachments/41574255868827)
2. 检查将 Olo SMS 订阅者同步到 Klaviyo 的设置。然后，从下拉列表中选择您的主短信列表（或其他列表，如果需要）。 ![](https://klaviyo.zendesk.com/hc/article_attachments/41574280135835)
3. 单击****完成设置****。您的集成现已激活，个人资料、事件和同意更新将开始同步到 Klaviyo。 ## 了解您的 Olo 数据

Klaviyo 从 Olo 同步许多与约会和会员资格相关的不同事件。要查看您的 Olo 数据：

1. 单击左侧导航侧栏中的****分析****下拉列表。 2. 选择****指标****。在这里，您可以查看帐户中的所有指标。带有 Olo 图标的指标代表从 Olo 集成同步的所有指标。 3. 使用搜索栏旁边的过滤器选择器过滤此视图以仅查看 Olo 指标。 ![Klaviyo 中找到的 Olo 指标列表。](https://klaviyo.zendesk.com/hc/article_attachments/28716066864155)

第三方配送（Uber Eats、DoorDash 等）从 Olo 同步到 Klaviyo，您可以在 Klaviyo 中查看它们，以帮助了解您的订单来源。不过，这些配置文件会自动被抑制，因此不会被视为 Klaviyo 计费的活动配置文件。详细了解[您的 Olo 数据](https://help.klaviyo.com/hc/en-us/articles/15752146245403)。 ## 使用 Olo 数据细分客户

您可以使用 Olo 的指标来细分客户并针对他们开展营销活动。例如，您可以创建过去 30 天内下过订单的每个人的细分并向该细分发送营销活动。 ![使用 Olo 指标的示例片段。](https://klaviyo.zendesk.com/hc/article_attachments/28716056427803)

要创建上面所示的示例段：

1. 单击左侧导航边栏中的****受众**** 下拉列表。 2. 单击****列表和分段****。 3. 单击右上角的****新建****。 4. 选择****创建分段****。 5. 为您的分段命名并根据需要选择标签。 6. 在 **定义** 下，选择 ****某人已完成（或未完成）的操作**** > ****已下订单**** > ****至少一次**** > ****最近**** > ****30**** > ****天****。 7. 单击****创建分段****。 ## 在流中使用 Olo 数据

您可以使用 Olo 指标来触发流。例如，您可以使用 **已下订单** 指标来触发流程，以便在某人下订单时立即向其发送消息。要使用 Olo 指标创建流：

1. 从左侧导航侧栏导航至****Flows**** 选项卡。 2. 单击右上角的****创建流程****。 3. 单击右上角的****构建您自己的****。 4. 为流程命名并根据需要选择标签。 5. 单击****创建流****。 6. 在流程构建器中，选择****已下订单****作为触发器。 ![流程生成器，您可以在其中选择触发事件](https://klaviyo.zendesk.com/hc/article_attachments/34594327249051)
7. 检查触发器是否设置为从 Olo 同步。 8. 单击****保存****。 9. 添加与触发操作相关的时间延迟和消息。详细了解[创建购买后流程](https://help.klaviyo.com/hc/en-us/articles/360028872611)。 10. 内容准备好后，单击流程构建器右上角的****更新状态****以将流程设置为活动状态。 ## 结果

现在，您已将 Olo 与 Klaviyo 集成，并了解了 Klaviyo 中的 Olo 数据、使用 Olo 数据细分客户以及在流程中使用 Olo 数据。 ## 其他资源

参加我们的[增强餐厅宾客关系]课程(https://academy.klaviyo.com/en-us/courses/enhance-restaurant-guest-relationships)。了解有关 [Klaviyo 构建的集成](https://help.klaviyo.com/hc/en-us/articles/115000256472) 的更多信息。了解[集成同步数据的频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)。