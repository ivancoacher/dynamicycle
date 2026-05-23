---
id: "40116763040411"
title: "如何将 WhatsApp 添加到流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40116763040411-How-to-add-WhatsApp-to-a-flow"
section: "Send and use WhatsApp with Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:50:34Z"
language: "zh"
---
了解如何将 WhatsApp 消息操作添加到流程。与短信或推送通知一样，您可以将 WhatsApp 与电子邮件流结合使用，通过受众的首选渠道联系他们。

## 开始之前

在使用 WhatsApp with Flows 之前，请务必执行以下操作：

- [导入](https://help.klaviyo.com/hc/en-us/articles/40116243735579) 或[收集](https://help.klaviyo.com/hc/en-us/articles/40116301104539) WhatsApp 同意。
- 创建特定于您的流程的 [WhatsApp 模板](https://help.klaviyo.com/hc/en-us/articles/40116644987675)。

## 将 WhatsApp 添加到哪些流程

您可以在当前使用电子邮件的任何流程中使用 WhatsApp。

添加 WhatsApp 的前 2 个流程是：

- [废弃购物车流程](https://help.klaviyo.com/hc/en-us/articles/360036126951)
- [浏览放弃流程](https://help.klaviyo.com/hc/en-us/articles/15806802249883)

对于欢迎系列流程，最佳做法是为电子邮件和其他渠道（例如短信或 WhatsApp）创建单独的流程，因为客户可能会注册在不同时间接收来自每个渠道的消息。对于所有其他流程，将 WhatsApp 添加到您现有的电子邮件流程。

## 添加条件分割以检查是否同意

如果您要将 WhatsApp 添加到现有流程，则应首先添加条件拆分以检查是否有人订阅了 WhatsApp。

1. 在流程构建器中，从左侧边栏拖动条件拆分组件并将其放在第一封电子邮件之前。请注意，您的电子邮件现在位于拆分的 YES 路径上，并且有一个空的 NO 路径，您可以在其中开始 WhatsApp 路径。
2. 单击分割。
3. 在详细信息侧栏中，添加以下条件：****如果某人可以或不能接收营销**** > ****不能接收**** > ****WhatsApp 营销****。使用“无法接收”会将您的电子邮件保留在拆分的“是”路径上。任何未订阅 WhatsApp 的人都会收到电子邮件。
5. 单击****保存****。

## 将 WhatsApp 操作添加到流程中

要将新的 WhatsApp 消息添加到流程中：

1. 在流程构建器中，将 WhatsApp 操作从左侧边栏拖放到流程画布上。如果您使用条件拆分来检查是否同意，请将 WhatsApp 操作放在与电子邮件路径相反的路径上。
3. 单击流程中的 WhatsApp 消息。
4. 在详细信息侧栏中，单击****选择模板****。
5. 单击您要使用的模板的名称。
6. 单击****使用模板****。
8. 如果需要，在侧边栏的 **设置** 部分中，关闭 [智能发送](https://help.klaviyo.com/hc/en-us/articles/115002779311)。默认情况下此功能处于启用状态。
9. 将 WhatsApp 消息的状态更改为 ****Live****。