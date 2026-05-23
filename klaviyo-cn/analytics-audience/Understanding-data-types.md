---
id: "115005237648"
title: "了解数据类型"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005237648-Understanding-data-types"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T10:55:08Z"
language: "zh"
---
## 你将会学到

了解可用于在 Klaviyo 中存储数据的不同选项，以及如何使用每一种选项。 Klaviyo 允许您利用收集到的客户数据来支持数据驱动的营销选择，从而发展您的品牌。话虽这么说，了解提取到您帐户中的数据非常重要。 ## Klaviyo 中数据类型出现的位置

使用**有关某人的属性**创建分段或配置流过滤器时，您会注意到在为条件选择维度后会出现一个下拉菜单。该下拉菜单与您输入的值的数据类型相关。 ![分段中的数据类型下拉列表](https://klaviyo.zendesk.com/hc/article_attachments/34356876375579)

可以选择以下数据类型：

- 文字
- 数量
- 日期
- 布尔值
- 列表

## 文本

文本输入是任何有限的字符序列（即字母、符号和标点符号）。它始终用于表示纯文本，即使它包含数字或格式类似于日期。使用文本数据类型：

- 名字
- 与其他字符混合的数字（例如货币符号）
- 街道地址
- 对问题的简短或详细回答（例如购物偏好、最喜欢的颜色）

此外，当预期数据类型不清楚时，文本是默认数据类型。您可以将文本输入视为可能出现在段落中引号内的内容。无论引号中的内容如何，​​引号内的内容都作为有限的字符序列存在。下面是一个注册表单，其中收集了将被转换为文本属性的偏好信息。 ![收集多种类型数据的注册表单](https://klaviyo.zendesk.com/hc/article_attachments/28716053736091)

## 数量

数字是不带小数的数值。当您导入数值时，Klaviyo 会自动将该值识别为数字，而不是文本。输入的数字可以参考某人的年龄、收到的电子邮件数量或客户向您购买的次数。下面的部分通过与上个月点击或打开的电子邮件数量的交互来显示客户参与度。 ![段条件中使用的数字数据类型](https://klaviyo.zendesk.com/hc/article_attachments/34356876382107)

## 日期

日期用于任何日期时间值。与数字不同，Klaviyo 仅在以某种方式（即 YYYY-MM-DD HH:MM:SS）[格式化](https://developers.klaviyo.com/en/docs/acceptable_date_and_timestamp_formats_for_profile_and_event_properties) 时，才会自动将日期值识别为日期。日期可以参考某人的生日、他们第一次订阅您的时事通讯的日期或与合作伙伴的周年纪念日。以下是收集生日信息作为日期的注册表单。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38342176407835)

## 布尔值

布尔数据类型只能表示两个值：true 或 false。布尔数据的一个示例是当某人接受您的营销时存储的属性。以下是同意营销的客户资料示例。 ![属性的二进制数据类型](https://klaviyo.zendesk.com/hc/article_attachments/34356906949147)

接受的 **true** 值为：

`真`、`"1"`、`1`、`"真"`、`"t"`、`"是"`、`"y"`

接受的 **false** 值为：

`False`、`"0"`、`0`、`"false"`、`"f"`、`"no"`、`"n"`、`无`

所有字符串值（用引号引起来的值）都不区分大小写。如果您使用 CSV 将布尔值上传到 Klaviyo 或通过 API 发送[自定义对象](https://help.klaviyo.com/hc/en-us/articles/35105337172123)数据，请使用“True”和“False”。 ## 列表

列表是任何值数组；例如[“优惠1”，“优惠2”]。在 Klaviyo 中，当目标是收集单词或短语数组（其中数组中的每个项目都可以单独识别）时，就会使用列表。一种常见的用例是在单个属性下收集不同的标签，例如 **Shopify Tags** 属性。当 Klaviyo 将属性存储为列表时，您可以在分段或过滤器中使用该属性，然后包含任意数量的可用标签。您可以从作为列表一部分存储的任何值中进行选择。另一个常见的用例是，Klaviyo 通过集成捕获 **已下订单** 指标，并且我们随该下订单一起收到的数据包括 **Items** 属性。 此单个 **Items** 属性需要包含订单中购买的所有商品。 ![列出事件数据中使用的数据类型](https://klaviyo.zendesk.com/hc/article_attachments/34356876391835)

为了实现这一点，该属性始终被同步并作为数组（列表）存储在 Klaviyo 中。这允许我们存储 **Items** 属性，同时包含一系列值（即以单个订单购买的每个项目），其中数组中的每个值都可以单独标识。上传包含列表属性的 CSV 时，请在单元格中包含完整的列表格式。确保列中的每个条目都遵循列表格式，即使特定人员的列表仅包含一项。 ![准备上传列表数据的 CSV 文件](https://klaviyo.zendesk.com/hc/article_attachments/28716053749403)

## 字符串（列表上传期间）

将配置文件列表上传到 Klaviyo 时，可能会出现另一种数据类型；细绳。字符串与[文本数据类型相同。](#h_01ENR9PD67WK686H8Z5SHCVK59) 创建分段时，可以使用文本数据类型基于字符串数据进行分段。 ## 其他资源

- [分段入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005237908)
- [关于个人资料的信息部分](https://klaviyo.zendesk.com/hc/en-us/articles/115005247028)
- [如何使用链接收集有关收件人的信息](https://klaviyo.zendesk.com/hc/en-us/articles/115005255248)
- [如何在订单确认页面嵌入表格](https://klaviyo.zendesk.com/hc/en-us/articles/360031724251)