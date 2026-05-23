---
id: "22500017241883"
title: "如何使用 Tapcart 将 Klaviyo Reviews 小部件添加到您的移动应用程序"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/22500017241883-How-to-add-Klaviyo-Reviews-widgets-to-your-mobile-app-using-Tapcart"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:29Z"
language: "zh"
---
## 你将会学到

了解如何将 Klaviyo Reviews 小部件添加到使用 Tapcart 构建的移动应用程序中。可以使用自定义块将这些小部件添加到您的 Tapcart 应用程序中：

- ****星级小部件****
  仅产品页面；显示产品的整体星级
- ****产品评论小部件****
  仅产品页面；显示产品所有评论的摘要和列表，以及用于提问或留下评论的按钮
- ****特色评论轮播小部件****
  任何页面；显示多个产品的精选评论

Tapcart 仅适用于使用 Shopify 建立的商店。 ## 开始之前

此流程仅适用于以下公司：

- 已经使用 Tapcart 构建了移动应用程序
- 使用 Tapcart Enterprise 计划
- 有一个积极的 Klaviyo 评论计划

如果您尚未设置 Klaviyo Reviews，请参阅我们关于 [Klaviyo Reviews 入门] 的文章(https://help.klaviyo.com/hc/en-us/articles/15937542819355)。 ## 使用 Tapcart 中的自定义块添加 Klaviyo Reviews 小部件

按照以下步骤在 Tapcart 中添加任何评论小部件。您需要对所有 3 个小部件重复这些步骤（即创建单独的自定义块）。 1. 打开 Tapcart 编辑器。 2. 在**App Studio**中，从**设计块**切换到****自定义块****。 ![启动块编辑器](https://klaviyo.zendesk.com/hc/article_attachments/28723685323035)
3. 单击****启动块编辑器**** 以创建新的自定义块。 4. 将小部件命名为清晰的名称，例如 **Klaviyo 星级自定义块**。 5. 在块编辑器的 ****JS**** 选项卡中，添加以下代码片段。将 PUBLIC\_API\_KEY 替换为您的 [6 个字符的 Klaviyo 站点 ID](https://help.klaviyo.com/hc/en-us/articles/115005062267)。 ````
   var script = document.createElement('script');
   script.type = '文本/javascript';
   script.async = true;
   script.src = 'https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js&module=reviews';
   document.head.appendChild(脚本);
   ````
6. 在块编辑器的 ****HTML**** 选项卡中，粘贴您要添加的小部件的代码段（例如，星级小部件）。找到下面的代码片段：
   1. [星级小部件代码](https://klaviyo.zendesk.com/hc/en-us/articles/undefined#h_01HNDJ2XVMJGSX6T4QKBBDDBZ2)
   2. [产品评论小部件代码](https://klaviyo.zendesk.com/hc/en-us/articles/undefined#h_01HNDJ2XVMZEZKE2MH9KF46K6M)
   3. [特色评论轮播小部件代码](https://klaviyo.zendesk.com/hc/en-us/articles/undefined#h_01HNDJ2XVMV6D8422M9NF6BSS4)
      ![Tapcart HTML 选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28723663126811)
7. 单击****保存****。 8. 单击****关闭****退出编辑器。 9. 从****App Studio**** 下拉列表中，选择****产品详细信息****。 ![产品详情页](https://klaviyo.zendesk.com/hc/article_attachments/28723663130907)

   星级评定和产品评论小部件需要此步骤。您可以将特色评论小部件放置在任何应用程序页面上。 10. 将刚刚创建的保存的自定义块拖到模板中。 11、编辑器可能无法直接加载widget；相反，您将看到纯文本形式的块名称。这是预料之中的。 12. 单击****预览您的应用程序****并导航到您添加应用程序的页面。请注意，该小部件正确显示。 ****问问题**** 和****发表评论**** 按钮在预览模式下不起作用。将更改发布到应用程序后，单击应用程序中的这些按钮将打开一个新的浏览器选项卡。 ## 代码片段

### 星级小部件

````
<div class="klaviyo-star- rating-widget" data-id="{{product.id}}" data-product-title="{{product.title}}" data-product-type="{{product.type}}"></div>
````

### 产品评论小部件

````
<div id="klaviyo-reviews-all" data-id="{{product.id}}"></div>
````

### 精选评论轮播

````
<div id="klaviyo-featured-reviews-carousel"></div>
````

## 预览应用程序小部件

Klaviyo Reviews 小部件不会自动出现在 Tapcart 预览中，但会在您的应用程序上正确加载。这是因为小部件需要真实的产品 ID 才能知道要显示哪些评论。要预览小部件，请在 Tapcart 编辑器的 **变量预览值** 字段中添加产品 ID 变量。 1. 在 Tapcart **App Studio** 中，选择 ****自定义**** 以查看您的自定义小部件。 2. 单击审阅小部件块之一旁边的三点图标，然后单击****启动编辑器****。 3. 单击****设置****。 ![设置按钮](https://klaviyo.zendesk.com/hc/article_attachments/28723663139099)
4. 滚动或搜索 JSON 以查找 **product** 对象中的 **id** 变量。请注意，其他对象中还有其他 **id** 变量；您只需编辑此处显示的产品 ID。 ![代码中的产品ID变量](https://klaviyo.zendesk.com/hc/article_attachments/28723663133979)
5. 将示例产品 ID 替换为您商店中至少有 1 条评论的产品的 ID。要查找产品 ID，请导航至 Klaviyo 中的****内容 > 产品****，然后复制项目 ID。 ![Klaviyo 中的项目 ID](https://klaviyo.zendesk.com/hc/article_attachments/28723663136667)
6. 单击****保存****。 7. 对其他审阅小组件块重复这些步骤。 8. 如果预览没有立即正确显示，请刷新编辑器。 ## 样式应用程序小部件

主窗口小部件编辑器中所做的任何更改都将应用于您的网站和应用程序。要将更改仅应用到您的应用程序，请将自定义 CSS 添加到 Tapcart 中自定义块编辑器的 ****CSS**** 选项卡。了解如何使用自定义 CSS 来设置 Klaviyo Reviews 小部件的样式。