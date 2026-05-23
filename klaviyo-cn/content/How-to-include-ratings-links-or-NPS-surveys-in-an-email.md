---
id: "115005084627"
title: "如何在电子邮件中包含评级链接或 NPS 调查"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005084627-How-to-include-ratings-links-or-NPS-surveys-in-an-email"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:21Z"
language: "zh"
---
## 你将会学到

了解如何通过电子邮件发送简单的调查以收集用户信息，然后将该信息作为自定义属性发送回 Klaviyo。一个常见的用例是在电子邮件或 NPS 调查中包含评级链接。

## 配置您的电子邮件模板来收集用户评分

使用下面提供的代码片段时，请确保使用直引号 (') 而不是弯引号 (')，以确保代码正确呈现。这可以通过复制下面的代码并使用“粘贴为纯文本”功能（Ctrl+Shift+V 或 Cmd+Shift+V）将其直接粘贴到模板中来实现。

1. 在电子邮件模板中，拖入 **标题** 块。
2. 在**桌面布局**和**移动布局**菜单中，选择****仅限链接和按钮****。
3. 在块设置的**内容**部分中，单击****添加链接****，直到您有 10 个链接字段（或根据需要添加任意数量）。
4. 对于**链接 1**，在 **文本** 字段中添加数字 1。对**链接 2** 中的数字 2 重复，依此类推。
5. 在每个链接的 **链接地址** 字段中添加以下标签：
   `{% update_property_link 'profile_property' 'property_value' 'redirect_link' %}`
6. 将上述标签中的通用占位符替换为以下信息：
   - ****profile\_property**** 应记录在某人的个人资料上的自定义属性名称（例如“NPS 评级”）。
   - ****property\_value**** 为自定义属性记录的实际值，如本示例中的数字 1-10。
   - ****redirect\_link****这是某人在选择一个值后将被带到的 URL（例如，您的网站主页）。

在下面的示例中，按钮 ****1**** 的完整标记为：

````
{% update_property_link 'NPS 评级' '1' 'https://botanic-organics.com/' %}
````

按钮 ****2**** 的完整标签是：

````
{% update_property_link 'NPS 评级' '2' 'https://botanic-organics.com/' %}
````

![电子邮件模板中的NPS配置.png](https://klaviyo.zendesk.com/hc/article_attachments/34368159432475)

收件人单击按钮后，他们将被带到您指定为重定向 URL 的 URL，并且该值将作为自定义属性自动添加到他们的个人资料中。请注意，如果有人回复使用相同 ****profile\_property**** 的多封 NPS 调查电子邮件，他们输入的新值将覆盖他们之前的回复。

## 预览您的模板

当您预览模板并单击任何评级链接时，您将被定向到占位符页面，而不是更新属性标记中提供的链接。

![从预览电子邮件中单击“更新属性”链接时显示的占位符](https://klaviyo.zendesk.com/hc/article_attachments/28723517937819)

如果您想测试链接或按钮的完整功能，请按照我们的指南向自己发送一封实时电子邮件：[如何在 Klaviyo 中发送个人电子邮件](https://klaviyo.zendesk.com/hc/en-us/articles/115005246328)。

## 其他资源

- [如何根据动态变量显示或隐藏模板块和部分](https://klaviyo.zendesk.com/hc/en-us/articles/7655965301531)
- [创建购买后流程指南](https://klaviyo.zendesk.com/hc/en-us/articles/360028872611)