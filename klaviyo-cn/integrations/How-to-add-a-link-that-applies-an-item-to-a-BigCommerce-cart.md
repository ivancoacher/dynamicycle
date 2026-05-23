---
id: "115005082747"
title: "如何添加将商品应用到 BigCommerce 购物车的链接"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005082747-How-to-add-a-link-that-applies-an-item-to-a-BigCommerce-cart"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:39Z"
language: "zh"
---
## 你将会学到

了解如何添加电子邮件链接以将商品应用到 BigCommerce 购物车。如果您提示某人查看和购买特定产品（例如促销商品），您可以提供一个链接，他们可以单击该链接将商品添加到购物车。

## 开始之前

确保您已[已将您的 Klaviyo 帐户与 BigCommerce 集成](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce)，并创建了一封要在其中添加链接的电子邮件。

请注意，此过程仅适用于没有变化的 BigCommerce 产品。

## 添加您的商品链接

1. 在 BigCommerce 中查找并复制相关商品的产品 ID。您可以通过[从 BigCommerce 导出产品](https://support.bigcommerce.com/articles/Public/Exporting-Products) 并检查“产品 ID”列来找到此 ID。

或者，您可以通过编辑产品并在 URL 中找到产品 ID 来完成此操作，如下图所示。

![示例产品的 BigCommerce 管理产品编辑页面，URL 中的产品 ID 以蓝色突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28716328734363)

2. 在 Klaviyo 中，找到您要编辑的电子邮件模板，然后将按钮块拖到您的模板中；您可以使用任何您想要的按钮文本。

3. 在按钮块内的链接 URL 框中输入以下字符串：
`{{organization.url}}cart.php?action=add&product_id=##`

![Klaviyo 中的电子邮件模板编辑器，突出显示按钮和按钮块设置链接 URL](https://klaviyo.zendesk.com/hc/article_attachments/28716301371547)

4. 在您看到 ## 的地方，将这些双哈希替换为您复制的 BigCommerce 产品 ID。

5. 单击****保存**** 保存您的内容。

当收件人单击该按钮时，他们将被直接带到您网站上的购物车，其中已添加指定的产品。如果您不想使用按钮，您可以超链接电子邮件中的任何文本并使用相同的 URL 字符串。

## 结果

现在，您已添加电子邮件链接，将商品应用到 BigCommerce 购物车。

## 其他资源

- [BigCommerce 入门](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce)
- [如何在BigCommerce中使用优惠券](https://help.klaviyo.com/hc/en-us/articles/360022884472-Guide-to-Using-Coupons-with-BigCommerce)