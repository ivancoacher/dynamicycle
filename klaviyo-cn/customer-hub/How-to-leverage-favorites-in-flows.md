---
id: "36998789661595"
title: "如何利用流中的收藏夹"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/36998789661595-How-to-leverage-favorites-in-flows"
section: "Build and use Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:53Z"
language: "zh"
---
了解如何使用流程自动向购物者发送电子邮件，告知他们在您网站上收藏的商品。无论您是发送专门的收藏提醒还是过滤现有流程（例如降价警报）以优先考虑喜欢产品的客户，这些自动消息都会通过在适当的时刻接触最感兴趣的购物者来推动转化。 Shopify 客户中心目前支持标准店面和 Shopify Headless。对于 WooCommerce，请导航至 https://help.klaviyo.com/hc/en-us/articles/47792369863451

有关客户中心功能的反馈，请发送电子邮件至 customerhub@klaviyo.com。 ## 开始之前

要设置收藏夹提醒流程，您必须：

1. 在您的网站上启用[客户中心](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675)。 2. 在 Klaviyo 中启用[**收藏夹**功能](https://klaviyo.zendesk.com/hc/en-us/articles/33660543083419)。 ## 按流触发器中的收藏夹状态过滤

对于具有基于产品的触发器（例如降价）的流程，您现在可以根据客户是否喜欢该商品来过滤进入流程的条目，无需额外的流程过滤器或解决方法。在触发器设置下，滚动到****按收藏夹过滤****部分并选择以下选项之一：

- ****所有客户**** — 任何满足触发条件的客户都会进入流程，无论收藏状态如何
- ****Only if favorited**** — 只有收藏该商品的顾客才会进入流程
- ****仅在未收藏时**** — 只有**未**收藏该商品的客户才会进入流程

这对于降价流程特别有用：通过选择****仅在收藏时****，您可以确保降价警报专门发送给对该产品表示最强烈兴趣的客户，从而使消息更加相关和及时。 ![屏幕截图 2026-02-19 9.36.58AM.png](https://klaviyo.zendesk.com/hc/article_attachments/48619956991515)

## 关于 Klaviyo 的收藏夹提醒流程

在网站上安装收藏夹后，请使用 Klaviyo 流程提醒并鼓励购物者重新访问他们保存的商品。 Klaviyo 的流程库中提供了预构建的收藏夹提醒流程，标题为：**客户中心收藏夹提醒**。 ![favflow0.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006292191771)

此流程触发**客户中心添加到收藏夹**指标，该指标记录购物者何时单击商品上的收藏夹按钮。每个收藏的项目都会记录为单独的事件。但是，购物者每次购物会话只会收到 1 封提醒电子邮件，即使他们喜欢多个商品。该电子邮件最多显示该会话中最近收藏的 3 个项目。默认情况下，**客户中心收藏夹提醒**流程应用以下配置文件过滤器：

- **过去 1 天内没有处于流动状态**
- **客户中心收藏夹至少有 1 件**

这些过滤器使用 AND 逻辑，这意味着必须满足这两个条件，配置文件才有资格进入流程并接收电子邮件。 [了解有关配置文件过滤器的更多信息](https://help.klaviyo.com/hc/en-us/articles/115002779051#h_01HDAFKRKRJ7N44M7NWEQRSANP)。 ## 创建收藏夹提醒流程

1. 在 Klaviyo 中，导航至****Flows**** 选项卡。 2. 单击****创建流程****。 3. 搜索“收藏夹”，然后选择****客户中心收藏夹提醒****流程模板。 ![favflow.5.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006297282843)
4. 单击****使用模板****。 ![favflow2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006297285787)
5. 可选：根据需要调整时间延迟和消息传递。单击画布中的任意一个进行编辑。 - 默认的预构建流程在浏览会话一天后发送一封电子邮件，其中至少有一个项目已添加到收藏夹。电子邮件模板会自动提取您建立的客户中心样式，并预先配置为显示购物者在该会话中最近喜欢的商品。如果调整流中的时间延迟，您还应该调整配置文件过滤器上的时间范围，以确保维持消息之间的预期延迟。默认情况下，两者都设置为 1 天的延迟。 ![favflow3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006297286043)
6. 单击右上角的****查看并打开****。 7. 从下拉列表中选择****实时****。 8. 单击****保存****。 流程上线后，符合条件的购物者会自动输入您的流程以接收收藏夹提醒电子邮件。 ![favflow.jpg](https://klaviyo.zendesk.com/hc/article_attachments/37006297286171)

当收件人单击电子邮件中的“查看收藏夹”按钮时，他们将被引导回您的网站，同时打开客户中心界面并显示他们收藏的商品，从而简化了购买路径。 ## 其他资源

- [如何在您的网站和客户中心显示收藏夹按钮](https://klaviyo.zendesk.com/hc/en-us/articles/33660543083419)
- [如何为客户中心启用产品推荐](https://klaviyo.zendesk.com/hc/en-us/articles/33660504643867)
- [如何为客户中心创建内容块](https://klaviyo.zendesk.com/hc/en-us/articles/33660517680795)