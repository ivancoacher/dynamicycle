---
id: "360034336572"
title: "如何使用注册表单提供分级折扣"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360034336572-How-to-use-sign-up-forms-to-offer-tiered-discounts"
section: "Form best practices"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:45Z"
language: "zh"
---
## 你将会学到

了解如何使用注册表单向不同类型的客户提供不同的折扣，然后设置您的欢迎系列，以便每个订阅者都能获得适当的折扣。在表单中设置特定的定位设置可以帮助您避免提供不必要的折扣，并根据您对联系人的了解来定制电子邮件中的语言。 ## 开始之前

考虑您想要定位哪些客户以及您希望如何激励他们。例如，您可能希望通过在首次购买时提供折扣来激励网站访问者注册您的电子邮件列表。您可能想要提供：

- 向您网站的新访客且以前从未购买过商品的访客提供 15% 的折扣
- 以前浏览过您网站但从未购买过的访问者可享受 10% 的折扣
- 过去从您这里购买过的人没有折扣

您可以使用细分、注册表单、优惠券和流程的组合来完成此任务。 ****单击展开其他示例用例****

- 针对购物车中高价值商品的购物者，比低价值购物者提供更大的折扣。 - 针对 VIP 客户提供与其他客户不同的欢迎优惠和消息。 ## 创建您想要定位的受众群体

在构建新细分时，您可以通过注册表单上的优惠来确定您想要定位的受众群体。在我们的示例中，我们将隔离四个组，并在分段构建器中遵循定义来创建每个组：

1. 访问我们网站次数少于3次且从未购买过的访客（20%折扣）
2. 访问我们网站3次或以上且从未购买过的访客（15%折扣）
3. 180天前购买过且此后未购买过的访客（10%折扣）
4. 过去180天内购买过的访客（无折扣）

导航至****受众 > 列表和细分 > 创建列表/细分 > 创建细分****。根据每个段的定义对其进行命名，以便您可以轻松跟踪每个段。 ### 浏览次数少于 3 次且从未购买过

您可以通过识别一直以来在您的网站上活跃次数少于 3 次的用户来构建此细分。或者，您可以将其限制在特定的时间范围内，例如 90 天，以缩小受众范围。没有 cookie 的浏览器不会属于此部分，因为没有可用的电子邮件地址。要定位该群体，请按照下列步骤操作。接下来，您需要添加一个条件，指定他们从未下过订单。 ![正在为浏览次数少于 3 次且从未购买过的用户创建一个新细分。](https://klaviyo.zendesk.com/hc/article_attachments/28713335847451)

### 浏览 3 次或以上但从未购买过

在这里，您需要隔离那些在您的网站上活跃过至少 3 次的人。您可能还希望包括一直以来浏览过至少 3 个产品的浏览者。同样，如果您愿意，您也可以将其限制为更小的时间段，例如 90 天。接下来，添加一个条件，指定他们以前从未下过订单。对于这种情况，请务必将时间范围延长至所有时间。 ![正在创建一个新细分，其定义设置为包括浏览超过 3 次但从未购买过的用户。](https://klaviyo.zendesk.com/hc/article_attachments/28713330163227)

### 超过 180 天前购买，此后就没有再购买过

在此细分中，您需要识别之前购买过商品但在过去 180 天内没有购买过商品的用户。这是一个很好的团体，可以提供折扣，反映您在 [winback 系列](https://help.klaviyo.com/hc/en-us/articles/115002775192-Create-a-Winback-Flow) 中所传达的信息。 ![正在创建一个新的细分，其定义设置为包括之前购买过但不在过去 180 天内购买过的用户。](https://klaviyo.zendesk.com/hc/article_attachments/28713330141851)

### 过去 180 天内购买过

最后，您希望定位过去 180 天内购买过商品的用户，鼓励他们注册我们的电子邮件列表，但是，我们不会向他们提供折扣，因为他们最近才购买过商品。 ![正在创建一个新细分，其定义设置为包括过去 180 天内购买过产品的用户。](https://klaviyo.zendesk.com/hc/article_attachments/28713330146075)

## 构建针对细分市场的注册表单

一旦您构建了想要定位的细分，下一步就是[创建一个单独的表单](https://help.klaviyo.com/hc/en-us/articles/360002049952)来定位每个组并提示他们订阅您的主列表。 1. 导航到****注册表单****选项卡，然后从库中选择模板或从头开始构建新的表单。 2. 使用编辑器设计表单以匹配您的品牌。 3. 在****样式****选项卡中，选择表单类型。我们建议选择弹出窗口、弹出窗口或整页表单，以便吸引购物者的注意力。 4. 在 ****Targeting &**** ****Behaviors**** 部分中，您需要配置几个关键设置：
   - 在 ****Targeting**** 下，您将希望仅向刚刚构建的 4 个相应分段之一中的人员显示表单。 - 在****定位****下，您还需要排除那些已经在您的列表中的人查看该表单。由于我们没有在我们构建的细分中包含某人不在我们的主列表中的条件，因此此设置特别重要。 ![示例表单的访客定位设置为包括分层折扣列表中的访客，并排除主列表。](https://klaviyo.zendesk.com/hc/article_attachments/28713335856283)
5. 根据您是否启用了[双重选择加入](https://help.klaviyo.com/hc/en-us/articles/115005251108-The-Double-Opt-In-Process)（默认情况下，为所有列表启用双重选择加入），请务必通过单击****成功****来更新成功消息中的语言。如果您选择使用静态优惠券，或者是 Shopify 用户，您还可以直接在成功消息中包含优惠券代码。如果您的列表是单选加入，您可能只想这样做，以防止人们注册接收折扣但不确认他们的电子邮件地址。如果您的列表设置为双重选择加入，并且订阅者未确认其电子邮件，则他们不会被添加到列表中或触发欢迎系列。 6. 对您在上一步中创建的每个段重复此过程，以便每个段都有相应的表单。 7. 构建第一个表单后，您可以多次克隆它并更改其连接的折扣金额和细分。 8. 为了确保您向未接受 cookie 的浏览器显示表单（因此不属于您的任何细分），请克隆您的 20% 折扣表单并将其配置为仅向未跟踪的浏览器显示。为此，您可以导航至****定位和行为****部分，然后在****定位****下选择**不向现有 Klaviyo 个人资料显示。**

   ![示例注册表单的访客定位设置为“不向现有 Klaviyo 个人资料显示”。](https://klaviyo.zendesk.com/hc/article_attachments/28713335842331)

   ## 在您的欢迎系列中加入折扣

   接下来，您需要更新您的[欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172-Guide-to-Creating-a-Welcome-Series)。如果您使用 [Shopify](https://help.klaviyo.com/hc/en-us/articles/115006155388-Unique-Coupon-Codes-for-Shopify) 或 [Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005246547-Set-Up-Coupons-for-Magento-1-x-)，您可以通过集成使用动态优惠券。否则，您可以利用[上传优惠券功能](https://help.klaviyo.com/hc/en-us/articles/115005084727-How-to-Use-Coupon-Codes-in-Klaviyo#upload-unique-coupon-codes2)向您的订阅者提供唯一代码。由于我们为每个级别提供不同的折扣，因此我们需要创建 3 个单独的优惠券代码，每个优惠券代码都有不同的折扣百分比。请按照上述相关指南中概述的说明创建这些独特的优惠券代码。 ![其中包含优惠券标签和优惠券名称的欢迎系列电子邮件示例。](https://klaviyo.zendesk.com/hc/article_attachments/28713330131099)

   接下来，创建一个流（****流 > 创建流 > 从头开始创建****）。为了向不同类型的订阅者发送不同的电子邮件，我们需要将几个[条件拆分](https://help.klaviyo.com/hc/en-us/articles/115003872171-Add-a-Conditional-Split)拖到我们的流程中。这些条件分割将与我们用于构建第一步中概述的段的条件相匹配。 ![使用 4 个条件分割路径构建的列表触发流程，用于您创建的 4 个相应的分级折扣，并向每个电子邮件发送一封包含正确优惠券的不同电子邮件。](https://klaviyo.zendesk.com/hc/article_attachments/28713330169115)

   根据您希望联系人在收到第一封电子邮件后如何在流程中移动，您可能需要[重新加入拆分](https://help.klaviyo.com/hc/en-us/articles/360002419512-Rejoin-a-Flow-Split)以简化体验。从这里，您可以遵循我们的其他[欢迎系列最佳实践](https://help.klaviyo.com/hc/en-us/articles/115002775172-Guide-to-Creating-a-Welcome-Series#take-your-welcome-series-to-the-next-level7)。 ## 其他资源

   - [如何创建欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172-Guide-to-Creating-a-Welcome-Series)
   - [如何创建和定位近期购物车放弃者的细分](https://help.klaviyo.com/hc/en-us/articles/360032334511-Create-a-Segment-of-Recent-Cart-Abandoners)
   - [Klaviyo 优惠券代码入门](https://help.klaviyo.com/hc/en-us/articles/115005084727-How-to-Use-Coupon-Codes-in-Klaviyo)