---
id: "25825620314651"
title: "如何在动态表块中跳过行"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/25825620314651-How-to-skip-lines-in-a-dynamic-table-block"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:36Z"
language: "zh"
---
## 你将会学到

了解如何跳过动态表块中的行（例如项目）。最常见的用例是从废弃的购物车电子邮件中隐藏不相关的项目，例如运输保险或免费礼品。但是，您可以对使用动态表块的任何电子邮件执行以下步骤。此过程涉及直接编辑电子邮件的代码。仅建议精通技术的营销人员或能够接触开发人员的人员使用此方法。我们的支持团队无法帮助您编写超出本文档涵盖的一般指导的自定义代码。为了维护数据的安全，Klaviyo 的支持团队无法打开 HTML 文件。 ## 开始之前

本文介绍如何隐藏现有动态表块中的项目。如果您尚未创建有效的动态表块（例如，废弃购物车中的产品或订单确认电子邮件），请了解如何[从头开始创建一个](https://klaviyo.zendesk.com/hc/en-us/articles/4408802597659) 或从我们的[流程中的消息开始]库](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)。 ## 写下你的 **if** 语句

在对模板进行更改之前，请使用文本或代码编辑器创建 2 个代码片段（您可以在以后复制并粘贴代码片段）。每个代码片段将由 3 部分组成：

1. [开始 **if** 标记](#h_01HY3CPMXG09XHJQTMZP0VJV82)，`{% if … %}`，指示哪些项目应出现在表格块中。 2. [内容](#h_01HY3CPMXGEPNZ4B9JC9SS91F2)，例如有关产品的图像标签或文字。 3. [结束标记](#h_01HY3CPMXGHQ358JG8EH463SGG), `{% endif %}`。 ### 创建开始 **if** 标签

以下是打开 **if** 标签的一些示例：

|  |  |
| --- | --- |
| ****标签**** | ****含义**** |
| {% if item.price != 0 %} |如果商品价格 (**item.price**) 不是 0。 |
| {% if item.product.name != "航线运输保险" %} |如果商品名称 (**item.product.name**) 不是“路线运输保险”。 |
| {% if item.product.title % 中不是“T 恤”} |如果商品的标题 (**item.product.title**) 不包含“T 恤”。 |
| {% if item.title %} |如果项目的标题 (**item.title**) 已设置（即具有任何值）。 |

这些标签区分大小写，并且必须与您的数据完全匹配。例如，如果商品价格的变量不是 **item.price**（例如 **item.Price** 或 **item.details.line\_price**），请更新代码以匹配您的数据源。 ### 创建 if 语句的内容

对于内容，请按照以下步骤使用动态表块中的现有内容。在代码或文本编辑器中编写此代码片段；您将在下一部分中将其添加到模板中。 1. 在表格块图像的**单元格内容**下，单击****替换****以查看图像占位符。 ![替换单元格内容按钮.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717391398811)
2. 从**动态变量或动态 URL** 字段复制整个代码。请注意，这可能是一个简单的动态变量，也可能是一个较长的代码片段；复制全部内容，无论长度如何。 ![废弃购物车产品图片变量.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717418658971)
3. 将此代码片段中的占位符替换为您从 **动态变量或动态 URL** 字段复制的代码。 ````
   <img src="PLACEHOLDER" style="宽度：200px；高度：自动；"宽度=“200”>
   ````

如果您现有的表块有一个简单的图像动态变量，则生成的内容将如下所示：

````
<img src="{{item.product.variant.images.0.src}}" style="width: 200px; height: auto;"宽度=“200”>
````

如果您现有的表块包含较长的代码片段，则生成的内容可能如下所示：

````
<img src="{% if item.product.variant.images.0.src %}{{item.product.variant.images.0.src}}{%else%}{{item.product.images.0.src|missing_product_image}}{%endif%}" style="宽度：200px；高度：自动；"宽度=“200”>
````

### 添加结束标签

然后，将所有内容放在一起：开始 if 语句，然后是内容，最后是结束“{% endif %}”标记。 ### 重复文本内容

然后，使用表格块右侧的内容（例如文本内容）重复此过程。单击 ****</>**** 打开代码编辑器并复制所有 HTML 内容，然后将此内容包装在与图像内容相同的 if 语句（步骤 1 和 3）中。 这是所有内容组合在一起的样子：

|  |  |
| --- | --- |
| ****代码片段 1（产品图片）**** | ****代码片段 2（产品详细信息）**** |
| ``` {% if item.product.name != "路线运输保险" %} <img src="{% if item.product.variant.images.0.src %} {{item.product.variant.images.0.src}}{%else%} {{item.product.images.0.src|missing_product_image}} {%endif%}"style="width: 200px; height:汽车；”宽度=“200”> {% endif %} ``` | ``` {% if item.product.name != "路线运输保险" %} <h3><a href="{{organization.url }}products/{{ item.product.url }}"> {{ item.product.name }} </a></h3> <p> 数量：{{ item.quantity|floatformat:0 }} — 总计：{%currency_format item.line_price|floatformat:2 %} </p> {% endif %} ``` |

以下是这些代码片段的细分：

|  |  |
| --- | --- |
| ****代码片段 1（产品图片）**** | ****代码片段 2（产品详细信息）**** |
| ``` {% if CRITERIA %} 图像占位符内容 {% endif %} ``` | ``` {% if CRITERIA %} 产品描述 {% endif %} ``` |

使用这些代码片段时，请确保使用直引号 (") 而不是弯引号 (“)，以确保代码正确呈现。编写完两个代码片段后，请在模板编辑器中继续执行以下步骤。 ## 跳过动态表块中的行

在编辑动态表块之前，请考虑将原始块保存为通用内容，以便您需要在将来的消息中引用它。然后取消链接块并单独编辑它，这样您的编辑就不会保存到通用内容块中。 1. 如果您的电子邮件是流程的一部分，请将其设置为 **草稿** 或 **手动**，以便在您编辑流程消息时不会发送消息。 2. 确保新表格块两列的 **单元格内容** 均设置为 **文本**。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717418651163)
3. 单击****</>**** 打开表格块左侧的 HTML 编辑器。 4. 复制您在上一节中创建的产品图像代码片段并将其粘贴到 HTML 字段中。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28717418647579)
5. 单击左上角的****完成****。 6. 导航到表块右侧的编辑器。 7. 单击****</>**** 打开表格块右侧的 HTML 编辑器。 8. 复制您在上一节中创建的产品详细信息代码段并将其粘贴到 HTML 字段中，替换所有先前的内容。 9. 单击****完成****。 10. 预览电子邮件以确保其按预期显示：跳过的项目不应出现，但所有其他项目将正常显示。确保预览包含您要隐藏的项目的事件，以便确保它被隐藏。 ### 条件语句和内联文本编辑器

当您将某些条件语句添加到文本块时，它们可能会从内联文本编辑器中消失。代码仍然存在；它只是被隐藏了。要查看和编辑条件语句，请打开文本块的**源代码**字段。以下标签仅在文本块的**源代码** 字段中可见：

- {% 为 ... %}
- {% endfor %}
- {% 如果...%}
- {% elif ... %}
- {%其他%}
- {% endif %}
- {% 与 ... %}
- {% 结尾为 %}

## 故障排除

****预览中没有出现任何项目****

1. 确保您正在预览的事件与您使用的数据源相匹配（例如，针对废弃购物车消息的 **开始结帐**）。 2. 确认**重复**和**行别名**与原始块中的**行集合**和**行别名**完全匹配。 ****应该跳过的项目仍然出现****

检查 if 语句的拼写和大小写。如果该产品仍然出现，则意味着它符合您的 if 语句中的条件，因此您的 if 语句配置不正确。详细了解[模板中的条件逻辑](https://help.klaviyo.com/hc/en-us/articles/7655926841499)。 ## 结果

执行这些步骤后，任何不符合 if 语句中条件的商品都不会出现在废弃购物车或订单确认电子邮件等消息中。 ## 其他资源

- [消息个性化参考](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)
- [如何导入自定义 HTML 模板](https://klaviyo.zendesk.com/hc/en-us/articles/115005254068)