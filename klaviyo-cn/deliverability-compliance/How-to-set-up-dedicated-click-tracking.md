---
id: "360001550572"
title: "如何设置专用点击跟踪"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360001550572-How-to-set-up-dedicated-click-tracking"
section: "Warm and ramp your domain"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:41Z"
language: "zh"
---
## 你将会学到

了解如何设置专门的点击跟踪以及这样做时的最佳实践。专用点击跟踪允许您在点击跟踪链接上显示您自己的域，而不是默认的 Klaviyo 域。 ## 什么是专用点击跟踪？专用点击跟踪允许您在点击跟踪链接上显示您自己的域，而不是默认的 Klaviyo 编码。任何公司都有资格进行专门的点击跟踪。 ### 为什么要设置专门的点击跟踪？专用点击跟踪是有益的，因为它可以让您的客户进一步信任来自您品牌的电子邮件，因为链接很容易识别。当将鼠标悬停在您电子邮件中的链接上时，他们将看到您的品牌名称，而不是来自 Klaviyo 编码链接的一长串字母和数字。这可能会增加他们点击您的链接的机会。此外，许多邮箱提供商和过滤软件都会考虑您的消息传递中使用的所有域的声誉。在专用点击跟踪链接和[发送域](https://help.klaviyo.com/hc/en-us/articles/115000357752) 中使用相同的根域可以使您的品牌保持一致。专用点击跟踪也是使用[电子邮件中的通用链接和应用程序链接](https://help.klaviyo.com/hc/en-us/articles/41701832186523)的先决条件。 ## 设置专用点击跟踪

您可以通过添加新的 DNS 记录来手动配置专用点击跟踪，或者如果您使用的是动态品牌发送域，则可以联系 Klaviyo 自动启用它。 ### 自动设置专用点击跟踪

如果您在 Klaviyo 中拥有[动态品牌发送域](https://help.klaviyo.com/hc/en-us/articles/115000357752)配置，则可以[联系 Klaviyo 的支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272)为您的帐户启用 SSL 的点击跟踪域。如果您采用静态配置且 CNAME 记录指向 **klaviyodns.com**，您还可以代表您设置专用的点击跟踪域，如下所示。您必须拥有 Klaviyo 的付费帐户才能代表您设置点击跟踪域。 Klaviyo 将为您的品牌设置以下点击跟踪域：

- **trk.send.yourbrandeddomain.com**

例如，如果品牌发送域是 **send.klaviyo.com**，则专用点击跟踪域将为 **trk.send.klaviyo.com**。在此示例中，**send** 是品牌发送域的子域，但点击跟踪域将反映您自己对子域的选择。 Klaviyo 无法代表您创建自定义点击跟踪域，并且点击跟踪域将始终与上面的示例匹配。 ### 手动设置专用点击跟踪

设置专用点击跟踪需要向托管提供商的 DNS 设置中添加额外的 CNAME 记录。我们提供以下记录，您可以将其添加到您的 DNS 提供商中。添加以下 CNAME 记录以设置您的专用点击跟踪域：

|类型 |主机名 |价值|
| --- | --- | --- |
|别名 | `trk` | dct.klaviyodns.com |

根据您的 DNS 提供商的不同，上例中的“主机名”和“值”字段的名称可能有所不同。例如，某些 DNS 提供商可能将其称为“主机名”，而其他提供商可能将其称为“名称”。但是，您需要输入的记录是相同的。如果您遇到问题，请查看下面的[一些流行 DNS 提供商的文档](#h_01HQ3KN3Y0V7​​23N3RAD8DSMNC6) 的链接。如果您的 DNS 提供商允许您代理记录，您将在启用此功能的 Klaviyo 中看到专用点击跟踪设置的问题。 Cloudflare 中通常会发生这种情况，但其他 DNS 提供商也可能发生这种情况。您需要禁用记录的代理，以便它们通过互联网进行解析，以便可以验证它们的存在。更新 DNS 记录后，请通过相关帐户[联系 Klaviyo 支持](https://help.klaviyo.com/hc/en-us/articles/115001002272) 以验证您的记录。 ## 用于专用点击跟踪的 SSL

强烈建议将 SSL 证书用于专用点击跟踪域。 SSL 是一种基于加密的互联网安全协议，用于确保互联网通信的隐私、身份验证和数据完整性。通过配置 SSL 证书，您的 URL 可以以 HTTPS 而不是 HTTP 开头，并且您的点击跟踪域可以指向您自己的内容分发网络 (CDN)。 这向点击您的链接的用户表明与关联域的连接是安全的，从而提高了客户的信任和安全性。如果代表您动态设置点击跟踪域，或者您通过 DNS 更新手动设置指向 **klaviyodns.com** 域的点击跟踪域，Klaviyo 将为您的子域自动生成 SSL 证书。对于后一种方法，如果您的域有 [CAA 记录](#h_01JHG3R2YKC01NT85Z6ZTNNGVAG) 并且没有必要的要求，则必须进行相应的更新。 ## CAA 记录

CAA（证书颁发机构授权）记录是一种 DNS 记录，可降低未经授权的证书生成风险。如果您的品牌有 CAA 记录，该记录必须包含以下属性：

|类型 |域名|价值|
| --- | --- | --- |
|中国航空协会 | `example.com` | 0 期 pki.goog |

这允许 Klaviyo 为您的子域生成证书。这仅与添加指向 **klaviyodns.com** 的新 DNS 记录的手动设置方法相关。 ## 有关在何处更新 DNS 记录的提示

无论您在何处注册或当前管理域名，都可以更新您的 DNS 记录。但是，并非所有域注册服务都允许您编辑所有 DNS 记录。如果您无法更新上述记录，请联系您的 DNS 提供商以获取有关如何更新这些记录的信息。将记录添加到 DNS 的过程取决于您使用的域名提供商。以下是常见提供商的文档链接：

- [GoDaddy](https://www.godaddy.com/help/manage-dns-680)
- [Google Domains](https://support.google.com/a/answer/48090?hl=en)
- [Cloudflare](https://support.cloudflare.com/hc/en-us/articles/200169046-How-do-I-add-a-CNAME-record-)
- [Name.com](https://www.name.com/support/articles/115004895548-Adding-a-CNAME-Record)
- [Hostgator](http://support.hostgator.com/articles/hosting-guide/lets-get-started/dns-name-servers/manage-dns-records-with-hostgatorenom)
- [悬停](https://help.hover.com/hc/en-us/articles/217282457-Managing-DNS-records-)
- [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9214/31/email-authentication-tool-in-cpanel-spf-records)
- [Squarespace](https://support.squarespace.com/hc/en-us/articles/205812348-Opening-Advanced-DNS-settings)

## 禁用单个 URL 的点击跟踪

如果您想禁用特定链接的点击跟踪，可以使用以下 HTML 标记来实现：

````
<a clicktracking=off href="https://example.com">Klaviyo 主页</a>
````

## 其他资源

- [Klaviyo现场追踪指南](https://help.klaviyo.com/hc/en-us/articles/115005076767)