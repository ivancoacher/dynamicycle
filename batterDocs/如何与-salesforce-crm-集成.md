<h1>如何与 Salesforce CRM 集成</h1>

<h2>你将会学到</h2>
<p>了解如何将 Salesforce CRM 与 Klaviyo 集成。通过这种集成，您可以轻松连接 Salesforce 帐户、选择要同步的对象以及映射字段，所有这些都通过引导式应用内设置流程完成。通过这种集成，Klaviyo 可以自动将 Salesforce 数据（例如潜在客户或联系人）同步到 Klaviyo 配置文件中，从而允许您使用 CRM 数据个性化消息传递并细分客户。 ## 开始之前</p>
<p>在开始集成之前，请确保：</p>
<ul>
<li>您拥有 Salesforce 帐户的管理员访问权限</li>
<li>您的 Salesforce 版本 [支持 API 访问](https://help.salesforce.com/s/articleView?language=en_US&id=000326486&mode=1&type=1)</li>
<li>您有可用的 Salesforce 用户名、密码和安全令牌</li>
</ul>
<h2>获取 Salesforce 安全令牌</h2>
<p>要在 Klaviyo 中启用 Salesforce CRM 集成，您首先需要获取 Salesforce 安全令牌。您应该在初始设置 Salesforce 帐户时收到安全令牌。如果您属于使用 Salesforce 的大型组织，请联系您的 Salesforce 管理员以获取安全令牌。如果您没有安全令牌的记录，则需要重置您的安全令牌才能接收新的安全令牌。下面按 Salesforce 版本细分了重置安全令牌的步骤，具体取决于您使用的是 Lightning Experience 还是 Salesforce Classic。 ### 闪电体验令牌重置</p>
<p>1. 在 Salesforce 中，单击屏幕右上角的个人资料，然后选择<strong><em>*设置</strong></em>*。 ![Salesforce 中的弹出窗口以蓝色显示设置和注销](https://klaviyo.zendesk.com/hc/article_attachments/28723628867355)</p>
<p>2. 这将带您进入您的个人信息页面。从左侧菜单中，单击<strong><em>*重置我的安全令牌</strong></em>*。 ![菜单包括以灰色突出显示的个人信息和重置我的安全令牌项目](https://klaviyo.zendesk.com/hc/article_attachments/28723628870171)</p>
<p>3. 单击<strong><em>*重置安全令牌</strong></em>*。 4. 如果您的安全令牌用于连接到任何其他应用程序，请使用此新安全令牌更新这些集成。 ![重置安全令牌页面并显示黄色警告，重置安全令牌按钮显示灰色背景](https://klaviyo.zendesk.com/hc/article_attachments/28723623583899)</p>
<p>5. 然后，您将收到来自 Salesforce 的一封电子邮件，其中包含您的新安全令牌。记下安全令牌并确保该信息的安全。 ### Salesforce Classic 令牌重置</p>
<p>1. 在 Salesforce 中，单击屏幕右上角您的姓名，然后选择<strong><em>*我的设置</strong></em>*。 ![我的设置以蓝色突出显示的菜单](https://klaviyo.zendesk.com/hc/article_attachments/28723623587227)</p>
<p>2. 从<strong>我的设置</strong>菜单中，单击<strong><em>*个人</strong><strong>。然后，选择</strong><strong>重置我的安全令牌</strong></em>*。 ![我的设置下的个人下拉菜单，重置我的安全令牌以深灰色突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28723623591451)</p>
<p>3. 单击<strong><em>*重置安全令牌</strong></em>*。 4. 如果您的安全令牌用于连接到任何其他应用程序，请使用此新安全令牌更新这些集成。 ![重置安全令牌页面并带有黄色警告，重置安全令牌按钮带有蓝色背景](https://klaviyo.zendesk.com/hc/article_attachments/28723628879003)</p>
<p>5. 然后，您将收到来自 Salesforce 的一封电子邮件，其中包含您的新安全令牌。记下安全令牌并确保该信息的安全。 ## 将 Salesforce 连接到 Klaviyo</p>
<p>1. 在 Klaviyo 中，选择<strong><em>*集成</strong><strong>选项卡。 2. 单击</strong><strong>探索应用程序</strong><strong>，搜索 </strong>Salesforce<strong>，然后单击该卡。然后，单击</strong><strong>安装</strong><strong>。 3. 输入您的 Salesforce 用户名、密码和安全令牌。输入这些必需的详细信息后，单击</strong><strong>连接到 Salesforce</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/47042695892379)</p>
<p>4. 如果集成成功，您应该会收到成功消息。 ## 选择要同步的 Salesforce 对象</p>
<p>连接后，系统将提示您选择要同步到 Klaviyo 的 Salesforce 对象。单击<strong><em>*下一步</strong><strong>继续。您现在可以选择</strong><strong>最多 3 个对象</strong></em>* 同步到 Klaviyo。 可用选项包括：</p>
<ul>
<li>****潜在客户 -**** 对您的 Salesforce 产品或服务表现出兴趣的潜在客户</li>
<li>****联系人**** - 与您的 Salesforce 组织中的帐户关联的个人</li>
<li>****帐户**** - 与您的业务相关的组织或个人（例如客户、竞争对手和合作伙伴）</li>
<li>****机会**** - 潜在的销售或交易</li>
<li>****其他****（可用性取决于您的 Salesforce 设置）</li>
</ul>
<p>从 Salesforce 同步的对象将创建或更新为 Klaviyo 配置文件。同步多个对象时：</p>
<ul>
<li>所有选定对象的记录将同步到 Klaviyo。 - 如果记录的电子邮件地址与现有的 Klaviyo 个人资料匹配，则该个人资料将被更新。 - 如果 Klaviyo 中不存在记录的电子邮件地址，则会创建新的个人资料。 - 如果同一个人存在于具有相同电子邮件地址的多个同步对象中，Klaviyo 会根据电子邮件将它们合并为****单个配置文件****。 （在下一步中为每个对象配置字段映射。）</li>
</ul>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/47042705488411" alt="" />
<h3>将 Salesforce 字段映射到 Klaviyo 属性</h3>
<p>接下来，您将 Salesforce 字段映射到 Klaviyo 配置文件属性。请注意，一些核心映射，例如<strong><em>*电子邮件</strong><strong>、</strong><strong>电话号码</strong><strong>、</strong><strong>名字</strong><strong>和</strong><strong>姓氏</strong><strong>是预先映射的。 </strong>需要 Salesforce 电子邮件地址的映射。</em>*</p>
<p>当您选择要同步的多个 Salesforce 对象时，您将为每个对象<strong><em>*单独配置字段映射</strong></em>*。这允许您控制每个对象中的哪些字段成为 Klaviyo 配置文件属性。 ### 添加或编辑映射</p>
<ul>
<li>使用****添加映射****为**当前选定的对象**映射其他 Salesforce 字段。 - 在左侧选择 Salesforce 字段，在右侧选择相应的 Klaviyo 属性。 - 如果需要，使用****垃圾桶图标****删除映射。 - 对每个同步对象重复此过程。如果从多个 Salesforce 对象映射相同的 Klaviyo 配置文件属性（例如，**电话号码** 或 **城市**），Klaviyo 会将 Salesforce 中最近更新的值同步到配置文件中。 ![屏幕截图 2026-01-20 3.31.46 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/45678170090523)</li>
</ul>
<h3>通过 CSV 导入映射（可选）</h3>
<p>CSV 导入将替换所选对象的所有现有字段映射。如果文件中不包含某个字段，它将从您的配置中删除。为了避免同步中断，请确认您的 CSV 包含所有必填字段（例如<strong><em>*电子邮件</strong></em>*）以及您想要继续同步的任何其他字段。要通过 CSV 导入映射：</p>
<p>1. 单击<strong><em>*添加映射→导入映射</strong></em>*。 2. 下载 CSV 模板。 3. 将 Salesforce → Klaviyo 字段映射添加到 CSV 模板。 4. 上传完成的 CSV 以批量应用映射。 ![屏幕截图 2026-01-20 下午 3.32.11.png](https://klaviyo.zendesk.com/hc/article_attachments/45678170093979)</p>
<h3>取消订阅处理（可选）</h3>
<p>当 Salesforce 对象上的电子邮件选择退出设置为 true 时，您可以启用该选项以将 Salesforce 对象同步为取消订阅。这将在 Klaviyo 中将该个人资料标记为取消订阅电子邮件。 ## 完成设置</p>
<p>映射完成后，单击<strong><em>*完成设置</strong></em>*。 Klaviyo 将完成集成（这通常需要几秒钟）。您的 Salesforce 帐户成功连接并同步后，您将看到一条确认消息。 ## 监控 Salesforce 同步并验证数据</p>
<p>Salesforce 集成每小时同步到 Klaviyo。要检查您的集成：</p>
<p>1. 单击 Klaviyo 中的<strong><em>*分析</strong><strong>下拉列表，然后选择</strong><strong>指标</strong><strong>。按 Salesforce 筛选，然后找到指标 </strong>成为领先</em>​​ 并单击其 <strong><em>*活动源</strong><strong> 图标。 2. 如果您的集成已开始同步数据，您将看到添加到此活动源的 </strong>成为潜在客户</em>* 事件以及 Salesforce 图标。 3. Klaviyo 导入您的所有 Salesforce 潜在客户。要验证这一点，请将特定日期添加到 Klaviyo 的潜在客户数量与添加到 Salesforce 的潜在客户数量进行比较，并确认它们匹配。 4. 将鼠标悬停在昨天的数据点上（在“成为潜在客户”的活动源上，您可以通过单击指标找到该数据点）或查看图表下方的数据表，了解昨天发生的付款数量，并将其与 Salesforce 中存储的数据进行比较。 5. 如果数据不匹配，问题很可能是您的 Klaviyo 帐户中的时区与您的 Salesforce 帐户中的时区不匹配。要检查您在克拉维约的时区设置：</p>
<ul>
<li>单击左下角您的帐户名。 - 选择然后单击****设置 > 组织****。 - 向下滚动到**时区**。 ## Klaviyo 中的 Salesforce 指标</li>
</ul>
<p>目前，Klaviyo 与 Salesforce CRM 同步一项指标：<strong>成为潜在客户</strong>。 ![屏幕截图 2026-01-20 下午 3.25.16.png](https://klaviyo.zendesk.com/hc/article_attachments/45678170095131)</p>
<p>在 Salesforce 中创建新潜在客户时会跟踪此指标。事件本身不包含来自 Salesforce 的任何数据，但记录此事件时，Klaviyo 将为每个潜在客户同步以下自定义属性，并将它们附加到潜在客户的 Klaviyo 个人资料中：</p>
<ul>
<li>身份证号</li>
<li>名字</li>
<li>姓氏</li>
<li>标题</li>
<li>公司</li>
<li>街道</li>
<li>城市</li>
<li>状态</li>
<li>邮政编码</li>
<li>国家</li>
<li>纬度</li>
<li>经度</li>
<li>电话</li>
<li>电子邮件</li>
<li>网站</li>
<li>铅源</li>
<li>状态</li>
<li>工业</li>
<li>员工人数</li>
<li>已选择退出电子邮件</li>
<li>业主电子邮件</li>
</ul>
<p>然后，您可以在段、流中使用这些属性，并将客户属性动态填充到消息模板中。 ## 故障排除</p>
<h3>字段映射警告和错误</h3>
<p>Klaviyo 不断验证您的 Salesforce 字段映射，以确保数据能够可靠同步。如果映射的 Salesforce 字段变得不可用（例如，删除、重命名或权限更改），您可能会在集成设置中看到警告或错误。 #### 当非必填字段不可用时</p>
<p>如果映射的 Salesforce 字段不再可用并且不需要，Klaviyo 将：</p>
<ul>
<li>显示警告，指示缺少哪个字段。 - 继续同步所有其他可用字段。 - 从未来的同步中排除不可用的字段，直到它被更新或删除。为了解决这个问题，</li>
</ul>
<p>1. 导航到 Klaviyo 中的<strong><em>*Salesforce 集成</strong><strong>。 2. 打开受影响的对象。 3. 更新或删除无效的字段映射。 4.</strong><strong>保存</strong></em>*您的更改。更新后，同步将按预期继续。 ![图片 (10).png](https://klaviyo.zendesk.com/hc/article_attachments/45678170098075)</p>
<p>##</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/45678150584731" alt="" />
<h4>当必填字段（电子邮件）不可用时</h4>
<p>如果 Salesforce 电子邮件字段不再可用于某个对象（例如，由于架构更改或权限），Klaviyo 将：</p>
<ul>
<li>显示错误，指示电子邮件字段丢失。 - 停止同步受影响对象的数据。 - 提示您更新字段映射以恢复同步。 ![图片 (17).png](https://klaviyo.zendesk.com/hc/article_attachments/45678170102171)</li>
</ul>
<p>为了解决这个问题，</p>
<p>1. 导航到 Klaviyo 中的<strong><em>*Salesforce 集成</strong><strong>。 2. 打开受影响的对象。 3. 确保有效的 Salesforce 电子邮件字段映射到 Klaviyo 的电子邮件属性。 4.</strong><strong>保存</strong></em>*您的更改。一旦电子邮件字段再次成功映射，数据同步将自动恢复。 #### Klaviyo 中缺少个人资料</p>
<p>如果 Salesforce 记录未在 Klaviyo 中显示为配置文件，请首先验证您正在同步的每个对象是否映射了<strong><em>*有效的电子邮件字段</strong></em>*。 Klaviyo 使用电子邮件地址作为创建或更新个人资料所需的标识符；没有映射电子邮件字段或没有有效电子邮件值的记录将不会同步为配置文件。确保：</p>
<ul>
<li>Salesforce ****电子邮件**** 字段映射到每个选定对象的 Klaviyo 的电子邮件属性。 - 映射的电子邮件字段包含 Salesforce 中的实际电子邮件值 - 空白或无效电子邮件可能会阻止记录作为配置文件同步。一旦映射了有效的电子邮件字段并且记录包含电子邮件地址，Klaviyo 将在下次同步时创建或更新这些配置文件。 ## 结果</li>
</ul>
<p>您现在已将您的 Klaviyo 帐户与 Salesforce CRM 集成并查看了您的同步数据。</p>
