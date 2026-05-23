---
id: 7160
title: "了解 Campaign 的排期与发送选项"
slug: "campaignscheduleandsendoptions"
category: "活动与营销（Campaigns）"
category_slug: "campaigns"
wp_url: "https://dynamicycle.com/docs/campaignscheduleandsendoptions/"
wp_modified: "2026-03-04T08:55:35"
---

##### 计划发送 (Schedule) 与立即发送 (Send now)

如果您在发送 ****Campaign**** 时选择 ****立即发送 (Send now)****，它将立即开始发送流程。这一过程可能需要几分钟或更长时间。

或者，您可以选择 ****计划发送 (Schedule)****，为 ****Campaign**** 选定一个未来的发送时间。在计划发送 ****Campaign**** 时，您有几种发送策略可供选择，具体说明如下。

![安排或发送活动的界面，包含发送时间、日期、时区和每小时接收者百分比的设置选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/03/image-16.png?resize=445%2C840&ssl=1)

##### 发送策略

在计划发送 ****Campaign**** 时，您可以在 ****Type****（类型）菜单中选择固定发送、逐渐发送或智能发送时间。

###### 固定发送时间 (Fixed send time)

如果您希望所有受众在大约相同的时间接收邮件，请选择此选项。适用于邮件、SMS 和推送通知。

****提示：**** 在高峰时段（如整点或半点），发送速度可能会略有延迟。若要加快发送速度，建议通过手动输入分钟值（例如下午 3:04 而非 3:00）来避开高峰时段。

****注意：**** 发送邮件需要一定的处理时间，因此即使在非高峰时段，在您的计划发送时间与实际送达之间也可能会有几分钟的间隔。

###### 在数小时内逐渐发送 (Gradual send over several hours)

选择此选项可将发送任务分成批次，每小时向一定比例的受众发送，直到所有人均收到消息。

- 如果您正在对该 ****Campaign**** 进行 ****A/B 测试****，则无法使用此策略。
- 适用于邮件、SMS 和推送通知。

###### 智能发送时间 (Smart send time)

此选项仅适用于满足特定标准的发送者。利用 Klaviyo 的 AI 工具确定受众的最佳发送时间，从而获得最佳效果。

- 了解[如何使用智能发送时间功能](https://www.klaviyo.com)。
- 仅适用于****邮件****。

##### 在发送时确定受众 (Determine recipients at send time)

当启用 ****Determine recipients at send time**** 时，Klaviyo 会在尽可能接近发送时间时，为您的目标列表或 ****Segment**** 生成一份全新的快照，以确保触达的是最新的受众群体。

****配合不同发送时区使用时的逻辑：****

- ****特定时区 (Specific timezone)：**** Klaviyo 会在该时区计划发送时间前立即生成快照。
- ****受众当地时区 (Recipient Local Timezone)：**** Klaviyo 会在第一条消息发送给最早时区的受众之前生成一份快照。该快照随后将用于所有后续时区的发送。

****此选项适用于：****

- 电子邮件 (Email)
- 短信 (SMS)
- 移动推送通知 (Mobile push notification)

默认情况下，“在发送时确定受众”功能处于关闭状态。了解如何[更改 Campaign 确定受众的时间](https://www.klaviyo.com)。

![显示发送时间确定收件人的选项，包含说明文字和调度活动及取消按钮。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/03/image-17.png?resize=445%2C234&ssl=1)

当未勾选此选项时，Klaviyo 会在您点击 ****Schedule campaign****（计划 Campaign）的那一刻抓取目标列表或 ****Segment**** 的快照。如果在您计划消息到实际发送期间，有任何人被添加进列表或从列表中移除，这些变化将****不会****反映在发送名单中。

****注意：**** 任何退订（Unsubscribe）的用户都将被过滤掉，即使他们在您计划消息之后、开始发送之前退订。然而，由于您的列表或 ****Segment**** 自创建 ****Campaign**** 以来可能有所增长，这可能会导致您使用的点数（Credit）或发送量超出预期。

##### 时区选项 (Timezone options)

根据您的发送策略，您可能有 2 种时区选项：****受众当地时区 (Recipient’s local timezone)**** 或****您选择的特定时区****。

![显示选择收件人所在时区的界面，包含"美国/东部"的选项](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/03/image-18.png?resize=612%2C410&ssl=1)

##### 受众当地时区 (Recipient’s local timezone)

选择此选项，可以按照每位受众所在当地时区的特定时间发送 ****Campaign****。

- 对于带有 ****A/B 测试**** 的 ****Campaign****，仅当测试比例为 50/50 分流时，此选项才会出现。
- ****示例：**** 如果您设置在下午 3 点发送并选择了受众当地时区，居住在加利福尼亚的订阅者将在太平洋时间 (PT) 下午 3 点收到邮件，而英国订阅者将在格林威治标准时间 (GMT) 下午 3 点收到。如果受众的时区未知，他们将在您****账户设置的时区****下收到消息。

如果计划发送时间在某些受众的时区已经过去，您有两种选择：

1. ****立即向这些受众发送 Campaign。****
2. ****等到第二天的计划时间再向这些受众发送。****

****注意：**** 如果您选择“立即发送”，在计划好 ****Campaign**** 后将无法更改发送时间。

当您选择根据每位受众的时区发送时，您将****无法****同时使用“在发送时确定受众”功能。这意味着在您点击 ****Schedule****（计划）后，不会有新受众被添加到该 ****Campaign**** 中。

###### 特定时区 (Specific timezone)

当选择特定时区时，消息将在该统一时间发送给所有人。

- ****示例：**** 如果您在太平洋时间 (PT) 下午 3 点发送消息，无论订阅者身在何处，所有人都会在那个时刻收到消息。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)