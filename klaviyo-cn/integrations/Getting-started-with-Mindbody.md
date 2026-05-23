---
id: "15348624462747"
title: "开始使用 Mindbody"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15348624462747-Getting-started-with-Mindbody"
section: "Mindbody"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: "zh"
---
## 你将会学到

了解如何与 Mindbody 集成，Mindbody 是一款帮助健康和保健品牌进行预订、安排、营销、付款、报告等的工具。电子邮件同意从 Mindbody 同步到 Klaviyo。请注意，我们不会同步 Mindbody 的短信同意。 ## 将 Mindbody 与 Klaviyo 集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 单击右上角的****探索应用程序****。 3. 搜索 **Mindbody**，单击该卡，然后单击****安装****。 4. 输入您的 Mindbody 站点 ID（也称为客户端 ID）并单击****连接到 Mindbody****。 - 如果您需要帮助查找此 ID，请查看 Mindbody 的帮助中心文章：[如何查找我的客户端 ID](https://support.mindbodyonline.com/s/article/206398178-How-do-I-find-my-Client-ID?language=en_US)。 5. 如果您有多个站点或客户端 ID，您可以将它们输入为以逗号分隔的列表。 6. 接下来，单击****生成激活链接****。 7. 单击生成的链接以激活您的站点，然后按照 Mindbody 中的说明进行操作。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28716056289435)
8. 激活所有站点后（激活状态显示为绿色），导航回 Klaviyo。状态可能需要几分钟才能变成绿色。 9. 选中该框以将 Mindbody 电子邮件订阅者同步到 Klaviyo 列表，然后从下拉列表中选择一个列表。 10. 单击****连接****，您将看到 Mindbody 和 Klaviyo 之间将传递哪些信息。 11. 要继续集成，请选择****允许****。您将被重定向到可以查看所有集成的页面。您无法在不重新集成的情况下添加更多站点/客户端 ID。如果您需要添加另一个站点 ID：
12. 在 Klaviyo 中，在左下角选择您的帐户名。然后，单击****集成。****
13. 在列表中找到 **Mindbody**，然后单击三点菜单。 14. 选择****删除集成****，然后在模式中确认。 15. 按照上述说明重新集成并包含所有站点 ID。 - 请注意，重新集成时，您必须等待先前安装的站点 ID 的激活状态变为绿色。然后，只需单击您添加的任何新站点 ID 的激活链接。 - 如果您在 Mindbody 中收到错误，请退出并重试。 ## 了解您的 Mindbody 数据

Klaviyo 同步客户资料以及 Mindbody 中与预约和会员资格相关的不同事件。要查看您的 Mindbody 事件数据：

1. 单击左侧导航侧栏中的****分析****下拉列表。 2. 选择****指标****。在这里，您可以查看帐户中的所有指标。带有 Mindbody 图标的指标代表从 Mindbody 集成同步的所有指标。 3. 使用搜索栏旁边的过滤器选择器过滤此视图以仅查看 Mindbody 指标。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37303645882779)

请注意，只有您在 Mindbody 中使用的指标才会同步到 Klaviyo，因此您可能无法在帐户中看到上面列出的所有指标。详细了解[您的 Mindbody 数据](https://help.klaviyo.com/hc/en-us/articles/15344283585819)。 ## 使用 Mindbody 数据细分客户

您可以使用 Mindbody 的指标来细分客户并针对他们开展营销活动。例如，您可以为过去 30 天内激活会员的每个人创建一个细分，并向该细分发送营销活动。要创建上面所示的示例段：

1. 单击左侧导航边栏中的****受众**** 下拉列表。 2. 单击****列表和分段****。 3. 单击右上角的****新建****。 4. 选择****创建分段****。 5. 为您的分段命名并根据需要选择标签。 6. 在 **定义** 下，选择 ****某人已完成（或未完成）的操作**** > ****激活的会员资格**** > ****至少一次**** > ****最近**** > ****30**** > ****天****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37303645885595)
7. 如果您希望仅包括首次激活会员资格的人员：

   - 单击****AND**** 添加新的独占条件。 - 添加条件 ****某人已完成（或未完成）的操作**** > ****激活会员资格**** > ****等于**** > ****1**** > ****一直以来****。这将排除多次激活会员资格的任何人。！[](https://klaviyo.zendesk.com/hc/article_attachments/37303645887515)
8. 单击****创建分段****。 ## 在流程中使用 Mindbody 数据

您可以使用 Mindbody 指标来触发流程。例如，您可以使用 **激活的会员资格** 指标来触发流程，以便在某人激活其会员资格时立即向其发送消息。您还可以使用该流程发送一系列消息，让他们知道如何充分利用其会员资格。如果您的 Mindbody 套餐包含自动发送电子邮件的功能，请确保关闭您希望通过 Klaviyo 流程发送的电子邮件，以便您的客户不会收到重复的消息。有关如何禁用自动电子邮件的更多信息，请参阅 [Mindbody 的支持文档](https://support.mindbodyonline.com/)。要使用 Mindbody 指标创建流程：

1. 从左侧导航侧栏导航至****Flows**** 选项卡。 2. 单击右上角的****创建流程****。 3. 单击右上角的****构建您自己的****。 4. 为流程命名并根据需要选择标签。 5. 单击****创建流****。 6. 在流程构建器中，选择****所有触发器****选项卡。 7. 从下拉列表中，选择一个 Mindbody 指标，例如****激活的会员****，由 Mindbody 图标指示。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37303645889051)
8. 单击****保存****。 9. 添加与触发操作相关的时间延迟和消息。对于**激活的会员资格**示例，您可以创建包含以下内容的消息：

   - 感谢客户激活其会员资格。 - 告知客户其会员资格的好处。 - 发送与其会员资格相关的宣传材料。！[由已激活会员资格指标触发的流程示例，其中发送了有关客人会员资格的电子邮件](https://klaviyo.zendesk.com/hc/article_attachments/28716056282395)
10. 内容准备好后，[设置直播流程](https://help.klaviyo.com/hc/en-us/articles/360048376172)。 ## 结果

现在，您已将 Mindbody 与 Klaviyo 集成，并了解了 Klaviyo 中的 Mindbody 数据、使用 Mindbody 数据对客户进行细分以及在流程中使用 Mindbody 数据。