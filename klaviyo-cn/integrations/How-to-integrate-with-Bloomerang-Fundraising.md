---
id: "115005082847"
title: "如何与Bloomerang筹款整合"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005082847-How-to-integrate-with-Bloomerang-Fundraising"
section: "Bloomerang Fundraising"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:21Z"
language: "zh"
---
## 你将会学到

了解如何将 Bloomerang 筹款与 Klaviyo 集成。完成这些步骤后，您将能够根据每个贡献者的捐赠和网站活动来个性化和定位电子邮件。以下是我们从 Bloomerang 筹款同步的一些数据：

- 每笔捐款金额
- 贡献者信息，包括名字和姓氏、位置以及他们如何找到您的网站
- 每项贡献是否重复出现，如果是，出现的频率

首先，您需要在 Bloomerang Fundraise 中生成 API 令牌，然后在 Klaviyo 中启用集成。 ## 生成您的 Bloomerang 筹款 API 令牌

1. 登录您的 Bloomerang 筹款帐户。 2. 单击帐户左侧边栏中的****数据工具****，然后单击****API访问******。**
3. 单击****创建 API 令牌******。**
4. 然后，系统将提示您创建令牌名称并建立令牌类型。在**令牌类型**下，选择“永久”。 ![屏幕截图 2026-01-29 7.11.22PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46052097347867)
5. 选择“永久”作为**令牌类型**后，选择您想要在 Klaviyo 中访问的表单。如果您想要所有捐赠数据，请选择您的所有活动。 6. 然后，Bloomerang Fundraise 将为您提供 API 令牌**。**这是您在下一步将 Bloomerang Fundraise 与 Klaviyo 集成时需要的。 ## 在 Klaviyo 中添加 Bloomerang 筹款集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 选择****探索应用****，搜索 Bloomerang 筹款，然后单击该卡片。 3. 然后，单击****安装****。 4. 输入您的 API 令牌并单击 ****连接到**** ****Bloomerang********筹款********.****
   ![屏幕截图 2026-01-29 7.05.43PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46052097349787)
5. 您应该会收到一条成功消息。 ## 监控 Klaviyo 同步并验证数据

要检查您的 Bloomerang 筹款集成：

1. 单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****。 2. 单击 **Made Contribution** 指标以验证是否已填充该指标的数据。如果有数据，您只需等待初始 Bloomerang 筹款集成同步完成即可；此过程最多可能需要几个小时，具体取决于您帐户中的数据量。 3. Klaviyo 将导入您所有的历史 Bloomerang 筹款数据。要验证这一点，您可以将 Klaviyo 中特定日期的订单数量与 Bloomerang 筹款界面中的订单数量进行比较，并确认它们匹配。例如，在探索 Klaviyo 中的 **Made Contribution** 指标时，您可以将鼠标悬停在昨天的数据点上或查看图表下方的数据表，以了解昨天报告了多少订单。 4. 将该数字与昨天存储在 Bloomerang 筹款中的数字进行比较，您应该会看到它们完全匹配。如果没有，问题很可能是您的 Klaviyo 帐户的时区与您的 Bloomerang 筹款时区不匹配。 5. 要检查您在 Klaviyo 的时区设置：
   - 单击左下角您的帐户名。 - 选择然后单击****设置 > 组织****。 - 向下滚动到**时区**。 ## 从 Bloomerang 筹款同步的数据

Bloomerang 筹款捕获并同步到 Klaviyo 的两个指标：**做出贡献**和**注册活动**。 ### 做出贡献

当捐赠者在 Bloomerang 筹款活动中捐款时，系统会跟踪此事件。您可以根据以下条件过滤和定位**做出的贡献**事件：

- 捐赠来源
- 限制
- 选择加入
- 类型
- 匿名
- 表格名称
- 表格ID
- 价值$

### 已注册活动

当提交点对点事件注册表单时，将跟踪此事件。您可以根据以下条件过滤和定位**注册活动**活动：

- 表格ID
- 注册ID
- 交易ID
- 标题
- 筹款目标
- 捐赠来源
- 队长
- $事件\_id
- 价值$

### 客户数据

除了 Klaviyo 从 Bloomerang 筹款同步的指标之外，每个 Klaviyo 个人资料中还添加了自定义属性。您可以在段和流中使用这些属性。 以下属性是内置的 Klaviyo 字段，将自动同步：

- 电子邮件
- 名字
- 姓氏
- 城市
- 州/地区
- 邮政编码
- 国家
- 电话号码

### 回旋镖筹款同步的频率

Bloomerang 筹款的指标和个人资料属性使用网络钩子同步。这意味着 Bloomerang 筹款会在事件发生时向 Klaviyo 发出指示，然后 Klaviyo 将提取所有数据。这几乎是瞬间发生的。 ## 添加 Klaviyo 现场跟踪

最后一步是将 Klaviyo 的 **Active on Site** 跟踪代码添加到您的网站页脚。此 Klaviyo 跟踪代码将使我们能够为您跟踪**网站活跃**指标，以便您可以查看和利用与网站访问和访客行为相关的数据。通过这个指标，Klaviyo 将跟踪已知浏览器的网站活动。例如，您可以使用**网站活跃**指标来创建访问过您的网站（登录时）但尚未捐款的用户细分。要启用现场跟踪：

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 选择****管理数据> 设置网络跟踪****。 3. 复制**步骤 1** 下的代码并将其粘贴到网站主模板中的 </body> 标记之前。确保将其粘贴到与您所在的 Klaviyo 帐户关联的网站上。 ![启用现场跟踪模式显示安装现场跟踪的步骤。](https://klaviyo.zendesk.com/hc/article_attachments/34456524887835)
4. 粘贴代码片段后，单击“**步骤 2**”下的“****确认****”以测试跟踪设置。如果工作正常，您应该会收到成功消息。 ![成功消息通知您已启用现场跟踪。](https://klaviyo.zendesk.com/hc/article_attachments/34456509068443)

## 结果

您现在已与 Bloomerang 筹款集成，验证了您的同步数据，并添加了 Klaviyo 现场跟踪。 ## 其他资源

- [集成常见问题解答参考](https://help.klaviyo.com/hc/en-us/articles/115005081007)
- [集成同步参考频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)