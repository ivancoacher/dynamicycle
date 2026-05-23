---
id: 6724
title: "如何在 Klaviyo 中进行预热"
slug: "warmsendingdomain"
category: "账户与计费（Account &amp; Billing）"
category_slug: "account-billing"
wp_url: "https://dynamicycle.com/docs/warmsendingdomain/"
wp_modified: "2026-01-30T08:13:28"
---

##### 了解如何在 Klaviyo 中预热你的发送基础设施

****预热发送基础设施**** 是训练邮箱服务商将你识别为“良好发件人”的过程。每当你迁移到新的邮件服务提供商（ESP），这个步骤都是必不可少的。

##### 在开始之前

所有使用新的 Klaviyo 客户 都必须完成相应的域名预热流程。在开始之前，请确认你的品牌应使用哪种预热路径：

- 如果你的品牌属于****标准预热流程****，请按照本指南中的建议操作。
- 如果你的品牌应使用****平台引导预热流程****，请遵循对应的步骤。

域名预热路径的选择取决于你的品牌规模、发送历史等条件。

##### 引导式预热（Guided Warming）

如果你的品牌属于 Klaviyo 的标准预热流程，那么在你开始提升发送量或满足条件时，系统可能会在账户中显示引导式预热通知。

在引导预热过程中，Klaviyo 会判断你的 Campaign 发送行为是否与当前预热阶段相符。如果你超出了建议的受众规模，Klaviyo 会发出提醒，并自动排除未活跃的用户群体，以帮助你合理预热账户。

###### 迁移历史互动数据

如果你是因为从其他邮件服务提供商（ESP）迁移到 Klaviyo 而进行发送基础设施预热，那么将历史互动数据一并迁移至关重要。这能帮助你准确构建已互动用户的细分受众（segment），并确保预热阶段的发送对象是与你品牌已有联系的订阅者。

这样，你可以以正面的方式将你与 Klaviyo 的新发送关系介绍给邮箱服务提供商（Mailbox Providers, MBPs）——只向那些已经表现出兴趣的用户发送邮件，避免打扰不再活跃或不希望接收邮件的人。

Klaviyo 提供了多个平台的数据迁移指南，帮助你导入包括打开率、点击率等在内的互动数据。支持的平台包括：

- Mailchimp
- Constant Contact
- Campaign Monitor
- Listrak
- Sailthru
- Salesforce Marketing Cloud

##### 从旧 ESP 需要导出哪些数据？

建议至少准备以下几个 CSV 文件：

1. ****主订阅名单（Active Subscribers）****
2. 建议字段包含：
   - Email（必填）
   - 名 / 姓（如有）
   - 订阅状态（例如：已订阅 / 已退订）
   - 注册日期 / 订阅日期（如有）
   - 其他您希望在 Klaviyo 中继续使用的客户属性（国家、语言、VIP 等级等）
3. ****历史互动数据（用于建立“已互动分组”）****
4. 如果旧平台支持，建议同时导出：
   - 最近一次打开日期（Last Open Date）
   - 最近一次点击日期（Last Click Date）
   - 过去 30 / 60 / 90 / 180 天有打开或点击的标记（有些 ESP 会直接帮您打好标签）
5. 将这些字段导入 Klaviyo 之后，可以快速建立「30 天内有互动」「90 天内有互动」等分组，对后续健康预热非常关键。
6. ****退订及禁止发送名单（Unsubscribes / Suppression List）****
   - 建议准备一个****仅包含 Email**** 的 CSV 文件（不要含其他字段，以免被系统拒绝导入）
   - 这份名单会导入 Klaviyo 的 Suppressed（已抑制）列表，确保这些地址不会再收到营销邮件。
7. ****（如适用）硬退信 / 无效地址名单****
   - 如果旧 ESP 能导出「硬退信（Hard Bounce）」或明显无效的 Email，也可以另存一份 CSV
   - 这类地址同样可以在 Klaviyo 端做抑制，减少预热期间的退信与风险。

如果您目前使用 Mailchimp、Constant Contact 等平台，Klaviyo 也有对应的迁移说明，可以参考：[Migrate from Another Email Service Provider to Klaviyo](https://us-42115.email-composer-webhooks.gong.io/email-tracking/clicked?email-info-token=eyJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiI4NDg3MjI0NDUzNjkyNjA2OTY1IiwiZHJhZnRJZCI6InI3MTg0ODM4NTMyMTQ5Njg2MDM5IiwibGlua1VybCI6Imh0dHBzOi8vaGVscC5rbGF2aXlvLmNvbS9oYy9lbi11cy9hcnRpY2xlcy8xMTUwMDUwODI3NjctTWlncmF0ZS1mcm9tLUFub3RoZXItRW1haWwtU2VydmljZS1Qcm92aWRlci10by1LbGF2aXlvIiwibGlua1RleHQiOiJNaWdyYXRlIGZyb20gQW5vdGhlciBFbWFpbCBTZXJ2aWNlIFByb3ZpZGVyIHRvIEtsYXZpeW8iLCJ0ZW1wbGF0ZUlkIjoiIiwiZXhwIjoxNzcxNTYzNDU5LCJpYXQiOjE3Njk3NDkwNTksImp0aSI6Ijh4cmJoMUl2THdtYyJ9.koOKOZKmnxDW9k_ZHI9kp7H5YabCjGunBXmFk7leb24)

##### 关键指南

****替换已嵌入的简单 sign-up forms****
确保将你网站上的所有现有 sign-up forms 切换为 Klaviyo forms，以确保这些用户现在会被添加到你在 Klaviyo 中的邮件列表。

****重定向集成的订阅表单****
如果你正在使用第三方表单工具（例如 Wufoo、Facebook 上的 forms 等）将用户发送到你的 ESP，请确保将它们调整为指向 Klaviyo。

****在结账时同步订阅者****
如果你通过购物车结账流程自动收集 email 订阅者，请确保这些订阅者能同步到 Klaviyo；对于 Shopify 和 Magento 等平台，该功能可通过标准集成实现。

****导入当前的 bounces 和 unsubscribes****
如果你使用 Klaviyo 的内置集成从之前的 ESP 迁移，那么这里已经处理好了；如果没有，你需要确保任何退回/退订列表都直接上传到 Klaviyo 的 suppression list 中。

****迁移当前的 autoresponders****
将你现有的 autoresponders 迁移到 flows，并将其开启。

****迁移保存的 email templates****
如果你想把之前 ESP 的 email templates 转移到 Klaviyo，你可以按照我们的指南导入自定义 HTML 模板。

****确保所有现有订阅者已添加到 Klaviyo：****
如果你使用 Mailchimp、Campaign Monitor、Constant Contact、Mad Mimi，Klaviyo 提供内置集成来同步现有列表，你可以通过以下步骤找到该功能：

- 在 Klaviyo 中选择 Integrations 标签
- 点击 Explore apps
- 搜索你的 ESP，选择它，然后点击 Install 并按照流程完成设置

如果你的 ESP 不在我们的集成列表中，或者你有 CSV 或 Excel 格式的订阅者列表，你可以轻松将订阅者导入 Klaviyo。

完成以上所有步骤后，你将不再需要与之前的 ESP 保持关联。

##### 重要注意事项

- 确保你已将之前 ESP 中所有需要保留的数据导入 Klaviyo，这样在迁移完成后，这些数据才能正常使用。
- 在将所有 sign-up forms 切换为指向 Klaviyo 之后，等待几天并观察你在之前 ESP 中的列表。如果你发现仍然有订阅者被添加到旧 ESP 的列表中，那说明至少还有一个表单尚未替换。
- 在导入任何现有 email 列表之前，另一个需要重点考虑的问题是列表清理（list cleaning）。我们强烈建议你将清理后的列表导入 Klaviyo，并从第一次发送开始就向活跃受众发送。如果你计划同步或手动导入现有列表，而跳过清理步骤，你的邮件可达性可能会受到影响。

你的旧 ESP 通常会提供用于分析主列表互动度的工具，例如打开率、退回率等。在将订阅者列表迁移到 Klaviyo 之前，我们建议你使用所有可用的数据来找出并移除无效或不活跃的邮箱地址，这些地址只会拉低你的投递表现。这些操作都应在你进行第一次 Klaviyo 发送之前完成。
如果 Klaviyo 没有与你的 ESP 提供内置集成，你可以通过以下两种方式确保你向一个活跃列表发送：

- 上传包含互动数据的主列表，将互动信息作为 custom properties
- 上传单独的主列表、活跃列表和不活跃列表

完成以上任一方式后，你应在前几次 Campaign 中只向活跃列表或活跃 Segment 发送。

- 如果你是每日发送，请在第一周只发送给这组受众
- 如果你每周发送多次，请将前 2–3 次 Campaign 发送给该列表或 Segment

##### 在 Klaviyo 中如何导入这些数据？

1. ****在 Klaviyo 中建立 / 确认主订阅 List****
   - 在 ****Lists & Segments**** 中新建一个主邮件 List（例如「Main Newsletter Subscribers」），后续的主订阅 CSV 都会导入到这个 List 里。
2. ****导入主订阅名单（含客户属性和互动字段）****
   - 进入 ****Lists & Segments → 选择主订阅 List → Import****
   - 上传包含 Email + 其他字段的 CSV
   - 在映射（mapping）界面中：
     - 把 Email 字段映射到 Klaviyo 的 Email
     - 姓名、国家等映射到对应的 Profile 字段
     - 最近打开 / 最近点击日期等，映射为自定义属性（如 `last_open_date`、`last_click_date`）
3. 更详细的导入说明可参考：
   - [How to import your contacts from a previous ESP or CRM](https://us-42115.email-composer-webhooks.gong.io/email-tracking/clicked?email-info-token=eyJhbGciOiJIUzI1NiJ9.eyJjb21wYW55SWQiOiI4NDg3MjI0NDUzNjkyNjA2OTY1IiwiZHJhZnRJZCI6InI3MTg0ODM4NTMyMTQ5Njg2MDM5IiwibGlua1VybCI6Imh0dHBzOi8vaGVscC5rbGF2aXlvLmNvbS9oYy9lbi11cy9hcnRpY2xlcy8xMTUwMDIwNTM3NTItSG93LXRvLWltcG9ydC15b3VyLWNvbnRhY3RzLWZyb20tYS1wcmV2aW91cy1FU1Atb3ItQ1JNIiwibGlua1RleHQiOiJIb3cgdG8gaW1wb3J0IHlvdXIgY29udGFjdHMgZnJvbSBhIHByZXZpb3VzIEVTUCBvciBDUk0iLCJ0ZW1wbGF0ZUlkIjoiIiwiZXhwIjoxNzcxNTYzNDU5LCJpYXQiOjE3Njk3NDkwNTksImp0aSI6IkRPdnJ2VnR1elg4TSJ9.rMh7ycV1WoFS7zJvoBK9Gauseqw8766l-mZR5Q_RG2E)
4. ****导入退订 / 禁止发送名单****
   - 进入 ****Profiles → Suppressed Profiles****
   - 上传仅包含 Email 的 CSV
   - 这样可以保证今后从 Klaviyo 发送邮件时，不会误发给已经退订或不应联系的收件人。
5. ****（如有）导入硬退信 / 无效地址****
   - 同样在 Suppressed 中上传仅含 Email 的 CSV
   - 让这些地址一开始就被屏蔽，避免影响预热期的送达率和信誉。

###### 关闭你的 welcome series

你是否已经在 Klaviyo 中开启了 welcome series？如果是，在导入联系人之前应将其关闭，以避免向现有联系人发送欢迎邮件。导入完成后，再将其重新开启。

##### 识别你的活跃订阅者

首先，你需要在现有平台中清理联系人列表，将活跃订阅者与不活跃订阅者区分开来。
我们强烈建议将清理后的列表导入 Klaviyo，并在第一次发送时只向活跃列表发送邮件——如果你计划同步或手动导入现有订阅者，而跳过此步骤，你的邮件可达性可能会受到影响。

你的旧 ESP 很可能提供分析主列表互动度的功能，例如打开率、退回率等。在将订阅者列表迁移到 Klaviyo 之前，我们建议使用所有可用数据来识别并删除无效或不活跃的邮箱地址，因为这些地址只会拖慢发送表现和可达性。所有这些步骤应在你开始第一次 Klaviyo 发送之前完成。

你可以根据你能从旧 ESP 导出哪些数据，以以下两种方式将联系人导入 Klaviyo：

###### 导入方式 1：上传带有互动数据的主列表

适用于能从旧 ESP 导出以下字段的情况：

- 添加日期（date added）
- 上次打开时间（last opened）
- 上次点击时间（last clicked）

###### 导入方式 2：分别上传主列表、活跃列表和不活跃列表

适用于无法导出上述字段的情况。

###### 上传活跃主列表

导出一份包含你所有活跃邮箱地址的列表，并确保其中包括以下信息：

- ****Date added****（他们首次进入你账户的时间）
- ****Last opened****（他们上次打开你发送的邮件的时间）
- ****Last clicked****（他们上次点击你邮件中链接的时间）

每个 ESP 和 CRM 的导出方式都不同，如果你不确定如何导出这些数据，建议联系你的服务提供商的客服团队获取协助。

请注意：那些****未加入你的 email 列表、但曾下单、遗弃购物车等的联系人****会通过你的平台集成自动同步到 Klaviyo，而不是通过上传列表的方式同步。

##### 创建用于发送 Campaign 的 Engaged Segments

持续向高度活跃的用户发送邮件，有助于保持良好的发件人信誉，降低退订和投诉率，尤其是在你使用全新域名或刚迁移到 Klaviyo 时，前几次发送会显著影响你的发送声誉。

随着 iOS15、macOS Monterey、iPadOS 15 和 WatchOS 8 的发布，Apple 的 Mail Privacy Protection（MPP）通过预取追踪像素的方式改变了我们接收邮件打开率数据的方式。由于这一变化，需要注意打开率将会被抬高。

如果你的 Campaign 数据中显示有大量 iOS 用户的打开行为，我们建议在你的订阅者 Segments 中识别这些受影响的打开记录。

根据 30、60、90、120 和 180 天的互动情况创建 Segments。你会在后续发送中使用这些 Segments，并从 30 天的 Segment 开始。如果你向不活跃的订阅者发送邮件，你有可能被邮箱服务商（如 Google、Hotmail 等）判定为垃圾邮件。

如果你刚开始使用 Klaviyo 或从其他平台迁移过来，请利用你之前平台的历史互动数据来创建这些 Segments。

然而，如果你在预热期间尝试向超过建议数量的收件人发送 Campaign，Klaviyo 会向你发出警告，提示你查看本指南并减少 Campaign 的收件人数。对于你的第一次 Campaign，我们建议发送数量少于 10,000 人。随着你逐步向更多用户发送邮件，这一建议的收件人数会动态增长，因此警告也会相应调整。

##### 向活跃 Segments 发送 campaigns

当你开始向 30、60、90、120 和 180 天的 Segments 发送邮件时，你应尽量达到各阶段建议的打开率（如下文所示）。不过需要注意，不同行业与不同发件人之间的打开率会有所差异，因此请结合以下指导，同时尽力在你的业务中获得尽可能高的互动率。

##### 30 天 Segment（初始预热与每日发送）

在你的首次发送中，尽量争取达到 ****30% 以上的打开率****。要获得这样的打开率，你需要向以下用户组成的 Segment 进行发送：

- 最近 30 天内有点击行为的用户，或
- 最近 15 天内新订阅的用户

这些用户属于互动度最高的群体，有助于在预热阶段快速建立良好的发件人信誉。

![展示了一个电子邮件营销筛选界面，包含多个条件，如订阅状态和参与活动的时间窗口。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-156.png?resize=1024%2C646&ssl=1)

如果你的 30 天活跃 Segment 规模非常大，可以考虑以下做法：

###### 使用 Smart Send Time 分散发送

通过 Smart Send Time，你的邮件会在 24 小时内自动分散发送，从而将一次发送拆分为多个较小的发送批次，帮助你在预热期间更平稳地提升发送量。同时，你还能了解未来向这些订阅者发送邮件的最佳时间。
（注意：Smart Send Time 需要你的 Klaviyo 账户中至少有 12,000 名订阅者。）

###### 使用 Batch Sending 分批发送

通过 Batch Sending，可以将一次大规模发送拆分成多个较小的用户组，从而降低风险并保持良好的发送表现。

###### 从活跃 Segment 中随机抽样

对你的活跃 Segment 进行随机抽样，可以有效将大规模发送拆分为多个更小的组别。

###### 发送策略建议

请在此阶段保持保守的发送策略，尽可能追求高互动率。

- ****前两周****：专注向 30 天活跃 Segment 发送
- 只要打开率保持 ****20% 以上****，你就可以在第 3、4 周将活跃标准放宽到 ****60 天****
- 当 4 周内打开率始终达到至少 ****20%**** 时，可以将标准放宽到 ****90 天****

此后继续每两周逐步放宽标准。你的最佳活跃时间范围会根据业务需求有所不同。

###### 当打开率下降时

如果你的打开率降至 ****20% 以下****：

- 继续向当前活跃 Segment 发送
- 暂缓扩展到更宽的 Segment

这通常表明你的发件人信誉可能受到影响，需要先提升信誉，再扩大发送范围。

##### 60 天 Segment（每周发送最多 3 次）

在向 30 天活跃 Segment 连续发送两周并保持高互动后，如果扩大受众范围不会显著增加你的发送名单规模，你就可以将发送对象拓展到 60 天活跃 Segment。

在这个阶段，请继续保持保守的发送频率（每周最多 3 次），并确保：

- 打开率持续高于 20%
- 若打开率低于 20%，请立即回到 30 天 Segment 继续发送，以恢复发件人信誉
- 保持稳健的发送策略，将有助于你的域名持续建立良好信誉。

![用于邮箱营销过滤条件的界面元素，包含接收营销、打开邮件、点击邮件和订阅状态的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-157.png?resize=1024%2C822&ssl=1)

##### 90 天 Segment（每周最多发送 2 次）

如果你在使用 60 天活跃 Segment 时表现良好，你可以将受众进一步扩展到 ****90 天活跃 Segment****。

与前面阶段一样，请确保：

- ****打开率维持在 20% 或更高****
- 如果打开率低于 20%，请收紧范围，回到较短的活跃时间窗口（如 60 天或 30 天）

- 保持高互动率是持续提升发送信誉的关键。

![显示过滤器的电子邮件营销设置界面，包括选择可以接收营销的人员、他们的订阅状态以及过去90天内的电子邮件打开和点击活动的条件。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-158.png?resize=1024%2C799&ssl=1)

##### 120 天 Segment（每周发送）

在向 30–90 天的活跃用户群体发送数周后，你可以将活跃条件进一步放宽到 ****120 天****（或 180 天）。

在此阶段，依然需要：

- ****保持打开率高于 20%****
- 继续监测表现，确保发送质量稳定

- 逐步扩大活跃窗口可以让你安全地触达更多用户，同时保持良好的发件人信誉

![设置电子邮件营销接收条件的界面，包含过滤器选项，如订阅状态、打开邮件和点击邮件的时间范围等。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-159.png?resize=1024%2C793&ssl=1)

##### 180 天 Segment（每月发送）

如果你在向更近期的活跃 Segments 发送时表现良好，可以将活跃范围扩展到 ****180 天****。

但需要注意：

- 如果打开率低于 ****20%****，请立即将活跃范围收紧回 ****120 天**** 或更短
- 在此阶段保持低频发送（每月一次）有助于保护你的发件人信誉
- 通过谨慎扩大发送范围，你可以在保持互动率的同时逐步触达更多订阅者。

![电子邮件营销筛选条件界面，包含关于订阅者是否可以接收营销邮件、打开和点击电子邮件的活动时间限制，以及与通讯列表相关的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-160.png?resize=1024%2C816&ssl=1)

##### 启用高互动度的 Flow 邮件

当你已经创建并向所有活跃 Segments 发送过邮件后，就可以开始开启你的Flows。
此时****只应开启历史表现良好的 flows****，以确保你的发送信誉在预热阶段继续保持稳定。

你应重点检查并启用以下三类高互动Flows：

- ****Welcome series****（欢迎系列）
- ****Abandoned cart****（购物车遗弃）
- ****Browse abandonment****（浏览遗弃）

这些Flows通常拥有高打开率和高点击率，有助于在预热期间进一步巩固你的发件人信誉。

###### 判断哪些是你的高互动度 Flows

我们建议你先回顾这些 flows 过去的表现，****只有在它们的表现足够好时才开启****。
以下是判断 flow 是否属于高互动和高表现的参考指标：

- ****Open rate 高于 40%****
- ****Click rate 高于 1%****
- ****Unsubscribe rate 低于 0.1%****
- ****Complaint rate 低于 0.1%****

###### 如果你没有高表现的Flows，该怎么做？

若你的 flows 过去表现并不理想，请按照以下时机再开启：

- ****Welcome series****：在使用 Klaviyo 发送 campaigns ****满 2 周后****
- ****Abandoned cart****：在发送 campaigns ****满 30 天后****
- ****Browse abandonment****：在发送 campaigns ****30–60 天之间****

### 需要更晚开启的高风险 Flows

****Winback、re-engagement 和 sunset flows**** 通常属于高风险类型，因为它们本身的互动率就偏低。
因此在预热尚未完全完成之前，不建议开启这些 flows。

若你需要创建这些 flows，可参考以下资源：

- Creating a winback flow
- Creating a sunset flow
- Creating a re-engagement flow

##### 监测数据

以下工具可以帮助你在预热发送域的过程中持续监控数据表现：

###### 查看 flow analytics

定期查看 flows 的打开率、退订率和垃圾邮件投诉率，以评估订阅者与这些邮件的互动情况。

###### 使用 trends report 监测 campaigns

trends report 会显示所有关键邮件互动指标随时间的变化趋势。
特别要关注以下图表：

- ****Marked as spam（被标记为垃圾邮件）****
- ****Hard bounce（硬退回）****

如发现任何异常上升，应回溯相关 campaigns 并检查导致行为波动的原因。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)