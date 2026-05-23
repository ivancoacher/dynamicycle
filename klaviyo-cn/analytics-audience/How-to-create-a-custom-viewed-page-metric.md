---
id: "360059075151"
title: "如何创建自定义查看页面指标"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360059075151-How-to-create-a-custom-viewed-page-metric"
section: "Build and use metrics"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:53Z"
language: "zh"
---
## 你将会学到

了解如何创建自定义**查看的页面**指标并了解客户何时访问您网站上的非产品页面。 ## 开始之前

在继续阅读本文之前，请确保您已将电子商务平台（例如 [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)）与 Klaviyo 集成。将以下 JavaScript 代码段添加到您想要跟踪其**查看页面** 指标的网站的每个页面非常重要。此代码段适用于登陆页面和任何其他网站页面。 ## 安装代码片段

1. 将下面的完整代码段复制并粘贴到您的页面文件中。 2. 然后使用更新的代码保存并发布您的网站文件。 ````
<脚本类型=“文本/javascript”>
//在页面加载时初始化 Klaviyo 对象的脚本
!function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,参数)}}}}(); </脚本>
<脚本类型=“文本/javascript”>
//跟踪查看页面的脚本
klaviyo.track("查看过的页面", {
   页面名称：“关于我们”
});
</脚本>
````

将代码段添加到您的网站后，它将记录一个自定义 **查看的页面** 指标，其中属性名称 **PageName** 等于值“关于我们”。 ### 更改 **PageName** 值

您可以更改上面的默认值以代表您网站上的另一个页面名称。 1. 删除默认的“关于我们??”值。 2. 添加引号内包含的所需文本。例如，如果您想跟踪对品牌故事页面的访问，则可以使用“客户故事”作为值。 ### 更改 **查看的页面** 值

您可以更改 **查看的页面** 值来表示另一个值（例如，**访问的页面**、**跟踪的页面** 等）。 1. 删除默认的 **查看的页面** 值。 2. 添加引号内包含的所需文本。 ### 通过 URL 跟踪查看的页面

如果您想跟踪 **按 URL 查看的页面**而不是按页面标题，您可以使用下面的备用代码片段。请注意，**您要跟踪的页面**应包含引号，并且是您要跟踪的页面的 URL。 ````
<脚本类型=“文本/javascript”>
//在页面加载时初始化 Klaviyo 对象的脚本
!function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,参数)}}}}(); </脚本>
<脚本类型=“文本/javascript”>
//跟踪查看页面的脚本
klaviyo.track("查看过的页面", {
      网址：window.location.href
});
</脚本>
````

## 测试您查看的页面跟踪

要测试您的 **查看页面** 跟踪是否有效，请确保您的页面已发布，并且您已将“?utm\_email=youremail@example.com”修改为页面的 URL，以对您自己进行 cookie 并跟踪您的活动。 1. 访问您的页面后，进入您的 Klaviyo 帐户。 2. 导航至****分析 > 指标****。 3. 在上面的字段中搜索 **查看的页面**（或者您为此指标使用的任何替代名称）。 ![metric_search_field.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720893682843)

4. 单击您的 ******查看页面****** 指标（或您正在使用的任何指标）。 5. 选择****活动源****选项卡。然后，您可以检查您的指标是否正在跟踪，如下例所示。 ![viewed_metric_example.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720848624795)

如果您可以查看您的活动，则意味着指标已成功跟踪。如果您没有看到自己的活动，请尝试在 Klaviyo 中重新加载页面。 对于 Shopify 商店，根据您在 Shopify 中的客户隐私设置，Klaviyo 可能不会跟踪您位于欧盟、欧洲经济区、英国和瑞士的 Shopify 商店的访问者的现场活动，除非他们已表示同意。 ## 其他资源

- [了解 Klaviyo 中的 cookies](https://help.klaviyo.com/hc/en-us/articles/360034666712-About-Cookies-in-Klaviyo)
- [Klaviyo现场跟踪入门](https://help.klaviyo.com/hc/en-us/articles/115005076767)
- [设置基于 API 的网站活动事件](https://developers.klaviyo.com/en/v1-2/docs/guide-to-setting-up-api-based-website-activity-events)