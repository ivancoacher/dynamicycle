---
id: "115005083107"
title: "Shift4Shop 入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005083107-Getting-started-with-Shift4Shop"
section: "Shift4Shop"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:21Z"
language: "zh"
---
## 你将会学到

了解如何将 Shift4Shop（以前称为 3dcart）与 Klaviyo 集成，以便根据每个客户的购买和网站活动个性化和定位电子邮件。从 Shift4Shop 同步到 Klaviyo 的数据包括：

- 有关客户订单的数据，包括销售、退款、已履行订单和已取消订单
- 详细的客户信息，包括人们访问您网站的时间和频率

Klaviyo 仅同步过去三年内下过订单的客户的信息。 ## 目录

1. 添加 Shift4Shop 集成
2.添加Klaviyo现场追踪
3. 监控数据同步
4.从Shift4Shop同步的数据
5. 额外资源

## 添加 Shift4Shop 集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 选择****探索应用程序****。 3. 搜索 **Shift4Shop** 并单击该卡，然后单击 ****安装****。 4. 要查找您的 Shift4Shop 商店 URL（也称为安全 URL），请在新选项卡中打开您的 Shift4Shop 帐户。 5. 在 Shift4Shop 中，转到****设置 > 常规 > 商店设置****。 6. 在商店信息下，单击****管理域名和商店 URL****。！[显示商店信息的 Shift4Shop 设置页面](https://klaviyo.zendesk.com/hc/article_attachments/28717985271707)
7. 从域设置下方复制商店 URL。 ![Shift4Shop 域设置显示商店 URL](https://klaviyo.zendesk.com/hc/article_attachments/28717985269659)
8. 返回 Klaviyo，将您的商店 URL 粘贴到框中，然后单击****连接到 Shift4Shop****。 9. 复制下一页上显示的 Klaviyo 公共 API 密钥。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717985290907)
10. 单击****转到 Shift4Shop**** 按钮。 11. 在 Shift4Shop 的 **REST API 应用程序** 页面上，单击右上角的****添加**** 以添加 Klaviyo API 密钥。 ![Shift4Shop 中的 REST API 应用程序页面，带有蓝色背景的“添加”按钮](https://klaviyo.zendesk.com/hc/article_attachments/28717991178907)
12. 粘贴 Klaviyo 公共 API 密钥 (2bd83b00fcd7d56916a28c452d3d080c)。 ![Shift4Shop 中的公共密钥设置，带有蓝色背景的“保存”按钮](https://klaviyo.zendesk.com/hc/article_attachments/28717985281051)
13. 单击****保存****。 14. 将出现一个弹出窗口，要求您授予 Klaviyo 授权将 Shift4Shop 数据拉入我们的平台；单击****授权****。 ![Shift4Shop 中的 Klaviyo 设置显示所需的权限以及蓝色背景的授权按钮](https://klaviyo.zendesk.com/hc/article_attachments/28717991176859)
15. 您将被重定向回您的 Klaviyo 帐户，并且您的数据将开始同步。成功标注将确认您的数据正在同步。 ## 添加 Klaviyo 现场跟踪

您可以将两个 Klaviyo 现场跟踪代码片段添加到 Shift4Shop 网站。第一个现场跟踪代码段允许您跟踪 cookied 用户何时在您的网站上处于活动状态（**网站上活动**指标），第二个现场跟踪代码段允许您跟踪他们查看的产品（**查看的产品**指标）。然后，您可以使用**网站上的活动**指标来创建访问过您的网站但未购买任何东西的已知浏览器的细分。 **Active on Site** 代码段（也称为 Klaviyo.js）还支持使用 Klaviyo 注册表单。 **查看的产品** 跟踪最常用于触发浏览放弃自动电子邮件流。有关更多信息，请参阅我们关于[创建浏览放弃​​流程]的文章(https://help.klaviyo.com/hc/en-us/articles/115002775252)。 1. 登录 Shift4Shop 商店管理员并导航至****内容 > 网站内容****。 2. 单击页眉和页脚下的****编辑****按钮。 ![Shift4Shop 中的站点内容页面，在页眉和页脚下进行蓝色背景的编辑](https://klaviyo.zendesk.com/hc/article_attachments/28717985286939)
3. 单击全局标题右侧的****+**** 打开标题编辑器。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717985293211)
4. 单击 **WYSIWYG 模式关闭/打开**旁边的滑块将视图切换到 HTML 编辑器。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717991195803)
5. 要添加 **Active on Site** 跟踪，请将以下脚本粘贴到 HTML 编辑器的底部：

   ````
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
   <脚本类型=“文本/javascript”>
   //在页面加载时初始化Klaviyo对象
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,参数)}}}}(); </脚本>
   ````
6. 在代码片段的第一行中，将 **公共 API 密钥** 替换为您的 Klaviyo 公共 API 密钥（可在 Klaviyo 中的****帐户名称 > 设置 > API 密钥**** 下找到）。 7. 要添加 **查看的产品** 跟踪，请将此脚本添加到标题中的 **Active on Site** 脚本下方：

   ````
   <脚本类型=“文本/javascript”>
   var klaviyo = window.klaviyo || []；

   // 跟踪每个产品视图。 if ('[价格]' !== '[' + '价格]') {
      klaviyo.track("查看过的产品", {
         产品ID：“[id]”，
         姓名：“[姓名]”，
         描述：“[描述]”，
         URL: [location.protocol, '//', location.host, location.pathname].join(''),
         类别：“[catid]”，
         ImageURL: [location.protocol, '//', location.host, '/[image1]'].join(''),
         价格：parseFloat("[价格]".slice(1), 10)
      });
   }
   </脚本>
   ````

     8. 在页面右上角，点击****保存****

## 监控 Klaviyo 同步

要查看您的 Shift4Shop 集成数据：

1. 在您的 Klaviyo 帐户中，导航至****分析 > 指标****。 2. 单击****已下订单**** 指标以验证您的数据是否已开始填充。如果您看到数据填充图表，则意味着 Shift4Shop 集成已成功同步到您的帐户。同步完成后，在 ****Integrations**** 选项卡中查看时，您将在 Shift4Shop 集成旁边看到绿色边框。 ![Klaviyo 中的 Shift4Shop 集成卡，左侧有绿色条](https://klaviyo.zendesk.com/hc/article_attachments/28717991184411)
3. Klaviyo 导入所有历史 Shift4Shop 数据。要验证这一点，请将 Klaviyo 中特定日期的订单数量与 Shift4Shop 界面中的订单数量进行比较，并确认它们匹配。 4. 如果不匹配，则问题很可能是您的 Klaviyo 帐户的时区与您的 Shift4Shop 时区不匹配。要检查您在 Klaviyo 中的时区设置，请转至****帐户名称 > 设置 > 组织****。 5. 在此页面中间，您将看到一个用于设置时区的区域。将您的 Klaviyo 帐户更新为正确的时区，然后单击****更新信息****。 ## 从 Shift4Shop 同步的数据

Shift4Shop 集成每小时将数据同步到 Klaviyo 一次，因此您应该会在 Shift4Shop 中记录事件后的一小时内看到 Klaviyo 中出现的事件。以下指标从 Shift4Shop 同步：

- 已履行的订单
- 订购的产品
- 已下订单
- 开始结账

![由 Shift4Shop 过滤的 Klaviyo 指标选项卡显示已履行订单和已订购产品等指标](https://klaviyo.zendesk.com/hc/article_attachments/28717991188635)

### 已履行订单

当客户完成结账流程并在您的 Shift4Shop 商店中创建订单时，系统会跟踪此事件。它包括有关某人购买的商品的所有产品信息，包括产品名称、图像以及在购买后续电子邮件中使用的变体信息。您可以根据以下条件过滤和定位**已履行订单**事件：

- 商品：某人订单中的商品名称，例如 T 恤或裤子
- 类别：某人订单中产品的完整类别集，例如T恤、男装、裤子和促销

### 订购的产品

当客户下订单时会跟踪此指标，并跟踪某人购买的每件商品的事件。例如，如果有人购买一件 T 恤和一条裤子，则会创建两个 **订购产品** 事件 - 一个用于 T 恤，一个用于裤子。 **订购的产品**事件包括有关某人购买的每种产品的详细信息。 当根据产品变体选项和**已下订单**事件中不可用的其他详细信息创建行为细分时，这非常有用。您可以根据以下条件过滤和定位**订购产品**事件：

- 名称：Shift4Shop 中产品的名称或标题，例如 T 恤或裤子
- SKU：产品变体的 SKU，例如 REDMEDIUMTSHIRT
- 类别：产品的完整类别，例如T恤、男装、促销

### 已下订单

当客户完成结账流程并在您的 Shift4Shop 商店中创建订单时，系统会跟踪此事件。它包括有关某人购买的商品的所有产品信息，包括产品名称、图像以及在购买后续电子邮件中使用的变体信息。您可以根据以下条件过滤和定位 **已下订单** 事件：

- 商品：某人订单中的商品名称，例如 T 恤或裤子
- 类别：某人订单中产品的完整类别集，例如T恤、男装、裤子和促销
- 商品数量：订单中的商品数量，例如 **2**

注意：默认情况下，Shift4Shop 同步已下订单的两个状态：2、4

### 开始结帐

当客户在 Shift4Shop 结帐流程中付款页面之前的页面上输入联系方式和送货信息并单击“继续”时，就会跟踪此事件。它包括有关某人购物车中商品的所有产品信息，包括产品名称、图像以及要在废弃购物车电子邮件中使用的变体信息。您可以根据以下条件过滤和定位 **Started Checkout** 事件：

- 商品：某人购物车中商品的名称，例如 T 恤或裤子
- 类别：某人购物车中产品的完整类别，例如 T 恤、男装、裤子和促销

### 客户数据

除了 Klaviyo 从 Shift4Shop 同步的指标之外，还有添加到每个 Klaviyo 配置文件中的属性。您可以在段和流中使用这些属性。以下内置 Klaviyo 属性自动从 Shift4Shop 同步：

- 电子邮件
- 名字
- 姓氏
- 城市
- 州/地区
- 邮政编码
- 国家
- 电话号码

## 结果

您现在已与 Shift4Shop 集成，启用了 Klaviyo 现场跟踪，并验证了同步的 Shift4Shop 数据。现在，您可以在 Klaviyo 中查看 Shift4Shop 数据，并根据每个客户的购买和网站活动个性化和定位电子邮件。 ## 更新您的 Shift4Shop 集成

您是否在 2025 年 5 月 12 日之前将 Klaviyo 与 Shift4Shop 集成？如果是这样，您正在使用我们的旧应用程序。 Klaviyo 发布了新的 Shift4Shop 应用程序，以提高安全性和稳定性。我们的旧应用程序将于 2025 年 9 月 6 日停用，届时将停止工作。要更新到新集成，您需要在 Klaviyo 中重新安装 Shift4Shop 应用程序：

1. 在 Klaviyo 中，单击****集成****选项卡。 2. 从启用的集成列表中选择 ****Shift4Shop****。 3. 在右上角，单击****管理集成****。 4. 选择****重新验证****。 5. 复制 Klaviyo 公共 API 密钥。 6. 单击****转到 Shift4Shop**** 按钮。 7. 在 Shift4Shop 的 **REST API 应用程序** 页面上，单击 ****添加**** 添加 Klaviyo API 密钥，然后粘贴该密钥。 8. 单击****保存****。 9. 在出现的授权请求模式中，单击****授权****。 10. 您将被重定向回您的 Klaviyo 帐户，其中确认模式将指示您的 Shift4Shop 帐户现已连接。您的集成现已更新，并将开始使用新的应用程序。虽然没有必要，但您可能希望从 Shift4Shop 中的**连接的应用程序**中删除已弃用的 Klaviyo 应用程序。为此，请从 Shift4Shop REST API 应用程序页面中删除“Klaviyo”应用程序。 ## 其他资源

- [Klaviyo现场跟踪入门](https://help.klaviyo.com/hc/en-us/articles/115005076767)
- 切换电商后如何更新[Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360003124151)平台