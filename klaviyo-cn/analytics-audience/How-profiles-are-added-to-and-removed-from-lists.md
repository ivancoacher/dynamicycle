---
id: "4407853491483"
title: "如何在列表中添加和删除配置文件"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4407853491483-How-profiles-are-added-to-and-removed-from-lists"
section: "Getting started with lists and segments"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:56:57Z"
language: "zh"
---
## 你将会学到

了解在 Klaviyo 中将配置文件添加到列表或从列表中删除的各种方式。在大多数情况下，配置文件会在他们订阅时添加到列表中，并在他们从该列表取消订阅时删除。还有几种方法可以手动或通过集成在列表中添加和删除配置文件，如下所述。

本文中的信息适用于列表，不适用于段。配置文件根据其操作和配置文件数据[动态添加到分段中或从分段中删除](https://help.klaviyo.com/hc/en-us/articles/115005233488)。

## 如何将配置文件添加到列表中

如果满足以下条件，配置文件将被添加到列表中：

- 通过 Klaviyo 注册表单或订阅页面订阅
  - 例外：仅限交易的 SMS 订户不会添加到列表中。
- 通过第三方集成或 Klaviyo 的 API 添加
- 通过快速添加添加
- 包含在 CSV 上传中
- 当 Klaviyo 用户从个人资料的 **列表和分段** 选项卡中单击 **添加到列表**** 时添加

单个配置文件可以添加到无限数量的列表中。如果配置文件重复订阅同一列表（例如，通过多次填写注册表单），它们仍然是列表的成员，但不会创建重复的配置文件。

准备好将订阅者导入您自己的列表了吗？了解如何[添加单个订阅者或上传订阅者列表](https://help.klaviyo.com/hc/en-us/articles/115005251128)。

## 如何从列表中删除配置文件

如果出现以下情况，配置文件将从列表中删除：

- 取消订阅该列表
- 是否[被抑制](https://help.klaviyo.com/hc/en-us/articles/115005246108) 和用户[从列表中删除被抑制的个人资料](https://help.klaviyo.com/hc/en-us/articles/115005077307)
- 由用户单击其个人资料中列表名称旁边的****删除****来删除
- 从 Klaviyo 中删除（例如，由用户手动删除）
- 通过第三方集成或 API 从列表中删除

如果某个个人资料被营销渠道（例如电子邮件或短信）禁止，则它们可能仍然是列表的一部分，具体取决于它们被禁止的方式。当您向他们发送消息时，所有被抑制的联系人都将被跳过，以避免损害您的发件人声誉。