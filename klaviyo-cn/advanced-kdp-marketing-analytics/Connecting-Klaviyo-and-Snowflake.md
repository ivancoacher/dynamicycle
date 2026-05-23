---
id: "41373252392731"
title: "连接 Klaviyo 和 Snowflake"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41373252392731-Connecting-Klaviyo-and-Snowflake"
section: "Syncing"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: "zh"
---
[高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672)，了解如何购买此计划。在本文中，我们使用术语“表”，但视图、物化视图和表都是可以导入的有效 Snowflake 对象。只要 Klaviyo 可以在对象上运行 SELECT col1 FROM table\_name，您就可以自由使用您喜欢的任何内容。本文档中的关键字“必须”、“不得”、“必需”、“应”、“不应”、“应该”、“不应该”、“推荐”、“可以”和“可选”应按照 [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119) 中的描述进行解释。 ## Snowflake 管理设置

本部分概述了在 Snowflake 环境中必须遵循的步骤，以允许 Klaviyo 导入数据。 1. 在本地终端中运行以下命令生成私钥：

   ````
   openssl genrsa 2048 | OpenSSL genrsa 2048 | openssl pkcs8 -topk8 -通知 PEM -out rsa_key.p8 -nocrypt
   ````
2. 通过在终端中运行以下命令来生成引用私钥的公钥：

   ````
   openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
   ````
3. 复制 rsa\_key.pub 并将其粘贴到下面的脚本中，以替换 user\_rsa\_public\_key 的占位符“GENERATE\_PUBLIC\_KEY”值。下面的脚本适用于 Mac 用户，或者您也可以在 IDE 中打开 rsa\_key.pub 并复制该文件的完整内容（如果您愿意）。 ````
   # Mac 终端命令将密钥写入终端并将其复制到剪贴板
   猫 rsa_key.pub |三通 /dev/tty | PB复制
   ````
4. 在 Snowflake 环境中运行以下脚本来创建供 Klaviyo 使用的服务用户。您必须具有 securityadmin 和 sysadmin 权限才能完成以下设置。要查看您拥有的角色，请运行 SHOW GRANTS TO USER <your\_username> 并确保您已列出这两个角色。如果您需要调整角色，请联系系统管理员。 1. 您应该随意更新脚本开头设置的任何变量。 2. 总之，您将：
      1. 选择现有仓库或创建新仓库
      2. 选择一个现有数据库或创建一个新数据库来保存新模式
      3. 创建两个新模式`KLAVIYO_TMP`和`KLAVIYO_IMPORT_FROM_DWH`
      4. 创建新的网络策略并将 Klaviyo IP 列入允许列表
      5.为Klaviyo创建用户和角色
   3. 该脚本是幂等的（可以安全地运行多次），但不会覆盖名称冲突的现有对象。 ````
开始；

-- 为用户/密码/角色/仓库/数据库创建变量。 -- 将它们更改为您喜欢的任何内容。设置角色名称 = 'KLAVIYO_DATA_TRANSFER_ROLE'; -- 所有字母必须为大写，例如。 'KLAVIYO_DATA_TRANSFER_ROLE'
设置用户名 = 'KLAVIYO_DATA_TRANSFER_USER'; -- 所有字母必须为大写，例如。 'KLAVIYO_DATA_TRANSFER_USER'
SET 仓库名称 = 'KLAVIYO_DATA_TRANSFER_WAREHOUSE'; -- 所有字母必须为大写，例如。 'KLAVIYO_DATA_TRANSFER_WAREHOUSE'
SET 数据库名称 = 'KLAVIYO_DATABASE'; -- 所有字母必须为大写，例如。 'KLAVIYO_DATABASE'。如果该数据库不存在，则会创建一个新数据库。设置网络策略 = 'KLAVIYO_DATA_TRANSFER_NETWORK_POLICY'; -- 所有字母必须为大写，例如。 'KLAVIYO_NETWORK_POLICY'
设置网络规则 = 'KLAVIYO_DATA_TRANSFER_NETWORK_RULE'; -- 所有字母必须为大写，例如。 'KLAVIYO_NETWORK_RULE'
/* 将下面的 GENERATE_PUBLIC_KEY 替换为生成的公钥 */

-- 不要改变
SET schema_name_tmp = $database_name || '.KLAVIYO_TMP';  -- 不要改变
SET schema_name_import = $database_name || '.KLAVIYO_IMPORT_FROM_DWH';  -- 不要改变
SET full_network_rule_tmp = $schema_name_tmp || '.' || $网络规则； -- 不要改变
SET full_network_rule_import = $schema_name_import || '.' || $网络规则； -- 不要改变


-- 将仓库/数据库步骤的角色更改为 sysadmin
使用角色系统管理员；

-- 创建数据传输服务的仓库
如果标识符不存在，则创建仓库（$warehouse_name）
    仓库大小 = xsmall
    仓库类型 = 标准
    自动挂起= 60
    自动恢复=真
    最初_暂停=真；

-- 创建数据传输服务的数据库
如果标识符不存在，则创建数据库（$database_name）；

-- 创建数据传输服务模式
如果标识符不存在，则创建架构（$schema_name_tmp）；
如果标识符不存在，则创建架构（$schema_name_import）；

-- 将用户/角色步骤的角色更改为 securityadmin
使用角色 securityadmin；

-- 为数据库创建网络规则和策略
将数据库标识符（$database_name）的使用权限授予角色 securityadmin；
向角色 securityadmin 授予使用权，并在架构标识符 ($schema_name_tmp) 上创建网络规则；
授予使用权限，在模式标识符（$schema_name_import）上创建网络规则给角色 securityadmin；

-- 白名单 klaviyo IP 范围，用于 KLAVIYO_TMP 模式
如果标识符不存在，则创建网络规则($full_network_rule_tmp)
    类型 = IPV4
    值列表 = (
        '184.72.183.187/32'，'52.206.71.52/32'，'3.227.146.32/32'，'44.198.39.11/32'，'35.172.58.121/32'，'3.228.37.244/32'， '54.88.219.8/32', '3.214.211.176/32'
        ）
    comment = '截至 2025 年 4 月的 Klaviyo IP 范围';
如果标识符不存在，则创建网络策略($network_policy)
    allowed_network_rule_list = ($full_network_rule_tmp);

-- 白名单 klaviyo IP 范围，用于 KLAVIYO_IMPORT_FROM_DWH 模式
如果标识符不存在，则创建网络规则($full_network_rule_import)
    类型 = IPV4
    值列表 = (
        '184.72.183.187/32'，'52.206.71.52/32'，'3.227.146.32/32'，'44.198.39.11/32'，'35.172.58.121/32'，'3.228.37.244/32'， '54.88.219.8/32', '3.214.211.176/32'
        ）
    comment = '截至 2025 年 4 月的 Klaviyo IP 范围';
如果标识符不存在，则创建网络策略($network_policy)
allowed_network_rule_list = ($full_network_rule_import);


-- 创建数据传输服务角色
如果标识符不存在则创建角色($role_name);
将角色标识符（$role_name）授予角色系统管理员；

-- 创建数据传输服务的用户
如果标识符不存在则创建用户($user_name)
    类型 = 服务
    网络策略 = $网络策略
    默认角色 = $角色名称
    默认仓库 = $仓库名称
    rsa_public_key = 'GENERATE_PUBLIC_KEY';
将角色标识符（$role_name）授予用户标识符（$user_name）；
更改用户标识符($user_name) SET NETWORK_POLICY = $network_policy;

-- 授予服务角色访问仓库的权限
拨款用途
    ON 仓库标识符($warehouse_name)
    至角色标识符($role_name);

-- 授予服务访问数据库的权限
授予监控、使用情况
    ON 数据库标识符($database_name)
    至角色标识符($role_name);

-- 授予KLAVIYO_TMP权限
将架构标识符（$schema_name_tmp）的使用权限授予角色标识符（$role_name）；
授予监控、使用、创建表、创建视图、创建序列、创建函数、创建过程
    ON 模式标识符（$schema_name_tmp）
    至角色标识符($role_name);
将 SCHEMA IDENTIFIER($schema_name_tmp) 中未来表中的所有内容授予 ROLE IDENTIFIER($role_name);

-- 授予 KLAVIYO_IMPORT_FROM_DWH 权限
将架构标识符（$schema_name_import）的使用权限授予角色标识符（$role_name）；
授予选择
    未来的餐桌
    在模式标识符中（$schema_name_import）
    至角色标识符($role_name);

犯罪;
````

## 雪花数据设置

在上面，您创建了两个新模式。 - KLAVIYO\_TMP 将由 Klaviyo 独家使用。您不得修改在此模式中创建的任何表。当不再需要这些表时，Klaviyo 将删除它们。 - KLAVIYO\_IMPORT\_FROM\_DWH 是您应该存储最终表以供 Klaviyo 导入的位置。当您完成同步创建过程时，将列出该架构中的所有表供您选择。因此，您应该只存储要导入的最终表，以避免在设置过程中出现混乱。 您计划导入到 Klaviyo 的所有表必须满足以下条件。 ### 时间戳要求

1. 表必须包含一个时间戳字段，指示行的创建或更新时间。通常这会被插入\_at 或更新\_at。您将在同步创建过程中为每个表设置此项。 1. 时间戳字段必须单调递增（即它必须始终变大或保持不变，永远不会变小）。 2. 创建同步后，您不得将行的时间戳值设置为过去的时间，否则 Klaviyo 可能无法获取该行。 3.该字段的时区对Klaviyo来说并不重要，只要遵循上述要求即可
   4. Klaviyo 建议您使用 CURRENT\_TIMESTAMP() 或等效函数设置时间戳字段。多行可以具有相同的时间戳。请参阅下面的示例。 ````
      INSERT INTO 表名 AS

      SELECT ... , CURRENT_TIMESTAMP() AS insert_at

      ...````
2. 您的时间戳必须采用 UTC 格式，或包含时区信息。如果时区信息丢失，Klaviyo 将采用 UTC。对于自定义属性，这些时间戳保留为字符串格式，允许您在您的首选时区中解释它们。 ### 表结构

1.表应该被视为仅附加（又名仅插入）
   1. 如果您希望就地更新行，则必须更新时间戳字段，以便 Klaviyo 可以识别更改。 2. 表应该在时间戳列上排序。 Snowflake 将根据您的插入顺序处理集群和分区。这将有助于优化 Klaviyo 的导入查询，从而降低 Snowflake 中的计算成本

### 个人资料的独特性和一致性

1. 您必须确保每个配置文件属性仅从一个数据源（表）导入。 Klaviyo 防止在同步创建期间从不同的表中选择相同的属性，从而简化了这一要求。 2. 您应该在所有导入表中使用相同的配置文件标识符（电子邮件、电话号码、外部 ID 等），以尽量减少创建重复配置文件的风险。 1. 如果您提供的个人资料标识符与 Klaviyo 中的现有个人资料不匹配，Klaviyo 将创建新的个人资料。 2. 示例：Table1（电子邮件、fav\_color）+ Table2（电话、生日）
      1. 如果个人资料当前不存在，这可能会为同一个人创建 2 个个人资料。如果配置文件确实存在，Klaviyo 将在内部处理配置文件解析和更新。 3. 避免此问题的一种方法是对所有配置文件仅使用一个导入表。 ### 循环导入-导出循环预防

1. 您应该仔细管理同时使用导入和导出功能的场景，以防止循环导入-导出循环。确保导出过程不会将数据反馈到导入表上游的表中，因为 Klaviyo 当前未检测到这种情况。 1. Klaviyo 还没有逻辑来检测这种情况。 2. 这看起来像：
      1. 在每个导出同步周期，Klaviyo 都会导出您的所有配置文件
      2. 然后，通过一系列转换将所有导出的配置文件添加到导入表中。 3. 在每个导入同步周期，Klaviyo 将读取导入表中的所有配置文件，这些配置文件最终将被重新导出
   3. 可能安全的场景
      1. 如果您仅使用导出表来限制添加到导入表的行
      2. 如果您验证导出表未将行添加到导入表中。 4. 进出口循环会产生什么后果？ 1. 这将为您和 Klaviyo 带来不必要的计算成本。