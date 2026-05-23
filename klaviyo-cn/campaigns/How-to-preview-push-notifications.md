---
id: "18011985278875"
title: "如何预览推送通知"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18011985278875-How-to-preview-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:09Z"
language: "zh"
---
## 你将会学到

了解如何将推送通知的预览发送到设备。通过发送预览，您可以确保您的推送通知在客户看到之前完全符合您的预期。

要在 iOS 上进行测试，您必须在应用程序中使用 v2.2.0 或更高版本的 Klaviyo Swift SDK 才能使用此功能。对于 iOS 和 Android，您可以向生产或沙盒环境中的应用程序发送预览通知。

## 开始之前

在预览通知之前，您需要：

- 将 Klaviyo SDK 集成到您的 [iOS](https://github.com/klaviyo/klaviyo-swift-sdk) 或 [Android](https://github.com/klaviyo/klaviyo-android-sdk) 移动应用程序中。
- 在您的 Klaviyo 帐户中配置 [iOS](https://help.klaviyo.com/hc/en-us/articles/360023213971) 或 [Android](https://help.klaviyo.com/hc/en-us/articles/14750928993307) 推送通知。
- 通过测试设备上的应用程序在 Klaviyo 中创建配置文件。
- 选择在您的测试设备上推送通知。
- 复制您设备的推送令牌（您可以在您的个人资料中找到）。

想要请求 Klaviyo 推送通知功能吗？填写此 [Google 表单](https://forms.gle/7iPm6JQ4eKB6H2C4A) 告诉我们！

## 预览推送通知

预览推送通知很简单：

1. 创建营销活动或流消息。
2. 在推送编辑器的右上角，单击****预览和文本****。
3. 粘贴您的推送令牌。
4. 选择****发送测试****。

![](https://klaviyo.zendesk.com/hc/article_attachments/33627734554139)

您在 24 小时内最多可以发送 100 条预览推送通知。