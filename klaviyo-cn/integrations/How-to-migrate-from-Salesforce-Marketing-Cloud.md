---
id: "115000267471"
title: "如何从 Salesforce Marketing Cloud 迁移"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115000267471-How-to-migrate-from-Salesforce-Marketing-Cloud"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T10:57:41Z"
language: "zh"
---
## 你将会学到

了解如何将 Salesforce Marketing Cloud（以前称为 ExactTarget）与 Klaviyo 集成。此集成旨在帮助您从 Salesforce Marketing Cloud 迁移到 Klaviyo。我们不建议同时使用这两个平台，除非在您进行切换的过渡期间。

## 开始之前

请务必查阅我们的[一般清单](https://klaviyo.zendesk.com/hc/en-us/articles/115005082767)，其中介绍了如何从不同的电子邮件服务提供商 (ESP) 完全迁移到 Klaviyo。

您在集成时使用的 Salesforce Marketing Cloud 用户应该有权访问 Web 服务。了解如何[查找 WSDL 链接。](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/wsdl-endpoint-links.html)

## 添加 Salesforce Marketing Cloud 集成

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 在下一页上，选择****探索应用程序****并搜索 **Salesforce Marketing Cloud**。然后，单击该卡。
3. 单击****安装****。
4. 在下一页上，提供用于登录 Salesforce Marketing Cloud 的用户名和密码，以及用于连接到 Salesforce Marketing Cloud 实例的 SOAP API 的 WSDL 链接。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28716328059163)
5. 单击****连接到 Salesforce Marketing Cloud****。
6. 在下一页的 **高级** 下，您可以选择 1) 从您的营销活动收集打开和点击数据（强烈推荐）和 2) 仅同步特定列表，这将允许您选择要从 Salesforce Marketing Cloud 同步的特定列表。
   - 如果您同时选中两个复选框，Klaviyo 将同步所有营销活动数据，无论营销活动是否发送到指定列表。此外，Klaviyo 随后将为打开和/或点击这些活动的所有人员创建个人资料，无论他们是否在指定列表中。
7. 完成后，单击****完成设置。**** 您的集成现在应该已启用。

## 监控 Klaviyo 同步

要检查启用的集成，请单击 Klaviyo 中的****受众****下拉列表，然后选择****列表和细分****选项卡。

在这里，您应该开始看到您的 Salesforce Marketing Cloud 列表填充在 Klaviyo 中。这些列表将与 Salesforce Marketing Cloud 列表中的订阅者同步。

Klaviyo 从 Salesforce Marketing Cloud 接收过去 180 天的历史参与数据。新数据每 5 分钟同步到 Klaviyo。

以下指标将与 Klaviyo 同步：

- 单击电子邮件
- 打开电子邮件
- 收到电子邮件

如果您在 Klaviyo 中选择****分析****下拉列表，然后选择****指标****，您将能够查看这些指标。

![Klaviyo 中的“指标”选项卡由 Salesforce Marketing Cloud 过滤，列表中包含“单击的电子邮件”、“打开的电子邮件”和“已接收的电子邮件”](https://klaviyo.zendesk.com/hc/article_attachments/28716328052763)

如果配置文件在 Salesforce Marketing Cloud 中处于非活动状态，则该配置文件将在 Klaviyo 中全局禁止。非活动状态包括“已退回”、“已保留”、“取消订阅”和“已删除”。

## 最佳实践

您可以使用上述参与度指标来细分 Klaviyo 中的 Salesforce Marketing Cloud 列表。这将保护您的送达率，并确保您通过专门向想要接收您的电子邮件的联系人发送邮件来开始良好的开端。

首先，建立一个订阅者的参与部分：

- 在过去 30 天内至少打开过一次电子邮件 (ExactTarget) 或
- 在过去 30 天内至少点击过一次电子邮件 (ExactTarget)

![使用 ExactTarget 事件在 Klaviyo 细分构建器中吸引订阅者细分](https://klaviyo.zendesk.com/hc/article_attachments/28716300671387)

如果您是每日发送者，则应将第一周的营销活动发送至此细分受众群。如果您是每两周发送一次的发送者，则应将前 2-3 个营销活动发送到此细分受众群。有关更多信息，请参阅我们关于[如何创建参与细分]的文章(https://help.klaviyo.com/hc/en-us/articles/115000200072)。

## 结果

您现在已将 Salesforce Marketing Cloud 与 Klaviyo 集成、验证同步数据并查看最佳实践。

## 其他资源

- [分段入门](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [了解电子邮件送达率](https://help.klaviyo.com/hc/en-us/articles/115005247008)