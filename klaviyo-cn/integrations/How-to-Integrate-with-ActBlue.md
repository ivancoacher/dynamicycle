---
id: "115005255208"
title: "如何与 ActBlue 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005255208-How-to-Integrate-with-ActBlue"
section: "ActBlue"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:40Z"
language: "zh"
---
## 你将会学到

了解如何将 ActBlue 与 Klaviyo 集成。完成这些步骤后，您将能够根据每个贡献者的捐赠和网站活动来个性化和定位电子邮件。以下是我们从 ActBlue 同步的一些数据：

- 捐款金额
- 贡献者信息，包括名字和姓氏、位置以及他们如何找到您的网站
- 捐赠是否经常性，如果是，发生的频率
- 接受捐赠的委员会
- EntityID 和 FecID

## 添加 ActBlue 集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 单击****探索应用程序****，搜索**ActBlue**，然后单击该卡。然后，单击****安装****。 3. 选择****连接到 ActBlue****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723518757659)
4. 在下一页上，复制 Webhook URL、用户名和密码并将其发送给您的 ActBlue 帐户经理。如果您没有 ActBlue 的联系人，请[联系我们的支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272)，我们会将其转发给 ActBlue（此过程通常需要不到 24 小时）。 5. 单击****完成设置****。 ## 监控 Klaviyo 同步

要检查您的 ActBlue 集成（完全集成后）：

1. 单击 Klaviyo 帐户中的****分析****下拉列表，然后选择****指标****选项卡。 2. 单击 ****Made Contribution**** 指标（可通过 ActBlue 图标识别）以验证是否已填充该指标的数据。 3. 如果有数据，您只需等待 ActBlue 集成的历史同步完成即可；此过程最多可能需要几个小时，具体取决于您帐户中的数据量。 4. Klaviyo 将导入您的所有历史 ActBlue 数据。为了验证这一点，您可以将 Klaviyo 中特定日期的订单数量与 ActBlue 界面中的订单数量进行比较，并确认它们匹配。例如，在探索**做出的贡献**指标**时，**您可以将鼠标悬停在昨天的数据点上或查看图表下方的数据表，以了解昨天报告了多少订单。 5. 将该数字与昨天存储在 ActBlue 中的数字进行比较，您应该看到它们完全匹配。如果没有，问题很可能是您的 Klaviyo 帐户的时区与您的 ActBlue 时区不匹配。 6. 要检查您在 Klaviyo 的时区设置：
   - 单击左下角您的帐户名。 - 选择然后单击****设置**** ****> 组织****。 - 向下滚动到**时区**。 ## 从 ActBlue 同步的数据

ActBlue 捕获并同步到 Klaviyo 的一项主要指标：**做出的贡献**。 ![Klaviyo 中的“指标”选项卡由 ActBlue 过滤，显示“贡献”指标](https://klaviyo.zendesk.com/hc/article_attachments/28723518748571)

### 做出贡献

当客户完成结账流程并在 ActBlue 中做出贡献时，系统会跟踪此事件。 Klaviyo 同步的事件包括 ActBlue 收集的所有信息，包括捐款金额、捐款是否重复，以及如果是，捐款重复的频率。您可以根据以下条件过滤和定位**做出的贡献**事件：

- ****金额****
- ****重复出现****这是对或错。 - ****重复周期****如果捐赠不是重复的，则这将是“一次”，否则它将指示捐赠重复的频率。 - ****委员会名称****做出贡献的委员会的名称。 - ****实体ID****
- ****FecID****

以下是我们随 **Made Contribution** 事件收到的数据示例：

![Klaviyo 中弹出“做出贡献”活动的活动详细信息](https://klaviyo.zendesk.com/hc/article_attachments/28723507080091)

### 客户数据

除了 Klaviyo 从 ActBlue 同步的两个核心指标之外，Klaviyo 还为每个贡献者创建了全面的 Klaviyo 个人资料。除了基本联系信息外，Klaviyo 还会同步您可能存储在 ActBlue 中的有关特定人员的任何其他详细信息 - 这些详细信息将作为自定义属性同步，添加到每个 Klaviyo 个人资料中。您可以在段和流中使用这些属性。以下是从 ActBlue 自动同步的默认属性：

- 电子邮件
- 名字
- 姓氏
- 城市
- 州/地区
- 邮政编码
- 国家
- 电话号码

### ActBlue 同步的频率

ActBlue 的“贡献”指标和自定义配置文件属性使用 Webhooks 进行同步。 这意味着 ActBlue 会在事件发生时向 Klaviyo 发出指示，然后 Klaviyo 将提取该事件​​的所有相关数据。这几乎是瞬间发生的。 ## 添加 Klaviyo 现场跟踪

最后一步是将 Klaviyo 的 **Active on Site** 跟踪代码添加到您的网站页脚。此 Klaviyo 跟踪代码将使我们能够为您跟踪**网站活跃**指标，以便您可以查看和利用与网站访问和访客行为相关的数据。通过这个指标，Klaviyo 将跟踪已知浏览器的网站活动。例如，您可以使用**网站活跃**指标来创建访问过您的网站（登录时）但尚未捐款的用户细分。 1. 通过选择****集成****选项卡，然后单击右上角的****管理数据> 设置网络跟踪****，可以在 Klaviyo 中找到以下跟踪脚本。 2. 我们还在此处添加了 Klaviyo **Active on Site** 跟踪脚本，您可以将其粘贴到应用程序主模板中的“</body>”标记之前。请记住添加您自己的 API 密钥，可以在****设置 > API 密钥****下找到，您可以在其中看到“公共 API 密钥”：

   ````
   <script type="application/javascript" 异步
    src="https://static.klaviyo.com/onsite/js/klaviyo.js?company_id=公共 API 密钥"></script>
   ````
3. 然后，您需要在 **设置网络跟踪** 页面上输入您的网站 URL。输入 URL 后，单击****下一步****以测试跟踪设置。如果工作正常，您应该会收到成功消息。 ![使用 URL 文本框和蓝色背景的“下一步”按钮设置网络跟踪的第 2 步](https://klaviyo.zendesk.com/hc/article_attachments/28723507087771)

## 结果

您现在已与 ActBlue 集成、验证了同步数据并添加了 Klaviyo 现场跟踪。 ## 其他资源

- [集成常见问题解答参考](https://help.klaviyo.com/hc/en-us/articles/115005081007)
- [集成同步参考频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)