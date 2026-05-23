---
id: "15752461211547"
title: "Zenoti 入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15752461211547-Getting-started-with-Zenoti"
section: "Zenoti"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:43Z"
language: "zh"
---
## 你将会学到

了解如何与 Zenoti 集成，Zenoti 是一款帮助美容、健康和健身品牌进行预订、日程安排、营销、付款、报告、库存等的工具。 ## 开始之前

- 此集成依赖于 Zenoti Webhooks 和 API，这需要订阅 Zenoti 的 Klaviyo 集成包。要验证您是否拥有此软件包，请以所有者身份访问 Zenoti 仪表板并导航至****管理 > 设置 > 应用程序****。如果您在侧边栏中看不到此选项，请联系您的 Zenoti CSM 或 Zenoti 支持以确认您对该软件包的订阅。 - 您必须在 Zenoti 中拥有所有者凭据才能设置此集成。 ## 将 Zenoti 与 Klaviyo 集成

### 生成 Zenoti API 密钥

要将 Zenoti 与 Klaviyo 集成，您首先需要在 Zenoti 中生成 API 密钥：

1. 在您的 Zenoti 帐户中，导航至****配置 > 集成 > 应用****。 2. 在右上角，选择****添加****。 3. 在下一个屏幕上，输入以下信息：
   - ****姓名****
     克拉维约
   - ****URI****
     （留空）
   - ****描述****
     克拉维约整合
   - ****登录用户类型****
     员工
   - ****源应用程序****
     客户端应用程序
4. 选择****下一步****。 5. 在下一页上，滚动到底部并为 **JWT Groups** 和 **APIKEY Groups** 列单击 ****Select All****，然后选择 ****Next****。 6. 在下一页上，选择****生成 API 密钥****。确保将此信息存储在安全的地方，以便在后续步骤中使用。 7. 选择****完成****。 ### 在 Klaviyo 中添加集成

接下来，在 Klaviyo 中添加集成：

1. 登录 Klaviyo 并选择****集成****选项卡。 2. 单击****探索应用程序****。 3. 搜索 ****Zenoti**** 并单击该卡。 4. 在下一页上，单击****安装****。 5. 粘贴来自 Zenoti 的 API 密钥，然后单击****连接****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38368623578011)
6. 检查权限并单击****允许****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38368577930267)
7. 在下一页上，复制 Webhook URL 并将其保存在安全的地方以供以后使用。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38368623583259)
8. 在**电子邮件订阅者**下，选中****将您的 Zenoti 电子邮件订阅者同步到 Klaviyo****（如果您愿意）。 9. 如果您选择了上述设置，请选择要添加这些订阅者的 Klaviyo 列表。 10. 完成后，单击****保存****。 ### 创建 Zenoti Webhook

最后，您需要在 Zenoti 中创建一个 Webhook：

1. 返回 Zenoti，导航至****配置 > 集成 > Webhooks****。 2. 选择****创建 Webhook****。 3. 在 **创建新的 Webhooks 侦听器** 页面上，选择 **Appointment**、**AppointmentGroup**、**Class**（如果您使用的是类）、**Guest** 和 **Invoice** 下的所有选项，然后单击 ****Next****。 4. 在下一个屏幕上，输入以下信息：
   - ****姓名****
     克拉维约
   - ****描述****
     Klaviyo/Zenoti 集成
   - ****请求类型****POST
   - ****URL****粘贴从 Klaviyo 复制的 Webhook URL。 5. 单击右上角的****完成****。 ## 了解您的 Zenoti 数据

Klaviyo 同步来自 Zenoti 的许多与约会和会员资格相关的不同事件。我们同步 1 年的 Zenoti 历史数据。要查看您的 Zenoti 数据：

1. 单击左侧导航侧栏中的****分析****下拉列表。 2. 选择****指标****。在这里，您可以查看帐户中的所有指标。带有 Zenoti 图标的指标代表从 Zenoti 集成同步的所有指标。 3. 使用搜索栏旁边的过滤器选择器过滤此视图以仅查看 Zenoti 指标。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38368577931675)

详细了解 [您的 Zenoti 数据](https://help.klaviyo.com/hc/en-us/articles/15752724401691)。 ## 使用 Zenoti 数据细分客户

您可以使用 Zenoti 的指标来细分客户并针对他们开展活动。例如，您可以为过去 30 天内激活会员的每个人创建一个细分，并向该细分发送营销活动。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38368623589659)

要创建上面所示的示例段：

1. 单击左侧导航边栏中的****受众**** 下拉列表。 2. 单击****列表和分段****。 3. 单击右上角的****创建列表/细分****。 4. 选择****段****。 5. 为您的分段命名并根据需要选择标签。 6. 在“定义”下，选择 **某人已完成（或未完成）的操作 > 激活的会员资格 > 至少一次 > 在过去 > 30 > 天内**。 7. 单击****创建段****。在此示例中，如果您想确保该细分受众群仅包含首次激活会员资格的人员：

1. 单击****AND**** 添加新的排除条件。 2. 添加条件：**某人已完成（或未完成）的操作 > 已激活的会员资格 > 等于 > 1 > 一直以来**。这将排除多次激活会员资格的任何人

![](https://klaviyo.zendesk.com/hc/article_attachments/38368577934491)

## 在流中使用 Zenoti 数据

您可以使用 Zenoti 指标来触发流。例如，使用“已激活的会员资格”指标来触发流程，以便在某人激活其会员资格时立即向其发送消息。您还可以使用该流程发送一系列消息，让他们知道如何充分利用其会员资格。如果您使用 Zenoti 发送电子邮件和短信通知，请确保关闭您希望通过 Klaviyo 流发送的消息，以便您的客户不会收到重复的消息。有关如何禁用电子邮件和短信通知的更多信息，请参阅 [Zenoti 的支持文档](https://help.zenoti.com/)。要使用 Zenoti 指标创建流程：

1. 从左侧导航侧栏导航至****Flows**** 选项卡。 2. 单击右上角的****创建流程****。 3. 单击右上角的****从头开始创建****。 4. 为流程命名并根据需要选择标签。 5. 单击****创建流****。 6. 在流程构建器中，选择****Metric**** 作为触发器。 7. 从下拉列表中，选择 Zenoti 指标，例如 **激活的成员资格**，由 Zenoti 图标指示。 8. 单击****完成****。 9. 添加与触发操作相关的时间延迟和消息。对于激活的会员资格示例，您可以创建消息以：

1. 感谢客户激活会员资格。 2. 告知客户其会员资格的好处。 3. 发送与其会员资格相关的宣传材料。 10. 内容准备就绪后，单击流程构建器右上角的****更新操作状态****以将流程设置为活动状态。 ## 结果

现在，您已将 Zenoti 与 Klaviyo 集成，并了解了 Klaviyo 中的 Zenoti 数据、使用 Zenoti 数据对客户进行细分以及在流中使用 Zenoti 数据。 ## Zenoti API 密钥过期

请注意，Zenoti 的 API 密钥目前每 12 个月过期一次，必须在 Klaviyo 中更新才能继续集成同步。每 12 个月，您需要在 Zenoti 中创建一个新的 API 密钥，并按照以下步骤与 Klaviyo 重新集成：

1. 删除 Klaviyo 中当前的 Zenoti 集成。 1. 在 Klaviyo 中，选择****集成****选项卡
2. 在启用的集成列表中找到 Zenoti。 3. 单击三点，然后选择****删除集成****。 2. 按照本文中的步骤重新集成。 ## 其他资源

- 了解有关 [Klaviyo 构建的集成](https://help.klaviyo.com/hc/en-us/articles/115000256472) 的更多信息。 - 了解[集成同步数据的频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)。 - 了解[从 Zenoti 集成同步的数据](https://help.klaviyo.com/hc/en-us/articles/15752724401691)。