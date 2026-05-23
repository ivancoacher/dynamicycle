---
id: "360023213971"
title: "如何设置 iOS 推送通知"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360023213971-How-to-set-up-iOS-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:50:07Z"
language: "zh"
---
您必须是所有者或管理员才能设置移动推送通知

## 你将会学到

了解如何在您的 Klaviyo 帐户中设置推送通知。完成本文中的步骤后，您将能够在流程和营销活动中发送推送通知。

## 开始之前

在 Klaviyo 中使用推送通知有 3 个先决条件：

1.您必须拥有自己的原生移动iOS应用程序。
2. 您必须从 Apple 生成 APNs 身份验证密钥，并将其上传到 Klaviyo（更多详细信息如下）。
3. 您必须安装 [Klaviyo SDK](https://github.com/klaviyo/klaviyo-swift-sdk) 并在您的 iOS 应用程序中设置事件跟踪和推送通知。

## 在 Klaviyo 中设置推送通知

1. 单击左下角您的组织名称。
2. 导航至****设置 >**** ****推送通知****。
3. 单击 iOS 部分中的****启用****。
   ![ios推送通知可以通过点击启用按钮打开](https://klaviyo.zendesk.com/hc/article_attachments/28717387111323)
4. 填写所需信息。
   请注意，您需要正确的角色才能访问您的 APNs 通知密钥和密钥 ID。您可以[在此处查看 Apple 的角色和权限](https://developer.apple.com/support/roles/)。

   1. 登录您的 [App Store Connect](https://appstoreconnect.apple.com/apps) 或 [Apple Developer](https://developer.apple.com/account) 帐户。
   2. 单击****我的应用****。
   3. 选择您的应用程序，您的捆绑包 ID 可在****应用程序信息**** 选项卡上找到。
      请注意，捆绑包 ID 区分大小写，并且应类似于以下内容：
      **com.YOUR\_APP\_NAME.**
      ![设置 iOS 推送通知所需的信息](https://klaviyo.zendesk.com/hc/article_attachments/28717380841243)

   - ****APN 身份验证密钥****
     如果您还没有，请[创建 APNs 身份验证密钥](https://developer.apple.com/account/ios/authkey/create)。请务必将密钥类型设置为 **APNs**。
     创建密钥后，下载 .p8 文件，并将其上传到您的 Klaviyo 帐户。
   - ****密钥 ID****
     要查找您的密钥 ID，请[导航到您的密钥列表](https://developer.apple.com/account/ios/authkey/)。单击您的密钥以展开详细信息，然后复制密钥 ID。
   - ****团队ID****
     在此处找到您的[团队 ID](https://developer.apple.com/account/#/membership)。
   - ****捆绑包 ID****
     要查找您的捆绑包 ID：
5. 填写完所有必填信息后，单击****设置 iOS Push****。

绿色的成功标注确认您的应用程序已连接到您的 Klaviyo 帐户。

## 其他资源

- 还有 Android 应用程序吗？了解[如何设置 Android 推送](https://help.klaviyo.com/hc/en-us/articles/14750928993307)。
- 了解如何[使用营销活动推送通知](https://help.klaviyo.com/hc/en-us/articles/360006653972)。
- 查看如何[在推送通知中使用深层链接](https://help.klaviyo.com/hc/en-us/articles/14750403974043)。

想要请求 Klaviyo 推送通知功能吗？填写此 [Google 表单](https://forms.gle/7iPm6JQ4eKB6H2C4A) 告诉我们！