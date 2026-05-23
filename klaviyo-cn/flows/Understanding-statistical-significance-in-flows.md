---
id: "11233978755611"
title: "了解流量的统计显着性"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/11233978755611-Understanding-statistical-significance-in-flows"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:10Z"
language: "zh"
---
了解 A/B 测试的结果何时被认为在 Klaviyo 流程中具有统计显着性。本文将解释流量的统计显着性以及何时确定。

统计显着性是指 Klaviyo 在数学上能够确定某种变化是否会提高性能。您可以配置流 A/B 测试，以便在测试结果被认为具有统计显着性时自动选择获胜变体。

A/B 测试是通过数据驱动的方法推动更好的参与和改善客户关系的关键。了解测试是否具有静态显着性非常重要。例如，如果一封流电子邮件有 2 个变体，变体 A 的点击率为 15%，而变体 B 的点击率为 14%，您如何确定变体 A 或 B 的效果是否更好？

## Klaviyo 如何确定流量中的统计显着性

对于流量，Klaviyo 观察收到消息的人数和获胜概率，即基于某个变体优于其他变体的程度，该变体产生更好结果的可能性。

在以下情况下，流消息变化被认为具有统计显着性：

- 至少有 500 名收件人收到了每种变体。
- 变体的获胜概率至少为 90%。
- 排名靠前的变体清晰分开：当领先变体和亚军的可能性能范围重叠太少（可信区间内重叠小于 10%）时，我们仅显示统计显着性

获胜概率是根据您在配置 A/B 测试时选择的指标计算的。默认情况下，该指标是您正在测试的消息的点击率。在“自动获胜者选择”部分中，您可以选择在根据配置的指标确定消息变体获胜后自动结束测试，也可以选择在到达特定日期后结束测试。您可以选择其中一个或两个选项。如果两者都选择，则测试将根据先达到哪个、统计显着性或指定日期结束。

有关更多详细信息，请参阅我们关于[如何对流电子邮件进行 A/B 测试](https://help.klaviyo.com/hc/en-us/articles/6960371049115) 的文章。

查看当前正在运行或已完成的测试的结果时，您将在**A/B 测试**部分看到获胜概率。在这里，您将看到测试结果是否具有统计显着性以及哪种变体可能表现更好。

![](https://klaviyo.zendesk.com/hc/article_attachments/40172449245979)

有关更多详细信息，请参阅我们关于[如何查看流程的电子邮件 A/B 测试结果](https://help.klaviyo.com/hc/en-us/articles/9360405808027) 的文章。

## 其他资源

请查看我们关于[A/B 测试最佳实践]的文章(https://help.klaviyo.com/hc/en-us/articles/360045012632)。

了解您可以运行的其他 A/B 测试：

- [如何对流程电子邮件进行 A/B 测试](https://help.klaviyo.com/hc/en-us/articles/6960371049115)
- [如何对营销活动电子邮件进行 A/B 测试](https://help.klaviyo.com/hc/en-us/articles/115005228148)
- [如何对注册表单进行 A/B 测试](https://help.klaviyo.com/hc/en-us/articles/360045462071)