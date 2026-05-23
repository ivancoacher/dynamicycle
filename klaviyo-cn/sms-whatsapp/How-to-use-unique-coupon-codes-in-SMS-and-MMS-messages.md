---
id: "360044863132"
title: "如何在短信和彩信中使用唯一的优惠券代码"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360044863132-How-to-use-unique-coupon-codes-in-SMS-and-MMS-messages"
section: "Format your SMS messages"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: "zh"
---
## 你将会学到

了解如何在短信/彩信中使用独特的优惠券，以便您可以向短信订阅者发送一次性优惠券并鼓励他们购买。您不能使用****设置 > SMS**** 下的自动回复消息的唯一优惠券代码（也称为动态优惠券）。 ## 开始之前

使用 SMS 和 MMS 消息的唯一优惠券代码有多种最佳做法：

- 添加超出严格需要的代码；建议拥有 50 个额外优惠券代码。 - 提前上传或生成优惠码；此过程需要时间，特别是对于大量代码，因此最好在开始发送前 1 或 2 天进行。 - 如果您上传优惠券代码并在流程中使用它们，请定期检查您是否有 50 个代码的缓冲区。 - 对每个活动和流程使用单独的优惠券代码。为每次发送使用不同的优惠券代码可以更轻松地生成/上传正确数量的代码以及跟踪人们在哪里看到优惠券。 - 当您包含唯一的优惠券时，您的短信或彩信中至少允许有 5 个额外字符。 ****使用独特优惠券时为什么要为更多字符留出空间？****

每当涉及动态内容（例如具有唯一优惠券）时，Klaviyo 只能提供 SMS 的估计字符长度，而不是确切的字符长度。代码的默认长度为 8 个字符；然而，实际长度有所不同。假设您在营销活动中包含一张恰好有 160 个字符的独特优惠券。如果优惠券代码的实际字符数为 10，您的活动将以 2 条短信（而不是 1 条）的形式发送，从而花费您比您计划的更多的积分。 ## 将优惠券代码添加到 Klaviyo

为短信创建唯一优惠券代码的过程与电子邮件相同。 Klaviyo 可以为 [Shopify](https://help.klaviyo.com/hc/en-us/articles/115006155388)、[Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005246547) 和 [Magento] 生成这些代码2](https://help.klaviyo.com/hc/en-us/articles/360041971851)。 ![在优惠券选项卡中单击右上角的创建优惠券以创建新优惠券。](https://fast.wistia.com/embed/medias/xfixhpcuc5/swatch)

对于所有其他电子商务集成，包括 [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360022884472) 和 [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/360031279471)，您可以在 Klaviyo 外部生成优惠券，然后[上传优惠券代码](https://help.klaviyo.com/hc/en-us/articles/115005084727#upload-unique-coupon-codes2) 到您的帐户。 ![菜单栏中带有箭头的优惠券选项卡指向已上传的优惠券选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28713331515163)

## 发送带有优惠券的短信活动

生成优惠券或将优惠券上传到 Klaviyo 后，您就可以开始将优惠券包含在发送给订阅者的短信或彩信活动中。一条短信中只能添加 1 个优惠券代码。 1. 导航至****营销活动****
2. 单击****创建营销活动****。 3. 选择****短信****，为活动命名，然后选择收件人。 4. 在内容屏幕中构建您的消息。要添加优惠券代码，请包含以下模板标签。请记住将“CouponName”更改为您的优惠券名称：

`{% coupon_code 'CouponName' %}`

优惠券发送给订阅者时的显示方式与预览窗口中的显示方式不同。在预览中显示实际优惠券将使用您的优惠券代码之一。为了避免这种情况，您将看到优惠券代码的名称，后跟“-PREVIEW”。

下面的示例显示了名为“SummerSale”的优惠券的预览如何显示。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33627679377691)

配置完内容后，点击****下一步****。 Klaviyo 将检查优惠券是否有足够的代码供收件人使用，只有当您有足够的代码供所有收件人使用时，您才能发送。最佳做法是添加比您需要的更多的优惠券代码，以防您计划稍后发送活动并且有更多的人加入您要发送的列表或细分群体。 ![来自 Klaviyo 的错误消息，告诉您优惠券没有足够的代码供收件人使用。](https://klaviyo.zendesk.com/hc/article_attachments/28713331519515)

一旦您确认您有足够的优惠券代码，请安排短信活动或立即发送。 ## 在短信流中使用优惠券代码

使用相同优惠券的流消息将向收件人发送相同的优惠券代码。 例如，如果短信和电子邮件包含相同的 20% 优惠券，则优惠券代码将相同。要将优惠券代码添加到流程中的 SMS 消息中：

1. 导航至您想要获取优惠券的特定流程和消息。 2. 接下来，将以下代码段添加到消息中，将 CouponName 替换为您的优惠券名称：

`{% coupon_code 'CouponName' %}`

![](https://klaviyo.zendesk.com/hc/article_attachments/33627693014427)

有足够的优惠券可用于流量非常重要。与营销活动不同，没有审核阶段可以检查您是否有足够的资金。当人们有资格获得流量时，流量会自动发送，因此您需要验证是否有足够的优惠券可用。对于 Shopify、Magento 1 和 Magento 2，如果优惠券代码数量低于 100 个，Klaviyo 将自动生成 100 个代码。但是，对于其他集成，您必须手动上传新代码；因此，我们建议定期检查可用优惠券的数量。 ## 错误信息

在短信中使用优惠券时，您可能会收到 3 种类型的错误。这些错误将在屏幕左侧显示营销活动和流程。第一个错误是Klaviyo找不到与优惠券名称匹配的优惠券代码。例如，姓名中缺少数字、拼写错误等。在这种情况下，请检查您输入的姓名是否与**优惠券**中的姓名相同。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33627693020315)

第二种错误是模板标签的格式不正确。例如，如果它有多余的空格或缺少括号。确保标签的格式如下：

`{% coupon_code 'CouponName' %}`

![](https://klaviyo.zendesk.com/hc/article_attachments/33627679398171)

如果您在单个文本中包含多个优惠券，您也会收到错误消息。每条短信仅允许使用 1 个优惠券，因此请检查您是否意外使用了 2 个不同的优惠券。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33627693036571)

## 其他资源

- [Klaviyo 优惠券代码入门](https://help.klaviyo.com/hc/en-us/articles/115005084727)
- [如何创建和发送短信或彩信活动](https://help.klaviyo.com/hc/en-us/articles/360040039971)
- [各个级别的短信营销策略[+12个专业技巧]](https://www.klaviyo.com/blog/sms-marketing-strategies)