---
id: "115003872251"
title: "如何建立库存回流"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115003872251-How-to-build-a-back-in-stock-flow"
section: "Back in stock flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:15Z"
language: "zh"
---
## 你将会学到

如果您使用 Shopify、BigCommerce、Magento 2、PrestaShop、SFCC 或 Shopware 平台，或者您有通过自定义目录 Feed 或 API 同步的库存感知目录，了解如何构建 Klaviyo 返回库存流，以提醒客户有关库存的信息。 **返回库存** 功能有 2 个关键组成部分：

1.****返回库存流****当有人订阅补货提醒时，他们的 Klaviyo 个人资料上将跟踪 **订阅返回库存** 事件。您将使用此事件来触发库存流量恢复。当购物者订阅补货警报时，他们将进入流程，并等待补货延迟，直到他们感兴趣的商品补货。 2. ****退货表格****一旦您的流程准备就绪并等待，您就可以将退货表格添加到您的网站。有 2 种类型的库存形式。 - 第一个使用 Klaviyo 的表单生成器，可用于 Shopify 和 Bigcommerce。 - [如何为 Shopify 和 BigCommerce 设置库存形式。](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
   - 第二种方法要求您将返回库存片段添加到商店的主题文件中。当商品售完时，此代码段将自动显示“有货时通知我”按钮。当购物者单击此按钮时，他们将填写一份表格并直接进入您的流程。具体平台说明如下：
     - [Magento 2](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)
     - [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/33059375555099)
     - [SFCC](https://help.klaviyo.com/hc/en-us/articles/22495505773083)
     - [商店软件](https://help.klaviyo.com/hc/en-us/articles/13325405718939)
     - [自定义目录源](https://developers.klaviyo.com/en/docs/how_to_enable_back_in_stock_for_custom_catalog_feeds)[API](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)

自定义指标不能用于触发库存流量回流。只有与列出的集成之一、自定义目录或补货订阅 API 调用一起使用的 Klaviyo 特定指标才能触发补货流。请记住，如果您使用 Shopify 的销售点 (POS) 硬件和电子商务商店，则库存流量将计算您实体店和仓库中的所有库存。 ## 流程最佳实践

使用流程时需要记住一些最佳实践：

- 从流程库中的预构建流程开始，获取实施最佳实践的模板。 - 将消息流保持在 1 到 3 条之间，以免订阅者超载。 - [优化您的发送频率](https://help.klaviyo.com/hc/en-us/articles/10948996125083)以确保客户有足够的时间检查他们的电子邮件。 - 为非必要消息开启[智能发送](https://help.klaviyo.com/hc/en-us/articles/115002779311)。如果您还没有这样做，请设置这些流程以最大限度地提高订阅者的转化率：

- [欢迎系列](https://klaviyo.zendesk.com/hc/en-us/articles/115002775172)
- [废弃的购物车](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)
- [浏览废弃](https://klaviyo.zendesk.com/hc/en-us/articles/115002775252)
- [Winback](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192)
- [审核请求](https://klaviyo.zendesk.com/hc/en-us/articles/115002779391)
- [购买后](https://klaviyo.zendesk.com/hc/en-us/articles/360028872611)

## 设置库存回流

Klaviyo 已在流量库中预先构建了可用的库存流量。 1. 导航至****流****选项卡。 2. 选择****创建流程****。 3. 您可以通过以下目标过滤您的视图，找到我们提供的所有忠诚度和销售导向的流程：“提醒人们购买”。
   ![流量库屏幕突出显示库存流量类别中的预建返回。](https://klaviyo.zendesk.com/hc/article_attachments/28720666883739)

您还可以通过在流程库顶部的工具栏中搜索“返回库存”来轻松找到这些可用的返回库存流程。从库填充您帐户中的任何流程后，我们建议您查看所有电子邮件内容并更新模板以匹配您的品牌。如果您想从头开始建立库存回流，您也可以这样做。 ![Klaviyo 电子邮件流示例设置，用于在商品有货时通过电子邮件提醒订阅者](https://klaviyo.zendesk.com/hc/article_attachments/28720621559067)1。 单击****创建流程 > 构建您自己的****。 2.进入流程构建器触发器选择后，选择****您的指标****。选择 Klaviyo 品牌的指标**订阅到库存**。不要添加任何触发器或流过滤器，然后单击****保存****。 3. 您想要拖入的下一个组件（直接在触发器之后）是**返回库存延迟**。进入您流程的收件人将在此延迟后等待，直到他们感兴趣的商品重新进货。发生这种情况后，他们将继续流程中的下一步（通常是电子邮件，但也可能是短信）。 4. 通常，您在此流程中只需要一条消息作为该项目已返回的通知。请务必为此消息[关闭智能发送](https://help.klaviyo.com/hc/en-us/articles/115002779311-Smart-Sending-for-Flows#how-to-disable-smart-sending)，以确保每个人都收到警报。您不需要向该系列添加任何时间延迟组件，因为库存延迟将确保进入您流程的每个人都会等到他们订阅的商品回到库存后再继续。 ## 返回库存流量设置

您可以根据库存流量调整 2 个关键设置：

- 最低库存规则
- 客户通知规则

这些可以在您的帐户设置中进行配置，并且适用于电子邮件和短信。在左下角选择您的帐户名，然后单击****设置>其他>返回库存设置****。 **退货设置**选项卡仅在您的帐户中记录至少 1 个**订阅退货**事件后才会出现。如果您没有看到这些设置，请确保首先触发事件。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34361520770843)

### 最低库存规则

最低库存规则是指在您通知订阅者之前需要补充多少商品。根据您在库存耗尽时处理补货的方式，您可能一次只能收到给定 SKU 或变体的少量产品。如果是这种情况，您可能更愿意设置一个阈值，在该阈值下您认为数量足以让人们知道该商品已重新有库存。 ### 通知策略规则

通知策略规则有 2 个子设置，它们协同工作以自定义发回库存消息的数量和频率。这些设置允许您一次或批量发送补货通知。您可以配置的 2 个组件是：

- ****要通知的客户**** 这决定了在重新进货时会通知多少客户。如果您有高需求的商品，当缺货时您可能会收到数百个订阅。如果一件商品重新进货，您不想向所有这些人发送有关该商品的电子邮件。 - ****通知之间的等待时间****如果您选择指定每个重新进货的商品发送的电子邮件数量，这将确定批次电子邮件之间等待的时间。例如，如果补货了 20 件商品的库存，并且您将“要通知的客户”设置为 5，则每件商品将通知 5 名客户，从而导致最早的 100 名客户收到通知。然后，该流程将根据“通知之间的等待时间”设置进行等待，然后根据剩余库存发送给下一批客户。电子邮件将继续批量发送，直到现有库存降至您帐户的最低库存阈值以下。如果在等待期内补货了其他商品，则在等待期结束之前不会发送其他电子邮件。在等待期结束时，我们将确定该商品的库存数量，并通知正确的订阅者数量。 ## 返回库存报告

检查库存报告页面以查看库存流中的活动。 1. 单击库存延迟组件。 2. 单击详细信息侧栏中的****查看库存报告****链接。 ![返回库存延迟组件内的左侧边栏，光标悬停在查看返回库存产品请求报告的链接上](https://klaviyo.zendesk.com/hc/article_attachments/28720621560987)

此页面将显示最近的库存恢复活动，您也可以将其导出到 CSV 文件。虽然股票报告页面背面未显示，但您可以[导出所有当前排队返回股票订阅者的 CSV 文件](https://help.klaviyo.com/hc/en-us/articles/1260805819449)。 您还可以通过点击“****订阅****”按钮来订阅接收此报告的电子邮件通知。 ![Klaviyo 库存报告模式，带有用于订阅报告的菜单选项、电子邮件地址字段以及发送频率菜单](https://klaviyo.zendesk.com/hc/article_attachments/28720621546011)

****预定报告****选项卡可让您调整您订阅的报告以及每个报告的设置。您可以通过转至****帐户 > 设置 > 更多 > 返回库存报告**** 导航到此选项卡。 ![Klaviyo 计划报告页面视图，显示报告名称、频率以及接收报告的人员](https://klaviyo.zendesk.com/hc/article_attachments/28720621551899)

## 其他资源

查找有关库存流量背面的其他文章：

- [如何将短信添加到库存流](https://help.klaviyo.com/hc/en-us/articles/7954040204827)
- [如何配置库存邮件](https://help.klaviyo.com/hc/en-us/articles/360051612751)
- [了解库存流量如何运作](https://help.klaviyo.com/hc/en-us/articles/360051612551)
- [如何导出排队的库存订阅者列表](https://help.klaviyo.com/hc/en-us/articles/1260805819449)