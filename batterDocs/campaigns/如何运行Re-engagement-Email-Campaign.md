---
id: 7088
title: "如何运行Re-engagement Email Campaign"
slug: "re-engagementcampaign"
category: "活动与营销（Campaigns）"
category_slug: "campaigns"
wp_url: "https://dynamicycle.com/docs/re-engagementcampaign/"
wp_modified: "2026-02-27T08:49:30"
---

##### 运行重新互动 Campaign

若要运行重新互动 Campaign，请执行以下步骤：

1. ****创建以下 2 个 Segment：**** 一个针对“不活跃的已购买者”，另一个针对“不活跃的未购买者”。
2. ****向这些订阅者发送个性化 Email Campaign：**** 展示您的最新发布，并提供更新偏好或退订的便捷方式。
3. ****清理（Suppress）未产生互动的 Profile：**** 如果他们未参与此次重新互动 Campaign，请将其清理以保持良好的送达率。

##### 将不活跃订阅者拆分为 2 个 Segment

首先，将不活跃订阅者拆分为两个 Segment：已购买过的和从未购买过的。这能让您在发送 Campaign 后，轻松判断哪一组受众更具价值。

###### 不活跃订阅者 – 已购买

该 Segment 应包含满足以下条件的受众：

- ****是订阅者，且订阅时间已超过 60 天。****
- ****在过去 120 天内未打开过任何邮件。****
- ****历史上邮件退回（Bounce）次数少于 5 次。****
- ****历史上至少下单过一次。****

![一组电子邮件营销条件筛选规则的界面，包含订阅日期、邮件打开次数、退件次数和下单情况的设置选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-47.png?resize=1024%2C961&ssl=1)

###### 不活跃订阅者 – 从未购买

您的第二个 Segment 应具备与第一个完全相同的条件，唯一的区别是他们从未下过订单：

- ****是订阅者，且订阅时间已超过 60 天。****
- ****在过去 120 天内未打开过任何邮件。****
- ****历史上邮件退回（Bounce）次数少于 5 次。****
- ****历史上从未下过订单（下单次数为 0）。****

![一组条件和规则，用于设置用户接收电子邮件营销的资格，包括订阅时间、邮件开启次数和订单情况。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-48.png?resize=1024%2C973&ssl=1)

##### 发送 Campaign

向这些不活跃的订阅者发送 ****Campaign****。在进行重新互动 Campaign 时，请参考以下最佳实践：

- ****让邮件更具个性化：**** 尝试使用****纯文本邮件****，以营造一种私人信件的亲切感。
- ****使用 `{{ first_name }}` 标签：**** 为每位 ****Recipient****（收件人）定制专属邮件。
- ****尝试“友好发件人”地址：**** 例如使用 “来自 Klaviyo 的 Marissa”。
- ****包含醒目的退订和管理偏好链接：**** 以防订阅者只是想更新他们的设置，而不是完全退订。

![电子邮件信息界面，包含主题行、预览文本、发件人名称和电子邮件地址字段，标题为'夏季促销开始！'](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-49.png?resize=1000%2C650&ssl=1)

- 包含自他们处于不活跃状态以来发布的所有新产品内容。
- 考虑提供折扣，以诱导他们产生购买行为。
- 包含醒目的退订和管理偏好链接，以防订阅者只是想更新其设置，而不是完全退订。您也可以考虑按发送频率对 Newsletter 进行受众分群，以避免因邮件轰炸导致订阅者从一开始就变得不活跃。

![包含调度或发送选项的窗口，允许用户选择发送类型、日期、时间和接收者百分比。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-50.png?resize=1024%2C890&ssl=1)

##### 使用分批发送 (Batch sending)

当您准备好发送 ****Campaign**** 时，可以考虑使用****分批发送****选项。这会将邮件投递分布在较长的一段时间内，如果您是向一大群不活跃用户发送邮件，这是一种更安全的做法。

![创建或发送邮件活动的界面，包含调度、立即发送选项，设置发送类型、日期、开始时间、时区和每小时接收者百分比的字段。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-51.png?resize=1024%2C890&ssl=1)

在您发送 ****Campaign**** 后，请密切监测结果，以确定是否需要每年重复执行此操作。如果您看到打开率超过 10%，则可以认为该 ****Campaign**** 是成功的。可能会出现其中一个 Segment 的打开率高于另一个的情况，在这种情况下，您在未来的重新互动 ****Campaign**** 中可能只想给那一个 Segment 发送邮件。

您可能还希望****清理 (Suppress)**** 任何未响应这些邮件的用户。您可以通过创建并导出“收到了任一邮件但未打开”的 Segment 来实现（见下文）。导出该 Segment 后，导航至 ****Audience > Profiles > View suppressed profiles > Import****，以清理这些 Profile，使他们不再接收未来的邮件。

在下方的 Segment 设置中，请将 ****Campaign Name 1**** 和 ****Campaign Name 2**** 替换为您自己的重新互动 ****Campaign**** 名称。

![展示电子邮件营销活动筛选条件的界面，包括接收和打开电子邮件的条件设置和计数结果。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-52.png?resize=1024%2C669&ssl=1)

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)