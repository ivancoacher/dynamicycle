---
id: "115001618871"
title: "将 Klaviyo 嵌入式表单添加到 Shopify 免费主题"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115001618871-Add-a-Klaviyo-Embedded-Form-to-a-Shopify-Free-Theme"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:12Z"
language: "zh"
---
## 概述

本文介绍向 Shopify 商店添加 Klaviyo 注册表单。我们使用 Shopify 的每个免费主题作为示例。每个主题都包含该过程的视频概述。如果您在此处没有看到您的主题，或者您使用的是自定义主题，我们还提供了[本指南末尾的一个部分，介绍了将 Klaviyo 注册表单添加到 Shopify 商店的基本流程](https://help.klaviyo.com/hc/en-us/articles/115001618871#custom-theme10)。您还可以观看下面的视频来了解一般方法。从下面的列表中找到您的主题：

- [布鲁克林](https://help.klaviyo.com/hc/en-us/articles/115001618871#brooklyn)
- [叙述](https://help.klaviyo.com/hc/en-us/articles/115001618871#narrative)
- [供应](https://help.klaviyo.com/hc/en-us/articles/115001618871#supply)
- [Jumpstart](https://help.klaviyo.com/hc/en-us/articles/115001618871#jumpstart)
- [首次亮相](https://help.klaviyo.com/hc/en-us/articles/115001618871#debut)
- [无边](https://help.klaviyo.com/hc/en-us/articles/115001618871#boundless)
- [流行音乐](https://help.klaviyo.com/hc/en-us/articles/115001618871#pop)
- [简单](https://help.klaviyo.com/hc/en-us/articles/115001618871#simple)
- [最小](https://help.klaviyo.com/hc/en-us/articles/115001618871#minimal)
- [自定义主题](https://help.klaviyo.com/hc/en-us/articles/115001618871#custom-theme10)

## 布鲁克林

将 Klaviyo 注册表单添加到 Shopify 的免费 [布鲁克林主题](https://themes.shopify.com/themes/brooklyn/styles/classic)。 ## 叙述

将 Klaviyo 注册表单添加到 Shopify 的免费 [Narrative 主题](https://themes.shopify.com/themes/narrative/styles/warm)。 ## 供应

将 Klaviyo 注册表单添加到 Shopify 的免费 [Supply 主题](https://themes.shopify.com/themes/supply/styles/blue)。 ## 快速启动

将 Klaviyo 注册表单添加到 Shopify 的免费 [Jumpstart 主题](https://themes.shopify.com/themes/jumpstart/styles/jumpstart)。 ## 首次亮相

将 Klaviyo 注册表单添加到 Shopify 的免费 [Debut 主题](https://themes.shopify.com/themes/debut/styles/default)。 ## 无边无际

将 Klaviyo 注册表单添加到 Shopify 的免费 [Boundless 主题](https://themes.shopify.com/themes/boundless/styles/black-white)。 ## 流行音乐

将 Klaviyo 注册表单添加到 Shopify 的免费 [Pop 主题](https://themes.shopify.com/themes/pop/styles/bone)。 ## 简单

将 Klaviyo 注册表单添加到 Shopify 的免费[简单主题](https://themes.shopify.com/themes/simple/styles/light)。 ## 最小

将 Klaviyo 注册表单添加到 Shopify 的免费 [最小主题](https://themes.shopify.com/themes/minimal/styles/vintage)。 ## 自定义主题

要将 Klaviyo 注册表单添加到 Shopify 商店，我们遵循上面每个 Shopify 免费主题的视频中介绍的相同基本方法。本节介绍了针对具有可能与上述示例不完全匹配的自定义主题的用户的此方法的步骤。也就是说，基本过程是相似的，因此请根据需要使用上面的视频作为参考。 1. 在您的 Klaviyo 帐户中，找到您希望将注册客户添加到的列表。点击进入列表，然后点击****注册表单****选项卡。 2. 选择**标准嵌入**选项卡。您可以在此屏幕上编辑样式设置。编辑表单后，滚动到屏幕底部。单击进入代码块以复制表单代码。 3. 切换到您的 Shopify 商店管理员。单击 ****在线商店****，然后从 **操作** 下拉列表中选择 ****编辑代码****。这将打开 Shopify 网页编辑器。 4. 接下来，滚动到 **Snippets** 文件夹并单击 **Add a new snippet****。将您的新片段命名为“klaviyo-form”。将您的 Klaviyo 表单代码粘贴到新代码段中，然后单击 ****保存****。您的 Klaviyo 表单代码现已作为主题文件保存在您的 Shopify 商店中。 5. 接下来，我们将在您商店的页脚中引用您的新代码片段文件。搜索“footer.liquid”文件并单击在网页编辑器中将其打开。 6. 在 `footer.liquid` 文件中找到要添加表单的区域，并使用以下代码行引用您的表单，其中“klaviyo-form”与新代码段的名称匹配。 `{% include 'klaviyo-form' %}`
7. 最后一步是清理所有现有的注册表单。首先，扫描文件中是否存在任何现有的“<form>”元素。如果找到任何内容，请突出显示开始和结束表单元素以及其间的任何代码，然后按“⌘/”注释掉该代码。 8. 搜索包含默认新闻通讯片段的任何声明。 这些将类似于以下内容：
   `{% include '新闻通讯形式' %}`

之后，您的表单应该在店面的页脚中可见。您可以通过以下方式测试该表单：提交电子邮件地址，打开并接受收件箱中的确认电子邮件，然后在 Klaviyo 中检查您的列表以确保电子邮件地址已添加到列表中。