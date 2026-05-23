---
id: "115005083427"
title: "如何与 Volusion 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005083427-How-to-integrate-with-Volusion"
section: "Volusion"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:39Z"
language: "zh"
---
## 你将会学到

了解如何将 Volusion 与 Klaviyo 集成。完成这些步骤后，您将能够根据同步的订单数据和客户属性对电子邮件进行个性化和定位。 Klaviyo 从 Volusion 跟踪**订购产品**和**下订单**指标；通过添加一些额外的代码，我们还可以跟踪**废弃的购物车**信息。 ## 开始之前

Volusion 要求[每 90 天更新一次 Volusion 商店的管理员帐户密码](http://helpcenter.volusion.com/extend-your-site/more-integrations/the-volusion-api)。在对您的 Volusion 帐户进行此更新时，您还必须对 Klaviyo 帐户中的 Volusion 集成进行此更新。您还可以按照本文相应部分中的步骤创建永久 API 密钥。 ## 在 Klaviyo 中添加 Volusion 集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 选择****探索应用程序****。 3. 搜索 **Volusion** 并单击该卡，然后单击 ****安装****。 4. 在下一页上，输入您的商店 URL、登录电子邮件和 API 密钥/加密密码。然后，单击****连接到 Volusion****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711662648859)
5. 在下一页上，您将看到一个复选框 **将新的 Volusion 客户添加到 Klaviyo 列表********。****如果选中此框，您可以在 Klaviyo 中选择一个列表，未来的客户在下订单时将添加到该列表中。 6. 最后，点击 ****完成设置****。 ## 在 Klaviyo 中禁用电子邮件到网络跟踪

1. Klaviyo 中的“电子邮件到网络跟踪”功能使用点击跟踪来识别通过 Klaviyo 电子邮件到达您网站的用户，然后我们最初能够识别他们（例如当他们进行购买或订阅您的电子邮件列表时）。 2. Volusion 不支持我们的点击跟踪使用的 URL 格式，当用户尝试通过这些链接之一访问您的商店时，Volusion 会产生错误，因此必须在 Klaviyo 中禁用此功能，以确保您电子邮件中的链接正确到达您的 Volusion 商店。 3. 您可以在****帐户名称 > 设置 > 电子邮件 > 归属****下的帐户设置中禁用此跟踪。 4. 禁用此功能后唯一失去的功能是能够通过他们点击的电子邮件跟踪您网站上的新个人资料。只要您的网站上有 Klaviyo 现场跟踪分析（我们将在下一节中添加），只要我们通过在您的商店中购买或注册电子邮件列表获得用户的电子邮件地址，我们仍然能够跟踪用户。 ## 将现场跟踪添加到您的 Volusion 商店

Klaviyo 提供两个现场跟踪片段来帮助您收集有关客户的有价值的信息：

- ****在网站上活跃****此片段跟踪您的客户何时访问您的网站。必须将此代码段添加到网站中，以便其他代码段（例如**查看的产品**）正常工作。 - ****查看的产品****此片段跟踪您的客户何时查看特定产品。您可以通过将 **查看的产品** 代码段添加到您的商店来跟踪此事件。 ### 添加活动网站跟踪

添加以下 Klaviyo.js 代码片段，以便它出现在您网站的每个页面上。这将启用**Active on Site** 跟踪和 Klaviyo 表单。确保将 PUBLIC\_API\_KEY 替换为您的 [Klaviyo 公共 API 密钥](https://help.klaviyo.com/hc/en-us/articles/115005062267-How-to-Manage-Your-Account-s-API-Keys)。 ````
<script type="application/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
<脚本类型=“文本/javascript”>
//在页面加载时初始化 Klaviyo 对象的脚本
!function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,参数)}}}}(); </脚本>
````

### 添加查看的产品跟踪

要启用 **查看的产品** 跟踪，您需要将下面的代码片段添加到 Volusion 的文件编辑器中的商店模板页面，您可以通过单击 ****设计 > 文件编辑器**** 找到该编辑器。 ````
<脚本类型=“文本/javascript”>
// 在执行代码之前检查客户是否在产品页面上。 if ($("meta[property='og:type']").attr("内容") == "产品") {
        var klaviyo = window.klaviyo || []；
        // 跟踪产品何时被查看的函数
        var trackViewedProduct = 函数（项目）{
            klaviyo.track("查看过的产品", item);
            klaviyo.trackViewedItem({
                “标题”：项目.产品名称，
                "ItemId": 商品.ProductID,
                "ImageUrl": 项目.ImageURL,
                "Url": 项目.URL,
                “元数据”：{
                    “价格”：商品价格，
                    “描述”：项目.描述，
                    "CompareAtPrice": item.CompareAtPrice,
                    “YouSave”：项目.YouSave
                }
            });
        };
        变量项 = {}
        $.get(`/ProductDetails.asp?ProductCode=${global_Current_ProductCode}`, 函数(数据) {
            var Product_saleprice = $("table.colors_pricebox div.product_saleprice").length ? Number(`${$("table.colors_pricebox div.product_saleprice").text().trim().split("$")[1].split(".")[0]}.${$("table.colors_pricebox div.product_saleprice").text().trim().split("$")[1].split(".")[1].substring(0,2)}`) : null;
            var Product_listprice = $("table.colors_pricebox div.product_listprice").length ? Number(`${$("table.colors_pricebox div.product_listprice").text().trim().split("$")[1].split(".")[0]}.${$("table.colors_pricebox div.product_listprice").text().trim().split("$")[1].split(".")[1].substring(0,2)}`) : null;
            var Product_productprice = $("table.colors_pricebox div.product_productprice").length ? Number(`${$("table.colors_pricebox div.product_productprice").text().trim().split("$")[1].split(".")[0]}.${$("table.colors_pricebox div.product_productprice").text().trim().split("$")[1].split(".")[1].substring(0,2)}`) : null;
            var Product_yousave = $("table.colors_pricebox div.product_yousave").length ? Number(`${$("table.colors_pricebox div.product_yousave").text().trim().split("$")[1].split(".")[0]}.${$("table.colors_pricebox div.product_yousave").text().trim().split("$")[1].split(".")[1].substring(0,2)}`) : 0;
            项目={
                "产品名称": $("meta[property='og:title']").attr("内容"),
                “产品ID”：global_Current_ProductCode，
                "描述": $("meta[property='og:description']").attr("内容"),
                "ImageURL": $("meta[property='og:image']").attr("内容"),
                "URL": $("meta[property='og:url']").attr("内容"),
                “价格”：产品销售价格？产品销售价格：产品产品价格，
                “比较价格”：产品列表价格？产品列表价格：产品产品价格，
                “YouSave”：product_yousave
            };
            跟踪查看的产品（项目）；
        });
    }
</脚本>
````

### 添加废弃购物车提醒

Volusion 不提供开箱即用的方式通过我们的集成来跟踪废弃的购物车，但我们创建了一个自定义脚本，您可以将其添加到您的 Volusion 商店，这将允许您在 Klaviyo 中使用此功能。这需要一些向商店模板添加代码的知识，因此如果您有开发人员，您可以向他们发送此文档以逐步完成添加代码。 废弃购物车功能仅适用于使用一页结账功能的 Volusion 商店，以及不需要用户在购买前拥有帐户的商店。 1. 您需要将下面的代码片段添加到 Volusion 的文件编辑器中的商店模板页面，您可以通过单击 ****设计 > 文件编辑器**** 找到该页面。 ````
   <脚本类型=“文本/javascript”>
       // 在执行代码之前检查客户是否位于结账页面。 if (window.location.pathname == "/one-page-checkout.asp") {
           var klaviyo = window.klaviyo || []；
           // 跟踪结帐何时开始的函数。 var trackStartedCheckout = 函数() {
               $.post('/AjaxCart.asp', 函数(数据) {
                   if (!data || !data.Products || !data.Products.length) {
                       返回；
                   }
                   var 项目 = [],
                       名称=[]，
                       sku = [];
                   // 获取每个产品及其 SKU/名称/数量/价格/总价/图片 url
                   $.each(data.Products, 函数(i, 记录) {
                       var item_price = +(record.ProductPrice.replace(/[\$,]+/g, '')) / record.Quantity;
                       项目.push({
                           SKU：记录.产品代码，
                           名称：记录.产品名称，
                           数量：+记录.数量，
                           商品价格：商品价格，
                           RowTotal: item_price * record.Quantity,
                           ImageURL：记录.ImageSource
                       });
                       名称.push(记录.ProductName);
                       skus.push(记录.ProductCode);
                   });
                   // 将“开始结帐”指标与客户数据一起推送到 Klaviyo。 klaviyo.track("开始结账", {
                       $值：+(data.Totals[0].CartTotal.replace(/[\$,]+/g, "")),
                       物品： 物品，
                       产品名称：名称，
                       SKU：sku
                   });
               }, 'json');
           };
           $(函数() {
               // 获取电子邮件表单以获取客户电子邮件，并将活动与 Klaviyo 中的该电子邮件关联起来。 $('[name="OnePageCheckoutForm"] [name="Email"]').change(function(e) {
                   var email = $(this).val();
                   // 进行一些简单的验证。收到数据后，Klaviyo 会进行更多验证。如果（电子邮件 && /@/.test（电子邮件））{
                       klaviyo.identify({
                           $电子邮件：电子邮件
                       });
                       trackStartedCheckout();
                   }
               });
           });
   }
   </脚本>
   ````
2. 此代码只能跟踪未来的结帐事件；您将无法重新填充 Klaviyo 内废弃的购物车流。 3. 将此代码保存到您的商店后，Klaviyo 将自动开始跟踪 **开始结帐** 指标，您可以从中触发废弃的购物车流程。 ## 监控 Klaviyo 同步

1. 与 Volusion 集成后，Klaviyo 将需要时间来同步您的数据，然后才能使用。您可以通过导航回****集成****选项卡并在**启用的集成**列表中查找您的 Volusion 集成来检查此同步的状态。 2. 如果出现灰色轮廓，则表示集成仍在同步。您的商店越大，同步所需的时间就越长。当您的集成显示有绿色边框时，您就可以开始了。 3. 当您首次启用集成时，Klaviyo 会导入所有历史 Volusion 数据。要验证这一点，您可以将特定日期的订单数量与 Volusion 界面中的订单数量进行比较，并确认它们匹配。例如，在探索 **已下订单** 指标（在 Klaviyo 中的 **分析 > 指标**** 下）时，您可以将鼠标悬停在昨天的数据点上或查看图表下方的数据表，以了解昨天报告了多少订单。 4. 将该数字与昨天存储在 Volusion 中的数字进行比较，您应该看到它们完全匹配。如果没有，问题很可能是您的 Klaviyo 帐户的时区与您的 Volusion 时区不匹配。 5. 要检查或更新您帐户的时区：
   - 单击左下角您的帐户名。 - 选择然后单击****设置**** ****> 组织****。 - 向下滚动到**时区**。 ## 从 Volusion 同步的数据

导航至****分析>指标****以查找您帐户中的所有指标。带有 Volusion 图标的指标是从您的 Volusion 集成同步的。 Volusion 的指标和配置文件属性会在有人下订单后一小时内同步。 ![Klaviyo 中按 Volusion 过滤的“指标”选项卡显示已下订单和已订购产品的指标](https://klaviyo.zendesk.com/hc/article_attachments/28711674775067)

### 已下订单

当客户完成结账流程并在您的 Volusion 商店中创建订单时，系统会跟踪此事件。 **已下订单** 事件包括有关某人购买的商品的所有相关信息，包括产品名称、产品代码、图像和价格信息，以便您可以在购买后续电子邮件中使用该信息。 ### 订购的产品

当客户下订单时也会跟踪此事件，但订单中的每一项都会跟踪一个事件。例如，如果有人购买一件 T 恤和一条裤子，则会跟踪一个 **下订单** 事件和两个 **订购产品** 事件 - 一个针对 T 恤的事件，一个针对裤子的事件。 **订购的产品**事件包括有关购买的每个产品的详细信息。当根据产品变体选项和**已下订单**事件中不可用的其他详细信息创建行为细分时，这非常有用。您可以根据以下条件过滤和定位**订购产品**事件：

- ****名称****Volusion 中产品的名称或标题，例如 **T 恤**。 - ****产品代码****Volusion 中您的产品的产品代码。 - ****数量****订单中购买的商品的数量。 ### 从 Volusion 同步的客户数据

除了 Klaviyo 从 Volusion 同步的上述指标之外，还有添加到每个 Klaviyo 配置文件中的客户属性。您可以在段和流中使用这些属性。以下是从 Volusion 自动同步的属性：

- 电子邮件
- 名字
- 姓氏
- 城市
- 州/地区
- 邮政编码
- 国家
- 电话号码
- 来源（Klaviyo 将跟踪来自 Volusion 的客户，其个人资料上的来源属性设置为“Volusion”）

## 故障排除

### Volusion 已下订单数据未在 Klaviyo 中报告

这可能是您允许导出数据的 Volusion API 设置的问题。 1. 要解决此问题，请导航至 Volusion 管理面板的 **库存** 选项卡。从下拉菜单中选择**导入/导出**。 ![Volusion 中的库存下拉菜单，导入/导出为蓝色](https://klaviyo.zendesk.com/hc/article_attachments/28711662634139)
2. 单击 **Volusion API** 访问 API 主页面。 3. 在**通用**部分，您将找到****运行****导出商店通用/订单的选项。导出运行后，页面将刷新。 ![Volusion 中的导入/导出页面，鼠标悬停在 Run for Generic\Orders 上](https://klaviyo.zendesk.com/hc/article_attachments/28711662626331)
4. 通过单击名为****\***** 的列中的复选框来选择所有列，然后单击 ****运行****。 ![Volusion API：运行通用\订单页面并选中星号列](https://klaviyo.zendesk.com/hc/article_attachments/28711662644763)
5. 点击**运行**导出通用订单后，页面顶部会生成一个 API URL。例如，URL 将显示为：“https://storename.com/net/WebService.aspx?Login=user@storename.com&EncryptedPassword=ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789&EDI_Name=GenericOrder”。 ![Volusion API 页面上的链接中突出显示的 API 密钥：运行 Generic\Orders](https://klaviyo.zendesk.com/hc/article_attachments/28711674788251)
6. “EncryptedPassword=”和“&EDI\_Name=GenericOrders”之间出现的值（在上面的屏幕截图中突出显示）用作您的 API 密钥。使用它可以从 Klaviyo 仪表板的“集成”选项卡重新建立集成设置。 7. 完成后，单击****分析>指标****进行测试。查看 Volusion **已下订单** 指标的近期活动，看看是否有任何新数据已在 Klaviyo 中同步。如果您看到“已下订单”指标的新数据，请[联系我们的支持团队](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272)，以对 Klaviyo 中缺失的订单进行填补或寻求任何进一步帮助。 8. 有关使用 Volusion API 导出数据的更多信息，请参阅 [Volusion 支持](https://support.volusion.com/hc/en-us/articles/208837888-Exports-Orders-Export-Developer-)。 ### 人们在点击我的电子邮件链接时看到“无效输入”错误

Klaviyo 中的“电子邮件到网络跟踪”功能使用点击跟踪将活动与通过 Klaviyo 电子邮件到达您网站的用户联系起来，然后我们最初能够识别他们（例如当他们进行购买或订阅您的电子邮件列表时）。 Volusion 不支持我们的点击跟踪使用的 URL 格式，并且当用户尝试通过这些链接之一访问您的商店时会产生错误，因此必须在 Klaviyo 中禁用此功能，以确保电子邮件中的链接正确到达您的 Volusion 商店。要解决此问题，请确保按照本文开头所述在 Klaviyo 中禁用电子邮件到网络跟踪。 ## 如何在 Volusion 中创建永久 API 密钥

通常，当您重置帐户密码时，Volusion 会要求您每 90 天重置一次 API 密钥，这导致您需要在 Klaviyo 中重新配置 Voluision 集成。以下步骤将允许您创建一个不过期的 API 密钥；它涉及为您从未登录过的管理员帐户生成 API 凭据：

1. 在您的 Volusion 管理面板中，转至****客户 > 管理员****并创建一个新的管理员帐户。 2. 导航至 ****库存 > 导入/导出**** 并选择 ****Volusion API**** 选项卡。 3. 在“通用”部分下，单击****Volusion API 集成帮助**** 的链接。 4. 选择****导出****并从下拉列表中选择您创建的新管理员。 5. 展开“带有查询字符串的 URL...”框以查找您的永久 URL、登录名和加密密码（API 密钥）。请勿使用此帐户登录，该帐户仅用于 API 访问。使用此帐户登录将导致密码在 90 天后过期，您将需要重做这些步骤来生成新的永久 API 密钥。 ## 结果

现在，您已将 Klaviyo 与 Volusion 集成、添加了现场跟踪、查看了同步数据，并了解了如何创建永久 API 密钥。 ## 其他资源

- [集成同步参考频率](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208)
- 需要更多与 Klaviyo 集成的帮助吗？查看 [Klaviyo 的代理合作伙伴](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=integrations)