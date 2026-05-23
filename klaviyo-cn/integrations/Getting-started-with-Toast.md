---
id: "24302505547163"
title: "开始使用吐司"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/24302505547163-Getting-started-with-Toast"
section: "Toast"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-08T13:45:24Z"
language: "zh"
---
## 你将会学到

了解如何将 Klaviyo 与 Toast 集成，这是一种帮助餐厅无缝、安全地接受付款的工具。 Klaviyo 同步来自 Toast 的订单事件，这使您可以个性化向客户发送的消息。当提供客人标识符时，Klaviyo 会同步来自 Toast 的在线订单和离线订单，包括为 Toast 表启用“在 POS 上开始订购”时列入候补名单的客人订单。 ## 在 Toast 中添加 Klaviyo 集成

在 Klaviyo 中执行操作之前，首先在 Toast 中添加集成。 1. 登录您的 Toast 帐户。 2. 按照 Toast 的指南[如何设置 Toast Partner Connect](https://central.toasttab.com/s/article/Toast-Partner-Connect-Setting-Up-Integrations-with-Toast)。 3. 搜索并添加 **Klaviyo** 集成。请参阅 Toast 指南了解更多关于[如何添加或删除集成](https://central.toasttab.com/s/article/Adding-or-Removing-an-Integration-with-Toast-Partner-Connect)。 4. 如果您有多个地点，请导航至 ****报告**** > ****设置**** > ****数据导出**** 并导出您的[餐厅 ID 映射](https://www.toasttab.com/restaurants/admin/export/restaurantidmapping)，收集每个餐厅的 ID。 ## 在 Klaviyo 中添加 Toast 集成

1. 在 Klaviyo 中，选择 ****集成**** ****> 探索应用程序****。 2. 搜索**Toast**，然后单击该卡。然后，单击****安装****。 3. 在设置页面上，输入您在上一部分中获得的餐厅 ID。如果您要连接多个餐厅，请输入多个餐厅 ID 作为逗号分隔列表（例如 a1b2-c3d4、e1f2-g3h4）。 ![](https://klaviyo.zendesk.com/hc/article_attachments/45709956500379)
4. 单击****连接****。 ## 了解您的 Toast 数据

Klaviyo 从 Toast 同步许多不同的订单放置和履行相关事件。当提供客人标识符时，Klaviyo 会同步来自 Toast 的在线订单和离线订单，包括为 Toast 表启用“在 POS 上开始订购”时列入候补名单的客人订单。 Klaviyo 同步 Toast 3 年的历史数据。 Toast 不会与 Klaviyo 同步电子邮件和短信同意，但 Toast 集成可以将数据添加到已通过其他来源提供同意的配置文件中。通常建议[通过 CSV 上传手动导入同意](https://help.klaviyo.com/hc/en-us/articles/360043841811)。要查看您的 Toast 数据：

1. 导航至****分析 > 指标。****
   在这里，您可以查看帐户中的所有指标。带有 Toast 图标的指标代表从 Toast 集成同步的所有指标。 2. 在 **搜索指标** 字段中搜索“Toast”集成，或使用 **所有集成** 下拉列表查找它并筛选您的视图。 ![指标屏幕显示搜索栏、“Toast”过滤器和订单指标列表：已履行订单、已订购产品、已下订单、已准备订单和已退款订购。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/3ca74e49bf07b000f15b96481b8fd6f90e4f4838-437x453.png)

详细了解您的 [Toast 数据](https://help.klaviyo.com/hc/en-us/articles/24302613403931)。 ## 使用 Toast 数据细分客户

您可以使用 Toast 的指标来细分客户并针对他们开展营销活动。例如，您可以为过去 30 天内下过订单的每个人创建一个细分，并向该细分发送营销活动，以通知他们有关促销活动或优惠的信息。要创建示例段：

1. 导航至****受众 > 列表和细分****。 2. 单击****新建****并选择****新建**** ****段****。 3. 为您的分段命名并根据需要选择标签。 4. 在 **定义** 下，选择 ****某人已完成（或未完成）的操作**** > ****已下订单**** > ****至少一次**** > ****最近**** > ****30**** > ****天****。 5. 单击****创建分段****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720660479771)

## 在流中使用 Toast 数据

您可以使用 Toast 指标来触发流。例如，您可以使用 **已下订单** 指标来触发流程，以便在某人下订单时立即向其发送消息。要使用 Toast 指标创建流：

1. 导航至****流****。 2. 单击右上角的****创建流程****。 3. 单击右上角的****从头开始创建****。 4. 为流程命名并根据需要选择标签。 5. 单击****创建流****。 6. 在流程构建器中，在触发器侧栏中选择 ****您的**** ****指标 > Toast****。 7. 从列表中选择一个 Toast 指标，例如 **已下订单**。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720660481563)
8. 单击****保存 > 确认并保存****。 9. 添加与触发操作相关的任何时间延迟和消息。详细了解[创建购买后流程](https://help.klaviyo.com/hc/en-us/articles/360028872611)。 10. 内容准备好后，单击流程构建器右上角的****查看并打开****或****更新操作状态****以将流程设置为活动状态。 ## 结果

现在，您已将 Toast 与 Klaviyo 集成，并了解了 Klaviyo 中的 Toast 数据、使用 Toast 数据对客户进行细分以及在流中使用 Toast 数据。 ## 添加额外的餐厅地点

如果您在初始集成后扩展业务或向 Toast 帐户添加新地点，则可以将这些餐厅 ID 添加到集成设置中，以确保这些特定地点的数据流。要添加新位置：

1. ****在 Toast 中****，确保新位置已获得 Klaviyo 集成授权。有关在 Toast 平台内管理位置的具体步骤，请参阅 Toast 关于[如何添加或删除集成]的指南(https://central.toasttab.com/s/article/Adding-or-Removing-an-Integration-with-Toast-Partner-Connect)。 2.****在 Klaviyo**** 中，单击左侧导航菜单中的****集成****。 3. 从已启用的集成列表中选择 ****Toast**** 以打开设置页面。 4. 找到 **餐厅 ID** 部分，然后单击 ****添加****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/46509585937691)
5. 输入您要添加的 Toast 餐厅 ID。如果一次添加多个 ID，请用逗号分隔它们（例如，a1b2-c3d4、e1f2-g3h4）。 6. 单击****添加****。 7. 屏幕底部将出现有关未保存更改的通知。单击****保存****完成更新。保存后，Klaviyo 将开始同步新位置的数据。这些新餐厅 ID 的历史数据可能需要很短的时间才能填充到您的 Klaviyo 帐户中。