---
id: "26922347702939"
title: "如何安装 WooCommerce 的 Klaviyo 评论"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/26922347702939-How-to-install-Klaviyo-Reviews-for-WooCommerce"
section: "Getting started with reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-05-06T16:29:16Z"
language: "zh"
---
## 你将会学到

了解如何在 WooCommerce 商店上安装 Klaviyo 评论并添加评论小部件。要了解开始所需的所有步骤，请前往 [Klaviyo Reviews 入门]。(https://klaviyo.zendesk.com/hc/en-us/articles/15937542819355)

## 开始之前

有 4 种安装 Klaviyo Reviews for WooCommerce 的方法。适合您的方法取决于您的技术知识水平和 WordPress 设置。使用下面的流程图选择最适合您的安装方法。 ![流程图表明不习惯使用代码的用户应该添加插件并使用可视化主题编辑器；那些无法访问主题文件的人应该使用插件和代码片段；那些使用第三方或自定义主题的人应该使用短代码，那些有权访问其网站的functions.php 文件的人应该直接修改他们的主题文件。这些选项从技术难度最小的开始，到技术难度最大的选项结束。](https://klaviyo.zendesk.com/hc/article_attachments/28722599957275)

选择安装方法时，请考虑以下因素：

- 仅支持两种安装方法向收藏页面添加星级：带有可视化编辑器的插件和短代码。 - 考虑您在 WordPress 中的编辑器访问级别。并非所有用户都可以选择直接编辑网站主题文件。如果您无法访问 [functions.php 文件](https://developer.wordpress.org/themes/core-concepts/custom-functionity/) 或类似文件，请使用其他方法之一。 - 其中一些方法需要向您的 WordPress 站点添加另一个插件。下面的说明引用了代码片段插件，但 Klaviyo 不认可任何特定插件，也无法协助解决与插件相关的问题。选择适合您的安装步骤后，请继续执行相关说明。了解如何通过以下方式安装 Klaviyo Reviews for WooCommerce：
- [安装插件并使用可视化主题编辑器](#h_01J1FFYXRRSR45ACAKVXCNQB91)
- [安装插件，不使用可视化主题编辑器](#h_01J1FFZZ2EHN1PKBZXEHA4MSEK)
- [添加短代码](#h_01J1FG22Y6SERD6MYYC0T28AD9)
- [修改主题文件](#h_01J1FG38N26A6DCNCRG02YR0W9)

## 可用的评论小部件

安装 Klaviyo Reviews 后，您的商店将显示评论小部件，其中包含评级和评论详细信息。 - ****星级小部件****
  显示特定产品的当前星级，并且通常添加在产品页面或产品系列页面上的产品名称下方。 ![星级](https://klaviyo.zendesk.com/hc/article_attachments/28722611980187)
- ****产品评论小部件****
  显示一个图表，详细列出产品收到的所有评分、提交评论的用户图像以及产品收到的最常见反馈。下面是所有已发布评论和客户问题的列表，以及搜索栏、评论过滤器、****撰写评论****按钮和****提出问题****按钮。该小部件通常添加在产品页面底部附近。 ![摘要小部件](https://klaviyo.zendesk.com/hc/article_attachments/28722599979035)
  ![评论列表](https://klaviyo.zendesk.com/hc/article_attachments/28722611982363)
- ****特色评论轮播小部件****
  显示您所有产品的突出评论。您可以在主页、独立评论页面或网站上的任何其他位置上展示此内容。您还可以选择此小部件中的评论。如果有的话，客户提交的图像会附在每次评论中；如果未提交图像，则会使用您的产品图像。 ![评论轮播](https://klaviyo.zendesk.com/hc/article_attachments/28722599980571)
- ****SEO / 所有评论小部件****
  在一个页面上显示您对所有产品的所有评论。使用此小部件可以改进您的搜索引擎优化，并为潜在客户提供一个单一的位置来查看当前客户的喜好。此小部件通常添加到您网站上的独立**评论**页面。 ![所有评论小部件](https://klaviyo.zendesk.com/hc/article_attachments/28722599987355)

## 安装插件并使用可视化主题编辑器

为了使用可视化主题编辑器将 Klaviyo Reviews 小部件添加到您的网站，您必须首先添加一段代码以在主题中加载这些拖放块。 您可以使用 [代码片段](https://wordpress.org/plugins/code-snippets/) 等工具添加这些块的源代码，然后使用可视化主题编辑器将 Klaviyo Reviews 小部件拖放到您的主题中。 ### 添加评论小部件源代码

这些说明假设您已经安装了 [代码片段](https://wordpress.org/plugins/code-snippets/) 插件，但您可以使用其他插件。 1. 从 Wordpress 侧边栏选择****代码段 > 添加新****。 ![Wordpress 侧边栏中的“片段”选项](https://klaviyo.zendesk.com/hc/article_attachments/28722611964443)
2. 在 **在此处输入标题** 字段中，为片段命名清晰的名称，例如“Klaviyo Reviews Widgets Code”。 3. 在 **代码** 部分的 **函数 (PHP)** 选项卡中，添加下面的代码片段。 4. 单击****保存更改并激活****。 #### 评论小部件源代码

````
函数register_klaviyo_reviews_blocks() {
    // 注册块
    register_block_type( 'klaviyo/产品评论', array(
        'editor_script' => 'klaviyo-block-editor-script',
        'render_callback' => 'render_klaviyo_product_reviews',
    ））；
    register_block_type( 'klaviyo/产品星级评级', array(
        'editor_script' => 'klaviyo-block-editor-script',
        'render_callback' => 'render_klaviyo_star_ ratings',
    ））；
    register_block_type( 'klaviyo/特色评论', array(
        'editor_script' => 'klaviyo-block-editor-script',
        'render_callback' => 'render_klaviyo_featured_reviews',
    ））；
    register_block_type( 'klaviyo/all-reviews', array(
        'editor_script' => 'klaviyo-block-editor-script',
        'render_callback' => 'render_klaviyo_all_reviews',
    ））；
}
add_action( 'init', 'register_klaviyo_reviews_blocks' );
函数 enqueue_klaviyo_block_editor_assets() {
    // 注册并入队徽标图像
    wp_注册脚本（
        'klaviyo-块编辑器脚本',
        假的，
        数组( 'wp-blocks', 'wp-element', 'wp-editor' ),
        假的，
        真实
    ）；
    $logo_url = plugins_url( 'img/klaviyo-logo.png', 'klaviyo/klaviyo.php' );
    wp_add_inline_script( 'klaviyo-block-editor-script', '
        （函数（块，元素）{
            var el = element.createElement;
            // 添加自定义类别
            block.updateCategory( "小部件", {
                弹头：“klaviyo”，
                标题：“克拉维约”，
                图标: el("img", { src: "' . $logo_url . '", 样式: { 宽度: "20px", 高度: "20px" } })
            } );
            block.registerBlockType(“klaviyo/产品评论”, {
                标题：“Klaviyo 产品评论”，
                图标：“管理员评论”，
                类别：“克拉维约”，
                编辑：函数（）{
                    返回 el(
                        “div”，
                        { className: "klaviyo-产品评论" },
                        “此处将显示 Klaviyo 产品评论”
                    ）；
                },
                保存：函数（）{
                    返回空值；
                },
            });
            block.registerBlockType(“klaviyo/产品星级评级”, {
                title: "Klaviyo 星级评定",
                图标：“充满星星”，
                类别：“克拉维约”，
                编辑：函数（）{
                    返回 el(
                        “div”，
                        { className: "klaviyo-产品星级-评级" },
                        “此处将显示 Klaviyo 产品星级”
                    ）；
                },
                保存：函数（）{
                    返回空值；
                },
            });
            block.registerBlockType(“klaviyo/特色评论”, {
                标题：“Klaviyo 精选评论”，
                图标：“管理帖子”，
                类别：“克拉维约”，
                编辑：函数（）{
                    返回 el(
                        “div”，
                        { className: "klaviyo-featured-reviews" },
                        “此处将显示 Klaviyo 精选评论”
                    ）；
                },
                保存：函数（）{
                    返回空值；
                },
            });
            block.registerBlockType(“klaviyo/all-reviews”, {
                标题：“Klaviyo 所有评论”，
                图标：“管理页面”，
                类别：“克拉维约”，
                编辑：函数（）{
                    返回 el(
                        “div”，
                        { className: "klaviyo-all-reviews" },
                        “Klaviyo 所有评论都将显示在这里”
                    ）；
                },
                保存：函数（）{
                    返回空值；
                },
            });
        } )(
            窗口.wp.块，
            窗口.wp.元素
        ）；
    '）；
}
add_action( 'enqueue_block_editor_assets', 'enqueue_klaviyo_block_editor_assets' );
// 渲染块的回调函数
函数 render_klaviyo_product_reviews( $attributes, $content ) {
    全球$产品；
    if ( is_product() && isset($product) ) {
        返回“<div id='klaviyo-reviews-all' data-id='” 。 esc_attr($product->get_id()) 。 “'></div>”；
    }
}
函数 render_klaviyo_star_ ratings( $attributes, $content ) {
    全球$产品；
    如果（isset（$产品））{
        返回“<div class='klaviyo-star- rating-widget' data-id='” 。 esc_attr($product->get_id()) 。 “'></div>”；
    }
}
函数 render_klaviyo_featured_reviews( $attributes, $content ) {
    返回“<div id='klaviyo-featured-reviews-carousel'></div>”；
}
函数 render_klaviyo_all_reviews( $attributes, $content ) {
    返回“<div id='fulfilled-reviews-all' data-id='all'></div>”；
}
````

### 添加 Klaviyo 评论插件

1. 导航至****外观 > 编辑器****。 2. 选择****模板****。 3. 选择您的**单一产品**模板。请注意，它的名称可能略有不同。 4. 单击****+**** 打开阻止菜单。 ![Wordpress 可视化编辑器中的 + 选项](https://klaviyo.zendesk.com/hc/article_attachments/28722599964955)
5. 导航至 **Blocks** 菜单的 **Klaviyo** 部分。 ![Wordpress 可视化编辑器的 Klaviyo 部分阻止菜单](https://klaviyo.zendesk.com/hc/article_attachments/28722599969307)
6. 将 Klaviyo Reviews 小部件拖放到您的主题中。 7. 单击****保存****。 ### 添加收藏星级小部件

1. 导航至****外观 > 编辑器****。 2. 选择****模板****。 3. 选择包含产品集合的页面。 4. 单击****+**** 打开阻止菜单。 ![Wordpress 可视化编辑器中的 + 选项](https://klaviyo.zendesk.com/hc/article_attachments/28722599964955)
5. 导航至 **Blocks** 菜单的 **Klaviyo** 部分。 6. 将****星级****小部件拖到集合中的任何产品上。 7. 单击****保存****。 如果需要，请使用下面的代码片段将星级小部件居中对齐。请注意，您必须将 YOUR\_PAGE\_ID 占位符替换为集合页面的页面 ID。了解如何[查找页面 ID](https://wordpress.com/support/pages/#find-the-page-id)。 ````
.page-id-YOUR_PAGE_ID

.klaviyo-星级评级小部件{
    显示：柔性；
    调整内容：居中；
    对齐项目：居中；
    文本对齐：居中；
    保证金：0 自动；
}
````

## 安装插件并使用代码添加小部件

使用此方法时，小部件会根据 WooCommerce [视觉挂钩](https://wordpress.org/plugins/woo-visual-hook-guide/) 的位置添加到您的网站。因此，如果您的产品页面上没有 WooCommerce 小部件，则必须使用备用安装选项。此过程需要添加第三方代码片段工具，因此您可以将代码添加到您的网站，而无需直接编辑主题文件。您可以使用 [代码片段](https://wordpress.org/plugins/code-snippets/) 等工具来添加这些小部件的代码。 ### 添加评论小部件源代码

这些说明假设您已经安装了 [代码片段](https://wordpress.org/plugins/code-snippets/) 插件，但您可以使用其他插件。 1. 从 Wordpress 侧边栏选择****代码段 > 添加新****。 ![Wordpress 侧边栏中的片段菜单](https://klaviyo.zendesk.com/hc/article_attachments/28722599971739)
2. 在 **在此处输入标题** 字段中，为片段命名清晰的名称，例如“Klaviyo Reviews Widgets Code”。 3. 在 **代码** 部分的 **函数 (PHP)** 选项卡中，添加以下代码片段。 4. 单击****保存更改并激活****。您必须为计划使用的每个小部件安装一个代码片段。以下部分概述了每个小部件的代码。 ### 产品评论小部件代码片段

要调整小部件在网站上的位置，请在“add_action”函数中编辑 (“woocommerce_after_single_product_summary”) 的位置和优先级 (“15”)。 ````
函数 klaviyo_add_product_reviews_widget() {
    全球$产品；
    if (is_product() && isset($product)) {
        $product_id = $product->get_id();
        echo "<div id='klaviyo-reviews-all' data-id='{$product_id}'></div>";
    }
}
add_action('woocommerce_after_single_product_summary', 'klaviyo_add_product_reviews_widget', 15);
````

### 星级评分小部件代码片段

要调整小部件在网站上的位置，请在“add_action”函数中编辑 (“woocommerce_single_product_summary”) 的位置和优先级 (“6”)。 ````
函数 klaviyo_add_product_star_ ratings_widget() {
    全球$产品；
    if (is_product() && isset($product)) {
        $product_id = $product->get_id();
        echo "<div class='klaviyo-star- rating-widget' data-id='{$product_id}'></div>";
    }
}
add_action('woocommerce_single_product_summary', 'klaviyo_add_product_star_ ratings_widget', 6);
````

### 其他可选代码片段

使用这些代码片段在您网站的任何位置添加可选小部件。请注意，您必须将这些添加到特定页面的 HTML 中；它们无法添加到您的functions.php 文件中。 #### SEO 小工具

`<div id='klaviyo-reviews-all' data-id='all'></div>`

#### 特色评论轮播小部件

`<div id='klaviyo-featured-reviews-carousel'></div>`

## 添加短代码

此过程涉及首先在主题文件中注册短代码，然后将短代码插入网站上的任何位置。要完成此操作，您必须首先添加第三方代码片段工具，以便您可以将代码添加到您的网站，而无需直接编辑主题文件。您可以使用 [代码片段](https://wordpress.org/plugins/code-snippets/) 等工具来添加这些小部件的代码。 ### 注册短代码并添加小部件

这些说明假设您已经安装了 [代码片段](https://wordpress.org/plugins/code-snippets/) 插件，但您可以使用其他插件。 1. 从 Wordpress 侧边栏选择****代码段 > 添加新****。 ![Wordpress 侧边栏中的片段菜单](https://klaviyo.zendesk.com/hc/article_attachments/28722611974171)
2. 在 **在此处输入标题** 字段中，为片段命名清晰的名称，例如“Klaviyo Reviews Widgets Code”。 3. 在 **代码** 部分的 **函数 (PHP)** 选项卡中，添加以下代码片段。 4. 单击****保存更改并激活****。 5. 将每个小部件的短代码添加到您希望显示小部件的页面。 ### 代码片段和短代码

### 产品评论小部件

代码片段（添加到“函数 (PHP)”选项卡）：

````
函数 klaviyo_add_product_reviews_widget() {
    全球$产品；
	如果（isset（$产品））{
        $product_id = $product->get_id();
        $tag = "<div id='klaviyo-reviews-all' data-id='{$product_id}'></div>";
		返回$标签；
    }
}
add_shortcode('klaviyo-reviews-all', 'klaviyo_add_product_reviews_widget');
````

****短代码：**** [klaviyo-reviews-all]

### 星级小部件

代码片段（添加到“函数 (PHP)”选项卡）：

````
函数 klaviyo_add_product_star_ ratings_widget() {
    全球$产品；
    如果（isset（$产品））{
        $product_id = $product->get_id();
        $tag = "<div class='klaviyo-star- rating-widget' data-id='{$product_id}'></div>";
		返回$标签；
    }
}
add_shortcode('klaviyo_star_ rating', 'klaviyo_add_product_star_ ratings_widget');
````

****短代码：**** [klaviyo\_star\_ rating]

将此短代码添加到您的产品页面以显示单个产品的星级，或添加到任何产品系列页面以显示产品系列中所有商品的星级。 ### SEO / 所有评论和特色轮播小部件

代码片段（添加到“函数 (PHP)”选项卡）：

````
函数 klaviyo_add_featured_reviews_widget() {
    返回“<div id='klaviyo-featured-reviews-carousel'></div>”；
}
函数 klaviyo_add_all_reviews_widget() {
    返回“<div id='fulfilled-reviews-all' data-id='all'></div>”；
}
````

****短代码：**** [klaviyo-featured-reviews-carousel]

****短代码：**** [fulfilled-reviews-all]

## 直接修改你的主题文件

如果您有权访问 WordPress 实例的functions.php 文件，请使用下面的代码片段添加评论小部件。这些说明适用于具有 Wordpress PHP 经验的开发人员。如果您不熟悉 Wordpress PHP，请使用替代方法。 ### 产品评论小部件代码片段

````
// 创建一个函数来呈现具有正确产品 ID 的动态 div
函数 klaviyo_add_product_reviews_widget() {
    全球$产品；
    if (is_product() && isset($product)) {
        $product_id = $product->get_id();
        echo "<div id='klaviyo-reviews-all' data-id='{$product_id}'></div>";
    }
}
// 将小部件放置在单品摘要之后
add_action('woocommerce_after_single_product_summary', 'klaviyo_add_product_reviews_widget', 15);
````

### 星级评分小部件代码片段

````
// 创建一个函数来呈现具有正确产品 ID 的动态 div
函数 klaviyo_add_product_star_ ratings_widget() {
    全球$产品；
    if (is_product() && isset($product)) {
        $product_id = $product->get_id();
        echo "<div class='klaviyo-star- rating-widget' data-id='{$product_id}'></div>";
    }
}
// 将小部件放置在单品摘要之后
add_action('woocommerce_single_product_summary', 'klaviyo_add_product_star_ ratings_widget', 6);
````

### 其他可选代码片段

添加这些代码片段以在站点上的任何位置添加可选小部件。请注意，您必须将这些添加到特定页面的 HTML 中；它们无法添加到您的functions.php 文件中。 #### SEO / 所有评论小部件

`<div id='klaviyo-reviews-all' data-id='all'></div>`

#### 特色评论轮播小部件

`<div id='klaviyo-featured-reviews-carousel'></div>`

## 结果

完成这些步骤后，Klaviyo Reviews 小部件将出现在您的在线商店中。