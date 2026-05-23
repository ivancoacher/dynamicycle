---
id: "4417768780827"
title: "解决品牌发送域问题"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4417768780827-Troubleshooting-branded-sending-domain-issues"
section: "Monitor deliverability and metrics"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:56:57Z"
language: "zh"
---
## 你将会学到

了解在 Klaviyo 中设置品牌发送域（也称为专用发送域）时如何诊断验证问题。品牌发送域使您能够发送来自您的品牌的电子邮件，而不是来自 Klaviyo 的共享域。有关设置说明，请访问我们的指南[如何设置品牌发送域](https://help.klaviyo.com/hc/en-us/articles/115000357752)。 Google 和雅虎已宣布新的发件人要求，计划于 2024 年 2 月开始实施。虽然这已经是最佳实践，但设置品牌发送域将成为批量发件人进入 Gmail 收件箱的要求。 Google 将每天向 Google 帐户发送 5000 封或更多电子邮件的人视为“批量发件人”。来自发件人的所有流量都计入 5000 封电子邮件阈值，包括交易电子邮件。详细了解 [Gmail 和 Yahoo 即将推出的发件人要求。](https://www.klaviyo.com/blog/gmail-update)

## 开始之前

在开始以下故障排除步骤之前，请确认您已尝试在 Klaviyo 中验证您的发送域并看到错误。请注意，Klaviyo 在验证后不会自动应用您的域，因为我们希望确保您准备好首先预热您的发送基础设施（如果适用）。验证后，您需要单击****应用域名****。我们还建议给 DNS 传播和清除缓存的时间。此过程可能需要长达 48 小时，具体取决于您的 DNS 提供商。 ## 使用第三方工具进行故障排除

Klaviyo 需要 3 个 CNAME 或 NS 记录用于电子邮件身份验证，以及 1 个 TXT 记录用于域所有权验证。在 Klaviyo 中设置品牌域名时，您会看到根据您的[子域名](https://klaviyo.zendesk.com/hc/en-us/articles/360055457791) 选择显示的类似记录：

![NS 记录](https://klaviyo.zendesk.com/hc/article_attachments/28705664613147)

设置品牌发送域时，选择**动态**路由方法需要将 NS 记录添加到您的 DNS 提供商，而**静态**路由选项需要 CNAME 记录。 Klaviyo 建议使用 **动态** 路由选项来最好地优化您的发送，但如果您的 DNS 提供商不支持 NS 记录，请考虑使用 **静态** 路由选项。如果您的品牌选择使用二级子域，例如 **example.send.klaviyo.com**，则根域将为 **send.example.com**，发送域将为 **example.send.klaviyo.com**。

在预期发送域为 **send.klaviyo.com** 的示例中，“send”作为子域，“klaviyo.com**”** 作为根域，预期的 DNS 记录如下：

对于 **动态** 路由选项：

|  |  |  |
| --- | --- | --- |
| ****主持人**** | ****价值**** | ****记录类型**** |
|发送.helloworld.com | ns1.klaviyo.com | NS |
|发送.helloworld.com | ns2.klaviyo.com | NS |
|发送.helloworld.com | ns3.klaviyo.com | NS |
|发送.helloworld.com | ns4.klaviyo.com | NS |
| helloworld.com | klaviyo-site-verification=public\_API\_key | klaviyo-site-verification=public\_API\_key |文本 |

对于 **静态** 路由选项：

这些只是示例，您帐户的实际 CNAME 记录值可能会有所不同。确保使用您帐户中生成的值。 |  |  |  |
| --- | --- | --- |
| ****主持人**** | ****价值**** | ****记录类型**** |
|发送.klaviyo.com | 1.klaviyodns.com |别名 |
| kl.\_domainkey.klaviyo.com | kl1.domainkey.1.klaviyodns.com |别名 |
| kl2.\_domainkey.klaviyo.com | kl2.domainkey.1.klaviyodns.com |别名 |
| klaviyo.com | klaviyo-site-verification=public\_API\_key | klaviyo-site-verification=public\_API\_key |文本 |

MxToolbox 的 DNS 查找是一组有用的工具，可检查您的记录是否正确传播：

- [DNS查找](https://mxtoolbox.com/SuperTool.aspx)
- [TXT查找](https://mxtoolbox.com/TXTLookup.aspx)

您可以使用 DNS 查找工具在主机中搜索 CNAME 和 NS 记录，并使用 TXT 查找工具搜索 TXT 记录。 ## NS 和 CNAME 查找示例

使用 MxToolbox 下拉列表中的 DNS 检查选项：

![DNS 检查.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705664615835)

### NS 记录

![NS 故障排除.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705664614299)

### CNAME 记录

发送.klaviyo.com：

![send.klaviyo.com.jpg](https://klaviyo.zendesk.com/hc/article_attachments/36642522069531)

kl.\_domainkey.klaviyo.com：

![kl._domainkey.klaviyo.com .jpg](https://klaviyo.zendesk.com/hc/article_attachments/36642522076699)

kl2.\_domainkey.klaviyo.com：

![kl2._domainkey.klaviyo.com .jpg](https://klaviyo.zendesk.com/hc/article_attachments/36642522084763)

### TXT 查找示例

klaviyo.com：

![klaviyo.com 的 TXT 查找](https://klaviyo.zendesk.com/hc/article_attachments/28705664611739)

根据您是否看到查询返回的值，一些常见错误可能是问题的根源。 ## 如果查询返回值

为了使您的发送域在 Klaviyo 中成功验证，您的查询返回的值必须与 Klaviyo 中显示的值完全匹配。确保您看到的返回值与 Klaviyo 中的值之间没有任何差异。 ### 根域自动附加到值中

一些 DNS 提供商希望附加值末尾有一个句点 (.)。如果没有这段时间，DNS 提供商会假定整个值字段是正在配置的域的子域，并将自动添加根域。例如，如果您输入 **u161779.wl030.sendgrid** （末尾没有句点），这将使值 **u161779.wl030.sendgrid.net.rootdomain.com** 而不仅仅是 **u161779.wl030.sendgrid.net。**

## 如果查询没有返回值

### 根域在主机名中重复

我们还建议检查您的 DNS 提供商是否只需要主机名字段中的子域，并自动附加根域。例如，如果您添加 CNAME 记录 **send.domain.com**，它将自动变为 **send.domain.com.domain.com**。相反，您可能只需要在此实例中添加“send”子域，以使记录的主机名成为 **send.domain.com。** 比较您的其他 DNS 记录，看看您是否需要附加它，或者您的提供商是否自动执行此操作。 ### 被代理的记录

如果您的 DNS 提供商允许您代理记录，并且启用此功能，您将在 Klaviyo 中看到品牌域设置问题。 Cloudflare 中通常会发生这种情况，但其他 DNS 提供商也可能发生这种情况。您需要禁用记录的代理，以便它们通过互联网进行解析，这样就可以通过 Klaviyo 中的发送域设置工具来验证它们的存在。在设置过程之后，记录代理需要保持禁用状态，并且电子邮件才能按预期进行身份验证。 ## 其他 DNS 提供商问题

### DNS 提供商不支持 @ 符号

如果 DNS 提供商不支持符号“@”，则需要将根域设置为站点验证记录的主机名。 “@”符号是根域 (business.com) 的简写，因此您可以根据您的 DNS 提供商支持的内容使用任一选项。 ### DNS 提供商不支持下划线

某些 DNS 提供商不支持 CNAME 记录使用下划线。但是，为了使您的发送域在 Klaviyo 中正常工作，这些下划线是必要的。如果您的 DNS 提供商不支持 CNAME 中的下划线，我们建议您首先联系 DNS 提供商的支持团队，看看他们是否可以为您创建记录。通常，如果您联系 DNS 提供商，他们将能够手动调整您的 CNAME 以包含下划线。如果您的 DNS 提供商最终无法支持下划线，请[考虑使用其他提供商](https://www.hostinger.com/tutorials/how-to-change-domain-nameservers)，因为这些对于您在 Klaviyo 中的域设置是必需的。 ### 根域上已存在 TXT 值

如果您的根域上存在现有 TXT 记录，您可以将 Klaviyo 值附加到现有字段。只要存在 Klaviyo 请求的值，在 Klaviyo 中设置您的品牌域名时，记录就会成功验证。 ## DMARC

为了使电子邮件符合 [DMARC](https://help.klaviyo.com/hc/en-us/articles/4402601857307)，您帐户上的根域需要与电子邮件的发件人地址域保持一致。 例如，如果您使用 **sales@example.com** 作为发件人地址发送电子邮件，其中 example.com 受 DMARC 保护，则您的帐户将需要对从 Klaviyo 发送的所有电子邮件使用品牌发送域（例如 **send.example.com**），以满足 DMARC 身份验证要求。