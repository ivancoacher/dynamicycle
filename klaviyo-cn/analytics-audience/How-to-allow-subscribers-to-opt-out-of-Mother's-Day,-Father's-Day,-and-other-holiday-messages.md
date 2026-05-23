---
id: "5495696206363"
title: "如何允许订阅者选择退出母亲节、父亲节和其他节日消息"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/5495696206363-How-to-allow-subscribers-to-opt-out-of-Mother-s-Day-Father-s-Day-and-other-holiday-messages"
section: "List and segments best practices"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T12:54:29Z"
language: "zh"
---
## 你将会学到

了解如何为您的订阅者提供选择退出与特定节日相关的电子邮件和短信的选项，例如[母亲节](https://www.klaviyo.com/blog/mothers-day-emails)、[父亲节](https://www.klaviyo.com/blog/fathers-day-marketing)、BFCM 或圣诞节。然后，了解如何排除那些选择退出这些消息的人。对于社区中的某些成员来说，假期可能是一年中的敏感时间，因此允许订阅者选择退出可能是建立信任并提供更好的客户体验的一种方式。 ## 创建一个带有选择退出按钮的模板

您可以通过发送带有[更新属性链接](https://klaviyo.zendesk.com/hc/en-us/articles/115005255248)的营销活动，为订阅者提供选择退出假日电子邮件的选项。使用下面提供的代码片段时，请确保使用直引号 (') 而不是弯引号 (')，以确保代码正确呈现。这可以通过复制下面的代码并使用“粘贴为纯文本”功能（Ctrl+Shift+V 或 Cmd+Shift+V）将其直接粘贴到模板中来实现。 1. 导航至****模板 > 创建模板****，然后按照提示创建新的电子邮件模板。 2. 将按钮块添加到您的模板中。 3. 在按钮块的 **URL** 字段中，粘贴以下代码片段之一：
   母亲节：`{% update_property_link 'mothers_day_opt_out' 'True' 'REDIRECT_LINK' %}`
   父亲节：`{% update_property_link 'fathers_day_opt_out' 'True' 'REDIRECT_LINK' %}`


   根据需要使用其他属性名称，例如 BFCM\_opt\_out。 ![带有父亲节退出按钮的 Klaviyo 电子邮件模板](https://klaviyo.zendesk.com/hc/article_attachments/28713339359515)

   SMS 和 MMS 不支持 update\_property\_link。 4. 将粘贴代码中的“REDIRECT_LINK”替换为您网站上构建的确认页面的链接。 5. 填写按钮文本。使用与您的品牌相符的号召性用语，并明确表明单击按钮将使您退出母亲节或父亲节消息。更新属性链接在整个模板编辑器中都有效，而不仅仅是在按钮块中。如果您的设计需要，您可以在任何 URL 字段中使用更新属性链接代码，或者在文本块中使用超链接文本。添加选择退出按钮后，请完成营销活动的设计，以便准备发送。 ## 测试功能并发送活动

为了确保您的按钮正常工作，请将其发送给自己来测试其功能。按照以下说明发送带有功能按钮的实时电子邮件。不要向自己发送预览电子邮件，因为预览消息中的更新属性 URL 使用占位符链接。 1. 通过搜索您自己的电子邮件地址导航到您在 Klaviyo 中的个人资料。 ![Search_for_profile.gif](https://klaviyo.zendesk.com/hc/article_attachments/28713339352603)
2. 单击个人资料右上角的****消息****。 3. 单击“消息”选项卡中的****发送电子邮件****。 4. 单击****继续发送电子邮件****，然后按照提示选择您在上一步中构建的模板，将其设置为立即发送。 5. 一旦您在收件箱中收到消息，请单击选择退出链接。 6. 像在步骤 1 中一样导航回您的个人资料。 7. 在 **自定义属性** 部分中，找到属性 **mothers\_day\_opt\_out: True** 或 **fathers\_day\_opt\_out: True**。如果您在自己的个人资料中看到该属性，则可以确定该按钮按预期工作。将活动发送给您的受众，收集他们对母亲节或父亲节信息的偏好。 ## 创建一个分段并将其从假期发送中排除

将选择退出营销活动发送给您的订阅者后，创建一个细分来识别那些不希望收到该假期营销活动的用户。使用以下分段定义，将 **mothers\_day\_opt\_out** 替换为您的假期选择退出属性：

****关于某人的属性 > mothers\_day\_opt\_out 为 True****

![Opt_out_is_true.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713384009371)

随着更多订阅者分享他们的偏好，该部分将继续更新。当您准备好发送假日消息时，请在“**不发送至**”字段中的“**收件人**”下选择此分段。在安排邮件时，请务必选择****在发送时确定收件人****，以便使用最新版本的分段。 ![campaign_setup.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713339338395)