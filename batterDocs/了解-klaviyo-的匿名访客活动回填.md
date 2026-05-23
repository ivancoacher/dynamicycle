<h1>了解 Klaviyo 的匿名访客活动回填</h1>

<h2>你将会学到</h2>
<p>了解匿名访客活动回填以及如何在识别购物者之前捕获其现场参与情况。 ## 开始之前</p>
<p>默认情况下，Klaviyo 的网络跟踪支持：</p>
<ul>
<li>*****现场活跃***** ****跟踪****</li>
</ul>
<p>每当可识别的浏览器访问您的网站时，就会跟踪此指标。 - <strong><em></strong>查看的产品<strong></em></strong><em> <strong></em><em>跟踪</strong></em>*</p>
<p>每当可识别的浏览器查看您网站上的产品页面（对于电子商务商店）时，就会跟踪此指标。 <strong>活跃的网站</strong>可以帮助您细分正在访问您网站的个人资料，而<strong>查看的产品</strong>跟踪可以让您在浏览放弃流程中向客户发送提醒。请注意，某些集成不会自动安装<strong>查看的产品</strong>跟踪。 ## 匿名访客活动回填</p>
<p>通过 Klaviyo 的匿名访客活动回填，您可以在识别之前捕获购物者的现场活动。一旦将来识别出该访客，您就可以访问他们的历史现场活动。这使您可以更全面地了解客户的旅程，无论他们何时通过 Klaviyo 的网络跟踪被识别。匿名活动回填仅捕获和设置个人资料上的历史事件，此功能不会捕获其他历史信息，例如[来源](https://help.klaviyo.com/hc/en-us/articles/115005075187)。 ## 匿名访客回填如何工作</p>
<p>当网站访问者同意分析和营销 cookie 且尚未被识别时，Klaviyo 将在客户端 cookie“kl-post-identification-sync”下在浏览器的本地存储中跟踪其网站活动长达 14 天。一旦识别出网站访问者，存储在 cookie 中的所有事件都将被推送到该配置​​文件的 Klaviyo。匿名回填将在以下情况下触发：</p>
<p>1. 通过表格提交同意书后</p>
<p>2. 单击 Klaviyo 消息中的链接</p>
<p>3.使用Klaviyo的Identify API进行识别</p>
<p>4. 已输入联系信息或已在大多数电子商务平台上进行购买</p>
<p>默认情况下，Klaviyo 支持大多数电商平台的结账识别：</p>
<p>|  |  |</p>
<p>| --- | --- |</p>
<p>| <strong><em>*电子商务平台</strong><strong> | </strong><strong>支持</strong></em>* |</p>
<p>|店铺主页 个人中心 关注我们 线下门店 店铺信息✅ [启用 Shopify 附加跟踪时](https://help.klaviyo.com/hc/en-us/articles/4425956184731) |</p>
<p>| WooCommerce | ✅ |</p>
<p>|大商务| ⚠️ - 需要在您的结帐页面上安装自定义脚本 |</p>
<p>| Magento 2 | ⚠️ - 需要验证 |</p>
<p>| Salesforce 商务云 | ⚠️ - 23.7.0 版本之后 |</p>
<p>| Prestashop| ✅ |</p>
<p>|维克斯 | ❌ |</p>
<p>|定制等电商平台 |需要自定义脚本安装 |</p>
<p>如果您使用的是 BigCommerce、Magento 2 的某些版本、自定义或其他电子商务平台，并且您希望在客户在您的网站上进行购买时触发匿名访问者回填，则需要在结帐页面上安装以下脚本：</p>
<p>````</p>
<p>window.onload = function() { // 用于在输入后立即抓取电子邮件 // 将包含客户电子邮件地址的字段添加到此列表 const emailSelectors = [ "input[id='email']", "input[name='email']", "input[placeholder='Email']", "input[type='email']" ] document.querySelector(emailSelectors.join(",")).addEventListener('blur', function() { klaviyo.identify({"email" : this.value}).then(() => console.log("Identified")) });};window.onload = function() { // 用于在按下提交/订购按钮时抓取电子邮件 // 将包含客户电子邮件地址的字段添加到此列表const emailSelectors = [ "input[id='email']", "input[name='email']", "input[placeholder='Email']", "input[type='email']" ] // 将购买或完成交易按钮添加到此列表 const SubmitSelectors = [ "input[id='submit']", "input[name='submit']", "input[type='submit']" ] document.querySelector(submitSelectors.join(",")).addEventListener('click', function() { klaviyo.identify({ "email" : document.querySelector(emailSelectors.join(",")).value }).then(() => console.log("已识别")) });};</p>
<p>````</p>
<h2>测试匿名访客回填</h2>
<p>要验证匿名访客历史回填是否正常工作，您可以执行以下步骤：</p>
<p>确保在测试之前成功触发前端事件，例如<strong>查看的产品</strong>，详细信息可以在[此处](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACFYSN7F22XPPCGT6B)找到。 #### 测试对您网站上匿名活动的捕获</p>
<p>1. 在私人窗口中导航到您的网站，然后执行现场操作，例如 <strong>查看产品。</strong></p>
<p>2. 在浏览器上[打开开发者控制台](https://www.computerhope.com/issues/ch002153.htm)并导航到本地存储。这可能位于开发者控制台的 <strong>存储</strong> 或 <strong>应用程序</strong> 选项卡上，具体取决于您的浏览器。 ![Chrome 控制台中的本地存储](https://klaviyo.zendesk.com/hc/article_attachments/17929088337691)</p>
<p>3. 验证浏览器中设置的键和值是否与您匿名时执行的操作匹配。请注意数据的时间戳。 4. 确认数据已存储在浏览器中后，将 <strong><em>*?utm\_email=example@gmail.com</strong><strong> 添加到网站 URL 末尾，用测试电子邮件地址替换 </strong>example@gmail.com</em>* 并重新加载页面。这将根据您提供的电子邮件地址识别浏览器。 5. 在 Klaviyo 中搜索电子邮件地址。您应该会看到与您提供的电子邮件地址相匹配的个人资料，以及与您匿名时所采取的操作相对应的活动时间表。确保本地存储中的键和值已被清除，并且事件已以正确的时间戳进入您的 Klaviyo 帐户。 ## 测试匿名访客结帐时的回填</p>
<p>1. 在私人窗口中导航到您的网站，然后执行“查看产品”等现场操作。 2. 将产品添加到购物车并开始结账</p>
<p>3. 输入您的联系信息</p>
<p>4. 下订单</p>
<p>5. 在 Klaviyo 中搜索电子邮件地址。您应该会看到与您提供的电子邮件地址相匹配的个人资料，以及与您匿名时所采取的操作相对应的活动时间表。确保本地存储中的键和值已被清除，并且事件已以正确的时间戳进入您的 Klaviyo 帐户。 ## 常见问题</p>
<h3>我可以禁用匿名访客活动回填吗？要禁用匿名访客活动回填：</h3>
<p>1. 导航至 Klaviyo 左下角的<strong><em>*帐户 > 设置</strong><strong>。 2. 在帐户设置的</strong>数据<strong>选项卡上，取消选中</strong>启用匿名访客跟踪<strong>框。 3. 选择</strong><strong>更新</strong></em>*按钮。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39973078206363)</p>
<h3>Klaviyo 的标准网络跟踪</h3>
<p>为了让 Klaviyo 默认跟踪购物者的现场活动<strong><em>*，</strong></em>* 必须识别他们的身份。这是通过 [Klaviyo 的 JavaScript](https://help.klaviyo.com/hc/en-us/articles/360002035871) 完成的，它设置一个 [cookie](https://help.klaviyo.com/hc/en-us/articles/360034666712)，允许通过自动生成的 ID 跟踪和识别网站访问者，当他们：</p>
<ul>
<li>填写 Klaviyo 注册表</li>
<li>单击 Klaviyo 消息中的链接</li>
</ul>
<p>该 cookie 可以暂时保存个人身份信息，最长持续时间为两年。 Klaviyo cookie 仅在识别购物者后用于网络跟踪，不会存储匿名访问者的数据。 ### Klaviyo 如何收集匿名访客的现场数据</p>
<p>为了收集匿名访问者的现场数据，Klaviyo 会记录访问者发生的操作数据，并将其存储在本地浏览器中。将来，当该访问者被识别时，该数据就会发送到 Klaviyo 并从浏览器中清除。任何未来的现场活动一旦被识别，都将像往常一样通过 Klaviyo cookie 进行跟踪。要在浏览器中存储数据，购物者的浏览器必须支持本地存储中的设置项目。查看支持[将数据写入本地存储]的浏览器列表(https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage#browser_compatibility)。请注意，如果网站访问者使用任何类型的 cookie 阻止（例如 Chrome 中的隐身模式或 Safari 中的私密浏览），Klaviyo 无法记录和恢复匿名事件。 ### 识别后同步中包含哪些事件？通过 Klaviyo 的网络跟踪，仅捕获客户端事件（也称为前端事件），以识别和匿名访问者。这些事件是通过 Klaviyo 的主要现场跟踪片段（称为 Klaviyo.js）捕获的。一些常见事件包括：</p>
<ul>
<li>现场活跃 - 所有集成</li>
<li>查看的产品 - 大多数电子商务集成</li>
<li>[添加到购物车](https://help.klaviyo.com/hc/en-us/articles/6985692431259) - 大多数电子商务集成</li>
</ul>
<p>但是，通过 [klaviyo.track()](https://developers.klaviyo.com/en/docs/guide_to_setting_up_api_based_website_activity_events) 现场记录的任何事件也包含在匿名活动回填中。请注意，某些集成可能会使用服务器端事件来实现这些目的。例如，Magento 2 上的 <strong>添加到购物车</strong> 事件是在服务器端发送的。 ### 本地存储中可以存储多少个事件？浏览器的本地存储有 5MB 的限制，最多允许 10,000 个事件。 ### 为什么使用本地存储而不是 cookie 来存储数据？与本地存储相比，Cookie 的稳健性较差。例如，cookie 具有到期日期和大约 4KB 的最大大小。本地存储平均可容纳 5 MB（取决于浏览器）。 Safari 的本地存储有 7 天的过期政策。 ### 是否存在任何 GDPR 或隐私问题？匿名访问者活动回填使用浏览器的本地存储来存储作为配置文件属性或事件发送的数据，直到识别浏览器（之后本地数据被清除）。在清除之前，任何网站上的 Javascript 都可以访问本地存储中的数据。如果您通过前端事件发送某些类型的敏感数据，这可能会引起隐私问题。对于敏感数据，Klaviyo 建议仅通过[服务器端请求](https://developers.klaviyo.com/en/v1-2/docs/getting-started-with-track-and-identify-apis) 发送数据，或者仅在识别浏览器后发送数据。 ### 匿名访客活动回填是否可以与 cookie 同意工具一起使用？如果您的商店使用 Cookie 同意工具（例如 [OneTrust](https://help.klaviyo.com/hc/en-us/articles/4764571493275)），则购物者需要选择加入要捕获的匿名活动。如果没有访问权限，Klaviyo 将无法将数据写入浏览器的本地存储。 ### 匿名访客会触发流量吗？ 一旦通过 Klaviyo 的标准网络跟踪识别出匿名访问者，只要他们符合资格并且没有超过时间延迟，他们就会触发流量。</p>
