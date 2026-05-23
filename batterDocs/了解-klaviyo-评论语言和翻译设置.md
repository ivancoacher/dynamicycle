<h1>了解 Klaviyo 评论语言和翻译设置</h1>

<h2>你将会学到</h2>
<p>了解评论小部件的语言、翻译和区域设置。这些设置决定您的小部件和审阅提交表单显示的语言。</p>
<h2>设置默认小部件语言</h2>
<p>默认情况下，所有 Klaviyo 评论内容均为英文。要选择不同的语言：</p>
<p>1. 导航至 Klaviyo 中的<strong><em>*评论</strong></em>*选项卡。</p>
<p>2. 单击<strong><em>*评论设置</strong></em>*。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28858800593179" alt="评论设置选项卡" />
<p>3. 选择<strong><em>*常规</strong></em>*。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28858800595611" alt="评论设置的常规部分" />
<p>4. 在 <strong>选择语言</strong> 菜单中，选择您的首选语言。</p>
<p>更新 Klaviyo 评论的语言会影响以下所有内容：</p>
<ul>
<li>审核提交页面</li>
<li>现场小部件</li>
<li>星级小部件</li>
<li>审查摘要小部件</li>
<li>评论列表小部件</li>
<li>产品评论小部件</li>
<li>精选评论轮播小部件</li>
<li>SEO 小部件（以前称为“所有评论小部件”）</li>
</ul>
<p>您无法使用此方法更新单个小部件的语言设置。所选语言适用于所有小部件，包括您网站上已存在的小部件，并且更改会立即应用。</p>
<p>更新 Klaviyo 评论的语言<em>*</em>*不适用于其他 Klaviyo 功能（例如自定义问题、流程、注册表单、同意页面、客户提交评论的内容等）。这些必须手动翻译和编辑。</p>
<h2>根据每个访问者的浏览器设置设置语言</h2>
<p>Klaviyo 可以使用网站访问者的浏览器设置确定其所在国家/地区。要使用此信息自动选择评论小部件语言：</p>
<p>1. 导航至 Klaviyo 中的<strong><em>*评论</strong></em>*选项卡。</p>
<p>2. 单击<strong><em>*评论设置</strong></em>*。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28858800593179" alt="评论设置选项卡" />
<p>3. 选择<strong><em>*常规</strong></em>*。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28858800595611" alt="评论设置的常规部分" />
<p>4. 打开<strong><em>*根据访客偏好设置语言</strong></em>*开关。</p>
<p>5. 可选：选中选项 <strong>如果可用，请使用访客的送货地点来设置语言。</strong></p>
<p>6. 选择<strong><em>*保存更改</strong></em>*。</p>
<p>评论小部件只能翻译成默认语言下拉菜单中显示的语言。如果 Klaviyo 检测到站点访问者位于尚不支持的区域，则会使用您的默认语言。</p>
<p>送货地点只能在评论提交页面上使用。如果访问者的送货地点不可用，语言将回退到他们的浏览器设置。如果浏览器设置不可用，语言将默认为您在 Klaviyo Reviews 设置中选择的语言。</p>
<h2>以编程方式设置语言（需要自定义代码）</h2>
<p>此选项仅适用于 Klaviyo Reviews 的自定义编码实现。如果您使用拖放编辑器来安装评论小部件，则此选项不可用。</p>
<p>如果您有权访问开发人员，则可以为评论小部件实施自定义编码的语言选择流程。</p>
<p>所有评论小部件都接受 lang 参数，该参数接受 [2 个字母的 ISO 639 语言代码](https://www.iso.org/iso-639-language-code)。您只需将此参数应用于页面上的 1 个评论小部件。一旦为 1 个小部件设置，所有其他小部件也将使用此参数。</p>
<p>正确实现后，评论代码中的语言参数如下所示：</p>
<p>`<div id="klaviyo-reviews-all" data-id="{{product.id}}" lang="en"></div>`</p>
<h3>**lang** 参数和单页应用程序</h3>
<p>该设置是在注入小部件代码时获取的。在单页应用程序中，只有在卸载并重新安装小部件占位符元素时，对 <strong>lang</strong> 参数的实时更改才会生效。</p>
<h2>其他资源</h2>
<ul>
<li>[如何根据语言自定义内容](https://klaviyo.zendesk.com/hc/en-us/articles/115005239028)</li>
<li>[如何自定义评论小部件](https://klaviyo.zendesk.com/hc/en-us/articles/16691401577883)</li>
<li>[如何自定义评论提交页面](https://klaviyo.zendesk.com/hc/en-us/articles/19481466872859)</li>
</ul>
