---
id: "115005082547"
title: "BigCommerce 入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005082547-Getting-started-with-BigCommerce"
section: "Getting started with BigCommerce"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: "zh"
---
## 你将会学到

了解如何在 Klaviyo 中启用 BigCommerce 集成、添加 **查看的产品** 跟踪，并确认您商店的所有现场跟踪均正常运行。当您与 BigCommerce 集成时，您的历史电子商务、客户和目录数据将同步到您的 Klaviyo 帐户中。该集成会自动将 Klaviyo 的现场跟踪代码段添加到您的 BigCommerce 商店，这使您可以将 Klaviyo 注册表单添加到您的网站并跟踪客户何时在您的网站上活跃。 BigCommerce 集成还设置实时同步以捕获未来数据。 ## 开始之前

在集成之前，我们建议退出 BigCommerce 和 Klaviyo。 ## 如何集成视频

![](https://fast.wistia.com/embed/medias/cklrl4qtcm/swatch)

## 启用 BigCommerce 集成

要将 Klaviyo 与 BigCommerce 集成：

1. 登录您的 Klaviyo 帐户。 2. 在左侧导航栏中选择****集成****。 3. 单击****探索应用程序****并搜索 BigCommerce，然后单击该卡。然后，单击****安装****。 4. 单击****连接到BigCommerce****，出现提示时登录BigCommerce，然后单击****安装****。 5. 检查权限并单击****确认****以返回Klaviyo。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28716053446555)
6. 在 **Store URL** 下，输入您商店的永久地址。您商店的永久地址与客户访问您商店时所用的商店网址不同。永久地址是 BigCommerce 用于管理您的商店的特殊 URL。 1. 要查找此地址，请进入您的 BigCommerce 管理员并导航至****帐户设置 > 商店详细信息****。向下滚动找到您商店的****永久地址****。 ![BigCommerce 商店详细信息页面显示地址模糊的永久地址字段](https://klaviyo.zendesk.com/hc/article_attachments/28716063842075)
7. 选中此框可自动添加 Klaviyo 现场 javascript，这将允许现场跟踪和表单。 8. 接下来，如果您想在结帐时收集电子邮件订阅者，请选中****将您的 BigCommerce 电子邮件订阅者同步到 Klaviyo****。这将订阅在结帐期间或通过 BigCommerce 页脚表单选择加入的联系人。从下拉列表中选择您想要添加订阅者的 Klaviyo 列表。如果您愿意，可以改为[创建新列表](https://help.klaviyo.com/hc/en-us/articles/115005078967-How-to-Create-and-Add-Contacts-to-a-New-List#create-a-new-list2)。 9. 要收集通过 BigCommerce 选择加入的 SMS 订阅者，请检查设置****将 BigCommerce SMS 订阅者同步到 Klaviyo****。在启用此设置之前，您必须首先[为您的 Klaviyo 帐户设置 SMS](https://help.klaviyo.com/hc/en-us/articles/360035285472-How-to-Set-Up-SMS)。 10. 如果您决定在结账时收集短信订阅者，请从下拉列表中选择您希望将其添加到的列表。系统还会提示您添加指向服务条款和隐私政策的链接，并将代码片段复制到您的 BigCommerce 结账文件中。有关如何执行此操作的说明，请按照我们的指南[在 BigCommerce 结帐时收集短信同意](https://help.klaviyo.com/hc/en-us/articles/360058194032)。您还必须添加披露语言以确保 TCPA 合规性。 11. 完成后，单击****完成设置****。您已成功启用 BigCommerce 集成。 ## 确认现场跟踪安装

当您与 BigCommerce 集成时，如果您检查了相关设置，则会在您的 BigCommerce 商店中自动安装启用现场跟踪的 Klaviyo.js 文件。 Klaviyo.js 做了两件事：

- 它使您能够直接从您的 Klaviyo 帐户将 Klaviyo 注册表单添加到您的网站。 - 它添加了**活动网站**跟踪，使您可以跟踪客户何时访问您的网站。您无需采取进一步的操作，但您可以验证 Klaviyo.js 是否正常工作。 1. 在您的 Klaviyo 帐户中，单击****集成****。 2. 在右上角，单击****管理数据> 设置网络跟踪****。您在集成时已经完成了第一步，第二步将在下一节的**查看的产品**跟踪中介绍。 3. 转到第三步，在框中输入您的商店 URL，然后单击****下一步****。 4. 单击生成的链接以重定向到您的商店。 ![在 Klaviyo 中设置网络跟踪页面显示三个步骤，第三步有一个文本框，其中填充了 BigCommerce 商店 URL，下一步为蓝色背景](https://klaviyo.zendesk.com/hc/article_attachments/28716063844251)
5. 返回Klaviyo，检查是否有成功按钮表示数据已接收。这意味着网络跟踪正在成功运行。 ![Klaviyo 设置网络跟踪页面第 3 步显示一个带有生成链接的框，收到的数据继续带有箭头和绿色背景](https://klaviyo.zendesk.com/hc/article_attachments/28716053427739)
6. 单击绿色成功按钮返回到您的 Klaviyo 仪表板。 ## 添加查看过的产品跟踪

**查看的产品** 跟踪允许您跟踪客户何时查看您的产品。要启用 **查看的产品** 跟踪，您需要将 **查看的产品** 代码段添加到您的 BigCommerce 主题文件中。 **查看的产品** 跟踪对于构建浏览放弃流程等流程是必要的，您可以在[创建浏览放弃流程中了解更多信息流](https://help.klaviyo.com/hc/en-us/articles/115002775252-Creating-a-Browse-Abandonment-Flow?utm_source=How%20to%20Integrate%20with%20Big%20Commerc e%20Stencil%20Themes%20Viewed%20Product&utm_medium=Help%20Center%20article&utm_campaign=BC%20Viewed%20Product#build-your-own-browse-abandonment-flow9)。 1. 在您的 Klaviyo 帐户中，单击****集成****。 2. 在右上角，单击****管理数据>**** ****设置网络跟踪****。您已经完成了集成的第一步。 3. 复制第二步中的 **查看的产品** 代码段。 ![Klaviyo 设置网络跟踪页面第 2 步在框中显示查看的产品代码片段](https://klaviyo.zendesk.com/hc/article_attachments/28716053433243)
4. 接下来，您将 **查看的产品** 代码片段粘贴到您的 BigCommerce 主题文件中。在新选项卡中，登录 BigCommerce 仪表板并导航至 ****Storefront**** > ****我的主题****。 5. 从**当前主题**中，单击****高级设置****下拉列表，然后单击****编辑主题文件****。如果您使用默认主题，则不会显示编辑主题文件的选项。首先，制作主题的副本，然后对该副本进行编辑。您所做的任何编辑将仅适用于您正在编辑的主题。请注意，如果您将来更改主题，则需要将“查看的产品”跟踪安装到新主题。 ![BigCommerce 我的主题页面，其中包含针对当前主题打开的高级下拉菜单，并以浅蓝色突出显示编辑主题文件](https://klaviyo.zendesk.com/hc/article_attachments/28716053430427)
6. 在编辑器中，导航至****模板 > 页面****，向下滚动，然后单击打开****product.html**** 页面。 7. 在此页面底部粘贴查看的产品代码片段。然后单击****保存所有文件。 ![BigCommerce 文件编辑器显示 Product.html 文件，底部添加了 Klaviyo 查看的产品片段](https://klaviyo.zendesk.com/hc/article_attachments/28716053438363)****

您现在已在所有产品页面上启用“查看的产品”跟踪。 ## 数据同步到 Klaviyo

BigCommerce 集成与 Klaviyo 实时同步。启用 BigCommerce 集成后，它将同步有关您客户的以下信息：

- 销售和订单数据，包括购买的产品、产品图片、价格和数量。 - 客户信息，包括名字、姓氏以及他们如何找到您的商店。仅当客户下订单时，位置信息才会同步到 Klaviyo。 - 履行、退款和取消订单数据。 - 人们何时访问您的网站以及他们查看哪些产品和系列。要查看您的 Klaviyo 帐户中的 BigCommerce 事件数据：

1. 单击****分析****下拉列表并选择****指标****。 2. 从右上角的过滤器下拉列表中选择 ****BigCommerce**** 以显示所有 BigCommerce 事件。 BigCommerce 事件与 BigCommerce 图标相关联。 ![Klaviyo 指标选项卡由 BigCommerce 过滤，列表中显示 6 个 BigCommerce 指标，包括已取消订单和已履行订单](https://klaviyo.zendesk.com/hc/article_attachments/28716063859227)
3. 详细了解[您的 BigCommerce 数据](https://help.klaviyo.com/hc/en-us/articles/115005082587-Review-and-Understand-Your-BigCommerce-Data)，以获取同步到 Klaviyo 的所有数据类型和特定事件的完整参考。 Klaviyo 将您可以创建的唯一指标的数量限制为 200 个。 当您接近此阈值时，您将通过帐户中的警告以及发送给帐户所有者的电子邮件收到提醒。 ## 结果

您已成功启用 BigCommerce 集成，确认现场跟踪正常运行，并将 **查看的产品** 跟踪添加到您的商店。 ## 后续步骤

恭喜您完成设置！现在您已经运行了集成，是时候开始添加 Klaviyo 的核心功能了，这样您就可以开始赚钱并发展您的业务了。完成此类别中的项目后，您就可以充分利用 Klaviyo 的功能了。 - [设置您的欢迎系列流程](https://help.klaviyo.com/hc/en-us/articles/115002775172-Create-a-Welcome-Series-Flow)。 - [设置废弃的购物车流程](https://help.klaviyo.com/hc/en-us/articles/115002779411-Create-an-Abandoned-Cart-Flow)。 - [将 Klaviyo 注册表单添加到您的网站](https://help.klaviyo.com/hc/en-us/articles/360002035871-Install-Klaviyo-Signup-Forms)。我们还提供使用现有表单或第三方表单提供商的首选选项，但我们推荐 Klaviyo 表单，因为它们是免费的，并且您可以定位关键的 Klaviyo 细分市场。 - 创建您的核心细分（[参与](https://help.klaviyo.com/hc/en-us/articles/115000200072-Create-an-Engagged-Master-List)、[未参与](https://help.klaviyo.com/hc/en-us/articles/115005078347-List-Cleaning)， [VIP](https://help.klaviyo.com/hc/en-us/articles/115005065707-Create-a-Segment-of-VIP-Customers-))。 - [发送您的第一个营销活动](https://help.klaviyo.com/hc/en-us/articles/115005054847-Create-and-Send-a-Campaign)。 ## 其他资源

- [BigCommerce数据参考](https://klaviyo.zendesk.com/hc/en-us/articles/115005082587)
- [如何为 BigCommerce 创建自定义添加到购物车事件](https://help.klaviyo.com/hc/en-us/articles/360024310292-Create-a-Custom-Added-to-Cart-Event-for-BigCommerce)
- 需要更多入门帮助吗？查看 [Klaviyo 的代理合作伙伴](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=integrations)