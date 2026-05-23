<h1>连接 Klaviyo 和 Databricks</h1>

<p><a href="https://help.klaviyo.com/hc/en-us/articles/17655007276059">高级 KDP</a></p>
<p><strong><em>*概述：</strong><strong> 按照以下步骤为 Klaviyo 准备 Databricks。您将创建所需的</strong>架构<strong>（在目录中），为 Klaviyo 设置专用帐户和访问令牌，分配所需的最低权限，验证配置并将 Databricks 连接到 Klaviyo。 </strong><strong>重要提示：</strong><strong> Databricks 连接当前仅支持</strong><strong>将数据导入到 Klaviyo</strong><strong>。 - </strong><strong>配置文件</strong><strong>和</strong><strong>事件</strong><strong>现在可以导入。 - </strong><strong>导出到 Databricks</strong><strong> 尚不可用。在此之前，建议导出到 S3。 - </strong><strong>Unity 目录</strong></em>* 是必需的。要连接到使用 Hive 元存储 (HMS) 的 Databricks 实例，请考虑 [Hive 元存储联合](https://docs.databricks.com/aws/en/query-federation/hms-federation-concepts)。有关数据仓库导入如何在 Klaviyo 中工作的详细信息（包括架构结构、所需的表和字段映射），请参阅[数据仓库导入如何在 Klaviyo 中工作](https://klaviyo.zendesk.com/hc/en-us/articles/40939206649627) 和 [了解数据仓库事件导入。](https://klaviyo.zendesk.com/hc/en-us/articles/45442043369499)</p>
<p>---</p>
<h2>1) 创建所需的模式</h2>
<p>在 Databricks 中，<strong><em>*模式</strong><strong>（有时称为数据库）</strong><strong>位于目录</strong></em>*内。如果您的工作区使用 Unity Catalog，则可以使用默认的“main”目录或其他目录。 ````</p>
<p>使用目录主；  -- 或您组织的指定目录</p>
<p>如果不存在则创建架构 KLAVIYO_IMPORT_FROM_DWH；</p>
<p>如果不存在则创建架构 KLAVIYO_TMP；</p>
<p>````</p>
<ul>
<li>`KLAVIYO_IMPORT_FROM_DWH`：配置新同步时，在此架构中创建的表和视图将可供选择。 - `KLAVIYO_TMP`：同步期间使用的临时/暂存数据。 ****注意：**** 如果您的工作区不使用 Unity Catalog，Databricks 会将“架构”和“数据库”视为等效。您可以使用“CREATE DATABASE”而不是“CREATE SCHEMA”。 ---</li>
</ul>
<h2>2) 创建 Klaviyo 服务帐户和访问令牌</h2>
<p>Klaviyo 使用带有<strong><em>*个人访问令牌 (PAT)</strong></em>* 的专用帐户对 Databricks 进行身份验证。尽可能使用非人类（服务）帐户并安全地存储 PAT（例如密码管理器或秘密存储）。您将在初始设置期间向 Klaviyo 提供此令牌。 ### 2.1 创建账户</p>
<p>创建 Klaviyo 将专门用于此集成的 Databricks 工作区用户或服务主体。 ### 2.2 生成个人访问令牌</p>
<ul>
<li>****工作区用户帐户：**** 通过 Databricks Web UI 生成令牌（请参阅 Databricks 文档）：[为工作区用户创建个人访问令牌](https://docs.databricks.com/aws/en/dev-tools/auth/pat#create-personal-access-tokens-for-workspace-users)</li>
<li>****服务主体：**** 使用 Databricks CLI 生成令牌（请参阅 Databricks 文档）：[通过 Databricks CLI 创建个人访问令牌](https://docs.databricks.com/aws/en/dev-tools/auth/pat#create-personal-access-tokens-for-service-principals)</li>
</ul>
<p><strong><em>*重要：</strong></em>* 将 PAT 视为秘密。拥有令牌的任何人都可以使用关联帐户的权限访问 Databricks。 ---</p>
<h2>3) 分配所需的权限</h2>
<p>授予 Klaviyo 帐户对步骤 1 中创建的架构的以下权限。将 `klaviyo_service_user` 替换为您的实际用户名或服务主体名称，并使用正确的目录为架构添加前缀（例如，`main`）。 |架构|所需的最低权限 |目的|</p>
<p>| --- | --- | --- |</p>
<p>| `KLAVIYO_TMP` | `所有权限` <strong>或</strong> `USE SCHEMA`、`MODIFY`、`SELECT` 和 `CREATE TABLE` 的组合 |允许 Klaviyo 在同步期间创建和管理临时表。 |</p>
<p>| `KLAVIYO_IMPORT_FROM_DWH` | `使用模式`、`选择` |允许 Klaviyo 读取您的表和视图。 |</p>
<p>````</p>
<p>-- 授予临时模式的权限</p>
<p>将 SCHEMA main.KLAVIYO_TMP 上的所有权限授予 `klaviyo_service_user`；</p>
<p>-- 或者，授予细化权限：</p>
<p>将架构 main.KLAVIYO_TMP 上的使用架构、修改、选择、创建表授予 `klaviyo_service_user`；</p>
<p>-- 授予导入模式的只读访问权限</p>
<p>授予使用架构，选择架构 main.KLAVIYO_IMPORT_FROM_DWH 到 `klaviyo_service_user`；</p>
<p>````</p>
<p><strong><em>*最佳实践：</strong></em>* 应用最小权限原则——仅授予所需的权限。 ---</p>
<h2>4) 验证您的设置（可选）</h2>
<h3>4.1 确认模式存在</h3>
<p>在 Databricks SQL 笔记本或编辑器中运行：</p>
<p>````</p>
<p>在主文件中显示架构；  -- 如果不同，请将“main”替换为您的目录</p>
<p>````</p>
<p>你应该看到：</p>
<p>````</p>
<p>klaviyo_import_from_dwh</p>
<p>克拉维约_tmp</p>
<p>````</p>
<h3>4.2 测试身份验证（使用您的 PAT）</h3>
<p>使用 Databricks CLI 和您计划提供给 Klaviyo 的相同令牌：</p>
<p>````</p>
<h1>设置您的令牌和主机（以 AWS 为例）</h1>
<p>导出 DATABRICKS_HOST="https://<your-workspace>.cloud.databricks.com"</p>
<p>导出 DATABRICKS_TOKEN="<您的 PAT>"</p>
<h1>运行一个简单的 API 调用</h1>
<p>databricks 当前用户我</p>
<p>````</p>
<p><strong>预期结果：</strong> JSON 输出显示用户或服务主体详细信息（例如，显示名称、用户 ID）。如果收到 HTTP 403 或身份验证错误，请验证令牌和主机 URL。 ### 4.3 检查每个模式的权限</p>
<p>````</p>
<p>在架构 main.klaviyo_tmp 上显示补助金；</p>
<p>在架构上显示补助金 main.klaviyo_import_from_dwh;</p>
<p>````</p>
<p>确认您的 Klaviyo 帐户显示具有预期的权限（例如“USE SCHEMA”、“SELECT”、“MODIFY”、“CREATE TABLE”）。 ### 4.4 验证创建/读取操作</p>
<p>````</p>
<p>-- 在 KLAVIYO_TMP 中测试创建/删除</p>
<p>使用架构 main.klaviyo_tmp；</p>
<p>如果不存在则创建表 test_permissions (id INT);</p>
<p>删除表 test_permissions；</p>
<p>-- 在 KLAVIYO_IMPORT_FROM_DWH 中测试选择</p>
<p>使用架构 main.klaviyo_import_from_dwh;</p>
<p>显示表格；</p>
<p>````</p>
<p><strong><em>*提示：</strong></em>*</p>
<ul>
<li>使用您将与 Klaviyo 共享的相同身份和 PAT 运行这些验证步骤。 - 保留 SQL 授予语句和验证输出以供审核/故障排除。 - 在人员变动后定期轮换 PAT。 ---</li>
</ul>
<h2>5) 将 Klaviyo 连接到 Databricks</h2>
<p>配置 Databricks 后，在 Klaviyo 中完成连接。 1. 在 Klaviyo 中，打开<strong><em>*左侧边栏</strong><strong>并导航至</strong><strong>高级 > 同步</strong><strong>。 2. 单击</strong><strong>创建同步</strong><strong>。 3. 选择</strong><strong>从数据仓库导入数据</strong><strong>。 4. 选择</strong><strong>Databricks</strong><strong> 作为您的数据仓库。 5. 单击</strong><strong>连接到Databricks</strong></em>*。出现提示时，请提供以下连接详细信息：</p>
<p>|领域 |描述 |哪里可以找到它 |</p>
<p>| --- | --- | --- |</p>
<p>| <strong><em>*主机名</strong></em>* | Databricks 工作区的 URL 中指示的主机。 |登录 Databricks 后可在浏览器地址栏中找到：`https://<your-workspace>.cloud.databricks.com` 示例：`abc-12345678.cloud.databricks.com` |</p>
<p>| <strong><em>*HTTP 路径</strong><strong> |用于查询的 SQL 仓库的 HTTP 路径。 |在 Databricks UI 中： 1. 转到</strong><strong>SQL 仓库</strong><strong>。 2. 选择您计划使用的仓库。 3. 复制</strong><strong>连接详细信息</strong><strong>下的</strong><strong>HTTP 路径</strong></em>*。示例：`/sql/1.0/warehouses/1234abcd5678efgh` |</p>
<p>| <strong><em>*目录</strong></em>* |包含您的 Klaviyo 模式的目录（例如“main”）。 |使用以下方法验证：显示目录； |</p>
<p>| <strong><em>*访问令牌</strong></em>* |您在步骤 2 中创建的个人访问令牌 (PAT)。在设置过程中安全地存储和粘贴令牌。 |</p>
<p><strong><em>*连接后：</strong></em>* Klaviyo 将测试连接并确认对 Databricks 环境的访问。验证后，您可以配置同步以从您之前准备的架构导入数据。 ---</p>
<p><strong>下一步：</strong> 连接成功后，继续在 Klaviyo 中创建您的第一个同步并开始从 Databricks 导入数据。</p>
