---
id: "43671905324187"
title: "通过全渠道营销活动退出标准自动防止过度消息传递"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/43671905324187-Automatically-prevent-over-messaging-with-omnichannel-campaigns-exit-criteria"
section: "Getting started with campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-05-11T12:54:29Z"
language: "zh"
---
## 你将会学到

了解全渠道营销活动中的退出标准，包括它们是什么以及它们如何在客户转化后自动从营销活动中删除客户。

一旦客户满足定义的转化条件，退出标准就会自动将客户从多天的全渠道营销活动（例如产品下降、闪购和忠诚度推送）中删除，从而有助于防止过度消息传递。这可确保转换后的客户不再收到促销消息，从而创造更流畅的体验并提高整体营销活动绩效。

## 开始之前

本文介绍如何设置全渠道营销活动的退出标准。如果这是您第一次创建营销活动，请[了解如何创建和发送电子邮件营销活动](https://help.klaviyo.com/hc/en-us/articles/115005054847)。

## 它是如何工作的

1. 为您的广告系列选择转化指标。
2. Klaviyo 记录整个全渠道营销活动中最早的消息发送时的营销活动开始日期。
3. 如果配置文件在发送第一条消息后的任何时候都满足转化指标，则它们会自动从营销活动中的所有剩余消息中排除。

## 示例：运动鞋发布

- 第 1 天上午 9:00 电子邮件：抢先体验消息
- 第 1 天下午 1:00 短信：提醒消息
- 第 2 天上午 9:00 电子邮件：第二天的后续消息

****退出条件：已下订单****

在上午 9:15 购买的客户将自动从活动中的未来消息中排除，包括下午 1:00 短信提醒和第二天上午 9:00 电子邮件跟进。

## 配置退出标准

1. 打开或创建全渠道营销活动
2. 打开活动设置
   1.选项1-点击右上角的选项菜单
      ![](https://klaviyo.zendesk.com/hc/article_attachments/43671905301019)
   2. 选项 2 - 单击任意受众群体
   3. 单击营销活动设置组件中的编辑按钮
   4.![](https://klaviyo.zendesk.com/hc/article_attachments/43671905301915)
      ![](https://klaviyo.zendesk.com/hc/article_attachments/43671928147099)
3. 开启退出条件（默认关闭）
   ![](https://klaviyo.zendesk.com/hc/article_attachments/43671905312795)
4. 选择转化指标（建议下订单）
   ![](https://klaviyo.zendesk.com/hc/article_attachments/43671928160155)
5. 点击“X”关闭活动设置

![](https://klaviyo.zendesk.com/hc/article_attachments/43671928163611)

****一旦您的营销活动发送，退出标准就会被锁定****

发送活动中的第一条消息后，退出条件将被锁定，并且无法再更改或关闭该活动。相反，如果在发送第一条消息之前未启用退出条件，则无法为营销活动的其余部分启用退出条件。

此外，在计划消息时，退出条件会暂时锁定，但可以通过将计划的消息恢复为草稿来解锁。

## 故障排除

- 如果退出条件呈灰色，则表示至少已安排或发送一条消息并且设置已锁定。
- 如果您想排除在营销活动开始之前****转换的个人资料，请使用受众构建器中的“不发送”字段排除它们
- 自定义转化指标不能用作转化指标，因此它们不会出现在下拉菜单中。