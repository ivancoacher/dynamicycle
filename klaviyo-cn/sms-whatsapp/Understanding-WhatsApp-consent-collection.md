---
id: "40116301104539"
title: "了解 WhatsApp 同意收集"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40116301104539-Understanding-WhatsApp-consent-collection"
section: "Getting started with WhatsApp"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-05-11T12:54:30Z"
language: "zh"
---
了解如何收集同意发送 WhatsApp 消息，包括可用的方法和最佳做法。 ## Meta (WhatsApp) 选择加入要求

要通过 WhatsApp 向客户发送消息，企业必须遵守 Meta 的 WhatsApp 商业消息传递政策。企业在通过 WhatsApp 向人们发送消息之前必须获得选择加入许可。 ### 什么是有效的选择加入

仅当满足以下两项条件时，才可以通过 WhatsApp 联系客户：

- 客户已提供手机号码
- 企业已收到明确的选择加入许可，确认客户希望接收来自该特定企业的消息或电话

该许可必须有效且符合当地法律。 ### 收集选择加入的要求

在收集选择加入许可时，企业必须确保：

- 很明显，客户选择接收通信
- 清楚地注明公司名称，以便客户知道他们选择接收谁的消息
- 选择加入方法符合所有适用的当地法律和法规

企业有责任维护选择加入的记录，并确保持续遵守 Meta 的 [WhatsApp Business Messaging政策](https://business.whatsapp.com/policy?fbclid=IwY2xjawPM6lJleHRuA2FlbQIxMABicmlkETFGWE8zTm5iUG1Mb0tCaXl2c3J0YwZhc HBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHoG09ahzu-ZnkZ0n8iAO9vfZC2SKMaBKDg8YQ-hlLjaUu1nSMedgy0Vwo2nO_aem_OvOB23fZQ5hV4BWV0s7NRQ）。有关更多信息，请参阅 Meta 的[帮助文档](https://developers.facebook.com/documentation/business-messaging/whatsapp/getting-opt-in)。 ## WhatsApp 消息的类型和同意

WhatsApp 将其消息分为 4 类。 | ****消息类型**** | ****在克拉维约可用吗？**** | ****需要明确同意吗？**** |
| --- | --- | --- |
|营销（Klaviyo 中也称为“促销”）|是的 |是的 |
|实用程序（在 Klaviyo 中称为“事务性”）|是的 |是的 |
|支持|是的 |不适用 |
|认证|没有 |不适用 |

在大多数情况下，您需要[明确同意](https://help.klaviyo.com/hc/en-us/articles/4404203889947) 才能发送 WhatsApp 消息，这意味着有人必须直接告诉您他们希望接收来自您品牌的某些消息。 ### 收集 WhatsApp 同意的最佳做法

一些做法是：

- 永远不要假设你已经得到某人的同意。 - 如果某人同意使用其他渠道（例如注册短信）或提供其电话号码，这与同意接收 WhatsApp 消息不同。 - 无论您在何处征得 WhatsApp 同意，都应包含明确的披露语言。 - 这包括表格、您的网站、电子邮件等。 - 发送前验证电话号码（即，使用双重确认来确认该号码是真实的并且属于注册人）。 ****在收集 WhatsApp 的同意时是否需要使用披露语言？****

在增加 WhatsApp 列表时，建议使用披露（也称为免责声明）语言，但不是必需的。一般来说，在收集任何类型的同意时，披露语言是最佳做法。它告诉潜在订阅者他们将注册什么内容，因此不会产生混乱或错误的期望。然而，真正需要披露语言的唯一渠道是短信。 ## 收集 WhatsApp 同意的方法

您可以通过多种方式扩大 WhatsApp 订阅者名单：

- 克拉维约形式
- 关键字
- 克拉维约 API
- WhatsApp订阅链接或二维码

### 构建注册表单

通过创建注册表单，您可以要求您网站上的任何人同意使用 WhatsApp。如果您想将 WhatsApp 添加到表单：

1. 导航至****注册表单****选项卡。 2. 找到您要更新的表单。 3. 单击右侧的****3 个垂直点****。 4. 从下拉列表中选择****编辑****。 ![突出显示编辑的表单下拉列表](https://klaviyo.zendesk.com/hc/article_attachments/40772365929371)

#### 选项 1：添加新步骤

- 单击****+步骤****。 - 选择****移动选择加入****，然后单击****下一步****。 - 选择****WhatsApp****。 - 选择您要添加订阅者的列表，然后单击****添加步骤****。 - 要同时收集短信同意，请单击****电话号码****块，打开****频道****下拉列表，然后选择****WhatsApp****。 - 最后，添加一个同意下拉字段，其中包含以下选项：促销、交易或两者

#### 选项 2：添加新块（电话号码块）

- 选择****添加块****。 - 拖入****电话号码****块。 #### 选项 3：添加新块（按钮块 - 点击文本表单）

使用****按钮块****而不是电话号码块可以使订阅尽可能简单。只需单击一下，订阅者即可直接进入 WhatsApp，并收到****预先填写的选择加入消息****，因此他们所需要做的就是点击****发送****进行确认。 - 选择****添加块****。 - 拖入****Button**** 块。 - 将操作设置为****订阅 WhatsApp****。 - 查看****预先填写的消息****并选择订阅者将发送的****订阅关键字****以确认同意。最后，选择****发布****以生效您的更改！ ### 使用关键字

您可以添加****关键字****，以便人们更轻松地选择加入。例如，您可以将关键字与您的 WhatsApp 号码一起发布，以便发送该关键字的任何人都将注册接收您的 WhatsApp 营销消息。您还可以将关键字添加到您的 WhatsApp Business 帐户中配置的****订阅链接****。当有人点击链接并发送带有关键字的预填充消息时，他们将自动订阅。您可以随时在 ****WhatsApp 设置**** 中创建或编辑关键字。 ### 通过API收集

您可以通过在 API 调用中包含 WhatsApp，使用 API 调用来收集同意，类似于电子邮件和短信。 ````
“whatsapp”：{
  “营销”：{
    “同意”：“已订阅”，
    “consented_at”：“2025-01-01T00:00:00+00:00”
  }
  “交易”：{
    “同意”：“已订阅”，
    “consented_at”：“2025-01-01T00:00:00+00:00”
  }
}
````

- 完整的curl请求示例

````
卷曲--位置
'<https://a.klaviyo.com/api/profile-subscription-bulk-create-jobs>' \\
--header '授权：Klaviyo-API-Key <私钥>' \\
--header '接受：application/vnd.api+json' \\
--header '内容类型：application/vnd.api+json' \\
--header '修订：2024-10-15' \\
--数据'{
    “数据”：{
        “类型”：“个人资料订阅批量创建作业”，
        “属性”：{
            “个人资料”：{
                “数据”：[
                    {
                        “类型”：“个人资料”，
                        “属性”：{
                            "phone_number": "+18573905002",
                            “订阅”：{
                                “whatsapp”：{
                                    “营销”：{
                                        “同意”：“已订阅”，
                                        “同意”：
                                        “2025-01-01T00:00:00+00:00”
                                    },
                                    “交易”：{
                                        “同意”：“已订阅”，
                                        “同意”：
                                        “2025-01-01T00:00:00+00:00”
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            “历史导入”：true
        }
    }
}'
````

了解如何[通过 API 收集渠道同意](https://developers.klaviyo.com/en/docs/collect_email_and_sms_consent_via_api)。 ### 创建 WhatsApp 订阅链接或二维码帐户

如果您登录 WhatsApp Business 帐户，您可以创建链接或二维码，以便人们轻松订阅。您可以在电子邮件中添加此链接，将该链接用作表单中的按钮，或在名片上打印二维码。 ![WhatsApp 中的订阅链接](https://klaviyo.zendesk.com/hc/article_attachments/40772397275035)

## 后续步骤

- [导入 WhatsApp 同意](https://help.klaviyo.com/hc/en-us/articles/40116243735579)
- [验证您的 WhatsApp 帐户](https://help.klaviyo.com/hc/en-us/articles/40116148219163)