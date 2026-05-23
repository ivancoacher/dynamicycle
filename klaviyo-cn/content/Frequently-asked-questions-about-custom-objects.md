---
id: "37711720137755"
title: "有关自定义对象的常见问题"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/37711720137755-Frequently-asked-questions-about-custom-objects"
section: "Getting started with objects"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:56:55Z"
language: "zh"
---
## 你将会学到

了解与 Klaviyo 中的自定义对象相关的常见问题。如果您在下面的资源中没有看到您的问题，请访问我们的[社区论坛](https://community.klaviyo.com/)。 ## 关于对象的一般问题

### 我需要开发人员来创建对象吗？是的，此功能依赖于使用 API 来发送数据源并最终创建对象。 ### 我可以使用 Klaviyo 表单或 CSV 上传创建自定义对象吗？ Klaviyo 目前要求帐户通过 API 向我们发送数据来创建新的自定义对象。 ### 什么时候应该使用自定义对象而不是配置文件属性或事件？当自定义对象代表的类别与配置文件之间存在多对一关系时，您应该使用自定义对象。例如，如果您想保留有关客户宠物的信息，并且您的客户可能有不止一只宠物，则将这些宠物表示为自定义对象比配置文件属性或事件要好得多。当跟踪会员状态等项目时，个人资料一次只能有一种状态，个人资料属性更适合。但是，如果您还想存储有关个人资料成员资格的其他详细信息，则对象可以更好地工作。当跟踪广泛的内容时，例如收件人打开电子邮件的次数，我们建议使用事件。 ### 创建自定义对象后可以更新吗？是的，您始终可以向自定义对象添加其他非必需属性。有关更多信息，请阅读[更新自定义对象](https://help.klaviyo.com/hc/en-us/articles/35105337172123)。 ### 我应该什么时候发出事件而不是更新自定义对象的属性？事件旨在快速触发流程，使您能够及时发送相关消息。当对象的状态发生变化并且您希望因此触发消息时，您应该使用新信息更新对象并向我们发送一个事件以触发流程。您可以使用事件触发流程中的对象信息[个性化模板](https://help.klaviyo.com/hc/en-us/articles/35146367972763)。有两种方法可以实现此目的：

1. 使用“{{ event }}”标签在事件元数据中添加相关属性，以便在模板中使用。当及时性很重要时，这很有效。 2. 在事件的元数据中包含对象的 ID，这样您就可以使用“{% customobject id={{ event.pet_id }} as pet %}”在模板中获取对象。但是，使用最新属性更新对象可能需要一些时间，因此流可能会在对象更新之前触发消息发送。 ## 关于发送对象数据的问题

### 如何开始发送自定义对象的数据？ 1. [使用我们的 API](https://developers.klaviyo.com/en/reference/create_data_source) 创建一个新数据源。 2. 定义数据结构（请参阅示例 JSON）。 3. 通过[API](https://developers.klaviyo.com/en/reference/bulk_create_data_source_records)将您的数据源记录发送到Klaviyo。 4. [创建](https://help.klaviyo.com/hc/en-us/articles/35105337172123#h_01JPSTEQJQYKW8Y4AEKSPQ6YSF)您的自定义对象。 5. 创建自定义对象和配置文件之间的关系。 ### 数据源是如何创建和使用的？自定义对象是从数据源创建的。您的开发人员需要使用我们的[自定义对象 API](https://developers.klaviyo.com/en/reference/create_data_source) 创建新的数据源。创建新数据源后，Klaviyo 将返回一个唯一标识符作为 API 请求响应的一部分。这使得 Klaviyo 能够识别数据源，特别是在一个帐户具有多个数据源的情况下（例如，品牌业务所依赖的每个自定义集成、数据仓库或自定义第三方集成有 1 个数据源）。有了这个唯一标识符，您的开发人员就可以通过 [Klaviyo 的 API](https://developers.klaviyo.com/en/reference/bulk_create_data_source_records) 创建数据源记录。 ### ****我应该如何格式化我的数据？****

您的开发人员需要将 JSON 格式的数据发送到 Klaviyo。我们建议您以带有逗号分隔列表的文本形式发送数据。您将能够使用分段和流过滤的“包含”运算符来过滤此逗号分隔字符串中的值。 有关过滤的更多信息，请参阅[段条件参考](https://help.klaviyo.com/hc/en-us/articles/115005062847)。自定义对象中支持的[数据类型](https://help.klaviyo.com/hc/en-us/articles/115005237648)：

- 文字
- 整数
- 十进制
- [日期](https://help.klaviyo.com/hc/en-us/articles/115005237648#h_01J15GVP683H6QPWVMJDA9HGYM) - 在我们的系统中所有日期时间均转换为 UTC。例如，如果您上传“2025-04-03”，它将转换为“2025-04-03 00:00:00”。对于时区提前三个小时的客户，日期时间将显示为“2025-04-02 21:00:00”。 - [布尔](https://help.klaviyo.com/hc/en-us/articles/115005237648#h_01J15GVP68YBJZ962DJ3TRRR9H)

目前不支持列表数据类型。有关数据源记录 API 的示例负载，请参阅[批量创建数据源记录](https://developers.klaviyo.com/en/reference/bulk_create_data_source_records)。发送电话号码时，必须采用 [E.164 格式](https://help.klaviyo.com/hc/en-us/articles/360046055671)。发送日期时，它们必须采用我们的[可接受的时间戳格式](https://developers.klaviyo.com/en/docs/acceptable_date_and_timestamp_formats_for_profile_and_event_properties)之一。 ### ****自定义对象的数据限制是多少？****

每个媒体资源最多可上传 2 KB，每条总记录最多可上传 8 KB。 ### ****我可以使用嵌套数据进行映射吗？****

我们建议定义 JSON 对象时不要嵌套要用于自定义对象的属性。如果源数据深度嵌套或使用列表，则需要将 JSON 路径手动输入到对象管理器中。对于列表，您只能将属性映射到该列表中的位置（例如，第一个或第二个值）。 ### ****我可以将多个标识符与一个配置文件关联吗？****

是的，如果您想使用 2 个或更多配置文件标识符（例如电子邮件和电话号码）将自定义对象记录与配置文件关联，请确保在每次同步中都包含这两个属性，即使其中一个属性的值为 null。 ## 关于使用流对象的问题

### 如果我的对象没有触发流，并且我没有来自事件的对象 ID，我仍然可以个性化我的消息传递吗？是的，您可以使用[对象过滤器](https://help.klaviyo.com/hc/en-us/articles/35146367972763#h_01JPTH5R8840K0Q3XWH2CFYWRY)在个性化您的消息时找到正确的对象。 ### 当对象触发流时，我可以预览流消息吗？目前，当您使用“{{ object }}”标签时，无法使用应用程序中的预览功能查看消息。要测试流消息：

1. 创建一个[日期触发流](https://help.klaviyo.com/hc/en-us/articles/360002732652)并将其设置为实时。 2. 创建一个包含对象的配置文件，该对象的日期将在至少 24 小时内触发。 ### 我可以使用 webhooks 和 Klaviyo 代码等流程操作更新我的对象吗？此时，我们建议您先更新原始数据源，然后将修改后的对象以允许的格式发送回 Klaviyo。如果这两个系统不同步，您可能会冒着从系统将过时记录发送回 Klaviyo 的风险，将其恢复为原始值。