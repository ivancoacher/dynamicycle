---
id: "115005082687"
title: "如何将预览文本插入电子邮件中"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005082687-How-to-insert-preview-text-into-an-email"
section: "Getting started with templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: "zh"
---
## 你将会学到

了解预览文本是什么、它在电子邮件中的默认显示位置以及如何将其插入电子邮件正文中。 ## 关于预览文本

预览文本是电子邮件到达收件箱时收件人首先看到的内容之一。它显示在收件箱中电子邮件主题行之后，通常是从电子邮件正文中的第一行文本中提取的。 ![在 Gmail 收件箱中，电子邮件的预览文本部分会突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28720758454939)

您可以通过两种主要方式使用预览文本来增强您的电子邮件：

1. 使用预览文本来总结电子邮件。 2. 使用预览文本来补充主题行。如果您没有专门插入预览文本，收件箱会自动从电子邮件内的第一行文本中提取它 - 这意味着 ALT 文本、导航栏等可以作为预览文本提取，因此最好指定您希望预览文本显示的确切内容。要详细了解如何有策略地使用预览文本，请[前往 Klaviyo 博客](http://www.klaviyo.com/blog/how-to-use-preheader-text)。仅 Klaviyo 的拖放模板支持此功能。对于自定义 HTML 模板（包括[支持拖放的自定义 HTML 模板](https://help.klaviyo.com/hc/en-us/articles/115005254188-Import-a-Custom-HTML-Template-with-Drag-and-Drop-Support)），您的电子邮件设计者应将所需的预览文本插入到电子邮件代码的开头。对于纯文本电子邮件，电子邮件的开头用作预览文本。 ## 将预览文本添加到流电子邮件中

要在电子邮件预览屏幕上插入流电子邮件的预览文本：

1. 打开包含您要编辑的电子邮件的流程。 2. 单击流消息以打开**电子邮件详细信息**侧栏。 ![预览1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38062196975387)
3. 在**主题和发件人**下，单击内容侧栏中的****编辑****。 4. 在**预览文本**字段中，添加所需的预览文本。 ![preview2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38062169938587)

## 将预览文本添加到营销活动电子邮件中

要在电子邮件预览屏幕上插入营销活动的预览文本：

1. 打开您要编辑的广告活动。 2. 单击 ****下一步****。 3. 在**预览文本**字段中，添加所需的预览文本。 ![preview3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/38062196976411)

## 预览收件箱中的文本

**预览文本**输入会自动添加间隔符，因此只有您输入的预览文本才会显示在客户的收件箱中。 ![一个 Gmail 收件箱，其中包含一封邮件，主题行是你的老板想让你知道的事情和预览文本，给他们数字](https://klaviyo.zendesk.com/hc/article_attachments/28720770371995)

不同的设备和电子邮件客户端对显示的预览文本字符数有不同的限制，较小的屏幕显示的预览字符较少。请记住这一点，并保持预览文本简洁。以下是按电子邮件客户端划分的字符限制：

![电子邮件客户端列出的标题字符限制，Gmail iOS 为 34 个，Outlook.com 为 236 个](https://klaviyo.zendesk.com/hc/article_attachments/28720758448795)
**图片来自 [Acid 上的电子邮件](https://www.emailonacid.com/blog/article/email-development/tips-for-coding-email-preheaders)**

Gmail 可能会从预览文本中删除一组数字中的逗号。例如，在 Gmail 预览版中，10,000 将转换为 10000。 ## 在电子邮件中显示预览文本

在某些情况下，您可能希望在模板正文中显示预览文本。您可以使用以下标签引用您在电子邮件预览屏幕上设置的任何预览文本：

````
{% render_variable Preview_text %}
````

将标签粘贴到模板中的任何文本块中。 ## 隐藏预览文本

如果您想完全隐藏任何预览文本并且仅在客户的收件箱中显示您的主题行，请将下面的代码片段添加到电子邮件的最顶部。此代码将您的电子邮件内容推送到预览文本查看区域，因此它将显示为空白。 1. 将 HTML 块添加到电子邮件的最顶部，位于所有其他内容之上。 2. 添加以下代码片段：

   ````
   <div style="显示：无；最大高度：0px；溢出：隐藏；">͏ &zwnj;
       &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的;
       ͏&zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp;
       ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj;
       &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的;
       ͏&zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp;
       ＆害羞的; &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj;
       &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; &zwnj; &nbsp; ＆害羞的;
       ͏&zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp;
       ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj;
       &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的; ͏ &zwnj; &nbsp; ＆害羞的;
       ͏&zwnj; &nbsp; ＆害羞的;
   </div>
   ````
3. 保存 HTML 块。当您的电子邮件到达收件箱时，客户只会看到您的主题行。 ![Gmail 收件箱显示一封带有主题行的电子邮件，但没有预览文本](https://klaviyo.zendesk.com/hc/article_attachments/28720758451867)

## 其他资源

- [消息个性化参考](https://klaviyo.zendesk.com/hc/en-us/articles/115005084927)
- [模板和设计术语](https://klaviyo.zendesk.com/hc/en-us/articles/14904583929755)