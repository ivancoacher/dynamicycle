---
id: "17797912816795"
title: "如何构建客户终身价值 (CLV) 仪表板"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/17797912816795-How-to-build-a-customer-lifetime-value-CLV-dashboard"
section: "Predictive models"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: "zh"
---
## 你将会学到

了解如何构建和设置自定义客户生命周期价值 (CLV) 仪表板，以了解和预测每个客户随时间的购买行为。自定义 CLV 可以深入了解客户的购买习惯，包括未来潜在的购买以及针对即将购买的交叉销售和追加销售的机会。 [高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 和 [营销分析](https://help.klaviyo.com/hc/en-us/articles/33789259613595) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。前往我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672) 了解如何购买这些计划。 ## 导航到仪表板

CLV 仪表板的导航步骤根据您是高级 KDP 还是 Marketing Analytics 客户而有所不同。如果您是高级 KDP 客户，请导航至****高级 KDP > 智能 > 预测模型****。如果您是 Marketing Analytics 客户，请导航至****Marketing Analytics > 预测模型****。在这里，您将看到一个默认仪表板，其中包含当前使用的数据模型，后面是段、流、即将进行的活动以及使用特定 CLV 属性的表单。 ## 开始之前

### 仪表板要求

- 至少有500名已下订单的客户。这并不是指个人资料总数，而是实际向您的企业下过订单的人数。请注意，如果此部分位于个人资料中但为空，则 Klaviyo 没有足够的有关该人的数据来进行预测。 - 您有电子商务集成（例如 Shopify、BigCommerce、Magento 等）或使用 Klaviyo API 发送下订单。 - 您有至少 180 天的订单历史记录，并且在过去 30 天内有订单。 - 您至少有一些客户下了 3 个或更多订单。 ### 设置您的细分

如果您尚未这样做，则需要在查看仪表板之前设置 CLV 分段和定义。您的分段定义和属性将用于填充 CLV 仪表板中的各种卡片。了解如何[创建和设置 CLV 分段](https://help.klaviyo.com/hc/en-us/articles/360013201072)。只有所有者、管理员、经理和分析师可以访问此仪表板。 ## 自定义您的仪表板

### 检查您的 CLV 计算

1. 要查看您的 CLV 设置，请单击右上角的****设置****。 2. 在此设置卡的顶部，您可以查看当前的 CLV 计算方式（即 **下订单**、**退款订单** 和 **取消订单** 指标）。如果这 3 个指标中的任何一个指标的数据不足，您将不会看到该特定指标出现。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30666718756635)
3. 可选：要调整任何这些指标，请单击****更新指标映射****。从这里，您将进入指标映射设置以调整您正在使用的指标。请记住，更新任何指标映射将适用于您帐户中的所有[适用报告](https://help.klaviyo.com/hc/en-us/articles/25829057055899#h_01HZ2MPFB9V6HCZES9JCP8KV2R)。如果您正在编辑[映射指标](https://help.klaviyo.com/hc/en-us/articles/25829057055899)映射或使用[新自定义指标](https://help.klaviyo.com/hc/en-us/articles/22311085738395/)，则此更改最多可能需要 48 小时才会反映在您的报告中。此外，如果最近在您的帐户中编辑了某个内容，您可能会看到一条横幅，指出该内容仍在更新。 ### 调整你的预测时间范围

您的预测窗口是 Klaviyo 提供客户购买预测的时间范围。换句话说，在这段时间内，Klaviyo 预测特定客户预计花费多少钱以及他们的订单总数。默认情况下，您的预测窗口设置为 365 天。这意味着 Klaviyo 提供未来 365 天的 CLV 预测。但是，您可能会发现您想要缩小某个时间段（例如黑色星期五和网络星期一），或者如果您的购买周期往往较长，则需要增加该时间段。调整预测时间范围将更改使用预测 CLV 属性的所有细分、流程、营销活动和表单。 ****更新并保存您的新预测窗口****

要更改预测窗口的时间范围：

1. 在**天**字段中输入您想要分析的天数。请勿在字段中使用任何负数或特殊字符（例如，用逗号分隔较大的数字）。请注意，如果您有足够的数据支持，您最多可以分析 50,000 天。 ![天田.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713341019419)
2. 将数字添加到天数字段后，建议预览您想要的预测窗口。通过预览，Klaviyo 可以提供预测置信度和潜在数据的示例。 - Klaviyo 将提供 **高**、**中** 或 **低** 预测置信度，让您知道您选择的时间范围是否会提供准确或不准确的预测。 ![预测置信度.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713341022491)
   - 单击****预览**** 预览此更改。您将看到一条横幅，指出仪表板正在提供数据的预览示例。查看此示例仪表板，确保它满足您的需求，并且您使用了预测日期范围内的准确天数。！[预览数据banner.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713385531163)
3. 一旦您对预测窗口感到满意，请单击****保存****。 4. 将出现一个额外的弹出窗口，确认您的更改。再次单击****保存****以完成这些更新。如果您想放弃更改，请单击右上角的“****X****”以放弃更改。对预测窗口的更改最多可能需要 2 小时才能反映在您的数据中。然后将出现一条绿色成功消息，确认您保存的任何更改。详细了解[使用客户终身价值仪表板和卡片](https://help.klaviyo.com/hc/en-us/articles/17797865070235#01H8AHH3WBJTHF6H7M85PD3R43)。