---
id: 6010
title: "Klaviyo Billing 运作机制"
slug: "klaviyobillingworks"
category: "账户与计费（Account &amp; Billing）"
category_slug: "account-billing"
wp_url: "https://dynamicycle.com/docs/klaviyobillingworks/"
wp_modified: "2026-01-04T01:58:43"
---

了解 Klaviyo 如何针对 Profiles（配置文件）和 Emails、Mobile Messaging（移动消息）、Reviews、Advanced Klaviyo Data Platform（原名“CDP”）、Marketing Analytics（营销分析）、Customer Hub、Helpdesk 以及 Customer Agent 向客户计费。

本文仅适用于未使用****手动 billing****（即未签署长期合同）的客户。

##### ****查看并更改您的 Billing 方案****

要查看您的方案，请按照以下步骤操作：

1. 点击左下角的组织名称。
2. 点击 [Billing](https://www.klaviyo.com/settings/billing)。
3. 进入 [Overview](https://www.klaviyo.com/settings/billing/overview)选项后，您将能够查看当前付费的方案。Monthly Total（月度总额）反映了如果您在 billing 周期更新前未对账户进行任何更改，即将支付的下月总额。

您还可以在更改方案时查看其他 Klaviyo 方案的价格。操作如下：

1. 选择左下角的账户名称。
2. 导航至 [Billing](https://www.klaviyo.com/settings/billing/overview) > Change plan。
3. 打开方案类型下的下拉菜单以查看所有方案。
4. 选择一个方案以查看其价格。

![Klaviyo的更改方案界面，展示了多个营销平台选项，包括Profiles和Email、移动消息和评论，及其对应的费用和可选计划。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-3.png?resize=1024%2C543&ssl=1)

##### ****Billing 方案何时更新？****

所有 Klaviyo 方案每月都会自动更新。具体日期取决于您的个人 billing 周期：

- 免费方案：始终在每月 1 号更新。
- 付费方案：在您的账户开始支付 Klaviyo 费用的日期更新。

要查看您的 billing 周期何时更新：

1. 点击左下角的组织名称。
2. 点击 [Billing](https://www.klaviyo.com/settings/billing/overview)。
3. 查看 Overview 选项卡页面顶部的日期，即为您的周期时间。

从 2025 年 10 月 8 日起，Klaviyo 将客户的使用量周期与 billing 周期进行了统一。您的 billing 周期基于您首次注册 Klaviyo 付费方案的时间，您可以在 Billing Overview 页面查看该信息。在此之前，您的使用量周期在当天午夜结束。通过这种新的简化流程，您的使用量周期和 billing 周期将共享相同的日期和时间。仅时间点发生了变化，billing 日期保持不变，您无需采取任何行动。

- 什么是 billing cycle？

Billing cycle 指的是从上一期账单（或 invoice）结束日期到下一期 billing statement date 之间的 30 天时间周期。
您的 billing cycle 基于您首次订阅 Klaviyo 付费方案的时间确定，可在 Overview page 中查看。

- 我的 billing date 或时间会改变吗？

不会。您的 billing date 和时间将保持不变。不过，您的 usage cycle 将与 billing cycle 对齐，以确保一致性。

- 我可以在哪里查看 billing date 和时间？

您可以在 Billing Overview page 中，在 Billing Cycle 旁查看对应的 billing date 和时间。

- 我需要做什么吗？

不需要。此次更改将自动生效。

- 我可以更改 billing cycle 吗？

目前暂不支持更改 billing cycle。

- 为什么现在要进行这项更改？

我们持续优化客户体验。本次调整主要用于改进后台系统，对客户几乎没有影响。

- 我可以选择不进行这项更改吗？

不可以。此次更改将自动生效。

- 如果本月的 usage period 变长或变短，会发生什么？

本次调整的时间差不会超过一天，预计不会对 usage 产生影响。

##### 了解 Klaviyo 的产品与方案类型

所有 Klaviyo 方案均按月计费，billing 周期从您开始使用付费方案的当天起计算。

目前共有 9 个可用产品：

- ****Klaviyo Marketing****Profile and Email
  Mobile Messaging（SMS、MMS、WhatsApp 及其他移动渠道）
  Reviews
- ****Klaviyo Service****Customer Hub
  Customer Agent
  Helpdesk
- ****Klaviyo Data Platform****Advanced Klaviyo Data Platform（KDP，原名 CDP）
- ****Klaviyo Analytics****Marketing Analytics
- ****Klaviyo Success****
- ****Profile and Email（即基础方案）****

Profile and Email 方案的费用基于以下两个因素计算：

- 您账户中的 active profiles 数量
- 当前 billing cycle 内发送的 email 数量

###### 什么是 active profiles？

这意味着，如果您有 7,000 个 active profiles，您的方案必须至少支持 7,000 个 profiles。

您可以向任意 active profiles 发送 email。
您可以平均向所有 profiles 发送（例如每个发送 10 封），也可以向部分分组发送更多、向其他分组发送较少（例如向 A 组发送 100 封，向 B 组发送 1 封）。

Klaviyo 仅对实际从系统中发出的消息计费。
任何成功送达或退回（bounced）的 email 都会计入方案上限，而被跳过（skipped）的 email 不会计入。

###### Mobile Messaging

Mobile Messaging 方案完全基于 message credits 计费，也就是您每月计划发送的移动消息数量。

发送短信时所需的 credits 数量取决于以下 3 个关键因素：

- 订阅者所在的国家或地区（如 US、UK、AUS 等）
- 发送的消息类型（SMS、MMS 或 WhatsApp）
- message segments 的数量

###### 什么是 message segment？

举例来说，如果您要向 100 人发送一条 SMS，其中 50 人在 United States，50 人在 Canada，下表展示了对应的 credit 计算方式：

Country | Credit | # of recipients | Message segments | Total
United States | 1 | 50 | 1 | 1 × 50 × 1 = 50
Canada | 3 | 50 | 1 | 3 × 50 × 1 = 150

合计：50 + 150 = 200 credits
需要注意的是，被跳过（skipped）的消息和收到的 inbound messages 不会消耗 credits，但发送失败的消息仍会扣除 credits。此外，short codes 的费用不包含在 Mobile Messaging 方案内，需单独计费。

###### WhatsApp

Klaviyo 遵循 Meta 的计费模式，即按 template 计费，而不是按 conversation 计费。
这意味着，只要 marketing 或 utility / transactional template 消息成功送达，就会产生费用。

在 Klaviyo 中，WhatsApp 消息同样以 credits 方式计费，并使用与 Mobile Messaging 方案相同的计费体系。
购买包含 credits 的方案后，您可以将 credits 用于 SMS、MMS、WhatsApp，或任意组合使用。

WhatsApp 消息需要多少 credits？
与 SMS 类似，每条 WhatsApp 消息所需的 credits 数量取决于以下因素：

发送目标国家或地区
消息类型：
Marketing（也称 promotional）
Transactional（也称 utility）

![A detailed table displaying marketing, transactional, and service credits for various regions, including Argentina, Brazil, France, Germany, and more.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-189.png?resize=1024%2C856&ssl=1)

###### 如何购买 WhatsApp credits？

要通过 Klaviyo 开始发送 WhatsApp 消息，您的账户中必须有 Mobile Messaging credits。

对于已签约客户（即采用手动计费的客户），请联系您的 Klaviyo success representative，将 credits 添加到您的方案中。如果您已经有 credits，可直接用于发送 WhatsApp 消息。

如果您未签约（非 contract 客户），可以随时获取 credits：

如果您已经有 Mobile Messaging 方案，可直接使用现有 credits 发送 WhatsApp 消息，或通过升级方案获取更多 credits。
如果您还没有 Mobile Messaging 方案，则需要先在 Klaviyo 中完成 Mobile Messaging 的设置。

##### Klaviyo Reviews

Klaviyo Reviews 仅适用于 Shopify 和 WooCommerce 商店。

通过使用该产品，您可以收集、展示并管理商品评价。

Klaviyo Reviews 的定价基于您网站每月产生的订单数量。

###### 什么情况下会被计为一个 “order”？

这里的 “order” 指的是根据客户在 Klaviyo 中的配置，在平台内生成的一个 Ready to review 事件。
每一个 Ready to review 事件都会计入您的 Klaviyo Reviews 方案额度。

Ready to review 事件会在满足以下条件时触发：

自订单完成（fulfilled）或送达（delivered）起，已经过您设置的指定天数
该订单符合评价条件（eligible for reviews）

###### 我可以将某些订单排除在评价范围之外吗？

可以。您可以在电商平台中，为某个商品、客户或订单添加 klaviyo\_reviews\_exclude 标签，将其设为不参与评价。

###### 不符合评价条件的订单也会被计费吗？

不会。不符合评价条件的订单不会计入方案上限。
需要注意的是，klaviyo\_reviews\_exclude 标签不具备追溯效力。也就是说，如果评价邀请已经发送，再添加该标签无法撤销该操作，该订单仍会计入 Klaviyo Reviews 的计费方案中。

##### Customer Hub

Customer Hub 通过将个性化、商品推荐和自助式支持整合在同一个站内界面，为消费者提供个性化的客户账户体验。

Customer Hub 的定价基于您的 active profile 数量，起价为每月 20 美元，最多支持 10,000 个 active profiles。

##### Helpdesk

Helpdesk 将 AI 与人工客服整合到一个统一的工作空间中，支持通过 email、chat、SMS、WhatsApp 以及社交渠道与客户沟通。

Helpdesk 的定价基于由消费者发起的 tickets 数量，起价为每月 10 美元，最多包含 50 个 tickets。

Ticket 指的是由消费者发起的消息，或在适用情况下，由 “Customer Agent” 发起并升级为需要人工客服处理的支持请求。这些消息通过支持的渠道发送，并需要人工客服介入。
Ticket 在创建时即计入费用。

Helpdesk 提供 AI 垃圾信息检测功能，会对来自客户的消息进行审核，并自动标记非真实客户咨询的 tickets（例如 iMessage 自动回复、email 的 OOO 自动回复，以及恶意发送的垃圾或钓鱼信息）。
此类消息不会计入 ticket 数量，也不会产生费用。

****如何定义一个 Ticket？****Ticket 指的是由消费者发起的消息，或在适用情况下，由 “Customer Agent” 发起并升级为需要人工客服支持的支持请求。
该消息需通过支持的渠道发送，并需要人工客服介入。Ticket 在创建时即开始计费。

****Ticket 可以保持打开状态多久？****

每个 Ticket 会在以下任一情况发生时关闭（以最先发生者为准）：

- 在 48 小时后自动关闭
- 由客户手动关闭
- 通过其他基于规则的自动化方式关闭

****Ticket 关闭后会发生什么？****Ticket 关闭后，如果同一位消费者再次发起需要人工客服支持的消息，将会创建一个新的 Ticket。
客户需单独承担与该 Ticket 相关的其他服务使用费用（例如 SMS 或 email 的发送费用）。

****在 Helpdesk 中创建的 Spam tickets 会计费吗？****不会。Helpdesk 中位于 spam 文件夹内的 tickets 不会计费。
如果您将其标记为非 spam，同样不会产生费用。

##### Customer Agent

Customer Agent 是一款 7×24 小时运行的 AI 助手，可在购买前和购买后为客户提供支持，包括解答问题、推荐商品以及即时处理问题。
Customer Agent 目前支持 SMS、web chat 和 email，WhatsApp 与 RCS 即将上线。

Customer Agent 的定价基于已解决的、由消费者发起的 conversations 数量，起价为每月 50 美元，最多包含 75 个 conversations。
Conversation 指的是在支持的渠道上，由消费者发起并由 Klaviyo 的 “Customer Agent” 全程处理的对话。

****Conversation 可以保持打开状态多久？****当 “Customer Agent” 提供回复后，如果在 48 小时内消费者没有再回复，该 Conversation 即视为完成并开始计费。

****如果 Customer Agent 未能解决该 Conversation，会发生什么？****被升级给人工客服处理的 conversations 不会计入消费量（如适用，也包括升级至 Helpdesk 的情况）。
与 AI Conversation 同时产生的其他服务使用（例如 Mobile Messaging 或 email 发送）需另行计费。

##### Marketing Analytics

Marketing Analytics 提供可执行的客户与商品洞察，帮助您通过更多数据和使用场景来丰富营销策略，实现更精准的个性化营销。
Marketing Analytics 不包含在 Klaviyo 的基础 email 与 profiles 方案中，需单独订阅才能使用相关功能。

Marketing Analytics 的定价基于您的 active profile 数量，起价为每月 100 美元，最多支持 13,500 个 active profiles。

****什么是 active profiles？****在 Klaviyo 中，任何可以通过系统发送 email 的 profile，无论其是否已同意接收邮件，都被视为 active profile。
这包括已订阅的用户，以及通过一般互动被添加的用户（例如在结账页面留下 email，但未明确选择订阅）。

这意味着，如果您有 7,000 个 active profiles，您的方案必须至少支持 7,000 个 profiles。

****如何为账户添加 Marketing Analytics？****如果您当前使用的是 Advanced KDP 方案，需要先取消该方案，才能添加 Marketing Analytics。您可以查看 Klaviyo 中关于如何取消方案的相关说明。

对于其他用户，或在取消 KDP 方案后，只需按照添加或更改方案的步骤操作即可。

##### Advanced Klaviyo Data Platform（此前称为 CDP）

Advanced Klaviyo Data Platform（KDP）此前名为 CDP，以下将统一称为 “Advanced KDP”。

Advanced KDP 不包含在 Klaviyo 的基础 email 与 profiles 方案中，需单独订阅才能使用相关功能。

由于 Advanced KDP 可帮助您更全面地了解所有客户（不仅限于您发送营销内容的用户），其方案定价基于您 Klaviyo 账户中的 total profiles 数量。

total profiles 指所有存储并被 Klaviyo 跟踪的 profiles，包括：

- Subscribers（email、mobile messaging、push 等）
- Suppressions
- Non-subscribers

您可以前往 Audience > Profiles 查看当前的 profile 数量。

****为什么 Advanced KDP 基于 total profiles 而非 active profiles 计费****

通过 Advanced KDP，您可以对所有 profiles 及其相关数据进行激活、转换和分析，而不仅仅是用于营销触达的 active profiles。

这些功能可帮助您更深入地了解客户、其行为以及整体趋势，从而优化营销和业务策略。

即使是被 suppressed 的用户，您仍然可以通过以下方式洞察整个客户群体：

- 通过 RFM analysis 和 audience performance comparison，分析历史趋势，识别可重新触达的用户及分群
- 通过 funnel analysis 识别退订行为中的模式，从而降低 unsubscribe rate
- 通过 Group membership API，无论订阅状态如何，实现个性化的站内体验
- 通过 data transformation 转换 profile 属性，提升数据质量，并建立可信的 customer source of truth，用于分析决策

##### 自 2025 年 10 月 24 日起：Customer Hub、Marketing Analytics 和 Advanced Klaviyo Data Platform 的按比例计费（Proration）

自 2025 年 10 月 24 日起，购买 Customer Hub、Marketing Analytics 和 Advanced Klaviyo Data Platform 将适用按比例计费（proration）。在以下情况下将触发 proration：

- 在 billing cycle 中途首次购买其中任一方案
- 在 billing cycle 中途升级其中任一方案

按比例计费金额将根据您当前 billing cycle 剩余的时间计算。
例如，如果您在 billing cycle 进行到一半时购买了一个每月 $100 的 Marketing Analytics 方案，那么该周期只需支付 $50；在下一个 billing cycle，您将支付完整的 $100。

您可以在通过邮件发送给您的 invoice 中查看按比例计费的费用明细（也可在 Klaviyo 账户的 Billing Settings 中下载 invoice）。
自 2025 年 10 月 24 日起，proration 将自动生效，您无需进行任何操作，即可适用于 Customer Hub、Marketing Analytics 和 Advanced Klaviyo Data Platform。

##### 达到方案上限时会发生什么

当您达到方案上限时，具体处理方式取决于产品类型。

基于用量计费的产品（如 Email、Mobile Messaging、Helpdesk 和 Customer Agent）在产生超额用量时的处理方式相似。
而 Advanced KDP、Marketing Analytics 和 Customer Hub 等产品则基于 Active Profiles 计费，Active Profiles 会随着业务增长而增加，这三类产品在超额情况下的处理逻辑也基本一致。

##### Email 和 Mobile Messaging

对于营销类产品，达到上限后的处理方式取决于您触及的是哪种限制（profile 上限或发送量上限），以及所使用的产品类型。

###### Profile 上限

当您的 active profile 数量超过当前方案上限时，Klaviyo 不会阻止您继续发送消息或添加新的 profiles。
但系统会向您发出通知，并在下一个 billing cycle 自动将您升级到一个支持更多 profiles 的更高方案等级。

需要注意的是，profile enforcement 与 Automatically upgrade 设置不同。Automatically upgrade 是一项可选功能，会在您达到消息发送上限时自动升级到更高方案。

如果您不希望被升级，可以通过管理 active profiles 数量，使其保持在当前方案允许的范围内。

如果您使用的是免费的 Profiles & Email 方案，且已超过 profile 上限，系统不会为您自动升级方案，但在 active profile 数量降回上限以内之前，您将无法发送 email（也无法将 flow emails 设置为启用状态）。

###### Send 或 credit 上限

当您的账户达到方案的发送上限（例如 email 发送量或 mobile messaging credits 用尽）时，您可以选择以下三种方式之一：

- 使用 flexible overage plans（即 flexible sending），可额外获得下一个方案等级对应的完整发送量。flex 的费用基于您当月开始时所使用的基础方案的单价计算。
- 手动升级，或通过 auto-upgrade 升级到更高等级的方案。如果您的升级需求较为持续，升级方案通常比使用 flex sending 更具成本优势。
- 停止所有发送，直到下一个 billing cycle 开始。

![An infographic illustrating three options when reaching a plan limit: 'Stop sending', 'Upgrading', and 'Flexible sending'. Each option is paired with a visual representation of a person interacting with boxes.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-190.png?resize=1024%2C430&ssl=1)

##### Helpdesk & Customer Agent

Helpdesk 和 Customer Agent 的计费逻辑与 Email 和 Mobile Messaging 类似，但 Helpdesk 基于 tickets 计费，Customer Agent 基于 conversations 计费。

对于 Service 类产品，当您达到方案上限时，并不会停止您继续使用产品。
一旦您购买了 Customer Agent 或 Helpdesk，即表示您同意为该产品承担最低消费，并为超出方案范围的使用量支付 overages 费用。

当超出方案上限时，会产生 usage fee。
在购买 Helpdesk 或 Customer Agent 后，系统会默认将您的计费偏好设置为 Flexible Overages，用于处理产生的任何 overages。
您可以随时前往 Billing > Billing Preferences，将该偏好更改为 Auto-Upgrade。

要继续使用 Helpdesk 和 Customer Agent，您必须启用 Flexible Overages 或 Auto-Upgrade 其中之一。
如果您希望停止产生 overages，可以在产品内关闭 Customer Agent 或 Helpdesk，或直接取消相关方案。

##### Reviews

Reviews 方案的逻辑与 email 和 SMS 类似，但计费基础不是消息数量，而是来自您商店的 orders 数量。

例如，如果您的方案允许 20 个 orders，则您只能为这 20 个订单发送评价邀请。
当达到方案上限后，您可以选择手动升级方案，或暂停发送评价邀请，直到 billing cycle 更新。

##### Advanced Klaviyo Data Platform (KDP)

Advanced KDP 方案采用“方案费用 + 超额用量费用”的计费方式。

当超出方案上限时，将产生 usage fee，计算方式如下：
超出当前方案的 profile 数量（以每 1,000 个为单位） × 当前方案每 1,000 个 profiles 的单价。

使用费用示例

假设 Funky T-shirts 公司每月支付 $4,765，使用的是支持 100 万 profiles 的 Advanced KDP 方案。
但在下一个月，其 profile 数量增长至 152 万，超出方案 52 万 profiles。

系统不会强制 Funky T-shirts 升级到下一个方案等级（200 万 profiles，$9,100），而是按以下方式计算 usage fee：

****超出部分的 1,000 profiles 数量：520×当前方案每 1,000 profiles 的价格：$4.77****

usage fee 总计：$2,480.40

这意味着该月的总费用为方案费用 $4,765 + usage fee $2,480.40 = $7,245.40，
低于直接升级方案所需的费用。

与其他产品不同，Advanced KDP 的 usage fee 是在使用后计费，而不是预付。

通常情况下，如果您的使用量低于下一个方案等级的 85%，承担 usage fee 会更具成本优势；
当使用量达到或超过下一个方案等级的 85% 时，升级方案会更划算。

usage fee 将体现在下个月的 invoice 中。

##### Marketing Analytics

Marketing Analytics 方案基于 active profiles 计费。
系统会在 billing cycle 结束时，根据您账户中的 active profile 数量，自动调整方案等级，并在下一个 billing cycle 开始时生效。

##### Customer Hub

Customer Hub 同样基于 active profiles 计费。
系统会在 billing cycle 结束时，根据您账户中的 active profile 数量，自动升级或降级方案，并在下一个 billing cycle 开始时生效。

##### 升级与降级 billing plan

您可以在 billing cycle 内的任意时间升级或降级方案，但需注意以下规则：

- 升级会立即生效，并在您选择降级之前持续有效

每次升级后，单条消息的成本都会降低，方案等级越高，性价比越高

- 降级将在下一个 billing cycle 开始时生效

如果您的 active profile 数量超过目标低等级方案的上限，则无法降级
如在 billing cycle 中途降级，Klaviyo 不会退款（详见服务条款）
如果您已选择降级，但随后又进行升级（无论是手动还是自动），该降级将被取消

- 只有在以下情况下，降级才会在下一个 billing cycle 之前生效：

您取消了相关方案
您关闭账户，并选择立即生效

###### How to change plans

请注意：如果您当前使用的是 Advanced KDP 方案，并希望切换至 Marketing Analytics，必须先取消 Advanced KDP 方案，之后才能添加 Marketing Analytics。

更改方案的操作步骤如下：

- 在左下角选择您的 account name
- 点击 Billing
- 选择 Change plan
- 在您想要更改的 plan 类型下，打开对应的下拉菜单

![用户计划更新页面，显示当前个人资料和邮件发送限额，提供不同方案选项供选择。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-191.png?resize=1024%2C652&ssl=1)

- 选择你的套餐。

如果你要降级 Email 和 Profiles 套餐，当前账户中的 Active Profiles 数量必须少于你要切换到的套餐上限。

- 点击 Continue to payment以确认套餐更改。

###### Klaviyo 还提供了多种设置，可用于自动切换套餐：

****自动升级（也称 auto-upgrade）****依据：超额使用的单位数量（消息、工单、会话）
适用于：

- Mobile Messaging
- Email and Profiles
- Helpdesk
- Customer Agent

****灵活发送（Flexible sending）****依据：超额使用的单位数量（消息、工单、会话）
适用于：

- Email and Profiles
- Mobile Messaging（仅限 $495 及以上套餐）
- Helpdesk
- Customer Agent

****自动降级（Auto-downgrade）****依据：Profiles 数量
适用于：

- 仅限 Email and Profiles，并且需要开启 flexible sending

****手动升级（None 选项）****依据：任意条件
适用于：

- 除 Marketing Analytics 以外的所有套餐

说明：

- Marketing Analytics 和 Email & Profiles 都会基于 profiles 数量自动升级，但该行为无法关闭。
- Marketing Analytics 和 Customer Hub 会基于 profiles 数量自动降级，该过程是自动发生的，无法手动开启或关闭。

你可以随时在这些选项之间进行切换。

##### 如何选择不同的升级/降级选项

- 点击左下角的账户名称。
- 前往 ****[Billing](https://www.klaviyo.com/settings/billing/overview) > [Preferences](https://www.klaviyo.com/settings/billing/preferences)****。

![Klaviyo设置页面的计费选项卡下，显示账户偏好的选项菜单。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image.png?resize=420%2C532&ssl=1)

- 找到您想要更改选项的方案（例如：电子邮件、Mobile Messaging 等）。

![Klaviyo Email upgrade settings interface showing the option to select email upgrade preference with a dropdown menu.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-1.png?resize=1024%2C393&ssl=1)

- 打开下拉菜单。

选择以下选项之一，以更改当该方案达到计划限制时的处理方式：

- None（无）：停止发送或手动升级。
- Automatically upgrade（自动升级）：启用自动升级功能。
- Flexible overages（弹性超额）：使用弹性方案。

注意与升级或弹性发送相关的费用。

![A screenshot displaying the current SMS plan details, including pricing and allowance for monthly SMS credits, with an option for flexible sending plan upgrades.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-2.png?resize=762%2C322&ssl=1)

点击 Update 以保存设置。

##### 使用弹性超额 (Use flexible overages)

****Flexible sending（弹性发送）**** 适用于 Email、Mobile Messaging、Helpdesk 和 Customer Agent 方案。该功能****不适用于**** Reviews、Advanced KDP、Marketing Analytics 和 Customer Hub 方案。

当您在使用弹性超额期间达到方案上限时，系统会为您提供一次性附加额度，包含下一更高层级方案中所有的配置文件和消息额度，而不会永久升级您的账户。通过这种方式，您可以保持当前方案，无需担心在下一个 ****Billing**** 周期前还需要手动降级。

弹性超额的费用是根据您当前方案的单位成本以及下一层级方案的容量来计算的。弹性操作是一次性购买，包含下一层级的所有容量（短信的点数，电子邮件的配置文件和消息数），并按您当前方案的单价计费。这意味着，虽然弹性操作没有额外的手续费，但通常比直接升级更贵，因为升级到更高层级后，您通常可以享受更低的大宗单价。

您可以在 ****Billing Preferences****选项卡或结账页面查看弹性超额的具体费用。

- 弹性升级方案示例 (Example of flexing up plans)

假设 Funky T-shirts 公司支付 $7,000 购买了一个电子邮件和配置文件方案，该方案允许拥有 7,000 个配置文件并发送 70,000 封邮件。然而，下个月适逢“黑色星期五/网络星期一（BFCM）”，他们需要发送 80,000 封邮件。

Funky T-shirts 可以选择弹性升级，而不是永久升级账户：

当前单位费率：方案成本 ($7,000) / 邮件数量 (70,000) = 0.1

乘以后一档层级与当前层级的邮件差额：下一层级 (80,000) – 当前层级 (70,000) = 10,000

弹性升级费用 (Flex cost)：0.1 × 10,000 = $1,000

- 何时选择升级 vs. 弹性方案

弹性升级通常比直接升级更贵。当您选择弹性方案时，您是以当前层级的每条消息成本购买下一层级的所有配置文件、发送量或点数。如果您频繁使用弹性方案，直接升级会更具性价比。

弹性升级适用于：不经常超出方案限制的情况。同时，它也适合那些不想费心去记住在下个周期前手动降级的用户。

- 什么是单位费率 (Unit rates)？

在 Klaviyo 中，单位费率本质上是 1 条消息的价格。计算方法是用方案成本除以消息数量：方案成本 / 消息数量。

- 基于配置文件的自动降级 (Auto-downgrading based on profiles)

自动降级功能：

- 仅在使用弹性发送时，适用于配置文件方案。
- 对于 Marketing Analytics 和 Customer Hub 方案，该功能始终开启。
- 无法基于邮件发送量进行自动降级。

您可以在 Klaviyo 的 Billing Preferences（首选项）页面中选择对您的电子邮件和配置文件方案开启自动降级。在 Billing 周期结束前 24 小时，您的方案将自动降级到能够覆盖您当前活跃配置文件数量的最低层级。降级将在下一个周期生效。

##### ****基于使用量自动升级（也称为 Auto-upgrade）****

****Auto-upgrad****计划限额的功能仅适用于 Profile & Email 方案、Mobile Messaging 方案、Helpdesk 方案以及 Customer Agent 方案。当您达到使用量限制（如电子邮件数量、移动消息点数、工单数或会话数）时，系统会自动将您提升至下一个层级。

| ****支持自动升级**** | ****不支持自动升级**** |
| --- | --- |
| ****Email**** | ****Reviews**** |
| ****Mobile Messages**** | ****Advanced KDP**** (原 CDP) |
| ****Helpdesk**** |  |
| ****Customer Agent**** |  |

此功能可确保您不会触及每月发送限制，从而能够不受阻碍地继续发送移动消息、电子邮件和自动化 Flow。

###### ****当我被自动升级时会发生什么？****

在您****开启自动升级****后：

- ****触发条件****：当您遇到以下任一情况时：
  - 达到方案的消息限制（例如：您的方案允许发送 2,000 封邮件，但您尝试发送更多）。
  - 排期发送的 Campaign 将导致您超过当前 ****Billing**** 窗口的消息限制。
- ****升级结果****：自动升级会将您移至更高一级方案。
- ****注意事项****：
  - 您可以在 ****Billing**** 周期内的任何时间被自动升级。
  - 账户一旦升级，系统会立即向 Owner 发送电子邮件告知此项更改。
  - 一旦进入更高层级的方案，您将保持在该层级，直到您手动选择降级、再次升级或再次被自动升级。****系统不会为您自动降级。****

当您选择升级时，在第一个月内，您只需支付“基础套餐”（即进入该 ****billing**** 周期时的套餐）与您升级到的套餐之间的****差额****。

如果您一年内使用弹性方案（Flexing）超过几次，建议您直接选择升级，因为这样通常更具成本效益。

##### ****手动升级或停止发送：使用 None 选项****

如果您希望手动选择升级时机，或者在达到套餐限制时停止发送，您可以将 ****billing**** 升级偏好设置为 ****None****。

- ****操作路径****：前往 [****Settings****](https://www.klaviyo.com/settings) ****> [Billing](https://www.klaviyo.com/settings/billing/overview) > [Preferences](http://e7199a37-af03-44c4-b3e3-9027c3356650)****。
- ****具体影响****：这意味着您将无法发送任何 Flow（自动化流）和 Campaign（营销活动）消息，且当前 ****billing**** 周期内已排期的任何消息都将被取消。但是，如果您决定升级或使用弹性方案，则可以恢复发送。
- ****注意****：****None**** 选项仅适用于电子邮件（Email）和移动消息（SMS）方案。

##### ****调整信用卡详情****

Klaviyo 不支持在单个账户中绑定多张信用卡。如果您使用与账户中现有的不同的信用卡购买套餐，系统将更改备案的信用卡。如果支付失败，账户所有者（Owner）和 ****billing**** 联系人将收到电子邮件提醒。

- ****如何更新****：有关如何更改备案信用卡的详细信息，请参阅关于更新信用卡信息的文章。
- ****查看发票****：要查看发票及近期费用的详细信息，请选择 ****[Billing](https://www.klaviyo.com/settings/billing/preferences) >**** [****Payment History****。](https://www.klaviyo.com/settings/billing/payment-history)

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)