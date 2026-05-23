---
id: "115005254968"
title: "如何与 Campaign Monitor 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254968-How-to-integrate-with-Campaign-Monitor"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "zh"
---
## 你将会学到

了解如何将 Campaign Monitor 与 Klaviyo 集成，以便同步您的 Campaign Monitor 列表和联系人并跟踪 Klaviyo 中的 Campaign Monitor 分析。 Klaviyo 从 Campaign Monitor 同步以下数据：

- 活动监控联系人
- 来自 Campaign Monitor 的接收、点击和打开指标
- 活动监控列表（部分或全部，取决于您的偏好）

## 添加营销活动监控集成

1. 首先，您需要在 Campaign Monitor 帐户中找到您的 API 密钥。在 Campaign Monitor 帐户的 **帐户设置** 页面中，点击****API 密钥****。 2. 单击****显示 API 密钥**** 并复制该值。 ![Campaign Monitor 中的管理 API 密钥页面，API 密钥和客户端 ID 已模糊](https://klaviyo.zendesk.com/hc/article_attachments/28715962541211)
3. 在您的 Klaviyo 帐户中，选择****集成****选项卡，然后单击 ****探索应用程序。****
4. 搜索 **Campaign Monitor**，然后单击该卡。 5. 单击****安装****。 6. 在下一页上，添加您的 Campaign Monitor API 密钥并单击****连接到 Campaign Monitor****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28715962550683)
7. 在下一页上，您可以在**高级**下配置以下集成设置：
   - ****收集 Campaign Monitor 活动的打开和点击数据****
     选择此设置将同步您的 Campaign Monitor 营销活动中的打开数据和点击数据。 - ****从 Campaign Monitor 列表创建 Klaviyo 列表****
     选择此设置将从您的营销活动监视器列表中创建相应的 Klaviyo 列表。 - ****仅为特定营销活动监控列表创建 Klaviyo 列表****
     选择此设置将允许您指定应使用哪些营销活动监视器列表来创建相应的 Klaviyo 列表。系统将提示您添加以逗号分隔的营销活动监控列表 ID 列表。请注意，即使您选择此设置，所有收到、打开或单击电子邮件的 Campaign Monitor 联系人也会同步到 Klaviyo。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32010057312027)
8. 完成后单击****完成设置****。完成设置后，数据将在几分钟内开始同步到 Klaviyo。 Klaviyo 运行历史同步并设置定期同步以提取新数据。 Klaviyo 从 Campaign Monitor 接收过去 90 天的历史参与度数据。新数据每小时同步到 Klaviyo。 ## Klaviyo 中的活动监控数据

当您的集成同步时，您应该开始看到来自 Campaign Monitor 活动的数据填充。一旦 Campaign Monitor 集成出现在您的 **启用的集成** 列表中并且旁边有绿色边框，您的集成就已完全同步。要在 Klaviyo 中查看营销活动监视器数据，请单击****分析****下拉列表并选择****指标****。在这里，您可以按**营销活动监视器**进行过滤。点击****收到的电子邮件（营销活动监控）**** 指标。 ![Klaviyo 中的“指标”选项卡显示营销活动监控指标列表](https://klaviyo.zendesk.com/hc/article_attachments/28715969163291)

## 最佳实践

为了确保保持良好的送达率，您应该仅将前几封电子邮件营销活动发送到营销活动监视器中列表中参与的部分。由于您将拥有来自 Campaign Monitor 的打开和点击数据，因此您将能够使用它来细分您的列表。您还应该包含来自 Klaviyo 的打开和点击数据，因为这将添加未来与您的 Klaviyo 电子邮件进行交互的活跃用户。最后，请务必添加限制向已添加到主列表中的客户发送邮件的条件。这将确保您的电子邮件针对已选择接收消息（通过加入您的列表）的客户。使用以下条件构建您的参与细分市场。下面的打开和点击条件的期限为 30 天。如果您发送电子邮件的频率较低，则可以将这些时间范围放宽至 60 甚至 90 天。每当增加参与窗口时，请务必监控您的交付能力。如果您发现打开率和点击率下降，请通过将时间范围缩短至 30 天来收紧参与标准。 创建段：

- 名称：参与部分
- 如果某人在或不在列表中 > 此人 > 在电子邮件列表中
- 以及某些人已完成（或未完成）> 打开电子邮件（营销活动监控）> 至少一次 > 在过去 > 30 > 天内
- 或某些人已完成（或未完成）> 点击电子邮件（营销活动监控）> 至少一次 > 在过去 > 30 > 天内
- 或某些人已经做过（或未做过）的事情 > 打开电子邮件 (Klaviyo) > 至少一次 > 在过去 > 30 > 天内
- 或某些人已完成（或未完成）> 单击电子邮件 (Klaviyo) > 至少一次 > 在过去 > 30 > 天内
- 或如果某人在或不在列表中 > 此人 > 在电子邮件列表中 > 并且是在过去 > 7 > 天内添加的

![Klaviyo 细分生成器，具有用于营销活动监视器的参与细分定义，创建带有蓝色背景的细分按钮](https://klaviyo.zendesk.com/hc/article_attachments/28715969152539)

## 结果

您现在已将 Campaign Monitor 与 Klaviyo 集成，以便跟踪分析并将列表和联系人同步到 Klaviyo。 ## 其他资源

- [如何从其他电子邮件服务提供商迁移到 Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005082767)
- [分段入门](https://help.klaviyo.com/hc/en-us/articles/115005237908)