---
id: "360015392131"
title: "如何使用 Google 跟踪代码管理器添加 Klaviyo 现场跟踪"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360015392131-How-to-add-Klaviyo-onsite-tracking-using-Google-Tag-Manager"
section: "Build and use metrics"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:43Z"
language: "zh"
---
## 你将会学到

了解如何使用 [Google 跟踪代码管理器](https://marketingplatform.google.com/about/tag-manager/) 将 [Klaviyo 的现场跟踪代码段](https://help.klaviyo.com/hc/en-us/articles/115005076767-Klaviyo-Web-Tracking) 添加到您的网站。一些网站所有者使用 Google 跟踪代码管理器作为单点来管理他们需要添加到其网站的所有第三方网络代码段。 Klaviyo 的现场跟踪属于此类，可以通过 Google 跟踪代码管理器添加和管理。 ## 开始之前

如果您使用 Google 跟踪代码管理器和 Shopify 安装 Klaviyo 的现场跟踪代码段，请[在 Shopify 上使用 Google 跟踪代码管理器进行检查](https://help.klaviyo.com/hc/en-us/articles/360015392131#h_01HTFQ2G4BPPR9P1WHEQ1FWQR3)。 ## 设置 Google 跟踪代码管理器

如果您已经创建了 Google 跟踪代码管理器帐户，则可以跳过这些步骤并前往[创建代码](#h_01GMKGSDWVDMW5DJF0RAQCWE2E) 部分。 1. 创建一个 Google 跟踪代码管理器帐户。 2. 将安装脚本添加到您的站点。 ![在 Google 跟踪代码管理器中，需要将两个安装脚本复制到网站 html 的头部和正文中](https://klaviyo.zendesk.com/hc/article_attachments/28705663190299)

如果您不熟悉使用 Google 跟踪代码管理器，请[查看有关设置帐户并将安装脚本添加到您的网站的文档](https://support.google.com/tagmanager/answer/6103696)。 ## 创建一个新标签

1. 在您站点的工作区中，为 Klaviyo **Active on Site** 跟踪创建一个新触发器。我们建议为您的**网站活跃**和**查看的产品**跟踪创建一个单独的触发器。这是因为**查看的产品**跟踪只会在您的产品页面上触发，而**网站上活动**跟踪应在您网站的每个页面上触发。 2. 选择****自定义 HTML**** 作为标记类型。 ![在站点的工作区中打开选择标签类型菜单并选择自定义 html](https://klaviyo.zendesk.com/hc/article_attachments/28705636475419)

3. 要在 Klaviyo 中找到您的 **Active on Site** 代码段，请单击您的帐户菜单并选择 ****Integrations.****4。从这里点击右上角的****设置网络跟踪****按钮****.****！[在设置的集成页面内，用于设置网络跟踪的右上角按钮突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28705663185819)

5. 复制第一个片段。 ![突出显示要复制的网络跟踪代码段示例](https://klaviyo.zendesk.com/hc/article_attachments/28705636471067)

6. 从 Google 跟踪代码管理器中，将 Klaviyo **Active on Site** 代码段粘贴到 HTML 框中。 ![活跃的网站网络跟踪代码段已粘贴到 Google 跟踪代码管理器中的 HTML 框中](https://klaviyo.zendesk.com/hc/article_attachments/28705636463131)

7. 将触发器设置为在所有页面的页面视图上触发。这可确保每当客户查看您网站上的页面时，您的 **Active on Site** 代码段就会触发。 ![选择页面视图触发器示例作为所有网站页面的触发器](https://klaviyo.zendesk.com/hc/article_attachments/28705636456347)

8. 保存新标签。这样就完成了使用 Google 跟踪代码管理器添加 **Active on Site** 跟踪代码段的过程。您可以使用相同的方法添加您的 **查看的产品** 代码段。将触发器修改为仅在包含您的产品的页面上触发。在某些网站上，这可以通过将触发器限制为仅在 URL 包含单词“产品”的页面上触发来实现。 ![URL 中突出显示 /products 的示例商业网站](https://klaviyo.zendesk.com/hc/article_attachments/28705663198363)

## 测试您的现场跟踪

1. 导航到您的网站。 2. 将以下内容添加到 URL 末尾：

`?utm_email=klaviyogreen@gmail.com`

您可以将“klaviyogreen@gmail.com”替换为您自己的电子邮件地址。按 Enter 键重新加载页面。 3. 然后，在您的 Klaviyo 帐户中，导航至****仪表板 > 活动源****。如果您的现场跟踪安装正确，您将在您在上面的 URL 参数中输入的电子邮件的活动源顶部看到一个新的 **Active on Site** 事件。 ![在活动源部分内显示网站上处于活动状态的配置文件，表明跟踪正在工作](https://klaviyo.zendesk.com/hc/article_attachments/28705636483867)

如果您在触发 **查看的产品** 事件时遇到问题，请确保您的标签设置为按特定顺序触发。 您始终希望您的 **Active on Site** 代码段在 **Viewed Product** 代码段之前触发。如果您在尝试在 Google 跟踪代码管理器中保存任一跟踪代码段时遇到错误，则必须将代码段直接粘贴到您的网站中。 ## 在 Shopify 上使用 Google 跟踪代码管理器

使用 Shopify，而不是使用 Google 跟踪代码管理器，我们鼓励您通过 [Shopify 中嵌入的 Klaviyo 应用程序](https://klaviyo.zendesk.com/hc/en-us/articles/4425956184731) 启用 Klaviyo 现场跟踪。应用程序嵌入可启用“网站上活动”和“查看过的产品”跟踪，前提是它已打开并且在集成设置页面上选中了“查看过的产品”设置。我们的 Shopify 集成还可以通过 **跟踪行为事件** 设置实现 **提交的搜索**、**查看的收藏** 和 **添加到购物车**。如果您想通过 Google 跟踪代码管理器添加现场跟踪，请确保首先关闭应用程序嵌入。然后，使用下面的代码片段。 “集合”无法通过 Shopify 的 AJAX API 获得，因此 Shopify 产品标签（标签）将在下面的代码片段中捕获。 ````
<脚本类型=“文本/javascript”>
//在页面加载时初始化Klaviyo对象
!function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,参数)}}}}(); </脚本>
<脚本类型=“文本/javascript”>
//查看过的产品
var klaviyo = window.klaviyo || []；
产品句柄 = location.href.split( '/' ).pop().split( '?' )[0];
fetch('/products/'+product_handle+'.js').then(function(response){return response.json()})
.then(函数(产品){
  变量项 = {
    名称：产品.标题，
    产品ID：产品.id，
    标签： 产品.标签,
    图片URL：“https：”+product.featured_image，
    URL: location.href.split( '/' )[0] + '//' + location.href.split( '/' )[2]+product.url,
    品牌：产品.供应商，
    价格：产品.价格/100，
    比较价格：product.compare_at_price_max/100
  };
  klaviyo.track("查看过的产品", item);
  klaviyo.trackViewedItem({
    标题：项目.名称，
    ItemId：item.ProductID，
    标签： item.Categories,
    ImageUrl: 项目.ImageURL,
    网址：项目.URL，
    元数据：{
      品牌: item.Brand,
      价格：商品.价格，
      比较价格： item.比较价格
    }
  });
// 如果您还想添加“已添加到购物车”代码段，请将其放在此处，不带脚本标签
})
.catch(函数(e){
  console.log('Klaviyo 无法跟踪查看的产品。请联系 Klaviyo 支持寻求帮助。')
});
</脚本>
````

根据您在 Shopify 中的客户隐私设置，Klaviyo 可能不会跟踪您位于欧盟、欧洲经济区、英国和瑞士的 Shopify 商店的访问者的现场活动，除非他们已表示同意。 ## 其他资源

- [Klaviyo 现场跟踪入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005076767)
- [了解消息转化跟踪](https://klaviyo.zendesk.com/hc/en-us/articles/115005248128)
- [创建浏览放弃流程指南](https://klaviyo.zendesk.com/hc/en-us/articles/115002775252)