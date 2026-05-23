---
id: "4416791883163"
title: "如何识别iOS15邮件隐私保护开启"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4416791883163-How-to-identify-iOS15-Mail-Privacy-Protection-opens"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:55:00Z"
language: "zh"
---
## 你将会学到

了解如何识别 Klaviyo 分段中的 Apple 邮件隐私保护 (MPP) 打开，包括如何构建不会因这些自动打开而膨胀的分段。前往 Klaviyo 的博客[了解有关 iOS15 和 MPP 的更多信息](https://www.klaviyo.com/blog/apple-ios15-klaviyo)。

通过使用 Apple Privacy Open 标志（对于每个开放事件设置为 True 或 False），您可以区分 MPP 开放与真正的收件人参与。

Apple Privacy Open 标志适用于 2021 年 11 月 20 日或之后发生的 Opened Email 事件。在此版本之前的 Opens 可能不会在其元数据中包含此信息。

## 识别 MPP 打开

打开事件包含一个名为 Apple Privacy Open 的属性，对于所有打开事件，该属性为 **True** 或 **False**。如果 Apple Privacy Open 为 **True**，则意味着消息是在打开 MPP 的设备上打开的。因此，打开事件可能归因于 Apple 的 MPP，并不一定反映真正的电子邮件打开。在这些情况下，邮件可能已被收件箱或收件人打开，并且无法区分两者。

如果 Apple Privacy Open 为 **False**，则打开事件可归因于收件人在未启用 Apple MPP 功能的设备上打开并查看您的消息。

要将 Apple Privacy Open 条件添加到分段，请使用以下条件：

- ****某人做了什么 > 打开电子邮件****
  - 单击****添加过滤器****并添加规则****其中Apple Privacy Open等于True/False****（取决于您的使用案例）

![打开的APO是假的.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716354559003)

下面的示例片段提供了如何在您自己的帐户中使用此资源的示例。

### 从您参与的细分市场中删除 MPP 开启者

如果您的参与分段遵循我们的文章[如何创建参与分段](https://help.klaviyo.com/hc/en-us/articles/115000200072-How-to-Create-an-Engged-Segment)中的建议，您可以通过将过滤器 ****where Apple Privacy Open equals False**** 添加到“打开的电子邮件”条件来排除 MPP 打开。以下细分包括过去 30 天内打开或点击电子邮件（不包括 MPP 打开）或过去 15 天内订阅的所有订阅者。

![参与不是 APO.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716354562459)

### 找到所有 MPP 开启器

如果您想查看受 MPP 影响的配置文件总数，请使用下面的部分。此部分将包括自 Klaviyo 开始跟踪 Apple 隐私开放以来在其 Apple Mail 帐户中启用 MPP 功能的任何人。

![打开的APO是假的.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716354559003)

### 识别未参与的 MPP 开启器

使用下面的部分来识别最近未直接与您的消息互动（通过在没有 MPP 的设备上打开电子邮件，或在任何设备上单击电子邮件）的 Apple Privacy 打开的个人资料。考虑从您的营销活动发送中排除此分段。

![未参与的 APO 开启器.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716331545499)

## 关于 MPP 打开

随着 iOS15、Monterey、WatchOS8 和 iPadOS8 的发布，Apple Mail 用户可以选择开启 MPP。当您的收件人之一打开此功能时，无论收件人是否打开电子邮件，他们收到的邮件中的所有图像都将被抢先加载。

由于在加载跟踪像素（一个几乎不可见的小图像）时会跟踪打开情况，因此这会导致在 Klaviyo 中跟踪错误的打开事件。反过来，这会人为地提高您的打开率，并使识别真正参与的订户变得更加困难。

Klaviyo 识别这些 Apple 隐私开放，以便您可以将它们排除在细分的参与标准之外，并查看哪些收件人真正与您的消息互动。

如果订阅者为同一电子邮件地址设置了多个收件箱（例如 Gmail 收件箱和 Apple Mail 收件箱），您可能会看到同一邮件的 Apple Privacy 打开和 true open 事件（即 Apple Privacy Open 设置为 **False** 的打开电子邮件事件）。