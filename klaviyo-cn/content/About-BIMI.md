---
id: "4406592127515"
title: "关于BIMI"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4406592127515-About-BIMI"
section: "Design best practices"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:56:57Z"
language: "zh"
---
了解如何使用消息识别品牌指示器 (BIMI) 在收件人收件箱中您的发件人地址旁边显示您的品牌徽标。实施 BIMI 可以提高品牌认知度、使您的业务合法化，并通过与收件人建立信任来提高送达率。

## 什么是 BIMI？

BIMI 使用您的 DNS 设置来验证您发送的电子邮件中的视觉品牌标识。这项技术允许品牌在发送消息时控制收件箱中使用的徽标，以建立信任和品牌认知度。此外，Gmail 还会向已完成验证的发件人附加一个蓝色复选图标。 Gmail、Yahoo 和某些版本的 Apple 支持 BIMI。 [查看支持 BIMI 的最新收件箱列表。](https://bimigroup.org/bimi-infographic/)

![带有 BIMI 徽标的电子邮件标题示例](https://klaviyo.zendesk.com/hc/article_attachments/28720772382875)

要在 Outlook 收件箱中添加品牌徽标，请使用 [Bing Pages](https://www.microsoft.com/en-us/bing/bing-pages-overview)。

## 为 BIMI 准备您的帐户

[BIMI 集团](https://bimigroup.org/) 设定了某些要求，以确保 BIMI 得到正确使用，并且不会误导任何收件人或允许发件人冒充其他品牌。为了实施 BIMI，您的品牌必须采取以下步骤：

- SVG (.svg) 格式
- 图像为方形，徽标居中，无附加文字
- 存储使用过的HTTPS
- 不大于 32 kb

- [实施 SPF、DKIM 和 DMARC。](https://help.klaviyo.com/hc/en-us/articles/4402601857307-Understanding-DMARC) 您的 DMARC 策略必须设置为 p=quarantine OR p=reject。
- 准备您的徽标图像，确保其符合 [BIMI 集团的徽标标准](https://bimigroup.org/creating-bimi-svg-logo-files/)，包括以下内容：
- 为您的徽标添加商标并获取[验证标记证书](https://support.google.com/a/answer/10911028?hl=en)（发送到 Gmail 地址时需要）

## 实施 BIMI

完成所有先决条件后，请按照 Validity 提供的 [BIMI 实施步骤](https://help.returnpath.com/hc/en-us/articles/360029588491-How-to-implement-Brand-Indicators-for-Message-Identification-BIMI-on-my-emails) 操作。请注意，Klaviyo 对 VMC 的发行或 BIMI 的实施没有直接控制权。如果您对实施 BIMI 有疑问或疑虑，请[参阅 BIMI Group 的常见问题解答](https://bimigroup.org/faqs-for-senders-esps/)。

BIMI 仅受[某些收件箱](https://bimigroup.org/bimi-infographic/) 支持。实施 BIMI 不会影响您的邮件向使用不受支持的收件箱的收件人显示的方式。