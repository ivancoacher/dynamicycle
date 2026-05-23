---
id: "115005081447"
title: "如何与 Olark 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005081447-How-to-integrate-with-Olark"
section: "Olark"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "zh"
---
## 你将会学到

了解如何将实时聊天提供商 Olark 与 Klaviyo 集成，以便在聊天对话结束后自动将聊天活动同步到您的 Klaviyo 帐户。 Klaviyo 通过您的 Olark 帐户中配置的 Webhook 接收来自 Olark 的数据。要启用集成，您首先需要从 Klaviyo 获取 Webhook 端点 URL，您将其添加到您的 Olark 帐户以完成集成。 ## 从 Klaviyo 获取 webhook 端点

1. 在您的 Klaviyo 帐户中，选择****集成****选项卡。 2. 选择****探索应用程序****，搜索**Olark**，然后单击该卡。然后，单击****安装****。 3. 单击****连接到Olark****。 4. 复制提供的 Webhook 端点 URL 并确保其安全，以便在本指南的下一部分中使用。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717810667547)
5. 如果您希望将特定聊天同步到 Klaviyo，请选中选项**仅与特定 Olark 群组中的访问者同步聊天**。然后，添加您想要同步到 Klaviyo 的组的名称，并用逗号分隔。您可以在第一次开始时利用此功能，也可以稍后返回并调整集成设置。 6. 完成后，单击****完成设置****。 ## 在 Olark 中设置 webhook

1. 登录 Olark 并导航至****集成****页面。 2. 在页面顶部的搜索框中输入“Webhooks”，然后在出现时单击****Webhooks****。 ![Olark 中的集成页面，搜索栏中包含 web，搜索结果中包含 Webhooks](https://klaviyo.zendesk.com/hc/article_attachments/28717850261659)
3. 在 **要发布到的 URL** 下的框中，粘贴您之前从 Klaviyo 复制的 Webhook 端点 URL。 ![在 Olark 中连接一个 Webhook 框，其中包含要发布到框的 URL、其他设置，并以蓝色背景保存](https://klaviyo.zendesk.com/hc/article_attachments/28717810654875)
4. 如果需要，您可以选择在 webhook URL 框下添加任何选项。 5. 单击****保存****。 6. 如果 Webhook 连接成功，您将看到一个绿色框，其中包含文本“**设置已成功保存！**”以及用于测试新连接的选项。 ![在 Olark 中连接 Webhook 框，带有绿色“设置已成功保存”横幅和蓝色“已连接”横幅，并发送白色背景文本](https://klaviyo.zendesk.com/hc/article_attachments/28717810646427)
7. 如果 webhook 连接不成功，请查看 Olark [Webhooks 集成指南](https://www.olark.com/help/webhooks) 获取更多帮助。 8. 单击 ****发送测试**** Helvetica、Arial、sans-serif;"> 确保您的端点配置正确。如果测试成功，您将看到一个带有笑脸的绿色框和文本 **测试已发送**。![在 Olark 中连接一个带有笑脸的绿色已发送测试横幅的 Webhook 框脸](https://klaviyo.zendesk.com/hc/article_attachments/28717810650011)

## Klaviyo 中的 Olark 数据

当 Olark 聊天结束时，Klaviyo 将自动记录聊天对象以及您在该聊天中设置的任何自定义属性。如果聊天是匿名的，Klaviyo 将不会存储任何聊天数据。 Klaviyo 中跟踪了一项 Olark 指标：**在网站上聊天**。导航到 Klaviyo 中的 ****Metrics**** 选项卡（在 ****Analytics**** 下）下拉列表中，您可以通过过滤到 **Chatted on Website** 事件来查看和过滤所有记录的事件。 ![Klaviyo 中的“指标”选项卡由 Olark 过滤，并在列表中的网站上聊天](https://klaviyo.zendesk.com/hc/article_attachments/28717810659611)

作为**网站聊天**指标的一部分，Klaviyo 自动接收有关客户的以下信息（如果有）：

- 电子邮件
- 名字
- 姓氏
- 组织
- 电话号码
- 城市
- 地区
- 国家

您可以展开事件以查看“发件人”字段以及聊天消息。如果没有可用的位置信息，Klaviyo 将自动使用 IP 地理定位来确定客户所在的位置。 Klaviyo 还记录您可能为客户设置的任何自定义属性。 ![网站聊天事件的 Klaviyo 活动源显示了 Natalie 的一个带有时间戳的事件](https://klaviyo.zendesk.com/hc/article_attachments/28717810662555)

## 结果

您已将 Olark 与 Klaviyo 集成，现在新的 Olark 聊天将在 Klaviyo 中实时跟踪。 ## 其他资源

- [了解 Klaviyo 和应用程序之间交换的信息类型](https://help.klaviyo.com/hc/en-us/articles/360030696012)
- [了解 Klaviyo 和应用程序之间如何交换信息](https://klaviyo.zendesk.com/hc/en-us/articles/360030265051)