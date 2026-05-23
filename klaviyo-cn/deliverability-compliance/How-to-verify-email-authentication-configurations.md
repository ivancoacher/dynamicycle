---
id: "21330028699419"
title: "如何验证电子邮件身份验证配置"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/21330028699419-How-to-verify-email-authentication-configurations"
section: "Monitor deliverability and metrics"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:33Z"
language: "zh"
---
## 你将会学到

了解如何使用 SPF、DKIM 和 DMARC 记录验证您的电子邮件是否已成功通过身份验证。 [Google 和 Yahoo](https://www.klaviyo.com/blog/gmail-update) 宣布了新的发件人要求，计划于 2024 年 2 月开始实施。对于每天发送超过 5000 封电子邮件的品牌来说，设置 DMARC 身份验证将是成功登陆 Gmail 和 Yahoo 收件箱的关键要求。 [Microsoft Outlook](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730) 也将从 2025 年 5 月开始强制执行这些要求。## 电子邮件身份验证

“电子邮件身份验证”是指允许验证电子邮件发件人身份的技术标准。最常用的电子邮件身份验证标准是 SPF、DKIM 和 DMARC。邮件服务器使用这些身份验证协议来验证传入的电子邮件是否来自合法发件人，从而保护您的品牌和客户免受恶意行为者的侵害。除了防止网络钓鱼和欺骗尝试之外，实施这些协议还可以帮助提高投递能力，因为邮箱提供商将能够确认发件人的身份。在开始之前，了解[电子邮件身份验证](https://help.klaviyo.com/hc/en-us/articles/4402601857307) 并设置 DMARC。 ## 使用电子邮件标头验证身份验证

### 关于电子邮件标头

电子邮件标头包含有关电子邮件及其所采用的网络路径的元数据。这包括发件人地址、主题行、收件人和关键身份验证详细信息等信息。您可以使用您的品牌发送的电子邮件标头中的身份验证信息来验证 SPF、DKIM 和 DMARC 是否通过。了解如何在不同的收件箱提供商上[获取完整的电子邮件标头](https://help.klaviyo.com/hc/en-us/articles/360002117891)。 ### 标题摘要

某些收件箱提供商（例如 Gmail）可能会在电子邮件标头中提供关键身份验证信息的摘要。这可能看起来像这样：

![Gmail 标头摘要](https://klaviyo.zendesk.com/hc/article_attachments/28711702459035)

### 完整标题

在完整的电子邮件标头中，关键身份验证信息可能如下所示：

````
发送至：email@klaviyo.com
收到：2002 年之前：a59:9a44:0:b0:437:660e:55f2，SMTP ID 为 a4csp4934052vqp；
    2023 年 12 月 10 日星期日 16:03:01 -0800（太平洋标准时间）
身份验证结果：mx.google.com；
    dkim=pass header.i=@klaviyo.com header.s=s1 header.b=kBByyR4j;
    spf=pass（google.com：域名
ounces+27486840-770f-email=klaviyo.com@send.klaviyo.com 指定 000.000.00.000
作为允许的发件人）
smtp.mailfrom="bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com";
    dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=klaviyo.com
````

您看到的电子邮件标头可能因收件箱提供商而异，但关键身份验证信息应位于名为 **身份验证结果** 的部分中。 ### 防晒指数

发件人策略框架 (SPF) 是一种电子邮件身份验证方法，旨在检测电子邮件传送过程中的伪造发件人地址。 SPF 允许接收邮件服务器验证来自特定域的电子邮件是否是通过该域管理员授权的 IP 地址发送的。如果您的收件箱提供商有标头摘要，您应该会看到 SPF 以及通过或失败值以及发送电子邮件所通过的 IP 地址。 ![SPF 通过在标题摘要中突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28711731439131)

在完整的电子邮件标头中，您可以看到 SPF 记录正在通过 (spf=pass)，表示允许用于发送电子邮件的 IP 地址（即 000.000.00.000）发送到 send.klaviyo.com 发送域（即 SPF 域）。 ````
身份验证结果：mx.google.com；
     dkim=pass header.i=@klaviyo.com header.s=s1 header.b=kBByyR4j;
     spf=pass（google.com：域名
     ounces+27486840-770f-email=klaviyo.com@send.klaviyo.com 指定 000.000.00.000
作为允许的发件人）
smtp.mailfrom="bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com";
     dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=klaviyo.com
````

### DKIM

域名密钥识别邮件 (DKIM) 充当添加到电子邮件标头的数字签名，以进一步验证发件人的身份。 接收电子邮件服务器将验证 DKIM 签名是否与关联的发送域的签名匹配。如果您的收件箱提供商有标头摘要，您应该会看到 DKIM 以及发送电子邮件的域的通过或失败值。 ![DKIM 通行证在标题摘要中突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28711702472603)

在完整的电子邮件标头中，您可以看到 DKIM 记录正在传递 (dkim=pass)，这表明 DKIM 设置的数字签名与关联的发送域的数字签名匹配。 ````
身份验证结果：mx.google.com；
     dkim=pass header.i=@klaviyo.com header.s=s1 header.b=kBByyR4j;
     spf=pass（google.com：域名
ounces+27486840-770f-email=klaviyo.com@send.klaviyo.com 指定 000.000.00.000
作为允许的发件人） smtp.mailfrom="bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com"；
     dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=klaviyo.com
````

### DMARC

DMARC 代表基于域的消息身份验证、报告和一致性。它是一种使用 SPF 和 DKIM 来确定电子邮件真实性的协议，使域所有者能够保护其域免遭未经授权的使用。 DMARC 向接收服务器提供有关如何处理传入邮件的说明。为了投递，邮件需要根据 DMARC 策略设置的要求通过 DKIM 和 SPF 对齐检查。未通过 DMARC 检查的邮件可以被允许、拒绝或放入垃圾邮件文件夹。如果您的收件箱提供商有标头摘要，您应该会看到 DMARC 以及通过或失败值。 ![标题摘要中突出显示 DMARC 通行证](https://klaviyo.zendesk.com/hc/article_attachments/28711702474779)

在完整的电子邮件标头中，您可以看到 DMARC 正在通过 (dmarc=pass)，表示电子邮件通过了发送域的 DMARC 检查。此外，您还可以查看在发送域上设置的特定 DMARC 策略（即 p=reject）。 ````
身份验证结果：mx.google.com；
     dkim=pass header.i=@klaviyo.com header.s=s1 header.b=kBByyR4j;
     spf=pass（google.com：域名
ounces+27486840-770f-email=klaviyo.com@send.klaviyo.com 指定 000.000.00.000
作为允许的发件人） smtp.mailfrom="bounces+27486840-770f-email=klaviyo.com@send.klaviyo.com"；
     dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=klaviyo.com
````

## 使用第三方工具验证身份验证

验证 DMARC 策略是否已成功发布的另一种方法是使用第三方工具，例如 EasyDMARC 提供的 DMARC 检查器。使用此工具，您只需输入品牌的根域，如果设置了 DMARC 记录，则会返回该记录。 ![在 EasyDMARC 上查找 klaviyo.com 域的示例](https://klaviyo.zendesk.com/hc/article_attachments/28711702480155)

如果您的 DMARC 策略设置为 **p=none，** 在使用 EasyDMARC 时，**状态**将显示为 **警告**。 **警告** 与 **p=none** 策略一起出现，因为它不能保护您的域免遭欺骗，并且即使发送域和友好发件人地址域之间存在不一致，也允许电子邮件到达收件人的主收件箱。 EasyDMARC 上的 **警告** 和 **有效** 状态表明您品牌的 DMARC 政策满足 Gmail 和 Yahoo 发件人要求。您可以忽略 **EasyDMARC 报告** 结果，除非您使用 EasyDMARC 的报告服务。 ## 其他资源

[了解电子邮件身份验证](https://help.klaviyo.com/hc/en-us/articles/4402601857307)

[如何设置品牌发送域](https://help.klaviyo.com/hc/en-us/articles/115000357752)