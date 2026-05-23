---
id: "5379853359771"
title: "如何删除 Shopify 的现场跟踪"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/5379853359771-How-to-remove-onsite-tracking-for-Shopify"
section: "Shopify troubleshooting"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:03Z"
language: "zh"
---
## 你将会学到

了解如何从 Shopify 商店中删除 Klaviyo 现场跟踪，其中包括 **现场活动** 和 **查看的产品** 跟踪，还可能包括 **查看的收藏品**、**提交的搜索** 和 **添加到购物车** 跟踪，具体取决于您的设置。有关更多背景信息，请阅读[我们关于 Shopify 现场跟踪的文章](https://help.klaviyo.com/hc/en-us/articles/4425956184731)。

## 开始之前

出于网站速度性能原因，您可能希望删除现场跟踪，尽管 Klaviyo.js 最近已更新为[最大限度地减少其影响](https://klaviyo.tech/improving-forms-performance-c67c98114d49)。请注意，Klaviyo 的 Shopify 应用程序嵌入绕过了网站的本机标签管理器，因此可以更快地加载 Klaviyo 的 JavaScript。此外，我们还通过 Shopify Server Pixel 跟踪一些事件（**查看的集合**、**提交的搜索**和**添加到购物车**）。

您可以：

- 删除**查看的产品**跟踪
- 删除**查看的收藏**、**提交的搜索**和**添加到购物车**跟踪
- 删除所有现场跟踪

第一个意味着您将无法跟踪某人何时查看您商店中的产品，这意味着您将无法发送浏览放弃消息。

如果您删除所有现场跟踪，您也将无法再使用 Klaviyo 注册表单。

以下有关删除 **添加到购物车** 跟踪的指南是指通过 Shopify Server Pixel 同步的 Shopify 品牌 **添加到购物车** 事件。如果您希望删除通过代码片段启用的“添加到购物车”跟踪，请查看[我们的指南](https://help.klaviyo.com/hc/en-us/articles/28709780787355)。

## 删除查看过的产品跟踪

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 选择****Shopify.****
3. 取消选中**跟踪“查看的产品”事件**设置。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28709107573275)
4. 单击****更新设置****。

## 删除查看的收藏、提交的搜索并添加到购物车

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 选择****Shopify.****
3. 取消选中**跟踪行为事件**设置。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28709113412123)
4. 单击****更新设置****。

## 删除所有现场跟踪

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 选择****Shopify.****
3. 取消选中**跟踪“查看的产品”事件**和**跟踪行为事件**设置。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28709113412123)
4. 单击****更新设置****。
5. 单击 **Klaviyo 应用程序嵌入已在您的 Shopify 商店** 旁边的 **** 编辑**** 以引入 Shopify。
6. 如果出现提示，请登录。
7. 关闭应用程序嵌入。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28710075007131)
8. 单击****保存****。

## 结果

您现在已从 Shopify 商店中删除了选定的现场跟踪。