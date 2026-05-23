---
id: "360049181631"
title: "深色模式电子邮件设计最佳实践"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360049181631-Dark-mode-email-design-best-practices"
section: "Design best practices"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:49Z"
language: "zh"
---
## 你将会学到

了解深色模式，这是一些用户打开以使显示器变暗的设备设置。 This setting impacts how emails are displayed.深色模式是在设备级别选择的最终用户设置，Klaviyo 无法直接控制每个设备上如何实现深色模式。 ## 人们为什么使用深色模式？深色模式之所以流行，是因为它被认为具有多种好处。 Users may choose dark mode to:

- 尽量减少眼睛疲劳。 - Support healthier sleep habits. - Extend a device’s battery life. - 提高可访问性。根据 [Litmus](https://www.litmus.com/wp-content/uploads/pdf/Trends-in-Email-Engagement2022.pdf)，在深色模式下查看电子邮件的人数从 2021 年的 28% 增加到 2022 年的 34%。## 深色模式和您的品牌

深色模式通过调整用于在收件箱中呈现电子邮件的 HTML 来影响您的电子邮件品牌。这些调整可以小到反转[纯文本电子邮件](https://help.klaviyo.com/hc/en-us/articles/12415384810651)中的颜色（同时保持 HTML 电子邮件不变），也可以大到调整完全设计的电子邮件模板中的每种颜色。如果您在设计电子邮件时不考虑深色模式，可能会导致文本难以阅读、颜色与您的品牌风格不相符等。 Consider SWAK Cosmetics’ logo. On a white background, it looks great. ![移动设备上的 SWAK 徽标灯模式](https://klaviyo.zendesk.com/hc/article_attachments/28705636951195)

但在深色模式设备上查看时，无法阅读。 ![SWAK 徽标在移动设备上的深色模式下不可见](https://klaviyo.zendesk.com/hc/article_attachments/28705636942747)

请注意此电子邮件标题在浅色和深色模式之间的变化。电子邮件背景颜色、文本颜色和链接栏颜色全部反转。 ## 提供暗模式的设备和操作系统

暗模式变化的具体情况因设备和操作系统而异。 Litmus 提供了有关 [提供暗模式的设备以及它们如何处理 HTML 电子邮件](https://www.litmus.com/blog/the-ultimate-guide-to-dark-mode-for-email-marketers#chart) 的资源。一般来说，收件箱分为以下两类之一：进行最小更改或不进行更改的收件箱，以及反转电子邮件颜色的收件箱。 ### 最小的改变

某些收件箱（例如桌面版 Apple Mail）不会直接更改您的电子邮件内容（除非您包含暗模式元标记）。在此收件箱中，您在深色或浅色模式下看到的消息之间的唯一变化是发件人信息后面的颜色。 ![Bolas 电子邮件在明暗模式下并排](https://klaviyo.zendesk.com/hc/article_attachments/28705636952347)

### 颜色反转

其他收件箱（例如桌面版 Outlook）会部分反转颜色。这意味着一些较浅的颜色会被替换为较暗的色调，而一些较暗的颜色会被替换为较浅的颜色（例如，以前在浅色背景上的深色文本）。最终结果是一封比原始邮件明显更暗的电子邮件。 ![outlook 中同一电子邮件的浅色和深色模式版本](https://klaviyo.zendesk.com/hc/article_attachments/28705636945179)

## 缓解策略

有多种策略可以在优化浅色和深色模式的同时维护您的品牌。选择最适合您团队的能力和品牌需求的一种。 ### 开发设计时考虑浅色和深色模式

如果您使用 Klaviyo 的拖放编辑器发送电子邮件，那么此策略是最好的。开发电子邮件模板，同时牢记它们在深色模式设备上会发生哪些变化：

- 使用在浅色和深色背景下看起来都很棒的徽标和图像，例如 Bola 烘焙食品的徽标和图像。 ![深色和浅色背景上的波拉斯标志](https://klaviyo.zendesk.com/hc/article_attachments/28705636946459)
- 或者在透明背景的深色徽标上添加浅色阴影，使其在深色模式下脱颖而出。 ![深色和浅色背景上的 SWAK 徽标](https://klaviyo.zendesk.com/hc/article_attachments/28705636954907)
- 或者，使用包含背景颜色的图像文件，而不是使用透明背景。如果您选择此选项，请确保您的图像完全填满其占用的空间（例如，全角图像的宽度为 600 像素）。 ![浅色和深色背景上的 Nani 标题](https://klaviyo.zendesk.com/hc/article_attachments/28705636948379)
- 尽可能使用文本，而不是使用包含文本的图像。这允许全颜色反转（另外，它更易于访问）。 ### 自定义代码深色和浅色版本

如果您的开发团队可以从头开始对 HTML 电子邮件进行自定义编码，您可以提供 CSS 来检测查看者是否使用深色模式或浅色模式，并相应地调整设计。这可以覆盖某些收件箱中的某些暗模式默认设置，以便您拥有更多控制权。每个收件箱、设备和操作系统都是不同的，因此在设计电子邮件的深色和浅色模式版本时，您需要考虑各种电子邮件收件人。您可以在电子邮件代码中使用“@media (prefers-color-scheme: dark)”和“[data-ogsc]”专门针对深色模式用户。详细了解[哪些电子邮件客户端支持这些标签](https://www.litmus.com/blog/the-ultimate-guide-to-dark-mode-for-email-marketers#chart) 和[在您自己的设计中使用哪些代码](https://www.litmus.com/blog/the-ultimate-guide-to-dark-mode-for-email-marketers#part2)。 ### 使用纯图像电子邮件

出于多种原因，我们不建议使用仅包含图像的电子邮件：

- 如果没有替代文本，您的电子邮件在收件箱中可能会显得[可疑](https://help.klaviyo.com/hc/en-us/articles/12034571748251)并进入垃圾邮件文件夹。 - 仅图像电子邮件不是可访问性最佳实践，因为它们对许多人和屏幕阅读器来说难以阅读。 - 使用纯图像电子邮件强制采用浅色模式外观会规避订阅者的偏好。不过，很多品牌都采用这种策略，所以这里值得一提。仅图像电子邮件不依赖 HTML 来设置颜色、字体、间距等。这意味着它们不能颠倒，因此收件箱将显示一封通常与您的原始设计一致的电子邮件。 ## 其他资源

- [电子邮件模板编辑器指南](https://help.klaviyo.com/hc/en-us/articles/4407911841435)
- [电子邮件和表单中的辅助功能最佳实践](https://help.klaviyo.com/hc/en-us/articles/360034711931)
- 课程：[电子邮件设计入门](https://academy.klaviyo.com/get-started-with-email-design)