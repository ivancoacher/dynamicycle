---
id: "360004785571"
title: "目录查找标签参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360004785571-Catalog-lookup-tag-reference"
section: "Getting started with products"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: "zh"
---
## 你将会学到

了解如何使用目录标签，它允许您在电子邮件、短信和推送消息中引用目录中的特定产品信息。当您想要创建自定义产品推荐或交叉引用产品信息时，这非常有用。例如，如果您使用自己的推荐引擎，则可以将自己的产品推荐作为事件或个人资料数据传递给 Klaviyo，然后在模板中使用该数据。请注意，本指南是为精通技术的营销人员或有权联系开发人员的客户而设计的。 ## {%目录%}标签

`{% Catalog %}` 标签使用以下语法：

````
{% 目录 itemID unpublished="取消" %}
... {% endcatalog %}
````

将 **itemID** 替换为您引用的产品的产品 ID。这是从您自己的产品目录同步的产品 ID。请注意，此查找专门针对产品 ID，而不是 SKU。添加**unpublished="cancel"** 将确保您在引用的项目未发布时不会发送消息。该参数是可选的。 - 如果您的消息中引用的任何项目在查找时未在您的目录中发布，则整个消息将被跳过。 - 对于给定的流消息，您可以导航到****分析 > 收件人活动 > 其他**** 并查看标记为 **已跳过：目录项不可用** 的列表。此列表包括由于消息中的某个商品缺货或不可用而被跳过的所有配置文件。使用此功能时，在开始和结束目录标签之间，您可以引用与 Klaviyo 产品目录中 **itemID** 关联的商品的特定数据。以下数据可在“{% Catalog %}”块内部引用。 | ****模板标签**** | ****姓名**** | ****描述**** |
| --- | --- | --- |
| `{{ Catalog_item.description }}` |描述 |项目的描述。 |
| `{{ Catalog_item.url }}` |网址 |用于访问商店中商品的 URL。 |
| `{{ Catalog_item.title }}` |标题 |项目的标题。 |
| `{%currency_formatcatalog_item.metadata|查找："价格"%}`|价格|商品的价格。此标签使用正确的货币前缀来格式化商品价格。 |
| `{{ Catalog_item.currency_symbol }}` |货币符号|用于表示货币单位的图形符号 |
| `{{ Catalog_item.currency_code }}` |货币代码 |用于表示货币的字母代码 |
| `{{ Catalog_item.featured_image.full.src }}` |完整图像 |商品完整图片的 URL。在图像块或 <img> 标签内使用它。 |
| `{{ Catalog_item.featured_image.thumbnail.src }}` |缩略图|商品完整图片的 URL。在自定义 HTML 中的 <img> 标记中使用它，或将其用作由开始和结束 {% Catalog %} 标记包围的动态图像占位符 URL |
| `{{ Catalog_item.id }}` |身份证 |商品的产品 ID。 |
| `{{ Catalog_id }}` |目录 ID |目录的 ID，以便您可以指定从哪个目录中提取（如果有多个目录）。 |

可能还有其他可用的数据字段被视为元数据。要引用这些附加项目属性之一，您可以使用变量语法：{{ Catalog\_item.metadata.color }}。在这种情况下，变量将提取与存储在项目元数据中的项目关联的“颜色”值。要访问存储在商品上的所有可用详细信息（包括所有元数据）的预览，请将以下代码段添加到测试模板中的文本块，并使用目录中当前产品之一的产品 ID 更新 **itemID**。 ````
{% 目录项 ID %}
{{ 目录项 }}
{% 最终目录 %}
````

然后，预览消息。此预览提供了可用于您的产品的所有数据的原始版本。 ## 按目录 ID 过滤

如果您有多个目录，您可以使用“{{catalog id}}”标签指定要从中提取的目录。例如，您可能有通过 Klaviyo 集成（例如 Shopify）同步的目录、通过 API 同步的目录或自定义目录源。标签详细信息可能会因您的集成而异。在以下示例中，多个目录同步到同一个 Klaviyo 帐户，我们希望从 API 目录中包含的特定产品中提取产品描述。首先，找到目录 ID：

1. 在 Klaviyo 中，导航至****内容 > 产品****。 2. 从 **所有目录** 下拉列表中选择要使用的目录。 ![截图 2025-05-13 12.08.19PM.png](https://klaviyo.zendesk.com/hc/article_attachments/36947752771483)
3. 从 URL 复制目录 ID。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36947760688539)

然后，找到项目 ID：

1. 选择目录后，从目录中选择您要使用的产品。 2. 在产品详细信息页面上，您将看到商品 ID。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36947760692891)

对于上面的示例，代码如下所示：

````
{％目录“SAMPLE-DATA-ITEM-15”集成=“api”catalog_id=“1060935”％} {{catalog_item.description}}{％endcatalog％}
````

## 按区域设置过滤

可以按区域设置搜索区域设置感知目录，例如 Klaviyo 中的 Shopify 目录。区域设置语言和区域可以使用 ISO 3166 和 639 标准通过两个字母的国家和语言代码来引用。如果找不到本地化产品，将使用默认产品信息。 ````
{％目录“SAMPLE-DATA-ITEM-15”集成=“api”catalog_id=“1060935”语言='fr'区域='CA'%} {{catalog_item.description}}{%endcatalog%}
````

## 查找随事件传递的项目 ID

将目录查找与事件结合使用主要用于以下场景：

- 如果您使用的是自定义集成，其中产品推荐与要在消息中显示的事件一起传递。例如，浏览放弃消息，其中根据查看的项目生成独特的推荐。您可以根据查看的项目生成并填充一组推荐项目，而不是填充客户在消息中查看的单个项目。一组产品 ID 需要与事件一起发送到 Klaviyo。 - 如果您使用自定义集成，并且您不希望发送需要在消息中包含的所有产品详细信息。例如，对于废弃的购物车消息，仅发送所有废弃商品的产品 ID，Klaviyo 可以查找每一项以提取所有相关详细信息。不需要每个事件都包含产品名称、价格、图像等，因为所有这些都可以通过仅将产品 ID 传递给 Klaviyo，然后在 Klaviyo 产品目录中查找信息来填充。当对事件使用“{% Catalog %}”标签时，查找基于目录项的项 ID（这将是产品 ID 或 SKU，具体取决于集成）。对于传递的标识值是项目 ID 的事件，查找标签将如下所示：

````
{% 目录事件.ItemID %}
……
{% 最终目录 %}
````

在此“{% Catalog %}”块中，为您想要填充的每个项目（即标题、图像等）的数据添加模板变量

例如，使用下面的示例目录项数据，我们可以构建一个引用关键产品信息的“{%目录%}”块：

****目录项数据：****

````
{
  "description": "所有 Klaviyos 的标配。这款 T 恤正面有 Klaviyo 标志，背面有标记图。",
  “url”：“https://klaviyogear.myshopify.com/collections/klaviyo-classics/products/short-sleeve-t-shirt-1”，
  "title": "经典 Klaviyo T 恤",
  “特色图像”：{
    “满”：{
      “src”：“https://www.klaviyo.com/media/images/examples/products/klaviyo-tshirt-full.png”
    },
    “缩略图”：{
      “src”：“https://www.klaviyo.com/media/images/examples/products/klaviyo-tshirt-thumbnail.png”
    }
  },
  “id”：“KLAVIYO-T恤”，
  “元数据”：{
    “颜色”：“灰色”，
    “设计”：“标准”
  }
}
````

****模板块语法：****

以下“{% Catalog %}”块的语法将从目录中提取事件中每个项目的项目图像、项目标题和项目描述：

````
{% for item in event.Items %}
	{% 目录项.SKU %}
 		<img src="{{ Catalog_item.featured_image.full.src }}"/>
 		{{catalog_item.title}}
 		{{catalog_item.description}}
 	{% 最终目录 %}
{% 结束 %}
````

如果查找无法找到它要查找的项目，则消息将被跳过并且不会发送。 ## 查找项目 ID 作为自定义属性

如果您使用自己的推荐引擎，则可以将推荐的项目 ID 作为 [自定义配置文件属性](https://klaviyo.zendesk.com/hc/en-us/articles/115000250912) 传递到 Klaviyo 中的配置文件。使用“{% Catalog %}”标签，您可以在向该客户发送消息时引用任何这些产品的信息。如果查找无法找到它要查找的项目，则消息将被跳过并且不会发送。 ### 存储在单个属性中的多个项目 ID 的语法

````
{% for item in person|lookup:'推荐产品' %}{% 目录项 %}

<img src="{{catalog_item.featured_image.thumbnail.src }}" style="display: inline-block; border: none" width="150px" />

<p>{{ Catalog_item.title }} {% endcatalog %}</p>

{% 结束 %}
````

### 配置文件属性中单个项目 ID 的语法

````
{% 目录人|查找："推荐产品" %}

<img style="显示：内联块；边框：无；" src =“{{catalog_item.featured_image.thumbnail.src}}”宽度=“150px”/>

  <p>{{ Catalog_item.title }} {% endcatalog %}</p>
````

## 关于 has\_category 标签

使用 **has\_category** 标签来确定目录中的项目是否属于特定类别。它必须在特定项目的目录查找标签中使用。使用下面的示例代码来使用此标签，将 **itemID** 替换为目录中的产品 ID，并将 **category\_name** 替换为全部或部分类别名称。 ````
{% 目录项 ID %}
{{catalog_item.title}}
{% has_category Catalog_item "category_name" as in_category %}
{% if in_category %}
我正在出售！ {%其他%}
{% 结束 %}
{% 最终目录 %}
````

此示例显示产品标题，然后检查该产品是否属于类别 **category\_name**。如果评估结果为 **true**，则会显示消息“我正在促销！”将出现在产品标题后面。 **has\_category** 标签搜索与您设置的类别名称的完全匹配和部分匹配。例如，如果您使用“sale”作为类别名称，并且产品具有标签“on-sale”，则该产品的 **has\_category** 标签将评估为 **true**。 ## 其他资源

- [如何使用产品源和推荐](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787)
- [电子邮件模板编辑器概述](https://klaviyo.zendesk.com/hc/en-us/articles/115005082447)