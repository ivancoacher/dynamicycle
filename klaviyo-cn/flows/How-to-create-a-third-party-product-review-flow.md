---
id: "115002779391"
title: "如何创建第三方产品审核流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002779391-How-to-create-a-third-party-product-review-flow"
section: "Post-purchase flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:37Z"
language: "zh"
---
## 你将会学到

了解如何使用流消息询问客户对最近购买的反馈。这是建立社会证明并推动客户与您的品牌互动的好方法。

要发送产品评论电子邮件，您可以使用 Klaviyo 的内置产品评论/交叉销售流程作为起点，也可以从头开始构建自己的产品评论/交叉销售流程。

如果您使用 Klaviyo 评论，请了解如何[使用 Klaviyo 评论流程请求评论](https://klaviyo.zendesk.com/hc/en-us/articles/16319809379611)。

Klaviyo 不支持电子邮件内产品评论，这意味着客户无法直接在从您那里收到的产品评论电子邮件中撰写评论。

## 第三方与 Klaviyo 评论

无论您使用哪个评论平台，您都可以使用 Klaviyo 发送评论请求。该资源提供第三方评论平台的说明。

Klaviyo 评论和其他工具之间的一个关键区别是评论请求时间。使用其他评论工具，您必须在订单履行时触发流程，然后添加时间延迟以允许包裹到达的时间。借助 Klaviyo，您可以根据包裹的送达时间发送审核请求，这样您就可以确定您不会向包裹延迟的客户发送审核请求。

## 在 Klaviyo 中构建第三方审核流程

要使用第三方评论应用程序在 Klaviyo 中创建评论流程：

1. 在 Klaviyo 中，导航至****Flows**** 选项卡。
2. 单击****创建流程****。
3. 在流程库中搜索**产品评论/交叉销售**模板。
   ![第三](https://klaviyo.zendesk.com/hc/article_attachments/28704476264475)
4. 选择****已履行订单**** 作为触发指标。
5. 使用比平均递送时间更长的时间延迟（例如 14 天），以增加包裹在发送审核请求之前到达的可能性。
6. 一旦您对流程感到满意，请将其启动。

### 将客户链接到页面上的评论区域

Klaviyo 的模板审核流程使用[锚链接](https://help.klaviyo.com/hc/en-us/articles/360043506852)。因此，当有人点击您的电子邮件时，他们将直接进入您网页的特定区域，在那里他们可以提交评论，而不必向下滚动并找到它。

模板流使用 #reviews 锚点，但您可以对此进行调整。请注意，根据您特定的电子商务集成，以下说明可能略有不同。

打开网站产品页面代码的模板编辑器。滚动到代码中显示产品评论的区域。在这里，粘贴以下代码：

`<a id="reviews"></a>`

这充当标识符，因此当有人单击带有 #reviews 锚点的产品页面链接时，他们会到达正确的位置。

### 第三方评论应用

Klaviyo 与多个不同的产品评论应用程序集成，包括 [Judge.me](https://www.klaviyo.com/integrations/01J9V8Q5GDH7JVJ4HAV819VNV1/details) 和 [REVIEWS.io](https://www.klaviyo.com/integrations/01HWYW81ATNHZEXT7KNRTRY14C/details)。如果您使用这些应用程序中的任何一个并希望将它们与 Klaviyo 集成，请查看链接页面以获取更多信息。

## 其他资源

- [如何创建追加销售或交叉销售流程](https://klaviyo.zendesk.com/hc/en-us/articles/115002775212)
- [如何创建补货流程](https://klaviyo.zendesk.com/hc/en-us/articles/360003195232)
- [如何创建日落流](https://klaviyo.zendesk.com/hc/en-us/articles/360017518492)
- [如何调整审核请求时间](https://klaviyo.zendesk.com/hc/en-us/articles/16682549669403)