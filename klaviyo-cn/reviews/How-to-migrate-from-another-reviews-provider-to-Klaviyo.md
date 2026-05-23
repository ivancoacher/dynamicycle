---
id: "27631521070235"
title: "如何从其他评论提供商迁移到 Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/27631521070235-How-to-migrate-from-another-reviews-provider-to-Klaviyo"
section: "Getting started with reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:43Z"
language: "zh"
---
## 你将会学到

了解如何从以前的评论提供商迁移到 Klaviyo Reviews。本指南涵盖了整个迁移过程，从导入数据到设置小部件、选择计划和查看结果。目前，使用 Shopify 或 WooCommerce 作为电子商务平台的用户支持 Klaviyo Reviews。 ## 概述

如果您选择遵循应用程序内入门向导，它将引导您完成下面概述的初始步骤。跳到您尚未完成的第一步。 1. [集成您的电子商务平台](#h_01J3FXGG9SYS0RNVA554MN7QR1)
2. [从您过去的提供商导入数据](#h_01J3FXGG9S4AE7XR6TXEKVP7HN)
3. [创建评论流程](#h_01J3FXGG9SKNET9BDV5YXZGM1C)
4. [测试您的设置](#h_01J3FXGG9S4F4WTKSA0H4YATGP)
5. [切入Klaviyo评论](#h_01J3FXGG9SVB6SCS27NV20E1NH)
6. [实施最佳实践](#h_01J3FXGG9S3TXTD2AJ5C2NF5V4)
7. [回顾你的表现](#h_01J3FXGG9SNJVTCSDE7XE41K08)

## 1. 集成您的电子商务平台

与您的电子商务平台集成涉及两个步骤：

1.添加Klaviyo评论应用程序。 2. 在您的网站上安装评论小部件。在安装 Klaviyo Reviews 之前，请确保您登录到正确的帐户。安装该应用程序允许 Klaviyo Reviews 与您的商店交换信息，例如订单活动和网站流量。如果您没有看到下面列出的电子商务平台，则说明您的商店尚无法使用 Klaviyo Reviews。 - [安装适用于 Shopify 的 Klaviyo Reviews 应用程序](https://apps.shopify.com/klaviyo-reviews)
- [安装 WooCommerce 的 Klaviyo 评论插件](https://help.klaviyo.com/hc/en-us/articles/26922347702939)

  安装应用程序后，将 Klaviyo Reviews 小部件添加到您的商店。小部件向网站访问者显示评论信息，例如产品的星级或过去客户的评论。请按照适合您的平台和主题类型的小部件安装说明进行操作：
- [如何在 Shopify 2.0 主题上安装 Klaviyo Reviews 小部件](https://help.klaviyo.com/hc/en-us/articles/16318951826331)
- [如何在 Shopify 上安装 Klaviyo Reviews 小部件（复古主题和无头）](https://help.klaviyo.com/hc/en-us/articles/16318891028635)
- [如何在 WooCommerce 上安装 Klaviyo 评论小部件](https://help.klaviyo.com/hc/en-us/articles/26922347702939)

提示：在草稿主题上安装这些小部件，以便您有机会在设置它们之前对其进行测试。请注意，Klaviyo 无法检测草稿主题上的小部件，因此您可能会看到一条应用内消息，指示您的小部件尚未安装，直到您设置草稿主题为止。 ## 2. 从您过去的提供商处导入评论

导入过去的评论，这样您在迁移时就不会丢失任何数据。首先，从当前平台导出数据：

- [Yotpo](https://support.yotpo.com/docs/exporting-reviews-from-yotpo)
- [Okendo](https://help.octaneai.com/en/articles/7932726-exporting-reviews-from-okendo)
- [已盖章](https://stampedsupport.stamped.io/hc/en-us/articles/8839244356891-Exporting-Reviews-Checkout-Comments-or-NPS)
- [Reviews.io](https://support.reviews.io/en/articles/9185047-how-to-export-your-reviews)
- [Judge.me](https://help.judge.me/en/articles/8236266-exporting-reviews)
- [Loox](https://help.loox.io/article/21-how-do-i-export-my-reviews)

如果此处未列出您当前的平台，您可以参考其支持文档以了解如何导出评论。要将您的评论导入 Klaviyo：

1. 从 Klaviyo 侧边栏选择****评论****。 2. 导航至****所有评论****选项卡。 3. 选择****选项****。 4. 选择****导入评论****。 ![导入评论按钮](https://klaviyo.zendesk.com/hc/article_attachments/28705639211931)
5. 从提供的选项中选择您之前的评论平台。如果您没有看到您的平台列出，请选择****其他/不确定****。如果您选择****其他/不确定****，则必须先使用[我们的示例模板](https://help.klaviyo.com/hc/en-us/articles/16318811222555#h_01HS15C65Q8NZ2HNVTHR66R0PH)格式化您的CSV，然后再继续。 6. 选择****选择文件**** 或将 CSV 文件拖放到上传工具中。 7. 如果准确，请选中**我确认导入的评论是真实的**旁边的框。只有合法的评论才可以上传到 Klaviyo。 8. 检查上传的字段映射并根据需要进行调整。 9. 选择****下一步****。 如果您在导入时遇到问题，请参阅我们的文章[如何从其他平台导入评论数据](https://help.klaviyo.com/hc/en-us/articles/16318811222555)，以获取更多信息和故障排除帮助。 ## 3. 创建评论流程

有 2 个关键审核流程：

- ****审查请求流程****
  请最近的购买者评论他们订单中的产品。考虑提供激励措施（例如 15% 折扣、下一个订单免费送货、额外忠诚度积分），这可能会增加转化率。此流程由 **准备审核** 事件触发。 - ****审查后续流程****
  我们建议提供奖励以换取客户评论。使用由 **已提交评论** 事件触发的流程提交评论后，即可交付奖励。您可以通过导航到****流 > 创建流****并在流库中搜索**查看**来查找这些流的模板。所有带有 **Klaviyo Reviews** 标签的评论都使用 Klaviyo Reviews 指标。 ![评论流程](https://klaviyo.zendesk.com/hc/article_attachments/28705699645595)

了解[如何通过 Klaviyo 评论流程向客户请求评论](https://help.klaviyo.com/hc/en-us/articles/16319809379611)。此外，您可以创建一个[针对收到的每条负面评论提交客户服务票证的流程](https://help.klaviyo.com/hc/en-us/articles/16680027976731)。这可以让您的支持团队主动解决问题，并将不满意的审阅者转变为忠实的长期客户。 ## 4. 测试您的设置

为了确保您准备好切换到 Klaviyo Reviews，请测试以下内容：

- 检查所有评论小部件是否正确显示在您的草稿主题上，并显示您导入的任何评论。 - 预览审核请求中的消息并审核后续流程，以确保它们符合您的品牌并按需要显示。 - 确认您的[审核时间设置](https://help.klaviyo.com/hc/en-us/articles/16682549669403) 对您的产品有意义。默认情况下，审核请求会在订单交付后 7 天发送。 ## 5. 切换到 Klaviyo 评论

一旦您测试完所有内容并准备好上线 Klaviyo Reviews，请遵循以下清单：

1. 选择适合您订单量的[Klaviyo Reviews计划](https://help.klaviyo.com/hc/en-us/articles/115000976672#01H84M7N01NF4JEY8DJC88PC31)。 2. 可选：如果自您最初从之前的平台导入评论以来已经过去了几天或更长时间，请[导入此后您收到的任何新评论](https://help.klaviyo.com/hc/en-us/articles/16318811222555)。 3. 将您的评论流程从**手动**或**草稿**转为****实时****。 4. 发布安装了评论小部件的草稿商店主题。 5. 取消之前的评论平台并关闭所有自动化功能。 6. 可选：[请求对过去订单的评论](https://help.klaviyo.com/hc/en-us/articles/25930166202651)，以便您的评论请求流程立即开始发送。 ## 6. 实施最佳实践

设置核心 Klaviyo Reviews 功能后，请考虑使用高级功能：

- 向评论者询问[自定义问题](https://help.klaviyo.com/hc/en-us/articles/16319181846171)有关他们自己或他们对您的品牌的体验。 - [将您的评论同步](https://help.klaviyo.com/hc/en-us/articles/16681460907035) 到 Google Shopping feed。 - 了解如何[审核评论](https://help.klaviyo.com/hc/en-us/articles/19351110471323)。 - 当您收到负面评论时，[创建客户服务票](https://help.klaviyo.com/hc/en-us/articles/16680027976731)。 - 在您的电子邮件中[突出显示正面评论](https://help.klaviyo.com/hc/en-us/articles/18007373861915)。 - 使用[自定义CSS来实现高级样式选项](https://developers.klaviyo.com/en/docs/use_css_to_style_klaviyo_reviews_widgets)。 ## 7. 回顾你的表现

开始使用 Klaviyo Reviews 几周后，前往****评论 > 性能**** [评估您的评论计划是否成功](https://help.klaviyo.com/hc/en-us/articles/22567673911707)。在这里，您可以检查您请求和收到的评论数量，并查看网站访问者如何与评论内容互动。