---
id: "5486899706267"
title: "如何集成无头 Magento 2 设置"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/5486899706267-How-to-integrate-a-headless-Magento-2-setup"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:03Z"
language: "zh"
---
## 你将会学到

了解如何将 Klaviyo 与无头 Magento 2 设置集成。如果您使用 Magento 2 来支持电子商务商店的后端，但前端使用不同的框架（例如 React.js、Angular 等），那么以下信息与您相关。此集成需要 3 个步骤：

1. 通过 Klaviyo 的本机集成连接您的 Magento 2 商店，以同步订单、目录和订户数据。 2. 手动将代码片段添加到您的站点以启用现场跟踪功能。 3.（如果您的产品目录使用自定义 URL 结构）添加产品 URL 重写规则。 ## 连接 Klaviyo 的原生集成

首先，通过 Klaviyo 的本机集成连接您的 Magento 2 商店，以[按照 Magento 2 入门](https://help.klaviyo.com/hc/en-us/articles/115005254348)中的步骤同步订单、目录和订户数据。 Klaviyo 的 Magento 2 集成的很大一部分依赖于通过 Magento 的服务器端 API 获取数据。通常，这不会受到使用解耦前端的影响，并且本机集成将跟踪以下事件而无需进一步设置：

- 已下订单
- 已履行的订单
- 已完成装运
- 取消订单
- 已退款的订单
- 开始结账

  此外，请注意：
- **开始结帐** 事件将同步，前提是您在用户结帐时仍在创建报价并为其分配电子邮件地址。 - 如果您已启用同步订阅 Magento 2 新闻通讯表的客户，则同步应按预期进行。 ## 手动添加代码片段

如果您使用无头设置，则必须手动将 Klaviyo 的“Active on Site”JavaScript（也称为 **Klaviyo.js**）添加到您的站点。 Klaviyo.js 跟踪用户何时在您的网站上处于活动状态并启用 Klaviyo 表单。我们还提供了允许您执行以下操作的代码片段：

- ****查看的产品跟踪****
  跟踪用户何时查看您网站上的特定产品（可以在[浏览放弃流程](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow)中利用）。 - ****最近查看的项目跟踪****
  跟踪用户个人资料上最近查看的项目。 - ****添加到购物车跟踪****
  跟踪用户何时将商品添加到购物车。 - ****登录用户跟踪****
  如果您有帐户创建功能，请跟踪用户何时登录。 ### 站点上活动

添加以下 Klaviyo.js 代码片段，以便它出现在您网站的每个页面上。这将启用**Active on Site** 跟踪和 Klaviyo 表单。确保将 PUBLIC\_API\_KEY 替换为您的 [Klaviyo 公共 API 密钥](https://help.klaviyo.com/hc/en-us/articles/115005062267-How-to-Manage-Your-Account-s-API-Keys)。 ````
<script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
````

添加 Klaviyo.js 后，您需要在要添加以下片段之一（例如 **查看的产品**、**添加到购物车** 等）的任何页面上加载 [Klaviyo 对象](https://developers.klaviyo.com/en/docs/introduction_to_the_klaviyo_object)。 **klaviyo**对象每页只需加载一次。要加载 **klaviyo** 对象，请在必要的页面上手动安装以下代码片段：

````
<script type="text/javascript"> !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,参数)}}}}(); </脚本>
````

### 查看的产品

如果您想设置[浏览放弃流程](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow) 或根据产品浏览活动构建细分，则需要为 **查看的产品** 指标添加 JavaScript 事件跟踪。所有**查看的产品**指标都与用户配置文件相关联。在您的产品页面模板上，添加以下代码片段。 ````
<脚本类型=“文本/javascript”>
var klaviyo = window.klaviyo || []；
变量项 = {
     “产品名称”：项目.产品名称，
     “产品ID”：项目.产品ID，
     “SKU”：商品.SKU，
     “类别”：项目.类别，
     "ImageURL": 项目.ImageURL,
     "URL": 项目.URL,
     “品牌”：商品.品牌，
     “价格”：商品价格，
     “CompareAtPrice”：item.CompareAtPrice
 };
 klaviyo.track("查看过的产品", item);
 </脚本>
````

确保更新代码片段中 JSON 属性的值，以便它们动态地从该属性所需的相关信息中提取。 ### 最近查看的项目

此外，还有另一个片段允许将条目添加到用户个人资料上的可视“最近查看的项目”提要中。以下代码段可以直接添加到 **查看的产品** 代码段下方。确保将代码片段中的 item.\_\_\_ 替换为您的平台用于产品属性的任何项目对象。 ````
<脚本类型=“文本/javascript”>
var klaviyo = window.klaviyo || []；
klaviyo.trackViewedItem({
     “标题”：项目.产品名称，
     "ItemId": 商品.ProductID,
     “类别”：项目.类别，
     "ImageUrl": 项目.ImageURL,
     "Url": 项目.URL,
     “元数据”：{
       “品牌”：商品.品牌，
       “价格”：商品价格，
       “CompareAtPrice”：item.CompareAtPrice
     }
   });
 </脚本>
````

### 添加到购物车

如果您想向将商品添加到购物车但未进入结帐页面的访问者发送废弃购物车电子邮件，则您需要跟踪 **添加到购物车** 指标。必须识别客户（即 cookie）才能跟踪此事件。以下是一个示例请求，其中购物车已包含一件商品（小熊维尼），而另一件商品刚刚添加到购物车（两个城市的故事）：

````
<脚本类型=“文本/javascript”>
klaviyo.track("已添加到购物车", {
     “价值”：29.98，
     "AddedItemProductName": "两个城市的故事",
     "添加的商品产品 ID": "1112",
     "AddedItemSKU": "TALEOFTWO",
     "AddedItemCategories": ["小说", "经典", "儿童"],
     "AddedItemImageURL": "http://www.example.com/path/to/product/image2.png",
     "AddedItemURL": "http://www.example.com/path/to/product2",
     “添加商品价格”：19.99，
     “添加的项目数量”：1，
     “ItemNames”：[“小熊维尼”，“两个城市的故事”]，
     "CheckoutURL": "http://www.example.com/path/to/checkout",
     “项目”：[{
         “产品ID”：“1111”，
         “SKU”：“温尼波”，
         “产品名称”：“小熊维尼”，
         【数量】：1个，
         “商品价格”：9.99，
         “行总计”：9.99，
         "ProductURL": "http://www.example.com/path/to/product",
         "ImageURL": "http://www.example.com/path/to/product/image.png",
         “产品类别”：[“小说”、“儿童”]
       },
       {
         “产品ID”：“1112”，
         “SKU”：“TALEOFTWO”，
         “产品名称”：“两个城市的故事”，
         【数量】：1个，
         “商品价格”：19.99，
         “行总计”：19.99，
         "ProductURL": "http://www.example.com/path/to/product2",
         "ImageURL": "http://www.example.com/path/to/product/image2.png",
         "ProductCategories": ["小说", "经典"]
       }
     ]
   });
 </脚本>
````

### 登录用户

如果客户可以在您的网站上创建帐户，您可能需要添加额外的代码来识别和跟踪登录的用户。用户登录后应执行此代码。下面是一个可帮助您入门的示例脚本：

````
klaviyo.identify({
  “$email”：客户.email，
  "$first_name" : 客户.first_name,
  "$last_name" : 客户.last_name
});
````

## 添加产品URL重写规则

您的 Magento 2 产品目录应通过我们的本机集成与 Klaviyo 正常同步，但如果您使用自定义 URL 结构，则需要向代码库添加一些重写规则。默认的 Magento 2 产品 URL 遵循以下结构：

````
https://[您的商店]/catalog/product/view/id/[产品 ID]
````

如果您的商店使用如下 URL 结构：

````
https://[您的商店]/products/[产品名称]
````

然后，您需要向代码库添加一些重写规则，以将标准 Magento 2 产品链接重定向到您的自定义 URL 结构