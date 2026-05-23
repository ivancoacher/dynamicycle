---
id: "115005255108"
title: "如何与 Funraise 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005255108-How-to-integrate-with-Funraise"
section: "Funraise"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "zh"
---
## 你将会学到

了解如何将 Funraise 与 Klaviyo 集成，以便根据每个贡献者的捐赠和网站活动个性化和定位电子邮件。从 Funraise 同步到 Klaviyo 的数据包括：

- 作出贡献时
- 贡献金额
- 客户信息，包括名字和姓氏、位置以及他们如何找到您的网站
- 捐赠是否经常性，如果是，发生的频率
- 贡献者是否愿意匿名

## 添加 Funraise 集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 单击****探索应用程序****，搜索**Funraise**，然后单击卡片。然后，单击****安装****。 3. 输入您的用户名和密码，然后单击****连接到 Funraise****。请注意，电子邮件和密码必须具有管理员访问权限，否则，Klaviyo 将无法提取您的所有筹款和活动数据。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723629819803)
4. 在下一页上，您可以选择自动将新支持者添加到 Klaviyo 列表，然后从下拉列表中选择一个列表。 5. 单击****完成设置****。 ## 添加 Klaviyo 现场跟踪

Klaviyo 提供不同类型的现场跟踪，其中一种跟踪已知用户何时在您的网站上活跃。这种类型的跟踪称为“网站上活动”跟踪，您可以为您的 Funraise 网站启用它。要启用它，您必须将代码片段添加到站点页脚。通过 **Active on Site** 跟踪，您将能够查看和利用与网站访问和访客行为相关的数据。例如，您可以使用**网站活跃**指标来创建访问过您的网站（登录时）但尚未捐款的用户细分。 1. 复制下面的 **Active on Site** 代码片段：

   ````
   <script type="application/javascript" 异步
    src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=公共 API 密钥"></script>
   ````
2. 导航到您的 Funraise 网站，并将代码片段粘贴到应用程序主模板中的 </body> 标记之前。 3. 将代码段中的“公共 API 密钥”文本替换为您的 Klaviyo 公共 API 密钥，该密钥可在您的 Klaviyo 帐户中****帐户名称 > 设置 > API 密钥****下找到。 4. 保存您的更改。 5. 在您的 Klaviyo 帐户中，导航至右上角的****集成 > 管理数据 > 设置网络跟踪****，然后在第二步中输入您的站点 URL。 6. 单击****下一步**** 测试您的跟踪设置。 ![Klaviyo 网络跟踪设置测试的 URL 文本框，带有蓝色背景的 Next](https://klaviyo.zendesk.com/hc/article_attachments/28723624474651)
7. 如果您的跟踪设置正确，您将收到一条成功消息。 ## 监控 Klaviyo 同步并验证捐赠数据

要监控和验证您的 Funraise 集成数据同步：

1. 单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****。 2. 搜索并单击 **Made Contribution** 指标以验证是否已填充该指标的数据。 3. 如果有数据，您只需等待初始 Funraise 集成同步完成即可；此过程最多可能需要几个小时，具体取决于您帐户中的数据量。 4. Klaviyo 将导入您所有的历史 Funraise 数据；为了验证这一点，您可以将 Klaviyo 中特定日期的贡献数量与 Funraise 界面中的数量进行比较，并确认它们匹配。 5. 如果不匹配，问题很可能是您的 Klaviyo 帐户的时区与您的 Funraise 时区不匹配。 6. 要检查 Klaviyo 中的时区设置，请单击左下角的帐户名称，选择 ****设置**** ****> 组织****。 7. 找到**时区**部分。 ## 数据从 Funraise 同步

Funraise 捕获并同步 Klaviyo 的一项主要指标：**做出的贡献**。当支持者在 Funraise 中做出贡献时，就会跟踪此事件。 Klaviyo 跟踪的事件包括 Funraise 收集的所有信息，包括捐款金额、捐款是否重复，以及如果是，捐款重复的频率。 您可以根据以下关键条件过滤和定位**做出的贡献**事件：

- 捐赠类型
- 表格名称
- 表单网址
- 是匿名的（真或假）
- 奉献精神（真还是假）
- 重复出现（正确或错误）
- 页面网址

以下是 Klaviyo 接收到的所有数据以及“贡献”事件的示例：

![Klaviyo 中的“贡献”指标的活动详细信息，显示价值和捐赠类型等字段](https://klaviyo.zendesk.com/hc/article_attachments/28723629805851)

除了从 Funraise 同步 Klaviyo 的这一核心指标之外，Klaviyo 还为每个贡献者创建一个 Klaviyo 个人资料。除了基本联系信息外，Klaviyo 还会同步您可能存储在 Funraise 中的有关特定人员的任何其他详细信息。这些详细信息将作为自定义属性同步，添加到每个 Klaviyo 配置文件中。您可以在段和流中使用这些属性。以下是从 Funraise 自动同步的默认属性：

- 电子邮件
- 名字
- 姓氏
- 城市
- 州/地区
- 邮政编码、国家/地区
- 电话号码

## 结果

您已完成与 Funraise 的集成、设置网络跟踪，并已在 Klaviyo 中验证您的 Funraise 数据。现在，您将能够根据每个贡献者的捐赠和网站活动来个性化和定位电子邮件。 ## 其他资源

- [集成常见问题解答参考](https://help.klaviyo.com/hc/en-us/articles/115005081007)
- [集成同步参考频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)