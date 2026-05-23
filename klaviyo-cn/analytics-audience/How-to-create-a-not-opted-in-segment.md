---
id: "360024584671"
title: "如何创建未选择加入的分段"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360024584671-How-to-create-a-not-opted-in-segment"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "zh"
---
## 你将会学到

了解如何使用细分来识别帐户中未明确选择参与营销的活动个人资料。发送营销活动时，从某些营销活动发送中排除此分段可能会很有用。这可以代替向目标细分添加条件以仅包含选择加入的订阅者。

## 创建一个未选择加入的段

## 电子邮件

由于可以通过多种方式将[活动个人资料](https://klaviyo.zendesk.com/hc/en-us/articles/115005246968) 或可通过电子邮件发送的联系人添加到您的帐户中，因此排除未选择加入的联系人非常重要，这样您就不会收到很高的退订率或垃圾邮件投诉率。未选择加入且未[禁止](https://help.klaviyo.com/hc/en-us/articles/115005246108) 的联系人仍然可以触发流量。详细了解[如何将联系人添加到您的 Klaviyo 帐户](https://help.klaviyo.com/hc/en-us/articles/115005246968)。

此部分包含禁止发送电子邮件的任何人（即无法发送电子邮件，可能是因为他们取消订阅）以及可以发送电子邮件但未明确同意接收营销信息的任何人。这些配置文件可能是通过一般参与添加的（例如，通过启动结账但未完成结账）。

要创建未选择加入的分段：

1. 导航至****受众 > 列表和细分****。
2. 单击****新建 > 创建分段****。
3. 使用以下段定义：
   - **如果某人可以或不能接收营销>无法接收>电子邮件营销**
     或
   - **如果某人可以或不能接收营销>可以接收>电子邮件营销>因为该人>从未订阅。
     ![不同意电子邮件营销的部分人](https://klaviyo.zendesk.com/hc/article_attachments/33130558099995)**

### 短信或推送通知

您可以为其他渠道（例如短信或推送）创建类似的细分。对于这些频道，该频道无法访问“从未订阅”的联系人，因此您可以简单地使用此细分定义：

**如果某人可以或不能接收营销>无法接收>短信营销/移动推送营销**

**！[未选择短信营销的细分](https://klaviyo.zendesk.com/hc/article_attachments/33130558103835)**

## 结果

发送营销活动时，请使用[不发送至功能](https://help.klaviyo.com/hc/en-us/articles/115005227808)，以确保此分段从您的发送中排除。然后，当您准备好发送下一个营销活动时，[克隆上一个营销活动](https://help.klaviyo.com/hc/en-us/articles/115006199048)。克隆的营销活动继承相同的收件人组，因此您不必担心每次创建营销活动时都会排除此细分。

## 其他资源

- [创建客户参与等级](https://klaviyo.zendesk.com/hc/en-us/articles/360000407272)
- [了解有关 GDPR 的常见问题](https://klaviyo.zendesk.com/hc/en-us/articles/360003211651)
- [如何细分渠道同意](https://klaviyo.zendesk.com/hc/en-us/articles/19514751281307)