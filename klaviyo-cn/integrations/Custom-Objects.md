---
id: "360004775072"
title: "自定义对象"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360004775072-Custom-Objects"
section: "Custom integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: "zh"
---
## 概述

自定义对象是可以接受任何架构并且可以包含对任何 Klaviyo 配置文件对象的外键引用的 Klaviyo 对象。虽然我们的其他记录类型（个人资料、事件、活动等）具有固定模式（例如，个人资料具有名字、姓氏、电子邮件、位置、接受营销等），并且虽然有些记录类型（如个人资料）可以接受自定义字段（最喜欢的颜色、宠物类型），但接受替代数据结构的灵活性有限。自定义对象是一种灵活的选择。 #### 警告

这是为有权访问开发人员或开发人员支持的客户保留的高级功能。要启用此功能，您必须[联系我们的客户成功团队](https://help.klaviyo.com/hc/en-us/requests/new)。 ## 什么是架构？模式是定义数据库表的结构。您可以将模式视为 Excel 电子表格中的列标题：它告诉您每个字段的名称以及它将保存的数据类型，例如日期、字符串（文本）、数字、布尔值（真/假）等。例如，以下是存储在 Klaviyo 中的标准配置文件。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28713335502747)

如果我们查看数据在 Klaviyo 中的存储方式，我们可以看到 JSON 格式的结构（或模式）。 ````
{
 “创建”：“2018-07-10 13:28:25”，
 “更新”：“2018-07-10 13:28:26”，
 “对象”：“人”，
 “id”：“Lwxf3r”，
 "$email": "klaviyogreen@gmail.com",
 "$first_name": "约翰",
 "$last_name": "史密斯",
}
````

## 自定义对象可以让您做什么？自定义对象允许您为新的数据库对象定义架构。该对象可以具有外键关系（即，它可以指向）Klaviyo 中任何其他现有的配置文件对象。当您的配置文件具有多个共享相同架构的相关记录时，这会很有帮助。例如，如果您的业务模型使用礼品卡，则单个客户可以拥有零张、一张或数百张与其个人资料关联的礼品卡。其他示例包括以下内容：

- 调查回复（客户多次填写同一份调查
- 出席活动
- 与您的客户对话
- 产品评论

## 如何在 Klaviyo 中使用自定义对象数据？自定义对象数据可用于在 Klaviyo 中构建分段并将数据传递到电子邮件中。 ### 使用自定义对象数据进行分段

分段目前仅适用于日期字段（日期之前/之后/日期/之间）和数字字段（大于、小于、等于、之间）。假设您创建了一个自定义对象来存储客户的礼品卡信息。使用自定义对象中的数据，您可以构建一个细分，其中包含一张或多张价值低于 50 美元或以上的礼品卡的所有配置文件。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28713329823003)

如果您要传递日期信息，则可以构建一个分段，其中包含 2018 年 3 月 1 日至 2018 年 3 月 31 日期间参加活动的所有个人资料。 ### 将自定义对象数据传递到电子邮件中

自定义对象中的任何字段都可以提取到电子邮件正文中。例如，您可以使用模板标记插入一个显示礼品卡代码、礼品卡当前价值和到期日期的变量。该标签可以循环遍历与配置文件相关的所有记录并显示所有记录的值。如果客户有八张不同的礼品卡，您可以在文本块中显示其所有代码，并在其旁边显示当前值。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28713329825947)

该标签可以对自定义对象记录中的数值数据进行求和或执行其他基本操作（最小值、最大值）。例如，您可以将所有八张礼品卡的价值相加，并将其显示在电子邮件的主题行中。有关更多信息，请参阅我们的[模板标签和变量语法](https://help.klaviyo.com/hc/en-us/articles/115005084927-Template-Tags-and-Variable-Syntax)指南。 ## 如何设置？联系我们的客户支持团队后，您的第一步是将现有数据源映射到架构框架以创建 Klaviyo 自定义对象。下面是来自 Klaviyo 内单个自定义对象的数据示例。 ````
“配置”：{
    “602”：{
        “所需字段”：[
            “custrecord_gc_shopify_gc_internal_id”，
            “custrecord_gc_remaining_balance”，
            “custrecord_gc_initial_balance”，
            “custrecord_gc_disabled”，
            “custrecord_gc_gift_card_type”，
            “custrecord_gc_sales_order”，
            “custrecord_gc_customer”，
            “custrecord_gc_retrieve_balance”，
            “custrecord_gc_gift_card_number”
        ],
        “所需字段映射”：{
            "custrecord_gc_gift_card_number": "代码",
            "custrecord_gc_gift_card_type": "类型",
            "custrecord_gc_remaining_balance": "值",
            "custrecord_gc_sales_order": "shopify_order_number"
        },
        "email_field": "custrecord_gc_customer",
        “emails_separate”：1，
        “要显示的字段”：[
            “custrecord_gc_sales_order”，
            “创建_外部”，
            “custrecord_gc_gift_card_type”，
            “custrecord_gc_initial_balance”，
            “custrecord_gc_remaining_balance”
        ],
        “索引”：[
            “custrecord_gc_gift_card_type”，
            [
                “klaviyo_customer_id”，
                “custrecord_gc_gift_card_number”，
                “custrecord_gc_remaining_balance”
            ]
        ],
        “映射”：“礼品卡”，
        “解析器”：{
            “custrecord_gc_sales_order”：[
                “销售订单#”，
                “之后”
            ]
        }
    }
}
````

我们可以使用此示例数据来分解 Klaviyo 的自定义对象模式框架。 ````
“配置”：{
    “602”：{
        “所需字段”：[]，
        “desired_fields_mapping”：{}，
        "email_field": "custrecord_gc_customer",
        “emails_separate”：1，
        “要显示的字段”：[]，
        “索引”：[
            “custrecord_gc_gift_card_type”，
            [
                “klaviyo_customer_id”，
                “custrecord_gc_gift_card_number”，
                “custrecord_gc_remaining_balance”
            ]
        ],
        “映射”：“礼品卡”，
        “解析器”：{
            “custrecord_gc_sales_order”：[
                “销售订单#”，
                “之后”
            ]
        }
    }
}
````

|  |  |
| --- | --- |
|关键|价值|
| ****602**** |来自数据源的对象 ID。您的数据源应该为每个对象有一些唯一的标识符。 |
| ****所需\_字段**** | Klaviyo 应从源对象中检索哪些字段？我们需要在 Klaviyo 中定义我们想要访问的每个字段。 |
| ****所需\_字段\_映射**** |您想要将哪些人类可读的标签应用于这些字段？源字段在源系统中将被命名为“custrecord\_gc\_remaining\_balance”，可以在字段映射中压缩为“value”（稍后在模板标记中使用）。 |
| ****电子邮件\_字段**** |使用电子邮件作为查找的配置文件对象的外键引用是什么字段？ （这将由工程师配置。）与****emails\_separate**** 结合使用。 |
| ****电子邮件\_separate**** |源系统中的该对象上是否存在电子邮件值？与****电子邮件\_字段****结合使用。 |
| ****要显示的字段**** |您希望在自定义对象的配置文件块中看到哪些字段？客户希望能够检查以确保细分中包含正确的配置文件，这使他们可以确定要显示哪些字段。某些字段包含您不希望显示的敏感数据，例如您客户的一张礼品卡上的剩余余额。 |
| ****索引\_on**** |我们应该使用哪些字段作为该数据的索引？我们将使用哪些字段来频繁查询和检索数据？在字段上建立索引可以更快地检索数据，因此如果您要使用字段进行分段或将数据提取到电子邮件中，则在其上添加索引会很有帮助。这也可以在初始集成后重新配置，因此如果您稍后需要添加其他索引字段，这不是问题。 |
| ****映射**** |与 ****desired\_fields\_mapping**** 类似，这让我们可以在 Klaviyo 中为该对象分配一个用户友好的名称，以便在分段界面和模板标签中使用。 |
| ****解析器**** |这使我们可以从指定字段中修剪字符，以便我们可以以不同的方式使用其中的数据。在此示例中，Shopify 销售订单号在数据源中存储为“销售订单 # 100000”。 这意味着我们无法将其与现有的 Shopify 销售订单编号字段交叉引用，该字段仅存储值 100000。因此，我们需要删除“销售订单编号”。 |

一旦您定义了架构以匹配 Klaviyo 的自定义对象框架，您将与 Klaviyo 工程师合作实现一种将数据发送到 Klaviyo 的方法。 #### 注意

我们目前没有面向公众的自定义对象 API。要将自定义对象数据发送到 Klaviyo，您需要联系我们并与我们的工程团队合作。