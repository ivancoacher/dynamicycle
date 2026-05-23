---
id: "24206444868251"
title: "开始使用 ChowNow"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/24206444868251-Getting-started-with-ChowNow"
section: "ChowNow"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:35Z"
language: "zh"
---
了解如何与在线订购平台 ChowNow 集成。 Klaviyo 与 ChowNow 的集成将订单事件以及相关配置文件引入 Klaviyo。 ## 将 ChowNow 与 Klaviyo 集成

1. 登录您的 Klaviyo 帐户。 2. 在左下角选择您的帐户名，然后单击****集成****。 3. 单击****探索应用程序****。 4. 搜索 **ChowNow** 并选择该卡。 5. 单击****安装****。 6. 单击****连接到 ChowNow****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37404916279963)
7. 检查 Klaviyo 中的权限并单击****允许****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37404893963291)
8. 如果出现提示，请登录 ChowNow。 9. 检查 ChowNow 中的权限并单击****授权****。您将被重定向到 Klaviyo 并且应该看到一条成功消息。您现在已将 ChowNow 与 Klaviyo 集成。 ## Klaviyo 中的 ChowNow 数据

ChowNow 的历史同步可追溯到 2 年前。以后的定期同步每 5 分钟发生一次。 Klaviyo 从 ChowNow 同步 3 个订单事件：

- 已接受订单
- 已下订单
- 取消订单

  Klaviyo 会从 ChowNow 同步以下与订单事件关联的配置文件数据：
- ChowNow ID
- 名字
- 姓氏
- 电话号码

要查看您的 ChowNow 数据：

1. 单击左侧导航侧栏中的****分析****下拉列表。 2. 选择****指标****。在这里，您可以查看帐户中的所有指标。 3. 按顶部的 **ChowNow** 进行过滤，以查看所有 ChowNow 指标。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37404893964699)

详细了解您的 [Klaviyo 中的 ChowNow 数据](https://help.klaviyo.com/hc/en-us/articles/24206475048219)。 ## 电子邮件同意

Klaviyo 目前不同步电子邮件地址和 ChowNow 的同意。 ## 短信同意

虽然电话号码已同步，但短信同意并未同步。这意味着未经单独收集同意，无法将短信发送到从此集成同步的电话号码。 ## 用例

Klaviyo 目前不同步电子邮件地址和 ChowNow 的同意。如果您从不同来源（例如 [POS 系统](https://help.klaviyo.com/hc/en-us/articles/11117215837211)）收集了有关个人资料的电子邮件同意，您可以使用 ChowNow 数据个性化向该客户发送的消息。您可以通过以下一些高级方法将 ChowNow 数据用于 Klaviyo：

- ****交易消息****
  通过 Klaviyo 流程发送订单确认更新。详细了解 [Klaviyo 交易电子邮件](https://help.klaviyo.com/hc/en-us/articles/360003165732)。 - ****营销信息****
  根据订购偏好（例如堂食与外卖）创建营销活动，以交叉推广不同渠道。跟踪首次光临的客人，以推动第二次光临或订购，或根据食物偏好或更新的菜单项制定针对特定食物的促销活动。 - ****报告****
  了解有关流行菜品的菜单见解，并利用这些见解来预测库存。为了实现交易或营销消息传递，您需要对客户进行细分并通过活动吸引他们，或通过 Klaviyo 流吸引他们。下面，我们将解释如何做到这一点。 ## 使用 ChowNow 数据细分客户

您可以使用 ChowNow 指标来细分客户并针对他们开展活动。例如，您可以创建之前下过订单的每个人的细分。要创建此段：

1. 单击左侧导航边栏中的****受众**** 下拉列表。 2. 单击****列表和段****。 3. 单击右上角的****创建列表/细分****。 4. 选择****段****。 5. 为您的分段命名并根据需要选择标签。 6. 在 **定义** 下，选择 **某人已完成（或未完成）的操作** > **已下订单** > **至少一次** > **一直以来**。 7. 单击****创建段****。 ## 在流中使用 ChowNow 数据

您可以使用 ChowNow 指标来触发流。例如，您可以使用 **已下订单** 指标来触发流程，以便在某人下订单时立即向其发送消息。要使用 ChowNow 指标创建流：

1. 从左侧导航侧栏导航至****Flows**** 选项卡。 2. 单击右上角的****创建流程****。 3. 单击右上角的****从头开始创建****。 4. 为流程命名并根据需要选择标签。 5. 单击****创建流****。 6. 在流程构建器中，选择****Metric**** 作为触发器。 7. 从侧边栏中，选择 ****您的指标 > ChowNow > 已下订单****。 8. 单击****完成****。 9. 添加与触发操作相关的时间延迟和消息。详细了解[如何创建指标触发流](https://help.klaviyo.com/hc/en-us/articles/360003057151)。 10. 内容准备就绪后，单击流程构建器右上角的****更新操作状态****以将流程设置为活动状态。 ## 结果

您现在已将 ChowNow 与 Klaviyo 集成，并了解了如何在 Klaviyo 消息传递中使用 ChowNow 数据。