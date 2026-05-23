---
id: "32004602396443"
title: "如何将嵌入表单添加到您的 Shopify 网站"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/32004602396443-How-to-add-an-embed-form-to-your-Shopify-site"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:38Z"
language: "zh"
---
## 你将会学到

了解如何将 Klaviyo 嵌入表单添加到您的 Shopify 网站。这涉及在 Klaviyo 中创建一个表单，然后将其嵌入代码粘贴到您希望其显示的网站文件中，例如页脚中。已经在使用 Shopify 注册表单？如果您[在集成时选择将 Shopify 订阅者同步到 Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005080667)，则任何新订阅者都将自动同步。 ## 开始之前

在 Klaviyo 中创建嵌入表单之前，您必须[与 Shopify 集成](https://klaviyo.zendesk.com/hc/en-us/articles/115005080407) 并启用注册表单功能（也称为“现场跟踪”）。对于 Shopify 商店，必须启用应用程序嵌入才能使注册表单正确显示和同步数据。要验证应用程序嵌入是否已启用：

1. 导航到 [Shopify 集成设置页面](https://www.klaviyo.com/integration/shopify)。 2. 滚动到**现场跟踪**部分。 - 如果您看到绿色横幅，显示 **Klaviyo 应用嵌入已在您的 Shopify 商店中启用**，则表示您已准备就绪。继续阅读本文的下一部分，将嵌入表单添加到您的网站。 ![示例帐户的 Shopify 集成设置页面的现场跟踪部分显示绿色横幅，表明应用程序嵌入已启用。](https://klaviyo.zendesk.com/hc/article_attachments/32005661682331)
   - 如果黄色横幅显示 **Klaviyo 应用程序嵌入已关闭。打开后，在 Shopify 主题编辑器中选择“保存”以应用更改。**
     - 在继续阅读本文之前，请参阅有关 [为 Shopify 启用 Klaviyo 应用程序嵌入](https://help.klaviyo.com/hc/en-us/articles/4425956184731) 的指南。 ![示例帐户的 Shopify 集成设置页面的现场跟踪部分显示黄色横幅，表明应用程序嵌入已关闭。](https://klaviyo.zendesk.com/hc/article_attachments/32005632820251)

本文中的示例使用 Shopify 2.0 主题。 [您的主题可能有所不同](https://help.shopify.com/en/manual/online-store/themes/managing-themes/versions)，这可能会影响某些文件的名称或代码片段的位置。 ## 将嵌入表单添加到您的网站

想要在 Shopify 感谢页面或订单状态页面上嵌入表单？ Shopify 本身不再支持此功能，但您可以使用 Klaviyo 的 [短信应用阻止功能](https://help.klaviyo.com/hc/en-us/articles/35067557759771) 在 Shopify 结账（仅限 Shopify Plus）、谢谢或订单状态页面上收集短信同意。 1. 创建您的嵌入表单。 2. 在表单编辑器中，选择****定位和行为> 显示****。 3. 在 **嵌入** **代码** 下，从代码中复制表单 ID，如下所示：
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36496429064347)
4. 发布您的表单。 5. 导航到您的 Shopify 仪表板。 6. 选择****在线商店 > 主题****。 7. 单击****自定义****。 ![示例 Shopify 仪表板上的主题菜单显示突出显示的“自定义”按钮以供单击。](https://klaviyo.zendesk.com/hc/article_attachments/32005632829979)
8. 从顶部菜单栏中，选择您要添加表单的页面模板（例如，您的主页或密码页面）。 ![Shopify 商店管理员显示页面模板下拉列表在顶部打开，并选择主页在主题编辑器中进行编辑。](https://klaviyo.zendesk.com/hc/article_attachments/32005661703195)
9. 在左侧菜单中的 **应用程序** 下，选择 ****添加部分 > 应用程序 > Klaviyo 嵌入式表单****。 - 如果您只希望此表单出现在该特定页面上，请在 **模板** 部分中执行此操作。 ![Shopify 商店的希望页面在主题编辑器中打开，并在模板部分显示 Klaviyo 嵌入式表单应用程序。](https://klaviyo.zendesk.com/hc/article_attachments/32005632834715)
   - 如果您希望表单保留在网站的每个页面上，请在 **页脚** 部分执行此操作。请注意，在网站页脚中嵌入表单也是 Klaviyo 列表增长的最佳实践。 ![Shopify 商店的希望页面在主题编辑器中打开，并在页脚部分显示 Klaviyo 嵌入式表单应用程序](https://klaviyo.zendesk.com/hc/article_attachments/32005632838939)
10. 单击左侧菜单中新创建的****Klaviyo Embedded Form**** 部分。 11. 将从 Klaviyo 复制的表单 ID 粘贴到指定的文本框中。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36496429068443)
12. 单击****保存**** 将嵌入表单添加到页面模板中。 请注意，只有在保存后，嵌入表单才会出现在预览中。 13. 可选：保存后，您可以通过在菜单中单击并拖动 Klaviyo Embedded Form 应用程序来重新排列它。在 Shopify 中粘贴嵌入代码并保存更改后，导航回您的网站并刷新页面。网站访问者将看到您的表单，并可以选择通过填写该表单来加入您的列表。如果您没有看到表单，请参阅[嵌入表单疑难解答](https://help.klaviyo.com/hc/en-us/articles/360006897412#h_01JFAQY2NHMG3PPV523K4ESXEV)。 ## 后续步骤

接下来，创建一个[欢迎系列流程](https://help.klaviyo.com/hc/en-us/articles/115002775172)，以立即对您的新订阅者产生影响。 ## 其他资源

- [如何更改表单提交到的列表](https://help.klaviyo.com/hc/en-us/articles/360002049952#01H8PDB7M745EXVSGVWXR6Q5QA)
- [Shopify 入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005080407)
- [注册表单入门](https://klaviyo.zendesk.com/hc/en-us/articles/360026474752)