---
id: "115002779471"
title: "排除流程故障"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002779471-Troubleshooting-a-flow"
section: "Troubleshooting flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:15Z"
language: "zh"
---
了解当您发现流的行为与预期不同时如何对流进行故障排除。流程是高度可定制的，并且复杂程度可能有所不同。故障排除资源的设计范围广泛，涵盖适用于大多数 Klaviyo 帐户的常见问题。 ## 了解流量警报

根据问题的不同，您可能会在**流**选项卡中的流旁边或流构建器中的特定流组件上看到红色或黄色警告图标。如果您没有看到任何警报图标，请跳至下一部分。对于 **Flows** 选项卡上的警报，请将鼠标悬停在图标上以查看问题的描述。 ![](https://klaviyo.zendesk.com/hc/article_attachments/29108306914331)

对于流程构建器中的警报，请单击标题栏右侧的****警报****图标按钮，以查看流程组件的问题列表。 ![](https://klaviyo.zendesk.com/hc/article_attachments/46630156351771)

有关更多信息，请参阅我们关于[了解流量警报]的文章(https://klaviyo.zendesk.com/hc/en-us/articles/29091293276187)。 ## 您的经验水平是多少？如果以下部分与您的问题相关，请单击以下部分：

### 对于新帐户

对于新帐户，在开始故障排除之前，请确保
您已完整阅读我们的指南
[流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)
了解流程的基本组成部分以及如何设置您的流程
第一流直播。避免常见流程类型（例如欢迎系列和
废弃的购物车，我们建议使用以下方法创建您的第一个流程
我们的预构建模板
[流库](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-started-with-flows#choose-a-pre-built-flow-from-the-library3)
并编辑预先构建的内容以匹配您的品牌。 ### 对于以前的工作流程

#### 查看流程的变更日志

如果您的流程之前运行正常，但您最近注意到
行为发生变化，您应该首先查看流程的变更日志
查看所做更改的历史记录。这对于
具有多个用户的旧流程和帐户。如果你注意到这一点
流的行为在特定日期和时间后发生了变化，
变更日志将能够告诉您以下信息：

- 发生了什么变化
- 谁做出了改变
- 更改发生的时间（您帐户所在时区的日期和时间）

如果更改与您开始遇到问题的时间一致
您的流程，更改很可能是问题的根源。 ![](https://fast.wistia.com/embed/medias/qksjoa5aq4/swatch)

请按照以下步骤查看流的历史记录：

1. 在标题栏中，单击****查看流历史记录****
   图标按钮。 ![在标题栏中查看流量历史记录选项。](https://klaviyo.zendesk.com/hc/article_attachments/46630172148763)
2. 选择****查看流量历史记录****将打开
   **流历史记录**面板位于屏幕右侧。 ![流程历史记录面板，也称为变更日志。](https://klaviyo.zendesk.com/hc/article_attachments/46630172153243)

在我们的文章中了解有关 **流程历史记录** 面板的更多信息
上
[如何查看流程的历史记录](https://help.klaviyo.com/hc/en-us/articles/4402385748635)。 ## 资源故障排除

### 流触发器

如果用于触发流的指标的活动突然下降，您将收到如下所示的警报，并且您必须解决问题以确保流正确触发。 ![流列表视图中的流名称，下方显示有关活动下降的警告。](https://klaviyo.zendesk.com/hc/article_attachments/28720621452699)

对于 **查看的产品**、**添加到购物车**、**开始结帐** 和 **下订单** 跟踪，请参阅以下文章了解故障排除步骤：

- [已查看商品跟踪问题排查](https://help.klaviyo.com/hc/en-us/articles/4416172774939-Troubleshooting-viewed-product-tracking)
- [添加到购物车跟踪的问题排查](https://help.klaviyo.com/hc/en-us/articles/6985692431259-Troubleshooting-added-to-cart-tracking)
- [开始结帐跟踪问题排查](https://help.klaviyo.com/hc/en-us/articles/6998274713371-Troubleshooting-started-checkout-tracking)
- [已下订单跟踪问题排查](https://help.klaviyo.com/hc/en-us/articles/7000906101019-Troubleshooting-placed-order-tracking)

对于所有其他指标，[了解 Klaviyo 如何监控流的指标活动](https://help.klaviyo.com/hc/en-us/articles/13913401149595-Understanding-how-Klaviyo-monitors-metric-activity-for-flows)。 ### 预定和跳过的消息

如果您在流程中发现大量跳过的配置文件，请了解[对流程消息跳过配置文件的原因进行故障排除](https://help.klaviyo.com/hc/en-us/articles/1260805003210-Troubleshooting-why-a-flow-message-skipped-a-profile)。如果您看到在一个流中多次安排配置文件，请了解[排查为什么配置文件在流中多次排队](https://help.klaviyo.com/hc/en-us/articles/115002779491-Troubleshooting-why-a-profile-is-queued-in-a-flow-multiple-times)。如果您不确定个人资料如何或为何在流程中移动，请了解[联系人如何在流程中移动](https://help.klaviyo.com/hc/en-us/articles/360017706091-Understanding-how-contacts-move-through-a-flow)。 ### 送达率

如果您收到有关流性能突然下降的通知，请参阅[Klaviyo 如何监控流的指标活动](https://help.klaviyo.com/hc/en-us/articles/13913401149595-Understanding-how-Klaviyo-monitors-metric-activity-for-flows)。如果您遇到流邮件成为垃圾邮件的问题，请了解[电子邮件成为垃圾邮件的原因排查](https://help.klaviyo.com/hc/en-us/articles/12034571748251-Troubleshooting-why-emails-go-to-spam)。 ### 对特定流类型进行故障排除

如果您遇到特定类型流的问题，请参阅下面的文章了解进一步的故障排除步骤。 - [列表或段触发流故障排除](https://help.klaviyo.com/hc/en-us/articles/12414318812827-Troubleshooting-a-list-or-segment-triggered-flow)
- [对指标触发流进行故障排除](https://help.klaviyo.com/hc/en-us/articles/12278373016603-Troubleshooting-a-metric-triggered-flow)

如果您不确定遇到问题的是哪种类型的流程，您可以根据流程的触发器来判断。 1. 在流程构建器中单击流程的触发器。 2. 查看右侧边栏的顶部部分，查看该流是否由列表、细分或指标触发。 3. 确定您正在查看的流类型：
   - 当某人被添加到特定列表或分段时，会触发列表或分段触发的流。常见的例子包括欢迎系列和 VIP 部分流程。 - 指标触发的流由电子商务平台等集成中的指标触发。常见的例子包括废弃的购物车和购买后流程。 ## 帮助我们改进这篇文章

如果您认为上面列出的故障排除方案中缺少有用的信息，请向我们提供反馈，以便我们改进帮助中心体验并为您和其他客户提供更好的支持。如果您对本文中提供的故障排除步骤不满意，请从文章底部的提示中选择****否****。下面的表格将要求您提供更多信息来改进本文。 ![反馈模式询问文章是否有帮助。](https://klaviyo.zendesk.com/hc/article_attachments/28720666788379)

提供反馈时，请包括以下内容：

1. 您正在排除什么类型的流程（欢迎流程、废弃购物车等）
2. 您在本文中找不到相关信息的流程问题的详细信息

## 联系 Klaviyo 支持

如果您在查阅本文并查看流程历史记录后仍然遇到问题，请通过我们的[社区](https://community.klaviyo.com/got-a-question-1)或我们的[支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)联系。