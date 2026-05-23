---
id: "115005246547"
title: "如何设置优惠券（适用于 Magento 1.x）"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005246547-How-to-set-up-coupons-for-Magento-1-x"
section: "Coupons and ecommerce integrations"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:22Z"
language: "zh"
---
Klaviyo 的 Magento 1 集成不再接受新安装，并将于 2027 年末完全终止支持。Klaviyo 支持不再能够协助处理 Magento 1 相关请求。 ## 你将会学到

Magento 支持[购物车价格规则](http://docs.magento.com/m1/ce/user_guide/marketing/price-rules-shopping-cart.html)，可用于对客户的订单应用折扣。可以为现有价格规则创建优惠券代码，以便购物者可以轻松地利用给定代码在结账过程中应用折扣。 Klaviyo 的 Magento 优惠券功能允许 Magento 1.0 商店执行以下操作：

- 在 Klaviyo 中创建与 Magento 中预先存在的价格规则相关联的新优惠券。 - 在流电子邮件中包含动态优惠券，以便每个收件人收到一个唯一的代码。本指南将解释如何在 Klaviyo 中使用 Magento 优惠券进行设置。发送活动电子邮件时，当前无法使用动态优惠券代码。在活动中发送唯一的优惠券代码需要每秒生成数千个代码。 Klaviyo 无法保证特定 Magento 服务器的速率限制设置不会影响以此数量和速度生成动态优惠券。因此，动态优惠券仅在发送流电子邮件时可用。 ## 要求

作为先决条件，请确保您已[在 Klaviyo 中启用 Magento 集成并在 Magento 中安装 Klaviyo 扩展](https://help.klaviyo.com/hc/en-us/articles/115005082187)。 ## 启用 REST API

首先通过创建新的 REST 角色并授予其完全访问权限来启用 REST API，然后将该角色分配给您的管理员用户之一。 1. 单击****系统 > Web 服务 > REST - 角色****。 2. 创建新的管理员角色。在“**角色名称**”字段中输入名称，例如“管理员”。 3. 单击左侧的****角色 API 资源****选项卡。将“**资源访问权限**”设置为“****全部****”，然后单击“****保存角色****”。 4. 接下来，导航至****系统 > Web 服务 > REST - 属性****。 5. 从用户类型列表中选择****管理员****。 6. 将**资源访问**设置为****全部****，然后单击****保存。****
7. 接下来，导航至****系统 > 权限 > 用户****。 8. 从列表中选择管理员用户，然后单击 ****编辑用户****。 9. 单击左侧边栏上的****REST 角色**** 选项卡。 10. 单击单选按钮将新的 REST 管理员角色分配给您的用户。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717985502747)
11. 单击 ****保存用户****。您现在已经为 Magento 商店启用了 REST API。如果您不确定 REST API 是否配置正确，请查看我们的[Magento 1x 优惠券故障排除资源](#h_01GZ248ZJVNJTRVFYKMTKFXFEK) 中概述的步骤。 ## 在 Magento 中生成 REST 凭证

要启用 Klaviyo 的 Magento 优惠券功能，请首先使用您刚刚创建的 REST 管理员帐户从您的 Magento 商店生成 REST API 凭据，然后将这些凭据粘贴到您的 Klaviyo 帐户中。 1. 以您在上面的[启用 REST API 部分](https://help.klaviyo.com/hc/en-us/articles/115005246547#enable-the-rest-api2)中创建的 REST 管理员用户身份登录
2. 单击“****系统”>“配置****”，然后单击“**客户**”部分下的“****Klaviyo****”。 3. 单击 ****生成 OAuth 令牌****。！[763276](https://klaviyo.zendesk.com/hc/article_attachments/28717985489051)

将填充**消费者密钥、消费者秘密、授权令牌**和**授权秘密**。您将在下一步中将这些值复制/粘贴到您的 Klaviyo 帐户中。 ## 在 Klaviyo 中设置 Magento 优惠券

1. 从您的 Klaviyo 帐户，[导航到您的 Magento 集成](https://www.klaviyo.com/integration/magento)。 2. 单击****高级选项****箭头以展开**优惠券设置**。 3. 粘贴您在上面创建的 REST 凭据。您的 Magento 服务器必须支持 HMAC-SHA1 签名以进行 OAuth 身份验证。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717985495067)
4. 单击****更新 Magento 设置。****

Klaviyo 将验证您的 REST 凭据，您将能够开始使用帐户的优惠券选项卡创建优惠券。 ## 在 Klaviyo 中创建 Magento 优惠券

当您在提供 REST 凭据后首次导航到 [Klaviyo 帐户中的 **优惠券** 选项卡](https://www.klaviyo.com/coupons) 时，您将看到消息“您尚未添加任何优惠券”。

在创建新优惠券之前，您首先需要在 Magento 中定义一个价格规则，其中包括优惠券的所有规格。无法从 Klaviyo 内部创建价格规则。在 Klaviyo 中创建的新优惠券必须引用 Magento 中预先存在的价格规则。在 Magento 中创建价格规则时，请注意，将新价格规则与特定优惠券关联的选项应保留设置为“特定优惠券”，并且您必须选中 **使用自动生成** 复选框。 1. 点击****添加优惠券**** 创建新优惠券。 2. 填写以下信息：**优惠券名称**和**Magento 规则 ID。**

- ****优惠券名称：**** 您指定的名称只能由字母、数字和下划线组成，长度最多为 32 个字符
- ****Magento 规则 ID：**** 首先在 Magento 中创建一条规则，然后将该规则的 ID 粘贴到此处以将其与此优惠券关联起来

![](https://klaviyo.zendesk.com/hc/article_attachments/28717985497243)

所有创建的优惠券将显示以下概述详细信息：

- ****优惠券名称：**** 优惠券名称
- ****活动时间范围：**** 有以下选项：
  - 有效，无有效期
  - 日期 A - 无有效期
  - 日期 A - 日期 B
  - 有效，到期日期 B
- ****创建日期：**** 优惠券创建日期
- ****最后更新日期：**** 优惠券最后更新日期

可以通过右侧的下拉菜单从此选项卡中编辑和删除优惠券。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717985500315)

## 在 Flow 电子邮件中使用 Magento 优惠券

创建优惠券后，您可以使用以下占位符变量将其插入流电子邮件中。每封电子邮件只能添加一个优惠券代码。您可以在多个位置显示相同的优惠券代码，但不能使用多个代码。 ````
{% coupon_code '优惠券名称' %}
````

将 **CouponName** 替换为您的优惠券名称。例如：

![mceclip0__2_.png](https://klaviyo.zendesk.com/hc/article_attachments/28717991395995)

## 在 SMS Flow 消息中使用独特的优惠券

流程中的[短信/彩信](https://help.klaviyo.com/hc/en-us/articles/360044863132-Using-Unique-Coupon-Codes-in-SMS-and-MMS-Messages)也可以使用独特的优惠券。就像生成电子邮件一样生成代码。然后，使用下面的模板标签将优惠券代码添加到您的短信或彩信中：

`{% coupon_code 'CouponName' %}`。在代码段中，将 **CouponName** 更改为您想要的优惠券的名称，并将其添加到消息（流程或活动）中。 ![2020-06-16_17-58-37.png](https://klaviyo.zendesk.com/hc/article_attachments/47772696564635)

与电子邮件不同，每条短信只能使用一个优惠券代码。通过电子邮件，您可以访问[隐藏块](https://help.klaviyo.com/hc/en-us/articles/115005258208-Show-or-Hide-Template-Blocks-Based-on-Dynamic-Variables)，根据某人的居住地点或做过的事情发送不同的优惠券。如果您尝试将多张优惠券添加到一条短信中，您将看到一条错误消息。 ![2020-06-17_09-51-08.png](https://klaviyo.zendesk.com/hc/article_attachments/28717991397787)

## 排除错误

### 错误消息：“无法使用指定的 REST 凭据连接到 REST API。请检查这些凭据在您的 Magento 管理员中是否有效。”

如果您在 Klaviyo 中看到此错误消息，可能有两个根本原因：

1. 您的 Magento 服务器未设置为支持 OAuth 身份验证的 HMAC-SHA1 签名。 2. 您可能尚未启用 REST API 的完整角色访问权限。要解决此问题，请在 Magento 服务器上启用 HMAC-SHA1 签名以进行 OAuth 身份验证。然后完成以下步骤来更新您的 REST 权限：

1. 在 .htaccess 文件中取消注释或添加重写规则。您需要确保这一行未被注释：
   `RewriteRule ^api/rest api.php?type=rest [QSA,L]`
2. 仔细检查您的 REST 角色是否设置正确
   我们在[此处链接的部分中为 Magento 设置优惠券的指南](https://help.klaviyo.com/hc/en-us/articles/115005246547#enable-the-rest-api) 中介绍了这方面的说明。 3. 另一个常见原因是各种 Apache 模块可以剥离“Authorization: Basic base64 (user:password)”标头。 查看[这篇文章了解更多信息](https://devhacksandgoodies.wordpress.com/2014/06/27/apache-pass-authorization-header-to-phps-_serverhttp_authorization/)

### Klaviyo 填充到电子邮件中的优惠券代码并不唯一 - 所有收件人似乎都收到相同的代码。在 Magento 中创建价格规则时，将新价格规则与特定优惠券关联的选项应保留设置为“特定优惠券”，并且必须选中“使用自动生成”复选框。单击 Magento 中的价格规则，然后在 **一般信息** 下，向下滚动到“优惠券”行选项，并将此设置更改为“特定优惠券”。接下来，选中此处的自动生成框。这应该可以解决问题，并允许我们为每个电子邮件收件人生成新的唯一优惠券代码。