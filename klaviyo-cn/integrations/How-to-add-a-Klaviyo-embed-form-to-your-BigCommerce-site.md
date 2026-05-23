---
id: "360022594552"
title: "如何将 Klaviyo 嵌入表单添加到您的 BigCommerce 网站"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360022594552-How-to-add-a-Klaviyo-embed-form-to-your-BigCommerce-site"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:43Z"
language: "zh"
---
## 你将会学到

了解如何将 Klaviyo 嵌入表单添加到您的 BigCommerce 网站，这需要在 Klaviyo 中创建表单，然后将其嵌入代码粘贴到您希望其显示的网站文件中（例如页脚）。本指南介绍如何使用 Klaviyo 嵌入表单替换 BigCommerce 默认注册表单。 ## 开始之前

在 Klaviyo 中创建嵌入表单之前，您必须首先与 BigCommerce 集成，然后启用注册表单功能（也称为“现场跟踪”）。如果您在[与 BigCommerce 集成](https://help.klaviyo.com/hc/en-us/articles/115005082547-Integrate-with-BigCommerce-Stencil-Themes#step-3---install-klaviyo-js-and-viewed-product-tracking5) 时选中设置 **自动添加 Klaviyo 现场 JavaScript**，则一切就绪。如果没有：

1. 在 Klaviyo 中，选择****集成****选项卡。 ![在 Klaviyo 中选择的示例帐户名称，显示从导航菜单中选择的“集成”选项卡。](https://klaviyo.zendesk.com/hc/article_attachments/32015108658459)
2. 单击****BigCommerce****。 3. 检查设置****自动添加Klaviyo现场javascript****。 4. 单击****保存****。本文中的示例使用 BigCommerce 的默认 Cornerstone 主题。请记住，您的主题以及某些文件的名称或代码片段的位置可能会有所不同。 ## 将表单的嵌入代码添加到您的网站

首先，[在 Klaviyo 中创建并发布嵌入表单](https://help.klaviyo.com/hc/en-us/articles/360006897412)。本部分将介绍将表单的嵌入代码粘贴到 BigCommerce 网站上的后续步骤，以便其正确显示和同步数据。 1. 如果您尚未复制嵌入表单的嵌入代码，请复制嵌入代码。您可以通过在编辑器中打开表单并单击****定位和行为****部分来访问表单的嵌入代码。 ![突出显示示例表单的嵌入代码，以便从表单编辑器内“定位和行为”选项卡的“显示”菜单复制。](https://klaviyo.zendesk.com/hc/article_attachments/32015108670619)
2. 导航到您的网站并找到默认的 BigCommerce 注册表单。如果您使用的是 Cornerstone 主题，它位于网站的页脚中。 ![在网站页脚中显示示例产品和电子邮件订阅表格的 BigCommerce 店面](https://klaviyo.zendesk.com/hc/article_attachments/28723630357531)
   - 如果您在网站上没有看到默认表单：
     - 打开您的 BigCommerce 仪表板。 - 导航至****营销 > 电子邮件营销****
     - 选中标有**允许订阅新闻通讯**的框。这使您能够收集网站访问者的电子邮件同意，并在您的 BigCommerce 网站上添加默认电子邮件注册框。如果此框已被选中，但您仍然没有看到默认表单，那么您的主题可能不包含默认表单。 3. 打开 BigCommerce 仪表板，然后导航至****店面 > 主题****。 4. 从**当前主题**部分，单击****高级****下拉列表，然后选择****编辑主题文件****。 ![BigCommerce 仪表板显示当前主题，高级设置下拉列表打开，编辑主题文件以蓝色突出显示。](https://klaviyo.zendesk.com/hc/article_attachments/28723625055131)
   - 如果您使用默认主题，您将无法选择此选项。相反：
     - 单击****制作副本****，为其命名，然后选择****保存副本****。 - 将其添加到 **主题** 部分后，选择 3 个点，然后选择 ****编辑主题文件****。请注意，您所做的任何编辑都只会应用于您正在编辑的主题，并且您需要将该主题应用到您的网站才能看到所反映的更改。 5. 在左侧边栏中，打开与站点上出现的默认表单相对应的文件。如果默认表单位于页脚中（如示例所示），请导航至 ****templates > Components > common****，然后单击 ****footer.html**** 文件。 6. 使用查找快捷方式（Mac 上的 Command+F 或 Windows 上的 Control+F）在页脚文件中搜索单词“newsletter”。 ![查找术语的快捷命令](https://klaviyo.zendesk.com/hc/article_attachments/32015094392091)
7. 在其下面的代码中，找到对表单的引用。在示例中，表单在不同的文件路径中引用：{{> Components/common/subscription-form}}。 ![示例网站页脚文件中引用的新闻通讯表单的文件路径。](https://klaviyo.zendesk.com/hc/article_attachments/32015094399003)
8. 在左侧边栏中，按照代码中引用的文件路径进行操作（在本例中，选择****组件 > 通用 > 订阅表单****）。您将从这里看到默认表单的实际组件。 - 因为默认表单的标题和语言与我们网站的其余样式相匹配，所以我们只会替换实际的表单输入。在源代码中，您可以看到默认表单的输入包含在 <form> 元素中。 9. 突出显示开始和结束 <form> 标记之间的所有内容，然后粘贴从 Klaviyo 复制的嵌入代码以替换突出显示的文本。 ![示例网站的订阅表单文件，显示表单标签中突出显示的默认表单输入。](https://klaviyo.zendesk.com/hc/article_attachments/32015108693787)
10. 单击****保存并应用文件****，将这些更改应用到您的网站。 - 如果按钮只显示****保存文件****，那么您刚刚编辑的文件还不是您的**当前主题**。您需要单击****保存文件****，然后向上滚动并选择右上角的****编辑主题文件>保存>用作活动主题****，以将主题应用到您的网站。在 BigCommerce 中粘贴嵌入代码、保存并应用更改后，导航回您的网站并刷新页面。您的 Klaviyo 嵌入表单将显示在您的网站上，并开始将新订阅者添加到链接到该表单的 Klaviyo 列表中。如果您没有看到表单，请参阅[嵌入表单疑难解答](https://help.klaviyo.com/hc/en-us/articles/360006897412#h_01JFAQY2NHMG3PPV523K4ESXEV)。 ## 后续步骤

接下来，创建一个[欢迎系列流程](https://help.klaviyo.com/hc/en-us/articles/115002775172)，以立即对您的新订阅者产生影响。 ## 其他资源

- [如何创建电子邮件欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172-How-to-Create-an-Email-Welcome-Series)
- [如何禁用BigCommerce发送的通知电子邮件](https://help.klaviyo.com/hc/en-us/articles/4403594764315-How-to-Disable-Notification-Emails-Sent-by-BigCommerce)