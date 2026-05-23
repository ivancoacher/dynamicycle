---
id: 5876
title: "如何创建Never Engaged Segment"
slug: "neverengagedsegment"
category: "投递与合规（Deliverability &amp; Compliance）"
category_slug: "deliverability-compliance"
wp_url: "https://dynamicycle.com/docs/neverengagedsegment/"
wp_modified: "2025-12-26T06:54:04"
---

##### ****您将学到****

学习如何识别参与度最低的邮件订阅者，以便避免向他们发送内容，从而改善并维护您的Deliverability。一旦识别出这些人，可以考虑将他们排除在营销计划之外、发送最后一次重新参与尝试，或在清理list时将其Suppress。在本文中，您将学习如何创建此 Segment。

请注意，定期向不参与邮件互动的 Profile 发送邮件，会导致服务商（如 Gmail、Yahoo、Outlook）开始将您的邮件放入垃圾邮件箱。

从未互动的 Profile 最有可能随着时间的推移损害您的发件人信誉。停止向他们发送邮件是解决所有送达率问题最有效的方法，这些问题包括：

- 邮件掉入垃圾邮件文件夹
- 低打开率
- 低点击率
- 低转化率
- 高垃圾邮件举报率
- 高退信率（Bounce rate）
- 高取消订阅率

##### ****创建 Never Engaged Segment****

###### 一键创建 Never Engaged Segment

如果您尚未创建此 Segment，也可以通过 Klaviyo 的 [Deliverability Hub](https://www.klaviyo.com/analytics/deliverability/email/score) 快速创建一个。

要访问该页面，请导航至 Klaviyo 中 Analytics 下的 Deliverability 选项卡。在操作中心针对“Create a Never engaged segment”建议选择 Create segment。

![A screenshot of Klaviyo's Deliverability Hub, highlighting the Action Center where users can create a 'Never engaged' segment to improve email deliverability.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-157.png?resize=1024%2C570&ssl=1)

在 Deliverability Hub 创建该 Segment 后，您可以在 Klaviyo 的 Lists & Segments 页面看到它。

###### 手动创建 Never Engaged Segment

请按照以下步骤在您的 Klaviyo 账户中手动创建一个 Never Engaged Segment。

- 导航至账户中的 [Audience](https://www.klaviyo.com/lists) > [Lists & Segments](https://www.klaviyo.com/lists)。

![Klaviyo平台的Lists & segments页面，展示邮件订阅者的相关信息及创建新Segment的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-158.png?resize=1024%2C572&ssl=1)

- 选择 Create New > Create Segment。

![Klaviyo界面显示创建段落选项的下拉菜单，包含'创建列表'和'创建段落'的选择。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-159.png?resize=474%2C268&ssl=1)

- 您可以将其命名为：Never Engaged。

![创建新细分的界面，显示细分构建器，标记名称为“Never Engaged”。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-160.png?resize=1024%2C537&ssl=1)

添加以下条件，然后选择 Create：

- If someone can or cannot receive marketing > Person can receive email marketing
- AND
- What someone has done (or not done) > Person has Received Email 至少为 5 次，在过去 180 days 内
- AND
- What someone has done (or not done) > Person has Opened Email 0 times，时间范围为 over all time
- AND
- What someone has done (or not done) > Person has Clicked Email 0 times，时间范围为 over all time
- AND
- What someone has done (or not done) > Person has Placed Order 0 times，时间范围为 over all time

![Klaviyo界面中的条件设置，显示如何创建一个从未参与的细分。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-161.png?resize=1024%2C975&ssl=1)

##### 批量Suppress该 Segment 以优化送达率

Suppress操作仅适用于Email渠道。

1. 导航至账户中的 [Audience](https://www.klaviyo.com/lists) > [Lists & Segments](https://www.klaviyo.com/lists)。
2. 点击您想要归档的 Segment 旁的三个点（更多选项）。
3. 点击 Suppress current members。

![Klaviyo账户中的Lists & Segments页面，显示不同邮件列表和Segment选项，包括Dog Lovers Segment，旁边有Suppression选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-162.png?resize=1024%2C591&ssl=1)

随着 iOS15、macOS Monterey、iPadOS 15 和 WatchOS 8 的发布，Apple 的邮件隐私保护（MPP）通过预取我们的tracking pixel，改变了接收邮件打开率数据的方式。鉴于这一变化，务必理解打开率将会因此被虚高。

如果您的 Campaign分析数据显示有大量的 iOS 打开者，我们建议在您的个人订阅者 Segment 中识别这些受影响的打开行为。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)