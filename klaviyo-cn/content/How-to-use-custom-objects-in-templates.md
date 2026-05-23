---
id: "35146367972763"
title: "如何在模板中使用自定义对象"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/35146367972763-How-to-use-custom-objects-in-templates"
section: "Use objects in Klaviyo"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:40Z"
language: "zh"
---
您必须有权访问[自定义对象](https://help.klaviyo.com/hc/en-us/articles/35105337172123)才能使用此功能。 ## 你将会学到

了解如何在模板中使用自定义对象，以便您可以在流和营销活动发送中使用对象数据。您必须先[创建一个对象](https://help.klaviyo.com/hc/en-us/articles/35105337172123)，然后才能在模板中使用自定义对象数据。 ## 通过个性化菜单访问对象数据

您可以使用自定义对象的属性或对象的记录计数在模板编辑器中个性化文本块。了解[如何使用Klaviyo的模板编辑器](https://help.klaviyo.com/hc/en-us/articles/4407911841435)。要开始将对象数据添加到模板中：

1. 添加新文本块或选择现有文本块。 2. 双击文本块，然后将光标置于要插入动态属性的位置。 3. 选择右上角的****个性化****按钮。 ![](https://klaviyo.zendesk.com/hc/article_attachments/35160309938075)

3. 在个性化模式中，从 **所有类型** 下拉列表中选择 **对象****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/35160309944475)

4. 在**对象**中，您将看到帐户中可用于将数据提取到模板中的所有对象。选择包含您要在模板中使用的数据的对象。 5. 选择要包含在模板中的特定对象属性或[对象过滤器](#h_01JPTH5R8840K0Q3XWH2CFYWRY)。您还可以在此处创建新的对象过滤器。 6. 设置默认文本和文本样式。要指定对象数据的大小写规则，您需要在个性化标签中手动设置规则。例如：

- ****{{ object.full\_name|标题|默认:'值' }}****
  约翰·多伊
- ****{{ object.full\_name|upper|default:'value' }}****
  约翰·多伊
- ****{{ object.full\_name|lower|default:'value' }}****
  约翰·多伊

了解有关[使用 Django 过滤器修改值]的更多信息。(https://developers.klaviyo.com/en/docs/glossary_of_variable_filters)

## 使用个性化标签访问对象数据

您可以在电子邮件（包括电子邮件的主题行）、短信/彩信、推送通知和客户中心中使用个性化标签来显示对象数据。了解[如何在 Klaviyo 中使用个性化标签](https://help.klaviyo.com/hc/en-us/articles/18986347580827)。 ### 对象个性化标签参考

您可以对对象使用以下个性化标签。 ****使用触发流程的对象****

{{ object }} 仅当对象触发流时才可用。 {{ object }} 模板标记仅在基于对象的日期触发流中可用。这类似于事件触发流的 {{ event }} 模板标记。这些示例使用以下内容：

- 名为 **Pet** 的对象，通过模板中的 **object** 标签引用。 - 名为 **Name** 的对象属性

|  |  |
| --- | --- |
| ****结构**** | ****示例**** |
| {{ object.object\_property }} | {{ 对象.名称 }} |
| {{ 对象 |查找：'object\_property' }} | {{ 对象 |查找：'名称' }} |

****通过ID获取对象****

这些示例使用以下内容：

- 名为 **Pet** 的对象
- 名为 **Name** 的对象属性
- 使用名为 **pet\_id** 的对象属性触发流的事件。此字段与 **Pet** 对象的对象 ID 相同。 |  |  |
| --- | --- |
| ****结构**** | ****示例**** |
| {% customobject event.object\_id  object\_type\_title="Title" as alias %} {{ alias.object\_property }} {% endcustomobject %} | {% customobject event.pet\_id  object\_type\_title="Pet" as pet %} {{ pet.Name }} {% endcustomobject %} |
| {% customobject event.object\_id  object\_type\_title="Title" as alias %} {{ 别名 |查找：'object\_property' }} {% endcustomobject %} | {% customobject event.pet\_id  object\_type\_title="Pet" as pet %} {{ pet |查找：'名称' }} {% endcustomobject %} |

****从对象过滤器返回单个对象****

这些示例使用以下内容：

- 一个名为 **oldest\_dog** 的附加对象过滤器
- 名为 **Name** 的对象属性

|  |  |
| --- | --- |
| ****结构**** | ****示例**** |
| {{ 对象\_filter.object\_filter\_name.object\_property}} | {{ object\_filter.oldest\_dog.Name }} |
| {{ 对象\_filter.object\_filter\_name |查找：'object\_property' }} | {{ object\_filter.oldest\_dog |查找：'名称' }} |

****从对象过滤器返回一个整数****

这些示例使用以下内容：

- 一个名为 **count\_of\_dogs** 的附加对象过滤器

|  |  |
| --- | --- |
| ****结构**** | ****示例**** |
| {{ 对象\_filter.object\_filter\_name }} | {{ object\_filter.count\_of\_dogs }} |

****检索对象记录****

要检索对象的最新对象记录，您需要循环遍历所有对象记录。此示例使用以下内容：

- 名为**宠物**的对象

|  |  |
| --- | --- |
| ****结构**** | ****示例**** |
| {% customobjects object\_type\_title="Title" as alias %} {% for object\_instance in alias %} {{ object\_instance.record }} {% endfor %} {% endcustomobjects %} | {% customobjects object\_type\_title="宠物资料" as pets %} {% for pets in pets %} {{ pet.name }} {% endfor %} {% endcustomobjects %} |

## 主题行中的对象数据

您可以使用任何自定义对象标签来个性化您的主题行：

- {% 对象\_filter %}
- {% 对象 %}
- {% 自定义对象 %}

例如，您可以在消息的主题行中使用 {% object %} 标记来直接显示客户宠物的名称。草稿视图：

![](https://klaviyo.zendesk.com/hc/article_attachments/37963491682331)

电子邮件预览：

![](https://klaviyo.zendesk.com/hc/article_attachments/37963491688475)

## 显示/隐藏逻辑中的对象数据

您还可以根据对象数据配置是否显示或隐藏模板中的块。基于对象数据动态显示或隐藏块使用与模板构建器相同的标签。您可以通过 ID、对象过滤器中的属性或对象过滤器中的聚合来引用对象。您必须先创建对象过滤器，然后才能在显示/隐藏逻辑中引用它们。例如，如果您有一个带有名为 **Breed** 属性的 **Pet** 对象，您可以选择使用 **object.Breed** 条件仅向拥有某种狗品种的宠物主人显示一个块。要设置显示/隐藏逻辑，请单击您要为其设置规则的块，然后在 **显示** 选项卡上选择****使用代码****。直接在代码编辑器中输入条件。如果它是基于对象数据的日期触发流的消息，则可以使用对象过滤器和对象模板标记。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37963491690267)

为了获得更大的灵活性（例如，使某些信息以 {% customobject %} 或 {% customobjects %} 返回的信息为条件），请考虑直接在文本块中使用带有 {% if … %} 逻辑的[高级条件逻辑](https://help.klaviyo.com/hc/en-us/articles/7655926841499)。 ## 对象过滤器

### 什么是对象过滤器？对象过滤器使您能够根据您设置的特定条件限制返回的对象记录，以便您可以显示特定类型的记录。 ### 创建一个新的对象过滤器

要开始创建对象过滤器：

1. 添加新文本块或编辑模板中现有文本块中的文本。 2. 选择****个性化****按钮。 ![](https://klaviyo.zendesk.com/hc/article_attachments/35160309938075)

3. 在个性化模型中，从 **所有类型** 下拉列表中选择 **对象****。 4. 选择包含您要设置过滤器的数据的对象。 5. 选择您想要设置过滤器的对象属性。 6. 选择****创建新过滤器****。在 **创建对象过滤器** 模式中，设置以下信息：

- ****姓名****
  为您的对象过滤器创建一个名称。 - ****过滤条件****
  定义对象必须满足才能包含在文本块中的规则。 - ****多条记录满足条件时的行为****
  定义多个记录满足条件的情况下的行为。 ![](https://klaviyo.zendesk.com/hc/article_attachments/35305347554715)

创建对象过滤器后，您可以在显示/隐藏逻辑和个性化标签中使用它，以根据您设置的条件显示特定对象记录。 ## 其他资源

[对象入门](https://help.klaviyo.com/hc/en-us/articles/35105337172123)

[消息个性化参考](https://help.klaviyo.com/hc/en-us/articles/4408802648731)

[如何使用预览面板进行消息个性化](https://help.klaviyo.com/hc/en-us/articles/27843522951707)