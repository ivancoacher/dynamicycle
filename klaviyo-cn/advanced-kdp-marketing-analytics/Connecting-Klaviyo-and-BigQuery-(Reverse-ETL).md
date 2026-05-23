---
id: "41406928654107"
title: "连接 Klaviyo 和 BigQuery（反向 ETL）"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41406928654107-Connecting-Klaviyo-and-BigQuery-Reverse-ETL"
section: "Syncing"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: "zh"
---
[高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672)，了解如何购买此计划。 # 环境设置和连接

****概述：**** 请按照以下步骤为 Klaviyo 准备 BigQuery。您将创建所需的架构（在数据集/项目中）、设置专用服务帐户和密钥、分配所需的最低权限、验证配置并将 BigQuery 连接到 Klaviyo。有关数据仓库导入如何在 Klaviyo 中工作的详细信息（包括架构结构、所需的表和字段映射），请参阅[数据仓库导入如何在 Klaviyo 中工作](https://help.klaviyo.com/hc/en-us/articles/40939206649627)。 ---

## 1) 创建所需的模式/数据集

在 BigQuery 中，在将用于 Klaviyo 的项目中创建两个数据集。 ````
创建架构“KLAVIYO_IMPORT_FROM_DWH”；
创建模式“KLAVIYO_TMP”；
````

- `KLAVIYO_IMPORT_FROM_DWH`：在此数据集中创建的表和视图可供 Klaviyo 读取/写入。 - `KLAVIYO_TMP`：同步操作期间使用的临时或暂存数据。 ---

## 2) 创建 Klaviyo 服务帐户和密钥

创建一个 Google 服务帐户（例如 KLAVIYO\_DATA\_TRANSFER\_USER），Klaviyo 将专门用于此集成。下载此帐户的 JSON 密钥并安全存储。 - 转至 GCP Console 中的 ****IAM 和管理 → 服务帐户****。 - 创建一个新的服务帐户（或选择专用于 Klaviyo 的现有帐户）。 - 在“密钥”选项卡中，创建 JSON 类型的新密钥。确保此密钥文件安全 - 在 Klaviyo 中配置连接时需要它。 ---

## 3) 分配所需的权限

向服务帐户授予以下角色，范围仅限于您创建的两个数据集：

|数据集 |最低所需角色 |描述 |
| --- | --- | --- |
| `KLAVIYO_TMP` | `BigQuery 数据编辑器` + `BigQuery 作业用户` |允许 Klaviyo 创建和管理临时表、作业等。
| `KLAVIYO_IMPORT_FROM_DWH` | `BigQuery 数据查看器` + `BigQuery 作业用户` |允许 Klaviyo 从您的表中读取内容。 |

````
-- GCP CLI 中的示例命令（替换占位符）：
gcloud 项目 add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:KLAVIYO_DATA_TRANSFER_USER@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataEditor" \
  --条件=无 \
  --数据集=“KLAVIYO_TMP”

gcloud 项目 add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:KLAVIYO_DATA_TRANSFER_USER@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataViewer" \
  --条件=无 \
  --dataset="KLAVIYO_IMPORT_FROM_DWH"
````

---

## 4) 验证您的设置（可选）

### 4.1 确认数据集存在

````
选择模式名称
来自“YOUR_PROJECT_ID.INFORMATION_SCHEMA.SCHEMATA”
WHERE schema_name IN ('KLAVIYO_IMPORT_FROM_DWH','KLAVIYO_TMP');
````

### 4.2 确认服务帐户访问

使用服务帐户密钥通过 BigQuery CLI 或 API 进行身份验证并运行简单的查询：

````
bq --project_id=您的项目ID \
   --dataset_id=KLAVIYO_IMPORT_FROM_DWH \
   查询 --use_legacy_sql=false \
   '从 `YOUR_PROJECT_ID.KLAVIYO_IMPORT_FROM_DWH.some_table` LIMIT 1 选择 COUNT(*) 个'
````

### 4.3 检查每个数据集的权限

````
选择*
来自“YOUR_PROJECT_ID.KLAVIYO_IMPORT_FROM_DWH.INFORMATION_SCHEMA.OBJECT_PRIVILEGES”
WHERE 受让人 = 'KLAVIYO_DATA_TRANSFER_USER@YOUR_PROJECT_ID.iam.gserviceaccount.com';
````

### 4.4 可选：验证创建/读取操作

````
-- 在 KLAVIYO_TMP 中测试创建
创建表`YOUR_PROJECT_ID.KLAVIYO_TMP.test_permissions`（id INT64）；
删除表`YOUR_PROJECT_ID.KLAVIYO_TMP.test_permissions`；

-- 在 KLAVIYO_IMPORT_FROM_DWH 中测试选择
从“YOUR_PROJECT_ID.KLAVIYO_IMPORT_FROM_DWH.some_existing_table”中选择* LIMIT 1；
````

****提示：**** 使用您将提供给 Klaviyo 的相同服务帐户和密钥运行这些检查。保留结果副本以供审核。 ---

## 5) 将 Klaviyo 连接到 BigQuery

配置 BigQuery 环境后，在 Klaviyo 中完成连接。 1. 在 Klaviyo 中，导航至左侧边栏中的****高级 → 同步****。 2. 单击****创建同步****。 3. 选择****将数据导入或导出到您的数据仓库****。 4. 选择****BigQuery**** 作为您的数据仓库。 5. 单击****连接到 BigQuery****。 出现提示时，提供以下连接配置详细信息：

|领域 |描述 |哪里可以找到它 |
| --- | --- | --- |
| ****项目ID**** |您的 Google Cloud 项目 ID。 |可在项目页面顶部的 GCP 控制台中找到。 |
| ****数据集**** |包含 Klaviyo 表的数据集（架构）（例如“KLAVIYO_IMPORT_FROM_DWH”）。 |使用您在步骤 1 中创建的数据集。配置连接时选择该数据集。 |
| ****服务帐户密钥 (JSON)**** |您为服务帐户下载的 JSON 密钥文件。 |上传或粘贴您在步骤 2 中创建的 JSON 密钥文件的内容。

****连接后：**** Klaviyo 将验证连接、测试对数据集的访问，然后允许您配置同步 — 用于将数据导入 Klaviyo 并将 Klaviyo 数据导出到 BigQuery。 ---

**下一步：** 连接成功后，在 Klaviyo 中创建第一个导入或导出同步，并开始将数据移入或移出 BigQuery。