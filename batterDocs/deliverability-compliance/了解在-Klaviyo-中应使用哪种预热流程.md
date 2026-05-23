---
id: 6065
title: "了解在 Klaviyo 中应使用哪种预热流程"
slug: "warmingprocess"
category: "投递与合规（Deliverability &amp; Compliance）"
category_slug: "deliverability-compliance"
wp_url: "https://dynamicycle.com/docs/warmingprocess/"
wp_modified: "2026-01-05T07:50:07"
---

##### Warming（预热）

预热是一个至关重要的过程，通过集中向最活跃的客户发送邮件，并逐渐增加从新域名或 IP 发出的邮件量，从而建立初始发件人信誉。任何新发件人在迁移到像 Klaviyo 这样的新电子邮件服务商时，都必须对其发送基础架构进行预热。

##### Ramping

爬坡是辅助整体预热过程的一种手段，无论您使用专用 IP 还是共享 IP，它都能帮助您成为信誉良好的发件人。爬坡涉及从极小量的邮件发送开始，随着时间的推移逐渐增加发送量。

##### 如何选择您的预热流程

根据客户类型、是否拥有互动事件数据、是否使用新域名以及其他潜在因素，您的预热流程可能会有所不同。请参考以下指南决定应遵循哪种流程。

注意：如果您正在与入驻专家（Onboarding Specialist）或客户成功经理（CSM）合作，在开始以下任何流程前，请先与他们确认您具体的预热需求。

##### 预热的使用场景

###### 迁移至Branded Sending Domain的客户

现有的 Klaviyo 客户在迁移至品牌发件域名时，无需再次预热基础架构，只要满足以下条件：


- 域名已注册至少 30 天
- 您已经使用该域名发送过电子邮件（例如：您过去在之前的服务商或在 Klaviyo 的发件人地址中使用过该域名）。

###### 新的 Klaviyo 客户（无论使用共享域名还是品牌域名）如果满足以下条件，请遵循 标准预热流程：

- 拥有互动数据（即：打开、点击等数据）
- 正在使用支持同步打开和点击事件的 Klaviyo 原生集成工具。
- 新注册域名（由新客户或现有客户投入使用）如果是在过去 30 天内创建/注册的。
- 从未用于发送过邮件，也应遵循 标准预热流程。

##### 关于“引导式预热” (Guided Warming)

如果您属于标准预热类别，在您开始增加发送量或满足相关要求时，您的账户中可能会出现引导式预热通知。在引导式预热期间，Campaign 编辑器中会出现一个横幅，根据您所处的预热阶段指导您执行最佳实践。

注意：如果您符合引导式预热资格但 45 天内未发送邮件，预热通知将消失且无法重新启用。在这种情况下（我们强烈建议您进行预热），请遵循 如何预热发件域名 的指南进行手动操作。

###### 没有互动事件或数据的客户

如果您符合以下情况，应使用 平台引入流程 (Platform Introduction Process)：

- 未使用支持同步打开和点击事件的 Klaviyo 原生集成工具
- 根本没有任何可以带入 Klaviyo 的互动数据（例如：您只有基于日期的属性，如“最后打开时间”、“最后点击时间”，而没有具体的事件记录）。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)