---
id: "4579120745115"
title: "如何为 Shopify 安装 Markdown 通知"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4579120745115-How-to-Install-Markdown-Notifications-for-Shopify"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:58Z"
language: "zh"
---
## 概述

了解如何为 Shopify 安装 Klaviyo 的降价通知片段，以便您的客户可以在商品价格下降时订阅降价警报，以及如何构建降价通知流来发送警报。 Klaviyo 针对 Shopify 商店的 Markdown 通知功能有两个关键组件：

1.****Markdown 通知流程****：当有人订阅 Markdown 提醒时，将在其 Klaviyo 个人资料上跟踪“订阅 Markdown 通知”事件。这是您将用来触发 Markdown 通知流程的事件。购物者在订阅降价提醒时就会进入流程，并等待“降价通知延迟”，直到他们感兴趣的商品开始销售。 2.****网站按钮****：您需要在 Shopify 主题中添加一个片段，当商品降价时，该片段会自动显示“价格下降时通知我”按钮。当购物者单击此按钮时，他们将填写表格并订阅通知。 ## 添加 Markdown 通知片段

由于粘贴此代码需要访问您网站的 HTML 和电子商务平台，因此我们的支持团队无法提供实际帮助。如果您的团队中没有开发人员并且不愿意自己添加代码，请考虑[向 Klaviyo 合作伙伴寻求帮助](https://klaviyo.partnerpage.io/)。使用 Markdown 通知功能需要将 JavaScript 代码段粘贴到您的 Shopify 产品页面模板中。一旦您安装了下面提供的代码片段，就会发生以下情况：

- 当购物者浏览产品时，产品页面上会出现“降价时通知我”按钮。 - 当有人点击“通知我...”按钮时，会弹出一个表单，允许购物者注册以便在商品价格下降时收到通知。 - 提交表单后，购物者就可以收到来自降价通知流的警报。 Markdown 通知片段是：

````
[插入降价通知代码片段]
````

Shopify 2.0 主题的产品页面模板的管理方式有所不同。请根据您的主题查看下面相应的部分。 ### 对于 Shopify 2.0 主题

如果您的 Shopify 商店使用 Shopify 2.0 主题，您需要通过自定义 Liquid 块添加 Markdown 通知片段。 1. 在 Shopify 中，导航到您的主题并单击****自定义****。 2. 在页面顶部，单击****主页****下拉菜单，然后选择****产品>默认********产品****以进入默认产品页面。 1. 如果您有除默认模板之外的多个产品页面模板，您还需要将代码段添加到这些模板中。 3. 单击左侧边栏中的****添加部分****，然后选择****自定义液体****。 4. 将上述部分的代码片段粘贴到“自定义液体”文本框中。 ****[在自定义液体块中插入代码片段的屏幕截图]****
5. 单击右上角的****保存****。 6. 在左侧栏中，您的新自定义液体块应自动放置在页面上其他部分的下方。 1. 如果需要移动它，请将鼠标悬停在该块上，然后单击六个点将其拖动到其他部分下方。 ![Shopify 产品页面部分层次结构，其中自定义液体选项显示六个灰点，位于产品信息部分下方的产品推荐部分下方](https://klaviyo.zendesk.com/hc/article_attachments/28717988165659)

### 对于所有其他主题

对于其他 Shopify 主题，需要将 Markdown 通知片段粘贴到 ****product.liquid**** 文件的底部。 1. 复制本文前面包含的代码片段。 2. 在您的 Shopify 管理员中，单击****在线商店 > 主题****。从下拉列表中，单击“****编辑代码****”。 ![Shopify 主题页面在右下角显示浓缩咖啡杯，操作下拉菜单打开并选择编辑代码](https://klaviyo.zendesk.com/hc/article_attachments/28717988160411)
3. 搜索****product.liquid**** 文件。单击该文件以在编辑器中将其打开。 ![Shopify 的编辑主题页面呈灰色，并且选定并突出显示了product.liquid 文件](https://klaviyo.zendesk.com/hc/article_attachments/28717988162331)
4. 将代码片段粘贴到文件底部所有现有代码之后，然后单击****保存****。 ****[在 Shopify 主题编辑器中插入代码片段的屏幕截图]****

如果您使用自定义产品页面，则可能需要将此代码段添加到不同的主题文件或单个自定义产品页面。 ## 设置 Markdown 通知流程

Klaviyo 在 [流程库](https://www.klaviyo.com/library/flows) 中提供了预构建的 Markdown 通知流程。导航到“流程”选项卡后，您可以选择“****创建流程****”或“****浏览创意****”以直接进入库。您可以通过在流程库顶部的工具栏中搜索“markdown notification”轻松找到此 markdown 通知流程。 ****[在流程库中插入预建流程的屏幕截图]****

从库填充您帐户中的任何流程后，我们建议您查看所有电子邮件内容并更新模板以匹配您的品牌。如果您想从头开始构建 Markdown 通知流程，也可以这样做。 1. 单击****创建流****，为您的 Markdown 通知流命名，并添加标签。 2. 进入 Visual Flow Builder 后，选择触发选项****采取操作****。在随后的下拉菜单中，选择指标**订阅 Markdown 通知**。不要添加任何触发器或流过滤器，然后单击****完成****。 3. 您要直接拖入触发器之后的下一个组件是 **Markdown 通知延迟**。进入您流程的收件人将在此延迟后等待，直到他们感兴趣的商品重新进货。发生这种情况后，他们将继续流程中的下一步（通常是电子邮件，但也可能是短信）。 4. 通常，您在此流程中只需要一条消息作为商品降价的通知。请务必为此消息[关闭智能发送](https://help.klaviyo.com/hc/en-us/articles/115002779311-Smart-Sending-for-Flows#how-to-disable-smart-sending)，以确保每个人都收到警报。 ****[插入基本 Markdown 通知流程的屏幕截图]****

您不需要向该系列添加任何时间延迟组件，因为降价通知延迟将确保进入您的流程的每个人都会等到他们订阅的商品价格下降后再继续。 ## Markdown 通知流程与降价流程

Klaviyo 具有与 Markdown 通知类似的功能，即 [降价流程](https://help.klaviyo.com/hc/en-us/articles/4404249033755-Guide-to-Creating-a-Price-Drop-Flow)。这两个功能都允许根据商品降价的时间触发流程。但是，存在一些关键差异。请参阅下面的图表进行比较。 |  |  |
| --- | --- |
| ****Markdown 通知流程**** | ****降价流程**** |
|仅适用于 Shopify 商店。 |适用于 BigCommerce、Magento 2、Shopify 和 WooCommerce 商店。 |
|要求客户通过产品商店页面上的表单明确订阅产品的降价提醒。 |根据客户是否开始结帐购物车中的特定产品或在指定时间段内查看该产品而触发。 |
|为了符合客户的期望，客户将收到有关产品**任何**降价的通知，因为他们已明确订阅了降价警报。 |允许您自定义产品价格需要下降多少或百分比才能触发流程。 |
|即使客户过去购买过产品，也可以订阅降价提醒。 |不会发送给任何已经购买该产品的人，无论他们是以全价购买还是以折扣价购买。 |

可以同时使用两种流程类型，但如果您觉得这多余，您可以选择使用最适合您首选业务策略的功能。 ## 其他资源

- 在本课程中，了解如何[通过流程自动化客户旅程](https://academy.klaviyo.com/automating-the-customer-journey-with-flows)
- 了解如何在帮助中心创建其他流程：

- [欢迎系列流程](https://help.klaviyo.com/hc/en-us/articles/115002775172-How-to-Create-an-Email-Welcome-Series)
- [返回库存流程](https://help.klaviyo.com/hc/en-us/articles/115003872251-Building-a-Back-in-Stock-Flow)
- [追加销售或交叉销售流程](https://help.klaviyo.com/hc/en-us/articles/115002775212)
- [日期属性触发的流量](https://help.klaviyo.com/hc/en-us/articles/360002732652)