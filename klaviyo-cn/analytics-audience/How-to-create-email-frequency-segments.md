---
id: "115000769631"
title: "如何创建电子邮件频率段"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115000769631-How-to-create-email-frequency-segments"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:56:36Z"
language: "zh"
---
## 你将会学到

了解如何向订阅者提供不同的电子邮件频率首选项，以便您可以预先设定期望并提供更多相关内容。允许订阅者选择收到您消息的频率是保持参与度和减少取消订阅的好方法。如果你表现得过于强势并频繁向订阅者发送电子邮件，则可能会面临新注册者立即取消订阅的风险。 ## 让您的订阅者设置电子邮件频率首选项

根据频率偏好对电子邮件列表进行细分的第一步是允许您的订阅者选择他们收到您邮件的频率。了解如何将频率首选项字段添加到“管理首选项”页面：

1. 单击左下角您的帐户名称。 2. 选择****设置****。 3. 选择****其他****。 4. 在**首选项页面**下，点击****编辑页面****。 ![同意页面](https://klaviyo.zendesk.com/hc/article_attachments/28711672627611)

   如果您之前创建了特定于列表的同意页面，请导航到主列表的首选项页面编辑器。 5. 单击****添加块****。 ![将块添加到首选项页面](https://klaviyo.zendesk.com/hc/article_attachments/28711660470811)
6. 将**单选按钮**块添加到您的首选项页面。 7. 在**标签文本**字段中，输入“您希望多久收到一次我们发送的电子邮件？” （或类似）。 ![首选项页面的单选按钮设置显示标签文本字段](https://klaviyo.zendesk.com/hc/article_attachments/28711660455835)
8. 在**配置文件属性**字段中，输入“电子邮件频率”，然后点击****创建[“电子邮件频率”]****。如果您希望使用不同的属性名称，请从菜单中选择它或将其输入到搜索字段中以创建它。 ![首选项页面的单选按钮设置显示配置文件属性字段](https://klaviyo.zendesk.com/hc/article_attachments/28711660459419)
9. 在**标签**列中，添加一系列电子邮件频率选项（例如，每日、每周、每月）。这些标签将出现在您的首选项页面上。 10. 在**值**列中，添加相应的属性值。这些值将出现在 Klaviyo 的客户档案中。 ![首选项页面的单选按钮设置显示多个值字段](https://klaviyo.zendesk.com/hc/article_attachments/28711672625947)
11. 点击 ****发布**** 发布您的首选项页面。当有人注册或选择编辑其偏好设置时，他们的联系人个人资料中将添加或更改[自定义属性](https://help.klaviyo.com/hc/en-us/articles/115005074627-Add-Custom-Properties-to-a-Contact-Profile)。 ## 询问订阅者的偏好

一旦您的偏好页面包含有关电子邮件频率偏好的问题，请发送活动要求订阅者完成它。要在电子邮件中包含指向您的首选项页面的链接，请使用模板标签“{%
管理首选项%}`。或者，要自定义管理首选项链接中显示的文本，请使用标签“{% manage_preferences”click
这里' %}` 并将文本“单击此处”替换为您喜欢的文本。除了专门发送活动来请求订阅者首选项之外，还可以考虑在电子邮件页脚中包含管理首选项链接。 ## 建立电子邮件频率段

从订阅者那里收集到此信息后，在您的营销活动发送中构建细分以[包含或排除](https://help.klaviyo.com/hc/en-us/articles/115005227808-Send-a-Campaign-to-Multiple-Lists)。如果您将频率首选项设置为可选，则您将需要有一个默认的发送节奏，以防订阅者不选择所提供的任何选项。通常最好将其作为中间立场，而不是立即向订阅者发送每日电子邮件。 ### 每日

![每日偏好片段](https://klaviyo.zendesk.com/hc/article_attachments/28711660472475)

### 每周

![每周偏好部分](https://klaviyo.zendesk.com/hc/article_attachments/28711660478747)

### 每月

![每月偏好部分](https://klaviyo.zendesk.com/hc/article_attachments/28711660487963)

## 未设置电子邮件频率首选项的订阅者

如果您将电子邮件频率首选项设置为可选，则您的电子邮件列表中将会有一些人的频率未设置****。**** 请务必不要忘记向这些订阅者发送消息。 要计算有多少人，请使用以下条件构建一个细分：

![无频率设置段](https://klaviyo.zendesk.com/hc/article_attachments/28711672652059)

向这些订阅者发送电子邮件营销活动，并排除您的每日、每周和每月细分。 ![针对没有频率偏好的人的活动](https://klaviyo.zendesk.com/hc/article_attachments/28711660453531)

然后，您可以为每日、每周和每月细分构建营销活动，并像平常一样发送给他们。您发送到每个分段的内容应该有所不同。例如，每周新闻通讯可以是一周内发生的任何新产品发布等的摘要，而每日更新可以突出显示您正在进行的任何销售或促销活动。由于您不经常与这些订阅者沟通，因此每月简讯应该更长且精心策划。 ## 其他资源

- 课程：[开发内容日历](https://academy.klaviyo.com/developing-a-content-calendar)
- [如何根据电子邮件参与度创建发送计划](https://help.klaviyo.com/hc/en-us/articles/360037527052-Create-a-Sending-Schedule-Based-on-Email-Engagement)
- [如何创建客户参与度](https://klaviyo.zendesk.com/hc/en-us/articles/360000407272)