<h1>如何将 Shopify Markets 与 Klaviyo 结合使用</h1>

<h2>你将会学到</h2>
<p>了解如何将 Shopify Markets 与 Klaviyo 集成，以确保您销售的每个区域和语言的客户和产品信息、货币和定价同步到 Klaviyo。 ## 要求</p>
<ul>
<li>您必须拥有配置了 [Shopify Markets](https://help.shopify.com/en/manual/international/managing) 的 Shopify 商店。 - 您的 Klaviyo 帐户必须[与 Shopify 集成](https://help.klaviyo.com/hc/en-us/articles/115005080407)</li>
</ul>
<h2>概述</h2>
<p>如果您使用 Shopify Markets 在多个区域进行销售，则可以使用 Klaviyo 以客户的首选语言和区域向客户发送消息，包括定价、货币和相应市场的 URL。使用Klaviyo进行跨境个性化；使用一个模板向每位收件人发送正确的语言、货币和产品推荐。 ## 如何启用 Shopify 市场</p>
<p>1. 在 Klaviyo 中，选择集成选项卡。 2. 单击 Shopify 访问集成设置页面。 3. 在从 Shopify 同步数据部分中，选中将 Shopify Markets 同步到 Klaviyo 以开始同步店面拥有的每个市场的目录数据。最初同步所有市场目录需要时间</p>
<p>4. 保存您的集成设置。 5. 如果出现提示，请使用与 Klaviyo 集成的帐户登录 Shopify，并批准新的访问权限以同步市场数据</p>
<p>6. 返回 Shopify 后，选择更新集成。 ![](https://klaviyo.zendesk.com/hc/article_attachments/45224022464283)</p>
<h2>同步了什么</h2>
<p>Klaviyo 将同步 Shopify 配置文件、事件和目录数据中的区域设置信息。区域设置是语言和区域信息的组合。位于美国的英语使用者的区域设置为“en-US”，位于美国的西班牙语使用者的区域设置为“es-US”。 ### 个人资料</p>
<ul>
<li>语言环境</li>
<li>Locale 属性包括从 Shopify 同步的配置文件的区域设置（例如“en-US”）。 - 如果 Shopify 未知，Shopify 同步配置文件可能并不总是包含语言或区域设置信息。 ### 活动</li>
</ul>
<ul>
<li>语言环境</li>
<li>Shopify 中的所有订单相关事件都将包含区域设置。有关每个事件的详细信息以及区域设置信息，请参阅 [Shopify 数据参考](https://help.klaviyo.com/hc/en-us/articles/115005080447)。 ### 目录</li>
</ul>
<ul>
<li>语言环境</li>
<li>您店面支持的每种区域和语言组合都将同步到 Klaviyo，以获取目录中的所有产品和变体。这包括产品和变体标题、价格、价格比较、状态、货币和 URL 的本地化版本。 ## 如何在 Klaviyo 中使用区域设置感知的 Shopify Markets</li>
</ul>
<p>同步后，区域设置数据可以在 Klaviyo 中使用，为您的客户提供更个性化的体验。 ### 智能翻译</p>
<p>借助 Klaviyo 中的 Shopify Markets，智能翻译中使用的动态产品块将自动将客户的语言和国家/地区与符合其偏好的产品信息、货币和定价进行匹配。当产品未在特定国家/地区销售时，该产品将不会推荐给该国家/地区的客户。 1. 在智能翻译编辑器中，选择后备目录区域设置。这将与客户国家/地区未知一起使用</p>
<p>1. 可以从您的帐户设置中配置每种语言的默认后备目录区域设置。 2. 如果您选择了多种语言进行翻译，请单击顶部的箭头或使用下拉菜单在语言之间切换。 ![](https://klaviyo.zendesk.com/hc/article_attachments/45224022465435)</p>
<p>3. 预览电子邮件时，您可以输入任何区域设置的配置文件，以查看客户将看到的动态区域化示例</p>
<h3>静态积块</h3>
<p>查看使用静态乘积块的[完整指南](https://help.klaviyo.com/hc/en-us/articles/115000219092)</p>
<p>对于自动本地化，请选中阻止设置中的<strong><em>*本地化收件人</strong></em>*复选框。 ![](https://klaviyo.zendesk.com/hc/article_attachments/47692428749467)</p>
<p>启用后，静态产品块将根据发送时收件人的语言和区域自动显示本地化产品定价、货币和信息，这与动态产品块与智能翻译配合使用的方式相同。如果收件人的区域设置未知，则阻止将回退到您的 Shopify 商店中配置的默认市场。 这样就无需为每个区域创建单独的静态产品块，也无需依靠智能翻译来处理共享语言的区域（例如美国、英国和澳大利亚的英语客户）之间的定价差异。手动选择本地化产品：</p>
<p>1. 从静态产品块选择器中，选择区域设置感知目录。对于 Shopify 集成，目录名称为“Shopify：默认”</p>
<p>2. 将出现语言和区域输入。选择您想要包含的产品的语言和区域。 3. 选择添加产品。 ![](https://klaviyo.zendesk.com/hc/article_attachments/45224038988955)</p>
<h3>目录查找标签</h3>
<p>查看使用目录查找标签的[完整指南](https://help.klaviyo.com/hc/en-us/articles/360004785571)</p>
<h4>按语言环境过滤</h4>
<p>目录标签中有两个新的语言和区域过滤器。区域设置语言和区域可以使用 ISO 3166 和 639 标准通过两个字母的国家和语言代码来引用。产品的区域化版本包括标题、价格和 URL 等值。此示例显示了 Shopify 产品的加拿大法语版本。 ````</p>
<p>{% 目录“SAMPLE_ITEM”集成='shopify' 语言='fr' 区域='CA' %}</p>
<p>{{catalog_item.title}}</p>
<p>{% 最终目录 %}</p>
<p>````</p>
<p>如果找不到本地化产品，将使用默认产品信息。 #### 货币模板标签</p>
<p>本地化产品的代码和符号可以通过模板标签引用。此示例显示对货币符号和货币代码的引用。 - 货币\_符号</p>
<ul>
<li>用于表示货币单位的图形符号</li>
<li>货币\_代码</li>
<li>用于表示货币的字母代码</li>
</ul>
<p>````</p>
<p>{% 目录“SAMPLE_ITEM”集成='shopify' 语言='fr' 区域='CA' %}</p>
<p>{{catalog_item.title}}</p>
<p><a href="{{ Catalog_item.url }}"></p>
<p><img alt="{{catalog_item.title }}" src="{{catalog_item.image_full_url }}" > 的图片</p>
<p>{{ Catalog_item.currency_symbol }}</p>
<p>{{catalog_item.price}}</p>
<p>{{catalog_item.currency_code}}</p>
<p>{% 最终目录 %}</p>
<p>````</p>
<h3>根据区域设置和 Shopify 市场进行细分</h3>
<p>通过区域设置、区域设置语言和区域设置国家/地区属性，您可以根据 Shopify 市场对客户进行细分。 <strong><em>*使用案例</strong></em>*</p>
<p>我想按照讲西班牙语的客户来细分我的客户，无论他们位于哪个国家/地区</p>
<p><strong><em>*解决方案</strong></em>*</p>
<p>使用区域设置语言 = ‘es’ 的分段</p>
<p><strong><em>*使用案例</strong></em>*</p>
<p>我希望根据在英国购物的客户对客户进行细分，无论他们使用哪种语言</p>
<p><strong><em>*解决方案</strong></em>*</p>
<p>使用区域设置国家/地区=“GB”的分段</p>
<p><strong><em>*使用案例</strong></em>*</p>
<p>我想按在比利时购物并讲法语的客户对客户进行细分</p>
<p><strong><em>*解决方案</strong></em>*</p>
<p>使用 Locale = ‘fr-BE’ 的分段</p>
<h3>随区域设置和 Shopify 市场流动</h3>
<p>您可以使用此区域设置信息来个性化您的 Flow 中的内容。大多数 Shopify 事件将在事件数据中包含可在消息中使用的区域设置信息。智能翻译还可用于本地化带有产品数据的消息。 Klaviyo 有一组预建的流程模板，将自动引用相关货币和翻译后的产品信息</p>
<ul>
<li>添加本地化的[废弃结账流程](https://www.klaviyo.com/flows/create?object_id=WvMGgv)</li>
<li>添加本地化的【订单确认流程】(https://www.klaviyo.com/flows/create?object_id=Seu8ne)</li>
</ul>
<h2>故障排除</h2>
<p>为什么我无法启用 Shopify Markets？ - 每个 Shopify 账户只能启用一次 Shopify Markets。如果您的 Shopify 帐户已在单独的 Klaviyo 帐户上启用了 Shopify 市场，您可以关闭该帐户上的 Shopify Markets，然后在您想要的 Klaviyo 帐户上启用它</p>
<ul>
<li>您的 Shopify 帐户可能位于旧版本的 Shopify Markets 上。您可以使用 [Shopify 测试驱动](https://help.shopify.com/en/manual/markets-new#markets-sp) 启用新版本的 Shopify Markets。 Klaviyo 建议您在启用 Shopify 试驾之前联系 Shopify。为什么我看不到我的 Shopify B2B 或零售市场？ - Klaviyo 支持 Shopify 区域市场，目前不同步 B2B 或零售市场</li>
</ul>
<p>我在 Klaviyo 中看不到我的本地化产品</p>
<ul>
<li>根据您的目录大小，本地化产品数据的初始同步可能需要几天时间</li>
</ul>
