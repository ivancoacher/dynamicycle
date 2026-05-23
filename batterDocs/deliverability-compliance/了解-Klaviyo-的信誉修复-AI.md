---
id: 6192
title: "了解 Klaviyo 的信誉修复 AI"
slug: "reputationrepairai"
category: "投递与合规（Deliverability &amp; Compliance）"
category_slug: "deliverability-compliance"
wp_url: "https://dynamicycle.com/docs/reputationrepairai/"
wp_modified: "2026-01-06T07:15:42"
---

##### 使用 Reputation Repair AI 的前提条件

要获得使用 Reputation Repair AI 的资格，您的账户必须满足以下前提条件：

- ****送达率得分（Deliverability Score）低于 50****（即处于 Poor的状态）。
- 当前****未处于****活跃的Guided Warming阶段。
- 拥有至少 ****5,000 个活跃 Profile****。
- 在 Klaviyo 中拥有****参与互动数据****（即过去 30 天内至少有 100 次邮件点击或打开）。对于新账户，这些数据可以从以下ESP同步：
  - Mailchimp
  - Constant Contact
  - Campaign Monitor
  - ExactTarget
- 在过去 30 天内，至少发送过 ****1 个接收人数达到或超过 1,000 人****的 Campaign（包括在上述 4 个符合条件的 ESP 上发送的记录）。

##### Reputation Repair AI 的运作流程

Reputation Repair AI 的核心流程是仅向特定的活跃细分人群（即：近期点击过、打开过邮件或新订阅的 Profile）发送 Campaign，并随着您送达率得分的提高，逐渐扩大发送范围。

在整个过程中，Klaviyo 会自动从您的发送列表中移除不活跃的 Profile。您可以通过发送一定数量的“达标 Campaign”，或者让 30 天送达率得分超过 75 分，来晋级到下一个阶段。

****达标 Campaign 的定义：**** 发送人数至少为 1,000 人，且该次发送的送达率得分至少为 75 分。

###### 修复阶段详解

- ****Phase 1（第一阶段）**** 发送范围限制在：过去 ****30 天内****有互动记录的 Profile ****或者****过去 ****30 天内****新订阅的 Profile。
- ****Phase 2（第二阶段）**** 发送范围限制在：过去 ****60 天内****有互动记录的 Profile ****或者****过去 ****60 天内****新订阅的 Profile。
- ****Phase 3（第三阶段）**** 发送范围限制在：过去 ****90 天内****有互动记录的 Profile ****或者****过去 ****90 天内****新订阅的 Profile。
- ****Phase 4（第四阶段）**** 发送范围限制在：过去 ****120 天内****有互动记录的 Profile ****或者****过去 ****120 天内****新订阅的 Profile。

晋级下一阶段所需的达标 Campaign 数量取决于您的****发送频率****。发送越频繁的用户，需要发送更多次高绩效的 Campaign 才能进入下一阶段并最终完成整个信誉修复过程。

##### 基于发送频率完成修复流程的要求

****每日发送者（每月发送 20 天以上）：****

- 在每个阶段发送 5 个达标 Campaign（即：总计 20 个）
- ****或者****当前 30 天送达率得分高于 75 分。

****每周发送 3 次者（每月发送 12-19 天）：****

- 在每个阶段发送 3 个达标 Campaign（即：总计 12 个）
- ****或者****当前 30 天送达率得分高于 75 分。

****每周发送 2 次者（每月发送 8-11 天）：****

- 在每个阶段发送 2 个达标 Campaign（即：总计 8 个）
- ****或者****当前 30 天送达率得分高于 75 分。

****每周发送 1 次者（每月发送 4-7 天）：****

- 在每个阶段发送 1 个达标 Campaign（即：总计 4 个）
- ****或者****当前 30 天送达率得分高于 75 分。

****每月发送者（每月发送 1-3 天）：****

- 在每个阶段发送 1 个达标 Campaign（即：总计 4 个）
- ****或者****当前 30 天送达率得分高于 75 分。

##### 开始信誉修复流程

如果您的账户符合使用 Reputation Repair AI 的资格，当您创建新的 Campaign 时，会在 Campaign 向导页面看到以下****弹窗****。

![A welcome popup for Reputation Repair on Klaviyo highlighting a deliverability score of 47 and offering tips for maintaining email reputation.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-39.png?resize=691%2C441&ssl=1)

在为您选择 Campaign 接收者时，您会看到一个额外的板块。在这里，您可以查看您的信誉修复计划（Reputation Repair Plan），并****自动排除****不活跃的 Profile。

![界面显示 Reputation Repair 选项，提供排除不活跃收件人的建议，显示需跳过的收件人比例及进度信息。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-40.png?resize=1024%2C426&ssl=1)

****Exclude unengaged profiles****（排除不活跃 Profile）选框默认处于勾选状态，以便自动从您的 Campaign 中排除不活跃的 Profile。

Klaviyo 会根据在互动期内 Profile 的打开记录（排除 Apple Mail Privacy Protection 的打开记录）以及点击记录来衡量参与度（Engagement）。

##### Reputation Repair AI 侧栏 (Drawer)

当您选择 ****View repair plan****（查看修复计划）时，信誉修复侧栏将会打开，并显示以下信息：

- ****Reputation repair progress（信誉修复进度）**** 显示您当前所处的信誉修复阶段。 这里显示的时间线（例如：30 天、60 天等）是指您的发送对象中包含的 Profile 的****参与互动期****。
- ****Current deliverability score（当前送达率得分）**** 根据过去 30 天的数据显示您当前的送达率得分，以及随时间变化的趋势。
- ****Unengaged profiles removed（已移除的不活跃 Profile）**** 显示从您的发送中排除的 Profile 的互动期限，并详细列出活跃 Profile 与不活跃 Profile 的分布情况。

![A screen displaying the 'Reputation Repair Plan' in Klaviyo AI, showing a deliverability score of 50, labeled as 'Fair', along with statistics on engaged and unengaged profiles over 30, 60, 90, and 120 days.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-41.png?resize=651%2C1024&ssl=1)

##### 最终结果

完成信誉修复流程后，您的送达率得分（Deliverability Score）将达到 ****75 分或以上****。这一得分代表了极佳的送达表现，邮件服务商（Inbox Providers）会更加青睐您品牌发送的邮件，因此邮件更有可能进入接收者的****主收件箱（Main Inbox）****。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)