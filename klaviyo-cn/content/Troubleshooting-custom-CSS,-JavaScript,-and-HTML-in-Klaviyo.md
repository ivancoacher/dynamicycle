---
id: "115005254488"
title: "对 Klaviyo 中的自定义 CSS、JavaScript 和 HTML 进行故障排除"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254488-Troubleshooting-custom-CSS-JavaScript-and-HTML-in-Klaviyo"
section: "Template troubleshooting "
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "zh"
---
## 你将会学到

了解如何在[导入自定义 HTML 模板](https://help.klaviyo.com/hc/en-us/articles/115005254068-Import-a-Custom-HTML-Template-into-Klaviyo) 或构建您自己的自定义编码模板时对自定义代码进行故障排除。

我们仅建议精通技术的营销人员或有权访问开发人员的任何人使用自定义 HTML。虽然我们的产品确实支持自定义 HTML，但我们的支持团队除了提供本文档中涵盖的一般指导之外，无法帮助您构建自定义模板。

为了维护您的数据安全，Klaviyo 的支持团队无法打开您的 HTML 文件。

## 自定义 HTML 和 CSS 元素

如果您要创建自定义 HTML 模板，则无法在电子邮件中使用产品 Feed。

目前不支持某些用于使电子邮件具有交互性的 HTML 和 CSS 元素。例如，如果您希望使用某些 CSS 属性选择器在 Gmail 中实现电子邮件交互，则您的模板可能会在 Klaviyo 中触发错误。

Klaviyo 目前不支持电子邮件模板中的某些运算符（例如 ~）。这可能会限制某些自定义 HTML 和 CSS 的使用范围。如果您的模板包含不完全支持的 HTML 或 CSS，您将无法生成电子邮件预览，而是会看到一条错误消息。

## 常见的 HTML 问题

如果您发现自定义 HTML 电子邮件看起来不正确，可以在以下几个常见位置检查问题。

### 字体中的单引号

无论您在 CSS 中的何处添加 font-family 属性，请查找单引号或不必要的引号。添加字体时删除所有引号。

|  |  |
| --- | --- |
| ****问题**** | ****已修复**** |
|字体系列：'Helvetica Neue'、Helvetica、Arial |字体系列：Helvetica Neue、Helvetica、Arial |

### 媒体查询

如果媒体查询不是标准格式，它们将无法正确呈现。遵循所有媒体查询的标准格式。

|  |
| --- |
| ****标准媒体查询格式**** |
| @media only 屏幕和（最大宽度：460px）|

### 不必要的中心标签

如果您的电子邮件模板中有多个 HTML <center> 标记，则它可能无法在 Gmail 中正确呈现。要解决此问题，请删除所有不必要的 <center> 标记。电子邮件模板顶部 <body> 标记附近只需要一个 <center> 标记。所有附加的 <center> 标签都是多余的。

## Klaviyo 不支持 JavaScript 电子邮件

大多数电子邮件客户端（Gmail、Hotmail、Yahoo 等）将电子邮件中的 JavaScript 视为安全威胁。这是因为脚本可以隐藏恶意内容。因此，这些主要电子邮件客户端完全阻止电子邮件中的脚本。鉴于电子邮件中与 JavaScipt 相关的固有安全威胁，以及大多数主要电子邮件客户端缺乏对此类脚本的支持，任何添加的脚本都将被自动删除。

## Klaviyo 不支持嵌入表单或视频

Klaviyo 不支持模板中嵌入的表单、小部件或视频。这是因为我们的测试表明这些类型的功能无法在所有主要电子邮件客户端上可靠地呈现。与 JavaScript 片段类似，大多数电子邮件客户端将这些元素视为安全威胁，并将它们从电子邮件中完全删除。

如果您有兴趣了解此问题的解决方法，请[查看这篇有关向电子邮件添加视频或 GIF 的文章](https://help.klaviyo.com/hc/en-us/articles/115005256968)。

## 其他不支持的标签和属性

这里介绍的 HTML 标签和属性并不是 Klaviyo 支持的详尽列表。一般来说，[主要收件箱提供商支持](https://www.caniemail.com/) 的 HTML 元素也受 Klaviyo 支持。

如果您的模板具有不受支持的 HTML，Klaviyo 将尝试用受支持的替代元素（即 span 标签）替换不受支持的元素。如果没有明确的替换，则 HTML 的该部分将被删除。如果 HTML 的某些部分在添加后似乎消失了，这意味着它们可能不受支持；尝试使用替代的 HTML 标记或属性来实现类似的效果。

## 其他资源

- [如何导入自定义 HTML 模板](https://klaviyo.zendesk.com/hc/en-us/articles/115005254068)
- [电子邮件模板错误消息疑难解答](https://klaviyo.zendesk.com/hc/en-us/articles/4402386684187)