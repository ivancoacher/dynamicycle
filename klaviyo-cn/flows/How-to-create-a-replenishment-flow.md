---
id: "360003195232"
title: "如何创建补货流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360003195232-How-to-create-a-replenishment-flow"
section: "Post-purchase flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:50Z"
language: "zh"
---
## 你将会学到

如果您销售的产品是客户在特定时间范围内重复购买的产品，了解如何创建补货流程，以便在客户生命周期的不同阶段培养客户。通过查看现有的购买数据，您可以确定客户和产品的既定购买周期，然后通过友好且适时的提醒设置针对目标购买者的补货流程。

## 流触发器和过滤器

对于 Shopify 和 BigCommerce 集成，在设置并启用集成后，流程库中提供了预构建的补货流程。要查看这些：

1. 导航至****流****选项卡。
2. 点击****创建流****查看流库。
3. 在**按目标浏览**部分中，点击****鼓励重复购买****或使用搜索栏搜索“补货”。

但是，只要您有 **Placed Order** 事件，您就可以通过创建指标触发的流程，然后使用 **Placed Orde**r 事件从头开始构建此流程。如果您要为特定产品创建流程，则可以添加[触发过滤器](https://help.klaviyo.com/hc/en-us/articles/115002779051-Flow-Triggers-and-Filters#setting-trigger-filters)，以将此流程限制为购买该产品的客户。

![配置“物品包含高级能量水”的触发过滤器示例](https://klaviyo.zendesk.com/hc/article_attachments/28723519600027)

您还需要确保删除进入此流程后进行购买的客户。预构建的补货流程附带一个[配置文件过滤器](https://help.klaviyo.com/hc/en-us/articles/115002779051-Flow-Triggers-and-Filters#setting-flow-filters)，该过滤器会在每封电子邮件发送之前进行检查，以确保客户自进入流程后没有购买过产品。确保您已添加此配置文件过滤器。如果您将流量限制为特定产品，则还应该将此过滤器限制为特定产品。

![有条件拆分，检查自开始流程以来是否有人未下订单高级能量水](https://klaviyo.zendesk.com/hc/article_attachments/28723507929627)

## 流量计时

根据客户既定的购买周期调整首次提醒的时间。例如，如果您销售的补充剂的供应量为 30 天，您很可能希望在客户进入流程后 25 天左右发送提醒电子邮件。

![具有 1 个触发器过滤器和 1 个流过滤器的下订单流触发器](https://klaviyo.zendesk.com/hc/article_attachments/28723519607835)

您可以尝试使用额外的提醒电子邮件，但请记住不要骚扰您的客户。一个好的经验法则是发送两封提醒电子邮件，然后在预计的购买周期结束后发送一封后续电子邮件，其中包括折扣或优惠券等额外奖励。

![25 天后第一封电子邮件和 3 天后第二封电子邮件的示例流程](https://klaviyo.zendesk.com/hc/article_attachments/28723519603995)

## 流量内容

您需要根据您的目标定制内容，以包含与客户购买相关的产品信息。例如，如果您销售的产品供应期为 30 天，那么您需要发送提醒客户再次购买同一产品的内容。

![示例补货电子邮件，其中包含优质能量水的名称和图像以及“再次购买”按钮链接](https://klaviyo.zendesk.com/hc/article_attachments/28723519597211)

您可能还想包含使用产品块的类似产品的建议。例如，如果您销售咖啡豆，补货流程可能会建议购买新口味或杯子。

## 其他资源

- [如何创建特定于产品的流程](https://help.klaviyo.com/hc/en-us/articles/115002779431)
- [如何使用流程发送交易电子邮件](https://help.klaviyo.com/hc/en-us/articles/360003165732)