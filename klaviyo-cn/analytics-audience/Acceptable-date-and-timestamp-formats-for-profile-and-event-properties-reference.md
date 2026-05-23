---
id: "115005253428"
title: "配置文件和事件属性参考可接受的日期和时间戳格式"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005253428-Acceptable-date-and-timestamp-formats-for-profile-and-event-properties-reference"
section: "Profile management"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 在通过我们的 API 发送或以 CSV 上传形式发送的事件和个人资料数据中识别哪些日期和时间格式。请注意，这不适用于通过 Track API 发送的事件时间戳，该时间戳必须是 UNIX 时间（以秒为单位）。

## 可接受的日期和时间戳格式

请参阅下面的示例，了解有关在 CSV 文件中设置日期和时间戳格式的信息。请注意，您必须将日期格式设置为 YYYY-MM-DD 或 MM/DD/YYYY。如果没有与您的日期关联的时间，您可以使用 HH:MM:SS 值 00:00:00 将其设置为午夜。

如果您的时间戳中不包含秒数，则它们将默认为 0。例如，时间戳“2014-09-30 13:34”将作为“2014-09-30 13:34:00”提交给 Klaviyo

例如，日期 2014 年 9 月 30 日下午 1:34:08 应使用以下支持的格式之一进行格式化：

`2014-09-30 13:34:08`

`2014-09-30 13:34:08+00:00`

`2014 年 9 月 30 日 13:34:08`

`2014 年 9 月 30 日 13:34:08`

`2014 年 9 月 30 日 13:34`

`09/30/14 13:34`

`2014-09-30T13:34:08`

`2014-09-30 13:34:08.000001`

`2014-09-30T13:34:08.000001`

`2014-09-30 13:34:08.000001-04:00`

`1412098448` (Unix)

如果您在将电子表格中的日期转换为 CSV 文件之前需要重新格式化日期的帮助，请参阅我们的文章[格式化 CSV 文件的日期](https://klaviyo.zendesk.com/hc/en-us/articles/360039859932)。

以下示例展示了使用正确的日期/时间格式上传的 CSV 文件的外观。

![2018-06-13_21-47-57.gif](https://klaviyo.zendesk.com/hc/article_attachments/28722594609819)

请注意，当您导入带有时间戳的日期时，此字段会映射到日期数据类型。但是，当您导入不带时间戳的日期时，映射到日期数据类型时，默认时间午夜 UTC 将应用于该日期。这可能会导致[日期属性触发的流程](https://klaviyo.zendesk.com/hc/en-us/articles/360002732652)根据帐户的时区提前或推迟一天发送。因此，如果您只有日期（没有时间戳）要上传，则将其映射到文本数据类型。

有关将 CSV 文件上传到 Klaviyo 的更多信息，请参阅我们关于[如何将订阅者添加到现有列表](https://klaviyo.zendesk.com/hc/en-us/articles/115005251128) 的文章。

## 其他资源

- [CSV 文件参考格式日期](https://klaviyo.zendesk.com/hc/en-us/articles/360039859932)
- [Klaviyo 的默认列表和段参考](https://klaviyo.zendesk.com/hc/en-us/articles/360024538231)