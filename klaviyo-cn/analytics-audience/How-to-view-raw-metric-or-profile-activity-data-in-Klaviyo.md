---
id: "115005076747"
title: "如何在 Klaviyo 中查看原始指标或配置文件活动数据"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005076747-How-to-view-raw-metric-or-profile-activity-data-in-Klaviyo"
section: "Build and use metrics"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:17Z"
language: "zh"
---
## 你将会学到

了解如何查看 Klaviyo 从集成或 API 调用接收到的原始事件或配置文件活动数据。如果您想要验证配置文件的数据以及给定事件，或者只是查看此数据以更好地了解每个指标捕获的内容，这可能会很有用。 ## 查找原始指标数据

1. 要查看原始指标或事件数据，请转至 ****Analytics**** ****>**** ****Metrics.****
2. 您可以通过在上面的 **搜索指标** 字段中搜索指标或单击下面列表中的指标来查看活动源数据。 3. 进入指标后，导航至****活动源****选项卡。 ![activity_feed_tab.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720891621915)

   请注意，如果单击指标页面顶部的活动源按钮，您将无法在此处看到原始数据输出。档案活动详细信息只能从特定指标内访问。 4. 找到您要查看的配置文件，然后单击右侧的****三点菜单****。 5. 点击********活动详情******。 ![activity_details-new.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720891619483)

然后，您将看到一个模式，其中包含与该指标和特定配置文件相关的所有 JSON 信息。例如，如果您使用 **打开的电子邮件** 指标，您将看到有关所使用的电子邮件域、关联消息、客户端类型、客户端操作系统、客户端操作系统系列、客户端名称、消息名称等的信息。下面的示例使用 **添加到购物车** 并捕获产品名称、产品 ID、URL、图像 URL、价格等信息。 ![activity_details_modal-new.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720891626395)

然后，如果您愿意，您可以复制任何或所有此事件数据的 JSON 版本。 ## 理解时间戳

现在您已经从 **活动详细信息** 检索了数据，了解此信息中包含的两个时间戳背后的含义非常重要。这两个时间通常但并不总是相同。第一个时间戳是指事件第一次被触发的时间。例如，如果流的触发器是 **结帐开始**，则此时间戳会详细说明您的电子商务网站上发生结帐的确切时间。第二个时间戳是事件在 Klaviyo 中出现的时间。通常，这些时间戳是相同的或相隔几秒，如下例所示。 ![活动详细信息时间戳位于顶部，活动和记录时间戳为相同值](https://klaviyo.zendesk.com/hc/article_attachments/28720891616155)

根据您的[集成](https://help.klaviyo.com/hc/en-us/categories/115000032731-Ecommerce-Integrations)，Klaviyo 从其他来源接收此信息所需的时间可能会导致延迟。下面显示了此类预期延迟的示例。 ![顶部的活动详细信息时间戳以及活动和记录的时间戳为不同的值](https://klaviyo.zendesk.com/hc/article_attachments/28720846537371)

在上面的示例中，第一个时间戳是相同的（第一张图像），第二个时间戳（第二张图像）准确说明了 Klaviyo 从集成注册事件的时间。详细了解[特定集成同步的频率](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208)。 #### 为什么两个时间戳都很重要

了解时间戳对于确保您的电子邮件及时且相关至关重要。在规划营销策略时，尤其是在创建流程时，务必考虑事件同步中的任何延迟。对于废弃的购物车流程，如果客户开始结帐然后完成购买，则此事件数据可能需要一个小时（WooCommerce 的情况），Klaviyo 才能注册他们完成了购买。如果您将第一封流程电子邮件设置为在 **结帐开始** 事件后半小时发送，并且我们尚未收到结账已完成的确认信息，则该客户可能会错误地收到废弃的购物车流程电子邮件。一般来说，如果您的集成存在同步延迟，我们建议您将流程电子邮件设置为在触发事件后一小时（或更晚）发送，以避免出现意外后果。这是最佳实践，但欢迎系列除外，该系列通常在有人订阅后立即发送，并且不会受到时间延迟的负面影响。 ## 其他资源

- [集成同步参考频率](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208)
- [指标入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005076787)