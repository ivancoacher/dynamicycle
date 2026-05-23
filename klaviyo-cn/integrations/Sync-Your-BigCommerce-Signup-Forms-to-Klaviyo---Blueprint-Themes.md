---
id: "115005254988"
title: "将您的 BigCommerce 注册表单同步到 Klaviyo - 蓝图主题"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254988-Sync-Your-BigCommerce-Signup-Forms-to-Klaviyo-Blueprint-Themes"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "zh"
---
## 概述

本指南逐步介绍如何将 BigCommerce 注册表单同步到 Klaviyo 列表。

## 将 BigCommerce 表单同步到 Klaviyo 列表

首先选择要同步的列表，然后通过编辑 BigCommerce 主题源文件将 BigCommerce 注册表单替换为 Klaviyo 表单。

1. 从 BigCommerce 仪表板中，导航至****店面 > 我的主题****。
2. 在当前主题中，单击****编辑 HTML/CSS**** 链接。这将打开网页编辑器。
   ![bc_editBPtheme.png](https://klaviyo.zendesk.com/hc/article_attachments/28722594733467)
3. 导航到 ****其他模板文件 > 面板**** 并单击 ****SideNewsletterBox********.html**** 文件。这会将 SideNewsletterBox.html 文件加载到 Web 编辑器中。
   ![bc_BPsideNewsletterBox.png](https://klaviyo.zendesk.com/hc/article_attachments/28722556305947)
4. 下一步是将现有源代码替换为默认的 Klaviyo 表单代码。在您的 Klaviyo 帐户中，导航到您想要同步的列表，然后点击****注册表单****链接。
5. 选择您要使用的注册表单样式，然后复制源代码。
6. 切换回 BigCommerce 网页编辑器，将 Klaviyo 注册表单源代码粘贴到 **SideNewsletterBox.html** 文件中。您应该粘贴所有现有代码。
   ![blueprintSignupFormKlaviyoCode.png](https://klaviyo.zendesk.com/hc/article_attachments/28722594738331)
7. 单击 ****保存****。

您现在可以检查您的店面以验证是否已添加新的注册表单。输入测试电子邮件地址并确认订阅以验证注册是否正常。

从这里，您可以在 Klaviyo UI 中或直接编辑源代码来编辑表单的样式。 更新 UI 中的任何样式都会更新 UI 中的源代码。您必须复制此源代码并将其粘贴到您的 **subscription-form.html** 文件中，才能将这些更改推送到您的店面。

## 故障排除

如果您遇到任何表单问题，可以通过点击 ****恢复为原始格式来恢复为 BigCommerce 主题文件的原始格式。****

![647770](https://klaviyo.zendesk.com/hc/article_attachments/28722594729755)