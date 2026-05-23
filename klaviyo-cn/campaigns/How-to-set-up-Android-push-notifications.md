---
id: "14750928993307"
title: "如何设置 Android 推送通知"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/14750928993307-How-to-set-up-Android-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:48:41Z"
language: "zh"
---
## 你将会学到

了解如何在您的 Klaviyo 帐户中设置 Android 推送通知。完成本文中的步骤后，您将能够在流程和营销活动中发送推送通知。

## 开始之前

在 Klaviyo 中使用推送通知有 4 个先决条件；你必须：

1.拥有自己的原生移动Android应用程序。
2. [创建Google服务帐户](https://help.klaviyo.com/hc/en-us/articles/19893982562203)。
3. [生成 Google 服务身份验证密钥](https://cloud.google.com/iam/docs/keys-create-delete)，该密钥将上传到 Klaviyo（更多详细信息如下）。
4. 安装 [Klaviyo SDK](https://github.com/klaviyo/klaviyo-android-sdk) 并在 Android 应用程序中设置事件跟踪和推送通知。

## 设置Android推送

1. 单击左下角您的组织名称。
2. 导航至****设置 > 推送通知****。
3. 在 **移动应用程序设置** 页面上，单击 Android 选项旁边的****启用****。
4.填写所需信息：

   - ****包名称****
     添加您的[软件包名称](https://support.google.com/admob/answer/9972781?hl=en#:~:text=You%20can%20find%20an%20app's,example.)，您可以在 Google Play 商店中的列表网址中找到该名称。它看起来像：**com.yourcompany.yourproject**。
   - ****Google服务身份验证密钥****
     创建您的 [Google 服务身份验证密钥](https://cloud.google.com/iam/docs/keys-create-delete)，然后将 JSON 文件上传到 Klaviyo。密钥的 JSON 文件应如下所示：
     `{“类型”：“服务帐户”，
     "project_id": "PROJECT_ID",
     "private_key_id": "KEY_ID",
     "private_key": "-----开始私钥-----\nPRIVATE_KEY\n-----结束私钥-----\n",
     "client_email": "SERVICE_ACCOUNT_EMAIL",
     "client_id": "CLIENT_ID",
     “auth_uri”：“https://accounts.google.com/o/oauth2/auth”，
     "token_uri": "https://accounts.google.com/o/oauth2/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     “client_x509_cert_url”：“https://www.googleapis.com/robot/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL”}`
5. 单击****保存**** 完成 Android 应用程序的推送通知设置。

![Android 推送通知设置屏幕](https://klaviyo.zendesk.com/hc/article_attachments/28717853174171)

## 结果

现在，您可以向 Android 应用程序用户发送推送通知，让他们了解废弃的购物车或特殊的应用程序内优惠。

## 其他资源

- [如何在推送通知中使用深层链接](https://help.klaviyo.com/hc/en-us/articles/14750403974043)
- [如何设置iOS推送通知](https://help.klaviyo.com/hc/en-us/articles/360023213971)

想要请求 Klaviyo 推送通知功能吗？填写此 [Google 表单](https://forms.gle/7iPm6JQ4eKB6H2C4A) 告诉我们！