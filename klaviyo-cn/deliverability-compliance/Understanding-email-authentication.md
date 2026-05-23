---
id: "4402601857307"
title: "了解电子邮件身份验证"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4402601857307-Understanding-email-authentication"
section: "Getting started with email deliverability"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: "zh"
---
## 你将会学到

了解电子邮件身份验证协议，这些协议用于建立发件人信誉、验证电子邮件是否来自合法发件人以及防止电子邮件滥用。 [Google 和 Yahoo](https://www.klaviyo.com/blog/gmail-update) 宣布了新的发件人要求，计划于 2024 年 2 月开始实施。对于每天发送超过 5000 封电子邮件的品牌来说，设置 DMARC 身份验证将是成功登陆 Gmail 和 Yahoo 收件箱的关键要求。 [Microsoft Outlook](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) 也将从 2025 年 5 月开始强制执行这些要求。## 关于电子邮件身份验证

“电子邮件身份验证”是指允许验证电子邮件发件人身份的技术标准。最常用的电子邮件身份验证标准是 SPF、DKIM 和 DMARC。邮件服务器使用这些身份验证协议来验证传入的电子邮件是否来自合法发件人，从而保护您的品牌和客户免受恶意行为者的侵害。除了防止网络钓鱼和欺骗尝试之外，实施这些协议还可以帮助提高投递能力，因为邮箱提供商将能够确认发件人的身份。 ## 防晒指数

发件人策略框架 (SPF) 是一种电子邮件身份验证方法，旨在检测电子邮件传送过程中的伪造发件人地址。 SPF 允许接收邮件服务器验证来自特定域的电子邮件是否是通过该域管理员授权的 IP 地址发送的。当电子邮件从未通过 SPF 允许的 IP 地址发送时，接收邮件服务器可能会拒绝该电子邮件，或将其从主收件箱转移出去。如果没有 SPF 记录，您将无法使用发送域对 IP 进行身份验证，从而使恶意行为者可以轻松冒充您的品牌。在 Klaviyo 的共享发送域上，电子邮件会自动通过 SPF 进行身份验证。如果您在 Klaviyo 中使用自己的[品牌发送域](https://help.klaviyo.com/hc/en-us/articles/115000357752)，则必要的 SPF 记录将通过设置期间添加的 CNAME 或 NS 记录自动添加。 ## DKIM

域名密钥识别邮件 (DKIM) 充当添加到电子邮件标头的数字签名，以进一步验证发件人的身份。接收电子邮件服务器将验证 DKIM 签名是否与关联的发送域的签名匹配。由于 DKIM 签名存在于电子邮件的标头中，因此在转发电子邮件时它也会保留下来，这与 SPF 身份验证不同。在 Klaviyo 的共享发送域上，电子邮件会通过 DKIM 自动进行身份验证。如果您在 Klaviyo 中使用自己的[品牌发送域](https://help.klaviyo.com/hc/en-us/articles/115000357752)，则会通过在设置过程中添加的 CNAME 或 NS 记录自动添加必要的 DKIM 记录。 ## DMARC

DMARC 代表基于域的消息身份验证、报告和一致性。它是一种使用 SPF 和 DKIM 来确定电子邮件真实性的协议，使域所有者能够保护其域免遭未经授权的使用。 ![](https://fast.wistia.com/embed/medias/1xamzihlg0/swatch)

DMARC 向接收服务器提供有关如何处理传入邮件的说明。为了投递，邮件需要根据 DMARC 策略设置的要求通过 DKIM 和 SPF 对齐检查。未通过 DMARC 检查的邮件可以被允许、拒绝或放入垃圾邮件文件夹。在您的域上实施 DMARC 策略可以帮助保护您免受欺骗，限制您的品牌和收件人接触潜在的欺诈性和有害消息。 ****DMARC 政策示例****

DMARC 是一种电子邮件身份验证、策略和报告协议，它会影响从您的品牌发送的任何电子邮件，而不仅仅是 Klaviyo。请注意，与您的 IT 团队或第三方专业人士合作实施最适合您品牌需求的 DMARC 政策非常重要。以下示例展示了简单的 DMARC 记录的外观以及不同的记录如何影响电子邮件传送。 `v=DMARC1； p=无； rua=mailto:dmarc-reports@yourbrand.com`

在 DMARC 记录中省略 **sp** 标记是很常见的，在这种情况下，**sp** 标记默认为 **p** 标记的值。 虽然 DMARC 策略可以拥有许多具有不同功能的标签，但对于 Klaviyo 和您的电子邮件营销而言，**p** 和 **sp** 策略标签是最重要的。这两个标签的值告诉收件箱提供者当对齐检查失败时他们应该如何反应。在发件人电子邮件地址中使用时，**p** 标签适用于根域（例如 **@yourbrand.com**），而 **sp** 标签适用于[子域](https://help.klaviyo.com/hc/en-us/articles/360055457791)（例如**@shop.yourbrand.com**）。同时，示例中的 **rua** 标记确定 DMARC 报告将邮寄到的收件箱。建议使用此标签，但不是必需的。如果您打算使用 **rua** 标签，请务必将上面的占位符电子邮件地址（即 [**dmarc-reports@yourbrand.com**](mailto:dmarc-reports@yourbrand.com)）替换为准备接收 DMARC 报告的收件箱。 |  |  |
| --- | --- |
| ****p/sp 标签的值**** | ****收件箱提供商如何处理未对齐的电子邮件**** |
| p=无 |尽管存在错位，但仍可以正常接受电子邮件。 |
| p=隔离|接受电子邮件但显示警告并将电子邮件放入垃圾邮件中。 |
| p=拒绝 |阻止未对齐的电子邮件。 |

DMARC 策略作为 TXT 记录放置在域的 DNS 控制面板上，但需要遵循特定的语法规则。 ### **p** 和 **sp** 标签如何影响 Klaviyo 上的发送

在共享发送域上发送时，电子邮件的发件人地址（例如，**marketing@yourbrand.com**）与电子邮件的实际发送域（例如，**ksdn.klaviyomail.com**）之间始终存在不一致。 Klaviyo 自己的共享发送域将 DMARC 策略设置为 **p=none**，这样您的电子邮件就可以到达客户收件箱，尽管存在错位。当您使用品牌发送域（您的品牌拥有的域）时，发件人地址域与发送域一致。因此，DMARC 检查将通过。 ### **rua** 标签和 DMARC 报告

DMARC 记录中的 **rua** 标签允许关联的电子邮件地址接收 .xml 格式的 DMARC 报告。这些报告难以解读且繁琐，因此，如果您计划使用 **rua** 标签进行 DMARC 报告，Klaviyo 建议与 DMARC 服务提供商合作。这些提供商帮助处理 .xml DMARC 报告并呈现它们，以便您的品牌可以更轻松地收集见解。在 **rua** 标签中设置的用于接收 DMARC 报告的电子邮件地址的域必须与 DMARC 记录的根域匹配。要通过不同的域接收 DMARC 报告，您需要将域所有者提供的 TXT 记录添加到您品牌的根域。 ****DMARC 报告示例****

[“示例](https://www.napkin.io/api/embed/7121123fc84f4509)

Klaviyo 推荐的 DMARC 提供商的一些示例包括：

- [Valimail](https://www.valimail.com/google-and-yahoo-compliance-check/?utm_source=klaviyo&utm_medium=partner%20生成)
- [EasyDMARC](https://easydmarc.com/)
- [Dmarcian](https://dmarcian.com/)

## 配置邮件验证

使用 Klaviyo 发送电子邮件时，您不需要添加自己的 SPF 和 DKIM 记录。如果您在 Klaviyo 的共享发送域上发送，则已设置必要的记录以通过身份验证。通过品牌发送域（也称为专用发送域），在设置过程中添加的 Klaviyo NS 或 CNAME 记录会自动启用 DKIM 和 SPF 身份验证。但是，设置 DMARC 是在 Klaviyo 外部与您的 DNS 提供商一起执行的外部过程。您设置的 DMARC 策略确定如何处理 SPF 和 DKIM 身份验证失败的邮件。 DMARC 策略可以隔离未经身份验证的电子邮件并将其发送到收件人的垃圾邮件文件夹，允许它们在未对齐的情况下进入收件箱，或者完全拒绝它们并阻止发送给收件人。如果您的品牌目前没有 DMARC 策略，配置 **p=none** 是满足 [Gmail 和 Yahoo 的要求](https://www.klaviyo.com/blog/gmail-update) 的良好第一步。但是，如果您想配置更严格的 DMARC 策略以防止欺骗并允许报告对齐失败，Klaviyo 强烈建议您与 IT 团队或第 3 方专业人员合作。 Klaviyo 无法代表您实施 DMARC，因为该流程会影响您的品牌安全以及向 Klaviyo 之外发送的情况。此外，实施 DMARC 需要访问和控制您品牌的 DNS 设置。 Klaviyo 无法为您的品牌进行此类 DNS 更改，以保护您的安全和域名所有权。 ## 在您的 DNS 中设置 DMARC

设置 DMARC 是在 DNS 提供商的 Klaviyo 外部执行的过程。有大量不同的 DNS 提供商，但以下步骤描述了 DMARC 的一般实施方式。要设置 DMARC，域的网络管理员需要登录域的 DNS 设置以添加 DMARC 记录，如下所示。登录到您的 DNS 提供商后，使用以下信息创建新记录。 - ****类型****：TXT
- ****主机****：\_dmarc
- **值****：v=DMARC1； p=无

  **rua** 标签是用于 DMARC 报告的可选标签。如果计划使用报告并希望将其接收到收件箱，则 DMARC 记录值为：`v=DMARC1; p=无； rua=mailto:email@yourbrand.com`

  创建新记录的字段、接口和流程的名称可能因 DNS 提供商而异。 DNS 提供商的一些示例包括 GoDaddy 和 Namecheap，但还有许多其他提供商。有关如何为您的域设置 DMARC 的进一步说明，我们建议您使用以下资源和服务，或者联系您的 DNS 提供商。 - [了解 DMARC 如何保护您的域名声誉](https://academy.klaviyo.com/understand-how-dmarc-protects-your-domain-reputation/1832471)
- [MXToolBox：如何设置 DMARC](https://mxtoolbox.com/dmarc/details/how-to-setup-dmarc)
- [DMARCian：DMARC 入门](https://dmarcian.com/getting-started-with-dmarc/)
- [Valimail](https://www.valimail.com/)

## 使您的 Klaviyo 电子邮件符合 DMARC

为了符合 DMARC，您需要将品牌发送域连接到您的帐户，该帐户与您的友好发件人电子邮件地址（即您的发件人地址）中的根域相匹配。例如，如果您使用 **sales@yourbrand.com** 作为发件人地址发送电子邮件，并且 **yourbrand.com** 受 DMARC 保护，则您的帐户将需要使用 **send.yourbrand.com** 等品牌发送域来满足 DMARC 要求。了解如何[更新您的发件人电子邮件地址](https://help.klaviyo.com/hc/en-us/articles/360024994912)，使其与您的品牌发送域保持一致。 ### 内部收件人

当使用共享域向内部收件人发送电子邮件时，当收件人的电子邮件地址与发件人地址域匹配时，收件箱提供商可能会显示警告消息并将电子邮件放入垃圾邮件中。例如，在 Gmail 上：

![gmailwarningjpg.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713383110683)

虽然这只会影响电子邮件地址与您自己的发件人地址域相匹配的用户，但您可以设置品牌发送域来防止这种情况发生。如果您在个人非企业收件箱中看到此警告，则可能是 DMARC 失败的结果。为了符合 DMARC，您需要将品牌发送域连接到与您的发件人电子邮件地址（即您的发件人地址）中的域相匹配的帐户。 ## 验证您的电子邮件身份验证配置

要验证记录是否已成功发布，您可以将您的域名输入到 [EasyDMARC](https://easydmarc.com/tools/dmarc-lookup) 提供的 DMARC 检查器中。使用此工具，**警告**或**有效**状态符合 Gmail 和 Yahoo 的发件人要求。 ![easydmarcklaviyo.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28713383120027)

或者，您可以使用您的品牌发送的电子邮件标头来验证您的电子邮件身份验证设置是否正确。电子邮件标头包含有关电子邮件及其所采用的网络路径的元数据。这包括发件人地址、主题行、收件人等信息以及关键身份验证详细信息（例如 SPF、DKIM 和 DMARC 是否通过）。了解如何[使用电子邮件标头验证电子邮件身份验证配置。](https://help.klaviyo.com/hc/en-us/articles/21330028699419)

![Gmail 中的标头摘要](https://klaviyo.zendesk.com/hc/article_attachments/28713338438811)

## 转向更安全的 DMARC 策略

虽然 **p=none** 的 DMARC 策略足以满足 Gmail 和 Yahoo 设置的初始发件人要求，但转向更安全的策略可以更好地保护您的企业免受恶意行为者的侵害。 ### 更安全策略的好处

使用 **p=quarantine** 或 **p=reject** 的主要好处是，它们可以防止未对齐的电子邮件（即从与您的品牌根域不匹配的发送域发送的电子邮件）进入收件人的主收件箱。 **P=none** 在从未对齐的域发送电子邮件的情况下不会影响收件箱放置，因此收件人仍然可以收到来自试图冒充您品牌的恶意行为者的电子邮件。如果用户最终查看了看似从您的品牌发送的欺骗性电子邮件，这可能会导致客户对您品牌的电子邮件的信任受到影响。同时，当使用 **p=quarantine** 或 **p=reject** 策略时，未对齐的电子邮件将被阻止或发送到收件人的垃圾邮件文件夹。收件箱提供商会知道避免向收件人显示电子邮件，并且欺骗性电子邮件不会进入主收件箱。 ### 其他考虑因素

请务必注意，DMARC 适用于从您的品牌发送的任何电子邮件，包括在 Klaviyo 之外发送的电子邮件。通过 **p=none** 策略，您的发送不会受到影响，因为电子邮件仍会到达主收件箱。但是，如果您的域与企业的整个电子邮件发送基础设施和用例不一致，则更严格的 DMARC 策略可能会导致电子邮件无法送达。因此，Klaviyo 建议与您的 IT 团队或 DMARC 服务提供商合作，实施最适合您品牌需求的策略。