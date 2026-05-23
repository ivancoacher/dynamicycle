---
id: "46643094275099"
title: "如何将 Klaviyo 现场跟踪添加到您的预订引擎"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/46643094275099-How-to-Add-Klaviyo-Onsite-Tracking-to-Your-Booking-Engine"
section: "General"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-09T15:57:35Z"
language: "zh"
---
本指南将引导您使用 ****Klaviyo Hotels Tag**** 将 ****Google Tag Manager (GTM)**** 与您的物业管理系统（Mews、Cloudbeds 或 Guesty）集成。完成此设置后，您将能够直接在您的 Klaviyo 帐户中跟踪关键网站访问者行为，例如 ****活跃现场、**** ****查看列表、**** 和 ****开始结账****。这将使您能够轻松设置创收自动化，例如浏览放弃和放弃的购物车流程，并创建高度针对性的细分。 ****在开始之前，如果您还没有 Google 跟踪代码管理器帐户，请按照 Google 的**** [****指南****](https://support.google.com/tagmanager/answer/14842164?hl=en) ****了解如何设置帐户。****

---

## 步骤 1：找到您的 GTM 容器 ID

在开始之前，您需要确定要使用的特定容器。 1. 登录您的 [Google 跟踪代码管理器](https://tagmanager.google.com/) 帐户。 2. 选择与您酒店网站关联的****Container****。 3. 在窗口顶部的“提交”和“预览”按钮旁边，您将看到您的****容器 ID****（看起来像“GTM-XXXXXXX”）。 4.****将此 ID**** 复制到剪贴板。 ![0.9.png](https://klaviyo.zendesk.com/hc/article_attachments/46643062813851)

---

## 步骤 2：将 GTM 连接到您的物业管理系统 (PMS)

您需要告诉您的预订引擎“监听”您的 GTM 容器。请按照以下适合您的特定平台的步骤操作：

### 对于云床

1. 登录 Cloudbeds。 2. 单击****帐户图标**** > ****设置 > 预订引擎****。 3. 选择****分析****选项卡****.****
4. 将您的****容器 ID**** 粘贴到 GTM 字段中并保存。 ![2.png](https://klaviyo.zendesk.com/hc/article_attachments/46643062816923)

有关更多说明，请遵循 [Cloudbeds 指南](https://myfrontdesk.cloudbeds.com/hc/en-us/articles/25825202111387-Connect-Google-Analytics-with-Cloudbeds-Booking-Engine)。 ### 对于马厩

1. 登录Mews。 2. 转到****设置 > 服务****。 3. 选择可预订服务。 4. 单击****预订引擎****。 5. 选择您想要使用 Google 跟踪代码管理器跟踪的预订引擎。 6. 在 ****Google 标签管理器 ID**** 下，粘贴您的 ****容器 ID。****
7. 单击****保存****。 ![3.png](https://klaviyo.zendesk.com/hc/article_attachments/46643094244763)

有关更多说明，请遵循 [Mews 指南](https://help.mews.com/s/article/google-tag-manager)。 ### 对于客人

1. 要在您的站点上安装代码：
2. 登录Guesty。 3. 选择顶部的****操作****下拉菜单，然后选择****增长 > 分布****。 5.![](https://klaviyo.zendesk.com/hc/article_attachments/46643062822683)
6. 选择****宾客预订引擎****。 7. 单击预订引擎旁边的三个点，然后选择****编辑预订引擎****。 8. 滚动到 **Web 分析** 部分并经过您的 ****容器 ID****。 10. ![4.png](https://klaviyo.zendesk.com/hc/article_attachments/46643062823963)
11. 选择****保存预订引擎。****

如需更多说明，请遵循[宾客指南](https://help.guesty.com/hc/en-gb/articles/16714065345821-Using-analytics-tools-in-your-Guesty-Booking-Engine)。 ---

## 步骤 3：在 GTM 中添加 Klaviyo Hotels 模板

现在 GTM 已连接到您的 PMS，您需要添加 Klaviyo 特定的跟踪逻辑。 1. 返回 Google 跟踪代码管理器，单击左侧边栏上的****模板****。 2. 在****标签模板****部分中，单击****搜索库****。 3. 搜索****“Klaviyo 酒店标签”****。 ![6.png](https://klaviyo.zendesk.com/hc/article_attachments/46643094254363)
4. 选择模板并单击****添加到工作区****。 5. 再次单击****添加****进行确认。 ---

## 步骤 4：创建并配置您的标签

此步骤将模板连接到您的特定 Klaviyo 帐户。 1. 转到左侧边栏的****标签****，然后单击****新建****。 2. ****为您的标签命名****（例如“Klaviyo Hotels Tracking”）。 3. 单击****标签配置****并选择您刚刚添加的****Klaviyo Hotels Tag****。 4. ****输入您的 Klaviyo 公共 API 密钥：**** 这是在您的 Klaviyo 帐户设置中找到的 6 个字符标识符（请参阅我们的[查找公共密钥指南](https://help.klaviyo.com/hc/en-us/articles/115005062267)）。 5. ****选择您的 PMS：**** 从下拉菜单中选择 Mews、Cloudbeds 或 Guesty。 6.![](https://klaviyo.zendesk.com/hc/article_attachments/46643062833051)
7. ****设置触发器：**** 将鼠标悬停在 ****触发**** 部分。 单击右上角出现的铅笔。选择****所有页面****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/46643094261531)
8. 为标签命名（例如 [Cloudbeds/Mews/Guesty] 标签）。单击****保存****。 ---

## 步骤 5：发布您的更改

在您提交这些更改之前，您的跟踪不会生效。 1. 点击GTM右上角的蓝色****提交****按钮。 ![10.png](https://klaviyo.zendesk.com/hc/article_attachments/48511182753179)
2. 为您的版本命名（例如“添加了 Klaviyo 酒店跟踪”）。 3. 单击****发布****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/46643062844187)

---

## 接下来会发生什么？发布后，标签将自动开始向 Klaviyo 发送活动数据，以识别预订引擎上已识别的访客。 [了解 Klaviyo 可以在此处追踪的人](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACVVC4BXQ0ES5Y50TC)。您可以通过检查 Klaviyo 帐户中的“指标”选项卡中的以下事件来验证是否正在跟踪事件：

- ****活跃现场：**** 当有人在网站上活跃时触发。 - ****查看的列表：**** 当旅行者查看特定房间或房产时触发。 - ****开始结帐：**** 当旅客进入预订流程时触发。现在，您可以使用浏览放弃和放弃购物车流程模板，在选择 PMS 集成后可以在[此处](https://www.klaviyo.com/flows/create) 找到这些模板。但这只是开始 - 了解更多有关 Klaviyo 现场跟踪的信息 [此处](https://help.klaviyo.com/hc/en-us/articles/115005076767)！