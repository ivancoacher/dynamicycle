---
id: "115005081687"
title: "如何与 Zoho 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005081687-How-to-integrate-with-Zoho"
section: "Zoho"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "zh"
---
## 你将会学到

了解如何将 Klaviyo 与 Zoho 的 CRM 服务集成。完成这些步骤后，您将能够使用 Zoho 中潜在客户的自定义属性数据来个性化 Klaviyo 中的消息。 ## 开始之前

请注意，Klaviyo 的 Zoho 集成仅同步 Zoho 潜在客户，而不同步 Zoho 联系人/客户。 ## 添加 Zoho 集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 单击****探索应用程序****，搜索 **Zoho**，然后单击该卡。然后，单击****安装****。 3. 单击****连接到 Zoho****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28713333871131)
4. 如果需要，登录 Zoho，选择您要连接的组织，并接受权限。 5. 返回 Klaviyo，从下拉列表中选择您的 Zoho CRM 时区。这必须与您的 Zoho 账户处于同一时区。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28713333873947)
6. 通过选中该框并输入以逗号分隔的列表，添加您想要从 Zoho 同步的任何其他字段。确保逗号之间没有空格。 - **字段 API 名称**输入必须使用 Zoho 中字段的 API 名称。单击 Zoho 帐户右上角的齿轮找到 API 字段名称。然后，在 **Developer Space** 下，选择 ****APIs > API Names。**** 单击 ****Leads**** 查看字段名称及其相应的 API 名称。 ![Zoho 中的 API 名称列表，包括字段标签和数据类型](https://klaviyo.zendesk.com/hc/article_attachments/28713328255515)
7. 完成后，单击****完成设置****。 ## 监控 Zoho 同步并验证数据

至少需要十五分钟才能完成 Zoho 同步。完成初始集成设置后，您的 Zoho 会每小时与 Klaviyo 同步一次数据。一旦您将 Zoho 与 Klaviyo 集成并同步，您的所有 Zoho 潜在客户都将使用默认客户属性以及您在集成设置中设置的任何可选字段导入到 Klaviyo。要验证这一点，请使用 **潜在客户状态** 属性创建 Zoho 潜在客户的分段。这将对您帐户中从 Zoho 导入或使用 Zoho 数据更新的所有配置文件进行分组。 1. 在 Klaviyo 中，导航至****受众 > 列表和细分****。 2. 单击****创建列表/细分****并选择****细分****
3. 为您的分段指定一个描述性名称和您想要的任何标签
4. 将分段定义设置为：****有关某人的属性 > 潜在客户状态 > 已设置****。 ![潜在客户状态是在 Klaviyo 细分构建器中使用创建蓝色背景细分来设置细分的](https://klaviyo.zendesk.com/hc/article_attachments/28713333864987)
5. 单击****创建段****。 6. 将此细分中的人员与您的 Zoho 帐户中的潜在客户进行比较；列表应该匹配。 ## Zoho 指标

与其他集成不同，Zoho 没有可见的指标，但 Klaviyo 会同步每个 Zoho 潜在客户的以下信息：

- 电子邮件
- 名字
- 姓氏
- 公司
- 电话
- 城市
- 状态
- 邮政编码
- 国家
- 潜在客户状态
- 电子邮件选择退出

![Klaviyo 中个人资料的联系人、渠道和信息部分，客户财产潜在客户状态设置为丢失潜在客户](https://klaviyo.zendesk.com/hc/article_attachments/28713333862427)

此信息可在从 Zoho 同步的每个 Klaviyo 配置文件中查看。要一次性查看所有 Zoho 潜在客户，您可以使用上面讨论的 **潜在客户状态** 分段。 ## 更新我们的新 Zoho 集成

您的 Zoho 集成有问题吗？您可能正在使用我们已弃用的旧集成。 Klaviyo 发布了新的 Zoho 集成，以提高安全性和稳定性。要更新到新集成，您需要使用 Zoho 重新验证 Klaviyo：

1. 在 Klaviyo 中，单击****集成****选项卡。 2. 从启用的集成列表中选择 ****Zoho****。 3. 在右上角，单击****管理集成****。 4. 选择****重新验证****。 5. 单击 Zoho 权限页面上的****接受****。您的集成现已更新。虽然没有必要，但您可能希望从 Zoho 中的**连接的应用程序**中删除已弃用的 Klaviyo 应用程序。为此，请遵循 [Zoho 关于撤销 OAuth 令牌的指南](https://www.zoho.com/accounts/protocol/oauth/revoke-refresh-token.html)。 ## 结果

您现在已与 Zoho 集成并查看了您的同步数据。 ## 其他资源

- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [分段入门](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [了解 Klaviyo 和应用程序之间交换的数据类型](https://help.klaviyo.com/hc/en-us/articles/360030696012)