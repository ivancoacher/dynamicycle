---
id: "115002053752"
title: "如何从以前的 ESP 或 CRM 导入联系人"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002053752-How-to-import-your-contacts-from-a-previous-ESP-or-CRM"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T10:57:19Z"
language: "zh"
---
## 你将会学到

了解如何将联系人从以前的电子邮件服务提供商 (ESP) 或客户关系管理平台 (CRM) 导入到 Klaviyo。 Klaviyo 提供内置集成来同步来自某些 ESP 和 CRM 的数据。 ## 开始之前

如果您要从以下任何 ESP 迁移，我们有针对您的使用案例的说明，您应该参考这些说明：

- [活动监控](https://help.klaviyo.com/hc/en-us/articles/115005254968)
- [持续联系](https://help.klaviyo.com/hc/en-us/articles/115005082727)
- [Hubspot](https://help.klaviyo.com/hc/en-us/articles/360039708512-How-to-Migrate-from-HubSpot)
- [Salesforce 营销云](https://help.klaviyo.com/hc/en-us/articles/115000267471)
- [Listrak](https://help.klaviyo.com/hc/en-us/articles/360034550591)
- [Mailchimp](https://help.klaviyo.com/hc/en-us/articles/115005254948)
- [Sailthru](https://help.klaviyo.com/hc/en-us/articles/360036945872)

如果您来自其他服务，请继续阅读以了解如何将联系人和数据导入 Klaviyo。本文专门介绍了导入联系人，但有关从其他服务迁移到 Klaviyo 的一般准则，[查看我们的迁移指南](https://help.klaviyo.com/hc/en-us/articles/115005082767)。 ## 关闭您的欢迎系列

您已经在 Klaviyo 中打开了[欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172) 吗？如果是这样，您应该在导入之前将其关闭，以避免向现有联系人发送欢迎消息。完成后，将其重新打开。 ## 确定您的订阅者

首先，您需要清除现有平台中的联系人列表。这涉及区分参与和未参与的订户。我们强烈建议您将干净的列表导入到 Klaviyo 中，并在第一次发送时发送到已参与的列表 - 如果您打算同步现有电子邮件列表，或手动将现有列表导入到 Klaviyo 中，如果您跳过此步骤，您的电子邮件送达率可能会面临风险。您以前的 ESP 可能提供了一种使用打开率、跳出率等数据点来分析主列表参与度的方法。在将任何现有订阅者列表迁移到 Klaviyo 之前，我们建议使用所有可用数据来隔离和删除任何无效或不活动的电子邮件，这些电子邮件只会使您的发送变得臃肿并降低您的送达率。这一切都应该在您第一次使用 Klaviyo 发送之前完成。您可以通过两种方式将联系人导入 Klaviyo，具体取决于您可以从现有提供商导出哪些信息：

1. 上传包含参与标准的主列表 - 这适用于那些可以从之前的 ESP 导出添加日期、上次打开和上次点击时间戳的人
2. 上传单独的主要列表、参与列表和非活动列表 - 这适用于无法从之前的 ESP 导出添加日期、上次打开和上次点击时间戳的用户

## 上传参与的主列表

导出列表中所有活动电子邮件的列表，其中包含以下信息：

- 添加日期（当他们第一次进入您的帐户时）
- 上次打开（他们上次打开您发送的电子邮件的时间）
- 最后一次点击（他们最后一次点击您发送的电子邮件中的链接的时间）

每个 ESP 和 CRM 都不同，因此如果您不确定如何导出此信息，我们建议您联系您的服务的支持团队。请注意，不在您的电子邮件列表中但已下订单、放弃购物车等的联系人将通过您的集成进行同步，而不是通过列表上传进行同步。 ### 设置数据格式

1. 将这些数据保存在 CSV 中后，您需要将这些日期/时间值添加为[自定义属性](https://help.klaviyo.com/hc/en-us/articles/115005074627)。这将允许您根据此信息在 Klaviyo 中构建分段。 2. 为了上传这些联系人，您至少必须有一个“电子邮件地址”栏。除了您想要同时上传的任何其他自定义属性（例如“性别”）之外，您可能还需要添加“名字”和“姓氏”列。 3. 请务必采用以下格式之一输入添加日期、上次打开日期和上次单击日期：
   年-月-日 时:分:秒
   月/日/年 时:分:秒
   月/日/年 时:分:秒
   月/日/年 时:分
   月/日/年 时:分
   YYYY-MM-DDTHH:MM:SS
   如果您不使用此格式，Klaviyo 不会将该值识别为时间戳。 如果您使用的是 Excel，则可以通过将单元格格式更改为“文本”来删除自动格式设置。如果没有与日期关联的时间，您可以使用 HH:MM:SS 值 00:00:00 将其设置为午夜。 4. 完成后，CSV 的格式应如下所示：
   ![显示联系人 bob.klaviyo@example.com 的电子表格，其中包含名字、姓氏、添加日期 - 旧 ESP 等字段](https://klaviyo.zendesk.com/hc/article_attachments/28723623146907)
5. 接下来，您可以[将此作为主列表上传到Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005078967)。 ### 在 Klaviyo 中建立一个参与的细分市场

将主列表上传到 Klaviyo 后，您就可以构建一个参与的细分并开始发送。请查看我们的[如何创建参与细分](https://klaviyo.zendesk.com/hc/en-us/articles/115000200072)。 ## 上传单独的主要列表、参与列表和非活动列表

1. 如果您无法从之前的 ESP 或 CRM 导出添加日期、上次打开和上次点击时间戳，您可以根据参与度上传三个单独的列表。在您之前的平台中，根据以下标准构建细分：
   - ****主要列表****
     您的电子邮件列表中的每个人
   - ****参与列表****您的电子邮件列表中在过去 120 天内至少打开或单击过一次电子邮件的每个人，或者在过去 120 天内被添加到您的电子邮件列表中的每个人。 - ****非活动列表****在列表中超过 120 天或在过去 120 天内未打开或单击电子邮件的每个人
2. 将这些列表导出为 CSV 并将其上传到 Klaviyo。请记住，如果列表中的每个人都明确同意接收您的电子邮件营销，请仅在“导入审核”步骤中单击“订阅电子邮件营销”。 3. 如果您是每日发送者，请将您第一周的营销活动发送到您的参与列表。如果您是每两周发送一次的发送者，请将您的前 2-3 个营销活动发送到此列表。 ## 将禁止的联系人上传到您的禁止列表

上传这些列表后，您需要将所有已退订、硬退回或将您的电子邮件标记为垃圾邮件的联系地址上传到您帐户的[禁止列表](https://help.klaviyo.com/hc/en-us/articles/115005078487)。这将确保您不会意外地向他们发送电子邮件并损害您的送达率。 ## 结果

现在，您已从之前的 ESP 或 CRM 导入了联系人。 ## 其他资源

- [CSV 文件日期格式参考](https://help.klaviyo.com/hc/en-us/articles/360039859932)
- [了解电子邮件送达率](https://klaviyo.zendesk.com/hc/en-us/articles/115005247008)
- [列表导入疑难解答](https://help.klaviyo.com/hc/en-us/articles/115005078807)