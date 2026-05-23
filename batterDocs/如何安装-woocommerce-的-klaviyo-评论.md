<h1>如何安装 WooCommerce 的 Klaviyo 评论</h1>

<h2>你将会学到</h2>
<p>了解如何在 WooCommerce 商店上安装 Klaviyo 评论并添加评论小部件。要了解开始所需的所有步骤，请前往 [Klaviyo Reviews 入门]。(https://klaviyo.zendesk.com/hc/en-us/articles/15937542819355)</p>
<h2>开始之前</h2>
<p>有 4 种安装 Klaviyo Reviews for WooCommerce 的方法。适合您的方法取决于您的技术知识水平和 WordPress 设置。使用下面的流程图选择最适合您的安装方法。 ![流程图表明不习惯使用代码的用户应该添加插件并使用可视化主题编辑器；那些无法访问主题文件的人应该使用插件和代码片段；那些使用第三方或自定义主题的人应该使用短代码，那些有权访问其网站的functions.php 文件的人应该直接修改他们的主题文件。这些选项从技术难度最小的开始，到技术难度最大的选项结束。](https://klaviyo.zendesk.com/hc/article_attachments/28722599957275)</p>
<p>选择安装方法时，请考虑以下因素：</p>
<ul>
<li>仅支持两种安装方法向收藏页面添加星级：带有可视化编辑器的插件和短代码。 - 考虑您在 WordPress 中的编辑器访问级别。并非所有用户都可以选择直接编辑网站主题文件。如果您无法访问 [functions.php 文件](https://developer.wordpress.org/themes/core-concepts/custom-functionity/) 或类似文件，请使用其他方法之一。 - 其中一些方法需要向您的 WordPress 站点添加另一个插件。下面的说明引用了代码片段插件，但 Klaviyo 不认可任何特定插件，也无法协助解决与插件相关的问题。选择适合您的安装步骤后，请继续执行相关说明。了解如何通过以下方式安装 Klaviyo Reviews for WooCommerce：</li>
<li>[安装插件并使用可视化主题编辑器](#h_01J1FFYXRRSR45ACAKVXCNQB91)</li>
<li>[安装插件，不使用可视化主题编辑器](#h_01J1FFZZ2EHN1PKBZXEHA4MSEK)</li>
<li>[添加短代码](#h_01J1FG22Y6SERD6MYYC0T28AD9)</li>
<li>[修改主题文件](#h_01J1FG38N26A6DCNCRG02YR0W9)</li>
</ul>
<h2>可用的评论小部件</h2>
<p>安装 Klaviyo Reviews 后，您的商店将显示评论小部件，其中包含评级和评论详细信息。 - <strong><em>*星级小部件</strong></em>*</p>
<p>显示特定产品的当前星级，并且通常添加在产品页面或产品系列页面上的产品名称下方。 ![星级](https://klaviyo.zendesk.com/hc/article_attachments/28722611980187)</p>
<ul>
<li>****产品评论小部件****</li>
</ul>
<p>显示一个图表，详细列出产品收到的所有评分、提交评论的用户图像以及产品收到的最常见反馈。下面是所有已发布评论和客户问题的列表，以及搜索栏、评论过滤器、<strong><em>*撰写评论</strong><strong>按钮和</strong><strong>提出问题</strong></em>*按钮。该小部件通常添加在产品页面底部附近。 ![摘要小部件](https://klaviyo.zendesk.com/hc/article_attachments/28722599979035)</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28722611982363" alt="评论列表" />
<ul>
<li>****特色评论轮播小部件****</li>
</ul>
<p>显示您所有产品的突出评论。您可以在主页、独立评论页面或网站上的任何其他位置上展示此内容。您还可以选择此小部件中的评论。如果有的话，客户提交的图像会附在每次评论中；如果未提交图像，则会使用您的产品图像。 ![评论轮播](https://klaviyo.zendesk.com/hc/article_attachments/28722599980571)</p>
<ul>
<li>****SEO / 所有评论小部件****</li>
</ul>
<p>在一个页面上显示您对所有产品的所有评论。使用此小部件可以改进您的搜索引擎优化，并为潜在客户提供一个单一的位置来查看当前客户的喜好。此小部件通常添加到您网站上的独立<strong>评论</strong>页面。 ![所有评论小部件](https://klaviyo.zendesk.com/hc/article_attachments/28722599987355)</p>
<h2>安装插件并使用可视化主题编辑器</h2>
<p>为了使用可视化主题编辑器将 Klaviyo Reviews 小部件添加到您的网站，您必须首先添加一段代码以在主题中加载这些拖放块。 您可以使用 [代码片段](https://wordpress.org/plugins/code-snippets/) 等工具添加这些块的源代码，然后使用可视化主题编辑器将 Klaviyo Reviews 小部件拖放到您的主题中。 ### 添加评论小部件源代码</p>
<p>这些说明假设您已经安装了 [代码片段](https://wordpress.org/plugins/code-snippets/) 插件，但您可以使用其他插件。 1. 从 Wordpress 侧边栏选择<strong><em>*代码段 > 添加新</strong></em>*。 ![Wordpress 侧边栏中的“片段”选项](https://klaviyo.zendesk.com/hc/article_attachments/28722611964443)</p>
<p>2. 在 <strong>在此处输入标题</strong> 字段中，为片段命名清晰的名称，例如“Klaviyo Reviews Widgets Code”。 3. 在 <strong>代码</strong> 部分的 <strong>函数 (PHP)</strong> 选项卡中，添加下面的代码片段。 4. 单击<strong><em>*保存更改并激活</strong></em>*。 #### 评论小部件源代码</p>
<p>````</p>
<p>函数register_klaviyo_reviews_blocks() {</p>
<p>// 注册块</p>
<p>register_block_type( 'klaviyo/产品评论', array(</p>
<p>'editor_script' => 'klaviyo-block-editor-script',</p>
<p>'render_callback' => 'render_klaviyo_product_reviews',</p>
<p>））；</p>
<p>register_block_type( 'klaviyo/产品星级评级', array(</p>
<p>'editor_script' => 'klaviyo-block-editor-script',</p>
<p>'render_callback' => 'render_klaviyo_star_ ratings',</p>
<p>））；</p>
<p>register_block_type( 'klaviyo/特色评论', array(</p>
<p>'editor_script' => 'klaviyo-block-editor-script',</p>
<p>'render_callback' => 'render_klaviyo_featured_reviews',</p>
<p>））；</p>
<p>register_block_type( 'klaviyo/all-reviews', array(</p>
<p>'editor_script' => 'klaviyo-block-editor-script',</p>
<p>'render_callback' => 'render_klaviyo_all_reviews',</p>
<p>））；</p>
<p>}</p>
<p>add_action( 'init', 'register_klaviyo_reviews_blocks' );</p>
<p>函数 enqueue_klaviyo_block_editor_assets() {</p>
<p>// 注册并入队徽标图像</p>
<p>wp_注册脚本（</p>
<p>'klaviyo-块编辑器脚本',</p>
<p>假的，</p>
<p>数组( 'wp-blocks', 'wp-element', 'wp-editor' ),</p>
<p>假的，</p>
<p>真实</p>
<p>）；</p>
<p>$logo_url = plugins_url( 'img/klaviyo-logo.png', 'klaviyo/klaviyo.php' );</p>
<p>wp_add_inline_script( 'klaviyo-block-editor-script', '</p>
<p>（函数（块，元素）{</p>
<p>var el = element.createElement;</p>
<p>// 添加自定义类别</p>
<p>block.updateCategory( "小部件", {</p>
<p>弹头：“klaviyo”，</p>
<p>标题：“克拉维约”，</p>
<p>图标: el("img", { src: "' . $logo_url . '", 样式: { 宽度: "20px", 高度: "20px" } })</p>
<p>} );</p>
<p>block.registerBlockType(“klaviyo/产品评论”, {</p>
<p>标题：“Klaviyo 产品评论”，</p>
<p>图标：“管理员评论”，</p>
<p>类别：“克拉维约”，</p>
<p>编辑：函数（）{</p>
<p>返回 el(</p>
<p>“div”，</p>
<p>{ className: "klaviyo-产品评论" },</p>
<p>“此处将显示 Klaviyo 产品评论”</p>
<p>）；</p>
<p>},</p>
<p>保存：函数（）{</p>
<p>返回空值；</p>
<p>},</p>
<p>});</p>
<p>block.registerBlockType(“klaviyo/产品星级评级”, {</p>
<p>title: "Klaviyo 星级评定",</p>
<p>图标：“充满星星”，</p>
<p>类别：“克拉维约”，</p>
<p>编辑：函数（）{</p>
<p>返回 el(</p>
<p>“div”，</p>
<p>{ className: "klaviyo-产品星级-评级" },</p>
<p>“此处将显示 Klaviyo 产品星级”</p>
<p>）；</p>
<p>},</p>
<p>保存：函数（）{</p>
<p>返回空值；</p>
<p>},</p>
<p>});</p>
<p>block.registerBlockType(“klaviyo/特色评论”, {</p>
<p>标题：“Klaviyo 精选评论”，</p>
<p>图标：“管理帖子”，</p>
<p>类别：“克拉维约”，</p>
<p>编辑：函数（）{</p>
<p>返回 el(</p>
<p>“div”，</p>
<p>{ className: "klaviyo-featured-reviews" },</p>
<p>“此处将显示 Klaviyo 精选评论”</p>
<p>）；</p>
<p>},</p>
<p>保存：函数（）{</p>
<p>返回空值；</p>
<p>},</p>
<p>});</p>
<p>block.registerBlockType(“klaviyo/all-reviews”, {</p>
<p>标题：“Klaviyo 所有评论”，</p>
<p>图标：“管理页面”，</p>
<p>类别：“克拉维约”，</p>
<p>编辑：函数（）{</p>
<p>返回 el(</p>
<p>“div”，</p>
<p>{ className: "klaviyo-all-reviews" },</p>
<p>“Klaviyo 所有评论都将显示在这里”</p>
<p>）；</p>
<p>},</p>
<p>保存：函数（）{</p>
<p>返回空值；</p>
<p>},</p>
<p>});</p>
<p>} )(</p>
<p>窗口.wp.块，</p>
<p>窗口.wp.元素</p>
<p>）；</p>
<p>'）；</p>
<p>}</p>
<p>add_action( 'enqueue_block_editor_assets', 'enqueue_klaviyo_block_editor_assets' );</p>
<p>// 渲染块的回调函数</p>
<p>函数 render_klaviyo_product_reviews( $attributes, $content ) {</p>
<p>全球$产品；</p>
<p>if ( is_product() && isset($product) ) {</p>
<p>返回“<div id='klaviyo-reviews-all' data-id='” 。 esc_attr($product->get_id()) 。 “'></div>”；</p>
<p>}</p>
<p>}</p>
<p>函数 render_klaviyo_star_ ratings( $attributes, $content ) {</p>
<p>全球$产品；</p>
<p>如果（isset（$产品））{</p>
<p>返回“<div class='klaviyo-star- rating-widget' data-id='” 。 esc_attr($product->get_id()) 。 “'></div>”；</p>
<p>}</p>
<p>}</p>
<p>函数 render_klaviyo_featured_reviews( $attributes, $content ) {</p>
<p>返回“<div id='klaviyo-featured-reviews-carousel'></div>”；</p>
<p>}</p>
<p>函数 render_klaviyo_all_reviews( $attributes, $content ) {</p>
<p>返回“<div id='fulfilled-reviews-all' data-id='all'></div>”；</p>
<p>}</p>
<p>````</p>
<h3>添加 Klaviyo 评论插件</h3>
<p>1. 导航至<strong><em>*外观 > 编辑器</strong><strong>。 2. 选择</strong><strong>模板</strong><strong>。 3. 选择您的</strong>单一产品<strong>模板。请注意，它的名称可能略有不同。 4. 单击</strong><strong>+</strong></em>* 打开阻止菜单。 ![Wordpress 可视化编辑器中的 + 选项](https://klaviyo.zendesk.com/hc/article_attachments/28722599964955)</p>
<p>5. 导航至 <strong>Blocks</strong> 菜单的 <strong>Klaviyo</strong> 部分。 ![Wordpress 可视化编辑器的 Klaviyo 部分阻止菜单](https://klaviyo.zendesk.com/hc/article_attachments/28722599969307)</p>
<p>6. 将 Klaviyo Reviews 小部件拖放到您的主题中。 7. 单击<strong><em>*保存</strong></em>*。 ### 添加收藏星级小部件</p>
<p>1. 导航至<strong><em>*外观 > 编辑器</strong><strong>。 2. 选择</strong><strong>模板</strong><strong>。 3. 选择包含产品集合的页面。 4. 单击</strong><strong>+</strong></em>* 打开阻止菜单。 ![Wordpress 可视化编辑器中的 + 选项](https://klaviyo.zendesk.com/hc/article_attachments/28722599964955)</p>
<p>5. 导航至 <strong>Blocks</strong> 菜单的 <strong>Klaviyo</strong> 部分。 6. 将<strong><em>*星级</strong><strong>小部件拖到集合中的任何产品上。 7. 单击</strong><strong>保存</strong></em>*。 如果需要，请使用下面的代码片段将星级小部件居中对齐。请注意，您必须将 YOUR\_PAGE\_ID 占位符替换为集合页面的页面 ID。了解如何[查找页面 ID](https://wordpress.com/support/pages/#find-the-page-id)。 ````</p>
<p>.page-id-YOUR_PAGE_ID</p>
<p>.klaviyo-星级评级小部件{</p>
<p>显示：柔性；</p>
<p>调整内容：居中；</p>
<p>对齐项目：居中；</p>
<p>文本对齐：居中；</p>
<p>保证金：0 自动；</p>
<p>}</p>
<p>````</p>
<h2>安装插件并使用代码添加小部件</h2>
<p>使用此方法时，小部件会根据 WooCommerce [视觉挂钩](https://wordpress.org/plugins/woo-visual-hook-guide/) 的位置添加到您的网站。因此，如果您的产品页面上没有 WooCommerce 小部件，则必须使用备用安装选项。此过程需要添加第三方代码片段工具，因此您可以将代码添加到您的网站，而无需直接编辑主题文件。您可以使用 [代码片段](https://wordpress.org/plugins/code-snippets/) 等工具来添加这些小部件的代码。 ### 添加评论小部件源代码</p>
<p>这些说明假设您已经安装了 [代码片段](https://wordpress.org/plugins/code-snippets/) 插件，但您可以使用其他插件。 1. 从 Wordpress 侧边栏选择<strong><em>*代码段 > 添加新</strong></em>*。 ![Wordpress 侧边栏中的片段菜单](https://klaviyo.zendesk.com/hc/article_attachments/28722599971739)</p>
<p>2. 在 <strong>在此处输入标题</strong> 字段中，为片段命名清晰的名称，例如“Klaviyo Reviews Widgets Code”。 3. 在 <strong>代码</strong> 部分的 <strong>函数 (PHP)</strong> 选项卡中，添加以下代码片段。 4. 单击<strong><em>*保存更改并激活</strong></em>*。您必须为计划使用的每个小部件安装一个代码片段。以下部分概述了每个小部件的代码。 ### 产品评论小部件代码片段</p>
<p>要调整小部件在网站上的位置，请在“add_action”函数中编辑 (“woocommerce_after_single_product_summary”) 的位置和优先级 (“15”)。 ````</p>
<p>函数 klaviyo_add_product_reviews_widget() {</p>
<p>全球$产品；</p>
<p>if (is_product() && isset($product)) {</p>
<p>$product_id = $product->get_id();</p>
<p>echo "<div id='klaviyo-reviews-all' data-id='{$product_id}'></div>";</p>
<p>}</p>
<p>}</p>
<p>add_action('woocommerce_after_single_product_summary', 'klaviyo_add_product_reviews_widget', 15);</p>
<p>````</p>
<h3>星级评分小部件代码片段</h3>
<p>要调整小部件在网站上的位置，请在“add_action”函数中编辑 (“woocommerce_single_product_summary”) 的位置和优先级 (“6”)。 ````</p>
<p>函数 klaviyo_add_product_star_ ratings_widget() {</p>
<p>全球$产品；</p>
<p>if (is_product() && isset($product)) {</p>
<p>$product_id = $product->get_id();</p>
<p>echo "<div class='klaviyo-star- rating-widget' data-id='{$product_id}'></div>";</p>
<p>}</p>
<p>}</p>
<p>add_action('woocommerce_single_product_summary', 'klaviyo_add_product_star_ ratings_widget', 6);</p>
<p>````</p>
<h3>其他可选代码片段</h3>
<p>使用这些代码片段在您网站的任何位置添加可选小部件。请注意，您必须将这些添加到特定页面的 HTML 中；它们无法添加到您的functions.php 文件中。 #### SEO 小工具</p>
<p>`<div id='klaviyo-reviews-all' data-id='all'></div>`</p>
<h4>特色评论轮播小部件</h4>
<p>`<div id='klaviyo-featured-reviews-carousel'></div>`</p>
<h2>添加短代码</h2>
<p>此过程涉及首先在主题文件中注册短代码，然后将短代码插入网站上的任何位置。要完成此操作，您必须首先添加第三方代码片段工具，以便您可以将代码添加到您的网站，而无需直接编辑主题文件。您可以使用 [代码片段](https://wordpress.org/plugins/code-snippets/) 等工具来添加这些小部件的代码。 ### 注册短代码并添加小部件</p>
<p>这些说明假设您已经安装了 [代码片段](https://wordpress.org/plugins/code-snippets/) 插件，但您可以使用其他插件。 1. 从 Wordpress 侧边栏选择<strong><em>*代码段 > 添加新</strong></em>*。 ![Wordpress 侧边栏中的片段菜单](https://klaviyo.zendesk.com/hc/article_attachments/28722611974171)</p>
<p>2. 在 <strong>在此处输入标题</strong> 字段中，为片段命名清晰的名称，例如“Klaviyo Reviews Widgets Code”。 3. 在 <strong>代码</strong> 部分的 <strong>函数 (PHP)</strong> 选项卡中，添加以下代码片段。 4. 单击<strong><em>*保存更改并激活</strong></em>*。 5. 将每个小部件的短代码添加到您希望显示小部件的页面。 ### 代码片段和短代码</p>
<h3>产品评论小部件</h3>
<p>代码片段（添加到“函数 (PHP)”选项卡）：</p>
<p>````</p>
<p>函数 klaviyo_add_product_reviews_widget() {</p>
<p>全球$产品；</p>
<p>如果（isset（$产品））{</p>
<p>$product_id = $product->get_id();</p>
<p>$tag = "<div id='klaviyo-reviews-all' data-id='{$product_id}'></div>";</p>
<p>返回$标签；</p>
<p>}</p>
<p>}</p>
<p>add_shortcode('klaviyo-reviews-all', 'klaviyo_add_product_reviews_widget');</p>
<p>````</p>
<p><strong><em>*短代码：</strong></em>* [klaviyo-reviews-all]</p>
<h3>星级小部件</h3>
<p>代码片段（添加到“函数 (PHP)”选项卡）：</p>
<p>````</p>
<p>函数 klaviyo_add_product_star_ ratings_widget() {</p>
<p>全球$产品；</p>
<p>如果（isset（$产品））{</p>
<p>$product_id = $product->get_id();</p>
<p>$tag = "<div class='klaviyo-star- rating-widget' data-id='{$product_id}'></div>";</p>
<p>返回$标签；</p>
<p>}</p>
<p>}</p>
<p>add_shortcode('klaviyo_star_ rating', 'klaviyo_add_product_star_ ratings_widget');</p>
<p>````</p>
<p><strong><em>*短代码：</strong></em>* [klaviyo\_star\_ rating]</p>
<p>将此短代码添加到您的产品页面以显示单个产品的星级，或添加到任何产品系列页面以显示产品系列中所有商品的星级。 ### SEO / 所有评论和特色轮播小部件</p>
<p>代码片段（添加到“函数 (PHP)”选项卡）：</p>
<p>````</p>
<p>函数 klaviyo_add_featured_reviews_widget() {</p>
<p>返回“<div id='klaviyo-featured-reviews-carousel'></div>”；</p>
<p>}</p>
<p>函数 klaviyo_add_all_reviews_widget() {</p>
<p>返回“<div id='fulfilled-reviews-all' data-id='all'></div>”；</p>
<p>}</p>
<p>````</p>
<p><strong><em>*短代码：</strong></em>* [klaviyo-featured-reviews-carousel]</p>
<p><strong><em>*短代码：</strong></em>* [fulfilled-reviews-all]</p>
<h2>直接修改你的主题文件</h2>
<p>如果您有权访问 WordPress 实例的functions.php 文件，请使用下面的代码片段添加评论小部件。这些说明适用于具有 Wordpress PHP 经验的开发人员。如果您不熟悉 Wordpress PHP，请使用替代方法。 ### 产品评论小部件代码片段</p>
<p>````</p>
<p>// 创建一个函数来呈现具有正确产品 ID 的动态 div</p>
<p>函数 klaviyo_add_product_reviews_widget() {</p>
<p>全球$产品；</p>
<p>if (is_product() && isset($product)) {</p>
<p>$product_id = $product->get_id();</p>
<p>echo "<div id='klaviyo-reviews-all' data-id='{$product_id}'></div>";</p>
<p>}</p>
<p>}</p>
<p>// 将小部件放置在单品摘要之后</p>
<p>add_action('woocommerce_after_single_product_summary', 'klaviyo_add_product_reviews_widget', 15);</p>
<p>````</p>
<h3>星级评分小部件代码片段</h3>
<p>````</p>
<p>// 创建一个函数来呈现具有正确产品 ID 的动态 div</p>
<p>函数 klaviyo_add_product_star_ ratings_widget() {</p>
<p>全球$产品；</p>
<p>if (is_product() && isset($product)) {</p>
<p>$product_id = $product->get_id();</p>
<p>echo "<div class='klaviyo-star- rating-widget' data-id='{$product_id}'></div>";</p>
<p>}</p>
<p>}</p>
<p>// 将小部件放置在单品摘要之后</p>
<p>add_action('woocommerce_single_product_summary', 'klaviyo_add_product_star_ ratings_widget', 6);</p>
<p>````</p>
<h3>其他可选代码片段</h3>
<p>添加这些代码片段以在站点上的任何位置添加可选小部件。请注意，您必须将这些添加到特定页面的 HTML 中；它们无法添加到您的functions.php 文件中。 #### SEO / 所有评论小部件</p>
<p>`<div id='klaviyo-reviews-all' data-id='all'></div>`</p>
<h4>特色评论轮播小部件</h4>
<p>`<div id='klaviyo-featured-reviews-carousel'></div>`</p>
<h2>结果</h2>
<p>完成这些步骤后，Klaviyo Reviews 小部件将出现在您的在线商店中。</p>
