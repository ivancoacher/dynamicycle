---
id: "115005082267"
title: "开始使用条纹"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005082267-Getting-started-with-Stripe"
section: "Stripe"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: "zh"
---
## 你将会学到

了解如何将 Stripe 与 Klaviyo 集成，以便根据客户的发票和付款数据个性化和定位电子邮件。您将通过 2 个步骤设置 Stripe 集成。首先，您将通过在 Klaviyo 中启用集成来连接 Stripe。然后，您在 Stripe 中设置 Webhooks，这将使特定 Stripe 数据实时同步到 Klaviyo 中。以下是我们从 Stripe 同步的数据的概述：

- 开具发票时，以及每张发票中包含的项目
- 用户支付失败、退款、支付成功时的支付信息

## 在 Klaviyo 中启用 Stripe 集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 选择****探索应用程序****，搜索**Stripe**，然后单击该卡。 3. 然后，单击****安装****。 4. 单击****连接到 Stripe****。这会将您带到 Stripe 的网站 - 如果需要请登录。 5. 选择您想要连接到 Klaviyo 的 Stripe 帐户，然后单击****连接****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720667423771)
6. 回到 Klaviyo，您可以选择通过输入签名密钥来验证 Stripe webhooks（推荐）。这可以在 Stripe 的 ****Developers > Webhooks**** 下找到，并且将为您的集成增加额外的安全级别。 ![条带集成配置页面。](https://klaviyo.zendesk.com/hc/article_attachments/28720667432987)
7. 复制此页面中的 Webhook URL。这将在下一部分中粘贴到您的 Stripe 帐户中。 8. 单击****完成设置****。 ## 设置 Stripe webhook

现在我们将设置您的 Stripe webhooks，这将使您能够实时同步 Stripe 数据。 1. 在新选项卡中打开 Stripe，然后导航到 ****Developers**** 选项卡。 2. 选择****Webhooks****，然后单击****添加端点****。 ![Stripe 中的 Webhooks 选项卡显示带有添加端点按钮的端点部分](https://klaviyo.zendesk.com/hc/article_attachments/28720667411867)
3. 填写以下字段：
   - ****端点 URL****
     粘贴您刚刚从 Klaviyo 复制的 URL。 - ****版本****
     选择最新的API版本。 - ****要发送的事件****
     Klaviyo 需要费用和发票数据点。在 **要发送的事件** 下拉列表中，选择所有 **收费** 和 **发票** 事件。您可以选择忽略所有 **charge.dispute** 事件。为以下所有事件创建端点：
     - 电荷.捕获
     - 收费.过期
     - 充电失败
     - 收费待定
     - 收费.退款
     - 充值成功
     - 充电.更新
     - 发票.创建
     - 发票.已删除
     - 发票.最终确定
     - 发票.marked\_uncollectible
     - 发票.付款\_action\_required
     - 发票.付款\_失败
     - 发票.付款\_成功
     - 发票.已发送
     - 即将推出的发票
     - 发票.更新
     - 发票作废
4. 选择所有费用和发票事件后，选择****添加端点****。 ![添加包含完整事件列表的 Webhook 端点并添加带有紫色背景的端点](https://klaviyo.zendesk.com/hc/article_attachments/28720667409691)
5. 您将收到网络钩子已启用的确认信息。 ![Stripe webhook 页面，状态“已启用”以绿色突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28720667414043)
6. 您的 Stripe 集成现已启用。 ## 查看从Stripe同步的数据

要检查您启用的集成：

1. 单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****。 2. 找到 Stripe 的 **成功支付** 指标，然后单击 ****活动源**** 图标。 ![Klaviyo 中 Stripe 成功支付指标的活动源](https://klaviyo.zendesk.com/hc/article_attachments/34455209929883)
3. 如果您的集成已开始同步数据，您将在此处看到通过 Stripe 开具的发票。当您的集成完全同步后，Stripe 集成将在您的 Klaviyo 帐户中的旁边显示绿色边框。 Klaviyo 导入您的所有 Stripe 数据。要验证这一点，您可以将特定日期的成功付款数量与 Stripe 界面中的数量进行比较，并确认它们匹配。 4. 例如，单击 **成功支付** 指标的****图表****标题。该图表默认显示最近 30 天的数据。将鼠标悬停在昨天的数据点上，或者查看图表下方的数据表，了解您昨天有多少笔付款。将该数字与 Stripe 中存储的数字进行比较，您应该会看到它们完全匹配。 5. 如果数据不匹配，问题很可能是您的 Klaviyo 帐户中的时区与您的 Stripe 帐户中的时区不匹配。要检查您在克拉维约的时区设置：
   - 单击左下角您的帐户名。 - 选择然后单击****设置**** ****> 组织****。 - 向下滚动到**时区**。 ## Stripe 指标

Stripe 将以下指标同步到 Klaviyo：

- 付款失败
- 开具发票
- 退款
- 支付成功

![Klaviyo 中的“指标”选项卡由 Stripe 过滤，指标包括付款失败和开具的发票](https://klaviyo.zendesk.com/hc/article_attachments/28720622067739)

### 支付失败

每次通过 Stripe 进行的付款被标记为失败时，都会记录此指标。使用此指标来定位付款失败的客户，让他们知道他们有逾期余额。您可以根据以下条件过滤和定位失败付款事件：

- ****AttemptCount**** 此发票尝试向用户收费的次数。 - ****币种****支付失败的发票币种，例如**美元**、**英镑**。 - ****发票****此失败付款在 Stripe 中关联的发票。 - ****原因**** Stripe 中此付款失败的原因，例如，**您的卡已过期**、**您的卡被拒绝**。 ### 已开具发票

每次通过 Stripe 向您的客户开具发票时都会记录此指标。使用此指标对已开具发票但尚未付款或付款失败的客户进行细分。它还可用于触发分段以通知客户即将付款。 ### 已退款

该指标记录您通过 Stripe 退款时的事件。您可以根据以下条件过滤和定位退款事件：

- ****金额****退款的金额。 ### 支付成功

每次客户通过 Stripe 成功支付发票时都会记录此指标。这些事件包括有关您的客户、他们的发票以及发票中的产品的数据。使用此指标可在客户付款后向其发送自动发票，或在电子邮件流中发送自动发票，以确定客户何时在您的网站上处于活动状态，但尚未为您的产品或服务付款。然后，您可以向这些用户发送电子邮件，提供在您的网站上购物的折扣。您可以根据以下条件过滤和定位成功支付的事件：

- ****货币****支付发票的货币，例如**美元**、**英镑**。 - ****发票****此付款在 Stripe 中关联的发票。 ## 客户数据

Klaviyo 通过电子邮件地址唯一地识别每个人。如果 Stripe 将客户数据与新电子邮件地址同步，Klaviyo 将创建一个包含客户电子邮件地址和关联 Stripe 指标的新配置文件。信用卡到期日期作为自定义属性存储在客户的个人资料中。必须发生上面列出的 Stripe 事件之一才能在 Klaviyo 中创建配置文件。 ## 在 Klaviyo 中使用 Stripe 数据

任何 Stripe 指标或元数据都可用于触发 Klaviyo 中的流。 ### 自动发票

您可以通过设置由 Stripe 的 **成功支付** 指标触发的发票流，在客户付款后自动将发票收据发送给他们。 ![Klaviyo 流程生成器中由成功支付触发的流程](https://klaviyo.zendesk.com/hc/article_attachments/28720622098843)

此流程可以使用引用 Stripe 付款属性的模板标签自动填充显示动态付款详细信息的电子邮件。有关将动态数据嵌入电子邮件模板的更多信息，请参阅我们关于[模板标签和变量语法](https://klaviyo.zendesk.com/hc/en-us/articles/115005084927)的文章。 ### Stripe 支付失败流程

通过由 Stripe **失败付款** 指标触发的自动流程，提醒您的客户付款失败。 ![Klaviyo 流程构建器中由支付失败触发的流程](https://klaviyo.zendesk.com/hc/article_attachments/28720622094235)

## 故障排除

### 我没有看到 Stripe 中的所有活动都同步到 Klaviyo。 Stripe 事件无法同步到 Klaviyo 的最常见原因是没有与该事件关联的电子邮件地址。由于 Klaviyo 使用电子邮件地址来唯一标识一个人，因此我们无法为未与电子邮件地址关联的人创建个人资料。 同样，如果事件未与电子邮件地址关联，则 Klaviyo 无法将事件链接到个人资料。请记住，名字和姓氏输入不一定一致或唯一，因此我们不会仅根据此信息创建个人资料。这样做可能会导致重复和不准确的跟踪。如果即使关联了电子邮件地址，您仍然没有看到 Stripe 数据同步到 Klaviyo，请联系[我们的支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272)。 ## 结果

您现在已经将 Stripe 与 Klaviyo 集成，并了解了如何使用同步数据。 ## 其他资源

- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [分段入门](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [了解 Klaviyo 和应用程序之间交换的数据类型](https://help.klaviyo.com/hc/en-us/articles/360030696012)