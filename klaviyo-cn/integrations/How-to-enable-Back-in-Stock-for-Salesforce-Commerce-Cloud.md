---
id: "22495505773083"
title: "如何为 Salesforce Commerce Cloud 启用“返回库存”"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/22495505773083-How-to-enable-Back-in-Stock-for-Salesforce-Commerce-Cloud"
section: "Salesforce Commerce Cloud"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: "zh"
---
## 你将会学到

了解如何为 Salesforce Commerce Cloud (SFCC) 启用 Klaviyo Back in Stock 和变体同步。首先，您将通过添加代码片段确保在 SFCC 集成中启用“返回库存”，这也将启用变体同步。然后，您将使用 Klaviyo 的 API 在您的网站上设置“返回库存”表单。最后，您将在 Klaviyo 中设置“库存补货”流程，向已订阅提醒的客户发送电子邮件。

## 开始之前

如果您尚未将 SFCC 商店与 Klaviyo 集成，您应该首先[集成](https://help.klaviyo.com/hc/en-us/articles/360033744951)，然后跳至本文的 **添加库存表单** 部分。

如果您之前已经将 Klaviyo 与 SFCC 集成，请注意，当您在 SFCC 中启用“返回库存”时，将会发生以下情况：

- 您的 Klaviyo 目录将被重组。之前作为顶级产品同步的变体现在将成为其各自父级产品下的嵌套变体。如果您在任何产品变体的消息传递中使用静态产品块，则需要更新这些块。
- 在添加启用“补货”后的短时间内，您的**畅销产品** Feed 推荐将显示为空，或者可能会推荐不常见的产品。 3 天内，这些建议应该会恢复正常。您可能想要暂停在此期间使用 **最畅销产品** Feed 发送的任何消息。

## 为 SFCC 启用返回库存/变体同步

要将 Klaviyo 的“返回库存”功能与 SFCC 结合使用，您需要将 **/variations** 代码段添加到 OCAPI 数据 API 设置中（如果您尚未这样做）。此代码片段还支持变体同步。为此：

1. 在 SFCC 业务管理器中，导航至****管理 > 站点开发 > 开放商务 API 设置****。
2. 在分配给 Klaviyo 的 client\_id 下，将以下 JSON 添加为类型 **Data** 和上下文 **Global（组织范围内）** 下的列出资源（您应该已经在此处拥有其他代码段）：

   ````
   {
                  "resource_id":"/产品/*/变体",
                  “方法”：[“获取”]，
                  "read_attributes":"(**)",
                  “write_attributes”：“（**）”
   }
   ````

   添加后，设置应类似于以下内容：
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28704487196955)
3. 单击****保存****。

就是这样！下次运行目录同步时（此同步每 8 小时运行一次），您将看到产品变体已同步到您的 Klaviyo 目录。要查看它们：

1. 前往 Klaviyo 中的****内容 >**** ****产品****。
2. 搜索父产品并单击它。
3. 滚动到底部并单击****变体****下拉列表以验证变体是否正确列出。

## 添加退回库存表单

现在，是时候向您的网站添加“补货”按钮和表单，以便您的客户可以请求补货警报。此按钮和随附的表单应显示在缺货产品页面上，提交后，应向我们的 [Back in Stock API](https://developers.klaviyo.com/en/reference/create_back_in_stock_subscription) 提出请求。

请查看我们的开发人员门户，[了解如何向我们的 Back in Stock API 发出客户端请求并为客户订阅电子邮件提醒](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock#client-side-request)。

## 建立您的库存返还流程

最后，您需要创建一个流程来自动向订阅了“库存补货”通知的客户发送消息（通过电子邮件、短信或两者）：

- 查看我们的文章[了解如何设置此流程](https://help.klaviyo.com/hc/en-us/articles/115003872251#h_01HBBYWCR7VMA1Q70QTGAXQBGR)。
- 设置流程时，从流程库中选择 SFCC 的预建 Back in Stock 流程：
  ![](https://klaviyo.zendesk.com/hc/article_attachments/28704487199259)
- 确保[配置您帐户的“退回库存”流程设置](https://help.klaviyo.com/hc/en-us/articles/115003872251#h_01HBBYXYTAXRW86A1XXE4FRV2T)。

## 其他资源

- [SFCC 入门](https://help.klaviyo.com/hc/en-us/articles/360033744951)
- [SFCC数据参考](https://help.klaviyo.com/hc/en-us/articles/360058323811)
- [如何升级 SFCC 墨盒](https://help.klaviyo.com/hc/en-us/articles/16708128591259)