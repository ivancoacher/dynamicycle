---
id: "9042531198747"
title: "如何将您的品牌发送域从以前的电子邮件服务提供商 (ESP) 迁移到 Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/9042531198747-How-to-migrate-your-branded-sending-domain-from-a-previous-email-service-provider-ESP-to-Klaviyo"
section: "Warm and ramp your domain"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:55:06Z"
language: "zh"
---
## 你将会学到

了解如何将现有品牌发送域（也称为专用发送域）从以前的电子邮件服务提供商 (ESP) 迁移到 Klaviyo。 ## 开始之前

新的 Klaviyo 帐户和注册时间少于 30 天的域上的帐户应计划在 Klaviyo 中设置域时[预热其发送基础设施](https://help.klaviyo.com/hc/en-us/articles/360025945671)。升温是指您建立合法或“良好”电子邮件发件人声誉的时期。如果没有适当的预热，您可能会面临损害发件人声誉的风险。要确认您的帐户是否有必要进行预热，请参阅我们的指南，了解[如何增强和预热您的发送基础设施](https://help.klaviyo.com/hc/en-us/articles/360025945671)。此外，重要的是您拥有用于发送电子邮件的域，并且能够访问和更新您的 DNS（域名系统）主机记录。 ## 在 Klaviyo 中设置您的专用基础设施

### 品牌发送域名

当您准备好使用 Klaviyo 启动发送域时，[设置品牌发送域](https://help.klaviyo.com/hc/en-us/articles/115000357752)。您将更新 DNS 设置以包含通过 Klaviyo 帐户生成的 CNAME 和 TXT 记录，这将允许您通过自己的品牌发送域而不是 Klaviyo 的共享域发送电子邮件。确保 [品牌发送子域](https://help.klaviyo.com/hc/en-us/articles/360055457791) 尚未在您的 DNS 中使用。如果品牌发送子域已在您的 DNS 中使用，则可能会导致与现有记录发生冲突并破坏域上的其他配置。连接品牌发送域还可以对使用该域从 Klaviyo 发送的邮件启用 DKIM 和 SPF 身份验证。身份验证是一种常见的电子邮件最佳实践，有助于预防和缓解递送问题并提高递送能力。 ### 专用点击跟踪

如果您在之前的 ESP 中使用了自定义点击跟踪域，或者想要开始在 Klaviyo 中使用自定义点击跟踪域，则可以将其他 CNAME 记录添加到您的 DNS 设置中。 [专用点击跟踪](https://help.klaviyo.com/hc/en-us/articles/360001550572) 允许您在点击跟踪链接上显示您自己的域，而不是默认的 Klaviyo 编码，让您的客户进一步信任来自您品牌的电子邮件，因为这些链接很容易识别。 ### 专用IP地址

大多数小型企业或刚刚开始使用 Klaviyo 的企业将使用共享 IP。根据您的电子邮件实践和数量，这应该足以满足您的发送需求。使用[专用 IP 地址](https://help.klaviyo.com/hc/en-us/articles/7675517826587) 的主要好处是 IP 地址的声誉只能受到使用它的单个帐户的影响。因此，您可以完全控制电子邮件发件人的声誉，尤其是当您的电子邮件发送量较大时。请注意，专用 IP 仅适用于符合条件的帐户。要了解您是否有资格获得专用 IP，请联系您的客户成功经理以获取更多信息。 ## 产能因素

从另一个 ESP 迁移您的品牌发送域时，请务必注意送达能力，以确保您成功进入客户的收件箱。 ### 发件人信誉

当您将发送域从之前的 ESP 迁移到 Klaviyo 时，与该域关联的发件人信誉也将保留。您的域的发送信誉是邮箱提供商 (MBP) 在确定如何对传入电子邮件进行排序时考虑的关键因素。如果您发现现有品牌发送域存在送达问题，请按照[电子邮件送达最佳实践](https://help.klaviyo.com/hc/en-us/articles/115005247008) 来提高发件人信誉并调整发送策略。交付能力问题不会通过切换 ESP 自动解决。 ### DMARC

如果发件人电子邮件地址（即发件人地址）中使用的域设置了 DMARC 策略，则当品牌发送域和发件人地址域之间存在不一致时，这可能会影响收件箱的放置。 [DMARC](https://help.klaviyo.com/hc/en-us/articles/4402601857307) 是一种协议，旨在让域所有者能够保护其域免受未经授权的用户发送电子邮件（通常称为电子邮件欺骗）的影响。 对于品牌发送域名，请确保您的域名与 Klaviyo 中的发件人地址保持一致。例如，如果您使用 **sales@example.com** 作为发件人地址发送电子邮件，其中 **example.com** 受 DMARC 保护，则您的帐户将需要对从 Klaviyo 发送的所有电子邮件使用品牌发送域（例如 **send.example.com**），以满足 DMARC 身份验证要求。如果与发件人电子邮件地址不一致，则具有品牌发送域的帐户可能会受到影响。不一致通常会影响使用 Klaviyo 默认共享发送域来发送具有 DMARC 策略的发件人地址域的电子邮件的帐户。如果您使用 Klaviyo 的共享域，请删除与发件人地址域关联的 DMARC 以避免这种情况。 ## 删除通过之前的 ESP 生成的 DNS 记录

一旦您不再需要在以前的 ESP 上发送，请从 DNS 中删除关联的记录。这要求您在 Klaviyo 之外完成任务，并且您可能需要咨询您的 IT 团队了解以下后续步骤。请注意，并非所有域注册服务都允许您直接编辑所有 DNS 记录。如果您无法更新记录，请联系您的 DNS 提供商以获取有关如何更新记录的信息。删除之前 ESP 中的 DNS 记录后，电子邮件将停止从该平台上的品牌发送域发送。在删除记录之前，请确认您不再需要之前的 ESP 上的专用基础设施。 1. 导航至适用的 DNS 提供商。常见的提供商包括：
   - [GoDaddy](https://www.godaddy.com/help/manage-dns-records-680)
   - [Google Domains](https://support.google.com/a/answer/48090?hl=en)
   - [Hostgator](https://www.hostgator.com/help/article/manage-dns-records-with-hostgatorenom)
   - [悬停](https://help.hover.com/hc/en-us/articles/217282457-How-to-Edit-DNS-records-A-CNAME-MX-TXT-and-SRV-Updated-Aug-2015-)
   - [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9214/31/cpanel-email-deliverability-tool-spf-and-dkim-records/)
   - [Squarespace](https://support.squarespace.com/hc/en-us/articles/205812348-Opening-Advanced-DNS-settings)
   - [AWS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-editing.html)
   - [Cloudflare](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/)
2. 删除 DNS 设置中通过之前的 ESP 生成的所有 CNAME 和 TXT 记录。如果服务处理回复管理，某些提供商可能还安装了 MX 记录。如果您的 DNS 中有来自之前 ESP 的其他类型记录，请联系我们的[支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272)。 ## 重要注意事项

### 迁移取消订阅和抑制数据

将专用发送域迁移到 Klaviyo 时，引入先前 ESP 上有关权限的所有可用数据非常重要。这包括电子邮件和短信选择加入的订阅方法和时间戳等信息，以及所有取消订阅和退回数据。通过将此数据导入 Klaviyo，您可以避免发送到可能损害基础设施交付能力的配置文件。有关从以前的提供商迁移数据的更多信息，请参阅我们关于[如何将现有电子邮件订阅者（和取消订阅）迁移到 Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005078487) 的指南。如果您[从 Mailchimp 迁移](https://help.klaviyo.com/hc/en-us/articles/115005254948)，您还应该禁止 Mailchimp 中具有 1 星级评级的联系人，因为向他们发送邮件可能会损害您的送达率。