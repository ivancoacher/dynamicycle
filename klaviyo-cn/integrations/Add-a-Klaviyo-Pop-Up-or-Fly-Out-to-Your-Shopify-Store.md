---
id: "115005080847"
title: "将 Klaviyo 弹出窗口或飞出窗口添加到您的 Shopify 商店"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005080847-Add-a-Klaviyo-Pop-Up-or-Fly-Out-to-Your-Shopify-Store"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "zh"
---
## 概述

如果您有兴趣向 Shopify 商店添加新的注册表单，Klaviyo 提供了一种构建三种不同类型表单的简单方法：

- 嵌入表格
- 弹出/模式表单
- 飞出表格

本文将介绍如何通过将 Klaviyo 表单代码添加到您的 Shopify 商店主题来在您的网站上启动并运行这些表单。

要首先探索如何在 Klaviyo 中创建和自定义这些表单，请[查看本指南](https://help.klaviyo.com/hc/en-us/articles/360001910631)。

## 将 Klaviyo 表单代码添加到您的网站

在 Klaviyo 中完成弹出窗口或飞出窗口的自定义后，就可以将其添加到您的 Shopify 商店了。为此，请在新选项卡中打开 Shopify 商店的后端，然后导航至****销售渠道 > 在线商店 > 主题。****

进入****主题****后，单击右上角的小省略号，然后单击****编辑代码********。**

![shopifyEditCode.png](https://klaviyo.zendesk.com/hc/article_attachments/28720891831067)

从那里，将您的代码粘贴到 ****theme.liquid**** 模板中紧邻“<body>”起始标记之后。

![](https://klaviyo.zendesk.com/hc/article_attachments/28720846741019)

将代码粘贴到模板中后，请访问您商店的 URL 以确保一切正常。这就是我们的基本弹出窗口的样子：

![](https://klaviyo.zendesk.com/hc/article_attachments/28720891849627)

这就是我们的基本飞出的样子：

![](https://klaviyo.zendesk.com/hc/article_attachments/28720846746267)

## 常见问题解答

****每次有人访问我的网站时，即使他/她已经订阅，我的弹出或飞出表单都会显示吗？****

默认情况下，当用户关闭飞出窗口或弹出窗口时，此人将在一段时间内不会再次看到该表单。您可以通过查看下面的自定义弹出窗口和飞出窗口指南来调整此设置。

****如果有人访问我的网站并关闭一个弹出窗口，当此人继续浏览时，它会阻止我的其他表单出现吗？****

如果用户关闭飞出窗口或弹出窗口，则当用户继续浏览网站时，网站上的所有其他飞出窗口和弹出窗口将保持关闭状态。这也是可以调整的。

#### 了解更多

有兴趣对您的弹出窗口或飞出表单进行更多自定义吗？

- [查看我们的弹出窗口自定义指南](https://help.klaviyo.com/hc/en-us/articles/115005249548-Customize-a-Pop-Up-or-Modal-Form)
- [查看我们的飞出定制指南](https://help.klaviyo.com/hc/en-us/articles/115005249528-Customize-a-Fly-Out-Form)