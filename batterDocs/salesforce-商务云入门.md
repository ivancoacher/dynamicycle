<h1>Salesforce 商务云入门</h1>

<h2>你将会学到</h2>
<p>了解如何将 Salesforce Commerce Cloud 与 Klaviyo 集成。 Klaviyo 盒和 API 集成允许使用 Salesforce Commerce Cloud（以前称为 Demandware）的网站快速连接实时和历史数据并将其发送到 Klaviyo。当您将 Klaviyo 与 Salesforce Commerce Cloud (SFCC) 集成时，Klaviyo 将开始实时跟踪人们执行的操作，例如网站导航、搜索跟踪、查看产品、查看类别、将商品添加到购物车、结帐和订购。将 SFCC 与 Klaviyo 集成有 3 个主要步骤：</p>
<p>1. 在 SFCC 中安装 Klaviyo 墨盒。 2. 将启用片段添加到 SFCC。 3. 在 Klaviyo 中启用 SFCC OCAPI 集成。 ## 开始之前</p>
<p>Klaviyo 与基于 SFCC 控制器的 Site Genesis (SG) 和 Storefront Reference Architecture (SFRA) 站点集成。每个框架都需要稍微不同的墨盒设置和片段，如下所述。您是否使用版本 23.7.0 以下的 Klaviyo SFCC 墨盒？ 23.7.0 及更高版本包括许多附加功能、更完整的开箱即用安装以及与开发人员体验相关的改进。如果您想升级，请阅读[如何升级您的 Salesforce Commerce Cloud 墨盒](https://help.klaviyo.com/hc/en-us/articles/16708128591259)。为了使用我们的 23.7.0 版墨盒（或任何更高版本），我们建议将您的 SFCC 兼容模式更新到 21.7 或更高版本。如果您想首先集成您的开发环境，您可以使用[本文中描述的方法](https://help.klaviyo.com/hc/en-us/articles/360002165611-Multi-Account-User-Privileges#create-multiple-accounts-with-the-same-email-address2)创建链接的 Klaviyo 帐户，并将您的开发环境与该帐户连接。我们建议您在设置帐户时使用的公司名称中包含“Dev”或“Staging”一词，以便在登录时更好地区分帐户。## 设置 Klaviyo 墨盒</p>
<h3>下载墨盒</h3>
<p>您可以在 [Salesforce AppExchange](https://appexchange.salesforce.com/listingDetail?listingId=a0N4V00000Jg1peUAB&tab=e) 上找到我们的应用程序列表。在 AppExchange 上，您可以了解有关 Klaviyo 的更多信息，然后单击<strong><em>*立即获取</strong></em>*即可转到 Github，我们的墨盒以 zip 文件形式提供，可供下载。如果您有 SFRA 站点，请下载 KlaviyoSFRA zip 文件，如果您有 Site Genesis 站点，请下载 KlaviyoSG zip 文件。您需要安装 2 个盒式磁带，它们都包含在您下载的 zip 文件中。这些墨盒包括：</p>
<ul>
<li>int\_klaviyo 或 int\_klaviyo\_sfra：特定于站点的盒带； int\_klaviyo 适用于基于 Site Genesis 的网站，int\_klaviyo\_sfra 适用于基于 SFRA 的网站。 - int\_klaviyo\_core：对于两种类型的基础设施，包含一些基本的、重叠的功能。 ### 导入墨盒</li>
</ul>
<p>第一步是在 Visual Studio Code 或 Eclipse 中导入盒式磁带，以便它们可以与您的 SFCC 实例链接。 #### 在 VS 代码中</p>
<p>1. 复制并粘贴 int\_klaviyo\_core 盒带。 2. 将 int\_klaviyo (Site Genesis) 或 int\_klaviyo\_sfra (SFRA) 文件夹复制到代码库中，作为其他卡带文件夹的同级文件夹。 #### 在日食中</p>
<p>1. 导航至<strong><em>*管理 > 导入 > 常规 > 将现有项目导入工作区</strong><strong>。 2. 使用导入向导导入 int\_klaviyo\_core 目录。 3. 选择要连接盒的 SFCC 实例。 4. 选择</strong><strong>属性</strong><strong>。 5. 选择</strong><strong>项目参考</strong></em>*。 6. 检查 int\_klaviyo\_core 盒式磁带。 7. 对特定于您的框架的其他盒（int\_klaviyo 或 int\_klaviyo\_sfra）重复步骤 2 到 6。 ### 将墨盒添加到墨盒路径</p>
<p>导入墨盒后，需要使用 SFCC 的业务管理器将它们添加到您的站点使用的墨盒列表中。 1. 导航至<strong><em>*管理 > 站点 > 管理站点</strong><strong>。 2. 选择您的站点。 3. 选择</strong><strong>设置</strong><strong>选项卡。 4. 在标记为 Cartridges 的磁带路径输入的开头，添加导入的 Klaviyo 磁带的名称，最后添加核心磁带（int\_klaviyo:int\_klaviyo\_core 或 int\_klaviyo\_sfra:int\_klaviyo\_core）。 5. 单击</strong><strong>应用</strong><strong>。单击“应用”后，您现在应该在标有“</strong>有效墨盒路径</em>*”的字段开头看到 2 个墨盒。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711698596635)</p>
<h3>添加服务</h3>
<p>导入盒式磁带并将其添加到站点盒式磁带路径后，必须添加 Klaviyo 服务以启用盒式磁带的设置配置。在 Klaviyo 墨盒 zip 文件的根目录中是另一个名为metadata.zip 的 zip 文件。以下说明将引用此 zip 文件。 1. 导航至<strong><em>*管理 > 网站开发 > 网站导入和导出 > 服务</strong></em>*。 2. 上传并导入metadata.zip 文件。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711698559131)</p>
<p>3. 当系统提示您确认是否要导入所选存档时，选择<strong><em>*确定</strong><strong>。 4. 现在，您应该会在页面底部附近的 </strong>Status</em>* 部分看到正在运行的导入。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711677142427)</p>
<p>5. 您现在可以访问首选项页面：<strong><em>*商家工具 > 站点首选项 > 自定义首选项 > klaviyo</strong></em>*。从这里，您可以管理以下设置：</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28711677147035" alt="" />
<ul>
<li>****Klaviyo 启用****</li>
</ul>
<p>必须设置为“是”才能启用墨盒。 - <strong><em>*Klaviyo 私钥</strong></em>*</p>
<p><a href="https://help.klaviyo.com/hc/en-us/articles/115005062267">Klaviyo 私有 API 密钥</a></p>
<p>您的 [Klaviyo 公共 API 密钥或站点 ID](https://help.klaviyo.com/hc/en-us/articles/115005062267-Manage-Your-Account-s-API-Keys#your-public-api-key---site-id2)。 - <strong><em>*将事件标记为 SFCC</strong></em>*</p>
<p>如果您选择将事件标记为 SFCC，您将可以使用 SFCC 数据访问 Klaviyo 中的预构建流。当前标记事件的一个缺点是，如果您选择标记它们，您将无法访问 Klaviyo 产品源中的 <strong>查看的产品</strong> 或 <strong>添加到购物车</strong> 推荐。 - 如果您之前安装的盒式磁带版本早于 23.7.0，现在要升级到版本 23.7.0 或更高版本，请设置为 <strong>否</strong>。 2023 年 7 月 13 日之前创建的集成（即 23.7.0 之前的盒式磁带版本）会生成未标记为 SFCC 的指标。如果您过去使用过 23.7.0 之前的版本，此设置会考虑旧的命名约定，以防止帐户中的指标数据不连续。 - <strong><em>*将“添加到购物车”事件发送为“添加到购物车”</strong></em>*</p>
<p>如果您之前安装的盒式磁带版本早于 23.7.0，现在要升级到版本 23.7.0 或更高版本，请设置为 <strong>是</strong>。否则，设置为<strong>否</strong>。此设置可防止您帐户中指标数据的不连续性。 - <strong><em>*Klaviyo 电子邮件字段选择器</strong><strong> 和 </strong><strong>结账电子邮件字段选择器</strong></em>*</p>
<p>有关如何配置这两个字段的详细信息，请参阅以下部分。 - <strong><em>*图像类型</strong></em>*</p>
<p>您希望在发送到 Klaviyo 的事件数据中使用的产品图像类型。如果您不确定要设置哪种图像类型，请导航至<strong><em>*商家工具 > 产品和目录 > 产品</strong><strong>，单击产品，然后根据可用的内容确定要使用的视图类型（例如大、中、小、高分辨率）。 - </strong><strong>营销电子邮件列表 ID</strong></em>*</p>
<p>您可以在结账时收集电子邮件订阅者并将其同步到 Klaviyo 列表。此设置是您想要添加电子邮件订阅者的 Klaviyo 列表的 ID。了解[如何在 Klaviyo 中查找列表 ID](https://help.klaviyo.com/hc/en-us/articles/115005078647)。要在结账时收集电子邮件订阅者，您还需要添加一个复选框片段，稍后部分将对此进行描述。 - <strong><em>*营销短信列表 ID</strong></em>*</p>
<p>您可以在结账时收集短信订阅者并将其同步到 Klaviyo 列表。此设置是您想要添加 SMS 订阅者的 ID Klaviyo 列表。了解[如何在 Klaviyo 中查找列表 ID](https://help.klaviyo.com/hc/en-us/articles/115005078647)。如果您同时收集短信和电子邮件订阅者，请为短信选择与电子邮件不同的列表。这可以确保同意始终正确地归因于正确的渠道。要在结账时收集 SMS 订阅者，您需要一些其他先决条件以及复选框片段，这将在后面的部分中进行描述。！[](https://klaviyo.zendesk.com/hc/article_attachments/28711698587803)</p>
<p>6.metadata.zip 文件还将在 SFCC 中创建一个新服务。 导航到<strong><em>*管理 > 操作 > 服务</strong></em>*，您现在应该在“服务”选项卡下看到 2 个名为 KlaviyoEventService 和 KlaviyoSubscribeProfilesService 的新条目，每个条目都有各自的配置文件和凭据条目。 ### 配置 Klaviyo 电子邮件字段选择器和结帐电子邮件字段选择器</p>
<p>这些偏好对于 Klaviyo 成功识别和跟踪网站访问者至关重要。如果 Klaviyo 未识别访客身份，则不会跟踪该访客的任何事件。完成集成后，您可以在下面的<strong>测试您的 SFCC 设置</strong>部分中了解如何测试您的 Klaviyo 电子邮件和结账电子邮件字段选择器设置。 #### Klaviyo 电子邮件字段选择器</p>
<p>Klaviyo 电子邮件字段选择器站点首选项用于定位站点上的所有电子邮件和电话号码输入字段（位于结帐中的电子邮件输入除外，这将在下面处理）。我们通过标准 CSS 选择器来识别这些字段，每个字段都单独添加到站点首选项中（这是一组“字符串集”，允许逐个输入多个字符串值）。可以使用任何可以在标准样式表中用于定位特定元素的复杂选择器，例如，#dwf​​rm\_login div.username input.input-text 是可接受的，可以基于共享属性来定位跨站点的多个元素的选择器，例如 input[type=email]。请务必避免通过任何动态生成的 ID 来定位输入（这在 SiteGen 中很常见），因为这些 ID 将根据页面加载而更改，从而失败（例如，#dwf​​rm\_login\_username\_d0fignzngiyq）。请注意，添加到 DOM 页面加载后的字段仍然可以作为目标。此类示例包括在 AJAX 调用后插入到模式中的电子邮件地址字段，或者由第三方 JavaScript 注入到 DOM 中的电子邮件地址字段。另请注意，仅电话号码字段可能无法完全识别 Klaviyo 的用户，具体取决于您的 Klaviyo 帐户中的 SMS 设置（如果启用了 SMS 并且您有与输入电话号码所在国家/地区关联的发送号码，则浏览器将被识别）。因此，将 CSS 选择器添加到目标电话号码字段可以被认为是“很好的选择”或“根据需要”，而为电子邮件字段添加它们应该被认为是必要的。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711677152283)</p>
<h4>结帐电子邮件字段选择器</h4>
<p>结帐中的电子邮件收集字段是一种特殊情况，因此有其自己的网站定位偏好。其原理与 Klaviyo 电子邮件字段选择器网站首选项完全相同：只需输入一个 CSS 选择器，该选择器针对网站结帐流程中的电子邮件地址字段，无论它是否出现在结帐开始、结束或中间。成功配置此站点首选项以定位结帐中的电子邮件收集字段对于正确跟踪 <strong>开始结帐</strong> 事件至关重要，因此强烈建议您进行测试，以确保在结帐中的电子邮件收集字段中输入电子邮件地址后，<strong>开始结帐</strong> 事件出现在 Klaviyo 中。另请注意，除了触发 <strong>Started Checkout</strong> 事件之外，结帐电子邮件字段选择器站点首选项所针对的结帐电子邮件字段将自动连接以识别用户（即，无需在 Klaviyo 电子邮件字段选择器和结帐电子邮件字段选择器站点首选项中都包含结帐电子邮件字段的 CSS 选择器）。 ### 添加设置片段</p>
<p>盒式磁带设置的最后一部分是将片段添加到站点模板文件中，以使盒式磁带能够与站点进行通信。这些步骤对于 Site Genesis (SG) 和 Storefront Reference Architecture (SFRA) 基础设施有很大不同，因此请确保遵循正确的设置说明。 #### 店面参考架构 (SFRA) 片段设置</p>
<p>将以下代码添加到 pageFooter.isml 文件的底部：</p>
<p>````</p>
<p><isinclude template="klaviyo/klaviyoFooter"/></p>
<p>````</p>
<p>您现在已完成 SFRA 商店的代码段设置。 #### Site Genesis (SG) 片段设置</p>
<p>1. 要将 KlaviyoFooter.isml 添加到全局页脚： 将以下代码添加到 footer.isml 文件的底部（或在每个页面底部附近加载的任何类似模板）。 ````</p>
<p><isinclude template="klaviyo/klaviyoFooter"/></p>
<p>````</p>
<p>2. 添加用于服务器端用户识别的代码片段：在调用呈现各自的模板（即 app.getView(...)）之前，将以下代码片段添加到您的 Account-Show 和 Cart-Show 控制器中。 ````</p>
<p>// 克拉维约</p>
<p>var klaviyoUtils = require('*/cartridge/scripts/klaviyo/utils'), klid;</p>
<p>if(klaviyoUtils.klaviyoEnabled &&</p>
<p>!klaviyoUtils.getKlaviyoExchangeID()){</p>
<p>klid = klaviyoUtils.getProfileInfo();</p>
<p>}</p>
<p>// 克拉维约结束</p>
<p>````</p>
<p>3. 然后，您将更新 app.getView(...) 调用以将 klid 作为 pdict 变量包含在内。 - 在您的帐户显示控制器中：</p>
<p>````</p>
<p>app.getView({downloadAvailable: true, klid: klid}).render('account/accountoverview');</p>
<p>// KLAVIYO：添加了“klid：klid”</p>
<p>````</p>
<ul>
<li>在您的 Cart-Show 控制器中：</li>
</ul>
<p>````</p>
<p>app.getView('Cart', {cart: app.getModel('Cart').get(),RegistrationStatus: false,klid: klid // KLAVIYO: 添加 'klid: klid'}).render('checkout/cart/cart');</p>
<p>````</p>
<p>4. 要将 <strong>Added To Cart</strong> 代码段添加到 Cart-AddProduct 控制器： 将以下代码段添加到您的 Cart-AddProduct 控制器中调用呈现模板之前的任意位置（即 app.getView(...)）。 ````</p>
<p>/<em> Klaviyo 添加到购物车事件跟踪 </em>/</p>
<p>var BasketMgr = require('dw/order/BasketMgr');</p>
<p>var klaviyoUtils = require('*/cartridge/scripts/klaviyo/utils');</p>
<p>var addedToCartData = require('*/cartridge/scripts/klaviyo/eventData/addedToCart');</p>
<p>如果（klaviyoUtils.klaviyoEnabled）{</p>
<p>var ExchangeID = klaviyoUtils.getKlaviyoExchangeID();</p>
<p>var dataObj, serviceCallResult, currentBasket;</p>
<p>var isKlDebugOn = request.getHttpReferer().includes('kldebug=true') ？真实</p>
<p>：假；</p>
<p>if (交换ID) {</p>
<p>currentBasket = BasketMgr.getCurrentBasket();</p>
<p>if (currentBasket && currentBasket.getProductLineItems().toArray().length)</p>
<p>{</p>
<p>dataObj = addedToCartData.getData(currentBasket);</p>
<p>serviceCallResult = klaviyoUtils.trackEvent(exchangeID, dataObj, klaviyoUtils.EVENT_NAMES.addedToCart,</p>
<p>假）；</p>
<p>如果（isKlDebugOn）{</p>
<p>var klDebugData = klaviyoUtils.prepareDebugData(dataObj);</p>
<p>var serviceCallData = klaviyoUtils.prepareDebugData(serviceCallResult);</p>
<p>var siteGenKlDebutData = `<输入类型=“隐藏”名称=“siteGenKlDebutData”</p>
<p>id="siteGenKlDebutData" value="${klDebugData}"/>`;</p>
<p>var siteGenServiceCallData = `<输入类型=“隐藏”名称=“siteGenServiceCallData”</p>
<p>id="siteGenServiceCallData" value="${serviceCallData}"/>`;</p>
<p>response.writer.print(siteGenKlDebutData);</p>
<p>响应.writer.print(siteGenServiceCallData);</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>/<em> END Klaviyo 添加到购物车事件跟踪 </em>/</p>
<p>````</p>
<p>5. <strong>Started Checkout</strong> 片段：将 Klaviyo 片段添加到结账控制器以跟踪 <strong>Started Checkout</strong> 事件时，请务必记住以下几点：</p>
<ul>
<li>添加这些代码片段的目的是检查电子邮件地址是否已附加到结账流程中的购物篮对象，并在附加后触发 **Started Checkout** 事件。在结帐流程中尽早捕获电子邮件地址与购物篮的关联非常重要。 - 由于基于站点的结帐自定义，Klaviyo 无法准确定义哪个控制器将第一个接收附有电子邮件地址的购物篮对象。 - 我们建议将代码片段添加到结账时触发的所有主要路线中。如果您能够使用调试器准确识别电子邮件地址何时附加到结帐流程中的购物篮，请随意将代码片段仅添加到该路线，但要彻底测试以确保所有可能的结帐路径（访客、登录、在结帐中登录等）都会触发代码。 6. 结账时命中的第一条路线（通常为 COCustomer-Start）的代码片段如下。将其插入调用渲染模板之前的任何位置（即 app.getView(...)）。请注意此片段中的关键区别 - 将第一个参数 KLCheckoutHelpers.startedCheckoutHelper 方法传递为 true 而不是 false - 与其他结帐片段（下面突出显示）相比。请注意，在下面的代码片段中，KLCheckoutHelpers.startedCheckoutHelper 方法为 true 而不是 false（就像在其他结账代码片段中一样）。这对于让代码知道我们有一个新的 **Started Checkout** 事件要跟踪至关重要。 ````</li>
</ul>
<p>/<em> Klaviyo 开始结帐事件跟踪 </em>/</p>
<p>var KLCheckoutHelpers = require('*/cartridge/scripts/klaviyo/checkoutHelpers');</p>
<p>var customerEmail = KLCheckoutHelpers.getEmailFromBasket();</p>
<p>var KLTplVars = KLCheckoutHelpers.startedCheckoutHelper(true, customerEmail);</p>
<p>if (KLTplVars.klDebugData || KLTplVars.serviceCallData) {</p>
<p>应用程序.getView({</p>
<p>klDebugData：KLTplVars.klDebugData，</p>
<p>serviceCallData：KLTplVars.serviceCallData</p>
<p>}).render('klaviyo/klaviyoDebug');</p>
<p>}</p>
<p>/<em> END Klaviyo 开始结帐事件跟踪 </em>/</p>
<p>````</p>
<p>7. 然后，更新 app.getView(...) 调用以将 klid 作为 pdict 变量包含在其中：</p>
<p>````</p>
<p>应用程序.getView({</p>
<p>ContinueURL: URLUtils.https('COCustomer-LoginForm').append('scope', 'checkout'),</p>
<p>klid: KLTplVars.klid, // KLAVIYO: 添加了 'klid: klid'</p>
<p>}).render('结帐/结账登录');</p>
<p>````</p>
<p>8. 以下代码片段应添加到将电子邮件地址附加到 Basket 对象后触发的第一个路由中。如果您不确定，或者只是想覆盖您的基础，我们建议将此代码段添加到以下所有路由中：与上述代码段一样，请在调用渲染模板之前或在调用后续控制器之前的任何位置添加此代码段（来自 COBilling-Save 的示例：app.getController('COSummary').Start()）。 - 中海联运-Start</p>
<ul>
<li>COBilling-PublicStart</li>
<li>COBilling-保存</li>
<li>COPlaceOrder-Start</li>
</ul>
<p>````</p>
<p>/<em> Klaviyo 开始结帐事件跟踪 </em>/</p>
<p>var KLCheckoutHelpers = require('*/cartridge/scripts/klaviyo/checkoutHelpers');</p>
<p>var customerEmail = KLCheckoutHelpers.getEmailFromBasket();</p>
<p>var KLTplVars = KLCheckoutHelpers.startedCheckoutHelper(false, customerEmail);</p>
<p>if (KLTplVars.klDebugData || KLTplVars.serviceCallData) {</p>
<p>应用程序.getView({</p>
<p>klDebugData：KLTplVars.klDebugData，</p>
<p>serviceCallData：KLTplVars.serviceCallData</p>
<p>}).render('klaviyo/klaviyoDebug');</p>
<p>}</p>
<p>/<em> END Klaviyo 开始结帐事件跟踪 </em>/</p>
<p>````</p>
<p>9. 对于直接调用模板的路由（例如，COshipping-Start），请更新 app.getView(...) 调用以将 klid 作为 pdict 变量包含在内。以下是 COshipping-Start 路线的示例：</p>
<p>````</p>
<p>应用程序.getView({</p>
<p>ContinueURL: URLUtils.https('COshipping-SingleShipping'),</p>
<p>购物篮：购物车.对象，</p>
<p>送货上门： 送货上门，</p>
<p>klid: KLTplVars.klid, // KLAVIYO: 添加了 'klid: klid'</p>
<p>}).render('结帐/运输/单次运输');</p>
<p>````</p>
<p>10. 要将<strong>订单确认</strong>代码段添加到 COSummary-ShowConfirmation 控制器：将以下代码段添加到 COSummary-ShowConfirmation 控制器中调用呈现模板之前的任意位置。 ````</p>
<p>/<em> Klaviyo 订单确认事件跟踪 </em>/</p>
<p>var klaviyoUtils = require('*/cartridge/scripts/klaviyo/utils');</p>
<p>var orderConfirmationData = require('*/cartridge/scripts/klaviyo/eventData/orderConfirmation');</p>
<p>var Logger = require('dw/system/Logger');</p>
<p>如果（klaviyoUtils.klaviyoEnabled）{</p>
<p>session.privacy.klaviyoCheckoutTracked = false;</p>
<p>var ExchangeID = klaviyoUtils.getKlaviyoExchangeID();</p>
<p>var dataObj, serviceCallResult;</p>
<p>if (order && order.customerEmail) {</p>
<p>// 检查状态是新建还是已创建</p>
<p>if (order.status == dw.order.Order.ORDER_STATUS_NEW || order.status == dw.order.Order.ORDER_STATUS_OPEN)</p>
<p>{</p>
<p>dataObj = orderConfirmationData.getData(订单, 交换ID);</p>
<p>serviceCallResult = klaviyoUtils.trackEvent(exchangeID, dataObj, klaviyoUtils.EVENT_NAMES.orderConfirmation,</p>
<p>订单.客户电子邮件);</p>
<p>}</p>
<p>if(session.custom 中的“KLEmailSubscribe”|| session.custom 中的“KLSmsSubscribe”)</p>
<p>{</p>
<p>var email = order.customerEmail;</p>
<p>var 电话 = order.defaultShipment.shippingAddress.phone;</p>
<p>var e164PhoneRegex = new RegExp(/^\+[1-9]\d{1,14}$/);</p>
<p>如果（电话）{</p>
<p>// 注意：Klaviyo 仅接受包含 + 和国家/地区代码的电话号码</p>
<p>在开始时（例如美国：+16465551212）</p>
<p>// 为了成功让用户订阅短信列表，您必须收集</p>
<p>您订单电话号码字段中的国家/地区代码！电话 = '+' + 电话.replace(/[^a-z0-9]/gi, '');</p>
<p>if(!e164PhoneRegex.test(电话)) {</p>
<p>如果（session.custom.KLSmsSubscribe）{</p>
<p>var logger = Logger.getLogger('Klaviyo', 'Klaviyo.core: 订单确认');</p>
<p>logger.error(`用户请求短信订阅，但电话号码无效</p>
<p>被提供。 电话号码：${电话}`);</p>
<p>}</p>
<p>phone = null;</p>
<p>}</p>
<p>}</p>
<p>if (email || phone) {</p>
<p>klaviyoUtils.subscribeUser(电子邮件、电话);</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>/<em> END Klaviyo 订单确认事件跟踪 </em>/</p>
<p>````</p>
<p>您现在已经完成了 Site Genesis 商店的代码段设置。 ### 在结账时添加同意复选框片段（SG 和 SFRA）</p>
<p>请注意在结帐时将短信同意同步到 Klaviyo 的以下先决条件：</p>
<ul>
<li>[在 Klaviyo 中启用短信并设置发送号码](https://help.klaviyo.com/hc/en-us/articles/4404274419355)。 - 结账表单上的电话号码字段必须支持国家/地区代码。要在结帐时收集电子邮件和短信的同意，除了配置上面 **添加服务** 部分中所述的列表 ID 设置之外，您还需要包含同意复选框的代码片段，以在需要的位置显示。例如，要使这些代码段出现在结账中，可以将其放置在 SFRA 内的shipmentCard.isml 模板 (app\_storefront\_base) 中，或放置在 SiteGen 内的 billing.isml 模板 (app\_storefront\_core) 中。以下是 Site Genesis 和 SFRA 的 ISML 片段，它们可以放置在结账流程中最适合您的特定网站的任何位置。请注意，为了在结帐时同意在 Site Genesis 上正常运行，您必须包含上面 **添加设置片段** 部分中引用的订单确认片段。下面的代码片段假设您选择的电子邮件和短信语言包含在名为“checkout”的属性资源包中。您需要分别将“your.email.subscribe.resource.string.here”和“your.sms.subscribe.resource.string.here”替换为与您的电子邮件和短信选择语言相对应的密钥。该语言将出现在复选框旁边。例如，您选择加入的语言可能如下所示：</li>
</ul>
<ul>
<li>****电子邮件****</li>
</ul>
<p>订阅电子邮件更新</p>
<ul>
<li>****短信****</li>
</ul>
<p>订阅短信更新。选中此框并在上面输入您的电话号码，即表示您同意通过所提供的号码接收来自[公司名称]的营销短信（例如[促销代码]和[购物车提醒]），包括自动拨号器发送的消息。同意不是任何购买的条件。消息和数据速率可能适用。消息频率各不相同。您可以随时通过回复“停止”或单击我们其中一封消息中的取消订阅链接（如果有）来取消订阅。查看我们的隐私政策 [链接] 和服务条款 [链接]。 ````</p>
<p><isset name="KLEmailSubscribed" value="${(session.custom.KLEmailSubscribe</p>
<p>== 正确）？ '检查'：''}"范围=“页面”/></p>
<p><isset name="KLSmsSubscribed" value="${(session.custom.KLSmsSubscribe == true)</p>
<p>？ '检查'：''}"范围=“页面”/></p>
<p><input type="checkbox" id="KLEmailSubscribe" ${KLEmailSubscribed} /> ${Resource.msg('your.email.subscribe.resource.string.here',</p>
<p>'结账', null)} <br /></p>
<p><input type="checkbox" id="KLSmsSubscribe" ${KLSmsSubscribed} /> ${Resource.msg('your.sms.subscribe.resource.string.here',</p>
<p>'结账'，空）}</p>
<p>````</p>
<h2>在 Klaviyo 中启用 OCAPI 集成</h2>
<h3>Endpoints</h3>
<p>为了与 SFCC 集成产品目录和历史/持续订单数据，Klaviyo 使用四个 OCAPI 端点：</p>
<ul>
<li>****/订单\_搜索****</li>
</ul>
<p>将历史订单数据同步到 Klaviyo，每 60 分钟同步一次正在进行的订单事件。 <strong>订购的产品</strong>和<strong>已下订单</strong>事件将同步用于细分和流过滤的附加数据，并且非常适合<strong>订单确认</strong>事件无法提供的增强个性化。对于实时订单确认电子邮件，请使用墨盒中的 <strong>订单确认</strong> 事件。 - <strong><em>*/sites</strong></em>*</p>
<p>允许您选择在集成设置期间 Klaviyo 同步数据的站点。 - <strong><em>*/产品\_搜索</strong></em>*</p>
<p>将您的目录连接到 Klaviyo 以启用包括电子邮件中的产品推荐在内的功能。 - <strong><em>*/产品/\</em>/变体</strong>**</p>
<p>允许将变体同步到 Klaviyo，以实现补货、低库存和降价流程等功能。 ### SFCC-side setup</p>
<p>在我们与SFCC的OCAPI通信之前，必须在SFCC中设置一些权限和设置。请注意，虽然 Klaviyo 集成需要 <strong>order\_search</strong> 和 <strong>product\_search</strong> 的 POST 权限，但我们实际上并未将数据发布到 SFCC；这是由于SFCC的OCAPI的设计造成的。 1. 导航到 <https://account.demandware.com/dw/account/APIAdmin> 并添加 Klaviyo 的 API 客户端。需要 API 客户端 ID 和密码来生成 OCAPI 的不记名令牌。 2. Once the API client is added, navigate to <strong><em>*Administration > Site Development > Open Commerce API Settings</strong><strong> in the SFCC Business Manager. 3. Add the following snippets, replacing the API version and Client ID.我们支持 API 版本 19.5 及更高版本以及 18.8。将 CLIENT\_ID 替换为上一步中 API 客户端设置生成的 API 客户端 ID（应类似于“xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”）。 If the settings already exist for these APIs, you may only need to add the highlighted sections below to the existing clients JSON array. 1. 在类型 </strong>Shop<strong> 和上下文 </strong>Global（组织范围）<strong> 下添加以下 JSON，将 SHOP\_API\_VERSION 替换为您的 OCAPI Shop API 版本，然后单击 </strong><strong>保存</strong></em>*。 Once added, the settings should appear similar to this:</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28711698592795" alt="" />
<p>````</p>
<p>{</p>
<p>"_v":"SHOP_API_VERSION",</p>
<p>“客户”：[</p>
<p>{</p>
<p>"client_id":"CLIENT_ID",</p>
<p>“资源”：[</p>
<p>{</p>
<p>"resource_id":"/order_search",</p>
<p>“方法”：[“帖子”]，</p>
<p>"read_attributes":"(**)",</p>
<p>“write_attributes”：“（**）”</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>````</p>
<p>2. 在类型 <strong>数据</strong> 和上下文 <strong>全局（组织范围）</strong> 下添加以下 JSON，将 DATA\_API\_VERSION 替换为您的 OCAPI 数据 API 版本，然后单击 <strong><em>*保存</strong></em>*。添加后，设置应类似于以下内容：</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28711677167515" alt="" />
<p>````</p>
<p>{</p>
<p>"_v":"DATA_API_VERSION",</p>
<p>“客户”：[</p>
<p>{</p>
<p>"client_id":"CLIENT_ID",</p>
<p>“资源”：[</p>
<p>{</p>
<p>"resource_id":"/product_search",</p>
<p>“方法”：[“帖子”]，</p>
<p>"read_attributes":"(**)",</p>
<p>“write_attributes”：“（**）”</p>
<p>},</p>
<p>{</p>
<p>"resource_id":"/站点",</p>
<p>“方法”：[“获取”]，</p>
<p>"read_attributes":"(**)",</p>
<p>},</p>
<p>{</p>
<p>"resource_id":"/产品/*/变体",</p>
<p>“方法”：[“获取”]，</p>
<p>"read_attributes":"(**)",</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>]</p>
<p>}</p>
<p>````</p>
<h3>Klaviyo 端设置</h3>
<p>1. 在 Klaviyo 中，选择<strong><em>*集成 > 添加集成</strong><strong>。 2. 搜索 </strong>Salesforce Commerce Cloud<strong> 并单击该卡，然后单击</strong><strong>安装</strong><strong>。 3. 单击登陆页面上的</strong><strong>连接到 Salesforce Commerce Cloud</strong></em>*。 4. 在下一页上，填写以下信息：</p>
<ul>
<li>****商店网址****</li>
</ul>
<p>您的网站域（例如 example.com 或 dev03-na01-example.demandware.net）。 - <strong><em>*授权令牌</strong></em>*</p>
<p><a href="https://documentation.b2c.commercecloud.salesforce.com/DOC1/index.jsp?topic=%2Fcom.demandware.dochelp%2FOCAPI%2Fcurrent%2Fusage%2FOAuth.html">创建此集成的身份验证令牌</a></p>
<p>您在 SFCC 端设置步骤中添加了访问权限的数据 API 的版本（例如 v19\_10）。 - <strong><em>*商店 API 版本</strong></em>*</p>
<p>您在 SFCC 端设置步骤中添加了访问权限的 Shop API 的版本（例如 v19\_10）。 - <strong><em>*目录 ID</strong></em>*</p>
<p>与 Klaviyo 同步的 SFCC 目录的 ID（例如，storefront-catalog-en）。您可以在 Salesforce Business Manager 中的<strong><em>*商家工具 > 产品和目录 > 目录</strong></em>*下找到您的目录 ID。![](https://klaviyo.zendesk.com/hc/article_attachments/28711677165723)</p>
<p>5. 输入这些凭据后，单击<strong><em>*检索站点列表</strong><strong>链接以检索 SFCC 实例上的站点列表。 6. 检索到站点后，选择要与此帐户集成的站点，然后单击</strong><strong>完成设置</strong></em>*。您的集成现在应该开始同步您的订单、目录和客户数据。 ## 测试您的 SFCC 集成</p>
<p>要测试您的墨盒设置，请访问您的站点并按照以下说明进行操作：</p>
<p>1. 通过将 url 参数 utm\_email 作为您的电子邮件地址添加到地址栏来自行设置 Cookie。例如：https://www.example.com/?utm\_email=your@email.com。 2. 搜索您的目录。 3. 查看类别页面。 4. 查看产品页面。 5. 将商品添加到您的购物车。 6. 下测试订单。 7. 在 Klaviyo 中导航<strong><em>*分析 > 指标</strong></em>*，然后查找来自 Salesforce Commerce Cloud 的指标。 ### 测试 Klaviyo 电子邮件字段选择器</p>
<p>要测试给定的电子邮件字段是否已正确定位并正确识别 Klaviyo 用户：</p>
<p>1. 打开隐身浏览器窗口。 2. 在开发者控制台中输入以下命令并按 Enter 键：</p>
<p>`klaviyo.isIdentified();`</p>
<p>这应该会产生以下输出：</p>
<p>`承诺{<已实现>: false}`</p>
<p>3. 在目标字段中输入电子邮件地址，然后单击 Tab 键将焦点更改为页面上的任何其他元素。 4. 返回开发者控制台并再次输入“klaviyo.isIdentified();”。这应该会产生以下输出：</p>
<p>`承诺{<已实现>：true}`</p>
<p>5. 您可以通过前往 Klaviyo 中的<strong><em>*分析 > 指标</strong><strong> 并查找 </strong>Active on Site</em>* 事件的活动源，仔细检查 Klaviyo 是否确实收到了 Identity 呼叫，您应该在其中看到列出的您输入的电子邮件地址。 ### 测试结帐电子邮件字段选择器</p>
<p>要测试结账电子邮件集合字段是否成功触发 <strong>Started Checkout</strong> 事件：</p>
<p>1. 将一件或多件产品添加到购物车，然后开始结帐。 2. 在结账中，在目标字段中输入电子邮件地址，然后单击 Tab 键将焦点更改为页面上的任何其他元素。 3. 您可以通过前往 Klaviyo 中的<strong><em>*分析 > 指标</strong><strong>并查找 </strong>开始结帐</em>* 事件的活动源来仔细检查 Klaviyo 是否确实正在接收识别调用，您应该在其中看到您最近的事件已被跟踪。 ## 结果</p>
<p>您现在已将 Salesforce Commerce Cloud 与 Klaviyo 集成并测试了您的集成。</p>
