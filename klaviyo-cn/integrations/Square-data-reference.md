---
id: "11117271030555"
title: "平方数据参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/11117271030555-Square-data-reference"
section: "Square"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:10Z"
language: "zh"
---
## 你将会学到

了解哪些数据从 Square 同步到 Klaviyo、如何查看数据以及 Square 事件包含哪些属性。此外，了解如何在 Klaviyo 中查看 Square 数据。 ## 开始之前

如果您还没有阅读我们关于[Square 入门](https://help.klaviyo.com/hc/en-us/articles/11117215837211) 的文章，以获取有关如何集成您的商店的分步说明，然后再继续阅读本文。 ## 如何查看您的数据

要检查从 Square 到 Klaviyo 的数据同步：

1. 在您的 Klaviyo 帐户中，选择****集成****选项卡。 2. 在**启用的集成**列表中选择****Square****。 3. 选择顶部的****数据****选项卡。在这里，您将看到从 Square 同步到 Klaviyo 的最新数据，以及历史数据同步的同步进度条。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720659703835)

如果您遇到同步问题，您可以在此处选择****重新启动导入****来重新启动历史数据同步。 ## 从 Square 同步的数据

Square Online 的事件实时同步到 Klaviyo，Square POS 的事件每 30 分钟同步一次。从 Square 同步到 Klaviyo 的数据包括：

- [已知网站访问者](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Onsite-Tracking#who-klaviyo-tracks5) 被跟踪为 **Active on Site** 事件（如果您选中了现场 JavaScript 设置）
- 电子邮件退订
- 与订单事件相关的客户信息
- 您的 Square 目录（包括仅限 POS 的商品）
- 以下事件：
  - 放弃结账
  - 已下订单
  - 订购的产品
  - 已退款的订单
  - 取消订单
  - 已履行部分订单
  - 已履行的订单

如果存在与客户直接与您的公司共享的订单关联的电子邮件地址和/或电话号码，Square POS 订单事件将同步到 Klaviyo（并且将创建 Klaviyo 配置文件）。 Square 事件将有一个名为 **source name** 的属性，该属性将显示该事件是来自 POS 还是来自在线/网络，以便您可以[在 Klaviyo 中对这些事件进行分段](https://help.klaviyo.com/hc/en-us/articles/115005237908-Getting-started-with-segments)。 ## 客户信息详情

如果客户直接与您的公司共享了与客户关联的电子邮件地址和/或电话号码，则客户资料会从 Square 同步到 Klaviyo。从 Square 同步到 Klaviyo 的配置文件将使用以下属性创建：

- ****电子邮件****客户的电子邮件地址
- ****名字****
  客户的名字（必填）
- ****姓氏****
  客户的姓氏
- ****城市****
  客户所在城市
- ****州/地区****
  客户状态
- ****邮政编码****
  客户的邮政编码
- ****国家****
  客户所在国家/地区
- ****电话号码****
  客户的电话号码。如果您[设置 Klaviyo SMS](https://help.klaviyo.com/hc/en-us/articles/4404274419355-How-to-turn-on-SMS-in-Klaviyo)，Klaviyo 只会创建仅限电话的配置文件
- ****生日****客户的生日（如果提供）
- ****方组****
  与客户关联的 Square 组。目前不包括方形线段

### 电子邮件同意

Square 平台是一个“选择退出”营销同意平台。这意味着向您提供电子邮件地址的任何人都没有机会明确同意您的电子邮件营销。相反，Klaviyo 会将 Square 中 email\_unsubscribed 设置为 false 的用户在 Klaviyo 中标记为“从未订阅”，而将 Square 中 email\_unsubscribed 设置为 true 的用户在 Klaviyo 中标记为“已取消订阅”。 ### 短信同意

Square Online 中收集的 SMS 订阅者目前无法同步到 Klaviyo。您可以通过 Square 网站上的 [Klaviyo 表单](https://help.klaviyo.com/hc/en-us/articles/360026474752-Getting-started-with-sign-up-forms) 收集短信同意。 ## 目录项详细信息

目录项目从 Square 同步到 Klaviyo，具有以下属性：

- 物品名称
- 物品ID
- 物品描述
- 商品价格
- SKU
- 网址
- 图片网址
- 库存数量
- 库存政策
- 类别
- 已发表
- 变体

## 同步事件及其属性

### 放弃结账

此事件在 Square 在线商店中废弃购物车 1 小时后触发，可用于[废弃购物车流程](https://help.klaviyo.com/hc/en-us/articles/115002779411-How-to-create-an-abandoned-cart-flow)。 为了使此活动同步到 Klaviyo，您必须首先在 Square 中关闭废弃的购物车电子邮件。为此：

1. 登录 Square 并导航至您的[概述页面](https://square.online/)
2. 选择****通讯 > 废弃的购物车****
3. 选择****禁用****

Klaviyo 中事件的顶级属性是：

- ****$价值****
  购物车中的总金额
- ****物品****
  订单中包含的项目
- ****收藏****
  与订单中包含的商品链接的集合
- ****物品数量****
  订单中包含的商品总数

### 已下订单

当在 Square 在线商店或 POS 终端上放置订单事件时，会触发此事件。 Klaviyo 中事件的顶级属性是：

- ****$价值****
  订单总金额
- ****物品****
  订单中包含的项目
- ****收藏****
  与订单中包含的商品链接的集合
- ****物品数量****
  订单中包含的商品总数
- ****折扣代码****
  应用于订单的折扣代码
- ****总折扣****
  折扣总额
- ****来源名称****订单来源（Square Online、POS）
- ****地点名称****方形地点名称

### 订购的产品

当在 Square 在线商店或 POS 终端上放置订单事件时，会触发此事件。 **已下订单**中的每件商品都会触发 **已订购产品** 事件。 Klaviyo 中事件的顶级属性是：

- ****$价值****
  订单总金额
- ****姓名****
  订购的产品名称
- ****变体名称****
  产品变体的名称
- ****SKU****
  产品库存单位
- ****产品 ID****
  产品标识符
- ****变体 ID ****变体标识符
- ****数量****
  产品数量
- ****收藏****
  与产品相关的集合
- ****变体选项****订购产品的变体选项
- ****修改选项****应用于订单的修改选项

### 订单退款

当 Square 在线商店或 POS 终端上的订单退款时，会触发此事件。 Klaviyo 中事件的顶级属性是：

- ****$价值****
  订单总金额
- ****收据 URL**** 订单收据的 URL
- ****来源名称****订单来源（Square Online、POS）
- ****地点名称****方形地点名称

### 取消订单

当客户在您的商店中创建订单但随后取消整个订单时，会触发此事件。 Klaviyo 跟踪的事件包括有关某人购买的商品的所有产品信息，包括产品名称和图像。不支持部分取消。 Klaviyo 中事件的顶级属性是：

- ****$价值****
  订单总金额
- ****商品****订单中包含的商品
- ****收藏****
  与订单中包含的商品链接的集合
- ****物品数量****
  订单中包含的商品总数
- ****折扣代码****
  应用于订单的折扣代码
- ****总折扣****
  折扣总额
- ****来源名称****订单来源（Square Online、POS）
- ****地点名称****方形地点名称

### 已履行部分订单

如果订单分多次配送发货，则将记录 **已配送的部分订单** 事件，并且每次部分配送都会记录一个事件。 Klaviyo 中事件的顶级属性是：

- ****$价值****
  履行总金额
- ****物品****
  履行中包含的项目
- ****收藏****
  与履行中包含的项目相关联的集合
- ****物品数量****
  履行中包含的项目总数
- ****折扣代码****
  应用于订单的折扣代码
- ****总折扣****
  折扣总额
- ****来源名称****订单来源（Square Online、POS）
- ****地点名称****方形地点名称

### 已履行订单

当 Square 在线商店或 POS 终端上完成订单时，会触发此事件。如果有多个订单与订单相关，则最后一次履行时将记录 **已履行订单** 事件。 Klaviyo 中事件的顶级属性是：

- ****$价值****
  订单总金额
- ****物品****
  订单中包含的项目
- ****收藏****
  与订单中包含的商品链接的集合
- ****物品数量****
  订单中包含的商品总数
- ****折扣代码****
  应用于订单的折扣代码
- ****总折扣****
  折扣总额
- ****履行状态****履行状态
- ****来源名称****订单来源（Square Online、POS）
- ****地点名称****方形地点名称

## 其他资源

- [Square 入门](https://help.klaviyo.com/hc/en-us/articles/11117215837211)
- [分段入门](https://help.klaviyo.com/hc/en-us/articles/115005237908-Guide-to-Creating-Segments)
- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-started-with-flows)