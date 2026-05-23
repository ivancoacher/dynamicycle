---
id: "115005255188"
title: "如何与 Donate.ly 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005255188-How-to-integrate-with-Donate-ly"
section: "Donate.ly"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "zh"
---
## 你将会学到

了解如何将 Donate.ly 与 Klaviyo 集成。完成这些步骤后，您将能够根据每个贡献者的捐赠和网站活动来个性化和定位电子邮件。以下是我们从 Donate.ly 同步的一些数据：

- 贡献金额
- 客户信息，包括名字和姓氏、位置以及他们如何找到您的网站
- 捐赠是否经常性，如果是，发生的频率
- 贡献者是否愿意匿名

首先，您将找到 Donate.ly 帐户 slug，然后在 Klaviyo 中启用集成。 ## 找到您的帐户 slug

1. 登录您的 Donate.ly 帐户。 2. 在右上角的菜单栏中，单击标有组织名称的下拉菜单，然后单击****帐户设置****。这将引导您进入一个页面，您可以在其中找到您的帐户别名。 ![Donate.ly 中的常规设置页面显示帐户标题和帐户别名](https://klaviyo.zendesk.com/hc/article_attachments/28717386426395)

## 在 Klaviyo 中启用 Donate.ly 集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 选择****探索应用程序****，搜索**Donate.ly**，然后单击该卡片。然后，单击****安装****。 3. 输入您的 Donate.ly 帐户名称、电子邮件和密码。电子邮件和密码必须具有管理员访问权限，否则 Klaviyo 将无法提取您的所有筹款和活动数据。单击****连接到 Donate.ly****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717380219803)
4. 您应该会收到一条成功消息。 ## 监控 Klaviyo 同步并验证数据

要检查您的 Donate.ly 集成：

1. 单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****选项卡。 2. 单击****做出的贡献**** 指标以验证是否已填充该指标的数据。如果有数据，您所需要做的就是等待初始 Donate.ly 集成同步完成；此过程最多可能需要几个小时，具体取决于您帐户中的数据量。 Klaviyo 将导入您所有的历史 Donate.ly 数据。为了验证这一点，您可以将 Klaviyo 中特定日期的捐款数量与 Donate.ly 界面中的捐款数量进行比较，并确认它们匹配。 3. 例如，在 Klaviyo 中探索 **Made Contribution** 指标时，您可以将鼠标悬停在昨天的数据点上或查看图表下方的数据表，以了解昨天报告了多少贡献。 4. 将该数字与昨天存储在 Donate.ly 中的数字进行比较，您应该看到它们完全匹配。如果没有，问题很可能是您的 Klaviyo 帐户的时区与您的 Donate.ly 时区不匹配。 5. 要检查您在 Klaviyo 的时区设置：
   - 单击左下角您的帐户名。 - 选择然后单击****设置**** ****> 组织****。 - 向下滚动到**时区**。 ## 了解您的 Donate.ly 数据

Donatel.ly 捕获并加载到 Klaviyo 中的一个主要指标是：**做出的贡献。**

![Donate.ly 在 Klaviyo 中做出的贡献指标](https://klaviyo.zendesk.com/hc/article_attachments/28717380211739)

当支持者在 Donatel.ly 中做出贡献时，就会跟踪此事件。 Klaviyo 跟踪的事件包括 Donatel.ly 收集的所有信息，包括捐款金额、捐款是否重复，如果是，捐款重复的频率。您可以根据以下条件过滤和定位**做出的贡献**事件：

- ****价值****
- ****匿名****（对或错）
- ****活动标题****
- ****营销活动唯一标识符****
- ****捐赠类型****
- ****重复出现****（正确或错误）

以下是我们随 **Made Contribution** 事件收到的数据示例：

![Klaviyo 中 Donate.ly 贡献指标的活动详细信息](https://klaviyo.zendesk.com/hc/article_attachments/28717380213275)

### 客户数据

除了 Klaviyo 从 Donate.ly 同步的两个核心指标之外，Klaviyo 还为每个贡献者创建了全面的 Klaviyo 个人资料。除了基本联系信息外，Klaviyo 还将同步您可能存储在 Donate.ly 中的有关特定人员的任何其他详细信息 - 这些详细信息将作为自定义属性同步，添加到每个 Klaviyo 个人资料中。您可以在段和流中使用这些属性。 以下是自动从 Donate.ly 同步到内置 Klaviyo 字段的默认属性：

- 电子邮件
- 名字
- 姓氏
- 城市
- 州/地区
- 邮政编码
- 国家
- 电话号码

## Donate.ly 同步的频率

Donatel.ly 的指标和配置文件属性使用 Webhooks 进行同步。这意味着 Donatel.ly 会在事件发生时向 Klaviyo 发出指示，然后 Klaviyo 将提取该事件​​的所有数据。这几乎是瞬间发生的。 ## 添加 Klaviyo 现场跟踪

最后一步是将 Klaviyo 的 **Active on Site** 跟踪代码添加到您的网站页脚。此 Klaviyo 跟踪代码将使我们能够为您跟踪**网站活跃**指标，以便您可以查看和利用与网站访问和访客行为相关的数据。通过这个指标，Klaviyo 将跟踪已知浏览器的网站活动。例如，您可以使用**网站活跃**指标来创建访问过您的网站（登录时）但尚未捐款的用户细分。 1. 通过选择****集成****选项卡，然后单击右上角的****管理数据> 设置网络跟踪****，可以在 Klaviyo 中找到以下跟踪脚本。 2. 我们还在此处添加了 Klaviyo **Active on Site** 跟踪脚本，您可以将其粘贴到应用程序主模板中的“</body>”标记之前。请记住添加您自己的 API 密钥，可以在****设置 > API 密钥****下找到，您可以在其中看到“公共 API 密钥”：

   ````
   <script type="application/javascript" 异步
    src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=公共 API 密钥"></script>
   ````
3. 然后，您需要在 **设置网络跟踪** 页面上输入您的网站 URL。输入 URL 后，单击****下一步****以测试跟踪设置。如果工作正常，您应该会收到成功消息。 ![使用 URL 文本框和蓝色背景的“下一步”按钮设置网络跟踪的第 2 步](https://klaviyo.zendesk.com/hc/article_attachments/28717386435995)

## 结果

您现在已与 Donor.ly 集成，验证了您的同步数据，并添加了 Klaviyo 现场跟踪。 ## 其他资源

- [集成常见问题解答参考](https://help.klaviyo.com/hc/en-us/articles/115005081007)
- [集成同步参考频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)