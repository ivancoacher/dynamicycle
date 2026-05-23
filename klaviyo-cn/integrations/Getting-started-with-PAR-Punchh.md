---
id: "19895874407579"
title: "PAR Punchh 入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/19895874407579-Getting-started-with-PAR-Punchh"
section: "PAR Punchh"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-19T18:44:36Z"
language: "zh"
---
## 你将会学到

了解如何与 PAR Punchh 集成，这是一个针对餐厅和便利店的一体化忠诚度和参与平台。 ## 开始之前

- 确保您拥有 PAR Punchh 白金 PAR Punchh 忠诚度套餐订阅，其中包括 PAR Punchh Amplify。如果您的品牌包含在 Essentials PAR Punchh Loyalty 或 Premium PAR Punchh Loyalty 套餐中，则您必须请求订阅 PAR Punchh Amplify 附加组件。只有订阅 PAR Punchh Amplify 才能访问 PAR Punchh Webhooks。 - 确保您对 PAR Punchh 帐户具有管理员或类似访问权限，以配置 PAR Punchh 中的设置。 ## 将 PAR Punchh 与 Klaviyo 集成

### 在克拉维约

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 单击****探索应用程序****。 3. 搜索 **Punchh** 并选择该卡。 4. 在下一页上，输入您的基本 URL 和业务管理密钥。 1. 有关更多信息，请参阅 [Punchh 帮助中心的这篇文章](https://support.punchh.com/s/article/How-do-I-generate-a-business-admin-key#:~:text=Information,to%20hit%20our%20Dashboard%20APIs.)。 ![显示将 Punchh 与 Klaviyo 集成的步骤的网页，包括 Punchh 凭据字段和这两种服务的徽标。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/22b4bd88283daddeab0e71a7827d20922070ec9e-1900x1400.png)

   5. 基本 URL 将是您访问 Punchh 平台的 URL。 ![在网络浏览器中突出显示 Punchh 仪表板的 URL。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/14d0163be976787c26987903d0387b8b35155fff-1896x444.png)

   6. 可以通过导航到****管理 > 所有用户、角色和权限 > 选择您的用户 > 滚动到底部以生成您的业务管理密钥来生成业务管理密钥。****

7. 单击****连接。****

8. 检查权限并单击允许。 9. 复制为您生成的 Webhook URL 并将其保存到安全位置。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32789350704283)

10. 检查设置以将未来的 Punchh 电子邮件订阅者同步到 Klaviyo。然后，从下拉列表中选择您的主电子邮件列表（或其他列表，如果需要）。我们建议将此列表设置为[单一选择](https://help.klaviyo.com/hc/en-us/articles/115005251108#h_01HZ5G5ZQBDHTV20V1BE7D4YAT)。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32789350712091)

11. 单击****保存****。 ### 在冲床

1. 在新选项卡中，登录 PAR Punchh 管理员。然后，导航至 ****Punchh > Webhooks Manager > 出站****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32789311418139)

2. 选择****Webhooks**** 选项卡。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32789311421467)

3. 单击****基本 URL****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32789311428635)

4. 单击****+ 添加新 URL****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32789350722971)

5. 输入以下内容：

- ****姓名****
  **克拉维约**
- ****Webhook 基本 URL****
  **https://a.klaviyo.com**
- ****管理员电子邮件****
  **餐厅@klaviyo.com**

  ![](https://klaviyo.zendesk.com/hc/article_attachments/32789311433627)

  6. 单击****提交****。 7. 选择****Webhooks**** 选项卡，然后单击****+ 创建 Webhook****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32789350731931)

  8. 输入以下内容：
- ****姓名****
  **克拉维约**
- ****描述****
  **Klaviyo 集成**
- ****基本网址****
  从下拉列表中选择 **Klaviyo**
  ![](https://klaviyo.zendesk.com/hc/article_attachments/32789311446427)
- ****Webhook 端点****
  粘贴您从 Klaviyo 复制的 Webhook URL。 然后，删除 **https://klaviyo.com**，这样你就只剩下 **/api/webhook...**
  ![](https://klaviyo.zendesk.com/hc/article_attachments/32789350740763)
- ****身份验证****
  选择**承载**
- ****授权不记名令牌****
  从 Webhook 端点中，选择 **s=** 之后和 **&k=** 之前的字符串并将其粘贴到此字段中
  ![](https://klaviyo.zendesk.com/hc/article_attachments/32789311455131)
- ****活动选择****
  选择下面列出的每个事件，一次一个
  - 客人
  - 忠诚度检查
  - 签到礼物
  - 救赎
  - 奖励
  - 交易通知：用户注册
  - 交易通知：POS 扫描仪签到
  - 交易通知：积分奖励
  - 交易通知：卡完成
  - 交易通知：已应用兑换
  - 可兑换

![](https://klaviyo.zendesk.com/hc/article_attachments/47657896980379)

9. 确保选中****活动****。 10. 单击****验证并提交****。然后您应该会看到一条成功消息。您的集成现已激活，个人资料、事件和同意更新将开始同步到 Klaviyo。 ## 更新您的 Punchh 集成

要更新 Klaviyo 中的集成：

1. 登录 Klaviyo。 2. 选择集成选项卡。 3. 选择打孔。 4. 单击横幅中的更新按钮。 ![Punchh 集成页面显示“需要采取行动”警告和提示“更新 Punchh”到新版本的横幅。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/9b62e54c8a3656fd91f95640ee974b390e47139e-3036x586.png)

5. 检查 Klaviyo 中的权限并单击****允许****。 6. 检查权限并选择允许。您将被重定向到 Klaviyo。 7. 选中该框以将 Punchh 电子邮件订阅者同步到 Klaviyo 列表，然后从下拉列表中选择一个列表。 8. 完成后，单击“保存”。 ## 了解您的 PAR Punchh 数据

Klaviyo 从 PAR Punchh 同步与奖励、会员资格和 PAR Punchh 属性相关的不同事件和对象。要查看您的 PAR Punchh 数据：

1. 单击左侧导航侧栏中的****分析****下拉列表。 2. 选择****指标****。在这里，您可以查看帐户中的所有指标。 3. 使用搜索栏旁边的过滤器选择器并选择 ****PAR Punchh**** 来过滤此视图以查看 PAR Punchh 指标。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32789350753179)

详细了解您的 [PAR Punchh 数据](https://help.klaviyo.com/hc/en-us/articles/19896802561307)。 ## 使用 PAR Punchh 数据细分客户

您可以使用 PAR Punchh 的指标来细分客户并针对他们开展活动。例如，您可以为过去 30 天内注册 PAR Punchh 忠诚度计划的每个人创建一个细分，并向该细分发送营销活动。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32789662897691)

1. 单击左侧导航边栏中的****受众**** 下拉列表。 2. 单击****列表和段****。 3. 单击右上角的****新建****。 4. 选择****创建分段****。 5. 为您的分段命名并根据需要选择标签。 6. 在“定义”下，选择 ****某人已完成（或未完成）的操作**** > ****签名**** ****向上**** > ****至少一次**** > ****最近**** > ****30**** > ****天****。 7. 单击****创建段****。 ## 在流程中使用 PAR Punchh 数据

您可以使用 PAR Punchh 指标和对象来触发流。例如，您可以使用 **注册** 指标来触发当有人注册您的忠诚度计划时发送的流。您可以使用 Punchh 指标和对象来触发流程或自动化操作序列。 Klaviyo 使用 Punchh 数据提供多个预构建流程。要查看这些预构建的流程：

1. 在 Klaviyo 中，选择“流程”选项卡。 2. 单击创建流。 3. 按 **Punchh** 过滤以查看所有 Punchh 流。 ![三个输入字段：“搜索流”、“Punchh”过滤器和“选择频道”。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/e1494ff41321d84fd536a407838a3e2ee8f12be7-1818x150.png)

   您还可以从头开始创建自己的流程。例如，当某人注册您的忠诚度计划时，您可以立即向他们发送消息。要使用 PAR Punchh 指标创建流：
4. 从左侧导航侧栏导航至****Flows**** 选项卡。 5. 单击右上角的****创建流程****。 6. 单击右上角的****构建您自己的****。 7. 为流程命名并根据需要选择标签，然后单击****创建流程****。 8. 在流程构建器中，在 **选择触发器** 下，选择 ****您的指标****。 9. 选择 ****Punchh****，然后选择 Punchh 指标，例如 ****Signed Up****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32789674240539)

7. 单击****保存****。 8. 添加与触发操作相关的时间延迟和消息。详细了解[创建欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172)。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32842710057115)

9. 内容准备就绪后，单击流程构建器右上角的“****更新操作状态****”以将流程设置为活动状态。 ## 结果

现在，您已将 PAR Punchh 与 Klaviyo 集成，并了解了 Klaviyo 中的 PAR Punchh 数据、使用 PAR Punchh 数据对客户进行细分以及在流程中使用 PAR Punchh 数据。