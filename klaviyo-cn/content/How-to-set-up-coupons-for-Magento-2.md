---
id: "360041971851"
title: "如何为 Magento 2 设置优惠券"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360041971851-How-to-set-up-coupons-for-Magento-2"
section: "Coupons and ecommerce integrations"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: "zh"
---
## 你将会学到

了解如何在 Magento 2 中设置价格规则并在 Klaviyo 中创建优惠券，以便您的购物者可以在结账过程中轻松应用折扣。 Magento 支持[购物车价格规则。](https://docs.magento.com/user-guide/marketing/price-rules-cart.html)

Klaviyo 的优惠券允许 Magento 2 商店执行以下操作：

- 在 Klaviyo 中创建与 Magento 中预先存在的价格规则相关联的新优惠券。 - 在流电子邮件中包含唯一（也称为“动态”）优惠券，以便每个收件人收到唯一的代码。本指南将引导您分两步在 Klaviyo 中创建 Magento 2 优惠券：

1. 在 Magento 2 中设置价格规则。 2. 在 Klaviyo 中创建优惠券。如果您想发送包含 Magento 2 唯一优惠券代码的活动电子邮件，请按照有关[将唯一优惠券上传到 Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005084727#upload-unique-coupons-into-klaviyo3) 并在消息中使用它们的指南进行操作。 ## 开始之前

在开始之前，请确保您已[在 Klaviyo 中启用 Magento 2 集成并在 Magento 中安装 Klaviyo 扩展](https://help.klaviyo.com/hc/en-us/articles/115005254348-Integrate-with-Magento-2-x-CE-and-EE-)。 ## 在 Magento 2 中设置价格规则

1. 从您的 Magento 2 商店导航至****营销 > 购物车价格规则****。 ![视频显示 Magento 2 中的营销选项卡并选择购物车价格规则。](https://fast.wistia.com/embed/medias/mbqh9crj11/swatch)

2. 单击“****添加新规则****”创建价格规则。 ![magento 2 中的购物车价格规则菜单，选择添加新规则。](https://klaviyo.zendesk.com/hc/article_attachments/28715963480987)

3.填写规则信息：

- ****规则名称：**** Magento 2 中价格规则的名称。 - ****活动：**** 选择 **是**。如果未选择**是**，优惠券将不起作用。 - ****网站****：如果您只有一个 Magento 商店，请选择您的网站名称。如果您有多个 Magento 商店，请选择与优惠券关联的商店。 - ****客户组：**** 选择 **未登录**，或选择其他客户组。 - ****优惠券：**** 从下拉列表中选择 **特定优惠券**。 - ****优惠券代码：**** 您无需在此字段中输入任何内容； Klaviyo 会自动为您生成优惠券代码。 - ****使用自动生成：**** 您必须启用此字段。如果您不启用此字段，Klaviyo 将无法生成优惠券代码。 - ****每张优惠券的使用次数：**** 您的优惠券可以使用的次数；通常该值为 1。 - ****每个客户的使用次数：**** 每个客户可以使用您的优惠券的次数；通常该值为 1。 - ****从 -- 到：**** 输入优惠券有效的日期范围； ****To**** 日期将是优惠券的到期日期。设置为永不过期的优惠券仍将显示 Klaviyo 中列出的 1 年过期日期，但它们不会过期。 ![新的购物车价格规则菜单，您可以在其中填写所需的规则信息。](https://klaviyo.zendesk.com/hc/article_attachments/28715963487643)

4. 在**新购物车价格规则**屏幕底部，您将看到其他设置。 ****条件、操作和标签**** 设置是可选的，并将影响优惠券在 Magento 2 商店中的应用方式；这些不会影响 Klaviyo 优惠券的生成。 ![可选的条件、操作和标签设置位于新购物车价格规则页面的底部。](https://klaviyo.zendesk.com/hc/article_attachments/28715970087067)

5.****管理优惠券代码：****这些设置不需要填写。当Klaviyo生成优惠券代码时，这些代码将出现在该部分中。 6. 完成后，单击屏幕右上角的****保存****。 ![新购物车价格规则页面右上角突出显示的保存按钮。](https://klaviyo.zendesk.com/hc/article_attachments/28715970091163)

7. 查看您的 Magento 2 优惠券列表。每张 Magento 2 优惠券都与一个 ID 相关联。记下您创建的优惠券的 ID。您在下一步中将需要它。 ![您的 Magento 2 优惠券列表视图，其中圈出了您创建的优惠券 ID。](https://klaviyo.zendesk.com/hc/article_attachments/28715970094363)

## 在 Klaviyo 中创建 Magento 优惠券

接下来，您将在 Klaviyo 中创建优惠券。对于此步骤，您需要与刚刚在 Magento 2 帐户中创建的价格规则关联的 ID。 在 Klaviyo 中创建的新优惠券必须引用 Magento 中预先存在的价格规则。 1. 导航至****优惠券****部分并选择****Magento 2 优惠券****。 ![选择了 Magento 2 优惠券的优惠券选项卡。 ](https://klaviyo.zendesk.com/hc/article_attachments/28715963503387)

2. 单击****添加优惠券**** 创建新优惠券。 3. 在 **优惠券名称** 字段中输入优惠券的名称，然后输入与此优惠券关联的 Magento 2 价格规则 ID。同样，您需要在 Magento 2 中创建价格规则，然后才能在 Klaviyo 中创建优惠券。如果您需要再次引用此 ID 号，请返回您的 Magento 2 帐户。 4. 完成后，单击****添加优惠券****。 ![该模式询问您新创建的优惠券的名称及其 Magento 2 规则 ID。](https://klaviyo.zendesk.com/hc/article_attachments/28715970097435)

5. 您已创建新优惠券。 ## 连续使用您独特的优惠券

创建并配置优惠券后，将其插入流消息中。 1. 导航至 Klaviyo 左侧导航栏中的****Flows**** 选项卡。 2. 打开现有流程或[创建新流程](https://help.klaviyo.com/hc/en-us/articles/115002774932)。 3. 选择流程内的流程消息。 4. 打开所选流消息的消息编辑器。 5. 单击个性化图标。根据您的编辑器的不同，您可能会看到一个人物图标或标有“****个性化****”的按钮。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39892622216987)
6. 从**所有类型**菜单中，选择****优惠券****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39892629350171)
7. 选择您要添加的优惠券。 8. 可选：选择流程电子邮件上的****3 个点****，然后单击****预览****。请注意，当您直接在 Klaviyo 中预览电子邮件时，您将不会看到填充的唯一代码。相反，您会看到优惠券的名称带有“预览”连字符。 Klaviyo 只会在实际发送时创建和共享唯一代码。 ![在预览模式下显示带有优惠券标签的示例电子邮件。](https://klaviyo.zendesk.com/hc/article_attachments/39892622226843)

发送消息时，由您的前缀和 10 个随机数字组成的唯一折扣代码将动态替换每个收件人的变量。如果您在多条流消息中包含相同的优惠券标签，收件人每次都会收到相同的唯一代码。 ![优惠券前缀末尾添加了独特的10位代码](https://klaviyo.zendesk.com/hc/article_attachments/39892629356187)

实时流电子邮件的唯一优惠券代码会根据您在 **优惠券详细信息** 页面的 **最低库存** 部分中指定的数量自动生成。例如，如果您创建**最低库存**为 100 的优惠券，Klaviyo 会生成一批 100 个唯一代码。这些每天都会自动补充；但是，如果您在充值前使用了全部 100 个代码，则由于可用代码不足，将跳过第 101 次分配优惠券的尝试。这会自动触发 Klaviyo 生成另外 100 个代码。由于流程的优惠券代码会自动补充，因此您无需通过**添加代码**选项手动添加批量优惠券代码。 ## 其他资源

- [如何设置优惠券（适用于 Magento 1.x）](https://help.klaviyo.com/hc/en-us/articles/115005246547-How-to-set-up-coupons-for-Magento-1-x-)
- [如何查看优惠券历史](https://help.klaviyo.com/hc/en-us/articles/360048069712-How-to-view-coupon-history)
- [Magento 2 集成疑难解答](https://help.klaviyo.com/hc/en-us/articles/5510750923035-Troubleshooting-your-Magento-2-integration)