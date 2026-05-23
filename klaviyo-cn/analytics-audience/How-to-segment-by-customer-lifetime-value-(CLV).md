---
id: "360013201072"
title: "如何按客户终身价值 (CLV) 进行细分"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360013201072-How-to-segment-by-customer-lifetime-value-CLV"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:56:50Z"
language: "zh"
---
## 你将会学到

了解如何创建客户终身价值 (CLV) 细分并导出任何关键的 CLV 信息。 CLV 是 Klaviyo 的[预测分析](https://help.klaviyo.com/hc/en-us/articles/360020919731-Guide-to-Klaviyo-s-Predictive-Analytics) 的一部分，可以成为用于细分的强大工具。它是一段时间内客户从您的品牌购买的总金额（包括过去的金额和预测的金额）。 CLV 细分允许您根据此金额对客户进行分组，以便您可以向他们发送相关内容并触发基于细分的流。例如，您可以使用历史 CLV 构建 VIP 欢迎流程，或使用预测 CLV 向可能在一年内消费一定金额的客户发送有针对性的营销活动。 ## 开始之前

请注意，您只能在以下情况下根据 CLV 进行细分：

- 至少有500名客户已下订单。这不是指活跃的个人资料，而是指实际在您的企业进行过购买的人数。如果此部分位于个人资料中但为空，则意味着我们没有足够的有关该人的数据来进行预测。 - 您有电子商务集成（例如 Shopify、BigCommerce、Magento）或使用我们的 API 发送下订单。 - 您有至少 180 天的订单历史记录，并且在过去 30 天内有订单。 - 您至少有一些客户下了 3 个或更多订单。 ## 创建一个CLV段

要根据任何可用的 CLV 属性（即历史、预测和总 CLV）创建细分，请使用 **关于某人的预测分析** 条件。然后，选择您所需的指标和值。 ![CLV 超过 100 的客户群](https://klaviyo.zendesk.com/hc/article_attachments/28722556838299)

### 示例

假设您的客户平均订单价值约为 15 美元。您可能希望针对不太可能达到此平均订单价值的客户提供折扣，以推动他们下次购买。为了实现这一目标，创建一个预计花费不超过 5 美元的客户群，并针对他们开展折扣活动或流量 - 类似于 [winback](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192) 或重新参与活动。通过电子邮件定位时，您需要包含以下条件：

- 它们属于您的主要电子邮件列表（在本例中为时事通讯列表）
- 他们在给定的时间内打开了一封电子邮件，以确保您发送给参与的订阅者（在下面的示例中，时间线是过去 90 天）

![低预测 CLV.png](https://klaviyo.zendesk.com/hc/article_attachments/28722556847515)

## 导出 CLV 段

[导出CLV数据](https://help.klaviyo.com/hc/en-us/articles/115005078687)可以让您进一步分析和预测不同群体客户的行为。除了 CLV 和预测分析值之外，您还可以导出 **流失风险预测**。流失风险将以 0 到 1 之间的数字导出到 CSV 中。例如，0.45 对应于 45% 的流失风险。 ![选择 CLV 指标.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722556850459)

如果您有大量一次性购买者，您的平均流失风险可能会很高。为了降低平均流失风险，您可能需要将营销工作的重点放在首次购买后留住客户。您可以使用 Klaviyo 的预测 CLV 指标来识别不太可能再次购买的用户，如上例所示。将这些数据导出为 CSV 后，您就可以运行自己的分析。您可能感兴趣的一些计算包括：

- ****平均 CLV****您可以通过平均历史 CLV 和总 CLV 来计算细分市场的平均客户价值。 - ****预测细分市场的未来支出****将细分市场所有成员的预测 CLV 相加，您将获得该细分市场客户明年的预期收入。 - ****估计回头客的数量****首先，对流失风险预测的值进行平均。然后，用 1 减去该平均值。将结果乘以该分段中的人数。这将产生预计返回的客户数量。 ## 其他资源

- 课程：[通过预测洞察和自定义 CLV 减少客户流失](https://academy.klaviyo.com/mitigate-churn-with-predictive-insights-and-custom-clv/1791769)
- [Klaviyo 预测分析指南](https://klaviyo.zendesk.com/hc/en-us/articles/360020919731)