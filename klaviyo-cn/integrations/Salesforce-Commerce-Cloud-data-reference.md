---
id: "360058323811"
title: "Salesforce Commerce Cloud 数据参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360058323811-Salesforce-Commerce-Cloud-data-reference"
section: "Salesforce Commerce Cloud"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:53Z"
language: "zh"
---
## 你将会学到

了解[启用 Klaviyo 的 Salesforce Commerce Cloud 集成](https://help.klaviyo.com/hc/en-us/articles/360033744951) 后，哪些数据从 Salesforce Commerce Cloud 同步到 Klaviyo，以及如何查看这些数据。 ## 查看您的 Salesforce Commerce Cloud 指标

在您的 Klaviyo 帐户中，单击****分析****下拉列表并选择****指标****。在这里，您可以查看帐户中的所有指标，包括从 Salesforce Commerce Cloud 同步的指标。如果您在集成时启用**将事件标记为 SFCC**，则以下事件将显示并带有 SFCC 图标：

- 查看类别
- 查看过的产品
- 搜索网站
- 添加到购物车
- 开始结账
- 已下订单
- 订购的产品
- 订单确认

否则，SFCC 事件将显示为带有齿轮图标。无论您是否启用了品牌宣传，**网站上的活动**指标将始终带有齿轮图标。 ## Salesforce 商务云指标

以下是从 Salesforce Commerce Cloud 同步的所有指标的列表以及每个指标所包含数据的说明。您还可以在 Klaviyo 中[查看每个指标的原始数据](https://help.klaviyo.com/hc/en-us/articles/115005076747-View-Raw-Metric-or-Event-Data-in-Klaviyo)。 ### 现场活跃

当 cookie 访问者在您的网站上处于活动状态时，就会跟踪此指标。 ### 搜索站点

当 cookie 访问者发起搜索时，会跟踪此指标。 ### 查看的产品

当 cookie 访问者查看您网站上的产品页面时，系统会跟踪此指标。 ### 查看类别

当 cookie 访问者查看您网站上的类别页面时，系统会跟踪此指标。 ### 添加到购物车或添加到购物车

当 cookie 访问者添加或修改购物车中的商品时，系统会跟踪此指标。如果您使用我们的墨盒版本 23.7.0 或更高版本，此指标将称为 **添加到购物车**。如果您使用 23.7.0 之前的墨盒，此指标将称为 **添加到购物车**。如果您升级了墨盒并配置了相应的设置，出于连续性目的，它仍会被称为“**添加到购物车**”。请注意，使用名称**添加到购物车**将允许使用依赖于该指标的未来预构建的 Klaviyo 流。此指标跟踪每次有人将商品添加到购物车时，并记录当时购物车中的每个商品（第一个 **添加到购物车** 事件跟踪第一个商品，第二个事件跟踪第一个和第二个商品，等等）。 ### 开始结帐

当有人在结账时输入电子邮件，然后点击电子邮件字段之外的选项卡或单击时，就会跟踪此事件。此事件包括 cartRebuildingLink 属性，可用于将客户链接回其购物车。 ### 订单确认

该指标类似于**已下订单**，但实时同步，而不是每小时同步，并且可以使用**itemCategories** 属性进行分段。请注意，虽然 Klaviyo 可能会同步有关给定指标的许多详细信息，但并非所有同步的属性都可用于分段。出于数据管理目的，只有指标的主要详细信息会同步为“顶级”属性，并且只有这些顶级属性是可分段的。 Commerce Cloud 的 **已下订单** 和 **已订购产品** 指标不与顶级 **itemCategories** 属性同步。如果您希望使用 **itemCategories** 属性进行细分，则需要使用 **订单确认** 指标来执行此操作。这是实时订单确认电子邮件的理想选择。 ### 已下订单

当客户在 Salesforce Commerce Cloud 商店中完成结帐流程和订单时，系统会跟踪此指标。该活动将列出有关某人购买的商品的所有产品信息，包括产品名称和型号信息。然后，您可以在购买后续电子邮件中使用该信息。您可以根据以下条件过滤和定位 **已下订单** 事件：

- ****$价值****订单总价值，包括运费和任何适用的折扣。 - ****物品名称****
  订购产品的名称（例如 T 恤或裤子）。 - ****ItemCount****订单中的商品数量（例如 2）。 - ****订单号****与您的商店关联的订单号。 - ****站点ID****
  站点的 ID。 - ****状态****
  订单的状态。 - ****外部\_catalog\_id****
  设置为您的 SiteID；用于 Klaviyo 的目录组织。 ### 订购的产品

当客户下订单时也会跟踪此指标，但会针对某人购买的每件商品跟踪单独的事件。 例如，如果某人购买了一件 T 恤和一条裤子，则将跟踪整个购买的一个 **已下订单** 事件以及 2 个 **订购产品** 事件：1 个用于 T 恤，1 个用于裤子。 Klaviyo 跟踪的指标包括有关某人购买的每种产品的详细信息。当根据产品变体选项和**已下订单**事件中不可用的其他详细信息创建行为细分时，这非常有用。您可以根据以下条件过滤和定位**订购产品**事件：

- ****$价值****
  所购买商品的总价值；不包括运费或折扣。 - ****姓名****
  订购产品的名称或标题（例如 T 恤）。 - ****价格****
  商品的价格。 - ****SKU****
  产品变体的 SKU。 - ****产品ID****
  与您商店中的产品关联的 ID。 - ****数量****
  产品的订购总量。 - ****站点ID****
  站点的 ID。 - ****货币代码****
  用于购买产品的货币代码（例如美元）。 - ****外部\_catalog\_id****
  设置为您的 SiteID；用于 Klaviyo 的目录组织。 **下订单**和**订购产品**事件间隔几秒同步到 Klaviyo。因此，与用于触发和过滤流和段的指标保持一致非常重要。例如，如果流程由 **已下订单** 指标触发，并且您添加一个过滤器以排除自启动流程以来 **订购产品** 的任何人，则所有收件人都将被跳过，因为这两个事件是独立的，但同步间隔秒。作为最佳实践，使用**下订单**来触发和过滤流和段。 ## Salesforce Commerce Cloud 指标源

不同的 Salesforce Commerce Cloud 指标以不同的方式流入 Klaviyo：一些通过 Klaviyo 盒，一些通过 OCAPI 集成。当您与 Salesforce Commerce Cloud 集成时，您应该在 SFCC 中安装 Klaviyo 盒并在 Klaviyo 中启用 SFCC OCAPI 集成。有关这些步骤的更多信息，请参阅有关[与 Salesforce Commerce Cloud 集成](https://help.klaviyo.com/hc/en-us/articles/360033744951) 的文章。通过墨盒流入的指标如下：

- 订单确认
- 搜索网站
- 查看类别
- 查看过的产品
- 添加到购物车
- 开始结账

通过 OCAPI 流入的指标如下：

- 已下订单
- 订购的产品

历史数据每小时从 OCAPI 同步。您的目录应每 8 小时同步一次，所有其他指标将实时同步。 ## 其他资源

- [Salesforce Commerce Cloud 入门](https://help.klaviyo.com/hc/en-us/articles/360033744951)
- [如何升级 Salesforce Commerce Cloud 墨盒](https://help.klaviyo.com/hc/en-us/articles/16708128591259)
- [Klaviyo 开发者门户](https://developers.klaviyo.com/en)