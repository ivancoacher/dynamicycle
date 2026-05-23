---
id: "16318891028635"
title: "如何在 Shopify 上安装 Klaviyo Reviews（复古主题和无头）"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16318891028635-How-to-install-Klaviyo-Reviews-on-Shopify-vintage-themes-and-headless"
section: "Getting started with reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:48:48Z"
language: "zh"
---
## 你将会学到

了解如何使用老式 Shopify 主题或无头架构安装 Klaviyo Reviews。此过程涉及复制多个代码片段并将其粘贴到您网站的代码中。如果您使用的是 Shopify 2.0 主题，则无需使用代码即可安装 Klaviyo Reviews。请参阅我们关于 [Klaviyo 评论入门](https://help.klaviyo.com/hc/en-us/articles/15937542819355) 的文章以了解更多信息。如果您使用 WooCommerce，请了解如何[安装 WooCommerce 的 Klaviyo Reviews](https://help.klaviyo.com/hc/en-us/articles/26922347702939)。此过程需要直接在 Shopify 中编辑您的主题文件。如果您自己不愿意这样做，请联系您的开发人员或[联系 Klaviyo 合作伙伴](https://connect.klaviyo.com/) 寻求帮助。 ## 开始之前

在将这些代码段粘贴到您网站的代码中之前，请[将 Klaviyo Reviews 应用添加](https://apps.shopify.com/klaviyo-reviews) 到您的 Shopify 商店。对于复古主题，[启用 Klaviyo 的现场跟踪](https://help.klaviyo.com/hc/en-us/articles/4425956184731)。 ## 在 Shopify 上使用无头架构进行安装

要将 Klaviyo 评论与无头 Shopify 商店集成，请将 Klaviyo 的 JavaScript 跟踪代码段（也称为 Klaviyo.js）添加到您想要添加评论小部件的所有页面（例如产品页面）。如果您配置了 Klaviyo 的现场跟踪或注册表单，您可能已经安装了此代码段。了解如何[为 Shopify 商店安装 Klaviyo.js](https://help.klaviyo.com/hc/en-us/articles/360020342232)。将此脚本添加到您的网站后，请继续将以下步骤中的代码片段复制到您网站的代码中。 ## 添加代码片段

下面的代码片段允许某些评论小部件出现在商店的不同区域。 -****星级小部件****显示特定产品的当前星级，通常安装在产品名称下方。 - **评论摘要小部件****显示一个图表，其中详细列出了为产品选择的所有评级、随评论提交的用户图像以及产品收到的最常见反馈。它通常安装在产品页面底部附近。 - **产品评论小部件****是评论摘要和评论列表小部件的组合。如果您将产品评论小部件添加到您的网站，则无需单独添加评论列表和评论摘要小部件。 - **评论列表小部件****显示所有已发布评论和客户问题的列表，以及搜索栏、过滤器、****撰写评论****按钮和****提出问题****按钮。它通常安装在评论摘要小部件的正下方。 - **特色评论轮播小部件****显示您所有产品的突出评论。这可以出现在您的主页、独立评论页面或网站上的任何其他位置。您可以选择此小部件中的评论。如果有的话，客户提交的图像会附在每次评论中；如果评论中未提交任何图片，则会使用您的产品图片。 - ****SEO/所有评论小部件**** 在一个页面上显示您对所有产品的所有评论。使用此小部件可以改进您的搜索引擎优化，并为潜在客户提供一个单一的位置来查看当前客户的喜好。此小部件通常添加到您网站上的独立**评论**页面。 ### 星级小部件

使用星级小部件突出显示产品的平均评级和收到的评论数量。 ![星级小部件](https://klaviyo.zendesk.com/hc/article_attachments/28715965547163)

要将此小部件安装在产品标题下方：

1. 打开您的 Shopify 商店后台。 2. 在**销售渠道**下单击****在线商店****。 3. 单击当前主题旁边的三点菜单 > ****复制**** 创建当前主题的克隆。 4. 从三点菜单中，单击****编辑代码****。 ![编辑代码按钮](https://klaviyo.zendesk.com/hc/article_attachments/28715972087707)
5. 在文件搜索栏中搜索“产品”并找到用于产品页面内容的文件。它可能是 **product.liquid**、**product-template.liquid** 或​​类似的东西。 （如果您使用自定义产品页面模板，请选择该模板。）
   ![搜索产品页面内容](https://klaviyo.zendesk.com/hc/article_attachments/28715965535899)
6. 选择文件，然后搜索 {{product.title }} 以找到显示产品标题的代码。 ![产品标题代码](https://klaviyo.zendesk.com/hc/article_attachments/28715972092955)
7. 在此代码下方添加新行。 8. 在新行中粘贴以下代码片段：
   `<div class="klaviyo-star- rating-widget" data-id="{{product.id}}" data-product-title="{{product.title}}" data-product-type="{{product.type}}"></div>`
   ![星级代码片段](https://klaviyo.zendesk.com/hc/article_attachments/28715972095899)
9. 单击****保存****。 10. 单击****预览商店****。 11. 导航到商店预览中的产品页面。您应该在产品标题下方看到一个星形小部件。 ### 产品评论小部件

使用评论摘要和评论列表小部件（或仅产品评论小部件）为您网站上的每个产品添加所有已发布评论的摘要和列表。 ![带图片的评论摘要](https://klaviyo.zendesk.com/hc/article_attachments/28715972112795)

要单独安装摘要和列表小部件，请转到下面的[单独的审阅摘要和审阅列表小部件](#h_01H3W6P97SQ00C8CRMYP66RBZX) 部分。要安装此小部件：

1. 打开您的 Shopify 商店后台。 2. 在**销售渠道**下单击****在线商店****。 3. 单击当前主题旁边的****自定义****进行编辑，或者如果您想编辑草稿主题而不是实时主题，请单击三点菜单 > ****复制****。 4. 从三点菜单中，单击****编辑代码****。 ![编辑代码选项](https://klaviyo.zendesk.com/hc/article_attachments/28715972087707)
5. 在文件搜索栏中搜索“产品”并找到用于产品页面内容的文件。它可能是 **product.liquid**、**product-template.liquid** 或​​类似的东西。 （如果您使用自定义产品页面模板，请选择该模板。）
   ![定位产品页面内容](https://klaviyo.zendesk.com/hc/article_attachments/28715965535899)
6. 选择文件，然后导航到最底部（或您希望显示评论摘要和列表小部件的任何位置）。 7. 添加新行，然后粘贴以下代码片段：
   `<div id="klaviyo-reviews-all" data-id="{{product.id}}"></div>`
   ![所有评论代码片段](https://klaviyo.zendesk.com/hc/article_attachments/28715965542555)
8. 单击****保存****。 9. 单击****预览商店****。 10. 导航到商店预览中的产品页面，查找有评论的产品。您应该在页面底部附近看到评论摘要和列表视图小部件。 ### 单独的评论摘要和评论列表小部件

如果您希望单独安装评论摘要和评论列表小部件（而不是像上面部分所述一起安装），请使用以下代码片段：

#### 查看摘要小部件

`<div id="klaviyo-reviews-summary" data-id="{{product.id}}"></div>`

#### 评论列表小部件

`<div id="klaviyo-reviews-list" data-id="{{product.id}}"></div>`

### 特色评论轮播小部件（可选）

精选评论轮播会在您选择的任何页面（例如您的主页）上显示手动选择的评论。 ![特色评论轮播小部件](https://klaviyo.zendesk.com/hc/article_attachments/28715965550363)

要添加显示所有精选评论的轮播，您必须首先选择要推荐的评论。 1. 在 Klaviyo 的主导航中，选择****评论****。 2. 单击****所有评论****。 3. 在您想要推荐的评论旁边，单击****推荐****。 ![发表评论的选项](https://klaviyo.zendesk.com/hc/article_attachments/28715972110235)

选择要在网站上展示的多条评论后，您可以在任何页面上安装评论轮播小部件。导航到您想要显示轮播的页面，然后将以下代码段粘贴到该页面的代码中：

`<div id="klaviyo-featured-reviews-carousel"></div>`

## SEO / 所有评论小部件（可选）

SEO/所有评论小部件显示每个产品的所有已发布评论。将其添加到独立的评论页面或“关于”页面。 `<div id="klaviyo-reviews-all" data-id="all"></div>`

![所有评论小部件](https://klaviyo.zendesk.com/hc/article_attachments/28715972114843)

## 结果

安装本文中概述的小部件并启用新主题后，您的评论将显示在产品页面（以及您安装了它们的网站上的任何其他页面）。