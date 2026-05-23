---
id: "11117215837211"
title: "开始使用 Square"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/11117215837211-Getting-started-with-Square"
section: "Square"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:10Z"
language: "zh"
---
## 你将会学到

了解如何轻松地将 Klaviyo 与您的 Square Online 网站集成，以便将客户资料、订单和目录信息以及来自 Square 销售点 (POS) 的订单数据同步到 Klaviyo。有了这些数据，您将能够通过细分、自动化流程和营销活动，通过有针对性的消息传递来吸引客户。 ## 开始之前

当您将 Square 与 Klaviyo 集成时，只有 1 个 Square 帐户可以连接到您的 Klaviyo 帐户。如果您有多个 Square 帐户，则需要将每个帐户与单独的 Klaviyo 帐户集成。如果存在与客户直接与您的公司共享的订单关联的电子邮件地址和/或电话号码，Square POS 订单事件将同步到 Klaviyo（并将创建配置文件）。 Square 事件将有一个名为 **source name** 的属性，该属性将显示该事件是来自 POS 还是来自在线/网络，以便您可以[在 Klaviyo 中对这些事件进行分段](https://help.klaviyo.com/hc/en-us/articles/115005237908-Getting-started-with-segments)。 ## 集成视频

请观看我们有关与 Square 集成的分步视频。 ![](https://fast.wistia.com/embed/medias/5qlt7jxxy1/swatch)

## 如何与 Square 集成

1. 在您的 Klaviyo 帐户中，选择左侧导航栏中的****集成****。 2. 选择****探索应用程序****，搜索**Square**，然后单击该卡。然后，单击****安装****。 3. 在框中输入您的商店 URL，然后单击****连接到 Square****。 ![截图 2025-09-23 8.10.01 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/41382239155099)
4. 您将被带到您的 Square 帐户并提示您登录（如果您当前尚未登录）。 5. 登录后，检查权限并单击****允许****以带回 Klaviyo。 6. 检查您的商店 URL 设置，确保您选择了正确的 Square 帐户来与 Klaviyo 集成。 ![组 5.png](https://klaviyo.zendesk.com/hc/article_attachments/41382239156891)
7、默认勾选**自动添加Klaviyo现场JavaScript**设置；如果您想启用 Klaviyo 的 **Active on Site** 跟踪和注册表单，请将其保留为选中状态。 8. 单击****完成设置****。 9. 加载屏幕后，您应该会看到一条成功消息：**您的 Square 帐户现已连接到 Klaviyo！**

   ![截图 2025-09-23 8.11.28 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/41382239158427)

   您已完成集成，您的历史 Square 数据将开始同步到 Klaviyo。 Square Online 中的任何新活动都将开始实时同步到 Klaviyo，Square POS 中的活动将每 30 分钟同步一次。如果您需要编辑 Square 设置：
10. 在您的 Klaviyo 帐户中，选择****集成****选项卡。 11. 在列表中选择****方形****。 12. 您将进入集成设置页面，您可以在其中进行更改。 13. 单击****保存****。 ## 数据从 Square 同步到 Klaviyo

要检查从 Square 到 Klaviyo 的数据同步：

1. 在您的 Klaviyo 帐户中，选择****集成****选项卡。 2. 在列表中选择****方形****。 3. 选择顶部的****数据****选项卡。在这里，您将看到从 Square 同步到 Klaviyo 的最新数据，以及历史数据同步的同步进度条。 ![Klaviyo 中的数据页面显示 Square 的最新数据以及重新导入的选项。](https://klaviyo.zendesk.com/hc/article_attachments/34458041320987)

如果您在同步过程中遇到问题，请在此处选择****重新导入****以重新启动历史数据同步。从 Square 同步到 Klaviyo 的数据包括：

- [已知网站访问者](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Onsite-Tracking#who-klaviyo-tracks5) 被跟踪为 **Active on Site** 事件（如果您选中了现场 JavaScript 设置）
- 电子邮件退订
- 与订单事件相关的个人资料信息
- 您的 Square 目录（包括仅限 POS 的商品）
- 以下订单事件：
  - 放弃结账
  - 已下订单
  - 订购的产品
  - 已退款的订单
  - 取消订单
  - 已履行的订单
  - 已履行部分订单

Square 事件将有一个名为 **source name** 的属性，该属性将显示该事件是来自 POS 还是来自在线/网络，以便您可以[在 Klaviyo 中对这些事件进行分段](https://help.klaviyo.com/hc/en-us/articles/115005237908-Getting-started-with-segments)。 有关与 Square 同步的每个事件相关的属性的更多信息，请查看我们的文章 [Square 数据参考](https://help.klaviyo.com/hc/en-us/articles/11117271030555)。 ## 为您的 Square 网站创建 Klaviyo 注册表单

了解如何[创建 Klaviyo 注册表单](https://help.klaviyo.com/hc/en-us/articles/360026474752-Getting-started-with-sign-up-forms) 以收集 Square 网站上的电子邮件和短信订阅者。一旦发布，这些表单将自动显示在您的网站上，前提是您在集成时选中了 **自动添加 Klaviyo 现场 JavaScript** 设置。您可以创建以下类型的 Klaviyo 表单：

- 弹出窗口
- 弹出窗口
- 整页
- 嵌入（[请务必遵循我们的指南，将嵌入表单添加到 Square 网站](https://help.klaviyo.com/hc/en-us/articles/18229698831003)）

## 使用 Square 数据创建自动消息传递

Klaviyo 的流程库中有许多针对 Square 的预构建流程，您可以使用它们来个性化客户消息传递。要访问这些流：

1. 在 Klaviyo 中选择****Flows**** 选项卡。 2. 单击右上角的****浏览想法****，或者如果这不是您的第一个流程，则单击****创建****。 3. 从搜索栏旁边的过滤器下拉列表中选择****Square****。这些预先构建的流程包括：

- 放弃结账
- 赢回客户
- 发货确认
- 补货提醒
- 重复购买培育
- 废弃购物车提醒
- 顾客谢谢
- 赢回客户
- 产品评论/交叉销售
- 废弃购物车提醒；高价值购物车与低价值购物车
- 标记首次购买日期
- 购买后反弹
- 延迟履行
- 已履行部分订单
- 订单确认

## 结果

您已将 Square 与 Klaviyo 集成并验证了您的同步数据。现在，您可以根据 Square 同步的数据创建自动流消息、个性化营销活动、细分列表等。