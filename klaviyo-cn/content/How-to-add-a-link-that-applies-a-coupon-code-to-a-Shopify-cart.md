---
id: "115005253088"
title: "如何添加将优惠券代码应用到 Shopify 购物车的链接"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005253088-How-to-add-a-link-that-applies-a-coupon-code-to-a-Shopify-cart"
section: "Coupons and ecommerce integrations"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-05-08T14:09:04Z"
language: "zh"
---
## 你将会学到

了解如何在电子邮件或短信中添加链接，将优惠券代码直接应用到购物者的 Shopify 购物车。将优惠券应用到购物车后，他们可以更轻松地利用折扣并快速购买。要进行此设置：

1. 创建优惠券代码。这可以作为参数插入到链接中。 2. 将链接添加到电子邮件中的按钮或将链接粘贴到短信中。当订阅者单击电子邮件中的短信链接或按钮时，系统会将他们重定向到该链接，并自动将折扣应用到他们的下一个购物车。 ## 创建优惠券代码

1. 导航至****内容 > 优惠券****以创建优惠券代码。您可以创建[静态代码或唯一代码。](https://help.klaviyo.com/hc/en-us/articles/115005084727#unique-vs--static-coupon-codes2%20)

   - 要创建静态代码，请前往 Shopify 并根据您想要提供的促销类型创建百分比折扣代码或货币折扣代码。 ![Shopify for SPRINGSALE 商店中的折扣页面显示折扣代码、折扣类型和价值以及摘要。](https://klaviyo.zendesk.com/hc/article_attachments/28717810963099)
   - 要创建唯一（也称为“动态”）代码，请按照[如何为 Shopify 创建唯一优惠券代码](https://help.klaviyo.com/hc/en-us/articles/115006155388) 中概述的说明进行操作。请注意，必须在 Klaviyo 中导入或创建唯一优惠券，而必须在 Shopify 中创建静态优惠券。 2. 创建代码后，将其复制，以便稍后将其粘贴到消息中。 3. 选择是否要在流程或活动电子邮件或短信中发送优惠券，分别通过 Klaviyo 中的****流程****或****活动****选项卡找到。 4. 打开消息编辑器。 5. 对于电子邮件：

   - 将按钮块拖放到链接的电子邮件模板中（如果还没有）。 - 将链接粘贴到按钮的**链接地址**字段中（以代码作为参数）。如需格式化链接的帮助，请阅读[下一节](#link-formats-for-coupon-codes3)。 - 带有链接的按钮示例：

       ![](https://klaviyo.zendesk.com/hc/article_attachments/34361517003931)
       ![SHOPcart1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717810971803)
   - 自定义按钮文本以提醒购物者您的优惠券。 - 单击****下一步****。 6. 对于短信，只需粘贴链接，然后单击****下一步****。 ## 优惠券代码的链接格式

如果您最初将客户链接到非结帐页面，Klaviyo 无法确保在结帐时自动应用优惠券；您的 Shopify 网站最终可能会从网站 URL 中删除优惠券。如果您链接到非结帐页面并遇到此问题，您应该联系您的主题开发人员。 ### 应用折扣代码和结账链接

Shopify 将 **结帐开始** 事件与 **结帐 URL** 属性同步到 Klaviyo，该属性链接回每个客户的唯一购物车。如果您要发送废弃的购物车消息（由 **Checkout Started** 事件触发）并希望将客户链接到其废弃的购物车并添加折扣代码，请添加以下代码片段：

****静态 Shopify 优惠券链接结构：****

`{{ event.extra.checkout_url }}&discount=优惠券名称`

****Klaviyo 生成的优惠券链接结构：****

`{{ event.extra.checkout_url }}&discount={% coupon_code 'CouponName' %}`

### 将折扣代码应用于活动 URL

对于放弃浏览或添加到购物车流程，使用“{{ event.extra.checkout_url }}”将不起作用。这表示与结帐关联的 URL，但在开始结帐之前会捕获浏览放弃和添加到购物车事件。相反，您可以根据“{{ event.URL }}”使用以下命令将收件人重定向到已应用优惠券的产品页面：

`{{organization.url|trim_slash}}/discount/CouponName?redirect={{event.URL|cut:"https://YourSite.com"}}`

确保将 **CouponName** 替换为您的优惠券名称，并将 YourSite 替换为您的网站（例如 klaviyo.com）。 ### 应用折扣代码并链接到您的主页

您可以添加一个指向您主页的链接，并自动将折扣应用到客户的购物车。您可以使用多种格式：

1. `mysite.com/discount/CouponName`
2.`mysite.com/?discount=优惠券名称`
   对于独特的优惠券代码，您可以使用：
3. `mysite.com/discount/{% coupon_code 'CouponName' %}`

对于这些选项中的任何一个，您都应该将 mysite.com 替换为您的网站，并且在您看到 **CouponName** 的地方，请确保替换为您在 Shopify 中创建的折扣代码。例如，如果您的品牌网站是 [klaviyo.com](http://www.klaviyo.com,) 并且您使用的是名为 WELCOME 的优惠券，则完整网址将为`klaviyo.com/discount/WELCOME`或`klaviyo.com/discount/{% coupon_code 'WELCOME' %}`。 ### 应用折扣代码并链接到您网站上的另一个页面

您可能希望将折扣代码应用于购物会话，例如产品系列页面或网站上的其他页面，而不是将客户直接链接回您的主页或重建客户放弃的购物车。在这种情况下，您可以根据您使用的是静态优惠券还是唯一优惠券，使用以下 URL 结构之一：

1. `mysite.com/discount/CouponName?redirect=/new-path`
2. `mysite.com/discount/{% coupon_code 'CouponName' %}?redirect=/new-path`

对于任一结构，替换：

- **mysite.com** 与您的网站
- **CouponName** 与您的优惠券名称
- **new-path** 带有所需的 URL 扩展名。例如，如果您想将某人链接到特定的集合页面，您可以使用 `?redirect=/collections/mycollection`

例如，如果您的品牌网站是 [klaviyo.com](http://www.klaviyo.com,) 并且您使用名为 WELCOME 的优惠券，则完整网址将为`klaviyo.com/discount/WELCOME?redirect=/pricing`或 `klaviyo.com/discount/{% coupon_code 'WELCOME' %}?redirect=/pricing`

## 故障排除

以下是一些快速故障排除提示：

1. 预览消息时，请注意，它不会显示实时优惠券。相反，您会看到优惠券的名称，后跟 -PREVIEW。 2. 如果您触发实时发送并且您的优惠券代码没有自动应用到您的购物车，请问自己以下问题：

   - 购物车中的商品是否已打折？如果是，Shopify 将不允许在现有折扣之上提供额外折扣。 - 在优惠券定义中，是否有优惠券适用的特定产品或系列，以及购物车中的产品是否与配置匹配？如果产品不符合优惠券规则，这可能就是问题所在。 3. 如果您在实时发送中测试链接，但它无法正确应用您的折扣代码，您可能需要调整添加的参数，使其以“&”而不是“?”开头。 - 这是因为“？”仅当您的折扣是您添加到链接的唯一参数时才有效，并且如果您要添加多个参数，则需要使用“&”。将链接格式更改为以下内容，它应该可以工作：

`mysite.com/discount/{% coupon_code 'your_code' %}&redirect=/new-path`