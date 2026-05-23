---
id: 5233
title: "Helpdesk入门"
slug: "start-withhelpdesk"
category: "会话与沟通（Conversations）"
category_slug: "conversations"
wp_url: "https://dynamicycle.com/docs/start-withhelpdesk/"
wp_modified: "2025-12-17T07:37:09"
---

##### ****什么是 Klaviyo Helpdesk？****

Klaviyo Helpdesk 将你的客户支持消息集成到一个地方。当客户通过你的支持渠道联系时，他们的消息会创建一个 “Ticket”（工单），你的团队成员可以直接在 Klaviyo 内部查看并回复。

##### ****谁应该使用 Helpdesk？****

如果你符合以下情况，请使用 Helpdesk：

- 你有专门的人员或团队负责处理客户咨询。
- 你希望在一个地方管理来自多个渠道的支持对话。
- 你正在使用 Klaviyo，并希望将支持消息与客户数据（例如：Klaviyo profiles、事件和电商活动）关联起来。

##### ****我需要付费才能在 Klaviyo 中回复客户吗？****

不需要！ 如果你的免费试用结束且选择不购买，Klaviyo 会将你的账户降级为免费版的帮助台：Inbox。

Inbox 的功能相对有限，包括：

- Macros（快捷回复）
- Multi-Agent Support（多坐席支持）
- Full Channel support（全渠道支持：邮件、短信、WhatsApp、社交媒体）
- Auto Responders（自动回复）
- Profile details in conversation view（对话视图中的个人资料详情）
- Spam Filtering（垃圾邮件过滤）

##### ****核心术语 (Key terms)****

- Inbox： 客户 tickets 显示的地方，按渠道分类整理。
- Ticket： 团队与客户之间“一对一对话”的载体（工单）。
- Message thread： 在单个 ticket 中交换的一系列消息流，包括客户和客服的回复。
- Inbound message： 客户发给品牌的消息（例如：SMS 订阅者发送“HELP”或网站访客发送 Web Chat 消息）。
- Outbound message： 品牌发出的消息（例如：工单回复、Flows、Campaigns）。

##### ****Inbox 支持的渠道****

- Web chat： 开启后，客户通过 Customer Hub 界面发送的消息会作为新 ticket 进入 Helpdesk。
- Email： 设置转发后，发往支持邮箱（如 support@mycompany.com）的邮件会转为 ticket。
- SMS： 如果你使用 Klaviyo SMS，发送到你号码且不包含关键字的消息将显示为 ticket。
- Instagram： 开启后，发往你 Instagram 主页的私信会创建 ticket。
- WhatsApp： 如果你在 Klaviyo Marketing 中使用 WhatsApp，不包含关键字的消息会显示为 ticket。

| 渠道 | Ticket 重开逻辑 |
| --- | --- |
| Web chat | 每次对话都会创建一个新 ticket；关闭后的工单不会重开。 |
| Email | 每个邮件往来生成一个 ticket；回复已关闭的邮件会重新激活该工单。 |
| SMS | 每个人对应 1 个 ticket；该用户后续的消息会重开现有的工单。 |
| Instagram | 私信或回复快拍会创建新 ticket；后续消息会加入该工单除非其已关闭。 |
| WhatsApp | 每个人对应 1 个 ticket；后续消息会重开现有工单。 |

当客户发起 ticket 时，你可以通过 Web chat 或 Email 回复任何客户。然而，对于 SMS tickets，客户必须是 SMS marketing subscriber（短信营销订阅者），你才能进行回复。你可以使用 SMS auto-responder（短信自动回复）来告知非订阅者，他们需要先完成 Opt-in（加入订阅）才能收到回复。

在回复时，你无法执行以下操作：

- 主动发起对话： 你不能主动与客户开启 ticket；必须由客户先向你发送消息。
- 使用 Branded Sender ID： 无法在 Helpdesk 中使用带有品牌名称的发送者 ID（也称为 Alphanumeric Sender ID），因为这类号码无法接收 Inbound（入站）短信。
- 回复未授权的 Profile： 无法向未表示同意（Non-consented）的 profile 发送回复。

##### Helpdesk 操作导航

在 Klaviyo 中通过 Service > Helpdesk 访问 Inbox。

你可以通过 主要视图查看工单：

1. My Inbox： 分配给你的开启中的工单。

2. All tickets： Inbox 中的所有工单（无论状态如何），支持筛选和批量操作。

3. Unassigned： 尚未分配的新工单。

4. Spam： 系统自动扫描并拦截的垃圾消息。

![An interface screenshot of Klaviyo Helpdesk showing the 'Inbox' section with options for 'My Inbox', 'All tickets', and 'Unassigned', along with ticket counts.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-64.png?resize=450%2C148&ssl=1)

##### Ticket 状态

在任何视图中，你都可以根据 ticket 状态进行筛选。一个 ticket 共有 3 种状态：

- Open： 对话处于活跃状态或正等待处理。
- Snoozed： 暂时隐藏；你可以选择何时再次收到提醒。
- Closed： 对话已完成，并从 My Inbox 和 Unassigned 视图中归档。

##### 处理 Tickets

在查看 ticket 时，你可以执行以下操作：

1.查看历史消息： 最多可查看与该客户最近的 50 条消息记录。

2.使用 Overview面板： 查看有关 ticket 和 profile 的详细信息，包含以下板块：

###### Ticket 信息

- ID number： 工单编号
- Assignee： 负责人
- 创建日期和时间
- Channel： 来源渠道（Email, SMS, 或 Web chat）
- Tags： 标签

###### Predictive Analytics（预测分析）

(如果你的 Klaviyo 账户满足资格标准，该项才可用)

- Customer lifetime value： 客户终身价值 (CLV)
- Number of orders： 订单总数
- Churn risk： 流失风险
- Predicted next order date： 预测的下一次下单日期与该 profile 关联的 ticket 数量

###### Activity（活动记录）

- 最近订单（仅限 Shopify）： 点击 # of orders 可查看该访客最近的购买列表。

- 订单操作： 客服可以直接在订单视图中修改或取消客户的订单数量，这些更改会同步保存到 Shopify。

- 操作方法：点击 3 dots（三个点图标）并选择 Edit 或 Cancel。如果客服修改或取消了订单，客户会收到来自 Shopify 的新邮件（更新后的付款账单邮件或订单取消确认邮件）。
- Profile 触发的事件： 点击右侧的 # of events 按钮可查看最近的事件列表。你可以根据需要查看的Metric筛选这些活动，并可以保存筛选后的视图。

![A customer support conversation in Klaviyo Helpdesk, featuring messages about pet-friendly products, customer queries, and predictive analytics details.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-65.png?resize=733%2C678&ssl=1)

##### ****Helpdesk 设置与自定义****

你可以通过导航至 Helpdesk > Settings 来配置 Inbox 的运行模式。在这里，你可以找到适用于全局的通用选项，以及针对你所使用的每个支持渠道的特定设置。

![Klaviyo Helpdesk界面，显示Inbox菜单，包括My Inbox、All tickets、Unassigned和Reports选项，以及SMS和Web chat视图统计信息。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-66.png?resize=338%2C426&ssl=1)

##### ****渠道特定设置 (Channel-specific settings)****

根据你为 ****Inbox**** 配置的支持渠道，你可以通过设置菜单栏中对应的渠道选项卡（Tabs）来进行详细配置。

![显示了 Klaviyo Helpdesk 设置界面，包含通用设置、团队管理、入站消息和快捷回复的选项卡，以及为电子邮件、短信和网络聊天的特定配置选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-67.png?resize=617%2C98&ssl=1)

##### Email 设置

Email support and forwarding： 将收到的客户邮件转换为 Helpdesk tickets。从你的支持邮箱设置邮件转发，将消息直接路由至 Helpdesk。

##### SMS ticket 设置

1.短信自动回复： 当有人发送不包含关键字的消息时发送自动回复。将自动回复设置为仅发送给“未授权（non-consented）”的 profiles，并将消息更新为类似内容：“{{Organization prefix}}: 我们无法回复，因为你尚未同意接收短信。如需帮助，请通过 {{email}} 联系我们。”

2.新消息邮件通知： 当你在 Inbox 中收到新的 SMS 消息时，接收邮件提醒。 如果你计划使用 Helpdesk 进行客户支持，请开启此设置。

3.Link shortening（链接缩短）： 自动缩短外发 SMS 消息中的任何链接，以节省字符数，并允许在 Klaviyo 内进行归因。此设置默认开启，应保持启用状态。

##### Web chat ticket 设置

- 支持邮箱地址： 如果在你的最后一次回复后超过 3 分钟，客户在 Web chat 会话中掉线，系统将发送一封跟进邮件。 使用包含你域名的邮箱地址（如 support@yourbusiness.com），以降低被标记为垃圾邮件的风险。
- 办公时间与网页聊天自动回复： 定义团队处理 Web chat 的可用时间，并根据可用性向客户发送自动消息。设置清晰的服务时间以管理客户预期，并在团队离线时使用自动回复告知客户。

##### Helpdesk 核心功能

- 编辑订单或订阅： 客服可以直接在 ticket 中编辑或取消 Shopify 订单。他们还可以跳过、取消或编辑 Recharge 订阅。
- Segment与标签： 根据客户所属的 Segment 或 ticket 的 Tag，将工单分配给正确的团队。
- AI 自动标记： Helpdesk 会自动为入站 tickets 打上常见的电商标签，如“退货”、“产品相关”等。
- 工单自动关闭： 在客户一段时间无活动后，自动关闭 ticket。
- 轮询分配： 在可用的（“在线”）团队成员中均匀分配新工单。
- 快捷回复： 预先编写的可重复使用的回复，帮助客服更快地处理。
- 内部备注： ticket 内的私密评论，仅对你的团队可见，客户不可见。

##### Reporting

Klaviyo Helpdesk 中的报表仪表板汇总了你的支持活动和表现。使用它来追踪：

- Ticket volume（工单量）
- First response time（首次回复时间）
- Resolution time（解决时间）
- Agent or tag performance（客服或标签表现）

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)