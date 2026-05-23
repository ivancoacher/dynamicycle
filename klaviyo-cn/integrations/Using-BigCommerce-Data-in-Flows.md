---
id: "360037937891"
title: "在流程中使用 BigCommerce 数据"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360037937891-Using-BigCommerce-Data-in-Flows"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:47Z"
language: "zh"
---
## 概述

当您将 BigCommerce 帐户与 Klaviyo 集成时，您将可以访问历史和动态 BigCommerce 数据，您可以使用这些数据来个性化客户体验。使用 Klaviyo 流有很多出色的方法可以做到这一点。要深入了解您的 BigCommerce 数据，请查看我们关于如何[查看和了解您的 BigCommerce 数据](https://klaviyo.zendesk.com/hc/en-us/articles/115005082587) 的文章。 BigCommerce 数据可用于触发流并填充流电子邮件中的内容。本文将重点介绍特定类型的数据，并举例说明如何在流中使用该数据。 ## 流量计时

时间延迟允许您控制某人何时收到流程中相对于上一步的一个步骤。这使您可以确保您的流程电子邮件及时且相关。设置时间延迟时，如果集成事件用于触发流程，请务必考虑与您的 Klaviyo 帐户同步的频率。 BigCommerce 使用 Webhooks 与 Klaviyo 实时同步，因此您不应期望 BigCommerce 中发生事件以及与 Klaviyo 同步事件时出现延迟。 ## 废弃购物车流程

对于任何电子商务企业来说，废弃的购物车电子邮件是最有价值的电子邮件之一。它们是发送给将商品添加到购物车但未能完成购买的用户的一封电子邮件或一系列电子邮件。不联系这些顾客就会浪费金钱——平均近 70% 的购物车被遗弃。 Klaviyo 提供了一个预先构建的废弃购物车流程，当您与 BigCommerce 集成时，该流程会显示在您的 ****Flows**** 选项卡中。 **集成要求：** BigCommerce 插件安装网站跟踪

**您将使用的数据：[开始结帐](https://help.klaviyo.com/hc/en-us/articles/115005082587-Review-and-Understand-Your-BigCommerce-Data#started-checkout1)**（BigCommerce 指标）、动态产品数据
![BCflow5.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381708059)

**该指标的含义：** BigCommerce 中的[开始结账](https://help.klaviyo.com/hc/en-us/articles/360030732832-Review-and-Understand-Your-BigCommerce-Data#started-checkout1) 意味着客户在付款页面之前的页面上输入他/她的联系方式和送货信息，然后点击“继续”。 Klaviyo 跟踪的事件包括有关某人购物车中商品的所有产品信息，包括产品名称、图像和类别信息，以便您可以在废弃购物车电子邮件中使用该信息。 **流程名称：** 废弃购物车

**流程触发：** 基于事件；此流程由 **Started Checkout** 指标触发

这是 BigCommerce 商店的废弃购物车流程：
![BCflow3.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388013083)

这是开始结账、进入废弃购物车流程并收到第一封废弃购物车流程电子邮件的人的个人资料：
![BCflow11.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388033947)

您可以使用[动态模板变量](https://klaviyo.zendesk.com/hc/en-us/articles/115000096232)将 BigCommerce 产品数据拉入电子邮件 [文本] 来个性化流程电子邮件，以展示客户购物车中留下的商品阻止](https://help.klaviyo.com/hc/en-us/articles/115005082447-The-Email-Template-Editor#text-blocks4)。 ![BCAbCartEmails.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381705499)

**了解更多：** [创建废弃购物车流程指南](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)

## 浏览放弃流程

浏览放弃流程是一种强大的流程，可以在客户查看您网站上的特定产品时吸引客户的兴趣。尽管此流不是由 BigCommerce 指标触发的，但该流在流电子邮件中合并了 BigCommerce 数据。 Klaviyo 只能跟踪“已知浏览器”的浏览活动，这些浏览器之前至少访问过并参与过一次。我们可以通过两种关键方式识别网站访问者：是否有人点击了 Klaviyo 电子邮件访问您的网站，或者是否有人通过 Klaviyo 表单订阅或选择加入。匿名浏览器不会被跟踪。 Klaviyo 提供了一个预构建的浏览放弃流程，当您与 BigCommerce 集成时，该流程会显示在您的 ****Flows**** 选项卡中。 **集成要求：** 您必须已将查看的产品代码段安装到您的 BigCommerce 商店。 如果您尚未添加该代码，请按照以下说明[添加模板主题的查看产品](https://help.klaviyo.com/hc/en-us/articles/115005082547#add-viewed-product-tracking5) 或[添加蓝图的查看产品]主题](https://help.klaviyo.com/hc/en-us/articles/115005082627#add-viewed-product-tracking3)。 **您将使用的数据：** **查看的产品**（Klaviyo 指标），动态产品数据
 ![wooflow15.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381736603)

**该指标的含义：** 当客户查看产品时，我们会跟踪[查看的产品](https://help.klaviyo.com/hc/en-us/articles/360030732832-Review-and-Understand-Your-BigCommerce-Data#viewed-product5)。 **流程名称：** 浏览放弃

**流量触发：** 基于指标；此流程由 **查看的产品** 指标触发

这是 BigCommerce 商店的浏览放弃流程：
 ![wooflow9.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381739931)

您可以通过在电子邮件中使用[动态模板变量](https://klaviyo.zendesk.com/hc/en-us/articles/115000096232)提取 BigCommerce 产品数据来个性化流程电子邮件，以显示查看的商品阻止](https://help.klaviyo.com/hc/en-us/articles/115005082447-The-Email-Template-Editor#text-blocks4)。 ![BCBrowseEmails.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388031515)

这是查看过多种产品的人的个人资料。 Klaviyo 将此浏览活动跟踪为 **查看的产品** 事件，这些事件存储在客户的个人资料中：
![BCflow10.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381722011)

**了解更多：** [创建浏览放弃流程指南](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow)

## 产品评论/交叉销售流程

产品评论流程允许您定位购买特定商品的一组人。交叉销售流程使您可以定位一组已购买特定商品但尚未购买一个或多个相关商品的人群。例如，如果有人购买了视频游戏机，您可以考虑向他们发送一封电子邮件，介绍他们尚未购买的该游戏机最受欢迎的视频游戏。您可能需要按类别或系列过滤产品评论/交叉销售流程，以便您可以在电子邮件内容中提供更相关的建议。 Klaviyo 提供预构建的产品评论/交叉销售流程，可以在您的 [Klaviyo 流程库](https://klaviyo.zendesk.com/hc/en-us/articles/115002779211) 中找到。 **集成要求：** 有效的 BigCommerce 集成

**您将使用的数据：** **已配送订单** 指标或 **已订购产品** 指标（均为 BigCommerce 指标）
![BCflow6.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388022043)

**指标含义：**

- **[已履行订单](https://help.klaviyo.com/hc/en-us/articles/115005082587-Review-and-Understand-Your-BigCommerce-Data#ordered-product3)**当订单状态更新为 **已发货** 或 **已完成** 时，将跟踪（BigCommerce 指标）。 - **[已下订单](https://help.klaviyo.com/hc/en-us/articles/115005082587-Review-and-Understand-Your-BigCommerce-Data#placed-order2)**当客户完成结账流程并在您的 BigCommerce 商店中创建订单时，系统会跟踪（BigCommerce 指标）。许多产品可以包含在一个**已下订单**事件中。 **流程名称：** 产品评论/交叉销售

**流程触发：** 基于事件； **订购产品** 公制

这是 BigCommerce 商店的产品评论/交叉销售流程：
![BCflow7.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381713307)

您可以使用目录或产品源来个性化您的交叉销售电子邮件。有关更多信息，请查看[产品源和推荐](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787)。 ![BCCrossEmails.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388026651)

这是购买并收到已标记为交叉销售的商品的人的个人资料。 订单的完成由 **已完成的订单** 指标表示，并且客户已收到并打开了一封流程电子邮件：
![BCflow8.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381719323)

**了解更多信息：** [创建追加销售或交叉销售流程](https://help.klaviyo.com/hc/en-us/articles/115002775212-Create-an-Upsell-or-Cross-Sell-Flow) 和[创建产品评论流程](https://help.klaviyo.com/hc/en-us/articles/115002779391-Create-a-Product-Review-Flow)。 ## 客户赢回流程

赢回流程用于在不活跃的客户完全脱离您的品牌之前重新吸引他们。在设置后考虑[back-populate](https://help.klaviyo.com/hc/en-us/articles/115002779231-Back-Populate-a-Flow)您的赢回流程，以确保很久以前购买但此后没有购买过的任何人都可以及时收到您的赢回系列。举例来说，您的第一封赢回电子邮件设置为在有人购买后六个月发送。您不必等待六个月才有资格接收此电子邮件，而是可以重新填充流程，以便六个月前下了订单但此后未购买的每个人都将立即收到电子邮件。 Klaviyo 在“流程”部分中提供了预构建的客户赢回流程，但您也可以轻松[构建自己的流程](https://help.klaviyo.com/hc/en-us/articles/115002775192)。 **集成要求：** 有效的 BigCommerce 集成

**您将使用的数据：** **已下订单**（BigCommerce 指标）
![BCflow12.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388037275)

**该指标的含义：** 当客户完成结帐流程并在您的 BigCommerce 商店中创建订单时，我们会跟踪[已下订单](https://help.klaviyo.com/hc/en-us/articles/115005082587-Review-and-Understand-Your-BigCommerce-Data#placed-order2)。 **流程名称：** 客户赢回流程

**流触发器：** 基于指标；此流程由**已下订单** 指标触发

流过滤器：自开始此流以来**已下订单** 零次

这是 BigCommerce 商店的客户赢回流程：
![BCflow13.png](https://klaviyo.zendesk.com/hc/article_attachments/28717381731483)

您可以使用目录或产品提要来个性化您的赢回电子邮件。如需了解更多信息，请查看[产品 Feed 和推荐](https://help.klaviyo.com/hc/en-us/articles/115005082787)。 ![wooflow27.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388050715)

这是不久前购买过商品的人的个人资料。他们作为非购买者的时间已经足够长，足以触发赢回流程：
![BCflow14.png](https://klaviyo.zendesk.com/hc/article_attachments/28717388042651)

**了解更多：** [创建赢回流程](https://help.klaviyo.com/hc/en-us/articles/115002775192)