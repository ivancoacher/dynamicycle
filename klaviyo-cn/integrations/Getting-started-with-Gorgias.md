---
id: "4408023789083"
title: "高尔吉亚入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4408023789083-Getting-started-with-Gorgias"
section: "Gorgias"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:59Z"
language: "zh"
---
您必须是所有者或管理员才能设置此集成。了解如何与 Gorgias Helpdesk 集成以在 Gorgias 和 Klaviyo 之间同步支持票证信息。通过这种集成，您可以：

- 同步有关从 Gorgias 到 Klaviyo 的开放门票信息。 - 使用 Gorgias 回复传入的 SMS 和 WhatsApp 消息。 - 如果您使用 [Klaviyo Reviews](https://help.klaviyo.com/hc/en-us/articles/15937542819355)，请为负面评论创建支持票。 If you manage multiple brands in Gorgias, tickets, SMS messages, WhatsApp messages and reviews can be synced on a per-brand basis, given that you’ve set up proper tagging in Gorgias.我们建议每个 Klaviyo 帐户同步一个 Gorgias 品牌，以便轻松使用您的门票数据并组织您的短信对话。我们在下面详细介绍了如何通过多品牌设置实施 Gorgias 标签。 ## 开始之前

请注意，当客户回复 Klaviyo 发送的电子邮件时，此集成不会自动创建 Gorgias 票证。话虽这么说，Gorgias 将为您的支持电子邮件地址收到的任何电子邮件创建票证。 Thus, if your sender email address in Klaviyo is the same as your support email address in Gorgias, tickets will be created for responses to any marketing emails you send. ### 短信先决条件

仅支持设置了 SMS 的账户使用 Gorgias 集成的 SMS 相关功能：

- SMS 集成仅适用于您拥有免费电话号码、长代码或短代码的国家/地区。 - 品牌发件人 ID（也称为字母数字发件人 ID）无法接收短信，因此您无法为使用品牌发件人 ID 的国家/地区的订阅者使用此集成。了解更多[关于短信发送号码](https://help.klaviyo.com/hc/en-us/articles/6637671573403)。 - If you plan to use Gorgias to respond to SMS, you must have previously [set up SMS in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/4404274419355). - Make sure that you’ve [reviewed key Inbox settings](https://help.klaviyo.com/hc/en-us/articles/360059002271#h_01JMFEZW49YCGTZ5TPZ35ZYMZN) including your auto-responder. - Make sure that your [Inbox email notification address](https://www.klaviyo.com/inbox/settings/inbound-messages) is different from your Gorgias contact email address.否则，Gorgias 中的通知将无法正确显示。 ### WhatsApp 先决条件

您需要[在 Klaviyo 中设置 WhatsApp](https://help.klaviyo.com/hc/en-us/articles/40111819732635)。这包括将您的 WhatsApp Business 帐户连接到 Klaviyo、获取电话号码并验证您的帐户。 ### 审核先决条件

要使用集成的评论部分，您必须使用 Klaviyo Reviews 收集评论。了解如何[开始使用 Klaviyo 评论](https://help.klaviyo.com/hc/en-us/articles/15937542819355)。 ****多品牌账户指导****

If you manage multiple brands within one Gorgias account, syncing one Gorgias brand per Klaviyo account makes it easy to use your ticket data and organize your SMS and WhatsApp conversations. Before integrating Klaviyo with Gorgias, you’ll need to create a rule for each brand to tag tickets, and optionally create a view based on brand tags, to enable brand-specific syncing to and from Klaviyo. #### 在 Gorgias 中创建规则以按品牌标记门票

In Gorgias, for each brand, you’ll need to create a rule that looks at the email the user is writing in to, and then tags the ticket with the appropriate brand:

1. 在您的 Gorgias 设置中，选择 ****规则****（可在 **生产力**下找到）。 2. 添加新规则。 3. 为您的规则命名具有描述性的名称。 4. 添加以下规则条件：
   1. 何时 > 工单创建 > 然后
   2. IF > 消息集成 > IS > [品牌专用电子邮件地址]
   3. 然后 > 添加标签 > [品牌特定标签]
      ![](https://klaviyo.zendesk.com/hc/article_attachments/37721807239707)
5. 确保**启用规则**设置为****开****。 6. 单击****创建规则****。对您想要与单独的 Klaviyo 帐户集成的每个品牌重复此过程。 ####（可选）根据品牌标签在 Gorgias 中创建视图

After setting up rules to auto-tag tickets, we recommend creating a view in Gorgias for each brand, containing all of the tickets tagged with the brand name:

1. 在 Gorgias 中，创建一个新视图。 2. 添加以下过滤器：标签 > 包含全部 > [品牌标签]

![](https://klaviyo.zendesk.com/hc/article_attachments/37721807244699)

对您想要与单独的 Klaviyo 帐户集成的每个品牌重复此过程。 ## Integrate with Gorgias

请按照下面概述的步骤将 Gorgias 与 Klaviyo 集成：

1. 登录您的 Klaviyo 帐户。 2. 选择****集成****选项卡。 3. 选择****探索应用程序****，搜索**Gorgias**，然后单击该卡。然后，单击****安装****。 4. 输入您的 Gorgias 帮助台 URL，然后单击****连接到 Gorgias****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37721809907099)
5. Log in to Gorgias, if prompted. 6. 单击****授权****，允许 Klaviyo 访问所有资源。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37721809908635)
7. 选择是否要将所有新的 Gorgias 门票同步到 Klaviyo，或者仅同步包含特定标签的特定门票。 1. Klaviyo 与 Gorgias 的集成允许通过使用标签在每个品牌的基础上同步门票。 2. 如果您在一个 Gorgias 帐户中管理多个品牌，我们建议每个 Klaviyo 帐户同步一个品牌，以避免帐户之间出现重复的配置文件。在上一节中，我们解释了如何在 Gorgias 中为每个品牌添加标签和设置视图。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37721807261339)
8. 选中**同步 SMS 对话**框以使用 SMS 集成功能。 1. 对于多品牌帐户，我们建议添加与您要与此 Klaviyo 帐户一起使用的 Gorgias 品牌相对应的标签。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37721809916827)
9. 选中**同步 WhatsApp 对话**复选框以使用 WhatsApp 集成功能。 1. 支持代理还可以使用[扩展 WhatsApp 对话的模板](https://help.klaviyo.com/hc/en-us/articles/40116778911259)，确保他们可以在 24 小时服务窗口之外继续与收件人互动。 ![显示同步 WhatsApp 对话选项的对话框](https://klaviyo.zendesk.com/hc/article_attachments/41259951528475)
10. 如果您想使用集成的评论功能，请选中 **同步评论** 框并选择阈值。 1. 默认阈值为 3，这意味着任何提交的评分为 3 或更低的评论都会自动创建一张 Gorgias 票证，供您的团队跟进。 2. 对于多品牌帐户，我们建议添加与您要与此 Klaviyo 帐户一起使用的 Gorgias 品牌相对应的标签。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37721809920411)
11. 建议：选中**将客户个人资料信息从 Klaviyo 同步到 Gorgias**，将联系人的电子邮件地址、电话号码、个人资料属性等发送到 Gorgias。仅当您启用短信或评论时，此数据才会同步。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37721807279643)
12. 如果您使用 [客户中心](https://help.klaviyo.com/hc/en-us/articles/33660324811675) 和 AI 代理：您可以将 AI 服务代理无法回答的客户查询转交给您在 Gorgias 的团队。点击****管理设置****进入AI代理设置并选择Gorgias作为您的[代理切换]。(https://klaviyo.zendesk.com/hc/en-us/articles/37659474656027)
    ![](https://klaviyo.zendesk.com/hc/article_attachments/38074454281243)
13. Click ****Complete setup****. ## Metrics synced between Gorgias and Klaviyo

以下指标从 Gorgias 实时同步到 Klaviyo。这些指标将显示在个人的个人资料页面上，并且可以在细分和流程中使用。 - **Opened Ticket**
- **Resolved Ticket**
- 满意度调查已回复（例如，**已完成的调查**）

  每个指标都与关联的配置文件一起存储。如果配置文件不存在，则会在 Klaviyo 中创建一个配置文件。 如果您在特定的个人资料中并查看指标的活动，您将能够看到以下信息：
- 票被分配给谁
- 票证 ID 和 URL
- 渠道（短信或电子邮件）
- 留言内容
- 品牌

  如果您选中**将客户资料信息从 Klaviyo 同步到 Gorgias**，并启用短信或评论功能，则以下字段将从 Klaviyo 同步到 Gorgias 并显示在右侧边栏中：
- 电子邮件地址
- 电话号码
- 地点
- 同意
- 自定义属性
- 活动

请注意，如果个人资料中没有电话号码或电子邮件地址，Klaviyo 将同步占位符（即 **555-555-5555** 或 **sms-integrations+kl{客户电话号码})@klaviyo.com**）。请勿使用这些占位符发送支持消息，因为不会收到它们。 ## Gorgias SMS 集成如何工作

设置集成后，Klaviyo 将在满足以下条件时自动在 Gorgias 中创建票证：

- 同意的短信订阅者会向与您的帐户关联的电话号码发送短信。 - 短信不包含关键字（即 Klaviyo 短信设置页面中列出的[订阅单词](https://help.klaviyo.com/hc/en-us/articles/360050384091) 之一）。两个例外是 HELP 和 INFO，它们都会创建票证。品牌发件人 ID（也称为字母数字发件人 ID）无法接收短信，因此您无法为使用品牌发件人 ID 的国家/地区的订阅者使用此集成。了解更多[关于短信发送号码](https://help.klaviyo.com/hc/en-us/articles/6637671573403)。如果客户通过短信发送图像或 GIF，该图像将不会显示在 Gorgias 中。同样，您无法从 Gorgias 发送彩信。任何后续消息都会自动添加到票证中。来自 Gorgias 内部的回复也会出现在 Klaviyo 中，但在 [Klaviyo 收件箱](https://help.klaviyo.com/hc/en-us/articles/360059002271) 中发送的回复不会出现在 Gorgias 中。因此，我们建议您仅回复来自 1 个平台的客户。此外，通过 Klaviyo 发送的流程、活动和自动回复消息不会出现在 Gorgias 中。 Gorgias 的回复使用与最新入站消息相同的渠道发送，并通过与您的 Klaviyo 帐户关联的电话号码发送。如果订户向您发送短信，回复将是通过您帐户中的免费电话号码、长代码或短代码发送的短信。来自 Gorgias 的消息与其他消息一样计入您的 [短信计费](https://help.klaviyo.com/hc/en-us/articles/115000976672) 计划。如果可能的话，我们建议在 Gorgias 中为短信响应创建一个模板，其长度应小于 153 个字符。详细了解[短信最佳实践](https://help.klaviyo.com/hc/en-us/articles/360035661191#h_01HCJKFZS852ZMJJF6SXW2SJ55)。 ## Gorgias WhatsApp 集成如何运作

设置集成后，Klaviyo 将在满足以下条件时自动在 Gorgias 中创建票证：

- 客户通过 WhatsApp 向您的企业发送入站消息。 - 如果消息与合规性、订阅或自动对话关键字不匹配，Klaviyo 将提示在 Gorgias 中创建支持票证。您的支持代理可以回答 Gorgias 的客户，回复将通过您的 WhatsApp 业务号码发送。请注意，代理回复类型在 Gorgias 中将显示为 **电子邮件**，但将通过 WhatsApp 发送。 ![Gorgias 中的代理响应类型](https://klaviyo.zendesk.com/hc/article_attachments/41259964479003)

在 **Klaviyo 频道** 侧面板中，您将能够查看有关消息的信息，包括频道（WhatsApp 或 SMS）和同意状态。 ![消息详细信息，表示同意 WhatsApp](https://klaviyo.zendesk.com/hc/article_attachments/41259964480155)

如果 WhatsApp 同意状态为 **已过期**，并且您已启用上一节中引用的后续设置，您的客服人员可以单击 ****WhatsApp Follow Up**** 将模板发送给客户。如果客户回复，24 小时窗口将重置，对话可以继续。如果客户使用 WhatsApp 发送图像或其他媒体，该图像将不会显示在 Gorgias 中。同样，您无法从 Gorgias 发送图像或其他媒体消息。 ## 高尔吉亚评论集成如何运作

设置集成后，只要有人提交符合您设置的标准（即星级等于或低于您的选择）的评论，Klaviyo 就会自动创建一个新票证。票证中提供的详细联系信息取决于您是否在 Gorgias 集成设置中启用 **从 Klaviyo 同步客户资料信息** 选项。 - 如果该设置被禁用：
  Klaviyo 只会同步审阅者的电话号码（如果有）。如果评论者在 Klaviyo 没有电话号码，我们将使用欺骗电话号码 (555-555-5555) 来创建票证，并且您可能在 Gorgias 中看不到该票证的任何真实联系信息。 - 如果启用该设置：
  Klaviyo 会将他们的个人资料信息同步到 Gorgias，包括电子邮件和电话号码。如果个人资料没有电子邮件地址，Klaviyo 将同步一个欺骗性电子邮件地址：sms-integrations+kl{客户电话号码})@klaviyo.com。如果个人资料没有电话号码，我们将同步一个欺骗电话号码 (555-555-5555)。每个个人资料将至少有 1 种有效的联系信息。无论选择何种个人资料信息设置，工单侧边栏中都将提供以下评论详细信息：
- 审查属性：
  - 星级
  - 作者
  - 审核日期
  - 已验证状态
  - 发布状态
- 产品信息：
  - 产品名称
  - 产品网址
  - 产品图片网址

    此外，票证还包含以下信息：
- 产品名称
- 客户评价
- 审查机构

## 集成同步时

集成实时同步。一旦短信订阅者向您发送短信或客户提交评论，该消息就会出现在 Gorgias 中。请注意，没有历史同步。如果在您设置此集成之前订阅者给您发短信或留下评论，Klaviyo 中的短信票证和过去的评论将不会出现在 Gorgias 中。但是，所有进一步的消息都将同步。如果订阅者在您启用集成之前和之后向您发送短信或提交评论一次，则您设置集成后收到的消息将显示在 Gorgias 中，但之前发送的消息不会显示。