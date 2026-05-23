---
id: "115005085387"
title: "在 Microsoft Outlook 中查看我的电子邮件时看起来有所不同"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005085387-My-email-looks-different-when-viewed-in-Microsoft-Outlook"
section: "Template troubleshooting "
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:21Z"
language: "zh"
---
## 你将会学到

了解为什么某些电子邮件在 Microsoft Outlook 中看起来与其他收件箱不同，以及提高邮件在 Outlook 中呈现方式一致性的提示。

## Outlook 的渲染引擎

虽然 Outlook 的某些版本使用 Webkit（一种以预期方式解释和呈现 HTML 的现代浏览器引擎）来显示电子邮件，但许多其他版本使用 Microsoft Word 作为呈现引擎。

考虑一下您上次尝试在 Microsoft Word 中编辑表格或调整图像大小的情况。使用 Word 时面临的格式设置挑战与 Outlook 收件箱中的电子邮件面临的挑战类似。

因此，电子邮件在 Outlook 中的外观可能与您最初在 Klaviyo 中设计和预览时的外观略有不同。

如果您选择针对 Outlook 优化电子邮件，请使用 [Klaviyo 的内置收件箱测试](https://klaviyo.zendesk.com/hc/en-us/articles/37463094051611) 在各种设备和收件箱上预览邮件。

## 针对 Outlook 优化您的电子邮件

您可能会在 Outlook 中看到以下问题：

- div 和表格单元格中的背景图像不支持或不显示
- CSS 浮动和位置元素被忽略
- 不支持或不显示文本阴影
- 由于对这些元素的支持不佳，导致不寻常的填充和边距
- 由于对这些元素的支持较差，CSS 宽度和高度未按预期显示
- 嵌套元素的背景颜色显示不正确或被忽略

由于没有既定的指导方针，专门针对最新版本的 Outlook 优化电子邮件可能需要大量时间和大量测试。执行此操作还需要对图像的放置方式进行重大更改，这可能会影响电子邮件在其他电子邮件客户端和设备上的呈现方式。

### 调整 Outlook 图像的大小

Outlook 收件箱中的一个常见问题是图像被拉伸或过大。为了避免这种情况，请为模板中的每个图像设置宽度。

1. 选择一个图像块。
2. 将数字添加到 **图像布局 > W** 字段。对于全宽图像，请使用 600 像素（或您的电子邮件设置的任何宽度，可在 **样式** 部分找到）。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32083288343067)
3. 保存您的更改。

Outlook 中的 ### GIF

Outlook 不支持电子邮件中的 GIF。 Outlook 不会显示移动图像，而是选择 GIF 的第一帧并将其显示为静态图像。

## 了解 Outlook 对受众的影响

要查看使用 Outlook 打开电子邮件的受众百分比：

1. 导航至 Klaviyo 中的****营销活动****选项卡。
2. 单击最近发送的营销活动。
3. 单击活动摘要的****送达率****选项卡。
4. 查看**按电子邮件域的性能**部分，了解使用 Outlook 与您的邮件进行交互的收件人的百分比。

## 其他资源

- [如何在电子邮件中使用图像](https://help.klaviyo.com/hc/en-us/articles/115005253688-How-to-use-images-in-emails)
- [如何针对移动设备优化电子邮件](https://help.klaviyo.com/hc/en-us/articles/115005254428-Optimize-Your-Emails-for-Mobile)
- [了解 CSS 优化](https://help.klaviyo.com/hc/en-us/articles/360049848692-Understanding-CSS-Optimization-)