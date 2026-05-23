---
id: "360037501212"
title: "了解流中的 Magento 1 数据"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360037501212-Understanding-Magento-1-data-in-flows"
section: "Magento 1"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:46Z"
language: "zh"
---
Klaviyo 的 Magento 1 集成不再接受新安装，并将于 2027 年末完全终止支持。Klaviyo 支持不再能够协助处理 Magento 1 相关请求。 ## 你将会学到

了解哪些 Magento 1 数据同步到 Klaviyo，以及如何在流程中使用该数据的示例。当您将 Magento 1 帐户与 Klaviyo 集成时，您将可以访问历史数据和动态 Magento 1 数据，您可以在 Klaviyo 中使用这些数据来个性化客户体验。通过使用 Klaviyo 流，有许多出色的方法可以做到这一点。要深入了解您的 Magento 1 数据：[查看并了解您的 Magento 1 数据](https://help.klaviyo.com/hc/en-us/articles/115005254528-Review-and-Understand-your-Magento-1-Data)。 Magento 1 数据可用于触发流并填充流电子邮件。 ## 流量计时

流程延迟经过精心安排，以确保您的内容与客户体验相关。设置流程时，请记住 Magento 1 同步的一般时间。 Magento 1 每 30 分钟与 Klaviyo 同步一次。例如，如果您将第一封废弃购物车电子邮件设置为在某人放弃购物车后 15 分钟发送，则即使您的客户确实完成了购买，他们也可能会收到此电子邮件，因为在发送电子邮件之前，已下订单数据可能尚未同步到 Klaviyo。为了防止这种情况发生，最安全的做法是将延迟设置为至少 45，以适应 Magento 30 分钟的一般时间同步。 ## 废弃购物车流程

废弃的购物车流量通常是 Klaviyo 帐户中收入最高的流量。 Klaviyo 提供了一个预先构建的废弃购物车流程，当您与 Magento 1 集成时，该流程会出现在您的流程库中。 **集成要求：** Magento 1 插件安装网站跟踪

**您将使用的数据：** [Checkout Started](https://help.klaviyo.com/hc/en-us/articles/115005254528-Review-and-Understand-your-Magento-1-Data#checkout-started4)（Magento 1 指标），动态产品数据

请注意，**结帐开始** 指标与描述添加到购物车的产品的元数据相关联。您可以选择在事件时间轴上显示或折叠元数据。 **该指标的含义：** Magento 1 中的 [结帐开始](https://help.klaviyo.com/hc/en-us/articles/115005254528-Review-and-Understand-your-Magento-1-Data#checkout-started4) 意味着客户在 Magento 结帐流程的第一页上输入联系信息和送货信息，然后单击“继续”。 **如何触发指标：****结帐开始** 在 Magento 1 中，当有人登陆结帐页面并且客户在结帐字段中输入内容时，就会触发；当电子邮件字段更改时，Klaviyo 捕获 C**heckout Started** 事件。当 Magento cron 作业运行时，事件会同步到 Klaviyo。 **流程名称：** 废弃购物车

**流程触发：** 基于事件；此流程由 **Checkout Started** 指标触发

这是 Magento 1 商店的废弃购物车流程：
![](https://klaviyo.zendesk.com/hc/article_attachments/28715963355035)

您可以使用 [动态模板变量](https://klaviyo.zendesk.com/hc/en-us/articles/115000096232) 将 Magento 1 产品数据拉入电子邮件 [文本] 来创建包含客户购物车中剩余商品的个性化流程电子邮件块](https://help.klaviyo.com/hc/en-us/articles/115005082447-The-Email-Template-Editor#text-blocks4)。 **了解更多：** [如何创建废弃的购物车流程](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)

## 浏览放弃流程

浏览放弃流程是一个强大的流程，当客户在您的网站上查看特定产品时，可以吸引客户的兴趣。 Klaviyo 仅跟踪“已知浏览器”的浏览活动，这些浏览器之前至少访问过您的网站并与之互动过一次。我们可以通过两种关键方式识别网站访问者：

1. 如果有人点击 Klaviyo 电子邮件访问您的网站。 2. 如果有人通过 Klaviyo 表格订阅或选择加入。匿名浏览器不会被跟踪。 Klaviyo 在“流程”部分中提供了预构建的“浏览放弃”流程，但您可以[轻松创建自己的流程。](https://klaviyo.zendesk.com/hc/en-us/articles/115002775252)

**集成要求：** Magento 1 插件会自动安装查看的产品代码片段。 如果您尚未在 Magento 1 中实现查看的产品跟踪，请转到[与 Magento 1 集成](https://help.klaviyo.com/hc/en-us/articles/115005082187-Integrate-with-Magento-1-x-CE-and-EE-#install-the-klaviyo-extension-in-magento4)

**您将使用的数据：查看的产品**（Klaviyo 指标）、动态产品数据

**该指标的含义：** [**查看的产品**](https://help.klaviyo.com/hc/en-us/articles/360030732832-Review-and-Understand-Your-WooCommerce-Data#viewed-product5) 在客户查看产品时进行跟踪。 **流程名称：** 浏览放弃

**流量触发：** 基于指标；此流程由 **查看的产品** 指标触发

这是 Magento 1 商店的浏览放弃流程：
![](https://klaviyo.zendesk.com/hc/article_attachments/28715969966491)

**了解更多：** [创建浏览放弃流程指南](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow)

## 交叉销售和产品审核流程

交叉销售流程使您可以定位全部购买了特定商品但尚未购买一个或多个相关商品的一组人。例如，如果有人购买了视频游戏机，您可以考虑向他们发送一封电子邮件，介绍他们尚未购买的该游戏机最受欢迎的视频游戏。产品审核流程还允许您定位购买特定商品的一群人。您可能希望按类别或系列过滤交叉销售/产品评论流程，以便您可以在电子邮件内容中提供更相关的建议。 Klaviyo 提供预构建的产品评论/交叉销售流程，可以在您的 [Klaviyo 流程库](https://klaviyo.zendesk.com/hc/en-us/articles/115002774932) 中找到。 **集成要求：** 有效的 Magento 1 集成

**您将使用的数据：** **已履行订单** 指标或 **已订购产品** 指标（均为 Magento 1 指标）

**指标含义：**

- **已履行订单**（Magento 1 指标）跟踪您在 Magento 商店中将订单标记为已发货的时间。 - **订购的产品**（Magento 1 指标）跟踪客户下订单的时间。对于某人购买的每件商品，都会跟踪一个订购产品事件。 **流程名称：** 产品评论/交叉销售

**流程触发：** 基于事件； **已履行订单** 指标

这是 Magento 1 商店的产品评论/交叉销售流程：
![](https://klaviyo.zendesk.com/hc/article_attachments/28715969958811)

您可以使用目录或产品源来个性化您的交叉销售电子邮件。有关更多信息[了解如何使用产品源和建议](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787)。 **了解更多：** [创建产品评论流程](https://help.klaviyo.com/hc/en-us/articles/115002779391-Create-a-Product-Review-Flow) 或 [创建追加销售或交叉销售流](https://help.klaviyo.com/hc/en-us/articles/115002775212-Create-an-Upsell-or-Cross-Sell-Flow)

## 客户赢回流程

赢回流程用于在不活跃的客户完全脱离您的品牌之前重新吸引他们。设置赢回流程后，请考虑[添加过去的个人资料](https://help.klaviyo.com/hc/en-us/articles/115002779231-Back-Populate-a-Flow)，以确保很久以前购买但此后未购买的任何人都可以及时收到您的赢回系列。举例来说，您的第一封赢回电子邮件设置为在有人购买后 6 个月发送。您可以将过去的个人资料添加到流程中，而不是等待 6 个月才有资格接收此电子邮件，以便 6 个月前下了订单但此后未购买的每个人都将立即收到电子邮件。 Klaviyo 在“流程”部分中提供了预构建的客户赢回流程，但您也可以轻松[构建自己的流程](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192)。 **集成要求：** 有效的 Magento 1 集成

**您将使用的数据：** **已下订单**（Magento 1 指标）

**该指标的含义：** 当客户完成结帐流程并在您的 Magento 1 商店中创建订单时，将跟踪[已下订单](https://help.klaviyo.com/hc/en-us/articles/115005254528-Review-and-Understand-your-Magento-1-Data#placed-order7)。 **流程名称：** 客户赢回流程

**流量触发：** 基于指标；此流程由 **已下订单** 指标触发

流过滤器：自开始此流以来**下订单**零次

这是 Magento 1 商店的客户赢回流程：
![](https://klaviyo.zendesk.com/hc/article_attachments/28715969973915)

您可以使用目录或产品提要来个性化您的赢回电子邮件。有关更多信息，请查看[产品源和建议](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787)。 **了解更多：** [创建赢回流程](https://klaviyo.zendesk.com/hc/en-us/articles/115002775192)

## 您是否使用亚马逊 Prime 购买？如果您使用 Prime 购买来支持商店中任何产品的付款和履行，则需要对流程进行一些添加，并创建一些新流程。第一：

- [将 Buy with Prime 与 Klaviyo 集成](https://help.klaviyo.com/hc/en-us/articles/14708088221467) 将 Buy with Prime 数据引入您的 Klaviyo 帐户。对于您废弃的购物车流程：

- 创建 2 个单独的废弃购物车流：1 个由 Magento 的结帐事件触发（如上所述），1 个由 Buy with Prime 的结帐事件触发。对于您的“Buy with Prime”流程，请阅读[如何为 Amazon Buy with Prime 创建废弃购物车流程](https://help.klaviyo.com/hc/en-us/articles/14985388418331)。 - 对于您的 Magento 废弃购物车流程，添加以下流程过滤器，以排除通过 Buy with Prime 进行购买的客户收到不正确的消息：
  - **下订单**（使用 Prime 购买）**自开始此流程以来零次。**

对于您的浏览放弃流程：

- 当您创建浏览放弃流程时（您只需创建一个流程，因为它是由 **查看的产品** 事件触发的）添加以下流程过滤器以将“使用 Prime 购买”数据合并到您的流程中：
  - **已开始结帐**（使用 Prime 购买）**自开始此流程以来零次**并且
  - **下订单**（使用 Prime 购买）**自开始此流程以来零次**。对于您的客户赢回流程：

- 创建两个单独的赢回流程：一个由 Magento 的 **已下订单** 事件触发（如上所述），另一个由 Buy with Prime 的 **已下订单** 事件触发，以考虑通过 Buy with Prime 下原始订单的客户。有关“Buy with Prime”赢回流程，请阅读[如何为 Amazon Buy with Prime 创建赢回流程](https://help.klaviyo.com/hc/en-us/articles/15156331062171)。 - 当您创建 Magento 赢回流程时，请添加以下流程过滤器，以排除通过 Buy with Prime 进行购买的客户接收到错误消息：
  - **下订单**（使用 Prime 购买）**自开始此流程以来零次。**

## 其他资源

- [如何与 Magento 1.x（CE 和 EE）集成](https://klaviyo.zendesk.com/hc/en-us/articles/115005082187)
- [Magento 1 数据参考](https://klaviyo.zendesk.com/hc/en-us/articles/115005254528)