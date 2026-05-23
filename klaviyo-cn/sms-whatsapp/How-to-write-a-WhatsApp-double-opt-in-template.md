---
id: "44519286665115"
title: "如何编写 WhatsApp 双重选择加入模板"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/44519286665115-How-to-write-a-WhatsApp-double-opt-in-template"
section: "Getting started with WhatsApp"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:50:55Z"
language: "zh"
---
需要付费****移动消息****计划。
双重选择加入模板可以免费创建和使用，但您需要一个有效的计划才能访问此功能。

了解如何编写 WhatsApp 双重选择加入消息模板，帮助您收集新订阅者明确、合规的同意。

本指南将引导您完成元批准模板的创建和格式化，包括如何为您的受众设置多语言版本。

## 开始之前

在编写双重选择加入模板之前，请确保：

- 您的 WhatsApp Business 帐户已连接到 Klaviyo。
- 您有一个经过批准的 WhatsApp 发件人。
- 您了解Meta的消息模板审批流程。
- 您的列表或关键字配置为双重选择加入。

## 双重选择加入模板的工作原理

双重选择加入模板是您的品牌在订阅者提交电话号码后发送的第一条消息。它要求他们通过回复关键字（如 ****YES**** 或 ****JA****）来确认同意。

第一条消息必须是元批准的模板。一旦订阅者回复，Klaviyo 就会自动发送一条免费的确认消息来确认订阅。

## 编写您的双重选择加入模板

按照以下步骤在 Klaviyo 中创建和编写双重选择加入模板。

1. 在左下角选择您的帐户名。
2. 导航至****内容**** > ****模板**** > ****WhatsApp****。
3. 单击****创建新模板****。
4. 选择 ****Transactional**** 作为您的消息类别。
5. 使用清晰、合规的语言撰写邮件正文。

****示例：****
“对此消息回复“是”，即表示您同意接收来自[公司名称]的营销消息。”

保持信息简短、直接：

- 确定您的公司名称。
- 清楚地解释订阅者正在选择接收 WhatsApp 消息。

单击****保存****并提交以供元批准。

## 应用经批准的 WhatsApp 模板

您的 WhatsApp 模板获得批准后，您可以将其分配给****双重选择加入确认****关键字，以便客户收到正确的自动回复。

1. 前往****设置 > WhatsApp > 关键字响应****。
2. 打开****双重选择加入确认****关键字。
3. 打开****语言****下拉列表，然后选择您要使用的语言的模板。

- 如果您使用****智能翻译****，您将在此处看到其他语言选项。

除非您选择不同的语言版本，否则 Klaviyo 会自动应用批准的英语模板。

## 为什么使用事务模板

Klaviyo 建议对所有双重选择加入消息使用****交易****模板，以保持可靠的交付能力并遵守 Meta 的政策。

虽然营销模板在技术上可以使用，但它们可能会遇到交付失败的情况。要了解更多信息，请参阅 [Meta 的文档](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits)。

## 使用多语言模板

您现在可以为每种受支持的语言配置多个双重选择加入模板。

- 为您支持的每种语言添加单独的模板。
- 将国家或流量映射到正确的模板语言。
- 默认情况下，Klaviyo 为所有语言创建英语模板。
- 根据您的流程设置，每条选择加入的消息一次以一种语言发送。

## 示例模板

****英文示例：****
“对此消息回复“是”，即表示您同意接收来自[公司名称]的更新。回复“停止”即可取消订阅。”

****德语示例：****
“Wenn Sie mit JA antworten，erklären Sie sich einversstanden，Nachrichten von [Unternehmensname] zu erhalten。Antworten Sie mit STOP，um sich abzumelden。”