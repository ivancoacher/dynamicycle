---
id: "360046055671"
title: "Klaviyo 中接受的短信电话号码格式"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360046055671-Accepted-phone-number-formats-for-SMS-in-Klaviyo"
section: "Import SMS contacts"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 在导入电话号码进行短信营销时接受哪些电话号码格式。

## 接受的电话号码格式

您可以使用 Klaviyo 的电话号码使用多种不同的格式。

以下内容仅适用于 Klaviyo 的列表导入工具。如果您使用 API 调用，请注意 Klaviyo 仅接受 E.164 格式。

|  |  |  |
| --- | --- | --- |
| ****格式**** | ****没有国家代码的示例**** | ****带有国家/地区代码的示例**** |
| E.164 | 2345678901 | +12345678900 |
| 2-345-678-901 | +12-345-678-900 |
| 2 345 678 901 | +12 345 678 900 |
| RFC3966 |电话：2345678901 |电话：+12345678900 |
| E.123 国家符号 | (234) 567 8901 | (+1234) 567 8900 |
| 2345678901 | +12345678900 |
| E.123国际符号| 2 345 678 901 | +12 345 678 900 |
| 234 567 8901 | +1 234 567 8900 |

导入电话号码时，必须包含国家/地区。一般来说，最好的方法是添加标有“**国家/地区**”的列。

RFC3966 格式由前缀“tel:”组成，后跟数字。数字本身不需要采用特定的格式。

不接受品牌发件人 ID，但您可以通过 SMS 套餐免费获得一个。

## 导入电话号码

为了将同意应用于电话号码，我们建议包括以下列：

- 电子邮件（如果知道）
- 电话号码（必填）
- 国家
- 名字
- 姓氏
- [时间戳](https://help.klaviyo.com/hc/en-us/articles/115005253428)

这样，该文件就包含了所有必要且有用的信息。不仅可以正确应用同意，而且您还可以避免创建重复的配置文件。

有关更多详细信息，请阅读[上传短信联系人列表](https://help.klaviyo.com/hc/en-us/articles/360035428731)。

### 包括一个国家

您必须指明接受短信的电话号码所在的国家/地区。您可以：

- 包括国家/地区栏
  或
- 在电话号码开头添加国家/地区代码
  - 请注意，由于格式问题，您必须在 Google 表格和 Excel 中的加号（例如“+”）前添加撇号。

有关在 CSV 中格式化国家/地区的说明，请参阅[如何在 SMS 导入中包含国家/地区](https://help.klaviyo.com/hc/en-us/articles/5306587861531)。

|  |
| --- |
| ****与国家专栏**** |
| ![当有国家/地区列时将 SMS 同意导入 Klaviyo 的示例 CSV 文件](https://klaviyo.zendesk.com/hc/article_attachments/28720893303195) |

|  |
| --- |
| ****带国家代码**** |
| ![当存在国家/地区代码时将 SMS 同意导入 Klaviyo 的示例 CSV 文件](https://klaviyo.zendesk.com/hc/article_attachments/28720848243995) |

![mceclip0.png](https://klaviyo.zendesk.com/hc/article_attachments/28720848247579)

## Klaviyo 如何处理符号和空格

Klaviyo 还可以处理某些拼写错误和常见符号。例如，如果电话号码包含符号、多余空格或字母，Klaviyo 会在将电话号码添加到配置文件时将其删除。以下内容将全部更正为 E.164 格式：+12345678900：

- +12/345(678)\*900
- +12()\*- 345678900
- abcde()\*()++12 345 678 900
- +1-2-3-4-5-6-7-8-9-0-0

## 其他资源

- 了解有关如何导入短信订阅者的更多信息：
  - [从 CSV 中过滤选择退出的短信联系人](https://help.klaviyo.com/hc/en-us/articles/5302764979611)
  - [上传短信联系人列表](https://help.klaviyo.com/hc/en-us/articles/360035428731)
- 了解如何[收集短信同意](https://help.klaviyo.com/hc/en-us/articles/360035056972)