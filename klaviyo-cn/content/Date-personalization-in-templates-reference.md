---
id: "115005257788"
title: "模板参考中的日期个性化"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005257788-Date-personalization-in-templates-reference"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:25Z"
language: "zh"
---
## 你将会学到

了解如何在 Klaviyo 模板中动态填充日期并设置日期格式。您可以将配置文件属性中的日期（例如生日）输入到任何消息中，或将事件元数据（例如下订单日期）输入到由该事件触发的流消息中。 ## 填充当前日、周、月或年

日期标签为您提供了一种将活动时间插入消息的快速方法。该日期以您帐户的时区为准。 - ****当前日期****：当前日期是{% current\_day %}。 **当前日期是 5。**
- ****当前星期几****：当前星期几是{% current\_weekday %}。 **本周的当前日期是星期五。**
- ****当前月份****：当前月份是{% current\_month\_name %}。 **当前月份是九月。**
- ****当前年份****：当前年份是{% current\_year %}。 **当前年份是 2021 年。**

目前，我们仅支持月份和星期几的英文名称。要将动态日期添加到消息中：

1. 从任何文本字段（例如电子邮件中的文本块、短信编辑器、推送消息编辑器），单击个性化图标。 ![](https://klaviyo.zendesk.com/hc/article_attachments/32002716115355)
2. 从****所有类型****菜单中，选择****日期****。 3. 选择日期标签（例如当前日期、当前年份等）。正在寻找日期配置文件属性，例如生日？从“****所有类型****”菜单中选择“****自定义****”，然后搜索或滚动以查找该属性。可以在任何基于事件的流中的消息的预览窗口中找到事件的日期属性。 ## 将动态日期填充为流电子邮件中的事件变量

假设您要通过客户下订单时触发的流程发送感谢电子邮件。您可能需要添加一句“感谢您在 \_\_\_\_\_ 上的订单”并指定下订单的日期。如果您查看 [Klaviyo 随事件一起接收的数据](https://help.klaviyo.com/hc/en-us/articles/115002779071-Personalize-Flow-Emails-with-Dynamic-Data)，例如 **下订单** 事件，您应该能够在那里找到代表订单日期的变量。查找名为“订单日期”或类似名称的属性，因为属性名称会根据您的数据源而有所不同。找到此变量后，您接下来可能会注意到此日期的格式不适合在模板中使用 - 它是 UTC 时间戳，在电子邮件中看起来不太好，例如：

![UTC 格式的时间戳](https://klaviyo.zendesk.com/hc/article_attachments/28713335047835)

如果您想以对客户更友好的格式填充此日期，则需要应用一些过滤器。 Klaviyo 支持 [Django 模板语言](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/) 使用的大多数过滤器。对于此用例，您将需要使用以下过滤器：

- ****格式\_日期\_字符串****
  该过滤器解析并转换从完整 UTC 时间戳切片的字符串到实际日期；这是必要的，以便您可以使用日期过滤器对其进行格式化。 - ****日期****在这里您可以选择日期格式； Django 有一个[图表](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#date) 概述了如何解决这个问题。要应用这些过滤器，请用竖线 (|) 分隔它们，并且中间不要有空格：

`{{ your_variable|format_date_string|date:'F d, o' }}`

上面的内容会变成这样：

`2016-02-11T16:46:08-05:00`

进入这个：

2016 年 2 月 11 日

以下是一些其他常见的日期和时间格式，以及用于显示它们的格式。 |  |  |
| --- | --- |
| 2016 年 2 月 26 日 | {{ your\_variable|format\_date\_string|date:'F d, o' }} |
| 2016 年 2 月 26 日 | {{ your\_variable|format\_date\_string|date:'d F o' }} |
| 2016 年 2 月 26 日 | {{ your\_variable|format\_date\_string|date:'m-d-Y' }} |
| 2016年2月26日 | {{ your\_variable|format\_date\_string|date:'d-m-Y' }} |
| 2/26/16（无前导 0）| {{ your\_variable|format\_date\_string|date:'n/j/y' }} |
| 26/2/16（无前导 0）| {{ your\_variable|format\_date\_string|date:'j/n/y' }} |
| 2 月 11 日 | {{ your\_variable|format\_date\_string|date:'M d' }} |
| 2 月 11 日 | {{ your\_variable|format\_date\_string|date:'d M' }} |
| 2016 年 2 月 26 日 4:46:08 | {{ your\_variable|format\_date\_string|date:'m-d-Y g:i:s' }} |
| 2016 年 2 月 26 日下午 4:46 | {{ your\_variable|format\_date\_string|date:'m-d-Y g:i a' }} |
| 2016 年 2 月 26 日下午 4:46 | {{ your\_variable|format\_date\_string|date:'m-d-Y g:i A' }} |

有关日期格式选项的完整列表，请参考 [Django 的日期格式文档](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#date)。 ## 使用“今天”变量

Today 变量允许您显示发送消息时的今天日期。要显示今天的日期，请使用以下代码：

`{% 今天 "%Y-%m-%d" 作为今天 %} {{ 今天 }}`

日期将以这种格式显示：2021-03-18

确保使用上面的整行代码。如果您包含一个标签而不包含另一个标签，则日期变量将不会呈现（即，如果没有前面的标签 {% Today ... %}，则不能单独使用 {{ Today }} 标签）。要应用不同的格式，请将上面部分中的过滤器应用到“{{ Today }}”变量。例如， `{% 今天 '%Y-%m-%d' 作为今天 %} {{ Today|format_date_string|date:'m/d/Y'
}}` 将使用 MM/DD/YYYY 格式进行渲染。 ## 计算未来日期

如果您想显示相对于消息发送日期的未来日期，请将 days\_later 过滤器应用于上面概述的 Today 变量，如下所示：

`{% 今天 "%Y-%m-%d" 作为今天 %} {{ Today|days_later:5 }}`

该变量将显示消息发送后 5 天的日期。因此，如果消息于 3 月 18 日发送，则显示的日期将为 2021-03-23。此过滤器可以与上面列出的格式过滤器结合使用，以使用不同的日期格式。以这段代码为例：

`{% 今天 '%Y-%m-%d' 作为今天 %} {{ 今天|days_later:5|format_date_string|date:'M
d' }}`

如果消息是在 3 月 18 日发送的，则会呈现为 3 月 23 日。## 其他资源

- [消息个性化参考](https://help.klaviyo.com/hc/en-us/articles/115005084927)
- [如何格式化 CSV 文件的日期](https://help.klaviyo.com/hc/en-us/articles/360039859932-How-to-Format-Dates-for-CSV-Files)
- [如何使用预览面板进行消息个性化](https://klaviyo.zendesk.com/hc/en-us/articles/27843522951707)