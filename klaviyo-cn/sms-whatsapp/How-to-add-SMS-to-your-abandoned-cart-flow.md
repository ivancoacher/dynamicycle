---
id: "9352115400219"
title: "如何将短信添加到废弃的购物车流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/9352115400219-How-to-add-SMS-to-your-abandoned-cart-flow"
section: "Set up your first SMS flows "
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:06Z"
language: "zh"
---
## 你将会学到

了解如何将短信添加到废弃购物车流程以及合规性要求和最佳实践。 ## 开始之前

请注意，强烈建议使用安静时间来发送短信废弃购物车提醒。默认情况下，Klaviyo 中的短信功能处于打开状态，我们不建议将其关闭。美国对任何在废弃购物车流中发送短信的人有一定的要求。如果您要发送给美国收件人，则需要满足以下条件：

- 收集短信同意时使用双重选择加入。 - 每个收件人仅发送 1 条短信。 - 在有人放弃购物车后 48 小时内发送。 ## 创建短信废弃购物车流程

在这里，我们将引导您了解如何将短信添加到现有的废弃购物车流程中。在设置 SMS 废弃购物车流程之前，请阅读开始之前部分，因为它包含有关 SMS 合规性和最佳实践的重要信息。 ****还没有废弃的购物车流程吗？打开此部分。****

1. 导航至****流****。 2. 单击右上角的****浏览创意****。 3. 搜索“废弃购物车”，然后单击电子邮件和短信图标。 ![使用电子邮件和短信搜索废弃的购物车模板](https://klaviyo.zendesk.com/hc/article_attachments/28722597618843)
4. 选择废弃的购物车流程模板。 1. 在这里，我们选择名为“标准（电子邮件和短信）”的模板。
5. 为流程命名（例如“废弃购物车提醒”）。 ![废弃购物车流程模板的预览，您可以在其中命名流程](https://klaviyo.zendesk.com/hc/article_attachments/28722559225499)
6. 单击****创建流****。 7. 如果您使用 [Amazon Buy with Prime 并将其与 Klaviyo 集成](https://klaviyo.zendesk.com/hc/en-us/articles/14708088221467)，请添加以下流程过滤器以排除通过 Buy with Prime 进行购买的客户收到错误消息：

   - **下订单**（使用 Prime 购买）**自开始此流程以来零次。**
8. 进入每条消息并编辑文本

   1. 动态变量的格式必须完全正确，否则将不起作用。 2. 复制块可以让您进行更改，而不会带来破坏它们的风险。 - 注意：在更改有关动态变量的任何内容之前，请复制变量或变量块。 9. 保存您的更改。 10. 不要关闭短信的安静时段。 11. 单击右上角的****更新操作状态****。 12. 打开下拉菜单并选择****直播****。 13. 单击****更新状态****。 ### 将短信添加到废弃的购物车流程

1. 导航至****流****。 2. 找到要在其中包含 SMS 的废弃购物车流程。 3. 在流程中，在第一个时间延迟后放置条件分割。 1. 注意：延时必须在流量触发后48小时内。 4. 使用以下条件。 **如果某人可以或不能接收营销信息>**人**无法接收>短信营销信息。**
   ![在废弃购物车流中第一次延迟后进行条件分割](https://klaviyo.zendesk.com/hc/article_attachments/28722597626011)
5. 在“否”路径上，添加 SMS 消息。 ![将短信添加到无条件分割的路径](https://klaviyo.zendesk.com/hc/article_attachments/28722559236763)
6. 单击短信卡。 7. 单击详细信息面板中的****编辑****。 8. 添加您的消息。 “嘿 {{ person|lookup:"first\_name"|default:'there' }}，您的购物车即将过期！您想查看一下吗？[LINK]”
9.推荐：包括折扣以鼓励人们购买。 “嘿 {{ person|lookup:"first\_name"|default:'there' }}，您的购物车即将过期！立即使用代码 {% coupon\_code 'YOUR\_COUPON' %} [LINK] 即可享受 10% 的折扣”
   ![包含 10% 优惠券的废弃购物车流程消息示例](https://klaviyo.zendesk.com/hc/article_attachments/28722597622811)
10. 在短信之后到第一封电子邮件之后重新加入拆分。 ![在废弃购物车流程中收到第一封电子邮件和短信后重新加入拆分](https://klaviyo.zendesk.com/hc/article_attachments/28722597634331)
11. 将短信设置为实时。 ![将短信从草稿更改为实时](https://klaviyo.zendesk.com/hc/article_attachments/28722559231515)

## 改善您的短信废弃购物车流程

上面我们详细介绍了基本的短信和电子邮件废弃购物车流程。但是，您可以通过多种方式自定义此流程。虽然您不能向每个收件人发送超过 1 条短信作为废弃购物车提醒，但通过进一步定位受众，您可以在此流程中发送超过 1 条短信。请参阅下面的示例。 ****如果产品不可用，请跳过短信****

- 它使短信保持简短。 - 与电子邮件不同，短信无法动态填充某人放弃的确切数量的项目。因此，短信放弃消息应该只显示某人购物车中的第一个商品。但如果该产品缺货怎么办？ |  |  |
| --- | --- |
| ****格式**** | ****示例**** |
| `{% Catalog event.ProductID unpublished="cancel" %}` 您的消息提醒某人他们废弃的购物车... [链接到产品] `{% endcatalog %}` | `{% Catalog event.ProductID unpublished="cancel" %}` 嗨，朋友！你还想要这个吗？点击立即购买：`{{ event.URL }}` `{% endcatalog %}` |

****价值分割****

![使用触发器拆分向购物车低于 100 美元的用户发送不同的短信](https://klaviyo.zendesk.com/hc/article_attachments/28722559248027)

****产品集合分割****

![使用触发分割向购买特定系列的用户发送不同的短信](https://klaviyo.zendesk.com/hc/article_attachments/28722597641115)

****新购买者与回头客的划分****

![使用条件拆分向新购买者和回头客发送不同的短信](https://klaviyo.zendesk.com/hc/article_attachments/28722597631899)

****频繁购买者分裂****

![使用条件拆分向更频繁的购买者发送不同的短信](https://klaviyo.zendesk.com/hc/article_attachments/28722597655707)

## 其他资源

- 了解有关[废弃购物车流程]的更多信息(https://help.klaviyo.com/hc/en-us/articles/115002779411-)
- 了解如何创建其他短信流：
  - [将短信添加到您的浏览放弃流程](https://help.klaviyo.com/hc/en-us/articles/15806802249883)
  - [将短信添加到您的感谢流程中](https://help.klaviyo.com/hc/en-us/articles/15800790306715)