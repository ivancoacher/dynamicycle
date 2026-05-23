---
id: "360030732832"
title: "WooCommerce 数据参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360030732832-WooCommerce-data-reference"
section: "Getting started with WooCommerce"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "zh"
---
## 与 WooCommerce 集成同步的数据

本文介绍将 WooCommerce 商店与 Klaviyo 帐户集成时同步的数据。 Klaviyo 与 WooCommerce 实时同步。在您的 Klaviyo 帐户中，导航到 [分析](https://www.klaviyo.com/analytics/metrics) 选项卡并选择“指标”以查看帐户中的所有指标。所有 WooCommerce 指标都将具有 WooCommerce 图标，“添加到购物车”指标除外，该指标将具有齿轮图标。下面分别介绍了每个指标。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33638284951835)![mceclip0.png](https://klaviyo.zendesk.com/hc/article_attachments/28716329763867)

Klaviyo 将您可以创建的唯一指标的数量限制为 200 个。当您接近此阈值时，您将通过帐户中的警告以及发送给帐户所有者的电子邮件收到提醒。 ## 开始结账

此事件跟踪何时发生以下其中一种情况：

- 客户登录其帐户，将商品添加到购物车，然后查看结账页面
- 客户将商品添加到购物车、查看结账页面、输入帐单电子邮件地址

您可以根据以下条件过滤和定位 Started Checkout 指标：

- ****$value****：购物车的价值
- ****类别****：购物车中商品的类别
- ****货币****：购物车的货币类型
- ****CurrencySymbol****：购物车的货币符号
- ****ItemNames****：包含购物车中商品名称的数组

Klaviyo 在结帐时捕获购物车的价值，以及客户购物车的其他相关详细信息，您可以利用这些详细信息来发送个性化的废弃购物车电子邮件。 WooCommerce 有两种可能的放弃购物车流：由“已开始结帐”指标或“添加到购物车”指标触发的流。这两个指标都允许您利用购物车重建密钥，该密钥允许您创建一个链接，以便在客户通过此事件在另一台设备上触发的电子邮件返回购物车时重建客户的购物车。该键可以在“extra”属性数组中找到。您可以使用以下 URL 创建此链接：

`{{organization.url|trim_slash}}/cart?wck_rebuild_cart={{event.extra.CartRebuildKey}}`

## 添加到购物车

每当被 Klaviyo cookie 的客户将商品添加到购物车时，就会跟踪此指标。它包含有关已添加项目的详细信息。当根据用户添加到购物车的产品创建细分时，或者在构建废弃的购物车流时，这非常有用。您可以根据以下条件过滤和定位“添加到购物车”指标：

- ****$value****: 物品的价值
- ****AddedItemCategories****：项目所属的类别
- ****AddedItemDescription****：项目的描述
- ****AddedItemImageURL****: 项目图像的 URL
- ****AddedItemPrice****：商品的价格
- ****AddedItemProductID**** 产品在 WooCommerce 商店中的自定义 ID，例如 **1234**
- ****AddedItemProductName****：您商店中的产品名称，例如 **红色 T 恤**
- ****AddedItemQuantity****：商品的数量
- ****AddedItemSKU****：您商店中商品的 SKU，例如 **REDMEDIUMTSHIRT**
- ****AddedItemTags****：与该项目关联的任何标签
- ****AddedItemURL****：项目的 URL
- ****类别****：购物车中所有商品的类别
- ****ItemCount****：购物车中的商品总数
- ****ItemNames****：购物车中所有商品的名称
- ****标签****：购物车中所有商品的标签

Klaviyo 生成一个密钥（购物车重建密钥），允许您创建一个链接来重建客户的购物车，以防客户通过另一台设备上的此事件触发的电子邮件返回购物车。该键可以在“extra”属性数组中找到。您可以使用以下 URL 创建此链接：

`{{organization.url|trim_slash}}/cart?wck_rebuild_cart={{event.extra.CartRebuildKey}}`

“额外”属性数组虽然不可分段，但除了购物车重建键之外还包含有用的信息，例如：购物车的行项目、购物车的总计、购物车的小计和购物车的税金总额。 ## 已下订单

此事件跟踪客户何时完成结账流程并在您的 WooCommerce 商店中创建订单。当我们将订单与处理状态同步时，Klaviyo 会记录下订单事件。 Klaviyo 跟踪的事件包括 WooCommerce 捕获的所有产品信息，以便您可以在购买后续电子邮件中使用这些详细数据。您可以根据以下条件过滤和定位已下订单事件：

- ****$value:****订单的价值
- ****ItemNames****：某人订单中的产品名称，例如 **T 恤** 或 **裤子**
- ****IsDiscounted****：订单已打折； **真**或**假**
- ****UsedCoupon****：订单上使用了优惠券，例如 **true** 或 **false**
- ****ItemCategories:**** 购物车中的商品所属的类别
- ****运输方式（如果有）****
- ****优惠券（如果有）****

收入或**已下订单**值的计算方式如下：（小计 + 运费）- 任何折扣。您可能会发现 Klaviyo 仪表板上的 **收入** 值并不总是与您在 WooCommerce 中看到的收入值相符；这是因为 WooCommerce 会从其收入计算中减去退款订单，而 Klaviyo 则不会。 ## 已履行的订单

此事件跟踪订单何时在 WooCommerce 商店中变为“完成”。 Klaviyo 跟踪的事件包括有关某人购买的商品的所有产品信息，包括产品名称、图像和可变产品信息，以便您可以在购买后续电子邮件中使用该信息。您可以根据以下条件过滤和定位**已履行订单**事件：

- ****$value:****订单的价值
- ****ItemNames****：某人订单中的产品名称，例如 **T 恤** 或 **裤子**
- ****IsDiscounted****：订单已打折； **真**或**假**
- ****UsedCoupon****：订单上使用了优惠券，例如，**true** 或 **false**
- ****ItemCategories:**** 购物车中的商品所属的类别
- ****运输方式（如果有）****
- ****优惠券（如果有）****

## 订购的产品

当客户下订单时，系统会跟踪此事件，但客户购买的每件商品都会跟踪一个事件。例如，如果有人购买一件 T 恤和一条裤子，则会跟踪一个已下订单事件和两个已订购产品事件 - 一个为 T 恤事件，一个为裤子事件。 Klaviyo 跟踪的事件包括有关某人购买的每种产品的详细信息。当根据已下订单事件中不可用的产品选项和其他详细信息创建行为细分时，这非常有用。您可以根据以下条件过滤和定位订购产品事件：

- ****$价值:****该物品的价值
- ****ProductId****：WooCommerce 商店中产品的自定义 ID，例如 **1321**
- ****SKU****：您商店中产品的 SKU，例如 **REDMEDIUMTSHIRT**
- ****名称****：您商店中产品的名称，例如**红色T恤**
- ****数量：****订购商品的数量
- ****类别****：类别列表

## 取消订单

当客户在您的 WooCommerce 商店中创建订单但在履行之前取消订单时，系统会跟踪此事件。您可以根据以下条件过滤和定位**已取消订单**事件：

- ****$value:****已取消订单的总价值
- ****是否打折：**** 订单已打折； **真**或**假**
- ****ProductNames:****订单中不同产品的名称
- ****已用优惠券：**** 订单上使用了优惠券，例如，**true** 或 **false**
- ****ItemCategories:**** 购物车中的商品所属的类别
- ****商品名称：**** 某人订单中的产品名称，例如 **T 恤** 或 **裤子**
- ****优惠券（如果有）****
- ****运输方式（如果有）****

## 订单退款

当客户退款时，系统会跟踪此事件。您可以根据以下条件过滤和定位**退款订单**事件：

- ****$value:****退款订单的总价值
- ****是否打折：**** 订单已打折； **真**或**假**
- ****ProductNames:**** 订单中不同产品的名称
- ****已用优惠券：**** 订单上使用了优惠券，例如，**true** 或 **false**
- ****ItemCategories:**** 购物车中的商品所属的类别
- ****商品名称：**** 某人订单中的产品名称，例如 **T 恤** 或 **裤子**
- ****优惠券（如果有）****
- ****运输方式（如果有）****

## 查看的产品

当客户（之前由 Klaviyo 进行 cookie）查看产品时，会跟踪此事件。 如果您想设置[浏览放弃流程](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow)或根据产品浏览数据构建细分，这非常有用。 ## 现场活跃

当客户（之前由 Klaviyo 进行 cookie）在您的网站上处于活动状态时，就会跟踪此事件。 ## 客户数据

对于您的 WooCommerce 帐户中的每个客户，都会在您的 Klaviyo 帐户中创建一个个人资料。包括名字、姓氏和位置在内的客户信息将添加到此配置文件中。