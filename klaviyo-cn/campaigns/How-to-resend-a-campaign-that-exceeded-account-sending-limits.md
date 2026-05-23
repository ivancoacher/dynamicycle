---
id: "10730779545883"
title: "如何重新发送超出帐户发送限制的营销活动"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/10730779545883-How-to-resend-a-campaign-that-exceeded-account-sending-limits"
section: "Email campaign troubleshooting"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:42:35Z"
language: "zh"
---
## 你将会学到

了解如何向因超出发送限制而跳过的收件人重新发送营销活动。此错误显示为：“您的广告活动 CAMPAIGN\_NAME 由于超出帐户发送限制而被自动取消。”

## 活动为何被取消

当测试池超出帐户的每月发送限制时，Klaviyo 会自动取消活动。如果营销活动因此而被取消，那么当您稍后升级套餐时，营销活动不会自动继续发送。

要查看您帐户当前的每月发送限额：

1. 单击 Klaviyo 左下角您的公司名称。
2. 单击****计费****。
3. 找到 **个人资料 + 电子邮件** 卡以查看您当前的电子邮件限制和每月使用情况，或找到 **短信** 卡以查看您的短信限制和使用情况。
   ![账单概览页面，以及您的计划限制](https://klaviyo.zendesk.com/hc/article_attachments/28720900586523)

### 如何避免超出发送限制

为避免在达到每月发送限制时邮件被取消，请启用自动升级计费选项。启用此选项后，如果您超出当前计划的限制，Klaviyo 会自动将您升级到下一个计划级别。了解[如何开启自动升级计费](https://help.klaviyo.com/hc/en-us/articles/4405883690651)。

## 重新发送您的活动

启用自动升级计费后，继续发送营销活动。

首先，找到原始营销活动的营销活动 ID：

1. 导航至****营销活动****选项卡。
2. 在列表视图中，单击营销活动旁边的三点菜单。
3. 点击****复制广告活动 ID****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34609738033947)
   ![复制活动 ID mini.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720895276059)

然后，重新发送营销活动。

- 导航至****列表和分段****选项卡。
- 创建一个具有以下定义的段：
  - **某人做了什么 > 收到[电子邮件或短信] > 一直以来至少一次 > 其中 > 活动 ID 等于 [您的活动 ID]**
- 导航到您的****营销活动****选项卡并找到已取消的营销活动。
- 单击活动最右侧的三点图标，然后单击****克隆****。
- 从克隆的营销活动中排除您在步骤 2 中创建的分段。
- 发送活动。

通过执行上述步骤，在您的资金用完之前收到您消息的人将不会收到第二次重新发送的营销活动。

## 其他资源

- [了解 Klaviyo 计费的工作原理](https://help.klaviyo.com/hc/en-us/articles/115000976672-Understand-how-Klaviyo-billing-works-)
- [A/B 测试的最佳实践](https://help.klaviyo.com/hc/en-us/articles/360045012632-Best-Practices-for-A-B-Testing)