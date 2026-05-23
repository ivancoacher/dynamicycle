---
id: "1260807540249"
title: "如何为现有 Magento 2 集成设置 OAuth"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/1260807540249-How-to-set-up-OAuth-for-existing-Magento-2-integrations"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:27Z"
language: "zh"
---
## 概述

本指南将介绍如何将现有的 Magento 2 集成从 API 凭据身份验证更新到新的 OAuth 工作流程。如果您第一次需要[启用 Magento 2 集成](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348)，请访问此处的指南。如果您使用的是 Magento 2 版本 2.2.0 或更早版本，请按照本指南[手动启用 OAuth](https://help.klaviyo.com/hc/en-us/articles/4403350880411)。

## 设置 OAuth

登录您的 Magento 2 帐户。在这里，我们将启用 OAuth 将您的 Klaviyo 帐户安全地连接到 Magento 2 扩展。

从管理仪表板导航至****商店 > 配置****。单击****Klaviyo**** 并选择****设置 OAuth**** 选项卡。在 **名称** 字段中为您的集成指定一个容易记住的名称，稍后您需要通过该名称找到它。单击****保存配置****继续。

![OAUTHtab.png](https://klaviyo.zendesk.com/hc/article_attachments/28717987581723)

接下来，从左侧导航窗格中找到****系统****，然后从系统托盘中选择****集成****。

找到您在上面使用的名称的集成，然后单击****激活****。

![activateoauth.png](https://klaviyo.zendesk.com/hc/article_attachments/28717993386395)

激活集成将打开一个窗口，请求您批准对多个权限的访问。单击****允许****接受权限并重定向到 Klaviyo 以完成集成设置。

![oauthperms.png](https://klaviyo.zendesk.com/hc/article_attachments/28717993388315)

如果您尚未登录，请登录，或者确认您的帐户名正确并单击****集成。**** 这将更新显示的 Klaviyo 帐户中的 Magento 2 集成。如果您登录了多个 Klaviyo 帐户并且未显示正确的帐户，请注销任何其他会话。

![](https://klaviyo.zendesk.com/hc/article_attachments/28717993395739)

如果窗口自动关闭，则连接成功。您还可以通过在新的浏览器选项卡或窗口中打开您的 Klaviyo 帐户并选择 ****Integrations**** 选项卡进行确认。在集成列表中找到 Magento 2 - 单击它，您应该会看到如下所示的屏幕：

![](https://klaviyo.zendesk.com/hc/article_attachments/28717993399195)

如果您收到以下错误，请确保第一步中使用的 API 密钥与您当前登录的帐户相对应。

![apierror.png](https://klaviyo.zendesk.com/hc/article_attachments/28717993390235)

在 Magento 和 Klaviyo 之间建立连接时，如果您收到错误列表，则可以单击每个错误以了解有关原因的更多信息。
![oauthgenerror.png](https://klaviyo.zendesk.com/hc/article_attachments/28717993393563)