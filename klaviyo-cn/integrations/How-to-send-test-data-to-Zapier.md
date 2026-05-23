---
id: "4407493023131"
title: "如何将测试数据发送到 Zapier"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4407493023131-How-to-send-test-data-to-Zapier"
section: "Custom integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:59Z"
language: "zh"
---
## 你将会学到

了解在创建 Webhook 以向 Klaviyo 发送电子邮件和短信同意时如何通过 POST 请求向 Zapier 发送测试数据。

本文基于[如何通过 Zapier 向 Klaviyo 发送同意书](https://help.klaviyo.com/hc/en-us/articles/4407486310683) 中的信息。

## 创建 POST 请求

在测试触发器之前，您需要通过 POST 请求将测试数据发送到您的 webhook。下面列出的步骤解释了如何通过 Postman 发出 POST 请求，但欢迎您使用任何您喜欢的程序。

1. 复制 Zapier 生成的 Webhook URL。
2. 在Postman 中，单击****新建**** 开始新请求。
3. 从 **新建** 菜单中选择 **HTTP 请求****。
   ![Postman 的“创建新请求”菜单，在“构建块”部分下显示 HTTP 请求](https://klaviyo.zendesk.com/hc/article_attachments/28717851667739)
4. 将您之前复制的 Zapier Webhook URL 粘贴到 URL 框中。
5. 从 Webhook URL 左侧的下拉列表中选择 ****POST****。
   ![Postman 设置为创建 POST 请求，从下拉列表中选择 POST，并将 Zapier webhook URL 输入到 URL 框中](https://klaviyo.zendesk.com/hc/article_attachments/28717851660955)
6. 选择****Body**** 选项卡，选择****form-data**** 单选按钮，然后输入下表中的密钥和适当的测试数据。确保[电话号码格式正确](https://help.klaviyo.com/hc/en-us/articles/360046055671)。测试 Webhook 时，您需要使用真实的电话号码，以便将个人资料添加到您的列表中。
   ![邮差表单数据正文设置，用于姓名、电子邮件、电话号码和短信同意](https://klaviyo.zendesk.com/hc/article_attachments/28717851672219)

   |  |  |
   | --- | --- |
   | ****关键**** | ****价值**** |
   | `名称` | <测试名称> |
   | `电子邮件` | <测试电子邮件> |
   | `电话号码` | <测试电话号码> |
   | `短信同意` |真实|
7. 点击****发送****，将测试数据发送至Zapier。
8. 如果 POST 请求成功，您将在响应中看到行 `"status": "success"`。

![Postman POST请求响应，显示响应成功](https://klaviyo.zendesk.com/hc/article_attachments/28717851675163)

现在您可以返回 Zapier 并完成 webhook 设置过程。