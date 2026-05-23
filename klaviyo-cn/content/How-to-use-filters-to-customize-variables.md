---
id: "360058907911"
title: "如何使用过滤器自定义变量"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360058907911-How-to-use-filters-to-customize-variables"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:53Z"
language: "zh"
---
## 你将会学到

了解过滤器的工作原理以及如何使用它们来自定义变量。过滤器允许您自定义消息中变量的格式和内容（即个性化标签）。有关可在模板编辑器中使用的过滤器列表，请参考 Klaviyo 的[变量过滤器术语表](https://help.klaviyo.com/hc/en-us/articles/360058466052)。

## 开始之前

在开始之前，请熟悉[Klaviyo 中的个性化工作原理](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)。为了使用过滤器，您需要能够识别正确的基本变量并将它们添加到您的模板中。

## 过滤器的工作原理

过滤器应用于个性化标签以调整显示的输出。一些可能的用例是：

- 对一段文本应用一致的大写（例如，您可以使用 **upper** 过滤器来获取任何变量并将其全部大写）。
- 使用**乘法**过滤器显示应用促销后商品的价格。
- 使用 **floatformat** 过滤器设置要显示的数字变量的小数位数。

有关支持的过滤器列表，请参考我们的[变量过滤器词汇表](https://help.klaviyo.com/hc/en-us/articles/360058466052)。

## 对变量应用过滤器

要将过滤器应用于变量：

1. 识别您的个性化标签（例如“{{ item.price }}”）。
2. 在变量名称后添加管道符号 (|)。
3. 添加过滤器名称，例如**floatformat**，以指定要显示的小数位数。
4. 如果过滤器接受任何参数（即附加参数或输入），请添加一个冒号，后跟参数。

不要添加任何额外的空格。以下是应用了过滤器的变量的示例：

`{{ item.price|floatformat:2 }}`

在此示例中，“item.price”是变量名称，“floatformat”是过滤器，“2”是过滤器所需的参数。

如果参数是一段文本，则需要用直单引号括起来（即 '，而不是 '）。如果参数是数字，则不需要引号。请参考 Klaviyo 的[变量过滤器词汇表](https://help.klaviyo.com/hc/en-us/articles/360058466052) 作为示例。

## 使用过滤器的技巧

如果您要复制过滤器并将其粘贴到模板中，请确保粘贴为纯文本，以避免与过滤器本身一起粘贴格式。使用粘贴作为纯文本键盘快捷键（Ctrl+Shift+V 或 Cmd+Shift+V）。

确保变量中引用的数据适合所使用的过滤器非常重要。某些过滤器只能应用于文本[数据类型](https://help.klaviyo.com/hc/en-us/articles/115005237648)，而其他过滤器仅适用于列表或数字。如果过滤器未按预期工作，请检查您正在使用的事件或配置文件数据，以确保其类型正确。

## 应用多个过滤器

如果需要，您可以将多个过滤器应用于单个变量。为此，请使用管道符号 ( | ) 连接每个过滤器，并考虑过滤器通常会按顺序应用（从第一个到最后一个）。以下是应用多个过滤器的变量的一些示例：

`{{名字|标题|默认:'那里'}}`

第一个过滤器将标题大小写应用于收件人的名字，第二个过滤器提供在未提供名字时使用的默认单词。

`{{ item.price|multiply:.8|floatformat:2 }}`

第一个过滤器将基本商品价格乘以 0.8（以显示应用了 20% 优惠券的价格），第二个过滤器指定应显示两位小数。

## 其他资源

- [变量过滤器术语表](https://help.klaviyo.com/hc/en-us/articles/360058466052)
- [模板参考中的日期变量](https://help.klaviyo.com/hc/en-us/articles/115005257788-How-to-Format-Date-Variables-in-Templates)
- [消息个性化参考](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)