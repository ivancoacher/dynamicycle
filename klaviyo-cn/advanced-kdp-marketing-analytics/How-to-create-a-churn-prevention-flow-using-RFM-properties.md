---
id: "32652195725083"
title: "如何使用 RFM 属性创建流失预防流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/32652195725083-How-to-create-a-churn-prevention-flow-using-RFM-properties"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:38Z"
language: "zh"
---
## 你将会学到

了解如何基于 RFM 属性构建流失预防流程，以针对极度流失的客户。保留流是帮助赢回客户、在正确的时间向他们传达正确的信息的有用驱动力。您可以在客户群发生变化时自动联系这些订阅者，从而可能降低收入和流失风险。

## 开始之前

[高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 和 [营销分析](https://help.klaviyo.com/hc/en-us/articles/33789259613595) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。前往我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672) 了解如何购买这些计划。

## 创建流失风险预防流程

要创建流失风险预防流程，您首先需要在 **非活动** RFM 组中创建一段配置文件，以用作流程的触发器。

### 创建您的细分

如果您还没有这样做，您首先需要创建一个包含非活跃客户的细分。要创建此段：

1. 如果您是高级 KDP 客户，请导航至****高级 KDP**** > ****情报**** > ****客户洞察**** > ****RFM 分析****。或者，如果您是 Marketing Analytics 客户，请导航至 ****Marketing Analytics**** > ****客户洞察**** > ****RFM 分析****。
2. 滚动找到 **RFM 分段** 卡并选择 ****创建分段****。
   ![在 RFM 卡上创建分段按钮](https://klaviyo.zendesk.com/hc/article_attachments/32672459322651)
3. 为您的细分命名并应用任何相关标签。
4. 为您的段设置以下定义：

   有关某人的属性 > **当前 RFM 组** 等于 **非活动**
   ![非活动 RFM 组中的配置文件片段](https://klaviyo.zendesk.com/hc/article_attachments/32672450004763)
5. 可选：**非活动** RFM 组包括过去至少进行过 1 次购买的配置文件。如果您想要定位过去购买过特定次数的客户（例如，仅一次性购买者），但现在属于不活跃组，则可以将以下条件添加到您的细分中：

   某人已完成（或未完成）的操作 > **此人已下订单** 始终等于 X

### 设置您的流程

您可以使用流程库中预构建的流程快速创建流失预防流程。

1. 导航到 **流** 选项卡。
2. 单击****创建流****。
3. 在流程库中搜索并选择****客户流失********。
   ![流程库中的流失预防流程](https://klaviyo.zendesk.com/hc/article_attachments/32672459333531)
4. 为您的流程命名并选择您刚刚为非活动 RFM 配置文件创建的分段。
5. 选择****创建流程****。
6. 自定义您的流程电子邮件。
7. 可选：如果您想向流程中添加其他消息，请在它们之间添加另一个时间延迟。确保这是您最后一条消息后至少 2-3 天。
8. 创建流程后，单击右上角的****更新状态****，然后选择**实时**。如果您想手动批准发送到进入流程的每个配置文件，请选择 **手动** 状态。
9. 设置流程状态后，单击****保存****。

## 其他资源

[高级 KDP 入门](https://help.klaviyo.com/hc/en-us/articles/17655007276059)

[如何在营销活动和流程中战略性地使用 RFM 属性](https://help.klaviyo.com/hc/en-us/articles/18194102384539)