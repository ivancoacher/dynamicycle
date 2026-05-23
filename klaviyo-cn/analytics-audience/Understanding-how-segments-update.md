---
id: "115005233488"
title: "了解段如何更新"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005233488-Understanding-how-segments-update"
section: "Build and use segments"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:22Z"
language: "zh"
---
## 你将会学到

了解分段（即 Klaviyo 中的动态配置文件组）如何更新。大多数细分都会近乎实时更新，个人资料会根据他们与您的品牌的互动是否符合您设置的条件而移入和移出细​​分。创建细分后，它会根据您建立的定义从[您帐户中的所有人员](https://help.klaviyo.com/hc/en-us/articles/115005246968) 中提取成员。

在构建细分时，您只需设置一次条件。之后，该细分将根据您设置的条件不断添加和删除配置文件。

## 实时分段更新

分段请求的处理尽可能接近实时。这意味着您的细分在客户根据您创建的定义采取符合其资格的操作（例如下订单或打开电子邮件）后不久就会更新。在某些情况下，我们的客户群中大量的细分请求可能会导致延迟。

- 如果您手动更新分段，则最多可能需要 15 分钟来处理
- 如果您正在监控某个分段，更新可能最多需要一个小时

如果您更新航段并发现延迟超出了这些时间范围，请[检查 Klaviyo 的状态页面](https://status.klaviyo.com/) 或获取支持。

## 具有相对时间条件的片段

上述实时处理有一个值得注意的例外；依赖于相对时间条件的片段。例如，“过去 30 天内”是相对的，因为时间范围不断变化，而“2025 年 1 月 1 日之前”则不是。

如果配置文件采取的操作导致其符合或不再符合具有相对时间条件的段的资格，则会立即添加或删除它们。通过在过去的特定时间采取操作而符合分段资格的配置文件，或根据相对时间条件不再符合分段资格的配置文件，每 24 小时添加或删除一次。

例如，如果您的细分包含过去 30 天内至少进行过一次购买的个人资料，则任何进行购买的人都将立即添加。如果个人资料在 30 天内没有再次购买，则会在第 31 天从细分中删除。由于不购买不会触发任何事件，因此不再符合该细分资格的个人资料每天将被删除一次。

![过去 30 天内购买的个人资料片段](https://klaviyo.zendesk.com/hc/article_attachments/40167936832923)

此外，无法始终根据实时购买事件计算出在 30 到 60 天前至少购买过一次的人群。此部分将每 24 小时添加一次新的配置文件并删除旧的配置文件。

![30 至 60 天前购买的个人资料片段](https://klaviyo.zendesk.com/hc/article_attachments/40167946243611)

## 如何手动更新一个segment

要手动更新段，请选择该段并单击****编辑定义 > 更新段****。

请注意，手动更新的分段不允许用户输入分段触发的流。有关更多信息，请参阅我们关于[创建分段触发流]的文章(https://help.klaviyo.com/hc/en-us/articles/360003040052#how-a-segment-triggered-flow-works2)。

![手动更新片段的按钮](https://klaviyo.zendesk.com/hc/article_attachments/40167936840475)

## 其他资源

- [分段入门](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [AND 与 OR 指南](https://help.klaviyo.com/hc/en-us/articles/360036534631)
- [如何创建参与细分](https://help.klaviyo.com/hc/en-us/articles/115000200072)
- [使用日期参考进行分段](https://help.klaviyo.com/hc/en-us/articles/4403222359451)