---
id: "24990565562139"
title: "如何取消设置配置文件属性"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/24990565562139-How-to-unset-profile-properties"
section: "Profile management"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:35Z"
language: "zh"
---
## 你将会学到

了解如何从 Klaviyo 中的配置文件中批量删除配置文件属性。如果您想要为一组配置文件删除某个配置文件属性，则可以使用 CSV 上传来完成此操作。

## 通过 CSV 上传取消设置配置文件

Klaviyo 属性 **$id** 无法取消设置。如果您需要删除此属性，请联系 [Klaviyo 的支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272)。

首先，将要删除属性的所有配置文件分组到列表或分段中，然后[导出组](https://help.klaviyo.com/hc/en-us/articles/115005078687)。导出组时，您只需选择要删除的属性。

导出 CSV 文件后，您需要更新它以匹配以下结构：

1. 第一列应具有标题 **电子邮件**，每行对应于将删除该属性的配置文件的电子邮件地址。
2. 第二列应具有标题 **$unset**，每行包含要删除的属性的名称。必须采用列表格式（例如，（“属性 A”、“属性 B”、“属性 C”））。

要取消设置本机 Klaviyo 属性，请添加前缀 $。例如，要取消设置 [Klaviyo 属性](https://help.klaviyo.com/hc/en-us/articles/115005074627#h_01HA32RZBA24MZSHF2MQK71861) 城市，请在 CSV 文件中使用 $city 。

![unsetCSV.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716118917915)

当您的文件格式正确并准备好上传时，请选择一个新的或现有的列表来[上传配置文件](https://help.klaviyo.com/hc/en-us/articles/115005251128)。

![导入联系人按钮](https://klaviyo.zendesk.com/hc/article_attachments/28716118928923)

在您进入的 **导入联系人页面** 上，将具有您的属性的列映射到 Klaviyo 字段 **$unset**，并将该列的数据类型设置为 **List**。

映射文件时，您必须使用“创建新字段”选项手动写入此内容，因为默认情况下不会填充**$unset**。

![$unset.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716118919707)

完成映射后，选择****下一步****，成功上传后，相关属性将从文件中包含的配置文件中删除。

## 其他资源

[配置文件属性参考](https://help.klaviyo.com/hc/en-us/articles/115005074627)

[如何导出列表或细分](https://help.klaviyo.com/hc/en-us/articles/115005078687)