---
id: "43956692620059"
title: "如何将收藏夹链接（图标、文本或按钮）添加到您的 Shopify 标头"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/43956692620059-How-to-add-a-Favorites-link-icon-text-or-button-to-your-Shopify-header"
section: "Build and use Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: "zh"
---
在网站的导航栏（“标题”）中添加特定的“收藏夹”图标可以减少客户在客户中心找到他们的收藏夹的麻烦，从而提高参与度。通过为购物者提供一个专门的启动点来存放他们保存的商品，您可以鼓励他们建立更大的购物篮并更频繁地返回您的商店。您可以将其实现为****图标****（例如心形）、简单的****文本链接****（例如“收藏夹”）或****按钮****。本指南介绍如何使用 Shopify 的 Liquid 代码将必要的代码插入到网站的标头中。 ![](https://klaviyo.zendesk.com/hc/article_attachments/43956692602011)

本指南介绍如何将心形图标上传到您的主题资产，以及如何使用 Shopify 的 Liquid 代码将代码链接插入到您网站的标题中。 > ****注意**** 此过程涉及编辑您的 Shopify 主题代码。如果您不擅长编写代码或您的团队中没有开发人员，我们建议您联系 [Klaviyo 合作伙伴](https://www.google.com/search?q=https://connect.klaviyo.com/directory) 寻求帮助。 Klaviyo 支持无法对自定义代码实现进行故障排除。 ## 开始之前

我们强烈建议在进行更改之前复制您的实时主题。这使您可以在安全的环境中测试新图标，而不会影响您的实时商店。 1. 在 Shopify 中，转到****在线商店 > 主题****。 2. 单击实时主题旁边的****三点菜单 (...)****。 3. 选择****复制****。 ## 第 1 步：准备您的资源（如果您想使用图标）

首先，上传将用作按钮的图标文件。使用 SVG 文件是最好的，因为它可以缩放到任何屏幕尺寸而不会损失质量，并且可以继承主题的颜色。 1. 您需要找到您想要使用的图标。这可以是任何图标，但我们建议使用 SVG 以避免像素化。您可以在此处下载标准（MIT 许可）版本：[****Heroicons heart.svg****](https://raw.githubusercontent.com/tailwindlabs/heroicons/refs/heads/master/src/24/outline/heart.svg)。 2. 在您的 Shopify 后台中，导航至****在线商店 > 主题****。 3. 找到您的主题并单击****三点菜单 (...) > 编辑代码****。 4. 在左侧边栏中，向下滚动到****Assets**** 文件夹，然后单击****添加新资产****。 5. 上传您的图标文件。 ## 步骤 2：插入标题（顶部导航栏）链接

接下来，添加显示图标并将其链接到客户中心的代码片段。 1. 在主题代码编辑器中，找到控制标头的文件。 - ****Online Store 2.0 主题（例如 Dawn）：**** 搜索 `sections/header.liquid`。 - ****复古主题：**** 搜索“snippets/header-icons.liquid”或“header-bar.liquid”。 2. ****找到插入点：**** 按“Ctrl+F”（或 Mac 上的“Cmd+F”）并搜索单词“cart”或“account”。您希望将新代码粘贴到保存这些现有图标的同一容器（通常是“<div>”或“<ul>”）中。 3. 将****一个****代码选项粘贴到您希望链接出现的位置（例如，就在购物车图标之前）。 ###

### 选项 A：图标链接

如果您完成了步骤 1 并且想要显示心形图标，请使用此代码（假设在我们的示例中该图标名为 icon-heart.svg）：

````
<a href="#k-hub/收藏夹"
   id="收藏夹图标气泡"
   aria-label="打开收藏夹"
   标题=“收藏夹”
   样式=“显示：flex；对齐项目：中心；对齐内容：中心；高度：4.4rem；宽度：4.4rem；”>
  <span style="height:20px;width:20px">
    {{ 'icon-heart.svg' | 'icon-heart.svg' |内联资产内容 }}
  </span>
</a>
````

### 选项 B：文本链接或按钮

如果您喜欢文本链接或按钮，请使用此代码。您无需为此上传任何资源。 ****对于简单的文本链接：****

````
<a href="#k-hub/favorites" class="header__menu-item header__menu-item--list" style="text-decoration: none;">
  收藏夹
</a>
````

****对于按钮：****

````
<a href="#k-hub/favorites" class="button 按钮--primary">
  收藏夹
</a>
````

1. 单击****保存****。 > ****提示：匹配您的主题风格**** 如果您的主题对标题图标使用特定的 CSS 类（例如，`header__icon` 或 `icon-link`），您可以将上面代码中的内联 `style=` 属性替换为该类（例如，`class="header__icon"`）。这可确保间距和悬停效果与其他按钮完美匹配。 ## 结果

保存后，在****新的隐身/私人窗口****中打开您的商店，以绕过任何浏览器缓存。您应该在导航栏中看到心形图标。 单击此图标现在将打开客户中心内的****收藏夹****选项卡。 ## 故障排除

如果图标未出现或看起来不正确：

- ****图标是损坏的图像：**** 确保您已将文件上传到 ****Assets**** 文件夹并将其准确命名为“icon-heart.svg”。文件名区分大小写。 - ****图标未对齐：**** 您可能需要调整代码片段的“style”属性中的“height”和“width”值，以匹配主题的导航栏高度。 - ****更改未显示：**** Shopify 主题积极缓存。尝试在隐身窗口中预览主题，或者如果正在处理草稿主题，则将“?preview_theme_id=”附加到您的 URL。