---
id: "115005254068"
title: "如何导入自定义 HTML 模板"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254068-How-to-import-a-custom-HTML-template"
section: "Advanced template design"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: "zh"
---
## 你将会学到

了解如何将自定义 HTML 模板导入 Klaviyo。

我们仅建议精通技术的营销人员或有权访问开发人员的任何人使用自定义 HTML。虽然我们的产品确实支持自定义 HTML，但我们的支持团队除了提供本文档中涵盖的一般指导之外，无法帮助您构建自定义模板。为了维护您的数据安全，Klaviyo 的支持团队无法打开您的 HTML 文件。

## 上传自定义 HTML 模板

自定义 HTML 模板必须是 .html 文件，并且必须包含取消订阅链接（即 {% unsubscribe %} 或 {% unsubscribe\_link %} 标记）。了解有关[在 Klaviyo 中取消订阅](https://help.klaviyo.com/hc/en-us/articles/115005078267) 的更多信息。

1. 导航至****内容 > 模板****。
2. 选择****电子邮件模板****选项卡。
3. 单击****导入****。
4. 输入名称并上传模板的 HTML 文件。
5. 上传 HTML 中引用的任何图像或资源。
6. 单击****导入模板****。

不建议导出在 Klaviyo 拖放编辑器中构建的模板，然后将其导入回 Klaviyo，这可能会导致模板功能出现问题。

****删除不支持的模板标签和变量****

当您从其他电子邮件服务提供商导出模板时，它可能包含 Klaviyo 不支持的标签和变量。在导入 HTML 文件之前，请删除这些标签（如果需要，请将其替换为 [Klaviyo 个性化标签](https://help.klaviyo.com/hc/en-us/articles/4408802648731)）。

例如，请参阅下面的消息和 HTML。此邮件是从另一个电子邮件服务提供商导出的，包含当前年份的标签、公司地址等。这些外部标签与 Klaviyo 不兼容。

![带有不受支持标签的模板](https://klaviyo.zendesk.com/hc/article_attachments/28716302197275)

![包含不受支持标签的模板的 HTML](https://klaviyo.zendesk.com/hc/article_attachments/28716302194331)

Klaviyo 模板标签包含在大括号内。变量由两对大括号包围（例如，“{{first_name }}”），模板标签由一对大括号和百分号包围（例如，“{% unsubscribe %}”）。如果模板中的模板标签和变量用其他字符表示，Klaviyo 将不支持它们。

### 添加图像和附件（可选）

您可以通过上传包含附件的 zip 文件并通过模板中的文件名引用它们来引用图像和附件。

当您单击导入模板时，这些图像和资源会自动添加到我们的 CDN，并且它们的引用会在您的模板中更新。

## 将隐藏预览文本添加到自定义 HTML 模板

如果您想设置自定义 HTML 模板的预览文本（而不是让收件箱从邮件内容中提取预览文本），请将下面的代码块添加到您的模板中。此代码应立即添加到模板的开始“<body>”标记之后。

````
<div style="显示：无；字体大小：1px；行高：1px；最大高度：0px；最大宽度：0px；不透明度：0；溢出：隐藏；">
在此处插入预览文本。
</div>
````

## 表情符号和自定义 HTML 模板

截至 2024 年 2 月，所有 Klaviyo 电子邮件编辑器（即拖放编辑器、混合编辑器、纯文本编辑器和自定义 HTML 编辑器）均支持所有表情符号。

## 其他资源

- [Klaviyo 中的自定义 CSS、JavaScript 和 HTML 故障排除](https://klaviyo.zendesk.com/hc/en-us/articles/115005254488)
- [如何导入支持拖放的自定义 HTML 模板](https://klaviyo.zendesk.com/hc/en-us/articles/115005254188)