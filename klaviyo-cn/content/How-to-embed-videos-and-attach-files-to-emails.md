---
id: "115005256968"
title: "如何嵌入视频并将文件附加到电子邮件"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005256968-How-to-embed-videos-and-attach-files-to-emails"
section: "Getting started with templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:25Z"
language: "zh"
---
## 你将会学到

了解可以嵌入到电子邮件中的内容类型，以及如何避免因嵌入不受支持的内容而导致的送达问题。 ## 关于嵌入内容和附件

大多数主要电子邮件客户端（例如 Gmail）将调查、表单、视频和其他小部件等嵌入式内容视为安全威胁。这些电子邮件客户端通常会完全删除此嵌入代码，并且您的收件人在打开您的电子邮件时将看不到呈现的内容。 Klaviyo 致力于帮助我们的客户取得成功。由于我们的测试表明这些功能无法在所有主要电子邮件客户端上可靠地呈现，因此我们不支持在 Klaviyo 电子邮件中嵌入调查、表单、视频或小部件。也就是说，有几种方法可以确保良好的送达率，同时仍然为您的电子邮件订阅者提供独家内容的访问权限。 - 了解如何[通过电子邮件传送视频内容](https://help.klaviyo.com/hc/en-us/articles/115005256968#h_01J4MDQQ0XMJC9HQXDRCCBNKY5)
- 了解如何[通过电子邮件发送附件和文件](#h_01HE3NARPVQ7PVM7SA1TJJ2AFM)
- 了解如何[通过电子邮件发起调查](#h_01HE3NARPWVVV8CE6YS2H1Z3X0)

## 使用块通过电子邮件传送视频

使用带有播放按钮的静态图像是在电子邮件中展示视频的最常见（也是推荐）的方法。该图像应链接到视频的托管版本（例如，Youtube 或 Vimeo 上托管的视频）。 Klaviyo 提供了一个视频块来简化此过程。 1. 复制视频的 URL（例如，从 Youtube、TikTok、Vimeo 或其他视频托管平台）。 2. 在 Klaviyo 中打开电子邮件模板。 3. 将 ****Video**** 块拖到电子邮件中。 ![视频块图标](https://klaviyo.zendesk.com/hc/article_attachments/28723629942427)
4. 将视频 URL 粘贴到 **视频 URL** 字段中。 5. 对于视频的缩略图：
   1. 如果您使用 Youtube 托管视频，Klaviyo 会自动检测视频缩略图。请注意，Youtube Shorts 不支持自动缩略图检测，仅支持标准 Youtube 视频。 2. 如果您的视频托管在其他地方，请单击****选择图像****上传缩略图。 ![上传缩略图的选项](https://klaviyo.zendesk.com/hc/article_attachments/28723624611995)
6. 调整块的外观，包括打开或关闭播放按钮以及更改块的****样式****选项卡中的块填充。当有人打开您的电子邮件时，他们会看到一个看起来像视频播放器的图像。当他们点击它时，他们将被重定向到一个网页，视频将在其中自动播放。 ### 添加 GIF

如果您要分享的视频剪辑很短并且没有声音，请尝试使用 GIF。只要 GIF 动画大小小于 5 MB，就可以在电子邮件中使用。您可以像上传 JPEG 或 PNG 一样上传 GIF，只需将其拖到电子邮件模板中即可。 ![Klaviyo 电子邮件编辑器中的 gif](https://klaviyo.zendesk.com/hc/article_attachments/28723624605467)

## 在电子邮件中包含附件

要在电子邮件中包含 PDF、Word 文档或 Google 文档等附件，您首先需要在线托管文件，例如在您的网站、Google Drive 或 Dropbox 中。将文件上传到内容管理系统后，复制该文档的链接。要访问 Google 云端硬盘中文档的共享链接：

1. 单击项目卡右上角的 **更多选项** 图标（三个点），如果使用列表视图，则单击最右侧。 2. 打开****共享****菜单。 3. 单击****复制链接****。 ![Google Drive 文件，打开菜单可复制公共链接](https://klaviyo.zendesk.com/hc/article_attachments/28723624608283)
4. 为确保您的文件对收件人可见，请重新打开菜单，然后单击****共享 > 共享****，并将权限设置为****拥有链接的任何人****和****查看者****。然后，将链接插入您的电子邮件中。您可以将链接添加到电子邮件中的几乎任何元素，包括：

- 一个 CTA 按钮
- 一张图片
- 文本块中的文本

详细了解[使用电子邮件编辑器](https://help.klaviyo.com/hc/en-us/articles/4407911841435)。 ## 通过电子邮件发起调查

大多数调查平台都提供了一种根据收件人单击的按钮预先填充调查中的第一个问题的方法。了解如何[使用链接在 Typeform 调查中预选答案](https://www.typeform.com/help/a/preselect-answers-through-typeform-links-for-advanced-users-4410202791060/)。 通过调查平台生成这些链接后，请在电子邮件中为每个答案选项添加相应的按钮。例如，如果您的电子邮件询问“您对购买的产品满意吗？”，您可以在电子邮件中添加表示“非常满意”、“有些满意”和“不满意”的按钮。然后为每个按钮添加相应的链接。当收件人单击按钮时，他们将看到一项调查，并自动选择答案。