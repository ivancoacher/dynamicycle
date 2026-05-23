---
id: 4937
title: "Flow实操"
slug: "flow"
category: "自动化与生命周期（Flows）"
category_slug: "flows"
wp_url: "https://dynamicycle.com/docs/flow/"
wp_modified: "2025-12-22T06:37:05"
---

##### 如何在 Klaviyo 中使用Flow

Klaviyo 的 ****Flow****（自动化流程）是通过设定触发条件和用户筛选条件，实现个性化、自动化的邮件和短信沟通。当用户执行某个特定行为时（如加入列表、完成购买、遗弃购物车等），流程会自动触发。

以下是如何在 Klaviyo 中使用 ****Flow****，以及如何快速创建和优化它们的指南。

##### ****开始创建你的 Flow****

![Klaviyo Flows 页面，显示多个自动化流程的列表，包括每个流程的名称、类型、状态和更新日期等信息。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-28.png?resize=1024%2C525&ssl=1)

1.****进入 Flows 标签页****

登录到 Klaviyo 后，点击顶部导航栏的 ****Flows**** 标签页。

2.****选择创建新 Flow****

点击 ****Create Flow**** 按钮，选择从头开始创建或从模板库选择现成的 Flow。

##### ****选择 Flow 模板****

![Klaviyo Flow创建界面，展示多种邮件自动化模板选项，包括欢迎系列、购物车提醒和客户感谢邮件。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-30.png?resize=1024%2C630&ssl=1)

1.****浏览 Flow Library****

如果你不确定如何开始，可以浏览 ****Flow Library****，选择适合你需求的 Flow 模板。每个模板根据不同的营销目标、电商平台和消息渠道（邮件、短信等）提供不同的选项。

2.****从模板创建****

在 Flow Library 中，选择你需要的 Flow 类型（如欢迎系列、遗弃购物车等），并点击创建。

##### ****设置触发条件和用户筛选条件****

![Grapical interface showing various trigger options for Klaviyo flows, including 'Checkout started', 'Added to list', 'Viewed product', 'Best cross-sell date', and 'Placed order'. Each option includes descriptions of actions to take for each trigger.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-31.png?resize=581%2C1024&ssl=1)

1.****触发条件****

选择适当的触发条件来启动 Flow。常见的触发条件有：

- ****List****：当用户加入特定列表时触发（如欢迎邮件）。
- ****Segment****：当用户加入特定分群时触发。
- ****Metric****：基于用户执行的特定操作（如购买、点击）触发。
- ****Date Property****：基于用户的日期属性（如生日）触发。
- ****Price Drop****：当商品价格下降时触发。

2.****用户筛选条件****

在每个 Flow 中，你可以设置用户筛选条件，确保只有满足特定条件的用户才能继续执行后续操作。例如，“在过去 30 天内未购买”或“购物车中有商品但未结账”。

##### ****添加步骤到 Flow 中****

![A user interface displaying various actions, timing, and logic components for creating automation flows in Klaviyo, including options like Email, Text message, WhatsApp, and Time delay.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-32.png?resize=397%2C1024&ssl=1)

##### ****选择 Flow 组件****

Flow 组件包括 Action、Timing 和 Logic，你可以通过拖放来创建邮件、短信、延迟时间等。

- ****Action组件****

操作组件用于发送邮件、短信、更新用户资料等。

- ****Timing组件****

设置时间延迟，安排消息发送的时间。例如，你可以在欢迎邮件之间设置 24 小时的延迟，确保用户有足够的时间阅读邮件。

- ****Logic组件****

使用Conditional split或Trigger split来根据不同用户行为进行路径选择。

##### ****设置时间延迟****

![Klaviyo 流程示例，包含触发条件、时间延迟和邮件步骤，展示新客户感谢邮件的设置布局。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-10.png?resize=317%2C837&ssl=1)

1.****延迟设置****

你可以设置每个操作之间的时间延迟。例如，在Welcome Series中，第一封邮件发送后，可以设置 2 天延迟，第二封邮件才发送。

2.****延迟时间****

延迟时间可以是分钟、小时或天。如果你希望在特定时间点发送邮件，还可以设置为某天的特定时间。

##### ****发布 Flow 并设置状态****

![Klaviyo Flow状态设置界面，显示草稿( Draft )、手动( Manual )和上线( Live )状态选项，标注推荐的状态为 Live。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-33.png?resize=700%2C198&ssl=1)

##### ****Flow 状态****

Flow 或 Flow 中的操作可以有以下状态：

- ****草稿 (Draft)****：编辑中，未激活。

- ****手动 (Manual)****：需要人工审核和发送。

- ****上线 (Live)****：已激活，自动发送。

###### ****更改操作状态****

你可以随时通过点击每个操作的状态按钮，更新其状态为 ****手动**** 或 ****上线****。

###### ****批量更新****

通过点击 Flow 构建器右上角的 ****Review and Turn On**** 或 ****Update Status****，你可以批量更新所有操作的状态。

##### ****查看 Flow 数据和表现****

![一个Klaviyo的自动化流程界面，展示了条件分流，以及新客户和重复客户感谢邮件的发送状态和统计数据，包括打开率和点击率。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-14.png?resize=1024%2C986&ssl=1)

1.****Flow 分析****

你可以在 Flow 中查看每个操作的表现，包括邮件的打开率、点击率等关键指标。点击 Flow 中的 ****显示分析****，查看详细数据。

2.****查看收件人活动****

在 Flow 中，你可以查看哪些用户已经完成了步骤，哪些用户处于等待中，哪些用户被跳过。

![Klaviyo 欢迎系列邮件的收件人活动界面，显示需要审核的收件人、已打开的邮件、退信和点击记录等信息。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-15.png?resize=1024%2C576&ssl=1)

##### ****优先上线的 Flow****

- ****Welcome Series（欢迎系列）****

向新订阅者介绍品牌，并通过一系列邮件将他们转化为首次购买客户。

- ****Abandoned Cart（遗弃购物车）****

自动发送邮件或短信，将遗弃购物车的客户拉回来，增加转化。

- ****Post-Purchase（购买后）****

感谢客户购买，并推荐相关商品。

- ****Winback（重获活跃）****

激活那些曾经购买过的老客户，带回他们进行二次购买。

##### ****小贴士****

- ****清晰命名****：给每个 Flow 起一个清晰易懂的名称，方便团队管理。
- ****逐步优化****：开始时选择效果显著的 Flow，并逐步优化它们的设置。
- ****测试和迭代****：可以通过测试不同的消息和时机，逐步优化 Flow 的效果。

通过这些步骤，你可以在 Klaviyo 中高效创建、优化并管理自动化流程，提升客户体验并促进业务增长。

---

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)