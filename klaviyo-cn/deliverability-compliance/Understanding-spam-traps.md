---
id: "360003019251"
title: "了解垃圾邮件陷阱"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360003019251-Understanding-spam-traps"
section: "Monitor deliverability and metrics"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: "zh"
---
## 你将会学到

了解垃圾邮件陷阱以及如何防止向其发送邮件，以便保护您的送达能力。

## 什么是垃圾邮件陷阱？

垃圾邮件陷阱是一个电子邮件地址，用于识别未遵循最佳实践或发送未经请求的电子邮件的发件人。垃圾邮件陷阱通常用于将发件人放入垃圾邮件文件夹中，或更糟糕的是，阻止发送到特定收件箱提供商的所有流量，这就是为什么近年来它们变得越来越流行并受到主要收件箱提供商的监控。

### 原始垃圾邮件陷阱 (PST)

创建原始垃圾邮件陷阱的目的是找到发送垃圾邮件或不遵循最佳实践的人。这些电子邮件从未在现实世界中使用过，并且是全新的地址，因此点击 PST 可能会导致您的 IP 被列入黑名单或您的电子邮件成为垃圾邮件。在收件箱提供商看来，这意味着您要么购买了列表，要么不遵循最佳实践，因为这些地址不合法并且不会打开电子邮件。

### 回收垃圾邮件陷阱 (RST)

与原始垃圾邮件陷阱不同，回收的垃圾邮件陷阱是过去某个时刻用作真实地址的地址。通常将 RST 视为免费服务提供的域，例如 @yahoo 或 @gmail。但是，在某些情况下，您可能会看到已关闭企业的域被重新购买，目的是使其成为 RST。

过时的电子邮件并不总是在不再使用后立即成为 RST。一些收件箱提供商可能会在没有活动后删除该地址 - 即如果该地址停止接收电子邮件。地址被删除后，如果您发送到该地址，电子邮件将被硬退回。 Klaviyo 自动抑制硬弹跳。

通常，收件箱提供商会将帐户删除 6-12 个月，然后将其作为垃圾邮件陷阱回收。 RST 的目的是识别在列表清理方面未遵循最佳实践的人员，而不一定是识别垃圾邮件发送者。

下面的图表涵盖了收件箱提供商何时可以删除不活动的帐户：

|  |  |
| --- | --- |
| ****域名**** | ****删除前的不活动时间**** |
|雅虎 | 12 个月 |
|美国在线 | 3个月|
|邮箱 | 9 个月 |
| Outlook/Live/Hotmail | 12 个月 |

### 角色帐户

角色帐户是您希望避免向其发送营销电子邮件的电子邮件地址，因为它们不受一个人监控。通常，这些是组地址或别名，不会选择接收营销电子邮件。

|  |  |  |  |
| --- | --- | --- | --- |
|滥用@ |支持@ |工作人员@ |取消订阅@ |
|邮政局长@ |管理员@ |订阅@ |信息@ |
|工作@ |诺克@ |销售@ |站长@ |
|邮件守护进程@ |帮助@ | www@ |订单@ |
|无回复@（或noreply@）|主机管理员@ |计费@ |营销@ |

[RFC 2142](https://tools.wordtothewise.com/rfc/2142) 中概述了更多详细信息。

## 如何防止发送到垃圾邮件陷阱

通过使用以下一些策略可以轻松避免垃圾邮件陷阱：

- 禁止从未表现出任何参与迹象的个人资料。 [如何创建从未参与的细分](https://help.klaviyo.com/hc/en-us/articles/115005078347)
- 查看我们的指南[如何从您的帐户中删除垃圾邮件陷阱](https://help.klaviyo.com/hc/en-us/articles/360015537111-How-to-Remove-Spam-Traps-from-Your-Account)
- 使用[双重选择加入](https://help.klaviyo.com/hc/en-us/articles/115005251108)
- 切勿购买电子邮件列表

## 其他资源

- [如何创建从未参与过的细分](https://help.klaviyo.com/hc/en-us/articles/115005078347)
- [列表清理指南](https://help.klaviyo.com/hc/en-us/articles/115005078347-List-Cleaning)
- [了解 Klaviyo 中的退回电子邮件](https://help.klaviyo.com/hc/en-us/articles/115005250408-Bounced-Emails-in-Klaviyo)
- [如何从您的帐户中删除垃圾邮件陷阱](https://help.klaviyo.com/hc/en-us/articles/360015537111-How-to-Remove-Spam-Traps-from-Your-Account)