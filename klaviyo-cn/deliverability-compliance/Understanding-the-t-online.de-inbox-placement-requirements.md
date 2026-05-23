---
id: "1260804570090"
title: "了解 t-online.de 收件箱放置要求"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/1260804570090-Understanding-the-t-online-de-inbox-placement-requirements"
section: "Monitor deliverability and metrics"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:26Z"
language: "zh"
---
## 你将会学到

了解如何满足 t-online.de 的交付要求。 T-online.de 是一家收件箱提供商，主要由对交付有独特要求的德国订户使用。因此，您可能会看到来自该提供商的退回邮件增加，从而降低了您联系这些德国收件人的能力。如果您发现与 t-online.de 要求无关的跳出率上升，或者正在寻找有关此主题的其他指导，请参阅我们的关于[如何降低跳出率]的指南(https://klaviyo.zendesk.com/hc/en-us/articles/360057036052)。 ## 先决条件

在开始之前，请检查您是否已经在 Klaviyo 中创建了专用发送域。 1. 要查看您的帐户中是否已建立此功能，请单击右上角的帐户下拉列表，然后选择****设置****。 2. 然后，导航至****电子邮件 > 域****。在这里，您将看到有关您已建立的域的信息，或者您将看到入门信息。 3. 如果您需要创建专用发送域，请单击****开始****，然后按照我们关于[设置专用发送域]的指南中概述的说明进行操作。(https://help.klaviyo.com/hc/en-us/articles/115000357752)
4. 然后，继续执行本文中的下一步，以与 t-online.de 最佳实践保持一致。 ## t-online.de 交付要求

t-online.de 需要满足以下要求才能覆盖所有使用其收件箱服务的订阅者：

- 为您的列表启用双重选择加入
- 您的发件人策略框架 (SPF)、域名密钥识别邮件 (DKIM)、反向 DNS（rDNS；即您的专用 IP 域）以及 Klaviyo 中的发件人电子邮件域（每封电子邮件发送的发件人地址）必须全部对齐

在接下来的几节中，我们将深入探讨其中的每一项要求。 ## 启用双重选择加入

默认情况下，所有 Klaviyo 帐户中的列表都设置为双重选择加入，我们强烈建议您保持启用此设置，以避免 t-online.de 阻止您的电子邮件。双重选择加入是新订阅者在添加到您的列表之前必须通过电子邮件确认其订阅的过程。有关更多信息，请参阅我们的[有关双重选择加入流程的指南。](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108)

## 对齐您的发件人身份

t-online.de 收件箱放置的下一个要求是在所有以下发件人识别工具中调整您的域：

- ****发件人策略框架 (SPF)****
  SPF 域将是您的专用发送域，设置专用发送将自动执行此身份验证措施。 - ****域名密钥识别邮件 (DKIM)****
  DKIM 域也将使用与上述相同的专用发送域来建立。 - ****反向 DNS (rDNS)****
  当您获得专用 IP 地址时，rDNS 域就会建立。 - ****发件人电子邮件地址****
  这是您的发件人地址，可以针对每个营销活动和流程电子邮件进行调整。每个根域都必须彼此完全匹配，以便您的电子邮件到达 t-online.de 收件箱。例如，您在 Klaviyo 中的专用发送域将如下所示：**send.helloworld.com**。但是，如果您从 **personalemail@email.com** 向订阅者发送电子邮件，则您的邮件将被阻止到达 t-online.de 收件箱，因为您的发件人电子邮件地址与您的专用发送域不完全匹配。下表提供了根域何时对齐（t-online.de 将接受）和何时不对齐（t-online.de 将阻止到达收件箱）的示例。 |  |  |  |
| --- | --- | --- |
|  | ****根域对齐**** | ****根域**** ******不要***** ****对齐**** |
| ****专用发送域**** |发送@****helloworld.com**** |发送@****helloworld.com**** |
| ****发件人电子邮件地址（发件人地址）**** |示例@****helloworld.com**** |示例@****helloearth.com**** |
| ****rDNS 域名（用于您的专用 IP）**** | XXX.send.****helloworld.com**** | XXX.send.****helloworld.com**** | XXX.send.****helloearth.co.uk**** | XXX.send.****helloearth.co.uk**** |

至关重要的是，当您构建任何活动和流程时，请确保您的发件人电子邮件地址直接匹配您的专用发送域和专用 IP rDNS 域。对于营销活动和流程，您可以在标有“**发件人电子邮件地址**”的框中编辑发件人地址，如下所示。您还可以按照[本指南](https://klaviyo.zendesk.com/hc/en-us/articles/360024994912)中的说明在帐户设置中编辑默认发件人地址。 ![在活动编辑器内，包含用于设置发件人姓名、电子邮件地址、主题和预览文本的字段](https://klaviyo.zendesk.com/hc/article_attachments/28720658999963)

如果遵循这些最佳实践后，您发送到 t-online.de 的电子邮件继续被退回，请查看 [t-online.de postmaster 页面](https://postmaster.t-online.de/index.en.html)，以确保您当前的发送习惯符合他们的建议。 ## 其他资源

- [如何设置专用发送域](https://klaviyo.zendesk.com/hc/en-us/articles/115000357752)
- [如何选择专用发送的子域](https://klaviyo.zendesk.com/hc/en-us/articles/360055457791)
- [了解 Klaviyo 中的退回电子邮件](https://klaviyo.zendesk.com/hc/en-us/articles/115005250408)