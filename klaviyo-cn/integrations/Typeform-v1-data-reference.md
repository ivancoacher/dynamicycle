---
id: "115000107112"
title: "Typeform v1 数据参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115000107112-Typeform-v1-data-reference"
section: "Typeform"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:10Z"
language: "zh"
---
本参考资料涉及 Typeform v1 集成，该集成由 Klaviyo 构建，不再允许新安装。新客户应使用由 Typeform 构建的 [Typeform v2 集成](https://www.klaviyo.com/integrations/01JDAJZAM9TM3S5NFTKG67XQ8Z/details)。要了解更多信息，请访问 [Typeform 的帮助中心](https://www.typeform.com/help/a/sync-form-responses-and-send-out-forms-with-klaviyo-4417500739092/)。 ## 你将会学到

Klaviyo 从 Typeform 中引入：

- 当有人填写表格时
- 用户填写的表格的名称和 ID
- 从表单字段收集的数据。请注意，这仅包括客户的回答；它不包括您的组织根据客户答案生成的测验结果等内容。我们的集成允许您将表单订阅者添加到特定的 Klaviyo 列表，并每小时将 Typeform 表单中的关键信息同步到 Klaviyo 一次。 ## 了解您的 Typeform 数据

Klaviyo 跟踪 Typeform 中的一项事件：**填写的表格**。要查看同步事件，请单击 Klaviyo 中的 ****Analytics**** 下拉列表并选择 ****Metrics.**** 然后，按 Typeform 进行筛选。 ![](https://klaviyo.zendesk.com/hc/article_attachments/29520157195803)

每当有人填写表格时，来自 Typeform 的 **填写表格** 事件都会在 Klaviyo 中的该人的个人资料中进行跟踪。如果展开查看任何事件的详细信息，您将找到表单 ID 和名称。 ![](https://klaviyo.zendesk.com/hc/article_attachments/29520157202587)

当我们同步新的表单响应时，我们将查找代表电子邮件、名字、姓氏、组织/公司和电话号码的表单字段。如果找到，我们将自动同步这些字段并在个人的个人资料中设置这些属性。任何其他表单问题都将作为自定义属性记录在个人的个人资料中。表单问题将显示为属性标签，值将是提交者的答案。 ![](https://klaviyo.zendesk.com/hc/article_attachments/29520157206299)

## 在电子邮件中嵌入 Typeform

您需要在嵌入电子邮件的表单中包含一个电子邮件字段，以确保 Klaviyo 可以正确地从表单中收集信息。您可以使用文本块将 Typeform 问题嵌入到电子邮件中。 1. 首先，将 HTML 块拖到您的电子邮件模板中。 2. 导航到您的 Typeform 帐户。要将 Typeform 表单嵌入到您的 Klaviyo 电子邮件中，您需要确保您的表单已发布，并且表单中的第一个问题是以下之一：
   - 意见量表
   - 多项选择
   - 图片选择
   - 是/否
3. 满足这两个要求后，单击****共享 > 在电子邮件中启动 > 获取代码 > 复制代码****。这将复制表单的代码。 ![在 Typeform 中获取带有黑色背景的白色代码的电子邮件代码弹出窗口](https://klaviyo.zendesk.com/hc/article_attachments/28720666093467)
4. 返回 Klaviyo 并将代码粘贴到 HTML 块中。 5. 点击****完成****查看电子邮件中嵌入的表单。 ## 使用 Typeform 数据细分客户

您可以使用 Typeform 的 **填写表格** 指标来细分客户并通过特定的营销活动来定位他们。例如，您可以为过去 30 天内至少填写过一次表单的任何人创建一个细分，然后向该细分发送营销活动。 ![](https://klaviyo.zendesk.com/hc/article_attachments/29520157222811)

您还可以根据客户通过 Typeform 表单提供的信息对客户进行细分，然后向特定的客户组发送有针对性的营销活动。表单中的信息作为个人资料中的属性存在。例如，我们收集了有关顾客是否过敏以及这些过敏是否包括坚果的信息。根据答案并使用 AND 条件，我们创建了一个对坚果过敏的客户群。 ![](https://klaviyo.zendesk.com/hc/article_attachments/29520157225499)

## 在流程中使用 Typeform 数据

您可以使用 Typeform 的 **填写表格** 指标来触发 Klaviyo 中的流程。例如，您可以利用表单 ID 作为触发过滤器，在某人填写特定表单时触发流程。在下面的示例中，当客户填写表单（表单 ID：CIHFHQ）时，将触发流程。 ![](https://klaviyo.zendesk.com/hc/article_attachments/29520157232283)

您还可以根据从表单收集的信息在流程中进行分支，因为该数据作为个人资料中的属性存在。 例如，我们使用条件拆分向有和没有坚果过敏的人发送单独的消息。 ![](https://klaviyo.zendesk.com/hc/article_attachments/29520177001883)

## 其他资源

- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [分段入门](https://help.klaviyo.com/hc/en-us/articles/115005237908)