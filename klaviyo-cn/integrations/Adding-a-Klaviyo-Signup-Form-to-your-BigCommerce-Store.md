---
id: "115000099192"
title: "将 Klaviyo 注册表单添加到您的 BigCommerce 商店"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115000099192-Adding-a-Klaviyo-Signup-Form-to-your-BigCommerce-Store"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:10Z"
language: "zh"
---
## 概述

本指南逐步介绍如何将 BigCommerce 注册表单同步到 Klaviyo 列表。

如果您的商店中没有现有注册表单，或者对如何将现有订阅者列表和注册表单完全迁移到 Klaviyo 感兴趣，请浏览以下两个指南：

- [将现有注册表单重定向至 Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005080167-Redirect-Existing-Sign-Up-Forms-to-Klaviyo)
- [将现有订阅者（和取消订阅者）迁移到 Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005078487-Migrate-Existing-Subscribers-and-Unsubscribes-into-Klaviyo)


## 将 BigCommerce 表单同步到 Klaviyo 列表

首先选择要同步的列表，然后通过编辑 BigCommerce 主题源文件将 BigCommerce 注册表单替换为 Klaviyo 表单。

1. 从 BigCommerce 仪表板中，导航至****店面 > 我的主题****。
2. 现在，从 BigCommerce 仪表板导航至****店面设计 > 我的主题****。
3. 在 **当前主题框中**，单击 ****高级设置下拉菜单****，然后单击 ****编辑主题文件****。这将打开网页编辑器。
   ![bc_editTheme.png](https://klaviyo.zendesk.com/hc/article_attachments/28720845992987)

   #### 注意

   如果您使用默认主题，则不会出现**编辑主题文件**选项。首先制作主题的副本，然后对该副本进行编辑。如果您是 BigCommerce 新手或者您之前从未编辑过默认主题，则很可能会出现这种情况。
4. 导航到模板 > 组件 > 通用 > 订阅表单.html**。单击****subscription-form-html**** 在网络编辑器中打开该文件。
   ![signupFormSubscriptionTemplate.png](https://klaviyo.zendesk.com/hc/article_attachments/28720891042587)
5. 下一步是将现有源代码替换为默认的 Klaviyo 表单代码。在您的 Klaviyo 帐户中，导航到您想要同步的列表，然后点击 ****注册表单**** 链接。
6. 选择您要使用的注册表单样式，然后复制源代码。
7. 切换回 BigCommerce 网页编辑器，将 Klaviyo 注册表单源代码粘贴到 **subscription-form.html** 文件中。您应该粘贴所有现有的源代码。
   ![signupFormKlaviyoCode.png](https://klaviyo.zendesk.com/hc/article_attachments/28720845986843)
8. 单击 ****保存并应用文件****。

您现在可以检查您的店面以验证是否已添加新的注册表单。输入测试电子邮件地址并确认订阅以验证注册是否正常。

从这里，您可以在 Klaviyo UI 中或直接编辑源代码来编辑表单的样式。 更新 UI 中的任何样式都会更新 UI 中的源代码。您必须复制此源代码并将其粘贴到您的 **subscription-form.html** 文件中，才能将这些更改推送到您的店面。

## 故障排除

如果您遇到任何表单问题，请记住您正在编辑原始主题的副本。通过应用原始主题、访问编辑器并复制所需的源，可以访问所有原始的、未经编辑的文件。