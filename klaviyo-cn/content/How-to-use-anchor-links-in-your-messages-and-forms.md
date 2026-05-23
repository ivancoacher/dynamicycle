---
id: "360043506852"
title: "如何在消息和表单中使用锚链接"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360043506852-How-to-use-anchor-links-in-your-messages-and-forms"
section: "Design best practices"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: "zh"
---
## 你将会学到

了解如何使用锚链接来定位您的注册表单，或在电子邮件和短信中将访问者引导至网页的特定部分。

锚链接是一种为来自不同电子邮件、广告甚至现场活动的客户创建个性化现场体验的简单方法。您可以使用注册表单中的锚链接来定位具有相关内容的不同列表和细分。虽然锚链接与 UTM 参数类似，但您将无法像使用 UTM 参数那样跟踪客户。有关使用 UTM 参数的更多信息，请参阅我们关于 [Klaviyo 中的 UTM 跟踪](https://klaviyo.zendesk.com/hc/en-us/articles/115005247808) 的文章。

## 如何创建锚链接

要创建锚链接，请添加 # 符号，后跟一些描述性单词。例如，如果您希望有人单击您电子邮件中的链接时触发弹出窗口，表明他们有兴趣了解您正在发布的新产品，您可以创建一个如下所示的锚链接。

`https://www.example.com/#newproduct`

从那里，您可以将此 URL 添加到您的消息和表单中。

当有人导航到您创建的锚链接时，他们将登陆没有锚链接的页面（即上例中的 <https://example.com/>）。 ****可选：**** 如果您希望点击锚链接的用户被定向到页面中的特定位置，您可以将 HTML 标签“<a id="newproduct"></a>”添加到网页代码中（将 **newproduct** 替换为您的锚名称）。

## 如何在消息中添加锚链接

要在消息中使用锚链接，请将上面创建的 URL 添加到您的电子邮件和短信中。

### 电子邮件

要在电子邮件中添加锚链接：

1. 将文本、图像或按钮块添加到模板中
2. 在块的设置中，添加带有锚链接的 URL
3. 点击****保存****
   ![带有锚链接的按钮](https://klaviyo.zendesk.com/hc/article_attachments/28716055426971)

如果您想跟踪某人在电子邮件中点击的位置以便稍后在分段中使用，请按照我们关于[使用按钮收集有关收件人的信息](https://klaviyo.zendesk.com/hc/en-us/articles/115005255248) 的文章进行操作。

### 短信

要在 SMS 消息中添加锚链接，请在 SMS 编辑器中粘贴包含锚链接的 URL。请注意，如果您选择缩短链接，锚链接仍然有效。

![带有锚链接的短信](https://klaviyo.zendesk.com/hc/article_attachments/28716065955995)

## 在注册表单中使用锚链接

在您为客户创建了访问锚链接的方式后，您可以使用注册表单为每个浏览器自定义现场内容，使您的品牌看起来更加人性化。

继续上面的示例，如果有人单击电子邮件中的按钮或短信中的链接，目标是将他们定向到全页弹出窗口以注册接收有关产品发布的信息。在注册表单行为中，您可以指定只向点击此特定 URL 的用户显示此表单。为此：

1. 在注册表单生成器中，单击****行为和目标****
2. 向下滚动到 **定位** 部分
3. 选中****仅在某些网址上显示****
4. 将表单设置为仅出现在网址上****包含 > [您的锚点]****（例如，****包含 > #newproduct****）
   ![锚链接的定位表单](https://klaviyo.zendesk.com/hc/article_attachments/28716065958683)

在设置表单之前对其进行测试，然后返回以确保其性能良好。

## 其他资源

- [使用二维码收集订阅者指南](https://academy.klaviyo.com/using-qr-codes-to-gather-subscribers)
- [优化注册表单体验指南](https://academy.klaviyo.com/creating-an- effective-acquisition-strategy-using-signup-forms)
- [添加到按钮、链接或图像的日历事件](https://klaviyo.zendesk.com/hc/en-us/articles/360043932991)