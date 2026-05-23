---
id: "115005253728"
title: "Zendesk 入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005253728-Getting-started-with-Zendesk"
section: "Zendesk"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: "zh"
---
了解如何将 Zendesk 与 Klaviyo 集成，以改善客户的支持体验。这种集成使您能够：

- 根据客户与支持团队的互动来跟踪和定位客户。 - 从 Zendesk 内回复 SMS 和 WhatsApp 消息。门票、短信和 WhatsApp 消息可以按品牌同步。如果您在一个 Zendesk Enterprise 账户下设置了多个品牌，则为每个 Klaviyo 账户同步一个 Zendesk 品牌可以让您轻松使用您的工单数据并组织您的 SMS 和 WhatsApp 对话。 ## 开始之前

您可以使用 Zendesk/Klaviyo 集成来同步支持票证信息，或同步票证以及 SMS 和 WhatsApp 消息信息。如果不同步支持票证信息，您将无法使用 SMS 或 WhatsApp 功能。 ### 短信先决条件

如果您想从 Zendesk 内回复 SMS 和 WhatsApp 消息，则以下内容适用：

- 您必须已经[在 Klaviyo 中设置短信](https://help.klaviyo.com/hc/en-us/articles/4404274419355)。 - 此功能仅适用于您拥有免费电话号码、长代码或短代码的国家/地区。 - 品牌发件人 ID（也称为字母数字发件人 ID）无法接收短信，因此您无法为使用品牌发件人 ID 的国家/地区的订阅者使用此集成。了解更多[关于短信发送号码](https://help.klaviyo.com/hc/en-us/articles/6637671573403)。 - 当有人发送以下任何短信时，不会创建对话：
  - 订阅关键字（例如，JOIN）
  - 合规关键字（例如，STOP 或 JOIN）
  - 触发自动化关键字（会话短信）
- 确保您已查看我们的[双向消息传递最佳实践（称为 Klaviyo Inbox）](https://help.klaviyo.com/hc/en-us/articles/360059002271#h_01JMFEZW49YCGTZ5TPZ35ZYMZN)，包括自动回复设置。 - 此集成位于 Zendesk 的“支持”代理工作区中。它利用票证 API 创建票证并对其进行评论，不需要 Zendesk“Talk”呼叫中心工作区即可运行。 ### WhatsApp 先决条件

您需要[在 Klaviyo 中设置 WhatsApp](https://help.klaviyo.com/hc/en-us/articles/40111819732635)。这包括将您的 WhatsApp Business 帐户连接到 Klaviyo、获取电话号码并验证您的帐户。 ## 将 Zendesk 与 Klaviyo 集成

请按照下面列出的步骤将 Zendesk 与 Klaviyo 集成：

1. 登录您的 Klaviyo 帐户。 2. 选择****集成****选项卡。 3. 单击****探索应用程序****，搜索 Zendesk，然后单击该卡。然后，单击****安装****。 4. 在下一页上，输入您的 Zendesk URL 并单击****连接到 Zendesk****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36263452885147)

4. 如果需要，请登录 Zendesk。 5. 检查权限并批准。然后您将被带回克拉维约。 6. 在**票证下，** 选择是否要同步所有品牌或特定品牌的 Zendesk **已打开** 和 **已解决** 票证指标。 - 如果您选择 **特定品牌**，系统将提示您从下拉列表中选择所需的 Zendesk 品牌。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36263422312987)

7. 如果您想通过 Zendesk 回复入站短信，请选中****同步短信对话****旁边的框。如果出现提示，请选择要在其下创建 Zendesk 票证的品牌。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36263422320795)

8. 如果您想通过 Zendesk 回复入站 WhatsApp 消息，请选中****同步 WhatsApp 对话****旁边的框。如果出现提示，请选择要在其下创建 Zendesk 票证的品牌。 9. 如果您使用 [客户中心](https://help.klaviyo.com/hc/en-us/articles/33660324811675) 和 AI 代理：您可以将 AI 服务代理无法回答的客户查询转交给 Zendesk 中的团队。单击 ****管理设置**** 转到 AI 代理设置并选择 Zendesk 作为您的[代理切换]。(https://klaviyo.zendesk.com/hc/en-us/articles/37659474656027)

![](https://klaviyo.zendesk.com/hc/article_attachments/39896725334043)

10. 完成后，单击****完成设置****。 ## 测试短信发送

您可以通过向您的发送号码发送短信来测试您的集成（如果您已经是同意的订阅者，并且短信不包含除 HELP 或 INFO 之外的关键字）。在您的 Zendesk 管理员中，检查是否已创建票证，对其进行回复，然后查看您是否收到短信。 如果发送 SMS 的配置文件与从 Zendesk 回复的代理具有相同的电子邮件地址，则不会发送回复。在测试过程中，确保代理和客户（发送短信的个人资料）不共享相同的电子邮件地址。 ## 测试 WhatsApp 发送

您可以通过向您的 WhatsApp 业务号码发送 WhatsApp 消息来测试集成（如果该消息不包含合规性、订阅或自动化触发关键字）。在您的 Zendesk 管理员中，检查是否已创建票证，对其进行回复，然后查看是否收到回复的 WhatsApp 消息。如果发送 WhatsApp 消息的配置文件与从 Zendesk 回复的代理具有相同的电子邮件地址，则不会发送回复。在测试过程中，请确保代理和客户（配置文件消息中的）不共享相同的电子邮件地址。 # Zendesk SMS 集成如何工作

设置 SMS 集成后，只要满足以下两个条件，Klaviyo 就会自动在 Zendesk 中创建票证：

1. [同意的短信订阅者](https://help.klaviyo.com/hc/en-us/articles/360035056972) 向与您的帐户关联的电话号码发送短信。 2. 短信不包含关键字（即 Klaviyo 短信设置页面中列出的[订阅单词](https://help.klaviyo.com/hc/en-us/articles/360050384091)之一）。两个例外是 HELP 和 INFO，它们都会创建票证。来自[品牌发件人 ID](https://help.klaviyo.com/hc/en-us/articles/6637671573403#branded-sender-ids2)（也称为字母数字发件人 ID）的 SMS 消息不会显示，因为这些号码无法接收入站消息。同步按以下方式运行：

- Zendesk 代理在票证中的任何回复都会向客户发送短信。 Zendesk 内部的回复也将出现在 Klaviyo 中。 - 如果工单的状态为**打开**，新的客户消息将作为评论添加到工单中。如果票证的状态为**已解决**，新的客户消息将重新打开票证并将该消息添加为评论。如果工单的状态为 **已关闭**，新的客户消息将创建一个新工单。 - Zendesk 的回复通过与您的 Klaviyo 帐户关联的电话号码发送；该发送号码将是向其发送入站消息的号码。 - 来自 Zendesk 内部的回复也将显示在 Klaviyo 中，但在 Klaviyo 收件箱选项卡中发送的回复不会显示在 Zendesk 中。因此，我们建议您仅通过一个平台回复客户。 Klaviyo 发送的活动和流程 SMS 消息也将同步到 Zendesk。 - 来自 Zendesk 的消息与任何其他消息一样计入您的 SMS 计费计划。 ## 集成同步时

短信集成实时同步。一旦 SMS 订阅者向您发送短信，该消息就会出现在 Zendesk 中。 **已打开的工单**和**已解决的工单**指标也会实时同步。请注意，没有历史同步。如果订阅者在您设置此集成之前向您发送短信，短信票证（“对话”）将不会显示在 Zendesk 中。但是，所有进一步的消息都将同步。如果订阅者在您启用集成之前和之后分别向您发送短信一次，则您设置集成后收到的消息将显示在 Zendesk 中。如果客户通过短信发送图像或 GIF，该图像将不会显示在 Zendesk（或 Klaviyo）中。同样，您无法从 Zendesk 发送彩信。 # ****Zendesk WhatsApp 集成如何运作****

设置 WhatsApp 集成后，Klaviyo 会在以下情况下自动在 Zendesk 中创建票证：

客户通过 WhatsApp 向您的企业发送入站消息。该消息与合规性、订阅或自动对话关键字不匹配。如果消息与这些关键字不匹配，Klaviyo 将提示在 Zendesk 中创建支持票证。您的支持代理可以在 Zendesk 中回复客户，回复将通过您的 WhatsApp 业务号码发送。在 Klaviyo 频道侧面板中，您将能够查看有关消息的信息，包括频道（WhatsApp 或 SMS）和同意状态。如果 WhatsApp 同意状态为“已过期”，并且您在设置过程中启用了后续模板设置，则您的客服人员可以将模板发送给客户以重新参与。如果客户回复，24 小时窗口将重置，对话可以继续。如果客户通过 WhatsApp 消息发送图像或其他媒体，该图像将不会显示在 Zendesk 中。 同样，您无法通过 WhatsApp 从 Zendesk 发送图像或其他媒体消息。来自 Zendesk 内部的回复也将显示在 Klaviyo 中，但在 Klaviyo 收件箱选项卡中发送的回复不会显示在 Zendesk 中。因此，我们建议您仅通过一个平台回复客户。 Klaviyo 发送的营销活动和流程 WhatsApp 消息也将同步到 Zendesk。来自 Zendesk 的消息与任何其他消息一样计入您的 WhatsApp 计费计划。 ## ****当集成同步时****

SMS 和 WhatsApp 集成实时同步。一旦 SMS 订阅者向您发送短信或客户向您发送 WhatsApp 消息，该消息就会出现在 Zendesk 中。已打开的工单和已解决的工单指标也会实时同步。请注意，没有历史同步。如果订阅者在您设置此集成之前向您发送消息，则 SMS 和 WhatsApp 票证（“对话”）将不会显示在 Zendesk 中。但是，所有进一步的消息都将同步。如果订阅者在您启用集成之前和之后向您发送消息一次，则您设置集成后收到的消息将显示在 Zendesk 中。如果客户通过短信或 WhatsApp 消息发送图像或 GIF，该图像将不会显示在 Zendesk（或 Klaviyo）中。同样，您无法从 Zendesk 发送彩信或 WhatsApp 媒体消息。 ## Klaviyo 和 Zendesk 之间同步的指标

Klaviyo 跟踪 2 个 Zendesk 指标：**打开的工单**和 **已解决的工单**。这些指标显示在个人的个人资料页面上，可以在细分和流程中使用。他们实时同步。 ### 已开票

在 Zendesk 中打开新票证时会跟踪此事件，并包含有关新票证的以下信息：

- ****受让人\_电子邮件****
  Zendesk 中分配给票证的支持代理的电子邮件
- ****受让人\_name****
  在 Zendesk 中分配给票证的支持代理的名称
- ****频道****
  有关票证通过的渠道的信息（例如电子邮件、门户网站、短信），在可用时填充
- ****描述****票证中第一条消息的正文
- ****字段****来自 Zendesk 的任何自定义字段
- ****Group\_name****来自 Zendesk 的组字段
- ****优先级****来自 Zendesk 的优先字段
- ****主题****
  Zendesk 票证的主题
- ****标签****
  Zendesk 中与票证关联的标签
- ****机票\_id****
  来自 Zendesk 的票证 ID
- ****类型****
  来自 Zendesk 的类型字段
- ****通过****
  有关票证来源的信息，在可用时填充
- ****Zendesk\_url****Zendesk 中票证的 URL
- ****状态****Zendesk 中的票证状态

### 已解决的票证

当票证在 Zendesk 中标记为 **已关闭** 时，就会跟踪此事件。当票证在 Zendesk 中标记为 **已解决** 时，不会向 Klaviyo 发送任何事件。 Klaviyo 对此事件的跟踪包括有关已解决的票证电子邮件的以下信息：

- ****受让人\_电子邮件****
  Zendesk 中分配给票证的支持代理的电子邮件
- ****Assignee\_name****在 Zendesk 中分配给票证的支持代理的名称
- ****渠道****有关票证通过的渠道的信息（例如电子邮件、门户网站、短信），在可用时填充
- ****描述****票证中第一条消息的正文
- ****字段****来自 Zendesk 的任何自定义字段
- ****Group\_name****来自 Zendesk 的组字段
- ****优先级****来自 Zendesk 的优先字段
- ****主题****Zendesk 票证的主题
- ****标签****
  Zendesk 中与票证关联的标签
- ****票证\_id****来自 Zendesk 的票证 ID
- ****类型****来自 Zendesk 的类型字段
- ****通过****有关票证来源的信息，在可用时填充
- ****Zendesk\_url****Zendesk 中票证的 URL
- ****状态****Zendesk 中的票证状态

## 可选：在 Zendesk 中创建自动化，以更快地将 SMS 和 WhatsApp 票证标记为“已关闭”

如上所述，一旦票证在 Zendesk 中标记为“已关闭”（而不是标记为“已解决”时），“已解决票证”指标就会发送到 Klaviyo。通过在账户级别设置的规则，票证在 Zendesk 中标记为“已关闭”。如果您同时使用 Zendesk 进行消息传递（SMS 或 WhatsApp）和电子邮件，您可能希望将消息传递票证标记为“已关闭”，而不是电子邮件票证，具体取决于您的支持响应时间和解决问题的时间。这可以通过 Zendesk 自动化来实现。例如，您可以创建以下自动化来将 SMS 票证在 24 小时后标记为“已关闭”：

1. 登录 Zendesk 并导航到您的管理中心。 2. 选择****对象和规则****。 3. 选择****业务规则 > 自动化****。 4. 选择****添加自动化****。 5. 给你的自动化命名。 6. 在**满足以下所有条件**下，选择：

   - 票证：状态/已/已解决
   - 票证：解决后的小时数 / 是 / 24
   - 票证：标签/至少包含以下内容之一/“短信”！[](https://klaviyo.zendesk.com/hc/article_attachments/36263452896795)
7. 在 **执行这些操作** 下，选择：

   - 门票：状态/已关闭
8. 单击****创建自动化****。您现在已经创建了一个自动化功能，可以在 24 小时后关闭 SMS 票证。 ## 可选：在 Zendesk 中为 Klaviyo SMS 和 WhatsApp 创建视图

我们建议在 Zendesk 中创建一个视图，以便整理您的 Klaviyo SMS 和 WhatsApp 票证。此视图将过滤标签“SMS”和“WhatsApp”。请注意，如果您除了 Klaviyo SMS/WhatsApp 之外还有带有此标签的票证，它们也将包含在视图中。 1. 在 Zendesk 管理中心中，单击****工作区****下拉列表。 2. 选择 **代理工具** 下的 **视图****。 3. 单击****添加视图****。 4. 为您的视图命名，添加说明，然后选择有权访问的人员。 5. 在**票证必须满足所有这些条件才能显示在视图中**下，添加：
   状态 > 不是 > 已关闭
6. 在**票证必须满足所有这些条件才能显示在视图中**下，添加：
   标签 > 至少包含以下一项 > 短信
7. 根据您的规格编辑任何格式设置。 8. 单击****保存****。您现在已经创建了一个视图来组织您的 Klaviyo SMS/WhatsApp 票证。 ## Zendesk 指标的用例

以下是您可以考虑利用从 Zendesk 集成同步的指标的几种方法：

- 将持有未处理票证的用户排除在某些流程和活动之外，这样您的公司就不会因为向有待解决问题的用户发送促销电子邮件而冒着显得脱节的风险。 - 使用 Zendesk 数据，根据客户与支持团队的互动，主动跟踪 Klaviyo 中的客户；例如，如果您知道有人没有完成订单，但打开了支持票证，则可以自定义废弃购物车电子邮件。 - 通过使用 Klaviyo 提供的有关您已同步的 Zendesk 指标的详细分析报告，查看围绕未决和已解决的票证的趋势，包括群组分析。 - 调整您的电子邮件策略以减少支持请求并增加终生价值；利用 Klaviyo 中的所有数据，您可以构建细分来查看相关性并获得跨指标的见解。