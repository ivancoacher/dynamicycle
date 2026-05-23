---
id: "360034500652"
title: "如何在流程中使用 WooCommerce 数据"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360034500652-How-to-use-WooCommerce-data-in-flows"
section: "Getting started with WooCommerce"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:45Z"
language: "zh"
---
## 你将会学到

了解如何在流程电子邮件中使用 Klaviyo 的 WooCommerce 集成中的数据。当您将 WooCommerce 帐户与 Klaviyo 集成时，您将可以访问客户和购买数据，您可以使用这些数据来个性化客户体验。要查看我们从 WooCommerce 同步哪些事件，请参阅我们关于[查看您的 WooCommerce 数据](https://klaviyo.zendesk.com/hc/en-us/articles/360030732832) 的文章。 ## 预建流程

我们在 Klaviyo 流程库中提供各种预构建流程。要到达那里，请前往 Klaviyo 中的****Flows > Create Flow****。这些流程包括您需要在每个模板中预先填写的所有事件数据。下表列出了一些最受欢迎的 WooCommerce 预构建流程：

|  |  |  |
| --- | --- | --- |
|流程名称/链接|流量触发|笔记|
| [废弃购物车提醒（标准、电子邮件和短信）](https://www.klaviyo.com/library/flows?object_id=VEgT68) [废弃购物车提醒（标准、仅限电子邮件）](https://www.klaviyo.com/library/flows?object_id=JDzXbb) |开始结帐 |放弃的购物车流程可以使用 **开始结账** 或 **添加到购物车** 作为触发器；我们的标准流程使用**开始结帐**。 |
| [废弃购物车提醒（添加到购物车触发器、电子邮件和短信）](https://www.klaviyo.com/library/flows?object_id=UrgZwA) |已添加到购物车 |单击“**添加到购物车**”但尚未开始结帐的客户可能会更随意地浏览。 |
| [浏览放弃（标准、电子邮件和短信）](https://www.klaviyo.com/library/flows?object_id=VGYirB) [浏览放弃（标准、仅电子邮件）](https://www.klaviyo.com/library/flows?object_id=Lc85Du) |查看产品 | Klaviyo 只能跟踪“已知浏览器”的浏览活动，这些浏览器之前至少访问过并参与过一次。我们可以通过两种关键方式识别网站访问者：是否有人点击了 Klaviyo 电子邮件访问您的网站，或者是否有人通过 Klaviyo 表单订阅或选择加入。 |
| [产品评论/交叉销售（标准，仅限电子邮件）](https://www.klaviyo.com/library/flows?object_id=HgTBs2) |已履行订单 |您可以使用目录或产品提要来个性化您的赢回电子邮件。有关更多信息，请查看[产品源和推荐](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787)。 |
| [客户赢回（标准，仅限电子邮件）](https://www.klaviyo.com/library/flows?object_id=Nsiv5N) |已下订单 |在设置后考虑[back-populate](https://help.klaviyo.com/hc/en-us/articles/115002779231-Back-Populate-a-Flow)您的赢回流程，以确保很久以前购买但此后没有购买过的任何人都可以及时收到您的赢回系列。 |

请注意，要使用利用 SMS 的预构建流程，您必须首先[设置 Klaviyo SMS。](https://help.klaviyo.com/hc/en-us/articles/4404274419355-How-to-turn-on-SMS-in-Klaviyo)

## 从头开始构建流程

1. 要从头开始构建流程，请导航至 Klaviyo 中的****流程****选项卡。 2. 单击****创建流****。 3. 选择****构建您自己的****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33639117493147)
4. 为您的流命名，添加任何标签，然后单击****创建流****。 5. 接下来，设计流程。您可以根据从 WooCommerce 同步的任何事件触发流程。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33639088668315)
6. 要了解有关流触发器和过滤器以及向流添加步骤的更多信息，请参阅我们的[流入门指南](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8QEJ4GJ70BSKS4DNWQ)。 7. 接下来，您将创建[流电子邮件内容](https://help.klaviyo.com/hc/en-us/articles/115002774992)（或短信内容，如果需要）。请参阅以下部分，了解如何使用 WooCommerce 事件变量添加个性化。 8. 设计完流程电子邮件后，您就可以学习如何[设置流程上线](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8RVQANQHGVRJ6V4W63)。 ## 如何查找事件变量

### 电子邮件

要在流电子邮件中添加事件变量：

1. 在流程编辑器中打开电子邮件。 2. 点击 ****编辑电子邮件****。 3. 单击 ****预览和测试****。 4. 从“**事件属性**”菜单中单击属性名称进行复制。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28715969828763)
5. 将标签粘贴到您的流程电子邮件中。此预览窗口将显示该特定事件指标的所有可用数据。 列表条目从 0 开始编号。例如，如果 **{{ event.extra.line\_items.0.product.name }}** 是图像的变量条目，则 0 表示它是数组中的第一项。要使用事件变量，您必须准确复制它们。事件变量区分大小写，与预览窗口中的显示方式稍有偏差都可能导致变量不起作用。 ### 短信

1. 在流构建器中，单击要添加事件变量的 SMS 或 MMS。 2. 接下来，单击****配置内容****。 ![在流程中的 SMS 或 MMS 事件变量内，内容部分下方有一个用于配置内容的按钮，以便您可以添加事件变量](https://klaviyo.zendesk.com/hc/article_attachments/28715969808411)
3. 单击****配置内容****，查看可以在何处向消息添加文本、表情符号、静态或[动态图像](https://help.klaviyo.com/hc/en-us/articles/1260806102230) 和 GIF。在这里，您还可以插入配置文件个性化和事件变量。 4. 您可以在屏幕右侧的**预览**选项卡中找到事件变量。此选项卡显示您可以在其中导航的 10 个最近事件；例如，对于购买后流程，此处将显示最近 10 个**下订单**事件。 5. **预览**选项卡还将显示所有关联的事件变量。要查看变量，请点击选项卡右上角的****查看详细信息****按钮。 ![在短信或彩信中，导航到右上角的“预览”选项卡，并将鼠标悬停在信息图标上以查看“查看详细信息”操作](https://klaviyo.zendesk.com/hc/article_attachments/28715963229211)
6. 该下拉列表包含有关该事件的所有变量的信息。通过单击任何行项目，您可以自动将其复制到剪贴板，从而可以轻松地将事件变量添加到消息中。 ![在右上角的预览选项卡内，单击信息图标以在模式中显示下面的事件属性详细信息](https://klaviyo.zendesk.com/hc/article_attachments/28715963233179)

### WooCommerce 的常见事件变量

不同事件变量的语法取决于积分和事件指标。通过滚动预览窗口并单击不同的条目，您可以查看给定事件的所有可用变量的语法。下面列出了针对 **开始结帐** 事件的一些常见变量集成示例。请记住，确切的变量可能会有所不同，具体取决于用于触发流的指标。 |  |  |
| --- | --- |
| ****WooCommerce**** | |
| ****产品名称/标题**** | {{ event.extra.Items.0.Name }} |
| ****产品网址**** | {{ event.extra.Items.0.URL }} |
| ****图片**** | {{ event.extra.Items.0.Images.0.URL }} |
| ****产品价格**** | {{ event.extra.Items.0.LineTotal }} |
| ****数量**** | {{ event.extra.Items.0.Quantity }} |
| ****总计**** | {{ event.extra.Items.0.TotalWithTax }} |

您可以使用参数“?wck_rebuild_cart={{ event.extra.CartRebuildKey }}”[从 WooCommerce 中废弃的购物车流重建购物车](https://help.klaviyo.com/hc/en-us/articles/115005255808#01H8KXY3BCY0H4YDBT43XHS3R4)。 ## 您是否使用亚马逊 Prime 购买？如果您使用“Buy with Prime”来支持商店中任何产品的付款和履行，则需要对流程进行一些添加（无论是预建还是临时），并创建一些新流程。第一：

- [将 Buy with Prime 与 Klaviyo 集成](https://help.klaviyo.com/hc/en-us/articles/14708088221467) 将 Buy with Prime 数据引入您的 Klaviyo 帐户。对于您放弃的“开始结帐”流程：

- 创建两个单独的废弃购物车流程：一个由 WooCommerce 的结账事件触发（上面列出的预构建流程），另一个由 Buy with Prime 的结账事件触发。对于您的“Buy with Prime”流程，请阅读[如何为 Amazon Buy with Prime 创建废弃购物车流程](https://help.klaviyo.com/hc/en-us/articles/14985388418331)。 - 对于您的 WooCommerce 废弃购物车流程，添加以下流程过滤器，以排除通过 Buy with Prime 进行购买的客户收到不正确的消息：
  - **下订单**（使用 Prime 购买）**自开始此流程以来零次。**

对于您放弃的“添加到购物车”流程：

- 添加以下流过滤器，以排除开始结账或通过 Buy with Prime 进行购买的客户接收到错误消息：
  - **开始结帐**（使用 Prime 购买）**自开始此流程以来零次**并且
  - **下订单**（使用 Prime 购买）**自开始此流程以来零次。**
- “Buy with Prime”不需要第二个流程，因为“Buy with Prime”没有 **添加到购物车** 事件。对于您的浏览放弃流程：

- 当您创建浏览放弃流程时（您只需创建一个流程，因为它是由 **查看的产品** 事件触发的）添加以下流程过滤器以将“使用 Prime 购买”数据合并到您的流程中：
  - **已开始结帐**（使用 Prime 购买）**自开始此流程以来零次**并且
  - **下订单**（使用 Prime 购买）**自开始此流程以来零次**。对于您的客户赢回流程：

- 创建两个单独的赢回流程：一个由 WooCommerce 的 **已下订单** 事件（如上所列）触发，另一个由 Buy with Prime 的 **已下订单** 事件触发，以说明通过 Buy with Prime 下原始订单的客户。有关“Buy with Prime”赢回流程，请阅读[如何为 Amazon Buy with Prime 创建赢回流程](https://help.klaviyo.com/hc/en-us/articles/15156331062171)。 - 当您创建 WooCommerce 赢回流程时，请添加以下流程过滤器，以排除通过 Buy with Prime 进行购买的客户收到不正确的消息：
  - **下订单**（使用 Prime 购买）**自开始此流程以来零次。**

## 其他资源

了解有关 WooCommerce 的更多信息：

- [WooCommerce 数据参考](https://klaviyo.zendesk.com/hc/en-us/articles/360030732832)
- [如何为 WooCommerce 设置优惠券](https://klaviyo.zendesk.com/hc/en-us/articles/360031279471)
- [WooCommerce 集成问题排查](https://klaviyo.zendesk.com/hc/en-us/articles/4515829067803)