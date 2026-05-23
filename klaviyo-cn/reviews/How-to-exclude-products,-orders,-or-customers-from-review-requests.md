---
id: "16684841274139"
title: "如何从审核请求中排除产品、订单或客户"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16684841274139-How-to-exclude-products-orders-or-customers-from-review-requests"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:48:59Z"
language: "zh"
---
## 你将会学到

了解如何避免向某些客户或不需要审核的产品（例如礼品卡或运输保险）发送审核请求。

## 使用 klaviyo\_reviews\_exclude 标签

Klaviyo Reviews 提供了一个标签 **klaviyo\_reviews\_exclude**，可应用于产品、订单和客户以阻止发送评论请求。请参阅以下部分中的示例用例以及如何应用此标签。

![排除标签](https://klaviyo.zendesk.com/hc/article_attachments/28705665408795)

## 从未来的审核请求中排除产品

假设客户订购了一把带有运输保险的吉他。如果您将排除标签添加到运输保险订单项中，他们只会收到吉他的审核请求。

要从 Shopify 中的未来评论请求中排除产品：

1. 导航到 Shopify 后台中的产品页面。
2. 在 **标签** 字段中，添加标签 **klaviyo\_reviews\_exclude**。

   要从 WooCommerce 中的未来审核请求中排除产品：
3. 导航到 WooCommerce 管理员中的产品页面。
4. 在 **产品** **标签** 字段中，添加标签 **klaviyo\_reviews\_exclude**。

一旦您保存了此更改，我们将不再请求对此产品进行评论，即使它是某人订单中的唯一商品。请注意，这些更改仅适用于未来的订单；在您进行更改之前下的任何订单都可能会收到对此产品的审核请求。

## 从您的审核请求流程中排除订单（仅限 Shopify）

将此标签添加到订单中会将该订单排除在审核请求之外。这是一次性排除：如果同一客户将来下了另一个订单，则该订单将有资格获得审核请求。

1. 导航到 Shopify 后台中的订单。
2. 在 **标签** 字段中，添加标签 **klaviyo\_reviews\_exclude**。

## 排除客户接收评论请求（仅限 Shopify）

1. 导航到 Shopify 后台中的客户。
2. 在 **标签** 字段中，添加标签 **klaviyo\_reviews\_exclude**。
3. 保存客户的详细信息。

添加此标签将使客户不再接收未来的评论请求。请注意，如果他们最近的订单当前位于您的审核请求流程中，他们将继续接收消息，直到退出该流程。

## 排除产品、订单和客户的账单

如果订单被排除在接收评论请求之外（即客户、订单中的所有产品或订单本身具有 **klaviyo\_reviews\_exclude** 标签），则该订单将不计入您的 Klaviyo Reviews 计费计划。