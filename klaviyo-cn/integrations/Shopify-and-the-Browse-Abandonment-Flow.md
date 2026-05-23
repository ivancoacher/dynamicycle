---
id: "115005080787"
title: "Shopify 和浏览放弃流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005080787-Shopify-and-the-Browse-Abandonment-Flow"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "zh"
---
## 概述

浏览放弃电子邮件与放弃的购物车类似，但当可识别的浏览器访问产品页面时会触发 - 访问者不必将商品添加到他/她的购物车即可触发此流程，网站访问者所要做的就是查看该商品。由于访问产品页面并不完全表明与将商品添加到购物车相同的兴趣程度，因此我们建议在您的浏览放弃电子邮件中包含相关或类似的产品以扩大您的网络。在浏览放弃电子邮件中添加折扣代码还可以帮助将休闲浏览者转变为热情的客户。以下指南将引导您了解如何启动并运行新的浏览放弃流程。 ## 添加已查看的产品跟踪代码

首先，您需要将一段代码添加到 Shopify 商店的后端。此代码将添加到您商店的product.liquid 模板中。 |  |
| --- |
|注意：如果您已将代码添加到product.liquid 模板中以启用产品页面跟踪，则可能需要将之前添加的代码片段替换为本指南中共享的新更新代码。 |

通过在 Shopify 管理门户中导航到 **在线商店** --> **主题** --> **编辑 HTML/CSS**--> **product.liquid** 来查找商店的 Product.liquid 模板。单击进入您的product.liquid 模板并向下滚动到最底部。您将在此处放置以下代码：

````
<脚本文本=“文本/javascript”>
 var _learnq = _learnq || []；
 变量项 = {
   名称：{{product.title|json}}，
   产品ID：{{product.id|json}}，
   类别：{{product.collections|map:'title'|json }},
   ImageURL: "https:{{ Product.featured_image.src|img_url:'grande' }}",
   网址：“{{shop.secure_url}}{{product.url}}”，
   品牌：{{product.vendor|json}}，
   价格：{{product.price|money|json }}，
   CompareAtPrice：{{product.compare_at_price_max|money|json }}
 };

 _learnq.push(['track', '查看过的产品', item]);

 _learnq.push(['trackViewedItem', {
   标题：项目.名称，
   ItemId：item.ProductID，
   类别： 项目.类别，
   ImageUrl: 项目.ImageURL,
   网址：项目.URL，
   元数据：{
     品牌: item.Brand,
     价格：商品.价格，
     比较价格： item.比较价格
   }
 }]);
</脚本>
````

将此代码粘贴到product.liquid 模板的底部后，单击“**保存**”。请记住：如果您之前在product.liquid 模板中添加了一段非常短的代码片段以启用产品页面跟踪，则可能需要将其替换为上面的代码片段。更新后的代码在您的product.liquid 模板中将如下所示：

![647553](https://klaviyo.zendesk.com/hc/article_attachments/28717849944987)

## 监控“查看的产品”指标

|  |
| --- |
|注意：当您将上面的 Klaviyo 跟踪代码段添加到您的网站时，我们不会跟踪所有网站访问者的**查看的产品**事件。我们只能跟踪“已知浏览器”的此事件。我们可以通过两种关键方式识别网站访问者以进行网络跟踪： - 当有人点击 Klaviyo 电子邮件发送到您的网站时 - 当有人在某个时候通过 Klaviyo 表单订阅/选择加入时 |

将此代码段粘贴并保存到商店的product.liquid 模板中后，当已知访问者浏览您的产品页面时，“查看的产品”数据应开始填充到您的 Klaviyo 帐户中。要检查此指标，请单击您帐户的**[仪表板](https://www.klaviyo.com/dashboard)**并导航到**活动源**选项卡。在这里，您将看到一个标有“显示源”的下拉菜单。调整此下拉列表以过滤指标“查看的产品”。 ![647543](https://klaviyo.zendesk.com/hc/article_attachments/28717849946139)

如果没有可用数据，请浏览您自己的网站并单击查看不同的产品，自行测试该指标。您应该看到这些数据开始流入 Klaviyo。在您发送第一个营销活动或开始扩大订阅者列表后，随着 Klaviyo 能够识别越来越多的人与您的网站互动，此浏览数据将会增长。如果您担心此代码片段无法正常运行，请[联系我们的成功团队](https://help.klaviyo.com/hc/en-us/requests/new)，我们将帮助您排除故障！ ## 设置浏览放弃流程

如果您的帐户中未预先填充 Klaviyo 的最佳实践浏览放弃流程，您现在可以从 **流程** 选项卡的 **浏览 I****deas** 部分获取此流程。 ![647541](https://klaviyo.zendesk.com/hc/article_attachments/28717810315675)

|  |
| --- |
| [参考本指南](https://docs.klaviyo.com/customer/portal/articles/2475177#section4)，了解有关如何自定义 Klaviyo 的浏览放弃流程或构建自己的放弃流程的信息！ |