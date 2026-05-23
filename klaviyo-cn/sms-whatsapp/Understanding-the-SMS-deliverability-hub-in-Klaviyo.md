---
id: "21206358003355"
title: "了解 Klaviyo 中的 SMS 传送中心"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/21206358003355-Understanding-the-SMS-deliverability-hub-in-Klaviyo"
section: "SMS deliverability best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:33Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 的帐户级短信送达率报告。 Klaviyo 传送中心中的 **SMS** 选项卡是一个集中空间，可让您分析和诊断所有发送的 SMS 传送状况。 ## 帐户交付中心

Klaviyo 中的**送达率**中心允许您在帐户级别分析和诊断您的电子邮件和短信送达率运行状况。要访问该页面，请导航至 **Analytics** 下的 **Deliverability** 选项卡。 ![Klaviyo 中的短信中心接口](https://klaviyo.zendesk.com/hc/article_attachments/28723546085915)

要分析您的短信传送能力，请选择****短信****选项卡。 ## 短信传送中心内容

### 过滤器

在送达中心的 **SMS** 选项卡顶部，您可以设置适用于所有 SMS 报告的过滤器。 ![短信传递中心中的可用过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28723546098331)

可以使用以下过滤器：

- 过去 7 天
- 过去 30 天
- 过去 90 天
- 定制

- 时间段
- 消息类型（即活动或流程）
- 消息格式（即短信、彩信或两者）

### 警报

**警报**部分是一个可折叠的卡片，当您的帐户中发现短信传送问题时，就会出现该卡片。每个警报都表明关键的交付能力指标性能不佳，并提供有关该问题的详细信息以及解决步骤的故障排除指南的链接。警报基于过去 7 天的数据。您会在以下情况下看到警报：

- **设备断开连接**失败超过发送总数的 5%
- **设备无法访问**失败超过发送总数的 5%
- **运营商违规**错误超过发送总量的 10%
- **消息被阻止**错误超过发送总量的 5%
- **设备无法接收 SMS** 错误超过发送总数的 5%
- **免费电话号码未注册** / **号码未验证**
- **未知错误**超过发送总量的 10%
- 点击率低于6.0%
- 退订率高于1.3%

![短信送达提醒](https://klaviyo.zendesk.com/hc/article_attachments/28723524156827)

详细了解不同的[短信失败原因及其解决方法](https://help.klaviyo.com/hc/en-us/articles/360039239172)。 ### 关键指标

在**关键指标**卡上，您将看到关键短信送达率运行状况指标的概述以及每个指标的绩效。这些指标是：

- 交货率
- 失败率
- 点击率
- 退订率

每个指标下方都有一个徽章，显示自上一个时间段以来您的表现有何变化。此外，您可以在 **Rate** 和 **Count** 之间切换，以百分比或总计数形式查看指标。 ![影响短信送达率分数的关键指标比率](https://klaviyo.zendesk.com/hc/article_attachments/28723524142747)

![影响短信送达率分数的关键计数指标](https://klaviyo.zendesk.com/hc/article_attachments/28723546078363)

将您的表现与 [Klaviyo 的 SMS 基准](https://help.klaviyo.com/hc/en-us/articles/360051110111) 进行比较。 ### 失败详细信息

**失败详细信息**图表可深入了解您的邮件未能送达收件人的原因。您可以通过分段条形图查看此信息，该条形图显示每个故障原因的数量。 ![显示短信失败报告的分段条形图](https://klaviyo.zendesk.com/hc/article_attachments/28723524149915)

或者，您可以将视图切换到折线图，以显示随时间变化的不同故障原因的性能。 ![显示 Klaviyo 中短信失败的折线图](https://klaviyo.zendesk.com/hc/article_attachments/28723546075931)

### 最近的活动表现

**近期**营销活动绩效**卡向您显示您帐户上最近对您的整体送达率影响最大的 SMS 营销活动。 ![有助于短信传递的活动绩效报告](https://klaviyo.zendesk.com/hc/article_attachments/28723546093083)

您可以在具有 **健康** 状态的营销活动和具有 **需要注意** 状态的营销活动之间切换。 **健康**切换显示所有指标均处于健康区域的最近 5 个营销活动。当选择 **需要关注** 开关时，将显示至少有 2 个指标处于 **需要关注** 范围内的 5 个最新营销活动。 ### 流量性能

**最近********低性能**卡向您显示对您的整体交付能力影响最大的帐户流量。 ![有助于短信传送能力的流性能报告](https://klaviyo.zendesk.com/hc/article_attachments/28723546089883)

您可以在具有 **正常** 状态的流和具有 **需要注意** 状态的流之间切换。 **健康** 切换显示所有指标均处于健康区域的最近 5 个流。当选择 **需要注意** 开关时，将显示至少有 2 个指标处于 **需要注意** 范围内的 5 个最新流。