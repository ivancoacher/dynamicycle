---
id: "115005080907"
title: "如何使用Shopify标签过滤客户"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005080907-How-to-use-Shopify-tags-to-filter-customers"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:38Z"
language: "zh"
---
## 你将会学到

了解如何使用 Shopify 标签在 Klaviyo 中筛选客户。 ## 开始之前

如果您还没有阅读我们关于[Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) 的文章，了解有关集成的分步说明，然后再继续阅读本文。 ## 关于 Klaviyo 中的 Shopify 标签

Klaviyo 的 Shopify 集成创建了一个“Shopify Tags”属性，该属性作为列表数据类型存储在 Klaviyo 客户资料中。这是因为，当使用这些标签时，通常有多个标签应用于同一客户。列表和字符串之间的区别在于，字符串数据类型用于收集单个单词或单个短语，而列表数据类型用于收集单词或短语的数组，其中数组中的每个项目都可以单独标识。在分段或过滤器中使用 Shopify 标签属性时，您可以使用多个条件包含任意数量的可用标签。 ## 细分与单个 Shopify 标签关联的人员

要创建与单个 Shopify 标签关联的客户细分：

1. 在 Klaviyo 中，单击****受众****下拉列表并选择****列表和细分****
2. 单击****创建列表/细分****并选择****细分****
3. 为您的细分命名
4. 在定义下，选择****有关某人的属性 > Shopify 标签****。 5. ****Type**** 字段将自动设置为 **List**。 6. 在“包含”后面的框中输入您要使用的标签的名称
7. 单击****创建分段****

![Klaviyo 细分生成器显示由 Shopify 标签定义的细分包含时事通讯](https://klaviyo.zendesk.com/hc/article_attachments/28713327903771)

## 细分与多个 Shopify 标签关联的人员

要创建与多个 Shopify 标签关联的客户细分：

1. 在 Klaviyo 中，单击****受众****下拉列表并选择****列表和细分****
2. 单击****创建列表/细分****，然后选择****细分****
3. 为您的细分命名
4. 在定义下，选择****有关某人的属性 > Shopify 标签****
5. 然后，类型字段将自动设置为 **列表**。 6. 在“包含”后面的框中输入您要使用的第一个标签的名称
7. 单击****和****
8. 为您想要使用的每个标签添加另一个条件，就像您对第一个标签所做的那样
9. 单击“创建段”。 ![Klaviyo 细分生成器显示 Shopify 标签定义的细分包含 tag1，Shopify 标签包含 tag2](https://klaviyo.zendesk.com/hc/article_attachments/28713327901595)

## 在没有任何 Shopify 标签的情况下对人员进行细分

您可能想要创建一个不与任何 Shopify 标签关联的人员细分。要创建此段：

1. 在 Klaviyo 中，单击****受众****下拉列表并选择****列表和细分****
2. 单击****创建列表/细分****并选择****细分****
3. 为您的细分命名
4. 在定义下，选择****有关某人的属性 > Shopify 标签****
5. 将类型更新为**列表**
6. 选择选项**为空**
7. 单击****创建分段****

![](https://klaviyo.zendesk.com/hc/article_attachments/28713333528347)

## 对没有特定 Shopify 标签的人员进行细分

您可能想要创建一群不与特定 Shopify 标签关联的人员。要创建此段：

1. 在 Klaviyo 中，单击****受众****下拉列表并选择****列表和细分****
2. 单击****创建列表/细分****并选择****细分****
3. 为您的细分命名
4. 在定义下，选择****有关某人的属性 > Shopify 标签****
5. 将类型更新为**列表**
6. 选择****不包含****，然后选择要排除的标签
7. 单击****创建分段****

****！[](https://klaviyo.zendesk.com/hc/article_attachments/28713327919259)****

## 在个人资料过滤器中使用 Shopify 标签

您还可以在个人资料过滤器中使用 Shopify 标签，就像构建细分时所做的那样。 1. 编辑配置文件过滤器时，选择 ****Properties about**** ****someone > Shopify Tags > contains****
2. 选择您想要用作过滤器的标签
3. 确保类型设置为 **列表**

![Klaviyo 流构建器触发器设置显示配置文件过滤器 Shopify 标签包含新闻通讯](https://klaviyo.zendesk.com/hc/article_attachments/28713327909019)

## 其他资源

- [了解属性](https://help.klaviyo.com/hc/en-us/articles/115005074627-Add-Custom-Properties-to-a-Contact-Profile#how-to-use-custom-properties)
- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-Started-with-Flows)