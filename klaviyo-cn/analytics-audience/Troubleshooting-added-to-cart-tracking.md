---
id: "6985692431259"
title: "添加到购物车跟踪的故障排除"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/6985692431259-Troubleshooting-added-to-cart-tracking"
section: "Metrics troubleshooting"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: "zh"
---
## 开始之前

对于某些电子商务平台，会自动跟踪 **添加到购物车** 事件。对于其他电子商务平台，必须手动将代码片段添加到您的网站。在查阅本指南之前，请确保您：

- 如果未通过集成自动添加，则启用 **添加到购物车** 跟踪。 - 启用 Klaviyo 的“Active on Site”JavaScript（称为 Klaviyo.js），以便 **添加到购物车** 跟踪正常工作。请参阅下面的[“现场活动”部分](#h_01G6W496F0XVGZDAWAJ2RW5KEG) 了解具体操作方法。如果您使用的是 BigCommerce，请确保启用 **查看的产品** 跟踪，这是确保 **添加到购物车** 跟踪正常运行所必需的。下面链接的设置指南中给出了有关启用**查看的产品**跟踪的指南。如果您遇到 **已查看商品** 跟踪问题，请参阅我们的[已查看商品跟踪问题排查]指南(https://help.klaviyo.com/hc/en-us/articles/4416172774939-Troubleshooting-Viewed-Product-Tracking)。以下电子商务集成支持 **添加到购物车** 跟踪，其工作原理如下：
- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)
  当您检查 **跟踪行为事件** 设置时，通过 [Shopify Server Pixel](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01J6F7TREZAJM7M3R3DFVZSDGT) 启用
- [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547)
  需要[手动安装的代码片段](https://help.klaviyo.com/hc/en-us/articles/360024310292)
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115005254348)
  由 Klaviyo 自动添加
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808)
  由 Klaviyo 自动添加
- [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360054551492-How-to-Integrate-with-PrestaShop)
  由 Klaviyo 自动添加
- [Salesforce 商务云](https://help.klaviyo.com/hc/en-us/articles/360033744951)
  由 Klaviyo 自动添加 - 仅跟踪登录用户

如果您使用的电子商务平台没有预构建的 Klaviyo 集成或自定义平台，请了解[如何在我们的开发者网站上启用“查看的产品”和“添加到购物车”跟踪](https://developers.klaviyo.com/en/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration#viewed-product)。 ## 测试添加到购物车跟踪

要测试您的 **添加到购物车** 跟踪设置是否正确，请按照以下步骤操作：

1. 导航至您的网站
2. 在您的主页上，将以下内容添加到 URL 末尾，并将 **example@gmail.com** 替换为您的电子邮件地址：
   **?utm\_email=example@gmail.com**

   ![修改示例中使用的电子邮件地址后，将其添加到您网站 URL 的末尾并在任何浏览器中访问您的网站。](https://klaviyo.zendesk.com/hc/article_attachments/28705664805275)
3. 重新加载页面
4. 导航到您网站上有库存产品的产品页面
5.点击页面上的“添加到购物车”按钮
6. 在 Klaviyo 中搜索您在步骤 2 中使用的电子邮件地址
   ![搜索栏位于 Klaviyo 的右上角，您可以通过电子邮件地址搜索个人资料。](https://klaviyo.zendesk.com/hc/article_attachments/28705664806427)

   您应该看到已为您创建了 Klaviyo 个人资料（如果尚不存在），并且已在您的活动源上跟踪 **添加到购物车** 事件。要查看一段时间内所有**添加到购物车**指标的摘要：
7. 导航到 Klaviyo 中的****分析 > 指标****。 8. 按“已添加到购物车”进行筛选，以查看活动源、活动地图、图表、最佳人员和同期群报告中的跟踪数据。请注意，对于 Shopify，**添加到购物车** 将有一个 Shopify 图标，但对于所有其他集成，它将有一个齿轮图标。 ![“指标”页面顶部有一个搜索栏，您可以在其中按名称搜索不同的指标。](https://klaviyo.zendesk.com/hc/article_attachments/28705637945755)

查看下面的故障排除方案并进行更改后，您应该再次测试跟踪以确保其正常工作。 ## 故障排除场景

查看以下问题以诊断 **已添加到购物车** 问题的原因。请注意，某些步骤是通用的，其他步骤取决于您使用的电子商务平台。 ****您是否启用了 Klaviyo 的 Active on Site 跟踪？****

为了使 **添加到购物车** 跟踪正常工作，您必须首先启用 Klaviyo 的 **Active on Site** 跟踪，该跟踪允许您的客户被 cookied。 **主动网站**跟踪是通过向您的网站添加 JavaScript 代码段（称为“Klaviyo 的现场 JavaScript”或“Klaviyo.js”）来启用的。 Klaviyo 会在集成过程中自动添加 Klaviyo.js，但某些集成需要您检查设置才能启用它。了解您的特定电子商务平台以及如何测试 Klaviyo.js 是否正常工作：

1.****Shopify****
   Klaviyo.js 会通过集成或通过嵌入 Shopify 中的 Klaviyo 应用程序自动添加（如果您启用）。详细了解 [Shopify 的应用嵌入和现场跟踪](https://help.klaviyo.com/hc/en-us/articles/4425956184731)。 2.****WooCommerce****
   当您与 WooCommerce 集成时，Klaviyo.js 会自动添加，您可以通过阅读我们的 [WooCommerce 集成指南](https://help.klaviyo.com/hc/en-us/articles/115005255808-How-to-Integrate-with-WooCommerce) 确保您已完成所有步骤。要测试您的现场 JavaScript，请选择****集成****选项卡，然后单击****管理数据>********设置网络跟踪****。然后，找到可以在框中输入网站 URL 的步骤，并按照说明测试您的跟踪。 3. **大商务****
   确保您已选中[集成设置页面](https://www.klaviyo.com/integration/bigcommerce) 上的选项 **自动添加 Klaviyo 现场 JavaScript**。然后，[按照步骤测试您的现场 JavaScript](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#confirm-web-tracking-installation3)。 4.****Magento 2****
   当您与 Magento 2 集成时，Klaviyo.js 会自动添加，您可以通过阅读我们的[Magento 2 集成指南](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-) 来确保您已完成所有步骤。要测试您的现场 JavaScript，请选择****集成****选项卡，然后单击****管理数据>********设置网络跟踪****。 5. 然后，找到可以在框中输入站点 URL 的步骤，然后按照说明测试您的跟踪。 6. **PrestaShop****
   当您与 PrestaShop 集成时，Klaviyo.js 会自动添加，您可以通过阅读我们的 [PrestaShop 集成指南](https://help.klaviyo.com/hc/en-us/articles/360054551492) 来确保您已完成所有步骤。要测试您的现场 JavaScript，请选择****集成****选项卡，然后单击****管理数据>********设置网络跟踪****。 7. 然后，找到可以在框中输入站点 URL 的步骤，并按照说明测试您的跟踪。 ****对于 Shopify 用户：您是否启用了应用程序嵌入？****

在 Shopify 中启用应用嵌入并选中 **跟踪“查看的产品”事件** 设置后，**查看的产品** 跟踪将自动打开。请阅读我们关于[在 Shopify 中嵌入 Klaviyo 应用程序](https://help.klaviyo.com/hc/en-us/articles/4425956184731#enabling-the-klaviyo-app-embed-in-shopify4) 的文章，了解更多信息。 ****您最近更换过电子商务平台吗？****

如果您最近更换了电子商务平台，则需要将 **查看的产品** 和 **添加到购物车** 跟踪添加到您的新网站。请参阅上面的[开始之前部分](#h_01G6W48MBT2PX8MCX7D6RVT14Z) 中的信息，了解新平台的 **查看的产品** 和 **添加到购物车** 跟踪。 ****您最近是否更新了商店的主题，或对您的电子商务平台进行了任何其他更新？****

如果您最近更新了商店的主题，则可能需要在新主题上重新安装 Klaviyo.js、**查看的产品** 代码段和 **添加到购物车** 代码段（适用于 BigCommerce），具体取决于平台。对电子商务平台进行其他更新也可能会影响之前添加到您网站的代码片段。 要重新安装 BigCommerce 的 **查看的产品** 代码段，请按照 [BigCommerce 集成设置指南](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#confirm-web-tracking-installation3) 中的说明进行操作，对于 **添加到购物车** 代码段，请按照 [为以下内容创建“添加到购物车”事件的指南] BigCommerce](https://help.klaviyo.com/hc/en-us/articles/360024310292-Guide-to-Creating-an-Added-to-Cart-Event-for-BigCommerce)。如果您正在使用 WooCommerce 或 Magento，或者正在使用 Shopify 中嵌入的 Klaviyo 应用，但您已对网站进行了更改，但现在事件未跟踪，您应该[联系 Klaviyo 支持](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support) 来帮助诊断问题。 ****对于 BigCommerce 用户：您的电子商务商店是否连接到多个 Klaviyo 帐户？****

如果您有一个商店连接到多个 Klaviyo 帐户，这可能会导致 **在网站上活动**、**查看的产品** 和 **添加到购物车** 跟踪出现问题。重复的 Klaviyo.js 可能会导致现场跟踪中断。要检查您是否有重复的 Klaviyo.js：

1. 导航到您的主主题文件。 Klaviyo.js 看起来像这样：

   ````
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=API_KEY"></script>
   ````
2. 如果您在文件中搜索 company\_id 并找到它两次（并看到上面显示的两个片段），那么您就有了重复的 Klaviyo.js。等号后通常有两个不同的 API 密钥，每个 Klaviyo 帐户都有一个。 3. 为确保从您的网站中正确删除重复项，请[联系 Klaviyo 支持](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。 ****对于 BigCommerce 用户：您的“添加到购物车”按钮使用的代码片段是否正确？****

BigCommerce 需要手动安装的代码片段才能使用 **添加到购物车** 跟踪。有 2 个不同的片段可以安装到您的主题中，具体取决于您的“添加到购物车”按钮是否有 ID。请参阅我们的指南[如何为 BigCommerce 创建“添加到购物车”事件](https://help.klaviyo.com/hc/en-us/articles/360024310292)，了解有关如何检查这一点的更多信息。 ****对于 WooCommerce 和 Magento 用户：您是否使用最新版本的集成插件？****

如果您使用的是 WooCommerce 或 Magento，**添加到购物车** 跟踪问题可能与您平台的 Klaviyo 插件的其他问题有关。 1. 如果 **添加到购物车** 事件未跟踪，请通过在 Klaviyo 的 ****Analytics > Metrics**** 中搜索 **Started Checkout** 来检查 **Started Checkout** 事件是否正在跟踪。 2. 如果 **已添加到购物车** 和 **开始结帐** 均未跟踪，则您的插件可能存在问题。 3. 检查您是否使用最新版本的插件进行集成。如果需要，请更新到 WooCommerce 或 Magento 中的最新版本，或者您可以从相关平台的列表中下载最新版本。 - [Klaviyo WordPress (WooCommerce) 插件](https://wordpress.org/plugins/klaviyo/)
- [Klaviyo Magento 1 扩展](https://www.klaviyo.com/media/downloads/MagentoKlaviyo-Latest.tgz)
- [Klaviyo Magento 2 扩展](https://help.klaviyo.com/hc/en-us/articles/115005254348#h_01F7458JT1BK3PB93NXHJPMSKE)

****对于 Shopify 用户：在允许现场跟踪之前，您是否需要欧盟、欧洲经济区、英国和瑞士的访问者同意 cookie？****

根据您在 Shopify 中的客户隐私设置，Klaviyo 可能不会跟踪欧盟、欧洲经济区、英国和瑞士的 Shopify 商店访客的现场活动，除非他们同意。 ## 联系 Klaviyo 支持

如果您在查阅此列表并测试跟踪后仍然遇到问题，请通过我们的[社区](https://community.klaviyo.com/got-a-question-1)或我们的[支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)联系。了解如何对其他指标进行故障排除：

其他资源：