---
id: "46623602305563"
title: "如何将 WhatsApp 添加到您废弃的购物车流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/46623602305563-How-to-add-WhatsApp-to-your-abandoned-cart-flow"
section: "Send and use WhatsApp with Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:51:02Z"
language: "zh"
---
了解如何将 WhatsApp 消息添加到废弃的购物车流程并遵循最佳实践。

将 WhatsApp 添加到您的废弃购物车流程中，您可以提醒购物者使用直接且立即的渠道完成购买。与电子邮件结合使用时，可以提高恢复率，同时保持良好的客户体验。

## 将 WhatsApp 添加到废弃的购物车流程

请按照以下步骤将 WhatsApp 添加到您现有的废弃购物车流程中。

1. 导航至****流****。
2. 找到您想要添加 WhatsApp 的废弃购物车流程。
3. 在流程中，在第一个时间延迟后放置条件分割。
4. 使用条件配置拆分：

   **如果某人可以或不能接收营销信息>此人无法接收>WhatsApp 营销信息**。
5. 在 NO 路径上，添加 WhatsApp 消息。
6. 单击 WhatsApp 消息卡。
7. 单击详细信息面板中的****编辑****。
8. 添加您的消息内容。例如：

   “嘿 {{ person|lookup:"first\_name"|default:'there' }}，您的购物车即将过期。您想查看一下吗？[带链接的 URL 按钮]”
9. 为了鼓励转化，请考虑提供折扣。例如：

   “嘿 {{ person|lookup:"first\_name"|default:'there' }}，您的购物车即将过期。立即使用代码享受 10% 折扣。[复制代码按钮 {% coupon\_code 'YOUR\_COUPON' %}] [带链接的 URL 按钮]”
10. 在第一封电子邮件之后，将 WhatsApp 消息后的拆分重新加入到主流程中。
11. 将 WhatsApp 消息设置为实时。

## 改善您的 WhatsApp 废弃购物车流程

您可以通过额外的定位和拆分来自定义废弃的购物车流程。

虽然您应将单个废弃购物车事件的提醒限制为每个收件人一条 WhatsApp 消息，但您可以通过针对不同的受众在流程中添加其他 WhatsApp 消息。

### 如果产品不可用，请跳过 WhatsApp

最佳做法是在 WhatsApp 消息中仅显示一项。这使得消息简洁并确保清晰。

由于 WhatsApp 消息无法像电子邮件一样动态显示多个放弃的项目，因此请重点关注购物车中的第一个项目。如果该商品缺货，您可以使用以下格式取消消息：

````
{% 目录事件.ProductID unpublished="取消" %}
您的废弃购物车提醒消息
[产品链接]
{% 最终目录 %}
````

### 价值分割

使用触发器拆分根据购物车价值发送不同的 WhatsApp 消息。例如，仅向购物车价值超过特定阈值的客户提供折扣。

### 产品集合拆分

添加基于集合的触发器拆分，以根据特定产品类别定制 WhatsApp 消息。

### 新购买者与回头客的划分

使用有条件拆分向新客户和老客户发送不同的 WhatsApp 消息。

### 频繁购买者分裂

根据购买频率创建有条件的分割，以不同的激励措施奖励忠诚的客户。

## 后续步骤

将 WhatsApp 添加到废弃购物车流程后：

1. 测试流程以确认消息发送正确。
2. 检查时间安排，确保 WhatsApp 和电子邮件消息的间隔适当。
3. 监控绩效并调整激励措施或复制以提高回收率。