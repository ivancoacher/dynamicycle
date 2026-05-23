---
id: "35146339009691"
title: "如何在段中使用自定义对象"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/35146339009691-How-to-use-custom-objects-in-segments"
section: "Use objects in Klaviyo"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:41Z"
language: "zh"
---
您必须有权访问[自定义对象](https://help.klaviyo.com/hc/en-us/articles/35105337172123)才能使用此功能。

## 你将会学到

了解如何在细分中使用自定义对象，以便您可以根据对象数据创建客户组。

请注意，您必须先[创建一个对象](https://help.klaviyo.com/hc/en-us/articles/35105337172123)，然后才能在分段中使用自定义对象数据。

## 使用对象数据构建段

就像配置文件属性一样，您可以使用对象数据通过细分的客户组来个性化您的营销。

了解[如何在 Klaviyo 中使用分段](https://help.klaviyo.com/hc/en-us/articles/115005237908)。

要访问段构建器中的对象数据：

1. 导航至****列表和分段**** > ****创建分段****。
2. 在 **选择条件** 下拉列表中选择****有关某人的属性****。
3. 从 **对象** 组中选择要在分段条件中使用的对象。此处列出了所有可用的对象。
4. 在**人员**字段中设置对象记录计数。
5. 在 **Where** 行中选择要过滤的对象属性。
6. 设置运算符（即**等于**、**不等于**、**至少**等）。
7. 在**维度值字段**中设置特定的对象属性值。

您必须准确输入对象属性值才能在 **维度值** 下拉列表中查看结果。

![](https://klaviyo.zendesk.com/hc/article_attachments/35158640997147)

### 过滤对象条件

您可以过滤对象条件，仅允许具有满足您要求的记录的简档进入分段。分段构建器中的对象条件可以通过以下方式过滤：

1. 配置文件拥有的对象记录数。
2. 每个对象记录的特定对象属性值。

您最多可以对一个对象条件应用 5 个过滤器。

****对象记录数****

对象记录计数（即分段构建器中的 **人员** 字段）允许您定义配置文件必须具有多少个合格对象记录才能进入分段。例如，对于像 **Pets** 对象这样的东西，您可以识别拥有多个宠物的宠物主人，每个宠物都有自己的对象记录。

可用的记录计数过滤器有：

- ****Has at least one****Profile has at least one object record.
- ****没有任何**** 配置文件没有任何对象记录。
- ****Has****Profile 有一个对象记录集。
- ****没有****配置文件没有对象记录集。
- ****至少有**** 配置文件至少有 X 条对象记录。
- ****Has more than****Profile has more than X object records.
- ****少于**** 配置文件的对象记录少于 X 个。
- ****最多有**** 配置文件不超过 X 个对象记录。

## 使用对象数据的示例段

These object properties are just examples, and the filters available to you are based on the object data sent to Klaviyo.

### **宠物**对象

Say you have a **Pet** object that contains data about customers’ pets.您可能想要创建如下分段：

- 拥有至少 3 只猫的个人资料，可针对垃圾和食品等散装产品的优惠券进行定位。
- Profiles with dogs under the age of 1, to target with marketing specific for pet owners with puppies.
- Profiles with dogs of a specific breed, for targeted marketing campaigns featuring dogs similar to their own.

### **约会**对象

假设您有一个 **Appointment** 对象，其中包含有关客户约会的数据。您可能想要创建如下分段：

- Profiles that have an upcoming appointment, to send them reminders.
- Profiles that all have appointments with the same person, to send them updates when their availability unexpectedly changed.
- Profiles that had a good experience during their appointment, to target with review requests.

## 其他资源

[自定义对象入门](https://help.klaviyo.com/hc/en-us/articles/35105337172123)

[Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)