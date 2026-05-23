---
id: "19736852757915"
title: "如何删除 BigCommerce 的现场跟踪"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/19736852757915-How-to-remove-onsite-tracking-for-BigCommerce"
section: "Getting started with BigCommerce"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:33Z"
language: "zh"
---
## 你将会学到

了解如何从 BigCommerce 网站中删除 Klaviyo 现场跟踪。现场跟踪包括**现场活动**和**查看的产品**跟踪。

**网站上活动**跟踪是通过 Klaviyo 的现场 JavaScript（也称为 Klaviyo.js）启用的，因此删除**网站上活动**跟踪需要删除 Klaviyo.js。将 BigCommerce 与 Klaviyo 集成时，Klaviyo.js 会自动添加到您的网站，但可以在 Klaviyo 中关闭。

BigCommerce 的“查看的产品”跟踪是通过[在集成过程中]添加到网站的代码段启用的(https://help.klaviyo.com/hc/en-us/articles/115005082547#h_01HAQ99C0AKXHH3PH3ZY2V4TS8)，因此删除“查看的产品”跟踪需要删除此代码段。

## 开始之前

出于网站速度性能原因，您可能希望删除现场跟踪，尽管 Klaviyo.js 最近已更新为[最大限度地减少其影响](https://klaviyo.tech/improving-forms-performance-c67c98114d49)。

如果您不再希望在商店中启用 Klaviyo 现场跟踪，您可以：

- 仅删除**查看的产品**跟踪。
- 删除**现场活动**和**查看的产品**跟踪。请注意，删除“网站上活动”跟踪而不删除“查看的产品”跟踪会导致“查看的产品”跟踪不再起作用。

需要注意的是：

- 删除 **Active on Site** 跟踪也会导致 Klaviyo 注册表单不再有效。
- 删除**查看的产品**跟踪意味着您将无法跟踪某人何时查看您商店中的产品，因此您将无法再发送浏览放弃消息。
- 删除现场跟踪将导致 Klaviyo 的[添加到购物车功能](https://help.klaviyo.com/hc/en-us/articles/360024310292)（如果您已为 BigCommerce 设置此功能）不再工作。

## 删除 Active on Site 跟踪

从 BigCommerce 网站删除 **Active on Site** 跟踪需要取消选中 Klaviyo 中的集成设置。

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 从列表中选择****BigCommerce****。
3. 取消选中**自动添加 Klaviyo 现场 javascript** 设置。
   ![BigCommerce 现场跟踪设置](https://klaviyo.zendesk.com/hc/article_attachments/28723684603547)
4. 单击****更新设置****。

**现场活动**跟踪现在将从您的 BigCommerce 商店中删除。

## 删除查看过的产品跟踪

要从 BigCommerce 网站中删除**查看的产品**跟踪，需要从网站代码中删除您[在集成期间添加](https://help.klaviyo.com/hc/en-us/articles/115005082547#h_01HAQ99C0AEYNSZ7YKNX9PX6C9)的代码段。

1. 查看片段以供参考：

1. 在您的 Klaviyo 帐户中，选择****集成****选项卡。
2. 在右上角，单击****管理数据> 设置网络跟踪****。从这里，您可以查看**查看的产品**片段，以了解需要从您的网站中删除的内容。
   ![在 Klaviyo 中添加查看的产品跟踪步骤](https://klaviyo.zendesk.com/hc/article_attachments/28723684608667)

2. 在新选项卡中，登录 BigCommerce 仪表板并导航至 ****Storefront > 我的主题****。
3. 从当前主题中，单击****高级设置****下拉列表，然后单击****编辑主题文件****。请注意，如果您使用默认主题，则不会出现编辑主题文件的选项。您需要制作主题的副本，然后对该副本进行编辑。您所做的任何编辑将仅适用于您正在编辑的主题。
4. 在编辑器中，导航至****模板 > 页面****，向下滚动，然后单击打开****product.html**** 页面。
5. 在此页面底部，您将看到 **查看的产品** 代码片段。删除片段，然后单击****保存所有文件****。
   ![BigCommerce 中的产品页面模板，包含查看的产品片段](https://klaviyo.zendesk.com/hc/article_attachments/28723684606107)

**查看的产品**跟踪现已从您的 BigCommerce 网站中删除。

## 其他资源

- [Klaviyo现场跟踪入门](https://help.klaviyo.com/hc/en-us/articles/115005076767)
- [BigCommerce 入门](https://help.klaviyo.com/hc/en-us/articles/115005082547)
- [如何将 Klaviyo 嵌入式表单添加到您的 BigCommerce 网站](https://help.klaviyo.com/hc/en-us/articles/360022594552)