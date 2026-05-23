---
id: "41072989967515"
title: "如何在 Klaviyo 中使用 RCS 功能属性"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41072989967515-How-to-use-the-RCS-capability-property-in-Klaviyo"
section: "RCS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: "zh"
---
> ****先决条件：**** RCS 功能属性仅针对已激活 RCS 的帐户显示。如果您的帐户未启用 RCS，则此属性将不可见。

Klaviyo 中的****RCS 功能属性**** 可帮助您了解哪些订阅者可以接收 RCS（丰富通信服务）消息。您可以在个人资料中查看此信息，使用它来创建目标细分，并通过条件拆分将其应用到流程和营销活动中。

借助****RCS 功能属性****，您可以：

- 在短信营销订阅详细信息中检查个人资料是否支持 RCS
- 创建仅 RCS 或仅 SMS 段
- 在流程和营销活动中使用条件拆分，以确保您提供正确的消息格式

## ****查看配置文件上的 RCS 功能****

使用 RCS 功能属性的第一步是了解订户是否可以接收 RCS。

您可以直接在个人资料上的****短信营销****订阅框中查看。

![](https://klaviyo.zendesk.com/hc/article_attachments/41072989960091)

元数据包括****是否支持 RCS**** 字段，该字段将显示 **True** 或 **False**。

- **True** 表示订阅者的设备支持 RCS。
- **False** 表示订阅者的设备不支持 RCS。

****注意：**** 仅当帐户已激活 RCS 并且配置文件主动订阅 SMS 营销时，才会显示是否支持 RCS 字段。

## ****创建 RCS 段****

您可以使用 Klaviyo 的 [分段生成器](https://help.klaviyo.com/hc/en-us/articles/115005237908) 创建可以接收 RCS 消息的订阅者分段。

1. 导航至您的 Klaviyo 帐户中的列表和细分。
2. 选择创建列表/细分，然后选择细分。
3. 输入描述性名称，例如 RCS。
4. 在分段构建器中，设置条件如下：
   1. 人“可以接收”“营销短信”
   2. 因为人‘订阅’
   3.“是否支持 RCS”为“True”

您的片段应如下所示：

![](https://klaviyo.zendesk.com/hc/article_attachments/41072989961243)

创建专用 RCS 细分可确保您仅定位既选择了 SMS 营销又能够接收 RCS 消息的联系人。

## ****创建短信段****

如果您想为可以接收 SMS 但不能接收 RCS 的订阅者创建分段，只需将最后一个条件（支持 rcs）更改为“False”即可。

此部分确保 SMS 活动仅发送给无法接收 RCS 的联系人。

## ****在流程和活动中使用条件分割****

在流程和全渠道营销活动中创建****有条件拆分****时，您还可以使用****RCS功能属性****。这使您可以根据联系人是否可以接收 RCS 来对自动化进行分支，确保传递正确的消息类型。

例如：

- 如果某人****有 RCS 能力 = True****，则发送 RCS 消息。
- 否则，执行其他操作而不是发送短信回退。

你的分割应该是这样的：

![](https://klaviyo.zendesk.com/hc/article_attachments/41073018903707)