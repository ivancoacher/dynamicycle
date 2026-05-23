---
id: "48577674406683"
title: "如何通过 Klaviyo 管理和分发 Thanx 优惠"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/48577674406683-How-to-manage-and-distribute-Thanx-offers-via-Klaviyo"
section: "Thanx"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:03Z"
language: "zh"
---
## 你将会学到

了解如何直接在 Klaviyo 中创建和管理 Thanx 奖励优惠，并将其与您现有的列表和细分相关联。这使您能够在使用 Klaviyo 处理分发、消息传递和归因的同时精心策划复杂的忠诚度体验。

## 开始之前

在 Klaviyo 中创建优惠之前，请确保您的 Thanx 帐户中已配置 Thanx 奖励模板。

## 创建报价

第一步是定义活动详细信息以及您想要提供的不同奖励形式。

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 单击您的****Thanx**** 集成。
3. 在**优惠管理**部分中，单击****创建优惠。****

****！[](https://klaviyo.zendesk.com/hc/article_attachments/48578068237339)****

4. 在 Klaviyo 中创建新的 Thanx 营销活动，然后输入您想要与营销活动关联的 **名称、营销活动周期** 和 **变体**。
   - 每个优惠您最多可以创建 ****4 个变体****。对于每个变体：
     - 输入****变体名称****。
     - 从下拉列表中选择****奖励模板****。
   - 如果您选择从未来开始的****活动期间****，奖励将从该日期开始发放。

除非变体名为“Control”，否则所有变体都需要奖励模板。 “控制”变体允许您出于 A/B 测试目的而扣留特定组的奖励。

![](https://klaviyo.zendesk.com/hc/article_attachments/48577991674139)

## 分配奖励变量

定义奖励变体后，您必须将哪些客户映射到您的 Klaviyo 数据来决定哪些客户有资格获得哪种奖励。

1. 导航至优惠构建器的****分配奖励变体****部分。
2. 为奖励变体到特定 ****Klaviyo 列表或细分**** 的每个映射添加一行。

您可以将单个奖励变体映射到多个 Klaviyo 列表或细分，或将多个变体分配到单个列表或细分。

![](https://klaviyo.zendesk.com/hc/article_attachments/48577991679131)

## 通过 Klaviyo 消息分发奖励

创建优惠后，Klaviyo 会自动将 Klaviyo 列表或细分中的配置文件同步到 Thanx 奖励变体。当根据您的映射向配置文件发放奖励时，Klaviyo 会通过该配置文件的 Thanx 集成记录****获得的奖励****指标和****奖励****对象。

### 使用已获奖励指标

要使用 Klaviyo 分配您的 Thanx 奖励，您可以使用 **获得的奖励** 指标来触发自动流程，确保客户在符合条件时收到奖励通知。您还可以使用动态块在消息中包含奖励详细信息。

**！[](https://klaviyo.zendesk.com/hc/article_attachments/48578068255003)**

### 使用奖励对象

要使用 Klaviyo 分配您的 Thanx 奖励，您还可以使用 **奖励** 对象来触发自动流程并细分您的客户。您还可以使用动态块在消息中包含奖励详细信息。

例如，如果您想在奖励到期之前向客户发送提醒，您可以通过引用 **CampaignRedeemableTo** 或**到期于**属性。

**！[](https://klaviyo.zendesk.com/hc/article_attachments/48578068256923)**

## 其他资源

- [Thanx 入门](https://help.klaviyo.com/hc/en-us/articles/19458074597659)
- [Thanx数据参考](https://help.klaviyo.com/hc/en-us/articles/19457831690139)