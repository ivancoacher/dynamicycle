---
id: "360039881992"
title: "对电子邮件中的 Instagram 网络提要进行故障排除"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360039881992-Troubleshooting-your-Instagram-web-feed-in-emails"
section: "Meta Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-17T00:34:28Z"
language: "zh"
---
## 你将会学到

了解如何对您的 Instagram 网络提要在您的电子邮件中无法正常工作进行故障排除，这可能是由于 Klaviyo 在检索您的提要内容时出现问题。要确定原因，我们建议首先尝试测试您的 Feed。

## 测试你的 feed

如果您想测试或预览现有的 Instagram Feed，请通过执行以下操作导航至 Klaviyo 帐户的“数据 Feed”部分

1. 单击左下角您的帐户名称。
2. 导航至****设置 > 其他 > 网络源****。
3. 单击引用 Instagram 的源。
4. 在右上角，单击****预览。****

如果您能够预览 Feed 内容，则意味着您的 Feed 目前设置正确并且按预期工作。确保您的电子邮件中正确引用了您的 Feed。

如果您看到错误消息，这可能意味着您的 Feed URL 设置不正确或所需的访问权限已过期。如果您发现错误并认为您的 Feed 可能依赖于 Instagram 的旧版 API，请参阅以下部分。

## 您的 Feed 是否依赖 Instagram 旧版 API？

自 2020 年 6 月 29 日起，Instagram 将弃用其旧版 API。 Instagram 用户和第三方应用程序通常使用此 API 来提取 Instagram 内容并生成最近帖子的提要。

如果您的 Instagram 网络提要依赖于此旧版 API，或依赖于使用 Instagram 旧版 API 构建的第三方应用程序，则这些提要将不再起作用。不幸的是，由于该 API 由 Instagram 管理，因此 Klaviyo 无法控制。

首先，从 [数据源部分](https://www.klaviyo.com/feeds) 前往您的 Instagram 网络源。在这里，您将找到任何可能设置为从您的 Instagram 帐户提取内容的 Web Feed。

## 如果您的 Feed 依赖于 Instagram 旧版 API，该怎么办

#### ****如果您的 Feed 直接引用 api.instagram.com****

您需要探索使用 Instagram 的新 [基本显示 API](https://developers.facebook.com/docs/instagram-basic-display-api)（这需要您定期刷新您的 [访问令牌](https://developers.facebook.com/docs/instagram-basic-display-api/overview#instagram-user-access-tokens)）或 [RSS Feed 生成器](https://rss.app/) 直接从 Instagram 提取内容帐户。 [查看有关将 Instagram 内容添加到电子邮件的分步说明。](https://help.klaviyo.com/hc/en-us/articles/360004384031-Using-Instagram-Content-in-Campaign-Emails)

您也可以寻找支持为您生成 Instagram Feed 的第三方应用程序，例如 [Klaviyo 技术合作伙伴 Foursixty](http://foursixty.com/?utm_source=partners&utm_medium=blog&utm_campaign=Klaviyo)。

#### ****如果您使用第三方应用程序来生成提要****

联系您正在使用的服务并按照他们的说明进行操作，以确保您的 Feed 在可能的情况下保持活动状态。

## 使用 Instagram 网络提要的替代方案

如果实时更新的 Instagram feed 对您来说不是必需的，但不是最常青的选择，您可以将 Instagram 的静态图像添加到您的消息中。 如果您无法直接从 Instagram 帐户生成内容提要，建议您这样做。如需了解更多信息，请查看我们关于[在模板中使用图像]的文章(https://help.klaviyo.com/hc/en-us/articles/115000108632)。

## 其他资源

- [如何在活动电子邮件中使用 Instagram 内容](https://help.klaviyo.com/hc/en-us/articles/360004384031-Using-Instagram-Content-in-Campaign-Emails)
- [元广告入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005082127)