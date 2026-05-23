---
id: "16681460907035"
title: "如何将评论同步到 Google 购物"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16681460907035-How-to-sync-reviews-to-Google-Shopping"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:48:55Z"
language: "zh"
---
了解如何将评价与 Google 购物同步，以便网络上的购物者可以查看您的客户评分。此过程可能需要 2 周以上才能完成，因此请尽早开始此过程。不过，如果您之前已通过其他提供商将评论同步到 Google 购物，则它们将在整个迁移过程中继续显示在搜索结果中。评论必须包含文本才能出现在评论源中。只有星级的评论将被排除在外。只有已发布产品的评论才会推送到 Google 购物。 ## Google 对评论的内容要求

谷歌的审核要求非常严格。如果您的评价 Feed 不符合这些条件，您的 Feed 可能会从 Google 购物中删除，并且您提交的评价也不会显示在那里。简而言之，这些要求是：

- 您的 Feed 必须包含至少 50 条评论。 - 您必须每月至少将所有产品评论同步到 Google 一次。 Klaviyo 建议每天同步。 - “所有评论”意味着您无法根据星级筛选评论。您必须分享低评价和高评价的评论。 Klaviyo 为您创建的评论源包含除被拒绝的评论之外的所有评论。 - 评论必须符合 Google 的内容指南。它们不能包含垃圾邮件、识别信息（电话号码、电子邮件、URL、全名和信用卡号等机密信息）、淫秽、冒犯性语言、员工或朋友撰写的评论、付费评论、非法内容、受版权保护的内容、抄袭评论、露骨色情材料、仇恨言论、其他产品的交叉推广、偏离主题的评论、冒充另一个实体、从最初编写的语言翻译的评论以及重复内容。详细了解 [Google 的评论内容政策](https://support.google.com/merchants/answer/6098512#zippy=%2Creview-feeds-must-adhere-to-content-policies)。 - 您的提要应包含相关的、高质量的评论。仅包含表情符号或“喜欢它！”等消息的评论对潜在客户没有帮助，可能不会显示。 - 您应该只收集和分享您拥有的评论。通过 Klaviyo 评论收集的评论符合此标准。 - 如果您在 Feed 中包含客户图像，则它们应该是高质量的、由您的客户（而不是您或第三方）拍摄的，并且经过最低程度的过滤。这是 Google 要求的概述。 [完整阅读 Google 的要求。](https://support.google.com/merchants/answer/6098512)

## 使用唯一的产品标识符

当您向 Google 提交评论时，这些评论会使用全球唯一产品标识符（例如全球贸易项目编号 (GTIN)）与相关产品进行匹配。如果 GTIN 不可用，Google 可以使用 SKU、品牌和制造商部件号 (MPN) 对或产品网址将评论与产品进行匹配。 ## 创建 Google Merchant Center 帐户

访问 [Google Merchant Center](https://merchants.google.com/signup) 并创建一个帐户。 ## 上传您的产品并等待批准

了解如何使用 [Google 文档](https://support.google.com/merchants/answer/7439058) 创建产品 Feed。或者，使用 [Shopify](https://apps.shopify.com/search?q=google%20shopping%20feed) 或 [WooCommerce](https://woocommerce.com/product-category/woocommerce-extensions/marketing-extensions/advertising-and-promotions/?q=google+product+feed&collections=product&page=1) 应用生成您的 Feed。将 Feed 提交给 Google 后，最多可能需要几周时间才能获得批准。同时，继续执行以下步骤。 ## 注册产品评级

要注册 Google Merchant 产品评级，请填写兴趣表。 1. 导航至[产品评级意向表](https://support.google.com/merchants/troubleshooter/10994881)。 2. 在**您是否与经批准的第三方评论聚合商合作？**下，选择****否****。这仅意味着您现在将通过手动流程上传评论。 Klaviyo 评论正在努力尽快成为经批准的第三方评论聚合器。 3. 根据您的业务完成其他问题。 4. 提交表单后，Google 将在几天内与您联系并提供以下消息：
   **您的聚合器“Klaviyo 评论”尚未加入产品评级计划，因此他们无法为您提交直接提要。 相反，您需要将直接产品评分 Feed 发送到 Google Merchant Center。**
   **如果您想通过回复此电子邮件发送直接产品评级源，请告诉我们。**
5. 回复此电子邮件，确认您将提交直接产品评级源。 6. 一旦 Google 确认，您将在 Google Merchant Center 帐户的 **营销** 下看到 **产品评论**** 选项卡。 ## 生成评论提要

1. 点击 Klaviyo 左侧导航栏中的****评论****。 2. 单击****设置****。 3. 单击****Google 购物联合****。 4. 打开**启用 Google Shopping Feed**。 5. 可选：打开 **使用 SKU 作为 MPN**，以使用您的产品 SKU 作为制造商部件号。默认关闭；如果您没有在电子商务平台中为产品设置 UPC，请打开此设置。 6. 单击****更新 Google 购物设置****。 7. 复制 **您的 Google Shopping Feed URL:** 下显示的 URL；您将在下一节中需要它。 ## 上传您的评论源

Klaviyo 的支持团队无法解决 Google Merchant Center 或 Google Shopping 的问题。如果您遇到任何问题，请联系 [Google 支持](https://support.google.com/merchants/?hl=en#topic=7259123)。 1. 导航至 Google Merchant Center。 2. 单击左侧菜单中的****营销****。 3. 选择****产品评论****。 4. 单击右上角的****产品评论源****。 5. 单击****+**** 添加提要。 6. 选择源的名称，然后选择****计划的获取****。 7. 单击****继续****。 8. 添加您从上一部分复制的 URL。 9. 对于 **获取频率**，选择 ****每日****。 10. 将**用户名**和**密码**字段留空。 11. 单击****创建源****。 Google 最多可能需要一个月的时间来审核该 Feed，并且在获得批准之前，新的评论将不会在 Google Shopping 中显示。及时回复来自 Google 的任何电子邮件以加快流程。 ### 我在 Google 购物上的现有评论会怎样？如果您从之前的评论提供商同步了现有的产品评论，那么它们将继续显示在 Google 购物搜索结果中。迁移到 Klaviyo 期间，您不会遇到任何 Google 购物停机或中断的情况。 ## 结果

完成这些步骤后，您的产品评论将自动显示在 Google 购物中。跨平台查看这些评论可以增强您品牌形象的有效性，并鼓励那些可能找不到您的浏览器访问您的商店。