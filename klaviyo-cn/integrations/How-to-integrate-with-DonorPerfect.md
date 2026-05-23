---
id: "115005255168"
title: "如何与 DonorPerfect 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005255168-How-to-integrate-with-DonorPerfect"
section: "DonorPerfect"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:25Z"
language: "zh"
---
## 你将会学到

了解如何将 DonorPerfect 与 Klaviyo 集成。完成这些步骤后，您将能够根据每个贡献者的捐赠和网站活动来个性化和定位电子邮件。以下是我们从 DonorPerfect 同步的一些数据：

- 捐款金额
- 贡献者信息，包括名字和姓氏、位置以及他们如何找到您的网站
- 捐赠是否经常性，如果是，发生的频率
- 贡献者是否愿意匿名

首先，您需要找到 DonorPerfect API 密钥，然后在 Klaviyo 中启用集成。 ## 找到您的 API 密钥

您可以从 DonorPerfect 客户经理处检索您的 API 密钥。向您的客户经理发送一封电子邮件，请求您提供 API 密钥，他们会很快将其发​​送给您。 ## 在 Klaviyo 中添加 DonorPerfect 集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 在下一页上，单击 ****探索应用程序****，搜索 **DonorPerfect**，然后单击该卡。 3. 然后，单击****安装****。 4. 添加您的 DonorPerfect API 密钥，然后点击****连接到 DonorPerfect****。 5. 在下一页上，选择****将所有 DonorPerfect 捐赠者添加到 Klaviyo 列表****，然后从出现的下拉列表中选择一个列表。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28704476528923)
6. 单击****完成设置****。 ## 监控 Klaviyo 同步并验证数据

集成后要检查您的 DonorPerfect 集成：

1. 单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****选项卡。 2. 单击****做出的贡献**** 指标以验证是否已为此指标填充数据。如果有数据，您只需等待初始 DonorPerfect 集成同步完成即可；此过程最多可能需要几个小时，具体取决于您帐户中的数据量。 Klaviyo 将导入您所有的历史 DonorPerfect 数据。为了验证这一点，您可以将 Klaviyo 中特定日期的贡献数量与 DonorPerfect 界面中的数量进行比较，并确认它们匹配。 3. 例如，在探索 Klaviyo 中的****做出贡献**** 指标时，您可以将鼠标悬停在昨天的数据点上或查看图表下方的数据表，以了解昨天报告了多少贡献。 4. 将该数字与昨天存储在 DonorPerfect 中的数字进行比较，您应该看到它们完全匹配。如果没有，问题很可能是您的 Klaviyo 帐户的时区与您的 DonorPerfect 的帐户时区不匹配。 5. 要检查您在 Klaviyo 的时区设置：
   1. 单击左下角您的帐户名称。 2. 选择然后单击****设置**** ****> 组织****。 3. 向下滚动到**时区**。 ## DonorPerfect 数据

DonorPerfect 捕获并加载到 Klaviyo 中的主要指标有 1 个：****做出的贡献****。 ![Klaviyo 中“指标”选项卡中 DonorPerfect 做出的贡献指标](https://klaviyo.zendesk.com/hc/article_attachments/28704476521755)

### 贡献指标

当支持者在 DonorPerfect 中做出贡献时，就会跟踪此事件。 Klaviyo 跟踪的事件包括 DonorPerfect 收集的所有信息，包括捐款金额、捐款是否重复，如果是，捐款重复的频率。您可以根据以下条件过滤和定位**做出的贡献**事件：

- ****价值****
- ****活动****
- ****第一份礼物****
- ****礼物类型****
- ****纪念****
- ****重复出现****（正确或错误）

以下是我们随“贡献”事件一起收到的数据示例：

![在 Klaviyo 中弹出贡献指标活动详细信息](https://klaviyo.zendesk.com/hc/article_attachments/28704484671643)

### 客户数据

除了来自 DonorPerfect 的 Klaviyo 同步指标之外，每个 Klaviyo 配置文件中还添加了自定义属性。您可以在段和流中使用这些属性。以下是从 DonorPerfect 自动同步的属性：

- 电子邮件
- 名字
- 姓氏
- 城市
- 州/地区
- 邮政编码
- 国家
- 电话号码

### DonorPerfect 数据同步的频率

DonorPerfect 中的指标和配置文件属性使用 Webhook 进行同步。这意味着 DonorPerfect 会在事件发生时向 Klaviyo 发出指示，然后 Klaviyo 将提取该事件​​的所有数据。这几乎是瞬间发生的。 ## 添加 Klaviyo 现场跟踪

最后一步是将 Klaviyo 的 **Active on Site** 跟踪代码添加到您的网站页脚。此 Klaviyo 跟踪代码将使我们能够为您跟踪**网站活跃**指标，以便您可以查看和利用与网站访问和访客行为相关的数据。通过这个指标，Klaviyo 将跟踪已知浏览器的网站活动。例如，您可以使用**网站活跃**指标来创建访问过您的网站（登录时）但尚未捐款的用户细分。 1. 通过选择****集成****选项卡，然后单击右上角的****管理数据> 设置网络跟踪****，可以在 Klaviyo 中找到以下跟踪脚本。 2. 我们还在此处添加了 Klaviyo **Active on Site** 跟踪脚本，您可以将其粘贴到应用程序主模板中的“</body>”标记之前。请记住添加您自己的 API 密钥，可以在****帐户名称 > 设置 > API 密钥****下找到，您可以在其中看到“公共 API 密钥”：

   ````
   <script type="application/javascript" 异步
    src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=公共 API 密钥"></script>
   ````
3. 然后，您需要在 **设置网络跟踪** 页面上输入您的网站 URL。输入 URL 后，单击****下一步****以测试跟踪设置。如果工作正常，您应该会收到成功消息。 ![使用 URL 文本框和蓝色背景的“下一步”按钮设置网络跟踪的第 2 步](https://klaviyo.zendesk.com/hc/article_attachments/28704484675867)

## 结果

您现在已与 DonorPerfect 集成，验证了您的同步数据，并添加了 Klaviyo 现场跟踪。 ## 其他资源

- [集成常见问题解答参考](https://help.klaviyo.com/hc/en-us/articles/115005081007)
- [集成同步参考频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)