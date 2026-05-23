---
id: "22344173696539"
title: "如何为 React Native 应用程序设置推送通知"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/22344173696539-How-to-set-up-push-notifications-for-a-React-Native-app"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:27Z"
language: "zh"
---
## 你将会学到

了解如何使用 Klaviyo 的 React Native SDK 发送移动推送通知。

****什么是 SDK？****

SDK 提供了所有必要的工具、库和程序，以便您的应用程序可以与第三方软件（例如，移动推送提供商）进行通信。 SDK 框架必须与用于构建应用程序的框架相匹配。

## React Native SDK 的好处

React Native SDK 允许您使用 React Native 将 Klaviyo 连接到应用程序。

React Native 是一个框架，可让您创建可在 iOS 和 Android 上运行的移动应用程序。它是用 JavaScript 编写的，允许您在多个平台上使用单个代码库。 React Native 应用程序看起来就像任何其他应用程序。

React Native 的混合框架意味着开发人员只需编写一次应用程序，并且可以更轻松地为 iOS 和 Android 维护它。

React Native 与本机应用程序不同，本机应用程序是用 iOS（Swift 或 Objective-C）或 Android（Kotlin 或 Java）特定语言编写的应用程序。拥有适用于 iOS 和 Android 的本机应用程序本质上是使用 React Native 的两倍，因为您必须构建和维护 2 个不同的应用程序。

## 设置要求

在为 React Native 应用程序设置推送通知之前，您必须：

- 拥有您自己的适用于 iOS、Android 或两者的 React Native 应用程序。
- 安装 [React Native SDK](https://github.com/klaviyo/klaviyo-react-native-sdk?tab=readme-ov-file)。

  我们还推荐以下内容：
- 在您的应用程序中设置个人资料标识。我们建议您使用个人资料标识符（电子邮件地址、电话号码或外部 ID）为应用程序用户创建个人资料，特别是当您想要个性化推送通知时。否则，Klaviyo 中的所有个人资料都将是匿名的。
- 在您的应用程序中配置事件跟踪。

请注意，您还需要设置部分原生 [iOS SDK](https://github.com/klaviyo/klaviyo-swift-sdk) 和 [Android SDK](https://github.com/klaviyo/klaviyo-android-sdk)（如果适用）。

## 设置推送通知

满足上述要求后，您必须将 Klaviyo 连接到您的 iOS 和 Android 应用程序。

有关如何执行此操作的说明，请参阅我们的设置指南：

- [iOS](https://help.klaviyo.com/hc/en-us/articles/360023213971)
- [Android](https://help.klaviyo.com/hc/en-us/articles/14750928993307)

## 测试推送通知

在开始发送给客户之前测试您的推送通知非常重要。以下是一些要测试的建议：

- 您的应用程序可以处理来自 Klaviyo 的推送通知。
- 您可以通过推送通知在应用程序中的屏幕上显示图像或深层链接（如果您打算使用这些功能）。
- Klaviyo 正在正确创建配置文件并从您的应用程序接收信息。

在测试之前，请确保您已打开应用程序的通知。

最简单的测试方法是从活动或流程中[发送预览](https://help.klaviyo.com/hc/en-us/articles/18011985278875)。