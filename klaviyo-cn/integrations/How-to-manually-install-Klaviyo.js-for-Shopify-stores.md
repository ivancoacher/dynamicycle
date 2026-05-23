---
id: "360020342232"
title: "如何为 Shopify 商店手动安装 Klaviyo.js"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360020342232-How-to-manually-install-Klaviyo-js-for-Shopify-stores"
section: "Shopify troubleshooting"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:43Z"
language: "zh"
---
## 你将会学到

了解如何在您的 Shopify 商店中手动安装 Klaviyo 的 **Active on Site** 跟踪代码段（也称为 Klaviyo 的现场 JavaScript 或 Klaviyo.js）。仅当您遇到非常高的网络流量或您的网站因任何其他原因加载时间缓慢时才应执行此操作（尽管 Klaviyo 最近[改进了加载时间](https://klaviyo.tech/improving-forms-performance-c67c98114d49)，因此可能不是原因）。否则，我们建议您通过[启用 Klaviyo 的 Shopify 应用嵌入](https://help.klaviyo.com/hc/en-us/articles/4425956184731) 来安装 Klaviyo.js。 ## 开始之前

如果您选择手动安装 Klaviyo.js 并且之前通过 Klaviyo 的应用程序嵌入启用了它，则必须首先在 Shopify 主题设置中禁用该应用程序嵌入。 ![Shopify 中用于现场跟踪的 Klaviyo 应用嵌入已关闭](https://klaviyo.zendesk.com/hc/article_attachments/28716065121563)

由于粘贴此代码需要访问您网站的 HTML 和电子商务平台，因此我们的支持团队无法提供实际帮助。如果您的团队中没有开发人员并且不方便自己添加代码，请考虑[向 Klaviyo 合作伙伴寻求帮助](https://klaviyo.partnerpage.io/)。 ## 在您的 Shopify 商店中安装 Klaviyo.js

1. 复制下面的代码片段：

   ````
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
   ````
2. 在代码片段中，请务必将 PUBLIC\_API\_KEY 替换为 [您的六位 Klaviyo 公共 API 密钥](https://www.klaviyo.com/account#api-keys-tab)。 3. 如果您已为商店启用[客户帐户](https://help.shopify.com/en/manual/customers/customer-accounts)，请添加额外的脚本，以使用客户登录商店时使用的电子邮件来识别他们。完整的脚本集如下所示：

   ````
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
   <脚本类型=“文本/javascript”>
   //在页面加载时初始化Klaviyo对象
   !function(){if(!window.klaviyo){window._klOnsite=window._klOnsite||[];try{window.klaviyo=new Proxy({},{get:function(n,i){return"push"===i?function(){var n;(n=window._klOnsite).push.apply(n,arguments)}:function(){for(var n=arguments.length,o=new Array(n),w=0;w<n;w++)o[w]=arguments[w];var t="function"==typeof o[o.length-1]?o.pop():void 0,e=new Promise((function(n){window._klOnsite.push([i].concat(o,[function(i){t&&t(i),n(i)}]))}));return e}}})}catch(n){window.klaviyo=window.klaviyo||[],window.klaviyo.push=function(){var n;(n=window._klOnsite).push.apply(n,参数)}}}}(); </脚本>
   <脚本类型=“文本/javascript”>
   //客户账户
   var klaviyo = window.klaviyo || []；
   if ("{{ customer.email }}") {klaviyo.identify({"$email" : "{{ customer.email }}"})};
   </脚本>
   ````
4. 在您的 Shopify 管理员中单击 ****在线商店**** > ****主题****。从下拉列表中点击 ****编辑代码****。 ![Shopify 主题页面，操作下拉列表打开，显示编辑代码选项](https://klaviyo.zendesk.com/hc/article_attachments/28716065126043)
5. 搜索要添加代码片段的文件，然后单击在编辑器中将其打开。您可以将该代码段添加到要在相应页面上启用 Klaviyo 表单和跟踪的任何页面模板。 6. 滚动到文件底部并将您的代码片段粘贴到其他代码下方。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30186621806875)
7. 单击****保存****。 ## 测试您的 Active on Site 跟踪

要测试您的 **Active on Site** 跟踪设置是否正确，请按照以下步骤操作：

1. 导航到您的网站。 2. 在您的主页上，将以下内容添加到网址末尾，并将 **example@gmail.com** 替换为您的电子邮件地址：
   **?utm\_email=example@gmail.com
   ![在 Shopify 中测试商店，将 ?utm_email=example@gmail.com 修改为 URL](https://klaviyo.zendesk.com/hc/article_attachments/28716065123227)**
3. 重新加载页面。 4. 在 Klaviyo 中搜索您的电子邮件地址。 ![搜索栏中带有电子邮件地址的 Klaviyo 仪表板](https://klaviyo.zendesk.com/hc/article_attachments/28716065129883)

您应该看到已为您创建了 Klaviyo 个人资料（如果尚不存在），并且已在您的活动源中跟踪此活动。现在您已经安装了 Klaviyo.js，您将能够使用 Active on Site 跟踪、Klaviyo 注册表单等。 根据您在 Shopify 中的客户隐私设置，Klaviyo 可能不会跟踪您位于欧盟、欧洲经济区、英国和瑞士的 Shopify 商店的访问者的现场活动，除非他们已表示同意。 ## 其他资源

- [Shopify 入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005080407)
- [Klaviyo 现场跟踪入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005076767)
- [注册表单入门](https://klaviyo.zendesk.com/hc/en-us/articles/360026474752)