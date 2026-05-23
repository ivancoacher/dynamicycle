---
id: "50585012261531"
title: "如何通过 Klaviyo 管理和分发 Punchh 优惠"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/50585012261531-How-to-manage-and-distribute-Punchh-offers-via-Klaviyo"
section: "PAR Punchh"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-19T20:05:57Z"
language: "zh"
---
## 你将会学到

了解如何直接在 Klaviyo 中创建和管理 Punchh 奖励优惠，并将其与您现有的列表和细分绑定。这使您能够在使用 Klaviyo 处理分发、消息传递和归因的同时精心策划复杂的忠诚度体验。

## 开始之前

在 Klaviyo 中创建优惠之前，请确保您的 Punchh 帐户中已配置 Punchh 可兑换物品。

## 创建报价

第一步是在 Klaviyo 中定义 Punchh 活动的活动详细信息。

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 单击您的 ****Punchh**** 集成。
3. 在**优惠管理**部分中，单击****创建优惠。****

![Punchh 集成设置页面显示连接详细信息、Webhook 设置、订阅者同步和优惠管理。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/4e973b74ddaacb1191bb086389870128a24d650c-3456x1688.png)

4. 在 Klaviyo 中创建新的 Punchh 活动，并输入活动的 **名称** 和 **开始日期**。

- 您最多可以选择未来 3 个月后的开始日期。

![营销平台“创建优惠”页面的屏幕截图，显示活动详细信息、可兑换分配的输入字段以及有关最终更改的警告。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/5b2b23ec9dd3c4e3d5289ba079808e7b5eab647a-3456x1662.png)

## 分配可赎回项

定义可兑换项后，您必须通过将客户映射到您的 Klaviyo 数据来决定哪些客户有资格获得哪种奖励。

1. 导航至优惠构建器的****分配可兑换****部分。
2. 在您的可兑换项和特定****Klaviyo 列表或细分**** 之间创建映射。

您可以将单个可兑换项映射到单个 Klaviyo 列表或分段。

![Web 应用程序的“创建优惠”页面，显示“Punchh 活动详细信息”，其中包含“搜索可兑换”的打开下拉菜单和一条警告消息。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/d9c301f2e461ce87b5bb2497be259fb3dadf8991-3456x1662.png)

## 通过 Klaviyo 消息分发奖励

创建报价后，Klaviyo 会自动将 Klaviyo 列表或分段中的配置文件同步到 Punchh 分段（如果 Punchh 中已存在）。当根据您的映射向配置文件发放奖励时，Klaviyo 会通过该配置文件的 Punchh 集成记录****获得的奖励****指标和****奖励****对象。

### 使用已获奖励指标

要使用 Klaviyo 分配 Punchh 奖励，您可以使用 **获得的奖励** 指标来触发自动流程，确保客户在符合条件时收到奖励通知。您还可以使用动态块在消息中包含奖励详细信息。

![](https://klaviyo.zendesk.com/hc/article_attachments/50585012249755)

### 使用奖励对象

要使用 Klaviyo 分配 Punchh 奖励，您还可以使用 **奖励** 对象来触发自动流程并细分您的客户。您还可以使用动态块在消息中包含奖励详细信息。

例如，如果您想在客户的奖励到期之前向其发送提醒，您可以通过引用 **ExpiringAt** 属性，在 **Reward** 对象上设置[日期触发流](https://help.klaviyo.com/hc/en-us/articles/35146374047515#h_01JPTG7J0Q843B5XQGRMB6DVXM)。

![](https://klaviyo.zendesk.com/hc/article_attachments/50585012251291)