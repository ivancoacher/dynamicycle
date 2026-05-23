---
id: "46625983798299"
title: "如何发送 WhatsApp 交易消息"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/46625983798299-How-to-send-transactional-WhatsApp-messages"
section: "Send and use WhatsApp with Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:51:04Z"
language: "zh"
---
了解如何使用批准的实用程序模板发送 WhatsApp 交易消息。

交易性 WhatsApp 消息可让您发送订单确认、发货更新、帐户提醒和其他非促销更新。这些消息必须使用元批准的模板，分类为实用程序/事务性。

## 要求

您必须在您的帐户中启用 WhatsApp 并拥有批准的 WhatsApp 模板。您的 WhatsApp Business 帐户必须已连接并获得 Meta 的批准。

## 创建 WhatsApp 模板并对其进行分类

在发送 WhatsApp 交易消息之前，您必须创建并提交模板以供 Meta 批准。
[了解如何创建和提交模板。](https://help.klaviyo.com/hc/en-us/articles/40116644987675)

### 模板分类的工作原理

Meta 确定您的模板在审核期间是否被分类为实用型或营销型。

当您提交模板时：

- 元评论内容。
- 元分配模板类别。
- 如果您的模板不符合实用指南，Meta 可能会将您的模板重新分配给营销部门。

  [提交前查看 Meta 的官方指南](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization#utility-template-guidelines)。

### 如果您的模板被重新分配

如果 Meta 将您的模板重新分配给 Marketing，您将无法将其用于事务消息传递。

要解决这个问题：

- 使用经过修改的非促销内容创建新模板。
- 提交新模板以供审核。
- 在事务流程中使用之前等待元批准。

### 如果您编辑已批准的模板

如果您更改已批准模板的内容：

- 您必须重新提交以供元审核。
- 模板必须再次获得批准后才能使用。
- Meta 可能会在审核期间重新分配类别。

## 创建 WhatsApp 交易流程

使用由**已下订单**、**已履行订单**或其他帐户活动等事件触发的流程。

如果您的触发事件通过电子商务集成同步，请使用事件数据来个性化您的模板。例如，包括：

- 订单号
- 产品名称
- 追踪链接
- 运输状态

### 从头开始构建流程

请按照以下步骤创建 WhatsApp 事务流程：

1. 导航至****流****选项卡。
2. 单击右上角的****创建流****。
3. 选择****构建您自己的****。
4. 选择您的触发事件（例如，**已下订单**）。
5. 将 WhatsApp 操作添加到流程中。
6. 选择您认可的实用程序模板。
7. 将模板变量映射到事件数据，例如订单号或跟踪 URL。
8. 测试消息以确认变量填充正确。
9. 将 WhatsApp 消息设置为实时。

## 交易性 WhatsApp 消息的最佳实践

- 保持消息的信息性和非促销性。
- 清楚地提及相关交易或账户活动。
- 避免折扣、紧急语言或以销售为中心的文案。
- 使用动态事件数据以保证清晰度和准确性。

## 后续步骤

1. 确认您的模板在 Meta 中显示为已批准。
2. 使用真实事件发送测试消息。
3. 监控交付和参与度指标。
4. 在扩展容量之前检查模板性能。