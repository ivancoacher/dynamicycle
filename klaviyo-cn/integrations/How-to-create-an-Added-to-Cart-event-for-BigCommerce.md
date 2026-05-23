---
id: "360024310292"
title: "如何为 BigCommerce 创建“添加到购物车”事件"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360024310292-How-to-create-an-Added-to-Cart-event-for-BigCommerce"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "zh"
---
## 你将会学到

了解如何为 BigCommerce 创建 **添加到购物车** 事件，以跟踪客户何时将商品添加到购物车并触发放弃的购物车流。 **添加到购物车** 当您与 BigCommerce 集成时，事件不会自动跟踪；您必须首先将 JavaScript 代码段（包含在本指南中）添加（并可能修改）到您的 BigCommerce 主题文件中。 - 您不需要创建**添加到购物车**事件来发送废弃的购物车流程； **添加到购物车**废弃购物车流程与标准废弃购物车流程是分开的，后者由**开始结账**触发。 - 当客户将商品添加到购物车后在结帐过程中输入电子邮件时，Klaviyo 的内置 BigCommerce 集成已经跟踪 **开始结帐** 事件。 ## 开始之前

**添加到购物车**事件仅跟踪之前[由 Klaviyo 进行 cookie](https://help.klaviyo.com/hc/en-us/articles/360034666712-About-Cookies-in-Klaviyo) 的用户。您必须已安装 **查看的产品** 跟踪，才能确保 **添加到购物车** 事件正常运行。通常，Klaviyo 客户会在 BigCommerce 集成过程中安装此程序，并且可以在我们的[集成文章](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#add-viewed-product-tracking4)中找到说明。 ## 添加片段

1. 打开您的 BigCommerce 后台并导航至****店面 > 我的主题****。 2. 找到您当前的主题，然后单击****高级设置****下拉列表。 3. 搜索****product.html**** 文件并单击将其打开。 4. 将以下代码段直接粘贴到 Klaviyo **查看的产品** 代码段下方。 ````
   <脚本文本=“文本/javascript”>
   //在页面加载时立即初始化 Klaviyo 对象
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,参数)}}}}(); </脚本>
   <脚本文本=“文本/javascript”>
   //添加到购物车
   var klaviyo = window.klaviyo || []；
   document.getElementById("form-action-addToCart").addEventListener('click',function (){
      klaviyo.track("已添加到购物车", item);
   });
   </脚本>
   ````
5. 接下来，检查是否需要修改代码片段。为此，您需要检查网站上“添加到购物车”按钮的 ID，并查看它是否与下面代码片段中突出显示的“添加到购物车”变量匹配，该变量的默认值为“form-action-addToCart”。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717387201051)
6. 要检查按钮的 ID，请打开站点的产品页面之一，右键单击“添加到购物车”按钮，然后选择****检查****。 ![带有演示项目 Smith Journal 的 BigCommerce 商店，右键单击菜单，在“添加到购物车”按钮上打开，其中“检查”以蓝色突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28717387183515)
7. 控制台将打开，显示“添加到购物车”按钮的源代码。下图显示了控制台中突出显示的“添加到购物车”按钮的 ID。 ![Chrome 控制台打开并添加到购物车按钮 ID 的 BigCommerce 商店演示项目，form-action-addToCart，突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28717387187867)
8. 此处显示的页面上按钮的 ID 与“form-action-addToCart”匹配，因此无需进行任何更改。 - 如果您网站上的“添加到购物车”按钮的 ID 不是“form-action-addToCart”，您需要更改引号内的变量文本以匹配按钮的 ID
9. 如果您的源代码未显示按钮 ID，请跳至[下一部分](https://help.klaviyo.com/hc/en-us/articles/360024310292#alternate-snippet-for--add-to-cart--button-without-a-button-id3)，并了解如何使用带有类符号而不是按钮符号的备用代码片段。 10. 完成后，保存 ****product.html**** 文件。您已完成添加代码片段，现在将跟踪 **添加到购物车** 事件。 ## 没有按钮 ID 的“添加到购物车”按钮的备用代码片段

出于样式原因，某些网站对“添加到购物车”按钮使用类符号而不是按钮 ID。如果您的“添加到购物车**”**按钮没有按钮 ID（您可以按照上一节中的步骤确定），而是使用类表示法，则您应该使用下面的备用代码片段来启用 **添加到购物车** 事件。 1. 如果您的按钮是通过类表示法定义的，请将以下备用代码片段粘贴到 ****product.html**** 文件的底部：

   ````
   <脚本文本=“文本/javascript”>
   //在页面加载时立即初始化 Klaviyo 对象
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,参数)}}}}(); </脚本>
   <脚本文本=“文本/javascript”>
   //查看过的产品
   var klaviyo = window.klaviyo || []；
   var classname = document.getElementsByClassName("添加到购物车");
   var addToCart = 函数() {
      klaviyo.track("已添加到购物车", item);
   };
   for (var i = 0; i < 类名.length; i++) {
      classname[i].addEventListener('click', addToCart, false);
   }
   </脚本>
   ````
2. 此代码可能需要使用您的类名进行修改。将引号之间的按钮类名称（在以下示例中突出显示）与上面代码片段中“getElementsByClassName”后面的括号之间的内容进行比较。例如，屏幕截图中的类名称为“btn product-form_cart-submit btn--secondary-accent”，代码片段中的类名为“add-to-cart”。 ![在 Chrome 控制台中使用按钮类添加到购物车按钮代码，btn Product-form_cart-submit btn--secondary-accent，以黄色突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28717387188891)
   - 如果这两者不匹配，请更改代码片段以反映按钮的类名称。 3. 例如，下面的代码片段已修改为类名值 `btn Product-form_cart-submit btn--secondary-accent`，并用双引号引起来。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717380936347)
4. 保存您的****product.html**** 文件

保存后，您就完成了代码段的添加，现在可以跟踪 **添加到购物车** 事件。 ## 对“已添加到购物车”代码段进行故障排除

添加代码片段后，它应该监视“添加到购物车”按钮，并在 cookie 访问者单击此按钮时跟踪 **添加到购物车** 事件。此事件的功能与 **查看的产品** 事件类似。某人添加到购物车的每个项目都会触发一个新事件。您可以通过以下方式查看这些事件：

1. 导航至 Klaviyo 中的****分析 > 指标****
2. 搜索事件
3. 单击****活动源
   ![已添加到 Klaviyo 中的购物车指标活动源，列表显示最近添加到购物车的配置文件名称](https://klaviyo.zendesk.com/hc/article_attachments/28717380926747)****

如果您在帐户中没有看到 **已添加到购物车** 事件，请尝试以下操作：

- 确保您的 Klaviyo.js（也称为“现场活动”代码段）正在运行，这是 **添加到购物车** 正常运行所必需的。当您与 Klaviyo 集成时，它应该已自动添加到您的网站，但您可以按照[确认 BigCommerce 集成文章的现场跟踪安装部分](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#confirm-web-tracking-installation3) 中的步骤检查它是否正常工作。 - 检查您的**查看的产品**跟踪是否正常工作，这也是**添加到购物车**正常运行所必需的。此代码段是手动添加的，您可以在我们的集成文章的[查看的产品部分](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#add-viewed-product-tracking4)中了解如何添加和测试它。 如果您的 **添加到购物车** 代码片段仍然遇到问题，可能是由于识别“添加到购物车”按钮时出现问题。在这种情况下，[请联系 Klaviyo 支持](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。 ## “添加到购物车”放弃购物车流程

创建废弃购物车流程时（使用 **添加到购物车** 或 **开始结帐**），除了电子邮件之外，您还可以利用 Klaviyo SMS。出于合规性原因，请确保在您的流程中仅发送一条短信，如果您使用多种类型的废弃购物车流程，请确保仅在其中一种流程中使用短信。在库的 **Essentials** 部分，您将找到标准的废弃购物车提醒流程。此流程由 **Started Checkout** 事件触发。 ![Klaviyo 流程库中 BigCommerce 的标准废弃购物车提醒流程卡](https://klaviyo.zendesk.com/hc/article_attachments/28717380929051)

要使用 **添加到购物车** 事件开始处理废弃的购物车流程，我们建议使用 Klaviyo 的 [流程库](https://www.klaviyo.com/library/flows) 中提供的预构建流程，该流程已设置了正确的流程过滤器。此流程往往针对尚未开始结账的更休闲的潜在购物者。由 **添加到购物车** 事件触发的放弃购物车流程可以在“防止销售损失”目标部分中找到。 ![Klaviyo 流程库中 BigCommerce 添加到购物车废弃购物车提醒流程的卡](https://klaviyo.zendesk.com/hc/article_attachments/28717380931483)

如果您实施了 BigCommerce **添加到购物车** 代码段，则此流程将准备好与所有推荐的过滤器和动态电子邮件内容一起使用，以支持个性化购物车后续电子邮件。 ## 您是否使用亚马逊 Prime 购买？如果您使用“Buy with Prime”来支持商店中任何产品的付款和配送，您应该：

- [将 Buy with Prime 与 Klaviyo 集成](https://help.klaviyo.com/hc/en-us/articles/14708088221467) 将 Buy with Prime 数据引入您的 Klaviyo 帐户。 - 对于已放弃的“添加到购物车”流程，请添加以下流程过滤器，以排除开始结账或通过“Buy with Prime”进行购买的客户收到错误消息：
  - **开始结帐**（使用 Prime 购买）**自开始此流程以来零次**并且
  - **下订单**（使用 Prime 购买）**自开始此流程以来零次。**

## 其他资源

- [创建废弃的购物车流程](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow)
- [BigCommerce 数据参考](https://help.klaviyo.com/hc/en-us/articles/115005082587-Reviewing-Your-BigCommerce-Data)