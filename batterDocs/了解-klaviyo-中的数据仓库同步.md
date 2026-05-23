<h1>了解 Klaviyo 中的数据仓库同步</h1>

<h2>你将会学到</h2>
<p>了解如何将数据从 Klaviyo 同步到数据仓库，以及如何通过 SFTP 将仓库数据导入到 Klaviyo。您可以同步您的客户资料和事件数据，从而允许您在 Klaviyo 之外存储和分析有关客户的关键信息。 [高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672)，了解如何购买此计划。 ![](https://fast.wistia.com/embed/medias/1luu8fozn2/swatch)</p>
<h2>开始之前</h2>
<p>您需要确保将要连接的数据仓库配置为目标。为确保您已正确设置：</p>
<ul>
<li>确保提供给 Klaviyo 的用户具有正确的权限。 - 确保根据您的仓库设置具有适当名称的表，如下所示。此外，请确保将 Klaviyo 的出站数据仓库流量 IP 地址列入白名单。这将确保 Klaviyo 的请求不会被您的安全层阻止。这些地址由以下 CIDR 范围表示：</li>
<li>`184.72.183.187/32`</li>
<li>`52.206.71.52/32`</li>
<li>`3.227.146.32/32`</li>
<li>`44.198.39.11/32`</li>
<li>`35.172.58.121/32`</li>
<li>`3.228.37.244/32`</li>
<li>`54.88.219.8/32`</li>
<li>`3.214.211.176/32`</li>
</ul>
<h2>连接到数据仓库</h2>
<p>要将数据仓库连接添加到 Klaviyo，请导航至<strong><em>*高级 KDP ></strong><strong></em></strong><em>数据管理 > 同步<strong></em><em>。要添加数据仓库，请在 </strong>选择连接器模式<strong> 上选择支持的数据仓库。每个账户只能有 1 个数据仓库目标。或者，您可以通过转至</strong><strong>集成>探索应用程序</strong></em>*并搜索您的平台，从 Klaviyo 的应用程序市场选择您的数据仓库。连接仓库时，您可以将数据从数据仓库导入到 Klaviyo，或将仓库设置为出站同步目标。 ![import_export.jpg](https://klaviyo.zendesk.com/hc/article_attachments/29207563157019)</p>
<h2>通过SFTP导入数据</h2>
<p>如果您想将数据从数据仓库导入到 Klaviyo，可以通过 [SFTP](https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool) 执行此操作。要将数据导入 Klaviyo，请在首次连接仓库目标时选择<strong><em>*导入数据</strong><strong>，或者如果您已建立连接，则单击 </strong>数据同步<strong> 页面上的</strong><strong>导入</strong></em>* 按钮。将仓库数据导入Klaviyo的流程如下：</p>
<p>1. 从数据仓库中导出所需的数据。 2. 在本地计算机上生成 SSH 密钥。 3. 配置SFTP客户端并导入。这是通过 Snowflake 进行演示的，但无论您的仓库集成如何，导入过程都是相似的。 ### 导出您的数据库</p>
<p>首先，您需要从仓库导出数据。登录您的仓库并将您想要导入 Klaviyo 的数据导出到 CSV 文件中。根据 [CSV 格式和大小限制](https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool#general-csv-formatting-and-size-limitations) 设置导出数据的格式。 ### 在本地计算机上生成 SSH 密钥</p>
<p>从仓库导出所需数据后，在本地计算机上生成新的 SSH 密钥，并通过选择<strong><em>*添加 SSH 密钥</strong></em>* 按钮将其添加到 Klaviyo。添加密钥时，请确保它以下列之一开头：</p>
<ul>
<li>SSH-ras</li>
<li>Ecdsa-sha2</li>
<li>SSH-ed</li>
<li>SK-ecdsa</li>
</ul>
<p>-sk-ssh</p>
<h3>配置SFTP客户端并导入</h3>
<p>将 SSH 密钥成功添加到 Klaviyo 后，您需要配置 SFTP 客户端并导入数据。 1. 打开 SFTP 客户端并使用 Klaviyo 中提供的凭据配置新连接。成功添加 SSH 密钥后，您将看到显示的凭据</p>
<p>2. 经过身份验证后，请确保您的数据库在导入之前遵循建议的准则</p>
<p>3. 通过 SFTP 客户端上传数据库文件并查看</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/29207563159451" alt="configure.jpg" />
<p>您还将看到最近导入的列表视图，其中包含以下信息：</p>
<ul>
<li>****状态****</li>
</ul>
<p>已完成或未完成。 - <strong><em>*已处理的行</strong></em>*</p>
<p>到目前为止已处理的总行数的百分比。 - <strong><em>*导入日期</strong></em>*</p>
<p>进口日期。 - <strong><em>*进口者</strong></em>*</p>
<p>导入数据的用户。 ![面板.jpg](https://klaviyo.zendesk.com/hc/article_attachments/29207608998811)</p>
<h2>将数据导出到您的仓库</h2>
<p>要将数据仓库配置为目标，您需要为每个数据仓库提供以下信息和凭据集。 <strong><em>*亚马逊红移</strong></em>*</p>
<p>要将 Amazon Redshift 配置为目标，请运行以下脚本来创建 <strong>klaviyo\_event</strong> 和 <strong>klaviyo\_profile</strong> 表。 [“示例](https://www.napkin.io/api/embed/2907a5ae195545d4)</p>
<p>配置为目标后，使用以下一组凭据将您的仓库与 Klaviyo 连接：</p>
<ul>
<li>****名称：**** 您在 Redshift 中的数据库名称（建议使用与您在 Redshift 中的数据库相同的名称）</li>
<li>****主机 URL：**** Amazon Redshift 服务器的终端节点（在 Redshift 中称为连接 URL）</li>
<li>****数据库：**** 标识您的数据源的名称</li>
<li>****端口：**** Redshift 使用的端口号</li>
<li>****架构：**** 您的数据库架构</li>
<li>****用户名：**** 用于登录 Redshift 的用户名</li>
<li>****数据库密码：**** 用于登录 Redshift 的密码</li>
</ul>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28705665436571" alt="用于连接的 Redshift 凭据" />
<p><strong><em>*亚马逊S3</strong></em>*</p>
<p>要将 Amazon S3 配置为目标，请将表名称设置为 <strong>klaviyo\_profile</strong> 和 <strong>klaviyo\_event</strong>。配置为目标后，使用以下一组凭据将您的仓库与 Klaviyo 连接：</p>
<ul>
<li>****名称****：Amazon S3 数据库的机器可读名称。 - ****Bucket****：您的存储桶名称。 - ****Bucket location****：创建存储桶时选择的区域名称。 - ****访问密钥 ID：**** 您的 AWS 访问密钥 ID。 - ****秘密访问密钥****：您的 AWS 秘密访问密钥。 ![用于连接的 Amazon S3 凭证](https://klaviyo.zendesk.com/hc/article_attachments/28705665430939)</li>
</ul>
<p><strong><em>*谷歌BigQuery</strong></em>*</p>
<p>要将 Google BigQuery 配置为目标，请运行以下脚本来设置 <strong>klaviyo\_profile</strong> 和 <strong>klaviyo\_event</strong> 表。您的 Google BigQuery 帐户必须具有付款资料，连接过程才能成功。请注意，在此脚本中，您必须将占位符“SERVICE ACCOUNT EMAIL”替换为您的 BigQuery 服务帐户电子邮件地址。 [“示例](https://www.napkin.io/api/embed/5a9fffbe699c45b6)</p>
<p>配置为目标后，使用以下一组凭据将您的仓库与 Klaviyo 连接：</p>
<ul>
<li>****名称：**** 帮助您识别此目的地的名称</li>
<li>****项目 ID：**** 这称为项目 ID，可以在您的 API 控制台中找到。 - ****数据集：**** 也称为模式。这与您在安装时应该运行的脚本中使用的名称相同。 - ****服务帐户密钥：**** 粘贴您在 BigQuery 中创建服务帐户时下载的 JSON 文件的全部内容。 ![用于连接的 BigQuery 凭据](https://klaviyo.zendesk.com/hc/article_attachments/28705638604827)</li>
</ul>
<p><strong><em>*微软 Azure Synapse 分析</strong></em>*</p>
<p>要将 Microsoft Azure 配置为目标，请运行以下脚本来创建 <strong>klaviyo\_profile</strong> 和 <strong>klaviyo\_event</strong> 表。 [“示例](https://www.napkin.io/api/embed/9814f97b94764202)</p>
<ul>
<li>****名称：**** 建议使用与 Azure 中的数据库相同的名称。 - ****工作区：**** Azure Synapse 工作区名称。 - ****数据库名称：**** 这标识您的专用 SQL 池数据库。 - ****用户名：**** 您的专用 SQL 池数据库的登录用户名。 - ****数据库密码：****您的专用 SQL 池数据库的登录密码。 - ****帐户名称：**** 您的 Windows Azure 存储帐户或您创建的 DNS 前缀。 - ****访问签名：**** 您的共享访问签名 (SAS) 字符串，用于证明对 Blob 存储容器的访问权限。 - ****容器名称：**** 用于数据传输的临时暂存区域的 Azure Blob 容器名称。 ![Azure 凭据](https://klaviyo.zendesk.com/hc/article_attachments/28705665467547)</li>
</ul>
<p><strong><em>*雪花</strong></em>*</p>
<p>要将 Snowflake 配置为目标，请执行以下步骤：</p>
<p>1. 通过在终端中运行以下命令来生成私钥：</p>
<p>````</p>
<p>openssl genrsa 2048 | OpenSSL genrsa 2048 | openssl pkcs8 -topk8 -通知 PEM -out rsa_key.p8 -nocrypt</p>
<p>````</p>
<p>2. 通过在终端中运行以下命令来生成引用私钥的公钥：</p>
<p>````</p>
<p>openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub</p>
<p>````</p>
<p>3. 运行以下脚本以设置 <strong>KLAVIYO\_PROFILE</strong>、<strong>KLAVIYO\_EVENT</strong> 和 <strong>KLAVIYO\_METRIC</strong> 表。 您必须拥有 securityadmin 和 sysadmin 权限才能完成以下设置。要查看您拥有的角色，请运行 SHOW GRANTS TO USER <your\_username> 并确保您已列出这两个角色。如果您需要调整角色，请联系系统管理员。 [“示例](https://www.napkin.io/api/embed/06339b3a07a5475f)</p>
<p>配置为目标后，使用以下一组凭据将您的仓库与 Klaviyo 连接：</p>
<ul>
<li>****名称：**** 建议使用与 Snowflake 中的数据库相同的名称。 - ****用户名：**** 连接到数据库的用户名。这应该与安装脚本中的 **user\_name** 相同。 - ****私钥：**** 生成的 Snowflake 私钥。 - ****仓库：**** 你在 Snowflake 的仓库。 - ****帐户：**** 您在 Snowflake 中的帐户。 - ****数据库：**** 您的数据库名称。这应该与安装脚本中的 **database\_name** 相同。 - ****架构：**** 您的数据库架构。这应该与安装脚本中的 **schema\_name** 相同。 ![](https://klaviyo.zendesk.com/hc/article_attachments/36251501527707)</li>
</ul>
<p>输入要同步的数据仓库的凭据后，选择要从 Klaviyo 同步的数据。 ### 数据对象</p>
<p>在 <strong>数据对象</strong> 部分中，您可以通过选中每个选项旁边的适用框来选择同步所有配置文件数据、仅同步特定事件数据或两种类型的数据。 Klaviyo 在将数据发送到数据仓库时使用嵌套的 JSON 结构。配置文件和事件均作为单个表发送，允许您查询 1 个表，而不是数据仓库中的大量潜在表名。 ![配置文件和事件数据对象](https://klaviyo.zendesk.com/hc/article_attachments/28705638636059)</p>
<p>同步 Klaviyo 中的所有数据可能会导致您的数据仓库产生额外费用。 ### 要排除的集成</p>
<p>在 <strong>要排除的集成</strong> 字段中，您可以选择要在数据仓库同步中排除的特定集成。如果您想从同步中删除可能已经连接到 Klaviyo 的特定集成数据，这会很有帮助。排除特定集成数据仅适用于事件数据，并不排除配置文件数据。 ![排除字段的集成](https://klaviyo.zendesk.com/hc/article_attachments/28705665480347)</p>
<h3>选择性同步</h3>
<p>在 <strong>选择性同步</strong> 字段中，您可以选择要从 Klaviyo 同步到数据仓库的特定事件。默认情况下，包括所有事件。当您将特定事件设置为与此字段同步时，只有选定的事件才会同步。仅当您选择 <strong>Events</strong> 数据对象时，才会显示此字段。 ![选择性同步字段](https://klaviyo.zendesk.com/hc/article_attachments/28705665484699)</p>
<h3>选择数据同步的频率</h3>
<p>在名为“选择数据同步的频率”部分中为“定期同步节奏”字段设置的值定义了从 Klaviyo 到数据仓库同步的频率。定期同步节奏默认设置为每小时一次且无法更改。 ![定期同步节奏字段](https://klaviyo.zendesk.com/hc/article_attachments/28705665488283)</p>
<h3>选择您要同步的历史数据量</h3>
<p>在 <strong>选择要同步的历史数据量</strong> 部分中，您可以定义在初始连接期间要从 Klaviyo 同步到数据仓库的历史数据量。您可以选择：</p>
<ul>
<li>30 天</li>
<li>90 天</li>
<li>1年</li>
<li>所有时间</li>
</ul>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28705665476763" alt="选择要同步到数据仓库的数据量" />
<p>如果一次同步大量数据，您的数据仓库可能会产生额外费用。 ### 同步评论</p>
<p>连接集成后，如果设置成功，您将看到一个最终屏幕，指出连接已<strong>已启用</strong>，以及：</p>
<ul>
<li>您设置的同步的详细信息</li>
<li>正在共享哪些数据（个人资料、事件或两者）</li>
<li>任何排除的集成</li>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28705665449115" alt="连接成功模式" />
</ul>
<p>如果您的同步未成功连接，您将看到 <strong>无法连接</strong> 状态，以及重试连接或编辑凭据中信息的选项。成功连接数据仓库后，您将返回主<strong>数据同步</strong>列表页面。 在这里您将看到您的：</p>
<ul>
<li>仓库**目的地**</li>
<li>**启用**状态</li>
<li>过去 24 小时内同步可能发生的任何潜在错误</li>
<li>上次发生的同步以及该事件的时间戳</li>
</ul>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/29207563162267" alt="卡片.jpg" />
<p>由于您只能连接 1 个目的地，因此您只能看到此列表视图中反映的 1 个目的地。 ## 数据同步仪表板</p>
<p>成功连接后，从 <strong>数据同步</strong> 列表页面单击您的集成。从这里您将进入数据同步仪表板，提供有关已运行的数据同步的历史和当前信息。 ![连接仓库后同步界面](https://klaviyo.zendesk.com/hc/article_attachments/28705638606491)</p>
<p>在这里您将看到同步信息分为 2 个选项卡：</p>
<ul>
<li>历史</li>
<li>定期</li>
</ul>
<h3>历史</h3>
<p><strong>历史</strong>选项卡包含显示历史数据同步状态的日志。历史同步是指在建立连接时将现有数据从 Klaviyo 同步到数据仓库。您将看到每次同步的以下信息：</p>
<ul>
<li>****姓名****</li>
</ul>
<p>数据正在包含在同步中。 - <strong><em>*状态</strong></em>*</p>
<p>同步的状态和潜在进度以及指出的估计百分比或潜在错误。这些状态可能包括：</p>
<ul>
<li>****已完成****</li>
</ul>
<p>您的数据已完成此一次性同步的同步。它不会再次自动重新同步。 - <strong><em>*预定</strong></em>*</p>
<p>计划下次同步自动运行的时间。 - <strong><em>*进行中</strong></em>*</p>
<p>数据正在主动同步到您的数据仓库，预计完成百分比。 - <strong><em>*错误</strong></em>*</p>
<p>发生错误，但 Klaviyo 将继续尝试重新建立连接。根据集成情况，此时间可能略有不同。 - <strong><em>*失败</strong></em>*</p>
<p>即使尝试重新建立连接后，同步也完全失败。这意味着您将需要检查您的配置设置甚至数据仓库设置。 - <strong><em>*暂停</strong></em>*</p>
<p>您已手动暂停同步。 - <strong><em>*禁用</strong></em>*</p>
<p>同步已被禁用，因为集成本身已被禁用或删除。 - <strong><em>*开始于</strong></em>*</p>
<p>同步的开始时间。 - <strong><em>*结束于</strong></em>*</p>
<p>同步的结束时间。 ### 定期</p>
<p><strong>定期</strong>选项卡包含显示定期同步状态的日志。随着客户继续与您的品牌互动并创建新数据，这些数据将定期发送到您的数据仓库。设置数据仓库连接时，每小时都会进行定期同步。您将看到每次同步的以下信息：</p>
<ul>
<li>****姓名****</li>
</ul>
<p>数据正在包含在同步中。 - <strong><em>*状态</strong></em>*</p>
<p>同步的状态和潜在进度以及指出的估计百分比或潜在错误。这些状态可能包括：</p>
<ul>
<li>****已完成****</li>
</ul>
<p>您的数据已完成此一次性同步的同步。它不会再次自动重新同步。 - <strong><em>*预定</strong></em>*</p>
<p>计划下次同步自动运行的时间。 - <strong><em>*进行中</strong></em>*</p>
<p>数据正在主动同步到您的数据仓库，预计完成百分比。 - <strong><em>*错误</strong></em>*</p>
<p>发生错误，但 Klaviyo 将继续尝试重新建立连接。根据集成情况，此时间可能略有不同。 - <strong><em>*失败</strong></em>*</p>
<p>即使尝试重新建立连接后，同步也完全失败。这意味着您将需要检查您的配置设置甚至数据仓库设置。 - <strong><em>*暂停</strong></em>*</p>
<p>您已手动暂停同步。 - <strong><em>*禁用</strong></em>*</p>
<p>同步已被禁用，因为集成本身已被禁用或删除。 - <strong><em>*数据新鲜度</strong></em>*</p>
<p>数据新鲜度是指数据的最新程度。例如，如果同步的新鲜度为 2 分钟，则意味着过去 2 分钟内在 Klaviyo 中创建的任何新数据尚未在您的数据仓库中。 - <strong>暂停</strong>、<strong>恢复</strong>和重新启用单独同步的按钮。 ## 删除数据仓库连接</p>
<p>要从您的 Klaviyo 帐户删除数据仓库连接，请选择<strong><em>*集成</strong><strong>选项卡。打开数据仓库集成旁边的菜单，然后选择</strong><strong>删除集成</strong></em>*以删除连接。 ![integrations_page.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705638617627)</p>
<h2>查看错误日志</h2>
<p>如果您遇到 Klaviyo 和数据仓库之间的数据同步问题，查看关联的错误日志可以提供有关问题原因的更多信息。要查看错误，请单击 <strong>同步</strong> 页面上的仓库目标。在 <strong>历史</strong> 和 <strong>定期</strong> 同步选项卡上，您将看到导出及其状态的列表，以及显示是否存在任何活动错误的指示器。 ![导出到仓库的列表，其中包含有关运行状况和错误计数的信息](https://klaviyo.zendesk.com/hc/article_attachments/28705638663707)</p>
<p>要查看有关特定错误的更多详细信息，请单击出现故障的导出。在这里，您将看到出站同步的时间线，以及基于同步状态的错误或成功消息。 ![与健康状态的出站同步时间线](https://klaviyo.zendesk.com/hc/article_attachments/28705638666395)</p>
<p>单击特定错误将打开一个包含以下信息的抽屉：</p>
<ul>
<li>****总结****</li>
</ul>
<p>数据仓库返回的错误的简要描述</p>
<ul>
<li>****代码****</li>
</ul>
<p>错误的错误代码</p>
<ul>
<li>****外部消息****</li>
</ul>
<p>数据仓库实际返回的错误信息</p>
<ul>
<li>****日期****</li>
</ul>
<p>错误发生的日期和时间</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28705638658459" alt="带有有关同步错误信息的抽屉" />
