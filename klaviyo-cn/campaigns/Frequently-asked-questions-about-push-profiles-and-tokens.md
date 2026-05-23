---
id: "20582984332059"
title: "有关推送配置文件和令牌的常见问题"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/20582984332059-Frequently-asked-questions-about-push-profiles-and-tokens"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:21Z"
language: "zh"
---
## 你将会学到

了解有关推送配置文件和令牌的常见问题的答案。

在下面的部分中，我们回答以下问题：

- 推送个人资料
  - [Klaviyo 如何识别移动应用程序配置文件？](#h_01HFSRKVWE24ESV2Z19GH1CJVG)
  - [为什么我有匿名个人资料（即没有电子邮件或电话号码的个人资料）？](#h_01HFSRKVWERVC37FK8HJA7VBDZ)
  - [为什么我看到很多](#h_01HFSRKVWE8GMGAW0G5PA0TRPA) [**合并的个人资料**](#h_01HFSRKVWE8GMGAW0G5PA0TRPA) [个人资料上的事件？](#h_01HFSRKVWE8GMGAW0G5PA0TRPA)
- 推送令牌/同意
  - [为什么从配置文件中删除推送令牌？](#h_01HFSRKVWENNMPR6JGCZD7E0YX)
  - [什么时候生成新的推送令牌？](#h_01HFSRKVWEDBKK3V5HGSXN7H0T)

## 推送配置文件的常见问题解答

### Klaviyo 如何识别移动应用程序配置文件？

在移动应用程序中安装 Klaviyo SDK 允许 Klaviyo 识别个人资料并跟踪事件，就像添加 [Klaviyo 的](https://help.klaviyo.com/hc/en-us/articles/360020342232) [**现场活动**](https://help.klaviyo.com/hc/en-us/articles/360020342232) [跟踪snippet](https://help.klaviyo.com/hc/en-us/articles/360020342232) 到一个网站。

安装 SDK 后，Klaviyo 开始为使用您的应用程序的人员创建或更新配置文件。

当新用户进入您的应用程序时，Klaviyo 会检查是否有任何身份信息（例如电子邮件）。如果是这样，Klaviyo 会查找包含相同信息的任何现有配置文件。

如果 Klaviyo 找到具有匹配标识符的配置文件，则该应用程序配置文件将与现有配置文件合并。

如果没有具有该标识符的个人资料（或者用户未在应用程序中识别），Klaviyo 会创建匿名个人资料。

您的应用程序开发人员必须设置您的应用程序才能在 Klaviyo 中创建配置文件。如果没有创建配置文件（无论是已识别的还是匿名的），您应该联系您的应用程序开发人员。

### 为什么我有匿名个人资料（即没有电子邮件或电话号码的个人资料）？

没有电子邮件或电话号码的个人资料被称为“匿名个人资料”。

当以下三件事同时发生时，就会创建这些配置文件：

- 用户第一次打开应用程序。
- Klaviyo 识别出它是新用户或新设备。
- 没有为用户提供其他唯一标识符（电子邮件、电话号码或外部 ID）。

请注意，即使用户不同意推送通知，也可以创建匿名配置文件，以便您能够跟踪应用程序中的用户活动。

### 为什么我会看到该配置文件有很多“合并配置文件”事件？

如果 Klaviyo 将匿名个人资料与包含电子邮件、电话号码或外部 ID 的个人资料相匹配，您将看到合并的个人资料事件。

如果用户在多个设备上下载应用程序，则可能会发生多个合并的配置文件事件。在这种情况下，Klaviyo 为每个设备创建一个匿名 ID。但是，如果 Klaviyo 稍后通过电子邮件或电话号码识别每台设备上的用户，配置文件就会合并。

## 推送令牌/同意的常见问题解答

### 为什么推送令牌会从个人资料中删除？

当 iOS 或 Android 通知 Klaviyo 令牌无效时，Klaviyo 会从配置文件中删除推送令牌。

删除token的流程如下：

1. 您尝试向令牌发送推送通知（通过流程或活动）。
2. Android 或 iOS 发送响应称令牌无效。
3. Klaviyo 删除推送令牌。

请注意，用户的个人资料上可能有多个推送令牌，因为他们在多个设备（例如，他们的手机和平板电脑）上启用了推送通知。在这种情况下，仅删除无效令牌，您可以继续向用户的其他设备发送推送通知。

如果该令牌是配置文件中的唯一令牌，则该配置文件将从未来的推送通知中跳过。

### 新的推送令牌何时生成？

Android 和 iOS 确定何时生成新令牌。 Klaviyo 仅接受将通过 FCM 或 APN 传递的令牌。通常，当用户在设备上下载应用程序时，无论是第一次还是删除应用程序然后重新下载后，Android 和 iOS 都会生成新令牌。