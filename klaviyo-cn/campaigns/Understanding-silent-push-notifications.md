---
id: "34331926591003"
title: "了解静默推送通知"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/34331926591003-Understanding-silent-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:57Z"
language: "zh"
---
## 你将会学到

了解什么是静默推送通知以及如何在您的营销活动和流程中使用它们，以及特定的用例。

## 什么是静默推送通知？

无声推送通知是无形地发送到设备的推送通知。它们没有内容或声音，不会向用户显示。通过静默推送，您可以触发内容更新或任务，而无需通知用户或要求他们更新您的应用程序。常见用例包括：

- 在您的应用程序中显示新内容
- 个性化应用程序界面
- 从服务器下载信息

要通过静默推送触发应用程序任务，请利用[键值对](https://help.klaviyo.com/hc/en-us/articles/34331971195675)。键值对是可以包含在静默推送通知和标准推送通知中的自定义数据。

## 如何使用静默推送通知

静默推送通知与标准推送通知一样，可以在活动和流程中使用：

- 了解如何[发送推送通知活动](https://help.klaviyo.com/hc/en-us/articles/360006653972)
- 了解如何[向流程添加推送通知](https://help.klaviyo.com/hc/en-us/articles/12932504108571)

首先，确保您已在 Klaviyo 帐户中[设置推送通知](https://help.klaviyo.com/hc/en-us/articles/360023213971)。

发送静默推送涉及将推送类型设置为**静默**，然后配置任何键值对（可在 **行为** 选项卡上的 **自定义数据** 设置中找到）。

![](https://klaviyo.zendesk.com/hc/article_attachments/36082188321947)

键值对支持静默推送通知的许多用例，但不是必需的。

为了使用键值对，您的应用程序必须设置为识别键并响应其值，因此请务必与您的应用程序开发人员合作，以确保您的应用程序构建为支持您的用例。

## 示例用例

无提示推送通知（以及键值对）的好处是您可以在各种用例中使用它们。

您可以发送静默推送通知，以根据收件人的属性（例如存储在 Klaviyo 中的个人资料属性）个性化应用程序内容。例如，如果您有一个电子商务应用程序，则可以使用静默推送和键值对在客户购买后在其应用程序中显示更新的奖励积分。

## iOS 特定指南

如果您在传送静默推送通知时遇到问题，请注意，iOS 不保证静默推送通知的传送。他们可能不会[根据设备的当前状态](https://developer.apple.com/library/archive/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23)提供它们，例如电池电量和网络连接。

## 无声推送通知会影响 Klaviyo 性能报告吗？

您可以查看单个静默推送通知的送达率和退回率；但是，静默推送通知被排除在 Klaviyo 的所有聚合性能报告之外。这包括随着时间的推移移动推送打开率等内容，因为它们没有打开或转化。

请注意，您将看到静默推送与标准推送不同的事件，即**已接收静默推送**和**弹回静默推送**。