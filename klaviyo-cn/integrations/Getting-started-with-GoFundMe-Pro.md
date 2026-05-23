---
id: "115005083387"
title: "GoFundMe Pro 入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005083387-Getting-started-with-GoFundMe-Pro"
section: "Classy"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:21Z"
language: "zh"
---
## 你将会学到

了解如何将 GoFundMe Pro 与 Klaviyo 集成。完成这些步骤后，您将能够根据每个贡献者的捐赠和网站活动来个性化和定位电子邮件。 ## 开始之前

为了将 GoFundMe Pro 与 Klaviyo 集成，您需要访问 GoFundMe Pro 的 API，该 API 需要付费订阅 GoFundMe Pro。要详细了解如何访问 GoFundMe Pro API，请访问他们的[GoFundMe Pro API 入门](https://support.classy.org/s/article/getting-started-with-the-classy-api) 文章和开发者网站[请求访问权限](https://developers.classy.org/overview/request-access) 文章。 ## 在 GoFundMe Pro 中创建应用程序

为了将 GoFundMe Pro 与 Klaviyo 集成，您首先需要在 GoFundMe Pro 中创建一个新的 API 应用程序。这是因为您需要 GoFundMe Pro 客户端 ID 和客户端密钥才能进行集成，而生成这些凭据的方法是在 GoFundMe Pro 中创建 API 应用程序。 1. 登录您的 GoFundMe Pro 管理员帐户。 2. 在左侧菜单中，单击****应用程序和集成****
   ![Classy 中的 API + 应用程序选项卡显示启用了 Classy API](https://klaviyo.zendesk.com/hc/article_attachments/28713328533787)
3. 单击****GoFundMe Pro API****。您将进入应用程序创建页面，系统会要求您命名您的应用程序并输入 Oauth2 重定向 URI。您可以将您的应用程序命名为 Klaviyo API，并在 Oauth2 Redirect URI 下输入您网站的 URL。然后，单击****创建应用程序****。 ![在 Classy 中创建新应用程序，其中包含应用程序名称和 Oauth2 重定向 URI 字段，创建应用程序呈灰色](https://klaviyo.zendesk.com/hc/article_attachments/28713334167195)
4. 创建新应用程序后，它将列在您的 GoFundMe Pro 帐户中。通过单击应用程序旁边的****编辑****，您可以查看您的客户端 ID 和客户端密钥，您应该安全地存储它们，以便将它们复制粘贴到 Klaviyo 中。 ![编辑 API 应用程序页面中的 Classy Client ID 和 Client Secret 字段已模糊](https://klaviyo.zendesk.com/hc/article_attachments/28713328545819)

## 找到您的组织 ID

您还需要在 GoFundMe Pro 中找到您的组织 ID。 1. 导航至您的 GoFundMe Pro 控制面板。 2. 在这里，您将在 URL 末尾看到组织 ID。这将是在“/admin”之后找到的数值，如下面的屏幕截图所示。当您配置 GoFundMe Pro 集成时，需要将此 ID 复制并粘贴到 Klaviyo 中。 ![Classy 仪表板的 URL，包含 URL 的一部分，数字 55770，以灰色突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28713328548763)

## 添加 GoFundMe Pro 集成

现在，您将在 Klaviyo 中添加 GoFundMe Pro 集成。 1. 在 Klaviyo 中，选择****集成****选项卡。 2. 选择****探索应用程序****，搜索**GoFundMe Pro**，然后单击该卡。然后，单击****安装****。 3. 输入 GoFundMe Pro 中的客户端 ID、客户端密码和组织 ID。 ![屏幕截图 2026-02-02 7.44.26PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46213955465755)
4. 单击****连接到 GoFundMe Pro************。******
5. 在下一页上，您可以选择 **添加所有 GoFundMe** **Pro 支持者到 Klaviyo 列表**，然后从下拉列表中选择一个列表。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28713328579355)
6. 完成后，单击****完成设置****。 ## 监控 Klaviyo 同步

要检查您的 GoFundMe Pro 集成：

1. 单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****选项卡。 2. 单击 **Made Contribution** 指标以验证是否已填充该指标的数据。如果有数据，您只需等待初始 GoFundMe Pro 集成同步完成即可；此过程最多可能需要几个小时，具体取决于您帐户中的数据量。 Klaviyo 将导入您所有的历史 GoFundMe Pro 数据。 3. 要验证这一点，您可以将 Klaviyo 中特定日期的捐款数量与 GoFundMe Pro 界面中的捐款数量进行比较，并确认它们匹配。例如，在探索 **做出贡献** 指标时，您可以将鼠标悬停在昨天的数据点上或查看图表下方的数据表，以了解昨天报告了多少贡献。 4. 将该数字与昨天存储在 GoFundMe Pro 中的数字进行比较，您应该会看到它们完全匹配。 如果没有，问题很可能是您的 Klaviyo 帐户的时区与您的 GoFundMe Pro 时区不匹配。 5. 要检查您在 Klaviyo 的时区设置：
   - 单击左下角您的帐户名。 - 选择然后单击****设置 > 组织****。 - 向下滚动到**时区**。 ## 从 GoFundMe Pro 同步的数据

GoFundMe Pro 捕获了多个指标并将其加载到 Klaviyo 中。所有这些指标都可以通过过滤 GoFundMe Pro 来查看。 ![按 Classy 过滤的 Klaviyo 指标选项卡显示指标列表，包括创建的筹款团队](https://klaviyo.zendesk.com/hc/article_attachments/28713334189467)

GoFundMe Pro 每 30 分钟定期将数据同步到您的 Klaviyo 帐户。 ### 贡献指标

当支持者在 GoFundMe Pro 中捐款时，就会跟踪此事件。 Klaviyo 跟踪的事件包括 GoFundMe Pro 收集的所有信息，包括捐款金额、捐款是否重复，以及如果是，捐款重复的频率。您可以根据以下条件过滤和定位**做出的贡献**事件：

- 价值
- 活动结束
- 活动目标
- 活动 ID
- 活动名称
- 活动开始
- 活动类型（例如peer\_to\_peer）
- 活动场地
- 评论
- 费用
- 如果匿名（真或假）
- 组织ID
- 价格
- 产品编号
- 产品名称（例如线下捐赠）
- 数量
- 是否是一封奉献电子邮件（真或假）
- 交易ID
- 捐赠类型

以下是我们随 **Made Contribution** 事件收到的数据示例：

![Klaviyo 中的弹出窗口显示“做出贡献”活动的活动详细信息，包括价值](https://klaviyo.zendesk.com/hc/article_attachments/28713334195099)

### 注册事件指标

当支持者在 GoFundMe Pro 中注册活动时，系统会跟踪此活动。 Klaviyo 跟踪的活动包括 GoFundMe Pro 在活动注册时收集的所有信息。您可以根据以下条件过滤和定位**注册活动**事件：

- 价值
- 活动结束
- 活动目标
- 活动 ID
- 活动名称
- 活动开始
- 活动类型（例如peer\_to\_peer）
- 活动场地
- 评论
- 费用
- 如果匿名（真或假）
- 组织ID
- 价格
- 产品编号
- 产品名称（例如线下捐赠）
- 数量
- 定期计划 ID
- 是否是一封奉献电子邮件（真或假）
- 交易ID
- 类型（注册）

以下是我们收到的数据以及 Registered for Event 事件的数据示例：

![Klaviyo 中的弹出窗口显示注册活动事件的活动详细信息，包括值](https://klaviyo.zendesk.com/hc/article_attachments/28713334199835)

### 筹款团队和页面指标

除了 Klaviyo 同步的主要**做出贡献**和**注册活动**指标以跟踪支持者如何与您的组织互动之外，我们还将同步围绕筹款团队和页面的创建以及目标进度的以下事件：

- ****创建筹款团队****
  当有人创建筹款团队页面时记录。 - ****筹款达到目标的 25%****
  当筹款团队达到目标的 25% 时记录。 - ****筹款达到目标的 50%****
  当筹款团队达到目标的 50% 时记录。 - ****筹款活动达到目标的 75%****
  当筹款团队达到其目标的 75% 时记录。 - ****筹款活动达到目标的100%****
  当筹款团队达到 100% 目标时记录。以下是收到的详细信息以及每个指标的列表：

- 状态
- 筹集资金总额
- 筹款团队名称
- 平均捐赠
- 最大一笔捐款
- 活动 ID
- 组织ID
- 捐助者总数
- 捐款总额
- 活动名称
- 团队负责人 ID
- 目标百分比
- 筹款团队 ID
- 筹款活动邮政编码
- 筹款州
- 筹款总额

以下是筹款人的 Klaviyo 个人资料中这些跟踪事件的示例：

![Daniel Esrig 的 Klaviyo 个人资料显示了不同 Classy 事件的时间表](https://klaviyo.zendesk.com/hc/article_attachments/28713334204187)

### 客户数据

Klaviyo 将为每位贡献者创建全面的 Klaviyo 个人资料。除了基本联系信息外，Klaviyo 还会同步您可能存储在 GoFundMe Pro 中的有关特定人员的任何其他详细信息。这些详细信息将作为自定义属性同步，添加到每个 Klaviyo 配置文件中。 您可以在段和流中使用这些属性。以下是从 GoFundMe Pro 自动同步的属性：

- 电子邮件
- 名字
- 姓氏
- 城市
- 州/地区
- 邮政编码
- 国家
- 电话号码

## 结果

现在，您已完成 GoFundMe Pro 与 Klaviyo 的集成并查看了同步数据。 ## 其他资源

- [如何设置Classy活动和流程](https://klaviyo.zendesk.com/hc/en-us/articles/115005255868)
- [集成同步参考频率](https://klaviyo.zendesk.com/hc/en-us/articles/115005253208)