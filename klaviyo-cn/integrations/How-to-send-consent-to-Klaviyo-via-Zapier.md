---
id: "4407486310683"
title: "如何通过 Zapier 向 Klaviyo 发送同意书"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4407486310683-How-to-send-consent-to-Klaviyo-via-Zapier"
section: "Migrate from an SMS platform"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:59Z"
language: "zh"
---
## 你将会学到

了解如何创建自定义 Zapier Webhook 以向 Klaviyo 发送短信同意。您还可以轻松修改本指南中的说明以发送电子邮件同意书。以下步骤将帮助您使用触发 Python 脚本操作的 Webhook（也称为 catch hook）创建 Zap。该脚本向 Klaviyo 发送 API 调用，以将电子邮件和电话号码订阅到列表。此功能仅适用于拥有 Premium Zapier 计划的用户。 ## 关于集成

Klaviyo 并不完全支持此集成，但如果需要，可以将其用作解决方法。我们建议仅当您的团队中有可以支持此集成的开发人员时才使用此集成。本指南使用 Zapier 代码操作，该操作在检测到触发器时运行 Python 脚本。通过此解决方案，您可以将字段映射到 Klaviyo 端点所需的数据类型；具体来说，[订阅配置文件](https://developers.klaviyo.com/en/reference/subscribe_profiles)和[取消订阅配置文件](https://developers.klaviyo.com/en/reference/unsubscribe_profiles)端点。 ## 设置 Zapier webhook

1. 登录您的 Zapier 帐户。 2. 在 Zapier 的主页中，选择****+创建****，然后选择****Zap****。 3. 输入新 Zap 的名称（例如 Klaviyo Webhook）。 4. 搜索 **Webhook**，然后从“触发器”菜单中选择****Webhooks by Zapier****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717383531547)
5. 在下一个菜单中，从 **Trigger Event** 选项中选择 ****Catch Hook****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717389841051)
6. 单击****继续****。 7. 选择****测试****选项卡。 8. 复制 Zapier 提供的 Webhook URL，以便您将请求发送到。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717383537947)
9. 在测试之前，您需要将测试数据发送到您的 webhook。有关更多信息，请参阅我们的[如何将测试数据发送到 Zapier](https://help.klaviyo.com/hc/en-us/articles/4407493023131-How-to-Send-Test-Data-to-Zapier) 指南。发送测试数据时，请确保[电话号码格式正确](https://klaviyo.zendesk.com/hc/en-us/articles/360046055671)。 10. 将测试数据发送到 Webhook 后，单击****测试触发器****（在****测试****选项卡上）。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717389848475)
11. 如果请求成功，您将看到一条成功消息，并且测试数据将填充在成功消息下方，类似于以下示例：
    ![](https://klaviyo.zendesk.com/hc/article_attachments/28717389853211)
12. 触发器工作后，单击****继续选择记录****。 ## 设置 Zapier 操作

1. 在“操作”菜单中，在搜索框中输入****Code by Zapier****，然后从列表中选择选项。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717383547419)
2. 单击****选择事件 > 运行 Python****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717383551259)
3. 单击****继续****。 ## 设置字段映射并创建脚本逻辑

1. 设置字段映射，将下表中的输入数据与您之前发送的正确测试数据相关联。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717389869851)

   |  |  |
   | --- | --- |
   | ****输入数据**** | ****测试数据映射**** |
   | `电子邮件` | 1. 电子邮件：<测试电子邮件> |
   | `电话号码` | 1. 电话号码：<测试电话号码> |
   | `短信同意` | 1. 短信\_同意：true |
   | `名称` | 1. 姓名：<测试名称> |
2. 将如下所示的脚本添加到代码框中：

   ````
   导入请求

   # 配置短信订阅或取消订阅呼叫
   if (input_data["sms_consent"] == "true" 或 input_data["sms_consent"] == "True" 或 input_data["sms_consent"] == "TRUE"):
     url =“https://a.klaviyo.com/api/profile-subscription-bulk-create-jobs/”有效负载={“数据”：{
           “类型”：“个人资料订阅批量创建作业”，
           “属性”：{
               “配置文件”：{“数据”：[
                       {
                           “类型”：“个人资料”，
                           “属性”：{
                               “电子邮件”：input_data[“电子邮件”]，
                               “电话号码”：输入数据[“电话号码”]，
                               “订阅”：{
                                   "sms": { "营销": { "同意": "订阅" } }
                               }
                           }
                       }
                   ] }
           },
           “关系”：{ “列表”：{ “数据”：{
                       “类型”：“列表”，
                       “id”：“LIST_ID”
                   } } }
       } }

   elif (input_data["sms_consent"] == "false" 或 input_data["sms_consent"] == "False" 或 input_data["sms_consent"] == "FALSE"): url = "https://a.klaviyo.com/api/profile-subscription-bulk-delete-jobs/"
     有效负载= {“数据”：{
           "type": "个人资料订阅批量删除作业",
           “属性”：{
               “配置文件”：{“数据”：[
                       {
                           “类型”：“个人资料”，
                           “属性”：{
                               “电子邮件”：input_data[“电子邮件”]，
                               “电话号码”：输入数据[“电话号码”]，
                           }
                       }
                   ] }
           },
           “关系”：{ “列表”：{ “数据”：{
                       “类型”：“列表”，
                       “id”：“LIST_ID”
                   } } }
       } }
   标题= {
       “接受”：“应用程序/json”，
       “修订”：“2024-05-15”，
       “内容类型”：“应用程序/json”，
       “授权”：“Klaviyo-API-Key your-private-api-key”
   }

   响应 = requests.post(url, json=payload, headers=headers)

   # Zapier 需要一个“输出”对象
   输出 = {“响应文本”：response.text}
   ````
3. 将 `your-private-api-key` 替换为您的 Klaviyo 私有 API 密钥。像对待密码一样对待私有 API 密钥 - 将它们保存在安全的地方，并且永远不要向公众公开。 4. 将“LIST_ID”（两个位置中的）替换为您要将 Zapier 数据发送到的 Klaviyo 列表 ID。您可以通过导航至****受众 > 列表和细分 > 设置**** 在 Klaviyo 中找到您的列表 ID。如果您希望立即订阅人员而无需确认（这在测试期间可能会有所帮助），请确保您的列表设置为单一选择加入（可在列表设置中的“**同意**”选项卡下找到）。 5. 单击****继续****，然后单击****测试步骤****。 6. 如果测试成功，您将看到没有错误的响应，如下所示：
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717383558299)
7. 您还可以通过导航到列表并确保配置文件已添加来检查 Klaviyo 中的测试是否成功。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717389862939)
8. 测试成功后，单击****发布**** 发布您的 zap。如果您的测试不成功，请查看我们的[故障排除提示](#TroubleshootingTips) 了解常见问题。 ## 故障排除技巧

以下是您在设置 Zapier Webhook 时可能遇到的常见问题。如果您遇到任何其他问题，可以联系 [Klaviyo 社区](https://community.klaviyo.com/) 获取进一步指导。 ### 扫描字符串时 EOL

如果您看到此错误，则说明您在变量之一周围缺少引号。检查列表 ID 和私有 API 密钥，确保它们两边都用引号引起来。 ### SyntaxError：语法无效

如果您看到此错误，请删除 Python 代码中的注释（任何以“#”开头的行）。