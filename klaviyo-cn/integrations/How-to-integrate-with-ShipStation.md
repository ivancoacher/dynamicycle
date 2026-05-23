---
id: "360028298592"
title: "如何与 ShipStation 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360028298592-How-to-integrate-with-ShipStation"
section: "ShipStation"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "zh"
---
## 你将会学到

了解如何将 ShipStation 与 Klaviyo 集成。此集成每 30 分钟从 ShipStation 同步订单创建和运输状态数据。完成本文中的步骤后，您将能够根据 ShipStation 跟踪的运输事件和订单状态来个性化和定位电子邮件。 ## 开始之前

此集成使用 ShipStation 的 V1 API，需要 ShipStation 标准版或高级版计划。 ## 在 ShipStation 中创建 API 密钥和密码

要与 Klaviyo 集成，您需要来自 ShipStation 的 API 密钥和机密。您必须使用 ShipStation 的 V1 API 进行集成。 API 密钥和 API 机密仅在生成时才会显示在 ShipStation 的 UI 中，并且仅向生成它们的用户显示。如果您已经生成并保存了 V1 密钥和机密，则可以跳到下一部分。如果没有，请在 ShipStation 中创建它们：

1. 在您的 ShipStation 帐户中，选择齿轮图标以访问您的帐户设置。 2. 选择****帐户 > API 设置****。 3. 从下拉列表中选择****V1 API****，然后单击****生成 API 密钥****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37181395592731)
4. 单击 ShipStation 发送到您的电子邮件地址的验证链接。验证电子邮件后，**生成 API 密钥**按钮将重置。重置后，再次单击****生成 API 密钥****。 5. 设置新 API 密钥的有效期（3、6 或 12 个月），然后单击****生成****。 6. 复制新生成的 API 密钥和密码，并确保安全存储。请注意，一旦密钥过期，您将需要轮换密钥并在 Klaviyo 中更新它。详细了解 [API 密钥生成和轮换] ShipStation](https://help.shipstation.com/hc/en-us/articles/360025856212-ShipStation-AP我#UUID-c3bb4750-8145-1d9c-c8be-e3dd663d2eed_UUID-191ce2ed-16c1-9c98-d1fb-99bbf8bf3c0c)。 ## 将 ShipStation 与 Klaviyo 集成

1. 前往您的 Klaviyo 帐户并选择 ****Integrations**** 选项卡。 2. 单击****探索应用程序****并搜索**ShipStation**，然后单击该卡。 3. 然后，单击****安装****。 4. 输入在 ShipStation 中生成的 API 密钥和 API 密钥，然后单击****连接到 ShipStation****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720892444955)
5. 检查权限并单击****允许****。 6. 如果您的集成成功，您将看到一条成功消息。 ## 监控 Klaviyo 同步

ShipStation 集成会同步所有 ShipStation 商店的数据，允许您根据商店名称过滤段和流，并自动同步最近 90 天的数据。初始集成完成后，每 30 分钟运行一次定期同步，查找状态更新以在 Klaviyo 中创建其他事件。要检查您的集成同步：

1. 单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****。 2. 单击****所有集成****下拉列表，然后选择 ShipStation。 3. 通过查看 ShipStation 指标之一来检查 ShipStation 事件是否正在同步到您的 Klaviyo 帐户。例如，**订单等待发货**。并单击该指标的“活动源”图标。 4. 如果您的集成已开始同步数据，您将开始看到事件被添加到此**活动源**。 Klaviyo 导入您的所有 ShipStation 数据。要验证这一点，请将特定日期添加到 Klaviyo 的已发货订单数量与 ShipStation 中已发货的订单数量进行比较，并确认它们匹配。 1. 在 Klaviyo 中，导航至****分析 > 指标****，然后单击“**订单已发货**”指标。 2. 这将带您进入指标图表页面，默认情况下，该页面将显示最近 30 天的数据。 3. 将鼠标悬停在昨天的数据点上或查看图表下方的数据表，了解昨天发生的付款数量，并将其与您在 ShipStation 中看到的数据进行比较。如果数据不匹配，问题很可能是您的 Klaviyo 帐户中的时区与您的 ShipStation 帐户中的时区不匹配。要检查您在克拉维约的时区设置：

1. 单击左下角您的帐户名称。 2. 选择然后单击****设置 > 组织****。 3. 向下滚动到**时区**。 ## ShipStation 指标

ShipStation 将以下指标同步到 Klaviyo：

- 订单等待发货
- 订单等待付款
- 订单暂停
- 订单已发货
- 订单已取消

![mceclip0.png](https://klaviyo.zendesk.com/hc/article_attachments/28720892442907)

有关 ShipStation 中跟踪的特定订单状态的更多信息，请查看 [ShipStation 的文档](https://help.shipstation.com/hc/en-us/articles/360025869712)。 ### 订单等待发货

当订单准备在 ShipStation 中发货时，将跟踪此指标。 ### 订单等待付款

当订单未付款并在 ShipStation 中标记为 **等待付款** 时，系统会跟踪此指标。并非所有商店都支持未付款订单。订单付款后，商店会将订单的更新信息发送给 ShipStation，或者您可以手动将订单标记为已付款，然后 ShipStation 会将订单状态更新为 **订单等待发货**。该事件随后将同步到 Klaviyo。 ### 订单暂停

当您使用 ShipStation 中的“保留”操作来保留订单时，系统会跟踪此指标。这对于预订、延迟缺货产品的订单或因任何其他原因延迟订单非常有用。订单可以设置为**保留**，直到设定的日期或指定的天数之后。 ### 订单已发货

一旦为订单打印标签，就会跟踪此指标，此时 ShipStation 会将订单移至 **已发货** 状态。生成出库发货标签时，订单将移至此处，但如果手动标记为已发货或由发货第三方标记为已发货，则不会收到此状态。 ### 订单已取消

当 ShipStation 中取消订单时，系统会跟踪此指标。 ## 结果

您已完成与 ShipStation 的集成，并已在 Klaviyo 中验证了您的 ShipStation 数据。现在，您将能够根据 ShipStation 跟踪的运输事件和订单状态来个性化和定位电子邮件。 ## 其他资源

- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [如何创建购买后流程](https://help.klaviyo.com/hc/en-us/articles/360028872611)