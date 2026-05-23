<h1>连接 Klaviyo 和 Redshift</h1>

<p><a href="https://help.klaviyo.com/hc/en-us/articles/17655007276059">高级 KDP</a></p>
<h2>概述</h2>
<p>本指南引导 Redshift 管理员为 Klaviyo 准备 Amazon Redshift、授予所需的最低访问权限并完成连接，以便您可以按计划导入配置文件数据。您将学习如何：</p>
<p>1. 创建`KLAVIYO_TMP`和`KLAVIYO_IMPORT_FROM_DWH`模式</p>
<p>2.为Klaviyo创建专门的服务用户</p>
<p>3.授予最低权限</p>
<p>4.（可选）验证权限和连接</p>
<p>5. 将 Redshift 连接到 Klaviyo 并开始创建同步</p>
<p>有关数据仓库导入工作原理的背景信息（包括支持的对象和表结构的最佳实践），请参阅[<strong>了解 Klaviyo 中的数据仓库导入</strong>](https://klaviyo.zendesk.com/hc/en-us/articles/40939206649627)。 ## 创建所需的模式</p>
<p>在 Redshift 将用于 Klaviyo 的数据库中创建两个架构：</p>
<p>````</p>
<p>-- 以 Redshift DB 管理员或具有 CREATE SCHEMA 的角色运行</p>
<p>如果不存在则创建架构 klaviyo_import_from_dwh;</p>
<p>如果不存在则创建架构 klaviyo_tmp；</p>
<p>````</p>
<ul>
<li>`KLAVIYO_IMPORT_FROM_DWH` – 将最终的、准备同步的表或视图放在这里。在设置过程中，Klaviyo 会列出此架构中的对象供您选择，因此仅包括您计划导入的表。 - `KLAVIYO_TMP` – Klaviyo 在同步作业期间专门用于临时/临时表。不要修改此处的数据 - Klaviyo 会自动管理和清理此架构。 ## 创建 Klaviyo 服务用户</li>
</ul>
<p>为 Klaviyo 创建一个专用的数据库用户，并设置一个可以独立轮换的强密码。 ````</p>
<p>-- 替换为您自己的名字和强密码</p>
<p>创建用户 klaviyo_data_transfer_user，密码为“REPLACE_WITH_STRONG_PASSWORD”；</p>
<p>````</p>
<p>创建一个角色来管理服务用户的授权：</p>
<p>````</p>
<p>创建角色 klaviyo_data_transfer_role；</p>
<p>将角色 klaviyo_data_transfer_role 授予 klaviyo_data_transfer_user；</p>
<p>````</p>
<p>安全地存储用户名和密码 - 您将在将 Klaviyo 连接到 Redshift 时使用它们。 ## 授予所需权限（最小权限）</p>
<p>````</p>
<p>-- 1) 允许临时表</p>
<p>将数据库 your_database 上的临时权限授予角色 klaviyo_data_transfer_role；</p>
<p>-- 2) Klaviyo 管理的暂存模式的权限</p>
<p>将架构 klaviyo_tmp 的使用权限授予角色 klaviyo_data_transfer_role；</p>
<p>将架构 klaviyo_tmp 上的创建授予角色 klaviyo_data_transfer_role；</p>
<p>-- 3) 对导入模式的只读访问</p>
<p>将架构 klaviyo_import_from_dwh 的使用权限授予角色 klaviyo_data_transfer_role；</p>
<p>将 SCHEMA klaviyo_import_from_dwh 中所有表的选择权限授予 ROLE klaviyo_data_transfer_role；</p>
<p>-- 记住授予将来对新表的访问权限</p>
<p>-- 3a) 对特定视图授予 SELECT（根据需要重复）</p>
<p>将视图中的选择 klaviyo_import_from_dwh.example_view_name 授予角色 klaviyo_data_transfer_role；</p>
<p>````</p>
<p>##（可选）验证您的设置</p>
<p>以 Klaviyo 用户身份运行一些快速检查，以确认授权是否正确。 ````</p>
<p>-- 切换到目标数据库</p>
<p>将 search_path 设置为 klaviyo_tmp；</p>
<p>-- 4.1 验证 KLAVIYO_TMP 中的创建/读取</p>
<p>如果不存在则创建表permission_check (id INT);</p>
<p>插入权限检查值（1）；</p>
<p>从权限检查中选择 COUNT(*)；  -- 预计 1</p>
<p>删除表permission_check；</p>
<p>-- 4.2 确认导入表的可见性</p>
<p>将 search_path 设置为 klaviyo_import_from_dwh；</p>
<p>从 pg_table_def 中选择表名</p>
<p>WHERE schemaname = 'klaviyo_import_from_dwh'</p>
<p>限制 25；</p>
<p>-- 4.3 在源表或视图上确认 SELECT</p>
<p>SELECT * FROM klaviyo_import_from_dwh.EXAMPLE_TABLE;</p>
<p>````</p>
<h2>网络访问</h2>
<p>Klaviyo 必须能够到达您的 Redshift 端点。 - <strong><em>*公共 Redshift 端点：</strong><strong> 将 Klaviyo 的静态 IP 添加到您的防火墙或安全组中。 - </strong><strong>专用端点（例如 PrivateLink）：</strong><strong> 通过内部网络路径和安全策略确保连接。 如果使用安全组，请允许在 Redshift 端口（默认 </strong><strong>5439</strong></em>*）上对 Klaviyo 的 IP 范围进行入站访问：</p>
<p>````</p>
<p>184.72.183.187/32</p>
<p>52.206.71.52/32</p>
<p>3.227.146.32/32</p>
<p>44.198.39.11/32</p>
<p>35.172.58.121/32</p>
<p>3.228.37.244/32</p>
<p>54.88.219.8/32</p>
<p>3.214.211.176/32</p>
<p>````</p>
<h2>准备导入表（结构和性能）</h2>
<p>确保您计划导入的所有表都遵循以下约定，以实现准确、高效的增量同步：</p>
<ul>
<li>****时间戳列：**** 包括每行创建或上次更新时间戳（例如，“inserted_at”、“updated_at”、“modified_at”）。 - ****单调更新：**** 每当行发生更改时，时间戳就应该增加。 - ****时区：**** 使用 UTC 或包含时区信息。如果缺失，Klaviyo 将采用 UTC。 - ****一致的标识符：**** 在导入表中使用相同的配置文件标识符（“电子邮件”、“电话”、“external_id”等）以避免重复。 - ****同意格式：**** 同步同意数据时，请遵循文件或 SFTP 上传中使用的相同有效值/格式。 - ****性能：**** 考虑在时间戳列上排序或分布键以实现高效的增量读取。 - ****视图：**** 您可以从表或视图导入，只要简单的“SELECT”适用于 Klaviyo 用户即可。 ## 将 Redshift 连接到 Klaviyo</li>
</ul>
<p>1. 在 Klaviyo 中，打开左侧边栏并转到<strong><em>*高级 → 同步</strong><strong>。 2. 单击</strong><strong>创建同步</strong><strong>。 3. 选择</strong><strong>从数据仓库导入数据</strong><strong>。 4. 选择</strong><strong>红移</strong><strong>。 5. 单击</strong><strong>连接到 Redshift</strong></em>* 并输入以下连接详细信息：</p>
<p>|领域 |描述 |</p>
<p>| --- | --- |</p>
<p>| <strong><em>*主持人</strong></em>* |您的 Redshift 端点（例如“example-cluster.abc123.us-east-1.redshift.amazonaws.com”）|</p>
<p>| <strong><em>*港口</strong></em>* | 5439（或您的自定义端口）|</p>
<p>| <strong><em>*数据库</strong></em>* |包含`klaviyo_tmp`和`klaviyo_import_from_dwh`的数据库 |</p>
<p>| <strong><em>*用户名/密码</strong></em>* | Klaviyo 服务用户凭据 |</p>
<p>连接后，Klaviyo 将测试您的凭据和网络连接。验证后，您可以创建同步并从“klaviyo_import_from_dwh”中选择表或视图。 ## 故障排除技巧</p>
<p><strong><em>*连接测试失败</strong></em>*</p>
<ul>
<li>验证防火墙或安全组规则是否允许 Klaviyo 的 IP 到达正确端口上的 Redshift 端点。 - 确认 SSL 设置以及您使用的是正确的端点（集群与工作组）、区域和端口。 ****表格不出现****</li>
<li>确保表位于“klaviyo_import_from_dwh”中。 - 确认 Klaviyo 用户在架构上具有“USAGE”，在表或视图上具有“SELECT”。 ****没有新行同步****</li>
<li>验证您的时间戳列在行更改时更新并使用 UTC 或包含时区信息。 ****运行时权限错误****</li>
<li>以 Klaviyo 用户身份重新运行验证 SQL。 - 如有必要，重新申请授予或默认权限。 ## 安全与维护</li>
</ul>
<ul>
<li>定期以及在员工变动后轮换服务用户密码。 - 将 Klaviyo 用户限制为上述两种模式，并仅在需要时授予“USAGE”。 - 保留一个简单的操作手册，记录您确切的“GRANT”语句以及您列入白名单的 IP 范围。 ## 常见问题解答</li>
</ul>
<p><strong><em>*我可以从多个 Redshift 数据库导入吗？</strong></em>*</p>
<p>是的。在每个数据库中创建两个架构，并将每个数据库中的对象连接为单独的同步。 <strong><em>*我可以使用物化视图吗？</strong></em>*</p>
<p>是的。将物化视图上的“SELECT”授予 Klaviyo 用户。 ## 附录：简单导入表的 DDL 示例</p>
<p>````</p>
<p>创建表 klaviyo_import_from_dwh.profile_base (</p>
<p>外部_id VARCHAR(128),</p>
<p>电子邮件 VARCHAR(320),</p>
<p>电话 VARCHAR(32),</p>
<p>名字 VARCHAR(128),</p>
<p>姓氏 VARCHAR(128),</p>
<p>国家 VARCHAR(64),</p>
<p>插入时间为时间戳</p>
<p>）；</p>
<p>-- 确保插入/更新时单调递增的时间戳</p>
<p>--（在加载时使用 ETL/ELT 设置 insert_at = GETDATE()）</p>
<p>````</p>
