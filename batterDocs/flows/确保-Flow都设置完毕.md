---
id: 6154
title: "确保 Flow都设置完毕"
slug: "flowstartsending"
category: "自动化与生命周期（Flows）"
category_slug: "flows"
wp_url: "https://dynamicycle.com/docs/flowstartsending/"
wp_modified: "2026-01-05T10:06:25"
---

##### 检查您的 Flow trigger

要检查您的 Flow trigger：

1. 点击 Flow 构建器顶部的 Flow trigger。
2. 在左侧侧边栏中查看 Flow Trigger 部分。

![图示展示了 flow trigger 设置，左侧为 'Checkout Started' 指标，右侧为触发器说明 '当有人开始结账'。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-28.png?resize=700%2C165&ssl=1)

##### List 与 Segment 触发的 Flow

您的账户中可能会有名称相似的 list 或 segment。为了确保您选择了正确的 trigger，请在左侧侧边栏的 Flow Trigger 部分，点击该 list 或 segment 的名称以进行查看。

##### Metric 触发的 Flow

在左侧侧边栏的 ****Flow Trigger**** 部分，确保您为电子商务集成选择了合适的 metric。在 metric 名称旁边会有一个与之对应的电子商务集成图标。点击该 metric 的名称，即可在账户的 ****Metrics**** 标签页中查看它。

##### Date property 触发的 Flow

在左侧侧边栏的 ****Flow Trigger**** 部分，确保您为电商集成选择了合适的日期属性（date property）。

1. 点击 ****Date Property**** 查看配置。
2. 检查 flow 是否设置为在您预期的时刻开始。
3. 确保配置了合适的时间和时区。
4. 确保根据您的意图设置了 flow 是否重复。
5. 如果您做了任何更改，请点击底部的 ****Save****。

##### 必要时更改 Trigger

如果您需要更改 flow 的 trigger，必须克隆该 flow：

1.导航至 [Flows](https://www.klaviyo.com/flows) 标签页，找到您想要更改 ****trigger**** 的那个 flow。

2.在右侧，点击 Edit Flow 旁的箭头以展开下拉菜单，然后选择 Clone。

![Screenshot of a flow management interface showing different flows with options to clone, edit, archive, or delete. The active flows include 'DC| Search Abandoned' and 'DC| Checkout Abandoned'.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-29.png?resize=1024%2C487&ssl=1)

3.点击 Clone 后，更新名称，并根据需要更改 flow trigger。

![用于克隆 flow 的弹窗界面，显示输入框以输入克隆名称和下拉菜单选择触发器。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-30.png?resize=926%2C954&ssl=1)

##### 检查时间延迟（Time Delays）

针对您的时间延迟，请检查以下各项：

- ****trigger**** 与第一条消息之间存在延迟（除非第一条消息本意就是立即发送）。
- 各条消息之间存在延迟，以便让客户有时间接收并阅读每一封邮件。
- 根据您的业务策略和首选发送频率，设置合适的时间延迟长度。
- 如果有任何时间延迟设置为“延迟到一天中的特定时间”，请确保配置了正确的时区或设置为“接收者的当地时区（Recipient’s Local Timezone）”。
- 如果有任何时间延迟设置为“延迟到一周中的特定日期”，请确保已进行相应配置。

##### 检查Trigger splits 和 Conditional splits

针对您的分流设置，请检查以下各项：

- 所有 split（分流）均已配置具体的条件。
- 如果一个 split 包含多个条件，各条件之间不存在矛盾。
- ****YES**** 和 ****NO**** 路径分别导向您预期的消息和动作。
- 在必要的地方，分流出的路径已重新合并（rejoin）到主路径。

##### 检查邮件标题和发件人信息

针对您的邮件标题和发件人信息，请检查以下各项：

- 每条消息都有与其内容相匹配的合适subject line。
- 主题行拼写和语法准确无误。
- 预览文本（Preview text）拼写和语法准确无误。
- 消息使用了符合您品牌形象的发件人名称。
- 消息使用了符合您品牌形象的发件人邮箱地址。
- 发件人邮箱使用您业务的自有域名，而非个人邮箱地址。
- 如有必要，请勾选“将其作为您的回复地址（reply-to address）”选项。
- 如有必要，添加抄送（CC）或密送（BCC）地址。

##### 检查 SMS 合规性选项

如果您在 flow 中使用了 SMS（短信），请按照以下步骤检查您的合规性选项：

1. 点击 flow 构建器中的 SMS 动作。
2. 在左侧侧边栏中点击 ****Edit****。
3. 在 SMS 编辑器中，点击 ****Compliance****。
4. 确保针对您发送短信的目标国家/地区，已选择了所有合适的合规选项。

##### 检查消息内容

针对您的消息内容，请检查以下各项：

- ****品牌一致性：**** 消息具有符合品牌的视觉形象。
- ****文本质量：**** 正文拼写和语法准确无误。
- ****个性化设置：**** 使用变量对内容进行个性化处理，以提高收件箱送达率。
- ****链接有效性：**** 确保所有链接都能正常工作并导向正确的目的地。
- ****链接频率：**** 链接的使用数量保持在适当范围。
- ****图片优化：**** 图片已进行优化以减小消息体积（提高加载速度）。
- ****图文比例：**** 保持平衡的图文比例，防止被识别为垃圾邮件。
- ****内容合规：**** 事务性消息（Transactional messages）中不包含营销内容。
- ****短信设置：**** 带有链接的 SMS 消息已开启链接缩短功能，这是转化跟踪所必需的。

##### 检查消息设置

要检查消息设置：

1.在 flow 构建器中点击一条消息。

2.在右侧侧边栏中，往下划。

![Klaviyo flow builder interface displaying email details and settings for a referral reminder flow.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-31.png?resize=1024%2C569&ssl=1)

###### Smart Sending（智能发送）

如果您希望跳过那些最近刚收到过您邮件或短信的接收者，请开启此项。对于事务性邮件（transactional emails），****请勿****开启此设置。

###### UTM parameters（UTM 参数）

如果您希望在 Google Analytics 等第三方报告工具中追踪链接来源，请开启此项。

###### Additional filters（额外过滤器）

如果您希望进一步限制谁能接收特定的一条消息，请开启此项。在大多数情况下，使用 conditional split（条件分流）或 trigger split（trigger 分流）来限制消息接收者效果更好。

##### 更改 Flow 状态以开始发送

在确认 flow 的所有组件均已按您的预期配置后，更改 flow 中消息的状态以开始发送。

- 当您首次创建 flow 时，点击右上角的 ****Review and Turn On**** 按钮，可以一次性更新 flow 中每个已配置动作的状态。
- 请注意，即使您批量更新了 flow 的状态，未配置的动作（unconfigured actions）仍将保持为草稿（draft）状态。

![用户界面展示了一个流构建器，其中的触发器设置为在启动结账时触发，并显示一个等待4小时的步骤。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-32.png?resize=604%2C329&ssl=1)

- 当确认弹窗出现时，如果您希望 flow 立即开始发送消息，请在 Action status 下拉菜单中选择 Live（实时）；如果您希望在发送前手动审批消息，请选择 Manual（手动）。

![确认并启动流的设置窗口，显示操作状态选项，包括实时和手动审批选择。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-33.png?resize=512%2C233&ssl=1)

- 点击 ****Turn On**** 进行确认。
- 如果您在将 flow 设置为 Live 或 Manual 状态后，需要再次更改 flow 动作的状态，请点击右上角的 ****Update Action Statuses****。

![Klaviyo flow builder interface showing an active referral reminder flow with actions for email, text message, and WhatsApp, along with a conditional split in the logic.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-34.png?resize=1024%2C568&ssl=1)

##### 如何修改上线的 Flow

在将 flow 设置为 Live（实时）后，您可能仍想对其进行修改。 联系人是按顺序调度到 flow 的每一个步骤的，他们必须先完成当前步骤，才能被调度进入下一步。这意味着对于正在流程中的用户，您对他们****尚未到达****的后续步骤所做的任何更改，都会影响他们的后续旅程。

请查看以下不同更改带来的影响：

- ****重新排序或添加步骤**** 如果某人已经预约（处于 Waiting 状态）了某个特定步骤，即使您在序列中移动了该步骤的位置，他们仍将按原计划执行该步骤。此外，假设他们正在等待第一封邮件，而您调整了 flow 在这封邮件之前添加了新步骤，除非您执行 back-populate（回填），否则他们不会收到这些新增的步骤。
- ****修改时间延迟（Time Delays）**** 如果某人已经根据之前的延迟设置预约了某个步骤，更改该时间延迟不会重新调度他们。但该步骤****之后****的任何时间延迟更改将会对他们生效。
- ****更新消息内容**** 如果您在用户收到某条消息之前更改了其内容，他们将收到更新后的版本。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)