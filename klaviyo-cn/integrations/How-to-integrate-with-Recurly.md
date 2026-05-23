---
id: "115005082207"
title: "如何与 Recurly 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005082207-How-to-integrate-with-Recurly"
section: "Recurly"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:20Z"
language: "zh"
---
## 你将会学到

了解如何将 Recurly 与 Klaviyo 集成，以便根据客户的发票和付款数据个性化和定位电子邮件。 Klaviyo 从 Recurly 同步以下数据：

- 开具发票时，以及每张发票中包含的项目
- 客户付款失败、退款或成功付款时的付款信息
- 与循环信息相关的配置文件属性

## Recurly 与 Klaviyo 集成

1. 要将 Recurly 与 Klaviyo 集成，您需要 Recurly API 密钥，因此首先登录您的 Recurly 帐户。 2. 导航至****集成 > API 凭证****。 3. 复制 ****Default API Key**** 下的 Private API Key 供以后使用。私有 API 密钥（例如此处使用的默认密钥）应像密码一样对待；将它们保存在安全的地方，切勿将其暴露给公众。 ![Recurly 中的默认 API 密钥部分，私有 API 密钥已模糊](https://klaviyo.zendesk.com/hc/article_attachments/28715962324763)
4. 如果您的默认 API 密钥已在其他第三方集成中使用，您可以通过单击****添加私有 API 密钥****为 Klaviyo 集成生成新的默认 API 密钥。 ![循环中的私有 API 密钥显示默认 API 密钥模糊，并在底部添加带有灰色背景的私有 API 密钥](https://klaviyo.zendesk.com/hc/article_attachments/28715968889883)

   Recurly 只会生成 5 个私有 API 密钥来与第三方应用程序集成。 5. 如果您创建了新的 API 密钥，请将其复制以在您的 Klaviyo 帐户中使用。 6. 在您的 Klaviyo 帐户中，选择****集成****选项卡。 7. 单击****探索应用程序****，搜索**Recurly**，然后单击该卡。然后，单击****安装****。 8. 输入您的 Recurly 子域和之前复制的 API 密钥，然后单击****连接到 Recurly****。 ****！[](https://klaviyo.zendesk.com/hc/article_attachments/28715962340123)****
9. 如果集成成功，将会出现成功消息。 ## 监控循环同步

您可以监控从 Recurly 到 Klaviyo 的数据同步。 1. 在 Klaviyo 中，单击****分析****下拉列表，然后选择****指标****。 2. 搜索 Recurly 指标之一，例如 **已签发的发票**，然后单击“活动源”图标。 ![显示通过 Klaviyo 中的 Recurly 指标开具发票列表并带有时间戳的页面](https://klaviyo.zendesk.com/hc/article_attachments/28715968896155)
3. 如果您的集成已开始同步数据，您将开始看到添加到此活动源的 **已签发发票** 事件以及 Recurly 图标。 4. Klaviyo 导入您的所有 Recurly 数据，为了验证这一点，您可以将特定日期的成功付款数量与 Recurly 中的数据进行比较，并确认它们匹配。 5. 如果数据不匹配，问题很可能是您的 Klaviyo 帐户中的时区与您的 Recurly 帐户中的时区不匹配。 6. 要检查您在 Klaviyo 的时区设置：
   - 单击左下角您的帐户名。 - 选择****设置****。 - 选择****组织****，然后向下滚动到**时区**。 ## 数据从 Recurly 同步到 Klaviyo

### 指标

将以下指标重复同步到 Klaviyo：

- ****付款失败****
  每次通过 Recurly 进行的付款被标记为失败时都会记录。 - ****开具发票****
  每次通过 Recurly 向客户开具发票时都会进行记录。 - ****订购的产品****
  每次客户通过 Recurly 下订单时都会记录。 - ****退款****
  当您通过 Recurly 退款时记录。 - ****支付成功****
  每次客户通过 Recurly 成功支付发票时都会进行记录。 ![Klaviyo 中的“指标”选项卡由 Recurly 过滤，包含付款失败和问题发票等指标](https://klaviyo.zendesk.com/hc/article_attachments/28715962335259)

### 配置文件属性

以下属性从 Recurly 同步到 Klaviyo 配置文件：

- 循环帐户代码
- 循环卡到期日期
- 循环计划代码
- 循环计划

## 结果

您已完成 Recurly 与 Klaviyo 的集成，并验证了您的同步数据。现在，您可以根据客户的发票和付款数据来个性化和定位电子邮件。 ## 其他资源

- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [分段入门](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [Klaviyo 和应用程序之间交换的数据类型参考](https://help.klaviyo.com/hc/en-us/articles/360030696012)