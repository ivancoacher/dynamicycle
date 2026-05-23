<h1>如何使用自定义 CSS 设计 Klaviyo Reviews 小部件的样式</h1>

<h2>你将会学到</h2>
<p>了解 Klaviyo Reviews 的自定义 CSS，包括如何实现一些基本用例。有关更高级的用例，请访问我们的 [Klaviyo Reviews 的自定义 CSS 开发人员资源](https://developers.klaviyo.com/en/docs/klaviyo_reviews_css_class_reference)。大多数小部件自定义可以使用[拖放编辑器](https://help.klaviyo.com/hc/en-us/articles/16691401577883)来实现；仅高级用例需要 CSS。为评论小部件实现自定义 CSS 涉及编辑网站的代码。仅建议精通技术的营销人员或能够接触开发人员的人员使用此方法。虽然我们的产品确实支持自定义 CSS，但我们的支持团队无法帮助您自定义超出本文档涵盖的一般指导的小部件。为了维护您的数据安全，Klaviyo 的支持团队无法打开您的 HTML 文件。 ## 关于 Klaviyo 评论的自定义 CSS</p>
<p>Klaviyo Reviews 提供了广泛的 CSS 类选择器，可用于编写自定义 CSS 并将高级样式选项应用到您的评论小部件。欲了解更多信息，请访问我们的[Klaviyo Reviews CSS 类完整词典](https://developers.klaviyo.com/en/docs/klaviyo_reviews_css_class_reference)。 ## 如何应用自定义 CSS</p>
<p>您可以将自定义 CSS 应用到 Klaviyo Reviews，就像应用任何其他自定义 CSS 一样：</p>
<ul>
<li>将自定义 CSS 添加到站点的主 CSS 样式表中。 - 在单个页面的代码中插入 <style> 标签以将 CSS 应用于该页面。 - 将 CSS 嵌入单个 HTML 元素（例如 div）中，以将其仅应用于该元素。 - 在****主题设置 > 自定义 CSS**** (Shopify) 或 ****样式 > CSS**** (WooCommerce) 中将自定义 CSS 添加到您的整个网站。我们将在这里重点关注最后一个选项，因为它是最简单的实现方式。请注意，Klaviyo 评论（包括默认样式）通常在电子商务平台的 CSS 之后加载。这意味着使用精确的选择器非常重要，这样您的自定义 CSS 就不会被默认值覆盖。 ### 为 Shopify 应用自定义 CSS</li>
</ul>
<p>1. 在您的 Shopify 后台中，导航至<strong><em>*在线商店 > 主题</strong><strong>。 2. 从当前主题的附加选项菜单（3 个点）中，单击 </strong><strong>Duplicate.</strong></em>*</p>
<p>不建议在当前主题上线时对其进行编辑，因为这些编辑可能会在您查看更改并解决任何问题之前向网站访问者显示。 ![复制您的主题](https://klaviyo.zendesk.com/hc/article_attachments/28717854192283)</p>
<p>3. 单击新主题副本旁边的<strong><em>*自定义</strong></em>*。 4. 单击主题设置图标。 ![主题设置按钮](https://klaviyo.zendesk.com/hc/article_attachments/28717881714203)</p>
<p>5. 从菜单中选择<strong><em>*自定义 CSS</strong></em>*。 ![自定义 css 字段](https://klaviyo.zendesk.com/hc/article_attachments/28717854198427)</p>
<p>6. 添加您的自定义 CSS。可以在下面的部分中复制示例 CSS 片段。 7. 导航到编辑器中显示评论小部件的页面（例如<strong><em>*默认产品</strong><strong>）。 8. 检查编辑内容，然后单击</strong><strong>发布</strong></em>*。 ### 为 WooCommerce 添加自定义 CSS</p>
<p>您必须使用页面 ID 选择器`.page-id-YOUR_PAGE_ID` 将 CSS 应用到特定页面。了解如何[查找页面 ID](https://wordpress.com/support/pages/#find-the-page-id)。 1. 在 WordPress 管理员中，导航至<strong><em>*外观 > 编辑器</strong><strong>。 2. 选择</strong><strong>样式</strong></em>*。 ![样式选项](https://klaviyo.zendesk.com/hc/article_attachments/28717854201883)</p>
<p>3. 打开三个点（<strong>更多</strong>）菜单。 4. 选择<strong><em>*其他 CSS</strong></em>*。 ![附加 CSS 选项](https://klaviyo.zendesk.com/hc/article_attachments/28717881720347)</p>
<p>5. 添加您的自定义 CSS。可以在下面的部分中复制示例 CSS 片段。 6. 检查编辑内容，然后单击<strong><em>*发布</strong></em>*。 ## 自定义 CSS 用例</p>
<p>下面的 CSS 片段涵盖了一些基本用例。更高级的定制需要开发人员的支持。如果您的团队中没有开发人员并且不方便自己编写代码，请考虑联系 [Klaviyo 合作伙伴](https://connect.klaviyo.com/) 寻求帮助。 <strong><em>*评级图标（星）外观</strong></em>*</p>
<p>将下面的 URL 替换为分别代表您首选的全星、部分星和空星的图像 URL。请注意，对于 Shopify 商店，根据其规则，您的 URL 必须引用 Shopify 中存储的图像。 ````</p>
<p>#klaviyo-产品评论-包装{</p>
<p>.kl_reviews__star {</p>
<p>显示：无；</p>
<p>}</p>
<p>.kl_reviews__full_star {</p>
<p>背景图像：url(“https://cdn.shopify.com/s/files/1/0284/3128/6351/files/full-moon.png?v=1705073898”);</p>
<p>背景大小：封面；</p>
<p>}</p>
<p>.kl_reviews__partial_star {</p>
<p>背景图像：url(“https://cdn.shopify.com/s/files/1/0284/3128/6351/files/last-quarter-moon.png?v=1705073898”);</p>
<p>背景大小：封面；</p>
<p>}</p>
<p>.kl_reviews__empty_star {</p>
<p>背景图像：url(“https://cdn.shopify.com/s/files/1/0284/3128/6351/files/new-moon.png?v=1705073898”);</p>
<p>背景大小：封面；</p>
<p>}</p>
<p>}</p>
<p>````</p>
<p><strong><em>*图像缩略图大小</strong></em>*</p>
<p>为评论列表中客户提交的图像设置特定宽度。 `#klaviyo-product-reviews-wrapper .kl_reviews__review__image { 宽度：225px; }`</p>
<p><strong><em>*按钮颜色和样式</strong></em>*</p>
<p>仅将样式应用于<strong><em>*撰写评论</strong></em>*按钮。 ````</p>
<p>#klaviyo-product-reviews-wrapper .kl_reviews__button:nth-child(1) {</p>
<p>颜色: 蓝色;</p>
<p>框阴影：0 0 15px #9ecaed；</p>
<p>}</p>
<p>````</p>
<p>仅将样式应用于<strong><em>*问问题</strong></em>*按钮。 ````</p>
<p>#klaviyo-product-reviews-wrapper .kl_reviews__button:nth-child(2) {</p>
<p>颜色: 蓝色;</p>
<p>框阴影：0 0 15px #9ecaed；</p>
<p>}</p>
<p>````</p>
