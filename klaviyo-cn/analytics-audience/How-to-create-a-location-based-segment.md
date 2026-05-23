---
id: "115005065887"
title: "如何创建基于位置的细分"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005065887-How-to-create-a-location-based-segment"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:16Z"
language: "zh"
---
## 你将会学到

了解如何使用基于位置的细分按区域发送营销活动、将表单定位到特定区域的客户，或更好地了解一部分客户。请注意，Klaviyo 在同步该联系人的帐单地址时确定配置文件的位置，或者如果他们尚未购买，则通过跟踪其 IP 地理位置来确定配置文件的位置。详细了解[如何在 Klaviyo 配置文件上设置位置](https://klaviyo.zendesk.com/hc/en-us/articles/115005073907)。 ## 创建基于位置的分段

创建基于位置的分段时，请使用“关于某人的属性”条件。然后，在国家/地区、州/地区、邮政编码或时区之间进行选择以进一步定义该分段。当您选择****邮政编码****时，分段构建器默认使用运算符“包括任何”，它支持选择****多个邮政编码****。您最多可以从下拉列表中选择 500 个邮政编码，并且可以单击“****添加邮政编码****”一次批量添加最多 ****500**** 个邮政编码。 ![](https://klaviyo.zendesk.com/hc/article_attachments/47099137466779)

![](https://klaviyo.zendesk.com/hc/article_attachments/47099137469211)

![](https://klaviyo.zendesk.com/hc/article_attachments/47099146168987)
另一个例子是，如果您想创建一封针对气候寒冷的北美地区的电子邮件，您可以使用以下分段定义：

****关于某人的属性 > 国家 > 等于 > 加拿大****

****或****

****关于某人的属性>州/地区>等于>马萨诸塞州****

****或****

****关于某人的属性 > 州/地区 > 等于 > ...****

![加拿大和新英格兰的一段资料](https://klaviyo.zendesk.com/hc/article_attachments/28720667010587)

请注意，通过在这些条件之间使用 OR 连接器，您的细分将更具包容性 - 因此，某人可以来自加拿大但不是来自马萨诸塞州（反之亦然），但仍然可以进入此细分。如果您想让细分更具排他性，请添加由 AND 连接器分隔的条件。这样做的意思是，所有条件都必须成立才能将某人包括在内。有关更多信息，请参阅我们的[AND 与 OR 指南](https://klaviyo.zendesk.com/hc/en-us/articles/360036534631)。 ## 创建受 GDPR 和英国 GDPR 影响的配置文件片段

位于欧盟或英国的人们受到某些数据保护法（分别是 GDPR 和 GDPR UK）的影响。要在这些位置创建配置文件段，请使用以下定义：

****如果某人位于或不在欧盟 (GDPR) 内 > 位于欧盟内****

****或****

****关于某人的属性 > 国家/地区等于英国****

如果您的个人资料包含存储在位置字段中的“英国”的多种变体（例如“UK”或“united Kingdom”），则应在细分中包含所有拼写。如果您只想定位欧洲客户群，或者将这些客户排除在某些通信之外，请使用此基于位置的细分。 ![受 GDPR 影响的一部分客户](https://klaviyo.zendesk.com/hc/article_attachments/28720667016347)

## 根据某人与某个位置的接近程度进行细分

您还可以通过关注特定邮政编码（即邮政编码）的特定半径内的配置文件来创建基于位置的分段。此功能只能识别以下位置的配置文件：

- 美国
- 欧盟
- 英国
- 加拿大
- 澳大利亚
- 新西兰

对于英国邮政编码，我们支持按外发代码过滤，不支持内向代码过滤，或者同时使用外向代码和内向代码过滤（通常用空格分隔）。例如，如果某人的完整邮政编码为“SW1W 0NY”，则只有第一部分（“SW1W”）适用于这些过滤器。举例来说，您在波士顿有一家快闪店，想要邀请您电子邮件列表中的波士顿客户。创建一个具有以下定义的段：

****某人与某个位置的邻近度 > 人员位于 > 30 英里范围内 > 02110 位于 > 美国****

****和****

****如果某人可以或不能接收营销>可以接收电子邮件营销>因为有人订阅****

![位于某个邮政编码附近的一段配置文件](https://klaviyo.zendesk.com/hc/article_attachments/28720667021467)

要对个人资料与某个位置的邻近程度进行分段，个人资料必须设置邮政编码和国家/地区属性，或其[为地理位置捕获的 IP 地址](https://help.klaviyo.com/hc/en-us/articles/115005073907)。 ## 其他资源

- [分段入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005237908)
- [段条件参考](https://klaviyo.zendesk.com/hc/en-us/articles/115005062847)
- [了解 Klaviyo 何时以及如何设置配置文件的位置](https://klaviyo.zendesk.com/hc/en-us/articles/115005073907)
- [增强餐厅宾客关系](https://academy.klaviyo.com/en-us/courses/enhance-restaurant-guest-relationships)