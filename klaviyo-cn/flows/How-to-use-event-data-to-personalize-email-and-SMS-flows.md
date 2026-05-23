---
id: "115002779071"
title: "如何使用事件数据个性化电子邮件和短信流"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002779071-How-to-use-event-data-to-personalize-email-and-SMS-flows"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-05-11T10:59:42Z"
language: "zh"
---
## 你将会学到

了解什么是动态事件数据、何时使用它、在哪里找到它以及如何将其包含在流消息中。了解客户采取的不同操作，以及如何使用该数据在 Klaviyo 中创建个性化消息流。例如，您可以使用废弃购物车流消息中的事件数据来向个人显示他们留下的产品、产品的图像等。这可以为客户提供更加个性化的体验，以及更高的转化机会。 ## 关于事件变量

当您与第三方服务或工具集成时，Klaviyo 会在客户档案采取操作时记录某些指标。 Klaviyo 跟踪哪些操作取决于您的集成，但常见的操作包括**开始****结帐**、**下订单**和**查看产品**。此外，Klaviyo 中记录的每个指标都包含有关事件的相关信息，称为元数据。例如，当客户开始结帐时，Klaviyo 会将其作为**开始****结帐** 事件进行跟踪。 Klaviyo 会定期从第三方平台发送有关购物车中剩余商品、每件商品的数量、总数、图像等的详细信息。在 Klaviyo 中，此数据存储为事件变量，并包括与特定客户所采取的操作相关的所有信息。您必须安装集成才能显示事件数据。了解有关 [Klaviyo 构建的集成](https://help.klaviyo.com/hc/en-us/articles/115000256472) 或使用 [Klaviyo API 构建自定义集成](https://help.klaviyo.com/hc/en-us/articles/360045726811) 的更多信息。 ## 什么时候可以使用事件变量

由于事件变量基于客户的行为，因此它们只能在指标触发的流消息中使用。列表、细分和日期属性触发的流不是由事件触发的，而是由客户档案中有关客户的信息触发。因此，没有可以从流电子邮件或短信中提取和使用的事件变量。同样，事件变量不能在营销活动中使用，因为这些变量是手动、一次性发送的，并且不基于客户所采取的操作。指标触发流的常见示例包括：

- [废弃购物车](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow)，通过**开始结帐**或**添加到购物车**指标
- [购买后](https://help.klaviyo.com/hc/en-us/articles/360028872611-Guide-to-Creating-a-Post-Purchase-Flow)，通过 **已下订单** 指标
- [产品评论](https://help.klaviyo.com/hc/en-us/articles/115002779391-Create-a-Product-Review-Flow)，通过 **下订单** 指标
- [浏览放弃](https://help.klaviyo.com/hc/en-us/articles/115002775252-Create-a-Browse-Abandonment-Flow)，通过**查看的产品**指标
- [Winback](https://help.klaviyo.com/hc/en-us/articles/115002775192-Create-a-Winback-Flow)，通过 **已下订单** 指标

## 如何查找事件变量

### 短信

1. 在流构建器中，单击要添加事件变量的 SMS 或 MMS。 2. 在“**内容**”旁边，单击“****编辑****”。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33627696749595)
3. 在这里，您可以在消息中添加文本、表情符号、静态或[动态图像](https://help.klaviyo.com/hc/en-us/articles/1260806102230) 和 GIF。您还可以插入配置文件个性化和事件变量。 4. 要查找事件变量，请单击****预览和测试****。此模式显示您可以在其中导航的 10 个最近事件（例如，对于购买后流程，此处将显示 10 个最近的 **已下订单** 事件）。 5. 该模式还显示所有关联的事件变量。要查看变量，请在预览模式中打开****所有属性****菜单。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33627696759835)
6. 该下拉列表包含有关该事件的所有变量的信息。通过单击任何行项目，您可以自动将其复制到剪贴板，从而可以轻松地将事件变量添加到消息中。 ### 电子邮件

要在流电子邮件中添加事件变量：

1. 在流程编辑器中打开电子邮件。 2. 在“**模板**”旁边，单击“****编辑****”。 3. 单击 ****预览和测试****。 4. 从“**事件属性**”菜单中单击属性名称进行复制。 ![用户在 Klaviyo 中复制事件变量](https://klaviyo.zendesk.com/hc/article_attachments/28713327618715)
5. 将标签粘贴到您的流程电子邮件中。 此预览窗口将显示该特定事件指标的所有可用数据。列表条目从 0 开始编号。例如，如果 **{{ event.extra.line\_items.0.product.name }}** 是产品的变量条目，则 0 表示它是数组中的第一项。要使用事件变量，您必须准确复制它们。事件变量区分大小写，与预览窗口中的显示方式稍有偏差都可能导致变量不起作用。 ## 事件变量的常见示例

不同事件变量的语法取决于积分和事件指标。通过滚动预览窗口并单击不同的条目，您可以查看给定事件的所有可用变量的语法。下面列出了 **开始结帐** 事件的一些常见变量集成示例。请记住，确切的变量可能会有所不同，具体取决于用于触发流的指标。 |  |  |
| --- | --- |
| ****BigCommerce**** | |
| ****产品名称/标题**** | {{ event.extra.line\_items.0.product.name }} |
| ****产品网址**** | {{ event.extra.items.0.product.url }} |
| ****图片**** | {{ event.extra.items.0.product.images.0.src }} |
| ****产品价格**** | {{ event.extra.line\_items.0.product.price } |
| ****数量**** | {{ event.extra.line\_items.0.quantity }} |
| ****总计**** | {{ event.extra.total\_inc\_tax }} |

|  |  |  |
| --- | --- | --- |
|  | ****Magento 1**** | ****Magento 2**** |
| ****产品名称/标题**** | {{ event.extra.line\_items.0.product.name }} | {{ event.extra.line\_items.0.product.name }} |
| ****产品网址**** | {{ event.extra.line\_items.0.product.key }} | {{ event.Items.0.Product.FullURL }} |
| ****图片**** | {{ event.extra.line\_items.0.product.images.0.url }} | {{ event.extra.line\_items.0.product.images.0.url }} |
| ****产品价格**** | {{ event.extra.items.0.base\_original\_price }} | {{ event.extra.line\_items.0.product.price }} |
| ****数量**** | {{ event.extra.line\_items.0.quantity }} | {{ event.extra.line\_items.0.quantity }} |
| ****总计**** | {{ event.extra.base\_grand\_total }} | {{ event.extra.base\_grand\_total }} |

|  |  |
| --- | --- |
| ****Shopify**** | |
| ****产品名称/标题**** | {{ event.extra.line\_items.0.product.title }} |
| ****产品手柄**** | {{ event.extra.line\_items.0.product.handle }} |
| ****图片**** | {{ event.extra.line\_items.0.product.images.0.src }} |
| ****产品价格**** | {{ event.extra.line\_items.0.line\_price }} |
| ****数量**** | {{ event.extra.line\_items.0.quantity }} |
| ****总计**** | {{ event.extra.customer.total\_spent }} |
| ****商店货币（商店的基础货币）**** | {{ 事件|查找：'$currency\_code' }} |
| ****出示货币（客户使用的货币）**** | {{ event.extra.presentment\_currency }} |

|  |  |
| --- | --- |
| ****WooCommerce\***** | |
| ****产品名称/标题**** | {{ event.extra.Items.0.Name }} |
| ****产品网址**** | {{ event.extra.Items.0.URL }} |
| ****图片**** | {{ event.extra.Items.0.Images.0.URL }} |
| ****产品价格**** | {{ event.extra.Items.0.LineTotal }} |
| ****数量**** | {{ event.extra.Items.0.Quantity }} |
| ****总计**** | {{ event.extra.Items.0.TotalWithTax }} |

\*您可以使用参数“?wck_rebuild_cart={{ event.extra.CartRebuildKey }}”[从 WooCommerce 中废弃的购物车流重建购物车](https://help.klaviyo.com/hc/en-us/articles/115005255808#rebuilding-carts-from-an-abandoned-cart-flow7)。购物车重建也可用于 Shopify 和 Magento 1 集成，但在默认的废弃购物车流程中预先生成。 ## 事件变量数组（仅限电子邮件）

如果将上面的变量添加到电子邮件中，您可以提取购物车中第一个商品的动态数据。这类似于走到一排人面前询问第一个人的名字。如果只能有一个项目，则此方法效果很好；然而，对于多个项目或者当您不知道有人可能添加多少项目时，这非常耗时。理想情况下，您希望使用单个命令立即获取组内项目的所有事件变量 - 就像能够喊出“姓名”并获取一长串中每个人的名字。当涉及事件变量列表时，数组可以让您做到这一点。当一个总括属性下有多个条目（如订单中的多个项目）时，就会出现数组。 如上所述，第一项将在中间或末尾有一个“0”，下一项将有一个“1”，依此类推。使用数组，您可以捕获有关总括属性（例如，**Items** 或 **Collections）** 以及该属性下的各个条目的信息。在下面的示例中，**已下订单** 事件的预览中有三个项目：

- “甜馅饼”项目的变量是 **{{ event.Items.0 }}**
- “Runts”项目的变量是 **{{ event.Items.1 }}**
- “Nerds”项目的变量是 **{{ event.Items.2 }}**

对于本示例，这些项目的事件变量数组是 **event.Items**。 ![Klaviyo 中基本下单事件的数据](https://klaviyo.zendesk.com/hc/article_attachments/28713327622811)

## 迭代动态事件变量（仅限电子邮件）

有两种不同的方法可以迭代电子邮件中的这些或其他事件变量数组：

1. ****[内容重复功能](https://help.klaviyo.com/hc/en-us/articles/115005083467)****
   此功能允许您添加单个块（文本、图像等），该块将自动重复并迭代属性数组中的所有条目。 2. ****[动态表](https://help.klaviyo.com/hc/en-us/articles/360032871031)****
   这可以帮助您创建一个更复杂的块，循环遍历单个变量数组的所有条目。请注意，虽然您可以将动态事件变量添加到文本消息中，但不能迭代多个事件变量。 ## 其他资源

- 了解有关使用[消息个性化]的更多信息(https://help.klaviyo.com/hc/en-us/articles/115005084927)
- 了解如何在彩信中包含[动态图像](https://help.klaviyo.com/hc/en-us/articles/1260806102230)
- 了解如何迭代事件数组：
  - [如何根据动态数据重复块](https://help.klaviyo.com/hc/en-us/articles/115005083467)
  - [如何在流电子邮件中构建动态块](https://help.klaviyo.com/hc/en-us/articles/360032871031)