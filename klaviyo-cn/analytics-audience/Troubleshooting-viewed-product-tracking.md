---
id: "4416172774939"
title: "已查看商品跟踪问题排查"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4416172774939-Troubleshooting-viewed-product-tracking"
section: "Metrics troubleshooting"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:55:00Z"
language: "zh"
---
## 你将会学到

了解如何解决 **查看的产品** 跟踪问题，该跟踪用于跟踪访问者何时在您的网站上查看产品。对于某些电子商务平台，当您与 Klaviyo 集成时，会自动跟踪**查​​看的产品**。对于其他电子商务平台，必须手动将代码段添加到您的产品页面模板中。 ## 开始之前

在查阅本指南之前，请确保您：

- 启用**查看的产品**跟踪（如果未通过集成自动添加）。 - 启用 Klaviyo 的 [**在网站上活动**](https://help.klaviyo.com/hc/en-us/articles/115005076767) JavaScript（称为 Klaviyo.js），以便**查看的产品**跟踪正常工作。对于以下电子商务集成，**查看的产品**跟踪的工作原理如下：
- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407)
  如果您已打开 [Klaviyo 应用程序嵌入](https://help.klaviyo.com/hc/en-us/articles/4425956184731) 并检查集成的**查看的产品**设置，**查看的产品**跟踪将自动添加到您的商店。 - [BigCommerce](https://help.klaviyo.com/hc/en-us/articles/115005082547)
  了解如何[手动添加代码段](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#add-viewed-product-tracking4)
- [Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005082187)
  由 Klaviyo 自动添加
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115005254348)
  由 Klaviyo 自动添加
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808)
  由 Klaviyo 自动添加

如果您使用的是 BigCommerce，因此手动添加了 **查看的产品** 跟踪，请确保您添加到网站的代码段与上面链接的文章中显示的代码段完全匹配。如果您没有复制并粘贴整个片段，它将无法正常工作。如果您使用的电子商务平台没有预构建的 Klaviyo 集成或自定义平台，请了解[如何在我们的开发者网站上启用查看的产品跟踪](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration#viewed-product-tracking-snippet)。 ### Test Viewed Product tracking

要测试您的**查看的产品**跟踪设置是否正确，请按照以下步骤操作：

1. 导航至您的网站
2. 在您的主页上，将以下内容添加到 URL 末尾，将 **testing.email@gmail.com** 替换为您的电子邮件地址：
   **?utm\_email=testing.email@gmail.com**

   ![Shopify 测试商店，URL 附加 ?utm_email=example@gmail.com](https://klaviyo.zendesk.com/hc/article_attachments/28720760666651)
3. 重新加载页面
4. Navigate to a product page on your site
5. Search in Klaviyo for your email address
   ![Klaviyo 中的搜索栏](https://klaviyo.zendesk.com/hc/article_attachments/33675380127515)

   您应该看到已为您创建了 Klaviyo 个人资料（如果尚不存在），并且已在您的活动源中跟踪此产品视图。要查看一段时间内所有**查看的产品**指标的摘要：
6. 单击 Klaviyo 中的****分析****下拉菜单并选择****指标****
7. 按**查看的产品**进行筛选，以查看活动源、活动地图、图表、最佳人员和群组报告中的跟踪数据

![Klaviyo 中的“指标”选项卡，搜索栏中显示“已查看的产品”，结果中的“已查看的产品”带有齿轮图标](https://klaviyo.zendesk.com/hc/article_attachments/28720772435867)

查看下面的故障排除方案并进行更改后，您应该再次测试跟踪以确保其正常工作。 ## 目录

本指南涵盖以下故障排除场景：

- 您是否启用了 Klaviyo 的 **Active on Site** 跟踪？ - 您最近更换过电子商务平台吗？ - 您最近是否更新了商店的主题，或对您的电子商务平台进行了任何其他更新？ - 对于 WooCommerce 和 Magento 用户：您是否使用最新版本的集成插件？ - 对于 BigCommerce 用户：您的电子商务商店是否连接到多个 Klaviyo 帐户？ - 对于 Shopify 用户：在允许现场跟踪之前，您是否需要欧盟、欧洲经济区、英国和瑞士的访问者同意 cookie？ ## 故障排除场景

查看以下问题以诊断您**查看的产品**问题的原因。请注意，某些步骤是通用的，其他步骤取决于您使用的电子商务平台。 ****您是否启用了 Klaviyo 的“现场活动”跟踪？****

为了使 **查看的产品** 跟踪正常工作，您必须首先启用 Klaviyo 的 **Active on Site** 跟踪，该跟踪允许您的客户被 cookied。 **主动网站**跟踪是通过向您的网站添加 JavaScript 代码段（称为“Klaviyo 的现场 JavaScript”或“Klaviyo.js”）来启用的。 Klaviyo 会在集成过程中自动添加 Klaviyo.js，但某些集成需要您检查设置才能启用它。了解您的特定电子商务平台以及如何测试 Klaviyo.js 是否正常工作：

1.****Shopify****
   Klaviyo.js 会通过集成或通过嵌入 Shopify 中的 Klaviyo 应用程序自动添加（如果您启用）。 2.****WooCommerce****
   当您与 WooCommerce 集成时，Klaviyo.js 会自动添加，您可以通过阅读我们的 [WooCommerce 集成指南](https://help.klaviyo.com/hc/en-us/articles/115005255808-How-to-Integrate-with-WooCommerce) 确保您已完成所有步骤。要测试您的现场 JavaScript，请导航至****集成****，然后单击右上角的****设置网络跟踪****按钮。然后，找到可以在框中输入网站 URL 的步骤，并按照说明测试您的跟踪。 3. **大商务****
   确保您已选中[集成设置页面](https://www.klaviyo.com/integration/bigcommerce) 上的选项 **自动添加 Klaviyo 现场 JavaScript**。然后，[按照步骤测试您的现场 JavaScript](https://help.klaviyo.com/hc/en-us/articles/115005082547-How-to-Integrate-with-BigCommerce#confirm-web-tracking-installation3)。 4.****Magento 1****
   当您与 Magento 1 集成时，Klaviyo.js 会自动添加，您可以通过阅读我们的 [Magento 1 集成指南](https://help.klaviyo.com/hc/en-us/articles/115005082187-How-to-Integrate-with-Magento-1-x-CE-and-EE-) 来确保您已完成所有步骤。要测试您的现场 JavaScript，请单击左下角的帐户名称，选择****集成****，然后单击右上角的****设置网络跟踪****按钮。然后，找到可以在框中输入网站 URL 的步骤，并按照说明测试您的跟踪。 5.****Magento 2****
   当您与 Magento 2 集成时，Klaviyo.js 会自动添加，您可以通过阅读我们的[Magento 2 集成指南](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-) 来确保您已完成所有步骤。要测试您的现场 JavaScript，请单击左下角的帐户名称，选择****集成****，然后单击右上角的****设置网络跟踪****按钮。然后，找到可以在框中输入网站 URL 的步骤，并按照说明测试您的跟踪。 ****您最近更换过电子商务平台吗？****

如果您最近更换了电子商务平台，则需要将 **查看的产品** 跟踪添加到您的新网站。请参阅上面的**开始之前**部分中的信息，了解新平台的**查看的产品**跟踪。 ****您最近是否更新了商店的主题，或对您的电子商务平台进行了任何其他更新？****

如果您最近更新了商店的主题，则可能需要在新主题上重新安装 Klaviyo.js 和 **查看的产品** 代码段。对电子商务平台进行其他更新也可能会影响之前添加到您网站的代码片段。要重新安装 BigCommerce 的 **查看的产品** 代码段，请按照上面 **开始之前** 部分中的说明进行操作。如果您正在使用 WooCommerce 或 Magento，或者正在使用 Shopify 中嵌入的 Klaviyo 应用，但您已对网站进行了更改，但现在事件未跟踪，您应该[联系 Klaviyo 支持](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support) 来帮助诊断问题。 ****对于 WooCommerce 和 Magento 用户：您是否使用最新版本的集成插件？****

如果您使用的是 WooCommerce 或 Magento，**查看的产品** 跟踪问题可能与您平台的 Klaviyo 插件的其他问题有关。 1. 如果未跟踪 **查看的产品** 事件，请通过在 Klaviyo 的 ****Analytics********>********Metrics**** 中搜索 **Started Checkout** 来检查 **Started Checkout** 事件是否正在跟踪。 2. 如果 **查看的产品** 和 **开始结帐** 均未跟踪，则您的插件可能存在问题。 3. 如果可能，检查您是否正在使用最新版本的插件进行集成。如果您仍然遇到问题，请[联系 Klaviyo 支持](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。 ****对于 BigCommerce 用户：您的电子商务商店是否连接到多个 Klaviyo 帐户？****

如果您有一个商店连接到多个 Klaviyo 帐户，这可能会导致您的网站上出现重复的 Klaviyo.js，从而导致 **查看的产品** 跟踪中断。要检查您是否有重复的 Klaviyo.js：

1. 导航到您的主主题文件。 Klaviyo.js 看起来像这样：

   ````
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=API_KEY"></script>
   ````
2. 如果您在文件中搜索 company\_id 并找到它两次（并看到上面显示的两个片段），那么您就有了重复的 Klaviyo.js。等号后通常有两个不同的 API 密钥，每个 Klaviyo 帐户都有一个。 3. 为确保从您的网站中正确删除重复项，请[联系 Klaviyo 支持](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。 ****对于 Shopify 用户：在允许现场跟踪之前，您是否需要欧盟、欧洲经济区、英国和瑞士的访问者同意 cookie？****

根据您在 Shopify 中的客户隐私设置，Klaviyo 可能不会跟踪欧盟、欧洲经济区、英国和瑞士的 Shopify 商店访客的现场活动，除非他们同意。 ## 联系 Klaviyo 支持

如果您在查阅此列表并测试跟踪后仍然遇到问题，请联系我们的[社区](https://community.klaviyo.com/got-a-question-1)或我们的[支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。