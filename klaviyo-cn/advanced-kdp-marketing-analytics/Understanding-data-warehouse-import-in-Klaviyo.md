---
id: "40939206649627"
title: "了解 Klaviyo 中的数据仓库导入"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40939206649627-Understanding-data-warehouse-import-in-Klaviyo"
section: "Syncing"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:55Z"
language: "zh"
---
![雪花更新.gif](https://klaviyo.zendesk.com/hc/article_attachments/41426468027419)

[高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672)，了解如何购买此计划。

＃＃ 介绍 。

数据仓库导入允许 Klaviyo 直接连接到 Snowflake 或 BigQuery 数据仓库，并为配置文件数据的表（或视图）配置导入同步。

事件和自定义对象导入同步即将推出，对其他数据仓库的支持也是如此。

## Klaviyo 中的数据仓库导入如何工作？

与仓库建立连接后，您可以选择要同步的数据集（例如表或视图）。

数据集必须包含配置文件标识符和修改后的时间戳。数据列可以映射到特定的配置文件属性，包括自定义属性。

按照所需的时间间隔（例如每小时、每天），Klaviyo 将提取自上次运行以来创建或修改的任何记录，然后导入它们，相应地创建或更新配置文件。

如果您没有包含要同步的所有字段的完全连接数据集，则可以使用不同的字段映射（例如联系信息、忠诚度余额和自定义细分）创建多个同步。

就有效值和格式而言，电子邮件和短信同意的工作方式与文件或 SFTP 上传的工作方式相同。

## 常见用例

### 档案管理

- 在 Klaviyo 中创建源自未与 Klaviyo 直接集成的系统的新配置文件（例如 POS、预订或订单管理系统）
- 从仓库内可用的离线来源更新 Klaviyo 中的个人资料信息。

### 个人资料丰富

- 将忠诚度计划余额同步到自定义 Loyalty\_Balance 属性。
- 同步仓库中运行的自定义模型的分数或类别（例如，定制生命周期事件的意图分数、亲和力类别、流失风险或 LTV 指标。）
- 将第三方人口统计或行为丰富数据同步到自定义配置文件属性
- 将支持或服务接触点同步到自定义配置文件字段中，以表示客户是否有开放的服务请求、自上次服务访问以来的天数或最近的支持交互类别。

### 自定义细分

- 在仓库内执行复杂的分段，并将分段名称同步到自定义配置文件属性，以用作分段或流程中的条件。
- 根据敏感、机密或受监管的数据在仓库内执行分段，并使用经过净化的名称（例如 A 组、B 组）作为自定义配置文件属性同步分段组分配或配置文件标记

## 设置指南

### 建立连接

这些文章提供了设置数据仓库导入的分步说明。

[****连接 Klaviyo 和 Snowflake****](https://klaviyo.zendesk.com/hc/en-us/articles/41373252392731)

[****连接 Klaviyo 和 BigQuery****](https://klaviyo.zendesk.com/hc/en-us/articles/41406928654107)

[****连接 Klaviyo 和 Redshift****](https://klaviyo.zendesk.com/hc/en-us/articles/42790298131611)

[****连接 Klaviyo 和 Databricks****](https://klaviyo.zendesk.com/hc/en-us/articles/42790208080283)

### 导入事件数据

[了解数据仓库事件导入](https://klaviyo.zendesk.com/hc/en-us/articles/45442043369499)

### 调试新同步

如果您设置了新的同步，但没有看到配置文件如您所期望的那样更新，我们建议您利用基于网络的列表上传工具中的错误报告来验证您的数据，特别是在同意字段和时间戳的情况下。

****识别源数据中的任何潜在错误：****

1. 将源表/视图导出到 CSV 文件。
2. 前往【观众 |仪表板中的列表和细分](https://www.klaviyo.com/lists)。
3. 选择现有列表或创建新列表以进行测试
4. 在右上角的“管理列表”菜单中选择“导入联系人”。
5. 上传第 1 步中的 csv 文件。
6. 如果数据存在任何问题，导致同步无法成功完成，这些问题将在可下载的错误文件中提供。