---
id: "7655926841499"
title: "模板的条件逻辑参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/7655926841499-Conditional-logic-reference-for-templates"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:55:05Z"
language: "zh"
---
## 你将会学到

了解可用于仅向某些收件人动态显示块、部分或自定义编码内容的所有可用条件。要了解如何在模板中使用这些条件，请参阅我们的文章[如何根据动态变量显示或隐藏模板块](https://help.klaviyo.com/hc/en-us/articles/7655965301531)。了解如何使用条件逻辑：

- [可以使用条件的地方](#h_01G90PC1GF28BCKX1H83E6W1GJ)
- [成功秘诀](#h_01G90PEBD7E3H2Y9YSE41Q7FK9)
- [条件结构](#h_01G90PC71XXASDF3ERB4F39QDK)
- [构建复杂条件](#h_01G90PE5WWGQETTSC7K9GY2SKX)

## 可以在哪里使用条件

您可以在以下位置使用条件：

- ****电子邮件****
  - 创建显示/隐藏逻辑以动态[仅向某些人显示块或部分](https://help.klaviyo.com/hc/en-us/articles/7655965301531)。 - 如果您不想编写代码，请改用[显示/隐藏逻辑生成器](https://klaviyo.zendesk.com/hc/en-us/articles/7655965301531)。 - 编写 if/else 条件来[创建自定义 Django 语句](https://developers.klaviyo.com/en/docs/use_conditionals_in_messages)。 - ****客户中心****
  - 在内容块中编写 if/else 条件以[创建自定义 Django 语句](https://developers.klaviyo.com/en/docs/use_conditionals_in_messages)

## 成功秘诀

构建显示/隐藏条件时，请注意细节。显示/隐藏条件区分大小写，并且拼写必须与您的个人资料或事件数据完全匹配。另外，请务必考虑所有可能的观看者。例如，如果您仅向某个州的居民显示特定街区，请涵盖该州名称的所有可能拼写（例如，Massachusetts、massachusetts、mass、MA）。还要考虑可能根本没有设置该属性的配置文件。构建消息并应用条件后，使用各种配置文件进行[预览](https://help.klaviyo.com/hc/en-us/articles/115005081907-How-to-Preview-and-Send-Test-Emails-in-Klaviyo)，以确认消息在所有情况下都按预期显示。 ## 条件结构

条件应包含 1-3 个元素，具体取决于您的块目标和您正在使用的数据。该条件必须至少包含一个变量（例如，**person|lookup:'Favorite Color'**）。它还可能包括一个比较函数，例如=（等于）或>（大于）和一个值，该值指定要查找的属性值。此外，如果您希望该块仅针对不满足条件的配置文件显示，则某些条件以 **not** 开头。下图包含显示/隐藏条件可以遵循的可能结构的完整列表。 |  |  |  |
| --- | --- | --- |
| ****样品状况**** | ****显示块如果...**** | ****可接受的数据类型**** |
| person|lookup:'最喜欢的颜色' | `Favorite Color` 属性已设置（具有任何值）并且不是布尔值 **False** |任何 |
|不是人|查找：'最喜欢的颜色' | `Favorite Color` 属性未设置（配置文件中不存在，或者为空），或者是布尔值 **False** |任何 |
| person|lookup:'最喜欢的颜色' == '绿色' | `Favorite Color` 属性的值为 `green` |文本、数字 |
| person|lookup:'最喜欢的颜色' != '绿色' | `Favorite Color` 属性没有值 `green` |文本、数字 |
| person|lookup:'年龄' > 20 | `Age` 属性包含大于 20 的数字 |数量 |
|人|查找：'年龄' >= 20 | `Age` 属性包含大于或等于 20 | 的数字数量 |
| person|lookup:'年龄' < 20 | `Age` 属性包含小于 20 的数字 |数量 |
|人|查找：'年龄' <= 20 | `Age` 属性包含小于或等于 20 | 的数字数量 |
|人中的“绿色”|查找：“最喜欢的颜色”|属性“Favorite Colors”包含一个列表，“green”是列表项之一，或者属性“Favorite Colors”包含文本，并且“green”存在于文本中的任何位置 |列表、文本|
|人不是“绿色”|查找：“最喜欢的颜色”|属性“Favorite Colors”包含一个列表，并且“green”不是列表项之一，或者属性“Favorite Colors”包含文本，并且“green”不存在于文本中的任何位置 |列表、文本|

### 布尔值的条件

如果您引用存储为布尔值的数据，则需要在显示/隐藏条件定义中使用 1 和 0，而不是“true”和“false”。不要将 1 或 0 用引号引起来。使用下面的示例条件作为模板。 |  |  |
| --- | --- |
| ****样品状况**** | ****显示块如果...**** |
|人|查找：'VIP' == 1 | `VIP` 属性设置为布尔值 `true` |
|人|查找：'VIP' == 0 | `VIP` 属性设置为布尔值 `false` |

### 存储为文本的布尔值的条件

如果您的真/假数据存储为文本而不是布尔值，请使用上面文本属性的示例条件。如果您不确定，或者引用的属性同时包含布尔值和文本，则可以使用这些结构来涵盖所有场景。包括数据中存在的所有拼写和大小写。 |  |  |
| --- | --- |
| ****样品状况**** | ****显示块如果...**** |
| person|lookup:'VIP' == 1 或 person|lookup:'VIP' == 'true' 或 person|lookup:'VIP' == 'True' | `VIP` 属性设置为布尔值 `true` 或字符串 `true` 或 `True` |
| person|lookup:'VIP' == 0 或 person|lookup:'VIP' == 'false' 或 person|lookup:'VIP' == 'False' | `VIP` 属性设置为布尔值 `false` 或字符串 `false` 或 `False` |

## 构建复杂条件

如果您希望您的块向满足多个条件的人显示，或者如果您有复杂的用例，则可以对一个块使用多个显示/隐藏条件。为此，请使用 AND 或 OR 连接一系列条件。例如，如果您想向马萨诸塞州的任何人显示一个区块，但马萨诸塞州在某些个人资料上的拼写不同，您可以使用如下条件：

**person.location.region == '马萨诸塞' 或 person.location.region == '马萨诸塞' 或 person.location.region == 'mass' 或 person.location.region == 'MA'**

如果您只想向最喜欢的颜色是绿色并且也是 VIP 的人显示一个区块，您可以使用如下条件：

**person|lookup:'最喜欢的颜色' == '绿色' 和 person|lookup:'VIP'== 1**

### 条件语句和内联文本编辑器

当您将某些条件语句添加到文本块时，它们可能会从内联文本编辑器中消失。代码仍然存在；它只是被隐藏了。要查看和编辑条件语句，请打开文本块的 **源代码** 字段。以下标签仅在文本块的 **源代码** 字段中可见：

- {% 为 ... %}
- {% endfor %}
- {% 如果...%}
- {% elif ... %}
- {%其他%}
- {% endif %}
- {% 与 ... %}
- {% 结尾为 %}