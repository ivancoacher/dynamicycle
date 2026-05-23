---
id: "115005252888"
title: "如何与 Eventbrite 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005252888-How-to-integrate-with-Eventbrite"
section: "Eventbrite"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: "zh"
---
## 你将会学到

了解如何将 Eventbrite 与 Klaviyo 集成。完成这些步骤后，您将能够根据购票活动个性化和定位电子邮件。 Klaviyo 将为每次购买同步“已购买门票”事件，并自动同步与购买以及下订单的个人相关的所有详细信息。 ## 启用 Eventbrite 集成

Eventbrite 集成使用网络钩子，这将在 Eventbrite 和您的 Klaviyo 帐户之间创建实时数据交换。首先，您将 Eventbrite 与 Klaviyo 连接。然后，您将指定一个组织，以便为您的集成创建适当的 Webhook。 1. 在 Klaviyo 中，选择****集成****选项卡。 2. 单击****探索应用程序****，搜索**Eventbrite**，然后单击该卡。然后，单击****安装****。 3. 单击****连接到Eventbrite****。您将被重定向到 Eventbrite 登录页面，如果您尚未登录，则需要在该页面登录您的 Eventbrite 帐户。![](https://klaviyo.zendesk.com/hc/article_attachments/28711676294299)
4. 系统将提示您允许 Klaviyo 访问您的 Eventbrite 帐户。在此选择****允许****。 ![屏幕询问是否允许 Klaviyo by Klaviyo 访问您的 Eventbrite 帐户？允许橙色背景，拒绝白色背景](https://klaviyo.zendesk.com/hc/article_attachments/28711676282139)
5. 然后，您将被带回Klaviyo完成整合。确认您的用户名正确，然后选择您的组织以与 Klaviyo 同步。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711676298779)
6. 单击****完成设置****。然后您应该会收到一条成功消息。 ## 监控您的 Eventbrite 同步

启用 Klaviyo 的内置 Eventbrite 集成后，会发生 2 件事：

- Klaviyo 将运行一次性历史同步，将所有过去的 Eventbrite **已购买门票** 指标拉入您的 Klaviyo 帐户。 - Klaviyo 还将开始通过 Eventbrite webhooks 实时同步新的 Eventbrite 指标。您应该会看到历史 Eventbrite **已购买门票** 数据填充您的帐户，并开始看到新订单事件跟踪实时数据。要检查您的 Eventbrite 集成：

1. 单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****选项卡。 2. 单击显示的 Eventbrite 指标之一以验证数据是否按预期填充。例如，单击****已购买的票******** 指标。 3. 如果您看到购买活动，您所需要做的就是等待初始历史 Eventbrite 集成同步完成；此过程可能需要几个小时，具体取决于您帐户中的历史数据量。您可以通过监控仪表板活动源来观察新订单事件的流入。 ![Eventbrite 在 Klaviyo 购买门票活动源，买家姓名经过审查](https://klaviyo.zendesk.com/hc/article_attachments/28711676285979)

## 从 Eventbrite 同步的事件

这些是从 Eventbrite 集成同步的事件指标：

- ****购买门票****当有人在 Eventbrite 中购买活动门票时。 - ****签到****当有人签到事件时，通常是在事件发生时。 - ****签出****当有人签出活动时。 - ****退款门票****当活动取消且门票退款给客户时。 - ****更新门票****当已购买的门票被更新时。例如，可以在客户的票证上更新票证上的数量或信息。 ## 已买票指标

Klaviyo 将为每次购买同步“已购买门票”事件，并自动同步与购买相关的所有详细信息以及下订单的个人：

### 客户数据

Klaviyo 将为每位购票者同步以下信息：

- 名字
- 姓氏
- 电子邮件地址

### 订单数据

Klaviyo 会将以下信息与每个订单同步（如果有）：

- 总价值
- 活动名称
- 活动说明
- 门票类型
- 门票说明
- 票证 ID
- 出席人数
- 与会者 ID

![Klaviyo 活动源中的单次购买门票指标显示事件详细信息，例如名称、价值等](https://klaviyo.zendesk.com/hc/article_attachments/28711697751963)

## 更新我们新的 Eventbrite 集成

您的 Eventbrite 集成有问题吗？您可能正在使用我们已弃用的旧集成。 Klaviyo 发布了新的 Eventbrite 集成，以提高安全性和稳定性。 要更新到新集成，您需要使用 Eventbrite 重新验证 Klaviyo：

1. 在 Klaviyo 中，单击****集成****选项卡。 2. 从启用的集成列表中选择****Eventbrite****。 3. 在右上角，单击****管理集成****。 4. 选择****重新验证****。 5. 单击 Eventbrite 权限页面上的****接受****。您的集成现已更新。 ## 结果

您现在已与 Eventbrite 集成并查看了您的同步数据。 ## 其他资源

- [集成常见问题解答参考](https://help.klaviyo.com/hc/en-us/articles/115005081007)