---
id: "360055457791"
title: "了解什么是品牌发送子域"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360055457791-Understanding-what-a-branded-sending-subdomain-is"
section: "Getting started with email deliverability"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-04-21T13:54:52Z"
language: "zh"
---
## 你将会学到

设置[品牌发送域](https://klaviyo.zendesk.com/hc/en-us/articles/115000357752)（也称为专用发送域）时，您需要选择关联的子域或前缀。在本文中，您将详细了解如何选择适合您业务的子域。

## 了解发送域前缀

发送域是您发送电子邮件的域，并将显示在您的电子邮件标头中。每个域都以一个子域开始。例如，如果您的发送域是 **send.helloworld.com**，则子域是 **send**。

您可以选择任何单词作为您的子域，只要它尚未在您的 DNS（域名系统）中使用即可。也就是说，您需要选择一个适合您的品牌和发送目的的词语。 “发送”是专用发送域最常见的前缀，也是我们在 Klaviyo 推荐的前缀，因为它通常不被 DNS 中的其他服务使用。我们将在下面的部分中深入探讨如何选择适合您的发送子域。

## 发送域名前缀最佳实践

在 Klaviyo 中设置专用发送域时，您需要在此过程中在 **发送域** 下添加子域。

![branded1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722596814107)

正如[上面](#h_01EW0NPYD4BBR1EYE6VQS0E1W9)所述，从技术上讲，您可以选择任何您想要的单词作为子域。选择子域时请记住以下最佳实践：

- ****您的 DNS 中不能有重复的子域****
  当您创建发送域时，它就会成为自己唯一的网址。因此，您只能在 DNS 中使用子域一次，因为不能有多个页面具有相同的地址。您可以在 DNS 注册表中检查给定的子域是否可用。
  然而，在 Klaviyo 中，您可以为多个帐户使用相同的子域，因为它将全部归属于您的 DNS 中的该域。例如，如果您管理给定品牌的美国和英国帐户，则可以为这两个帐户使用相同的发送域。如果您在多个帐户中使用一个发送域，则 [CNAME 或 NS 记录](https://help.klaviyo.com/hc/en-us/articles/360039295051-Deliverability-Glossary#c2) 应相同，但每个帐户将具有不同的 TXT 值，并且每个 TXT 值都需要添加到 DNS 记录中。
- ****您的子域应该建议发送电子邮件****
  尽管您可以为子域选择任何单词，但我们建议您选择暗示电子邮件发送的子域。您的 DNS 的其他用户可以轻松识别您的子域；这将减少其他用户错误删除或编辑它的机会。当您将来在任何时候查看您的 DNS 记录时，您都会看到这个子域，并且很容易知道它是用于专用发送的。

  您将希望轻松确定哪个子域指定您的发送域。例如，**send.helloworld.com**、**emails.helloworld.com** 或 **newsletter.helloworld.com** 等子域都可以工作。

我们建议您不要使用 **mail** 作为子域，因为它通常是为收件箱设置保留的并且已在 DNS 中使用。

简而言之，您可以选择任何单词作为您的子域，但最佳实践是选择适合您域的用途且尚未使用的单词。有关创建品牌发送域的更多信息，请参阅[如何设置品牌发送域](https://klaviyo.zendesk.com/hc/en-us/articles/115000357752)。

## 其他资源

- [如何设置品牌发送域](https://klaviyo.zendesk.com/hc/en-us/articles/115000357752)
- [如何设置专用点击跟踪](https://klaviyo.zendesk.com/hc/en-us/articles/360001550572)
- [电子邮件传递能力入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005247008)