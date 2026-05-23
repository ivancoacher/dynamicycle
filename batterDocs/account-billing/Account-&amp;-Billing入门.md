---
id: 5450
title: "Account &amp; Billing入门"
slug: "start-with-account-billing"
category: "账户与计费（Account &amp; Billing）"
category_slug: "account-billing"
wp_url: "https://dynamicycle.com/docs/start-with-account-billing/"
wp_modified: "2025-12-19T08:36:03"
---

##### ****核心概念 — Klaviyo 的计费体系****

在 Klaviyo 中，计费核心围绕以下几个维度：

###### ****1.计费计划****

Klaviyo 的计费是以 月度为周期 的，常见包括：

Profile & Email Plan

- 基于你拥有的 活跃客户 Profile 数量 以及邮件发送量定价。
- 如果当前活跃 profile 超出当前计划允许数，账户会在下一个计费周期自动调整到符合的计划。

Mobile Messaging（短信/WhatsApp 等）

- 使用短信/MMS/WhatsApp 时需购买 “移动消息计划 + 信用额度”。
- 发短信时会消耗 credit（信用额度）。

其他可选产品

- Customer Hub
- Marketing Analytics
- Advanced Klaviyo Data Platform
- Helpdesk / Customer Agent

这些产品根据不同使用量或 profile 数计费。

##### ****如何查看和变更计费计划****

###### ****1.查看当前计费计划****

在 Klaviyo 控制面板中：

1. 点击左下角的组织名称
2. 进入 Billing（计费） 页面
3. 在 Overview（概览） 中查看当前的计划和账单总额

![Klaviyo账单设置界面，显示当前计费周期、账单信息和月度总额。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-98.png?resize=1024%2C587&ssl=1)

你可以在这里看到：

- 当前 plan 名称
- 何时 renew（自动续费）
- 下一个周期将收取费用的金额预估。

###### ****2.更改计划（升级/降级）****

在同一 Billing 页面：

1. 点击 Change plan

![Klaviyo 签约与计费选项的概览，包括下一个计费周期和更新计费信息的按钮。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-99.png?resize=1024%2C593&ssl=1)

- 在需要调整的 plan 类型中下拉选择目标计划
- 确认操作

升级：立即生效

降级：将在 下一个计费周期 生效

（降级前必须确保你的活跃 profile 数符合目标 plan 限额）

##### ****计费周期和自动续费****

****计费周期****

- Klaviyo 的计费周期为每月循环，依据你首次付费日期决定。例如：你在 10 月 15 日开始付费 → 每月 15 日为续费日。

免费计划：统一每月 “1 号” 自动更新；

- 付费计划则按实际开始付费的日期自动续费

##### ****使用量和计费额度****

Klaviyo 提供 Account Usage（账户使用情况） 页面，用于监控：

- 活跃 Profiles
- 邮件发送量
- SMS 信用额度和使用
- Reviews/Helpdesk/Customer Agent 使用量
- 历史计费计划变更记录你可以在 Billing > Account usage 查看最近 3、6、12 个月的使用情况并可导出 CSV。

![A chart displaying active profiles usage over the last three monthly billing cycles in a Klaviyo account, with bars representing the number of active profiles each month.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-100.png?resize=1024%2C610&ssl=1)

##### ****计费相关设置与调整****

###### ****1.修改账单信息****

如需更新账单地址或账单接收的电子邮件地址：

进入 Billing > Preferences（计费偏好）

即可修改 Billing Address（账单地址） 和 Billing Email（账单邮箱）。

![Klaviyo 设置页面，显示账单偏好选项，包括账单地址和账单邮箱的更新框。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-101.png?resize=1024%2C663&ssl=1)

****注意：****

- 只有账户 Owner 或 Admin 才能修改。
- 支持设置不同的账单通知接收邮箱。

###### ****2.信用卡和支付方式****

- Klaviyo 默认使用单一信用卡。
- 如果添加新信用卡支付新的计划，账户上的信用卡将被替换。
- 支付失败时账户 Owner/账单联系人会收到通知。

##### ****共享计费与组合账户****

###### Shared Billing（共享计费）

- 允许最多 20 个 Klaviyo 账户共享一个邮件/短信 Plan。
- 所有消耗（发送次数、短信 credits 等）共用同一个累计额度。

需要特别区分：

- Shared billing 与 Portfolio（组合账户） 是不同概念，组合账户是用于集中管理多个账户的报表和状态，而不是自动共享余额/付费额度。

###### ****报表****

- 在 Billing 页面里，如果账户属于 Portfolio，也可以看到不同账户的费用和使用情况一览表，并可导出详细 CSV。

##### ****自动升级 / 灵活发送****

为了避免因为临时发送高峰导致邮件被阻止，Klaviyo 提供：

###### ****Auto-Upgrade****

系统会在达到当前计划限额后：

- 自动提升到下一个计划层级
- 发送通知邮件
- 保持发送不中断

这在营销高峰、促销期间特别有用。

###### ****Flexible Overage（灵活超出额度）****

针对部分付费计划，当发送量超过限额时：

- 只按当前 plan 的单位成本临时增加额度
- 不必立即升级至更高级 plan

这是应对突发性流量高峰的临时保护措施。

![An infographic explaining three options for managing email messaging limits: stop sending when limits are reached, upgrade to the next tier for more messages, or flexible sending by purchasing additional messages from higher tiers while remaining on the current plan.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/MTY4ODg1NDQyMTY5MTU5Nw_112147_GbgqCR558H_DIKfc_1766129933.png?resize=1600%2C672&ssl=1)

##### ****降级、取消计划与关闭账号****

###### ****降级到免费计划****

如果你想回归免费计划或暂时停止付费：

1. 前往 Billing > Preferences
2. 选择 Reactivate to free（恢复免费版本）
3. 确认操作

你仍保留原有数据，但 SaaS 功能将受免费版限制。

注意：

- 恢复免费版后，需要手动重新开启 Flows 和 Campaign。
- 可能需要重新激活某些集成。

###### ****关闭 Klaviyo 账号****

永久关闭账号会删除所有数据，因此：

- 请先导出重要数据（Profile、Campaign/Flows、Analytics 等）
- 然后依照提示确认关闭账号即可。

##### ****常见计费注意事项（实操贴士）****

###### 1.按 活跃 Profiles计费，而不是发送次数

Klaviyo 最新的计费主要根据：

- 活跃 Profiles 的数量（可发送的目标用户规模）

而不是简单“发了多少邮件”。

这意味着：不与 Klaviyo 同步的历史客户也可能被定义为 “活跃” 并计费（例如集成了 loyalty, referral, survey 等插件也可能产生额外 profiles）

###### 2.降级前必须确保 profile 数在目标计划范围内

如果你想降级至较低计划：

- 当前 活跃 profile 数必须低于该计划允许的上限，否则系统会阻止降级。

###### ****3.Flexible Overage vs Auto Upgrade****

- Flexible Overage：先消耗高计划额度，不改变 plan。
- Auto Upgrade：直接提升 plan，可能更省长期成本。

可根据业务节奏选择开启策略。

##### ****总结****

Klaviyo 的计费体系以 活跃 profile 数和消息使用量为核心，并提供灵活升级、共享计费、账单管理与报表视图等机制，帮助品牌在不同成长阶段管理好预算和发送资源

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)