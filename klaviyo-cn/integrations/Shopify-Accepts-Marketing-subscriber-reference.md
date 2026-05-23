---
id: "25184578360603"
title: "Shopify 接受营销订阅者参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/25184578360603-Shopify-Accepts-Marketing-subscriber-reference"
section: "Shopify troubleshooting"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:35Z"
language: "zh"
---
## 你将会学到

了解在 Klaviyo 于 2022 年 12 月更新此同步之前，您帐户中的订阅者如何从 Shopify 同步到 Klaviyo。

## 开始之前

2022 年 12 月 14 日，Klaviyo 发布了一项更新，更改了电子邮件订阅者从 Shopify 同步到 Klaviyo 的方式。此同步以前依赖于 Shopify 的 **接受营销** 标签，但现在，订阅者通过 Shopify 的订阅模型进行同步。

对于希望使用它的客户，此属性仍会同步到 Klaviyo，但它不再确定 Klaviyo 中的订阅状态，并且[自已被弃用] Shopify]（https://shopify.dev/changelog/removal-of-accepts-marketing-fields-in-admin-api-customer-resources#:~:text=As%20of%20API%20version%202024，emailMarketingConsent%20should%20be%20used%20。）。

如果您想了解 Klaviyo 的订阅者同步当前的功能，请前往[如何将 Shopify 电子邮件订阅者同步到 Klaviyo 列表](https://help.klaviyo.com/hc/en-us/articles/115005080667)。如果您想了解 2022 年 12 月之前同步的 Shopify 订阅者，请继续阅读。

## 订阅者之前如何从 Shopify 同步？

在 2022 年 12 月 14 日之前，Klaviyo 的 Shopify 订阅者同步依赖于 Shopify 的 **接受营销** 标签。

以下是该酒店如何出现在 Klaviyo 客户个人资料中的示例。

![Klaviyo 配置文件的信息部分，包括设置为 true 的“接受营销”属性](https://klaviyo.zendesk.com/hc/article_attachments/28715972898331)

在某些情况下，可能会导致现有客户将 **接受营销** 设置为 false，但他们仍然订阅了您的电子邮件列表：

- 如果客户当时签出并决定不接受电子邮件营销，但后来通过 Klaviyo 注册表单进行订阅，他们仍然会被添加到您的电子邮件列表中。
- 如果客户签出并接受电子邮件营销，他们将被添加到您的电子邮件列表中。如果他们再次查看，他们可能决定不再订阅，因为他们已经订阅了。根据您的结帐配置，Shopify 可能会将此视为不接受营销（**接受营销** = **错误**。）您可能不希望将此客户视为取消订阅。相反，您需要将该客户保留在您的电子邮件列表中。

此外，需要注意的是，将“接受营销”设置为“假”的现有客户不会自动被抑制。要了解有关抑制的更多信息，请查看我们的文章[了解抑制的电子邮件配置文件](https://help.klaviyo.com/hc/en-us/articles/115005246108)。

## 其他资源

- [Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407)
- [如何将 Shopify 电子邮件订阅者同步到 Klaviyo 列表](https://help.klaviyo.com/hc/en-us/articles/115005080667)