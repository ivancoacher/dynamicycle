---
id: "16917302437275"
title: "了解丰富的推送通知"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16917302437275-Understanding-rich-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:06Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 中丰富的推送通知。丰富的推送通知可用于活动和流程。

****什么是丰富的推送通知？****

与标准的纯文本推送通知相比，丰富的推送通知包括多媒体内容，例如图像、GIF 和视频。

****为什么要发送丰富的推送通知？****

在推送通知中包含丰富的内容（例如图像）是吸引收件人并鼓励他们打开您的应用程序的好方法。例如，您可以向收件人展示他们愿望清单上的产品现在打折，或者发送有趣的图形来宣布重大新闻。

## 开始之前

在尝试使用丰富的推送通知之前，您必须执行以下操作：

1. 在 Klaviyo 中设置 iOS、Android 或两者的推送。
2. 仅适用于 iOS，请与您的应用程序开发人员联系，以确保您的应用程序可以发送丰富的通知。您可能需要在应用程序端进行其他设置，例如服务扩展。

想要请求 Klaviyo 推送通知功能吗？填写此 [Google 表单](https://forms.gle/7iPm6JQ4eKB6H2C4A) 告诉我们！

## Android 和 iOS 可用性

静态和动态图像可用于 iOS 和 Android 应用程序。

但是，GIF 和视频只能发送到 iOS 应用程序，因为 Android 目前不支持 GIF。如果您尝试将 GIF 发送到 Android 设备，它将显示为 GIF 第一帧的静态图像。如果您尝试将视频发送到 Android 设备，通知将以纯文本形式发送。

## 每次推送的媒体数量

每个推送通知可以有 1 条多媒体内容（例如图像或 GIF）。

因此，您无法将图像发送给 Android 用户，将 GIF 发送给 iOS 用户。

![图像展开时的推送通知示例](https://klaviyo.zendesk.com/hc/article_attachments/28716333130523)

## 文件类型

Klaviyo 支持以下图像文件类型：

- JPEG
- 巴布亚新几内亚
- GIF（仅限 iOS）
- MP4（仅限 iOS）

## 文件大小

图像/GIF 的大小必须为 1 MB 或更小。视频必须为 10 MB 或更小。

如果您尝试添加大于限制的文件，您将收到一条错误消息。

请注意，虽然某些设备可以支持较大的文件大小，但最佳做法是使用较小的文件。较小的文件大小有助于确保用户能够始终看到您的媒体，即使他们的互联网连接较差。

## 媒体附件的最佳实践

图像和 GIF 以两种方式显示：折叠视图（左）和可展开视图（右）。在展开视图中，您附加的媒体会自动调整以适合手机，并缩放到屏幕宽度。

当您添加 GIF 或视频时，只有收件人展开通知后才会播放。在折叠视图中，视频或 GIF 将显示为第一帧的静态图像。

|  |  |
| --- | --- |
| ![示例推送通知，显示折叠状态下的图像（如图标）](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/9b57c787dc7743bbfacd8229101616d8e4506271-474x328.png) | ![示例推送通知，展开时显示图像](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/3a5c194f5e1fba49ba2aacfd0691e9ab52ff0366-974x1008.jpg) |

最佳做法是使用比例尺寸为 2:1 的介质。在某些情况下需要 2:1 的比例，并且无论收件人使用的是 iOS 还是 Android 设备，该比例看起来都不错。太高或太宽的图像在缩放以适合手机屏幕时可能会出现扭曲。

以下是丰富的推送通知最常见的媒体大小。

- 512 x 256 像素
- 1024 x 512 像素
- 2048 x 1024 像素