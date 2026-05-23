---
id: "115005255408"
title: "如何与 OpenCart 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005255408-How-to-integrate-with-OpenCart"
section: "OpenCart"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "zh"
---
## 你将会学到

了解如何将 OpenCart 与 Klaviyo 集成。完成这些步骤后，您将能够根据每个客户的购买和网站活动来个性化和定位电子邮件。 OpenCart 集成每小时同步一次。 ## 开始之前

请注意，Klaviyo 不会从 OpenCart 同步您的目录。 ## 添加 OpenCart 集成

添加 Klaviyo 的 OpenCart 集成的过程是多步骤的，需要在 OpenCart 和 Klaviyo 内部采取操作。首先，Klaviyo 目前支持 OpenCart 1.4.x 和 1.5.x。从此处下载 Klaviyo OpenCart 模块：<https://www.klaviyo.com/media/downloads/OpenCartKlaviyo-1.1.0.tgz>。 1. 将文件解压到 OpenCart 安装的根目录中。 2. 登录 OpenCart 管理部分并转到****扩展>模块****页面。 3. 安装 Klaviyo 模块，然后单击 Klaviyo 模块的 **编辑**。 4. OpenCart 安装要做的最后一件事是将以下 PHP 代码复制并粘贴到 `upload/index.php` 末尾、`$response->getOutput();` 行之前：

   ````
   // [Klaviyo] 保存客户购物车（如果存在）。 if ($registry->get('cart')->hasProducts()) {
     $registry->get('load')->model('module/klaviyo');

     if ($registry->get('客户')->isLogged()) {
       $registry->get('model_module_klaviyo')->saveCustomerCart(
         会话 ID(),
         $registry->get('客户')->getId(),
         $会话->数据['购物车']
       ）；
     } else if (array_key_exists('guest', $session->data)) {
       $registry->get('model_module_klaviyo')->saveGuestCart(
         会话 ID(),
         $session->data['guest'],
         $会话->数据['购物车']
       ）；
     }
   }
   ````
5. 在 Klaviyo 中，选择****集成****选项卡。 6. 单击****探索应用程序****并搜索 **OpenCart**，然后单击该卡片。然后，单击****安装****。 7. 您将进入 **集成设置** 页面。在设置页面上，输入 OpenCart 站点的 URL，然后单击****连接到 OpenCart****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28715969274139)
8. 在下一页上，复制 **Klaviyo OpenCart Module** 下的 API 密钥并将其粘贴到 OpenCart 中的 Klaviyo 模块设置中。在 OpenCart 管理中保存 Klaviyo 模块设置。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28715969282587)
9. 如果需要，请检查设置 **将新的 OpenCart 客户添加到 Klaviyo 列表**，然后从下拉列表中选择一个列表。 10. 返回 Klaviyo，单击****完成设置****开始同步数据。 ## 安装 Klaviyo 现场跟踪

要跟踪 OpenCart 中的现场活动，请首先登录您的帐户，单击左下角的帐户名称，然后导航至****设置 > API 密钥****，找到您的 Klaviyo 公共 API 密钥。您的公钥长度为六个字符。您可以安装两种类型的现场跟踪：

- ****现场活跃****只要可识别的浏览器访问您的网站，就会跟踪此指标
- ****查看的产品****每当可识别的浏览器查看您网站上的产品页面时，就会跟踪此指标

### 添加“现场活动”跟踪

每当可识别的浏览器访问您的网站时，就会跟踪此指标。要开始跟踪**现场活跃**活动：

1. 将以下代码片段添加到您的主商店模板中，以便将其包含在所有页面上。您应该将此代码段与您使用的其他分析脚本一起放置，或者放置在 **</body>** 结束标记之前：

   ````
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js></script>
   <脚本类型=“文本/javascript”>
   //在页面加载时初始化Klaviyo对象
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,参数)}}}}(); </脚本>
   ````
2. 确保将“PUBLIC_API_KEY”替换为您的 Klaviyo 帐户的公共 API 密钥。 3. 如果访问者或客户可以为您的商店创建帐户，请将以下代码段直接添加到第一个代码段下方：

   ````
   <脚本类型=“文本/javascript”>
     var klaviyo = window.klaviyo || []；
     {% if user.is_logged_in %}
     klaviyo.identify({
       $email: '{{ user.email }}',
       $first_name: '{{ user.first_name }}',
       $last_name: '{{ user.last_name }}'
       });
     {% 结束 %}
   </脚本>
   ````
4. 根据您网站使用的模板类型，**{% if user.is\_logged\_in %}** 和 **{{ user.email }}** 语法可能不同。使用可用的模板语言，您想要检查查看当前页面的人是否已登录。如果是，您应该输出他们的电子邮件和姓名（如果有）。如果您没有姓名信息，请删除这两行以及电子邮件 **$email** 行后的尾随逗号。 ### 添加“查看的产品”跟踪

如果您想要设置[浏览放弃流程](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow) 或根据产品浏览数据构建细分，则需要为“查看的产品”指标添加 JavaScript 事件跟踪。 1. 在您的产品页面模板上，添加以下代码段：

   ````
   <脚本类型=“文本/javascript”>
       var klaviyo = window.klaviyo || []；
       klaviyo.track("查看过的产品", {
         标题: '{{ 产品.title }}',
         商品 ID: {{ 产品.id }},
         Categories: {{category in product.categories|json }}, // 类别列表是一个字符串数组。图片网址: '{{ 产品.image_url }}',
         网址: '{{ 产品.url }}',
         元数据：{
           品牌: '{{ 产品.品牌 }}',
           价格：{{ 产品.价格 }}，
           CompareAtPrice: {{ Product.compare_at_price }} // 如果您有价格比较。您还可以以促销或特价的方式包含此内容。 }
     });
   </脚本>
   ````
2. 上面的代码片段使用了“{{ }}”占位符语法，该语法可能与您的 OpenCart 商店有所不同。重要的是，产品字段是根据您正在查看的产品页面动态呈现的。 3. 为您的网站配置**查看的产品**跟踪后，当已知访问者浏览您的产品页面时，**查看的产品**数据应开始填充到您的 Klaviyo 帐户中。 ### 现场跟踪的工作原理

当您将 Klaviyo 网络跟踪添加到您的网站时，我们只能跟踪“已知浏览器”的浏览活动，即之前至少访问过并参与过一次的浏览器。我们可以通过两种关键方式识别网站访问者以进行网络跟踪：

- 如果有人在某个时候通过 Klaviyo 电子邮件点击了您的网站
- 如果有人在某个时候通过 Klaviyo 表格订阅/选择加入

Klaviyo 不会跟踪匿名浏览器。 ## 监控 Klaviyo 同步

同步 OpenCart 商店中的所有历史客户和订单数据所需的时间取决于商店的规模。此历史性同步完成后，您将在**启用的集成**下看到 OpenCart 集成周围有一个绿色边框。要检查您的集成：

1. 导航到您账户的 ****Metrics**** 选项卡，位于 ****Analytics**** 下。在这里，您可以过滤以查看所有 OpenCart 指标。找到 OpenCart 的 **已下订单** 指标，然后单击“活动源”图标。如果您的集成已开始同步数据，您将开始看到此处填充**已下订单**事件。 2.我们会自动同步所有历史订单数据。要验证这一点，您可以将 Klaviyo 中特定日期的事件数量与 OpenCart 界面中的事件数量进行比较，并确认它们匹配。 3. 例如，在浏览“已下订单”指标时，您可以将鼠标悬停在昨天的数据点上或查看图表下方的数据表，以了解昨天报告了多少订单。 4. 将该数字与昨天存储在 OpenCart 中的数字进行比较，您应该看到它们完全匹配。如果没有，问题很可能是您的 Klaviyo 帐户的时区与您设置的 OpenCart 时区不匹配。 5. 要检查或更新您帐户的时区：

   - 单击左下角您的组织名称。 - 选择****设置****。 - 转到****组织****选项卡。 ## 从 OpenCart 同步的数据

- ****销售和订单数据****购买了哪些产品，包括产品详细信息和图像。 - ****客户信息****名字、姓氏、位置和客户群体。 - ****开始结账数据****用于触发废弃购物车电子邮件。这是通过集成时添加的 PHP 代码片段启用的。 - ****已履行的订单数据****用于跟踪订单何时发货。 - ****现场跟踪****当人们访问您的网站时

对于您的 OpenCart 指标，请导航至 Klaviyo**** 中的****分析 > 指标****，****，您可以在其中按 OpenCart 进行筛选。 ![Klaviyo 中的“指标”选项卡由 OpenCart 过滤，其中包含已完成的订单、已订购的产品、已下订单和已开始在列表中结帐](https://klaviyo.zendesk.com/hc/article_attachments/28715969267995)

默认情况下，Klaviyo 同步 **已下订单** 和 **已履行订单** 指标的以下状态：

- ****下订单：****待处理、已处理、处理中、已发货、已完成
- ****已履行的订单：****已发货，已完成

## 其他资源

- [集成同步参考频率](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208)
- 需要更多与 Klaviyo 集成的帮助吗？查看 [Klaviyo 的代理合作伙伴](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=integrations)