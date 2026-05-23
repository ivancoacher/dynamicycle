---
id: "17649677926299"
title: "了解短信缩短链接的差异"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/17649677926299-Understanding-the-difference-in-SMS-shortened-links"
section: "SMS deliverability best practices"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: "zh"
---
## 你将会学到

了解各种类型的 SMS 短链接之间的差异：默认 Klaviyo 链接、品牌 Klaviyo 链接和品牌自定义链接。 ## 开始之前

Klaviyo 中有 3 种可用的 SMS 短链接类型：

- Klaviyo 链接
- 品牌 Klaviyo 链接
- 品牌定制链接

请注意，品牌 Klaviyo 链接仅在发送后 90 天内有效。如果收件人在 90 天后点击链接，该链接将不起作用。下表显示了名为“James Black”的公司的这些链接可能是什么样子的示例。

|  |  |
| --- | --- |
| ****链接类型**** | ****示例**** |
|克拉维约链接 | klv3.io/382aNpW5 |
|品牌 Klaviyo 链接 | jblck.klv3.io/382aNpW5 |
|品牌定制链接| sms.jamesblack.com/382aNpW5 | sms.jamesblack.com/382aNpW5

Klaviyo 无法跟踪来自第三方的缩短链接。如果您没有使用 Klaviyo 缩短链接（即禁用 **自动缩短链接** 设置），则您无法跟踪或查看短信产生的点击次数、转化次数或收入。要向消息添加缩短的链接，只需将所需的链接粘贴到 **消息内容** 框中，并且不要取消选中标记为 **自动缩短链接** 的框。 ![Klaviyo 缩短链接示例](https://klaviyo.zendesk.com/hc/article_attachments/28711730648347)

## 品牌 Klaviyo 链接与品牌自定义链接

使用品牌子域或域的主要优点是链接显示它来自您的企业。 ****品牌****

子域名就像一个品牌前缀。它在开头显示您的品牌名称，后面是看起来像 Klaviyo 中的正常缩短链接的内容。例如：

- Klaviyo 链接：[klv3.io/382aNpW5](http://klv3.io/382aNpW5)
- 品牌 Klaviyo 链接：[jblck.klv3.io/382aNpW5](http://jblck.klv3.io/382aNpW5)

品牌自定义链接意味着您的短信中的链接看起来与您网站的任何其他链接一样。唯一的区别是它们比正常的短，没有显示它们链接到的特定页面。 - 普通网站链接：JamesBlack.com/catalog/signed-jerseys
- 品牌域名：sms.jamesblack.com/xxxx

****发件人信誉****

通过品牌自定义链接，您可以更好地控制特定的送达率和发件人声誉。这些 URL 具有自己的域，因此具有各自的发件人信誉。常规和品牌 Klaviyo 链接都使用共享域。一般来说，这不会对短信发送能力产生太大影响；但是，如果您对您的送达能力或短信发送者声誉有疑虑，建议您请求品牌自定义链接。 ****通用链接和应用程序链接****

[通用链接和应用程序链接](https://klaviyo.zendesk.com/hc/en-us/articles/41701832186523-How-to-set-up-iOS-universal-links-and-Android-App-Links) 仅在您有品牌自定义链接时适用于短信。这些链接会将您的客户引导至您的移动应用程序中的内容，或者如果未安装该应用程序，则引导至您网站上的相同内容。在电子邮件和短信中使用这些链接可以让您在所有营销渠道中使用一致的 URL，同时为您的客户（无论他们使用什么设备）打造无缝体验。 ****字符数****

品牌 Klaviyo 链接始终比默认 Klaviyo URL 长，因为品牌链接包含额外字符以及完整的 Klaviyo URL。当谈到品牌定制链接与品牌 Klaviyo 链接时，这取决于您使用的内容。让我们用上面詹姆斯·布莱克的例子来看看。 - 品牌自定义链接包含更多字符的示例
  - 自定义：[sms.jamesblack.com](http://sms.jamesblack.com)（18 个字符）
  - Klaviyo：[jblk.klv3.io](http://jblk.klv3.io)（12 个字符）
- 品牌 Klaviyo 和自定义链接相同的示例
  - 自定义：[sms.jamesblack.com](http://sms.jamesblack.com)（18 个字符）
  - Klaviyo：[jamesblack.klv3.io](http://jblk.klv3.io)（18 个字符）
- 品牌 Klaviyo 链接包含更多字符的示例
  - 自定义：[sms.jamesblack.com](http://sms.jamesblack.com)（18 个字符）
  - Klaviyo：[jamesblackSMS.klv3.io](http://jblk.klv3.io)（21 个字符）

请注意，最大子域长度为 20 个字符。 ****设置或编辑的时间****

创建品牌 Klaviyo 链接的过程既简单又快速。它们在您创建后也可用。至于品牌自定义链接，该过程最多可能需要 14 天才能完成。 还建议您熟悉网站托管方式的技术细节（例如，您的 DNS 提供商）。 ## 其他资源

- [如何为短信创建品牌短链接](https://help.klaviyo.com/hc/en-us/articles/17649597637147)
- [了解并检查您的短信传送能力](https://help.klaviyo.com/hc/en-us/articles/1260806260849)