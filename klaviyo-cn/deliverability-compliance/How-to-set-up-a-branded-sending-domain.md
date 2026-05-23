---
id: "115000357752"
title: "如何设置品牌发送域"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115000357752-How-to-set-up-a-branded-sending-domain"
section: "Warm and ramp your domain"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-15T09:38:12Z"
language: "zh"
---
## 你将会学到

了解如何设置品牌发送域（也称为专用发送域），以便当电子邮件到达收件箱提供商时，它们将显示为来自您的品牌而不是 Klaviyo。如果您要从之前的电子邮件服务提供商 (ESP) 转移现有的品牌发送域，请参阅我们详细的[迁移指南](https://help.klaviyo.com/hc/en-us/articles/9042531198747)。 ![](https://fast.wistia.com/embed/medias/yuhwp4mwi2/swatch)

## 什么是品牌发送域？品牌发送域允许您发送看似来自您的品牌的电子邮件，并允许您更好地全面控制发件人声誉。任何公司都有资格创建品牌发送域。默认情况下，大多数用户将从共享 IP 和 Klaviyo 域开始发送。该域将出现在电子邮件顶部的发件人信息中，如下所示（即“代表 '' 或“通过 klaviyomail.com 发送”）。在下面的 Gmail 示例中，您的收件人会看到您的发件人电子邮件地址包含“via klaviyomail.com”，因为您使用的是共享发送域。![在使用 klaviyomail.com 域之前发送的电子邮件的示例已更新](https://klaviyo.zendesk.com/hc/article_attachments/28723622866075)

通过转移到品牌发送域，您将删除发件人电子邮件地址旁边显示的“via klaviyomail.com”消息。这也意味着您的电子邮件将不再通过共享域发送，从而使收件箱提供商能够更轻松地验证您的身份并通过[DMARC 等电子邮件身份验证协议](https://help.klaviyo.com/hc/en-us/articles/4402601857307)。 Google 和雅虎已宣布新的发件人要求，计划于 2024 年 2 月开始实施。虽然这已经是最佳实践，但设置品牌发送域将成为批量发件人进入 Gmail 收件箱的要求。 Google 将每天向 Google 帐户发送 5000 封或更多电子邮件的人视为“批量发件人”。来自发件人的所有流量都计入 5000 封电子邮件阈值，包括交易电子邮件。详细了解 [Gmail 和 Yahoo 即将推出的发件人要求。](https://www.klaviyo.com/blog/gmail-update)

## 关于使用 Klaviyo 生成域名系统 (DNS)

连接品牌发送域的关键部分是生成所需的 DNS 记录。要生成记录，您需要在 Klaviyo 中设置品牌发送域时输入以下信息。 - ****根域****
  这是您购买或通过域名注册商注册的域名，它反映了您品牌的网站域名。您可能还拥有反映此域的电子邮件地址。例如，如果您的公司名为 **Hello World**，则您品牌的根域可能是 **helloworld.com**，您的友好发件人地址可能是 **name@helloworld.com**。 - ****品牌发送域名****
  该域名将用于从 Klaviyo 发送电子邮件，并将显示在您的电子邮件标头中。请务必注意，品牌发送域必须具有唯一的、未使用的子域，以免干扰根域上的任何外部电子邮件配置。 Klaviyo 最常用的子域名是“send”。使用上面的示例，Hello World 的品牌发送域可以是 **send.helloworld.com**。但是，您可以使用任何尚未使用的子域。只要所有相关的 DNS 记录都已到位，多个公司以及多个 Klaviyo 帐户就可以使用给定的发送域。如果您的公司有多个具有单独 Klaviyo 帐户的子品牌，您可以在每个帐户中使用相同的品牌发送域。为此，您需要将品牌发送域连接到每个帐户并生成每个帐户所需的唯一 DNS 记录。 ## 动态与静态路由

设置品牌发送域时，您可以选择是否将子域委托给 Klaviyo，以便它可以动态选择最佳发送提供商选项。通过委托您的子域名，您将向 Klaviyo 提供管理您品牌的子域名和创建 DNS 记录的授权。这些权限仅用于与您的发送相关的任务，子域委托不会影响您品牌的根域或任何其他子域。您可以随时通过删除在品牌发送域设置过程中添加的关联 DNS 记录来撤销子域委派。 在 Klaviyo 中，您可以在设置品牌域名时选择以下路由选项：

- ****动态****
  将您的子域委托给 Klaviyo，以动态选择电子邮件发送提供商，以获得最佳性能、声誉和稳定性。 - ****静态****
  允许 Klaviyo 通过单个静态电子邮件发送提供商发送电子邮件。生成 DNS 记录时，Klaviyo 将为 **动态** 路由选项创建 NS 记录，并为 **静态** 路由选项创建 CNAME 记录。某些 DNS 提供商不支持 NS 记录。如果您的 DNS 提供商不支持 NS 记录，则必须使用 **静态** 路由选项。 Klaviyo 建议选择 **动态** 路由选项以最好地优化您的发送性能。如果您使用的是在此功能之前创建的品牌发送域，或者决定从 **静态** 移动到 **动态**，请在 Klaviyo 中删除您的域，并删除 DNS 提供商中子域的现有 CNAME 记录。完成后，使用**动态**选项完成设置过程。请注意，记录传播最多可能需要 48 小时。 ## 创建品牌发送域的要求

### 开始之前

在开始此过程之前，新的 Klaviyo 帐户应确保您有时间[预热您的基础设施](https://help.klaviyo.com/hc/en-us/articles/360025945671)。此外，重要的是您拥有用于发送电子邮件的域，并且您或您团队中的某人有权访问 DNS 主机以创建所需的记录。迁移至品牌发送域的现有 Klaviyo 客户无需再次预热基础设施，只要您具备：

- 域名已注册至少 30 天并且
- 您已经使用该域名发送电子邮件（例如，您过去曾在之前的电子邮件服务提供商处使用过该域名，或者在您的发件人地址中使用过 Klaviyo）。在对您的帐户应用任何域更改之前，请暂停所有发送。应用更改并进行测试后，您就可以恢复流程并安排任何未来的活动。 ### 清单

1. 连接品牌发送域并生成 DNS 记录。 2. 与您的 DNS 提供商更新 DNS 记录（请注意，这不是在 Klaviyo 中完成的）。 3. 验证并应用您的域。 4. 新的 Klaviyo 帐户可以预热其发送基础设施。对于具有至少 30 天发送历史记录的现有 Klaviyo 帐户，他们可以恢复正常发送，而不必再次预热其基础设施。 ## 在 Klaviyo 中生成 DNS 记录

Klaviyo 需要 3 个 CNAME 或 4 个 NS 记录用于电子邮件身份验证，以及 1 个 TXT 记录用于域所有权验证。动态路由选项使用 NS 记录，而静态路由选项使用 CNAME 记录。只有具有 **所有者**、**管理员**、**经理** 和 **活动协调员**[用户角色](https://help.klaviyo.com/hc/en-us/articles/115005231648) 的用户才能设置品牌发送域。 1. 单击帐户左下角的公司名称。 2. 选择****设置****。 ![左下角的Klaviyo帐户菜单](https://klaviyo.zendesk.com/hc/article_attachments/28723628194843)
3. 从主选项卡中选择 ****Domains****。 4. 选择****添加域。****
5. 验证您品牌的根域是否正确。 Klaviyo 会自动从您的帐户中提取域名。 ![根域.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723622878235)
6. 单击****下一步****。 7. 在**发送域**（例如“发送”）下指定任意且未使用的子域（即您当前在营销中的其他地方未使用的子域）。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38091860756891)
8. 选择您所需的 **路由** 类型（即 **动态** 或 **静态**）。 **动态**选项仅适用于支持动态配置的域。 9. 选择是否要向您的域添加 DMARC 记录（建议这样做以满足 Gmail 和 Yahoo 发件人要求）。只有当前缺少 DMARC 记录的域才会看到此选项。 10. 选择是否要将域与 Entri 连接，或手动设置。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38092031975067)

只有符合 Entri 集成条件的域才会看到自动设置选项。如果您选择手动设置域，则会向您显示生成的 DNS 记录，以便您可以手动将它们添加到您的 DNS。 通过 Entri 自动配置，记录将代表您自动添加。目前，无法在 Sendgrid 基础设施上使用具有专用点击跟踪的静态品牌发送域。如果您使用 Sendgrid 的专用点击跟踪，请更新您的 CNAME 记录以使用 Klaviyo 基础设施或设置动态品牌发送域。 ### DNS 记录

在预期发送域为 **send.helloworld.com** 的示例中，“send”作为子域，“helloworld.com”作为根域，生成的 DNS 记录将具有以下结构。这些只是示例，您帐户的实际 CNAME 记录值可能会有所不同。确保使用您帐户中生成的值。 |  |  |  |
| --- | --- | --- |
| ****主持人**** | ****价值**** | ****记录类型**** |
|发送.helloworld.com | ns1.klaviyo.com | NS |
|发送.helloworld.com | ns2.klaviyo.com | NS |
|发送.helloworld.com | ns3.klaviyo.com | NS |
|发送.helloworld.com | ns4.klaviyo.com | NS |
| helloworld.com | klaviyo-site-verification=public\_API\_key | klaviyo-site-verification=public\_API\_key |文本 |

通过使用 CNAME 记录的 **静态** 路由选项，记录将如下所示：

|  |  |  |
| --- | --- | --- |
| ****主持人**** | ****价值**** | ****记录类型**** |
|发送.helloworld.com | 1.klaviyodns.com |别名 |
| kl.\_domainkey.helloworld.com | kl1.domainkey.1.klaviyodns.com |别名 |
| kl2.\_domainkey.helloworld.com | kl2.domainkey.1.klaviyodns.com |别名 |
| helloworld.com | klaviyo-site-verification=public\_API\_key | klaviyo-site-verification=public\_API\_key |文本 |

如果您品牌的预期发送域有两个子域，例如 **send.mail.helloworld.com，** “send”将用于子域，“mail.helloworld.com”将用于根域。预期的 DNS 记录如下：

|  |  |  |
| --- | --- | --- |
| ****主持人**** | ****价值**** | ****记录类型**** |
| send.mail.helloworld.com | ns1.klaviyo.com | NS |
| send.mail.helloworld.com | ns2.klaviyo.com | NS |
| send.mail.helloworld.com | ns3.klaviyo.com | NS |
| send.mail.helloworld.com | ns4.klaviyo.com | NS |
| helloworld.com | klaviyo-site-verification=public\_API\_key | klaviyo-site-verification=public\_API\_key |文本 |

通过使用 CNAME 记录的 **静态** 路由选项，记录将如下所示：

|  |  |  |
| --- | --- | --- |
| ****主持人**** | ****价值**** | ****记录类型**** |
| send.mail.helloworld.com | 1.klaviyodns.com |别名 |
| kl.\_domainkey.mail.helloworld.com | kl1.domainkey.1.klaviyodns.com |别名 |
| kl2.\_domainkey.mail.helloworld.com | kl2.domainkey.1.klaviyodns.com |别名 |
| helloworld.com | klaviyo-site-verification=public\_API\_key | klaviyo-site-verification=public\_API\_key |文本 |

## DMARC

DMARC 是一项[电子邮件身份验证](https://help.klaviyo.com/hc/en-us/articles/4402601857307) 策略，允许收件箱提供商验证电子邮件的真实性，使域所有者能够保护其域免遭未经授权的使用。 DMARC 政策也是 Gmail 和 Yahoo 为成功登陆收件箱而制定的[发件人要求](https://www.klaviyo.com/blog/gmail-update)。如果您希望 Klaviyo 生成 DMARC 记录，请在设置品牌发送域时打开“添加 DMARC 记录”选项。 ![内包装.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723622880923)

Klaviyo 将生成以下 DMARC 记录，这不会影响您的电子邮件的递送，但满足 Gmail 和 Yahoo 发件人要求：

v=DMARC1； p=无；

## 更新您的 DNS 记录

### 使用 Entri 自动发布记录

要让 Klaviyo 自动代表您发布 DNS 记录，请在品牌发送域设置过程中选择“与 Entri 连接”选项。当继续使用此选项时，Klaviyo 将分析您的域以检测其托管的 DNS 提供商。一旦识别，系统将提示您使用适当的凭据登录您的 DNS 提供商，从而授予 Klaviyo 代表您发布记录的权限。如果 Klaviyo 无法检测到您的 DNS 提供商，您需要手动设置您的品牌发送域。 ![登录.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723622903195)

如果您团队的另一名成员管理您的 DNS 设置，您可以通过选择“**或将登录信息转发给其他人**”来转发登录信息。此外，您可以通过选择“**显示已添加的 DNS** 记录”来查看正在添加的记录。登录后，Klaviyo 将设置必要的记录，并且您的域将成功配置为发送。 配置完成后，您将看到一条确认信息。 ![Entri Modal.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723628222363)

### 手动设置您的域

如果您选择手动设置品牌发送域，则该过程的此步骤要求您在 Klaviyo 之外完成任务。您需要将在 Klaviyo 中生成的新 DNS 记录应用到您的域。请注意，您需要访问公司的 DNS 提供商的平台才能进行这些更改。您可能还需要咨询您的 IT 团队了解以下后续步骤。您无需在 DNS 设置中创建子域。 CNAME 和 NS 记录应添加到您品牌的根域，并通过记录自动将品牌域设置过程中指定的子域重定向到 Klaviyo 基础设施。并非所有域名注册服务都允许您直接编辑所有 DNS 记录。如果您无法更新记录，请联系您的 DNS 提供商以获取有关如何更新记录的信息。 1. 选择 **手动设置** 后，在 **查找您的 DNS 区域文件** 页面上选择您的域提供商。根据您的域名提供商，Klaviyo 将显示在 DNS 提供商平台中查找区域文件的步骤。您将在区域文件中添加生成的 DNS 记录。 2. 选择****下一步****。 3. 将鼠标悬停在文本上并单击，将生成的 DNS 记录复制到剪贴板，以便您可以将它们添加到 DNS 区域文件。 4. 将记录添加到 DNS 提供商平台中的区域文件中。 ![记录.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723628225307)

一些常见的 DNS 提供商包括：

- [GoDaddy](https://www.godaddy.com/help/manage-dns-zone-files-680)
- [Google Domains](https://support.google.com/a/answer/48090?hl=en)
- [Hostgator](https://www.hostgator.com/help/article/manage-dns-records-with-hostgatorenom)
- [悬停](https://help.hover.com/hc/en-us/articles/217282457-How-to-Edit-DNS-records-A-CNAME-MX-TXT-and-SRV-Updated-Aug-2015-)
- [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9214/31/cpanel-email-deliverability-tool--spf-and-dkim-records/)
- [Squarespace](https://support.squarespace.com/hc/en-us/articles/205812348-Opening-Advanced-DNS-settings)
- [AWS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-editing.html)
- [Cloudflare](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/)

****对于 BigCommerce 域名****

如果您是使用 BigCommerce Domains 作为 DNS 提供商的商家，则您的 DNS 记录的主机值与您在 Klaviyo 中看到的内容略有不同。设置品牌发送域时，您必须使用 **静态** 路由选项，因为不支持与 **动态** 选项关联的 NS 记录。对于 3 个 CNAME 记录的 **主机**，您必须将一个句点后跟您的根域名附加到 Klaviyo 中提供的记录的**主机**。例如，如果您品牌的根域是 **helloworld.com**，则您必须在 BigCommerce 中输入的 **Host** 值如下所示：

这些只是示例，您帐户的实际 CNAME 记录值可能会有所不同。确保使用您帐户中生成的值。 |  |  |  |
| --- | --- | --- |
| ****主持人**** | ****价值**** | ****记录类型**** |
|发送.helloworld.com | 1.klaviyodns.com |别名 |
| kl.\_domainkey.helloworld.com | kl1.domainkey.1.klaviyodns.com |别名 |
| kl2.\_domainkey.helloworld.com | kl2.domainkey.1.klaviyodns.com |别名 |
| helloworld.com | klaviyo-site-verification=public\_API\_key | klaviyo-site-verification=public\_API\_key |文本 |

如果您使用 Google Domains 作为 DNS 提供商，并使用**动态**路由选项连接品牌发送域，请使用“向此记录添加更多选项”将所有 NS 记录添加到[到单个记录中](https://community.klaviyo.com/analytics-and-deliverability-72/help-dns-record-for-google-domains-10653)。

如果您的 DNS 提供商在此过程中不接受“@”符号，则需要添加您的 TXT 记录并使用您的根域作为主机名。 “@”符号只是实现相同结果的简写方法（即，将 TXT 记录放置在根域上）。例如，记录将简单地是：

`类型：TXT
主机名：YOURWEBSITE.COM
值：klaviyo-site-verification=YOUR_PUBLIC_API_KEY`

## 验证并应用您的域名

仅当您准备好开始使用您的域名发送时，才应开始执行以下步骤。 如果您要连接没有电子邮件历史记录的新品牌发送域，则需要首先[预热此域。](https://help.klaviyo.com/hc/en-us/articles/360025945671)

如果您是现有帐户并且在 Klaviyo 上有至少 30 天的发送历史记录，则无需重新预热。将生成的记录添加到 DNS 后，选择“验证”按钮开始验证过程。首次访问验证记录步骤时，预计会看到记录尚未经过验证。 ![验证.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723622898203)

查看出现的任何消息。您将看到以下消息之一：

- 如果活动存在冲突，您将看到一条通知，表明送达率可能会受到影响。为了避免任何冲突的错误，最佳做法是确保没有主动发送或计划很快发出的营销活动。最好的做法是（但不是必需）暂停流程和营销活动，直到应用并测试更改之后。 - 如果您的记录有效，您将看到一条成功消息。此成功消息可能表明您需要再次预热您的基础设施。请注意，这仅适用于全新的 Klaviyo 帐户或新注册的域名（过去 30 天内）。如果您是现有帐户并且在 Klaviyo 上有至少 30 天的发送历史记录，则无需重新预热。 - 如果您的记录无效，您将看到一条错误，指示哪些设置不正确。验证记录后，当您准备好开始在您的品牌域上发送时，请选择****应用域****。 DNS 记录在您的 DNS 设置中发布后，最长可能需要 48 小时才能更新。 Klaviyo 现在会将您的品牌发送域应用到您的帐户，并在完成后生成一条成功消息。您应该排除发件人地址中用于发送电子邮件的子域（例如 **@send.yourbusiness.com**）。如果它包含在您的发件人地址中，您将无法收到收件人对来自您的 Klaviyo 帐户的电子邮件的回复。相反，建议仅使用根域作为您的发件人地址（例如 **@yourbusiness.com**）。 ### 错误消息故障排除

如果由于某种原因无法应用该域，则会显示一条错误消息，指导您重试。我们建议您首先使用免费的在线 DNS 记录检查器来检查您的品牌发送域并尝试诊断问题。以下服务提供此快速检查：

- <https://dmarcian.com/dkim-inspector/>
- <https://www.whatsmydns.net/>
- <https://dnschecker.org/>

[了解有关品牌发送域故障排除的其他指导和提示](https://help.klaviyo.com/hc/en-us/articles/4417768780827)。如果使用上述工具之一无法解决问题，请联系我们的支持团队以获得进一步帮助。设置域后，当您返回 **域** 页面时，您将看到这些更改。您还将看到这些更改发生的日期以及有关如何在接下来的 2 到 4 周内预热发送基础设施的说明。 ## 温暖您的发送基础设施

如果您是新的合格 Klaviyo 帐户，开始使用品牌发送域或使用新注册的域（在过去 30 天内注册），则必须在设置品牌发送域后的前 2 到 4 周内[预热您的发送基础设施](https://help.klaviyo.com/hc/en-us/articles/360025945671)。温暖您的域名可以增强您的发件人声誉。根据您要带到 Klaviyo 的数据和您拥有的用例，您需要遵循适用于您的[预热或平台引入流程](https://help.klaviyo.com/hc/en-us/articles/360025945671-How-to-warm-your-sending-infrastruct)。迁移至品牌发送域的现有 Klaviyo 客户无需再次预热基础设施，只要您具备：

- 域名已注册至少 30 天并且
- 您已经使用该域名发送电子邮件（例如，您过去曾在之前的电子邮件服务提供商处使用过该域名，或者在您的发件人地址中使用过 Klaviyo）。 ## 发送域警报断开连接

当所需的 DNS 记录被删除时，品牌发送域将断开连接。在这些情况下，Klaviyo 会通知您，以便您可以修复必要的 DNS 记录。您将在 Klaviyo 的通知收件箱中收到警报。 ![](https://klaviyo.zendesk.com/hc/article_attachments/35380098109339)

只有具有配置品牌发送域所需的[权限](https://help.klaviyo.com/hc/en-us/articles/115005231648)的用户才会收到警报。 ## 结果

配置品牌发送域后，您的所有电子邮件（即营销和交易电子邮件）都将通过您的品牌域而不是 Klaviyo 的共享发送域发送。